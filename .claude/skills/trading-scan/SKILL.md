---
name: trading-scan
description: Run the multi-agent trading research pipeline (fundamentals → market → news → sentiment → bull/bear debate → trader → risk debate → portfolio mgr → sector comparator) over one or more tickers in an AI-related sector. Use when user asks to "scan", "analyze", "evaluate", "research" stocks, or when user names a sector key (semi/power/cooling/reit/oem/security/robotics/materials) or list of tickers.
---

# trading-scan

Orchestrate the TradingAgents-style multi-agent pipeline using Claude Code subagents. No paid API. Data via local yfinance CLI at `pipeline/tools/`.

## Universe

```
SECTORS = {
  "semi":       ["NVDA", "AMD", "AVGO", "MRVL", "TSM", "ASML", "MU", "ARM", "CBRS"],
  "power":      ["VST", "CEG", "TLN", "GEV", "ETN", "PWR", "NEE", "SO"],
  "cooling":    ["VRT", "MOD", "ANET", "COHR", "LITE", "FN", "AAOI", "IPGP", "GLW"],
  "reit":       ["EQIX", "DLR", "IRM", "AMT"],
  "oem":        ["SMCI", "DELL", "HPE", "2317.TW", "2382.TW"],
  "security":   ["CRWD", "PANW", "ZS", "S", "OKTA"],
  "robotics":   ["TSLA", "ISRG", "ABBNY", "FANUY", "SYM", "SPAI"],
  "materials":  ["FCX", "MP", "LIN", "APD", "ALB"],
  "quantum":    ["IONQ", "RGTI", "QBTS", "QUBT", "ARQQ", "LAES", "HON", "IBM"],
  "photonics":  ["POET", "CRDO", "ALAB", "GFS", "INTC"],
  "hedge":      ["GLD", "GDX", "TLT", "MUB", "UUP", "DBC", "BTAL", "SH"],
  # Taiwan-focused supply chain sectors (no duplicates with above)
  "abf":        ["3037.TW", "8046.TW", "3189.TW"],
  "tw_cooling": ["3324.TWO", "8996.TW", "3017.TW"],
  "tw_server":  ["6669.TW", "3231.TW", "2356.TW"],
  "tw_optics":  ["3363.TWO", "4979.TWO", "4977.TW"],
  "tw_power":   ["2308.TW", "1513.TW", "1519.TW"],
  "tw_pkg":     ["3661.TW", "8021.TW", "6438.TW"],
  "tw_photonics": ["3081.TWO", "2455.TW", "4908.TWO"],
}
```

## Taiwan sector composition

| Sector | Theme | Tickers |
|---|---|---|
| `abf` | ABF 載板三雄 (AI CPU/GPU substrate) | 欣興 3037 / 南電 8046 / 景碩 3189 |
| `tw_cooling` | 散熱模組 (TW VRT/MOD analogue) | 雙鴻 3324 / 高力 8996 / 奇鋐 3017 |
| `tw_server` | AI server ODM (補 oem 2317/2382) | 緯穎 6669 / 緯創 3231 / 英業達 2356 |
| `tw_optics` | 光通訊 / CPO 供應鏈 | 上詮 3363 / 華星光 4979 / 眾達-KY 4977 |
| `tw_power` | 電源 / 電網 (TW power) | 台達電 2308 / 中興電 1513 / 華城 1519 |
| `tw_pkg` | 先進封裝 (CoWoS supply chain) | 世芯-KY 3661 / 尖點 8021 / 迅得 6438 |
| `tw_photonics` | 矽光子 / 光元件磊晶 (TW) | 聯亞 3081 / 全新 2455 / 前鼎 4908 |

`photonics` (US 矽光子純玩家): POET / CRDO / ALAB / GFS / INTC — CPO 大廠 AVGO/MRVL/COHR/LITE 已在 semi/cooling, 此族群補未涵蓋的純玩家.

新族群皆 TW listed, 與 SMCI/DELL/HPE 等 US oem 互補. yfinance 用 `.TW` suffix 抓 OTC.

## Daily scan schedule (19 sectors / 7 days)

