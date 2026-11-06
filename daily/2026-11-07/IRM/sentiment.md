# Sentiment — IRM (Iron Mountain Inc.) as of 2026-11-07

## Executive summary

- 分析師共識偏多：rec_summary 為 4 Strong Buy / 7 Buy / 0 Hold / 1 Sell（共 12 筆評等），yf info 的 recommendationKey 為 buy，目標價均值 $144、最高 $155、最低 $132。
- 內部人 6 個月（2026-05-07 至 2026-11-07）淨賣出約 $36.1M（18 筆賣出，約 297.5K 股），買進為 $0。CEO William Meaney 占 $27.9M，多數與 $37.00 選擇權行使成對出現，屬例行性規律賣出，訊號強度偏弱。
- 機構持股高度集中且整體偏增持：前十大機構合計約 46.2%，BlackRock、Vanguard 系列、FMR、Schwab 增持；Cohen & Steers 大減 25.7%。
- 散戶情緒資料最薄弱：本次搜尋未找到 2026 年的 r/wallstreetbets 或 r/stocks 討論串，StockTwits 與 X 無法直接讀取。現有 Reddit 討論為 2024 年的偏空盡職調查帖。
- 綜合：分析師與機構面偏多，內部人面偏賣但屬機械式，散戶面資料不足。整體評為「偏多，信心中等」。

## Data availability

| 來源 | 狀態 | 備註 |
|---|---|---|
| yf recommendations / rec_summary | 可用 | 近三個期間（0m、-1m、-2m）的評等計數，僅含計數，無券商名稱與升降評明細。yf actions 回傳空值。 |
| yf insider | 可用 | 2024-11 至 2026-11-02 共 131 筆；6 個月視窗以程式加總。 |
| yf major_holders | 可用 | 機構持股 87.1%，內部人持股 0.88%，機構數 1,588。 |
| yf inst_holders | 可用 | 前十大機構，最新季資料日期多為 2026-06-30，Dimensional 為 2026-09-30。 |
| yf info | 部分可用 | 價格 $105.5 的快照時間不明，與 2026-10-30 收盤 $116.55 及 2026-11-02 內部人賣出價 $116.96 不一致，未能確認是否為財報後價位。 |
| yf earnings_dates | 可用 | 2026-11-05 財報已公布（早於 DATE）。 |
| Reddit（r/wallstreetbets、r/stocks） | 未直接抓取 | 依指示以 WebSearch 代替。搜尋只找到 2024-08 的 WSB 討論串。 |
| StockTwits | 未取得 | 直接 API 未呼叫；WebSearch 無可用的 2026 年讀數。 |
| X / 新聞輿情 | 僅間接 | WebSearch 找到一則 SentiSense（2026-06-25 標示）的偏多讀數，但僅 1 筆提及，樣本過小。 |
| 財報後股價反應 | 未確認 | WebSearch 未找到可靠的 2026-11-05 之後股價變動資料。 |

## Retail / social sentiment read

- **Reddit**：唯一找到的主要討論串為 2024-08-19 的 r/wallstreetbets 長文，標題為 "Iron Mountain isn't worth $30 billion"（僅 2024 年資料，不代表當前情緒）。
  - 偏空論點：負債水準高、負債權益比遠高於 REIT 產業中位數、Altman z-score 偏低、相較 Digital Realty 本益比偏高，以及資料中心業務規模不足以支撐估值。
  - 反駁論點：留言者質疑把單一 AWS 資料中心拿來比較的做法；認為 REIT 應以 FFO 與股息而非 GAAP 盈餘衡量；一位產業人士指出實體紀錄儲存量因數位化而下降。
  - 傾向：偏空，但為 2024 年舊資料，時效性低。
- **StockTwits / X**：無可靠的 2026 年讀數。SentiSense 標示 IRM 為 strong bullish（SentiSense Score 100，30 日均值 28），但僅 1 筆提及。Equibles 整體標示 Neutral，聰明錢（smart money）方向有 bearish 與 neutral 兩種說法，快照日期為 8 月。
- **空方論述**：一份 Gotham 空方報告估算合理價值僅 $22 至 $40，但報告日期未明。Barchart 引述的唯一 Strong Sell 評等，目標價 $44，理由為估值與資料中心競爭。
- **聲量**：無法量化提及次數。本次搜尋未找到 2026 年散戶討論串，聲量判定為低或未知。
- **主要主題**（依 2024 舊討論與近期媒體）：負債與槓桿、估值與 FFO 倍數、資料中心轉型是否可信、實體紀錄儲存量下滑、股息覆蓋率。
- 代表性觀點：「Iron Mountain isn't worth $30 billion」（2024 WSB 帖標題）。

