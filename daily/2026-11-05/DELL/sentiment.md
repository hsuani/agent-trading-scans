# Sentiment — DELL as of 2026-11-05

資料限制: 今日為 2026-11-04，分析日為 2026-11-05。Reddit 抓取被拒 (無法連線)，StockTwits 因 DNS 無法解析被擋 (需在 session 網路設定允許 api.stocktwits.com)。散戶面向幾乎無法直接量測，僅有一則 2026-08 的選擇權資金流數據。內部人資料最新一筆為 2026-10-22。

## Analyst consensus

rec_summary 當期 (0m) 分布 (USD 不適用，單位為家數):

| 評等 | 當期 (0m) | -1m | -2m | -3m |
|---|---|---|---|---|
| Strong Buy | 6 | 5 | 6 | 5 |
| Buy | 14 | 14 | 14 | 14 |
| Hold | 9 | 10 | 9 | 9 |
| Sell | 0 | 0 | 0 | 0 |
| Strong Sell | 0 | 0 | 0 | 0 |

當期合計 29 家: 20 買進 (6 Strong Buy + 14 Buy) / 9 持有 / 0 賣出。過去四個月評等結構幾乎不變，沒有賣出評等。

Recent moves: yf `recommendations` 回傳的仍是彙總計數，沒有逐筆升降評等紀錄，無法驗證個別事件的日期。以下為搜尋摘要中的零散資訊，未經官方評等歷史核對，且部分日期不明:
- Morgan Stanley 由 Underweight 升至 Equal Weight，目標價由 $170 升至 $448 (後更新為 $477，註記 2026-06-23)。
- Susquehanna 於 2026-05-29 升至 Positive，目標價 $700 (摘要稱為 Street-high)。
- GF Securities 於 2026-06-25 降至 Hold。
- UBS 降至 Neutral，目標價由 $167 調至 $243 (年份未標示，推測為 2026)。
- Citi 維持 Buy，目標價 $515 (2026-07-24)；Evercore ISI 維持 Buy，目標價 $500 (2026-07-15)。
- 彙總平均目標價約 $489 (摘要顯示距離當時股價約 +23%)，資料時點約為 2026 年中，不是 10 月。
- 2026-10 之後的評等變動未找到可靠來源，需以 StreetInsider 或 MarketBeat 評等歷史人工核對。

## Retail social

- Reddit (r/wallstreetbets、r/stocks): 抓取失敗 (無法連線 www.reddit.com)。無法取得討論量、熱門串或語氣分布。
- StockTwits: DNS 解析失敗，未取得資料。
- X / 新聞討論: 一則 WebSearch 結果提到 2026-08 的選擇權資金流看多 (call 美元成交量約 68%，put 約 32%)，同一摘要認為技術面可能過熱。社群輿論當時偏分歧，一方看 AI 題材的潛力，另一方警告風險。此資料已超過兩個月，不代表 11 月狀況。
- 新聞標題語氣: 「Dell Stock Has Been a Victim of AI. These Analysts Say It's a Winner」 (摘要標題，時間不明)，顯示媒體討論在 AI 伺服器題材與估值之間拉扯。
- 聲量 (相對典型水準): 無法量化，標示為未知。
- 主要主題 (由有限來源推斷): AI 伺服器需求與營收動能、估值是否過高、2025 年底的降評事件後的反彈論述。
- 散戶傾向: 無法判定 (bullish / bearish / mixed 皆無充分證據)。

## Insider activity

內部人資料取自 yf `insider` (共 150 筆，時間範圍 2026-07-06 至 2026-10-22)。6 個月窗口為 2026-05-05 至 2026-11-05，因 150 筆可能是工具上限，5 月至 7 月初的紀錄未出現在結果中，因此 6 個月淨額屬於下限估計，需補查。

Net 6mo: 公開市場買進 $0 (未見任何 Purchase 紀錄)，賣出約 $1.07B。若只計 Silver Lake 相關實體以外，主要高階主管與董事合計賣出約 $60.5M。

