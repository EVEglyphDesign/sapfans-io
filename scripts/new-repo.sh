#!/usr/bin/env bash
# EVEglyphDesign — scaffold a canon-conformant repository.
# Usage: bash scripts/new-repo.sh <name> "<one-line description>" [private|public]
# Read this before you run it. Never run a script against your own account unread.
set -euo pipefail

NAME="${1:?repository name required}"
DESC="${2:?one-line description required}"
VIS="${3:-private}"
OWNER="EVEglyphDesign"
KIT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

if [[ "$VIS" != "private" && "$VIS" != "public" ]]; then
  echo "visibility must be private or public" >&2; exit 1
fi

# Rule 2 — names must differ by more than one character.
STEM="$(echo "$NAME" | tr -d '-' | tr '[:upper:]' '[:lower:]')"
echo "checking for near-identical names…"
if gh repo list "$OWNER" --limit 300 --json name -q '.[].name' \
   | tr -d '-' | tr '[:upper:]' '[:lower:]' | grep -qx "$STEM"; then
  echo "REFUSED: a repository already exists whose name differs only by hyphenation." >&2
  echo "See rule 2 in pattern/REPO-PATTERN.md" >&2
  exit 1
fi

echo "creating $OWNER/$NAME ($VIS)…"
gh repo create "$OWNER/$NAME" --"$VIS" --description "$DESC" --clone
cd "$NAME"

cp -r "$KIT_DIR/templates/repo-skeleton/." .
mkdir -p docs

# Substitute the name and the visibility into the README.
sed -i.bak "s|<REPOSITORY NAME>|$NAME|; s|^\*\*Class\*\* \`ACTIVE\` · \*\*Visibility\*\* private|**Class** \`ACTIVE\` · **Visibility** $VIS|" README.md
sed -i.bak "s|One sentence: what this repository is the record of, and who it serves.|$DESC|" README.md
rm -f README.md.bak

git add -A
git commit -m "canon skeleton: $NAME

Applies the EVEglyphDesign repository pattern EgD-CON-001.
Pointer, licence notice, provenance register and docs surface in place."
git push -u origin HEAD

echo
echo "done. $OWNER/$NAME created and scaffolded."
echo "next:  edit TWIN-MANIFEST.yml if this is a twin, then run"
echo "       bash $KIT_DIR/scripts/check-canon.sh ."
