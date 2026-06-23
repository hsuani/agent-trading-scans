# Fundamentals — VST as of 2026-05-15

## Executive summary

Vistra Corp (Texas-based independent power producer, ~44 GW gas/nuclear/coal/solar/storage portfolio, ~5M retail customers) is a high-FCF cash machine that has been re-rated as an "AI power" play, but FY2025 results materially undershot FY2024 — net income fell from $2.66B to $944M and diluted EPS from $7.26 to $2.18 — driven by margin compression, higher D&A and interest expense, and $228M impairments. Balance sheet is highly levered (net debt $19.3B, D/E ~355%, current ratio 0.90) and capex is climbing fast ($2.75B FY25 vs $1.68B FY23) as Vistra finances data-center-aligned generation buildout. Q1'26 was a sharp recovery (net income $1.03B vs Q1'25's ($268M)), so the trailing P/E of 23.8x looks rich while forward P/E of 12.6x prices in a clean re-acceleration.

## Revenue & profitability

- Total revenue: FY22 $13.73B → FY23 $14.78B → FY24 $17.22B → FY25 $17.74B. 3y CAGR ~9.0%. FY25 YoY only +3.0% despite the AI-power narrative.
- Q1'26 revenue $5.64B vs Q1'25 $3.93B = +43.5% YoY (also matches `info.revenueGrowth` 0.434). TTM revenue $19.45B per `info.totalRevenue`.
- Gross margin: FY25 32.9% ($5.83B / $17.74B) vs FY24 43.7% ($7.53B / $17.22B) — significant compression. `info.grossMargins` 0.386 reflects TTM mix.
- Operating margin: FY25 12.0% ($2.13B) vs FY24 23.7% ($4.08B). TTM operating margin 26.6% per info, lifted by Q1'26 ($1.50B op income on $5.64B rev = 26.6%).
- EBITDA: FY25 $5.06B (28.5% margin) vs FY24 $6.96B (40.4% margin). `info.ebitdaMargins` 0.349 TTM.
- Net margin: FY25 5.3% ($944M) vs FY24 15.4% ($2.66B). `info.profitMargins` 0.115 TTM.
- ROE: 42.9% (`info.returnOnEquity`) — flattered by small/leveraged equity base ($5.10B common+pref); tangible book value is negative ($-2.62B).
- ROA: 6.0% — modest given $41.6B asset base.
- Segments (per longBusinessSummary): Retail, Texas, East, West, Asset Closure. Segment-level numbers not surfaced by yfinance.

## Cashflow & balance sheet

