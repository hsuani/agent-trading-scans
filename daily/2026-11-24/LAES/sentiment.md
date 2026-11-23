# LAES 情緒分析 (Sentiment Analysis)

- Ticker: LAES (SEALSQ Corp, Nasdaq)
- 分析日期: 2026-11-24
- 資料來源: `pipeline/tools/yf.py` (rec_summary, recommendations, major_holders, inst_holders, insider；`source: cache`) 與 WebSearch (retail / social)
- 資料限制: yf 取數時 Cookie/crumb 抓取失敗，已 fallback 並取得資料；分析師樣本數極少 (2 位)。

---

## 1. 分析師共識 (Analyst Consensus)

| 期間 (period) | strongBuy | buy | hold | sell | strongSell |
|---|---|---|---|---|---|
| 0m (當期) | 1 | 1 | 0 | 0 | 0 |
| -1m (前一月) | 1 | 1 | 0 | 0 | 0 |

- 當期共識為 **Buy** (2 位分析師，皆為買進或強力買進)，與前月無變化。
- 外部聚合站的目標價與評等數據不一致 (WebSearch 結果顯示 average price target 約 5.875 與 4.00 等不同數字，且日期不明)，無法確認最新目標價，僅作參考。
- 樣本極小 (n=2)，單一評等變動即會大幅改變共識，可信度低。

## 2. 機構持股趨勢 (Institutional Holdings Trend)

### 持股總覽 (major_holders)

| 指標 | 數值 |
|---|---|
| insidersPercentHeld | 3.79% |
| institutionsPercentHeld | 7.58% |
| institutionsFloatPercentHeld | 7.88% |
| institutionsCount | 120 |

### 前十大機構 (inst_holders, 報告日 2026-09-30)

| 機構 | 持股比例 | 持股股數 | 較前期變動 (pctChange) |
|---|---|---|---|
| Susquehanna International Group | 1.41% | 2,696,839 | +91.66% |
| Bank Of New York Mellon | 0.78% | 1,491,055 | +0.20% |
| UBS Group AG | 0.63% | 1,203,298 | -0.12% |
| Kessler Investment Group | 0.46% | 886,073 | -9.16% |
| Two Sigma Investments | 0.44% | 849,253 | -23.01% |
| Man Group PLC | 0.38% | 727,547 | +98.10% |
| Jane Street Group | 0.30% | 580,506 | +100.00% |
| Millennium Management | 0.24% | 468,384 | +1,106.90% |
| HRT Financial LP | 0.22% | 424,356 | -62.50% |
| SBI Securities | 0.18% | 353,606 | +6.83% |

- 前十大中 **6 家增持、4 家減持**。
- 增幅最大者多為量化／做市型機構 (Susquehanna, Man, Jane Street, Millennium)，其持股期間短，反映的是交易活動而非長期信心。
- 長期型機構持股比例偏低 (機構合計 7.58%)，且 two sigma、HRT 等明顯減碼。
- 判讀: 機構面 **中性**，以短線交易性資金為主，缺乏明確的長線累積訊號。

## 3. 內部人交易 (Insider Transactions)

### 近期交易摘要 (2026-03-18 至 2026-11-19)

| 類型 | 筆數 (約) | 合計股數 (約) | 備註 |
|---|---|---|---|
| 公開市場賣出 (Sale) | 25 | 約 432,000 | 主要為 O'HARA (CFO)、ENGUENT (Officer) 定期賣出 |
| 公開市場買進 (Purchase) | 0 | 0 | 區間內未見任何買進 |
| 選擇權／衍生性證券轉換 (Conversion at $0.01) | 多筆 | 數百萬 | 屬權益激勵性質，不等同賣出 |

**重點事件**

- **2026-11-13**: CEO MOREIRA CARLOS CREUS 轉換衍生性證券 **1,606,226 股** (Ownership: D)。為區間內單筆最大項目。目前資料中未見後續賣出，但若後續出售將構成明顯賣壓，需持續追蹤 Form 4。
- **2026-11-03**: ENGUENT JEAN-PIERRE 以約 **1.38 元/股** 賣出 35,000 股，為目前可見最新的公開市場成交價。
- **2026-06 (約 3.50–3.69 元)**: CEO 與 CFO 於 6 月初及 5 月底集中賣出。
- **2026-03 至 2026-05 (約 2.08–3.06 元)**: CFO O'HARA 多次定期賣出，共計數十萬股。
- 其他: CFO 於 2026-03-30 與 2026-04-13 有大額 $0.01 轉換 (100,000 與 130,500 股)。

**判讀**

