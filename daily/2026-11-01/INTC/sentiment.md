# Sentiment — INTC as of 2026-11-01

資料截止日：工具可取得的最新資料為 2026-10-31。Reddit 與 StockTwits 無法取得，以下 retail 部分為缺漏，非中性結論。

## Analyst consensus
48 家覆蓋：1 strong buy / 10 buy / 36 hold / 1 sell / 0 strong sell（買進側 11、持有 36、賣出側 1）。

| 期間 | 買進側 (SB+B) | 持有 | 賣出側 (S+SS) |
|---|---|---|---|
| 當期 (0m) | 11 | 36 | 1 |
| -1m | 15 | 32 | 2 |
| -2m | 14 | 32 | 2 |
| -3m | 14 | 31 | 3 |

近三個月趨勢：買進側由 14 降至 11，持有由 31 升至 36，賣出側由 3 降至 1。評等分布往持有集中，買進評等減少，賣出評等也減少，整體偏中性。

Recent moves：yf 工具只回傳月度彙總計數，沒有逐筆升降評與目標價變動明細，無法列出具體 upgrade / downgrade 事件或目標價調整，此為資料缺口。網路搜尋找到的 Q3 獲利指引與分析師評等片段日期混雜（部分為 2025 年文章），未能驗證，本報告不採用。

## Retail social
- Reddit：r/wallstreetbets 與 r/stocks 搜尋皆回傳 403 / 無法存取，無法取樣貼文，無法判斷 tilt。
- StockTwits：api.stocktwits.com 無法解析（DNS 失敗），需於 session 網路設定允許該網域後才能重試。
- X / 新聞：網路搜尋未找到可靠的 10 月散戶情緒資料。搜尋結果多為 8–9 月的自動生成期權與技術分析頁面，偏多頭的期權情緒與偏空的技術讀數並存。另一篇 TipRanks 文章提到 INTC 為 Reddit 熱門討論股，但日期不明，且內容似為較早季度，不採用。
- 討論量：無法量化，既無 mention count 也無同期基準，判定為資料不足。
- 主題：無可引用的可靠貼文樣本，無法列出 recurring themes。
- Tilt：無法判定（資料不足）。

## Insider activity
以 2026-05-01 至 2026-11-01 為 6 個月窗口，依 yf 交易明細計算（單位 USD）：

淨 6mo：買進 約 $10.00M，賣出 約 $6.49M，淨買入 約 +$3.51M。

| 日期 | 人員 | 職位 | 交易 | 股數 | 金額 (USD) |
|---|---|---|---|---|---|
| 2026-08-11 | TAN LIP-BU | CEO | 買進 @ $95.00（間接持有） | 105,263 | 約 $10.00M |
| 2026-05-01 | MILLER BOISE APRIL | Officer | 賣出 @ $99.53 | 40,256 | 約 $4.01M |
| 2026-05-29 | CHANDRASEKARAN NAGASUBRAMANIYAN | CTO | 賣出 @ $118.28 | 21,024 | 約 $2.49M |

注意：
- 2026-05-07 董事群的 12,552 股等無金額紀錄，與 2026-06-01、2026-07-30 的 CFO / CTO 無金額紀錄，多半為獎勵授予或歸屬，非公開市場買賣，未計入淨額。
- CEO 8 月買進為本窗口最重要的內部人訊號，單筆金額大於其餘所有窗口內交易合計。
- 窗口外參考：CFO ZINSNER DAVID A 於 2026-01-26 以 $42.50 買進 5,882 股（約 $0.25M）。

## Ownership shifts
- 機構持股 62.8%（流通股占比 73.0%），機構家數 4,439。
- 內部人持股 13.9%。
- 僅有當期快照，無前期比較，無法判定機構集中度趨勢，此為資料缺口。

## Net sentiment score
Composite：**中性（neutral），信心低**。
- 分析師：偏中性。買進側由 14 降至 11，持有升至 36，賣出側極少（1）。
- 內部人：偏正面。CEO 於 8 月以 $95 買入約 $10.0M，為本窗口淨買入來源；同期有 CTO 與一名 officer 的賣出（合計約 $6.5M）。
- 散戶：無資料。

Divergence flag：**無法判定**。散戶 tilt 缺失，無法與分析師 tilt 比對。分析師分布偏中性，內部人淨買偏多，兩者不構成明確反向。

資料注意事項：
- 報告日期 11-01 為週末前一日起算的 as-of，財報（Q3 2026）據報導於 10-29 盤後發布，但實際結果未能取得驗證。財報後的情緒可能與本報告所用資料不同步。
- 若要提高信心，需補足 Reddit / StockTwits（需網域允許）、逐筆評等變動與目標價資料，以及前期機構持股比較。

Sources:
- [TipRanks: Intel stock trending on Reddit](https://www.tipranks.com/news/article/intel-stock-nasdaqintc-is-this-trending-reddit-stock-predicted-to-rise)
- [Quiver Quant: Why Intel stock is up today](https://www.quiverquant.com/news/Why+Intel+%28INTC%29+Stock+Is+Up+Today)
- [Barchart: Intel Q3 earnings preview (Oct 29, average move about 13%)](https://www.barchart.com/story/news/37135682/intel-stock-is-already-up-19-in-2026-can-q4-earnings-propel-it-higher-in-2026)
- [Historical Option Data INTC analyses (Aug–Sep 2026)](https://historicaloptiondata.com/?p=86245)
