# Sentiment — OKTA as of 2026-10-30

> 資料註記：工具執行日為 2026-10-29，報告日期依指示標示為 2026-10-30。Reddit 與 StockTwits 無法取得，散戶面向資料不完整（見下方）。

## Analyst consensus
44 位分析師：9 strongBuy / 25 buy / 10 hold / 0 sell / 0 strongSell，買進側占約 77%，無賣出評等。
近四個月（0m 至 -3m）評等分布大致穩定：strongBuy 8–9、buy 25–26、hold 9–10；-3m 曾有 1 筆 strongSell，目前已無。
Recent moves: yf 工具只回傳各月評等計數，未回傳個別升降評等（upgrade/downgrade）與目標價變動明細，無法確認近期個別調整。網路摘要（TIKR 日文文章，日期不明）提到平均目標價約 $135，而 yf 內部交易價格顯示 2026-09 成交價約 $168–198，兩者時間點不同，且網路來源日期不明，不採用其股價數字。

## Retail social
- Reddit：r/wallstreetbets 與 r/stocks 的 JSON 搜尋皆回傳錯誤（WebFetch 無法連線 www.reddit.com），本次無法取得討論串樣本、分數或留言數。軟性失敗，略過。
- StockTwits / X：api.stocktwits.com 無法解析（DNS 失敗，需於 session 網路設定允許該網域），本次未取得。改以 WebSearch 補充：
  - SentiSense 頁面顯示 30 日情緒分數 9.2（偏多但轉弱），資料截至 2026-08-09，已過時約兩個半月；頁面標示 Reddit 中性、占提及 12%，新聞為多方提及主要來源。
  - 期權流向報導（Benzinga 2022–2025）多為偏空定位，屬舊資料，僅供參考。
  - 搜尋結果含大量無實質內容的通用頁面，已排除。
- Retail buzz volume：無法量化（缺乏 Reddit/StockTwits 提及數），定性上未見 2026-10 有明顯討論熱度的來源，但此判斷信心低。
- Retail tilt：無法可靠判定（mixed / 資料不足）。
- Themes（來自 WebSearch 摘要，非原始貼文）：估值偏高是否還能延續、Q3 財報後股價波動、內部人大額減持。

## Insider activity
過去 6 個月（2026-04-30 起）共 31 筆具金額之申報中，賣出合計約 $46.5M，買進為 $0（0 筆公開市場買入）。
> 註：另有約 15 筆金額欄位為空白（多為授予、轉換、贈與或扣繳類），未計入。

主要賣方（USD M）：
| 內部人 | 職位 | 賣出金額 (USD M) | 筆數 |
|---|---|---|---|
| TIGHE BRETT | CFO | 20.5 | 2 |
| MCKINNON TODD | CEO | 19.6 | 2 |
| SCHWARTZ LARISSA NICOLE | Officer | 4.1 | 3 |
| KELLEHER ERIC ROBERT | President | 2.1 | 3 |
| ARCHAMBEAU SHELLYE L | Director | 0.2 | 1 |

Notable：
- CEO Todd McKinnon：2026-09-22 出售 48,822 股，約 $9.4M（$189.04–197.79）；2026-07-08 出售 68,936 股，約 $10.1M。
- CFO Brett Tighe：2026-09-02 出售 80,000 股，約 $12.9M（$158.51–167.09）。
- President Eric Kelleher：2026-09 多筆賣出，合計約 $2.1M。
- 交易集中於 2026-06 至 2026-09，股價區間 $76–198，顯示期間價格大幅上行時內部人持續賣出。
- 注意：工具未標示交易是否屬 10b5-1 預定計畫，無法判斷是否為獨立判斷的減持，需另查 SEC Form 4 註記。

## Ownership shifts
- 機構持股：約 99.8%，機構數 1,242 家；內部人持股約 0.5%。
- 歷史趨勢：yf major_holders 僅回傳當期快照，無時間序列，無法判斷機構集中度趨勢。

## Net sentiment score
Composite：**中性偏多（neutral-to-bullish），信心低**。
- 分析師面：偏多（77% 買進、0 賣出，評等穩定）。
- 內部人面：偏空／中性（6 個月約 $46.5M 賣出、0 買入，集中於高點區間）。
- 散戶面：無資料（Reddit / StockTwits 未取得；WebSearch 來源過時）。
- 機構面：高持股比例，無趨勢資料。

Divergence flag：**無法判定**。缺乏可靠散戶傾向，無法確認散戶與分析師是否背離。若後續取得散戶資料，需重新評估。

SENTIMENT REPORT COMPLETE
