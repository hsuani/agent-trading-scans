# Sentiment — ARM as of 2026-10-24

> 資料時效警示：本次 WebSearch 與社群來源最新只到 2026 年 9 月初，無法取得 10 月的新聞、評等變動或散戶討論。下列「散戶」與「近期變動」段落為舊資料或缺漏，請勿當作即時訊號。Reddit 與 StockTwits 抓取失敗（見下文）。

## Analyst consensus

Rating distribution（yf rec_summary，0m 期，單位：家數）：

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 合計 |
|---|---|---|---|---|---|---|
| 現在 (0m) | 8 | 21 | 13 | 1 | 0 | 43 |
| -1m | 8 | 21 | 12 | 1 | 1 | 43 |
| -2m | 7 | 20 | 13 | 1 | 1 | 42 |
| -3m | 7 | 20 | 11 | 1 | 1 | 40 |

目前為 29 Buy（含 Strong Buy）/ 13 Hold / 1 Sell，Buy 佔約 67%，Sell 僅 1 家。近三個月 Buy 由 27 增至 29、Sell＋Strong Sell 由 2 降至 1、Hold 由 11 增至 13。整體評等分布偏多，但 Hold 增加，代表部分機構態度轉為觀望，而非轉空。

近期評等變動：yf recommendations 工具只回傳彙總計數，沒有逐筆升降評等紀錄，因此無法列出具體 upgrade / downgrade 事件與日期。

目標價（僅能取得 9 月初資料，已過時）：
- Benzinga 8 月下旬平均目標價約 $272（27 家 Buy 共識）。
- Barchart 平均目標價約 $309，共識評級 "Moderate Buy"。
- 9 月初股價約 $258。
- 9 月前後分析師提醒：HSBC 認為市場已提前反映多年成長；Needham 首評為 Hold，並指市場對遠期成長的多空辯論偏負面。

## Retail social

- Reddit（r/wallstreetbets、r/stocks）：抓取失敗（WebFetch 無法連線 reddit.com，已 soft-fail）。WebSearch 也未找到 2026 年 10 月的 r/wallstreetbets 討論串，無法判定散戶語氣。
- StockTwits：抓取失敗（api.stocktwits.com 無法解析），無法計算訊息量與 bullish / bearish 標籤比例。
- X / 新聞評論（WebSearch，最新為 2026 年 7 至 9 月）：
  - 選擇權流向：7 月 14 日一則選擇權分析頁顯示整體偏空，put 成交金額高於 call。6 月 22 日同站記錄有 $420 履約價大量 call 買盤，偏多。
  - Benzinga（9 月前後快照）：put/call ratio 0.50，偏多；空單比率升至約 12.6% of float（快照日期不明）。
  - MarketBeat：空單部位近期增加約 8.39%（日期不明）。
- 聲量：無法量化。以搜尋結果數量判斷，2026 年 9 月後幾乎無可用的散戶內容，聲量相對前期應屬偏低，但這是推論，非實測。
- Themes（僅能依 9 月前後媒體與分析師文章歸納，非散戶原文）：
  - 多空爭議集中在「2027 年以後的版稅與授權成長是否已被價格反映」。
  - 股價由 6 月 22 日兩年高點 $445.05 大幅回落，7 月財報前後跌至 $201.32，之後回升，波動劇烈。
  - Haas 大額股權激勵案（最高約 $800M，ISS 與 Glass Lewis 建議反對，SoftBank 持股約 86% 使否決機率低）。
- 散戶語氣：無法判定（bullish / bearish / mixed 皆無足夠樣本）。

## Insider activity

以 2026-04-24 至 2026-10-24 為 6 個月窗口（yf insider 原始值為 USD）。

