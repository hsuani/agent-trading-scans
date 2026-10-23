# Sentiment — GEV as of 2026-10-23

資料品質說明：分析師評等來自 `pipeline/tools/yf` 的即時 rec_summary，內部交易與持股來自 yf；散戶情緒（Reddit、StockTwits、X）無法直接抓取，只能用 WebSearch 取得的二手快照，且多數停留在 5 月至 8 月。散戶面以 DATA_UNAVAILABLE 為主，下方的結論信心據此降低。

## Analyst consensus

38 家覆蓋：6 strong buy / 25 buy / 7 hold / 0 sell / 0 strong sell。

| 期間 | Strong Buy | Buy | Hold | Sell | 買方占比 |
|---|---|---|---|---|---|
| 當期 (0m) | 6 | 25 | 7 | 0 | 81.6% |
| -1m | 6 | 24 | 7 | 0 | 79.0% |
| -2m | 6 | 24 | 7 | 0 | 79.0% |
| -3m | 6 | 24 | 8 | 0 | 78.9% |

Recent moves: yf 的 recommendations 工具回傳與 rec_summary 相同的期間快照，沒有逐筆升降評等紀錄，因此個別券商的升降級 DATA_UNAVAILABLE。近三個月買方家數由 30 增至 31、持有由 8 降至 7，評等結構小幅偏多但幅度不大。

網路快照（時效不一）：
- MarketBeat 10 月初彙整的共識為 Moderate Buy，平均目標價約 USD 1,172，並註記有一家券商降評至 hold。
- Guggenheim 在 7 月財報後把目標價由 USD 1,300 上調至 USD 1,450，MarketBeat 目標價區間約 USD 580 至 USD 1,450。
- Mizuho 7 月維持 Neutral，目標價 USD 949。
- 10 月 7 日股價約 USD 997.79，當日下跌 3.1%。

目標價與股價為 WebSearch 來源，無法與 yf 交叉驗證；覆蓋家數在 5 月 Barchart 報導為 30 家，與 yf 的 38 家不同，以 yf 為準。

## Retail social

- Reddit (r/wallstreetbets、r/stocks)：WebSearch 未回傳任何 GEV 相關討論串，無法取得聲量或語氣。DATA_UNAVAILABLE。
- StockTwits：StockTwits 情緒頁面快照未顯示情緒分數（N/A），無法判讀當前多空比。DATA_UNAVAILABLE。
- X：未取得可用的貼文或聲量資料。DATA_UNAVAILABLE。
- 替代訊號（時效過期，僅供參考）：
  - Benzinga 8 月快照：選擇權 put/call ratio 1.27，標示為偏空；空單占浮動股約 3.2%。
  - SentiSense 8 月快照：30 日情緒分數 6（略偏多），但單日已降溫至 -4；新聞提及 74% 為正面。
  - E*TRADE 5 月報導：股價自 4 月歷史高點回落後，社群情緒出現明顯負面極端值。
- 聲量（相對於常態）：無可量化數據，DATA_UNAVAILABLE。
- 主題（由新聞與分析快照歸納，非社群原文）：AI 與資料中心電力需求、股價自高點回檔後的估值與波動、10 月財報預期（Earnings Whispers 列 10 月 28 日，每股預估 USD 4.01；TrendSpider 列 10 月 21 日，日期衝突未確認）。

散戶傾向：無法在當日判定。最近可得的多筆快照偏向「新聞正面、選擇權與社群偏空」的混合態勢。

## Insider activity

評估區間 2026-04-23 至 2026-10-23（6 個月）。

公開市場買進：無（0 筆）。

公開市場賣出（USD）：約 USD 7.04M
| 日期 | 人員 | 職稱 | 性質 | 股數 | 金額 (USD) |
|---|---|---|---|---|---|
| 2026-06-01 | ABATE VICTOR | Officer | 賣出 @ 948.08 | 4,819 | 4.57M |
| 2026-05-14 | POTVIN MATTHEW JOSEPH | Officer | 賣出 @ 1,059.09 | 2,333 | 2.47M |

其他異動（非買賣）：
- 2026-04-27 STRAZIK SCOTT（CEO）：衍生性證券行權 44,496 股（行權價 92.13 至 149.78），yf 標示金額 USD 5.35M。屬選擇權行權，不等同市場買進，且區間內未見對應的同期賣出紀錄。
- 2026-05-14 董事會成員約 8 人各領取約 495 至 1,350 股，屬年度董事股權獎勵，無現金金額。

Net 6mo：USD 0 買進 / 約 USD 7.04M 賣出（公開市場）。CEO 未有區間內公開賣出，CFO Parks 最近一次紀錄為 2025 年 12 月與 2026 年 2 月，皆在區間之外。賣出者為兩位非 CEO/CFO 的高階主管。

內部人持股比例 0.13%，比例極低，因此內部人交易對整體籌碼的解讀空間有限。

## Ownership shifts

- 機構持股比例 81.5%，機構家數 4,249（yf major_holders 單一快照）。
- 季度變化趨勢：DATA_UNAVAILABLE（工具未提供歷史序列，無法判讀集中化或分散化方向）。

## Net sentiment score

Composite: **偏多（bullish），信心中低**

- 分析師面：偏多，信心高。31/38 為買方評等，0 家賣方，目標價區間寬但共識仍偏多。
- 散戶面：無法判定（DATA_UNAVAILABLE）。最後可得的快照偏向混合或偏空（選擇權偏空、5 月社群負面），但時效已超過兩個月。
- 內部人面：偏空至中性。6 個月內約 USD 7.04M 公開市場賣出、零買進，但集中於兩位高階主管，且內部人持股比例極低，訊號強度有限。

降低信心的因素：散戶資料缺席、社群快照過期、財報日期未確認（10 月 21 日或 28 日）、目標價與股價來源不一致。

Divergence flag: **無法確認（tentative: yes，待驗證）**。分析師面偏多，而最後可得的散戶與選擇權快照偏空，若該快照仍成立則屬於背離，但證據時效不足，不宜作為結論。建議在 10 月財報前後重抓 StockTwits、Reddit 與選擇權 put/call 以確認。

## Sources

- [MarketBeat GEV 10 月 7 日股價快照](https://www.marketbeat.com/instant-alerts/price-ge-vernova-nyse-gev-stock-price-down-31-heres-why-2026-10-07/)
- [MarketBeat GEV 分析師預測](https://www.marketbeat.com/stocks/NYSE/GEV/forecast/)
- [MarketBeat GEV 目標價](https://www.marketbeat.com/stocks/NYSE/GEV/price-target/)
- [Webull: Do Wall Street Analysts Like GE Vernova Stock?](https://www.webull.com/news/15343149511877632)
- [Barchart: Are Wall Street Analysts Predicting GE Vernova Stock Will Climb or Sink](https://www.barchart.com/story/news/37384347/are-wall-street-analysts-predicting-ge-vernova-stock-will-climb-or-sink)
- [Barchart: Do Wall Street Analysts Like GE Vernova Stock?](https://www.barchart.com/story/news/3627052/do-wall-street-analysts-like-ge-vernova-stock)
- [Benzinga GEV Sentiment](https://www.benzinga.com/quote/GEV/sentiment)
- [SentiSense GEV Sentiment](https://app.sentisense.ai/stocks/GEV/sentiment)
- [StockTwits GEV Sentiment（快照無分數）](https://stocktwits.com/symbol/GEV/sentiment)
- [Earnings Whispers GEV](https://www.earningswhispers.com/stocks/GEV)

SENTIMENT REPORT COMPLETE
