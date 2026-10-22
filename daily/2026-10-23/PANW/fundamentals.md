# Fundamentals — PANW as of 2026-10-23

## Executive summary
Palo Alto Networks (PANW) 的現金流仍強（FY26 FCF $4.11B、FCF margin 35.8%、淨現金約 $0.57B），但 FY26 收購擴張後 GAAP 獲利急遽惡化（diluted EPS $0.40 vs FY25 $1.60，ROE 僅 1.7%），且股本稀釋約 22%、商譽占總資產近 60%。估值極度昂貴：forward P/E 71.2x、TTM 調整後 P/E 約 90.7x、P/S 24.7x，財務體質穩健但估值吸引力低。基本面結論為「現金流與營收動能強、獲利品質與估值為主要風險」，不含交易建議。

資料說明：價格為 yfinance fast_info 快取（2026-10-22 11:36 UTC，last_price $347.25），早於 as-of 日 2026-10-23，非 10-23 收盤價。財報為 FY26（FYE 2026-07-31）年度與季度資料，無 post-date 財報。

## Revenue & profitability
單位：USD（B = 十億美元，M = 百萬美元）。FY 為 7 月底結束的財政年度。

- **營收成長**：FY23 $6.89B → FY24 $8.03B → FY25 $9.22B → FY26 $11.48B。YoY：FY24 +16.5%、FY25 +14.9%、FY26 +24.5%。3 年 CAGR（FY23–FY26）約 18.5%。
- **最新季**：FQ4 FY26（2026-07 季）營收 $3.41B，YoY +34.5%（對比 FQ4 FY25 $2.536B）。yfinance `revenueGrowth` 0.345 即為此季 YoY，並非全年數字。FY26 季度營收序列：FQ1 $2.474B、FQ2 $2.594B、FQ3 $3.002B、FQ4 $3.410B（合計 $11.48B，與年度數字吻合）。
- **成長動能註記**：FY26 營收與資產負債表（商譽由 FY25 年底 $4.57B 增至 FY26 年底 $22.01B，股數由 667.9M 增至 815.0M）顯示有大型收購併入。資料未載明標的與營收貢獻比例，故 YoY 中有多少為併購貢獻無法量化（n/a）。
- **分部營收**：yfinance 不提供分部拆分（n/a）。業務摘要顯示產品線涵蓋 Prisma Access、Cortex（XSIAM/XDR/XSOAR/Xpanse）、Unit 42、VM/CN-Series 等，但無金額。
- **毛利率**：FY23 72.3% → FY24 74.3% → FY25 73.4% → FY26 70.4%（Gross Profit $8.08B / Revenue $11.48B）。FY26 Cost of Revenue $3.40B，YoY +38.9%，快於營收成長。
- **營業利益率**：FY23 5.6%、FY24 8.5%、FY25 13.5%、FY26 6.1%（Operating Income $0.695B vs FY25 $1.243B，YoY -44.1%）。
- **淨利率**：FY24 32.1%（含大額稅務利益，Tax Provision -$1.59B）、FY25 12.3%、FY26 2.7%（Net Income $0.307B）。
- **EPS**：FY26 diluted EPS $0.40（FY25 $1.60，-75%）。FY26 diluted 平均股數 764M（FY25 709M，+7.8%）。
- **季度 GAAP 虧損**：FQ3 FY26 淨損 -$0.177B（EPS -0.22），FQ4 FY26 淨損 -$0.282B（EPS -0.35）。FQ4 Operating Income 為 +$0.172B，但 Other Non-Operating 項目 -$0.530B 使稅前由正轉負（-$0.269B）。
- **ROE / ROIC**：ROE（平均權益）FY26 1.7%（yfinance returnOnEquity 0.0174），FY25 17.5%。ROIC 為估計值（NOPAT = Operating Income × (1 − 稅率)，稅率取 yfinance Tax Rate For Calcs 0.40）：FY26 約 2.2%，FY25 約 12.7%，FY24 約 10.3%。

## Cashflow & balance sheet
單位：USD B。

