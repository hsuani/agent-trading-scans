# Sentiment — QUBT as of 2026-11-17

資料狀態: 分析師與內部人資料取自 yf 工具 (成功)。Reddit (r/wallstreetbets, r/stocks) 抓取失敗; StockTwits 因網域無法解析而失敗 (需於 session 網路設定允許 api.stocktwits.com)。零售情緒無法量化, 以下僅以 WebSearch 公開新聞與評論作為替代參考。

## Analyst consensus

| 評等 | 家數 (0m) | 1m 前 | 2m 前 | 3m 前 |
|---|---|---|---|---|
| Strong Buy | 0 | 0 | 0 | 0 |
| Buy | 4 | 4 | 4 | 4 |
| Hold | 2 | 2 | 2 | 2 |
| Sell | 0 | 0 | 0 | 0 |
| Strong Sell | 0 | 0 | 0 | 0 |

目前共 4 買 / 2 持有 / 0 賣。近四個月分布完全未變, 工具未提供個別升降評等紀錄與目標價資料, 因此無法列出近期升降級或目標價調整。

第三方參考 (非券商評等): WebSearch 找到 MarketBeat 報導 2026-03-07 "Wall Street Zen" 將 QUBT 調為 sell。這屬於量化評級平台, 不計入上方家數。另有 Stockchase 報 2 買 / 0 賣, Stockalarm 報 3 家 consensus Buy, 來源家數不一致, 以 yf 數據為準。

## Retail social

- Reddit: 抓取失敗 (WebFetch 無法連線 www.reddit.com)。無樣本貼文, 無法判定 tilt。
- StockTwits / X: StockTwits 無法解析網域, 未取得訊息流。X 未取得可用貼文。WebSearch 找到 Benzinga "Bulls vs Bears" 頁面, 但未能讀取其多空比例。
- 搜尋結果中的公開評論多為媒體與新聞型內容, 非零售貼文, 不宜視為零售情緒。
- 聲量 (mention volume): 無法與平常基準比較。

Themes (取自公開新聞標題與摘要, 非零售原文):
- 估值爭論: Simply Wall St 報導 Dirac 3S 發表後出現估值爭議。
- 營收前階段與融資依賴: 評論普遍認為股價受情緒與資本取得能力主導。
- 財報事件: 搜尋結果提到 2026-11-09 盤後財報, 但未找到實際結果, 本報告無財報後反應資料。
- 股價參考: 2026-11-06 收盤約 US$5.6 至 6.3 (來源間不一致), 當日單日上漲約 12%。
- 注意: 網路上流傳 "fell 30% in November" 文章實為 2025 年 11 月的走勢, 不代表 2026 年情緒。

## Insider activity

Window: 2026-05-17 至 2026-11-17 (6 個月)。
Net 6mo: 公開市場買入 US$0.00M, 公開市場賣出 US$0.00M, 淨額 US$0.00M。

窗口內紀錄皆為授予或衍生性證券轉換, 非公開市場買賣:

| 日期 | 人員 | 職稱 | 交易 | 股數 | 金額 (US$M) |
|---|---|---|---|---|---|
| 2026-08-20 | HUANG YUPING | CEO | 股票授予 @ US$8.95 | 584,897 | 5.23 |
| 2026-08-20 | HUANG YUPING | CEO | 衍生性證券轉換 @ US$8.14 (同一批股數, 工具內重複列 3 筆) | 584,897 | 4.76 |
| 2026-05-28 | HUANG YUPING | CEO | 股票授予 @ US$0 | 58,558 | 0 |
| 2026-05-28 | DIANAT POUYA | Officer | 股票授予 @ US$0 | 24,774 | 0 |
| 2026-05-28 | BEGLIARBEKOV MILAN | COO | 股票授予 @ US$0 | 24,774 | 0 |

注意: 8/20 的授予與轉換數字疑似重複, 上表金額以單一事件 (約 US$4.8M 至 5.2M) 理解, 不應加總。

窗口外參考 (不計入 6mo):
- 2026-03-11 General Counsel ROBERTS CHRISTOPHER BRUCE 賣出 78,262 股 @ US$7.85 (約 US$0.61M)。
- 2026-01-07 COO BEGLIARBEKOV MILAN 賣出 2,860 股 @ US$11.85 (約 US$0.03M)。
- 2025 年全年以 CEO HUANG YUPING 與 CFO BOEHMLER 的賣出為主, 2025-09 起 CEO 公開市場賣出紀錄未再出現。

## Ownership shifts

| 指標 | 數值 |
|---|---|
| 內部人持股比例 | 12.89% |
| 機構持股比例 | 48.84% |
| 機構持股比例 (流通股口徑) | 56.07% |
| 持有機構家數 | 433 |

工具僅提供單一時點快照, 無法判定機構集中度的趨勢。

## Net sentiment score

Composite: 中性偏多 (信心: 低)

- 分析師面: 偏多。4 買 / 2 持有 / 0 賣, 無賣方評等, 四個月未變。
- 內部人面: 中性。窗口內無公開市場買賣, 僅有 CEO 等人的股權授予與衍生性證券轉換。
- 零售面: 無法判定 (Reddit 與 StockTwits 取不到資料)。
- 公開新聞面: 估值爭議與財報前後的不確定性並存。

信心偏低的原因: 零售情緒完全缺失, 且財報後反應未納入。

Divergence flag: 無法判定。 因零售情緒資料缺失, 無法確認零售 tilt 是否與分析師方向相反。待 Reddit 或 StockTwits 可用後應補查。

## 資料缺口與後續

1. StockTwits 需於 session 網路設定允許 api.stocktwits.com。
2. Reddit 需取得替代抓取方式, 或改用其他社群來源。
3. 2026-11-09 財報結果與之後的股價反應未取得, 應補查。
4. yf 工具未提供目標價與個別評等變動紀錄, 無法判斷分析師近期動向的細節。

## 來源

- Stockchase QUBT: https://stockchase.com/QUBT-Q
- Stockalarm QUBT analysts: https://pro.stockalarm.io/quote/QUBT/analysts
- MarketBeat, Wall Street Zen 降評 (2026-03-07): https://www.marketbeat.com/instant-alerts/wall-street-zen-downgrades-quantum-computing-nasdaqqubt-to-sell-2026-03-07/
- MarketBeat, 2026-08-21 股價快訊: https://www.marketbeat.com/instant-alerts/quantum-computing-nasdaqqubt-trading-up-75-time-to-buy-2026-08-21/
- Simply Wall St, Dirac 3S 估值爭議: https://simplywall.st/stocks/us/tech/nasdaq-qubt/quantum-computing/news/quantum-computing-qubt-unveils-dirac-3s-as-valuation-debate
- Benzinga 多空頁面 (未取得內容): https://kr.benzinga.com/quote/QUBT/sentiment

SENTIMENT REPORT COMPLETE
