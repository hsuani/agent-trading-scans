# Fundamentals — TLN (Talen Energy) as of 2026-10-15

## Executive summary
Talen 目前財務健康度偏弱: TTM 淨虧損 -185M USD、利息覆蓋倍數（EBIT / 利息）僅約 0.75x、Net debt 在 2026-06-30 升至 9.34B USD，且 Current ratio 0.78。估值面取決於對獲利回升的假設: 以 forward EPS 30.99 計算 forward P/E 約 11.6x 偏低，但以 trailing EBITDA 計算 EV/EBITDA 約 45.6x、以我方計算的 TTM FCF 計算 P/FCF 約 38x，兩者差距極大。數據來源為本地快取 (source: cache)，部分欄位在 yfinance 內部定義不一致，已於下方逐項標註。

## Revenue & profitability

**營收與成長**
- 年度營收 (Total Revenue): 2021 1,775M / 2022 2,412M / 2024 2,073M / 2025 2,626M USD。2023 年度欄位於工具輸出中缺漏，標為 DATA_UNAVAILABLE。
- 2025 YoY: +26.7% (2,626 / 2,073)。
- 2021–2025 4 年 CAGR: 約 +10.3%（以 2021 與 2025 年度值計算）。2022–2025 3 年 CAGR 約 +2.9%，顯示 2023–2024 之間營收波動大。
- 季度趨勢 (quarterly_fin): 2025Q2 454M / 2025Q3 770M / 2025Q4 771M / 2026Q1 1,241M / 2026Q2 959M。TTM 營收 3,741M（與 info.totalRevenue 3,740,999,936 吻合）。info.revenueGrowth 為 1.112（約 +111%），與 2026Q2 對 2025Q2 的 YoY (959 / 454 = +111%) 一致。
- 分部 (segment) 營收結構: info.longBusinessSummary 僅描述約 13.1 GW 發電資產（核能、天然氣、燃油、煤炭），未提供分部營收拆分，標為 DATA_UNAVAILABLE。

**毛利 / 營業利益 / 淨利率趨勢（年度，依 financials 計算）**

| 年度 | 毛利率 | 營業利益率 | 淨利率 | 正常化 EBITDA 利潤率 |
|---|---|---|---|---|
| 2021 | 13.6% (241 / 1,775) | -25.1% (-446 / 1,775) | -55.7% (-989 / 1,775) | 23.3% |
| 2022 | 31.9% (770 / 2,412) | 4.3% (104 / 2,412) | -53.4% (-1,289 / 2,412) | 21.5% |
| 2024 | 32.0% (664 / 2,073) | 8.0% (165 / 2,073) | 48.1% (998 / 2,073) | 39.2% |
| 2025 | 38.1% (1,001 / 2,626) | 0.6% (16 / 2,626) | -8.3% (-219 / 2,626) | 22.2% |

- 2024 淨利 998M 含 Gain On Sale Of Ppe 884M 等非經常項目，不代表經常性獲利水準。
- 季度 TTM: info.grossMargins 42.1%、info.operatingMargins -4.8%、info.profitMargins -4.9%。注意: 季度 Operating Income 加總（2025Q3 227 + 2025Q4 -261 + 2026Q1 364 + 2026Q2 139 = 469M，約 12.5%）與 "Total Operating Income As Reported" 加總（263 - 313 + 210 - 72 = 88M，約 2.4%）及 info.operatingMargins（-4.8%）三者不一致，無法從工具資料自行釐清，需以 10-Q 為準。

**ROE / ROIC**
- ROE (info, TTM): -12.8%。以 2026-06-30 股東權益 1,616M 與 TTM 淨利 -185M 粗估約 -11% 至 -14%，與 info 大致一致。
- ROIC: 工具未提供。我方粗估（2025 年 EBIT 136M × (1 - 21%) / (總負債 6,811M + 權益 1,093M - 現金 689M) = 107 / 7,215）約 1.5%，屬於估算值，僅供參考。