`daily_scan.sh` runs multiple sectors per day grouped by theme (US + TW supply chain pairs):

| Day | DOW | Sectors | Tickers | Theme |
|---|---|---|---|---|
| Mon | 1 | `semi tw_pkg` | 9 + 3 = 12 | AI core compute + 先進封裝 |
| Tue | 2 | `power tw_power quantum` | 8 + 3 + 8 = 19 | 電力 + TW 電源 + 量子運算 |
| Wed | 3 | `cooling tw_cooling tw_optics` | 9 + 3 + 3 = 15 | 散熱 + 光通訊 |
| Thu | 4 | `oem tw_server abf` | 5 + 3 + 3 = 11 | AI server + ABF 載板 |
| Fri | 5 | `security materials` | 5 + 5 = 10 | 安全 + 原料 |
| Sat | 6 | `hedge reit` | 8 + 4 = 12 | 避險 + 資料中心 REIT |
| Sun | 7 | `robotics photonics tw_photonics` | 7 + 5 + 3 = 15 | 機器人 + 矽光子 (US+TW) |

Total: 約 89 tickers fully covered weekly (含 photonics 5 + tw_photonics 3).

Multi-sector days run sequentially in `daily_scan.sh`; dashboard rebuild + catalyst extract happen once after all sectors finish.
```

## Quantum sector composition

量子運算族群 (Tue, 與 power 同日跑):

| Ticker | 公司 | 技術 / 角色 |
|---|---|---|
| IONQ | IonQ | 離子阱 (trapped ion) 純玩家 |
| RGTI | Rigetti | 超導 (superconducting) |
| QBTS | D-Wave Quantum | 量子退火 (annealing) |
| QUBT | Quantum Computing Inc | 光子 (photonic) |
| ARQQ | Arqit Quantum | 量子加密 (QKD / encryption) |
| LAES | SEALSQ | 後量子半導體 (post-quantum chips) |
| HON | Honeywell | **Quantinuum 母公司** (持股 ~54%) |
| IBM | IBM | 超導量子 + Qiskit 生態 |

注意: **Quantinuum 本身無獨立 ticker** — 私有公司, Honeywell 多數持股, IPO 規劃中尚未上市.
目前以母公司 HON 作代理曝險. Quantinuum 真正掛牌後, 換成其 ticker 並可降 HON 權重.
QMCO (Quantum Corp) 是儲存公司, 非量子運算, 名稱碰撞, 刻意排除.

## Hedge sector composition

The `hedge` sector is intentionally non-AI: gold (GLD/GDX), long Treasuries (TLT),
muni bonds (MUB), USD index (UUP), broad commodities (DBC), market-neutral
anti-beta (BTAL), and short S&P (SH). Use it to balance equity-cluster
correlation when the other sectors are net-long.

## Output language policy

**All subagent markdown outputs are 繁體中文 (Traditional Chinese).** Technical
identifiers (ticker symbols, financial metric names like P/E / EV/EBITDA /
MACD / RSI / ATR / R:R / NAV, regulatory body names like FERC / DOE / SEC,
and section markers like "FINAL TRANSACTION PROPOSAL" / "BULL ROUND N
COMPLETE") stay in English. Narrative, argumentation, table column labels,
and conclusions are in Chinese. No simplified Chinese.

The HTML renderer (`pipeline/tools/render_html.py`) renders the
Chinese markdown into a single self-contained HTML report and links the
glossary at `./HOWTO_READ.html`.

Agent-prompt tweaks for hedge tickers:
- Treat ETF tickers as instruments, not companies. Fundamentals agent reports
  holdings concentration, expense ratio, AUM trend, fund-flow data instead
  of revenue/margin.
- Sentiment agent skips insider/holders (not applicable to ETFs).
- News agent focuses on the underlying macro driver (gold spot, real rates,
  USD strength, VIX, etc).
- Bull/Bear debate is about whether the hedge is appropriately priced for
  the current macro regime, not about company moat.

Args:
- `sector=<key>` — run the named sector
- `tickers=AAA,BBB,CCC` — explicit list (overrides sector)
- `date=YYYY-MM-DD` — analysis as-of date (default: today)
- `rounds=N` — debate rounds (default 1, max 3)
- `mode=<full|plan_all|plan_c5|plan_c3>` — default `plan_all`.
  - `plan_all`  Phase 1 all + **all positive picks** full pipeline (quota-adaptive)
  - `plan_c5`   Phase 1 all + top 5 full pipeline (legacy)
  - `plan_c3`   Phase 1 all + top 3 only (emergency / near-cap)
  - `full`      every ticker through Phase 2-4 (expensive)

## Default mode: plan_all (quota-adaptive)

Standard for any sector scan:

1. Phase 1 (4 Haiku analysts) for **every** ticker in sector universe.
2. Score each ticker after Phase 1 using the **positive-pick criteria** (see below).
3. Check quota: run `python3 pipeline/tools/check_quota.py --pct` → get USAGE_PCT.
   **Important**: `check_quota.py` uses a 7-day rolling window, but billing resets monthly on the 23rd.
   Adjust interpretation:
   - Days 1–10 of billing cycle (23rd–3rd): treat USAGE_PCT thresholds as 2× relaxed (early cycle)
   - Days 11–20 (4th–13th): normal thresholds
   - Days 21–30 (14th–22nd): tighten — multiply USAGE_PCT by 0.7 before comparing thresholds
   In practice: if today is within 3 days of the 23rd and USAGE_PCT > 100%, still treat as "ample budget" (fresh cycle).
4. **Held tickers override** (check BEFORE quota cap):
   - If a prompt or args include `HELD TICKERS: AAA,BBB,...` (from `held_tickers.txt` via `daily_scan.sh`), those tickers **always** receive full Phase 2-4 pipeline regardless of USAGE_PCT or cap.
   - Held tickers are active positions requiring fresh analysis every cycle. Never stub them.
   - Add held tickers to the Phase 2-4 run list first, then apply quota cap to remaining positive picks.
5. Determine cap based on adjusted USAGE_PCT (applies to non-held positive picks):
   - `USAGE_PCT < 60%`  → run Phase 2-4 for **all positive picks** (no cap)
   - `60% ≤ USAGE_PCT < 90%` → cap at **top 5** positive picks
   - `USAGE_PCT ≥ 90%`  → cap at **top 3** only (conserve budget before 23rd reset)
6. Phase 2-4 (Sonnet) on capped pick list. Remaining positive picks get a Phase-1+ stub
   final_decision noting "near-quota skip". Non-positive picks get standard Phase-1-only stub.
7. Phase 5 sector-comparator across all picks with full decisions.

### Positive-pick criteria (Phase 1 scoring)

A ticker is a **positive pick** if it meets ≥ 3 of these 5 signals from Phase 1 reports:

| Signal | Pass condition |
|---|---|
| Fundamentals | Revenue growth >15% YoY AND no FCF collapse (FCF/NI > -1) |
| Market (technical) | RSI14 < 72 AND MACD histogram not deeply negative AND price > MA50 |
| News | Net headline sentiment POSITIVE (bullish macro / catalyst within 30 days) |
| Sentiment | Analyst consensus ≥ 60% BUY OR institutional flow net positive |
| Valuation | Forward P/E < 35x OR significant EPS growth catalyst confirmed |

Tiebreak within cap: rank by (conviction_signals × R:R_estimate). Pick highest ranked.

## Pipeline (per ticker)

Run all 4 Phase-1 analysts **in parallel** via Task tool, then sequential.

```
Phase 1 (parallel fanout via Task):
  Task(fundamentals-analyst, TICKER, DATE)
  Task(market-analyst,       TICKER, DATE)
  Task(news-analyst,         TICKER, DATE)
  Task(sentiment-analyst,    TICKER, DATE)
  → daily/{DATE}/{TICKER}/{fundamentals|market|news|sentiment}.md

