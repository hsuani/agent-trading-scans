# Sentiment — ASTS (AST SpaceMobile) as of 2026-10-26

> 資料時效註記: 系統日期為 2026-10-25，本報告依指定 as-of 2026-10-26 撰寫。yfinance 工具回傳的最新資料未附時間戳，視為截至拉取當下的最新值。

## Analyst consensus

目前 13 位分析師: 1 Strong Buy / 4 Buy / 6 Hold / 1 Sell / 1 Strong Sell，即 Buy 側 5 家、Hold 側 6 家、Sell 側 2 家。

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 合計 |
|---|---|---|---|---|---|---|
| 當前 (0m) | 1 | 4 | 6 | 1 | 1 | 13 |
| -1m | 1 | 4 | 7 | 1 | 1 | 14 |
| -2m | 1 | 3 | 7 | 1 | 1 | 13 |
| -3m | 1 | 3 | 7 | 1 | 1 | 13 |

近三個月趨勢: Buy 側由 4 家增至 5 家，Hold 由 7 家降至 6 家，Sell 側維持 2 家。工具只提供月度彙總計數，無法逐家追溯評等變動。

近期個別動作 (來自 WebSearch 彙整的新聞來源，未經交叉驗證):
- Deutsche Bank: 2026-10-12 由 Hold 升至 Buy，目標價 $93 USD，主張近期跌幅為較佳進場點。
- Clear Street: 維持 Buy，目標價 $115 USD，認為股價下跌源於第三方發射載具受阻 (Bluebird 7 於 5 月在 New Glenn 發射失敗)，而非需求下滑。
- Scotiabank: 由 Sell 升至 Hold，目標價 $50.80 USD，認為機會與風險大多已反映在股價中。Scotiabank 動作之確切日期 DATA_UNAVAILABLE。
- 目標價共識: DATA_UNAVAILABLE (WebSearch 來源提及的 Benzinga 共識 (平均目標價約 $73 USD) 為 2026-08 快照，早於 10 月大幅下跌，視為過期資料，不採用)。

股價背景 (來自同一批新聞來源，日期略有模糊): 股價曾於 5 月觸及歷史高點 $133.86 USD，10 月初附近約 $58 USD，較高點回落逾 60%。

## Retail social

- Reddit (r/wallstreetbets、r/stocks): DATA_UNAVAILABLE。WebFetch 回傳無法存取 reddit.com；直接以 curl 測試亦遭 proxy 回應 403 (CONNECT tunnel failed)。無法取得討論串樣本、提及數或多空傾向。
- StockTwits: DATA_UNAVAILABLE。WebFetch 回傳 DNS 解析失敗 (ENOTFOUND)；curl 亦遭 proxy 回應 403。無法取得多空標籤統計。
- X (Twitter): DATA_UNAVAILABLE。本次 WebSearch 未找到 2026-10 的社群情緒調查或社群貼文彙整，搜尋結果以 sell-side 評論與新聞為主。
- 討論量 (buzz volume) 相對一般水準: DATA_UNAVAILABLE。
- 散戶多空傾向: DATA_UNAVAILABLE。

- Themes (僅能從新聞與 sell-side 文字歸納，非散戶原文):
  - 發射端瓶頸是否緩解 (Bluebird 7 失敗後的 launch bottleneck)。
  - 股價自高點大幅回落後，估值是否已充分反映風險。
  - 空方持股比例高 (Benzinga 8 月快照曾提及 short interest 約 20% of float，屬過期資料)。

## Insider activity

Window: 2026-04-26 至 2026-10-26 (6 個月)。統計口徑: 僅計 open-market "Sale" 與 "Purchase"，排除 Stock Award (Grant) 與衍生性證券 Conversion。

- 6mo sells: 6 筆，合計約 $12.81M USD
- 6mo buys: 1 筆，合計約 $0.62M USD
- 淨額: 約 -$12.19M USD (淨賣出)

主要交易明細 (6 個月內):

| 日期 | 人員 | 職位 | 方向 | 股數 | 金額 (M USD) | 成交價 (USD) |
|---|---|---|---|---|---|---|
| 2026-09-16 | GUPTA SHANTI B. | COO | Sale | 12,000 | 0.71 | 58.89 |
| 2026-09-16 | YAO HUIWEN | CTO | Sale | 40,000 | 2.36 | 58.93 |
| 2026-08-31 | CISNEROS ADRIANA | Director | Purchase | 10,822 | 0.62 | 57.00–58.87 |
| 2026-06-11 | JOHNSON ANDREW MARTIN | CFO | Sale | 45,809 | 4.30 | 93.81 |
| 2026-06-05 | YAO HUIWEN | CTO | Sale | 40,000 | 3.85 | 96.37 |
| 2026-05-20 | JOHNSON ANDREW MARTIN | CFO | Sale | 5,000 | 0.45 | 90.25 |
| 2026-05-13 | TORRES JULIO A | Director | Sale | 15,000 | 1.15 | 76.34 |

