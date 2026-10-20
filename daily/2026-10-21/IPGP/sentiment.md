# Sentiment — IPGP as of 2026-10-21

## Analyst consensus
9 位分析師（yf `rec_summary`，cache）：6 buy（2 strongBuy + 4 buy）/ 2 hold / 1 sell（strongSell 1）。0m、-1m、-2m 三期分布完全相同，近三個月無可見評等變動。yf `recommendations` 僅回傳彙總，不含逐筆升降評等，故個別升降級為 DATA_UNAVAILABLE。

網路搜尋補充（非 yf 原始資料，日期與來源不一，未與 yf 交叉核對）：
- Needham 於 2026-05 由 Hold 升至 Buy，PT $110，理由為 book-to-bill 高於 1.0。此事件在 yf 三期窗口之外，與 yf 無衝突。
- Bank of America Securities 為唯一 Sell，PT $92.50。
- 平均 12 個月目標價報導數字不一，約 $126 至 $133，高點約 $152，低點約 $92.5。
- 最近一期財報為 FQ2 2026（2026-08-04），TipRanks 報導獲利優於預期。
- 內部人成交價由 2026-05 至 06 的 $117 至 $120，降至 2026-10-02 的 $85 至 $86，股價區間相關報導價格不一，以內部人成交價作為參考錨點。

## Retail social
- Reddit r/wallstreetbets、r/stocks：DATA_UNAVAILABLE。WebFetch 無法連線 www.reddit.com，WebSearch 亦未索引到 IPGP 相關討論串。
- StockTwits：DATA_UNAVAILABLE。api.stocktwits.com DNS 解析失敗（ENOTFOUND）。
- X：未取得可核實的貼文樣本。
- 討論量：DATA_UNAVAILABLE（無法與基準比較）。
- 散戶傾向：DATA_UNAVAILABLE。
- 主題：無散戶來源可用。以下僅為新聞媒體與分析平台的報導主題，並非散戶意見：
  - 獲利優於預期，國防、醫療、系統市場拓展（TipRanks）。
  - 股價高於內在價值（Simply Wall St）。
  - 關稅影響與估值為近期催化劑。

## Insider activity
6 個月窗口（2026-04-21 至 2026-10-21），僅計 open-market 交易（排除獎勵股與權證轉換）：
- 買入：$0.20M，1 筆（PEELER JOHN R，董事，2026-08-26，$72.84 至 $74.57，2,710 股）。
- 賣出：$23.38M，13 筆。
- 淨額：約 -$23.18M。

主要交易（依金額排序）：

| 日期 | 人員 | 職稱 | 交易 | 金額 |
|---|---|---|---|---|
| 2026-06-29 | IP FIBRE DEVICES LTD | 10% 以上受益人 | 賣出 | $6.81M |
| 2026-07-21 | VALENTIN GAPONTSEV TRUST I | 10% 以上受益人 | 賣出 | $5.76M |
| 2026-08-05 | IP FIBRE DEVICES LTD | 10% 以上受益人 | 賣出 | $2.90M |
| 2026-07-31 | IP FIBRE DEVICES LTD | 10% 以上受益人 | 賣出 | $2.32M |
| 2026-09-02 | VALENTIN GAPONTSEV TRUST I | 10% 以上受益人 | 賣出 | $2.07M |
| 2026-10-02 | IP FIBRE DEVICES LTD | 10% 以上受益人 | 賣出 | $1.32M |
| 2026-05-22 | MAMMEN TIMOTHY P V | CFO | 賣出 @ $119.6 至 $120.4 | $1.20M |
| 2026-10-02 | SCHERBAKOV EUGENE A | 董事，10% 以上受益人 | 賣出 | $0.26M |
| 2026-05-14 | DESMOND JEANMARIE F. | 董事 | 賣出 | $0.18M |
| 2026-06-22 | AGNES TANG | 董事 | 賣出 | $0.18M |
| 2026-06-29 | LOPRESTI ANGELO P | General Counsel | 賣出 | $0.11M |

