# Fundamentals — 2383.TW (台光電 Elite Material) as of 2026-11-06

資料來源: `pipeline/tools/yf.py` (info / financials / quarterly_fin / balance_sheet / quarterly_bs / cashflow / quarterly_cf / earnings_dates / insider / major_holders)。全部回傳 `source: cache`，屬預期行為。金額單位: **億 TWD** (1 億 = 100,000,000 TWD)，全文未混用 B。標註「推算」者為依原始欄位手動計算，非 yfinance 直接提供。報價時間戳 2026-11-06 05:30 UTC (台北 13:30)，未超出 DATE。

## Executive summary

台光電 (2383.TW) 2025 年營收 942.61 億 (YoY +46.4%)，2026 年前三季營收 1412.27 億 (推算)，Q3 2026 毛利率 37.7%、營業利益率 30.7%，獲利動能極強；但同期 FCF 持續為負 (9M26 推算 -47.9 億)，應收帳款與存貨大幅膨脹、有息負債由 201 億增至 449 億，現金流並未跟上獲利。估值上 trailing P/E 40.9x、EV/EBITDA 32.4x、P/B 18.6x 偏高，forward P/E 13.7x 則高度依賴 forwardEps 278.85 (較 TTM EPS 93.29 大幅成長) 的達成。insider 交易資料為空，無法評估內部人訊號。

## Revenue & profitability

**營收趨勢 (億 TWD, 來源: financials / quarterly_fin)**

| 期間 | 營收 | YoY | 毛利 | 毛利率 | 營業利益 | 營業利益率 | 淨利 | 淨利率 |
|---|---|---|---|---|---|---|---|---|
| FY2022 | 386.73 | n/a | 97.10 | 25.1% | 62.25 | 16.1% | 50.73 | 13.1% |
| FY2023 | 412.96 | +6.8% | 113.33 | 27.4% | 73.48 | 17.8% | 54.88 | 13.3% |
| FY2024 | 643.77 | +55.9% | 179.70 | 27.9% | 121.74 | 18.9% | 95.78 | 14.9% |
| FY2025 | 942.61 | +46.4% | 281.20 | 29.8% | 191.13 | 20.3% | 146.49 | 15.5% |
| 1Q26 | 330.67 | n/a | 97.29 | 29.4% | 71.35 | 21.6% | 53.40 | 16.1% |
| 2Q26 | 472.75 | +110.0% (vs 2Q25 225.08) | 160.03 | 33.8% | 127.40 | 26.9% | 98.73 | 20.9% |
| 3Q26 | 608.85 | n/a (3Q25 缺值) | 229.51 | 37.7% | 186.96 | 30.7% | 145.00 | 23.8% |

- **3-year CAGR (FY2022→FY2025, 推算)**: (942.61 / 386.73)^(1/3) - 1 = **约 34.6%**。FY2022-FY2025 為 3 年期；yfinance 無 FY2021 損益，無法計算 5 年 CAGR。
- **TTM 營收** 1661.54 億 (推算 = 4Q25 249.27 + 1Q26 330.67 + 2Q26 472.75 + 3Q26 608.85)，yfinance info `revenueGrowth` = 142.1%。
- **獲利率趨勢**: 毛利率、營業利益率、淨利率連續 4 年擴張，3Q26 單季三率為本次取得之季度資料中的最高水位。3Q26 毛利率 37.7% 相較 FY2025 全年 29.8% 提升約 7.9 個百分點。
- **ROE**: info `returnOnEquity` = 56.8% (TTM)。FY2025 推算 (淨利 146.49 / 平均股東權益 427.8) = 34.2%。
- **ROIC (FY2025 推算)**: NOPAT = EBIT 193.52 × (1 - 稅率 22.4%) = 150.1 億；平均投入資本 (699.38 + 516.64)/2 = 608.0 億；ROIC ≈ **24.7%**。
- **EPS**: FY2025 diluted EPS 40.81 (FY2024 27.30，YoY +49.5%)。2Q26 27.55、3Q26 40.44 (earnings_dates 公布值)。
- **分部營收組合**: yfinance 未提供分部拆分；info `longBusinessSummary` 描述產品為銅箔基板 (CCL)、電子用特用化學品與原料、印刷電路板 (PCB) 用 prepreg 等，應用於行動裝置、基礎建設、汽車、航太與自駕。**分部營收 DATA_UNAVAILABLE**。

