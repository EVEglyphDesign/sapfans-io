# MCP tool contract — template

**Use this when the client's front door is an agent platform, not a chat window.**

Copilot Studio, and platforms like it, do not read `CLAUDE.md`. They call **tools**.
So the seam between the client's existing agent and your repository-held record is an
MCP server, and this file is the contract for what that server exposes.

Fill it in *before* any diagram and *before* any code. It is committed to the project
repository and it is the thing everyone — client, integrator, the agent itself — reads to
know what the surface does and does not do.

Copy to `<repo>/mcp/TOOL-CONTRACT.md`. Replace every `<…>`. Delete this preamble.

---

## Contract

| Field | Value |
|---|---|
| Server name | `<org>-<subject>` |
| Version | `0.1.0` |
| Owner | `<name, role>` |
| Status | draft / agreed / live |
| Record of truth | `<repository or sidecar the tools read from>` |
| Caller | `<the client's agent — e.g. Copilot Studio agent "<name>">` |

## The shape — three tools

Three is enough for a first cut, and three is what a person can hold in their head.
One returns **evidence**, one returns the **record**, one returns **actions**. Add a
fourth only when a real call could not be served by these.

| # | Tool | Answers the question | Returns |
|---|---|---|---|
| 1 | `<domain>.query` | "Show me the pattern" | Evidence rows, each citing its source record |
| 2 | `<domain>.lines` | "Show me the actual record" | Source-of-record rows, verbatim, no inference |
| 3 | `<domain>.queue` | "What should someone do about it" | Prioritised, evidence-linked items. **Draft-only** — never sends, never writes back |

### Tool 1 — `<domain>.query`

- **Purpose:** parameterised lookups against known patterns. The tool knows the patterns;
  the caller supplies the parameters.
- **Inputs:** `<pattern id>`, `<date range>`, `<entity filter>`, `<limit>`
- **Outputs:** rows of `{ finding, value, source_ref, retrieved_at }`. Every row carries a
  `source_ref` that resolves to a Tool 2 row.
- **Never:** invents a value. If the pattern returns nothing, the answer is an empty set,
  not a plausible number.

### Tool 2 — `<domain>.lines`

- **Purpose:** the source of record, exactly as held. Raw evidence supersedes any
  inference the caller has made.
- **Inputs:** `<record id or range>`, `<as-of date>`
- **Outputs:** rows exactly as stored, plus `{ source_system, extracted_at, hash }`.
- **Never:** transforms, aggregates, or "helps". That is Tool 1's job.

### Tool 3 — `<domain>.queue`

- **Purpose:** the actionable list, ranked, each item linked to the evidence that put it
  there.
- **Inputs:** `<priority band>`, `<owner filter>`, `<limit>`
- **Outputs:** items of `{ priority, summary, evidence_refs[], suggested_action, draft }`.
  `draft` is text the caller may present to a human. It is not sent by this tool.
- **Never:** writes to the system of record. Never sends a message. Never changes state
  anywhere. If the caller wants an action taken, a human takes it.

## Entitlement rule

> The MCP server enforces exactly the read-only rules the caller's own platform already
> grants. It widens nothing. A user who cannot see a record through the client's existing
> tools cannot see it through this server.

- Identity arrives via: `<OAuth 2.0 / API key / platform-forwarded identity>`
- Row-level rule: `<what filters by whom>`
- Field-level rule: `<what is redacted, for whom>`
- Denied calls return: an empty set and an audit row. Not an error that leaks the shape of
  what was denied.

## Provenance and logging

Every call, every result, in the same action — not a follow-up.

| What | Where |
|---|---|
| The call: tool, parameters, caller identity, timestamp | `<observability store — e.g. LangFuse>` |
| The result: row count, source refs, hash | same |
| The record itself | stays in `<repository / sidecar>`. Never copied into the caller's platform |

The test: if the caller's platform were switched off tomorrow, would the record, the
reasoning and the audit trail all still be in the client's custody? If not, the seam is in
the wrong place.

## Platform requirements — Copilot Studio

Verified against Microsoft Learn, 2026-09-19. Re-check before go-live; these move.

| Requirement | Value | Why it matters |
|---|---|---|
| Transport | **Streamable HTTP.** SSE not supported after August 2025 | A server on SSE cannot be called at all |
| Auth | None · API key (header or query) · OAuth 2.0 (dynamic discovery, dynamic, or manual) | OAuth 2.0 is the entitlement seam; API key is for a locked-down pilot only |
| Connectivity | Rides **Power Platform connectors** | The client's DLP policy must allow the connector, or calls fail silently |
| Registration | MCP onboarding wizard in Copilot Studio, or a custom connector from an OpenAPI spec | Wizard is the supported path; custom connector is the fallback |

## What the caller may and may not do

| May | May not |
|---|---|
| Call any of the three tools with the identity it holds | Write to the system of record through this server |
| Present Tool 3 drafts to a human | Send a Tool 3 draft anywhere |
| Cache a result for the session | Persist results into its own platform's data store |
| Run its own generative reasoning on what comes back | Claim a figure this server did not return |

## Change control

This file is versioned. A change to any tool's inputs, outputs or entitlement rule is a
new version with the prior text kept verbatim in the change log below, per the
repository's canon (append, correct, supersede — never delete).

| Version | Date | Change | Prior text |
|---|---|---|---|
| 0.1.0 | `<date>` | Initial contract | — |

---

*Template from [SAPfans.io](https://sapfans.io) · © 2026 EVEglyphDesign · MIT. Remove this line in private copies.*
