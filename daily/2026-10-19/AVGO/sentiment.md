# Sentiment — AVGO as of 2026-10-19

資料截止: 2026-10-19 (台北時間)。2026-10-19 之後的資料視為未知。

## Analyst consensus
目前 (rec_summary 0m): 7 Strong Buy / 40 Buy / 3 Hold / 0 Sell / 0 Strong Sell, 共 50 家。
**BUY 佔比 94%** (47/50), HOLD 6%, SELL 0%。

- 4 個月趨勢: -3m 時 BUY 44/48 (92%), -2m 45/49 (92%), -1m 與 0m 皆 47/50 (94%)。HOLD 由 4 家降到 3 家, 共識略為收斂, 未見評等下修潮。
- 近期評等動態 (第三方彙整, 需以券商原文核對):
  - 2026-06: Jefferies 目標 $550、CLSA $600、JPMorgan $580、UBS $485, 均維持 Buy。
  - 2026-07-07: Erste Group 由 Buy 降為 Hold。
  - 2026-08 下旬 (財報前): Goldman (James Schneider) 維持 Buy, 目標 $525; TD Cowen (Joshua Buchalter) 維持 Buy, 目標 $500。
  - 2026-09-04: Citigroup 目標升至 $515 (Buy); DA Davidson 目標降至 $350 (Neutral)。
- 目標價: yfinance info 快取的 targetMeanPrice $527.59, 高 $660, 低 $215.88 (共 47 家)。
- 資料不一致: info 的 recommendationMean 1.26 (strong_buy) 與 numberOfAnalystOpinions 47, 而 rec_summary 合計為 50 家。另一個第三方來源 (Benzinga) 顯示 30 家中 26 Buy / 4 Hold。各來源的家數與目標價不同, 本報告以 rec_summary 的 94% BUY 為主。
- 快取中的價格 (currentPrice $328.75) 與 2026 年 6-7 月內部人交易價 ($373-401) 及 9 月初約 $358 有明顯落差。prices/yf/AVGO.json 的快照日期無法從內容確認, 目標價與價格相對位置請以當日行情重新確認。

## Retail social
- **Reddit (r/wallstreetbets, r/stocks)**: 本次未取得可用結果。WebSearch 找不到 2026-10 的 AVGO 相關 Reddit 討論串, 僅有一般性文章, 未能判斷散戶傾向。依規定 Reddit 主機被封鎖, 未以 WebFetch 嘗試。此來源 **缺漏**。
- **StockTwits / X**:
  - StockTwits 第三方彙整 (AltIndex) 顯示情緒分數 80/100, 標示為偏多。平均每日提及約 4,639 則, 較三個月前下降 27%; 2026-08 月提及 848 則。此為第三方估算, 未直接取得 API 資料。
  - X: 一篇 AI 生成的 Nasdaq 彙整文章描述 X 上討論熱絡, 集中在 AI 題材與分析師評等上調; 同時有少數聲音質疑估值倍數。該文未標示貼文日期, 不一定反映 2026-10。
- **聲量 (qualitative)**: 相對於 3 個月前, 提及量下降約四分之一, 屬於降溫而非升溫。以絕對水準看仍屬高關注的大型股。
- **Themes (主題)**:
  - 多方: AI 基礎建設與客製化 AI 晶片需求; 營收高成長 (第三方報 Q3 FY26 營收 $29.6B, 年增 86%, Q4 指引 $34.8B, 來源為 StocksToTrade 2026-10-09 條目, 未經 SEC 文件核對); 機構淨買入, 第三方另提及 ARK 為淨買方。
  - 空方 / 保留: 估值倍數偏高 (TradingView 摘要約 45x trailing earnings); 內部人持續減持; AI 資本支出的回報疑慮。
- Quote 樣本: 本次無可直接引用的原始貼文, 僅有第三方摘要的改寫, 故不附引文。

