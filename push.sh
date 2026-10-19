#!/usr/bin/env bash
# Usage: ./push.sh https://github.com/<your-username>/<repo>.git
# Creates ONE commit per experiment (exp1, exp2, ...) and pushes everything.
set -e
REPO_URL="$1"
[ -d .git ] || git init -b main
if ! git remote get-url origin >/dev/null 2>&1; then
  [ -z "$REPO_URL" ] && { echo "Give the GitHub repo URL"; exit 1; }
  git remote add origin "$REPO_URL"
fi
git add README.md .gitignore push.sh
git commit -m "Add lab record index" || true
for d in $(ls -d exp*/ | sort -V); do
  n=${d%/}
  title=$(head -1 "$n/README.md" | sed 's/^# //')
  git add "$n"
  git commit -m "$title" || true
done
git push -u origin main
