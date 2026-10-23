# Fundamentals — VST as of 2026-10-23

## Executive summary
VST 的體質屬於「現金流仍強、槓桿偏高、獲利正在下滑」的組合: TTM 營運現金流 USD 5.12B、TTM 自由現金流約 USD 2.26B, 足以覆蓋資本支出與股利, 但淨負債已升至 USD 19.46B (2026-06-30), 流動比率 0.97, 有形帳面價值為負, 且 2026 年 Q2 營收與營業利益同比皆下滑約 5%。估值上 trailing P/E 23.7x 偏高, forward P/E 13.6x 與 EV/EBITDA 10.5x 則隱含盈餘回升預期, 便宜與否取決於 2026-11-06 Q3 財報與後續獲利能否兌現; 6 個月內部人淨賣出 USD 24.7M 為負面訊號, 但規模僅占市值約 0.05%。

資料基準: 財報至 2026-06-30 (Q2 2026); 價格以 fast_info 快取 USD 140.83 與 info 收盤參考 USD 141.15 為準 (約 USD 141)。無資料落在 as-of 日之後。

## Revenue & profitability

**營收 (Total Revenue, USD B)**

| 年度 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|
| Total Revenue | 13.73 | 14.78 | 17.22 | 17.74 |
| YoY | n/a | +7.7% | +16.5% | +3.0% |

- 3 年 CAGR (2022-2025) 約 8.9%。yfinance 2021 欄位為 null, 無法計算 5 年 CAGR。
- Operating Revenue 口徑 2022 為 USD 15.63B (與 Total Revenue 差異來自避險與市價損益), 若以此計算 3 年 CAGR 僅約 4.3%。以 Total Revenue 為主。
- 2026 Q2 (USD M): Total Revenue 4,017 (Q2 2025 為 4,250, YoY -5.5%); Operating Revenue 4,401。TTM Total Revenue 合計 USD 19.21B, 與 info totalRevenue 19.21B 一致。
- 業務組成: 依 info.longBusinessSummary, 分為 Retail、Texas、East、West、Asset Closure 五個 segment, 服務約 500 萬客戶、裝置容量約 44,000 MW (天然氣、核能、煤、太陽能、儲能)。各 segment 營收占比: DATA_UNAVAILABLE。

**獲利能力 (annual)**

| 指標 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|
| Gross margin | 12.3% | 37.4% | 43.7% | 32.9% |
| Operating margin | -8.0% | 18.3% | 23.7% | 12.0% |
| EBITDA margin (reported) | 7.6% | 30.9% | 40.4% | 28.5% |
| Net margin (NI to common) | -10.0% | 9.1% | 14.3% | 4.2% |
| Diluted EPS (USD) | -3.15 | 3.82 | 7.26 | 2.22 |

- 2025 營業利益 USD 2.13B, 較 2024 的 USD 4.08B 下降約 48%。2025 認列 impairment of capital assets USD 228M, special income charges 為 -USD 108M, 這些一次性項目使 2025 獲利波動放大。
- 2025 NI to common USD 752M, 與 Diluted EPS 2.22 × 338.1M 股 ≈ USD 752M 一致 (已核對)。

**季度趨勢 (USD M)**

| 指標 | Q2 2025 | Q3 2025 | Q4 2025 | Q1 2026 | Q2 2026 | Q2 YoY |
|---|---|---|---|---|---|---|
| Total Revenue | 4,250 | 4,971 | 4,584 | 5,640 | 4,017 | -5.5% |
| Operating income | 583 | 1,042 | 629 | 1,499 | 553 | -5.1% |
| Operating margin | 13.7% | 21.0% | 13.7% | 26.6% | 13.8% | +0.1pt |
| NI to common | 280 | 604 | 185 | 980 | 258 | -7.9% |
| Diluted EPS (USD) | 0.83 | 1.78 | n/a | 2.90 | 0.77 | -7.0% |