**資料缺口**: quarterly_fin 缺 2025-03 季 (全欄 None) 與 2025-09 季 (不在序列)，因此 1Q26、3Q26 無法與同季前一年做準確 YoY 比較。

## Cashflow & balance sheet

**現金流 (億 TWD)**

| 期間 | 營業現金流 (CFO) | 資本支出 (Capex) | FCF (CFO-Capex) | FCF/NI | CFO/NI | FCF margin |
|---|---|---|---|---|---|---|
| FY2022 | 74.98 | 65.44 | 9.54 | 0.19 | 1.48 | 2.5% |
| FY2023 | 28.90 | 42.46 | -13.56 | -0.25 | 0.53 | -3.3% |
| FY2024 | 72.63 | 59.13 | 13.51 | 0.14 | 0.76 | 2.1% |
| FY2025 | 119.68 | 98.78 | 20.90 | 0.14 | 0.82 | 2.2% |
| 9M26 (推算) | 122.93 | 170.84 | -47.91 | -0.16 | 0.41 | -3.4% |
| TTM (推算, 4Q25-3Q26) | 186.34 | 200.82 | -14.48 | n/m | 0.56 | n/m |

- **FCF/NI 遠低於 0.9 健康門檻**: FY2025 為 0.14，9M26 為 -0.16。CFO/NI 亦低於 1.0 (FY2025 0.82、9M26 0.41)，盈餘品質偏弱。
- **營運資金吸收現金**: 9M26 應收帳款變動 -167.13 / -181.31 / -93.15 億 (3Q/2Q/1Q)，存貨變動 -31.92 / -24.35 / -38.25 億。FY2025 應收變動 -98.70 億、存貨變動 -70.85 億。
- **yfinance info 的 `freeCashflow` 為 -107.99 億**，與上表 TTM 推算 -14.48 億不一致，兩者均列出，以季度原始欄位推算值較可核對，此差異列入 Red flags。

**資產負債表 (億 TWD)**

| 科目 | 2025-12 | 2026-03 | 2026-06 | 2026-09 |
|---|---|---|---|---|
| Total Debt | 201.11 | 251.82 | 284.93 | 449.00 |
| Cash & ST investments | 200.08 | 221.35 | 225.68 | 296.79 |
| Net Debt (yfinance / 推算) | ~1.03 (推算) | 24.16 | 52.98 | 146.05 |
| Stockholders' Equity | 504.56 | 479.43 | 583.35 | 734.68 |
| Total Assets | 1079.13 | 1309.77 | 1585.77 | 1937.43 |
| Current Assets | 739.80 | 907.41 | 1132.89 | 1413.26 |
| Current Liabilities | 462.31 | 683.51 | 836.11 | 929.76 |
| Accounts Receivable | 360.65 | 464.20 | 652.78 | 827.04 |
| Inventory | 167.52 | 210.16 | 236.64 | 270.84 |

- **Net debt**: 9M26 由約 1 億 (推算) 增至 146.05 億；Net debt / TTM EBITDA (458.04 億) ≈ **0.32x** (推算)，絕對水位仍低，但增速快。
- **Total Debt / Equity**: 9/26 推算 449.00 / 734.68 = **61.1%** (yfinance `debtToEquity` 61.135，一致)。FY2024 為 172.31 / 350.94 ≈ 49.1% (推算)。
- **Current ratio**: 9/26 推算 1413.26 / 929.76 = **1.52** (info `currentRatio` 1.52，一致)。quick ratio (info) 1.215。
- **應收帳款周轉**: 3Q26 應收 827.04 億 vs 3Q 營收 608.85 億，推算 DSO 約 124 天；FY2025 年末應收 360.65 億，推算 DSO 約 132 天 (以 4Q25 營收 249.27 億計)。應收帳款年初至今 +129%，增幅快於同期營收 (TTM 營收 1661.54 億) 的成長節奏，應收占用資金快速擴大。
- **存貨**: 9/26 270.84 億，較 2025-12 +62%。
- **融資結構**: 1Q-3Q26 推算舉債 (Issuance of Debt) 合計 259.92 億、償還 23.03 億，淨舉債約 236.9 億。FY2025 舉債 114.03 億、償還 26.84 億。

