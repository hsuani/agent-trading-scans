# Sentiment — QUBT as of 2026-11-03

注意事項：
- 目前環境日期為 2026-11-02，報告以 2026-11-03 為標示日期。最新可取得的資料約停在 2026-09-22，距今約 6 週，多數分析師與價格資料已過時，需以即時來源覆核。
- Reddit 與 StockTwits 未直接抓取。Reddit 以 WebSearch 查詢未得到任何 reddit.com 結果，StockTwits 無可用頁面。

## Analyst consensus

6 位分析師：4 buy / 2 hold / 0 sell（strongBuy 0、strongSell 0）。`rec_summary` 顯示 0m、-1m、-2m 三期完全相同，近三個月評級分布沒有變動。`recommendations` 工具只回傳彙總計數，沒有逐筆升降評等事件。

近期動作（來自 WebSearch，多為第三方聚合頁，需以券商原文或 MarketBeat 覆核）：
- Wedbush：2026-08-03 首次覆蓋，Hold，目標價 $12（Matt Bryson）。
- Ascendiant Capital：2026-08-26 維持 Buy。
- Cantor Fitzgerald：2026-08-11 維持 Neutral。
- Rosenblatt：2026-07-29 重申 Buy，目標價 $22。
- Lake Street：2026-07-06 維持 Buy，目標價 $16。
- Northland：2026-04 首次覆蓋，Outperform。

目標價：各來源共識區間約 $16.58–$19.50。Fintel 顯示 2026-08-04 上調至 $21.76，2026-08-28 下調 12.5% 至 $19.04。TIKR 指出目標價在股價大跌期間大致持平。

資料衝突：Seeking Alpha 2026-08-21 快照標示 "Not Covered"，與上述覆蓋情況不一致。

## Retail social

- Reddit：WebSearch 未找到 r/wallstreetbets 或 r/stocks 的 QUBT 討論串，無法評估 tilt 或討論量。
- StockTwits / X：找不到 StockTwits 頁面，無法取得 bullish/bearish 比例。Quiver 的社群摘要（來源日期約 2026-05）描述語氣為投機性，QUBT 常出現在漲幅榜與推廣群組，部分貼文認為股價低於合理價值。
- 討論量：無法量化，僅能定性判斷為中等偏高（依據是 QUBT 常見於量子概念股話題與漲幅榜）。這點屬推論，信心低。
- 主要議題：
  1. 量子概念股題材與價格波動，有 FOMO 式追價紀錄。
  2. 營收與基本面質疑，Seeking Alpha 近期文章多為 "Strong Sell" 或 "Foundry Built On Hype" 等標題。
  3. Iceberg Research 長期做空（自 2022-10 起），近期另有新空方報告，質疑晶圓代工轉型與部分訂單公告。
  4. 估值爭論，一派認為低於合理價值，另一派認為缺乏基本面支撐。
  5. 下一次財報約 2026-11-13（預估，未確認），為近期催化劑。

- 價格脈絡：2026-05-21 單日大漲約 15.7% 至 $11.06；2026-08-01 約 $8.09；2026-09-22 收於約 $9.39（Benzinga）。TIKR 指出股價自高點回落約 37%。部分來源價格互相衝突，需以即時報價為準。

## Insider activity

以 2026-05-02 至 2026-11-02 計算近 6 個月：
- 公開市場買入：$0。
- 公開市場賣出：$0。
- 僅有股權授予與衍生性證券轉換，性質屬薪酬而非自主買賣。

主要紀錄：
- CEO Huang Yuping：2026-08-20 股票授予 584,897 股，單價 $8.95，約 $5.23M。另有兩筆 584,897 股、單價 $8.14、約 $4.76M 的衍生性證券轉換，可能是同一交易重複申報，需核對 SEC Form 4。
- CEO Huang Yuping：2026-05-28 授予 58,558 股，單價 $0。
- Officer Dianat Pouya、COO Begliarbekov Milan：2026-05-28 各授予 24,774 股，單價 $0。

6 個月窗口外的背景：2026-03 GC Roberts 出售 78,262 股（約 $0.61M）；2025-09 CEO Huang 出售 1,000,000 股（約 $14.4M）；2025-05 CEO Huang 出售 500,000 股（約 $5.85M）。Quiver 另提及 6 個月內 2 筆公開市場賣出，但該來源日期約為 2026-05，與本窗口不一致，不採用。

## Ownership

- 內部人持股：12.16%。
- 機構持股：47.93%（機構流通股占比 54.57%），機構數 414 家。
- 僅有單一快照，無法判斷趨勢。Equibles 標示聰明錢中性、機構流向為吸籌，但此為低品質聚合來源，僅供參考。

## Net sentiment score

- 分析師面：偏多但不強。4 buy / 2 hold / 0 sell 近三個月持平，但 2026-08 目標價有下修。信心：中。
- 散戶面：無法可靠評估。可見來源（Quiver 摘要、Equibles 評級、SA 文章）偏投機或偏空，但時效皆在 2026-05 至 2026-09。信心：低。
- 內部人面：中性。6 個月內無公開市場買賣，只有薪酬性授予。
- 綜合：中性（neutral），信心低。主要受資料過時與散戶面資料缺口限制。

Divergence flag：可能（待確認）。分析師評級偏多，而可見的媒體與評級網站（Equibles "Sell"、SA "Strong Sell"、Iceberg 空方）偏空。但這些來源分屬不同主體，且散戶社群資料缺失，不能視為確認的分歧。

## 資料來源

- pipeline/tools/yf：QUBT recommendations、rec_summary、insider、major_holders。
- WebSearch（聚合頁，多數時效不足，列出僅供追溯）：Equibles、StockScan、Quiver Quantitative 摘要、Fintel、Investing.com、TIKR、Benzinga、Seeking Alpha 相關頁面、Iceberg Research 新聞報導。

SENTIMENT REPORT COMPLETE
