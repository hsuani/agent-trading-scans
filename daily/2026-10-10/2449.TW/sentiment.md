# Sentiment — 2449.TW（京元電子）as of 2026-10-10

> 註：系統當日為 2026-10-09，本報告依任務指定之 as-of 日期命名。分析師評等數據為 yf 工具截取時點的快照；散戶與新聞資料多停在 2026 年 7 月至 8 月，未能取得 10 月的即時情緒資料。

## Analyst consensus
目前 15 家 buy（strongBuy 4 / buy 11），0 hold，0 sell，0 strongSell。
近三個月變化：-3m 時為 14 家 buy（4 SB / 10 B），目前為 15 家，淨增 1 家買進評等；未見 hold 或 sell 評等。
工具回傳的 recommendations 僅為彙總計數，未提供個別券商的升降評等事件，因此無法列出具體 upgrade / downgrade 名單。
目標價（非 yf，來自 WebSearch 新聞）：
- 美系外資 2026 年 5 月股東會前後維持「增持」，目標價 338 元，認為第三季受惠於 XPU 業務成長。
- FactSet 彙整之分析師預估：目標價中位數約 350 元；2026 年 EPS 中位數約 9.9 元，2027 年約 14.4 元。
- 上述目標價未能確認發布日期，視為參考值。

## Retail social
- Reddit：依任務指示不以 WebFetch 讀取金融網頁，未取得 r/wallstreetbets 或 r/stocks 樣本，列為 DATA_UNAVAILABLE（未抓取）。
- StockTwits：同上，未抓取，列為 DATA_UNAVAILABLE（未抓取）。
- X / 新聞與論壇（WebSearch）：
  - CMoney 股市社群氛圍偏悲觀。代表性留言如「只要跌275，跌300以上賣」，另提及外資訊息偏空。
  - 另有較樂觀的留言認為 255 附近有強力支撐，並預期 2027 年 EPS 可達 15 至 18 元（匿名留言，代表性有限）。
  - 股價參考點：2026-07-20 收盤 270.50 元（單日 -5.58%）；2026-08-26 收盤 244.00 元（單日 +1.88%）。另有一篇無日期的技術分析頁面引用 311 元收盤，時點不明，不採用為 10 月價格。
- 討論量：無法取得可靠的提及次數，無法與歷史基準比較，量能判讀為 DATA_UNAVAILABLE。
- Themes（由有限樣本歸納）：
  1. 股價高檔震盪、是否回檔至 255 附近再進場。
  2. 外資買賣超與評等方向。
  3. 2027 年獲利成長（EPS 預估）與 XPU / 第三季客戶動能。
  4. 估值偏高的疑慮（技術面偏多但 P/E 處於歷史偏高區間，來源為未標日期的第三方評分頁）。
- Retail tilt：偏空至中性（mixed-to-bearish），樣本少、時點舊，信心低。

## Insider activity
- yf insider 回傳空陣列，無法判定 6 個月淨買賣金額，列為 DATA_UNAVAILABLE。空結果可能是資料源缺漏而非真正無交易。
- 台股董監事持股異動另以公開資訊觀測站（MOPS）申報為準，本次未取得該來源。
- Notable：無。

## Ownership shifts
- 內部人持股比例：8.83%（yf major_holders）
- 機構持股比例：35.39%；流通股中機構佔比 38.82%；機構家數 225 家
- 僅有單一時點快照，無法判斷機構集中度的趨勢方向，趨勢判讀為 DATA_UNAVAILABLE。

## Net sentiment score
Composite：**偏多（analyst 主導）**，信心：**低至中**。
- 分析師面：強烈偏多（15 buy / 0 hold / 0 sell，近三個月淨增 1 家買進）。信心中高，但未取得個別券商評等細節與發布日期。
- 散戶面：偏空至中性，樣本僅來自匿名論壇與無日期的新聞搜尋，信心低。
- 內部人面：資料缺漏，不納入計分。
- 股價與目標價之間的資料時點不一致（最新可靠股價為 8 月底 244 元，目標價 338 至 350 元），無法確認目前上行空間。

Divergence flag：**是**。散戶論壇偏悲觀（「跌 300 以上賣」等留言），與分析師全數買進評等方向相反。此分歧可能有參考價值，但因散戶樣本過舊與稀少，不宜作為強烈訊號。

## 資料缺漏清單
- Reddit（r/wallstreetbets、r/stocks）：未抓取（依指示不 WebFetch 金融網頁）
- StockTwits：未抓取（同上）
- 10 月當期散戶討論量與情緒：DATA_UNAVAILABLE
- 內部人 6 個月買賣金額：DATA_UNAVAILABLE（yf 空回傳）
- 機構持股趨勢：DATA_UNAVAILABLE（僅單一快照）
- 個別券商評等變動與發布日期：DATA_UNAVAILABLE

SENTIMENT REPORT COMPLETE
