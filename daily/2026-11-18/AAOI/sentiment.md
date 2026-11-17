# Sentiment — AAOI as of 2026-11-18

資料來源說明: 分析師評等與內部人交易取自 `pipeline/tools/yf.py` (Yahoo cookie/crumb 取得失敗，回報為 ConnectionError，工具說明可能使用快取資料)。散戶情緒以 WebSearch 彙整第三方報導，Reddit / StockTwits 直接抓取依指示未使用。本報告不含歷史 daily 報告資料。

## Analyst consensus

目前分布 (yf `rec_summary`, period 0m): **4 buy** (strong buy 2 + buy 2) / **2 hold** / **0 sell**。

趨勢 (近兩個月):

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell |
|---|---|---|---|---|---|
| 0m (目前) | 2 | 2 | 2 | 0 | 0 |
| -1m | 2 | 1 | 3 | 0 | 0 |
| -2m | 2 | 1 | 3 | 0 | 0 |

- 最近動作: 兩個月內 Hold 減少 1 檔、Buy 增加 1 檔，屬於 hold 轉 buy 的小幅上調；無 sell 評等。
- 個別升降評等明細: DATA_UNAVAILABLE (yf `recommendations` 回傳內容與 `rec_summary` 相同，只有三期彙總，沒有逐筆 upgrade / downgrade 紀錄)。
- 目標價變化: DATA_UNAVAILABLE (yf 工具未回傳 price target)。
- 二手來源差異: WebSearch 引用 Benzinga 的說法為 "Outperform" 共 6 位分析師、平均目標價 $105、區間 $25 至 $220；AAII 提到 11 月初有 1 檔降評、0 檔升評。此數字與 yf 的 6 檔 (4 buy / 2 hold) 在結構上可相容，但未能逐筆核對，僅供參考。
- 價格背景 (來自交易紀錄與二手報導): 財報後股價約跌至 $50 附近；內部人 2026-11-10 的賣出價為 $48.83，2026-06 的賣出價約 $166 至 $205。

## Retail social

- **Reddit (r/wallstreetbets, r/stocks)**: DATA_UNAVAILABLE。直接 JSON 抓取依指示未使用；WebSearch 未找到 2026 年 11 月的 AAOI 相關 WSB 或 r/stocks 討論串，只找到 MarketBeat 的過期 WSB 聲量圖表 (2024-07 快照，無可讀數字)。因此無法估計發文量或多空傾向。
- **StockTwits**: 最近可得的讀數是 2026-10-12 前後的 "extremely bullish" (該文同時提到 LITE 為 bullish)，距今約 5 週，屬於過期資料。另一則 7 月報導指情緒由 "extremely bearish" 轉為 "bearish"。目前無即時讀數。
- **SentiSense (聚合 News / X / Reddit)**: 2026-11-08 的 30 天情緒為中性，且較一個月前有所改善。
- **X**: 未取得獨立可引用的 X 貼文，DATA_UNAVAILABLE。
- **聲量 (定性)**: 無法與歷史基準比較，因為 Reddit 與即時 StockTwits 皆無資料。二手報導指 AAOI 長期是散戶關注的 AI 光通訊標的，2026 年 10 月前後討論熱度高，但 11 月財報後股價大跌，熱度是否延續無法確認。
- **多空傾向**: 混合偏空中性。Oct 的讀數偏多，但財報後股價重挫，且近期可用的情緒指標只有中性。
- **主要主題** (來自 WebSearch 摘要，非逐篇閱讀):
  1. AI 資料中心與 hyperscaler 需求 (多頭論點)
  2. 財報後跌幅與 AI 基礎建設資金疑慮 (空頭論點)
  3. 產能 (commodity bottleneck) 是否限制獲利品質 (空頭批評，引用某知名空方)
  4. 短期空單比例上升 (Benzinga 報 16.9% 且上升，日期未明)
- 引述樣本 (≤15 字，來自 WebSearch 摘要而非原始貼文): 「extremely dangerous at current levels」 (StockTwits 用戶，日期未明)。

## Insider activity

