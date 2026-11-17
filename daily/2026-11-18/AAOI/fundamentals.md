# Fundamentals — AAOI (Applied Optoelectronics, Inc.) as of 2026-11-18

資料基準: 工具輸出 (pipeline/tools/yf, pipeline/tools/ta) 於 2026-11-17 盤中快照 (cache, cached_at 2026-11-17T15:54 UTC)。Yahoo 即時 feed 連線失敗 (CONNECT 403), 全部數字取自 repo cache, 屬預期情況。資料未超出 2026-11-18 日期, 無 post-date 資料。未引用任何過往 daily 報告數字。單位: 財務金額為 USD, 以 百萬美元 (USD M) 與 十億美元 (USD B) 標示, 不使用 億。

## Executive summary

AAOI 營收動能極強: TTM 營收 747.2 USD M, 較去年同期 +127.5% (info.revenueGrowth 1.275), 2026 Q3 為本報告所列季度中首次錄得正營業利益 (Operating Income +6.72 USD M), 但 TTM FCF 為 -884.0 USD M (FCF margin -118%), 資本支出 (TTM 777.7 USD M) 幾乎全靠增資支應 (TTM 股票發行 1,767 USD M), 股本 2025-12 至 2026-09 增加約 20%。資產負債表表面健康 (現金 605.4 USD M > 總債務 350.2 USD M, Current ratio 2.34), 但現金消耗與稀釋速度是主要風險; 估值上 P/S 5.2x、P/B 1.7x 不算貴, 但 trailing P/E 為負、forward P/E 11.4x 依賴 forwardEps 3.75 這一未標年度的分析師共識, 與 FY2026 epsCurrentYear 0.695 差距極大, 估值可信度低。內部人於過去 6 個月合計賣出 USD 94.2M (約市值 2.4%), 無公開市場買入。

## Revenue & profitability

**營收與成長**

| 年度 | 營收 (USD M) | YoY | 毛利率 | 營業利益率 | 淨利率 |
|---|---|---|---|---|---|
| 2022 | 222.8 | n/a | 15.1% | -26.4% | -29.8% |
| 2023 | 217.7 | -2.3% | 27.1% | -18.6% | -25.8% |
| 2024 | 249.4 | +14.6% | 24.8% | -28.3% | -74.9% |
| 2025 | 455.7 | +82.7% | 30.0% | -10.9% | -8.4% |

- 2022–2025 營收 CAGR 約 26.9% (3 年)。2025 年營收跳升, 2024 年淨利率 -74.9% 受 EBITDA 大幅虧損影響 (EBITDA -159.3 USD M, 來源 financials)。
- 季度趨勢 (quarterly_fin, USD M): Q4'25 營收 134.3 → Q1'26 151.1 → Q2'26 191.9 → Q3'26 269.9。Q3'26 YoY 為 +127.5% (對照 Q3'25 118.6)。
- 季度毛利率: Q4'25 31.2%, Q1'26 29.1%, Q2'26 27.7%, Q3'26 28.2%。毛利率在高成長下未見擴張, 最近兩季持平於 28% 左右。
- 季度營業利益率: Q4'25 -8.5%, Q1'26 -8.5%, Q2'26 -12.4%, Q3'26 +2.5% (Operating Income 6.72 USD M)。注意 quarterly_fin 另一列 "Total Operating Income As Reported" 為 -1.44 USD M, 兩者定義不同, 本報告以 Operating Income 為準並標示差異。
- 季度淨利: Q4'25 -2.0, Q1'26 -14.3, Q2'26 -22.8, Q3'26 +6.3 USD M。TTM 淨利 -32.8 USD M (與 info.netIncomeToCommon -32.78 USD M 吻合), 淨利率 -4.4%。

**獲利能力指標**

- ROE (info.returnOnEquity): -2.3%; ROA: -1.5%。
- ROIC (本報告推估, 非工具直接輸出): TTM 營業利益 -41.4 USD M / Q3'26 invested capital 2,518 USD M ≈ -1.6%。2025 年全年為 -49.7 / 931 ≈ -5.3%。仍為負值, 但 Q3'26 已轉正。
- 營收分部: yfinance 未提供分部拆分。longBusinessSummary 描述為光纖網路產品 (光模組、雷射、收發器、headend/node 等), 按客戶別為 data center、有線電視、電信設備商、FTTH 與 ISP。分部營收比重: DATA_UNAVAILABLE。