## Cashflow & balance sheet

**現金流量（年度）**
- Operating Cash Flow: 2021 -291M / 2022 187M / 2024 256M / 2025 704M。
- Capex: 2021 -250M / 2022 -312M / 2024 -189M / 2025 -206M。2023 缺漏。
- Free Cash Flow（cashflow 工具定義 = OCF - Capex）: 2025 498M，2024 67M，2022 -125M，2021 -541M。
- 2025 年 Stock Based Compensation 為 526M（2024 為 33M），占 2025 營收約 20.0%，超過 2025 年 FCF 498M。此為 2025 年 OCF 的重要加回項目，FCF 品質需打折看待。
- FCF / NI: 2025 年 NI 為負 (-219M)，比值 n/m（不適用）。

**現金流量（季度與 TTM）**
- 2025Q3 OCF 489M / Capex -65M / FCF 424M
- 2025Q4 OCF 280M / Capex -40M / FCF 240M
- 2026Q1 OCF 461M / Capex -69M / FCF 392M
- 2026Q2 OCF -434M / Capex -178M / FCF -612M
- TTM (我方加總): OCF 796M（與 info.operatingCashflow 796M 吻合）、Capex -352M、FCF 444M，FCF margin 約 11.9%。
- info.freeCashflow 為 1,261.75M，與 info 自身 OCF 796M 扣除 Capex 後不符，數據定義或來源有差異，本報告以我方加總 444M 為準並標註。

**資產負債表**

| 項目 | 2025-12-31 | 2026-03-31 | 2026-06-30 |
|---|---|---|---|
| Cash & equivalents (M USD) | 689 | 1,025 | 231 |
| Total debt (M USD) | 6,811 | 6,807 | 9,572 |
| Net debt (M USD) | 6,122 | 5,782 | 9,341 |
| Total assets (M USD) | 10,905 | 10,993 | 15,068 |
| Stockholders' equity (M USD) | 1,093 | 1,073 | 1,616 |
| Current assets / liabilities (M USD) | 1,349 / 1,050 | 1,509 / 1,210 | 1,028 / 1,316 |
| Current ratio | 1.28 | 1.25 | 0.78 |
| Working capital (M USD) | 299 | 299 | -288 |

- Debt / Equity: info.debtToEquity = 584.1%（以 Q2 數字計算約 592%，差異屬定義差異）。
- 2026 年上半年資產負債表急遽擴張: 總資產 2025 年底 10,905M 升至 2026-06-30 15,068M（+4.16B），總債務 +2.76B，權益 +0.52B，流通股數 (balance sheet Ordinary Shares) 由 45.4M 增至 47.9M。工具資料未說明交易性質（收購、融資或其他），需透過 10-Q 或公告確認，本報告不推測。
- 槓桿與利息覆蓋: 
  - 利息支出 (Interest Expense) 季度: 2025Q2 62M / 2025Q3 67M / 2025Q4 99M / 2026Q1 119M / 2026Q2 214M。TTM 499M。
  - 利息覆蓋（EBIT / 利息，EBIT 採季度 EBIT 加總 375M）約 0.75x。2025 年度 EBIT 136M / 利息 302M 約 0.45x。
  - Net debt / EBITDA: 以 info.ebitda 582M 計 約 16.0x；以季度 Normalized EBITDA TTM 1,128M 計約 8.3x；以季度 reported EBITDA TTM 770M 計約 12.1x。三種定義差異極大，建議以 8x–16x 區間理解槓桿水準。
- 現金部位: 2026-06-30 現金 231M，相對於 9.57B 總債務規模極小，短期流動性依賴再融資或經營現金流。

## Capital allocation & insider signal

