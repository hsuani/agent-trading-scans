# Fundamentals — ISRG as of 2026-11-13

資料來源: `pipeline/tools/yf`。yfinance 即時 feed 連線失敗 (Cookie/crumb 403), 工具回退 repo 快取, 一律標記 source: cache。info 快取時間 2026-11-12T15:05:48Z, fast_info 快取時間 2026-11-12T15:01:16Z。最新已公布季報為 FY2026 Q3 (期末 2026-09-30, 公布於 2026-10-20)。未使用 2026-11-13 之後的資料。

單位: 全部為 USD。金額以 B (十億美元) 或 M (百萬美元) 表示, 本報告不使用億。股數以 M 股表示。

## Executive summary
ISRG 財務體質極佳: 無有息負債, 現金及短期投資 USD 4.04B, TTM 營收 USD 11.58B (Q3 YoY +21.7%), GAAP 淨利率 25.5%, 非 GAAP EPS 連續四季超預期 (+11.6% 至 +18.7%)。估值屬高溢價: trailing GAAP P/E 53.5x、EV/EBITDA 34.0x、P/FCF 約 42.6x, 即使以非 GAAP TTM EPS 計 P/E 仍約 40.8x。另外兩項需留意: FY2026 Q3 出現 USD 450M 特殊費用 (原因工具無資料), 且 2026 年前三季買回 USD 4.42B 已超過 TTM 營業現金流 USD 4.09B。

## Revenue & profitability

年度與 TTM 數據 (USD B, %):

| 期間 | 營收 (USD B) | YoY | 毛利率 | 營業利益率 | 淨利率 | 稀釋 EPS (GAAP, USD) |
|---|---|---|---|---|---|---|
| FY2022 | 6.22 | n/a | 67.4% | 25.3% | 21.2% | 3.65 |
| FY2023 | 7.12 | +14.5% | 66.4% | 24.8% | 25.2% | 5.03 |
| FY2024 | 8.35 | +17.2% | 67.5% | 28.1% | 27.8% | 6.42 |
| FY2025 | 10.07 | +20.5% | 66.0% | 29.3% | 28.4% | 7.87 |
| TTM 至 2026-09-30 | 11.58 | Q3 YoY +21.7% | 66.6% (Yahoo grossMargins) | 28.4% (排除特殊費用約 32.2%, 計算值) | 25.5% | 8.27 |

