# Sentiment — ASML as of 2026-11-23

資料來源與時效：分析師評級、內部人、大股東資料取自 `prices/yf/ASML.json`（cache 刷新時間 2026-11-22 14:30 UTC，live Yahoo 因連線失敗未能取得）。Reddit 與 StockTwits 直連皆失敗（Reddit 拒絕、StockTwits DNS 無法解析），零售情緒改以 WebSearch 的二手報導為主，樣本量與精確度有限。

## Analyst consensus

rec_summary 目前（0m）評級分布：**41 家**，其中 Strong Buy 7 / Buy 31 / Hold 2 / Sell 1 / Strong Sell 0。買進側（Strong Buy + Buy）佔 38 家，約 93%。

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 合計 |
|---|---|---|---|---|---|---|
| 0m（當前） | 7 | 31 | 2 | 1 | 0 | 41 |
| -1m | 7 | 31 | 2 | 1 | 0 | 41 |
| -2m | 7 | 31 | 3 | 1 | 0 | 42 |
| -3m | 6 | 32 | 4 | 1 | 0 | 43 |

近三個月的變化很小：Hold 由 4 家降到 2 家，Buy 類合計維持在 38 家上下，覆蓋家數由 43 降到 41。近期沒有看到評級下調，但 `recommendations` 工具回傳的是同一份評級計數快照，不是逐筆 upgrade / downgrade 歷史，因此無法列出具體是哪幾家券商調整。WebSearch 另有一則 MarketBeat 報導提到 2026-10-17 有 Wall Street Zen 升評為 Buy（來源為新聞標題，未逐篇核實）。

目標價（cache `info`）：
- 平均目標價 **USD 2,108**、中位數 USD 2,254、最高 USD 2,789、最低 USD 849。
- `recommendationMean` 1.37（1 為最強買進），`recommendationKey` 為 strong_buy。
- 注意：`info` 的 `numberOfAnalystOpinions` 為 17，與 rec_summary 的 41 不一致。推測是有目標價的家數較少，兩者口徑不同，報告以 rec_summary 的 41 家為評級分布、以 17 家為目標價樣本。
- WebSearch 中 MarketBeat 的共識目標價為 USD 2,079，Benzinga 則為 USD 1,705，兩個來源差距大，且 Benzinga 的目標價時間點不明，未採用。

現價口徑衝突：cache `info.currentPrice` 為 USD 1,266.22（約 2026-11-22 刷新），但 WebSearch 中 Benzinga 頁面顯示 USD 1,527.33（標示 2026-11-12 更新）。兩者相差約 17%，無法判定哪個是最新價，這會影響「距目標價空間」的解讀，需由價格模組核對。

## Retail social

- **Reddit**：r/wallstreetbets 與 r/stocks 的 search.json 皆被拒（無法取得）。WebSearch 找到一則 AOL 報導，稱 ASML 與 IBM 在 Reddit 上獲得散戶追捧、情緒偏多，但報導日期不明，無法確認是否為近期資料。**Reddit 樣本缺失，此項無法評估提及量。**
- **StockTwits**：直連失敗（api.stocktwits.com 無法解析，需在 session 網路設定中允許該網域後才能重試）。依 WebSearch 找到的 StockTwits 新聞彙整，2026 年多數時間零售情緒偏多，常被描述為 "extremely bullish"。近期也有轉為 neutral 的情況：一次中國風險引發的拋售中，情緒由 bearish 轉為 neutral，且訊息量仍屬低檔。這些是新聞彙整對平台情緒計的描述，不是原始貼文統計。
- **X / 新聞**：未取得可核實的 X 貼文樣本。
- **提及量（相對一般水準）**：無法量化。從 WebSearch 結果看，ASML 在 StockTwits 與財經新聞上的報導頻率屬於中高，但未能與 Reddit 或歷史基準做比較，只能定性為「有關注、但缺乏量化數據」。