**資本配置**
- Dividend: 無配息（info.dividendYield = 0.0，trailingAnnualDividendRate = 0）。
- 股票回購 (Repurchase Of Capital Stock): 2021 無資料 / 2022 0 / 2024 -1,958M / 2025 -103M / 2026Q1 -100M / 2026Q2 -198M。2026 年上半年回購合計 -298M，同期 Q2 FCF 為 -612M，回購與負 FCF 同期發生，須以現金餘額下降與債務上升來支應。
- Capex 趨勢: 2025 年 206M，約為 D&A (376M) 的 0.55 倍。2026 年上半年 Capex 合計 247M（Q1 69M + Q2 178M），顯著高於 2025 年同期（Q2 2025 僅 37M）。
- 債務發行與償還: 2024 償還 661M；2025 發行 75M / 償還 92M；2026Q1 發行 500M；2026Q2 償還 1,208M，但季末總債務仍上升至 9,572M，與現金流量表的債務流量並不一致，需以 10-Q 核對。

**內部人交易（過去約 6 個月，2026-04-15 至 2026-10-15）**

| 日期 | 人員 | 職稱 | 股數 | 價格 / 金額 | 性質 |
|---|---|---|---|---|---|
| 2026-06-15 | ABBAS GIZMAN I. | Director | 2,600 | 380.00 / 約 988,000 USD | 公開市場賣出 |
| 2026-07-15 | NUTT TERRY L | President | 8,312 | 未揭露 | 性質未標註（Ownership D） |
| 2026-05-22 | 多位董事與高管 (MCFARLAND 354,865、WRIGHT 95,533、BERRYMAN 99,138 等) | 董事 / 高管 | 合計數十萬股 | 無價格 / 金額 | 無金額欄位，推測為年度獎勵股授予，性質未標註 |

- 過去 6 個月可辨識的公開市場交易僅 Abbas 一筆賣出，金額約 0.99M USD，占市值 16.95B 約 0.006%，規模極小。
- 2026-05-22 大量交易無價格與金額，無法判斷為賣出或授予，本報告不將其計為淨賣出。
- 歷史參考: 2024-12 Rubric Capital (>10% 持股者) 賣出 4,893,507 股 @204.35（約 1.0B USD）；2025-06 Rubric 賣出 388,530 股 @288.55–298.14（約 114M USD）；2025-03 HORTON 買進 1,000 股 @187.96–192.59（約 191K USD）。2025 年起內部人以賣出為主，沒有大規模公開買進。
- 機構持股 (inst_holders, 2026-06-30 季報): BlackRock 7.38%、Rubric Capital 6.10%（持股數不變）、MFN Partners 5.08%、ECP ControlCo 4.07%（較前期 +100%）、Vanguard 合計約 7.15%。info.heldPercentInstitutions 為 102.9%，超過 100%，屬資料定義差異。內部人持股 1.38%。
- 空單: sharesShort 2.50M，佔 float 5.94%，short ratio 3.0 天。

## Valuation

**估值倍數**（price 358.42，來源 fast_info 與 info，本地快取）
- Market cap: 16.95B USD（358.42 × 47.3M 股，與 info.marketCap 吻合）。Enterprise Value: 26.54B USD。
- Trailing P/E: n/a（TTM EPS -3.87）。
- Forward P/E: 11.56（forwardEps 30.99）。另 epsCurrentYear 22.08，對應 P/E 16.2x。
- EV/EBITDA: info 口徑 45.6x（EBITDA 582M）；以季度 Normalized EBITDA TTM 1,128M 計約 23.5x。
- P/S (trailing): 4.53x。EV/Revenue: 7.09x。
- P/B: 10.6x（bookValue 33.74/股）。
- P/FCF: 以 info.freeCashflow 1,262M 計約 13.4x；以我方加總 TTM FCF 444M 計約 38.2x。
- 分析師: 17 位，recommendationMean 1.59（buy）；目標價平均 455.53、中位 449、最低 307、最高 560。以現價計平均目標價隱含上行約 +27.1%。這是分析師共識數據，非本報告建議。
- 技術位置: 52 週區間 279.77–449.84，現價距高點 -20.3%；50 日均線 323.49（現價高於 +10.8%）；200 日均線 351.69（現價高於 +1.9%）。Beta 1.617。
- 當日: 前收 382.14，現價 358.42，約 -6.2%。info.fulldayPrice 352.0 與現價有差異，屬快取資料。

