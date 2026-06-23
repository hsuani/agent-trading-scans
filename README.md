# agent-trading-scans

Self-contained, cloud-runnable bundle of the multi-agent **trading-scan**
pipeline plus its daily output archive. Private.

A TradingAgents-style pipeline: per ticker it runs 4 Phase-1 analysts
(fundamentals / market / news / sentiment), a bull/bear debate, a trader
proposal, a risk debate, and a portfolio-manager decision; then a per-sector
comparator and a cross-sector Top-20 dashboard. No paid API — market data via
`yfinance`, reasoning via Claude Code subagents.

## Layout

```
.
├── daily/                      # all per-day scan output lives here
│   └── <YYYY-MM-DD>/           # one dir per day
│       ├── <TICKER>/           # fundamentals.md, market.md, …, final_decision.md
│       └── <sector>/           # sector_report.md + <sector>_<date>.html
├── dashboard.html              # cross-sector Top-20 + per-position tracker
├── _catalysts.json             # consolidated catalyst calendar
├── HOWTO_READ.html, SECTOR_OVERVIEWS.html, daily_briefing.html
├── .claude/
│   ├── skills/trading-scan/    # SKILL.md — the pipeline orchestration spec
│   └── agents/trading/         # 13 subagent definitions (analysts, debaters, …)
└── pipeline/
    └── tools/                  # python helpers + launcher
        ├── render_html.py      # sector md → html
        ├── build_dashboard.py  # rebuild dashboard.html (Top-20)
        ├── extract_catalysts.py# rebuild _catalysts.json
        ├── ta.py / yf.py       # technical-analysis + yfinance CLIs
        ├── daily_scan.sh       # LOCAL launchd launcher (not used in cloud)
        ├── held_tickers.txt    # positions forced to full Phase 2-4
        └── requirements.txt
```

## Path portability

The python helpers resolve the repo root from **`$TRADING_SCANS_ROOT`**, falling
back to the repo root computed relative to the file
(`<repo>/pipeline/tools/X.py` → `parents[2]`). So they work both in the local
checkout and cloned anywhere in the cloud. Set `TRADING_SCANS_ROOT` explicitly
if running from an unusual cwd.

## Run in the cloud (scheduled remote agent)

The remote routine should, in the cloned repo root:

```bash
pip install -r pipeline/tools/requirements.txt
export TRADING_SCANS_ROOT="$PWD"
```

then invoke the **trading-scan** skill (auto-discovered from `.claude/skills/`)
for the day's sector(s), which writes `daily/<date>/<TICKER>/*.md` and
`daily/<date>/<sector>/sector_report.md`; finally:

```bash
python3 pipeline/tools/render_html.py <sector> <date>
python3 pipeline/tools/extract_catalysts.py
python3 pipeline/tools/build_dashboard.py
git add -A && git commit -m "scan <date> <sector>" && git push
```

### Cloud caveats (validate on first test-run)

- **Quota check** (`check_quota.py`) reads local `~/.claude` session logs that do
  not exist in the cloud → treat as no-op and default to `mode=plan_all`.
- **Auth** is the remote agent's own Claude session, not local OAuth.
- **Network** — `yfinance` needs outbound network from the sandbox.

## Run locally

`pipeline/tools/daily_scan.sh` is the launchd launcher (night-window guarded,
caffeinate-held). It calls `claude -p` headlessly per sector. See the script
header for flags (`--date`, `--sector`, `--force`).