- Operating CF: FY22 $485M → FY23 $5.45B → FY24 $4.56B → FY25 $4.07B. TTM OCF $4.67B.
- Capex: $1.30B → $1.68B → $2.08B → $2.75B (FY25), trending up sharply as new-build / nuclear-uprate / battery spending accelerates.
- Free Cash Flow: FY23 $3.78B → FY24 $2.49B → FY25 $1.32B. TTM FCF $477M per info (far below FY-CF reported FCF, reflecting Q1'26 working-cap drag and stepped-up capex). FCF/NI FY25 = 1.40 (healthy at NI level), but capex absorbing the bulk.
- FCF margin FY25: 7.4% of revenue.
- Balance sheet (FY25):
  - Cash & equiv $785M; restricted cash $1.61B; total cash per info $658M
  - Total debt $20.07B (LT $15.84B, current $4.23B incl $1.23B revolver + $3.00B other current borrowings)
  - Net debt $19.28B (vs $15.86B end-FY24, +21.6%)
  - Stockholders' equity $5.10B (incl $2.48B preferred). Common equity only $2.62B.
  - Net debt / EBITDA FY25: 3.81x (rising — was 2.28x end-FY24).
  - Current ratio 0.78 ($9.18B / $11.81B) FY25 BS; `info.currentRatio` 0.896 TTM. Quick ratio 0.26.
  - Working capital -$2.64B (negative).
  - Goodwill+intangibles $5.25B → tangible book value -$2.62B.

## Capital allocation & insider signal

- Buybacks: $1.95B (FY22) → $1.25B → $1.27B → $1.03B (FY25). Treasury stock grew from $3.40B to $6.93B. Share count fell from 389.8M (FY22 diluted) to 345.7M (FY25 diluted).
- Dividend: $0.92/yr (`info.dividendRate`), yield 0.65%, payout ratio 15.2%. Common dividends paid $306M FY25; preferred dividends $192M FY25 (8% perpetual pref).
- Debt issuance: heavy — $6.02B issued FY25 vs $3.82B repaid, net +$2.20B. Funding capex + buybacks + M&A ($1.14B business purchase FY25, $3.07B FY24 — likely Energy Harbor / nuclear assets).
- Capex coverage: FY25 OCF $4.07B vs capex $2.75B + dividends $498M = $3.25B; small surplus, gap covered by debt.
- Insider activity last 6mo (cutoff 2025-11-15 to 2026-05-15): 21 transactions. Open-market buys: $0. Sales: ~$10.2M / 62.7k shares. Trivial vs $47.8B market cap (0.02%). Mix of Form 4 grants + small option exercises + sale by GC. Overall: net selling, but immaterial magnitude.
- 15-mo lookback (back to Jun 2024): total reported sales ~$346M — larger but still <1% of mkt cap; insider holdings only 0.80% per info.

## Valuation

- Price $141.90 (`info.currentPrice`). 52w range $138.53–$219.82; -9.4% over 52w vs S&P +25.9%. Down ~35% from all-time high.
- Market cap $47.85B; enterprise value $69.60B.
- Trailing P/E 23.77 (TTM EPS $5.97). Forward P/E 12.57 (forward EPS $11.29 — implies street expects EPS to nearly double).
- EV/Revenue 3.58x; EV/EBITDA 10.25x (`info.enterpriseToEbitda`).
- P/S TTM 2.46; P/B 18.30 (book value $7.75/sh, weighed down by treasury + negative tangible equity).
- PEG 1.21. P/FCF on TTM info FCF $477M ≈ 100x (distorted by capex spike); on FY25 FCF $1.32B ≈ 36x.
- Sector context (Utilities IPP — TLN, CEG comparable): IPP/AI-power peers typically trade EV/EBITDA 12–18x and forward P/E 18–28x post-AI-data-center re-rating. VST at 10.3x EV/EBITDA and 12.6x fwd P/E screens cheap vs that cohort — but only if forward EPS materializes.
- Analyst targets: mean $225.06, median $227.00, high $320, low $97. Recommendation mean 1.37 (strong_buy). Implies ~59% upside to mean target.

## Key catalysts

- Q1'26 already printed (period end 2026-03-31): $1.03B NI, $2.87 diluted EPS, $5.64B revenue — strong YoY rebound. This is reflected in TTM info data.
- Next earnings: not available via yfinance call (lxml error on earnings_dates). Q2'26 print historically lands early August.
- Capex ramp: $2.75B FY25, set to continue rising — every incremental gas/nuclear/battery dollar matters for data-center power contracts (hyperscaler PPAs).
- Net debt trajectory: $19.3B and growing; refinancing/rates exposure. $4.23B in current debt due within 12 months including a $1.23B revolver draw.
- Capital returns: buyback authorization continues but pace slowing ($1.95B → $1.03B).
- Holder concentration: 91.6% institutional. Blackrock 8.45%, Vanguard funds 11.4% combined, FMR 5.04%, State Street 4.89%. Short interest 12.5M shares (3.7% of SO, 4.3% of float, +33.6% MoM — short interest building).

## Metrics table

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| Revenue (TTM) | $19.45B | +43% (Q1'26 YoY) / +3% FY25 | n/a | Strong on Q1 |
| Gross margin (FY25) | 32.9% | -10.8pp | ~20–35% IPP | OK, compressed |
| Operating margin (TTM) | 26.6% | -- | ~15–25% | Good |
| EBITDA margin (TTM) | 34.9% | down vs FY24 40.4% | ~25–35% | In range |
| Net margin (TTM) | 11.5% | down vs FY24 15.4% | ~8–12% | OK |
| ROE | 42.9% | -- | ~10–15% utilities | Inflated by leverage |
| ROA | 6.0% | -- | ~3–5% utilities | Good |
| FCF (FY25) | $1.32B | -47% YoY | -- | Falling on capex |
| FCF / NI (FY25) | 1.40 | -- | >0.9 healthy | Healthy |
| Net debt / EBITDA (FY25) | 3.81x | up from 2.28x | <3.5x preferred | Stretched |
| Current ratio | 0.90 | down | >1.0 healthy | Weak |
| Debt / Equity | 3.55 (355%) | up | ~1.0–2.0 utilities | Very high |
| Trailing P/E | 23.77 | -- | ~18–22 utilities | Slight premium |
| Forward P/E | 12.57 | -- | ~16–20 | Cheap if EPS hits |
| EV/EBITDA | 10.25 | -- | ~10–14 IPP | Reasonable |
| P/B | 18.30 | -- | ~2–3 utilities | Very high (treasury distortion) |
| Div yield | 0.65% | -- | ~3–4% utilities | Below sector |
| Payout ratio | 15.2% | -- | ~50–70% utilities | Very low |
| Insider net activity (6mo) | -$10.2M | -- | -- | Mild net selling |
| Inst. ownership | 91.6% | -- | ~70–85% | Very concentrated |

## Red flags

- Net debt up 21.6% YoY to $19.28B; net debt/EBITDA at 3.81x and rising; D/E 355%; tangible book value negative ($-2.62B).
- Current ratio 0.78 on FY25 balance sheet — short-term liquidity tight; $4.23B current debt incl $1.23B revolver and $3.00B other current borrowings rolling within 12 months.
- FY25 net income halved YoY ($944M vs $2.66B) and gross margin contracted ~11pp. Trailing fundamentals are noticeably weaker than the "AI power" narrative implies; bull case rests on the Q1'26 snapback continuing.
- FCF down 47% YoY (FY25) as capex accelerates; capex now consumes 68% of operating cash flow.
- Heavy reliance on debt issuance ($6.02B FY25) to fund growth + buybacks; rate-sensitive refinancing risk.
- $228M of FY25 impairments and -$175M total unusual items signal asset/portfolio cleanup in motion.
- Short interest rising sharply (+33.6% MoM); 12.5M shares short, 4.3% of float.
- Stock down 9.4% over 52w vs S&P +25.9%; 50d MA ($156.83) and 200d MA ($176.04) both above spot ($141.90) — technical bear setup, even though analysts have 1.37 strong_buy.
- yfinance `earnings_dates` call failed (lxml import error in env) — next earnings date not verifiable from this tool.
- Stock-holder rights risk flagged at 5/10 by yfinance governance score; otherwise governance reasonable.

FUNDAMENTALS REPORT COMPLETE