**與產業中位數比較**: 工具未提供 sector median。以下為估計值（非工具輸出），僅供粗略參考。依 Utilities – Independent Power Producers 常見區間估計: forward P/E 約 15–20x、EV/EBITDA 約 10–14x、P/S 約 2–3x、P/B 約 2–3x、淨利率約 5–15%、ROE 約 8–12%。TLN 的 P/S 與 P/B 高於估計區間，EV/EBITDA trailing 也高於估計區間，forward P/E 則低於估計區間。

## Key catalysts
- 下次財報: 2026-11-03（earningsTimestamp 1,793,709,000，isEarningsDateEstimate = False）。該季 EPS 估計 8.37。
- 上次財報 (2026-08-05): 調整後 EPS 2.37 vs 估計 3.39，未達預期 -29.98%。前幾季: 2026-05-05 EPS 4.38 vs 4.26（+2.9%）、2026-02-26 EPS 4.38 vs 4.33（+1.2%）、2025-11-05 EPS 3.29 vs 3.67（-10.3%）。
- 注意 earnings_dates 的 Reported EPS（調整後口徑）與 quarterly_fin 的 Diluted EPS（GAAP 口徑，2026Q2 為 -2.00）定義不同，兩者不可直接比較。
- 資本結構事件: 2026 年上半年資產與債務大幅擴張，以及 Q2 現金下降至 231M，財報電話會議與 10-Q 應說明融資、收購或資本支出計畫。
- 分部與指引: 工具未提供管理層指引或分部營收，標為 DATA_UNAVAILABLE。
- 資料日期: 所有財務報表最新為 2026-06-30，早於分析日期 2026-10-15；未發現晚於分析日期的資料。價格為快取 (cached_at 2026-10-15T11:16 UTC)。

