# Sentiment — 2455.TW (全新光電) as of 2026-11-22

> 註：系統規則禁止撰寫報告類 .md 檔，以下為上游代為存檔的完整報告內容。

## 資料來源狀態
- yf 工具：recommendations、rec_summary、major_holders 有回傳；insider 回傳空陣列；Yahoo cookie/crumb 取得失敗（ConnectionError），數據可能不完整。
- Reddit（r/wallstreetbets、r/stocks）：WebFetch 無法連線（blocked），無法取得樣本。
- StockTwits：api.stocktwits.com DNS 解析失敗，session 網路未允許此網域，未取得資料。
- PTT / Dcard：搜尋未找到討論串，無法取得。
- WebSearch：有回傳新聞、券商研究與投資網站資料，但多數日期不明，且未找到 2026-10 至 11 月的散戶討論。

## Analyst consensus
11 位分析師：2 strongBuy / 8 buy / 1 hold / 0 sell / 0 strongSell（yf rec_summary 當期快照）。
- 買進側占 10 / 11，無賣出評等。
- 近三個月趨勢：strongBuy 由 3 降至 2、buy 由 7 升至 8，整體仍為買進。yf 僅提供彙總，未提供逐筆升降評等日期。
- 目標價（依 WebSearch 彙整，來源與日期不一）：
  - 澳系外資 236 元（2025-11，優於大盤）
  - 美系外資 130 元（2025-12，觀望，已為舊資料）
  - 美系外資 200 元調升至 290 元（2026-05 初，持股續抱）
  - 亞系外資 465 元（2026-06 中，優於大盤；預估 EPS 2026/27/28 為 6.04 / 11.62 / 16.69 元）
  - Macquarie 500 元（2026-04-29）升至 600 元（2026-07-14，買進）
  - 投資網站彙整平均目標價約 391 元，區間 160 至 600 元
- 近期 9 月下旬有法人上調獲利預估與目標價的報導，但未列出具體新目標價。目前沒有 10 至 11 月的逐筆評等資料。

## Retail social
- Reddit：無法取得（blocked），無樣本。
- StockTwits / X：StockTwits 未連線。X 未搜尋到可用內容。
- PTT / Dcard：未找到。
- 新聞熱度（替代指標）：2026 年多篇目標價上調、光通訊與磷化銦題材報導，媒體關注度高，屬於機構與法人主導的話題，無法換算為散戶聲量。以定性判斷，散戶聲量無法量化。
- Themes（來自新聞，非散戶直接發言）：
  - 1.6T 光偵測器與磷化銦磊晶需求（AI 資料中心光通訊）
  - 磷化銦基板供應短缺，中國放行基板出口後 7 月營收明顯回升
  - 砷化鎵與磷化銦磊晶價格調漲
  - 光電子占比提升（一則日期未確認的報導指出第三季占比約 43%，毛利率約 44.9%）
  - 風險：手機需求偏弱、MOCVD 新設備折舊、獲利持續性
  - 技術面：理財周刊指短線偏弱整理，需放量止穩訊號

## Insider activity
Net 6mo：資料不足（yf insider 回傳空陣列，無法判定）。
- Yahoo 對台股內部人交易覆蓋通常不完整，需改由 TWSE / MOPS 董監持股申報查核。
- 未能確認 CEO / CFO 是否有買賣。

## Ownership shifts
- insidersPercentHeld 5.12%、institutionsPercentHeld 32.29%、institutionsFloatPercentHeld 34.03%、institutionsCount 72。
- 僅為單一快照，無法判斷機構持股的趨勢方向。

## Net sentiment score
Composite：偏多（bullish lean），信心低。
- 分析師端：偏多，信心中高。買進側占比高，無賣出評等。但最近一筆有日期的逐筆目標價為 2026-07-14，之後到 11-22 之間缺乏明確的評等更新資料。
- 散戶端：無資料（Reddit / StockTwits 皆未取得，PTT 與 X 未找到），無法評估。
- 內部人：無資料。
- 股價參考不一致：搜尋結果中的股價快照從約 NT$242 到 NT$493 不等（nStock 為 2026-07 底約 272.5 元），無法確認當下價位，需以即時報價核對。
- 日期注意：一則標題為「全新(2455)公布11月營收，合併營收2.85億元…累計前1-11月營收30.61億元」的報導，因 11 月營收通常於 12 月公布，該文很可能為 2025 年舊報導，未採用為 2026 年數據。
- Divergence flag：無法判定（no retail sample）。若以新聞與分析師為參照，兩者方向一致偏多；但技術面與部分散戶敘述偏弱，無法驗證。

SENTIMENT REPORT COMPLETE
