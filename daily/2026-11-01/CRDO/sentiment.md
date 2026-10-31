# Sentiment — CRDO as of 2026-11-01

## Analyst consensus
20 家：5 strong buy / 14 buy / 1 hold / 0 sell / 0 strong sell（yf rec_summary，本月快照）。
近四個月趨勢：strong buy 由 4 升至 5（-2m 至 -1m 之間），buy 14 與 hold 1 不變，全期無 sell。
Recent moves：yf recommendations 工具回傳的仍是彙總計數，不含逐筆評等變動，因此無法列出具體 upgrade / downgrade 事件。
目標價（網路搜尋，來源不一、部分過時，僅供參考）：
- Google Finance 近 3 個月 14 家：13 buy / 1 hold，平均 12 個月目標價約 $280.5。
- Tickzen（2026-10 頁面）：mean target 約 $279.1，並列出 short interest 約 11.28M 股。
- Benzinga 共識頁（無日期）：約 $215。
- Barclays 目標價 $85 → $165、TD Cowen $140 → $160 的調升新聞，日期不明或為 2025 年，已視為過時。
- 現價存在衝突：Tickzen 記 2026-10-20 收盤約 $171.5，Google 頁面約 $214。內部人 10 月成交區間約 $155–$226，與 $171 的說法較吻合，但未確認。

## Retail social
- Reddit（r/wallstreetbets、r/stocks）：無法取得。WebFetch 與直接 curl 均被代理拒絕（www.reddit.com CONNECT 403），無樣本貼文、無提及量數據。
- StockTwits：無法取得。api.stocktwits.com DNS 無法解析，需在 session 網路設定中允許此網域後才能重試。
- X / 新聞：一次網路搜尋，結果稀疏且多為分析文章。Seeking Alpha 文章觀點分歧：一派認為是 "market mania" 下的真實執行，另一派質疑「單一產品故事」能否轉型為平台；Pluang（2026-05）評為 overvalued、hold、約 12% 下檔風險。
- 聲量：無法量化提及次數，無法與常態比較。
- 散戶傾向：無法判定（資料缺口），不應以此推論多空。
- 主題（僅由有限新聞歸納）：AI networking / 高速連接晶片的成長性、估值偏高、客戶集中度（revenue concentration）、高空頭部位與高波動。

## Insider activity
6 個月窗口（2026-05-01 至 2026-10-27，yf insider）：
- 公開市場買入：0 筆、$0M。
- 賣出：37 筆，合計約 $207.7M。
- 無任何內部人公開買入，為單邊賣出。

| 內部人 | 職稱 | 6 個月賣出（USD M） | 備註 |
|---|---|---|---|
| CHENG CHI FUNG | CTO | 103.5 | 多筆固定 27,500 股，2026-09 至 10 月近乎每週一次 |
| LAM YAT TUNG | COO | 67.0 | 2026-09-25 單筆 100,000 股，約 $205–208 |
| BRENNAN WILLIAM JOSEPH III | CEO | 17.5 | 約每月一次，約 16,700 股一筆 |
| FLEMING DANIEL W | CFO | 13.5 | 2026-10-08 賣出 7,580 股，約 $211–215 |
| LAUFMAN JAMES L | Officer | 4.4 | 小額定期 |
| 董事（Hoseini、Acevedo、Sutardja、Daneesh 等） | Director | 約 2.0 | 小額，另有年度股票授予 |

- 另有 2026-06-30 的 CEO 50,000 股與 CFO 25,000 股兩筆，Value 欄位為空，交易類型不明，未計入上表。
- 股票贈與（LAM 2026-09-25 175,000 股）與授予（董事 2026-10-13）不計入買賣。
- Cheng 單筆數值複算：27,500 股 × 約 $164 ≈ $4.5M，與工具回傳 $4.51M 相符，確認單位為 USD。
- 解讀限制：資料未標示 10b5-1 計畫，無法確認是否為預設交易。固定股數、定期賣出的型態與預設計畫相容，但不能僅憑資料下定論。

## Ownership
- 內部人持股 9.15%，機構持股 75.7%（float 口徑 83.3%），機構家數 1,335。
- 僅有當期快照，無歷史序列，無法判斷機構集中度的增減趨勢。

## Net sentiment score
- 分析師面：bullish，信心高（評等分布一致，但目標價來源不一）。
- 內部人面：bearish 偏向，信心中（6 個月約 $207.7M 單向賣出，0 買入；但可能屬計畫性賣出）。
- 散戶面：無法評估，信心低（Reddit / StockTwits 皆不可得）。
- Composite：neutral，信心低。分析師偏多與內部人單向賣出並存，缺少散戶資料使綜合判斷受限。

Divergence flag：無法判定（散戶傾向缺失，無法與分析師比較）。若以分析師（多）對內部人（賣）比較，則存在明顯分歧，但兩者性質不同，此分歧不能直接視為散戶與分析師背離。

資料缺口：Reddit（403）、StockTwits（DNS 不可解析）、yf recommendations 無逐筆評等變動、ownership 無時間序列。
