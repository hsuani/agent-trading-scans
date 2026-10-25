# Sentiment — TSLA as of 2026-10-25

資料完整度: 分析師評等與內部人交易可用; Reddit 與 StockTwits 無法取得 (見下方); 散戶情緒本次僅能以網路新聞與選擇權報導作粗略參考。

## Analyst consensus
43 家機構: 18 buy (strongBuy 4 + buy 14) / 23 hold / 2 sell (strongSell 0 + sell 2)。即 buy 約 42%、hold 約 53%、sell 約 5%。

近三個月趨勢 (yfinance 評等分布, 期間 -3m 至 0m):

| 期間 | Buy (含 strongBuy) | Hold | Sell (含 strongSell) |
|---|---|---|---|
| -3m | 23 | 19 | 6 |
| -2m | 22 | 20 | 5 |
| -1m | 19 | 21 | 4 |
| 0m (現況) | 18 | 23 | 2 |

Recent moves: 近三個月 buy 由 23 降至 18, hold 由 19 增至 23, sell 由 6 降至 2。 整體呈現「從 buy 轉向 hold、極端 sell 減少」, 並非明顯降評。yfinance 僅提供彙總分布, 未提供個別升降評明細, 因此無法確認具體哪家券商升或降評。

目標價 (網路來源, 日期不一, 僅供參考):
- Piper Sandler: Buy, 目標價 $500 (TipRanks, 無明確日期)
- Barclays: Hold, 目標價 $360 (TipRanks, 無明確日期)
- Fintel 彙整平均一年目標價約 $383 (頁面標示 2026-10-05, 股價欄位空白)
- 10 月初個股約 $354–357 (第三方分析, 2026-10-01)

## Retail social
- Reddit (r/wallstreetbets, r/stocks): 無法取得。WebFetch 遭拒 (Claude Code unable to fetch from www.reddit.com), 本次無貼文樣本、無 tilt 判斷、無討論量數據。
- StockTwits: 無法取得。api.stocktwits.com DNS 解析失敗, 無 bullish/bearish 標籤統計。
- X / 新聞: 單一網路搜尋結果, 來源品質參差。
  - 選擇權流向: 9 月一篇自動化選擇權分析顯示 bias 為 bullish、信心中等; 此為 9 月資料, 非 10 月。
  - 市場敘述: 10 月初報導指出賣方評等比例降至約 13%, 為 2023 年 4 月以來最低, 分析師「不願賣」但也「未明確看多」。
  - 催化劑: 第三季交付數據與延後的 Roadster 發表會被提及為近期焦點。
- Buzz volume: 無法量化 (缺 Reddit/StockTwits 資料), 不做相對於常態的量化判斷。
- Themes (僅依網路報導, 非社群樣本): 股價較 52 週高點 (約 $499) 回落約兩成、年初至今表現弱、Q3 交付、Roadster 發表時程。

Sample representative take (新聞報導語氣, 非社群原文): 「analysts increasingly reluctant to recommend selling」 — 以上為第三方報導之摘要, 非直接引用社群貼文。

## Insider activity
Net 6mo (2026-04-25 至 2026-10-25, 單位 USD M):

| 類別 | 筆數 | 金額 (USD M) | 說明 |
|---|---|---|---|
| 公開市場賣出 (Sale) | 4 | 約 13.3 (=0.0133B) | 含 Wilson-Thompson 約 10.0 (4/30, 董事); Taneja 合計約 3.3 |
| 公開市場買入 (Purchase) | 0 | 0 | 無 |
| 選擇權行權 (Conversion of Exercise) | 3 | 行權價值約 7,095 (含 CEO 約 7,094) | 非市價買入, 不計入淨買賣 |
| 未分類 (value 空白, 疑似稅扣或 RSU 相關) | 2 | — | Taneja, 6/5 與 9/4, 各約 6,500 股, 交易說明空白 |

Net 6mo (公開市場): 買入 $0M / 賣出 約 $13.3M → 淨賣出約 $13.3M。

Notable:
- Kathleen Wilson-Thompson (Director): 2026-04-30 賣出約 26,409 股, 金額約 $10.0M (價格區間 369–384); 同日另有 40,948 股選擇權行權。
- Vaibhav Taneja (CFO): 2026-05-13 以 $450 賣出 3,000 股 (約 $1.35M), 同日行權 3,000 股; 2026-06-08 以 $402 賣出 2,605 股 (約 $1.05M); 2026-09-08 以 $360 賣出 2,605 股 (約 $0.94M)。 呈規律性小額賣出。
- Elon Musk (CEO): 2026-06-16 行權約 303,960,630 股, 行權價 $23.34, 行權成本約 $7,094M。 此為選擇權行權紀錄, 資料中未附對應的賣出交易; 因未見公開市場買入, 不能視為看多訊號。是否伴隨出售, 需以 Form 4 原始申報核實。

Insider 解讀: 6 個月內無任何公開市場買入, 只有賣出 (金額約 $13M, 以 CFO 與董事為主); CEO 無公開買入, 其大額行權屬於選擇權行使, 性質不同。整體內部人訊號偏中性至略偏空。

## Ownership
- 內部人持股: 17.8%
- 機構持股: 43.7% (流通股口徑 53.1%)
- 機構數: 5,296
- 本次僅有單一時點快照, 無法判斷機構集中度的趨勢變化。

## Net sentiment score
Composite: **neutral** (信心: 低)

- 分析師: 偏中性 (buy 42% / hold 53% / sell 5%), 近期由 buy 轉 hold, sell 減少, 整體無明顯降評, 信心中等。
- 內部人: 偏空 (僅有公開市場賣出, 無買入), 但金額相對市值小, 且多為規律性或選擇權相關, 信心中等。
- 散戶: 無法判斷 (Reddit、StockTwits 皆無資料), 信心無。
- 新聞 / 選擇權: 報導互有矛盾 (9 月選擇權 bias 偏多, 10 月報導描述市場分歧), 信心低。

Divergence flag: **無法判定 (資料不足)**。散戶情緒缺失, 無法確認散戶與分析師是否方向相反。若後續補足 Reddit 或 StockTwits 資料, 需重新評估此旗標。

## Data gaps and caveats
- Reddit 與 StockTwits 本次無法存取, 散戶部分為空白, 不應由此推論「散戶沉默」。
- 評等分布為彙總值, 無個別券商升降評明細; 目標價來自第三方零散報導, 日期不一。
- 內部人 Musk 行權僅為 derivative conversion 紀錄, 未見對應賣出, 需 Form 4 核實。
- 未分類的 Taneja 交易 (value 空白) 未計入淨額。
