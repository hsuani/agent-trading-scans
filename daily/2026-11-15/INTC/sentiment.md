# Sentiment — INTC as of 2026-11-15

資料截止：2026-11-15。2026-11-15 之後的資料一律視為未知。Yahoo cookie/crumb 取得失敗，yf 工具以 repo cache 提供評等、內部人、持股資料，屬預期情況。

## Analyst consensus
目前 49 位分析師（rec_summary, 0m）：Buy 14（Strong Buy 2 + Buy 12）/ Hold 34 / Sell 1（Strong Sell 0）。
**BUY% = 28.6%**，Hold 69.4%，Sell 2.0%。

| 期間 | Buy 含 Strong Buy | Hold | Sell 含 Strong Sell | BUY% |
|---|---|---|---|---|
| 本月 (0m) | 14 | 34 | 1 | 28.6% |
| 上月 (-1m) | 12 | 36 | 1 | 24.0% |
| -2m | 15 | 32 | 2 | 30.6% |
| -3m | 14 | 32 | 2 | 29.2% |

- 近三個月 BUY% 在 24%–31% 之間，沒有明顯方向性變化，整體以 Hold 為主。
- Recent moves：`recommendations` 工具只回傳月度彙總，沒有逐筆升降評等紀錄，無法確認個別分析師的調評動作。
- 目標價資料互相矛盾，未經驗證：MarketBeat（2026-11-06 文章）列共識 Hold、平均目標價約 USD 97.42；StockChase 另一頁引用的目標價為 USD 53.77。以 2026-11-11 收盤約 USD 62.50 計，兩者分歧極大，後續需以原始分析師報告核對。
- 10/29 第四季展望偏弱後股價大跌（TIKR 報導近一個月約 -43%，自 6/30 高點約 -58%）。

## Retail social
- **Reddit：無法取得。** r/wallstreetbets 與 r/stocks 的 JSON 端點被阻擋（"unable to fetch"），依規定未重試。改以間接來源：24/7 Wall St. 2026-11-02 的 Reddit 熱門股排行中，INTC 排名第一，標記為 bearish，122 則留言、3.2K upvotes。這是第三方彙整，不是直接抓取的 thread。
- **StockTwits：無法取得。** api.stocktwits.com DNS 解析失敗（不在本 session 允許的網域內），已跳過，未重試。
- **X / 新聞 chatter：** TradingView 於 11-12 有一篇 idea 文章，主張「現在沒有理由看空 Intel」，並把可能的回檔歸因於科技股整體修正。AltIndex 的 Reddit 情緒分數於 2026 年中偏多（約 70–73/100），但找不到 11 月的讀數。
- **Buzz 量：** 定性判斷為**高於平常**。依據是 11/02 排行榜首位；但這只是單一時點的快照，無法量化提及數。
- **Retail tilt：** 偏空（低信心）。證據薄，主要來自一個排行榜快照加上少數 11 月初的文章。
- **Themes（重複出現的主題）：**
  - 第四季展望與 PC 需求放緩，擔心 2027 年 PC 市場走弱（MarketBeat 引用）。
  - 數據中心建設的政治與監管不確定性（MarketBeat 引用）。
  - 「便宜還是價值陷阱」之爭：跌幅大，有人看到機會，有人認為基本面仍差。
  - 科技股整體回檔的連動性（TradingView 觀點）。
- 代表性 take（短引）："No reason to be bearish Intel right now"（TradingView idea，2026-11-12，反方觀點）。

## Insider activity
資料窗口：2026-05-15 至 2026-11-15（6 個月）。

| 日期 | 人員 / 職位 | 類型 | 股數 | 金額 (USD M) |
|---|---|---|---|---|
| 2026-08-11 | Lip-Bu Tan / CEO | 公開市場買入 @ USD 95.00 | 105,263 | +10.0 |
| 2026-11-02 | Lip-Bu Tan / CEO | 公開市場買入 @ USD 64.73 | 150,000 | +9.7 |
| 2026-05-29 | Chandrasekaran Nagasubramaniyan / CTO | 賣出 @ USD 118.28 | 21,024 | -2.5 |

- **6 個月淨額：買入 USD 19.7M（全部為 CEO），賣出 USD 2.5M（CTO），淨買入約 USD 17.2M。**
- 其餘交易不計入金額：10/30 COO 179,698 股、7/30 CTO 33,007 股、6/1 CFO Zinsner 37,015 股，皆無價格，應為授予或其他非市場交易，未計入。
- 窗口外參考：2026-05-01 Miller 賣出 40,256 股 @ USD 99.53（約 USD 4.0M）；2026-05-07 多位董事的年度授予（每人約 12,552 股）。
- **Notable：** CEO Lip-Bu Tan 在 8 月與 11 月初分兩次以 USD 95 與 USD 64.73 公開買入，合計約 USD 19.7M。後者是在股價大跌後的買入，屬於較強的信號。
- 內部人持股比例約 14.2%（yf major_holders）。

## Ownership shifts
- 機構持股比例：yf 為 66.95%（機構可流通股 78.06%，機構數約 4,472 家）；MarketBeat 另列 64.53%，兩者未調和。
- **機構流向方向：無法確認，偏混合。** yf 只提供單一時點快照，沒有時間序列。WebSearch 抓到的 MarketBeat 13F 自動通知顯示 Q3 有增有減（例如 Van Eck +18.3%、Ossiam +18.0%、NEOS +53.4%、Winton -52.4%、BDF Gestion -11.3%），但大多數通知的發布日期與所述季度不一致，數字未經 EDGAR 驗證。Q3 2026 的 13F 申報截止日約為 11/14，完整資料可能尚未公開。
- 大型持股：Vanguard 約 3.86 億股（2Q 資料）、Capital World Investors 約 8,650 萬股（MarketBeat 所列，已增持約 2,120 萬股）。

## Net sentiment score
- **Composite：中性（信心：低至中）**
  - 分析師：Hold 為主，BUY% 28.6%，近三個月持平。傾向中性偏謹慎。
  - 散戶：偏空，但證據薄弱（單一排行榜快照加上少數文章），信心低。
  - 內部人：偏多，CEO 6 個月淨買入約 USD 19.7M，屬高信心的正面信號。
- **Divergence flag：是（部分）。** 散戶偏空與內部人買入方向相反。分析師傾向為 Hold，與散戶的偏空方向只是輕微不同。內部人與散戶的分歧較明顯。
- 資料缺口：Reddit 與 StockTwits 皆無法直接取得，散戶結論不完整，後續應在能取得時補上。
- 本報告僅描述情緒，不提供交易建議。

SENTIMENT REPORT COMPLETE
