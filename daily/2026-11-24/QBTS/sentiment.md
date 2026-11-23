# QBTS 情緒分析報告 (Sentiment Analysis)

- Ticker: QBTS (D-Wave Quantum Inc.)
- 報告日期: 2026-11-24
- 資料來源: `pipeline/tools/yf.py` (rec_summary / recommendations / major_holders / inst_holders / insider, `source: cache`)、WebSearch (retail / social sentiment)
- 資料時效注意: Yahoo cookie/crumb 取得失敗，資料為快取。機構持股以 2026-09-30 申報為準，內部人交易最後一筆為 2026-09-18，散戶情緒最新可得讀數未明確標示日期。

---

## 1. Analyst Consensus (分析師共識)

### 1.1 Current Rating Distribution (`rec_summary`, period 0m)

| Rating | Count |
|---|---|
| strongBuy | 1 |
| buy | 13 |
| hold | 3 |
| sell | 0 |
| strongSell | 0 |
| **Total** | **17** |

- Buy + strongBuy 佔比: 82.4% (14 / 17)
- 以 1-5 分制 (5=strongBuy, 1=strongSell) 計算的 mean rating: **3.88**

### 1.2 Trend (近 4 個月)

| Period | strongBuy | buy | hold | sell | strongSell | Mean Rating |
|---|---|---|---|---|---|---|
| 0m (current) | 1 | 13 | 3 | 0 | 0 | 3.88 |
| -1m | 1 | 14 | 2 | 0 | 0 | 3.94 |
| -2m | 1 | 14 | 2 | 0 | 0 | 3.94 |
| -3m | 1 | 15 | 1 | 0 | 0 | 4.00 |

**解讀**: 評級結構仍以 Buy 為主，且沒有任何 Sell 評級。但過去三個月 buy 由 15 降至 13，hold 由 1 升至 3，mean rating 由 4.00 微降至 3.88。方向為輕微降溫，未出現評級下調集中現象。

`recommendations` 與 `rec_summary` 回傳資料一致，未發現額外資訊。

---

## 2. Institutional Holdings Trend (機構持股趨勢)

### 2.1 Ownership Summary (`major_holders`)

| Metric | Value |
|---|---|
| insidersPercentHeld | 2.19% |
| institutionsPercentHeld | 54.81% |
| institutionsFloatPercentHeld | 56.04% |
| institutionsCount | 699 |

### 2.2 Top 10 Institutional Holders (`inst_holders`, 申報日 2026-09-30，除 NORGES BANK 為 2026-06-30)

| Holder | % Held | Shares | pctChange (原始欄位) | 方向 |
|---|---|---|---|---|
| Blackrock Inc. | 8.57% | 31,415,921 | -5.22% | 減持 |
| Vanguard Portfolio Management LLC | 5.98% | 21,920,294 | -0.46% | 持平偏減 |
| Vanguard Capital Management LLC | 4.52% | 16,587,163 | +4.06% | 增持 |
| UBS Group AG | 3.02% | 11,093,100 | -4.75% | 減持 |
| Geode Capital Management, LLC | 2.59% | 9,515,043 | +2.64% | 增持 |
| State Street Corporation | 2.49% | 9,141,711 | +1.24% | 增持 |
| NORGES BANK | 1.22% | 4,477,459 | 27.16 (單位待確認) | 大幅增持 |
| Van Eck Associates Corporation | 1.13% | 4,144,161 | +77.12% | 增持 |
| Goldman Sachs Group Inc | 1.01% | 3,696,003 | +37.84% | 增持 |
| Bank of America Corporation | 0.99% | 3,637,548 | -16.24% | 減持 |

**解讀**:
- 前十大機構中增持者 6 家、減持者 4 家，淨方向偏中性。
- 指數型基金 (Vanguard, Geode, State Street) 多為被動配置，增減幅度反映資金流而非主動看法。
- 主動型或量化資金 (Van Eck, Goldman, Norges) 增持幅度較大，屬於較正面訊號，但絕對持股比例仍小。
- 最大持有人 BlackRock 持續減持 (-5.2%)，需留意。
- 機構持股比例 54.8%、機構數 699 家，結構上仍屬機構參與度中高。

---

## 3. Insider Transactions (內部人交易)

資料區間: 約 2024-12 至 2026-09。以下統計以 **2025-11-24 至 2026-09-18** 為近 12 個月區間 (最後交易日為 2026-09-18)。

### 3.1 Summary (近 12 個月)

| Metric | Value |
|---|---|
| Open-market 買入 (Purchase) | **0 筆** (僅 2025-11-18 WEST STEVEN M. 買入 82 股，區間外且金額極小) |
| Open-market 賣出 (Sale) 筆數 | 約 33 筆 |
| 賣出總金額 (估算) | **約 USD 72.7M** |
| 主要賣方 | CEO BARATZ ALAN E、CFO MARKOVICH JOHN M、GC NGUYEN DIANE、Director GHAI ROHIT / DILULLO JOHN DAVID |
| 股票授予 (Stock Award) | 多筆，屬例行薪酬，不計入買賣判斷 |

### 3.2 Major Sales (金額 > USD 1M)