## Analyst consensus

- **評等分布**（rec_summary，0m）：4 Strong Buy / 7 Buy / 0 Hold / 1 Sell，共 12 筆。
- **期間變化**：-1m 為 4/7/0/1；-2m 為 4/6/0/1。近兩個月 Buy 由 6 增至 7，Strong Sell 維持 0，Sell 維持 1，總計由 11 增至 12。
- **目標價**（yf info）：均值 $144、最高 $155、最低 $132。以快照價 $105.5 計，距均值約 +36%。快照時間不明，此百分比僅供參考。
- **近期調整**（WebSearch 彙整，日期部分不一致）：Truist 目標價 $140 升至 $155（2026-08-27，Buy）；Wells Fargo 目標價 $135 升至 $140（2026-08-06，Overweight）；RBC 維持 Buy，目標價 $147（2026-08-11）；Barclays 目標價 $127 升至 $143（2026-07-01，Overweight）；JPMorgan 目標價 $121 升至 $138（2026-05-01）。
- **降評**：Wall Street Zen 於 2026-07-25 由 Buy 降為 Hold。此為非券商型量化評等機構，不計入 yf 共識。
- **財報**（yf earnings_dates）：2026-11-05 調整後 EPS $0.64，優於估計 $0.61（+4.6%）；2026-08-05 $0.60 優於 $0.56（+7.5%）；2026-04-30 $0.60 優於 $0.52（+15.8%）；2026-02-12 $0.61 優於 $0.59（+3.8%）。近四季皆為正向驚喜。
- **資料差異註記**：WebSearch 的 Q2 EPS 數字與 yf 不一致（$1.44 與 $0.60），本報告以 yf 為準。
- **單位換算**：市值約 $31.4B（297.7M 股 × $105.5 ≈ $31.4B，已核對）。

## Institutional / insider signal

**內部人（yf insider，視窗 2026-05-07 至 2026-11-07）**

| 項目 | 數值 |
|---|---|
| 買進金額（USD） | $0.0M，0 筆公開市場買進 |
| 賣出金額（USD） | $36.1M，18 筆，約 297.5K 股 |
| 最近一次公開市場買進 | 2025-11-19，董事 Kelly（$2,954，33 股），已超過 12 個月 |

主要賣方（USD）：

| 人員 | 職稱 | 6 個月賣出 | 備註 |
|---|---|---|---|
| William L. Meaney | CEO | $27.9M，6 筆（約 38.5K 股/月） | 每月賣出，多數與 $37.00 選擇權行使同日出現 |
| Mark Kidd | Officer | $3.7M，5 筆（6,000 股/月） | 固定每月約 6,000 股 |
| Greg McIntosh | Officer | $3.2M，4 筆 | 含 2026-08-06 $1.5M 大額賣出 |
| Daniel Borges | Officer | $0.9M，1 筆（2026-05-21） | |
| Pamela Arway | Director | $0.24M，1 筆（2026-05-12） | |
| Walter Rakowich | Director | $0.09M，1 筆（2026-05-20） | 另有 2026-05-01 股票贈與，非交易 |

- 解讀：CEO 與 Kidd 的賣出呈現固定月度節奏並伴隨選擇權行使，形態近似預先安排之交易計畫（10b5-1 類型），不宜直接解讀為看空。但持續且無公開買進仍為中性偏弱訊號。內部人持股僅 0.88%，持股比例低。

**機構持股（yf major_holders 與 inst_holders）**

- 機構持股比例 87.1%，持有機構數 1,588。前十大機構合計約 46.2%。

