# The repository pattern

**Every repository in this estate obeys this. No exceptions, including this one.**

The pattern is not bureaucracy. Each rule below exists because its absence has already cost
something measurable, and the cost is named next to the rule.

## The skeleton

```
<repo>/
├── README.md                  what this is, who it serves, its actual visibility
├── LICENSE-NOTICE.md          rights and restrictions
├── .canon/
│   └── POINTER.md             the contract this repository obeys
├── docs/                      the published reading — Pages surface, PDFs
├── registry/
│   └── PROVENANCE.md          every input: what, whence, when, hash
├── data/                      the record, or the manifest that indexes it
└── scripts/                   anything runnable
```

Copy it from
[`templates/repo-skeleton/`](https://github.com/EVEglyphDesign/sapfans-io/tree/main/templates/repo-skeleton) or let
[`scripts/new-repo.sh`](https://github.com/EVEglyphDesign/sapfans-io/blob/main/scripts/new-repo.sh) do it.

## The eleven rules

### 1. One lane, one repository

A repository serves exactly one subject. If you cannot say what it is of in a single
sentence, it is two repositories.

*Cost of ignoring it:* two repositories in this account — `eve-glyph-edu-health` and
`glyph-capture-eduhealth` — carry the same fourteen files, the same ingest workflow and the
same README. One lane, two records, neither authoritative.

### 2. Names must differ by more than one character

Before creating a repository, run `gh repo list EVEglyphDesign --limit 200 | grep -i <stem>`.

*Cost of ignoring it:* `dmz-open-ai` and `dmzopen-ai` are different works in different lanes
with different visibility. Every reference to either is now ambiguous.

### 3. The README states the actual visibility

If it says public, `gh repo view --json visibility` must agree.

*Cost of ignoring it:* three repositories currently assert a posture they do not have. The
README is the artefact a reader trusts, which makes a wrong one worse than a missing one.

### 4. `.canon/POINTER.md` exists, always

It is four lines. It tells any agent landing cold which contract binds this work.

*Cost of ignoring it:* 25 repositories in this account
have no pointer. An agent landing in one of them has no way to discover the rules and will
invent its own.

### 5. Under 100 MB

Bulk objects go to object storage; the repository holds the manifest.

*Cost of ignoring it:* two repositories hold 92% of all bytes in the account. Every clone
pays for the warehouse.

### 6. Provenance in the same commit as the data

Never a follow-up commit. Follow-up commits do not happen.

### 7. Append, correct, supersede — never delete

No force-push. No history rewrite. No squashing another person's commits. On a push
rejection, rebase. Superseded material gets a `SUPERSEDED-BY` line, not a deletion.

### 8. Secrets are persisted before they are used

A key is written to the secret store **in the same action that generates it**, before it
encrypts anything. Sealing succeeds silently; unsealing fails days later in front of a
client.

### 9. Committed and pushed, or it does not exist

Holding an unpushed commit while conversing is holding someone else's property hostage.
The session is a scratchpad that will be thrown away without warning.

### 10. Output canon

PDF by default for anything a human reads as a document. Markdown only for things that are
functionally markdown — READMEs, registers, provenance. Every PDF carries the watermark,
the copyright line, a SHA-256 content hash, the Key ID, an ISO-8601 UTC timestamp and the
closing mark. **Links are clickable markdown links** — a bare URL cannot be tapped on a
phone, and that is a defect.

### 11. Dormancy is stated, not implied

If a lane is parked, say so in the README with a date. 65
repositories here have not been committed to since 2026-07-25. Most were parked
deliberately; from outside, parked and abandoned look identical.

## Naming

- Exactly `EVEglyphDesign` for the account. Prose form `EVEglyph Design`. Short form `EgD`.
  No invented variants.
- Repositories: lowercase, hyphenated, subject first — `eve-hawkins-cdk-twin`,
  `paix-parish-platform`.
- Do not append `-public` or `-private` to a name. Visibility changes; names should not.

## The look

If the repository publishes anything a client sees, it uses the house palette and nothing
else.

| Role | Hex |
|---|---|
| Cream | `#fdfaf4` |
| Cream 2 | `#f7f2e7` |
| Ink | `#1a1a1a` |
| Line | `#e7e1d3` |
| Mute | `#6b665c` |
| Accent | `#e87722` |

Fraunces for display, Inter for body. **Forbidden:** teal, navy-and-gold, generic dark
dashboards, glassmorphism, space-scifi templates.

## Classes

Declare the class in the README. It tells a reader what kind of thing they have found.

| Class | Meaning |
|---|---|
| `L0` | Entry layer. The fixed landing point every agent reads first. |
| `CANON` | Doctrine. Changes here bind everything else. |
| `VAULT` | Restricted custody. Never public. |
| `DATA` | Bulk store. Should be an index into object storage. |
| `SURFACE` | Published surface with a live Pages address. |
| `ACTIVE` | Working lane with substance, no published surface. |
| `STUB` | Placeholder. Should not stay one for long. |

## Check it

```bash
bash scripts/check-canon.sh /path/to/repo
```

Run it before you ask for review. It is the same check that produced the deviation counts in
[the public register](https://github.com/EVEglyphDesign/sapfans-io/blob/main/registry/PUBLIC-REGISTER.md).

---

© 2026 EVEglyphDesign. Controlled copy. *Pour le bien-être du peuple.*
