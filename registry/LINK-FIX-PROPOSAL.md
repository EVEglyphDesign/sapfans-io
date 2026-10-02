# Link fix proposal

**Status** Proposal — nothing changed · **Version** 0.1 · **From** [LINK-CHECK.md](LINK-CHECK.md) run 2026-10-02T09:46:07Z

Six broken links in four groups. Each group has three options; the recommended one is marked. No file under `docs/` is touched until you choose.

## A. `pattern.html` — 2 links on `sovereign-start.html`, 1 on `index-v2.html`

The page was moved to `archive/pattern.html` by PR #2 (`6fe88e8`). Sovereign Start still tells readers to "go to the Pattern".

1. **Recommended** — Restore `archive/pattern.html` to `docs/` verbatim. Inverse: `git rm docs/pattern.html`.
2. Point the links at the starter landing, [eveglyphdesign.github.io/sovereign-starter](https://eveglyphdesign.github.io/sovereign-starter/). Changes reader wording.
3. Remove the links and leave the sentences as plain text.

## B. `doctrine.html` — 1 link on `index-v2.html`

No `doctrine.html` exists in `docs/` or `archive/`. `index-v2.html` is not in the main navigation.

1. **Recommended** — Point it at the controlled PDF already in `docs/`: `SAPfans_The_Additive_Doctrine.pdf`.
2. Remove the nav item from `index-v2.html`.
3. Leave it; `index-v2.html` is a draft page.

## C. SAP Learning 404 — 1 link on `index-v2.html`

The lesson URL returns 404; the course root [Guiding AI-Driven Transformation as an SAP Enterprise Architect](https://learning.sap.com/courses/guiding-ai-driven-transformation-as-an-sap-enterprise-architect) returns 200.

1. **Recommended** — Point at the course root until a peer confirms the new lesson link (open question Q-002).
2. Search SAP Learning for the replacement lesson now.
3. Remove the link.

## D. Plain http — 1 link on `heritage.html`

`easymarketplace.de/SAP-Groups.php` does not answer over https (checked 2026-10-02), so it cannot simply be upgraded.

1. **Recommended** — Keep it and label it "http only, historical".
2. Replace it with an Internet Archive snapshot.
3. Remove it.

---

© 2026 EVEglyphDesign. All rights reserved.
