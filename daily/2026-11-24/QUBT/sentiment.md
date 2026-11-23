# QUBT 情緒分析 (sentiment-analyst)

- 標的: QUBT (Quantum Computing Inc.)
- 任務日期: 2026-11-24
- 資料來源: `pipeline/tools/yf.py` (rec_summary, recommendations, major_holders, inst_holders, insider)，Yahoo cookie/crumb 取得失敗，資料為快取 (`source: cache`)；WebSearch 補充零售/社群情緒
- 注意: 系統當日為 2026-11-23，任務日期為 2026-11-24。最新可用價格約為 2026-11-05 的 USD 6.43。

---

## 1. 分析師共識 (Analyst Consensus)

| 指標 | 數值 |
|---|---|
| strongBuy / buy / hold / sell / strongSell (期間 0m) | 0 / 4 / 2 / 0 / 0 |
| 近 4 個月 (0m 至 -3m) | 每期皆為 0 / 4 / 2 / 0 / 0，無變化 |
| 平均目標價 (WebSearch, 2026-11-05 至 11-06) | 約 USD 18.67 至 18.86 (6 至 7 位分析師) |
| 目標價區間 | 高 USD 32 (Ascendiant, 2026-08-26 維持)，低 USD 10 (Cantor Fitzgerald, Hold, 2026-08-11) |
| 近期動作 | Northland 首次給予 Buy，目標 USD 20 (2026-04-20) |

判讀:
- 評級結構偏多 (4 Buy : 2 Hold : 0 Sell)，近 4 個月沒有調整。
- 平均目標價約 USD 18.7，相對 USD 6.43 的價格約有 +190% 上漲空間。這個差距極大，較可能反映目標價未隨股價更新，應視為訊號較弱。
- 來源之間的平均目標價略有出入 (USD 18.00 至 18.86)，可能來自不同分析師集合與日期。

## 2. 機構持股趨勢 (Institutional Holdings)

整體指標:

| 指標 | 數值 |
|---|---|
| institutionsPercentHeld | 48.89% |
| institutionsFloatPercentHeld | 55.64% |
| insidersPercentHeld | 12.13% |
| institutionsCount | 439 |

主要機構持股 (最新申報 2026-09-30 為主，Penserra 為 2026-06-30):

| 機構 | 持股比例 | 持股股數 | 季度變動 |
|---|---|---|---|
| BlackRock Inc. | 59.29% | 17,227,809 | -2.85% |
| Vanguard Capital Management | 30.84% | 8,962,225 | +1.28% |
| Penserra Capital Management | 24.02% | 6,979,349 | **+108.35%** (2026-06-30) |
| Defiance ETFs | 23.87% | 6,935,316 | -1.39% |
| Vanguard Portfolio Management | 22.36% | 6,495,958 | -1.08% |
| Geode Capital | 18.61% | 5,407,167 | +1.59% |
| State Street | 17.17% | 4,987,715 | +1.35% |
| Morgan Stanley | 13.16% | 3,824,328 | +16.17% |
| Mirae Asset Global ETFs | 12.79% | 3,715,467 | **+63.49%** |
| Susquehanna International | 9.82% | 2,853,333 | **+143.27%** |

判讀:
- 增持方多為主動型與新進者 (Penserra、Susquehanna、Mirae、Morgan Stanley)，屬於偏正面的訊號。
- 被動與 ETF 持股大致持平，屬於中性。
- BlackRock 小幅減持 (-2.85%)。
- 整體趨勢: **偏正面 (accumulation)**，但樣本集中於季度申報，時效約 1 至 2 個月。

## 3. 內部人交易 (Insider Transactions)

近期 (2026 年) 活動:

| 日期 | 內部人 | 職位 | 類型 | 股數 | 價格 |
|---|---|---|---|---|---|
| 2026-08-20 | HUANG YUPING | CEO | 股票獎勵 + 衍生性證券轉換 | 584,897 (多筆) | USD 8.14 至 8.95 |
| 2026-05-28 | HUANG YUPING / DIANAT / BEGLIARBEKOV | CEO / Officer / COO | 股票獎勵 | 58,558 / 24,774 / 24,774 | 0 |
| 2026-04-13 | 5 位董事 (TURMELLE, FAGENSON, WEIMER, SHABANI, SCHWARTZ) | Director | 股票獎勵 | 各 22,123 | USD 6.78 |
| 2026-03-11 | ROBERTS CHRISTOPHER BRUCE | General Counsel | **賣出** | 78,262 | USD 7.85 |
| 2026-03-10 | ROBERTS CHRISTOPHER BRUCE | General Counsel | 衍生性證券轉換 | 400,000 | USD 6.85 |
| 2026-01-07 | BEGLIARBEKOV MILAN | COO | **賣出** | 2,860 | USD 11.85 |