- 內部人 **持續淨賣出**，區間內 **無任何公開市場買進**。
- 賣出價由 3.5 元區間下滑至 1.38 元，內部人並未在低點承接。
- 衍生性證券轉換後賣出的模式常見於激勵方案到期或稅務安排，但 CEO 1.6M 股的轉換需列為待觀察的潛在賣壓。
- 整體內部人面: **偏空**。

## 4. 散戶／社群情緒 (Retail / Social Sentiment)

| 來源 | 內容 | 時間點 | 判讀 |
|---|---|---|---|
| TipRanks 投資人情緒 | "Very Positive"，約 826,191 名投資人，約 24.1% 散戶近 30 日變動持倉 | 不明確 | 偏多 (注意為聚合站自家指標) |
| Stocktwits 新聞標題 | SEALSQ 股價因智慧電表與 SpaceX 發射協議消息仍下跌，標題判定散戶偏空 | 不明確 (近期) | 偏空 |
| TipRanks 技術面 | 不同快照分別為負向與正向，兩者價格差距大 | 不一致 | 不可靠 |
| 空單比例 (Benzinga) | 約 5.8%–5.9% of float | 約 2026 夏季 | 中性偏低 |
| Reddit / 社群討論 | 搜尋未找到 2026-11 相關資料 | — | 無資料 |

- 散戶情緒訊號 **相互矛盾**: 聚合站偏多，但個別新聞與股價走勢偏空。
- 多數來源日期不明或過時，可信度低。
- 判讀: 散戶情緒 **中性，低信心**。

## 5. 綜合判斷 (Composite Judgment)

| 面向 | 主要依據 | 方向 | 信心 |
|---|---|---|---|
| 分析師共識 (Analyst Consensus) | 2 位分析師皆為 Buy，無變動 | 偏多 | 低 (n=2) |
| 機構持股 (Institutional Holdings) | 前十大 6 增 4 減，多為量化交易；機構僅 7.58% | 中性 | 中 |
| 內部人交易 (Insider Transactions) | ~432K 股公開賣出、零買進；價格由 3.5 跌至 1.38；CEO 1.6M 轉換待觀察 | 偏空 | 中高 |
| 散戶／社群 (Retail / Social) | 聚合站偏多與個別新聞偏空並存，資料陳舊 | 中性 | 低 |
| 價格趨勢佐證 (Price Context) | 公開成交價自約 3.5 元 (6 月) 下跌至約 1.38 元 (11 月) | 偏空 | 中 |

**綜合結論: 偏空至中性 (Negative-to-Neutral)，信心: 低至中**

- 主要風險: 內部人持續賣出、零公開買進、股價大幅下跌、CEO 1.6M 股轉換後可能的賣壓。
- 主要支撐: 分析師仍維持 Buy 評等、散戶聚合指標偏多，但樣本與資料時效性皆不足。
- 建議後續追蹤: (1) CEO 1.6M 股之後續 Form 4 申報；(2) 下一次 13F 機構持股更新；(3) 分析師評等與目標價變動；(4) 即時 Stocktwits / Reddit 討論。

---

## 資料與方法限制

- yf Cookie/crumb 取數失敗，資料來自 cache。
- 分析師樣本僅 2 位，統計意義有限。
- 機構持股為 2026-09-30 報告期資料，較 11 月落後約一個季度。
- WebSearch 結果多為聚合站與自動生成頁面，日期不一，已降低權重。
- 首次 WebSearch 查詢字串中混入與 LAES 無關的詞語，結果仍以 SEALSQ (LAES) 為主；已排除無關結果。

## Sources

- [TipRanks LAES stock investors](https://www.tipranks.com/stocks/laes/stock-investors)
- [TipRanks LAES forecast](https://www.tipranks.com/stocks/laes/forecast)
- [TipRanks LAES stock analysis](https://www.tipranks.com/stocks/LAES/stock-analysis)
- [Stocktwits: SEALSQ tumbles despite smart meter and SpaceX deals](https://stocktwits.com/news-articles/markets/equity/sealsq-tumbles-despite-landing-multi-million-dollar-smart-meter-deal-spacex-launch-agreement/chGBicfRZg)
- [Benzinga LAES sentiment](https://www.benzinga.com/quote/LAES/sentiment)
- [Benzinga LAES analyst ratings](https://www.benzinga.com/quote/LAES/analyst-ratings)
- [Investing.com SEALSQ consensus](https://ng.investing.com/equities/sealsq-consensus-estimates)
- [TradingView NASDAQ-LAES](https://www.tradingview.com/symbols/NASDAQ-LAES/?aff_id=118685)