Phase 2 (debate loop, max `rounds`):
  for N in 1..rounds:
    Task(bull-researcher, TICKER, DATE, ROUND=N)
    Task(bear-researcher, TICKER, DATE, ROUND=N)
  Task(research-manager, TICKER, DATE)
  → daily/{DATE}/{TICKER}/debate/round_N_{bull,bear}.md
  → daily/{DATE}/{TICKER}/investment_plan.md

Phase 3:
  Task(trader, TICKER, DATE)
  → daily/{DATE}/{TICKER}/trade_proposal.md

Phase 4 (risk debate, parallel then sync):
  parallel Task(risk-aggressive), Task(risk-conservative)
  then  Task(risk-neutral)
  then  Task(portfolio-manager)
  → daily/{DATE}/{TICKER}/risk_debate/{aggressive,conservative,neutral}.md
  → daily/{DATE}/{TICKER}/final_decision.md
```

Across tickers in a sector: run pipelines sequentially per-ticker to avoid yfinance rate-limit. Phase 1 still fans out inside each ticker.

After all tickers done:
```
Phase 5:
  Task(sector-comparator, SECTOR, DATE)
  → daily/{DATE}/{SECTOR}/sector_report.md

Phase 6 (mandatory, always run after Phase 5):
  Bash: python3 pipeline/tools/render_html.py {SECTOR} {DATE} \
    --out daily/{DATE}/{SECTOR}/{SECTOR}_{DATE}.html
  Bash: python3 pipeline/tools/extract_catalysts.py
  Bash: python3 pipeline/tools/build_dashboard.py
  → ./dashboard.html (Top 20 跨族群排行自動刷新)