| Date | Insider | Role | Shares | Price | Value (USD) |
|---|---|---|---|---|---|
| 2025-12-22 | BARATZ ALAN E | CEO | 793,712 | 30.13 | ~23.9M |
| 2025-12-22 | MARKOVICH JOHN M | CFO | 100,000 | 30.03 | ~3.0M |
| 2025-12-04 | MARKOVICH JOHN M | CFO | 200,000 | 25.05-27.56 | ~5.3M |
| 2026-01-14 | BARATZ ALAN E | CEO | 35,013 | 28.06 | ~1.0M |
| 2026-05-21 | NGUYEN DIANE | GC | 40,000 | 25.01 | ~1.0M |
| 2026-05-22 | MARKOVICH JOHN M | CFO | 328,752 | 27.70 | ~9.1M |
| 2026-06-08 | BARATZ ALAN E | CEO | 687,627 | 26.13 | ~18.0M |
| 2026-06-15 | MARKOVICH JOHN M | CFO | 246,043 | 24.01-25.75 | ~6.2M |

### 3.3 Context

- **Option-exercise 相關**: 多筆賣出與 "Conversion of Exercise of derivative security" (執行價約 0.85-0.92) 成對出現，顯示部分為 **行使選擇權後賣出**，獲利實現性質，不完全代表對股價的悲觀看法。CEO 與 CFO 的大額賣出多屬此類。
- **交易頻率**: 2026-06 為單月賣出最密集的月份，之後至 2026-09 僅零星小額交易。
- **Director 交易**: 多為小額，且部分為 stock award 或 gift。
- **>10% holder (PSPIB)**: 大額賣出集中於 2024-12 至 2025-01 (區間外)，目前無近期申報。

### 3.4 Interpretation

- 內部人 **無公開市場買入**，近 12 個月淨賣出規模大。
- 扣除選擇權行使的機械性成分後，仍有大額獲利了結，是偏負面的訊號。
- 2.19% 內部人持股比例偏低，持股與股價連動性有限。

---

## 4. Retail / Social Sentiment (散戶與社群情緒)

### 4.1 Findings

- **AltIndex 綜合情緒分數**: 66/100，標示為 bullish。資料來源為 Reddit、Stocktwits 與其他論壇 NLP 分析。目前讀數低於 30 日均值，顯示情緒正在降溫。月度序列至 2026-09 為 82，表示 2026-09 之後明顯回落。頁面未標示 66 分的取樣日期。
- **Stocktwits 歷史快照 (2025 年為主)**: 散戶意向在 "bearish" 與 "extremely bullish" 之間大幅擺動。曾出現 "extremely bullish" (86/100) 搭配 "extremely high" 討論量的時點，也有 "bearish" (36/100) 的時點。
- **散戶偏好**: Stocktwits 多次調查中，QBTS 在量子運算股中常被列為散戶首選，相對 RGTI、IONQ、QUBT 聲量較高。
- **質疑聲音**: 部分用戶認為此類股價漲幅由 Reddit / meme 資金推動，將其視為賣出訊號。

### 4.2 Limitations

- 搜尋未找到 **2026-11 當月** 的散戶情緒數據，目前引用的多為 2025 年快照與 AltIndex 的非當日讀數。
- 散戶情緒對 QBTS 這類高 beta 動能股的領先性不穩定，情緒高點常與股價高點重合。

---

## 5. Composite Judgment (綜合判斷)

| Dimension | Signal | Score (-2 ~ +2) | Weight | 主要依據 |
|---|---|---|---|---|
| Analyst Consensus | 偏多 (Buy 佔 82%) | +1 | 30% | mean 3.88，無 Sell；但近三月 Buy 減少、Hold 增加 |
| Institutional Holdings | 中性 | 0 | 20% | 機構持股 54.8%；前十大增減互見，BlackRock 減持、Van Eck / Goldman / Norges 增持 |
| Insider Transactions | 偏空 | -1 | 30% | 近 12 個月淨賣出約 USD 72.7M，無公開買入；部分為選擇權行使 |
| Retail / Social | 偏多但降溫 | +0.5 | 20% | AltIndex 66 分，低於 30 日均值；資料時效不足 |

**加權綜合分數**: 0.30 × 1 + 0.20 × 0 + 0.30 × (-1) + 0.20 × 0.5 = **+0.10** (範圍 -2 ~ +2)

| 綜合判斷 | 結果 |
|---|---|
| **總體情緒** | **中性 (Neutral)**，略偏謹慎 |
| 方向趨勢 | 分析師與散戶情緒均輕微降溫，內部人賣出為主要負面因子 |
| 信心程度 | **中低** (快取資料、機構資料為 9 月申報、散戶情緒缺乏 11 月實際讀數) |

### 關鍵觀察

1. **分析師仍多數看多，但評級結構正在緩慢鬆動** (Buy 由 15 降至 13，Hold 由 1 升至 3)。
2. **內部人大規模賣出是主要風險**，尤其 CEO / CFO 在 2025-12 與 2026-06 的集中出售。
3. **機構持股結構中性**，增減互見，無明顯資金撤離或大規模流入訊號。
4. **散戶情緒為高波動動能屬性**，目前降溫，但資料未涵蓋 11 月當下情況，需以即時數據補充。

### 建議後續動作

- 更新 `yf.py` 快取 (恢復 Yahoo cookie/crumb 連線) 以取得最新 insider 與 holders 資料。
- 於交易前取得 2026-11 當月 Stocktwits / Reddit 即時情緒讀數，驗證散戶訊號。

---

## Sources

- [AltIndex - QBTS Sentiment](https://altindex.com/ticker/qbts/sentiment)
- [Stocktwits - We Asked Retail Traders Their Top Quantum Stock](https://stocktwits.com/news-articles/markets/equity/qbts-is-retail-favorite-among-quantum-computing-stocks/ch7WtHvRbTV)
- [Stocktwits - Majority of retail investors anticipate rebound in quantum computing stocks](https://stocktwits.com/news-articles/markets/equity/majority-of-retail-investors-on-stocktwits-anticipate-rebound-in-quantum-computing-stocks/chGqNe5RV0)
