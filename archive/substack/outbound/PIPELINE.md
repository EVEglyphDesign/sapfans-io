# Outbound pipeline — SAPfans.io on Substack

`EgD-SAPF-002/OUT` · Key ID `EgD-KEY-2026-07`

## The first four posts

Written already, elsewhere in this repository. Each needs only a Substack-shaped intro paragraph and the canonical close.

| # | Working title | Source in repo | Notes |
|---|---|---|---|
| 1 | **The Additive Doctrine** | [`paper/ADDITIVE-DOCTRINE.md`](../../paper/ADDITIVE-DOCTRINE.md) | The whole essay. Publish in full. The four sovereignty tests are the money paragraph. |
| 2 | **Heritage — the community that lost its record** | [`heritage/HERITAGE.md`](../../heritage/HERITAGE.md) | The forums-to-vendor-to-practitioner arc. The [sapfans.com backup line](http://www.easymarketplace.de/SAP-Groups.php) is the hook. |
| 3 | **The repository pattern, and the cost of ignoring each rule** | [`pattern/REPO-PATTERN.md`](../../pattern/REPO-PATTERN.md) | Eleven rules, each with the price of skipping it. This is the one practitioners will bookmark. |
| 4 | **Data residency is not architectural sovereignty** | [`paper/ADDITIVE-DOCTRINE.md`](../../paper/ADDITIVE-DOCTRINE.md) §Why now | The Madrid table lifted out as a standalone piece. Written for the executive who was told their platform is sovereign. |

## Per-post workflow

1. Copy the source Markdown to `outbound/posts/<YYYY-MM-DD>-<slug>.md`. Commit before Substack sees it.
2. Add the two Substack-only lines at the top: a one-sentence subtitle, and a link back to the canonical repo file.
3. Commit again, note the SHA in the post.
4. Publish on Substack. Paste the Substack URL into the file's front-matter and commit a third time as the disposition.
5. If the piece is superseded, do not delete. Append `SUPERSEDED-BY: <path>` and commit.

## What the post must carry

- The `EgD-` document ID and the Key ID from the source file.
- A visible link to the canonical repo location.
- The close: **Pour le bien-être du peuple.**

## What the post must not carry

- No affiliate links, no tracker query strings, no email-capture popups beyond Substack's default.
- No screenshot of a client system, however anonymised it feels.
- No "hot take" on a named SAP employee, consultant or executive. Positions, yes. People, no.

## Cross-posting

The same essay can and should go to LinkedIn and to the [SAP Community blog space](https://community.sap.com) — as separate posts, each linking back to the repository, not to each other. That way no single platform is the record.

---

© 2026 EVEglyphDesign. Controlled copy.
*Pour le bien-être du peuple.*