```

**Top 20 全自動刷新** (mandatory step, do NOT skip):
- `build_dashboard.py` 掃所有 `daily/{DATE}/{TICKER}/final_decision.md` 重算 score
- Score 公式 = verdict_weight × conviction% × (1 + min(R:R_T2, 5) / 5) × phase_modifier
- verdict_weight: BUY=1.0, SELL=0.65, HOLD=0.3, UNKNOWN=0.05
- phase_modifier: Phase-1-only × 0.35 (壓低 stragglers)
- Top 20 表格寫到 dashboard.html 頂部 "🏆 Top 20 綜合排行" 區塊
- **任一 sector 跑完 Phase 5 後必須執行 build_dashboard.py**, 否則跨族群排行不會反映最新結果

## Output tree

```
daily/{DATE}/
  {SECTOR}/
    sector_report.md
  {TICKER}/                  # symlinked or copied into {SECTOR}/
    fundamentals.md
    market.md
    news.md
    sentiment.md
    debate/
      round_1_bull.md
      round_1_bear.md
    investment_plan.md
    trade_proposal.md
    risk_debate/
      aggressive.md
      conservative.md
      neutral.md
    final_decision.md
```

## Orchestrator behavior

1. Parse args. Resolve ticker list from `sector` or explicit `tickers`.
2. Print plan (which tickers, which date, how many phases).
3. For each ticker, run pipeline. On any phase failure, log to `daily/{DATE}/{TICKER}/errors.log` and continue.
4. After all tickers in a sector, run `sector-comparator`.
5. Final summary: print sector ranking table to user (top 3 BUY, any SELL, top contrarian).

## Cost / time estimate

- Phase 1 = 4 subagent calls / ticker (parallel)
- Phase 2 = 2*rounds + 1 calls / ticker
- Phase 3 = 1 call / ticker
- Phase 4 = 4 calls / ticker
- Phase 5 = 1 call / sector
- Total per ticker ≈ 12-14 subagent invocations
- 8-ticker sector ≈ 100 invocations
- Wall clock ≈ 15-40 min per sector on Sonnet 4.6

## Rate limiting

Between tickers: `sleep 3` to be polite to yfinance.

## Date discipline

Always pass `DATE` to each subagent and tell it to treat any data dated after `DATE` as unknown. Default `DATE = $(date +%Y-%m-%d)`.

## When user invokes

If user types something like:
- "scan semi" → run sector=semi
- "analyze NVDA AMD MU" → tickers=NVDA,AMD,MU
- "run trading-scan power" → sector=power

Confirm the ticker list + date with the user before starting (since it spawns many subagents).
