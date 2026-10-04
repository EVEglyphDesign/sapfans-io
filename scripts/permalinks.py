#!/usr/bin/env python3
"""SAPfans.io permanent links — EgD-SAPF-019. Standard library only.
Every reference or story id ever published keeps resolving, whatever the site becomes.
- archive/permalinks.json is APPEND-ONLY: an id, once in it, is never removed, renumbered or re-pointed.
- docs/r/<ID>.html is a static page per id: it opens the item on the board and always carries the article link,
  so it works even if the board page is redesigned or the item is retired.
- sapfans.io/#<ID> (the form used in signed posts) falls back to this ledger in index.html.
Run: python3 scripts/permalinks.py          (append new ids, write pages)
     python3 scripts/permalinks.py --check  (fail if any ledger id lost its page or changed URL)"""
import json, sys, html, pathlib, datetime
ROOT = pathlib.Path(__file__).resolve().parent.parent
LED = ROOT / "archive" / "permalinks.json"; REF = ROOT / "docs" / "references.json"; LAND = ROOT / "docs" / "landscape.json"; OUT = ROOT / "docs" / "r"
today = datetime.date.today().isoformat()
led = json.loads(LED.read_text()) if LED.exists() else {"schema": 1, "rule": "Append-only. Never remove, renumber or re-point an id.", "ids": {}}
items = {i["id"]: i for i in json.loads(REF.read_text())["items"]}
for p in json.loads(LAND.read_text())["platforms"]:
    items[p["id"]] = {"id": p["id"], "title": p["name"], "short": p["name"] + " on the Content Connect Board", "url": "https://sapfans.io/#" + p["id"], "why": p["class"]}
bad = []
for k, e in led["ids"].items():
    if k not in items: continue
    if items[k]["url"] != e["url"]: bad.append(f"{k}: URL changed from {e['url']} to {items[k]['url']}")
if "--check" in sys.argv:
    bad += [f"{k}: page missing" for k in led["ids"] if not (OUT / f"{k}.html").exists()]
    print("\n".join(bad) or f"ok: {len(led['ids'])} permanent ids"); sys.exit(1 if bad else 0)
if bad: print("\n".join(bad)); sys.exit("Refusing: a published id may not be re-pointed. Add a new id instead.")
for k, i in items.items():
    led["ids"].setdefault(k, {"url": i["url"], "title": i.get("short") or i["title"], "first": today})
LED.parent.mkdir(exist_ok=True); LED.write_text(json.dumps(led, ensure_ascii=False, indent=1) + "\n")
OUT.mkdir(exist_ok=True)
for k, e in led["ids"].items():
    i = items.get(k, {}); live = k in items and i.get("status") != "retired"
    t, u, why = html.escape(e["title"]), html.escape(e["url"]), html.escape(i.get("why", ""))
    board = f"https://sapfans.io/#{k}"
    go = f'<meta http-equiv="refresh" content="0;url={board}">' if live else ""
    (OUT / f"{k}.html").write_text(f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t} · SAPfans.io</title><link rel="canonical" href="https://sapfans.io/r/{k}.html">{go}
<style>body{{margin:0;background:#000;color:#fff;font:16px/1.6 Inter,system-ui,sans-serif}}main{{max-width:620px;margin:48px auto;padding:0 22px}}h1{{font:700 24px/1.25 Fraunces,Georgia,serif}}a{{color:#fff;text-decoration-color:#e87722}}.d{{color:#c8c8c8;font-size:14px}}</style></head>
<body><main><p class="d">SAPfans.io · {k}</p><h1>{t}</h1><p>{why}</p>
<p><a href="{u}">Read the article</a> · <a href="{board}">See it on the Content Connect Board</a></p>
<p class="d">Permanent link. This address will keep working.</p></main></body></html>
""")
print(f"{len(led['ids'])} permanent ids, pages in docs/r/")
