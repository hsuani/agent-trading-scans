# Sentiment — CRWD as of 2026-11-27

資料限制：今日系統日期為 2026-11-26，本報告依指定的 as-of 2026-11-27 撰寫。最新可得內部人交易日期為 2026-11-24，分析師資料為快取版本。Reddit 與 StockTwits 直連在沙箱中被阻擋，改用 WebSearch。直連來源皆標為 DATA_UNAVAILABLE。

## Analyst consensus

資料來源：`pipeline/tools/yf CRWD rec_summary`（快取，source: cache）。

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 合計 | 買進占比 |
|---|---|---|---|---|---|---|---|
| 當期 (0m) | 8 | 30 | 11 | 0 | 0 | 49 | 77.6% (38/49) |
| 上月 (-1m) | 10 | 30 | 12 | 0 | 1 | 53 | 75.5% (40/53) |
| -2m / -3m | 10 | 30 | 12 | 0 | 1 | 53 | 75.5% |

結論：49 位分析師中，38 買進 (78%)、11 持有 (22%)、0 賣出。近一個月買進占比小幅上升，Strong Sell 由 1 降為 0。

Recent moves:
- Hold 減少 1 家、Strong Sell 減少 1 家，與 WebSearch 提到的 Deutsche Bank 於 11/2 由 Hold 升為 Buy 方向一致，但該升評與 PT 調整 (240 至 300 USD) 僅來自二手網站，未經官方來源核實。
- -2m 與 -3m 數字與 -1m 完全相同，疑似快取未更新，歷史趨勢可信度低。
- 目標價 (Target price)：yf 工具未提供 PT 資料，DATA_UNAVAILABLE。網路上的說法互相矛盾（平均 PT 約 248.28 USD 與 300 USD 等），不採用。

## Retail social

- Reddit：DATA_UNAVAILABLE。直連 r/wallstreetbets 與 r/stocks search.json 被阻擋。WebSearch 找不到 2026-11 的 CRWD 相關討論串，只找到 2026-02 的一則 r/wallstreetbets 熱門串（主題是 Claude code-review 工具導致 CRWD 與 NET 下跌，約 1,200 贊與 241 則留言），以及多個 SEO 內容站的泛用描述（"Reddit sentiment bullish, 71.95 / 78"），這些來源日期不明或與 11 月無關，不納入評分。
- StockTwits：直連 DATA_UNAVAILABLE。WebSearch 找到的 StockTwits 文章 (Fal.Con 2026 前瞻) 提到散戶情緒「極度看多」且訊息量「高」，但文章日期不明，無法確認是否落在 11 月下旬，信心低。
- X：未取得有效結果，DATA_UNAVAILABLE。
- 訊息量 (Buzz volume)：DATA_UNAVAILABLE，無法與平時基準比較。
- 主題（僅依可得的二手報導，信心低）：
  - 11/17 單日下跌 9.9%，被歸因於高估值軟體股的風險趨避，以及 CEO 持續出售股票的消息。
  - 「AI 交易退潮」敘事，同類股 (PANW、NET) 同步下跌。
  - 12/1 或 12/2 的 Q3 財報是下一個催化劑（日期來源不一致）。
- 散戶傾向：無法可靠判定，標為 DATA_UNAVAILABLE。

## Insider activity

資料來源：`pipeline/tools/yf CRWD insider`，取 2026-05-27 至 2026-11-24 共 6 個月的交易。金額為 USD，以 B/M 表示。Grant (授予) 與 Gift (贈與) 的 0 金額列不計入。

買進：0 筆，$0。
賣出合計：約 $447.9M (= $0.448B)，共 120 筆交易中的 Sale 部分。

| 內部人 | 職稱 | 賣出金額 (USD M) | 筆數 |
|---|---|---|---|
| George Robert Kurtz | CEO | 306.5 | 79 |
| Gerhard Watzinger | Director | 35.6 | 3 |
| Sameer K. Gandhi | Director | 34.0 | 7 |
| Michael Sentonas | President | 19.9 | 2 |
| Burt W. Podbere | CFO | 17.3 | 4 |
| Roxanne Schuh Austin | Director | 11.9 | 1 |
| Anurag Saha | Officer | 10.3 | 4 |
| Cary J. Davis | Director | 7.4 | 1 |
| Denis J. O'Leary | Director | 2.7 | 1 |
| Johanna Flower | Director | 2.3 | 1 |

Notable:
- CEO Kurtz 賣出約 $306.5M，占總額約 68%。近幾個月多為每次約 2 萬股，間隔約 2 個交易日，節奏規律，是否屬於 10b5-1 計畫無法從資料判定。WebSearch 找到一則 7 月的報導提到 10b5-1 計畫，但未經 SEC Form 4 核實。
- 11/2 CFO Podbere 賣出 7,710 股 (約 $1.9M)，11/2 董事 Gandhi 賣出 14,000 股 (約 $3.4M)。
- 11/3 Kurtz 賣出 45,395 股 (約 $11.2M)，為近期單筆最大金額。
- 資料品質警示：2026-06-30 至 07-06 部分列的成交價為 $3,052 至 $3,091 或 $775，與前後數日的 $190 至 $200 明顯不符，疑似資料錯誤。這幾列合計約 $24.7M（Kurtz 6/30 約 $7.2M、7/1 約 $7.7M、7/6 約 $9.8M），若剔除，淨賣出約降至 $423M 級別。本報告未調整，保留原值。
- 抽樣核對：11/18 Kurtz 2 萬股，成交價區間 $215 至 $240，平均約 $227，金額 $4.51M，與工具回傳的 $4.51M 相符。

## Ownership shifts

- 內部人持股 1.35%，機構持股 77.87%（float 計算 78.94%），機構數 3,516 家。
- 趨勢：DATA_UNAVAILABLE。工具只提供單一時點快照，無法判斷近期機構增減。

## Net sentiment score

- 分析師：偏多（信心：高）。78% 買進、0 賣出，近月小幅改善。
- 內部人：偏空（信心：中）。6 個月淨賣 $447.9M、零買進，但 CEO 的規律賣出可能是預先安排的計畫，解讀價值受限。
- 散戶：DATA_UNAVAILABLE（信心：無）。僅有一則日期不明的 StockTwits 偏多描述，不計分。
- 綜合：中性偏多（信心：中低）。分析師面偏多，內部人面偏空，散戶面無法評估。

Divergence flag：無法判定 (retail 部分缺資料)。內部人淨賣與分析師偏多方向相反，這是現有資料中最明確的分歧訊號，但無法與散戶比對，因此無法判斷是否為「散戶與分析師反向」的典型情境。

Sources (WebSearch, 未經直接核實)：
- 分析師與股價敘述：https://www.nasdaq.com/articles/crowdstrike-ready-rally-after-its-recent-pullback
- StockTwits 前瞻文章：https://stocktwits.com/news-articles/markets/equity/crowd-strike-s-ai-security-rally-faces-its-next-test-at-fal-con-2026-what-investors-should-watch/cZYyZ8xRJrv
- 內部人交易彙整：https://kalkinemedia.com/us/news/announcements/crowdstrike-ceo-george-kurtz-executes-multiple-share-sales-under-10b5-1-plan-in-july-2026