- 營收 3 年 CAGR (FY2022 至 FY2025): 約 17.4% (計算值)。5 年 CAGR: DATA_UNAVAILABLE (財報僅四個年度)。
- 季度營收 (USD B): Q4'25 2.87, Q1'26 2.77, Q2'26 2.89, Q3'26 3.05 (Q3'25 為 2.51, 故 YoY +21.7%)。
- GAAP 稀釋 EPS 3 年 CAGR 約 29.2% (FY2022 到 FY2025, 計算值)。
- 非 GAAP EPS (依 earnings_dates 的 Reported EPS 欄位): FY2025 合計 8.93, 2026 前三季合計 8.30, FY2026 共識 11.25 (info epsCurrentYear), 年增約 +26%。
- 季度非 GAAP EPS YoY: Q1'26 2.50 vs 1.81 (+38%), Q2'26 2.80 vs 2.19 (+28%), Q3'26 3.00 vs 2.40 (+25%)。
- Q3 2026 特殊費用: quarterly_fin 的 Total Unusual Items 為 USD -0.45B (稅效應 -0.097B)。GAAP 營業利益 Q3 為 USD 0.59B, 排除後約 USD 1.04B。GAAP 淨利 Q3 為 USD 0.52B, 排除後約 USD 0.88B (與 tool 的 Normalized Income 0.876B 一致)。費用性質工具未提供, 為 DATA_UNAVAILABLE。
- 分部 (segment) 營收拆分: DATA_UNAVAILABLE。longBusinessSummary 僅列出 da Vinci 手術系統、Ion 內視鏡系統、器械與服務, 未提供金額比重。
- 獲利驗算: FY2025 稀釋 EPS 7.87 × 稀釋股數 362.7M ≈ USD 2.855B, 與 NI USD 2.856B 吻合。

## Cashflow & balance sheet

現金流 (USD B):

| 期間 | 營業現金流 | Capex | FCF | FCF / NI | FCF 利潤率 |
|---|---|---|---|---|---|
| FY2022 | 1.49 | 0.53 | 0.96 | 0.73 | 15.4% |
| FY2023 | 1.81 | 1.06 | 0.75 | 0.42 | 10.5% |
| FY2024 | 2.42 | 1.11 | 1.30 | 0.56 | 15.6% |
| FY2025 | 3.03 | 0.54 | 2.49 | 0.87 | 24.7% |
| TTM (Q4'25 至 Q3'26, 加總季度值) | 4.09 | 0.49 | 3.60 | 1.22 (GAAP NI); 約 1.09 (排除特殊費用) | 31.1% |

- FCF 定義說明: Yahoo info 的 freeCashflow 為 USD 3.43B, 與本表 TTM 加總值 3.60B 差距約 USD 0.16B, 兩者定義不同。本表採「OCF − Capex」。
- FY2025 FCF / NI 為 0.87, 略低於 0.9 健康門檻。主因為存貨增加 USD 1.06B 與應收增加 USD 0.30B 的營運資金佔用。TTM 比值偏高主要來自 Q3 營運資金流入 (其他流動負債 +USD 0.60B), 這部分可能與特殊費用的應計有關, 需以 10-Q 驗證。
- 資產負債表 (2026-09-30, USD B, 季末值):
  - 現金及約當現金 2.98, 短期投資 1.06, 合計 4.04 (與 info totalCash 4.04 一致)。
  - 長期投資 (Investments and advances) 2.76 (YE2025 為 3.10)。
  - 總債務: 0 (info totalDebt 為 0)。淨現金約 USD 4.04B, 佔市值約 2.6%。若計入長期投資, 淨現金約 USD 6.80B。
  - 總資產 19.35; 總負債 3.23; 股東權益 15.99 (Q2 為 18.17, YE2025 為 17.82)。
  - 流動資產 8.43 / 流動負債 2.53 = 流動比 3.33x (YE2025 為 4.87x)。速動比 2.32x (info quickRatio)。
  - 負債 / 股東權益 = 0.20x; 有息負債 / 權益 = 0。
  - 存貨 2.13 (YE2025 為 1.84, 年初至今 +15.7%); 應收帳款淨額 1.47。以 FY2025 COGS 計, 存貨週轉天數約 196 天, DSO 約 55 天 (計算值)。
  - 商譽加無形資產 0.75 (YE2025 為 0.38)。Q1 2026 Purchase of Business 為 USD 0.53B。被收購標的名稱與用途: DATA_UNAVAILABLE。
  - 每股帳面價值 USD 46.12, 有形帳面價值 USD 15.23B。
- 季末股權下降主要來自買回: Q3 股東權益由 18.17 降至 15.99, 保留盈餘由 6.84 降至 4.53。

## Capital allocation & insider signal

資本配置 (USD B):

- Capex: FY2022 0.53, FY2023 1.06, FY2024 1.11, FY2025 0.54 (YoY −51.4%), TTM 0.49。FY2025 Capex / 營收 5.4%, Capex / D&A 0.80 (D&A 0.68)。資本支出已由 2024 的高峰回落。
- 股票買回 (Repurchase of Capital Stock): FY2022 2.61, FY2023 0.42, FY2024 0.00, FY2025 2.30。2026 季度依序為 Q1 1.12, Q2 0.32, Q3 2.98, 前三季合計 4.42 (為 FY2025 全年的 1.93 倍)。前三季買回 / TTM OCF = 108%。
- 買回資金來源: 2026 前三季現金及短期投資由 5.94 降至 4.04, 長期投資由 3.10 降至 2.76。Q3 投資活動現金流 +1.90, 主要為淨投資出售 2.00。
- 股數: 普通股期末 355.1M (YE2025) → 353.3M (2026-09-30)。Q3 稀釋加權股數 351.6M, 較 Q3'25 的 361.8M 減少 2.8%。info sharesOutstanding (最新) 為 346.6M。
- 資料一致性提醒: Q3 買回金額 USD 2.98B, 但季末普通股僅減少約 0.6M 股 (Q2 353.9M → Q3 353.3M), 且 Q3 加權基本股數 349.0M 低於季末股數。此落差可能與 ASR 或結算時點有關, 工具無法確認, 需以 10-Q 核對。
- 股息: 無 (dividendYield 0, payoutRatio 0)。
- 股份基礎薪酬 (SBC): FY2025 USD 0.79B, 佔營收 7.8%。

內部人交易 (2026-05-13 至 2026-11-13, 35 筆):

- 公開市場賣出: 合計 USD 27.12M (62,110 股)。公開市場買入: 0 筆, USD 0。
- 衍生性證券行使後賣出 (conversion of exercise): 合計 USD 2.77M (18,509 股), 多與賣出同日出現。
- 主要賣方:
  - Gary S. Guthart (Executive Chair / 董事): USD 17.65M, 三筆 (2026-08-11 10,000 股 @ 400.00; 2026-10-23 20,095 股 @ 451.61; 2026-11-04 10,000 股 @ 457.34)。
  - Fredrik Widman (VP, 主計長): USD 4.62M (另有行使 USD 2.13M)。
  - Iman Jeddi (Officer): USD 2.37M (另有行使 USD 0.43M)。
  - Craig H. Barratt (董事): USD 1.04M。其餘 Mark Brosius、Patricia Wadors、Gary Loeb、Amy Ladd 合計 USD 1.5M 以內。
- 規模: 27.12M ÷ 市值 153,248M ≈ 0.018%, 規模小。
- 時間分布: 賣出集中在 2026-10-23 至 2026-11-04 (Q3 財報後) 及 2026-08 (股價約 400)。
- 「其他」類型 (value 為 n/a): David J. Rosa (CEO) 2026-06-10 1,358 股、2026-07-10 1,910 股。性質 (授予、稅務扣繳或其他) 工具無法確認, 為 DATA_UNAVAILABLE。
- 10b5-1 計畫與否: DATA_UNAVAILABLE。
- 內部人持股: 0.53% (insidersPercentHeld)。

## Valuation

價格基準: info regularMarketPrice USD 442.09 (2026-11-12 收盤前後, 前收 449.53, 日變動 −1.66%)。fast_info 的 last_price 為 USD 450.45 (cnyes 快取, 2026-11-12 15:01Z), 兩來源不一致, 本報告以 info 為主。

- 市值 USD 153.25B; 企業價值 (EV) USD 151.92B; 流通股 346.6M。
- 倍數 (計算值與工具值):

| 倍數 | 數值 | 計算或來源 |
|---|---|---|
| Trailing P/E (GAAP, EPS 8.27) | 53.5x | info trailingPE |
| Trailing P/E (非 GAAP, TTM EPS 10.83) | 40.8x | 2.53 + 2.50 + 2.80 + 3.00 (計算) |
| FY2026E P/E (非 GAAP EPS 11.25) | 39.3x | info priceEpsCurrentYear |
| Forward P/E (forwardEps 12.47) | 35.5x | info forwardPE |
| PEG | 2.02 | info pegRatio |
| EV / EBITDA (TTM EBITDA USD 4.47B) | 34.0x | info enterpriseToEbitda |
| EV / Sales (TTM) | 13.1x | info enterpriseToRevenue |
| P / S (TTM) | 13.2x | info priceToSalesTrailing12Months |
| P / FCF (TTM, 3.60B) | 42.6x | 計算 (以 info freeCashflow 3.43B 計為 44.6x) |
| P / B | 9.6x | info priceToBook |

- 同業中位數估計: 醫療器材 (Medical Instruments & Supplies) 同業中位數為分析師估計, 非工具回傳。估計區間: trailing P/E 25–30x、EV/EBITDA 18–22x、P/S 4–6x、P/FCF 25–30x、P/B 3–5x。
- 分析師共識 (30 位): 目標價均值 USD 486.57 (+10.1%)、中位數 USD 500 (+13.1%)、高 USD 685 (+54.9%)、低 USD 324 (−26.7%)。recommendationMean 1.76 (Buy)。
- 股價位置: 52 週區間 USD 328.57 至 603.88, 現價位於區間約 41% 位置; 距 52 週高點 −26.8%; 52 週漲跌 −20.5% (S&P 500 同期 +13.1%)。50 日均線 414.76 (現價 +6.6%), 200 日均線 430.11 (現價 +2.8%)。Beta 1.44。
- 空單: 7.06M 股, 佔流通股 2.05%, days to cover 3.06 (日期 2026-10-30)。
- 機構持股: 機構合計 90.86%, 共 3,148 家。前十大持股合計約 36.7%: BlackRock 8.66% (季變 −0.17%)、Vanguard Capital Management 6.67% (+0.22%)、State Street 4.63% (+1.36%)、Invesco 3.42% (+5.84%)、T. Rowe Price 3.25% (−10.09%)、Geode 2.46%、Capital World 2.23% (−3.79%)、Vanguard Portfolio Management 2.09%、Morgan Stanley 1.89% (+8.29%)、Norges Bank 1.43% (−1.78%)。
- 治理風險分數 (Yahoo 量表, 1 至 10, 越高越差): overall 4、board 6、compensation 6、audit 1。

## Key catalysts

- 2026-10-20 (已公布): FY2026 Q3 非 GAAP EPS USD 3.00, 共識 2.64, 超預期 +13.6%。GAAP EPS 1.49 含 USD 450M 特殊費用。
- 下次財報: 2027-01-21 (isEarningsDateEstimate = true, 為估計日期)。該季 EPS 共識 2.95 (即 FY2026 Q4 非 GAAP)。
- 近四季超預期紀錄: Q4'25 +11.6%、Q1'26 +18.7%、Q2'26 +11.9%、Q3'26 +13.6% (平均 +13.9%)。
- 買回持續: 最新流通股 346.6M, 較季末 353.3M 再減約 1.9%。
- Q1 2026 收購 (Purchase of Business USD 0.53B) 的整合與貢獻: DATA_UNAVAILABLE。
- 管理層財務指引 (guidance): DATA_UNAVAILABLE (工具無此欄位)。
- 手術量、裝機數與耗材成長等營運 KPI: DATA_UNAVAILABLE。
- Q3 特殊費用性質與是否為一次性: DATA_UNAVAILABLE。

## Metrics table

單位標示: 金額 USD B/M; 比率 %; 倍數 x。「同業中位數 (估計)」欄為分析師估計值, 非工具回傳。

| 指標 | 最新值 | YoY / 變化 | 同業中位數 (估計) | 判讀 |
|---|---|---|---|---|
| 營收 TTM (USD B) | 11.58 | Q3 YoY +21.7%; FY25 +20.5% | 約 5–8% 成長 | 高成長 |
| 毛利率 TTM | 66.6% | FY25 66.0% vs FY24 67.5% (−1.5 pt) | 約 60% | 優 |
| 營業利益率 TTM (GAAP) | 28.4% (排除特殊費用約 32.2%) | FY25 29.3% vs FY24 28.1% (+1.2 pt) | 約 15–20% | 優 |
| 淨利率 TTM (GAAP) | 25.5% | FY25 28.4% | 約 10–15% | 優 |
| ROE (TTM, Yahoo) | 17.9% | FY25 約 16.0% (計算) | 約 10–12% | 優 |
| ROIC FY2025 (計算) | 約 14.9% | n/a | 約 8–10% | 優 |
| FCF TTM (USD B) | 3.60 | FY25 2.49, +91% vs FY24 1.30 | n/a | 強 |
| FCF 利潤率 TTM | 31.1% | FY25 24.7% vs FY24 15.6% | 約 10–15% | 優 |
| FCF / NI (FY2025) | 0.87 | FY24 0.56 | 約 0.8–1.0 | 略低於 0.9 門檻; TTM 偏高 |
| 現金及短期投資 (USD B) | 4.04 | YE25 5.94 (−32%) | n/a | 充裕 |
| 有息負債 (USD B) | 0 | 無變化 | 約 0.1–0.3x D/E | 極佳 |
| 流動比 (x) | 3.33 | YE25 4.87 | 約 2.5x | 充裕 |
| 負債 / 股東權益 (x) | 0.20 | YE25 0.14 | 約 0.3x | 低 |
| Capex FY2025 (USD B) | 0.54 | YoY −51.4%; 佔營收 5.4% | 占營收約 5–8% | 回落 |
| 買回, 2026 前三季 (USD B) | 4.42 | 為 FY25 全年 2.30 的 1.93 倍; 為 TTM OCF 的 108% | n/a | 強度高, 需留意資金來源 |
| 股息殖利率 | 0% | 無配息 | 約 0–1% | 不配息 |
| 內部人 6 個月淨買入 (USD M) | 買入 0 / 賣出 27.1 | 佔市值 0.018% | n/a | 無買入, 賣出集中 |
| Trailing P/E (GAAP) | 53.5x | n/a | 25–30x | 偏高 |
| Trailing P/E (非 GAAP TTM) | 40.8x | n/a | 25–30x | 偏高 |
| FY2026E P/E (非 GAAP) | 39.3x | n/a | 約 25x | 偏高 |
| Forward P/E | 35.5x | n/a | 約 22x | 偏高 |
| EV / EBITDA (TTM) | 34.0x | n/a | 18–22x | 偏高 |
| P / FCF (TTM) | 42.6x | n/a | 25–30x | 偏高 |
| P / S (TTM) | 13.2x | n/a | 4–6x | 偏高 |
| P / B | 9.6x | n/a | 3–5x | 偏高 |
| PEG | 2.02 | n/a | 約 1.5–2.0 | 略高 |
| 分析師目標價均值 (USD) | 486.57 (較現價 +10.1%) | n/a | n/a | 共識仍高於現價 |
| 52 週股價變動 | −20.5% | S&P 500 +13.1% | n/a | 跑輸大盤 |
| Beta | 1.44 | n/a | 約 1.0 | 高於市場波動 |
| 空單佔流通股 | 2.05% | n/a | n/a | 低 |
| 非 GAAP EPS FY2026E (USD) | 11.25 | 年增約 +26% (vs 8.93) | n/a | 成長強 |
| 下次財報日 | 2027-01-21 (估計) | n/a | n/a | 日期待確認 |

## Red flags
- Q3 2026 出現 USD 450M 特殊費用 (稅後約 USD 354M), GAAP 淨利季減約 36%。性質工具未提供。
- 估值溢價高: GAAP P/E 53.5x、非 GAAP TTM P/E 40.8x、EV/EBITDA 34.0x、P/FCF 42.6x。估值對成長放緩的敏感度高。
- 買回強度: 2026 前三季買回 USD 4.42B, 為 TTM OCF 的 108%, 現金及短期投資由 5.94 降至 4.04。若營運現金流放緩, 買回資金將依賴投資出售。
- 股數資料內部不一致: Q3 買回金額與普通股減少量不成比例 (見資本配置段), 需以 10-Q 核對。
- 存貨累積: 存貨 YE25 至 2026-09 增加 15.7%, FY25 存貨年增 23.7% 高於營收 20.5%。存貨週轉天數約 196 天 (計算值)。
- 內部人賣出: 6 個月公開市場賣出 USD 27.1M (無買入), 其中 Chair Guthart 佔 USD 17.6M, 集中於 Q3 財報後。規模相對市值小, 但方向一致。
- 季末流動負債增加: Q3 流動負債由 1.92 升至 2.53, 應計費用由 0.51 升至 0.99, 性質待確認。
- 2026 年 Q1 收購 (USD 0.53B) 標的與效益: DATA_UNAVAILABLE。
- 股價表現落後: 52 週 −20.5%, 距 52 週高點 −26.8%, 儘管連續超預期, 市場反應原因工具無資料。
- 治理風險分數 (Yahoo): board 6、compensation 6, 高於 audit 1。

FUNDAMENTALS REPORT COMPLETE
