# Fundamentals — GOOGL as of 2026-10-26

> 資料說明: Yahoo 直連在本環境被 403 阻擋，所有 yf 欄位皆由 repo 快取 (`prices/yf/GOOGL.json`，`_refreshed_at` 2026-10-25T11:15 UTC) 提供。價格為 2026-10-23 (週五) 收盤 (`regularMarketTime` 2026-10-23 20:00 UTC)，2026-10-24 與 10-25 的盤勢不在資料內。金額單位: USD，以 B (十億美元) 表示。

## Executive summary
Alphabet 財務體質仍屬頂尖: TTM 營收 445.87B、營業利益率 33.1%、現金及短期投資 242.47B 高於總負債 112.76B (淨現金約 129.7B)，Q2'26 營收年增 24.2%。但 2026 年上半年資本支出急升 (TTM capex 132.39B，Q2'26 年增 +100.1%) 且總負債兩季內增加 90%，使 Q2'26 自由現金流轉為負值 (-5.86B)；TTM 淨利 244.21B 內含 Q1/Q2 合計約 135.8B 的非營運證券收益，trailing P/E 16.1x 明顯失真。以 normalized 盈餘估算 trailing P/E 約 31.6x、forward P/E 20.8x、EV/EBITDA 22.0x，估值在財務健康上可接受但並不便宜，分析師均價目標 429.12 (較 320.21 高約 34%) 反映市場對 AI 與雲端成長的高預期。

## Revenue & profitability

**營收趨勢 (annual, USD B):** 2022 282.84 → 2023 307.39 (+8.7%) → 2024 350.02 (+13.9%) → 2025 402.84 (+15.1%)。2022–2025 三年 CAGR 為 12.5%。5 年 CAGR: DATA_UNAVAILABLE (財報快取僅含 2022–2025 四個年度)。

**季度趨勢 (USD B):** Q2'25 96.43 → Q3'25 102.35 → Q4'25 113.83 → Q1'26 109.90 → Q2'26 119.80。Q2'26 年增 +24.2%、季增 +9.0%，與 info.revenueGrowth 0.242 一致。

**分業 (segment) 營收:** DATA_UNAVAILABLE。yf 僅於 longBusinessSummary 列出 Google Services、Google Cloud、Other Bets 三大分部，無分部數字。

**獲利能力 (annual):**