## Metrics table
| Metric | Latest | YoY | Sector median (估計) | Verdict |
|---|---|---|---|---|
| 股價 (USD) | 358.42 | 52 週 -8.6%; 前收 382.14 (-6.2%) | n/a | 中性 |
| Market cap (B USD) | 16.95 | n/a | n/a | 中型 |
| 營收 TTM (M USD) | 3,741 | Q2 YoY +111% | 低至中個位數成長 (估計) | 成長快，但季度波動大 |
| 營收 2025 年度 (M USD) | 2,626 | +26.7% | n/a | 正向 |
| 毛利率 TTM | 42.1% | 2025 年度 38.1% (2024: 32.0%) | n/a | 改善 |
| 營業利益率 TTM | -4.8% (info) | 2025 年度 0.6% | 約 10–20% (估計) | 弱；定義不一致 |
| 淨利率 TTM | -4.9% | 2025 年度 -8.3% | 約 5–15% (估計) | 弱 |
| ROE TTM | -12.8% | n/a | 約 8–12% (估計) | 弱 |
| ROIC (我方粗估, 2025) | 約 1.5% | n/a | 約 5–8% (估計) | 弱 |
| OCF TTM (M USD) | 796 | n/a | n/a | 正 |
| FCF TTM, 我方加總 (M USD) | 444 | 2025 年度 498 | n/a | 正但 2026Q2 為 -612 |
| FCF margin TTM | 11.9% | n/a | n/a | 中性 |
| FCF / NI | n/m (NI 為負) | n/a | 約 1.0 (估計) | 無法評估 |
| SBC 2025 占營收 | 約 20.0% (526 / 2,626) | 2024: 約 1.6% | n/a | 紅旗 |
| Net debt (B USD, 2026-06-30) | 9.34 | 2025 年底 6.12 (+53%) | n/a | 紅旗 |
| Net debt / EBITDA | 約 8.3x (Normalized) – 16.0x (info) | n/a | 約 3–5x (估計) | 紅旗 |
| 利息覆蓋 (EBIT / 利息, TTM) | 約 0.75x | 2025 年度 0.45x | 約 3–6x (估計) | 紅旗 |
| Current ratio | 0.78 | 2025 年底 1.28 | 約 1.0–1.5 (估計) | 紅旗 |
| Debt / Equity | 584% (info) | 2025 年底約 623% | 約 100–200% (估計) | 紅旗 |
| Cash (M USD, 2026-06-30) | 231 | 2025 年底 689 | n/a | 偏低 |
| 股息殖利率 | 0% | n/a | 約 3–5% (估計) | 無配息 |
| 回購 2026 年上半年 (M USD) | 298 | 2024 全年 1,958 | n/a | 與負 FCF 同期，需留意 |
| Capex 2025 (M USD) / 占 D&A | 206 / 0.55x | 2024: 189 | n/a | 資本開支回升 |
| Trailing P/E | n/a (EPS -3.87) | n/a | 約 15–20x (估計) | 無法評估 |
| Forward P/E | 11.6x | n/a | 約 15–20x (估計) | 偏低，依賴 EPS 預測 |
| EV/EBITDA (info, trailing) | 45.6x | n/a | 約 10–14x (估計) | 偏高 |
| P/FCF (info / 我方) | 13.4x / 38.2x | n/a | 約 10–15x (估計) | 口徑差異大 |
| P/S (trailing) | 4.53x | n/a | 約 2–3x (估計) | 偏高 |
| P/B | 10.6x | n/a | 約 2–3x (估計) | 偏高 |
| 分析師平均目標價 | 455.53 (+27.1%) | n/a | n/a | 共識偏多 (17 位) |
| 內部人 6 個月公開市場交易 | 約 0.99M USD 賣出 (0.006% 市值) | n/a | n/a | 中性偏弱 |
| 空單佔 float | 5.94% (3.0 天) | n/a | n/a | 中性 |
| Beta | 1.62 | n/a | 約 0.5–0.8 (估計) | 波動高於大盤 |

## Red flags
- TTM 淨虧損 -185M，2025 年度淨虧損 -219M，trailing EPS -3.87，獲利能力未穩定。
- 利息覆蓋倍數（TTM 約 0.75x）低於 1x，Q2 利息支出 214M 年化約 856M，偏離 2025 年水準。
- 2026 年上半年淨負債由 5.78B 升至 9.34B，單季增幅約 3.6B；總資產在 2026Q2 增加 4.08B，交易性質未揭露。
- Current ratio 0.78、營運資金 -288M、現金僅 231M，短期流動性緊。
- 2025 年 SBC 526M 超過同年 FCF 498M，OCF 含大量非現金加回。
- 2026Q2 OCF -434M、FCF -612M，同季仍回購 198M。
- 2026Q2 調整後 EPS 未達預期 -30%。
- 工具資料內部不一致: EBITDA 有三種口徑（582M / 770M / 1,128M）、TTM FCF 有兩種口徑（444M / 1,262M）、營業利益率有三種口徑。估值與槓桿結論對口徑敏感，須以 10-Q 與 10-K 核對後再使用。
- 2023 年度財報缺漏、分部數據缺漏、管理層指引缺漏（DATA_UNAVAILABLE）。
- 內部人無大規模公開買進；2026 年 5 月大量交易未標註性質，需確認是否為獎勵股授予或稅務扣繳。
- 機構持股合計 102.9%（資料定義差異）與空單比率 5.94%，增加股價波動風險（Beta 1.62）。
- 價格距 52 週高點 -20.3%，現價仍高於 200 日均線 +1.9%。

FUNDAMENTALS REPORT COMPLETE