## Capital allocation & insider signal

**資本支出 (億 TWD)**: FY2022 65.44 → FY2023 42.46 → FY2024 59.13 → FY2025 98.78 (YoY +67.1%)。9M26 已達 170.84 億 (推算)，為 FY2025 全年的 1.73 倍，資本支出進入明顯擴張期。FY2025 Capex / 折舊 (18.49 億) 約 5.3x。

**股利 (億 TWD)**: 現金股利支付 FY2022 33.33 → FY2023 28.30 → FY2024 34.39 → FY2025 58.94 (YoY +71.4%)。
- 股利 / FCF (FY2025) = 58.94 / 20.90 ≈ **2.8x**，即股利未由自由現金流覆蓋 (FCF 為正但遠低於股利)。
- 股利 / 淨利 (FY2025) = 58.94 / 146.49 ≈ 40.2%；info `payoutRatio` 0.268 (以 TTM EPS 計)。
- info `dividendRate` 25.0 TWD，`dividendYield` 0.61%。

**股份買回**: 現金流量表中無 Repurchase 科目，**buyback DATA_UNAVAILABLE / 未見**。

**股本稀釋**: 普通股股數 2024-12 346.632M → 2025-06 352.474M → 2025-12 358.321M (FY2025 YoY +3.4%)，APIC 由 56.91 億升至 115.21 億，顯示 2025 年有新股發行 (推算)。2026 年股數維持 358.321M。

**Insider 活動 (6 個月)**: yfinance `insider` 回傳空陣列 `[]`，**無法判定買賣金額與淨買賣方向 (DATA_UNAVAILABLE)**。info `companyOfficers` 所列高階主管 `exercisedValue` 與 `unexercisedValue` 皆為 0。持股結構: `heldPercentInsiders` 19.0%；`heldPercentInstitutions` 48.8%，機構數 374 家 (major_holders)；float 2.956 億股。

## Valuation

**價格與市值 (2026-11-06 報價)**

- 現價 NT$3,820 (前收 4,100，當日跌 -6.83%；日區間 3,690–3,920)。
- 市值 13,687.86 億 TWD (= 3,820 × 358.321M 股，推算一致)。
- EV 14,843.13 億 TWD (info `enterpriseValue`)。
- 52 週區間 1,295–6,470；50 日均 5,178.3 (現價低於 -26.2%)；200 日均 4,342.1 (現價低於 -12.0%)。
- beta 1.649。

**估值倍數**

| 倍數 | 數值 | 計算依據 |
|---|---|---|
| Trailing P/E | 40.9x | 價格 / TTM EPS 93.29 |
| Forward P/E | 13.7x | 價格 / forwardEps 278.85 |
| P/E (epsCurrentYear 134.11) | 28.5x | info `priceEpsCurrentYear` |
| EV/EBITDA (TTM) | 32.4x | EV 14,843.13 / EBITDA 458.04 (info) |
| P/S (TTM) | 8.24x | info `priceToSalesTrailing12Months` |
| P/B | 18.6x | 價格 / BVPS 205.04 |
| P/FCF (TTM) | n/m | TTM FCF 為負 (推算 -14.48 億) |
| PEG (info) | 0.23 | info `pegRatio` |

**分析師共識 (info, 18 家)**: recommendationMean 1.33 (strong_buy)，目標價平均 8,798.6、中位 8,512.5、最高 11,700、最低 6,340 TWD。目標價均值較現價高出約 130%。

