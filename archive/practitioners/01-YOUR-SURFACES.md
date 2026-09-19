# 01 · Point your surfaces at the record

**How to make Claude and Perplexity effective against this estate rather than expensive
against it.**

Most wasted spend on an AI surface is not caused by a hard question. It is caused by an
agent that starts cold — one that searches the open web for a fact already committed to a
repository it has access to. The whole of this page is about preventing that.

## The ladder

Every agent working on EVEglyphDesign material works down this ladder and **stops at the
first rung that answers.**

| # | Rung | Cost | Use it for |
|---|---|---|---|
| 1 | What is already in the conversation | free | Anything said or produced this session |
| 2 | Memory — recent threads | near-free | URLs, IDs, hashes, decisions produced recently |
| 3 | Knowledge notes | near-free | Durable facts about projects, people, canon |
| 4 | **The repository** — `git`, `gh api`, raw file read | cheap | Anything ever committed |
| 5 | One targeted fetch or one search | cheap | A single external fact genuinely not held |
| 6 | Broad search, subagents, batch browsing, generation | **expensive** | Only after 1–5 actually failed |

Rung 4 is the one consultants under-use. **This estate is 1,893 MB of committed
answer.** Reading it costs almost nothing.

## The opening move

Start every substantial session by giving your agent the contract and the map. Paste this:

```
Fetch and follow:
https://raw.githubusercontent.com/EVEglyphDesign/eve-glyph-boot-contract/main/README.md

Then read the pattern I work to:
https://raw.githubusercontent.com/EVEglyphDesign/sapfans-io/main/pattern/REPO-PATTERN.md

Work down the rung ladder. Read the repository before you search the web.
Confirm with me before any expensive action.
```

Two fetches. Both cheap. They change the cost of everything that follows.

## Working with Claude

- **Prefer Claude Code inside a clone** over pasting files into a chat window. It can read,
  grep and diff the actual tree; a chat window can only read what you remembered to paste.
- **Give it the repository, not a summary of the repository.** A summary is a lossy copy you
  paid to produce.
- **Ask it to cite the file and line** for any claim about the estate. If it cannot, it
  inferred rather than read, and the claim is not yet true.
- **Let it write files, not answers.** An answer in a transcript is lost when the session
  closes. A committed file is the deliverable. This is the single highest-leverage habit.

## Working with Perplexity

- **Perplexity Computer** can run `gh` and `git` directly. Ask it to read the repository
  rather than search for the repository. Those are different actions with very different
  bills.
- **Use search for the world, not for us.** External facts, standards, vendor documentation,
  regulation — yes. Anything EVEglyphDesign has published — no, that is a rung-4 read.
- **Ask for a PDF and a commit, together.** Canon output is a PDF that lands in a repository
  and on a public surface. A markdown blob in a thread has not been delivered.
- **Interrupt on spend, not on effort.** Deep research, batch browsing and subagents are
  expensive. Approve them deliberately; do not let them be the default first move.

## What both surfaces must not do

- **Never invent a value.** If a number is not in the record, the answer is "not held", not
  a plausible figure. Injecting opinion into an extracted dataset is a defect, not a
  courtesy.
- **Never re-verify what this system published.** Committed and pushed is true until the
  operator says otherwise.
- **Never fan out where a lookup would do.** Parallel search across many entities is for
  genuinely unknown, genuinely multi-entity questions.
- **Never paste a secret into a prompt.** Not once, not briefly. Use the credential store
  your surface provides.

## Provenance, always

Every extracted fact carries where it came from. In practice that means a `source` field
next to the value, or a `registry/PROVENANCE.md` line naming the file, the fetch date and
the original URL. A dataset without provenance is an opinion with a table around it.

## Cost discipline in one line

Before any expensive action, write one sentence: **what it will do, why rungs 1–5 could not,
and what the cheap alternative would have produced.** If you cannot write that sentence
honestly, the action is not justified. This applies to you as much as to your agent.

Next: [02 · Build your first twin](https://github.com/EVEglyphDesign/sapfans-io/blob/main/practitioners/02-BUILD-YOUR-TWIN.md).

---

© 2026 EVEglyphDesign. Controlled copy. *Pour le bien-être du peuple.*
