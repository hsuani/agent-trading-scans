# IBM 市場情緒分析 (Sentiment Analysis)

- 標的 (Ticker): IBM
- 報告日期 (Report date): 2026-11-24
- 資料基準日 (Data as of): 2026-11-23（工具回傳的最新資料，部分為 2026-09-30 季末 13F 或 2026-10 月社群資料）
- 資料來源: `pipeline/tools/yf.py`（rec_summary、recommendations、major_holders、inst_holders、insider）、WebSearch（分析師動態、散戶/社群情緒）
- 注意: yfinance 的 cookie/crumb 取得失敗（ConnectionError），但資料仍有回傳；目前沒有 2026-11 月的社群情緒原始資料。

---

## 1. 分析師共識 (Analyst Consensus)

### 1.1 評等分布 (Recommendation Distribution, 25 家)

| 期間 (Period) | strongBuy | buy | hold | sell | strongSell | Buy 側占比 | Mean Score (1=強買 ~ 5=強賣) |
|---|---|---|---|---|---|---|---|
| 0m（當期） | 3 | 9 | 11 | 1 | 1 | 48% (12/25) | 2.52 |
| -1m | 3 | 9 | 11 | 1 | 1 | 48% (12/25) | 2.52 |
| -2m | 3 | 9 | 10 | 1 | 1 | 48% (12/25) | 2.48 |
| -3m | 3 | 10 | 10 | 1 | 1 | 52% (13/25) | 2.48 |

觀察:
- 買方評等 (Buy-side) 由 13 家降為 12 家，持有 (hold) 由 10 家增為 11 家，評等略微降溫，但幅度很小。
- Mean Score 由 2.48 微升至 2.52，仍屬「Buy 與 Hold 之間」，整體偏中性偏多。
- `rec_summary` 與 `recommendations` 回傳的數值完全一致。

### 1.2 目標價 (Price Target, 來自 WebSearch，需人工核對)

| 指標 | 數值 | 備註 |
|---|---|---|
| 平均目標價 (Average Target) | 約 $257（Yahoo, 1y Target Est 257.22）至 $315（stockanalysis.com） | 各來源差異大 |
| 目標價區間 | $174 至 $300（單一追蹤來源） | 與上方 $315 平均值不一致，分散度高 |
| 近期調整 | Jefferies 270→280（Buy）、Citi 245→280（Buy）、Barclays 262→277（Overweight）、DZ Bank Buy $295 | 多數為 2026 年 10 月後的調整 |
| 2026-11-19 | Evercore ISI 重申 Outperform，目標價 $315 | 來自搜尋摘要，未在原始頁面核實 |

股價 (Price): 搜尋摘要顯示約 $247–$253，各來源不一致，請以即時報價為準。

---

## 2. 機構持股趨勢 (Institutional Holdings Trend)

### 2.1 持股概況 (`major_holders`)

| 指標 | 數值 |
|---|---|
| insidersPercentHeld | 0.16% |
| institutionsPercentHeld | 64.60% |
| institutionsFloatPercentHeld | 64.71% |
| institutionsCount | 4,294 |

### 2.2 前十大機構 (`inst_holders`, 報告日 2026-09-30)

| 機構 (Holder) | 持股比例 (pctHeld) | 持股數 (Shares) | 季度變動 (pctChange) |
|---|---|---|---|
| BlackRock Inc. | 8.04% | 75,972,691 | -1.03% |
| Vanguard Capital Management LLC | 6.52% | 61,668,152 | +0.46% |
| State Street Corporation | 5.91% | 55,859,074 | -0.33% |
| Vanguard Portfolio Management LLC | 3.01% | 28,494,218 | +0.51% |
| Geode Capital Management, LLC | 2.53% | 23,948,239 | +2.13% |
| Morgan Stanley | 1.79% | 16,929,285 | -3.04% |
| Bank of America Corporation | 1.66% | 15,699,618 | +4.75% |
| Capital World Investors | 1.16% | 10,939,006 | **-32.51%** |
| JPMorgan Chase & Co | 1.13% | 10,708,997 | -13.95% |
| Northern Trust Corporation | 1.00% | 9,444,636 | -7.66% |

觀察:
- 前十大合計約 32.75%，集中度穩定，屬指數型與被動型資金為主。
- 10 家中 4 家增持、6 家減持。最顯著的是 Capital World Investors 大幅減持 (-32.5%)，JPMorgan 與 Northern Trust 亦減持。
- 機構總持股率 64.6%，屬高持股，結構性支撐穩定；但主動型資金的邊際方向偏負向。
- 資料為 2026-09-30 季末數字，屬較舊的 13F 快照，請勿視為 11 月的即時部位。

---

## 3. 內部人交易 (Insider Transactions, `insider`)

### 3.1 公開市場交易 (Open-market Purchases / Sales)