**產業中位數 (Sector median)**: 本次未取得同業估值資料，**DATA_UNAVAILABLE**，不以估計數代替。

## Key catalysts

- **最近一次財報**: 2026-10-28 公布 3Q26，diluted EPS 40.44，分析師預估 35.56，**beat +13.7%**。
- **前一季**: 2026-07-29 公布 2Q26 EPS 27.55，預估 24.62，beat +11.9%。
- **1Q26**: 2026-04-29 公布 EPS 14.00 (預估 15.08，miss -7.2%)。注意 quarterly_fin 1Q26 diluted EPS 為 14.89，兩來源不一致 (見 Red flags)。
- **下一次財報日**: yfinance `earnings_dates` 列出 **2027-03-10** (EPS 預估 52.27)，為 DATE 之後的日期，時點可能為估計。
- **股利**: 最近除息日 2026-08-28，股利 25 TWD (info `lastDividendValue`)。
- **產能與資本支出**: 9M26 資本支出 170.84 億 (推算)，若後續產能開出將牽動折舊與獲利節奏；亦須觀察應收與存貨是否於後續季度回收。
- **預期成長**: forwardEps 278.85 相較 TTM EPS 93.29 為 +199%，此為市場/分析師對後續獲利的主要假設，屬下一季及下一年財報的檢驗重點。
- 未取得近期正式 guidance 或新聞公告資料，**guidance DATA_UNAVAILABLE**。

## Metrics table

金額單位: 億 TWD (營收、利潤、現金流、市值、EV、資產負債科目)；比率為 %、x。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 (億 TWD) | FY2025 942.61；TTM 1661.54 | FY2025 +46.4%；2Q26 vs 2Q25 +110.0% | DATA_UNAVAILABLE | 高成長 |
| 毛利率 | FY2025 29.8%；3Q26 37.7% | FY2025 +1.9 pt；3Q26 較 FY25 +7.9 pt | DATA_UNAVAILABLE | 改善明顯 |
| 營業利益率 | FY2025 20.3%；3Q26 30.7% | FY2025 +1.4 pt | DATA_UNAVAILABLE | 改善 |
| 淨利率 | FY2025 15.5%；3Q26 23.8% | FY2025 +0.6 pt | DATA_UNAVAILABLE | 改善 |
| ROE | 56.8% (info TTM)；FY25 推算 34.2% | n/a | DATA_UNAVAILABLE | 優 |
| ROIC | FY25 推算 24.7% | n/a | DATA_UNAVAILABLE | 優 |
| FCF (億 TWD) | FY2025 20.90；9M26 -47.91 (推算) | FY2025 vs FY2024 +54.7% (13.51→20.90) | DATA_UNAVAILABLE | 弱 |
| FCF / NI | FY2025 0.14；9M26 -0.16 | n/a | 0.9 (健康門檻) | 不健康 |
| CFO / NI | FY2025 0.82；9M26 0.41 | n/a | DATA_UNAVAILABLE | 偏弱 |
| FCF margin | FY2025 2.2%；9M26 -3.4% (推算) | n/a | DATA_UNAVAILABLE | 弱 |
| 淨負債 (億 TWD) | 146.05 (2026-09) | 2025-12 推算 ~1.03 → 146.05 | DATA_UNAVAILABLE | 惡化 |
| Net debt / EBITDA (TTM) | 0.32x (推算) | n/a | DATA_UNAVAILABLE | 尚可 |
| Debt / Equity | 61.1% (2026-09 推算) | FY2024 49.1% 推算 | DATA_UNAVAILABLE | 上升中 |
| Current ratio | 1.52 (2026-09) | 2025-12 推算 1.60 | DATA_UNAVAILABLE | 尚可，下滑 |
| 現金及約當現金 (億 TWD) | 296.79 (2026-09) | vs 2025-12 200.08 +48.3% | DATA_UNAVAILABLE | 改善 |
| 資本支出 (億 TWD) | FY2025 98.78；9M26 170.84 (推算) | FY2025 +67.1% | DATA_UNAVAILABLE | 擴張中 |
| 股利支付 (億 TWD) | FY2025 58.94 | +71.4% | DATA_UNAVAILABLE | 股利 / FCF 2.8x，未被 FCF 覆蓋 |
| 股利 / FCF | 2.8x (FY2025 推算) | n/a | DATA_UNAVAILABLE | 弱 |
| 普通股股數 | 358.32M (2025-12) | +3.4% (vs 2024-12 346.63M) | DATA_UNAVAILABLE | 輕度稀釋 |
| Insider 淨買賣 (6 個月) | DATA_UNAVAILABLE (insider 回傳空) | n/a | DATA_UNAVAILABLE | 無法判定 |
| 市值 (億 TWD) | 13,687.86 | n/a | DATA_UNAVAILABLE | 大型股 |
| EV (億 TWD) | 14,843.13 | n/a | DATA_UNAVAILABLE | n/a |
| Trailing P/E | 40.9x | n/a | DATA_UNAVAILABLE | 高 |
| Forward P/E | 13.7x | n/a | DATA_UNAVAILABLE | 依賴成長假設 |
| EV/EBITDA (TTM) | 32.4x | n/a | DATA_UNAVAILABLE | 高 |
| P/FCF (TTM) | n/m (TTM FCF 為負) | n/a | DATA_UNAVAILABLE | n/m |
| P/S (TTM) | 8.24x | n/a | DATA_UNAVAILABLE | 高 |
| P/B | 18.6x | n/a | DATA_UNAVAILABLE | 高 |
| 分析師目標價均值 (TWD) | 8,798.6 (18 家) | n/a | DATA_UNAVAILABLE | 共識偏多 |