- 手算核對: Q2 2026 Diluted EPS 0.768 × 平均稀釋股數 335.96M ≈ USD 258M, 與 NI to common 258 一致。
- Q4 2025 Diluted EPS 在 yfinance 為 null, 以 n/a 標示。
- 獲利高度季節性且波動大 (Q1 2026 單季 NI 980M, Q2 2026 僅 258M)。

**ROE / ROIC**
- ROE (info, TTM): 43.0%。此數字的分母為扣除優先股後的普通股權益 (2025 YE 約 USD 2.62B), 因庫藏股 USD 6.93B 使普通股權益被大幅壓縮, ROE 數值被放大, 解讀時需保留。
- ROIC (自算, 2025): EBIT USD 2.105B × (1 - 15.9% 稅率) ÷ Invested Capital USD 22.69B ≈ 7.8%。

## Cashflow & balance sheet

**現金流 (USD B, annual)**

| 指標 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|
| Operating cash flow | 0.49 | 5.45 | 4.56 | 4.07 |
| Capex | 1.30 | 1.68 | 2.08 | 2.75 |
| Free cash flow | -0.82 | 3.78 | 2.49 | 1.32 |
| FCF margin | -5.9% | 25.6% | 14.4% | 7.4% |
| FCF / NI to common | n/a | 2.81x | 1.01x | 1.75x |

- 2025 FCF / NI to common 為 1.75x, 高於 0.9 的健康門檻, 但 2022 為負、2023-2025 逐年下滑, 品質仍屬波動。
- TTM (自 4 季度加總): OCF USD 5.12B、Capex USD 2.87B、FCF USD 2.26B, FCF margin 約 11.7%, FCF / TTM NI to common ≈ 1.11x。TTM OCF 與 info operatingCashflow USD 5.12B 一致。
- info.freeCashflow 為 USD 37M, 與上述報表推算之 TTM FCF USD 2.26B 不符, 判定為 yfinance 口徑異常, 本報告以報表推算為準。
- Q2 2026 單季 (USD M): OCF 1,023、Capex 689、FCF 334。

**資產負債表**

| 指標 | 2025 YE (USD B) | 2026 Q2 (USD B) | 備註 |
|---|---|---|---|
| Total Debt | 20.07 | 19.90 | |
| Cash | 0.79 | 0.44 | 2026 Q2: USD 435M |
| Net Debt | 19.28 | 19.46 | 2024 YE 為 15.86 |
| Stockholders Equity (含優先股) | 5.10 | 5.48 | 優先股 USD 2.48B |
| 普通股權益 (扣優先股) | 2.62 | 3.01 | 自算 |
| Current Ratio | 0.78 | 0.97 | info currentRatio 0.973 |
| Working Capital | -2.64 | n/a | |
| Tangible Book Value | -2.62 | n/a | 2025 YE |
| Debt / Equity | n/a | 363% (自算) | info debtToEquity 373% (yfinance 口徑) |

- 淨負債 / EBITDA: 2025 約 3.8x (19.28 ÷ 5.06); 2026 Q2 TTM 約 2.9x (19.46 ÷ info EBITDA 6.65)。
- 利息保障倍數: 2025 EBIT ÷ 利息費用 = 2.1x (2.105 ÷ 0.982); TTM 約 3.9x (EBIT 合計 USD 3.77B ÷ 利息 USD 0.97B)。利息費用 2025 為 USD 982M, 較 2024 的 USD 859M 增加約 14%。
- 短期償債壓力: 2025 YE 流動負債 USD 11.81B 中, Current Debt 為 USD 4.23B。流動比率低於 1, 需依賴再融資。
- 商譽 USD 2.81B; 淨有形資產為負, 資產負債表主要靠實體電廠 (Net PPE USD 19.85B) 支撐。

## Capital allocation & insider signal

**資本配置 (USD B)**

| 項目 | 2022 | 2023 | 2024 | 2025 | TTM (至 Q2 2026) |
|---|---|---|---|---|---|
| 股票回購 | 1.95 | 1.25 | 1.27 | 1.03 | 1.15 |
| 普通股股利 | 0.30 | 0.31 | 0.31 | 0.31 | n/a |
| 優先股股利 | 0.15 | 0.15 | 0.17 | 0.19 | n/a |
| 淨舉債 (Issuance - Repayment) | n/a | n/a | n/a | 2.20 | n/a |
| 稀釋平均股數 (M) | 389.8 | 351.5 | 339.8 | 338.1 | 336.0 (Q2) |

