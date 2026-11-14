# Fundamentals — INTC as of 2026-11-15

資料說明: 數據來源為 pipeline/tools/yf 快取 (source: cache, 快取時間 2026-11-14 13:23–13:27 UTC)。單位: 金額以 USD 計, 大額以 B (十億) 或 M (百萬) 標示; 本報告不使用 億 (USD 不適用). 所有資料日期均不晚於 2026-11-14, 無 2026-11-15 之後的實際數據; 下次財報日期為預估值, 屬前瞻資訊而非資料外洩。

## Executive summary

INTC 以 info 欄位計, TTM 營收 59.89B (YoY +20.9%) 但 GAAP 淨虧 -12.03B, 自由現金流僅 0.81B (FCF margin 1.35%), 財務體質以淨現金約 3.9B 與流動比率 2.21 支撐, 尚屬穩定。估值方面, 前瞻 P/E 約 33x (以 59.66 計) 或約 73x (以 131.51 計), 且 6 個月內部人合計出售股票約 202.8M USD、無公開市場買入, 估值吸引力偏弱。最大問題是價格來源互相矛盾 (同一快取時段內 cnyes 報 131.51、Yahoo 報 59.66), 且財務報表 (financials / balance_sheet / cashflow) 量級與 info 不一致, 本報告以 info 為主要依據, 所有估值比率在價格確認前只能視為區間。

## Revenue & profitability

- 營收: info.totalRevenue = 59.89B USD, info.revenueGrowth = +20.9% (TTM YoY)。3-5 年 CAGR 無法計算: 年度損益表 (financials) 顯示 FY 營收 184M → 1,335M, 量級與 info 相差約 45 倍, 無法拿來算 CAGR (見 Red flags)。
- 季度營收趨勢 (quarterly_fin, 統計表單位, 僅看方向): 223M → 268M → 407M → 437M → 479M, 逐季上升; 同列數值與 info 量級不符, 只能定性為「連續季增」。
- 業務分部: info.longBusinessSummary 列出三大分部 CCG (Client Computing)、DCAI (Data Center & AI)、Intel Foundry; 分部營收數字 yfinance 未提供, 分部占比為 n/a。
- 毛利: info.grossProfits = 24.05B, info.grossMargins = 40.2%。
- 營業利益率: info.operatingMargins = 10.3% (營業利益約 6.2B, 由 margin × 營收推算)。
- EBITDA: info.ebitda = 19.14B, ebitdaMargins = 31.9%。EBITDA 與營業利益之間差距 (約 12.9B) 顯示折舊攤提規模極大, 與資本支出強度一致。
- 淨利率: info.profitMargins = -20.1%; netIncomeToCommon = -12.03B。
- 每股盈餘: trailingEps = -2.35 (GAAP), forwardEps = 1.79, epsCurrentYear = 1.49, earningsGrowth = -32.7%。
- 口徑檢查: EPS (-2.35) × 股數 (5.315B) ≈ -12.49B, 與 netIncomeToCommon -12.03B 誤差約 4%, 在加權股數差異範圍內, 符合。
- ROE = -9.6% (info.returnOnEquity); ROA = 1.8%。ROIC: n/a (可靠的 invested capital 資料不足)。
- earnings_dates 歷史季度 EPS (0.67, 1.07, 1.16, 1.20, 最近四季合計約 4.10) 與 GAAP TTM EPS -2.35 差距極大, 推測為非 GAAP 口徑; 兩者不可直接比較。

## Cashflow & balance sheet

Cashflow:
- 營業現金流 (info.operatingCashflow) = 17.47B。
- 自由現金流 (info.freeCashflow) = 0.81B。隱含資本支出 = 17.47B − 0.81B ≈ 16.67B, 約佔營收 27.8%。
- FCF margin = 0.81 / 59.89 ≈ 1.35%。
- FCF / NI: NI 為負 (-12.03B), 比率 n/m, 不適用 >0.9 健康標準。
- 季度 FCF (quarterly_cf, 統計表單位): 38.5M → 51.3M → 139.7M → 177.5M → 82.9M, 有改善但波動大; 量級待確認。

