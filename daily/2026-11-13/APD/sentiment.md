# Sentiment — APD (Air Products and Chemicals) as of 2026-11-13

資料截止：yf repo cache（refreshed 2026-11-12）。未使用 2026-11-13 之後的資料。
價格基準：yf cache currentPrice 313.5 USD（previousClose 315.18 USD）。

## Analyst consensus

21 位分析師 (info.numberOfAnalystOpinions)；rec_summary 加總為 24 筆評等（4 Strong Buy + 11 Buy + 9 Hold），兩者口徑不同，以下以評等分布為準。

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 合計 |
|---|---|---|---|---|---|---|
| 本月 (0m) | 4 | 11 | 9 | 0 | 0 | 24 |
| 上月 (-1m) | 4 | 11 | 8 | 0 | 0 | 23 |
| -2m | 4 | 11 | 7 | 0 | 0 | 22 |
| -3m | 3 | 11 | 7 | 0 | 0 | 21 |

結論：9 buy-side (Strong Buy + Buy 合計 15) / 9 hold / 0 sell。recommendationMean 1.92（1 = Strong Buy，5 = Sell），對應 recommendationKey = buy。

Recent moves: 三個月內 Hold 由 7 增至 9，Strong Buy 由 3 增至 4，Buy 不變、Sell 為零。評等整體仍偏多，但 Hold 連續增加，屬輕微降溫訊號。個別券商升降級明細：DATA_UNAVAILABLE（pipeline/tools/yf 的 recommendations 僅回傳月度彙總，無逐家券商紀錄）。

目標價（USD，現價 313.5 USD）：

| 指標 | 目標價 USD | 相對現價 |
|---|---|---|
| 平均 (mean) | 344.10 | +9.8% |
| 中位數 (median) | 347.00 | +10.7% |
| 最高 | 375.00 | +19.6% |
| 最低 | 275.00 | -12.3% |

財報：最近一季（FQ4，截至 2026-09-30）於 2026-11-05 公布 EPS 3.61，與預估 3.61 持平（yf 紀錄 surprise -0.02%）。Trefis 網頁則稱「beat expectations」，兩者說法不一，以 yf 數字為準。下次財報預估 2027-01-29，預估 EPS 3.43。

## Retail social

- **Reddit (r/wallstreetbets, r/stocks)**: DATA_UNAVAILABLE。依指示未直接抓取 Reddit；WebSearch 未找到 APD 專屬的 Reddit 討論串。無法給出情緒傾向與樣本討論串。
- **StockTwits**: DATA_UNAVAILABLE（未取得訊息流）。
- **X / 新聞與網站評論**:
  - Trefis 頁面（資料至 2026-11-03）描述共識為 "Moderate Buy"，平均目標價 333.88 USD，並提到 2026-11-04 股價約 318.87 USD。語氣偏正面。
  - TipRanks 技術指標模型標示 APD 情緒為 Negative，評等 Hold（引述："For APD, the sentiment is Negative."）。此為演算法技術訊號，非散戶貼文。
  - Webull 一篇文章提及估值風險（日期不明），認為若市場情緒降溫，股價溢價可能承壓。
  - 選擇權：Benzinga 顯示 Put/Call 比 0.24（日期不明，未能驗證），若屬實則偏向買權部位。
  - 空方部位：yf cache shortPercentOfFloat 2.15%；Benzinga 顯示約 1.8%。以 yf 為準。
- **Retail buzz volume**: 無法量化（DATA_UNAVAILABLE）。搜尋結果未見 APD 有顯著的社群熱議，推定聲量屬低可見度，但此為推論而非已驗證資料。
- **Retail tilt**: 無法判定（DATA_UNAVAILABLE）。
- **Themes（僅能由網路評論歸納）**: 估值（forward P/E 約 20.2，追蹤 P/E 因一次性損益被拉高至 131，數字失真）；財報後預期修正；技術面偏弱訊號與基本面偏多之間的分歧。

## Insider activity

查詢期間：2026-05-13 至 2026-11-13（近 6 個月）。

- **6 個月內（2026-05-13 至 2026-11-13）紀錄的公開市場買入或賣出：0 筆**。
- Net 6mo: $0 buys, $0 sells（USD M）。

6 個月窗口外、但最接近的紀錄：

| 日期 | 申報人 | 職位 | 交易 | 股數 | 金額 (USD M) |
|---|---|---|---|---|---|
| 2026-05-01 | SCHAEFFER MELISSA N | CFO | 賣出 @303.76 | 2,714 | 0.82 |
| 2026-02-12 | MANTLE RIDGE, L.P. | 10% 以上大股東 | 賣出 @284.21 | 70,175 | 19.94 |
| 2026-02-12 | MANTLE RIDGE, L.P. | 10% 以上大股東 | 贈與 | 1,759 | 0 |

