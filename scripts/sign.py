#!/usr/bin/env python3
"""SAPfans.io signatures — EgD-SAPF-009. Standard library only.
A "Sign a reference" issue -> docs/signatures.json. Identity is the GitHub account that opened
the issue. LinkedIn and X links come from that account's GitHub profile (social accounts), or from
the form if they are not on the profile. No comments, ratings or phone numbers are stored."""
import json, os, re, sys, urllib.request, pathlib, datetime
ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "signatures.json"
CAT = ROOT / "docs" / "references.json"
NETS = {"linkedin": "linkedin", "x": "x", "github": "github"}

def gh(path):
    req = urllib.request.Request("https://api.github.com" + path, headers={
        "Accept": "application/vnd.github+json", "User-Agent": "sapfans-io",
        "Authorization": "Bearer " + os.environ.get("GH_TOKEN", "")})
    with urllib.request.urlopen(req, timeout=20) as r: return json.load(r)

def field(body, label):
    m = re.search(r"### " + re.escape(label) + r"[^\n]*\n+(.+?)(?:\n###|\Z)", body, re.S)
    v = m.group(1).strip() if m else ""
    return "" if v == "_No response_" else v

def linkedin(u):
    u = u.strip()
    if not u: return None
    if not u.startswith("http"): u = "https://" + u
    m = re.match(r"^https?://([a-z]{2,3}\.)?(www\.)?linkedin\.com/in/([A-Za-z0-9\-_%]{3,100})/?(\?.*)?$", u)
    return "https://www.linkedin.com/in/" + m.group(3) if m else None

def xlink(h):
    h = re.sub(r"^https?://(www\.)?(x|twitter)\.com/", "", h.strip()).lstrip("@").split("/")[0].split("?")[0]
    return "https://x.com/" + h if re.fullmatch(r"[A-Za-z0-9_]{1,15}", h) else None

def say(msg, ok):
    with open(os.environ.get("GITHUB_OUTPUT", "/dev/null"), "a") as f:
        f.write("msg<<EOF\n" + msg + "\nEOF\nok=" + ("true" if ok else "false") + "\n")
    print(msg)

def main():
    body, login = os.environ.get("ISSUE_BODY", ""), os.environ["ISSUE_USER"]
    ref = field(body, "Reference").upper().strip()
    net = field(body, "Network").lower().strip()
    remove = field(body, "Action").lower().startswith("remove")
    ids = {i["id"] for i in json.loads(CAT.read_text())["items"]}
    if ref not in ids: return say(f"`{ref or '?'}` is not a reference on the page. Open the form from a reference card on [the Reference Board](https://sapfans.io).", False)
    if net not in NETS: return say("Pick LinkedIn, X or GitHub.", False)
    d = json.loads(OUT.read_text()) if OUT.exists() else {"schema": 1, "refs": {}}
    people = d["refs"].setdefault(ref, [])
    p = next((x for x in people if x["login"].lower() == login.lower()), None)
    if remove:
        if p and net in p["links"]:
            del p["links"][net]
            if not p["links"]: people.remove(p)
        if not people: d["refs"].pop(ref, None)
        save(d); return say(f"Removed your {net_name(net)} signature from {ref}.", True)
    user = gh("/users/" + login)
    social = {}
    try:
        for s in gh(f"/users/{login}/social_accounts"):
            if s.get("provider") == "linkedin": social["linkedin"] = linkedin(s.get("url", ""))
            if s.get("provider") in ("twitter", "x"): social["x"] = xlink(s.get("url", ""))
    except Exception: pass
    typed = field(body, "Your profile link")
    if net == "github": url = "https://github.com/" + user["login"]
    elif net == "linkedin": url = social.get("linkedin") or linkedin(typed)
    else: url = social.get("x") or xlink(typed)
    if not url:
        return say(f"No {net_name(net)} link found. Add it to your [GitHub profile](https://github.com/settings/profile) (Social accounts) or type it in the form, then sign again.", False)
    if not p:
        p = {"login": user["login"], "name": user.get("name") or user["login"], "links": {}}
        people.append(p)
    p["name"] = user.get("name") or user["login"]
    p["links"][net] = url
    save(d); say(f"Signed {ref} with your {net_name(net)}. It shows on [the Reference Board](https://sapfans.io) in a minute or two.", True)

def net_name(n): return {"linkedin": "LinkedIn", "x": "X", "github": "GitHub"}[n]
def save(d):
    d["updated"] = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    OUT.write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n")

if __name__ == "__main__": main()