Balance sheet (info, USD):
- 現金及等價物 (totalCash) = 54.00B。
- 總負債 (totalDebt) = 50.13B。
- 淨債務 = 50.13 − 54.00 = −3.87B, 即淨現金約 3.9B (注意: info.enterpriseValue 329.86B 與 市值 + 負債 − 現金 = 313.2B 相差約 16.6B, 來源未說明)。
- 流動比率 (currentRatio) = 2.21; 速動比率 (quickRatio) = 1.75。
- 負債/權益 (debtToEquity) = 38.1% (即 D/E ≈ 0.38x)。
- 每股帳面價值 (bookValue) = 21.64; 股東權益約 21.64 × 5.315B ≈ 115.0B (由 P/B 反推一致)。
- 年度/季度資產負債表 (balance_sheet / quarterly_bs) 總資產 2.30B、股東權益 2.06B、現金 1.17B, 與 info 量級不符 (見 Red flags), 未採用。

## Capital allocation & insider signal

資本配置:
- 股利: info.dividendYield = 0.0, trailingAnnualDividendRate = 0; 目前無配息 (前次除息日 2024-08-07, 最後配息金額 0.125, 之後未再配息)。
- 買回: 年度現金流量表之 Repurchase Of Capital Stock 於 2023–2026 年為 0 或 None; 無回購紀錄。
- 股數: info.sharesOutstanding = 5.315B, floatShares = 4.87B。統計表股數由 171.2M (FY 2025) 增至 185.4M (FY 2026), 增幅約 8.3%, 顯示有稀釋趨勢; 但統計表單位與 info 不一致, 此數字僅作方向參考。
- 資本支出: 隱含 capex 約 16.7B, 相對於 FCF 0.81B, 資本支出幾乎吞掉全部營運現金流; 投資強度高, 回報尚未在 FCF 出現。

內部人交易 (insider, 2026-05-15 至 2026-11-14, 約 6 個月):
- 出售交易 36 筆, 合計約 202.8M USD (以 Value 欄加總, 不含 Value 為 None 的 2026-06-30 CEO 50,000 股與 CFO 25,000 股 "D" 紀錄)。
- 出售股數合計約 941,722 股。
- 公開市場買入: 0 筆。
- 授予 (Grant) 9 筆, 贈與 (Gift) 5 筆, 不計為市場買賣。
- 主要出售人: CHENG CHI FUNG (CTO, 約 98.6M USD), LAM YAT TUNG (COO, 約 67.0M USD), BRENNAN WILLIAM JOSEPH III (約 17.5M USD), FLEMING DANIEL W (CFO, 約 13.5M USD), LAUFMAN JAMES L (約 4.4M USD)。
- 前一個 6 個月 (2025-11-15 至 2026-05-14) 出售約 187.3M USD, 36 筆, 規模相近, 顯示持續性賣出而非集中一次性減持。
- 相對市值: 202.8M / 317.1B (以 59.66 計) ≈ 0.064%, 絕對金額不大, 但方向一致 (全為出售)。
- 最近一筆出售為 2026-10-27 (CHENG CHI FUNG, 155.32–168.02 USD/股)。
- 內部人持股比例 (heldPercentInsiders) = 14.2%; 機構持股 67.0%, 機構數 4,472。
- 大股東 (inst_holders): BlackRock 8.02% (426.5M 股, 2026-06-30), Vanguard 5.37% (2026-06-30), State Street 4.20% (2026-09-30)。
- 做空: sharesShort = 152.9M, 占流通股 2.9%, shortRatio 1.34 日; 上月為 167.2M, 較上月減少約 8.6%。

## Valuation

價格錨點 (兩組數據同一快取時段, 無法判定哪組正確):
- 錨點 A: fast_info (cnyes) last_price = 131.51, previous_close = 139.81, 日內 126.26–141.00。
- 錨點 B: info (Yahoo) currentPrice = 59.66, previousClose = 61.20, 日內 57.00–61.34, regularMarketChangePercent = −2.52%。
- 兩者相差約 2.2 倍。info 自身的 52 週區間 (32.89–142.35)、50 日均線 (94.97)、200 日均線 (87.40) 與 2026-06 至 10 月內部人成交價 (155–281 USD) 亦互相矛盾。

