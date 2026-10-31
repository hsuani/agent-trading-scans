# Sentiment — ABBNY as of 2026-10-31

## Analyst consensus
6 家覆蓋券商（以 rec_summary 0m 為準）：0 buy / 5 hold / 1 strongSell / 0 strongBuy / 0 sell。

近四個月趨勢（yf recommendations，依月份序列）：
| 期間 | strongBuy | buy | hold | sell | strongSell | 合計 |
|---|---|---|---|---|---|---|
| -3m | 0 | 0 | 3 | 0 | 2 | 5 |
| -2m | 0 | 0 | 3 | 0 | 2 | 5 |
| -1m | 0 | 0 | 3 | 0 | 2 | 5 |
| 0m (當前) | 0 | 0 | 5 | 0 | 1 | 6 |

- 近一個月變化：1 家由 strongSell 轉為 hold，另新增 1 家 hold 覆蓋。沒有 buy 評級出現。
- 個別升評降評事件：yf recommendations 只回傳月度彙總，沒有券商名稱與目標價變動明細，無法列出具體 upgrade / downgrade。
- 目標價：本次工具未提供目標價數據。web 搜尋摘要提到 MarketBeat 2026-03 的共識目標價約 $58.00（來源為 web 摘要，未直接核對，且屬舊資料）。
- 資料注意：strongSell 數量在 -3m 至 -1m 間長期維持 2 家，與多數 hold 並存，屬於此 ADR 覆蓋結構的特徵，但樣本只有 5 到 6 家，單一券商評級變動就會大幅改變比例，解讀時應保守。

## Retail social
- Reddit（r/wallstreetbets、r/stocks）：本次 WebFetch 被拒絕（無法連線 www.reddit.com），無法取得討論串與傾向。軟失敗，未納入評分。
- StockTwits / X：StockTwits API 無法解析網域（api.stocktwits.com 不在目前 session 允許網路清單），本次未取得訊息流。需在 session 網路設定中允許該網域後才能重試。
- X / 新聞 web 搜尋（2026-10 前後）：找到的 ABBNY 專屬意見文章很少，沒有可驗證的散戶討論樣本。摘要提及的重點如下（均來自搜尋摘要，未逐篇核對原文）：
  - 2026-10-20 前後的財報消息被報導為訂單大幅成長、全年度預測上調，市場情緒偏正面。
  - 有報導提及一筆約 $5.5B 的 Rotork 收購案與機器人業務出售予 SoftBank，屬於新聞摘要，未經原始公告核對。
  - 有文章指出估值偏高（以 2028 年預期 P/E 約 23.5 計，相對 Siemens 溢價約四分之一），這是散戶與分析師都會引用的估值論點。
- 散戶聲量：無法量化。Reddit 與 StockTwits 皆未取得，無法與平時基準比較，本項標示為未知。
- 主要主題（僅依搜尋摘要）：訂單成長與上調預測、併購與業務重組、估值偏高的擔憂。

## Insider activity
Net 6mo: 無資料。yf insider 回傳空陣列，無法判斷 CEO / CFO 或其他高階主管的買賣方向與金額。
- 注意：空陣列可能代表近六個月沒有申報交易，也可能是資料源缺漏，兩者無法從本次資料區分。
- 方向性判斷不作結論。

## Ownership shifts
- insidersPercentHeld：0.0（資料源回傳，對 ADR 而言不合理，視為資料異常，不採用）。
- institutionsPercentHeld：0.00201（數值量級明顯偏低，疑為單位或比例換算錯誤，不採用）。
- institutionsCount：86（機構數量，可用但無歷史比較，無法判斷集中度趨勢）。
- 結論：本次無法可靠判斷機構持股集中度的變化方向。

## Net sentiment score
Composite: **neutral**（信心：低）

依據：
- 分析師端：0 buy、5 hold、1 strongSell，偏中性略偏保守；近一月有一家由 strongSell 轉為 hold，方向微幅改善，但沒有任何 buy 評級。
- 散戶端：無可用數據（Reddit / StockTwits 皆失敗），無法評分。
- 內部人：無資料。
- 網路新聞摘要偏正面（訂單與預測上調），但來源未逐一核對，權重有限。

Divergence flag: **無法判定**。散戶端沒有資料，無法與分析師傾向比較。若日後取得 StockTwits 或 Reddit 資料，再重新評估是否出現散戶偏多、分析師偏空（或相反）的背離。

資料缺口摘要：
1. Reddit 被拒絕存取。
2. api.stocktwits.com 無法解析。
3. yf insider 無資料。
4. yf major_holders 的 insiders 與 institutions 百分比數值異常，不採用。
5. 分析師資料只到月度彙總，無個別券商明細與目標價。

SENTIMENT REPORT COMPLETE