- 其他近期紀錄多為獎勵發放（Stock Award，2025-12 CEO MENEZES EDUARDO F 17,376 股；CFO SCHAEFFER 8,357 股等），無現金金額。
- 最後一筆公開市場買入為 2025-04 董事 EVANS ANDREW W 買入 5 股（約 0.001 USD M），實質意義可忽略。
- 2025-02 曾有一波較大規模的高層賣出（BOLS IVO 18,000 股，約 5.65 USD M；KURT LEFEVERE、GALOVICH BRIAN 等），屬一年以上前，不計入本期。
- 注意：feed 最新一筆為 2026-05-01，6 個月內無任何紀錄，可能為真實無交易，也可能為資料延遲。此點無法由 cache 單獨確認，應視為 DATA_UNAVAILABLE 的可能性存在。

## Ownership shifts

- 機構持股比例 94.66%（institutionsFloatPercentHeld 96.48%），機構戶數 2,256；內部人持股 1.89%。
- 前十大持股合計約 46.6%（依最近一期報告）。

| 機構 | 持股比例 | 股數變動 (vs 前期) | 市值 (USD M) | 報告日 |
|---|---|---|---|---|
| BlackRock Inc. | 8.23% | +1.45% | 5,743.6 | 2026-06-30 |
| Vanguard Capital Management | 6.53% | +0.51% | — | 2026-06-30 |
| State Farm Mutual Automobile Insurance | 5.32% | 0.00% | — | 2026-06-30 |
| Capital Research Global Investors | 4.76% | +1.84% | — | 2026-06-30 |
| State Street Corporation | 4.61% | +1.59% | — | 2026-06-30 |
| Capital International Investors | 4.30% | -3.71% | — | 2026-06-30 |
| Dodge & Cox | 4.22% | +1.75% | — | 2026-06-30 |
| Vanguard Portfolio Management | 3.97% | +54.94% | — | 2026-06-30 |
| JPMorgan Chase & Co | 2.36% | -13.15% | — | 2026-06-30 |
| Geode Capital Management | 2.28% | +1.13% | — | 2026-09-30 |

註：「市值」欄僅 BlackRock 有完整數值；其餘未在 cache 中逐一取得，標示 —。報告為季度申報，有時間落差。

趨勢：前十大中多數為增持（Dodge & Cox、Capital Research、State Street、Vanguard PM），減持者為 Capital International（-3.7%）與 JPMorgan（-13.2%）。整體為機構小幅淨增持，無大型集中撤出跡象。

## Market snapshot（參考）

- 市值約 69.8 B USD（313.5 USD × 222.7 M 股，手算驗證一致）。
- 52 週區間：229.11 – 324.00 USD；50 日均 295.27 USD，200 日均 292.07 USD。
- 平均成交量 1.07 M 股，近 10 日 1.24 M 股。

## Net sentiment score

- **Analyst 面**：偏多（中等信心）。Buy 類 15 / Hold 9 / Sell 0，目標價均值高於現價約 10%，但 Hold 三個月增加 2 家。
- **Retail 面**：無法評估（DATA_UNAVAILABLE）。僅有低可信的選擇權 Put/Call 與網路評論訊號，且日期不完整。
- **Insider 面**：中性。6 個月內無公開市場交易紀錄；窗口外有一筆 CFO 小額賣出與一筆大股東大額賣出。
- **Ownership 面**：中性偏多。機構淨增持、無集中撤出。
- **Composite**: 偏多（bullish lean），信心中等偏低。主要依據為分析師評等與機構持股，零售面缺失使整體信心受限。
- **Divergence flag**: 無法判定。零售傾向資料缺失，無法與分析師傾向比較。網路技術面訊號（TipRanks Negative）與分析師傾向（Buy 為主）略有分歧，但此為技術模型而非散戶情緒，不計入 divergence 判定。

### Sources

- [Trefis — Air Products and Chemicals (APD)](https://www.trefis.com/data/companies/APD?from=section_ticker)
- [TipRanks — APD stock analysis](https://www.tipranks.com/stocks/apd/stock-analysis)
- [Webull — Air Products valuation article](https://www.webull.com/news/15852961885625344)
- [Benzinga — APD sentiment](https://www.benzinga.com/quote/APD/sentiment)

SENTIMENT REPORT COMPLETE
