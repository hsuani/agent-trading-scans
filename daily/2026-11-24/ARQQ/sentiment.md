# ARQQ 情緒分析 (Sentiment Analysis)

- Ticker: ARQQ (Arqit Quantum Inc.)
- 目標日期: 2026-11-24
- 資料來源: `pipeline/tools/yf.py` (rec_summary, recommendations, major_holders, inst_holders, insider)、WebSearch (零售/社群情緒)
- 資料時效注意: yfinance 的 insider 與 institutional 資料最新只到 2026-10 / 2026-09-30 季報，未涵蓋 11 月的交易與持股變動。Cookie/crumb 取得失敗，但個股資料仍有回傳。

---

## 1. Analyst Consensus (分析師共識)

| 項目 | 結果 |
|---|---|
| `rec_summary` (yfinance) | 無資料 (空陣列) |
| `recommendations` (yfinance) | 無資料 (空陣列) |
| 外部彙整: H.C. Wainwright | Buy, 目標價 $60 (最後一次為 2025-12-18 reiterate，資料過舊) |
| 外部彙整: Investing.com consensus | Strong Buy (僅依單一評等) |
| 外部彙整: Benzinga consensus | 目標價 $30.75 (2 位分析師，最新評等 2025-10-13，資料過舊) |
| 外部彙整: TipRanks | Neutral, score 42, 目標價 $11.50 (06/06/26；為 AI 模型產出，非傳統券商評等) |

**判讀**: 傳統券商覆蓋極少 (實際僅見一家 H.C. Wainwright)，且最新一次評等距今超過 11 個月。若以 $60 目標價對比近期股價約 $12-13，落差極大，評等不具參考價值。TipRanks 的 AI 評等 (Neutral, $11.50) 與股價水準較接近，但屬於模型輸出。整體分析師共識 **無法可靠判定**。

---

## 2. Institutional Holdings Trend (機構持股趨勢)

### 2.1 總體指標 (major_holders)

| Metric | Value |
|---|---|
| `institutionsPercentHeld` | 82.92% |
| `institutionsFloatPercentHeld` | 85.62% |
| `institutionsCount` | 98 |
| `insidersPercentHeld` | 3.15% |

### 2.2 前十大機構持股 (inst_holders)

| Holder | Date Reported | pctHeld | Shares | pctChange (QoQ) |
|---|---|---|---|---|
| Penserra Capital Management LLC | 2026-06-30 | 32.46% | 5,081,219 | +249.9% |
| Defiance ETFs, LLC | 2026-09-30 | 32.21% | 5,041,148 | -1.14% |
| Legal & General Group PLC | 2026-09-30 | 1.84% | 287,603 | +4.23% |
| Mirae Asset Global ETFs | 2026-09-30 | 1.72% | 269,610 | +43.27% |
| UBS Group AG | 2026-09-30 | 1.69% | 264,451 | -49.42% |
| Marex Group Ltd. | 2026-09-30 | 0.92% | 144,491 | +100% |
| Kessler Investment Group | 2026-09-30 | 0.89% | 138,545 | -9.51% |
| Raymond James Financial | 2026-09-30 | 0.76% | 118,667 | +24.58% |
| Clear Street Group | 2026-09-30 | 0.71% | 111,571 | +100% |
| Van Eck Associates | 2026-09-30 | 0.58% | 91,164 | +84.22% |

註: `pctChange` 原始值為比率，已換算為百分比。Penserra 的 +249.9% 報告期為 2026-06-30，與其他 09-30 資料不同期，比較時需留意。

### 2.3 趨勢判讀

- 前十大中 **7 家增持、3 家減持**，增持者多為小型持股 (1% 以下) 的倍數增加，絕對股數變動有限。
- 持股高度集中: 前兩大 (Penserra, Defiance ETFs) 合計約 **64.7%**，前十大合計約 **73.8%**。大部分持股為 ETF 或被動/量化型結構，對短期情緒指向性較弱。
- Defiance ETFs 持股近乎持平 (-1.14%)，顯示大型結構性持有者未明顯撤退。
- 機構持股比例高 (82.9%)，但仍需注意集中度風險: 若任一大型持有者調整部位，對流動性與股價影響可能偏大。

