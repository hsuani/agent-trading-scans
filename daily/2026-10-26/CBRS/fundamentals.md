# Fundamentals — CBRS as of 2026-10-26

> **Ticker 核對警示**: 任務指定名稱為 Caribou Biosciences, 但 yfinance 對 CBRS 回傳的公司為 **Cerebras Systems Inc.** (Nasdaq: CBRS, sector Technology / industry Semiconductors, Sunnyvale CA)。本報告一律以 Cerebras 的資料為準。若交易員原意是 Caribou Biosciences, 本報告全部不適用, 需另行確認正確 ticker (本次未查詢 Caribou 相關資料)。
> 資料來源: `pipeline/tools/yf.py CBRS` 之 info / financials / quarterly_fin / cashflow / balance_sheet / earnings_dates / insider / major_holders / inst_holders, 來源標記為 cache, cached_at 2026-10-25 11:14 UTC。價格時間戳對應約 2026-10-24 收盤 (regularMarketTime)。2026-10-26 之後的資料一律視為未知。
> 金額單位: USD, 以 M (百萬) 與 B (十億) 標示, 不使用 億。

## Executive summary
Cerebras (CBRS) 於 2026-05-14 首次交易, 營收高速成長 (FY2025 營收 USD 510.0M, YoY +75.7%; 2026Q2 YoY +74.3%), 但 FY2025 FCF 為 USD -392.8M (capex USD 382.7M), 2026Q2 營業虧損擴大至 USD -477.2M, 且股價自 2026 年內高點 USD 386.34 回落至 USD 110.82 (52 週 -64.4%), 財務體質仍取決於 IPO 後約 USD 6.4B 的淨現金 (info 之 mrq 數字, 無法於年報核對)。估值上 trailing P/E 與 EV/EBITDA 均為負值無意義, forward P/E 87.0x、P/S 38.7x, 相對半導體同業明顯偏高; 6 個月內內部人淨賣出約 USD 408M 而無公開市場買入, 基本面屬於高成長但獲利與現金流尚未轉正的狀態。

## Revenue & profitability

### 營收成長 (USD M)
| 年度 | 營收 | YoY | 毛利率 | 營業利益率 | 淨利率 (GAAP) |
|---|---|---|---|---|---|
| FY2022 | 24.6 | n/a (無前期) | 11.7% | -726.3% | -721.9% |
| FY2023 | 78.7 | +219.9% | 33.5% | -170.1% | -161.5% |
| FY2024 | 290.3 | +268.6% | 42.3% | -34.9% | -166.0% |
| FY2025 | 510.0 | +75.7% | 39.0% | -28.6% | +46.6% (含 USD 363.3M 非營業收益, 扣除後約 -24.6%) |

