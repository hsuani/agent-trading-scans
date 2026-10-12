# Sentiment — QUBT as of 2026-10-13

資料時效: 可驗證的最新資料約為 2026-08 (Wedbush 2026-08-03 評等、CEO 2026-08-20 股權授予)。2026-09 至 2026-10-13 之間未找到任何分析師評等變動或散戶討論資料。Reddit 與 StockTwits 無法取得資料，散戶情緒部分為 DATA_UNAVAILABLE。

## Analyst consensus
目前 6 位分析師: 4 buy / 2 hold / 0 sell (strongBuy 與 strongSell 皆為 0)。yfinance 的 rec_summary 與 recommendations 在 0m、-1m、-2m 三個期間數字完全相同，代表近兩個月評等分布未改變，但 recommendations 端點未回傳具日期的升降評事件，此欄位可信度有限。

近期動態 (來自 WebSearch，多來源互相有出入，需以 MarketBeat 或 Benzinga 再確認):
- Wedbush 2026-08-03 首次評等 Hold，目標價 $12。
- Rosenblatt 2026-06-29 維持 Buy，目標價 $22。
- Lake Street 2026-07-06 (另一頁顯示 06/07) 維持 Buy，目標價 $16。
- Cantor Fitzgerald 2026-06-24 維持 Hold，目標價 $10。
- 一則 Simply Wall St 頁面稱目標價於 2026-07-10 前後由 $25 上調至 $30，來源未指名，未經驗證。
- 目標價共識均值約 $18.33，區間 $10 至 $30。
- 較舊的 2025 年事件 (僅供參考): Ascendiant 2025-10-03 目標價由 $22 上調至 $40；Wall Street Zen 2025-08-16 由 hold 降為 strong sell。

價格背景 (來源不一致，僅供參考): 52 週區間約 $6.18 至 $25.84，2026-07 末附近提及 $8.15 為壓力位，2026-08 CEO 授予價為 $8.14 至 $8.95。

## Retail social
- Reddit: 無法取得。r/wallstreetbets 與 r/stocks 的 JSON 搜尋皆遭拒絕存取 (WebFetch 回報無法連線 reddit.com)。WebSearch 亦未找到近期 QUBT Reddit 討論串。
- StockTwits / X: StockTwits API 無法解析網域 (getaddrinfo ENOTFOUND)，無法取得訊息數與多空標記。X 方面 WebSearch 未回傳可用的近期貼文。
- 聲量: 無法量化，DATA_UNAVAILABLE。
- 主題 (來自新聞與分析文章，非散戶原文):
  - 板塊連動性高: 文章普遍認為 QUBT 走勢受量子運算族群整體影響，個股新聞影響有限。
  - 技術面脆弱: 一篇 Traders Union 文章認為反彈偏向情緒驅動，技術面未站回主要均線。
  - 估值敏感: 文章指出產業仍處早期，估值對投機情緒敏感。

## Insider activity
過去 6 個月 (2026-04-13 至 2026-10-13):
- 公開市場買入: 0 筆，$0。
- 公開市場賣出: 0 筆，$0。
- 股權授予與衍生性證券轉換 (非公開市場買賣，不計入淨買賣):
  - CEO Huang Yuping 2026-08-20 授予 584,897 股，價格 $8.95 (名目約 $5.23M)。
  - CEO Huang Yuping 2026-05-28 授予 58,558 股，價格 $0。
  - 營運長 Begliarbekov Milan 與 Dianat Pouya 2026-05-28 各獲授予 24,774 股，價格 $0。
  - 董事 Turmelle、Fagenson、Weimer、Shabani、Schwartz 2026-04-13 各獲授予 22,123 股，價格 $6.78 (每人約 $150K)。

6 個月窗口外的最近公開市場交易 (用於判斷趨勢):
- 總法律顧問 Roberts Christopher Bruce 2026-03-11 賣出 78,262 股，價格 $7.85 (約 $614K)；2026-03-10 行使選擇權 400,000 股，價格 $6.85。
- 2025 年多筆大額賣出 (價格明顯高於目前): CEO Huang 2025-09-04 賣出 1,000,000 股，$14.42 (約 $14.4M)；CFO Boehmler 2025-06 陸續賣出，價格 $15 至 $20。

解讀: 近 6 個月無公開市場買賣，內部人士未出現明顯買進或賣出訊號。過去一年的賣出多集中於股價 $11 以上，目前股價約 $7 至 $9，內部人士未在低點加碼，亦未在近期大量出脫。

## Ownership shifts
- 內部人持股 12.16%。
- 機構持股 47.85% (流通股占比 54.47%)，機構數 410 家。
- 無時間序列資料，無法判斷集中度趨勢。

## Net sentiment score
綜合: 中性 (neutral)，信心度低。
- 分析師端: 偏多 (4/6 Buy，目標價均值遠高於近期價格)，但近期新增評等出現 Hold (Wedbush、Cantor)，且無可驗證的 2026-09 後動態。
- 散戶端: 無資料 (Reddit、StockTwits 不可取得)。
- 內部人: 中性 (6 個月無公開市場交易，僅有授予)。

Divergence flag: 無法判定 (N/A)。因缺少散戶資料，無法確認散戶傾向是否與分析師傾向相反。

## Metrics

| 指標 | 數值 | 備註 |
|---|---|---|
| 分析師 Buy | 4 | rec_summary，0m |
| 分析師 Hold | 2 | rec_summary，0m |
| 分析師 Sell | 0 | rec_summary，0m |
| 目標價均值 | 約 $18.33 | WebSearch 聚合，未逐一驗證 |
| 目標價區間 | $10 至 $30 | WebSearch 聚合 |
| 近期評等變動 (2026) | Wedbush Hold $12 (08-03)、Rosenblatt Buy $22 (06-29)、Lake Street Buy $16 (07-06)、Cantor Hold $10 (06-24) | 來源不一致 |
| 6 個月公開市場買入 | $0 | yfinance insider |
| 6 個月公開市場賣出 | $0 | yfinance insider |
| 6 個月股權授予名目值 (非買賣) | 約 $5.5M | 授予價值，不計入淨買賣 |
| 最近一次公開市場賣出 | 2026-03-11，Roberts，78,262 股 @ $7.85 | 6 個月窗口外 |
| 內部人持股比例 | 12.16% | yfinance major_holders |
| 機構持股比例 | 47.85% | yfinance major_holders |
| 機構數 | 410 | yfinance major_holders |
| Reddit 聲量 | DATA_UNAVAILABLE | 403 類拒絕存取 |
| StockTwits 聲量 | DATA_UNAVAILABLE | 網域無法解析 |
| 散戶多空傾向 | DATA_UNAVAILABLE | 無資料 |
| 綜合情緒 | 中性 | 信心度低 |
| 背離旗標 | N/A | 缺散戶資料 |

SENTIMENT REPORT COMPLETE