2025 年的歷史 (參考):
- 2025 年期間有大量賣出，包括 HUANG YUPING (2025-09-04，1,000,000 股，USD 14.42；2025-05-19，500,000 股，USD 11.70)、BOEHMLER (2025-06，約 27 萬股，USD 15 至 20)、TURMELLE、SHABANI 等。
- 2025-03-27 另有 HUANG 贈與 4,000,000 股 (Stock Gift)。

判讀:
- 過去 12 個月的公開市場賣出很少，只有兩筆小額 (Roberts 78k 股，Begliarbekov 2.9k 股)。
- 2026 年的主要活動為獎勵與衍生性證券轉換，**沒有看到大規模的公開市場買進**。
- 2025 年的高價大量賣出 (USD 11 至 20) 與目前股價 (USD ~6.4) 之間的對比，偏向負面。
- 整體: **中性偏謹慎**。
- 資料時效: 最新交易為 2026-08-20，約 3 個月前。

## 4. 零售與社群情緒 (Retail / Social Sentiment)

WebSearch 結果 (多為歷史快照，未取得即時數值):
- **Stocktwits**: 2026 年 3 月的報導指出，QUBT 訊息量在一週內上升約 602%，同時伴隨對估值與泡沫的疑慮 (引用 Barron's)。
- 2025 年 3 月與 5 月的 Stocktwits 情緒曾為 "extremely bullish" (96/100)，財報後的關注度也很高。
- **Reddit (ChartExchange)**: 情緒分數混合，有質疑公司商業模式的留言 (例如「Quantum Computing Inc 並不生產量子電腦」)。資料沒有日期。
- **AltIndex**: 單日 Stocktwits 提及次數估計約 1,485 次，屬於近期高峰的估計，未註明日期。
- **Yahoo 空頭文章**: 指出股價在一個月內上漲 110%，零售資金湧入，並提到內部人賣出。

判讀:
- QUBT 屬於高關注、高波動的零售熱門股，情緒在極度看多與估值疑慮之間快速切換。
- 目前沒有取得 2026-11 的即時情緒數值，**信心低**。
- 若零售熱度與股價同向上升，短期波動風險會升高。

## 5. 綜合判斷 (Composite Judgment)

| 面向 | 訊號 | 分數 (-1 至 +1，粗估) | 權重 | 信心 | 理由 |
|---|---|---|---|---|---|
| 分析師共識 | 偏多 | +0.5 | 30% | 中 | 4 Buy / 2 Hold / 0 Sell，但目標價與現價差距過大，可能過時 |
| 機構持股趨勢 | 偏多 | +0.4 | 25% | 中 | 新進與主動型機構大幅加碼；BlackRock 小幅減持 |
| 內部人交易 | 中性偏謹慎 | -0.1 | 25% | 中 | 2026 年以獎勵為主，無大量公開買進；2025 年有高價大量賣出 |
| 零售 / 社群情緒 | 高熱度、方向不明 | 0.0 | 20% | 低 | 只有歷史快照，無即時數值；估值與泡沫疑慮並存 |
| **綜合** | **中性偏多 (投機性)** | **約 +0.25** | 100% | 中低 | 機構與分析師偏多，內部人與零售面不支持追價 |

結論:
- 綜合情緒為 **中性偏多，但屬於投機性質**。
- 機構與分析師面較為正面，內部人與零售面則偏謹慎或不確定。
- 主要風險: 目標價與現價差距過大，零售熱度可能快速反轉，內部人 2025 年的高價賣出紀錄。
- 建議後續追蹤: (1) 取得 2026-11 的即時 Stocktwits / Reddit 情緒數值；(2) 以目前股價重新確認分析師目標價；(3) 留意 13F 於 2026-12 申報後的機構變動。

---

## 來源

- Stocktwits 零售熱度報導: https://stocktwits.com/news/equity/markets/qubt-qbts-ionq-rgti-stock-spark-retail-buzz-on-stocktwits-as-valuation-concerns-emerge/ch67F7yR3Ka
- Stocktwits 2025 Q1 零售情緒: https://stocktwits.com/news-articles/markets/equity/quantum-computing-retail-investors-excited-after-2025-q1-results/chivxzKRbnS
- Reddit 情緒 (ChartExchange): https://chartexchange.com/symbol/nasdaq-qubt/trends/reddit
- AltIndex Stocktwits 提及次數: https://altindex.com/ticker/qubt/stocktwits-mentions
- Yahoo Finance 空頭觀點: https://finance.yahoo.com/news/quantum-computing-inc-qubt-bear-140504803.html
- Investing.com 共識估計: https://www.investing.com/equities/quantum-computing-otc-consensus-estimates
- Benzinga 情緒頁: https://kr.benzinga.com/quote/QUBT/sentiment
- Fox Business 報價頁: https://www.foxbusiness.com/quote?stockTicker=QUBT
- Nasdaq (Northland 初始覆蓋): https://www.nasdaq.com/articles/northland-capital-markets-initiates-coverage-quantum-computing-qubt-outperform