以錨點 B (59.66) 計:
- 市值 = 59.66 × 5.315B ≈ 317.1B。
- 前瞻 P/E = 33.3x (info.forwardPE, 驗算 59.66 / 1.79 = 33.3)。
- 追溯 P/E: n/m (EPS 為負)。
- EV/EBITDA = 17.2x (info.enterpriseToEbitda)。
- P/S = 5.29x。
- P/FCF = 317.1B / 0.81B ≈ 393x。
- P/B = 2.76x。
- PEG = 1.36 (info.pegRatio)。

以錨點 A (131.51) 計 (由 A/B 股價比例換算, 僅供敏感度):
- 市值 ≈ 131.51 × 5.315B ≈ 698.9B。
- 前瞻 P/E ≈ 73.5x。
- EV/EBITDA ≈ 37x (以 feed EV 加上市值差額估算)。
- P/S ≈ 11.7x。
- P/FCF ≈ 866x。
- P/B ≈ 6.1x。

分析師共識 (info, 43 位分析師):
- recommendationMean = 2.51 (hold); 0 月內: strongBuy 2 / buy 12 / hold 34 / sell 1 / strongSell 0。
- 目標價: 平均 90.65, 中位數 86.00, 最高 160.00, 最低 63.00。
- 相對錨點 B: 平均目標價 +52%; 相對錨點 A: 平均目標價 −31%。

同業中位數 (估計, 非 yfinance 資料, 僅供粗略參考): 半導體同業前瞻 P/E 約 25–35x, EV/EBITDA 約 15–25x, P/S 約 5–8x, 毛利率約 50–60%。

## Key catalysts

- 下次財報: earnings_dates 預估 2026-12-01 (EPS 預估 1.28, isEarningsDateEstimate 未明示); info.earningsTimestampStart 則指向 2027-01-28 窗口。兩者不一致, 以官方公告為準。
- 上次財報 (2026-09-01 前後) EPS 1.20, 超出預估 1.17 (+2.7%); 前幾季超預期幅度 12%–14% (2026-06 與 2026-03), 2025-12 超出 35%。
- 分部轉變: Intel Foundry 與 DCAI 為主要敘事 (info.longBusinessSummary), 無分部營收數字可驗證。
- 管理層: info.companyOfficers 列 Lip-Bu Tan 為 CEO, 但內部人交易資料列 BRENNAN WILLIAM JOSEPH III 為 CEO (見 Red flags)。
- 資本支出: 隱含 capex 16.7B 的投入是否轉化為 FCF 改善, 為下一步觀察重點。
- 近期內部人出售集中在 2026-10 (CTO 多筆出售); 後續是否持續為觀察指標。
- 本報告未取得近期公司指引 (guidance) 原文, 指引內容為 n/a。

## Metrics table

