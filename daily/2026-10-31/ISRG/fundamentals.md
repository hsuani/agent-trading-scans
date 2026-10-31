# Fundamentals — ISRG as of 2026-10-31

## Executive summary
ISRG 財務體質穩健: 無負債、現金約 40.4 億 USD，TTM 自由現金流約 34.3 億 USD (FCF/NI ≈ 1.16)，最近四季 adjusted EPS 連續超預期 (近 8 季平均超出 ~14.8%)。估值仍屬高檔: 股價 432.01 USD 對應 trailing P/E 52.2、forward P/E 34.7、EV/EBITDA 32.6、P/FCF 約 44 倍，明顯高於一般醫材同業估計中位數。內部人 6 個月內僅有賣出 (合計約 19.8M USD)、無公開市場買進，金額占市值不到 0.02%。工具回傳的利潤表與部分資產負債表數值彼此無法對齊 (詳見 Red flags)，本報告的絕對金額以 yfinance `info` (TTM) 與現金流量表為準，利潤率與營收成長的口徑衝突需人工確認。

## Revenue & profitability
資料口徑說明: 下列 TTM 數字取自 `info`。`financials` / `quarterly_fin` 的利潤表數值與 `info` 差距過大 (毛利率僅 18–20% vs `info` 66.6%)，判定為工具端口徑或單位問題，**不作為絕對金額與利潤率依據**，僅保留其 YoY 方向性資訊並標註。

- **營收 (TTM, `info.totalRevenue`)**: 115.78 億 USD (11.58B)，`info.revenueGrowth` = +21.7%。
- **營收 CAGR (利潤表, FY2022→FY2025)**: 約 +5.2%，FY2025 營收 vs FY2024 為 −2.9%，與 `info` 的 +21.7% 明顯衝突，無法確認真實成長率。
- **季度 YoY (利潤表)**: 2026-Q3 營收 vs 2025-Q3 為 −0.2%，同樣與 `info` 不一致。
- **營收結構**: `info.longBusinessSummary` 未列分部營收，主要產品為 da Vinci 手術系統、Ion 內視鏡平台、器械耗材與服務 (`info` 敘述)，分部金額 n/a。
- **毛利率**: `info.grossMargins` = 66.6%。
- **營業利益率**: `info.operatingMargins` = 33.3%。利潤表 FY2025 營業利益率 5.1%，與 `info` 不符，已棄用。
- **淨利率**: `info.profitMargins` = 25.5%，TTM 淨利約 29.6 億 USD (= 25.5% × 115.78 億)。
- **ROE**: `info.returnOnEquity` = 17.9%。
- **ROIC**: n/a (工具未提供; 不自行推算)。
- **EPS (adjusted, `earnings_dates`)**: 最近四季 reported EPS 為 2.53 (2026-01 報告)、2.50 (2026-04)、2.80 (2026-07)、3.00 (2026-10-20)，合計 10.83 USD；對比去年同季 2.21 → 2.53 (+14%)、1.81 → 2.50 (+38%)、2.19 → 2.80 (+28%)、2.40 → 3.00 (+25%)。
- **EPS (GAAP-like, `info.trailingEps`)**: 8.27 USD；`info.forwardEps` = 12.45 USD (隱含 +50.6%)。
- **獲利動能矛盾**: `info.earningsGrowth` = −23.6%，與上述 adjusted EPS 連續成長及 forward EPS 大幅升高不一致，需人工確認基礎 (GAAP vs adjusted)。

## Cashflow & balance sheet
**現金流量 (可信度較高，與 `info` 可勾稽)**

- 以季度現金流量表加總的 TTM 營業現金流 = 4.09B USD (2025-Q4 + 2026-Q1..Q3 = 892.5 + 911.9 + 1,061.0 + 1,224.1 M)，與 `info.operatingCashflow` = 4,089,499,904 USD 完全吻合，確認此口徑正確。
- **TTM 自由現金流**: `info.freeCashflow` = 3.43B USD (FCF margin ≈ 29.7%)；季度 CF 加總為 3.60B，兩者差異約 1.6 億，屬口徑差。
- **OCF margin (TTM)**: 約 35.3%。
- **FCF / NI (TTM)**: 3.43 / 2.96 ≈ **1.16** (>0.9 健康)。
- **年度 FCF / NI (FY2025)**: 2,490.7 / 2,876.6 ≈ 0.87 (略低於 0.9)，因 FY2025 資本支出與營運現金流口徑不同所致；TTM 已回升。
- **年度 OCF 成長**: FY2022 14.9 億 → FY2023 18.1 億 → FY2024 24.2 億 → FY2025 30.3 億 USD，FY2022–25 CAGR ≈ +26.7%。
- **年度 FCF**: FY2022 9.6 億 → FY2023 7.5 億 → FY2024 13.0 億 → FY2025 24.9 億 USD。