| 年度 | 毛利率 | 營業利益率 | 淨利率 | 淨利 (B) |
|---|---|---|---|---|
| 2022 | 55.4% | 26.5% | 21.2% | 59.97 |
| 2023 | 56.6% | 27.4% | 24.0% | 73.80 |
| 2024 | 58.2% | 32.1% | 28.6% | 100.12 |
| 2025 | 59.7% | 32.0% | 32.8% | 132.17 |
| TTM (至 Q2'26) | 60.9% | 33.1% | 54.8% | 244.21 |

- 2025 年淨利率 32.8% 高於營業利益率 32.0%，主因非營運項目 (`Gain On Sale Of Security` 24.24B)。
- TTM 淨利率 54.8% 不具可比性: Q1'26 含 36.95B、Q2'26 含 98.84B 的 `Gain On Sale Of Security`。扣除這些項目後的 normalized 淨利 TTM 約 123.84B，對應 normalized 淨利率約 27.8%。
- 季度營業利益率: Q2'25 32.4%、Q3'25 30.5%、Q4'25 31.6%、Q1'26 36.1%、Q2'26 34.0%。
- R&D: 2025 61.09B (佔營收 15.2%)；Q2'26 18.22B (佔營收 15.2%)。

**ROE / ROIC:**
- ROE: info.returnOnEquity 48.7% (TTM，yf 口徑)。以 Q2'26 股東權益 640.48B 直接計算 TTM 淨利/權益為 38.1%，差異來自平均權益口徑。
- ROIC (估計): TTM 營業利益 147.63B × (1 − 稅率 0.191，取自 yf Q2'26 `Tax Rate For Calcs`) = NOPAT 約 119.4B，除以 Q2'26 `Invested Capital` 720.62B，約 16.6%。2025 年底 invested capital 為 461.81B，同口徑 ROIC 約 23.2%；2026 年上半年資本投入 (PPE、收購) 使分母大增，ROIC 下滑。

## Cashflow & balance sheet

**現金流 (annual, USD B):**

| 年度 | OCF | Capex | FCF (OCF − Capex) | FCF 利潤率 | FCF / NI |
|---|---|---|---|---|---|
| 2022 | 91.50 | 31.48 | 60.01 | 21.2% | 1.00 |
| 2023 | 101.75 | 32.25 | 69.50 | 22.6% | 0.94 |
| 2024 | 125.30 | 52.53 | 72.76 | 20.8% | 0.73 |
| 2025 | 164.71 | 91.45 | 73.27 | 18.2% | 0.55 |
| TTM (至 Q2'26) | 185.67 | 132.39 | 53.28 | 11.9% | 0.22 (normalized 基礎 0.43) |

- FCF / NI 自 2022 的 1.00 逐年下滑至 TTM 0.22，遠低於 0.9 健康門檻。主因為 capex 自 2022 年 31.48B 增至 2025 年 91.45B，2026 年上半年已達 80.59B (Q1 35.67B、Q2 44.92B)。
- 季度 FCF: Q2'25 5.30 → Q3'25 24.46 → Q4'25 24.55 → Q1'26 10.12 → Q2'26 −5.86 (B)。Q2'26 為本序列首次負值。
- Q2'26 OCF 39.07B，較 Q1'26 45.79B 下滑 14.7%。
- SBC: 2025 24.95B (佔營收 6.2%)；TTM 28.15B。
- info.freeCashflow 為 22.67B，與報表推算的 TTM FCF 53.28B 不一致；本報告以報表推算值為準。

**資產負債表 (USD B):**

| 項目 | 2025-12-31 | 2026-06-30 (Q2'26) | 變化 |
|---|---|---|---|
| Total Assets | 595.28 | 921.98 | +54.9% |
| Cash & Equivalents | 30.71 | 55.91 | +82.1% |
| Cash + Short-term Investments | 126.84 | 242.47 | +91.2% |
| Available For Sale Securities | 68.69 | 131.46 | +91.4% |
| Total Debt | 59.29 | 112.76 | +90.2% |
| Long-term Debt | 46.55 | 98.17 | +110.9% |
| Net PP&E | 261.82 | 338.91 | +29.4% |
| Goodwill | 33.38 | 57.83 | +73.2% |
| Stockholders' Equity | 415.26 | 640.48 | +54.2% |
| Current Assets | 206.04 | 343.52 | |
| Current Liabilities | 102.75 | 126.11 | |

- 淨現金 (Cash + STI − Total Debt): 2025 年底 +67.55B，Q2'26 +129.71B。
- yf 的 `Net Debt` 欄位為 Q2'26 42.25B、2025 年底 15.84B，定義與上列計算不同，已在本報告忽略該欄位，僅供參考。
- 流動比率 (Current Ratio): 2.72 (Q2'26 計算值 343.52 / 126.11；info.currentRatio 2.724)。Quick Ratio 2.47 (info)。
- 負債權益比 (D/E): 18.9% (info.debtToEquity 18.859，yf 以百分比表示)；Q2'26 Total Debt / Equity 為 17.6%。
- 利息費用: Q2'25 0.26B → Q2'26 1.28B。
- 併購: Q1'26 `Purchase Of Business` −33.62B，Goodwill 由 33.38B 增至 57.83B。

## Capital allocation & insider signal

**資本配置 (USD B):**
- 股票回購 (`Common Stock Payments`): 2022 59.30 → 2023 61.50 → 2024 62.22 → 2025 45.71 (年減 26.5%)。季度: Q3'25 11.90、Q4'25 5.50、Q1'26 0.00、Q2'26 0.00。2026 年上半年回購為零。
- 股利: 2024 7.36、2025 10.05；Q1'26 2.54、Q2'26 2.69。每股股利 lastDividendValue 0.22 (年化 0.88)，殖利率 0.27%，payoutRatio 4.3%。TTM 股利約 10.31B，以 TTM FCF 53.28B 計算的股利覆蓋倍數約 5.2x；以 2026 年上半年 FCF (10.12 − 5.86 = 4.26B) 計算，同期股利 5.23B 無法由自由現金流覆蓋。
- 2026 年上半年淨舉債 (`Net Issuance Payments Of Debt`): Q1'26 +29.90B、Q2'26 +21.07B，合計約 50.97B。
- Q2'26 `Net Common Stock Issuance` +30.50B，`Common Stock` 科目由 96.90B 升至 131.37B，同時 Ordinary Shares 由 12.09B (2025 年底) 增至 12.23B。此為異常項目，需以 10-Q 查證是否為股權發行或非現金交易，本報告無法確認。
- 稀釋: 2025 年平均稀釋股數 12.23B，年減 1.7%；Q2'26 季度稀釋股數 12.31B，已高於 Q4'25 的 12.23B。

**內部人交易 (last 6 months，即 2026-04-26 起):**
- 公開市場買入: 0 筆。公開市場賣出: 0 筆。
- 期間內記錄均為贈與 (Stock Gift，成交價 0): Sergey Brin 673,200 股 (2026-08-07，D)；Shriram Kavitark Ram 396,700 股 (2026-10-13，I)。
- 淨金額: 0；占市值比例: 0%。
- 較早的 Hennessy 賣出 (600 股，2026-02-13，約 184K USD) 不在 6 個月窗口內。
- 內部人持股占比 heldPercentInsiders 1.6%；機構持股 81.0% (7,435 家)。
- 空單: sharesShort 80.39M (約 float 的 1.37%)，較前月 77.70M 增 3.5%；shortRatio 2.99 天。

## Valuation

**估值指標 (價格 320.21，2026-10-23 收盤；市值 3,916.1B；EV 3,812.5B):**
- Trailing P/E (yf EPS 19.93): 16.1x。此數字受非營運收益拉高，不建議單獨引用。
- Normalized trailing P/E (估計): 市值 3,916.1B ÷ normalized 淨利 TTM 123.84B = 約 31.6x。
- Forward P/E (forwardEps 15.36): 20.8x；PEG 1.12。
- 當年度 P/E (epsCurrentYear 11.89): 26.9x (priceEpsCurrentYear)。
- EV/EBITDA: 22.0x (info.enterpriseToEbitda，EBITDA TTM 173.16B)。
- P/S (TTM): 8.8x。
- P/FCF: 以報表推算 TTM FCF 53.28B 計算為 73.5x；以 2025 年 FCF 73.27B 計算為 53.5x；以 info.freeCashflow 22.67B 計算為 172.8x (口徑不一，僅供參考)。
- P/B: 6.3x (bookValue 50.90 USD/股)。
- 分析師: 54 位，推薦均值 1.38 (strong_buy)；目標價均值 429.12 (+34.0%)、中位數 430.00、最高 500.00、最低 340.00 (+6.2%)。
- 同業中位數 (估計，非工具輸出): Communication Services / Internet Content 的 trailing P/E 約 20–25x、forward P/E 約 18–22x、EV/EBITDA 約 13–16x、P/S 約 3–4x。以上為估計值，僅作對照。

**技術面背景 (ta snapshot，as_of 2026-10-23):**
- 股價低於 MA20 (343.08) −6.7%、MA50 (342.94) −6.6%、MA200 (341.31) −6.2%。
- RSI14 31.3；MACD 柱狀體 −3.02；布林 %B −0.155 (低於下軌 325.63)；ATR14 8.60。
- 距 52 週高點 408.61 下跌 21.6%；12 個月動能 +27.2%，1 個月 −6.5%。
- 注意: ta 的 52 週低點為 251.85，info 為 264.28，兩來源不一致。

## Key catalysts

- **下一次財報**: 2026-10-28 20:00 UTC (美東盤後)，`isEarningsDateEstimate` = false。財報電話會議約 20:30 UTC。Q3'26 EPS 共識估計 3.00。
- **近四季 EPS 表現 (reported vs estimate):** Q3'25 2.87 vs 2.26 (+26.9%)；Q4'25 2.82 vs 2.64 (+7.0%)；Q1'26 5.11 vs 2.67 (+91.6%)；Q2'26 9.11 vs 2.90 (+214.2%)。Q1 與 Q2 的超額幅度主要來自非營運證券收益 (Q1 36.95B、Q2 98.84B)，與共識估計的口徑不同，市場反應可能聚焦於營業面與 capex/FCF 指引。
- **股利**: 最近一次除息日 2026-09-04，每股 0.22，於 2026-09-14 發放 (依 yf 日期欄位)。
- **資本支出與融資**: 2026 年上半年 capex 80.59B，已接近 2025 全年 91.45B；上半年淨舉債約 50.97B。財報中的資本支出與債務指引須由 10-Q/財報稿確認: DATA_UNAVAILABLE (本工具無指引欄位)。
- **分部營收與 AI/雲端數據**: DATA_UNAVAILABLE。
- **分析師目標價調整**: 目前共識目標價 429.12；下修或上修幅度需於財報後觀察。

## Metrics table
金額單位: USD B (十億美元)；比率單位以 % 或 x 表示。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 Total Revenue (TTM, B) | 445.87 | +24.2% (Q2'26 季) | n/a | 強勁，加速中 |
| 營收 3Y CAGR (2022–2025) | 12.5% | 2025 年 +15.1% | 約 8–10% (估計) | 優於同業估計 |
| 毛利率 Gross Margin (TTM) | 60.9% | 2025 較 2024 +1.5pt | 約 50–55% (估計) | 健康 |
| 營業利益率 Operating Margin (TTM) | 33.1% | 2025 持平 (32.0% vs 32.1%) | 約 20–25% (估計) | 強 |
| 淨利率 Net Margin (TTM, 含非營運) | 54.8% | 2025 +4.2pt | 約 15–20% (估計) | 失真，需用 normalized 27.8% |
| ROE (info, TTM) | 48.7% | n/a | 約 15–20% (估計) | 強，但含非營運收益 |
| ROIC (估計, TTM) | 16.6% | 2025 同口徑 23.2% → 下滑 | 約 12–15% (估計) | 仍具吸引力，但較 2025 下滑 |
| FCF 利潤率 (TTM) | 11.9% | 2025 18.2%，下降 6.3pt | 約 15–20% (估計) | 轉弱 |
| FCF / NI (TTM, reported) | 0.22 | 2025 0.55 | 健康門檻 > 0.9 | 不健康，主因 capex |
| Capex / Revenue (Q2'26) | 37.5% | 2025 全年 22.7%、Q2'25 23.3% | 約 10–15% (估計) | 高，投資周期 |
| 淨現金 Net Cash (Cash+STI − Debt) | +129.71B | 2025 年底 +67.55B | 約中性 (估計) | 仍為淨現金，但縮減 |
| Total Debt | 112.76B | YE25 59.29B，+90% (兩季) | n/a | 警示 |
| 流動比率 Current Ratio | 2.72 | YE25 2.01 (206.04/102.75) | 約 1.5 (估計) | 強 |
| D/E (yf) | 18.9% | n/a | 約 30–50% (估計) | 低 |
| Trailing P/E (GAAP-TTM) | 16.1x | n/a | 約 20–25x (估計) | 失真，偏低 |
| Normalized P/E (估計) | 31.6x | n/a | 約 20–25x (估計) | 偏貴 |
| Forward P/E | 20.8x | n/a | 約 18–22x (估計) | 中性 |
| EV/EBITDA | 22.0x | n/a | 約 13–16x (估計) | 溢價 |
| P/FCF (TTM, 報表推算) | 73.5x | n/a | 約 25–30x (估計) | 偏貴 |
| P/S (TTM) | 8.8x | n/a | 約 3–4x (估計) | 溢價 |
| 股票回購 (2026 H1) | 0.00B | 2025 全年 45.71B | n/a | 停止，需追蹤 |
| 股利殖利率 | 0.27% | n/a | 約 0.5–1% (估計) | 低，股利覆蓋充足 |
| 內部人淨買賣 (6M) | 0 (純贈與) | n/a | n/a | 中性 |
| 分析師目標均價 | 429.12 (+34.0%) | n/a | n/a | 強 |
| RSI14 / 股價 vs MA200 | 31.3 / −6.2% | n/a | n/a | 技術面偏弱 |

## Red flags
- 非營運收益占比過高: TTM 淨利 244.21B 中，Q1'26 與 Q2'26 的 `Gain On Sale Of Security` 合計約 135.8B；trailing EPS、P/E、ROE、淨利率皆不能直接與同業比較。
- FCF 轉負: Q2'26 FCF −5.86B，為本序列首次負值；TTM FCF/NI 0.22，遠低於 0.9。
- Capex 急速擴張: 2025 年 +74.1% (YoY)，Q2'26 年增 +100.1%；Q2'26 capex/revenue 37.5%；2026 年上半年 capex 80.59B 已接近 2025 全年。
- 負債快速上升: Total Debt 兩季內由 59.29B 增至 112.76B (+90%)；利息費用 Q2'26 1.28B，為 Q2'25 0.26B 的約 4.9 倍。
- 回購暫停且股本回升: 2026 年上半年回購為零 (2025 全年 45.71B)；Q2'26 Common Stock 科目與股數同步增加，異常 Net Common Stock Issuance +30.50B 需以 10-Q 查證。
- 股利覆蓋在 2026 年上半年轉弱: 同期 FCF 4.26B 小於股利 5.23B。
- 技術面弱勢: 股價低於 MA20/50/200 日均線 6–7%，RSI14 31.3，布林 %B 為 −0.155；距 52 週高點 −21.6%。
- 治理風險評分偏高: yf 治理評分 overallRisk 10、shareHolderRightsRisk 10、compensationRisk 10、boardRisk 9 (1–10 量表，數字越高風險越大)。
- 資料品質風險: (a) Yahoo 直連失敗，全部數據來自 repo 快取 (2026-10-25 11:15 UTC 更新)；(b) 價格與技術指標分別為 10-23 與 10-23 as_of，10-24、10-25 盤勢未涵蓋；(c) info.sharesOutstanding 5.87B 與 impliedSharesOutstanding 12.23B 不一致，本報告以 12.23B (與財報 Ordinary Shares 相符) 為準；(d) info.freeCashflow 與報表口徑不一；(e) yf `Net Debt` 與淨現金定義不同；(f) 52 週低點 264.28 (info) 與 251.85 (ta) 不一致。
- 分部數據與資本支出指引缺漏: segment 與 guidance 皆為 DATA_UNAVAILABLE。

FUNDAMENTALS REPORT COMPLETE