- **營運現金流**：FY23 $2.78B → FY24 $3.26B → FY25 $3.72B → FY26 $4.55B（YoY +22.5%）。
- **自由現金流（OCF − Capex）**：FY23 $2.63B → FY24 $3.10B → FY25 $3.47B → FY26 $4.11B（YoY +18.6%）。FCF margin：FY23 38.2%、FY24 38.6%、FY25 37.6%、FY26 35.8%。
- **FCF / NI**：FY26 13.4x（NI $0.307B 受收購相關費用與非營業損失壓低，比率失真，不宜作為品質指標）；FY25 3.06x；FY24 1.20x；FY23 5.98x。以 FCF 扣除 SBC 計算，FY26 為 $2.34B（margin 20.4%），此數字較能反映真實現金創造能力。
- **SBC**：FY26 $1.77B（YoY +37.0%），占營收 15.5%（FY25 14.0%）。SBC 占 FCF 比重約 43%。
- **Capex**：FY26 $0.44B（YoY +78%），占營收 3.8%，仍屬輕資產模式。
- **資產負債表（FY26 年底，2026-07-31）**：
  - 現金及短期投資 $3.07B（現金 $2.51B + 其他短期投資 $0.56B）
  - 總負債（債務）$2.50B（長期債務 $1.77B + 資本租賃 $0.73B；流動債務為 0）。yfinance info 顯示 totalDebt $2.567B，與 BS 有 $0.07B 差異，以 BS 為準。
  - 淨現金約 $0.57B（derived：$3.07B − $2.50B）；FY25 年底淨現金約 $2.57B（derived），淨現金大幅縮減源於收購與新增債務。
  - 流動比率 0.87（FY25 0.94），速動比率 0.735（info）。SaaS 模式下大量遞延收入使流動比率偏低屬常態。
  - Debt/Equity 0.09（FY25 0.04）。
  - 股東權益 $27.49B（FY25 $7.82B，主要來自發行股票支付收購）。
  - 商譽 $22.01B、無形資產 $7.02B，合計 $29.03B，占總資產 $48.46B 的 59.9%。Tangible Book Value 為 -$1.54B。
  - 遞延收入（current + non-current）合計 $14.76B，YoY +15.7%；current deferred revenue $7.75B，YoY +22.9%，屬正向先行指標。
  - 應收帳款 $3.63B，YoY +22.4%。

## Capital allocation & insider signal

**資本配置**
- **股利**：無（dividendYield 0）。
- **回購**：FY26 回購 $1.00B（FY25 為 0，FY24 $0.57B，FY23 $0.27B）。回購規模小於 SBC（$1.77B），且 FY26 年底股數 815.0M 較 FY25 年底 667.9M 增加 22.0%（主要為收購增發），淨股本仍在擴張。
- **收購**：FY26 併購現金支出 $4.66B（FY25 $1.05B）；另有股票支付部分。
- **債務**：FY26 償還 $0.16B（FY25 $0.97B、FY24 $1.03B）；FY26 年底長期債務 $1.77B 高於 FY25 的 $1.19B。現金流量表 FY26 債務發行僅 $0.01B，故新增負債多半為併購承接（推測）。
- **股利覆蓋率**：不適用（無股利）。

**內部人交易（2026-04-23 至 2026-10-23，6 個月）**
- 共 19 筆賣出，合計 $47.9M（155,199 股）；**零筆公開市場買入**。另有 1 筆 Stock Award 授予（7,211 股）。
- 主要賣方：Lee Klarich（CPO/CTO）$16.3M、James Joseph Goetz $13.1M、Dipak Golechha（CFO）$12.2M、John Phillip Key $3.0M、Joshua Paul $1.5M、Aparna Bawa $1.5M、Helle Thorning-Schmidt $0.2M。
- 規模：$47.9M ÷ 市值 $284.05B ≈ 0.017%，對估值衝擊極小，但 0 買入、全數為賣出，方向偏負面。
- 長期脈絡：2024-11 起至今，CEO Nikesh Arora 累計賣出約 $738M（yfinance 資料；6 個月窗口內無 Arora 交易）；Klarich 累計約 $351M、Nir Zuk 累計約 $248M。
- 機構持股 84.1%（3,920 家），內部人持股 0.75%。
- 放空：Short interest 21.6M 股，占流通股 2.66%，days to cover 3.1。
- 大股東（2026-06-30）：BlackRock 75.8M 股（約 9.3% 已發行股數，derived）、Vanguard Capital 53.1M 股（約 6.5%）、State Street 37.0M 股（約 4.5%）。yfinance 的 pctHeld 欄位數值失真，本報告未採用。

## Valuation
單位：USD B；價格 $347.25（快取 2026-10-22）；市值 $284.05B；EV $283.55B。