| 日期 | 內部人 (Insider) | 職位 | 類型 | 股數 | 價格 | 金額 (約) |
|---|---|---|---|---|---|---|
| 2026-08-26 | THOMAS ROBERT DAVID | Officer | **Sale** | 25,000 | $230.32 | $5.76M |
| 2026-02-25 | HOWARD MICHELLE J. | Director | Purchase | 50 | $237.83 | $11.9K |
| 2026-02-25 | MIEBACH MICHAEL | Director | Purchase | 434 | $233.33 | $101K |
| 2026-01-30 | FARR DAVID N | Director | Purchase | 1,000 | $304.00 | $304K |
| 2025-03-03 | THOMAS ROBERT DAVID | Officer | Sale | 26,543 | $253.01 | $6.72M（超過一年，僅供參考） |
| 2025-02-28 | FARR DAVID N | Director | Purchase | 1,200 | $249.00 | $299K（超過一年，僅供參考） |

### 3.2 近 12 個月彙總（2025-11-24 至 2026-11-23）

- 公開市場賣出: 1 筆，25,000 股，約 $5.76M（THOMAS ROBERT DAVID，2026-08-26）
- 公開市場買入: 3 筆，約 1,484 股，約 $0.41M（FARR、MIEBACH、HOWARD）
- 淨方向: 金額上明顯為淨賣出；但 FARR 的 $304 買進目前已處於虧損。
- 其他: 多筆 `Stock Award(Grant)`（2026-01-30 為主）、`Stock Gift`、以及 `Value` 為空的 vesting/withholding 類紀錄。這些非公開市場買賣，判讀時應排除，且 null 值交易的性質未經驗證。

觀察: 內部人近期以 Officer 的賣出為主，Director 端則有小額買入。金額與訊號強度有限，較像例行性出售與獎勵，但仍應列為負向因子。

---

## 4. 散戶與社群情緒 (Retail / Social Sentiment, WebSearch)

| 面向 | 觀察 | 時間 |
|---|---|---|
| Stocktwits | 情緒於 2026-10-22 前後轉為 Bullish，後升至 "extremely bullish"；訊息量單週暴增約 1,600% | 2026-10 |
| Stocktwits 股價 | YTD 約下跌 14%（同期報導） | 2026-10 |
| Reddit | 情緒兩極，2 月時於 48 小時內由 88（非常看多）翻至 32（看空） | 2026-02 |
| Reddit 主題 | 正面: IBM 對 AI 的策略較克制、不燒錢；負面: AI 基礎設施風險 | 近期 |
| Axios | 報導 IBM 成為散戶熱炒的「迷因股」，散戶關注度上升 | 2026-06 |

觀察:
- 散戶情緒近期偏多，但資料多為 2026-10 以前，**沒有 2026-11 的可驗證數據**，時效性不足約一個月。
- 散戶情緒與機構/內部人訊號方向不一致（散戶偏多、內部人淨賣），波動性偏高。
- 不同平台的情緒指標尺度不同，無法直接比較。

---

## 5. 綜合判斷 (Composite Judgment)

評分尺度: -2（強烈看空）至 +2（強烈看多），0 為中性。

| 面向 | 分數 | 依據 | 信心 |
|---|---|---|---|
| analyst consensus | +1 | 買方占比約 48%，hold 略增，mean score 約 2.5；目標價多數高於現價 | 中（目標價來源分歧大） |
| institutional holdings | 0 | 持股率 64.6%、結構穩定；前十大 4 增 6 減，Capital World 大減 | 中（資料為 9 月底快照） |
| insider transactions | -1 | 近 12 個月公開市場淨賣出約 $5.4M，買入金額小 | 中高（樣本少，多為 Officer 出售） |
| retail / social sentiment | +1 | 2026-10 轉為 Bullish，訊息量暴增 | 低（資料過時，波動大） |
| **綜合 (Composite)** | **+0.25** | 平均約 +0.25，判定為「中性偏多」 | **低至中** |

### 判斷摘要

- 整體情緒: **中性偏多 (Neutral-to-slightly-bullish)**。分析師評等與散戶情緒偏多，機構持股穩定；內部人公開市場淨賣出與機構部分減持構成主要反向力量。
- 主要風險: 內部人賣出、機構減持、目標價分歧大、社群資料過時。
- 資料缺口: 無 2026-11 月的社群情緒資料；股價來源不一致；13F 為 9 月底快照；Evercore 11/19 評等未經原始頁面核實。
- 建議使用方式: 此為情緒輸入，僅供與基本面、技術面、新聞面交叉比對，不構成單獨的交易建議。

---

## 來源 (Sources)

- yfinance 資料: `pipeline/tools/yf.py IBM {rec_summary, recommendations, major_holders, inst_holders, insider}`
- WebSearch 結果（已列於相關段落，未逐一核實原頁面）:
  - Stocktwits 系列報導（2026-10）: stocktwits.com 之 IBM 相關文章
  - Axios, "Guess who's a meme stock now? IBM" (2026-06-02): https://axios.com/2026/06/02/ibm-meme-stock-trump
  - Yahoo Finance, Analysts / Price Target 頁面: https://finance.yahoo.com/quote/ibm/analysts
  - stockanalysis.com 評等頁: https://stockanalysis.com/stocks/ibm/ratings/
