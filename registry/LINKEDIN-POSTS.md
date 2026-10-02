# LinkedIn posts — drafts

**Status** Draft for review · **Version** 0.1 · Operator's voice. Nothing is posted from this file.

Three posts, one per reference. Post order follows what is live: 2 and 3 can go now; 1 waits until PR #3 is merged and the page is on the site.

---

## Post 1 — Power Automate resilience (after PR #3 merges)

```
Most Power Automate flows I see in SAP-adjacent processes fail silently.

The fix is not complicated. Wrap the business actions in a Try scope. Add a Catch scope that runs after failure, timeout or skip. Log the action name, a safe error message, the run ID and a timestamp somewhere controlled. Notify with context, never with payloads. End the flow on purpose.

I wrote it up as a reusable reference on SAPfans.io, with the governance controls that keep notifications from leaking data. Credit to Ravi Potturu, whose post started it.

If you run flows against SAP, tell me what broke first. That is the part no reference covers yet.

sapfans.io/references.html
```

## Post 2 — The thread the build inherits (live)

```
Pick any line of an SAP build. A screen, a configuration, an interface, a test.

Can you walk it back to the decision that justified it, and the client source behind that decision?

On most projects the answer is "somewhere in a deck". That is where rework comes from.

On SAPfans.io I put the record in three layers: evidence, decision, handoff. The AI extracts and proposes. It never approves. The functional consultant owns the meaning, the client approves the decisions.

It starts with one Markdown file in a repository you hold.

sapfans.io/sovereign-start.html
```

## Post 3 — References, Data-first assessment lane (live)

```
The SAPfans.io references page was all SAP, and too long for someone coming up to speed.

Now it opens on the few references that matter first. And there is a new lane: Data-first assessment. Three references each for Google BigQuery, AWS, Palantir AIP, Databricks and Snowflake, because most SAP decisions now start with where the data lives.

Free, no sign-up, filterable by role, product and level.

If a reference you rely on is missing, send it. Practitioners review before anything is added.

sapfans.io/references.html
```

---

© 2026 EVEglyphDesign. All rights reserved.