| 類別 | 賣出金額 (USD) | 備註 |
|---|---|---|
| Silver Lake 相關實體 (10% 大股東，部分為董事指派關係) | 約 $1.01B | Partners IV $400.2M、SL SPV-2 $368.0M、Partners V $227.8M、Tech Investors IV $8.8M、Tech Investors V $4.0M |
| 高階主管與董事 (非 Silver Lake) | 約 $60.5M | 見下方明細 |
| 獎勵 / 贈與 / 選擇權行權 | 無市場金額 | 董事年度股票獎勵、Dorman 贈與，以及 Radakovich 的選擇權行權 (價格 $31.14，屬於行權而非市場買進) |

Notable (非 Silver Lake):
- Peter Trizzino (Officer): 2026-09-11，賣出 37,735 股，約 $21.1M。
- David Alan Kennedy (CFO): 2026-09-17，賣出 23,896 股，約 $14.0M。
- Jennifer D. Saavedra (Officer): 2026-09-04，賣出 25,251 股，約 $13.1M。
- Richard Jay Rothberg (General Counsel): 2026-09-11 與 09-17 合計賣出 10,000 股，約 $5.6M。
- Lynn Vojvodich Radakovich (Director): 2026-07-22、08-24、09-22、10-22 各有一次賣出，單次約 $0.8M–$1.1M，為定期小量出售。
- Jane Tunnell (Officer): 2026-09-04，賣出 5,436 股，約 $2.8M。

Silver Lake 賣出重點: 2026-07 至 2026-10 間連續多筆賣出，成交價區間約 $405–$592 (以 transaction 價格為準)。最近一批 (2026-10-06、10-09) 價位約 $572–$589。這種持續減持的型態較像財務買方分批退出，而非對公司前景的直接判斷，但無論動機為何，它仍是明確的淨賣壓來源。

價格脈絡 (由交易價推算，未經即時報價核對): 2026-10-22 董事 Radakovich 的賣出價為 $460.00，明顯低於 10 月初 Silver Lake 的成交價 (約 $572–$589)，代表 10 月內股價曾有約二成的回落。

## Ownership shifts

- 內部人持股 (insidersPercentHeld): 7.69%
- 機構持股 (institutionsPercentHeld): 77.36%；占流通股 (float) 83.80%
- 機構家數 (institutionsCount): 2,901
- 趨勢: 工具只回傳單一時點快照，無法判定機構集中度是增加或減少。Silver Lake 的持續出售會改變內部人持股比例，但缺少流通股數無法精確換算。

## Net sentiment score

Composite: **neutral (偏空的 insider 信號與偏多的分析師共識並存)**，信心 **低-中**。

分項判斷:
- 分析師共識: 偏多，信心中 (20 買進 / 9 持有 / 0 賣出，結構穩定，但共識資料本身沒有 10 月後的更新)。
- 內部人: 偏空，信心中 (1B 以上賣出，幾乎全部來自 Silver Lake 與高階主管也出售；但主要來源是財務買方退出，可能非資訊性)。
- 散戶: 未知，信心低 (Reddit 與 StockTwits 皆無資料，唯一的 2026-08 選擇權資料偏多但已過時)。

Divergence flag: **yes (內部人與分析師方向相反)**。分析師多數維持買進，內部人與大股東在 7–10 月持續賣出，股價於 10 月回落後仍有出售紀錄。散戶與分析師之間的分歧無法驗證，因為散戶資料缺失。

資料缺口 (需於下次補充):
1. Reddit 與 StockTwits 需允許連線或改用其他來源。
2. 內部人交易 2026-05 至 2026-07-05 區間需確認是否被 150 筆上限截斷。
3. 2026-10 之後的分析師評等變動需以官方評等歷史核對。
4. 機構持股需至少兩期快照才能判定趨勢。

SENTIMENT REPORT COMPLETE
