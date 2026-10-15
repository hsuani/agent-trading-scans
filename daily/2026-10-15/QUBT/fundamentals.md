# Fundamentals — QUBT as of 2026-10-15

## Executive summary
QUBT (Quantum Computing Inc.) 目前仍是營收極小、毛利為負、持續燒錢的早期量子光子公司: FY2025 營收 682K USD, 2026 上半年季度營收升至 5.55M USD (Q2'26), 但 Q2'26 毛利為 -1.17M USD, 營業利益 -23.0M USD, 季度 FCF 為 -16.5M USD。財務體質的主要優勢在流動性: 截至 2026-06-30 現金及短期投資合計 954.2M USD、總負債僅約 21–23M USD, 淨現金約 933M USD, 佔市值約 65%。估值方面, 以 TTM 營收計 EV/Revenue 約 50.6x、P/S 約 145x, 但 P/B 約 0.90x, 且股價 6.31 已低於 50 日 (8.36) 與 200 日 (9.05) 均線; 以 EPS/EBITDA/FCF 計的估值倍數皆為負值, 無法作傳統 P/E 或 EV/EBITDA 比較。整體評價: 財務健康度取決於「營收與毛利率能否由負轉正」這個未被證實的前提, 目前數據支持流動性安全、獲利能力與估值無法以傳統指標支撐。

資料說明: 價格來源為 yfinance cache (feed: cnyes, cached_at 2026-10-15T11:16:58Z), 屬正常快取回退; 最新已公告財報為 2026-06-30 季度; 未發現晚於 2026-10-15 的財務數據 (下一次財報日 2026-11-09 為未來事件)。

## Revenue & profitability

**營收成長**
- 年度營收 (USD): FY2022 136K / FY2023 358K / FY2024 373K / FY2025 682K。
- 3 年 CAGR (FY2022→FY2025) 約 71.2%。FY2025 YoY +82.8% (682K vs 373K), FY2024 YoY +4.2%。
- 季度營收: Q2'25 61K / Q3'25 384K / Q4'25 198K / Q1'26 3.69M / Q2'26 5.55M。Q2'26 QoQ +50.4%, 但 Q2'26 相對 Q2'25 為數十倍級成長 (info 欄位 revenueGrowth 為 90.0, 即約 9,000% 的原始比值)。
- TTM 營收 (Q3'25–Q2'26 加總) 為 9.82M USD, 與 info.totalRevenue 9,824,000 一致。
- 分部 (segment) 營收拆分: DATA_UNAVAILABLE。工具僅提供 longBusinessSummary 的業務描述: 薄膜鈮酸鋰 (TFLN) 光子晶片、量子機器 (EQC 熵量子電腦、Emucore / Neurawave 儲蓄池運算機)、LiDAR、量子光子振動儀、量子網路與量子認證產品。各產品線的營收占比無法由工具取得。

**毛利率 (Gross margin)**
- FY2022 55.1% (75K/136K) → FY2023 45.3% (162K/358K) → FY2024 30.0% (112K/373K) → FY2025 9.8% (67K/682K)。
- 2026 季度轉為負值: Q1'26 -19.5% (-721K/3.69M), Q2'26 -21.0% (-1.17M/5.55M)。成本 (Cost of Revenue) 由 FY2025 之 615K 急升至 Q1'26 4.41M、Q2'26 6.72M, 成本增速快於營收, 顯示目前交付/產能成本尚未攤平。

**營業與淨利率**
- 營業費用: FY2025 R&D 20.47M (YoY +80.9%), SG&A 30.67M (YoY +108.2%)。Q2'26 R&D 8.43M (YoY +41%), SG&A 13.42M (YoY +218%)。
- 營業利益: FY2024 -25.94M / FY2025 -51.08M / Q1'26 -20.55M / Q2'26 -23.01M。
- 營業利益率: FY2024 約 -6,953%, FY2025 約 -7,489%, Q2'26 約 -415%, TTM 約 -775% (營業利益 -76.2M / 營收 9.82M)。
- 淨利 (Net Income): FY2024 -68.54M (含 -40.5M 證券相關損失), FY2025 -18.67M (含 +11.75M 非營業利益), Q1'26 -4.05M, Q2'26 -11.75M。Q2'25 的 -36.5M 含 -28.1M 證券損失。
- 淨利率: FY2025 約 -2,738%, Q2'26 約 -212%。
- 利息收入是本期淨虧損的主要緩衝: FY2025 利息收入 20.7M, Q1'26 13.5M, Q2'26 12.95M。Q2'26 利息收入 (12.95M) 已接近營業虧損 (23.0M) 的 56%。
- ROE (info): -1.5%; ROA (info): -4.2%。
- ROIC (推算, 營業利益 / 年末 Invested Capital): FY2025 約 -3.2% (-51.08M / 1,598.2M)。
- EPS: FY2025 Diluted EPS -0.11 (FY2024 -0.73); 季度 Q2'26 -0.05, Q1'26 -0.02。

## Cashflow & balance sheet

**現金流 (USD)**
- 營運現金流 (OCF): FY2022 -15.38M / FY2023 -18.32M / FY2024 -16.22M / FY2025 -30.29M。Q1'26 -9.42M, Q2'26 -13.87M。
- 資本支出 (Capex): FY2022 0.87M / FY2023 2.11M / FY2024 6.04M / FY2025 6.69M; Q1'26 1.82M, Q2'26 2.67M。
- 自由現金流 (FCF): FY2022 -16.25M / FY2023 -20.43M / FY2024 -22.25M / FY2025 -36.98M。季度: Q3'25 -11.52M, Q4'25 -12.17M, Q1'26 -11.25M, Q2'26 -16.54M。
- TTM FCF (Q3'25–Q2'26 加總): -51.48M。info.freeCashflow 為 -53.9M, 與季度加總有約 2.4M 差異 (見 Red flags)。
- FCF margin: FY2025 約 -5,422%; TTM 約 -524%。
- FCF / NI: 因 NI 為負, 比值無意義 (n/a)。OCF/NI 同樣 n/a。
- SBC: FY2025 8.68M (占 FCF 虧損約 23%); TTM 約 8.50M。SBC 為現金以外的主要費用來源之一。
- 季度 FCF 較上季惡化 47% (Q2'26 -16.5M vs Q1'26 -11.2M), 燒錢速度正在加快。

**資產負債表 (2026-06-30, 季度)**
- 現金及等價物 (Cash & equivalents): 189.15M; 現金 + 短期投資 (Cash, cash equivalents & STI): 954.17M (其中 Other Short Term Investments 765.02M)。
- 總資產: 1,639.2M; 總負債: 47.2M; 股東權益: 1,592.0M。
- 流動資產 988.3M / 流動負債 18.6M → Current ratio 約 53.1x (info: 53.14), Quick ratio 約 52.1x (info)。
- 營運資金 (Working capital): 969.7M。
- 總負債 (Total debt): 21.10M (季度, 較 2026-03-31 的 3.68M 顯著增加); info.totalDebt 為 23.39M。
- 淨現金 (Net cash, 以 info.totalCash 954.2M 減 totalDebt 23.4M 計): 約 930.8M; 以季度表 cash+STI 954.17M 減 debt 21.10M 計: 約 933.1M。佔市值約 65%。
- Debt/Equity: info 為 1.469 (以百分比表示, 即約 1.5%); 季度表推算約 1.3%。負債極低。
- Goodwill 由 2025-12-31 的 55.6M 增至 2026-06-30 的 181.5M; 2026 上半年 Purchase of Business 現金流出合計約 168.7M (Q1'26 99.9M, Q2'26 68.8M)。Tangible book value 由 1,536.2M (2025-12-31) 降至 1,381.5M (2026-06-30)。
- 收購標的與交易細節 (名稱、價格、併購性質): DATA_UNAVAILABLE。

## Capital allocation & insider signal

**資本配置**
- 增資 (主要資金來源): FY2025 Issuance of Capital Stock 1,475.1M; FY2024 106.8M; FY2023 24.7M。2026 上半年僅 4.3M (Q1 3.51M, Q2 0.79M)。
- 2025 年底 Investing Cash Flow -788.3M, 主要為 Purchase of Investment -1,197.9M 與 Sale of Investment +416.2M, 即將增資所得轉為短期投資; 2026 年上半年持續買入/賣出投資 (Q1 淨買入約 372.5M, Q2 淨賣出約 16.0M)。
- 股本 (Ordinary shares): 2022-12-31 56.0M → 2024-12-31 129.0M → 2025-12-31 224.2M → 2026-06-30 226.3M。2025-06-30 至 2026-06-30 股本增加 43.3%。
- 稀釋: FY2025 加權平均股數 164.5M (FY2024 93.9M, YoY +75.2%); Q2'26 稀釋股數 224.7M。
- 回購: FY2024 Repurchase of Capital Stock 4.10M (資料欄位標示為 preferred stock payments, 非普通股回購); FY2025 與 2026 年季度為 0。
- 股息: 普通股股息 0 (dividendYield 0.0); FY2023 支付 0.87M (優先股相關), FY2024 0.22M。股息覆蓋率 n/a (無普通股股息、FCF 為負)。
- 資本支出占營收: FY2025 約 980% (6.69M/0.682M), 資本支出絕對值仍小。

**內部人交易 (6 個月視窗: 2026-04-15 至 2026-10-15)**
- 視窗內無公開市場買入或賣出紀錄 (工具資料中之交易皆為 Stock Award / derivative conversion / 0 價格贈與):
  - 2026-05-28: CEO Huang Yuping 獲 58,558 股獎勵 (0 USD); COO Begliarbekov Milan 獲 24,774 股; Officer Dianat Pouya 獲 24,774 股 (皆 0 USD)。
  - 2026-08-20: CEO Huang Yuping 紀錄 Stock Award 584,897 股 (價 8.95, 約 5.23M USD) 及 derivative conversion 584,897 股 (價 8.14, 約 4.76M USD), 同日重複列示多筆。屬獎勵與衍生性證券轉換, 非市場買入。
- 淨買賣: 公開市場淨買 0 股 / 淨賣 0 股。
- 規模比較: 視窗內最大單筆 (CEO 8/20 獎勵) 約 5.2M USD, 占市值 1,428.2M 約 0.37%。
- 歷史脈絡 (視窗外): 2026-04-13 五位董事各獲 22,123 股 (6.78 USD, 約 150K USD/人); 2026-03-11 General Counsel Roberts 賣出 78,262 股 (7.85 USD, 約 614K USD); 2025 年 CEO Huang 於 2025-09-04 賣出 1,000,000 股 (14.42 USD, 約 14.4M USD), 2025-05-19 賣出 500,000 股 (11.70 USD)。近期內部人信號偏中性, 2025 年高價區的大額賣出與 2026 年低價區的獎勵形成對照。
- 內部人持股比例 (major_holders): 12.16%。

**機構持股 (tool 提供, 2026-06-30 季報)**
- 機構持股比例 47.94%, 持有機構數 410。Short % of float 33.6% (info)。
- 前幾大持有人: BlackRock 17.73M 股 (欄位 pctHeld 61.03%); Vanguard Capital Mgmt 8.85M (30.45%); Defiance ETFs 7.03M (24.21%, 季度增 56.5%); Penserra Capital 6.98M (24.02%, 增 108.4%); Vanguard Portfolio Mgmt 6.57M (22.6%); Geode 5.32M (18.32%); State Street 4.92M (16.94%); Morgan Stanley 3.29M (11.33%, 增 41.8%); Marex 2.30M (7.92%, 減 48.7%); Mirae Asset 2.27M (7.82%)。
- 單一持股百分比加總遠超 100%, 與 major_holders 的 institutionsPercentHeld 47.94% 不一致, 屬資料品質問題, 僅供方向性參考 (見 Red flags)。

## Valuation

價格與市值 (cache, cnyes feed):
- 最新價 6.31 USD (前收 6.87, 當日 -8.2%; 日高 6.73, 日低 6.30)。52 週區間 6.18–21.44。
- 50 日均線 8.36、200 日均線 9.05; 股價低於兩條均線。平均 10 日成交量 6.80M 股; 平均成交量 7.67M 股。
- 市值 1,428.2M USD (流通股數 floatShares 200.6M, 發行股數 226.3M)。
- Enterprise Value 497.5M USD (市值 - 現金 + 債務, 與 info.enterpriseValue 一致)。
- Beta 3.75。

估值倍數:
- Trailing P/E: n/a (TTM EPS -0.05, 負值)。
- Forward P/E: -26.7x (forwardEps -0.237, 負值, 不具比較意義)。
- EV/EBITDA: -8.1x (TTM EBITDA -61.1M, 負值, 不具比較意義)。
- EV/Revenue (TTM): 50.6x。
- P/S (TTM): 145.4x。
- P/FCF: n/m (TTM FCF 為負, -51.5M 季度加總或 -53.9M info)。
- P/B: 0.90x (book value/share 7.03)。
- 同業/產業中位數 (sector median): DATA_UNAVAILABLE, 工具無同業數據, 不做估計數字。

分析師共識 (info, 6 位分析師): 目標均價 18.67, 最高 32.0, 最低 10.0; recommendationKey 為 none。以目標均價計相對 6.31 約 +196%。此為分析師預估, 不代表本報告之投資建議。

估值判讀 (定性): 市值約為淨現金的 1.5 倍, 企業價值 (EV) 僅約市值的 35%, 但營收基數 (TTM 9.8M) 極小, 估值高度依賴營收放量與毛利轉正的時程, 目前傳統獲利倍數無法使用。

## Key catalysts
- 下一次財報: 2026-11-09 (earnings_dates 列示, 共識 EPS -0.06)。此日期晚於 as-of 日期 2026-10-15。
- 近期財報表現 (earnings_dates 的 Reported EPS 與共識比較): 2026-08-10 (Q2'26) 報 -0.04 vs 估計 -0.05 (+16.0%); 2026-05-11 (Q1'26) 報 -0.03 vs 估計 -0.05 (+35.4%); 2026-03-02 報 -0.04 vs -0.04 (+1.3%); 2025-11-14 報 0.07 vs -0.05 (+239.4%, 含非營業利益影響)。過去 4 季皆優於共識 EPS, 但 EPS 口徑 (含/不含非營業項目) 與財務報表不一致, 見 Red flags。
- 近期指引 (guidance): DATA_UNAVAILABLE (工具未提供管理層指引與營收預測)。
- 營收結構轉變: Q1'26 起營收由個位數 K 躍升至 M 級, 但毛利為負; 下一季若毛利率仍負值, 將是基本面的主要監控點。
- 併購與商譽: 2026 上半年 Goodwill 大幅增加 (約 +126M), 併購標的與整合進度 DATA_UNAVAILABLE。
- 增資與稀釋風險: 2025 年籌資 1.48B USD, 2026 年上半年 OCF/FCF 燃燒與股本增長 (43% YoY), 後續融資節奏未知。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 (FY2025, USD) | 682K | +82.8% | DATA_UNAVAILABLE | 成長快但基數極小 |
| 營收 (Q2'26, USD) | 5.55M | QoQ +50.4%; YoY 約 +9,000% (base 61K) | DATA_UNAVAILABLE | 放量明確 |
| 營收 3Y CAGR (FY22–FY25) | 71.2% | n/a | DATA_UNAVAILABLE | 成長高 |
| 毛利率 (Q2'26) | -21.0% | 由 Q2'25 的 42.6% (26K/61K) 轉負 | DATA_UNAVAILABLE | 不健康 |
| 毛利率 (FY2025) | 9.8% | FY2024 30.0%, 下降 20.2pp | DATA_UNAVAILABLE | 不健康 |
| 營業利益率 (Q2'26) | -414.5% | Q2'25 約 -16,675% (-10.17M/61K) | DATA_UNAVAILABLE | 不健康 |
| 淨利率 (Q2'26) | -211.7% | n/a | DATA_UNAVAILABLE | 不健康 |
| ROE (info) | -1.5% | n/a | DATA_UNAVAILABLE | 偏弱 |
| ROA (info) | -4.2% | n/a | DATA_UNAVAILABLE | 偏弱 |
| ROIC (推算, FY2025) | -3.2% | FY2024 約 -24.2% (-25.94M / FY2024 Invested Capital 107.3M) | DATA_UNAVAILABLE | 偏弱 |
| TTM FCF | -51.5M | FY2024 TTM 不可比 (FY2025 FCF -37.0M vs FY2024 -22.2M, 惡化 66%) | DATA_UNAVAILABLE | 燒錢加快 |
| FCF margin (TTM) | -524% | n/a | DATA_UNAVAILABLE | 不健康 |
| FCF / NI | n/a (NI 為負) | n/a | DATA_UNAVAILABLE | 無法評估 |
| 現金 + STI (2026-06-30) | 954.2M | 2025-12-31 為 1,117.3M, 下降 14.6% | DATA_UNAVAILABLE | 流動性充足 |
| 淨現金 (cash+STI - debt) | 約 933M | 2025-12-31 約 1,115M | DATA_UNAVAILABLE | 強 |
| Total debt (2026-06-30) | 21.1M (info 23.4M) | 2025-12-31 為 1.8M, 增加 | DATA_UNAVAILABLE | 低, 但上升中 |
| Current ratio | 53.1x | 2025-12-31 約 102x (1,133.7M/11.1M) | DATA_UNAVAILABLE | 極高 |
| Debt / Equity | 約 1.5% (info 1.469) | n/a | DATA_UNAVAILABLE | 極低 |
| 股本 (shares out) | 226.3M | +43.3% (vs 2025-06-30) | DATA_UNAVAILABLE | 稀釋中 |
| 資本支出 (FY2025) | 6.69M | +10.8% (vs 6.04M) | DATA_UNAVAILABLE | 小額 |
| 股息 / 回購 | 0 / 0 (2025) | n/a | DATA_UNAVAILABLE | 無資本回報 |
| 內部人淨買賣 (6mo, 公開市場) | 0 股 (僅獎勵) | n/a | DATA_UNAVAILABLE | 中性 |
| 機構持股比例 | 47.9% | n/a | DATA_UNAVAILABLE | 正常 |
| Short % of float | 33.6% | n/a | DATA_UNAVAILABLE | 高, 需留意 |
| Trailing P/E | n/a (EPS 負) | n/a | DATA_UNAVAILABLE | 無法比較 |
| Forward P/E | -26.7x (負值) | n/a | DATA_UNAVAILABLE | 無法比較 |
| EV/EBITDA (TTM) | -8.1x (負值) | n/a | DATA_UNAVAILABLE | 無法比較 |
| EV/Revenue (TTM) | 50.6x | n/a | DATA_UNAVAILABLE | 極高 |
| P/S (TTM) | 145.4x | n/a | DATA_UNAVAILABLE | 極高 |
| P/FCF | n/m (FCF 負) | n/a | DATA_UNAVAILABLE | 無法比較 |
| P/B | 0.90x | n/a | DATA_UNAVAILABLE | 低於帳面價值 |
| 最新價 / 52 週區間 | 6.31 / 6.18–21.44 | 較 52 週高點 -70.6% | DATA_UNAVAILABLE | 處於年低 |
| 50 日 / 200 日均線 | 8.36 / 9.05 | 股價低於兩者 | DATA_UNAVAILABLE | 弱勢 |
| 分析師目標均價 | 18.67 (6 位) | 相對現價 +196% | DATA_UNAVAILABLE | 分歧大 (低 10, 高 32) |

## Red flags
- 毛利率由 FY2022 的 55.1% 連續下滑至 FY2025 的 9.8%, 2026 年季度已轉為負值 (Q2'26 -21.0%)。營收規模擴大並未帶來毛利改善, 成本增速 (Q2'26 Cost of Revenue 6.72M) 高於營收增速 (QoQ +50%) 的同時毛利反而減少 (Q1 -0.72M → Q2 -1.17M)。
- 季度 FCF 惡化: Q2'26 -16.5M, 較 Q1'26 的 -11.2M 增加 47%; FY2025 FCF -37.0M, 較 FY2024 -22.2M 惡化 66%。
- 持續稀釋: 股本 2025-06-30 至 2026-06-30 增加 43.3%, FY2025 加權股數較 FY2024 增加 75.2%。融資依賴度高 (FY2025 籌資 1.48B USD), 未來若再融資, 可能進一步稀釋。
- 商譽與併購擴張: Goodwill 由 55.6M 增至 181.5M, 2026 上半年併購現金流出約 168.7M, 但併購標的與整合績效無法由工具驗證。Tangible book value 下降至 1,381M。
- 獲利依賴利息收入: 淨利多次受非營業證券損益影響 (2024 年 -40.5M, 2025 年 +11.75M, 2025 Q2 -28.1M), 且利息收入 (Q2'26 12.95M) 占淨虧損的主要緩衝, 利率下行將直接削弱此緩衝。
- 短期投資佔比: cash+STI 中約 80% 為 Other Short Term Investments (765M), 其流動性與估值依賴投資組合公允價值, 需以季報附註確認。
- 空頭比例高: Short % of float 33.6%, 股價 1 日 -8.2%、低於 50/200 日均線、Beta 3.75, 波動風險高。
- 資料品質問題 (需人工核對):
  - info.debtToEquity 1.469 與季度表推算之 Debt/Equity 約 1.3% 不一致 (info 使用 totalDebt 23.4M, 季度表 21.1M)。
  - info.freeCashflow -53.9M 與季度 FCF 加總 -51.5M 不一致。
  - info.trailingEps -0.05 與季度 diluted EPS 加總 (0.01-0.01-0.02-0.05 = -0.07) 不一致; earnings_dates 的 Reported EPS (Q2'26 -0.04, Q1'26 -0.03) 與 quarterly_fin 的 diluted EPS (Q2'26 -0.05, Q1'26 -0.02) 不一致, 疑為 adjusted vs GAAP 口徑差異。
  - info.forwardEps -0.237 (較 trailing -0.05 更負) 與季度趨勢需人工核對; forward P/E 為負。
  - major_holders 機構比例 47.9%, 但 inst_holders 前幾大持股 pctHeld 加總遠超 100%。
  - 2025-03-31 與 2025-06-30 以前的季度資料 (Q1'25) 缺漏; 2021 年財報欄位全為 null。
- 無分部營收拆分、無管理層指引、無同業中位數, 無法完成完整的分部與同業比較。
- 不構成交易建議。本報告僅呈現基本面數據與風險, 交易決策由 trader 依整體研究判斷。

FUNDAMENTALS REPORT COMPLETE