- **Trailing P/E（GAAP）**：868x（n/m，受 FY26 低 GAAP 獲利影響，不具比較意義）。
- **TTM 調整後 P/E**：約 90.7x（以 yfinance earnings_dates 最近四季 reported EPS 合計 $3.83：FQ1 $0.93、FQ2 $1.03、FQ3 $0.85、FQ4 $1.02 計算，為 derived）。
- **Forward P/E**：71.2x（yfinance forwardEps $4.88）。yfinance epsCurrentYear $4.19 對應 P/E 82.9x；兩者定義不同，yfinance 未說明，此處以 forwardEps 為主。
- **EV/EBITDA**：181.8x（yfinance enterpriseToEbitda，EBITDA $1.56B）；以財報 EBITDA $1.39B 計算約 203.8x。
- **P/S（TTM）**：24.7x。
- **P/FCF（TTM，FCF $4.11B）**：69.1x。
- **P/B**：10.3x（yfinance priceToBook 10.29）。
- **PEG**：1.74（yfinance pegRatio）。
- **同業估計中位數**（非 yfinance 資料，為粗估，僅供參考）：大型雲端安全 / 基礎軟體 forward P/E 約 35–45x，EV/Revenue 約 10–14x，P/FCF 約 30–40x。
- **分析師共識**：50 位，recommendationMean 1.69（Buy 區間）；目標價平均 $398.52（較現價 +14.8%）、中位數 $415（+19.5%）、最高 $525、最低 $190。
- **價格位置**：52 週區間 $139.57–$432.33；現價較歷史高點 $432.33 低 19.7%，低於 50 日均線 $371.30（-6.5%），高於 200 日均線 $263.12（+32.0%）。Beta 0.933。

## Key catalysts
- **下一次財報**：2026-11-19（yfinance 標示為估計日期，isEarningsDateEstimate = true）。一致預期 EPS $0.97，對比去年同季實際 $0.93，YoY 約 +4.3%。
- **最近一次財報**：2026-09-01（FQ4 FY26），調整後 EPS $1.02，高於一致預期 $0.98（+4.35%）。資料中所有已公布季度 EPS 皆高於預期（資料期間 2020-11 起）。
- **EPS 成長催化**：forwardEps $4.88 相對 FY26 調整後合計 $3.83 隱含約 +27% 成長，但 yfinance 未說明此 forward 數字的期間定義，需與公司指引核對。
- **指引**：yfinance 未提供正式 guidance（n/a）。
- **營運催化**：遞延收入 +15.7%、current deferred +22.9%、AR +22.4%，為未來營收能見度的正向指標；但需觀察收購後整合成效與毛利率能否回穩。
- **分部轉變**：分部資料 n/a。

## Metrics table
單位：營收、利潤、現金流、市值、EV 以 USD B 或 USD M 計；比率以 % 或 x 計。Sector median 欄位為估計值，非資料來源。

