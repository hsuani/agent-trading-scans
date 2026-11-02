# Sentiment — GEV as of 2026-11-03

資料註記：今日系統日期為 2026-11-02，本報告以 2026-11-03 為基準日，取最新可得資料。Reddit 與 StockTwits 未直接抓取（依指示改用 WebSearch），零售情緒僅有聚合商快照，日期不明。

## Analyst consensus

38 家分析師：32 buy（含 6 strongBuy）/ 6 hold / 0 sell。相較前一個月（30 buy / 7 hold / 0 sell），buy 增加 2、hold 減少 1，整體偏多且略為上調。

| 指標 | 數值 | 來源 |
|---|---|---|
| Buy 占比 | 84%（32/38） | yf rec_summary |
| 共識目標價 | 約 $1,133（MarketBeat） | WebSearch |
| Susquehanna | 維持正面評等，目標價 $1,300 → $1,270（2026-10-14） | WebSearch |
| Morgan Stanley | 2026-08 由 overweight 降至 underweight | WebSearch（未經 yf 驗證） |
| GLJ Research | 首次覆蓋，Sell，目標價 $470 | WebSearch（未經 yf 驗證） |

注意：yf recommendations 只回傳月度彙總，沒有逐家券商的升降評等明細。Morgan Stanley 的 underweight 與 GLJ 的 Sell 與 yf 顯示的「0 sell」互相矛盾，可能是統計口徑或時間差，無法調和，請以券商原始報告為準。

## Retail social

- Reddit（r/wallstreetbets、r/stocks）：WebSearch 未找到近期 GEV 相關討論串。無法判斷傾向，列為資料缺口。
- StockTwits：官方情緒頁未能讀出標籤，無即時 bullish/bearish 比例。最近可得訊號為 2026-08 的 SentiSense，略偏多（30 日分數 6），並降溫，約 19 則提及/日。
- X / 聚合商（LunarCrush）：約 84–85% 正面，過去 24 小時約 369–377 則貼文。快照日期不明，未拆分 Reddit 或 WSB。
- 提及量：無常態基準可比，定性判斷為中等，無異常放量證據。
- 選擇權定位：Benzinga（日期不明）顯示 P/C ratio 1.27（偏 put），short float 3.2%。
- 主題：估值爭論（多方認為仍有空間，空方認為已反映 AI 電力需求超額定價）；AI 電力超級循環與指數資金流向；2026-05 曾出現明顯負面社群情緒（E*Trade 2026-05-20 提及），之後降溫。

## Insider activity

統計區間：2026-05-03 至 2026-11-03（6 個月）。

Net 6mo：約 $0 買入 / 約 $7.0M 賣出（可辨識的公開市場賣出）。

| 日期 | 姓名 | 職務 | 交易 | 股數 | 金額（USD M） |
|---|---|---|---|---|---|
| 2026-06-01 | ABATE VICTOR | Officer | Sale @ $948.08 | 4,819 | 4.57 |
| 2026-05-14 | POTVIN MATTHEW JOSEPH | Officer | Sale @ $1,059.09 | 2,333 | 2.47 |

- 2026-05-14 有 8 位董事各 495–1,350 股紀錄，無金額、無交易文字，判斷多為董事股票單位或例行配發，非公開市場買入，但資料無法確認。
- CEO STRAZIK SCOTT：2026-04-27 有 44,496 股衍生性證券轉換，2026-02-27 有 86,062 股紀錄，皆在窗口外。窗口內無公開市場交易。
- CFO PARKS KENNETH SCOTT：2026-02-27 與 2025-12-01 有股份紀錄，窗口內無公開市場交易。
- 內部人持股比例 0.13%，信號影響有限。
- 健全性檢查：ABATE 4,819 股 × $948.08 ≈ $4.57M，與 yf Value 欄位相符。

## Ownership shifts

- 機構持股 82.1%（約 4,234 家）。yf major_holders 只有單一時點快照，無法判斷趨勢方向。

## Net sentiment score

綜合：偏多（中等偏弱，信心低至中）

- 分析師面：強偏多（84% buy，無 sell 統計，近月小幅上調）。權重高，信心中高。
- 零售面：偏多但品質低。聚合商快照正面，但無 Reddit/StockTwits 直接讀數，日期不明。信心低。
- 內部人面：偏空傾向。窗口內約 $7.0M 公開市場賣出、零買入，但金額相對市值不大，兩位賣出者皆為 Officer，CEO 窗口內無交易。信心中。

背離旗標：否（零售與分析師同向偏多）。內部人賣出與分析師偏多方向相反，屬次要背離訊號。若 Morgan Stanley underweight 與 GLJ Sell 報導屬實，分析師面內部也有分歧，需以原始報告驗證。

SENTIMENT REPORT COMPLETE

Sources:
- [Webull: Do Wall Street Analysts Like GE Vernova Stock?](https://www.webull.com/news/15343149511877632)
- [MarketBeat GEV price target](https://www.marketbeat.com/stocks/NYSE/GEV/price-target/)
- [MarketBeat GEV forecast](https://www.marketbeat.com/stocks/NYSE/GEV/forecast/)
- [StockTwits GEV sentiment](https://stocktwits.com/symbol/GEV/sentiment)
- [Benzinga GEV sentiment](https://www.benzinga.com/quote/GEV/sentiment)
- [SentiSense GEV sentiment](https://app.sentisense.ai/stocks/GEV/sentiment)
- [LunarCrush GE Vernova](https://lunarcrush.com/fr/stock/ge-vernova-inc-gev)
- [E*Trade energy sentiment](https://us.etrade.com/knowledge/library/perspectives/daily-insights/energy-sentiment)
