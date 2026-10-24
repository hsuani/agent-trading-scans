# Sentiment — 2455.TW (全新) as of 2026-10-25

> 資料注意事項：今日實際日期為 2026-10-24，報告以要求的 2026-10-25 為基準，但最新可得股價為 10/16 收盤。Reddit 與 StockTwits 均無法取得，散戶面板資料缺失。

## Analyst consensus
11 家券商：3 strongBuy / 7 buy / 1 hold / 0 sell（合計 10 買方、1 持有、0 賣方）。近三個期間（0m、-1m、-2m）：-2m 為 3/6/1/0/0，-1m 與 0m 為 3/7/1/0/0，即最近一段期間新增 1 家買進，之後無變動。`recommendations` 工具回傳的是期間彙總，沒有逐筆升降評等事件，因此無法列出具體的調評券商。目標價變動資料無法取得。

搜尋結果中有兩筆目標價資訊，但都無法完整驗證：
- nStock 標題（2026-09-08）：「全新8月營收年增71%　外資升目標價至793元」。僅見標題，無券商與完整內文。
- FactSet 舊調查（2023-10）：目標價中位數 167 元，已過時，參考價值有限。

若 793 元屬實，相對 10/16 收盤 493 元約有 60% 上行空間，與上述 10 買方的結構一致，但需以券商原文確認。

## Retail social
- Reddit（r/wallstreetbets、r/stocks）：無法取得（抓取被擋，soft-fail）。
- StockTwits：無法取得（DNS 解析失敗，soft-fail）。
- X / 網路論壇：搜尋結果中 CMoney 股市論壇摘要，內容為「逢低買進」與「觀望」並存的分歧看法，但貼文未註明日期，且引用價位（約 300–336 元）明顯低於近期交易區間，判定為過時資料，權重低。
- 聲量：無法量化，無法與平均水準比較。
- 散戶傾向：**無法判定**（資料不足，不宜推定為看多或看空）。

Themes（僅依網路摘要）：
- 估值偏高：本益比約 120.8 倍（StatementDog），是散戶最常見的疑慮。
- 營收動能：9 月營收年增約 29.5%（StatementDog），8 月營收年增 71%（nStock 標題），可能是看多論點。
- 近期波動：10/13 單日下跌約 9.9%（Wantgoo 快照），引發買盤與觀望的分歧。

## Insider activity
過去 6 個月：`insider` 工具回傳空陣列，無資料。無 CEO、CFO 或其他內部人交易紀錄可呈現。這不代表沒有交易，可能只是工具未覆蓋台股內部人申報資料，需以公開資訊觀測站另行查核。淨買賣金額：無法計算。

## Ownership
- 機構持股：約 32.2%（68 家機構）。
- 內部人持股：約 5.2%。
- 流通股機構持股：約 34.0%。
- 趨勢：工具僅回傳單一時點快照，無法判斷機構集中度是增加或減少。

## Price context（非情緒來源，僅供對照）
- 10/13：508 元（日跌 9.93%，前收 564 元，Wantgoo 快照）。
- 10/16：收盤 493 元（+1.96%，StatementDog）。
- 本益比 120.81 倍對應近四季 EPS 4.08 元（493 ÷ 4.08 ≈ 121，與報價一致）。

## Net sentiment score
**綜合：偏多（信心：中低）**

- 分析師面：偏多，信心中高。10 買 / 0 賣，方向一致，但樣本僅 11 家。
- 散戶面：無法判定，信心低。Reddit 與 StockTwits 缺失，論壇資料過時。
- 內部人面：無資料，不加分也不扣分。
- 機構面：持股穩定（約 32%），未見明顯撤出訊號，但無趨勢資料。

Divergence flag: **無法判定**。散戶傾向資料不足，無法確認與分析師傾向是否相反。若後續取得 Reddit 或 StockTwits 資料，可再比對。

## 資料來源
- yf 工具：recommendations、rec_summary、insider、major_holders（2455.TW）
- Wantgoo 籌碼與股價快照：https://www.wantgoo.com/stock/2455/major-investors/branch-buysell/agent/1480
- StatementDog 個股分析：https://statementdog.com/analysis/2455
- CMoney 股市論壇：https://www.cmoney.tw/forum/stock/2455?tab=news
- nStock 個股頁：https://www.nstock.tw/2455
- nStock 新聞（目標價 793 元標題）：https://www.nstock.tw/news/article_c?id=372372
- 鉅亨網 FactSet 舊調查（2023）：https://news.cnyes.com/news/id/5239982

SENTIMENT REPORT COMPLETE