| 機構 | 持股比例 | 季末 | 較前期變化 |
|---|---|---|---|
| BlackRock | 11.28% | 2026-06-30 | +1.7% |
| Vanguard Portfolio Mgmt | 8.59% | 2026-06-30 | +2.2% |
| Vanguard Capital Mgmt | 6.37% | 2026-06-30 | +1.0% |
| State Street | 5.92% | 2026-06-30 | +0.5% |
| Cohen & Steers | 4.04% | 2026-06-30 | -25.7%（明顯減碼） |
| Geode Capital | 2.91% | 2026-06-30 | +1.9% |
| FMR | 2.64% | 2026-06-30 | +5.2% |
| Dimensional Fund Advisors | 1.57% | 2026-09-30 | +1.1% |
| Morgan Stanley | 1.49% | 2026-06-30 | -4.8% |
| Charles Schwab IM | 1.43% | 2026-06-30 | +6.2% |

- 趨勢：多數前十大機構為增持，減碼主要來自 Cohen & Steers。現有資料僅為單季快照，無法確認趨勢是否持續。

## Overall sentiment verdict

| 面向 | 判讀 | 信心 |
|---|---|---|
| 分析師共識 | 偏多（12 筆中 11 筆為買進評等，目標價均值較現價有明顯上行空間） | 高 |
| 內部人 | 偏空（機械式賣出，無公開買進），但屬例行性 | 中 |
| 機構 | 偏多（前十大多數增持，僅 Cohen & Steers 大幅減碼） | 中 |
| 散戶 / 社群 | 不確定（資料不足；2024 偏空，2026 唯一讀數偏多但樣本極小） | 低 |

- **綜合情緒評分**：偏多（bullish），信心中等。權重主要來自分析師與機構面，散戶面資料不足不納入實質加權。
- **背離旗標**：無法可靠判定。散戶方向不明，因此不構成可確認的背離。內部人淨賣出與分析師偏多之間存在輕度分歧，但內部人賣出的機械性使其參考價值有限。
- **待確認事項**：(1) 2026-11-05 財報後的實際股價反應；(2) yf info 價格快照的時間點；(3) 散戶社群（StockTwits、X、2026 年 WSB）的直接讀數。
- 本報告僅呈現情緒面資料，不提供交易建議。

## Sources

- 本地工具：`pipeline/tools/yf.py IRM` 之 recommendations、rec_summary、insider、major_holders、inst_holders、info、earnings_dates、actions（actions 回傳空值）、news（回傳空值）
- WebSearch，IRM 2026 年 11 月股票意見與情緒：[Webull AU 新聞](https://www.webull.com.au/news-detail/15394896723534848)、[Barchart 分析師評等彙整](https://www.barchart.com/story/news/3823318/iron-mountain-stock-analyst-estimates-ratings)、[Benzinga 情緒頁](https://www.benzinga.com/quote/IRM/sentiment)、[Barchart 2026-02-10 看多或看空](https://www.barchart.com/story/news/131628/iron-mountain-stock-outlook-is-wall-street-bullish-or-bearish)、[Yahoo Finance 分析師預測](https://finance.yahoo.com/news/wall-street-analysts-predicting-iron-102207821.html)
- WebSearch，r/wallstreetbets 舊討論（2024）：[r/wallstreetbets "Iron Mountain isn't worth $30 billion"](https://lr.sudovanilla.org/r/wallstreetbets/comments/1evvt1b/iron_mountain_isnt_worth_30_billion_dollars)、[MarketBeat 社群頁](https://www.marketbeat.com/stocks/NYSE/IRM/social-media/)
- WebSearch，2026 年 Q2 與 Q3 評等和目標價：[MarketBeat Q3 2026 指引（2026-08-05）](https://www.marketbeat.com/instant-alerts/iron-mountain-nyseirm-issues-q3-2026-earnings-guidance-2026-08-05/)、[JPMorgan 目標價調整（2026-05-01）](https://www.placera.se/telegram/iron-mountain-jpmorgan-adjusts-iron-mountain-price-target-to-138-from-121-20260501)、[TickerReport 共識評等](https://www.tickerreport.com/?p=13574039)
- WebSearch，散戶情緒與 SentiSense / Equibles：[SentiSense IRM 情緒](https://app.sentisense.ai/stocks/IRM/sentiment)、[Equibles IRM](https://equibles.com/stocks/IRM)

SENTIMENT REPORT COMPLETE