**資產負債表**

- **現金**: `info.totalCash` = 40.4 億 USD (現金 + 短期投資)。
- **有息負債**: `info.totalDebt` = 0 (`info` 口徑)。利潤表與資產負債表中的 "Total Debt" 於 FY2025 為 147.2 億 (工具單位，疑為含租賃負債之其他口徑)，本報告以 `info` 的 0 為主。
- **淨現金**: 約 40.4 億 USD，占市值約 2.6%。
- **Current ratio**: `info.currentRatio` = 3.33；FY2025 利潤表/資產負債表推算 = 2.16 (口徑差異)。
- **Debt / Equity**: `info.debtToEquity` = n/a；以 `info` 有息負債 0 判定無槓桿風險。
- **Book value**: `info.bookValue` = 46.12 USD/股，隱含股東權益約 163 億 USD (46.12 × 353.28M 股)，P/B = 9.37。
- **EV**: `info.enterpriseValue` = 145.84B USD (市值 152.62B − 淨現金 ~ 4.0B 以外的調整項目，工具口徑)。

## Capital allocation & insider signal
**資本支出 (現金流量表, 單位 USD M)**

| 年度 | 資本支出 | 股票回購 |
|---|---|---|
| FY2022 | 532 | 2,607 |
| FY2023 | 1,064 | 416 |
| FY2024 | 1,111 | 0 |
| FY2025 | 540 | 2,295 |

- **TTM 資本支出 (季度 CF)**: 約 4.9 億 USD (2025-Q4 162.5 + 2026-Q1 103.3 + Q2 112.6 + Q3 113.1 M)，占 OCF 約 12%，屬輕資本結構。
- **股票回購 TTM**: 46.2 億 USD (2025-Q4 201 + 2026-Q1 1,123 + Q2 320 + Q3 2,976 M)，**超過 TTM FCF 約 1.35 倍**。2026-Q3 單季回購 29.8 億 USD，為單季 OCF (12.2 億) 的約 2.4 倍，須由既有現金支應，淨現金規模會被壓縮。
- **股息**: 無 (`info.dividendYield` = 0)，股息覆蓋率 n/a。
- **股本**: `info.sharesOutstanding` = 353.28M 股。
- **SBC**: FY2025 7.88 億 USD (FY2024 6.77 億，+16.5%)。

**內部人交易 (`insider`, 6 個月視窗 2026-05-01 至 2026-10-31)**

- 合計 30 筆交易，其中 **賣出 22 筆、合計約 19.76M USD**，**公開市場買進 0 筆**，另有 4 筆為選擇權行使 (Conversion) 不計入賣出。
- 賣出金額占市值 (152.62B) 約 **0.013%**，規模極小。
- 主要賣方: Gary S. Guthart 約 13.08M USD (含 2026-10-23 賣 20,095 股 @451.61 約 9.08M USD，與 2026-08-11 賣 10,000 股 @400 約 4.00M USD)；Iman Jeddi 2.37M；Fredrik Widman 2.24M；其餘為 Craig Barratt、Gary Loeb、Patricia Wadors、Mark Brosius、Amy Ladd 等，每人 0.2–0.5M USD。
- 2026-10-20 財報後 10/23 出現賣出群聚，符合財報後交易窗口開放的例行模式；Brosius 於 2026-07 至 10 月多次小額定期賣出，屬計畫性出售特徵。
- **判讀**: 內部人淨賣出、無買進，訊號偏中性偏負，但金額相對市值可忽略。

**法人持股**: `major_holders` 顯示機構持股 91.4%、內部人持股 0.52%、機構數 3,136。前三大為 BlackRock 8.66% (30.0M 股)、Vanguard 6.67% (23.1M 股)、State Street 4.63% (16.1M 股)，持股集中度低、無單一大股東風險。

