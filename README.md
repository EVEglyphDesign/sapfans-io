# SAPfans.io

**Make the AI work accumulate.**

[https://sapfans.io](https://sapfans.io) · `EgD-SAPF-001 r2` · Key ID `EgD-KEY-2026-07`

You already use Claude, Copilot or Perplexity on your projects. This is how to point them
at a GitHub repository so the work lands somewhere, the decisions are recorded, and the
spend shows a return.

Written by a functional consultant, for functional consultants. No methodology, no product,
nothing to buy.

## Start here

| | |
|---|---|
| **[The tutorial](docs/tutorial.html)** | From nothing to a working repository and harness. About an hour. Assumes you have never used GitHub |
| **[Usage standards](docs/standards.html)** | For delivery leads and PMO — three spend classes, one test, and what to measure |
| **[Repositories](docs/repos.html)** | A searchable directory of useful GitHub repositories, grouped by what they are for. Backed by one file: `docs/repos.json` |
| **[Heritage](heritage/HERITAGE.md)** | Where the name comes from |

## The idea in three lines

1. **The repository is the control unit.** Developers settled this long ago. The functional
   side of a project can use the same one.
2. **A harness keeps the tools consistent.** One file you edit; the Claude, Copilot and
   Perplexity versions are generated from it so they cannot drift apart.
3. **Ask for files, not answers.** An answer in a chat window is gone when the tab closes.
   A file is still there when somebody asks why in six months.

## The harness

The kit lives in [EVEglyphDesign/canon](https://github.com/EVEglyphDesign/canon). One
command from your repository's root:

```bash
curl -sL https://raw.githubusercontent.com/EVEglyphDesign/canon/main/harness/install.sh | bash
```

It writes the source file, the generator and the tool-specific files. From then on you edit
`canon/CANON.md` and re-run the build; everything else updates together, and a check fails
the moment they drift apart.

## When the client already has an agent

If the front door is Copilot Studio or another agent platform, the harness sits behind an
MCP server instead of a `CLAUDE.md`. Three read-only tools; the record stays in the
client's custody. Start from
[`templates/MCP-TOOL-CONTRACT.md`](templates/MCP-TOOL-CONTRACT.md) — the contract is
written and committed before any diagram or code.

## Taking part

- **[Discussions](https://github.com/EVEglyphDesign/sapfans-io/discussions)** — introduce
  yourself, say what you are organising, report what worked.
- **[Issues](https://github.com/EVEglyphDesign/sapfans-io/issues/new/choose)** — questions
  and corrections. Corrections are the most useful thing anyone sends.
- **[LinkedIn](https://www.linkedin.com/in/danytheriault)** — if GitHub is not where you
  want to start.

Never post client material here — no data, no system names, no screenshots of a client
system. Describe the shape of the problem instead.

## What changed in r2

This site previously published a position paper — the Additive Doctrine — along with a
practitioner pattern and a community-engagement lane. That material is preserved in
[`archive/`](archive/) rather than deleted, per the rule this estate works to: append,
correct, supersede, never delete.

The surface was rewritten for the reader it is actually for: a functional consultant who
wants a practical way to organise AI work, not a doctrine to agree with.

---

© 2026 EVEglyphDesign. Independent. Not affiliated with, endorsed by or sponsored by SAP SE
or any service provider. SAP is a trademark of SAP SE.

*Pour le bien-être du peuple.*