**主要話題（依 WebSearch 結果歸納）：**
1. AI 晶片需求與設備訂單能見度，多數零售人士視 ASML 為 "gatekeeper of tech"（來自 StockTwits 新聞標題的引語，非原始貼文）。
2. EUV 獨佔地位與長期護城河。
3. 中國出口管制與營收風險，是拋售與情緒轉弱的主要觸發點。
4. 估值偏高的擔憂，新聞中提到 "expensive" 的分析觀點，與零售偏多並存。

## Insider activity

Net 6mo：**無法確認**。`insider` 工具在 live 與 cache 皆回傳空陣列 `[]`，沒有任何逐筆交易。這不等於內部人「零交易」，因為 ASML 為在荷蘭上市、以 Form 20-F 申報的外國私人發行人（foreign private issuer），Yahoo 內部人交易資料對此類公司常常缺漏。報告不列入任何買賣淨額，也不推論 CEO / CFO 的動向。
- 大股東顯示內部人持股比例約 0.009%（`insidersPercentHeld` = 9e-05），內部人持股本身占比極低。

## Ownership shifts

major_holders（cache）：
- 機構持股比例約 **19.9%**（`institutionsPercentHeld` 0.19927），機構家數 2,987。
- 內部人持股比例約 0.009%。

inst_holders 前幾大（資料日期 2026-09-30，13F 申報時點）：

| 機構 | 持股（股） | 市值（USD B） | 季度變動 |
|---|---|---|---|
| FMR, LLC | 5,984,181 | 7.58 | +9.2% |
| Fisher Asset Management, LLC | 4,839,202 | 6.13 | +2.1% |
| Capital World Investors | 3,426,093 | 4.34 | -8.1% |
| Invesco Ltd. | 2,791,444 | 3.53 | -11.1% |
| State Farm Mutual Automobile Insurance Co | 2,744,979 | 3.48 | -0.5% |
| Capital International Investors | 2,377,627 | 3.01 | -2.5% |
| Van Eck Associates Corporation | 2,289,190 | 2.90 | -6.9% |
| JPMorgan Chase & Co | 2,103,597 | 2.66 | -12.2% |
| Price (T. Rowe) Associates Inc | 2,032,256 | 2.57 | +5.1% |
| Morgan Stanley | 1,799,207 | 2.28 | +0.6% |

前十大中加碼（FMR、Fisher、T. Rowe）與減碼（Invesco、JPMorgan、Capital World、Van Eck）的家數大致相當，整體沒有單邊集中或撤離的訊號。機構持股比例僅約 20%，而 ASML 同時在 Euronext Amsterdam 與 Nasdaq 掛牌，部分持股可能未被 13F 口徑涵蓋，不宜直接解讀為低配。

## Net sentiment score

**Composite：偏多（bullish），信心中等偏低。**

- 分析師面：強烈偏多。41 家中 93% 為買進評級，mean rating 1.37，近三個月 Hold 家數下降，沒有下調跡象。
- 零售面：偏多但資料薄弱。StockTwits 新聞彙整顯示多數時間情緒偏多，但 Reddit 與 X 沒有可核實樣本，提及量無法量化。
- 內部人面：無資料，不計分。
- 機構面：中性。前十大持股有加有減，無方向性結論。
- 信心降低的原因：現價口徑衝突（USD 1,266 vs 1,527）、目標價來源差異大、Reddit / StockTwits 直連失敗。

**Divergence flag：否。** 零售與分析師方向一致，都偏多。唯一的分歧在於估值：新聞中有分析師認為 "expensive"，但這屬於個別觀點，不足以構成零售與分析師的反向訊號。

**資料缺口，供後續追蹤：**
1. 確認現價（cache USD 1,266 vs Benzinga USD 1,527），以決定目標價空間。
2. 取得 Reddit 與 StockTwits 原始樣本（需網域允許或另一來源）。
3. Yahoo 內部人交易資料對 ASML 缺漏，若需要內部人訊號，應改用荷蘭 AFM 或公司公告來源。

SENTIMENT REPORT COMPLETE
