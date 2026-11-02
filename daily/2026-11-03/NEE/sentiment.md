# Sentiment — NEE as of 2026-11-03

資料說明: yf 工具 cookie/crumb 取得失敗 (ConnectionError), 但 recommendations / rec_summary / insider / major_holders 仍有回傳。散戶社群部分無法直接取得 Reddit / StockTwits 原始貼文 (依指示不以 WebFetch 讀取社群平台), 僅能用 WebSearch 的第三方彙整結果, 日期多不明確或為 2024–2026 年舊資料。

## Analyst consensus

rec_summary (0m, 22 位分析師): Strong Buy 2 / Buy 12 / Hold 7 / Sell 1 / Strong Sell 0。買方合計 14 (約 64%), 持有 7 (約 32%), 賣方 1 (約 5%)。

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 合計 | 買方合計 |
|---|---|---|---|---|---|---|---|
| 本期 (0m) | 2 | 12 | 7 | 1 | 0 | 22 | 14 |
| 前一月 (-1m) | 3 | 11 | 6 | 1 | 0 | 21 | 14 |
| 前二月 (-2m) | 2 | 10 | 7 | 1 | 0 | 20 | 12 |

- 近兩個月買方評級由 12 增至 14, 持有由 7 降至 6 再回到 7, 賣方維持 1, 無評級下調的跡象。
- recommendations 工具僅回傳月度彙總, 無個別分析師升降評等事件, 無法確認具體 upgrade / downgrade 名單。
- 目標價: yf 本次未回傳目標價資料。WebSearch 彙整來源 (Barchart) 提及平均目標價約 $97.57 (隱含約 10% 上行空間, 22 位分析師); TipRanks 快照顯示平均目標價約 $93.06 (近 3 個月 17 位分析師), 另一快照為 $85.80, 兩者快照日期不同。Evercore ISI 於 7 月財報後維持 Buy, 目標價 $107 (來源年份未完全確認)。以上數字未經 yf 驗證, 採用前需以即時報價與目標價資料再確認。

## Retail social

- Reddit: 未能取得 r/wallstreetbets 或 r/stocks 上 NEE 的近期貼文 (WebSearch 未回傳相關討論串)。第三方情緒追蹤 SentiSense 顯示 (日期標示 2026-08-09) Reddit 提及中看多占 8%, 新聞面明顯較多頭; 此數字的定義與樣本數不明, 僅供參考。
- StockTwits / X: 未取得 StockTwits 串流資料。LunarCrush 頁面顯示過去 24 小時約 325 則 $NEE 貼文, 正向情緒約 26% (頁面日期不明)。X 的即時貼文未能取得。
- 聲量: 約 325 則 / 24h 的規模屬一般, 缺乏同期基準無法判斷相對於平常是放大或縮小。
- 主要主題 (來自第三方摘要, 未逐篇核實):
  - 利空: 針對 $67B Dominion 併購案的監管反對聲浪; 對 NextEra 在佛州政治關係的批評 (LunarCrush 將其與近一個月 -6.84% 跌幅連結)。
  - 利多: AI 資料中心用電需求成長的再生能源題材 (TradingView 社群貼文主張)。
- 散戶語氣: 整體偏混合。新聞與部落格面偏多頭, 社群正向比例偏低 (約 26%), 方向不一致, 信心低。
- 引述: 本次未取得可直接引用的原始貼文, 故不引述。

## Insider activity

Net 6mo (2026-05-03 至 2026-11-03): 無公開市場買進、無賣出紀錄於此區間。yf 回傳的最新一筆交易日期為 2026-03-13, 6 個月內資料可能不完整 (cookie 取得失敗), 需人工在 SEC Form 4 再確認。

6 個月窗口外的背景 (2026-01 至 2026-03) 公開市場賣出, 合計約 $17.9M (美元, 依 yf Value 欄位加總, 不含選擇權行使的轉換價值):
- CEO John W. Ketchum: 2026-02-09 賣出 99,603 股, 約 $8.9M (同日行使選擇權 99,603 股, 轉換價值約 $2.9M 未計入)
- Officer Charles E. Sieving: 2026-02-04 賣出 30,000 股, 約 $2.7M
- Officer Ronald R. Reagan: 2026-02-04 賣出約 $1.7M; 2026-02-17 約 $0.5M; 2026-01-22 約 $0.9M
- Officer Terrell Kirk Crews II: 2026-03-09 賣出約 $1.8M
- Officer James Michael May: 2026-03-09 賣出約 $0.6M
- Officer Nicole J. Daggs: 2026-03-13 賣出約 $0.5M
- Officer Mark Lemasney: 2026-03-09 賣出約 $0.3M
- CFO Michael Dunne: 2025-09 賣出約 $0.7M (超出窗口)
- Director Armando Pimentel Jr.: 2025-11-17 賣出 145,140 股約 $12.2M (超出窗口)

另有 2026-02-12 全體董事與高管的股票獎勵 (無現金價值)。
解讀: 過去 6 個月公開市場買進為零, 大額交易以 CEO 與高管的既有選擇權行使後賣出為主, 屬例行性質的減持而非加碼。方向偏中性偏負面, 信心中等 (資料窗口與完整性受限)。

## Ownership shifts

- 機構持股: 約 86.5% (institutionsPercentHeld 0.86509), 機構數 3,828。
- 內部人持股: 約 0.12%。
- 趨勢: major_holders 僅提供單一時點快照, 無歷史比較, 無法判斷機構集中度是增加或減少。

## Net sentiment score

Composite: **中性偏多 (neutral-to-bullish), 信心中等。**

- 分析師面: 偏多, 信心中高。買方占 64%, 近兩月買方評級小幅增加, 無下調跡象。
- 散戶面: 中性, 信心低。資料零散、日期不一, 正向比例約 26%, 社群與新聞面方向不一致。
- 內部人面: 中性偏負, 信心中等。無公開市場買進, 近期大額賣出多為選擇權行使後的減持。
- 機構面: 高持股比例 (約 86.5%), 無趨勢資料, 中性。

Divergence flag: **可能有 (弱)**。分析師偏多, 而第三方社群情緒數據 (正向約 26%) 與內部人減持方向偏弱, 與分析師的多頭立場不一致。但散戶樣本不足, 此背離訊號的可靠性低, 不宜單獨作為判斷依據。

資料缺口清單:
1. Reddit (r/wallstreetbets, r/stocks) 與 StockTwits 原始貼文未取得。
2. yf cookie/crumb 失敗, 內部人與目標價資料需以 SEC Form 4 與即時來源複核。
3. 第三方摘要多為 2024–2026 舊資料, 未能確認 2026-11 當月的最新散戶與新聞情緒。

SENTIMENT REPORT COMPLETE