---

## 3. Insider Transactions (內部人交易)

資料區間約 2026-04 至 2026-10。以下以「公開市場出售 (Text 含 'Sale at price')」為主要參考，無價格的條目多為歸屬、稅務扣繳或授權相關，無法從資料確認性質。

### 3.1 主要公開市場出售 (約 33 筆，估計)

| 日期 | 內部人 | 職位 | 股數 | 價格 | 金額 (USD) |
|---|---|---|---|---|---|
| 2026-10-13 | LEAVER ANDREW | CEO | 2,573 | $16.40 | 42,207 |
| 2026-10-06 | 多人 (CEO, GC, COO, Officer, Director) | - | 合計約 4,700 | $24.19 | 約 117,000 |
| 2026-10-05 | 多人 | - | 合計約 4,500 | $23.78 | 約 107,000 |
| 2026-10-02 | 多人 | - | 合計約 4,700 | $24.47 | 約 115,000 |
| 2026-07-02 | 多人 (CEO 9,893 股) | - | 合計約 14,900 | $25.20 | 約 375,000 |
| 2026-07-01 | LEFEBVRE D'OVIDIO MANFREDI (間接持有) | Director | 54,444 | $30.07-30.24 | 1,642,643 |
| 2026-06-30 | WILLCOCKS PATRICK | General Counsel | 4,000 | $29.48 | 117,920 |
| 2026-06-22 | BERS JENNIFER | Officer | 8,288 | $21.42 | 177,529 |
| 2026-04-20 | POINTON NICHOLAS | CFO | 435 | $15.87 | 6,903 |
| 2026-04-06 | LEAVER ANDREW | CEO | 7,595 | $13.51 | 102,621 |
| 2026-04-02 | 多人 (Director, GC, Officer, COO, CFO) | - | 合計約 5,900 | ~$13.3 | 約 79,000 |

### 3.2 股權轉換 / 其他 (參考)

| 日期 | 內部人 | 性質 | 股數 | 價格 |
|---|---|---|---|---|
| 2026-09-22 | LEFEBVRE D'OVIDIO MANFREDI (間接) | Conversion of derivative security | 4,600,000 | $2.50 |
| 2026-06-05 | RITCHIE GARTH | Conversion of derivative security | 73,562 | $2.50 |
| 2026-06-03 | CALABRIA CARLO | Conversion of derivative security | 120,000 | $2.50 |
| 2026-04-20 | POINTON NICHOLAS | Conversion of derivative security | 3,066 | $0.00 |

### 3.3 判讀

- **出售面廣**: CEO、CFO、GC、COO 及多位董事皆有出售紀錄，非單一人士行為。
- **出售集中於高價期**: 2026-06 至 2026-10 間多次以 $21-30 出售，最近一批 (2026-10-13) 價格已降至 $16.40。
- **出售頻率**: 2026-10 初出現多日連續出售 (10/02, 10/05, 10/06)，屬於集中性出售訊號。
- **轉換股數大**: 2026-09-22 一筆 4.6M 股以 $2.50 轉換，需確認是否隨後出售 (資料中未見對應出售)；若轉換後立即賣出，對供給壓力影響顯著。
- **資料斷點**: 資料最新為 2026-10-13，11 月內部人交易未知。
- 整體解讀: 內部人於近期股價下跌階段仍有持續出售，偏向 **負面情緒訊號**。但部分出售可能屬於既定計畫 (10b5-1) 或稅務相關，資料無法確認。

---

## 4. Retail / Social Sentiment (零售與社群情緒)

| 來源 | 情緒 / 訊號 | 備註 |
|---|---|---|
| TipRanks | Very Positive | 依平台用戶；零售持股 30 日增加 11.5%。與價格走勢相悖，樣本限於單一平台 |
| Investing.com 留言 | 多空混雜 | 匿名、未經驗證，僅反映情緒，非數據 |
| Stocktwits | 有「四個月高點」相關標題 | 頁面日期不明，無法確認時效 |
| AAII | Momentum: Very Weak | 動能評分極弱 |
| Tickeron | 技術面偏空 | MACD、Aroon 於 11 月中轉負；RSI 顯示超賣，可能有短線反彈 |
| 新聞面 | 遺失中東合約 | 下半年營收下滑，影響市場信心 |