- 股數自 2022 的 389.8M 降至 2025 的 338.1M, 約減少 13%; 2025 至 2026 Q2 僅再減約 0.6%, 回購動能趨緩但仍持續。
- 2025 股東總回報 (回購 USD 1.03B + 股利與優先股股利 USD 0.50B = USD 1.53B) 超過 FCF USD 1.32B, 差額約 USD 0.2B 由舉債支應。
- TTM 口徑 (回購 USD 1.15B + 股利約 USD 0.50B = USD 1.65B) 仍低於 TTM FCF USD 2.26B, 但 2026 Q2 單季回購 USD 337M + 股利 USD 152M = USD 489M, 超過當季 FCF USD 334M。
- 股利覆蓋: 普通股股利 2025 USD 306M, 2025 FCF 對普通股股利覆蓋約 4.3x。每股股利 USD 0.92/年 (季 0.23), 殖利率 0.65%, info payoutRatio 15.4% (以盈餘計)。最近除息日 2026-09-21。
- 資本支出: 2025 USD 2.75B, 較 2024 的 USD 2.08B 增加約 32%; 2026 Q1 單季 USD 883M, Q2 降至 USD 689M。D&A 2025 USD 2.95B, 同樣上升。

**內部人交易 (2026-04-23 至 2026-10-23, 6 個月)**

| 內部人 | 職稱 | 賣出 (USD M) | 買進 (USD M) | 成交價區間 (USD) | 日期 |
|---|---|---|---|---|---|
| HUDSON SCOTT A | Officer (Retail 總裁) | 10.31 | 0 | 150.97-160.14 | 2026-09-08、10-06 |
| MOLDOVAN KRISTOPHER E. | CFO | 6.32 | 0 | 151.03-165.00 | 2026-09-08、10-07 |
| HELM SCOTT BRADFORD | Director | 4.00 | 0 | 160.00 | 2026-06-16 |
| ACOSTA ARCILIA C | Director | 2.51 | 0 | 165.04-170.00 | 2026-06-18 |
| MONTEMAYOR MARGARET M. | CAO | 1.56 | 0 | 160.00-164.96 | 2026-05-27、06-02 |
| SULT JOHN R | Director | 1.10 | 0 | 170.00 | 2026-06-18 |
| BARBAS PAUL M | Director | 0.07 | 0 | 147.93-153.00 | 2026-06-15 |
| BURKE JAMES A. | CEO | 0 | 1.17 | 135.00-135.99 | 2026-08-24、09-01 |

- 合計: 賣出 10 筆 USD 25.88M; 買進 2 筆 USD 1.17M (CEO); 淨賣出 USD 24.71M, 占市值 USD 47.27B 約 0.05%。另有 2026-05-15 董事股票獎勵 (無現金價值) 10 筆。
- 解讀: 賣出多集中於 USD 150-170 區間, 而現價約 USD 141; CEO 則在約 USD 135 買進。yfinance 未提供 10b5-1 計畫標記, 無法判斷賣出是否屬預排計畫: 此為 DATA_UNAVAILABLE。
- 內部人持股比例 0.77% (info heldPercentInsiders), 機構持股 92.1%, 機構數 1,882。

## Valuation

**價格與市值**
- 價格: USD 140.83 (fast_info, 快取, cnyes feed); info 參考 USD 141.15; 前收 USD 156.14, 當日區間 USD 139.10-154.27。
- 市值 USD 47.27B; 企業價值 (EV) USD 69.83B; 稀釋前市值 USD 46.31B。
- 52 週區間 USD 132.66-203.66, 現價位於區間底部約 11.5% 位置。50 日均線 USD 145.32、200 日均線 USD 154.27, 現價皆在其下。

**倍數**

