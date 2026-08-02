# 00 · Link your GitHub account

**Read time 6 minutes. Do this before anything else — nothing further works without it.**

> **Two different things are described here.** Contributing to SAPfans.io needs nothing but
> a GitHub account and a fork — the repository is public and the pattern is yours to take.
> Steps 2 and 3 below concern *engagement access* to private EVEglyphDesign repositories,
> which only matters if you are working a client lane with us. Steps 1, 4 and 5 apply to
> everyone.

## What you are joining

`EVEglyphDesign` is a **GitHub user account, not an organisation.** That distinction matters
more than it sounds:

- There are no teams and no org-wide roles. Access is granted **one repository at a time**,
  to you personally, as an **outside collaborator**.
- Asking for "access to EVEglyphDesign" cannot be granted. Ask for access to a **named
  repository**, and say what you intend to do in it.
- Losing access to one repository does not touch the others, and neither does gaining it.

Of the 105 repositories in the account, 44 are already public and need no
invitation at all. Start there. Read
[the public register](https://github.com/EVEglyphDesign/sapfans-io/blob/main/registry/PUBLIC-REGISTER.md) and clone freely.

## Step 1 — Your account

1. Use a **named personal account**, not a shared or role account. Every commit must be
   attributable to a human being.
2. Turn on **two-factor authentication**. Use an authenticator app or a hardware key, not SMS.
   Access is refused to accounts without 2FA.
3. Set your **commit email**. Either your real work address or the GitHub-provided
   `USERNAME@users.noreply.github.com` — but the same one everywhere, so history is coherent.
4. Add a **profile name and photo**. You will appear in client-visible commit history.

```bash
git config --global user.name  "Your Real Name"
git config --global user.email "you@example.com"
```

## Step 2 — Ask for what you actually need

Open an issue on this repository titled `access: <repository-name>` and state:

- the repository you need,
- the engagement or client it serves,
- read or write,
- and for how long.

Time-boxed requests are approved faster than open-ended ones. Requests for `VAULT`-class
repositories are declined by default — those hold signed agreements, key material and
personal record, and they are not consultant surfaces.

You will receive an invitation by email. **Accept it within seven days** or it expires.

## Step 3 — Authenticate the command line

Install the GitHub CLI, then:

```bash
gh auth login          # choose HTTPS, authenticate in the browser
gh auth status         # must show your account and the correct scopes
gh repo list EVEglyphDesign --limit 200
```

The last command is your proof of access. It lists exactly what you can see — no more.
If a repository you were promised is missing, the invitation was not accepted.

**Prefer SSH?**

```bash
ssh-keygen -t ed25519 -C "you@example.com"
gh ssh-key add ~/.ssh/id_ed25519.pub --title "your-machine"
ssh -T git@github.com
```

## Step 4 — Link GitHub to your AI surfaces

### Claude

- **Claude Code** authenticates through your local `gh` / `git` credentials. Once step 3
  passes, run it from inside a clone and it has what it needs. Nothing else to link.
- **Claude on the web** connects to GitHub through its connector settings. Grant it the
  **specific repositories** you were invited to, never "all repositories". If the picker only
  offers all-or-nothing, use Claude Code instead.

### Perplexity

- Open **Connectors**, add **GitHub**, and authorise. It inherits exactly the repositories
  your GitHub account can see, which is why step 2 is scoped the way it is.
- In Perplexity Computer, prefer letting the agent run `gh` and `git` directly over pasting
  file contents into the thread. Reading a file from the repository is a cheap operation.
  Re-deriving its contents in conversation is not.

### The rule for both

**Grant per repository. Never grant all.** Your surface should be able to see the lane you
are working in and nothing else. This is not distrust; it is how a leak stays small.

## Step 5 — Prove the whole chain works

```bash
gh repo clone EVEglyphDesign/sapfans-io
cd sapfans-io && bash scripts/check-canon.sh .
```

If that prints a clean report, your account, your CLI and your clone are all correct, and
you can move to
[01 · Point your surfaces at the record](https://github.com/EVEglyphDesign/sapfans-io/blob/main/practitioners/01-YOUR-SURFACES.md).

## What gets your access revoked

- Pushing client data into a public repository.
- Force-pushing, rewriting history, or squashing someone else's commits.
- Committing a secret — key, token, password, connection string — even briefly.
- Deleting or renaming anything another engagement is using.

The record is append-only. Correct and supersede; never erase.

---

© 2026 EVEglyphDesign. Controlled copy. *Pour le bien-être du peuple.*
