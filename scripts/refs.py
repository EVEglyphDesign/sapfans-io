#!/usr/bin/env python3
"""SAPfans.io reference catalog — intake, review and upkeep. Standard library only.

  refs.py add URL [--title T] [--lane L] [--why W] [--credit C] [--by NAME]
                                                       paste a link -> review queue (state=open)
  refs.py issue                                        same, from a GitHub issue body in $ISSUE_BODY
  refs.py inbox                                        queue every link pasted in intake/INBOX.md, then clear it
  refs.py github [--days 7] [--cap 10]                 new SAP-org repos and active SAP x AI repos -> queue
  refs.py accept P-001 [--why "one line"]              queue -> docs/references.json (live page)
  refs.py reject P-001 --reason "..."                  closes the proposal, kept for the record
  refs.py check                                        link-check live rows; dead -> status=stale
  refs.py review                                       rewrite registry/PROPOSALS.md (the review list)

Nothing reaches the live page without `accept`. Nothing is deleted: rejected
proposals and stale rows stay in the files with their reason and date.
"""
import json, sys, datetime, urllib.request, pathlib, argparse
ROOT = pathlib.Path(__file__).resolve().parent.parent
CAT = ROOT / "docs" / "references.json"
Q = ROOT / "registry" / "proposals.json"
MD = ROOT / "registry" / "PROPOSALS.md"
TODAY = datetime.date.today().isoformat()

def load(p): return json.loads(p.read_text())
def save(p, d): d["updated"] = TODAY; p.write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n")

def known_urls():
    return {i["url"] for i in load(CAT)["items"]} | {p["url"] for p in load(Q)["proposals"] if p.get("url")}

def add(a):
    q = load(Q)
    if a.url in known_urls(): print("already held:", a.url); return
    n = max([int(p["id"][2:]) for p in q["proposals"]] + [0]) + 1
    q["proposals"].append(dict(id=f"P-{n:03d}", title=a.title or a.url, url=a.url, why=a.why, lane=a.lane,
        role=[], product=None, format=None, level=None, access=None, source=None, priority=None,
        credit=a.credit, found_by=a.by, proposed=TODAY, state="open", note=getattr(a, "note", None) or "Pasted; classification pending."))
    save(Q, q); review(None); print("queued", f"P-{n:03d}")

def issue(a):
    import os, re
    body = os.environ.get("ISSUE_BODY", "")
    def field(label):
        m = re.search(r"### " + re.escape(label) + r"[^\n]*\n+(.+?)(?:\n###|\Z)", body, re.S)
        v = m.group(1).strip() if m else None
        return None if v in (None, "_No response_", "Not sure") else v
    url = field("Link")
    if not url or not url.startswith("http"): sys.exit("no link in issue")
    a.url, a.why, a.lane, a.credit = url, field("Why it helps"), field("Lane"), field("Where you found it")
    a.title, a.by = None, "issue #" + os.environ.get("ISSUE_NUMBER", "?") + " by " + os.environ.get("ISSUE_USER", "?")
    add(a)

def inbox(a):
    """Queue every URL pasted below the --- line in intake/INBOX.md, then clear those lines."""
    import re
    f = ROOT / "intake" / "INBOX.md"; txt = f.read_text()
    head, sep, body = txt.partition("\n---\n")
    left, n = [], 0
    for line in body.splitlines():
        m = re.search(r"https?://\S+", line)
        if not m: left.append(line); continue
        url = m.group(0).rstrip(").,>]")
        rest = line.replace(m.group(0), "").strip(" -*:\t") or None
        ns = argparse.Namespace(url=url, title=None, lane=None, why=None, credit=None, by="inbox paste", note=rest or "Pasted to the inbox; classification pending.")
        add(ns); n += 1
    f.write_text(head + sep + "\n".join(l for l in left if l.strip()) + "\n"); print("inbox queued", n)

def github(a):
    """Free discovery over the GitHub API: new public repos from SAP's orgs and active SAP x AI repos. Capped."""
    import os, re, urllib.parse
    tok = os.environ.get("GITHUB_TOKEN"); held = known_urls(); since = (datetime.date.today() - datetime.timedelta(days=a.days)).isoformat()
    def get(u):
        h = {"Accept": "application/vnd.github+json", "User-Agent": "sapfans-refs"}
        if tok: h["Authorization"] = "Bearer " + tok
        return json.loads(urllib.request.urlopen(urllib.request.Request(u, headers=h), timeout=30).read())
    qs = [f"org:SAP-samples created:>={since}", f"org:SAP created:>={since}", f"org:SAP-docs created:>={since}",
          f"sap mcp in:name,description pushed:>={since} stars:>=10",
          f"sap agent in:name,description pushed:>={since} stars:>=25",
          f"topic:sap-btp pushed:>={since} stars:>=25"]
    n = 0
    for q in qs:
        try: items = get("https://api.github.com/search/repositories?sort=stars&order=desc&per_page=10&q=" + urllib.parse.quote(q)).get("items", [])
        except Exception as e: print("search failed:", q, e); continue
        for r in items:
            if n >= a.cap: break
            if r["html_url"] in held or r.get("archived") or r.get("fork"): continue
            official = r["owner"]["login"] in ("SAP", "SAP-samples", "SAP-docs")
            text = (r["full_name"] + " " + (r.get("description") or ""))
            if not official and not re.search(r"\bSAP\b|\bABAP\b|\bBTP\b|S/?4 ?HANA|\bHANA\b|Datasphere|\bJoule\b|\bCAP\b|\bUI5\b|SuccessFactors|\bAriba\b", text): continue
            ns = argparse.Namespace(url=r["html_url"], title=r["full_name"], lane=None, why=None, credit=None,
                by="ARK GitHub lane (" + q.split(" ")[0] + ")",
                note=((r.get("description") or "").strip()[:160] + f" · ★{r['stargazers_count']} · {'SAP official' if official else 'community'} · pushed {r['pushed_at'][:10]}"))
            add(ns); held.add(r["html_url"]); n += 1
    print("github queued", n)