| Metric | Latest (FY26 除非註明) | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| Revenue (USD B) | 11.48 | +24.5% | 約 +12–15% 成長 | 強（含併購） |
| Quarterly revenue FQ4 (USD B) | 3.41 | +34.5% | — | 強 |
| Gross margin | 70.4% | -3.0 pts（FY25 73.4%） | 約 75–80% | 偏弱，下滑 |
| Operating margin | 6.1% | -7.4 pts（FY25 13.5%） | 約 15–20% | 弱 |
| Net margin | 2.7% | -9.6 pts（FY25 12.3%） | 約 10–15% | 弱 |
| Diluted EPS (USD) | 0.40 | -75%（FY25 1.60） | — | 弱（GAAP） |
| Adj. EPS TTM (USD) | 3.83 | — | — | 合理 |
| ROE | 1.7%（avg equity） | -15.8 pts（FY25 17.5%） | 約 10–15% | 弱 |
| ROIC（estimate） | 約 2.2% | 下降（FY25 約 12.7%） | 約 8–12% | 弱 |
| FCF (USD B) | 4.11 | +18.6% | — | 強 |
| FCF margin | 35.8% | -1.8 pts（FY25 37.6%） | 約 25–30% | 強 |
| FCF / NI | 13.4x（失真） | FY25 3.06x | >0.9 為健康 | 強（但比率失真） |
| FCF − SBC margin | 20.4% | — | — | 中性 |
| SBC / Revenue | 15.5% | +1.5 pts（FY25 14.0%） | 約 10–15% | 偏高 |
| Operating cash flow (USD B) | 4.55 | +22.5% | — | 強 |
| Capex / Revenue | 3.8% | +1.3 pts（FY25 2.7%） | 約 3–5% | 正常 |
| Cash + ST inv. (USD B) | 3.07 | +5.7% | — | 充足 |
| Total debt (USD B) | 2.50 | +639%（FY25 0.34） | — | 可控 |
| Net cash (USD B, derived) | +0.57 | 由 +2.57 降至 +0.57 | — | 淨現金縮減 |
| Current ratio | 0.87 | 由 0.94 降 | 約 1.5–2.0 | 偏低（SaaS 遞延收入結構） |
| Debt / Equity | 0.09 | 由 0.04 升 | 約 0.1–0.3 | 健康 |
| Goodwill + intangibles / Total assets | 59.9% | — | 約 20–30% | 偏高，減值風險 |
| Tangible book value (USD B) | -1.54 | — | — | 弱 |
| Deferred revenue, total (USD B) | 14.76 | +15.7% | — | 強 |
| Shares outstanding (M) | 815.0 | +22.0%（FY25 667.9） | — | 稀釋明顯 |
| Diluted avg shares (M) | 764 | +7.8% | — | 稀釋 |
| Buyback (USD B) | 1.00 | 由 0 升 | — | 偏少，抵銷不足 |
| Dividend | 無 | — | 視情況 | n/a |
| Insider net (6M, USD M) | −47.9（賣出，0 買入） | — | — | 偏負面（規模小） |
| Forward P/E | 71.2x | — | 約 35–45x | 昂貴 |
| TTM Adj. P/E | 90.7x | — | 約 35–45x | 昂貴 |
| GAAP trailing P/E | 868x | — | — | n/m |
| EV / EBITDA | 181.8x（info） | — | 約 35–50x | 極貴 |
| P/S (TTM) | 24.7x | — | 約 10–14x | 極貴 |
| P/FCF (TTM) | 69.1x | — | 約 30–40x | 昂貴 |
| P/B | 10.3x | — | 約 5–8x | 偏貴 |
| PEG | 1.74 | — | — | 中性偏貴 |
| Analyst mean target | $398.52（+14.8%） | — | — | 中性偏多 |
| Short interest (% float) | 2.66% | — | — | 低 |

## Red flags
- **GAAP 獲利崩落**：FY26 diluted EPS $0.40（-75%）、營業利益 -44%、FQ3 與 FQ4 連續 GAAP 淨損。
- **毛利率下滑**：FY24 74.3% → FY26 70.4%，Cost of Revenue YoY +38.9%，快於營收成長，需追蹤是否為收購整合成本或結構性下降。
- **ROIC 大幅下降**：由 FY25 約 12.7% 降至 FY26 約 2.2%（estimate），收購資本尚未產生對等回報。
- **SBC 高企**：FY26 SBC $1.77B（+37%），占營收 15.5%，FCF 扣除 SBC 後 margin 僅 20.4%。
- **商譽與無形資產佔比高**：59.9% 的總資產為商譽與無形資產，Tangible Book Value 為負，存在日後減值風險。
- **股本稀釋**：股數 +22%（年底）、diluted 平均 +7.8%，回購 $1.0B 尚不足以抵銷。
- **估值極端**：forward P/E 71.2x、TTM 調整後 P/E 90.7x、EV/EBITDA 181.8x、P/S 24.7x；成長與利潤需大幅兌現方能支撐現價。
- **內部人全數賣出、零買入**：6 個月 $47.9M 賣出，CFO 與 CTO 均有大額出售。
- **治理風險指標偏高**：yfinance 風險評分 overallRisk 9、compensationRisk 10（滿分 10）、boardRisk 9、shareholderRightsRisk 9。
- **流動比率 < 1**：0.87（FY25 0.94），雖屬 SaaS 結構，但短期營運資金緩衝變薄。
- **資料一致性**：yfinance info 與財報 BS/CF 存在差異（totalDebt 2.567 vs 2.500；FCF 4.24 vs 4.11；EBITDA 1.56 vs 1.39），本報告以財報原始數字為主；fast_info 的 previousClose 與 pre-market 欄位不一致，價格以 last_price $347.25 為準。
- **GAAP vs 調整後落差**：FQ4 GAAP EPS -$0.35 vs 調整後 $1.02，落差約 $1.37/股，需檢視非 GAAP 調整項目的品質。
- **資料缺口**：分部營收、正式 guidance、收購標的與對價細節、商譽減值測試結果，yfinance 皆未提供（n/a）。

FUNDAMENTALS REPORT COMPLETE
