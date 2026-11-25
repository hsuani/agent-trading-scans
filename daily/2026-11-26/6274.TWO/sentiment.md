# Sentiment — 6274.TWO (Taiwan Union Technology, TPEx) as of 2026-11-26

注意事項：Reddit 與 StockTwits 皆無法取得，零售情緒部分資料不足。

## Analyst consensus
目前 15 位分析師：5 Strong Buy / 10 Buy / 0 Hold / 0 Sell（rec_summary 與 recommendations 工具回傳相同）。
近期變化：過去 3 個月 Strong Buy 由 4 家增至 5 家，Buy 維持 10 家，無 Hold 或 Sell。工具未提供逐筆升降評等紀錄與目標價歷史，無法判定具體升降評事件。
目標價：工具未提供。一則未註明日期的網路摘要提到平均 12 個月目標價約 TWD 2,114.62，但同一批來源的股價區間（TWD 420 至 1,470）與 52 週區間（TWD 249.5 至 1,920）彼此矛盾，此數字不可採信，僅供參考。

## Retail social
- Reddit：r/wallstreetbets 與 r/stocks 搜尋皆遭拒絕（WebFetch 無法存取 reddit.com），無樣本，無法判定情緒傾向。
- StockTwits / X：api.stocktwits.com 無法解析（DNS 失敗，需於 session 網路設定中允許該網域）。網路搜尋未找到 2026 年 11 月的可靠情緒記錄，結果多為未註明日期的股價頁面與技術訊號頁面，且彼此矛盾（技術訊號一則為 Strong Sell、一則為 Strong Buy）。
- 聲量：無法量化，以定性判斷屬於資料缺口。
- 主題：無可靠樣本，無法列出反覆出現的主題。

## Insider activity
Net 6mo：工具回傳空陣列，無可辨識的 6 個月內申報交易。此結果可能代表真實無交易，也可能是資料源未涵蓋 TPEx 的董監事申報，因此無法確認為「無內部人交易」。
Notable：無。

## Ownership shifts
- 內部人持股比例約 12.3%
- 機構持股比例約 44.2%（流通股口徑約 50.4%），機構數 137 家
- 工具僅提供單一時點快照，無季度變化趨勢，無法判定機構集中度的方向性變化。

## Net sentiment score
Composite：**偏多（bullish），信心度低**。
依據僅為分析師面：15 家全數買進或強力買進，且過去 3 個月 Strong Buy 小幅增加。零售面與內部人面均無可靠資料，因此綜合分數主要反映分析師觀點，無法與市場情緒交叉驗證。
Divergence flag：**無法判定**。零售情緒資料缺失，無法比較零售與分析師傾向是否相反。

## 資料缺口與後續建議
1. api.stocktwits.com 需於 session 網路設定中加入允許清單後重試。
2. Reddit 存取遭拒，建議改用其他可用來源或經授權的 API。
3. TPEx 內部人申報建議以公開資訊觀測站的董監持股申報資料補充。
4. 目標價與升降評歷史建議以付費或券商研究來源補齊。

SENTIMENT REPORT COMPLETE