注意事項:
- 2026-09 的 COO/CTO 賣出價約 $58.9 USD，與 10 月初股價接近；6 月的 CFO/CTO 賣出價為 $90–96 USD，屬於股價高點附近。
- 9 月的 CTO 出售與 8 月的 CTO 選擇權行使 (每股 $0.06 USD 行使價 Conversion) 有關聯，行使後隨即賣出。
- 工具未提供 10b5-1 計畫標記，無法判斷各筆賣出是否屬預先安排之計畫: DATA_UNAVAILABLE。
- 2026-04-15 另有 10% 以上持股人 MIKITANI HIROSHI 賣出約 3.04M 股、合計約 $270.9M USD (成交價 $86.22–91.42 USD)，但發生於 6 個月窗口之外，僅作背景參考，未計入上述淨額。
- 2025-12 有 American Tower Corporation (10% 持股人) 賣出約 2.29M 股、約 $159.6M USD，同樣在窗口之外，僅列為背景。
- 6 個月內 Director 層級有少量公開市場買進 (CISNEROS, 8/31)，為唯一買進紀錄。
- 2025-12 期間 Director LARSON KEITH R 曾三次小額買進 (合計約 $0.15M USD)，超出 6 個月窗口。

淨賣出規模以及主要高階主管 (CFO、CTO、COO) 的賣出為內部情緒面的負向訊號，但 Stock Award 大量發放 (CEO/CFO/President 於 8/17 與 3/24 等日) 屬於薪酬性質，不應解讀為買進。

## Ownership shifts

- insidersPercentHeld: 8.0%
- institutionsPercentHeld: 54.9% (of shares outstanding)
- institutionsFloatPercentHeld: 59.6% (of float)
- institutionsCount: 974
- 趨勢 (季度機構持股變動、前十大持股人名單): DATA_UNAVAILABLE。工具僅回傳單一時點快照，無法比較機構增減持。
- 10% 持股人動向: 由 insider 紀錄可見 MIKITANI HIROSHI (2026-04 賣出) 與 American Tower (2025-12 賣出) 兩筆大型減持，但其最新持股比例 DATA_UNAVAILABLE。

## Net sentiment score

- 分析師面 (analyst): 中性偏多。Buy 側 5 家、Sell 側 2 家，但 Hold 占多數 (6 家)，且近三個月 Buy 側小幅增加。
- 內部人面 (insider): 偏空。6 個月淨賣出約 $12.19M USD，主要為高階主管 (CTO、CFO、COO) 賣出，僅 1 筆 Director 小額買進。
- 散戶面 (retail): DATA_UNAVAILABLE。
- 綜合 (composite): **中性 (neutral)**，信心度 **低**。理由: 分析師面與內部人面方向不一致，而散戶面完全缺資料，無法形成可靠的整體判斷。

Divergence flag: **無法判定 (DATA_UNAVAILABLE)** — 散戶多空傾向無法取得，無法判斷散戶與分析師是否背離。但分析師面 (中性偏多) 與內部人面 (偏空) 之間存在方向差異，值得後續追蹤。

## 資料缺口與來源狀態

| 來源 | 狀態 | 說明 |
|---|---|---|
| yf recommendations / rec_summary | 成功 | 月度彙總計數；無逐家評等歷史 |
| yf insider | 成功 | 完整 78 筆紀錄 (2025-02 起) |
| yf major_holders | 成功 | 單一時點快照 |
| Reddit (r/wallstreetbets, r/stocks) | 失敗 | proxy 403 |
| StockTwits | 失敗 | DNS 解析失敗；proxy 403 |
| WebSearch (X/新聞) | 部分成功 | 以 sell-side 與新聞為主，無社群情緒量化資料 |
| 目標價共識 | DATA_UNAVAILABLE | 僅有過期 (8 月) 來源 |
| 機構持股趨勢 | DATA_UNAVAILABLE | 無歷史快照 |

SENTIMENT REPORT COMPLETE
