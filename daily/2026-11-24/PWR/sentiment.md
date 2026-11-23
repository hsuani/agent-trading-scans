# Sentiment — PWR (Quanta Services) as of 2026-11-24

## Analyst consensus
共 31 位分析師：1 Strong Buy / 24 Buy / 5 Hold / 0 Sell / 1 Strong Sell（買進側 25 家，約 81%；賣出側 1 家，約 3%）。

近 3 個月變化（yf rec_summary）：
| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 合計 |
|---|---|---|---|---|---|---|
| 目前 (0m) | 1 | 24 | 5 | 0 | 1 | 31 |
| 1 個月前 (-1m) | 1 | 24 | 4 | 0 | 1 | 30 |
| 2 個月前 (-2m) | 1 | 24 | 5 | 0 | 1 | 31 |
| 3 個月前 (-3m) | 0 | 23 | 6 | 0 | 1 | 30 |

- 買進側由 3 個月前的 24 家升至 25 家，Hold 由 6 家降至 5 家，屬於小幅正向漂移，未見大規模評等調整。
- `yf recommendations` 回傳內容與 rec_summary 相同，只有彙總計數，沒有逐家機構的升降評等紀錄，因此無法列出個別 upgrade / downgrade。
- 目標價變動 yf 工具未提供，以下為 WebSearch 找到的二手資料（日期不一，僅供參考）：
  - 2026-05-28 Oppenheimer 由 Perform 升為 Outperform。
  - 2026-04-27 Citi 目標價由 $640 上調至 $733，維持 Buy。
  - 2026-08-06 Argus 維持 Buy，目標價 $800。
  - 2026-09-24 Bernstein 目標價 $775（當時股價約 $634.9）。
  - 未找到 2026 年 11 月的評等調整，也未見 2026 年的降評紀錄。
- 各來源的平均目標價互相矛盾（約 $650 至 $795 不等），多為未標註日期的快照，不宜直接採用。

## Retail social
- Reddit（r/wallstreetbets、r/stocks）：DATA_UNAVAILABLE。WebSearch 未找到 2026 年與 PWR 相關的 WSB 或 r/stocks 討論串，未能取得可引用的樣本或討論方向。依任務指示未直接抓取 Reddit JSON。
- StockTwits / X：DATA_UNAVAILABLE（無實質貼文可引用）。本次未直接查詢 StockTwits API。
- 聚合型來源：AltIndex 的 NLP 情緒分數為 100/100（偏多），但其為自動化彙總、無法驗證樣本，且未拆出 WSB 單獨數據，僅作背景參考。
- 聲量（buzz）：無法量化對比典型水準。以搜尋結果判斷，散戶討論可見度偏低。
- 語氣傾向：來源有限，無法判定。聚合分數偏多，但缺乏實際貼文支撐。
- 主要題材（從新聞與聚合文章歸納，非散戶原文）：
  - AI 資料中心與電網投資題材，Weiss Ratings 將 11 月的上漲歸因於 CoreWeave 11/10 財報後的 AI 基建熱度。
  - 估值偏高的爭論：Trailing P/E 約 71.6、Forward P/E 約 38.3（引用資料來源與日期不明）。
  - 「電力是 AI 瓶頸」的長期敘事，常見於 2026 年 2 月的看多文章。

## Insider activity
過去 6 個月（2026-05-24 至 2026-11-24）：淨買入 $0M；賣出合計約 $123.2M。
| 日期 | 內部人 | 職位 | 交易 | 股數 | 金額 (USD M) |
|---|---|---|---|---|---|
| 2026-05-05 | Earl Charles Austin Jr. | CEO | 賣出 (價格 $765–778) | 155,992 | 120.2 |
| 2026-05-04 | Paul M. Nobel | Officer | 賣出 (價格 $756.98) | 4,000 | 3.0 |

- 以 CEO 的交易核對：155,992 股 × 約 $770 ≈ $120.1M，與工具回報的 $120.2M 相符。
- 6 個月窗口內無公開市場買進（Buy）紀錄。
- 其他窗口內紀錄為贈與（Stock Gift，價格 0）與董事股權發放（無交易價格，性質未標示，多為年度董事授予，待確認）。
  - 2026-05-05 CEO Austin 贈與 4,008 股。
  - 2026-05-11 董事 Wyrsch 贈與 2,500 股。
  - 2026-05-28 董事 Fried 4,823 股。
  - 2026-06-01 六位董事各 559 股，Beneby 870 股。
- 窗口外參考（2025-11）：GC Wayne 賣 14,000 股（約 $6.2M）、Ducey 賣 7,653 股（約 $3.4M）、董事 Jackman 賣 6,349 股（約 $2.9M）、董事 Fried 賣 4,000 股（約 $1.8M，間接持股）。合計約 $14.3M。
- 內部人持股比例約 0.67%（major_holders），持股集中度低，但 CEO 單次賣出金額較大。
- 是否為 10b5-1 預定計畫：工具未提供，無法判定。
- 注意：CEO 出售價位約 $765–778，與近期其他來源提到的股價（見下節）落差很大，需以即時報價核對。

