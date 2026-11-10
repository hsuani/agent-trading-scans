# Sentiment — AAOI as of 2026-11-11

資料完整度: 分析師與內部人資料為 yf 工具實際回傳; Reddit 與 StockTwits 無法取得 (見下方); X/新聞僅有 WebSearch 摘要, 多為二手來源, 日期不一。

## Analyst consensus

目前 (0m) 共 6 位分析師: 2 strongBuy / 2 buy / 2 hold / 0 sell / 0 strongSell, 即 4 位偏多、2 位中性、0 位偏空。

| 期間 | strongBuy | buy | hold | sell | strongSell | 偏多合計 |
|---|---|---|---|---|---|---|
| 目前 (0m) | 2 | 2 | 2 | 0 | 0 | 4 |
| 前一月 (-1m) | 2 | 1 | 3 | 0 | 0 | 3 |
| 前二月 (-2m) | 2 | 1 | 3 | 0 | 0 | 3 |

Recent moves: 相較前一月, 偏多評級由 3 增至 4, 中性由 3 減至 2, 無降評記錄。`recommendations` 工具只回傳彙總分佈, 未提供逐筆升降評與目標價變動。二手來源 (WebSearch, tikr 與 AAII 摘要) 提到 Northland 升評至 Outperform 並給予 $120 目標價, 但未能在工具資料中核實日期。另一頁 AllMind 顯示平均評等 1.75、目標價區間 $13 至 $50, 與目前股價區間明顯不符, 判定為過時資料, 不採用。

## Retail social

- Reddit: 無法取得。r/wallstreetbets 與 r/stocks 的 JSON 搜尋皆回傳 "unable to fetch", 本次無貼文樣本, 無法量化提及量或多空傾向。
- StockTwits / X: StockTwits API 因網路政策無法解析 (api.stocktwits.com 不在允許網域內), 需由使用者於 session 網路設定中允許後才能重試。二手來源 (Intellectia) 引述 StockTwits 散戶情緒為 "extremely bullish", 但此為轉述, 未經原始貼文驗證。
- 新聞與 X 摘要主要主題: 11 月初股價大幅回檔 (來源指一週內跌約 17%, 且 11/4 收盤約 $59.27, 單日約跌 7%), 並歸因於 Amazon 自由現金流轉負 (tikr 摘要) 等市場情緒因素。
- Buzz volume: 無法量化, 僅能從新聞數量判斷為近期討論度偏高 (定性)。
- Themes:
  - 動能與散戶熱度 vs. 近期急跌 (多空對立敘事)
  - 資料中心資本支出放緩疑慮 (Intellectia 提及, 為下行風險主題)
  - 內部人大量減持 (見下節)
  - Northland $120 目標價的多方論述
- 代表性引述 (二手, ≤15 字): "a $120 target looks conservative" (Northland 摘要引述, 非散戶)。散戶原始貼文樣本缺失。

## Insider activity

Net 6mo (2026-05-11 至 2026-11-11, 共 40 筆, 扣除獎勵與贈與後): **$94.6M 賣出 (sells), $0 買入 (buys)**。

以 yf insider 資料逐筆加總, 單位為 USD。另一頁 MarketBeat 摘要引用的 3 個月賣出約 $86.7M, 與本報告 6 個月口徑不同, 不直接比較。

Notable:
- 大額賣出: Officer CHANG HUNG-LUN FRED 2026-06-17 以 $170.60 賣出 40,329 股 (約 $6.9M); 2026-09-08 以 $110.21 賣出 32,172 股 (約 $3.5M)。
- CEO LIN CHIH-HSIANG THOMPSON: 2026-06-12 以 $166.53 賣出 59,000 股 (約 $9.8M); 2026-05-19 以 $173.26 賣出 58,000 股 (約 $10.0M)。
- CFO MURRY STEFAN J: 幾乎每月固定賣出 4,000 股左右 (2026-06 至 2026-10 持續), 另 2026-06-12 大額賣出 33,000 股 (約 $5.5M)。持續性小額賣出與 10b5-1 計畫的一致性無法由資料確認。
- Director CHEN MIN-CHU MIKE: 2026-06-02 以 $201.00 賣出 8,247 股 (約 $1.7M)。Director DELANEY CYNTHIA: 2026-05-26 以 $189.23 賣出 56,575 股 (約 $10.7M)。
- 無內部人買入紀錄。CEO 2026-07-31 與多位董事於 2026-06-09 有股票獎勵 (grant), 未計入買入或賣出。
- 價格脈絡: 2026-05 至 06 賣出價約 $166–$205, 2026-10 賣出價約 $103–$120, 反映期間股價大幅下跌。

## Ownership shifts

- 機構持股比例 61.5%, 機構持股數 642 家, 內部人持股比例 9.1% (yf major_holders 目前快照)。
- 工具僅提供單一時點快照, 無歷史序列, 無法判斷機構集中度的趨勢方向。

## Net sentiment score

Composite: **偏空 (bearish) 至中性 (neutral) 之間, 偏向中性偏空**; 信心度: **低** (low-to-medium)。

- 分析師面: 偏多 (4/6 偏多, 近月小幅上調, 0 賣出評級)。
- 內部人面: 明顯偏空 (6 個月 $94.6M 賣出, 0 買入, 且多位高階主管持續減持)。
- 散戶面: 無法直接驗證; 唯一的 StockTwits 資料為二手轉述 "extremely bullish", 無法定調。
- 價格與資訊面: 近期急跌 (約 -17% 於一週內), 且資料中提及資本支出放緩疑慮, 並有財報日期來源衝突 (Intellectia 稱 11/5, Earnings Whispers 稱 11/9), 兩者皆早於 as-of 日期, 需向公司投資人關係頁面確認最新財報內容。

Divergence flag: **無法確認 (資料不足)**。若二手來源 "extremely bullish" 屬實, 則散戶偏多與內部人偏空、分析師偏多之間存在分歧, 但此判斷信心低, 需待 Reddit 或 StockTwits 原始資料補齊後再確認。

資料缺口與待辦:
1. Reddit (r/wallstreetbets, r/stocks): 本次 WebFetch 失敗, 需後續重試或改用其他來源。
2. StockTwits: 需使用者於網路設定中允許 api.stocktwits.com。
3. 分析師逐筆升降評與目標價變動: 目前工具未提供, 需另尋來源或工具支援。
4. 機構持股歷史趨勢: 目前只有快照。

SENTIMENT REPORT COMPLETE
