#!/usr/bin/env python3
"""SAPfans.io link and staleness check — report before repair.

Reads every link the public site hands a reader and reports three things, in this
order, every run:

  1. Broken  — external links that fail, and internal links to files that do not exist
  2. Stale   — catalog repositories archived or quiet for a year, and a catalog date
               older than 30 days
  3. Held    — how many links were checked and passed

It never edits a page, a catalog entry, or a reference. A human reads the report and
decides what to fix or rotate out (ARK). That split — the check reads, a person
writes — is EgD-BOOT-008 in the boot contract.

Standard library only. Usage:

    python3 scripts/check-links.py            # print report, write registry/LINK-CHECK.md
    python3 scripts/check-links.py --no-write # print only
    python3 scripts/check-links.py --offline  # skip network; internal links + dates only

Set GITHUB_TOKEN to lift the GitHub API rate limit for the staleness pass.
Exit code: 0 when nothing is broken, 1 when anything is.

Pattern credit: the "report before repairing" lint in undefined-ui/second-brain-os
(MIT). Idea only; no code copied.
"""
from __future__ import annotations

import concurrent.futures as cf
import datetime as dt
import html.parser
import json
import os
import pathlib
import re
import sys
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
CATALOG = DOCS / "repos.json"
REPORT = ROOT / "registry" / "LINK-CHECK.md"
UA = "SAPfans-link-check/1.0 (+https://sapfans.io)"
QUIET_DAYS = 365
CATALOG_STALE_DAYS = 30
TIMEOUT = 15
# Hosts that refuse automated requests; a 403/999 from them is not evidence of a dead link.
BOT_WALLED = ("linkedin.com", "www.linkedin.com", "x.com", "twitter.com")