營收/獲利單位: USD B; 每股為 USD; 比率為 %/x。Sector median 欄為估計值, 非 yfinance 資料。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 TTM (B USD) | 59.89 | +20.9% | 約 +5–10% | 成長加速, 但需確認 |
| 毛利率 | 40.2% | n/a | 約 50–60% | 偏低 |
| 營業利益率 | 10.3% | n/a | 約 15–25% | 偏低 |
| EBITDA 利益率 | 31.9% | n/a | 約 25–35% | 中等 |
| 淨利率 (GAAP) | −20.1% | n/a | 約 10–20% | 虧損 |
| EPS TTM (GAAP, USD) | −2.35 | n/a | n/a | 虧損 |
| EPS 前瞻 (USD) | 1.79 | n/a | n/a | 需 1.79 達成 |
| ROE | −9.6% | n/a | 約 15% | 負值, 弱 |
| ROA | 1.8% | n/a | 約 8% | 偏弱 |
| 營業現金流 (B USD) | 17.47 | n/a | n/a | 有現金流入 |
| 自由現金流 (B USD) | 0.81 | n/a | n/a | 極薄 |
| FCF margin | 1.35% | n/a | 約 15% | 偏弱 |
| FCF / NI | n/m (NI 為負) | n/a | >0.9 健康 | 不適用 |
| 隱含資本支出 / 營收 | 約 27.8% | n/a | 約 10–15% | 投資強度高 |
| 淨債務 (B USD) | −3.87 (淨現金) | n/a | n/a | 穩健 |
| 流動比率 | 2.21 | n/a | 約 1.5–2.0 | 良好 |
| 速動比率 | 1.75 | n/a | 約 1.0–1.5 | 良好 |
| D/E | 0.38x | n/a | 約 0.3–0.5x | 中性 |
| 前瞻 P/E (@59.66 / @131.51) | 33.3x / 73.5x | n/a | 約 25–35x | 偏貴或極貴 |
| 追溯 P/E | n/m | n/a | 約 25–35x | 無法評估 |
| EV/EBITDA (@59.66 / @131.51) | 17.2x / 約 37x | n/a | 約 15–25x | 區間不一 |
| P/S (@59.66 / @131.51) | 5.3x / 11.7x | n/a | 約 5–8x | 區間不一 |
| P/FCF (@59.66 / @131.51) | 約 393x / 約 866x | n/a | 約 20–30x | 極貴 |
| P/B (@59.66 / @131.51) | 2.8x / 6.1x | n/a | 約 3–5x | 區間不一 |
| 股利殖利率 | 0.0% | n/a | 約 1–2% | 無配息 |
| 回購 | 無紀錄 | n/a | n/a | 無 |
| 內部人 6 個月出售 (M USD) | 202.8 (36 筆) | 前 6 個月 187.3 | n/a | 持續出售, 無買入 |
| 內部人公開買入 | 0 筆 | n/a | n/a | 無正向信號 |
| 內部人持股 | 14.2% | n/a | n/a | 持股高 |
| 機構持股 | 67.0% | n/a | 約 70–80% | 持平 |
| 做空比例 (占流通股) | 2.9% | 上月 3.1% | 約 3–5% | 偏低 |
| Beta | 2.43 | n/a | 約 1.2–1.5 | 波動大 |
| 分析師均價目標 (USD) | 90.65 | n/a | n/a | 相對 59.66 +52%, 相對 131.51 −31% |
| 分析師評等均值 | 2.51 (hold) | n/a | n/a | 中性 |

## Red flags

- 價格來源矛盾: 同一快取時段內 fast_info (cnyes) = 131.51 與 info (Yahoo) = 59.66, 相差約 2.2 倍; info 的 52 週高點 142.35 也低於 2026-06-30 之前的內部人成交價 (最高 274.94 USD)。在確認正確價格前, 所有估值數字只能視為區間, 交易端需先核對。
- 財務報表量級不一致: financials、balance_sheet、cashflow 的 FY 營收 (1.335B)、總資產 (2.30B)、股數 (185.4M)、每股 EPS (2.51) 與 info 的營收 (59.89B)、股數 (5.315B)、EPS (-2.35) 完全不一致, 且年度財報的會計年度結束日標為 04-30 (INTC 實際為 12 月結束)。本報告未採用統計表絕對值, 僅引用方向性資訊。
- GAAP 與非 GAAP 口徑差異大: TTM GAAP EPS -2.35 vs 最近四季 earnings_dates 報告 EPS 合計約 4.10, 差異很大, 不可直接比較。
- 自由現金流極薄: FCF 0.81B, FCF margin 1.35%, 隱含資本支出 16.7B (營收 27.8%); 營業現金流 17.47B 幾乎全被資本支出吸收。
- 持續獲利能力問題: 淨利率 −20.1%, ROE −9.6%, 歷史財報亦有多年虧損紀錄。
- 內部人持續出售: 6 個月 36 筆出售約 202.8M USD, 前一期亦 187.3M, 無任何公開市場買入; 主要出售者為 CTO 與 COO。
- 估值偏高與共識分歧: 前瞻 P/E 33x–73x, 分析師評等均值 2.51 (hold), 目標價區間 63–160。
- 高 Beta: Beta 2.43, 52 週區間 32.89–142.35, 價格波動極大。
- 管理層資料衝突: info.companyOfficers 列 Lip-Bu Tan 為 CEO, 內部人交易資料列 BRENNAN WILLIAM JOSEPH III 為 CEO; 需確認。
- 財報日期不確定: 預估 2026-12-01 與 2027-01-28 不一致, 且 info 標示為估計值。
- 無配息、無回購: 股東回報完全依賴股價, 股數有稀釋趨勢 (統計表 FY 股數 +8.3%, 單位不一致, 僅供方向參考)。

FUNDAMENTALS REPORT COMPLETE
