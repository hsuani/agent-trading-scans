# Fundamentals — NBIS as of 2026-11-09

資料說明: 本報告以 `pipeline/tools/yf` 輸出為準 (source 皆為 "cache", cached_at 2026-11-08 13:11–13:16 UTC, 無 2026-11-09 之後的資料)。金額單位: USD, 以 B (十億美元) / M (百萬美元) 標示; 本報告無 TWD / KRW 金額。Q2'26 指 2026-06-30 季度, Q3'26 尚未公布。

## Executive summary
Nebius (NBIS) 營收爆發式成長 (FY25 營收 0.53B, 較 FY24 的 0.09B 成長約 479%, 約 5.8 倍; Q2'26 營收 0.58B, 年增約 454%), 但仍處於大規模資本支出階段: TTM FCF 約 -5.88B, 同期 TTM 營運現金流 +5.26B 被 11.14B 資本支出完全吞掉, 財務體質高度依賴外部融資 (2025 年至 2026 年上半年股權與債務合計募資約 12.5B USD)。估值方面, 以 TTM 營收計 P/S 約 26x、EV/Sales 約 28x, TTM 淨利僅 0.04B 且含 Q1'26 約 0.78B 一次性證券處分利益, 傳統 P/E 與 forward P/E 均不具參考性; 分析師平均目標價 281 USD 相較現價 129.49 USD 有極大價差, 但 20 位分析師評級 key 為 "none", 此目標價僅作為市場共識參考。內部人 6 個月以淨賣出為主 (賣出約 303M USD, 買進僅約 0.26M USD), 財務健康度評估為「營運槓桿高、現金消耗極重、高度資本依賴」。

## Revenue & profitability

**營收趨勢 (USD B)**: FY22 0.0135 → FY23 0.0098 → FY24 0.0915 → FY25 0.5298。
- 3 年 CAGR (FY22–FY25) 約 240% (基期極低, 數字僅供參考; FY23 營收較 FY22 下滑, 歷史資料可能受 Yandex 分拆影響)。
- 季度趨勢 (USD M): Q2'25 105.1 → Q3'25 146.1 → Q4'25 227.7 → Q1'26 399.0 → Q2'26 582.3。Q2'26 年增約 454%, 季增約 46%。
- TTM 營收 (Q3'25–Q2'26) 1,355.1M, 與 info.totalRevenue 一致, 已交叉驗證。
- 分部營收 (segment mix): DATA_UNAVAILABLE。longBusinessSummary 僅描述業務為 AI 全端基礎設施 (GPU 叢集、雲端平台、開發者工具), 另有 TripleTen (edtech) 與 Avride (自駕/配送機器人), 但工具未提供各分部營收占比。

**獲利能力**:
- 毛利率: FY25 68.6% (363.6 / 529.8); Q2'26 77.1% (448.7 / 582.3); TTM 74.3% (與 info.grossMargins 0.7426 一致)。毛利率改善明顯。
- 營業利益率: FY25 -115.5% (營業利益 -611.7M); Q2'26 -30.2% (-175.9M); TTM -50.5% (-684.1M)。注意: yfinance info.operatingMargins 顯示 -0.22%, 與由損益表推算之 -50.5% 不一致, 本報告採用損益表推算值。
- 淨利率: FY25 15.6% (淨利 82.5M, 但由一次性證券處分利益 681.3M 拉高, 持續營運淨利 Normalized Income 為 -473.9M); Q1'26 淨利 621.2M 含 780.6M 證券處分利益; Q2'26 淨損 -190.4M。TTM 淨利 42.4M (淨利率 3.1%) 不反映核心營運。
- ROE: info 0.60% (TTM 淨利 42.4M / 平均權益); 由 TTM 淨利 / 期末權益 10,339.5M 推算約 0.41%。ROE 接近零是因為盈餘受一次性利益支撐, 非持續獲利。
- ROIC: 工具未直接提供。以 TTM 營業利益 / Q2'26 invested capital (18,885.2M) 粗估約 -3.6%, 僅為方向性參考。
- 研發費用: FY25 177.3M (Q2'26 單季 191.0M); SG&A FY25 380.1M。折舊與攤提 (D&A) 快速攀升: FY25 417.9M → Q2'26 單季 259.7M, 反映 GPU/資料中心資產的折舊壓力。

## Cashflow & balance sheet

**現金流量 (USD B)**:

| 期間 | 營運現金流 (OCF) | 資本支出 (Capex) | 自由現金流 (FCF) | FCF / NI |
|---|---|---|---|---|
| FY22 | 0.697 | -0.015 | 0.682 | n/m (淨利 0.746, 含處分收益) |
| FY23 | 0.830 | -0.083 | 0.747 | n/m (淨利 0.241) |
| FY24 | 0.246 | -0.808 | -0.562 | n/m (淨利 -0.641) |
| FY25 | 0.385 | -4.066 | -3.681 | -44.6x (淨利 0.083) |
| TTM (Q3'25–Q2'26) | 5.258 | -11.142 | -5.884 | n/m (淨利 0.042) |
| Q2'26 單季 | 2.246 | -5.657 | -3.411 | n/m |

- FCF 利潤率 (TTM): -434%。FCF / NI 比率遠低於 0.9 健康門檻, 且為負值, 不健康。
- Q1'26 與 Q2'26 OCF 的主要來源為營運資金變動 (Q1 +2.12B、Q2 +2.03B), 其性質 (如客戶預付款、應收帳款變化等) 工具未提供, 需進一步確認其可持續性。Q2'26 應收帳款由 Q1 的 1,479.2M 降至 288.6M, 與營運資金大幅回收相符。
- 資本支出強度: FY25 capex 占營收 767%; Q2'26 單季 capex 5,657.4M 為營收 582.3M 的約 9.7 倍。

**資產負債表 (USD B, Q2'26 為最新季度)**:
- 現金及約當現金 + 短期投資: 8.04 (YE25 3.68; Q1'26 9.30)。
- 總負債 (Total Debt): 10.17 (YE25 4.97, 半年內增加約 5.2B; 其中長期負債 8.50、資本租賃負債 1.63、短期負債 0.05)。
- 淨負債 (由 Total Debt - 現金推算): 約 2.13B。注意: yfinance 的 Net Debt 欄位顯示 Q2'26 為 0.50B, 與其自身 Total Debt 與現金的差額不符, 本報告採用推算值 2.13B。
- 股東權益 10.34B (YE25 4.59B), 有形帳面價值 9.65B。
- 負債 / 權益 (D/E): 約 98% (info debtToEquity 98.6)。
- 流動比率: 4.03 (流動資產 9.62B / 流動負債 2.39B); 營運資金 7.23B。短期償債能力不是問題, 長期槓桿上升才是重點。
- 利息支出: Q2'26 119.1M (Q2'25 僅 4.8M), TTM 約 239.5M; 利息收入 TTM 約 58.0M。EBIT 為負, 利息保障倍數 n/m。

## Capital allocation & insider signal

**資本配置**:
- 股利: 無 (dividend yield 0.0%)。
- 買回: 2023–2025 年度無買回 (Repurchase 為 0 或 null); 2021 年買回 93.4M。目前庫藏股數量已由 YE24 的 126.3M 股降至 YE25 的 69.0M, 但 Q2'26 的 treasury 欄位為 null, 無法確認當期狀態。
- 資本支出: 呈指數成長, FY22 14.6M → FY23 82.9M → FY24 807.5M → FY25 4,066.0M → TTM 11,141.8M。
- 股權與債務募資 (USD B):
  - 股權募資: FY24 0.70、FY25 1.15、Q2'26 2.85。
  - 債務募資: FY25 4.16 (Q2'25 1.00、Q3'25 3.16、Q1'26 4.34、Q2'26 0)。
- 股本稀釋: 流通股數 (ordinary shares) 由 FY24 235.8M 增至 FY25 253.0M (+7.3%), 再增至 Q2'26 271.9M (半年內再增約 7.4%)。Q2'26 加權稀釋股數 280.4M。以目前股價 129.49 計, 市值約 35.20B (隱含股數 271.9M, 與 Q2'26 股數一致)。

**內部人交易 (最近 6 個月, 2026-05-08 至 2026-11-08)**:
- 賣出: 26 筆, 10 位內部人, 合計約 303.1M USD, 約占市值 0.86%。
  - 主要賣方: COO Ophir Nave (2026-10-05, 500,000 股, 約 117.8M USD); Director Charles E. Ryan (2026-08-14, 50,000 股, 約 13.3M USD); CEO Arkady Volozh (2026-07-01, 46,627 股, 約 11.0M; 2026-10-01 另 37,778 股, 約 8.8M); Andrey Korolenko (2026-07-01 與 10-01 合計約 14.8M); CTO Danila Shtan (2026-07-01 與 10-01 合計約 7.4M); Marc Boroditsky 多筆 (2026-07-15 約 5.5M 等)。
  - 賣出價格區間 約 164–277 USD (2026-08 至 10 月), 與目前 129.49 相比高於市價約 27%–114%。
- 買進: 4 筆, 全部為 Director Arne Grimme (2026-10-19 至 10-28), 合計約 0.26M USD, 金額極小。
- 其他: 2026-09-01 董事與管理層有例行股票獎勵 (每人 1,352 股, 0 價格), 非市場交易。
- 判讀: 6 個月內以淨賣出為主, 賣出規模約為市值 0.9%, 絕對金額大但相對市值不大; 因資料未標示 10b5-1 計畫, 無法區分計畫性與主動性賣出。買進僅一位獨立董事之小額買進, 信號偏弱。

**持股結構**: 機構持股 70.8%, 內部人持股 3.4%, 機構數 1,467。前五大: BlackRock 5.25% (季增 16%)、Goldman Sachs 4.47% (季增 218%)、Invesco 3.16%、Orbis Allan Gray 2.96%、Bank of America 2.80%。做空比例: 流通股 20.2% (short ratio 2.61 日)。

## Valuation

| 指標 | 數值 | 說明 |
|---|---|---|
| 市值 (market cap) | 35.20B | 129.49 × 271.9M 股 |
| 企業價值 (EV) | 37.65B | info.enterpriseValue |
| P/S (TTM) | 25.98x | 市值 / TTM 營收 1.355B |
| EV/Sales (TTM) | 27.8x | |
| EV/EBITDA (TTM) | 145.9x | 以 info EBITDA 258M 計; 季度 EBITDA 含一次性利益, 口徑不一 |
| P/E (TTM) | 101.2x | info trailingPE; trailingEps 1.28 與季度稀釋 EPS 加總 (約 0.00) 不一致, 不可靠 |
| P/E (TTM, 以淨利計) | 約 830x | 35.20B / TTM 淨利 0.042B |
| Forward P/E | n/a | forwardPE 為負 (forwardEps -3.60, epsCurrentYear -2.10), 無意義 |
| P/B | 3.43x | bookValue 37.72 USD |
| P/FCF | n/m | TTM FCF 為負 |
| PEG | 0.29 (info) | 因 forward EPS 為負, 不具參考性 |
| 同業 / 行業中位數 | DATA_UNAVAILABLE | 工具未提供 sector / industry 中位數資料, 不予估算 |

- 股價位置: 現價 129.49 (cache, 2026-11-08); 52 週高 299.86 (下跌約 57%), 52 週低 73.52; 50 日均線 201.70, 200 日均線 178.38, 現價分別低於兩線約 36% 與 27%。
- Beta 1.539。
- 分析師: 20 位, 目標價 最低 84 / 中位數 302 / 平均 281 / 最高 410 USD; 平均目標價相較現價約 +117%。recommendationKey 為 "none", 無明確買賣評級共識。

## Key catalysts
- **Q3'26 財報 (2026-11-12, 盤前或盤中, 未公布)**: 距離分析基準日 (2026-11-09) 約 3 天。EPS 預估 -1.24 (earnings_dates)。Q2'26 EPS -0.68 相較預估 -0.86 優於 21%; Q1'26 EPS 2.11 相較預估 -0.71 為大幅超預期, 但主要來自一次性證券處分利益 780.6M; Q4'25 EPS -0.99 vs 預估 -0.60 (不及預期 63%)。
- **營收動能**: Q2'26 營收 582.3M (季增 46%); 關鍵在於 Q3'26 營收能否延續高速成長, 工具未提供營收預估 (DATA_UNAVAILABLE)。
- **資本支出與融資**: Q2'26 單季 capex 5.66B、TTM capex 11.14B。後續融資 (債務、股權) 規模與條件、以及 capex 是否持續放大, 是最大的財務不確定性。
- **債務結構**: 總負債半年內由 4.97B 增至 10.17B, 利息支出 Q2'26 達 119.1M。新增債務的利率與到期結構工具未提供 (DATA_UNAVAILABLE)。
- **公司指引 (guidance)**: DATA_UNAVAILABLE。工具輸出未包含管理層的營收或 capex 指引。
- **分析師目標價 / 評級變化**: 目標價區間極大 (84–410 USD), 近期評級變動未提供 (DATA_UNAVAILABLE)。
- **命名變更**: info.nameChangeDate 為 2026-11-07, prevName 為 Yandex N.V.; 工具未說明對財務揭露的影響。

## Metrics table

金額單位: USD (B / M), 比率為 %, 倍數為 x。Sector median 全部為 DATA_UNAVAILABLE。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 (Q2'26, USD M) | 582.3 | +454% (vs Q2'25 105.1) | DATA_UNAVAILABLE | 高速成長 |
| 營收 (TTM, USD B) | 1.355 | FY25 +479% (vs FY24 0.0915) | DATA_UNAVAILABLE | 高速成長, 基期低 |
| 毛利率 (TTM) | 74.3% | FY25 68.6% (FY24 52.2%, +16.4 pts) | DATA_UNAVAILABLE | 良好, 持續改善 |
| 營業利益率 (TTM) | -50.5% | FY25 -115.5% | DATA_UNAVAILABLE | 仍深度虧損, 但改善中 |
| 淨利率 (TTM) | 3.1% | n/m | DATA_UNAVAILABLE | 失真, 由一次性利益支撐 |
| ROE (info) | 0.6% | n/a | DATA_UNAVAILABLE | 弱 |
| ROIC (粗估) | -3.6% | n/a | DATA_UNAVAILABLE | 弱 |
| 營運現金流 (TTM, USD B) | 5.258 | n/a | DATA_UNAVAILABLE | 受營運資金推動, 品質存疑 |
| 資本支出 (TTM, USD B) | 11.142 | FY25 +404% (vs FY24 0.808) | DATA_UNAVAILABLE | 極高, 占營收約 822% |
| 自由現金流 (TTM, USD B) | -5.884 | FY25 -3.681 | DATA_UNAVAILABLE | 嚴重負值 |
| FCF 利潤率 (TTM) | -434% | n/a | DATA_UNAVAILABLE | 極弱 |
| FCF / NI (FY25) | -44.6x | n/a | 0.9 (健康門檻) | 不健康 |
| 現金及短期投資 (Q2'26, USD B) | 8.04 | Q2'25 1.68 → +379% | DATA_UNAVAILABLE | 流動性充足 |
| 總負債 (Q2'26, USD B) | 10.17 | YE25 4.97 (半年 +104%) | DATA_UNAVAILABLE | 槓桿快速上升 |
| 淨負債 (推算, USD B) | 2.13 | n/a | DATA_UNAVAILABLE | 中度, 需留意成長 |
| D/E | 98% | YE25 ~108% | DATA_UNAVAILABLE | 偏高 |
| 流動比率 | 4.03x | n/a | DATA_UNAVAILABLE | 健康 |
| 股利殖利率 | 0.0% | n/a | DATA_UNAVAILABLE | 無股利 |
| 流通股數 (M) | 271.9 | YE25 253.0 (+7.4% 半年) | DATA_UNAVAILABLE | 稀釋中 |
| 股權募資 (TTM, USD B) | 3.996 (Q3'25 1.15 + Q2'26 2.85) | FY25 1.15 | DATA_UNAVAILABLE | 依賴股權融資 |
| 內部人 6 個月淨交易 (USD M) | 淨賣出約 303 (買進 0.26) | n/a | DATA_UNAVAILABLE | 偏空 (弱) |
| 機構持股比例 | 70.8% | n/a | DATA_UNAVAILABLE | 高 |
| 做空比例 (流通股) | 20.2% | n/a | DATA_UNAVAILABLE | 高 |
| P/E (TTM, info) | 101.2x | n/a | DATA_UNAVAILABLE | 不可靠 |
| Forward P/E | n/a (EPS 為負) | n/a | DATA_UNAVAILABLE | 無法評估 |
| P/S (TTM) | 25.98x | n/a | DATA_UNAVAILABLE | 極高 |
| EV/EBITDA (TTM, info) | 145.9x | n/a | DATA_UNAVAILABLE | 極高 |
| P/B | 3.43x | n/a | DATA_UNAVAILABLE | 偏高 |
| 分析師平均目標價 (USD) | 281 (中位數 302) | 現價 129.49, 價差 +117% | DATA_UNAVAILABLE | 分歧大, 參考性有限 |
| Beta | 1.54 | n/a | DATA_UNAVAILABLE | 高波動 |

## Red flags
- **FCF 嚴重為負**: TTM FCF -5.88B, FY25 -3.68B; 營運現金流完全無法覆蓋 capex (TTM capex 11.14B vs OCF 5.26B), 成長高度依賴外部融資。
- **融資規模急速擴張**: 總負債半年內由 4.97B 增至 10.17B, Q2'26 利息支出 119.1M (較 Q2'25 增加約 25 倍); 利息覆蓋比率為負。
- **股權稀釋**: 流通股數 半年內 +7.4%; Q2'26 股權募資 2.85B; 持續發行股份將壓抑每股價值。
- **獲利品質低**: TTM 淨利 42.4M 幾乎全由一次性證券處分利益 (Q1'26 780.6M, Q2'25 622.4M 等) 支撐, 持續營運虧損 (Normalized Income FY25 -473.9M)。
- **營運現金流品質存疑**: Q1'26、Q2'26 OCF 合計 4.50B 中, 營運資金變動貢獻約 4.15B, 其性質需確認。
- **內部人 6 個月淨賣出約 303M USD**: 大額賣出集中於 COO 與 CEO/CTO 等高層, 買進僅 0.26M USD。
- **股價大幅回落**: 現價 129.49, 較 52 週高點 299.86 下跌約 57%, 低於 50 日與 200 日均線; 內部人在 230–277 USD 區間賣出後股價已大幅低於其成交價。
- **估值極度依賴成長敘事**: P/S 約 26x, EV/EBITDA 約 146x, forward EPS 為負; 任何營收增速放緩或融資成本上升都可能造成估值重估。
- **資料一致性問題 (需交易員注意)**:
  - info.freeCashflow (-9.61B) 與損益表與現金流量表推算之 TTM FCF (-5.88B) 不一致, 本報告採用報表推算值。
  - info.operatingMargins (-0.22%) 與推算 TTM 營業利益率 (-50.5%) 不一致。
  - info.trailingEps (1.28) 與季度稀釋 EPS 加總 (約 0.00) 及 TTM 淨利/股數 (約 0.16) 不一致。
  - yfinance Net Debt (Q2'26 0.50B) 與 Total Debt 減現金 (2.13B) 不一致。
  - info.ebitda (258M) 與季度 EBITDA 加總 (約 1,156M, 含一次性利益) 口徑不一。
  - fast_info 的 market_cap、50/200 日均線、52 週高低為 null 或 NaN; 本報告改用 info 欄位。
- **資料缺口**: 分部營收、公司指引、sector 中位數、營收預估、債務條款與利率、分析師評級變動 均為 DATA_UNAVAILABLE。
- **價格時效**: 現價 129.49 為 cache 資料 (cnyes feed, 2026-11-08 13:11 UTC), 非 2026-11-09 即時報價, 交易前需由交易員確認實際價格。
- 財報 (Q3'26, 2026-11-12) 尚未公布, 屬於後續事件風險。

FUNDAMENTALS REPORT COMPLETE