| 倍數 | 數值 | 計算基礎 |
|---|---|---|
| Trailing P/E | 23.7x | 價格 ÷ TTM EPS 5.93 (info) |
| Forward P/E | 13.6x | info forwardPE; 隱含 forward EPS 約 USD 10.4 (forwardEPS 欄位為 null, 為推算值) |
| PEG | 0.44x | info pegRatio |
| EV / EBITDA | 10.5x | info enterpriseToEbitda, EV USD 69.83B ÷ TTM EBITDA USD 6.65B |
| EV / Revenue | 3.6x | info |
| P / S | 2.5x | info priceToSalesTrailing12Months |
| P / FCF | 21.0x | 市值 USD 47.27B ÷ TTM FCF USD 2.26B (自算) |
| P / OCF | 9.2x | 市值 ÷ TTM OCF USD 5.12B (自算) |
| P / B | 15.7x | info, 因普通股權益低而數值偏高, 參考性低 |

**分析師共識 (info)**: 22 位分析師, recommendationKey strong_buy; 目標價平均 USD 208.86 (較現價約 +48%)、最高 USD 305、最低 USD 106。此為外部共識資料, 非本報告結論。

**同業中位數**: 本工具未提供產業中位數。以下為估計值 (非工具輸出, 僅供粗略參照): IPP 產業 forward P/E 約 14-18x; EV/EBITDA 約 10-13x; P/FCF 約 15-20x; P/S 約 1.5-2.5x; ROE 約 8-12%; 淨利率約 8-12%; Debt/Equity 約 150-250%; 流動比率約 1.0-1.3。

## Key catalysts
- **Q3 2026 財報 (2026-11-06)**: yfinance earnings_dates 列出 EPS 預估 USD 2.59 (未公布)。對照 Q3 2025 Diluted EPS USD 1.78, 預估暗示 YoY 約 +45%。注意: yfinance 歷史 EPS 為 GAAP 口徑, 與分析師預估 (常為調整後) 可能不一致, 歷史 surprise 數字需謹慎解讀。
- **近期盈餘歷史**: 2026 Q2 EPS 0.76 對預估 1.63 (-53%); 2026 Q1 2.87 對 1.87 (+53%); 2025 Q4 0.54 對 2.30 (-77%)。盈餘波動極大, 與 mark-to-market 與避險損益認列有關 (Total Revenue 與 Operating Revenue 差距可佐證)。
- **資本支出與資本配置**: 2026 Q1 Capex USD 883M 為近期高點; 後續資本計畫、回購節奏與股利政策為觀察重點。
- **指引 (guidance)**: DATA_UNAVAILABLE (工具未提供管理層指引)。
- **Segment 營收變化**: DATA_UNAVAILABLE (工具未提供 segment 財務資料)。
- **短期持股狀況**: 放空比率 3.6% of float (10.48M 股, 2026-09-30 資料, 較上月 10.78M 微降)。

## Metrics table

