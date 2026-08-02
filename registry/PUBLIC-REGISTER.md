# EVEglyphDesign — Public Repository Register

**Document ID** `EgD-CON-001/REG` · **Key ID** `EgD-KEY-2026-07` · **Generated** `2026-08-02T21:39:26Z`

> The consultant-facing reading of the estate. Every **public** repository is named in full. Private repositories are counted and weighed but not named — access to those is granted per repository, per person, on request. Nothing here is inferred; every value was read from the GitHub repository layer.

## Shape of the estate

| Measure | Value |
|---|---|
| Repositories | **105** |
| Public | 44 |
| Private (named on request) | 61 |
| Total size | **1,893 MB** |
| Lanes | 9 |

### By lane

| Lane | Repositories | Public | MB |
|---|---|---|---|
| Hawkins / Peterbilt | 10 | 7 | 1,061 |
| Parish / community | 8 | 7 | 678 |
| Research / outreach | 19 | 8 | 80 |
| Client lanes | 5 | 0 | 32 |
| Education / games | 13 | 8 | 13 |
| Epiq / Steel Cloud | 9 | 2 | 11 |
| Sovereign data / twins | 11 | 2 | 6 |
| EVE Glyph core / canon | 17 | 6 | 6 |
| Enterprise / SAP / DMZ | 13 | 4 | 6 |

### By class

| Class | Count | Meaning |
|---|---|---|
| `L0` | 1 | Entry layer — the fixed landing point every agent reads first. |
| `CANON` | 9 | Doctrine and record of truth. Changes here bind everything else. |
| `VAULT` | 8 | Restricted custody. Never public. |
| `DATA` | 9 | Bulk data store. Candidate for index-plus-object-storage. |
| `SURFACE` | 30 | Published surface with a live GitHub Pages address. |
| `ACTIVE` | 39 | Working lane with substance, no published surface. |
| `FORK` | 3 | Third-party upstream vendored in. Not EgD authorship. |
| `STUB` | 4 | Four files or fewer, no substantive README. |
| `EMPTY` | 2 | No files on the default branch. |

### Canon deviations across the estate

These are the counts the pattern in this kit exists to drive to zero.

| Deviation | Repositories |
|---|---|
| no commit since 2026-07-25 | 65 |
| missing `.canon/POINTER.md` | 25 |
| no LICENSE or LICENSE-NOTICE.md | 17 |
| no README on the default branch | 12 |
| over 100 MB | 2 |
| README asserts a visibility the repository does not have | 2 |
| named `-public` but held private | 1 |

## Public repositories

Sorted by lane, then by weight. These are readable by anyone; clone them to see the pattern applied.

### EVE Glyph core / canon — 6 public

