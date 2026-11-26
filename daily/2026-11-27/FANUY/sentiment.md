# Sentiment — FANUY (Fanuc ADR, 基礎標的 TSE:6954) as of 2026-11-27

注意事項:
- 日期落差: 系統當日為 2026-11-26, 任務要求 as-of 2026-11-27。所有資料最新僅到 11/19 (股價) 與 10/28 (ADR 技術面), 11/27 當日資料不存在。
- 資料來源以 yf 快取 (source: cache) 為主, 並以 WebSearch 補充。Yahoo 直連與 Reddit、StockTwits 直連於本沙箱受阻, 依指示改用 WebSearch。
- 基礎標的為東京上市 6954, FANUY 為 ADR。ADR 專屬的分析師覆蓋極少, 故分析師資料以 6954 為主。

## Analyst consensus

資料來源衝突, 需分開看:

| 來源 | Buy | Hold | Sell | 備註 |
|---|---|---|---|---|
| yf rec_summary (FANUY, 當期) | 1 (strongBuy) | 1 | 0 | 樣本僅 2 家, 不具代表性 |
| yf rec_summary (FANUY, 前一月) | 0 | 2 | 0 | 同上 |
| Investing.com 6954 共識 (日期不明) | 8 | 10 | 2 | 共 20 家, 標示為 Buy 共識 |

Recent moves (6954 為主, 來自 WebSearch, 未經 yf 驗證):
- 8/13: UBS 降至 Hold (Investing.com 列表)。StockAnalysis 另顯示 UBS 仍為 Buy, 目標價 ¥8,630 (5/8), 兩來源矛盾。
- 8/18: Citi 降至 Hold。
- 9/24: Goldman Sachs Sell。另一頁顯示 5/28 維持 Sell, 且 TipRanks 有 Goldman 自 Conviction Buy 降至 Buy 的新聞 (日期不明), 高盛評等路徑不一致。
- 10/28: JPMorgan 以 Hold 新覆蓋。Macquarie、CLSA 為 Buy。
- 沒有找到 11 月的評等變動。

價格與目標價背景:
- 6954 股價 ¥5,331 (11/19), 較 5/26 的 ¥8,399 下跌約 36.5%。52 週區間 ¥4,056 至 ¥8,880。
- ADR 價格來源不一: Tradestie 為 $18.72 (10/28), Motley Fool 約 $20, Yahoo 52 週區間 $14.54 至 $27.54。
- 結論: 分析師 Buy 共識與近期降評並存, 股價在 11 月已明顯弱於 5 月, 但目標價的最新更新時點不明。

## Retail social

- Reddit (r/wallstreetbets, r/stocks): 直連受阻。以 WebSearch 查詢未找到任何提及 FANUY 的 2026 年討論串。判定: 無可用資料, DATA_UNAVAILABLE。
- StockTwits: DATA_UNAVAILABLE。查詢未回傳 FANUY 的多空比。
- X / 新聞輿情: 未找到 2026 年 FANUY 相關的社群討論。
  - TipRanks 新聞情緒: 本週 59% 正面 (產業平均 56%), 但 news volume 未揭露。
  - TipRanks 部落客: Bullish 70%, 但僅 1 篇意見, 樣本不足。
  - Moomoo 留言頁: 僅見一則短評, 無實質論述。
- 聲量 (buzz volume): 無法量化。以查詢結果推斷為低關注度, 屬推論而非量測值。
- 傾向: 僅能判定 "資料不足"。新聞面偏正面, 但樣本極小, 不足以代表散戶情緒。
- 主題: 無可穩定辨識的重複主題。可見的主題僅為「股價大幅回落」與「技術面偏弱」(Investing.com 日線訊號 Strong Sell、Tradestie RSI 48.8 偏空動能)。這屬技術面, 不是社群情緒。

## Insider activity

Net 6mo: DATA_UNAVAILABLE。yf insider 回傳為空陣列 []。這可能是真的無交易申報, 也可能是快取缺漏或 ADR 不適用日本內部人申報資料, 無法區分。不能推定為「無內部人交易」。

## Ownership shifts

- yf major_holders: institutionsCount 27。institutionsPercentHeld 為 0.00187, insidersPercentHeld 為 0.0。這些數值疑似以小數而非百分比記錄, 且 insider 0% 與 Fanuc 實際持股結構不符, 判定為不可靠, 標記 DATA_UNAVAILABLE。
- 機構持股趨勢 (季度變化): DATA_UNAVAILABLE。

## Net sentiment score

- 分析師面: 中性偏多。Investing.com 共識為 Buy (8/10/2), 但 8 月起出現多家降至 Hold 或 Sell, 方向不一致。yf 小樣本僅 2 家, 權重低。
- 散戶面: DATA_UNAVAILABLE。新聞情緒 (TipRanks 59% 正面) 為唯一可用的訊號, 但樣本薄弱。
- 價格與技術面 (參考, 非情緒): 偏弱。股價較 5 月下跌約 36%, 日線訊號 Strong Sell。
- Composite: **中性 (neutral)**, 信心: **低**。原因是散戶資料缺失、內部人與機構資料不可靠, 且分析師來源互相矛盾。

Divergence flag: **無法判定 (DATA_UNAVAILABLE)**。散戶端無資料, 無法與分析師傾向比較。若日後取得散戶資料, 應特別留意: 分析師降評方向 (Hold/Sell 增加) 與新聞面正面 (59%) 之間是否存在背離。

## Sources (WebSearch / yf 輸出)
- https://www.investing.com/equities/fanuc-corp.-consensus-estimates
- https://stockanalysis.com/quote/tyo/6954/ratings/
- https://www.tipranks.com/news/the-fly/fanuc-downgraded-to-buy-from-conviction-buy-at-goldman-sachs
- https://www.tipranks.com/stocks/fanuy/stock-analysis
- https://www.tipranks.com/stocks/fanuy/bloggers
- https://tradestie.com/stocks/FANUY/why-moving-today/
- https://finance.yahoo.com/quote/FANUY
- https://www.fool.com/quote/otc/fanuy/
- https://moomoo.com/stock/FANUY-US/comments