Net 6mo (2026-05-18 至 2026-11-18，以 yf `insider` 交易欄位 Value 加總，單位 USD):
- **Sell**: 27 筆，合計 **$94.2M** (94,168,878 USD)
- **Buy (open market)**: 0 筆，**$0**
- 股票授予 (Stock Award) 6 筆與贈與 (Gift) 2 筆未計入金額

依職位 (6 個月賣出金額，USD):
| 職位 | 賣出金額 (USD) | 占比 |
|---|---|---|
| Officer (其他高階) | $47.9M | 51% |
| CEO | $19.9M | 21% |
| Director | $12.4M | 13% |
| CFO | $14.0M | 15% |

注意: 合計 $94.2M 與上表四項加總 (47.9 + 19.9 + 12.4 + 14.0 = 94.2) 一致。

Notable:
- **CEO LIN CHIH-HSIANG THOMPSON**: 2026-05-19 賣出 58,000 股 @ $173.26 (約 $10.0M)；2026-06-12 賣出 59,000 股 @ $166.53 (約 $9.8M)。最近一次 CEO 大額賣出為 2026-06-12。
- **CFO MURRY STEFAN J**: 6 個月內多筆賣出，包含 2026-06-12 賣出 33,000 股 (約 $5.5M)；此後約每月固定賣出 4,000 股 (2026-07-10、08-10、09-10、10-12、11-10)，最近價格 $48.83。固定股數與月度節奏可能屬於 10b5-1 計畫，但未經 filing 驗證。
- **Officer CHANG HUNG-LUN FRED**: 2026-09-08 賣出 32,172 股 @ $110.21 (約 $3.5M)。
- **Director DELANEY CYNTHIA**: 2026-05-26 賣出 56,575 股 @ $189.23 (約 $10.7M)。
- **Director CHEN MIN-CHU MIKE**: 2026-06-02 賣出 8,247 股 @ $201.00。
- 2026-06-12 有 5 位高階 (CEO、CFO 與 3 位 Officer) 同日以 $166.53 賣出，屬於群體性同日賣出。
- 最近 2025-08 有少量公開市場買入 (CEO 與數位董事，約 $0.1M 至 $0.4M 不等)，6 個月視窗外。

## Ownership shifts

- insiders 持股占比 9.11%；institutions 持股占比 61.94%；institutions float 占比 68.15%；機構家數 634 (yf `major_holders`)。
- 趨勢 (季度對比): DATA_UNAVAILABLE。yf 只回傳單一快照，無法判斷機構持股是增加或減少。

## Net sentiment score

- **分析師**: 偏多 (信心: 中)。4 buy / 2 hold / 0 sell，近兩月 hold 轉 buy，無賣出評等。
- **內部人**: 偏空 (信心: 高)。6 個月 $94.2M 賣出、零公開市場買入，包含 CEO 與多位高階同日賣出。固定股數的月度賣出為慢性出貨特徵，但仍是單向。
- **散戶**: 中性 (信心: 低)。最近的 StockTwits 讀數 (Oct) 偏多但已過期；SentiSense 11 月中性；Reddit 無資料。
- **綜合**: **中性 (信心: 低)**，偏向分析師多頭與內部人空頭拉扯，散戶方向資料不足無法確認。

Divergence flag: **是** — 分析師偏多與內部人單向賣出方向相反；內部人賣出時股價約在 $100 至 $200，目前股價約 $50，賣出價與現價差距大，此訊號的解讀需要保留。散戶方向因資料過期，無法判定是否與分析師相反。

## Data gaps

- Reddit WSB / r/stocks 即時討論: DATA_UNAVAILABLE
- StockTwits 即時讀數: DATA_UNAVAILABLE (僅 2026-10 過期資料)
- X 貼文: DATA_UNAVAILABLE
- 逐筆升降評等 與 目標價: DATA_UNAVAILABLE
- 機構持股趨勢 (多期比較): DATA_UNAVAILABLE
- yf Yahoo cookie/crumb 取得失敗；若工具使用快取，數字可能非 11-18 當日最新值

SENTIMENT REPORT COMPLETE
