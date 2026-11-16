# Sentiment — 2301.TW (Lite-On) as of 2026-11-17

## Analyst consensus
12 家覆蓋：4 Strong Buy / 6 Buy / 2 Hold / 0 Sell / 0 Strong Sell（yf rec_summary，0m 期間）。
買方評等占 83%（10/12），無賣方評等。

近四個月趨勢（yf recommendations，月度彙總）：

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell |
|---|---|---|---|---|---|
| 0m（本期） | 4 | 6 | 2 | 0 | 0 |
| -1m | 4 | 6 | 2 | 0 | 0 |
| -2m | 4 | 6 | 2 | 0 | 0 |
| -3m | 4 | 5 | 2 | 0 | 0 |

Recent moves：-3m 至 0m 之間僅 Buy 由 5 增至 6，其餘欄位不變，合計家數由 11 增至 12（推測為一家新覆蓋券商以 Buy 進入，yf 未提供個別券商資料，無法確認）。yf 工具未回傳個別券商的升降評與目標價變動，目標價趨勢未能確認。

## Retail social
- Reddit（r/wallstreetbets、r/stocks）：資料無法取得。WebFetch 回傳 "unable to fetch from www.reddit.com"，本次未納入散戶論壇樣本。
- StockTwits：資料無法取得。api.stocktwits.com DNS 解析失敗（ENOTFOUND），需於 session 網路設定允許該網域後才能重試。
- X / 新聞搜尋：僅找到分析師共識與技術面快照頁（Investing.com、Simply Wall St、Stockopedia 等），未找到具日期、可歸類為散戶情緒的 2026-11 討論串。
- 聲量：無法量化，無法與平常基準比較。
- 傾向：無法判定（bullish / bearish / mixed 皆無資料支持）。
- 主題：無可引用樣本。搜尋所得的技術面與估值資訊（技術指標偏空、P/E 略高於同業、週波動率高於產業均值）屬機構/聚合網站的描述，不代表散戶主題。

## Insider activity
Net 6mo：無資料。yf insider 回傳空陣列，無法確認近六個月內部人買賣金額，也無法判斷 CEO/CFO 或其他人員是否有交易。此項不納入綜合評分。

## Ownership shifts
- 內部人持股比例：14.2%
- 機構持股比例：38.6%（占流通股 45.0%）
- 機構家數：273
- 歷史趨勢：yf major_holders 僅提供單期快照，無法判定機構集中度的增減方向。

## Net sentiment score
Composite：**偏多（bullish），信心中低**。

依據：
- 分析師端偏多且一致（10/12 買方、0 賣方、近四個月結構穩定）。
- 散戶端與內部人端皆無資料，綜合分數僅能以分析師共識為主要依據，信心因此受限。
- 網路搜尋中的技術面快照偏空（50 日與 200 日均線位於現價之上，RSI/MACD 呈賣訊），與分析師偏多的方向不同，但屬單一聚合來源且日期不明，不列為主要評分依據。

Divergence flag：**無法判定**。散戶傾向資料缺失，無法確認散戶與分析師是否方向相反。待 Reddit 或 StockTwits 可存取後再重算。

資料限制：
- Reddit 與 StockTwits 皆無法存取，散戶面為空白。
- yf insider 回傳空值，內部人面為空白。
- 網路搜尋的股價快照互相矛盾（約 217 至 255 TWD），且日期不一，未用於本報告的判斷。
- yf 的 Yahoo cookie/crumb 取得失敗，仍回傳分析師與持股資料，但建議以即時資料核對。

SENTIMENT REPORT COMPLETE
