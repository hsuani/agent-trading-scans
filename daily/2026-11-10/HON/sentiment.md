# Sentiment — HON as of 2026-11-10

資料截止說明：本報告只採用 2026-11-10 之前可取得的資料。Reddit 與 StockTwits 無法取得（見「Retail social」）；內部交易資料最新到 2026-10-26。

## Analyst consensus

目前 24 位分析師分布（yf rec_summary，period 0m）：14 buy（含 3 strong buy）/ 9 hold / 1 sell（strong sell）。

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell |
|---|---|---|---|---|---|
| 0m（目前） | 3 | 11 | 9 | 0 | 1 |
| -1m | 3 | 11 | 9 | 0 | 1 |
| -2m | 3 | 11 | 9 | 0 | 1 |
| -3m | 3 | 12 | 8 | 0 | 1 |

- 近 3 個月評等分布幾乎不變，僅 -3m 有一家 hold 轉 buy 的跡象。yf recommendations 工具只回傳彙總計數，沒有個別評等變動紀錄，無法列出具名 upgrade/downgrade。
- 次級來源（Barchart、MarketBeat 等聚合頁，日期混雜）提到：Barclays 將目標價由 $243 上調至 $251，維持 overweight（確切日期未確認）。BofA 降至 Underperform 的時間是 2025-11-18，已超過一年，不是近期動作。
- 目標價均值約落在 $248–254 區間（聚合頁數字，日期不一，僅供參考）。
- 共識傾向：中度偏多（14/24 ≈ 58% buy，sell 僅 1 家，空頭評等稀少）。

## Retail social

- Reddit：WebFetch 無法連線 reddit.com（r/wallstreetbets、r/stocks 皆失敗），軟失敗，無樣本。
- StockTwits / X：api.stocktwits.com 解析失敗（DNS 無法解析，需在 session 網路設定中允許該網域）。以網頁搜尋間接取得兩則 StockTwits 文章，語氣互相矛盾：一則稱散戶情緒「bearish」且訊息量「high」，另一則稱「bullish」且訊息量「high」。兩者日期皆不明，無法判斷哪一個是現況，因此散戶傾向標示為**不確定**。
- 聲量（相對常態，定性）：2026-05 至 06 間 Quantinuum IPO 前後新聞與討論量明顯升高（HON 因量子子公司 IPO 上漲的新聞多見）。2026-11 的聲量無資料，無法與常態比較。
- 量子題材的散戶討論多半以 Quantinuum 價值為核心，HON 本身不是純量子標的。與 IONQ、RGTI、QBTS、QUBT、ARQQ、LAES、IBM 的聲量比較在本次未取得資料，無法列入。
- 主題（來自新聞與聚合頁，非直接 Reddit 樣本）：
  - Quantinuum 價值釋放：母公司約 54%（IPO 前）持股的價值是否被低估，是多頭主要論點。
  - 航太與自動化拆分：分拆計畫被分析師視為改善營運專注度的正面因素。
  - Solstice 分拆後的評等雙降：2025 年底的負面敘事，仍被提及。
  - 美國政府對量子公司的股權投資計畫（約 $2B，9 家公司）提振題材情緒。

## Insider activity

查詢區間 2026-05-10 至 2026-11-10，單位 USD M。

| 日期 | 內部人 | 職稱 | 性質 | 金額（USD M） | 備註 |
|---|---|---|---|---|---|
| 2026-10-26 | KAPUR VIMAL M | CEO | 賣出 | 1.43 | 221 美元附近賣出，同日以 $114.44 行使選擇權（exercise 金額 0.99） |
| 2026-10-26 | LU SU PING | General Counsel | 賣出 | 0.65 | 221 美元附近賣出，同日行使選擇權（exercise 金額 0.46） |
| 2026-08-03 | WEST KENNETH J | Officer | 賣出 | 0.08 | 245 美元附近 |
| 2026-07-27 | WEST KENNETH J | Officer | 賣出 | 4.15 | 244 美元附近，同日行使選擇權 $181.3（exercise 金額 3.31） |

- 6 個月淨額：公開市場買入 $0M / 公開市場賣出約 $6.3M（四筆合計）。
- 另有約 10 筆 value 為空白、text 為空的交易（2026-06-01 至 07-31，CEO、CFO、GC 及數名 officer），性質無法從資料判定（可能為 RSU 歸屬、稅款代扣或其他非公開市場交易），本報告不計入金額。
- 數字驗算：2,943 股 × $221.18 ≈ $0.65M；6,459 股 × $220.99 ≈ $1.43M，與工具金額一致。
- 解讀：CEO 與 GC 的賣出與選擇權行使同日發生，較像行使後變現，而非主動看空的公開市場賣出；且 6 個月內無任何公開市場買入。這是中性偏空的弱訊號。

## Ownership shifts

- 機構持股：84.5%，機構數 2,828 家。
- 內部人持股：0.085%（極低，代表 insider 利益與股東利益的連結較弱）。
- 持股趨勢（季度變化）：工具只提供當前快照，無法判定集中度變化方向。

## Net sentiment score

- 分析師共識：**中度偏多**（14 buy / 9 hold / 1 sell）。信心：中（評等結構穩定，但缺少個別動作紀錄）。
- 內部人：**中性偏空（弱）**。約 $6.3M 公開市場賣出、無買入，但多數與選擇權行使綁定。信心：中低。
- 散戶：**不確定**。Reddit 與 StockTwits 皆無法取得，StockTwits 間接來源矛盾。信心：低。
- 綜合：**中性（略偏多）**，信心低。主要依據是分析師評等結構，內部人賣出與散戶資料缺失拉低信心。

Divergence flag：**部分是**。分析師偏多與內部人賣出方向不同（analyst-insider divergence）。散戶與分析師是否背離無法判定，因為散戶資料缺失，不能以此作為背離證據。

資料限制摘要：
- Reddit（r/wallstreetbets、r/stocks）：403/連線拒絕，無樣本。
- StockTwits API：DNS 解析失敗，需於 session 網路設定允許 api.stocktwits.com。
- yf 工具執行時部分 Yahoo 子網域（fc.yahoo.com、query2.finance.yahoo.com）被 proxy 拒絕，cookie/crumb 失敗，但 recommendations、rec_summary、insider、major_holders 仍回傳資料。
- 聚合與新聞來源多為模板化頁面，日期混雜，僅作輔助。

SENTIMENT REPORT COMPLETE