金額單位: 年度與 TTM 為 USD B; 季度為 USD M; 比率為 %, 倍數為 x。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| Total Revenue (USD B, 2025) | 17.74 | +3.0% | n/a | 中性 |
| Total Revenue (USD M, Q2 2026) | 4,017 | -5.5% | n/a | 偏弱 |
| Operating margin (2025) | 12.0% | 2024 為 23.7% | 約 15-20% (估計) | 偏弱 |
| Net margin (NI to common, 2025) | 4.2% | 2024 為 14.3% | 約 8-12% (估計) | 偏弱 |
| ROE (info, TTM) | 43.0% | n/a | 約 8-12% (估計) | 受低權益基數放大, 參考性低 |
| ROIC (自算, 2025) | 7.8% | n/a | 約 6-8% (估計) | 中性 |
| FCF (USD B, 2025) | 1.32 | -47% | n/a | 偏弱 |
| FCF (USD B, TTM) | 2.26 | n/a | n/a | 中性 |
| FCF margin (TTM) | 11.7% | n/a | 約 8-12% (估計) | 中性 |
| FCF / NI to common (2025) | 1.75x | n/a | 約 1.0x (估計) | 健康 |
| Net Debt (USD B, Q2 2026) | 19.46 | 較 2025 YE +0.9% | n/a | 偏弱 |
| Net Debt / EBITDA (TTM) | 2.9x | 2025 為 3.8x | 約 3-4x (估計) | 中性偏弱 |
| Interest coverage (TTM) | 3.9x | n/a | 約 3-5x (估計) | 中性 |
| Current Ratio (Q2 2026) | 0.97 | 2025 YE 為 0.78 | 約 1.0-1.3 (估計) | 偏弱 |
| Debt / Equity (自算, Q2 2026) | 363% | n/a | 約 150-250% (估計) | 偏高 |
| Tangible Book Value (USD B, 2025) | -2.62 | 2024 為 -1.93 | n/a | 偏弱 |
| 股票回購 (USD B, 2025) | 1.03 | -19% | n/a | 中性 |
| 股利殖利率 | 0.65% | n/a | 約 3-4% (估計) | 偏低 |
| 普通股股利覆蓋 (FCF 2025 ÷ 普通股股利) | 4.3x | n/a | n/a | 健康 |
| Capex (USD B, 2025) | 2.75 | +32% | n/a | 偏高 |
| 稀釋平均股數 (M, Q2 2026) | 335.96 | -0.9% | n/a | 中性 |
| 內部人 6 個月淨買賣 (USD M) | -24.71 | n/a | n/a | 偏弱 |
| Trailing P/E | 23.7x | n/a | 約 15-20x (估計) | 偏貴 |
| Forward P/E | 13.6x | n/a | 約 14-18x (估計) | 偏便宜 |
| EV / EBITDA (TTM) | 10.5x | n/a | 約 10-13x (估計) | 中性 |
| P / FCF (TTM) | 21.0x | n/a | 約 15-20x (估計) | 中性偏貴 |
| P / S (TTM) | 2.5x | n/a | 約 1.5-2.5x (估計) | 中性 |

## Red flags
- 2026 Q2 營收 (-5.5%)、營業利益 (-5.1%)、NI to common (-7.9%) 與 EPS (-7.0%) 同比皆下滑; 2025 營業利益較 2024 下降約 48%。
- 淨負債持續上升: 2024 YE USD 15.86B → 2025 YE USD 19.28B → 2026 Q2 USD 19.46B; 現金僅 USD 435M, 流動比率 0.97, 營運資金與有形帳面價值皆為負。
- 2025 股東回報 (USD 1.53B) 超過 FCF (USD 1.32B), 2026 Q2 單季回購與股利 (USD 489M) 亦超過當季 FCF (USD 334M), 資本配置對舉債依賴增加。
- 6 個月內部人淨賣出 USD 24.7M, 主要賣方為 Retail 總裁 Hudson 與 CFO Moldovan, 賣出價多在 USD 150-165, 高於現價; CEO 則在 USD 135 附近買進, 方向有分歧。
- 股價位於 50 日與 200 日均線之下, 接近 52 週低點 (USD 132.66), 技術面偏弱 (此處僅引用, 不作交易判斷)。
- 資本支出 2025 年升 32%, 2026 Q1 單季 Capex USD 883M, 成長性投資壓縮自由現金流。
- 普通股權益極薄 (約 USD 2.6-3.0B) 且庫藏股 USD 6.93B, 使 ROE 與 P/B 等比率失真, 不宜直接與同業比較。
- yfinance 治理風險評分中, shareholderRightsRisk 為 5 (10 分制高分代表風險較高), auditRisk 為 4; overallRisk 為 1。
- 資料缺口與品質問題: (1) info.freeCashflow USD 37M 與報表推算 TTM FCF USD 2.26B 不符, 已改採報表值; (2) info.forwardEPS 為 null, forward EPS 為推算; (3) Q4 2025 Diluted EPS 為 null; (4) Yahoo 即時報價與 crumb 取得失敗 (403 / connection), fast_info 價格取自 cnyes 快取; (5) 分部營收、管理層指引、10b5-1 計畫標記皆為 DATA_UNAVAILABLE; (6) 無產業中位數工具資料, 所有 sector median 為估計值。

FUNDAMENTALS REPORT COMPLETE
