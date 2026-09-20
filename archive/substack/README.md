# Substack lane

`EgD-SAPF-002` · Key ID `EgD-KEY-2026-07`

The Substack posture for [SAPfans.io](https://sapfans.io), in two directions.

## The two directions

| Direction | What it is | Where it lives |
|---|---|---|
| **Outbound** — publish our own | A SAPfans.io publication seeded by the [Additive Doctrine](../paper/ADDITIVE-DOCTRINE.md) and [Heritage](../heritage/HERITAGE.md), one essay at a time, cross-linked to the repository so no post depends on the platform to survive. | This directory — outbound plan, post pipeline, publishing checklist. |
| **Mirror + engage** — read others | The SAP-adjacent and enterprise-ledger Substacks worth reading. Mirror the ones we read into [`eve-substack-archive`](https://github.com/EVEglyphDesign/eve-substack-archive), so the record does not depend on the platform, and stage engagement drafts where the Additive Doctrine has a genuine response. | [`eve-substack-archive`](https://github.com/EVEglyphDesign/eve-substack-archive) holds the mirror; this directory holds the engagement register. |

Both directions obey the [repository pattern](../pattern/REPO-PATTERN.md) — provenance in the same commit as the post, append/correct/supersede, and no client material ever.

## Outbound — the publication

- Publication name: **SAPfans.io** (matching the domain, so no reader has to reconcile two names).
- Editorial tone: [`../paper/ADDITIVE-DOCTRINE.md`](../paper/ADDITIVE-DOCTRINE.md) sets it. Practitioner-first, provider-neutral, useful before it is polished. No attack on engineers, no attack on providers.
- Cadence: one essay when there is something to say. Not on a calendar.
- Every post is committed to [`outbound/posts/`](outbound/posts/) **before** it is published, with the ISO date and slug in the filename. The Substack post is a mirror of the repository, not the source.
- Every post ends with the same close: `Pour le bien-être du peuple.`

The first four posts are already written elsewhere in this repo and just need to be reformatted for the platform. See [`outbound/PIPELINE.md`](outbound/PIPELINE.md).

## Inbound — mirror and engagement

- The register of Substacks we track lives in [`eve-substack-archive/sources.json`](https://github.com/EVEglyphDesign/eve-substack-archive/blob/main/sources.json). Set `"ingest": true` on a source and the mirror picks it up.
- Candidates specific to this lane are listed in [`inbound/CANDIDATES.md`](inbound/CANDIDATES.md) — SAP, enterprise-ledger, data-platform and sovereignty writers.
- When one of their posts is worth a reply, a draft is staged in [`inbound/engagements/<YYYY-MM-DD>-<slug>.md`](inbound/engagements/) with the source URL, the specific quote being engaged with, and the reply.
- Engagement drafts are never posted from a bot. A human posts, from a named account, with the link back to the repository post.

## What this lane will not do

- **It will not repost SAP Community threads.** That is other people's work in someone else's home. Link, credit, do not mirror.
- **It will not attack a named consultant, engineer, or vendor employee.** The [Additive Doctrine](../paper/ADDITIVE-DOCTRINE.md) covers that discipline; it applies on Substack too.
- **It will not publish client material**, however anonymised it feels.

---

© 2026 EVEglyphDesign. Controlled copy.
*Pour le bien-être du peuple.*