| Repository | Class | MB | Last commit |
|---|---|---|---|
| [eve-glyph-boot-contract](https://github.com/EVEglyphDesign/eve-glyph-boot-contract) | `CANON` | 0.4 | 2026-08-02 |
| [umbrella-copyright-proof](https://github.com/EVEglyphDesign/umbrella-copyright-proof) | `EMPTY` | 0.3 | 2026-07-25 |
| [enterprise-grade-criteria](https://github.com/EVEglyphDesign/enterprise-grade-criteria) | `SURFACE` | 0.2 | 2026-08-02 |
| [agent-governance-ledger](https://github.com/EVEglyphDesign/agent-governance-ledger) | `CANON` | 0.0 | 2026-07-31 |
| [eveglyph-arrivals](https://github.com/EVEglyphDesign/eveglyph-arrivals) | `ACTIVE` | 0.0 | 2026-07-25 |
| [EVEglyphDesign](https://github.com/EVEglyphDesign/EVEglyphDesign) | `CANON` | 0.0 | 2026-07-25 |

### Education / games — 8 public

| Repository | Class | MB | Last commit |
|---|---|---|---|
| [paix-educational-game](https://github.com/EVEglyphDesign/paix-educational-game) | `SURFACE` | 3.8 | 2026-07-27 |
| [eve-glyph-education-public](https://github.com/EVEglyphDesign/eve-glyph-education-public) | `SURFACE` | 2.2 | 2026-07-25 |
| [game-universal-reference-model](https://github.com/EVEglyphDesign/game-universal-reference-model) | `SURFACE` | 1.6 | 2026-08-02 |
| [eve-hyperloop](https://github.com/EVEglyphDesign/eve-hyperloop) | `SURFACE` | 0.7 | 2026-07-25 |
| [godot-action-adventure-starter](https://github.com/EVEglyphDesign/godot-action-adventure-starter) | `SURFACE` | 0.4 | 2026-08-02 |
| [Victoria](https://github.com/EVEglyphDesign/Victoria) | `SURFACE` | 0.3 | 2026-07-25 |
| [carbon-engine-intake](https://github.com/EVEglyphDesign/carbon-engine-intake) | `SURFACE` | 0.1 | 2026-08-02 |
| [starship-academy-demo](https://github.com/EVEglyphDesign/starship-academy-demo) | `SURFACE` | 0.0 | 2026-07-25 |

### Enterprise / SAP / DMZ — 4 public

| Repository | Class | MB | Last commit |
|---|---|---|---|
| [eve-no-more-ivr](https://github.com/EVEglyphDesign/eve-no-more-ivr) | `SURFACE` | 0.8 | 2026-07-31 |
| [dmzopen-ai](https://github.com/EVEglyphDesign/dmzopen-ai) | `SURFACE` | 0.4 | 2026-07-25 |
| [NA-Nuclear-Utilities](https://github.com/EVEglyphDesign/NA-Nuclear-Utilities) | `SURFACE` | 0.1 | 2026-07-25 |
| [godaddy-killer](https://github.com/EVEglyphDesign/godaddy-killer) | `SURFACE` | 0.1 | 2026-07-31 |

### Epiq / Steel Cloud — 2 public

| Repository | Class | MB | Last commit |
|---|---|---|---|
| [epiq-revenue-leakage](https://github.com/EVEglyphDesign/epiq-revenue-leakage) | `SURFACE` | 0.2 | 2026-07-25 |
| [epiq-audit-surface](https://github.com/EVEglyphDesign/epiq-audit-surface) | `STUB` | 0.0 | 2026-08-01 |

### Hawkins / Peterbilt — 7 public

| Repository | Class | MB | Last commit |
|---|---|---|---|
| [eve-hawkins-telus-twin](https://github.com/EVEglyphDesign/eve-hawkins-telus-twin) | `DATA` | 1,054.8 | 2026-07-31 |
| [hawkins-twin-platform](https://github.com/EVEglyphDesign/hawkins-twin-platform) | `SURFACE` | 1.2 | 2026-08-02 |
| [eve-hawkins-cdk-twin](https://github.com/EVEglyphDesign/eve-hawkins-cdk-twin) | `SURFACE` | 1.0 | 2026-07-31 |
| [eve-vendor-sphere](https://github.com/EVEglyphDesign/eve-vendor-sphere) | `SURFACE` | 0.6 | 2026-08-02 |
| [eve-hawkins-sovereign-enterprise](https://github.com/EVEglyphDesign/eve-hawkins-sovereign-enterprise) | `SURFACE` | 0.1 | 2026-07-28 |
| [eve-dealer-parts-twin](https://github.com/EVEglyphDesign/eve-dealer-parts-twin) | `EMPTY` | 0.0 | 2026-07-25 |
| [dicoe-partner-program](https://github.com/EVEglyphDesign/dicoe-partner-program) | `SURFACE` | 0.0 | 2026-07-25 |

### Parish / community — 7 public

| Repository | Class | MB | Last commit |
|---|---|---|---|
| [ark-midwest-watch](https://github.com/EVEglyphDesign/ark-midwest-watch) | `DATA` | 639.0 | 2026-07-29 |
| [paix-parish-platform](https://github.com/EVEglyphDesign/paix-parish-platform) | `SURFACE` | 36.0 | 2026-08-01 |
| [sanatana-community-platform](https://github.com/EVEglyphDesign/sanatana-community-platform) | `SURFACE` | 1.5 | 2026-07-31 |
| [paroisse-sainte-anne-des-pays-bas](https://github.com/EVEglyphDesign/paroisse-sainte-anne-des-pays-bas) | `SURFACE` | 1.2 | 2026-07-25 |
| [holy-trinity-caisse](https://github.com/EVEglyphDesign/holy-trinity-caisse) | `SURFACE` | 0.4 | 2026-07-25 |
| [lenexa-city-center-commons](https://github.com/EVEglyphDesign/lenexa-city-center-commons) | `SURFACE` | 0.2 | 2026-08-02 |
| [johnson-county-twin](https://github.com/EVEglyphDesign/johnson-county-twin) | `SURFACE` | 0.1 | 2026-07-29 |

### Research / outreach — 8 public

| Repository | Class | MB | Last commit |
|---|---|---|---|
| [icloud_photos_downloader](https://github.com/EVEglyphDesign/icloud_photos_downloader) | `FORK` | 45.8 | 2026-07-25 |
| [freefred](https://github.com/EVEglyphDesign/freefred) | `SURFACE` | 1.0 | 2026-07-25 |
| [eve-substack-archive](https://github.com/EVEglyphDesign/eve-substack-archive) | `DATA` | 0.8 | 2026-08-01 |
| [jre-montreal-bridge](https://github.com/EVEglyphDesign/jre-montreal-bridge) | `ACTIVE` | 0.1 | 2026-08-02 |
| [ark-peer-review-ledger](https://github.com/EVEglyphDesign/ark-peer-review-ledger) | `SURFACE` | 0.1 | 2026-07-25 |
| [eve-cokins-lane](https://github.com/EVEglyphDesign/eve-cokins-lane) | `SURFACE` | 0.0 | 2026-08-01 |
| [us-healthcare](https://github.com/EVEglyphDesign/us-healthcare) | `SURFACE` | 0.0 | 2026-07-26 |
| [video-dispatch](https://github.com/EVEglyphDesign/video-dispatch) | `SURFACE` | 0.0 | 2026-07-25 |

### Sovereign data / twins — 2 public

| Repository | Class | MB | Last commit |
|---|---|---|---|
| [eve-datasphere-sovereign](https://github.com/EVEglyphDesign/eve-datasphere-sovereign) | `DATA` | 2.6 | 2026-08-01 |
| [data-liberation-kit](https://github.com/EVEglyphDesign/data-liberation-kit) | `ACTIVE` | 0.1 | 2026-07-31 |

## What is withheld and why

61 repositories are private. They hold signed agreements, key material, biometric and personal record, client data under NDA, and intake lanes that are not ready to be read. Naming them publicly would leak the shape of client work. If your engagement needs one, ask and you will be added to that repository specifically — see [Link your GitHub account](https://github.com/EVEglyphDesign/sapfans-io/blob/main/practitioners/00-LINK-YOUR-GITHUB.md).

---

© 2026 EVEglyphDesign. Controlled copy. *Pour le bien-être du peuple.*