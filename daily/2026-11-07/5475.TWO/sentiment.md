# Sentiment — 5475.TWO (德宏, TPEx) as of 2026-11-07

資料完整度: 低。分析師、內部人、Reddit、StockTwits 皆無有效資料,本報告無法給出可靠的情緒評分。

## Analyst consensus
0 buy / 0 hold / 0 sell (資料缺漏,非真實零評等)。`yf rec_summary` 與 `yf recommendations` 皆回傳空陣列,且同次呼叫的 Yahoo cookie/crumb 取得失敗 (ConnectionError),判定為資料源無法連線,不是該股無券商覆蓋。
網頁搜尋未找到任何券商或外資評等、目標價變動。唯一可見的目標價來自 poorstock.com (目標價 150 TWD),該站為 AI 依技術指標自動產生,不是分析師目標價,不納入共識。
Recent moves: 無可確認資料。

## Retail social
- Reddit (r/wallstreetbets, r/stocks): 抓取失敗 (Claude Code 無法連線 www.reddit.com),無樣本、無 tilt 判斷。
- StockTwits / X: StockTwits 因 api.stocktwits.com DNS 解析失敗而無法連線 (此 session 網路白名單未包含該網域)。需由使用者於 session 網路設定允許該網域後才能重試。X 端無可用貼文。
- 網頁新聞: 僅一則可見新聞標題提及 德宏 (2026-10-20) 因「銅價大漲、玻纖布缺貨潮持續擴大」攻上漲停。文章內文未取得,無法判斷市場解讀。這是唯一可得的題材線索,屬於產業價格與缺貨題材,不等同於散戶情緒。
- 聲量: 無法量化,無法與平時比較。
- Themes: 缺料/漲價題材 (銅、玻纖布) 為目前唯一可見主題;其餘無資料。

## Insider activity
Net 6mo: 無資料 (`yf insider` 回傳空陣列,與連線失敗訊息同時出現,無法區分「無交易」與「取得失敗」)。
Notable: 無。

## Ownership shifts
- 內部人持股 (insidersPercentHeld): 約 27.9%
- 機構持股 (institutionsPercentHeld): 約 2.7%;浮動股中機構占比約 3.8%
- 機構家數 (institutionsCount): 7
- 趨勢: 單一時點快照,無歷史比較,無法判斷集中度變化。
- 注意: 機構比例偏低且來源為 Yahoo 欄位,對台灣櫃買個股可能覆蓋不完整,信心低。內部人持股高於 25%,代表股權相對集中於內部人,流通股比例偏低。

## Net sentiment score
Composite: 中性 (neutral),信心: 低。
理由: 四項主要訊號中,分析師與內部人資料缺漏,散戶資料來源全數失效;僅剩一則題材新聞 (缺料漲價) 與技術面自動評論 (不採納),不足以判斷多空方向。此評分不應被解讀為看多或看空。

Divergence flag: 無法判定 (缺分析師與散戶其一或兩者的有效資料)。

## 待補項目
1. 於 session 網路設定允許 api.stocktwits.com 後重試 StockTwits 串流。
2. Reddit 公開 JSON 端點目前無法連線,需確認網路白名單或改用其他來源。
3. 以中文來源補券商評等與目標價: MoneyDJ、鉅亨網、公開資訊觀測站個股研究報告,搜尋「德宏 5475」並核對發布日期。
4. 重新執行 `yf` 工具,確認 Yahoo cookie/crumb 連線恢復後,rec_summary、recommendations、insider 是否有資料。
5. 補查 10 月 20 日漲停新聞全文,確認缺料/漲價題材的持續性與市場解讀。

SENTIMENT REPORT COMPLETE
