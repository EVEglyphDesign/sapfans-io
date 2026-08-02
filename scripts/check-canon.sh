#!/usr/bin/env bash
# EVEglyphDesign — check a repository against the pattern in pattern/REPO-PATTERN.md.
# Usage: bash scripts/check-canon.sh [path]   (default: current directory)
set -uo pipefail

DIR="${1:-.}"
cd "$DIR"
FAIL=0
pass() { printf '  ok    %s\n' "$1"; }
fail() { printf '  FAIL  %s\n' "$1"; FAIL=$((FAIL+1)); }
warn() { printf '  warn  %s\n' "$1"; }

echo "canon check — $(basename "$(pwd)")"
echo

# --- skeleton
[[ -f README.md ]]                && pass "README.md present"            || fail "README.md missing (rule 3)"
[[ -f .canon/POINTER.md ]]        && pass ".canon/POINTER.md present"    || fail ".canon/POINTER.md missing (rule 4)"
[[ -f LICENSE-NOTICE.md || -f LICENSE ]] && pass "licence notice present" || fail "no LICENSE or LICENSE-NOTICE.md"
[[ -f registry/PROVENANCE.md ]]   && pass "provenance register present"  || warn "registry/PROVENANCE.md missing (rule 6)"
[[ -d docs ]]                     && pass "docs/ present"                || warn "docs/ missing — no reading for humans"

# --- visibility honesty (rule 3)
if command -v gh >/dev/null 2>&1 && git remote get-url origin >/dev/null 2>&1; then
  ACTUAL="$(gh repo view --json visibility -q .visibility 2>/dev/null | tr '[:upper:]' '[:lower:]')"
  if [[ -n "${ACTUAL:-}" && -f README.md ]]; then
    CLAIM=""
    grep -qiE 'visibility[^a-z]{0,4}(private)|this repository is private' README.md && CLAIM=private
    grep -qiE 'visibility[^a-z]{0,4}(public)|this repository is public'  README.md && CLAIM=public
    if [[ -n "$CLAIM" && "$CLAIM" != "$ACTUAL" ]]; then
      fail "README claims $CLAIM, repository is $ACTUAL (rule 3)"
    else
      pass "README visibility consistent with repository ($ACTUAL)"
    fi
  fi
fi

# --- weight (rule 5)
if [[ -d .git ]]; then
  KB=$(du -sk . 2>/dev/null | cut -f1)
  MB=$((KB/1024))
  if   (( MB > 100 )); then fail "repository is ${MB} MB — over 100 MB (rule 5); index bulk into object storage"
  elif (( MB > 50  )); then warn "repository is ${MB} MB — approaching the 100 MB limit (rule 5)"
  else pass "repository weight ${MB} MB"
  fi
  BIG=$(find . -path ./.git -prune -o -type f -size +25M -print 2>/dev/null | head -5)
  [[ -n "$BIG" ]] && warn "files over 25 MB committed:
$(echo "$BIG" | sed 's/^/        /')"
fi

# --- secrets (rule 8)
if grep -rInE '(AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{30,}|-----BEGIN [A-Z ]*PRIVATE KEY-----|xox[baprs]-[A-Za-z0-9-]{10,})' \
     --exclude-dir=.git . >/dev/null 2>&1; then
  fail "possible secret committed — see rule 8. Rotate it, do not just remove it."
else
  pass "no obvious secret patterns"
fi

# --- twin manifest
if [[ -f TWIN-MANIFEST.yml ]]; then
  for k in subject class visibility owner provenance; do
    grep -q "$k:" TWIN-MANIFEST.yml && pass "manifest declares $k" || fail "manifest missing $k"
  done
  grep -q 'does_not_cover' TWIN-MANIFEST.yml && pass "manifest states what it does not cover" \
    || warn "manifest has no does_not_cover — state the gaps honestly"
fi

# --- dormancy (rule 11)
if [[ -d .git ]]; then
  LAST=$(git log -1 --format=%cs 2>/dev/null || echo "")
  if [[ -n "$LAST" ]]; then
    DAYS=$(( ( $(date +%s) - $(date -d "$LAST" +%s 2>/dev/null || echo "$(date +%s)") ) / 86400 ))
    if (( DAYS > 30 )); then warn "last commit $LAST (${DAYS} days ago) — if parked, say so in the README (rule 11)"
    else pass "last commit $LAST"; fi
  fi
fi

echo
if (( FAIL == 0 )); then echo "clean — $FAIL failures."; else echo "$FAIL failure(s). See pattern/REPO-PATTERN.md"; fi
exit $(( FAIL > 0 ))