## Valuation
**股價基準 (`fast_info`, feed: cnyes，快取時間 2026-10-31 12:06 UTC)**

- 最新價 432.01 USD，前收 448.76 USD (−3.7%)，日內區間 431.19–453.60 USD。
- 52 週區間 328.57 – 603.88 USD，現價距高點 −28.5%、距低點 +31.5%。
- 50 日均 401.54 USD (現價 +7.6%)；200 日均 433.06 USD (現價 −0.2%，貼近 200 日均線)。
- Beta: 1.463。

**估值倍數 (`info`, 以 TTM / forward 計)**

- **市值**: 1,526.2 億 USD (152.62B)；**企業價值 EV**: 1,458.4 億 USD (145.84B)。
- **Trailing P/E**: 52.2x；**Forward P/E**: 34.7x。
- **EV/EBITDA (TTM)**: 32.6x (EBITDA 44.7 億 USD)。
- **P/FCF (TTM)**: 約 44.4x (市值 152.62B ÷ FCF 3.43B)；P/OCF 約 37.3x。
- **P/S (TTM)**: 13.2x；EV/Revenue 12.6x。
- **P/B**: 9.4x。
- **PEG**: n/a (`earningsGrowth` 為負，不具可比性)。
- **分析師目標價 (平均)**: 482.63 USD (30 位分析師，推薦 buy)，隱含 +11.7% 空間。此為外部參考，非本報告建議。

**與同業比較 (估計值，非工具輸出)**: 一般醫療器材同業 trailing P/E 中位數估計約 25–30x、EV/EBITDA 約 18–22x、P/FCF 約 25–30x、P/S 約 5–7x。ISRG 各項倍數皆顯著高於估計中位數，溢價主要來自高毛利 (66.6%)、高 ROE、淨現金與手術機器人的長期成長預期。

## Key catalysts
- **最近一次財報**: 2026-10-20 (盤後)，adjusted EPS 3.00 USD，優於預期 2.64 USD (+13.6%)；前一季 2026-07-16 EPS 2.80 vs 2.50 (+11.9%)。
- **下次財報**: 2027-01-21 (yfinance 日期，盤後時間戳；屬預估)，EPS 預估 2.95 USD，較前年同季 2.53 USD 約 +16.6%。
- **指引 (guidance)**: 工具未提供公司正式全年度指引內容，n/a。
- **分部/產品動向**: 工具未提供分部資料，n/a。需另行查證 da Vinci 裝機與手術量 (procedure volume)、Ion 平台與 SP 系統進度，本報告不做推估。
- **回購動能**: 2026-Q3 單季回購 29.8 億 USD，為近期最大的資本配置事件，後續是否持續需留意下季 CF。
- **股價技術位**: 位於 200 日均線附近 (433.06)，50 日均線 401.54 為下方支撐參考位，52 週高點 603.88 為遠端壓力。

