# Reference Packing Standard

## Purpose
This standard governs the order of curated references, link collections, repository index entries, transfer manifests, and regenerated documentation surfaces in SAPfans.io. It preserves the intended domain hierarchy and prevents automated rebuilds from alphabetizing, merging, or otherwise reshuffling reference groups.

## Mandatory packing order

Apply the following order exactly wherever references are presented, transferred, or regenerated:

1. **SAP references** — always first. These are the primary domain references for SAPfans.io.
2. **AWS and other platform or vendor references** — immediately after SAP, following the approved architecture or solution packing order.
3. **Microsoft automation references** — including Power Automate, GitHub Copilot, Microsoft Copilot, Power Platform, and operational-resilience material.
4. **Other supporting technical, governance, implementation, partner, and research references.**
5. **EVE Glyph Design and personal/source design material** — always last. Do not interleave this material with SAP, vendor, implementation, or governance references.

## Rebuild and transfer controls

- Do not alphabetize reference groups globally.
- Do not merge groups solely because their subjects are similar.
- Preserve the sequence above in transfer files, JSON manifests, HTML link panels, Markdown indexes, and generated repository surfaces.
- If a source is classified in more than one group, place it in the earliest applicable group, except that EVE Glyph Design material remains in the final group.
- Any change to this order requires an explicit maintainer decision and a documented rationale.

## Review checklist

Before publishing or accepting a regenerated surface, verify that:

- SAP references are visibly first.
- AWS and other platform/vendor groups follow SAP in their intended packing order.
- Microsoft automation and resilience material follows the relevant vendor/platform groups.
- EVE Glyph Design references are visibly last.
- No generation or formatting step has silently alphabetized or reordered the groups.