def accept(a):
    q, c = load(Q), load(CAT)
    p = next(p for p in q["proposals"] if p["id"] == a.id)
    if not p.get("url"): sys.exit(f"{a.id} has no confirmed URL yet")
    why = a.why or p.get("why")
    if not why: sys.exit("a one-line --why is required: a link with no sentence is a bookmark")
    n = max(int(i["id"][2:]) for i in c["items"]) + 1
    row = {k: p.get(k) for k in ("title","url","lane","role","product","format","level","access","source","priority","credit")}
    row.update(id=f"R-{n:03d}", why=why, added=TODAY, checked=TODAY, status="live", from_proposal=p["id"])
    c["items"].append(row); p["state"] = "accepted"; p["decided"] = TODAY; p["row"] = row["id"]
    save(CAT, c); save(Q, q); review(None); print("accepted", a.id, "->", row["id"])

def reject(a):
    q = load(Q); p = next(p for p in q["proposals"] if p["id"] == a.id)
    p.update(state="rejected", decided=TODAY, reason=a.reason); save(Q, q); review(None); print("rejected", a.id)

def alive(url):
    for m in ("HEAD", "GET"):
        try:
            r = urllib.request.urlopen(urllib.request.Request(url, method=m, headers={"User-Agent": "Mozilla/5.0 SAPfans-refcheck"}), timeout=20)
            return r.status < 400
        except urllib.error.HTTPError as e:
            if e.code in (401, 403, 429): return True   # behind sign-in or bot wall: held, not dead
            if m == "GET": return False
        except Exception:
            if m == "GET": return False
    return False

def check(a):
    c = load(CAT); dead = []
    for i in c["items"]:
        if i["status"] == "retired": continue
        ok = alive(i["url"]); i["checked"] = TODAY
        if not ok: i["status"] = "stale"; dead.append(i["id"])
        elif i["status"] == "stale": i["status"] = "live"
    save(CAT, c); print("stale:", dead or "none")

def review(a):
    q = load(Q)["proposals"]; c = load(CAT)
    op = [p for p in q if p["state"] == "open"]
    L = ["# Review list — proposed references", "",
         f"Updated {TODAY}. {len(op)} open. Accept: `python3 scripts/refs.py accept P-001 --why \"one line\"` · Reject: `... reject P-001 --reason \"...\"`.",
         "Or reply in the session with the IDs to accept or reject.", "",
         "| ID | Proposed | Title | Lane · Role · Product | Pri | Found by | Note |", "|---|---|---|---|---|---|---|"]
    for p in sorted(op, key=lambda p: (p.get("priority") or 9, p["id"])):
        t = f"[{p['title']}]({p['url']})" if p.get("url") else p["title"] + " (no URL yet)"
        L.append(f"| {p['id']} | {p['proposed']} | {t} | {p.get('lane') or '—'} · {', '.join(p.get('role') or []) or '—'} · {p.get('product') or '—'} | {p.get('priority') or '—'} | {p.get('found_by') or '—'} | {p.get('note') or ''} |")
    st = [i for i in c["items"] if i["status"] == "stale"]
    L += ["", f"## Stale on the live page ({len(st)})", ""] + [f"- {i['id']} [{i['title']}]({i['url']}) — last checked {i['checked']}" for i in st]
    dn = [p for p in q if p["state"] != "open"]
    L += ["", f"## Decided ({len(dn)})", ""] + [f"- {p['id']} {p['state']} {p.get('decided','')} — {p['title']}" + (f" ({p.get('reason')})" if p.get('reason') else "") for p in dn]
    L += ["", "---", "", "© 2026 EVEglyphDesign. Pour le bien-être du peuple.", ""]
    MD.write_text("\n".join(L)); 

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); s = ap.add_subparsers(dest="cmd", required=True)
    x = s.add_parser("add"); x.add_argument("url"); x.add_argument("--title"); x.add_argument("--lane"); x.add_argument("--by", default="operator paste"); x.add_argument("--why"); x.add_argument("--credit"); x.add_argument("--note"); x.set_defaults(f=add)
    x = s.add_parser("accept"); x.add_argument("id"); x.add_argument("--why"); x.set_defaults(f=accept)
    x = s.add_parser("reject"); x.add_argument("id"); x.add_argument("--reason", required=True); x.set_defaults(f=reject)
    s.add_parser("issue").set_defaults(f=issue); s.add_parser("inbox").set_defaults(f=inbox)
    x = s.add_parser("github"); x.add_argument("--days", type=int, default=7); x.add_argument("--cap", type=int, default=10); x.set_defaults(f=github)
    s.add_parser("check").set_defaults(f=check); s.add_parser("review").set_defaults(f=review)
    a = ap.parse_args(); a.f(a)
