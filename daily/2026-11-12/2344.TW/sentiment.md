# Sentiment — 2344.TW (華邦電) as of 2026-11-12

## Analyst consensus
目前 yf rec_summary 顯示 **8 buy / 0 hold / 0 sell**（strongBuy 4、buy 4）。近四個月分布幾乎未變：0m、-1m、-2m 皆為 8 buy；-3m 為 7 buy（strongBuy 4、buy 3）。近期未見評級下調紀錄。

注意事項：
- yf 的 `recommendations` 只回傳各期的分布計數，沒有逐筆的升降評等事件，因此無法確認個別券商的升級或降級時點。
- 網路搜尋的摘要提到 Morgan Stanley 於 2026-03 下調至 Hold，且 Investing.com 的共識為 5 buy / 1 hold。這與 yf 的 0 hold 不一致，可能是不同資料源的覆蓋家數或日期差異。本報告以 yf 數字為主，並標示此差異。
- 目標價：搜尋結果中各站數字互相矛盾（平均約 183.60 TWD、另一站 245.38 TWD），無法採信為單一基準。yf 工具在本次執行未提供目標價欄位。
- 搜尋摘要引用的股價為 155.50 TWD（2026-10-19 報價，來源非即時），僅作參考，未經本次工具驗證。

## Retail social
- Reddit（r/wallstreetbets、r/stocks）：**無法取得**。WebFetch 回傳 "unable to fetch from www.reddit.com"，此來源在本沙盒中被阻擋，未重試。
- StockTwits：**無法取得**。api.stocktwits.com 無法解析（DNS 失敗），需在 session 網路設定中允許該網域後才能重新抓取。
- X / 新聞輿情：僅有一次一般網路搜尋，結果以財經資料站（simplywall.st、investing.com、marketscreener）為主，未找到 2026-11 月的個股評論或散戶討論串。因此**無法判斷散戶語氣**。
- 聲量：無法量化（無 Reddit、StockTwits 原始樣本），只能說明本次未取得任何散戶資料。
- 主題：無法萃取，因無原始貼文。

## Insider activity
yf insider 回傳空陣列，**近 6 個月無可辨識的內部人交易紀錄**（或來源未覆蓋台股內部人申報）。因 yf 對台股的 insider 覆蓋度有限，無法區分「確實零交易」與「資料缺漏」。
Net 6mo: $0 buys / $0 sells（資料缺漏，未驗證）。Notable: 無。

## Ownership shifts
- 內部人持股比例：約 30.26%
- 機構持股比例：約 27.53%（占流通股約 39.47%）
- 機構家數：217
- 本次工具僅提供單一時點快照，無歷史序列，因此**無法判斷機構集中度的趨勢方向**。

## Net sentiment score
Composite: **偏多（bullish），信心低**。
- 分析師面：8 buy / 0 sell，分布穩定，偏多。
- 散戶面：無資料，無法計分。
- 內部人面：無資料，無法計分。
- 信心低的原因：僅單一來源（分析師）有效，散戶與內部人兩個維度缺失，且分析師家數、目標價在不同來源間不一致。

Divergence flag: **無法判定**。散戶語氣缺失，無法比較與分析師傾向是否背離。若後續補上 Reddit 或 StockTwits 資料，應再次評估。

## 資料缺口與後續建議
1. 允許 api.stocktwits.com 網域後重抓 StockTwits。
2. Reddit 於本沙盒不可用，需替代來源（例如手動或經允許的 API）。
3. 台股內部人申報（公開資訊觀測站）需另行查證，yf 覆蓋不足。
4. 目標價應以單一可信來源與明確日期統一後再使用。

SENTIMENT REPORT COMPLETE
