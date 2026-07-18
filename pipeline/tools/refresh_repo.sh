#!/bin/bash
#
# LOCAL repo refresh — pulls the latest cloud-pushed dashboard.html + scan data
# into the local checkout so you just refresh the browser to see newest content.
#
# The cloud routine runs in Anthropic's sandbox and CANNOT write to this Mac;
# it commits to GitHub. This script is the local half: git pull. Driven by a
# launchd agent at daytime hours (Mac awake) + on login.
#
# --rebase --autostash: replay any stray local commit on top, and stash/restore
# uncommitted noise (e.g. daily_briefing.html touch) so the pull never blocks.

set -uo pipefail

# Repo root = two levels up from this file (<repo>/pipeline/tools/refresh_repo.sh).
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
LOG="$ROOT/.refresh.log"

{
  echo "=== refresh $(date '+%F %T') ==="
  cd "$ROOT" || { echo "cd failed"; exit 1; }
  git fetch origin main --quiet
  # This checkout is a pure CONSUMER of the cloud output — nothing here authors
  # dashboard.html / _catalysts.json / daily_briefing.html / alerts.* /
  # validation.json. A past run left dashboard.html stuck in an unmerged (UU)
  # state, which made `pull --rebase --autostash` fail every day (silent stall).
  # Self-heal first: abort any orphaned rebase/merge and hard-discard local edits
  # to the generated files so a stuck conflict can never block the pull again.
  git rebase --abort 2>/dev/null || true
  git merge  --abort 2>/dev/null || true
  git checkout -- dashboard.html _catalysts.json daily_briefing.html \
                  alerts.json alerts.html validation.json 2>/dev/null || true
  BEFORE=$(git rev-parse HEAD)
  git pull --rebase --autostash origin main 2>&1
  AFTER=$(git rev-parse HEAD)
  if [[ "$BEFORE" == "$AFTER" ]]; then
    echo "already up to date ($AFTER)"
  else
    echo "updated $BEFORE -> $AFTER"
    git log --oneline "$BEFORE..$AFTER" | head -8
  fi
} >> "$LOG" 2>&1
