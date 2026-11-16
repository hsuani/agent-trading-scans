# Sentiment — SO as of 2026-11-17

## Analyst consensus
22 家評等：7 buy（1 strong buy + 6 buy）/ 12 hold / 3 sell（2 sell + 1 strong sell）。Buy 占比約 32%，hold 約 55%，sell 約 14%。

近四個月評等分布（yf rec_summary，單位：家數）：

| 期間 | strong buy | buy | hold | sell | strong sell | 合計 |
|---|---|---|---|---|---|---|
| 當期 (0m) | 1 | 6 | 12 | 2 | 1 | 22 |
| -1m | 1 | 7 | 13 | 2 | 1 | 24 |
| -2m | 1 | 6 | 14 | 2 | 0 | 23 |
| -3m | 1 | 6 | 13 | 2 | 1 | 23 |

Recent moves: 工具只回傳彙總家數，沒有逐筆升降評與目標價變動明細，無法確認個別券商動作。近一個月 buy 由 8 降到 7、hold 由 13 降到 12，sell 端無變化，屬小幅變動，未見明顯轉向。Web 搜尋有一則 Barchart 文章稱共識較一個月前轉弱，但日期不明，未驗證。另有 Raymond James 升評與降目標價的相互矛盾報導，日期與先後順序都不清楚，不採信為結論。Zacks Rank #3（Hold）為較可靠的第三方訊號，但來源日期不明。

## Retail social
- Reddit: 無法取得。r/wallstreetbets 與 r/stocks 的 public JSON 端點抓取失敗（Claude Code 無法連線 www.reddit.com），本次沒有樣本貼文，無法判斷提及量與多空傾向。
- StockTwits / X: StockTwits 端點 DNS 解析失敗（api.stocktwits.com 不在此 session 允許網域內），需在 session 網路設定中放行後才能重試。X 端只有一次 Web 搜尋，結果多為 Zacks、Barchart、Trefis、Simply Wall St 等財經媒體與評等彙整頁，不是散戶貼文，不能當散戶情緒樣本。
- 提及量（相對常態）：無資料，不估算。
- 散戶多空傾向：無法判定（bullish / bearish / mixed 均不下結論）。
- Themes: 目前可觀察到的主題僅來自媒體面，包括 Q3 財報（排定 2026-11-05，有報導稱優於預期，但年份與內容未能確認）、估值（P/E 倍數下修是股價區間震盪的主因）、太陽能與再生能源擴張的成長敘事。這些是媒體觀點，不代表散戶論述。

## Insider activity
Net 6mo（2026-05-17 至 2026-11-17）：$0 M 買進（公開市場買入 0 筆）/ 約 $1.18 M 賣出（10 筆公開市場賣出，USD M 單位）。

| 日期 | 內部人 | 職位 | 股數 | 金額 (USD M) | 性質 |
|---|---|---|---|---|---|
| 2026-11-06 | Spainhour, Sterling A. Jr. | Officer | 3,333 | 0.31 | 賣出 @ 91.81 |
| 2026-11-02 | Kim, Matthew M. | Officer | 100 | 0.01 | 賣出 @ 93.39 |
| 2026-10-01 | Kim, Matthew M. | Officer | 100 | 0.01 | 賣出 @ 82.73 |
| 2026-09-03 | Sena, Peter P. III | Officer | 4,266 | 0.38 | 賣出 @ 88.59 |
| 2026-09-03 | Kim, Matthew M. | Officer | 1,400 | 0.12 | 賣出 @ 88.87 |
| 2026-09-01 | Kim, Matthew M. | Officer | 100 | 0.01 | 賣出 @ 88.45 |
| 2026-08-06 | Spainhour, Sterling A. Jr. | Officer | 3,333 | 0.31 | 賣出 @ 94.02 |
| 2026-08-03 | Kim, Matthew M. | Officer | 100 | 0.01 | 賣出 @ 94.28 |
| 2026-07-01 | Kim, Matthew M. | Officer | 100 | 0.01 | 賣出 @ 95.77 |
| 2026-06-01 | Kim, Matthew M. | Officer | 100 | 0.01 | 賣出 @ 91.16 |

另有兩筆無金額、交易代碼不明的紀錄：Sena (2026-06-26，712 股) 與 CEO Womack, Christopher C. (2026-05-22，7,662 股)。兩筆都沒有價格欄位，性質可能是稅務代扣、歸屬或其他非市場交易，本次不計入買賣淨額，需以原始 Form 4 確認。

Notable:
- CEO Womack 在window內無公開市場買賣，唯一紀錄為上述無金額紀錄；2026-02-13 的 179,550 股為 grant，不在window內。
- 賣出集中於 Kim, Matthew M.（100 股為主的小額、約每月一筆，形式上接近定期計畫性賣出，是否屬 10b5-1 計畫無法從資料確認）與 Spainhour, Sterling A. Jr.（每季約 3,333 股）。
- 窗口前（2026-03）有較大額賣出：Greene 25,000 股（約 $2.4 M）、Connally 12,500 股（約 $1.2 M），以及 Cummiskey 6,669 股（約 $0.6 M），屬較早期的內部人減持，不計入本期淨額，但可作為趨勢背景。
- 整體內部人持股僅約 0.36%，sell 金額相對公司市值很小，內部人訊號偏弱，主要是「未見內部人買進」而非「大舉減持」。

## Ownership shifts
- 機構持股比例約 74.0%（institutionsPercentHeld 0.740），機構家數約 2,775。
- 內部人持股約 0.36%。
- 工具只給單一時點快照，沒有前期對照，無法判斷機構集中度是增加或減少。major_holders 中的 Top 持股明細未取得完整資料。

## Net sentiment score
Composite: **neutral**（信心：低）

- 分析師面：偏中性略正（7 buy vs 3 sell，但 12 hold 佔多數，近三個月分布幾乎持平）。
- 內部人面：偏中性略負（期間無公開市場買入，約 $1.18 M 賣出，多為小額、規律性交易，衝擊有限）。
- 散戶面：無資料，無法納入評分。
- 整體因散戶端缺失、且分析師分布無明顯轉向，只能給中性；信心低，主因是 Reddit 與 StockTwits 皆不可用。

Divergence flag: **無法判定**。散戶多空傾向沒有樣本，無法與分析師傾向比較。若後續 StockTwits 或 Reddit 可取得，應重新評估。

資料缺口與注意事項：
- Reddit 與 StockTwits 不可用，散戶情緒欄位為空白，不應從媒體文章推估散戶情緒。
- 分析師評等只有彙總家數，沒有個別升降評與目標價變動明細；Web 搜尋的目標價與評等來源日期混雜（含 2026-01 的舊資料），不納入計算。
- 報告日期 2026-11-17 與執行環境系統日期 2026-11-16 不一致，本報告以指定日期 2026-11-17 為準，資料為工具可取得的最新快照。

SENTIMENT REPORT COMPLETE
