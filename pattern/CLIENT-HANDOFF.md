# Client handoff

**How a new client design requirement arrives, gets recorded, and gets routed — so that the
consultant who picks it up second knows exactly as much as the one who took the call.**

The handoff is not a meeting. It is a commit.

## The five stages

### 1. Capture — within 24 hours of the conversation

Copy
[`templates/CLIENT-REQUIREMENTS.md`](https://github.com/EVEglyphDesign/sapfans-io/blob/main/templates/CLIENT-REQUIREMENTS.md) into the
client's lane repository as `requirements/<YYYY-MM-DD>-<slug>.md` and fill it in **in the
client's own words first.** Your interpretation goes in a clearly marked section underneath.

Those two must never be blended. When a requirement is disputed six weeks later, the
question is always "what did they actually say", and a blended record cannot answer it.

### 2. Classify — what kind of work is this

| Type | Meaning | Lands in |
|---|---|---|
| **Twin** | A record of a real thing | New twin repository |
| **Surface** | Something a client or public reads | `docs/` + Pages |
| **Lane** | Ongoing extraction or ingestion | Existing lane repository |
| **Canon** | A rule change | `eve-glyph-boot-contract` — operator approval required |
| **Enquiry** | A question, not yet work | Issue only. Do not create a repository. |

**Do not create a repository for an enquiry.** Four repositories in this account are stubs
and two are entirely empty because a conversation was mistaken for a commitment.

### 3. Route — name the owner and the destination

Every requirement gets, in the file:

- **Owner** — one named human. Not a team, not "TBD".
- **Destination** — the exact repository, existing or to be created.
- **Class** — from the table in
  [the repository pattern](https://github.com/EVEglyphDesign/sapfans-io/blob/main/pattern/REPO-PATTERN.md).
- **Access needed** — who must be invited, to what, read or write.

If the destination does not exist yet, `scripts/new-repo.sh` creates it in one command, and
the requirement file is the first thing committed into it.

### 4. Accept — the receiving consultant confirms in writing

The person taking the work appends an **acceptance block** to the same file: what they
understood, what they will produce, by when, and what they need that they do not have.

The handoff is complete when that block is committed. Not when the call ends.

### 5. Close — supersede, never delete

When the requirement is met, append a **disposition block**: what was built, where it lives,
its SHA if it is a document, and the date. Requirements are never deleted and never edited
into irrelevance. Superseded ones get a `SUPERSEDED-BY` line pointing at the successor.

## What must be in the record before work starts

- [ ] The client's own words, verbatim, dated
- [ ] Your interpretation, separately labelled
- [ ] Constraints — regulatory, contractual, technical, calendar
- [ ] What is explicitly **out** of scope
- [ ] Data the client will supply, in what form, by when
- [ ] Named owner and named destination repository
- [ ] Visibility decision — private by default, public only in writing
- [ ] Acceptance block from the receiving consultant

Any box unticked is the thing that will be argued about later.

## Data handling on handoff

Client data arrives private and stays private until the client says otherwise **in writing,
recorded in the requirement file.** Personally identifying material never enters a public
repository. Bulk exports go to object storage with a manifest, not into git — see
[Build your first twin](https://github.com/EVEglyphDesign/sapfans-io/blob/main/practitioners/02-BUILD-YOUR-TWIN.md).

If a client supplies credentials, they go to the secret store immediately and are never
pasted into a prompt, a commit, an issue or a chat.

## Reassigning work

Reassignment is an append. The new owner writes their own acceptance block; the previous
owner writes one line saying what state they left it in and what they know that is not yet
written down. That last clause is the whole point — the undocumented knowledge is the thing
that gets lost, and asking for it explicitly is the only reliable way to get it.

---

© 2026 EVEglyphDesign. Controlled copy. *Pour le bien-être du peuple.*
