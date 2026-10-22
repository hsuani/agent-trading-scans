# Sentiment — TSM as of 2026-10-22

## Analyst consensus
21 名分析師評級 (rec_summary)：6 strong buy / 14 buy / 1 hold / 0 sell / 0 strong sell，買進比例約 95%。近四個月趨勢：-3m 與 -2m 為 19 家（18 buy + 1 hold），-1m 起增至 21 家（20 buy + 1 hold），無任何 sell 評級。近一個月的增量來自 buy 由 12 增為 14，屬於新增覆蓋或上調，未見降評紀錄。

Yahoo info 欄位顯示 numberOfAnalystOpinions 為 20、recommendationKey 為 strong_buy，與 rec_summary 的 21 家略有出入，屬資料源差異，以 rec_summary 為準。

目標價：targetMeanPrice 約 $584.39，targetHighPrice $1,000，targetLowPrice $440；現價 $431.89（cache 更新於 2026-10-22），距均值目標約 +35%。最低目標 $440 略高於現價。

近期調整（來自網路搜尋，多為 2026 年 7 月前後，未能確認 10 月內的評級變動）：
- D.A. Davidson（2026-07-17）：目標價上調至 $500。
- UBS：目標價由 T$3,000 上調至 T$3,400，維持 Buy。
- Citi：目標價由 NT$2,875 上調至 NT$3,800，維持 Buy。
- MarketBeat 彙整平均目標 $496.25（7 月底資料）。

注意：Yahoo 目標均值 $584 與 MarketBeat 的 $496 差距明顯，代表不同來源的樣本與日期不一致，引用時需標註來源。

財報：2026-10-15 公布 Q3，EPS 4.60 vs 預估 4.52（surprise +1.67%）。前一季（7 月中）EPS 4.31 vs 3.89（surprise +10.89%）。下次財報日 2027-01-14，EPS 預估 5.16。

## Retail social
- Reddit：WebSearch 對 r/wallstreetbets 與 r/stocks 皆無法取得 TSM 相關串文，無 2026 年 10 月的樣本。依規定以 WebSearch 為準，此來源 DATA_UNAVAILABLE（未能取得可用 thread）。無法給出 Reddit 的語氣判斷。
- StockTwits：AltIndex 頁面（日期未標示）顯示 Sentiment 分數 90/100，偏多；平均每日提及約 89 則，較三個月前下降約 52%，屬聲量降溫。月度提及數：2026-03 為 162、2026-07 為 483、2026-08 為 173。StockTwits API 本次未直接抓取，屬 soft-fail。
- X / 其他聊天：Historical Option Data 的 X 情緒頁面，6 月為 75% 偏多，7 月為 72%，7 至 8 月中某頁為 60% 偏多 / 20% 偏空 / 20% 中性，且各頁價格數字彼此矛盾，數據可信度低，只能作為方向參考。
- 其他：Boursorama 論壇與 Korean/German 金融頁面有討論，但無法量化。
- 聲量判斷：以 StockTwits 月度提及看，8 月較 7 月明顯降溫，接近 3 月水準的 1.1 倍，屬於中低於近期高點的平靜期（定性判斷）。

## Insider activity
資料窗口 2026-04-22 至 2026-10-22（6 個月）：
- 淨買入約 $24,378（4 筆，全部為 TIEN BOR-ZEN，feed 標示 Position = Officer）
- 賣出：0 筆
- 淨額：+$24.4K，全為買進

明細：
- 2026-07-28：買入 15 股 @ $390.00，約 $5,850
- 2026-07-20：買入 10 股 @ $405.00，約 $4,050
- 2026-05-20：買入 17 股 @ $391.81–400.00，約 $6,718
- 2026-04-28：買入 20 股 @ $386.00–390.00，約 $7,760

窗口外參考：2026-03-31 DIRECTOR BURNS URSULA M 買入 1,000 股 @ $322.05，約 $322,050（距今約 6.7 個月，不計入 6 個月淨額）。

判讀：本窗口內買入金額小，但連續四筆、跨四個月、價格區間約 $386–405，屬於小額但持續的加碼訊號。Feed 未標示 Tien Bor-Zen 的具體職稱，本報告不自行推斷。

## Ownership shifts
- insidersPercentHeld 0.013%（ADR 結構下內部人持股比例不具參考價值）
- institutionsPercentHeld 15.5%，機構數 4,687 家（ADR 持有人結構，參考性有限）
- 前十大機構持股（2026-06-30 季報）變動，方向混合：
  - 增持：BlackRock +10.4%、Morgan Stanley +7.3%、Goldman Sachs +71.5%、Capital World +4.5%、Bank of America +8.3%、Fisher +1.3%（6 家）
  - 減持：Van Eck -10.7%、Sanders Capital -6.8%、FMR -2.4%、JPMorgan -0.7%（4 家）
- 最大持有者 FMR 持股 58.9M 股（1.14%），但較上期減少 2.4%。
- 整體判讀：前十大中增持家數略多於減持，但幅度不一，無明顯集中化或撤出趨勢。

## Net sentiment score
Composite：**偏多（bullish）**，信心中等。

依據：
- 分析師：強烈偏多（95% 買進，無賣出，目標價均值仍高於現價約 35%）。權重高。
- 內部人：小額但持續買入，無賣出。權重中低。
- 機構：前十大增減混合，偏中性。
- 散戶：StockTwits 分數偏多但聲量明顯降溫；Reddit 無資料；X 數據可信度低。權重中等，但資料缺口大，信心下調。

信心下調原因：Reddit 缺資料、StockTwits 日期不明、X 來源矛盾，散戶面向只能給出低至中等信心。

Divergence flag：**否**。分析師與散戶（有限資料）同為偏多，未見反向背離。唯一的弱訊號是散戶聲量降溫，若後續 Reddit 或 StockTwits 聲量持續下滑，與分析師偏多形成「分析師強、散戶冷」的背離，屆時需重新檢視。

## 資料缺口與來源
- Yahoo Finance 即時 API 在本次 session 因 proxy 限制多數失敗（guce / query2 / fc.yahoo.com），主要資料取自 repo cache prices/yf/TSM.json（refreshed 2026-10-22T11:41Z），_misses 為空。
- Reddit：WebSearch 無結果，DATA_UNAVAILABLE。
- StockTwits API：未直接抓取，依 AltIndex 第三方頁面。
- 網路搜尋結果日期多為 2026 年 7–8 月，未能找到 2026 年 10 月的分析師變動或散戶貼文，故本報告的「近期」僅能覆蓋至 2026 年 8 月前後。

來源（WebSearch 結果）：
- https://www.marketbeat.com/instant-alerts/taiwan-semiconductor-manufacturing-nysetsm-trading-down-15-time-to-sell-2026-07-28/
- https://altindex.com/ticker/tsm/stocktwits-mentions
- https://historicaloptiondata.com/?p=71779
- https://tipranks.com (search summary, D.A. Davidson / UBS / Citi 7 月評論)

SENTIMENT REPORT COMPLETE
