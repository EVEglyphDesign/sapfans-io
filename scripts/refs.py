#!/usr/bin/env python3
"""SAPfans.io reference catalog — intake, review and upkeep. Standard library only.

  refs.py add URL [--title T] [--lane L] [--why W] [--credit C] [--by NAME]
                                                       paste a link -> review queue (state=open)
  refs.py issue                                        same, from a GitHub issue body in $ISSUE_BODY
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
        credit=a.credit, found_by=a.by, proposed=TODAY, state="open", note="Pasted; classification pending."))
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
    x = s.add_parser("add"); x.add_argument("url"); x.add_argument("--title"); x.add_argument("--lane"); x.add_argument("--by", default="operator paste"); x.add_argument("--why"); x.add_argument("--credit"); x.set_defaults(f=add)
    x = s.add_parser("accept"); x.add_argument("id"); x.add_argument("--why"); x.set_defaults(f=accept)
    x = s.add_parser("reject"); x.add_argument("id"); x.add_argument("--reason", required=True); x.set_defaults(f=reject)
    s.add_parser("issue").set_defaults(f=issue); s.add_parser("check").set_defaults(f=check); s.add_parser("review").set_defaults(f=review)
    a = ap.parse_args(); a.f(a)