## Cashflow & balance sheet

**現金流 (USD M)**

| 期間 | 營運現金流 (OCF) | 資本支出 (Capex) | FCF | FCF margin |
|---|---|---|---|---|
| 2023 | -7.9 | -9.7 | -17.6 | -8.1% |
| 2024 | -69.5 | -43.9 | -113.4 | -45.5% |
| 2025 | -174.4 | -179.5 | -354.0 | -77.7% |
| Q4'25 | -29.6 | -75.1 | -104.7 | -78.0% |
| Q1'26 | -85.4 | -58.3 | -143.7 | -95.1% |
| Q2'26 | +11.6 | -285.6 | -274.1 | -142.8% |
| Q3'26 | -2.9 | -358.6 | -361.5 | -133.9% |
| TTM (Q4'25–Q3'26) | -106.2 | -777.7 | -884.0 | -118.3% |

- FCF / NI: NI 為負 (TTM -32.8 USD M), 比率無意義 (n/m)。OCF 亦為負, 無法以 FCF/NI > 0.9 標準評估, 判定為現金流品質不達標。
- 注意: info.freeCashflow 報 -1,309.3 USD M, 與季度現金流表加總 (-884.0 USD M) 不一致, 差額 DATA_UNAVAILABLE 原因不明, 本報告採用季度現金流表加總。
- 營運現金流於 Q2'26 首度轉正 (+11.6), Q3'26 再轉負 (-2.9), 且 Q1'26 營運資金消耗 -90.1 USD M (Change In Working Capital), 反映應收與存貨快速增加。

**資產負債表 (USD M)**

| 項目 | 2025-12-31 | 2026-09-30 | 變動 |
|---|---|---|---|
| 現金及約當現金 | 206.1 | 605.4 | +399.3 |
| 總債務 (Total Debt) | 248.1 | 350.2 | +102.1 |
| 淨現金 / (淨債務) | (41.9) | +255.2 | 由淨債務轉為淨現金 |
| 應收帳款 (AR) | 244.4 | 413.8 | +69.3% |
| 存貨 (Inventory) | 183.1 | 378.0 | +106.4% |
| 股東權益 | 733.9 | 2,241.4 | +205.4% |
| 總資產 | 1,168.4 | 3,135.6 | +168.4% |
| 總負債 | 434.5 | 894.3 | +105.8% |