- 公開市場買入（Purchase）：0 筆，合計 $0。
- 公開市場賣出（Sale，已剔除無金額之獎勵 / 贈與）：約 $56.4M，合計 21 筆，其中大多數集中於 5 月 11 至 22 日（財報後開放交易窗口）以及 6 月。
- 股權獎勵（Stock Award）：5 月 15 日大量授予，CEO Rene Haas 265,643 股、CFO Jason Child 81,359 股等（無現金流）；8 月 31 日 Haas 64 股 grant（$15,482，以 $241.91 計）。
- Notable：
  - CFO Jason E. Child：5 月 20 日賣出約 $7.23M（31,920 股，$226.54）；8 月 27 日賣出 $2.66M（10,400 股，$255.33）；9 月 21 日賣出 $3.12M（10,400 股，$300.00）。三次合計約 $13.0M，為窗口內最持續的賣方。
  - Officer Spencer Collins：5 月 11 日賣出約 $11.0M（51,961 股，約 $211.7）；5 月 19 日賣出約 $8.8M（40,941 股，$215.00）。
  - Officer William Abbey：5 月至 6 月多筆賣出，合計約 $10M 以上。
  - CEO Rene Haas：窗口內無公開市場賣出；3 月與 4 月的賣出（約 $6.6M）已在 6 個月窗口之前。
  - 解讀註記：多數賣出可能為 10b5-1 計畫或稅務相關處置，無法從資料判定動機。大額與持續性賣出仍是偏空的訊號，但無買入對照，信心中等偏低。

## Ownership

- 機構持股：96.2%（institutionsPercentHeld），機構數 1,304 家。
- 內部人持股：0.07%（yf 數值，以 float 計算）。
- 趨勢：yf major_holders 只提供單一快照，無法判定近期集中度變化。
- 資料註記：SoftBank 約持有 86% 股權（來源見 Capital.com 摘要），與 yf 的「機構 96%」口徑明顯不同，前者為控股股權，後者應為 float 口徑。兩者不能直接比較，本報告以「控股集中、float 機構化高」理解。

## Net sentiment score

- 分析師（Analyst）：偏多（Buy 佔約 67%，Sell 僅 1 家，近三月趨勢略偏多）。信心：中高。注意：目標價與評級資料皆為 9 月前的快照。
- 散戶（Retail）：無法判定。Reddit、StockTwits 皆抓取失敗，X / 新聞來源最新僅到 9 月，樣本不足。信心：低。
- 內部人（Insider）：偏空（6 個月約 $56.4M 公開市場賣出、零買入，CFO 與多位 officer 持續賣出）。但多數屬窗口內或計畫性處置，信心：中偏低。
- 選擇權與空單：混合（7 月偏空，9 月 P/C 0.50 偏多；空單比率上升）。信心：低，日期不一。

Composite：**中性偏多（neutral-to-bullish），信心：中低**。分析師面偏多，內部人面偏空，散戶面缺資料。綜合來看，訊號強度有限，主要受限於本期社群資料缺漏。

Divergence flag：**無法判定**。散戶語氣資料不足，無法確認是否與分析師傾向相反。若 10 月取得可靠散戶資料後，應再檢視是否出現「分析師偏多、散戶偏空」或相反的背離。

## 資料缺口與後續建議

1. Reddit（r/wallstreetbets、r/stocks）與 StockTwits 皆無法取得，需由其他管道或稍後重試。
2. 2026 年 9 月後無可用新聞，10 月的評等變動、目標價調整與財報後反應需補查。
3. yf recommendations 無逐筆評等變動，需改用其他來源取得 upgrade / downgrade 清單。
4. 目標價與股價參考值皆為 8 至 9 月資料，不應作為 10 月 24 日的現價或目標價使用。

## 參考來源（WebSearch 摘要，僅列出實際用於本報告者）

- [Benzinga ARM sentiment](https://es.benzinga.com/quote/ARM/sentiment)
- [Capital.com ARM stock forecast](https://capital.com/en-gb/analysis/arm-holdings-stock-forecast)
- [Barchart: ARM downgrade story](https://www.barchart.com/story/news/3282839/this-analyst-just-downgraded-arm-stock-here-s-why)
- [Investing.com ARM scoreboard](https://www.investing.com/equities/arm-scoreboard)
- [Historical Option Data, ARM 2026-07-14](https://historicaloptiondata.com/?p=68167)
- [MarketBeat ARM news](https://www.marketbeat.com/stocks/NASDAQ/ARM/news)

SENTIMENT REPORT COMPLETE