## Metrics table
單位: 金額以 USD B / USD M 標示，未與 億 混用。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 股價 (USD) | 432.01 | 52 週區間 328.57–603.88 | n/a | 中性 |
| 市值 (USD B) | 152.62 | n/a | n/a | 大型股 |
| 企業價值 EV (USD B) | 145.84 | n/a | n/a | — |
| 營收 TTM (USD B) | 11.58 | +21.7% (`info`); 利潤表 FY25 −2.9% (衝突) | n/a | 成長方向待確認 |
| 毛利率 (TTM) | 66.6% | n/a | 約 60–65% | 優於同業 |
| 營業利益率 (TTM) | 33.3% | n/a | 約 15–20% | 優於同業 |
| 淨利率 (TTM) | 25.5% | n/a | 約 12–18% | 優於同業 |
| ROE | 17.9% | n/a | 約 10–15% | 良好 |
| ROIC | n/a | n/a | 約 10–15% | 無資料 |
| EPS trailing (USD) | 8.27 | 獲利 `earningsGrowth` −23.6% (衝突) | n/a | 口徑待確認 |
| EPS forward (USD) | 12.45 | +50.6% vs trailing | n/a | 成長預期高 |
| Adjusted EPS 最近四季合計 (USD) | 10.83 | 單季 YoY +14% 至 +38% | n/a | 強 |
| 最近 8 季 EPS 平均超預期 | +14.8% | n/a | 約 +5% | 優 |
| FCF TTM (USD B) | 3.43 | n/a | n/a | 健康 |
| FCF margin (TTM) | 29.7% | n/a | 約 15–20% | 優 |
| FCF / NI (TTM) | 1.16 | FY25 0.87 | 約 0.8–1.0 | 健康 (>0.9) |
| OCF 成長 (FY22–25 CAGR) | +26.7% | FY25 +25.5% | n/a | 強 |
| 有息負債 (USD B) | 0 (`info`) | n/a | 約 0–1 | 極佳 |
| 現金 (USD B) | 4.04 | n/a | n/a | 充足 |
| 淨現金 占市值 | 約 2.6% | n/a | n/a | 緩衝有限 |
| Current ratio | 3.33 | FY25 2.16 (口徑不同) | 約 2–3 | 充足 |
| P/B | 9.4x | n/a | 約 3–5x | 偏貴 |
| Trailing P/E | 52.2x | n/a | 約 25–30x | 偏貴 |
| Forward P/E | 34.7x | n/a | 約 22–26x | 偏貴 |
| EV/EBITDA (TTM) | 32.6x | n/a | 約 18–22x | 偏貴 |
| P/FCF (TTM) | 約 44.4x | n/a | 約 25–30x | 偏貴 |
| P/S (TTM) | 13.2x | n/a | 約 5–7x | 明顯偏貴 |
| 股票回購 TTM (USD B) | 4.62 | 2026-Q3 單季 2.98 | n/a | 超過 FCF 1.35 倍，需關注 |
| 股息 | 0 | n/a | n/a | 無 |
| 內部人 6 個月賣出 (USD M) | 19.76 (22 筆) | 買進 0 | n/a | 中性偏負，金額小 |
| 機構持股 | 91.4% | n/a | n/a | 高 |
| Beta | 1.46 | n/a | ~1.0 | 波動高於大盤 |

## Red flags
- **利潤表數值與 `info` 無法對齊**: 利潤表毛利率 18–20%、營業利益率 2–5%，與 `info` 的 66.6% / 33.3% 差距過大；季度營收加總 1,035.7 億 (工具單位) 約為 `info` TTM 115.8 億 USD 的 9 倍；FY2025 EPS 1.08 與 `info` trailing EPS 8.27 不一致。判定利潤表於本工具輸出存在單位或口徑問題，已排除其絕對金額。建議人工對照 SEC 10-Q/10-K 再確認。
- **營收成長方向衝突**: `info.revenueGrowth` +21.7%，但利潤表 FY25 −2.9%、2026-Q3 YoY −0.2%。成長率是本報告最關鍵的未確定項目，需交由下游再查證。
- **獲利成長口徑衝突**: `info.earningsGrowth` −23.6%，與 adjusted EPS 逐季 YoY +14% 至 +38% 相反，需確認 GAAP / non-GAAP 差異。
- **回購超過自由現金流**: TTM 回購 46.2 億 USD 為 FCF 的 1.35 倍；2026-Q3 單季回購為該季 OCF 的約 2.4 倍。淨現金 40.4 億僅占市值約 2.6%，若回購持續將壓縮緩衝。
- **估值極高**: P/E 52x (trailing)、EV/EBITDA 32.6x、P/FCF 44x、P/S 13.2x，對成長不如預期的風險敏感度高。
- **股價動能**: 股價單日 −3.7%，且已由 52 週高點 603.88 回落 28.5%，目前貼近 200 日均線，趨勢轉弱風險需與技術面報告交叉驗證。
- **內部人持續賣出**: 6 個月 22 筆賣出、零買進，雖金額小但方向一致。
- **資料快取**: `fast_info` 來源為快取 (cnyes feed, cached 2026-10-31 12:06 UTC)，50/200 日均與 52 週區間欄位為 null，本報告改採 `info` 的 fiftyDayAverage / twoHundredDayAverage 與 52 週區間。
- **資料一致性**: 同一 session 內內部人交易資料曾出現兩次不同筆數 (92 筆 vs 150 筆)，本報告採用完整的 150 筆版本 (最新交易日 2026-10-28)，建議下游以 SEC Form 4 再核對。
- **無資料欄位**: ROIC、分部營收、正式全年指引、Debt/Equity 皆為 n/a，未推估。

FUNDAMENTALS REPORT COMPLETE
