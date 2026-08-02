# Pointing sapfans.io at this site

The site is live now at
<https://eveglyphdesign.github.io/sapfans-io/>. The custom domain is **one DNS change plus
one command away**.

`sapfans.io` is currently on Cloudflare nameservers (`luke.ns.cloudflare.com`,
`bristol.ns.cloudflare.com`) with no A or CNAME record published.

## 1. In Cloudflare DNS, add these five records

| Type | Name | Value | Proxy |
|---|---|---|---|
| A | `@` | `185.199.108.153` | **DNS only** (grey cloud) |
| A | `@` | `185.199.109.153` | **DNS only** |
| A | `@` | `185.199.110.153` | **DNS only** |
| A | `@` | `185.199.111.153` | **DNS only** |
| CNAME | `www` | `eveglyphdesign.github.io` | **DNS only** |

Proxying must be off, or GitHub cannot issue the TLS certificate.

## 2. Then restore the CNAME file and set the domain

```bash
git mv docs/CNAME.pending docs/CNAME
git commit -m "cutover: sapfans.io" && git push
gh api -X PUT repos/EVEglyphDesign/sapfans-io/pages -f cname=sapfans.io -F https_enforced=true
```

Certificate issuance takes a few minutes. Verify with:

```bash
curl -sI https://sapfans.io | head -1
```

## 3. Verify before announcing

Fetch the live URL and read it. A green build is not evidence.

---

© 2026 EVEglyphDesign. Controlled copy. *Pour le bien-être du peuple.*
