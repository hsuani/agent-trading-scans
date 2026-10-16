# Sentiment — AMT as of 2026-10-17

## Analyst consensus
25 家覆蓋 (yf rec_summary)：7 strongBuy / 15 buy / 3 hold / 0 sell / 0 strongSell，買進類佔 88%，無賣出評等。
近四個月 (-3m 至 0m) 結構幾乎不變，唯一變化為 hold 由 4 降為 3、strongBuy 由 6 升為 7。

Recent moves：yf 的 recommendations 端點僅回傳彙總計數，沒有逐家機構的升降評事件，因此以下個別事件來自 WebSearch 聚合頁，未經一手來源核實：
- Mizuho：Buy，目標價 $208（2026-08-20）
- Barclays：升評至 Buy，目標價 $198（2026-08-20）
- BMO Capital：升評至 Market Perform，目標價 $195（2026-07-29，由 $190 上調）

目標價共識：聚合頁顯示平均 12 個月目標價約 $215.70，高 $260、低 $188（約 23 家覆蓋）。覆蓋家數與 yf 的 25 家略有出入，屬不同時點快照，僅供參考。
股價參照：聚合頁提及近期約 $175 附近，未取得 2026-10-17 的已核實收盤價。

## Retail social
- Reddit：WebSearch 未取得任何 2026 年 r/wallstreetbets 或 r/stocks 的 AMT 相關討論串，回傳皆為低品質股票聚合頁。**資料缺口，無法判定 tilt。**
- StockTwits：未取得 2026 年 AMT 的 bullish/bearish 比例，僅有第三方頁面的價格報導。**資料缺口。**
- X / 新聞：無可用的社群情緒樣本。WebSearch 結果以分析師評等與 Barchart 文章為主，屬機構側而非散戶側資料。
- 聲量：無法量化，相對於典型水準無法判斷。
- 主題 (由有限來源歸納，非散戶原文)：
  - 防禦性 REIT 與長期合約、穩定現金流 (多頭論點)
  - 業者需在未來 5 年將容量加倍，對基礎設施有利 (多頭論點)
  - EchoStar 租約取消風險與營運商整併 (空頭論點，出自 Investing.com SWOT 摘要)
  - 過去 52 週股價落後大盤 (Barchart 報導，約 -19%)

## Insider activity
統計區間：2026-04-17 至 2026-10-17 (6 個月)，僅計公開市場買賣，排除 Stock Award/Grant 與 Gift。

Net 6mo：約 $0.50M 買入、約 $1.38M 賣出，淨賣出約 $0.88M。

Notable：
- Kalathur Rajesh，Director，2026-08-21 買進 2,829 股 @ $177.00，約 $0.50M。為此區間唯一的重要買入，同一人於 2026-03-10 另以 $185.30 買進 2,671 股 (約 $0.49M，已超出 6 個月窗口)。
- Meyer Robert Joseph Jr，Officer，2026-07-29 賣出 5,000 股 @ $178.89，約 $0.89M。
- Dowling Ruth T，General Counsel，2026-07-29 賣出 1,791 股 @ $169.54-$174.96，約 $0.31M；2026-04-29 另賣出 972 股，約 $0.17M。
- CEO Steven Vondran 與 CFO Rodney Smith：窗口內無公開市場交易。最後一次大額賣出分別在 2026-03-04 (約 $6.3M) 與 2026-02-17 (約 $6.6M)，均已超出窗口。
- 2026-10-01 Paul Blanchett (Officer) 獲配 16,299 股股票獎勵，屬授予而非買賣。

解讀：高階管理層近期賣出多為行使既有選擇權後出售 (部分交易附帶 derivative conversion 紀錄)，規模對比其持股不算大；唯一的獨立董事買進發生在股價約 $177-$185 區間。

## Ownership shifts
- 機構持股：96.8%，機構家數 2,389。
- 內部人持股：0.08%。
- 趨勢：yf major_holders 僅提供目前快照，無歷史序列，無法判斷集中度的方向性變化。

## Net sentiment score
Composite：**中性偏多 (信心：低)**
- 分析師面：偏多 (88% 買進類評等，評等結構穩定，目標價區間高於 $175 參照價)。
- 內部人面：偏空至中性 (窗口內淨賣出約 $0.88M，但多為管理層行使選擇權後的出售，且有一筆獨立董事買進)。
- 散戶面：無資料，無法納入評分。
- 信心偏低的原因：散戶樣本完全缺失，且分析師事件細節來自未核實的聚合頁。

Divergence flag：**無法判定**。缺乏可靠的散戶 tilt 樣本，無法比較與分析師傾向是否相反。

資料品質注意事項：
- yf 的 cookie/crumb 取得失敗 (ConnectionError)，但資料仍有回傳，數值可用。
- Reddit、StockTwits 與 X 在本次環境中無有效結果；WebSearch 回傳多為重複的自動生成頁面，已剔除。
- 下一個催化事件為 Q3 2026 財報，日期來源不一致 (10-22 與 10-27)，需至投資人關係頁確認。

SENTIMENT REPORT COMPLETE
