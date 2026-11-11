# Sentiment — 2382.TW (廣達) as of 2026-11-12

資料來源注意: Reddit 與 StockTwits 本次皆無法取得 (Reddit 回傳 fetch 失敗; api.stocktwits.com DNS 無法解析)，零售情緒部分僅能以 WebSearch 的二手資訊推估，信心偏低。Yahoo 的 cookie/crumb 也連線失敗，但 recommendations 與 major_holders 有回傳資料。分析師數字的快照日期不明，可能不是 11-12 當天的值。

## Analyst consensus
目前 rec_summary 為 17 buy (strongBuy 5 + buy 12) / 1 hold / 1 sell (strongSell 1)，共 19 家。近四個月 (0m 至 -3m) 分布完全相同，沒有觀察到評等上調或下調。外部快照顯示 Investing.com 的 consensus 為 Buy，另一份 aggregator 以 26 家分析師計算，目標價區間約 252.50 至 446.25 TWD，最樂觀 NT$420、最保守 NT$240 (Simply Wall St)。Goldman Sachs 在 2026-06-17 快照中為 Hold，目標 299 TWD。目標價的平均值在不同來源間差距很大 (約 364 至 375 TWD)，而各快照的股價落在約 287 至 330 TWD，需以即時報價為準。Investing.com 列出下次財報日為 2026-11-06 (或 6 月 11 日，日期格式不明)，此日期早於本報告日，財報後的評等變動未能從本次資料確認。

| 評等分布 | 家數 | 占比 |
|---|---|---|
| Strong Buy | 5 | 26% |
| Buy | 12 | 63% |
| Hold | 1 | 5% |
| Sell | 0 | 0% |
| Strong Sell | 1 | 5% |

## Retail social
- Reddit (r/wallstreetbets、r/stocks): 本次無法取得搜尋結果，無法列出樣本貼文或估計 tilt。
- StockTwits / X: StockTwits 無法連線。WebSearch 未找到 PTT 或 X 上的近期討論串，僅找到 Simply Wall St 社群 narrative 與券商研究摘要。
- 社群 narrative 偏多的敘述: AI 伺服器營收成長、雲端與 AI 需求擴張、全球供應鏈彈性。引用 KGI 2026-02 報告的說法，AI 伺服器佔伺服器營收已達 75 至 80% 以上。
- 社群 narrative 偏空的敘述: NB 需求疲弱、AI 伺服器毛利偏低、EV 與汽車業務弱、營運資金隨出貨增加而擴大、侵蝕自由現金流。Simply Wall St 空方 narrative 預估淨利率由 4.1% 降至 2.9%。
- 零售 tilt 判定: 無法可靠判定，僅依二手社群 narrative 看，偏多與偏空論述並存，略偏多。
- 討論量: 無法量化 (來源缺失)，定性判斷為低可見度，且未見明顯的 meme 式炒作跡象。
- Themes: AI 伺服器佔比與成長、毛利率壓力、營運資金與現金流、EV 與 NB 業務拖累、供應鏈與關稅風險。

## Insider activity
Net 6mo: 無資料。yf insider 回傳空陣列，無法得知 6 個月內的內部人買賣金額。這可能代表真的沒有申報，也可能是 Yahoo 連線失敗造成的缺漏，不能直接視為「無內部人交易」。若要確認，需以台灣公開資訊觀測站的董監事持股申報為準。

## Ownership shifts
- 內部人持股 (insidersPercentHeld): 29.7%
- 機構持股 (institutionsPercentHeld): 34.3%
- 機構佔流通股比例 (institutionsFloatPercentHeld): 48.9%
- 機構家數 (institutionsCount): 305
- 單一時點快照，無法判斷趨勢方向。內部人持股比例高，代表股權集中在控制股東手中，流通股的機構比重接近一半。

## Net sentiment score
Composite: **偏多 (bullish)**，信心中等偏低。
- 分析師面: 強烈偏多 (17/19 為買進，評等四個月未變，目標價高於多數快照股價)。
- 零售面: 無法可靠量測，二手 narrative 略偏多但含明顯空方論點。
- 內部人面: 無資料，無法計入。
- 股權面: 機構持股穩定但無趨勢資料。

Divergence flag: **無法判定**。分析師面偏多，零售面資料不足，無法確認是否與零售 tilt 相反。若後續補上 Reddit 或 StockTwits 資料，且零售偏空，才會成為值得注意的分歧訊號。

資料缺口與建議: (1) 允許 api.stocktwits.com 與 reddit.com 網域後重跑；(2) 以 TWSE 董監事持股申報補 insider 資料；(3) 以即時報價與財報後評等更新校正目標價與 consensus 快照。

SENTIMENT REPORT COMPLETE
