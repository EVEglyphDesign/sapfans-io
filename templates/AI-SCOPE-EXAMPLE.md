# AI scope file — worked example

**Status** Draft for review · **Version** 0.1 · **Illustrative only** — no real client, person or data.

A filled-in copy of [`AI-SCOPE-FILE.md`](AI-SCOPE-FILE.md) for a functional consultant on an S/4HANA Finance greenfield.

---

## 1. The work

| Field | Answer |
|---|---|
| Operator | Finance functional consultant, S/4HANA FI-CO |
| Objective | A fit-to-standard record for the record-to-report process that the build team can trace line by line |
| Client or context | Mid-size manufacturer, S/4HANA Cloud Private Edition, Explore phase |

## 2. The boundary

| The AI may | The AI may not | The AI must ask first |
|---|---|---|
| Read workshop notes and the client's chart of accounts extract | Approve a design decision | Running anything that costs credits beyond a single search |
| Draft requirement rows with their source line | Send anything outside this repository | Deleting or rewriting a committed file |
| Propose open questions for the next workshop | Touch any SAP system | Adding scope outside record-to-report |

## 3. The record

| Layer | Where it lives |
|---|---|
| Evidence | `evidence/workshops/` — notes kept with date and attendee role |
| Decision | `decisions/DECISIONS.md` — one row per decision, owner and reason |
| Handoff | `handoff/BUILD-ITEMS.md` — each item points back to its decision row |

Mistakes go to `registry/OBSERVATIONS.md`.

---

## Why this one works

Every build item walks back to a decision, and every decision walks back to something the client said.
The AI extracts and proposes. The consultant owns the meaning. The client approves.
