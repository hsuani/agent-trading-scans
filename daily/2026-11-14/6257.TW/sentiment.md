# Sentiment — 6257.TW (矽格 Sigurd) as of 2026-11-14

## Analyst consensus
目前 yf rec_summary 僅顯示 1 筆 strongBuy，0 buy / 0 hold / 0 sell / 0 strongSell（當期與前一期皆同，樣本量極小，不足以代表市場共識）。
近期評等變動：歷史評等變動工具（recommendations）回傳的仍是同一組彙總數字，**沒有逐筆升降評紀錄**，無法確認近期 upgrade / downgrade，也無法取得目標價變動。
新聞面補充：2025 年 12 月工商時報報導提到本土法人調升至 Buy，但該資料已超過 11 個月，且在 11 月的資料中無法再次確認。2026 年 11 月無可核對的券商評等或目標價報告。

## Retail social
- Reddit（r/stocks、r/wallstreetbets）：**無法取得**。WebFetch 被拒，直接 curl 經 proxy 回 403（CONNECT tunnel failed），依規則軟失敗，未取得任何貼文樣本，無法判斷熱度與多空傾向。
- StockTwits / X：StockTwits API 網域無法解析（api.stocktwits.com 不在本 session 允許網路範圍內），**無法取得**。需在 session 網路設定中允許該網域後才能重試。X 端未找到可用的散戶貼文，WebSearch 結果只有財經新聞與數據頁。
- 聲量（buzz volume）：無法量化。搜尋索引中沒有明顯的散戶討論痕跡，但這不等於聲量低，因為 Reddit 與 StockTwits 兩個主要來源都缺資料。
- 多空傾向：無法判定（bullish / bearish / mixed 皆無可用樣本）。
- 主題（僅來自新聞，非散戶原文）：AI、光通訊、HPC 訂單驅動營運；2026 年資本支出預算 59.3 億 TWD（年增 25%）；11 月單月營收約 17 億 TWD，Q4 毛利率預期季增至約 30.5%。這些是公司與媒體敘事，不是散戶情緒的直接證據。
- 股價波動：nstock 頁面顯示 11 月 6 日盤中 159.5 元，單日下跌 13.50 元（-7.80%）。同一搜尋結果另一頁面標示 2026 年 10 月 2 日股價約 257.5 元，兩者差距大，判斷為舊快取，**未採用**。

## Insider activity
Net 6mo: 無資料。yf insider 回傳空陣列，無法判斷為「無交易」或「資料缺漏」，因此不能推論淨買或淨賣，也無法判定是 CEO / CFO 或其他人員。
Ownership 補充：insidersPercentHeld 約 7.87%。

## Ownership shifts
- 機構持股約 19.04%（流通股占比約 20.67%），機構家數 77 家。
- 只有單一時點快照，無法判斷機構集中度的趨勢方向。

## Net sentiment score
Composite: **neutral（信心：低）**
- 分析師面：樣本僅 1 筆 strongBuy，沒有近期評等變動紀錄，傾向偏正面但證據薄弱。
- 散戶面：Reddit 與 StockTwits 均不可得，無法評分。
- 內部人面：6 個月交易資料為空，無法評分。
- 綜合：資料覆蓋不足，三個面向中有效訊號只有一筆薄弱的分析師評等，因此給出 neutral，信心低。若要提高可信度，需要補足 Reddit / StockTwits 資料與 TWSE 公開資訊觀測站的內部人申報紀錄。

Divergence flag: **no（無法判定）**。因為散戶傾向無資料，無法確認與分析師傾向是否相反。

## 資料來源與限制
- yf rec_summary / recommendations / major_holders：成功，但樣本小、無逐筆評等紀錄。
- yf insider：回傳空陣列。
- Reddit（r/stocks, r/wallstreetbets）：403，軟失敗。
- StockTwits：網域無法解析，軟失敗。
- WebSearch（中文）：找到的股價與估值資料彼此矛盾（EPS 9.69、P/E 16.46 與 159.5 元一致，為本報告採用的時點；其他頁面的 257.5 元與 P/E 約 30 判為舊資料）。
- 本報告不含交易建議。

SENTIMENT REPORT COMPLETE