- 3 年 CAGR (FY2022–FY2025): 約 +175%。2 年 CAGR (FY2023–FY2025): 約 +154%。
- 季度趨勢 (quarterly_fin): 2025Q1 USD 99.5M → 2025Q2 USD 103.3M → 2026Q1 USD 193.4M (YoY +94.4%) → 2026Q2 USD 180.1M (YoY +74.3%, QoQ -6.9%)。2026Q2 營收首次出現季減。
- H1 2026 營收合計 USD 373.5M, 對 H1 2025 合計 USD 202.8M 為 +84.2%。
- TTM 營收 USD 680.7M (info `totalRevenue` 680.673M), 與 FY2025 加上 H1 2026 之季度加總 (Q3'25+Q4'25 推算 USD 307.2M + H1'26 USD 373.5M) 相符。

### 獲利能力與季度變化
- 2026Q2 毛利 USD 25.6M, 毛利率僅 14.2% (2026Q1 為 44.6%, 2025Q2 為 31.1%)。毛利率大幅壓縮, 原因於本次資料中無法確認 (DATA_UNAVAILABLE: 營收成本明細)。
- 2026Q2 營業損失 USD -477.2M, 其中 R&D USD 320.2M (2025Q2 為 USD 60.8M, 約 5.3 倍; 占營收 178%)。2026Q1 營業損失僅 USD -15.0M, 故 Q2 為明顯的費用跳升。
- 2026Q2 淨利 USD -450.5M, 歸屬普通股淨損 USD -901.1M (差額約 USD 450.5M 疑為 IPO 相關之優先股股利/視同股利調整, 資料未明確揭露, 標示為待查)。2026Q2 diluted EPS USD -2.98。
- FY2025 淨利 USD +237.8M 主要來自 USD 363.3M 非營業利益 (Gain On Sale Of Security, 見 financials `Total Unusual Items`), 扣除後淨損約 USD -125.5M。FY2025 營業損失 USD -145.9M。
- ROE: FY2025 年底股東權益為 USD -578.7M (負值), ROE 無意義 (n/m)。mrq ROE: DATA_UNAVAILABLE (無 mrq 權益數值直接揭露)。
- ROIC: Yahoo 之 invested capital 為負值 (FY2025 USD -578.7M), ROIC n/m。
- 研發占比: FY2025 R&D USD 243.3M, 占營收 47.7% (FY2024 為 54.5%); SG&A USD 101.6M, 占 19.9%。

### EPS 一致性核對
- FY2025 diluted EPS USD 0.42 × diluted average shares 207.5M ≈ USD 87.2M, 與 `Net Income Common Stockholders` USD 87.9M 相符 (誤差約 1%)。
- info `trailingEps` -5.14 與 `netIncomeToCommon` USD -487.2M 之間無法以目前股數 (sharesOutstanding 112.2M 或 implied 237.6M) 完全還原 (-487.2M / -5.14 ≈ 94.8M 股), 股數口徑不一致, 列為待查。

## Cashflow & balance sheet

### 現金流 (USD M)
| 年度 | 營運現金流 (OCF) | Capex | FCF | FCF 利潤率 | FCF / NI |
|---|---|---|---|---|---|
| FY2022 | -164.4 | -10.5 | -174.9 | -710.5% | n/m (NI 為負) |
| FY2023 | -79.0 | -6.6 | -85.6 | -108.7% | n/m (NI 為負) |
| FY2024 | +452.0 | -23.4 | +428.5 | +147.6% | n/m (NI 為負) |
| FY2025 | -10.1 | -382.7 | -392.8 | -77.0% | n/m (NI 含 USD 363.3M 非營業利益, FCF/NI 約 -1.65x) |

- FY2024 正向 OCF 主要來自營運資金變動 USD +443.5M (`Change In Working Capital`, 其中 other working capital USD +678.5M, 推測為客戶預收款/遞延收入增加; 性質待查), 不具可重複性。
- FY2025 capex 增至 USD 382.7M (FY2024 為 USD 23.4M, 約 16 倍), 占營收 75.0%, 為 FCF 轉負的主因。
- 2026 年 TTM 營運現金流 USD 66.3M (info `operatingCashflow`); TTM capex 與 TTM FCF: DATA_UNAVAILABLE (未取得 quarterly_cf)。
- SBC: FY2025 USD 49.8M (占營收 9.8%), FY2024 USD 58.6M。

### 資產負債表 (USD M)
| 項目 | FYE2025 (2025-12-31) | mrq (info, 2026-06-30 附近) |
|---|---|---|
| 現金及約當現金 | 701.7 | n/a (僅有 totalCash) |
| 現金 + 短期投資 | 1,108.2 | totalCash 7,921.5 (USD 7.92B) |
| 總負債 (Total Debt) | 261.8 (含租賃 USD 45.9M 流動 + USD 216.0M 非流動) | totalDebt 1,487.1 (USD 1.49B) |
| 淨現金 (現金 - 總債務) | +846.4 | +6,434.5 (USD 6.43B) |
| 總資產 | 2,326.0 | DATA_UNAVAILABLE |
| 股東權益 | -578.7 | bookValue USD 40.27/股 (推算權益約 USD 9.6B, 以 implied 股數估) |
| 優先股 (權益外) | 1,933.3 | DATA_UNAVAILABLE |
| 流動比率 | 2.15x (流動資產 1,543.6 / 流動負債 719.5) | currentRatio 5.83x |
| 速動比率 | DATA_UNAVAILABLE | quickRatio 5.17x |
| 負債權益比 | n/m (權益為負) | debtToEquity 16.2% (Yahoo 以百分比表示, 約 0.16x) |
| 營運資金 | 824.1 | DATA_UNAVAILABLE |

- FYE2025 為 IPO 前資產負債表 (權益為負, 優先股占負債大宗)。mrq 之 USD 7.92B 現金顯示 2026 年 IPO 與優先股轉換後之結構大幅改善, 但 mrq 數字來自 info 快取, 無對應季度 BS 原表可交叉核對 (quarterly_bs 未於本次取得), 列為待查。
- 交叉核對: EV 19.89B ≈ marketCap 26.33B + totalDebt 1.49B - totalCash 7.92B = 19.90B, 與 info 相符。
- 利息收入: FY2025 USD 26.8M, 為淨利中營運外收入來源之一。

## Capital allocation & insider signal

### 資本配置
- 股利: 無 (dividendYield 0.0)。
- 買回: FY2025 `Repurchase Of Capital Stock` USD -38.1M (FY2024 USD -0.1M)。Cash flow 內另有 Common Stock Payments USD -21.4M, 兩列口徑不一致, 以 USD 38.1M 為上限參考。
- 融資: FY2025 融資現金流 USD +1,026.6M, 其中優先股發行 USD 1,100M (pre-IPO 募資), 2026 年 IPO 後之募資金額 DATA_UNAVAILABLE。
- 投資: FY2025 投資活動現金流 USD -667.6M (購買投資 USD -525.4M, PPE USD -382.7M)。
- 稀釋: 歷史 diluted 股數於 FY2022–FY2025 皆為 207.5M (疑為快取固定值, 不可信), 歷史稀釋率 DATA_UNAVAILABLE。

### 內部人交易 (insider, 過去約 6 個月)
- 公開市場買入: 0 筆。
- 公開市場賣出 (Sale 文字列, 合計 USD 價值): 約 **USD 408M** (2026-06-25 至 2026-09-29), 占 marketCap USD 26.33B 約 1.6%。其中:
  - 2026-06 (06-25 至 06-30): 約 USD 20.7M
  - 2026-08 (08-14 至 08-21): 約 USD 245.3M (含 Lie Sean 08-21 之 USD 151.1M, 為單筆最大)
  - 2026-09 (09-04 至 09-29): 約 USD 142.4M (含 Mallick Dhiraj 09-29 之 USD 80.8M)
- 賣出價格區間: 約 USD 161–250 (2026 年 6 月約 161–190, 8 月約 196–250, 9 月約 195–212)。現價 USD 110.82, 較近期賣出價低約 45%。
- 主要賣方 (以 Sale 列計): Lie Sean (CTO) 約 USD 194M 賣出 (2026-06 至 09 之多筆, 含 08-21 之 USD 151.1M), Feldman Andrew (CEO) 約 USD 64M, Mallick Dhiraj (COO) 約 USD 104M (含 09-29 之 USD 80.8M), Komin Robert (CFO) USD 6.6M, Patel Yagnesh (CAO) USD 3.0M 左右, 董事 Vassallo Steven 約 USD 21M (Sale 列), 董事 Vishria Eric USD 15.7M。
- 其他非 Sale 列: 2026-05-15 因優先股轉換 (Conversion of Exercise of derivative security, 價格 279.72) 之 Benchmark / Foundation / Vassallo 大量列示 (合計約 43.4M 股), 屬轉換而非賣出, 不計入賣出金額。2026-08 之部分 Beneficial Owner 列無價格、無文字說明 (Benchmark 1.91M、Foundation 1.91M、Vassallo 1.22M 股等), 交易性質 DATA_UNAVAILABLE, 不納入統計。
- 贈與 (Stock Gift, 價格 0): 多筆 (Lie 合計約 26 萬股, Feldman 5 萬股), 不計入金額。
- 結論: 高層與董事於股價 USD 195–250 區間集中賣出, 無買入; 內部人持股比例 9.6% (heldPercentInsiders)。

## Valuation

| 指標 | 數值 | 評註 |
|---|---|---|
| 現價 | USD 110.82 | regularMarketPrice; 52 週區間 USD 106.13–386.34 |
| 市值 (marketCap) | USD 26.33B | 推算股數 237.6M (implied); 另 sharesOutstanding 112.2M 則市值約 USD 12.4B, 股數口徑待查 |
| 企業價值 (EV) | USD 19.89B | |
| Trailing P/E | n/m (EPS USD -5.14) | |
| Forward P/E | 87.0x | forwardEps USD 1.27; 但 epsCurrentYear (FY2026E) 為 USD -0.47, 共識前後不一致 |
| P/S (TTM) | 38.7x | TTM 營收 USD 680.7M |
| EV / Revenue (TTM) | 29.2x | |
| EV / EBITDA (TTM) | n/m (EBITDA USD -484.8M) | |
| P/FCF | n/m (FY2025 FCF 為負; TTM FCF DATA_UNAVAILABLE) | |
| P/OCF (TTM) | 約 397x | 26.33B / 66.3M |
| P/B | 2.75x | bookValue USD 40.27 |
| 分析師目標價 | 平均 USD 282.54 / 中位數 USD 300 / 區間 USD 175–330 | 11 位分析師, recommendationMean 1.27 (strong_buy) |
| 隱含上行 (平均目標) | 約 +155% | 目標價基準日 DATA_UNAVAILABLE, 疑似高於現價之前制定 |

- 同業中位數 (estimate, 本次無外部來源, 僅為粗估, 不可視為資料): 半導體同業 forward P/E 約 25–35x、P/S 約 6–10x、EV/Revenue 約 6–10x。CBRS 各項估值倍數明顯高於此估計區間。
- 技術面背景 (與估值相關): 現價 USD 110.82 較 50 日均線 USD 179.86 低約 38%, 較 200 日均線 USD 202.52 低約 45%。短期空單 14.1M 股, 占流通股 12.6%, days-to-cover 2.2 天 (sharesShort 2026-09 月底口徑)。
- 盤中 bid USD 81.72 / ask USD 136.62 價差極大, 市場狀態 CLOSED, 流動性與報價可靠度需再確認。

## Key catalysts
- **下次財報**: 2026-11-12 (earnings_dates, isEarningsDateEstimate=false), 共識 EPS USD -0.14。此日期在 as-of 日期之後。
- **上次財報**: 2026-08-12, 報告 EPS USD -0.05 vs 估計 USD -0.18 (surprise +74.57%); 2026-06-23 報告 EPS USD -0.04 vs 估計 USD -0.15 (surprise +73.96%)。以 EPS 而言連續兩季優於預期, 但營收與營業利益趨勢需與 Q2 營收季減及 R&D 暴增一併判讀。
- **指引 (guidance)**: DATA_UNAVAILABLE (本次資料未含公司指引文字)。
- **分部/產品組合**: DATA_UNAVAILABLE (info 僅描述為 AI compute platform, wafer-scale engine, 客戶為 hyperscalers / foundation model labs / sovereign AI, 未揭露營收分部)。
- **IPO 與禁售期**: 首次交易 2026-05-14。2026-05-15 起有優先股轉換列示, 禁售期解除 (lock-up expiration) 日期 DATA_UNAVAILABLE, 需留意後續內部人與早期股東之賣壓。
- **機構持股變動**: 最新 13F 日期 2026-06-30, 早於 8–10 月股價大幅下跌, 無法反映近期部位變化。

## Institutional holders (13F, 報告日 2026-06-30)
- 機構持股比例 80.4%, 持有機構數 556 家; 內部人持股 9.6%; 流通股機構持股 88.9%。
- 前十大持有人合計約 46.9% (以 pctHeld 加總)。

| 排名 | 機構 | 持股 (M 股) | 持股比例 | 持股市值 (USD M, 以現價估) |
|---|---|---|---|---|
| 1 | Eclipse Operations, LLC | 11.45 | 10.2% | 1,268.5 |
| 2 | FMR, LLC | 8.44 | 7.5% | 934.8 |
| 3 | Altimeter Capital Management, LP | 7.23 | 6.4% | 800.7 |
| 4 | Coatue Management LLC | 7.01 | 6.3% | 777.0 |
| 5 | Capital World Investors | 3.89 | 3.5% | 431.6 |
| 6 | Morgan Stanley | 3.22 | 2.9% | 357.3 |
| 7 | Atreides Management, LP | 3.11 | 2.8% | 344.7 |
| 8 | JPMorgan Chase & Co | 3.10 | 2.8% | 343.6 |
| 9 | Tiger Global Management, LLC | 3.00 | 2.7% | 332.3 |
| 10 | Vy Capital Management Co. Ltd. | 2.15 | 1.9% | 237.9 |

- pctChange 欄位全部為 1.0, 疑似資料格式問題, 持股增減方向 DATA_UNAVAILABLE。
- 持股市值欄位以現價 USD 110.82 反算, 非 13F 原始申報市值。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 (FY2025, USD M) | 510.0 | +75.7% | n/a (粗估 高成長半導體) | 高成長, 但 Q2 2026 季減 |
| 營收 (2026Q2, USD M) | 180.1 | +74.3% (QoQ -6.9%) | n/a | 增速仍高, 季增轉負 |
| TTM 營收 (USD M) | 680.7 | DATA_UNAVAILABLE | n/a | 規模快速擴大 |
| 毛利率 (FY2025) | 39.0% | 2024 為 42.3%, 下降 3.3pt | 約 50–60% (粗估) | 偏弱 |
| 毛利率 (2026Q2) | 14.2% | 2025Q2 為 31.1%, 下降 16.9pt | 約 50–60% (粗估) | 警示 |
| 營業利益率 (FY2025) | -28.6% | 2024 為 -34.9%, 改善 6.3pt | 約 15–25% (粗估) | 虧損, 趨勢改善 |
| 營業利益 (2026Q2, USD M) | -477.2 | 2025Q2 為 -57.2 | n/a | 警示 |
| R&D (2026Q2, USD M) | 320.2 | 2025Q2 為 60.8 (約 5.3x) | n/a | 費用急升 |
| 淨利率 (FY2025, GAAP) | +46.6% (扣除 363.3M 非營業收益約 -24.6%) | n/a | 約 10–15% (粗估) | 含一次性收益, 不可用作常態獲利 |
| ROE | n/m (FYE2025 權益為負) | n/a | 約 15% (粗估) | 無法評價 |
| ROIC | n/m | n/a | 約 10–15% (粗估) | 無法評價 |
| FCF (FY2025, USD M) | -392.8 | 2024 為 +428.5 | 正 FCF (粗估) | 警示 |
| FCF 利潤率 (FY2025) | -77.0% | n/a | 約 10–20% (粗估) | 警示 |
| FCF / NI (FY2025) | n/m (約 -1.65x, NI 含一次性收益) | n/a | >0.9 健康 | 不健康 |
| Capex (FY2025, USD M) | 382.7 | +1,535% (FY2024 為 23.4) | n/a | 大規模擴張投資期 |
| SBC (FY2025, USD M) | 49.8 | -15% (FY2024 為 58.6) | n/a | 占營收 9.8% |
| 現金 + 短期投資 (FYE2025, USD M) | 1,108.2 | n/a | n/a | 強 (IPO 前) |
| 淨現金 (mrq, info, USD B) | 6.43 | n/a | n/a | 強 (未能年報核對) |
| 總負債 (mrq, info, USD B) | 1.49 | n/a | n/a | 可控 |
| 流動比率 (mrq) | 5.83x | n/a | 約 2.0x (粗估) | 強 |
| 負債權益比 (mrq) | 0.16x (Yahoo 16.2%) | n/a | 約 0.3–0.5x (粗估) | 健康 |
| 股東權益 (FYE2025, USD M) | -578.7 | n/a | 正值 | 警示 (IPO 前) |
| Trailing P/E | n/m | n/a | 約 25–35x (粗估) | 無法評價 |
| Forward P/E | 87.0x | n/a | 約 25–35x (粗估) | 偏高 |
| P/S (TTM) | 38.7x | n/a | 約 6–10x (粗估) | 偏高 |
| EV / EBITDA (TTM) | n/m (EBITDA USD -484.8M) | n/a | 約 20–30x (粗估) | 無法評價 |
| P/FCF | n/m | n/a | 約 25–35x (粗估) | 無法評價 |
| 內部人淨買賣 (6 個月, USD M) | 淨賣出約 -408 (買入 0) | n/a | 中性 | 警示 |
| 內部人持股 | 9.6% | n/a | n/a | 中性 |
| 機構持股 | 80.4% (556 家) | n/a | 約 70–85% (粗估) | 中性偏強 |
| 股價 vs 52 週高 | -71.3% (高點 USD 386.34) | n/a | n/a | 警示 |
| 股價 52 週變動 | -64.4% | n/a | S&P 500 同期 +10.9% (SandP52WeekChange 0.109) | 大幅落後 |
| 分析師平均目標 vs 現價 | +155% (平均 USD 282.54) | n/a | n/a | 目標價偏離現價, 待查 |
| 空單占流通股 | 12.6% | 較上月 14.1M vs 13.3M, +5.9% | n/a | 偏高 |

## Red flags
- **Ticker 不符**: 任務名稱為 Caribou Biosciences, 但 CBRS 為 Cerebras Systems Inc. (半導體), 所有結論僅適用於 Cerebras。
- **現金流大幅轉負**: FY2025 FCF USD -392.8M, capex 16 倍成長至 USD 382.7M, 營運現金流幾近持平 (USD -10.1M)。
- **Q2 2026 獲利結構惡化**: 營業損失 USD -477.2M, R&D 占營收 178%, 毛利率由 Q1 的 44.6% 跌至 14.2%, 營收季減 6.9%。原因於本次資料中無法確認。
- **FY2025 獲利為一次性**: 淨利 USD +237.8M 主要來自 USD 363.3M 非營業收益, 扣除後為淨損。
- **股東權益與資本結構快速變動**: FYE2025 股東權益 USD -578.7M, 優先股占負債大宗; mrq 數字由 info 快取, 無季度 BS 原表可核對。
- **股價大幅回落**: 現價 USD 110.82, 較 50 日與 200 日均線分別低約 38% 與 45%, 52 週 -64.4%; 內部人於 USD 195–250 區間賣出, 股價隨後大幅低於賣出價。
- **內部人淨賣出**: 6 個月約 USD 408M 之 Sale 列, 無公開市場買入。
- **股數與市值口徑不一**: sharesOutstanding 112.2M / implied 237.6M / 歷史 diluted 207.5M 並存, marketCap 在 USD 12.4B 至 26.3B 之間取決於口徑, 估值倍數需以確認後之股數為準。
- **EPS 共識不一致**: forward EPS USD 1.27 與 FY2026E EPS USD -0.47 差距過大, forward P/E 87.0x 可靠度低。
- **分析師目標價偏離**: 平均目標 USD 282.54 與現價 USD 110.82 相差約 155%, 目標價之制定日期無法確認。
- **報價流動性**: 收盤後 bid USD 81.72 / ask USD 136.62, 價差極大, 價格發現可靠度低。
- **資料缺口**: 無季度現金流與季度資產負債表原表 (quarterly_cf / quarterly_bs 未取得)、無 TTM FCF、無公司指引與分部資訊、無 IPO 募資金額與禁售期日期、13F 為 2026-06-30 之舊資料。

FUNDAMENTALS REPORT COMPLETE