- 2025-12-31 淨債務以 Total Debt 248.1 − Cash 206.1 = 41.9 計算 (工具 Net Debt 欄位為 None, 本報告自行推算)。
- Current ratio: 2.34 (流動資產 1,544.8 / 流動負債 660.8)。Quick ratio 1.54 (info)。
- Debt/Equity: 15.6% (350.2 / 2,241.4; info.debtToEquity 15.625 為百分比格式)。總負債/總資產 28.5%。
- 營運效率 (以 Q3'26 季度數推算): DSO ≈ 140 天 (AR 413.8 / Q3 營收 269.9 × 91); 存貨天數 DIO ≈ 178 天 (存貨 378.0 / Q3 營業成本 193.7 × 91)。兩者均高, 且較 2025 年底快速攀升, 為營運資金壓力來源。
- 負債結構: 2026-09-30 長期債務 165.4, 短期債務 111.5 (Current Debt), 另有融資租賃負債 (Capital Lease) 73.3。2025-12-31 總債務為 248.1, 2026-09-30 增至 350.2 (+41.1%)。

## Capital allocation & insider signal

**資本配置**
- 資本支出: 2023 -9.7 → 2024 -43.9 → 2025 -179.5 USD M → TTM -777.7 USD M, TTM capex 約為 TTM 營收的 104%。2026 前 9 個月 capex 合計 -702.6 USD M。以資本支出驅動的產能擴張為主軸, 但 yfinance 未提供資本支出用途說明, 具體 project 細節 DATA_UNAVAILABLE。
- 融資: TTM 股票發行 1,767 USD M (Q4'25 176.4 / Q1'26 382.5 / Q2'26 645.8 / Q3'26 562.4), 債務淨增 (2025 年 Issuance 182.6 − Repayment 163.1)。
- 股本稀釋: 普通股 2025-12-31 為 75.0M, 2026-09-30 為 89.9M (+19.9%); info.sharesOutstanding 90.77M。Diluted average shares Q3'26 87.8M vs Q3'25 63.3M (YoY +38.7%)。
- 股利: 無 (dividendYield 0.0%)。買回: 現金流表無 repurchase 項目, 無買回。
- 結論: 資本配置以外部融資支應資本支出與營運虧損, 股東面臨高度稀釋風險。

**內部人交易 (yfinance insider, 2026-05-18 至 2026-11-17)**
- 期間內 27 筆賣出, 合計 566,387 股, 約 USD 94.2M, 買入 0 筆。
- 依人員 (USD M): Chang Hung-Lun Fred 22.7 (144,131 股); Lin Chih-Hsiang Thompson (CEO) 19.9 (117,000 股); Yeh Shu-Hua Joshua 17.0 (101,980 股); Murry Stefan J (CFO) 14.0 (90,000 股); Delaney Cynthia (董事) 10.7 (56,575 股); Kuo David C. 8.2 (48,454 股); Chen Min-Chu Mike (董事) 1.7 (8,247 股)。
- 相對市值: 94.2 / 3,878.2 (市值 USD M) ≈ 2.4%。
- 價格結構: 賣出價格區間為 USD 48.8–205.4, 2026 年 5–6 月多在 USD 159–205, 2026-10 後降至 USD 48–120 (2026-11-10 CFO 以 USD 48.83 賣出)。賣壓集中於股價高點附近; 是否依 10b5-1 計畫執行, 工具無法判定 DATA_UNAVAILABLE。
- 2025-08 曾有 CEO、董事於 USD 21–23 區間公開買入 (合計約 USD 1.3M), 2025-05 CEO 另於 USD 18.2 買入 (約 USD 0.4M), 但 2026 年以來無買入。
- 期間內另有 CEO 與部分高管授予股票 (Stock Award) 與贈與 (Gift), 不計入市場交易。
- 持股: 內部人持股 9.1% (heldPercentInsiders); 機構持股 61.9% (634 家機構)。
- 空頭: 空頭持股 18.04M 股 (2026-10-30), 佔流通股 20.8% (shortPercentOfFloat 0.2075), 較上月 13.87M 增加 30%; Short ratio 1.51 天。

## Valuation

以 2026-11-17 盤中價 USD 42.725 為基準 (info.currentPrice)。

- 市值: USD 3.88B (42.725 × 90.77M 股, info.marketCap 3,878.2 USD M)。
- 企業價值 EV: 本報告自行計算 = 市值 3,878.2 + 總債務 350.2 − 現金 605.4 = USD 3,623.0M。info.enterpriseValue 報 USD 3,844.0M, 兩者差 221 USD M, 原因工具無法說明, 以 Yahoo EV 與自算 EV 並列。
- Trailing P/E: n/m (TTM GAAP EPS -0.38)。
- Forward P/E: 11.4x (info.forwardPE, forwardEps 3.748)。注意: Yahoo 未標示 forwardEps 所屬年度; info.epsCurrentYear (FY2026 估計) 僅 0.695 (priceEpsCurrentYear 61.5x)。FY2026 GAAP 前三季合計 EPS 為 -0.40 (Q1 -0.19, Q2 -0.28, Q3 +0.07), 要達 FY2026 0.695 需 Q4 單季約 +1.1, 顯示共識數字之間存在明顯不一致。
- P/S (TTM): 5.19x (priceToSalesTrailing12Months)。
- P/B: 1.71x (price / bookValue 24.94); 自算 市值 / 股東權益 1.73x。
- EV/EBITDA: n/m。info.ebitda 為 -8.0 USD M, enterpriseToEbitda -480x; 但季度 EBITDA 加總 (Q4'25 -1.5 / Q1'26 -3.1 / Q2'26 -10.1 / Q3'26 +24.6) 為 +9.9 USD M, 兩來源不一致, 比率不作為判斷依據。
- EV/Sales (TTM): 5.1x (enterpriseToRevenue 5.144, 以 Yahoo EV)。
- P/FCF: n/m (TTM FCF 為負)。
- PEG: 0.78 (info.pegRatio), 依賴 forward 盈餘估計, 可信度低。
- 分析師: 5 位, recommendationKey buy (mean 2.0); 目標價 mean USD 109 / median USD 115 / low USD 45 / high USD 165。相對現價 mean 目標隱含 +155%, low 目標隱含 +5%。
- 同業中位數 (估計, 非工具輸出): 光通訊/網通設備同業 P/S 約 3–5x, forward P/E 約 20–30x, EV/Sales 約 3–5x。此為粗估, 不得視為工具數據。
- 股價動能 (ta snapshot, 價格 USD 43.36 為 ta 最近一根收盤序列): 52 週高 233.67 / 低 18.50, 現價距 52 週高 -81.7%; 1M -44.6%, 3M -64.5%, 6M -74.7%, 12M +102%; RSI14 31.2 (接近超賣); MACD 柱 -0.38 (仍在負區); BB %B 0.14; ATR14 7.35 (約佔現價 17.2%); 20 日年化波動 139%; Beta 3.99 (info)。

**價格來源不一致 (需留意)**
- info.currentPrice / regularMarketPrice: 42.725 (2026-11-17 15:54 UTC, 盤中, 日內區間 42.65–48.125, 較前收 -5.39%)
- fast_info (cnyes cache, 15:51 UTC): 44.57
- ta snapshot 最近價: 43.36
- info 中 bid 106.36 / ask 154.24 為不可信資料 (無實際掛單深度), 本報告不採用。

## Key catalysts

- 下次財報: Yahoo earnings_dates 最近一筆為 2026-11-05 (Q3'26, 已公布, EPS 估計 0.14 vs 實際 0.17, 超出 18.6%); 下一筆估計日 2027-02-25 (EPS 估計 0.51)。info.earningsTimestamp 仍顯示 2026-11-05, 屬過期欄位。
- EPS 口徑: earnings_dates 的 Reported EPS (Q3'26 0.17, Q2'26 0.06, Q1'26 -0.01) 與 GAAP diluted EPS (Q3'26 0.07, Q2'26 -0.28, Q1'26 -0.19) 差異大, 推測前者為調整後 (non-GAAP) 口徑, 本報告未能由工具確認, 標記為推論。
- 近期營運動態: 季度營收於 2026 年連續三季加速成長 (151 → 192 → 270 USD M), 同時資本支出與增資同步放大。若後續營收維持高成長, 營運虧損收斂與 FCF 轉正為主要觀察指標; 反之, 增資與存貨、應收增加將延長現金消耗期間。
- 管理層與治理: 高管 (CEO, CFO, 其他 officers) 在 2026 年多次於高價區間賣出, 此為重要敘事變化。
- 空頭部位: 短期空頭持股 20.8% 流通股, 月度增加 30%, 若業績符合預期可能形成軋空, 但也代表市場分歧大。
- 指引 (guidance) 與 segment shift: 工具無法取得管理層指引與分部資料, DATA_UNAVAILABLE。

## Metrics table

表中金額單位: USD M (百萬美元) 除非另標 USD B。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 TTM (USD M) | 747.2 | +127.5% (Q3'26 YoY) | n/a | 成長極強 |
| 毛利率 TTM | 28.8% | 2025 全年 30.0% (2024 24.8%) | 約 25–35% (估計) | 中性, 未擴張 |
| 營業利益率 Q3'26 | +2.5% | Q3'25 約 -12.6% (Operating Income -14.97 / 營收 118.63) | 約 5–10% (估計) | 首度轉正, 尚弱 |
| 淨利率 TTM | -4.4% | 2025 全年 -8.4% | 約 5–10% (估計) | 偏弱 |
| ROE (info) | -2.3% | n/a | 約 10–15% (估計) | 偏弱 |
| ROIC (推估) | -1.6% (TTM) | 2025 -5.3% | 約 8–12% (估計) | 偏弱 |
| FCF TTM (USD M) | -884.0 | 2025 -354.0 | n/a | 負值, 惡化 |
| FCF margin TTM | -118.3% | 2025 -77.7% | 約 0–10% (估計) | 不達標 |
| FCF / NI | n/m | n/m | >0.9 | 不達標 |
| Current ratio | 2.34 | 2025-12 2.63 (675.7/257.3) | 約 1.5–2.5 (估計) | 尚可 |
| 淨現金 (USD M) | +255.2 | 2025-12 為淨債務 41.9 | n/a | 短期安全 |
| Debt / Equity | 15.6% | 2025-12 33.8% (248.1/733.9) | 約 30–60% (估計) | 偏低, 但債務持續增加 |
| 股本變動 (普通股) | 89.9M | 2025-12 75.0M (+19.9% YTD) | n/a | 稀釋中 |
| 資本支出 TTM (USD M) | -777.7 | 2025 -179.5 (較 2024 的 -43.9 增 309%) | n/a | 擴張巨大 |
| 股利 / 買回 | 無 / 無 | n/a | n/a | 無回饋股東 |
| 內部人 6M 淨賣出 (USD M) | -94.2 (賣出) / 0 (買入) | 相對市值 2.4% | 通常 <1% (估計) | 偏空訊號 |
| 空頭持股 / 流通股 | 20.8% | 月增 +30% | 通常 <5% (估計) | 偏高 |
| Trailing P/E | n/m | n/a | 約 20–30x (估計) | n/m |
| Forward P/E | 11.4x | n/a | 約 20–30x (估計) | 低, 但依賴未明年度共識 |
| P/S TTM | 5.2x | n/a | 約 3–5x (估計) | 偏高 |
| P/B | 1.7x | n/a | 約 2–4x (估計) | 合理 |
| EV/EBITDA | n/m | n/a | 約 15–20x (估計) | n/m |
| 市值 (USD B) | 3.88 | n/a | n/a | 中小型 |
| 企業價值 (USD B, 自算) | 3.62 | n/a | n/a | — |
| 分析師目標價 mean (USD) | 109 | 相對現價 +155% | n/a | 共識偏多 |
| 52 週漲跌 (現價 vs 52W 高) | -81.7% | 52W 漲跌 +116.2% | n/a | 高波動, 回檔深 |
| Beta | 3.99 | n/a | 約 1.0–1.5 (估計) | 極高波動 |

## Red flags

- 現金流嚴重為負: TTM FCF -884.0 USD M, FCF margin -118%, 資本支出 TTM 為營收的 104%。
- 依賴增資: TTM 股票發行 1,767 USD M, 股本 2025-12 至 2026-09 增 19.9%, Q3'26 diluted 股數較去年同期 +38.7%, 稀釋持續。
- 內部人大量賣出: 6 個月 USD 94.2M 賣出 (27 筆), 0 筆買入; 多數賣出價格在 USD 100–205, 而現價 USD 42.7。
- 營運資金壓力: DSO 約 140 天, DIO 約 178 天 (Q3'26 推算), 應收與存貨年內增長 69% 與 106%, 高於營收增速的反面信號需追蹤。
- 股價高度波動與崩跌: 1M -44.6%, 3M -64.5%, 距 52W 高 -81.7%; Beta 3.99, 20 日年化波動 139%。
- 空頭集中: 空頭持股佔流通股 20.8%, 月增 30%。
- 共識數據不一致: forwardEps 3.75 與 FY2026 epsCurrentYear 0.695 相差約 5 倍; info.freeCashflow (-1,309.3) 與季度加總 (-884.0) 不一致; info.ebitda (-8.0) 與季度加總 (+9.9) 不一致; Yahoo EV (3,844) 與自算 (3,623) 不一致。估值比率需以原始季報驗證後再用。
- 治理風險 (info): overallRisk 6、auditRisk 9 (高)、shareHolderRightsRisk 8 (高)、boardRisk 7。審計風險分數高, 需留意。
- 資料缺口: 分部營收、管理層指引、sector median (工具未提供, 上表為估計)、內部人交易是否屬 10b5-1 計畫 — DATA_UNAVAILABLE。季度資料缺 2025 年 Q1、Q2 欄位 (quarterly_fin / quarterly_bs 為 None)。

FUNDAMENTALS REPORT COMPLETE