### 4.1 價格背景

- 2026-11-18 約 $12.75，當日 +3%，但 11 月累計約 -19%。
- 11 月區間: 高 $17.68 / 低 $11.72。
- 52 週區間: $11.52 - $62.00。
- 外部搜尋中部分價格快照 (13.57, 24.315) 互相矛盾，時間戳不明，**不採用**。

### 4.2 判讀

- 零售情緒 (TipRanks Very Positive, 零售持股增加) 與 **價格動能 (Very Weak, 技術面偏空)** 出現背離。
- 零售增持若發生在股價下跌中，可能屬於逢低承接，但也可能是投機性接盤；此資料無法區分。
- 社群情緒整體 **中性偏弱**，無明顯極端情緒 (無法判斷是否有逆向指標意義)。

---

## 5. Composite Judgment (綜合判斷)

評分尺度: -2 (極度負面) 至 +2 (極度正面)；0 為中性。信心: 高 / 中 / 低。

| 維度 | 關鍵依據 | 分數 | 權重 | 信心 |
|---|---|---|---|---|
| Analyst consensus | 僅見過時 Buy ($60)、AI Neutral ($11.50)，無近期券商評等 | 0 | 15% | 低 |
| Institutional holdings trend | 82.9% 機構持股，7 增 3 減，但前兩大持股占 64.7% | 0 | 20% | 中 |
| Insider transactions | 廣泛公開市場出售，2026-10 仍有出售，價格由 $30 降至 $16 | -1 | 30% | 中 |
| Retail / social sentiment | TipRanks Very Positive 與價格背離，社群多空混雜 | 0 | 15% | 低 |
| Price momentum (technical, from web) | AAII Very Weak，Tickeron 偏空，11 月跌約 19% | -1 | 20% | 中 |
| **Composite (加權)** | | **約 -0.5** | 100% | **低-中** |

**綜合判斷: 中性偏空 (Neutral to Bearish)**

- 主要負面因素: 內部人持續出售、動能偏弱、基本面利空 (遺失合約、營收下滑)。
- 主要正面因素: 機構持股比例高、部分機構增持、零售平台情緒偏正面。
- 資料缺口: 分析師共識不可靠、insider 資料止於 10 月、無 11 月持股與做空比率資料。信心因此僅為 **低-中**。
- 本報告僅為情緒面分析，不構成買賣建議；應與基本面、技術面及風控報告合併判斷。

---

## 6. 資料限制與後續建議

1. yfinance 的 `rec_summary` 與 `recommendations` 回傳空值，建議以付費終端機 (如 Bloomberg, FactSet) 核對分析師評等。
2. insider 資料止於 2026-10-13，建議於 SEC EDGAR Form 4 補查 10 月下旬至 11 月的交易。
3. institutional 資料為季報落後資料，建議補查 13F 最新申報與 short interest。
4. 外部價格來源互相矛盾，正式分析前應以單一可靠行情來源確認價格。

---

## 參考來源 (WebSearch)

- https://www.aaii.com/investingideas/article/543344-why-arqit-quantum-inc8217s-arqq-stock-is-up-504
- https://kr.benzinga.com/quote/ARQQ/sentiment
- https://www.tipranks.com/stocks/arqq/stock-investors
- https://www.tipranks.com/stocks/ARQQ/stock-analysis
- https://in.tradingview.com/symbols/ARQQ
- https://stocktwits.com/symbol/ARQQ
- https://tickeron.com/earnings/ARQQ/
- https://www.benzinga.com/quote/ARQQ/analyst-ratings
- https://www.zacks.com/stock/research/ARQQ/price-target-stock-forecast
- https://za.investing.com/equities/centricus-acquisition-consensus-estimates