## Insider activity
6 個月窗口 (2026-04-19 至 2026-10-19):
- 公開市場賣出 (gross): 約 $283.7M, 其中 Samueli (Director, 間接持股) 2026-06-24 約 $250.0M, 其餘約 $33.7M。
- 公開市場買入: 1 筆, Harry You (Director) 2026-06-11 買 1,000 股, 約 $0.37M (@ $373.57)。
- 淨額: 約 **-$283.3M** (含 Samueli); 排除 Samueli 後約 **-$33.3M**。淨流向為賣出。

主要人員:
- **Henry Samueli (Director, 間接)**: 2026-06-24 贈與 336,893 股後於同日賣出 654,241 股 (約 $250M, $377.61-388.17)。其 2025 年以來多次「贈與後賣出」的模式, 較像資產配置或家族信託操作, 不宜直接解讀為對公司前景的看法。需以 Form 4 確認間接持有與計畫性質。
- **Mark Brazeal (Officer)**: 2026-06-17 至 07-10 密集賣出 4 筆, 合計約 $32.4M (價格 $377-401)。為窗口內最大的管理層賣方。
- **Gayla Delly (Director)**: 2026-07-08 賣出約 $0.73M; **Justine Page (Director)**: 2026-06-29 賣出約 $0.60M, 屬小額、定期性質。
- **Hock Tan (CEO)**: 窗口內無公開市場賣出。最近一次公開市場賣出為 2026-01-06; 2026-04-08 有 22,000 股贈與。
- **Amie O'Toole (CFO)**: 2026-06-15 獲得 50,000 股授予, 無賣出。前任 CFO Kirsten Spears 最後一筆賣出為 2025-12-31。
- **Harry You (Director)**: 窗口內唯一公開市場買入, 且過去幾次買入 (2025-09、2025-12、2026-06) 皆為小額。

解讀: 內部人淨賣出, 且 CEO 本窗口內未賣出。買方僅為一位董事的小額買入, 信號較弱。

## Ownership shifts
- 機構持股 79.7% (float 81.3%), 機構家數 6,264; 內部人持股 1.9%。
- 前十大機構 (2026-06-30 申報) 方向:
  - 增持 7 家: FMR +16.3%、State Street +2.9%、Capital World +4.9%、JPMorgan +3.5%、BlackRock +3.2%、Geode +1.9%、Vanguard Capital Management +0.4%。
  - 減持 3 家: Vanguard Portfolio Management -1.1%、Capital Research Global -2.5%、T. Rowe -1.9%。
- 整體: 機構淨增持, 集中度微升 (前十大合計約 36%)。FMR 的增持幅度最大, 為主動型基金加碼的訊號。

## Net sentiment score
**Composite: 偏多 (bullish), 信心中等 (medium-low)**

| 面向 | 傾向 | 權重觀察 |
|---|---|---|
| 分析師共識 | 強烈偏多 (94% BUY, 0% SELL) | 高 |
| 散戶 (StockTwits 第三方) | 偏多 (80/100), 聲量降溫 | 中低, 數據為彙整 |
| 散戶 (Reddit) | 無資料 | 缺漏 |
| 內部人 | 淨賣出 (-$283M gross, 排除信託約 -$33M) | 中, 性質未核實 (需 Form 4 與 10b5-1 計畫確認) |
| 機構 | 淨增持 (7 增 / 3 減) | 中高 |

信心中等的原因: Reddit 缺漏; 社群數據為第三方彙整且多為未標示日期; 分析師家數與目標價在不同來源間不一致; 快取價格的快照日期不明。

**Divergence flag: no (散戶與分析師同向偏多)**。但 **內部人 vs 分析師方向相反** (內部人淨賣, 分析師高度 Buy), 此點值得留意。內部人賣出集中在 2026-06 至 07 (價格 $377-401), 且 CEO 本窗口未賣出, 故解讀上仍以機構與分析師為主。

此報告為情緒描述, 不構成交易建議。

SENTIMENT REPORT COMPLETE