class _Links(html.parser.HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.found: list[str] = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "link" and (a.get("rel") or "").lower() in ("preconnect", "dns-prefetch"):
            return  # connection hints, not reader-facing links
        for k, v in attrs:
            if k in ("href", "src") and v:
                self.found.append(v.strip())


def page_links(path: pathlib.Path) -> list[str]:
    p = _Links()
    p.feed(path.read_text(encoding="utf-8", errors="replace"))
    # skip template fragments built in JavaScript (e.g. "' + esc(r.url) + '")
    return [u for u in p.found if "'" not in u and "+" not in u and "${" not in u]


def check_url(url: str) -> tuple[str, str]:
    """Return (status, note). status is 'ok', 'broken' or 'walled'."""
    host = re.sub(r"^https?://", "", url).split("/")[0].lower()
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(url, method=method, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
                return "ok", str(r.status)
        except urllib.error.HTTPError as e:
            if method == "HEAD" and e.code in (403, 404, 405, 429, 501):
                continue  # many servers reject HEAD; retry once with GET
            if host in BOT_WALLED or host.endswith(BOT_WALLED) or e.code in (401, 403, 429, 999):
                return "walled", f"HTTP {e.code} (sign-in or bot wall — not proof the page is gone)"
            return "broken", f"HTTP {e.code}"
        except Exception as e:  # DNS, TLS, timeout
            if method == "HEAD":
                continue
            return "broken", type(e).__name__
    return "broken", "no response"


def gh_repo(full_name: str) -> dict | None:
    req = urllib.request.Request(
        f"https://api.github.com/repos/{full_name}",
        headers={"User-Agent": UA, "Accept": "application/vnd.github+json"},
    )
    tok = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if tok:
        req.add_header("Authorization", f"Bearer {tok}")
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        return {"_error": e.code}
    except Exception:
        return None


def main(argv: list[str]) -> int:
    offline = "--offline" in argv
    write = "--no-write" not in argv
    today = dt.date.today()

    broken: list[tuple[str, str, str]] = []  # (where, link, why)
    stale: list[tuple[str, str, str]] = []
    walled: list[tuple[str, str, str]] = []
    external: dict[str, set[str]] = {}
    internal_ok = 0

    # --- pages
    for page in sorted(DOCS.glob("*.html")):
        rel = page.relative_to(ROOT).as_posix()
        for link in page_links(page):
            if link.startswith(("mailto:", "tel:", "javascript:", "data:", "#")):
                continue
            if link.startswith("http://"):
                broken.append((rel, link, "plain http — serve over https"))
                continue
            if link.startswith("https://"):
                external.setdefault(link.split("#")[0], set()).add(rel)
                continue
            target = (page.parent / link.split("#")[0].split("?")[0]).resolve()
            if link.split("#")[0] and not target.exists():
                broken.append((rel, link, "internal file not found"))
            else:
                internal_ok += 1

    # --- catalog
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    updated = dt.date.fromisoformat(catalog["updated"])
    age = (today - updated).days
    if age > CATALOG_STALE_DAYS:
        stale.append(("docs/repos.json", f"updated {updated}", f"{age} days old — run an ARK sweep"))
    for repo in catalog["repos"]:
        external.setdefault(repo["url"], set()).add("docs/repos.json")

    # --- network passes
    ext_ok = 0
    if not offline:
        with cf.ThreadPoolExecutor(max_workers=8) as pool:
            results = dict(zip(external, pool.map(check_url, external)))
        for url, (status, note) in sorted(results.items()):
            where = ", ".join(sorted(external[url]))
            if status == "ok":
                ext_ok += 1
            elif status == "walled":
                walled.append((where, url, note))
            else:
                broken.append((where, url, note))

        for repo in catalog["repos"]:
            m = re.match(r"https://github\.com/([^/]+/[^/#?]+)", repo["url"])
            if not m:
                continue
            info = gh_repo(m.group(1))
            if not info or "_error" in info:
                continue  # a dead repo URL is already reported under Broken
            if info.get("archived"):
                stale.append(("docs/repos.json", repo["url"], "archived by its owner"))
                continue
            pushed = dt.date.fromisoformat(info["pushed_at"][:10])
            quiet = (today - pushed).days
            if quiet > QUIET_DAYS:
                stale.append(("docs/repos.json", repo["url"], f"no push for {quiet} days (last {pushed})"))

    # --- report: fixed shape, same three sections every run
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    total = len(external) + internal_ok + sum(1 for b in broken if "internal" in b[2])
    lines = [
        "# LINK-CHECK — SAPfans.io",
        "",
        f"**Run:** {stamp} · **Mode:** {'offline' if offline else 'online'} · "
        f"**Generator:** [`scripts/check-links.py`](../scripts/check-links.py)",
        "",
        "Report only. Nothing on the site was changed by this run. A person decides what to "
        "fix, replace or rotate out.",
        "",
        f"## 1. Broken — {len(broken)}",
        "",
    ]
    lines += (["| Where | Link | Why |", "|---|---|---|"]
              + [f"| `{w}` | {l} | {y} |" for w, l, y in broken]) if broken else ["None."]
    lines += ["", f"## 2. Stale — {len(stale)}", ""]
    lines += (["| Where | Item | Why |", "|---|---|---|"]
              + [f"| `{w}` | {l} | {y} |" for w, l, y in stale]) if stale else ["None."]
    lines += ["", "## 3. Held", ""]
    lines += [
        f"- Internal links resolved: {internal_ok}",
        f"- External links answered: {ext_ok if not offline else 'not checked (offline)'}",
        f"- Unverifiable (host blocks automated checks — open by hand): {len(walled)}",
    ]
    for w, l, y in walled:
        lines.append(f"  - {l} — {y}")
    lines += ["", "---", "", "© 2026 EVEglyphDesign. All rights reserved.", ""]
    text = "\n".join(lines)
    print(text)
    if write:
        REPORT.parent.mkdir(exist_ok=True)
        REPORT.write_text(text, encoding="utf-8")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
