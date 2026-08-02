# 02 · Build your first twin

**A twin is a repository that is the authoritative record of one real thing.** A client, a
fleet, a building, a person's health record, a parish, a product line. Not a model of it —
the record of it, with provenance, that a person or an agent can act on.

If you take one idea from this page: **the twin is the index, not the warehouse.**

## The five parts every twin has

| Part | File | What it holds |
|---|---|---|
| Identity | `TWIN-MANIFEST.yml` | What this twin is of, who owns it, what class it is |
| Sources | `registry/PROVENANCE.md` | Every input: what, from where, fetched when, by whom |
| Record | `data/` or an index into object storage | The facts themselves |
| Reading | `docs/` | The published surface a human actually looks at |
| Binding | `.canon/POINTER.md` | The contract this twin obeys |

A twin missing provenance is not a twin. It is a folder.

## Step 1 — Scaffold it

```bash
git clone https://github.com/EVEglyphDesign/sapfans-io.git
cd sapfans-io
bash scripts/new-repo.sh acme-fleet-twin "Acme fleet digital twin" private
```

That creates the repository, applies the skeleton, commits, and pushes. Read
[`scripts/new-repo.sh`](https://github.com/EVEglyphDesign/sapfans-io/blob/main/scripts/new-repo.sh) before you run it — never run a
script against your own account without reading it.

**Default to `private`.** A twin becomes public only when the client has said so in writing
and the record contains nothing that identifies a person.

## Step 2 — Declare what it is of

Fill in `TWIN-MANIFEST.yml`. The template is
[`templates/TWIN-MANIFEST.yml`](https://github.com/EVEglyphDesign/sapfans-io/blob/main/templates/TWIN-MANIFEST.yml). Be specific.
"Acme" is not a subject; "Acme Logistics — the 412 tractors and 690 trailers operated from
three yards" is.

## Step 3 — Bring in sources, with their provenance

For every input, append one row to `registry/PROVENANCE.md` **in the same commit that adds
the data.** Not afterwards. Afterwards never happens.

```
| 2026-08-02 | telematics-export-jul.csv | Acme Geotab export, supplied by J. Eden | 412 rows | sha256:… |
```

Rules that are not negotiable:

- **Preserve the source exactly as received.** Keep the original alongside anything derived
  from it. Transformations are additional files, never replacements.
- **Inject no opinion.** If the source says the odometer is blank, the record says blank.
  It does not say "likely 0".
- **Never commit personally identifying data to a public repository.** Not names, not
  addresses, not registration plates, not photographs of people.

## Step 4 — Keep the weight out

This is the failure the estate has already made, twice, and it is worth learning secondhand.
Two repositories in this account hold **92% of all its bytes** — 1,693 MB out of
1,893 MB — because bulk data was committed directly instead of indexed.

The consequence is not disk space. It is that every clone, every CI run and every agent
read pays for the whole warehouse to answer one question about one row.

**The pattern instead:**

- Bulk objects — media, exports over ~25 MB, archives, model weights — live in object
  storage.
- The repository holds a **manifest**: object key, size, SHA-256, retrieved date, and what
  the object contains.
- Anything that needs the bytes resolves them from the manifest.

A twin repository should stay **under 100 MB**. If it is growing past that, the weight is in
the wrong place. `scripts/check-canon.sh` will tell you before GitHub does.

## Step 5 — Publish the reading

The record is for agents. The **reading** is for people. Put a single page in `docs/` that
states what the twin is, what it currently knows, when it was last updated, and what it does
not cover. Turn on GitHub Pages for public twins.

An artefact that exists only in a chat transcript has not been delivered. An artefact that
exists only in a private repository has been delivered to no one but us.

## Step 6 — Check yourself before you hand it over

```bash
bash scripts/check-canon.sh .
```

It checks the skeleton, the pointer, the licence notice, the manifest, provenance, repository
weight and whether your README claims a visibility the repository does not have. That last
check exists because three repositories in this account currently fail it.

## What "done" means

- [ ] `TWIN-MANIFEST.yml` complete and specific
- [ ] Every source has a provenance row with a hash
- [ ] Repository under 100 MB; bulk indexed, not committed
- [ ] `docs/` page states what is known **and what is not covered**
- [ ] `check-canon.sh` clean
- [ ] Committed and pushed — not held in a working copy
- [ ] Access granted to the people who need it, and no one else

---

© 2026 EVEglyphDesign. Controlled copy. *Pour le bien-être du peuple.*