## Red flags

- **現金流與獲利背離**: FY2025 FCF/NI 0.14，9M26 FCF 為 -47.9 億 (推算)，TTM FCF 約 -14.5 億 (推算)，與 3Q26 淨利 145.0 億 形成明顯落差。
- **應收帳款急速擴張**: 2025-12 應收 360.65 億 → 2026-09 827.04 億 (+129%)；存貨 +62%。營運資金占用持續增加。
- **負債快速上升**: 有息負債 201.11 億 (2025-12) → 449.00 億 (2026-09)，約 +123%；淨負債由約 1 億增至 146.05 億。利息支出 FY2025 4.76 億，3Q26 單季已達 2.06 億 (推算為 quarterly_fin Interest Expense)。
- **股利未被 FCF 覆蓋**: FY2025 股利 58.94 億，FCF 僅 20.90 億，股利 / FCF 約 2.8x；且 2026 年資本支出已大幅擴張。
- **資本支出激增**: 9M26 資本支出 170.84 億，已為 FY2025 全年 (98.78 億) 的 1.73 倍。
- **估值高**: trailing P/E 40.9x、EV/EBITDA 32.4x、P/B 18.6x；forward P/E 13.7x 建立在 forwardEps 278.85 (較 TTM 93.29 成長 +199%) 的前提上。
- **Insider 資料不可得**: insider 交易紀錄為空，無法驗證內部人買賣方向。
- **資料不一致 (須於下游引用時注意)**:
  - info `freeCashflow` -107.99 億 vs 季度 CF 推算 TTM FCF -14.48 億。
  - info `forwardEps` 278.85 vs `epsCurrentYear` 134.11，兩者未對齊 (forward 可能指不同年度)。
  - 1Q26 EPS: earnings_dates 公布 14.00 vs quarterly_fin 14.89。
  - quarterly_fin 缺 2025-03 與 2025-09 季度，無法完整計算季度 YoY；FY2025 Q4 的 diluted EPS 在 quarterly_fin 為 None。
  - 分部營收與 guidance 皆未取得。
- **產業中位數與 insider 數據缺失**，本報告未以估計值代替。

FUNDAMENTALS REPORT COMPLETE
