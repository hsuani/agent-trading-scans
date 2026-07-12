#!/bin/bash
#
# Daily trading-scan routine. Designed for launchd / cron.
#
# Flow:
#   1. Pre-flight quota check (~/.claude/tools/trading/check_quota.py)
#        - if usage >= 50% of weekly budget: desktop alert + exit 1
#   2. Pick sector based on day-of-week (or --sector arg)
#   3. Invoke headless `claude -p` to run the trading-scan pipeline
#        - silent on stdout; logs go to ~/.claude/tools/trading/logs/{date}/
#   4. Render HTML via render_html.py
#   5. Desktop notification with file:// link to HTML
#
# Usage:
#   daily_scan.sh                    # picks sector from day-of-week
#   daily_scan.sh --sector power     # explicit sector
#   daily_scan.sh --sector power --force  # skip quota check
#   daily_scan.sh --dry-run          # show plan but don't execute
#
# Env overrides:
#   TRADING_SCAN_BUDGET        # full weekly subagent-call budget (default 600)
#   TRADING_SCAN_ALERT_PCT     # alert threshold % (default 50)
#   TRADING_SCAN_LOOKBACK      # lookback days (default 7)
#   TRADING_SCAN_DISABLE       # set to 1 to make this script a no-op

set -uo pipefail

# Hold the Mac awake for the whole run. launchd fires this at 01:26, right
# after the 01:25 pmset wake; without this the system idle-sleeps in ~90s and
# the long claude -p scan dies mid-flight. -w $$ ties caffeinate's lifetime to
# this script's PID. Harmless if caffeinate is absent (macOS always ships it).
command -v caffeinate >/dev/null 2>&1 && caffeinate -i -m -s -w "$$" &

# Headless `claude -p` otherwise terminates background tasks after 600s — which
# kills a trading-scan Workflow mid-run (leaving no final_decision/sector_report).
# 0 = wait indefinitely for the pipeline's subagents/workflow to finish.
export CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS=0

TOOL_DIR="$HOME/.claude/tools/trading"
PY="$TOOL_DIR/venv/bin/python"
LOG_ROOT="$TOOL_DIR/logs"
SCAN_ROOT="$HOME/Study/scans"

# Mon Tue Wed Thu Fri Sat Sun (date +%u → 1..7)
# Multi-sector per day. Space-separated list per slot; loop runs each in sequence.
# 16 sectors covered across 7 days, grouped by theme (US + TW supply chain pairs).
declare -a DAY_SECTORS=(
  ""                                # padding for index 0
  "semi tw_pkg serenity"            # Mon: AI core compute (US + TW packaging) + Serenity picks (dynamic)
  "power tw_power quantum"          # Tue: Power infrastructure (US + TW grid/PSU) + quantum computing (incl. HON=Quantinuum proxy)
  "cooling tw_cooling"              # Wed: Thermal (US + TW) — tw_optics merged into tw_photonics (Sun)
  "oem tw_server abf"               # Thu: AI server build (US + TW ODM + ABF substrate)
  "security materials robotics"     # Fri: Security + raw materials + robotics (moved off Sun to make room for photonics)
  "hedge reit tw_probe"             # Sat: Defensive (hedge 4 + REIT) + 探針測試 (TW probe-card/test, freest day after hedge trim)
  "photonics tw_photonics"          # Sun: Silicon photonics day (US POET/CRDO/ALAB/GFS/INTC + TW 上中下游+檢測 10 檔)
)

SECTOR=""
DRY_RUN=0
FORCE=0
DATE_OVERRIDE=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --sector) SECTOR="$2"; shift 2;;
    --date) DATE_OVERRIDE="$2"; shift 2;;   # backfill a past date: YYYY-MM-DD
    --dry-run) DRY_RUN=1; shift;;
    --force) FORCE=1; shift;;
    -h|--help)
      grep -E '^#' "$0" | sed 's/^# \?//' | head -40
      exit 0;;
    *) echo "unknown arg: $1" >&2; exit 2;;
  esac
done

if [[ "${TRADING_SCAN_DISABLE:-0}" == "1" ]]; then
  echo "TRADING_SCAN_DISABLE=1, skipping"
  exit 0
