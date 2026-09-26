# ARK web lane — scheduled task cec9f10d (daily 07:00 America/Bahia_Banderas)

Added 2026-09-26 (v2.5). Runs as its own daily task; the ERP + AI monitor (793da22e) belongs to
another session and was left unchanged. The task reads this file each run. To undo: delete task
cec9f10d from its session (or ask any session to), and revert v2.5.

---

=== LANE 8 — SAPfans.io references (propose-only; runs every slot, no notification of its own) ===

Purpose: keep https://sapfans.io/references.html current. Find NEW education and reference
material a functional consultant, PMO lead, architect or developer on SAP would use.
Queue it for review. Never edit the live catalog.

Search (pplx_sdk, last 7 days, 1 query per source is enough):
- SAP Learning new courses and live sessions (learning.sap.com)
- SAP Community events, Devtoberfest / TechEd sessions, product-group blogs (community.sap.com)
- SAP developer tutorials and missions (developers.sap.com, discovery-center.cloud.sap)
- LinkedIn posts listing SAP sessions or courses (site:linkedin.com/posts) — resolve to the SAP page; keep the post URL as credit
- MIT: MIT Sloan Management Review, MIT CISR, MIT Technology Review, MIT News, MIT OpenCourseWare — only enterprise systems, ERP, AI adoption, data governance, digital transformation
(GitHub repositories are covered for free by the sapfans-io GitHub Action — do not search GitHub here.)

Queue each qualifying item (max 10 per run):
  cd /home/user/workspace && [ -d sapfans-io ] || git clone https://git-agent-proxy.perplexity.ai/EVEglyphDesign/sapfans-io.git
  cd sapfans-io && git pull -q --rebase
  python3 scripts/refs.py add "<url>" --title "<title>" --lane "<lane>" --by "ARK web lane (<source>)" --credit "<post url or null>" --note "<one line: what it is, date>"
  (refs.py skips anything already held.) Then: git add -A && git commit -m "ARK web lane: queue N references" && git push   (bash with api_credentials=["github"]; on rejection, pull --rebase and push again)

Lanes: PMO & execution · Data security · AI usage standards · BDC & Datasphere · Semantic model · Connecting AI to SAP · Joule & agentic SAP · Tools to keep open
Skip: vendor marketing with no learning content, paywalled items with no abstract, anything older than 30 days unless it is an SAP course or official doc.
If you queued anything, add this line at the end of the notification body. If there are no other hits but you queued 3 or more, send an in-app notification with only this line:
  "SAPfans: N new references on the [review list](https://github.com/EVEglyphDesign/sapfans-io/blob/main/registry/PROPOSALS.md)."
