#!/bin/bash
#
# L1 cheap single-ticker re-check. ON-DEMAND — run this when the L0 monitor
# flags a ticker (stop breach / T1-T2 hit / entered zone) and you want a fresh
# read WITHOUT paying for the full weekly 12-agent pipeline.
#
# Cost: ~3 analyst calls (market + news + sentiment) + a short synthesis vs the
# locked thesis. Cheap by design — no debate, no risk panel, no portfolio mgr.
#
# Usage:
#   recheck.sh TICKER [DATE]
#   recheck.sh NVDA                 # today
#   recheck.sh MRVL 2026-06-23
#
# Writes:  <scans>/<DATE>/<TICKER>/recheck.md   (does NOT overwrite final_decision.md)
#
# Env:
#   TRADING_SCANS_ROOT   scans repo root (default: derive from this file)
#   RECHECK_MODEL        claude model (default: sonnet)

set -uo pipefail

TICKER="${1:-}"
if [[ -z "$TICKER" ]]; then
  echo "usage: recheck.sh TICKER [DATE]" >&2
  exit 2
fi
DATE="${2:-$(date +%F)}"

TOOLS_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="${TRADING_SCANS_ROOT:-$(cd "$TOOLS_DIR/../.." && pwd)}"
MODEL="${RECHECK_MODEL:-sonnet}"
OUT_DIR="$ROOT/$DATE/$TICKER"
mkdir -p "$OUT_DIR"

# Pull the locked levels from the most recent final_decision.md so the re-check
# can say "thesis intact / broken vs what we locked".
LOCKED=$(ls -t "$ROOT"/*/"$TICKER"/final_decision.md 2>/dev/null | head -1)
LOCKED_TXT=""
[[ -n "$LOCKED" ]] && LOCKED_TXT=$(cat "$LOCKED")

# Live price snapshot (free, no LLM) for grounding.
PY="${TRADING_SCANS_ROOT:+}"; PY_BIN="$TOOLS_DIR/venv/bin/python"
[[ -x "$PY_BIN" ]] || PY_BIN="python3"
PRICE_JSON=$("$PY_BIN" "$TOOLS_DIR/yf.py" "$TICKER" fast_info 2>/dev/null || echo '{}')
TA_JSON=$("$PY_BIN" "$TOOLS_DIR/ta.py" "$TICKER" snapshot 2>/dev/null || echo '{}')

PROMPT="L1 CHEAP RE-CHECK of a single ticker. NOT the full pipeline — keep it tight.

Ticker: ${TICKER}    Date: ${DATE}

Live snapshot (already fetched, free):
  fast_info: ${PRICE_JSON}
  ta:        ${TA_JSON}

Previously LOCKED decision (most recent full scan) — re-check whether this still holds:
-----
${LOCKED_TXT:-（no prior final_decision found — treat as fresh quick look）}
-----

DO exactly this, cheaply:
1. Run the market-analyst and news-analyst subagents (via Task tool) for ${TICKER} as of ${DATE}. Optionally sentiment-analyst if news is ambiguous. NO bull/bear debate, NO risk panel, NO portfolio manager.
2. Compare fresh read to the locked thesis. Decide ONE of:
   - THESIS INTACT  (levels still valid, hold the plan)
   - THESIS WEAKENING (some support eroded; tighten stop / trim)
   - THESIS BROKEN  (exit / invalidated — say why)
3. State whether current price has hit/approached the locked entry/stop/T1/T2.

Write the result to ${OUT_DIR}/recheck.md with this shape:
# ${TICKER} L1 re-check — ${DATE}
**Status**: INTACT | WEAKENING | BROKEN
**Price now**: \$X vs locked entry/stop/T1/T2
**What changed**: 2-4 bullets (market + news deltas)
**Action**: hold / tighten stop to \$Y / trim / exit
**Confidence**: low/med/high

Do NOT touch final_decision.md. Headless: no questions, soft-fail tools. Final reply: one line — ${TICKER} STATUS + action."

echo "L1 re-check ${TICKER} (${DATE}) — model=${MODEL}, output ${OUT_DIR}/recheck.md"
claude -p "$PROMPT" \
  --output-format text \
  --permission-mode bypassPermissions \
  --dangerously-skip-permissions \
  --setting-sources user,project,local \
  --add-dir "$ROOT" \
  --model "$MODEL"
RC=$?
echo "recheck exit: $RC"
[[ -s "$OUT_DIR/recheck.md" ]] && { echo "--- recheck.md ---"; cat "$OUT_DIR/recheck.md"; } || echo "(no recheck.md written)"
exit $RC
