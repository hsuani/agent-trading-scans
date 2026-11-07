# Sentiment — 8358.TWO as of 2026-11-07

資料完整度：低。分析師資料可用（樣本僅 4 位），Reddit、StockTwits 無法存取，內部人交易回傳空陣列，無法區分「無交易」與「資料缺漏」。

## Analyst consensus
目前 4 buy / 0 hold / 0 sell（其中 strongBuy 2、buy 2）。

歷史分布（yf recommendations，依期間彙總）：

| 期間 | strongBuy | buy | hold | sell | strongSell | 合計 |
|------|-----------|-----|------|------|------------|------|
| 本期 (0m) | 2 | 2 | 0 | 0 | 0 | 4 |
| 前 1 個月 (-1m) | 2 | 1 | 0 | 0 | 0 | 3 |
| 前 2 個月 (-2m) | 1 | 1 | 0 | 0 | 0 | 2 |

近期動向：近兩個月評級由 2 家增至 4 家，且全部為買進評級，未見 hold 或 sell。工具未提供個別券商名稱、升降評等明細與目標價，因此無法確認是升評或新增覆蓋，也無法計算目標價變動。

## Retail social
- Reddit（r/stocks、r/wallstreetbets）：無資料。WebFetch 無法連線 www.reddit.com，兩個子版均未取得搜尋結果。
- StockTwits / X：StockTwits 的 api.stocktwits.com 無法解析（DNS 失敗），需在 session 網路設定中放行後才能重試。
- 網頁搜尋：查詢結果未包含 8358.TWO 的任何討論，返回的是日本 TSE 8358（與本檔不同市場與公司）的頁面，已排除，未納入判斷。
- 聲量（相對常態）：無法評估。
- 散戶傾向：無法判定（無樣本）。
- 主題：無。

## Insider activity
Net 6mo：無資料（insider 工具回傳空陣列，未取得任何 CEO/CFO 或其他董監事的交易紀錄）。空值不等於零交易，此項不納入情緒判斷。

## Ownership shifts
- 內部人持股：17.94%
- 機構持股（占總股本）：25.12%；占浮動股本：30.62%
- 機構家數：52
- 趨勢：工具僅提供單一時點快照，無法判斷機構集中度變化方向。

## Net sentiment score
Composite：偏多（信心：低）。
- 分析師面：偏多。4 家全為買進，無持有或賣出，且近兩個月家數增加。但樣本僅 4 家，單一研究機構的調整即可大幅改變比例。
- 散戶面：無資料。
- 內部人面：無資料。

Divergence flag：無法判定。散戶資料缺失，無法比較散戶與分析師傾向是否相反。

建議後續：待 api.stocktwits.com 放行後重跑 StockTwits；Reddit 若可連線則補抓；另以 8358.TWO 公司名稱或正確英文名重新搜尋，並補充內部人交易資料來源確認。

SENTIMENT REPORT COMPLETE