## Institutional ownership trend
- 機構持股比例 90.98%（流通股 91.6%），機構家數 2,558 家；內部人 0.67%。
- 前十大持有人（13F，截至 2026-09-30）合計約 37.6% 持股：
| 機構 | 持股比例 | 股數 (百萬股) | 持股市值 (USD B) | 季度變化 |
|---|---|---|---|---|
| BlackRock | 8.80% | 13.26 | 8.05 | +1.5% |
| Vanguard Capital Management | 6.53% | 9.84 | 5.98 | +0.4% |
| Vanguard Portfolio Management | 4.66% | 7.02 | 4.26 | +1.3% |
| State Street | 4.39% | 6.62 | 4.02 | +0.6% |
| Peconic Partners | 2.69% | 4.05 | 2.46 | -14.3% |
| JPMorgan Chase | 2.63% | 3.96 | 2.41 | -25.4% |
| Geode Capital | 2.39% | 3.60 | 2.19 | +2.2% |
| Bank of America | 2.15% | 3.24 | 1.97 | +2.2% |
| FMR (Fidelity) | 1.95% | 2.94 | 1.78 | -16.4% |
| Morgan Stanley | 1.44% | 2.17 | 1.31 | -6.3% |

- 趨勢：被動型基金（BlackRock、Vanguard、Geode、State Street）持續加碼；主動型與部分銀行持有人（JPM、FMR、Peconic、Morgan Stanley）減碼。
- 隱含 9/30 每股價格約 $607（由 BlackRock 持股市值除以股數推算），可作為季末價位參考。
- 此為單一季度快照，且 13F 有申報延遲，不能代表 11 月的即時持股狀況。

## 價格資料衝突（對本報告的影響）
- 搜尋結果中，2026-11-06 收盤價有兩個來源：Fox Business 為 $509.04，Benzinga 為 $542.4。Benzinga 另記錄 11/5 單日下跌 12.3%。
- 上述價位與 CEO 5 月出售價（約 $770）及 9/30 隱含價（約 $607）差距很大，代表 11 月股價可能已大幅回檔，或其中一來源有誤。
- 本報告不採用任何單一價格作為結論，建議以即時報價核對後再使用本節資料。

## 來源（WebSearch 摘要，僅供核對）
- https://finance.yahoo.com/quote/PWR/analysts
- https://www.nasdaq.com/articles/oppenheimer-upgrades-quanta-services-pwr
- https://finance.yahoo.com/markets/stocks/articles/citi-raises-price-target-quanta-091309127.html
- https://site.financialmodelingprep.com/market-news/quanta-services-pwr-stock-775-price-target-22-upside
- https://weissratings.com/en/instant-news-alerts/quanta-services-inc-pwr-up-4-7-time-to-shift-from-cash-to-shares
- https://altindex.com/ticker/pwr/sentiment

## Net sentiment score
Composite: 偏多（neutral-to-bullish），信心：中低。

依據分項：
- 分析師共識：偏多（信心：中高）。買進側約 81%，近 3 個月小幅上修。
- 內部人：偏空訊號（信心：中）。6 個月內僅有賣出、無公開買進，CEO 單筆 $120M 為主要來源。但多數為既定薪酬與贈與背景下的出售，且未確認 10b5-1 性質。
- 散戶社群：無法判定（DATA_UNAVAILABLE）。聚合分數偏多，但缺乏原始貼文支撐，不納入計分。
- 機構持股：中性偏穩。被動持有增加，主動持有人減碼。

Divergence flag: 否（散戶與分析師方向無法比較，因散戶資料不足）。
補充：內部人賣出與分析師偏多方向相反，此為本次較值得留意的分歧點。

## 摘要表
| 面向 | 結論 | 關鍵數據 | 信心 |
|---|---|---|---|
| 分析師共識 | 偏多 | 買進側 25 / 31（約 81%），賣出側 1 家 | 中高 |
| 評等趨勢 | 小幅上修 | 3 個月內買進側 +1，Hold -1 | 中 |
| 目標價 | 資料分歧 | 二手來源約 $650–795，日期混雜 | 低 |
| 內部人交易 | 偏空訊號 | 6 個月內賣出約 $123.2M（CEO 佔 $120.2M），買進 $0 | 中 |
| 機構持股 | 中性偏穩 | 機構 90.98%，被動增持、主動減持 | 中 |
| 散戶情緒 | 無法判定 | Reddit / StockTwits 無實質樣本 | 低 |
| 價格資料 | 來源衝突 | 11/6 收盤 $509 vs $542 | 需核對 |
| 綜合 | 偏多（neutral-to-bullish） | 分析師偏多為主，內部人賣出為主要反向訊號 | 中低 |

SENTIMENT REPORT COMPLETE
