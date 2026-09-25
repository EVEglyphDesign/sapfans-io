# VERSIONS — SAPfans.io

**Document ID** `EgD-SAPF-001/VERSIONS` · **Key ID** `EgD-KEY-2026-07` · Arc required by
[EgD-BOOT-005](https://github.com/EVEglyphDesign/eve-glyph-boot-contract/blob/main/README.md#10-versioned-and-reversible--egd-boot-005).
The table only grows. A wrong row is corrected by a new row, never edited in place.

| Version | ID | Date (UTC) | Change | Inverse (exact command/action) | Tag | Confirmed (if irreversible) |
|---|---|---|---|---|---|---|
| v2.1 | L1.1 | 2026-09-25 | **Link and staleness check, report only.** Added `scripts/check-links.py` (standard library, no dependencies) and its first report `registry/LINK-CHECK.md`. Three fixed sections every run: Broken, Stale, Held. It reads `docs/*.html` and `docs/repos.json`; it never edits a page or catalog entry — a person decides what to fix or rotate out (ARK). Reader role under [EgD-BOOT-008](https://github.com/EVEglyphDesign/eve-glyph-boot-contract/blob/main/README.md#12-writers-and-readers--egd-boot-008). First run: 4 broken, 0 stale, 7 unverifiable behind sign-in or bot walls. No file under `docs/` changed, so the live site is untouched. Pattern credit: the lint skill in [undefined-ui/second-brain-os](https://github.com/undefined-ui/second-brain-os) (MIT) — idea only, no code copied. | `git revert` the commit that lands this row, or `git rm scripts/check-links.py registry/LINK-CHECK.md registry/VERSIONS.md` | `v2.1-link-check` | n/a — reversible |

---

© 2026 EVEglyphDesign. All rights reserved. Controlled copy.
*Pour le bien-être du peuple.*