fi

# Night-window guard. launchd runs MISSED StartCalendarInterval jobs on the next
# wake — if the Mac slept through the overnight slot, that catch-up fires during
# the day, eats interactive usage, and collides with the work-hours session
# limit (observed 2026-06-12: ran 16:26, hit "session limit · resets 8pm").
# So refuse to run outside the night window. Catch-up still fires but exits here
# cheaply (no claude -p). Window wraps midnight: [NIGHT_START,24) ∪ [0,NIGHT_END).
# Override via env; --force / --dry-run bypass.
NIGHT_START="${TRADING_SCAN_NIGHT_START:-22}"   # 22:00 inclusive
NIGHT_END="${TRADING_SCAN_NIGHT_END:-7}"        # 07:00 exclusive
HOUR=$((10#$(date +%H)))                         # base-10, no octal trap on 08/09
in_window=0
if (( NIGHT_START <= NIGHT_END )); then
  (( HOUR >= NIGHT_START && HOUR < NIGHT_END )) && in_window=1
else
  (( HOUR >= NIGHT_START || HOUR < NIGHT_END )) && in_window=1
fi
if [[ "$FORCE" != "1" && "$DRY_RUN" != "1" && "$in_window" != "1" ]]; then
  echo "outside night window (${NIGHT_START}:00–${NIGHT_END}:00, hour=$HOUR) — skip to avoid daytime usage. --force to override."
  exit 0
fi

if [[ -n "$DATE_OVERRIDE" ]]; then
  DATE="$DATE_OVERRIDE"
  # macOS BSD date: derive DOW (1..7) from the overridden date.
  DOW=$(date -j -f "%Y-%m-%d" "$DATE" +%u 2>/dev/null) || { echo "bad --date: $DATE (need YYYY-MM-DD)" >&2; exit 2; }
else
  DATE=$(date +%Y-%m-%d)
  DOW=$(date +%u)
fi

if [[ -z "$SECTOR" ]]; then
  SECTOR="${DAY_SECTORS[$DOW]}"
fi

if [[ -z "$SECTOR" ]]; then
  echo "no sector for day-of-week $DOW"
  exit 0
fi

# Split space-separated SECTOR list into array; supports multi-sector days.
read -r -a SECTOR_LIST <<< "$SECTOR"

LOG_DIR="$LOG_ROOT/$DATE"
mkdir -p "$LOG_DIR"

SCAN_MODE="plan_all"
OVERALL_RC=0
HTML_LIST=()

# Sync held_tickers.txt from the dashboard's exported holdings, if present.
# Dashboard "📤 匯出持倉" button downloads held_export.txt to ~/Downloads (browser
# file:// can't pick the dir). Pull it into scans/ first (newest wins), THEN
# merge — sync_held reads from scans/, so the file must be relocated before the
# sync. Order is mv -> sync, not the reverse. All best-effort.
DL_EXPORT="$HOME/Downloads/held_export.txt"
HELD_EXPORT="$SCAN_ROOT/held_export.txt"
if [[ "$DRY_RUN" != "1" && -f "$DL_EXPORT" ]]; then
  mv -f "$DL_EXPORT" "$HELD_EXPORT" \
    && echo "moved $DL_EXPORT -> $HELD_EXPORT" >> "$LOG_DIR/_post.log"
fi
if [[ "$DRY_RUN" != "1" && -f "$HELD_EXPORT" ]]; then
  echo "syncing held_tickers from $HELD_EXPORT ..." >> "$LOG_DIR/_post.log"
  "$PY" "$TOOL_DIR/sync_held.py" --export "$HELD_EXPORT" >> "$LOG_DIR/_post.log" 2>&1 || true
fi

# Load held tickers — these always get full Phase 2-4 regardless of quota cap
HELD_TICKERS_FILE="$TOOL_DIR/held_tickers.txt"
HELD_TICKERS=""
if [[ -f "$HELD_TICKERS_FILE" ]]; then
  # Strip comments and blank lines, join with comma
  HELD_TICKERS=$(grep -v '^\s*#' "$HELD_TICKERS_FILE" | grep -v '^\s*$' | tr '\n' ',' | sed 's/,$//')
fi

for SECTOR in "${SECTOR_LIST[@]}"; do
  RUN_LOG="$LOG_DIR/${SECTOR}_run.log"
  CLAUDE_LOG="$LOG_DIR/${SECTOR}_claude.log"
  HTML_OUT="$SCAN_ROOT/daily/$DATE/${SECTOR}/${SECTOR}_${DATE}.html"

  # serenity is a DYNAMIC sector — its universe is Serenity's current picks in
  # serenity/universe.txt (refreshed by serenity.py). Refresh + resolve now.
  SECTOR_TICKERS_ARG=""
  SECTOR_FORCE_FULL=""
  if [[ "$SECTOR" == "serenity" ]]; then
    "$PY" "$TOOL_DIR/serenity.py" >> "$RUN_LOG" 2>&1 || true
    SECTOR_TICKERS_ARG=$(grep -vE '^\s*#|^\s*$' "$SCAN_ROOT/serenity/universe.txt" 2>/dev/null | tr '\n' ',' | sed 's/,$//')
    # his high-conviction picks (mention>=threshold) force full Phase 2-4
    SECTOR_FORCE_FULL=$(grep -vE '^\s*#|^\s*$' "$SCAN_ROOT/serenity/force_full.txt" 2>/dev/null | tr '\n' ',' | sed 's/,$//')
    if [[ -z "$SECTOR_TICKERS_ARG" ]]; then
      echo "serenity universe empty — skip" >> "$RUN_LOG"; continue
    fi
  fi

  # Idempotency: if today's sector report already rendered, skip. Lets the
  # 07:35 fallback launchd slot be a no-op when the 01:26 run succeeded.
  # --force bypasses (re-run on demand).
  if [[ "$FORCE" != "1" && -s "$HTML_OUT" ]]; then
    echo "skip ${SECTOR}: $HTML_OUT already exists ($(date))" >> "$RUN_LOG"
    HTML_LIST+=("$HTML_OUT")
    continue
  fi

  {
    echo "===== daily_scan $DATE (DOW=$DOW) sector=$SECTOR ====="
    echo "start: $(date)"
  } >> "$RUN_LOG"

  # Quota check (informational only)
  echo "quota state (informational)..." >> "$RUN_LOG"
  "$PY" "$TOOL_DIR/check_quota.py" --quiet >> "$RUN_LOG" 2>&1 || true
  echo "SCAN_MODE=$SCAN_MODE (ignore-quota default)" >> "$RUN_LOG"

  # Dry-run short-circuit
  if [[ "$DRY_RUN" == "1" ]]; then
    echo "DRY RUN — would scan $SECTOR for $DATE" | tee -a "$RUN_LOG"
    continue
  fi

  # Headless Claude invocation
  # For serenity, pass the explicit dynamic ticker list; else scan by sector name.
  SECTOR_SPEC="sector=${SECTOR}"
  [[ -n "$SECTOR_TICKERS_ARG" ]] && SECTOR_SPEC="sector=${SECTOR} tickers=${SECTOR_TICKERS_ARG}"
  PROMPT="Run the \`trading-scan\` skill (via Skill tool) for ${SECTOR_SPEC}
date=${DATE} rounds=1 mode=${SCAN_MODE}. The skill is defined in
~/.claude/skills/trading-scan/SKILL.md and orchestrates 12+ subagents per
ticker.

Operating mode: HEADLESS / SILENT.

Required behaviour:
1. Invoke the trading-scan skill immediately.
2. Use the full sector universe from the skill (no truncation, no asking).
3. **Mode: ${SCAN_MODE}** (current default, ignores quota)
   - mode=plan_c5: Phase 1 (4 Haiku analysts) for ALL tickers, then
     identify TOP 3-5 picks based on Phase 1 signals. Run Phase 2-4
     (Sonnet/Opus) ONLY for those picks. Other tickers stop after Phase 1.
     Phase 5 sector-comparator notes which tickers got full pipeline.
4. After all eligible tickers complete: run Phase 5 (sector-comparator).
5. Each phase output writes to /Users/yht/Study/scans/daily/${DATE}/{TICKER}/*.md
   and /Users/yht/Study/scans/daily/${DATE}/${SECTOR}/sector_report.md.
6. Do NOT pause for confirmation. Treat tool failures as soft (log+continue).
7. No mid-run status reports. Final reply: one-line summary.

Sector=${SECTOR}, Date=${DATE}, Mode=${SCAN_MODE}.

HELD TICKERS (已持倉 / 掛單中): ${HELD_TICKERS:-（none）}
Rule: any ticker in the HELD TICKERS list that appears in today's sector universe MUST receive full Phase 2-4 pipeline regardless of quota cap or mode cap. Do not stub them out. They are active positions requiring fresh analysis every scan cycle.

FORCE FULL (Serenity 高信念 picks): ${SECTOR_FORCE_FULL:-（none）}
Rule: same as HELD — every ticker in this FORCE FULL list MUST receive complete Phase 2-4 pipeline (bull/bear debate, trader, risk debate, portfolio manager) EVEN IF its Phase-1 positive-signal score is below the normal threshold. These are Serenity's most-repeated conviction calls; we want our own full read on them regardless of the Phase-1 screen. Do not stub them as Phase-1-only.

Begin."

  echo "invoking claude -p for ${SECTOR}..." >> "$RUN_LOG"
  claude -p "$PROMPT" \
    --output-format text \
    --permission-mode bypassPermissions \
    --dangerously-skip-permissions \
    --setting-sources user,project,local \
    --add-dir /Users/yht/Study \
    --add-dir /Users/yht/.claude/tools/trading \
    --model sonnet \
    > "$CLAUDE_LOG" 2>&1
  CLAUDE_RC=$?
  echo "claude exit: $CLAUDE_RC" >> "$RUN_LOG"

  if [[ "$CLAUDE_RC" != "0" ]]; then
    osascript -e "display notification \"${SECTOR} scan failed (rc=$CLAUDE_RC). See log.\" with title \"Trading scan error\" sound name \"Basso\""
    OVERALL_RC="$CLAUDE_RC"
    continue   # don't render HTML for failed scan, but try next sector
  fi

  # Render per-sector HTML
  echo "rendering HTML for ${SECTOR}..." >> "$RUN_LOG"
  "$PY" "$TOOL_DIR/render_html.py" "$SECTOR" "$DATE" --out "$HTML_OUT" >> "$RUN_LOG" 2>&1
  RENDER_RC=$?
  if [[ "$RENDER_RC" != "0" ]]; then
    echo "render failed (rc=$RENDER_RC)" >> "$RUN_LOG"
    osascript -e "display notification \"HTML render failed for ${SECTOR}.\" with title \"Trading scan error\" sound name \"Basso\""
    OVERALL_RC="$RENDER_RC"
  else
    HTML_LIST+=("$HTML_OUT")
  fi

  {
    echo "done: $(date)"
    echo "html: $HTML_OUT"
    echo "===== end ($SECTOR) ====="
  } >> "$RUN_LOG"
done

# ---- After-all: refresh catalyst calendar + dashboard once ----
if [[ "$DRY_RUN" != "1" ]]; then
  GLOBAL_LOG="$LOG_DIR/_post.log"
  echo "refreshing catalyst calendar..." >> "$GLOBAL_LOG"
  "$PY" "$TOOL_DIR/extract_catalysts.py" >> "$GLOBAL_LOG" 2>&1 || true

  if [[ -f "$TOOL_DIR/build_dashboard.py" ]]; then
    echo "rebuilding dashboard..." >> "$GLOBAL_LOG"
    "$PY" "$TOOL_DIR/build_dashboard.py" >> "$GLOBAL_LOG" 2>&1 || true
  fi

  # Summary notification
  SECTOR_SUMMARY=$(printf "%s " "${SECTOR_LIST[@]}")
  osascript -e "display notification \"Sectors: ${SECTOR_SUMMARY}— ${#HTML_LIST[@]} reports built.\" with title \"Trading scan ($DATE)\" sound name \"Glass\""

  # Auto-open first HTML if interactive
  if [[ -t 1 && -n "${HTML_LIST[0]:-}" ]]; then
    open "${HTML_LIST[0]}" 2>/dev/null
  fi
fi

exit "$OVERALL_RC"