重點觀察：
- 10% 以上受益人實體（IP FIBRE DEVICES LTD、VALENTIN GAPONTSEV TRUST I、SCHERBAKOV EUGENE A）合計賣出約 $21.7M，占窗口賣出總額約 93%。資料未標示實體與創辦人的關係，此為推論，不作定論。
- 2025-09 起即可見 IP FIBRE DEVICES 與 Gapontsev Trust 的持續賣出，屬既有模式，並非近期才出現的新動作。
- CEO GITIN MARK MILTON：窗口內無 open-market 交易，僅有 2026-02-18 的獎勵股（不在窗口內）。
- CFO MAMMEN 於 2026-05-22 賣出 $1.20M，為窗口內唯一的 CFO 交易。
- 唯一的 open-market 買入來自董事 PEELER，價位在 $73 至 $75，較 10 月成交價低約 13%。

## Ownership shifts
- 機構持股 75.53%，持有機構 491 家。內部人持股 38.98%（含 10% 以上受益人，數字偏高屬正常）。
- 前十大機構（2026-06-30 13F 數據）：

| 機構 | 持股比例 | QoQ 變動 |
|---|---|---|
| First Eagle Investment Management | 7.85% | -27.3% |
| BlackRock | 6.70% | +5.1% |
| Vanguard Portfolio Management | 3.87% | +0.4% |
| Dimensional Fund Advisors | 3.76% | -5.9% |
| Lazard Asset Management | 3.36% | +3.9% |
| Sumitomo Mitsui Trust Group | 3.20% | +0.9% |
| Victory Capital Management | 3.09% | +325.6%（基期可能很小，需留意） |
| Vanguard Capital Management | 2.71% | +1.1% |
| Neuberger Berman Group | 2.30% | +15.7% |
| State Street | 2.14% | +11.0% |

- 趨勢：前十大中 8 家增持、2 家減持。最大持股 First Eagle 減持超過四分之一，是最主要的負向訊號。
- 數據品質：yf `major_holders` 的 `institutionsFloatPercentHeld` 為 1.23789（超過 100%），不可用。

## Net sentiment score
- 分析師面：偏多。6 buy / 2 hold / 1 sell，buy 占 67%。目標價報導普遍高於近期成交價。
- 內部人面：偏空。6 個月 open-market 淨賣出約 $23.2M，但主要來自 10% 以上受益人實體的持續減持，CEO 無窗口內交易，訊號強度有限。
- 散戶面：DATA_UNAVAILABLE。
- 機構面：中性偏多。持股集中度高，多數前十大機構增持，但最大持股減持。

**綜合傾向：中性（信心：低）**。分析師偏多，內部人淨賣出偏空，散戶情緒無法取得，三者無法形成一致結論。

**背離旗標：是（有限）**。分析師偏多與內部人淨賣出方向相反。散戶面缺資料，無法判定散戶與分析師是否背離。

## 資料缺口
- Reddit、StockTwits 無法取得，散戶情緒與討論量全部為 DATA_UNAVAILABLE。
- yf `rec_summary` 與 `recommendations` 為 cache，實際更新時間未知。
- 逐筆評等變動與目標價變動無法由 yf 取得，僅能參考網路報導，且來源日期不一。
- 股價區間在不同來源差異很大（52 週低點有 $71.35 與 $50.12 兩種說法），本報告未採用任何股價數字作為判斷依據。

## 來源
- yf：`rec_summary`、`recommendations`、`insider`、`major_holders`、`inst_holders`（cache）。
- 網路搜尋：[TipRanks 分析師新聞](https://www.tipranks.com/news/new-analyst-support-means-big-gains-for-ipgp-stock)、[Yahoo Finance Needham 升級報導](https://finance.yahoo.com/markets/stocks/articles/needham-upgrades-ipg-photonics-ipgp-121632650.html)、[Investing.com 共識預估](https://www.investing.com/equities/ipg-photonics-corp.-consensus-estimates)、[Google Finance IPGP](https://www.google.com/finance/quote/IPGP%3ANASDAQ)、[Simply Wall St IPG Photonics](https://www.simplywall.st/stocks/us/tech/nasdaq-ipgp/ipg-photonics)。

SENTIMENT REPORT COMPLETE
