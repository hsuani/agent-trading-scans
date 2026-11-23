# IONQ 情緒分析報告

- 股票代碼：IONQ（IonQ, Inc.）
- 分析日期：2026-11-24
- 資料來源：yfinance（`pipeline/tools/yf.py`）、WebSearch（Stocktwits、AltIndex、Motley Fool、Yahoo Finance 等）
- 注意：本次 yfinance 呼叫出現 `Cookie/crumb fetch failed` 警告，部分資料可能來自快取（`source: cache`），但內容完整可用。

---

## 1. 分析師共識（Analyst Consensus）

### 1.1 評等分布（`rec_summary` / `recommendations`）

| 期間 | strongBuy | buy | hold | sell | strongSell | 合計 | Buy 比重 |
|------|-----------|-----|------|------|------------|------|----------|
| 0m（本期） | 1 | 11 | 2 | 0 | 0 | 14 | 85.7% |
| -1m | 1 | 11 | 2 | 0 | 0 | 14 | 85.7% |
| -2m | 1 | 11 | 2 | 0 | 0 | 14 | 85.7% |
| -3m | 1 | 10 | 2 | 0 | 0 | 13 | 84.6% |

### 1.2 解讀

- 14 位分析師中有 12 位給予 Buy 或 Strong Buy，無任何 Sell 或 Strong Sell 評等。
- 過去三個月評等結構穩定，僅在 -3m 至 -2m 之間新增一個 Buy，屬於小幅上修。
- 共識明顯偏多，但 **高度一致的評等也常見於高波動的概念股**，不代表短期價格方向。

---

## 2. 機構持股趨勢（Institutional Holdings）

### 2.1 整體持股（`major_holders`）

| 指標 | 數值 |
|------|------|
| insidersPercentHeld | 0.62% |
| institutionsPercentHeld | 41.42% |
| institutionsFloatPercentHeld | 41.68% |
| institutionsCount | 1,009 |

### 2.2 前十大機構（`inst_holders`，多數為 2026-09-30 申報）

| 機構 | 持股比例 | 持股股數 | 季度股數變化（pctChange） | 申報日 |
|------|----------|----------|---------------------------|--------|
| Morgan Stanley | 5.98% | 25,868,100 | -1.57% | 2026-09-30 |
| BlackRock Inc. | 4.39% | 18,970,416 | -9.22% | 2026-09-30 |
| Vanguard Capital Management LLC | 4.15% | 17,946,984 | +15.06% | 2026-09-30 |
| Vanguard Portfolio Management LLC | 3.58% | 15,465,394 | +10.79% | 2026-09-30 |
| State Street Corporation | 2.04% | 8,804,339 | +8.38% | 2026-09-30 |
| Bank of America Corporation | 1.95% | 8,416,561 | +30.02% | 2026-09-30 |
| Geode Capital Management, LLC | 1.54% | 6,662,722 | +3.14% | 2026-09-30 |
| UBS Group AG | 1.38% | 5,973,252 | -24.36% | 2026-09-30 |
| NORGES BANK | 1.20% | 5,188,962 | +16.56% | 2026-06-30 |
| Goldman Sachs Group Inc | 0.75% | 3,259,096 | +82.11% | 2026-09-30 |

### 2.3 解讀

- 前十大機構中 **7 家增持、3 家減持**（減持者為 BlackRock、UBS、Morgan Stanley 小幅減碼）。
- 增持幅度較大者為 Goldman Sachs（+82%）與 Bank of America（+30%），屬於較明確的加碼訊號，但其絕對持股比例仍小。
- 機構持股約 41%，屬中等水準；內部人持股僅約 0.6%，對股權結構影響有限。
- 注意：`pctChange` 為季度間股數變化，不代表買賣金額或成本。

---

## 3. 內部人交易（Insider Transactions，`insider`）

### 3.1 近 12 個月（2025-11-24 至 2026-11-23）重要交易

| 日期 | 內部人 | 職位 | 類型 | 股數 | 單價（約） | 金額（約） |
|------|--------|------|------|------|------------|------------|
| 2025-11-11 | Teuber William J Jr | Director | 公開市場買入 | 2,000 | $54.82 | $110K |
| 2025-12-11 | Chou Kathryn K | Director | 行使選擇權後賣出 | 20,000 | $51.40 | $1.03M |
| 2025-12-22 | Chou Kathryn K | Director | 賣出 | 5,000 | $55.00 | $275K |
| 2026-02-24 | Toledano Gabrielle B | Director | 賣出 | 616 | $31.00 | $19K |
| 2026-02-26 | Cardillo Robert Thomas | Director | 賣出 | 5,165 | $39.44 | $204K |
| 2026-02-27 | Teuber William J Jr | Director | 公開市場買入 | 3,000 | $38.38 | $115K |
| 2026-03-12 | Raymond John W. | Director | 賣出 | 2,800 | $33.34 | $93K |
| 2026-04-16 | Cardillo Robert Thomas | Director | 賣出 | 2,500 | $44.90 | $112K |
| 2026-05-06 | Cardillo Robert Thomas | Director | 賣出 | 3,773 | $49.90 | $188K |
| 2026-06-18 | Toledano Gabrielle B | Director | 賣出 | 2,757 | $55.01 | $152K |
| 2026-06-18 | Chou Kathryn K | Director | 賣出 | 2,757 | $55.02 | $152K |
| 2026-06-18 | Raymond John W. | Director | 賣出 | 3,815 | $55.01 | $210K |
| 2026-09-10 | Raymond John W. | Director | 賣出 | 2,407 | $37.21 | $90K |

另有多筆例行性 **Stock Award（股票獎勵）**，主要為董事會成員年度授予（2026-06-17、2026-08-24）以及 CEO De Masi Niccolo M 與 COO Singh Inder M. 於 2026-02-20 的獎勵，屬於薪酬性質，非市場判斷訊號。

### 3.2 彙總

| 項目 | 筆數 | 金額（約） |
|------|------|------------|
| 公開市場賣出（Sale，近 12 個月） | 11 筆 | 約 $2.52M |
| 公開市場買入（Purchase，近 12 個月） | 2 筆（皆為 Director Teuber） | 約 $225K |
| 淨買賣（買入 − 賣出） | — | 約 −$2.30M |

### 3.3 解讀

- 近 12 個月 **以賣出為主**，賣出者多為董事（Chou、Cardillo、Raymond、Toledano），且 2026-06-18 出現多位董事在約 $55 同日賣出，屬較集中的獲利了結行為。
- 唯一的公開市場買入為董事 Teuber，兩次合計約 $225K，金額小但方向相反。
- **CEO De Masi 與 CFO Kramer 在近 12 個月內無公開市場賣出紀錄**（僅有獎勵股），這一點屬於相對中性訊號。
- 部分賣出搭配選擇權行使（`Conversion of Exercise` 於 $4.61 或 $11.24 等低行權價），實際獲利比賣出價所示更高，但不代表內部人看空。
- 整體判讀：**內部人情緒偏負（偏向獲利了結）**，但規模相對 IONQ 總市值仍屬小額。

---

## 4. 散戶與社群情緒（Retail / Social Sentiment，WebSearch）

| 來源 | 指標 | 讀數 | 時間 | 可信度 |
|------|------|------|------|--------|
| AltIndex（Stocktwits 提及量） | 日均提及數 | 379 則/日，較三個月前下降 53% | 未註明 | 中 |
| AltIndex（Stocktwits 情緒分數） | Sentiment score | 88 / 100（Bullish） | 未註明 | 低（無日期） |
| AltIndex（X cashtag） | X sentiment score | 91 / 100（Bullish） | 未註明 | 低（無日期） |
| AltIndex（X cashtag 月提及數） | 月提及數 | 2026-01: 152；02: 336；03: 71；04: 77；05: 219 | 2026 年 1–5 月 | 中 |
| Stocktwits 報導 | 近期情緒 | 轉為 Bearish，因 $1.3B 全股票收購 Elisity 宣布後股價下跌 | 約 6 週前（相對日期） | 中 |
| Stocktwits 報導 | 早期情緒 | Neutral，訊息量高 | 約 2 個月前（相對日期） | 中 |
| Stocktwits 報導 | 更早情緒 | Extremely bullish，訊息量極高 | 約 4 個月前（相對日期） | 中 |
| Motley Fool | 2026-11-19 股價大漲 | 受 IonQ 於 SC26 超級電腦大會（芝加哥）期間發出的 X 貼文帶動 | 2026-11-19 | 中高（有明確日期） |
| Yahoo Finance | Reddit 情緒 | 2026-02 底 Reddit 貼文使情緒短暫極度看多，隨後迅速消退 | 2026-02 | 中 |
| Yahoo Finance / Barchart | 空單比例 | Short interest 約 22.4% of float，論者認為可能推動軋空 | 未註明 | 低（偏宣傳語氣） |

### 4.1 解讀

- **聲量下降**：Stocktwits 日均提及數較三個月前減半，顯示散戶關注度降溫，但 AltIndex 的情緒分數仍為 Bullish。
- **情緒來回擺盪**：從 Bullish 到 Neutral 再到 Bearish，多次因財報、收購案與催化劑事件而快速轉向，缺乏持續性。
- **近期催化劑為正面**：2026-11-19 的 SC26 相關 X 貼文帶動股價上漲，顯示社群對公司發布內容的反應仍然強烈。
- **軋空題材**：空單比例約 22.4%，是散戶與媒體常用的敘事，但屬於技術與籌碼面議題，不代表基本面改善。
- **資料限制**：多數社群指標缺乏明確日期，且 WebSearch 未回傳 2026-11 的 Reddit 或 Stocktwits 即時讀數，因此本節為 **趨勢性判斷**，而非當日精確數據。

---

## 5. 綜合情緒判斷（Composite Sentiment Judgment）

評分範圍：**-2（極度看空）至 +2（極度看多）**

| 構面 | 權重 | 分數 | 理由 |
|------|------|------|------|
| 分析師共識（Analyst Consensus） | 30% | +1.5 | 12/14 為 Buy 以上，無 Sell，結構穩定 |
| 機構持股趨勢（Institutional Holdings） | 20% | +0.5 | 前十大 7 增 3 減；Goldman、BofA 明顯加碼，但 UBS、BlackRock 減碼 |
| 內部人交易（Insider Transactions） | 20% | -1.0 | 近 12 個月淨賣出約 $2.3M，僅董事 Teuber 有買入；CEO/CFO 無公開市場賣出 |
| 散戶與社群情緒（Retail / Social） | 20% | +0.5 | 情緒分數偏多，但提及量下降且讀數多數無日期，波動大 |
| 催化劑與籌碼面（Catalyst / Positioning） | 10% | +0.5 | 2026-11-19 SC26 相關上漲；空單比例高（約 22.4%）帶來軋空潛力，但缺乏基本面支撐 |
| **加權綜合分數** | 100% | **約 +0.4** | — |

### 5.1 綜合判斷

- **整體情緒：中性偏多（Mildly Bullish），信心度低。**
- 分析師與機構面偏多，但內部人賣出與散戶情緒的高波動性形成抵銷。
- 散戶與社群情緒（Stocktwits / X）偏多，但聲量下降、讀數多無日期，且過去 6 個月內曾多次在看多與看空之間快速轉換，**不宜作為單一進場依據**。
- 若要把此情緒結論納入後續流程（bull/bear 辯論、trader 決策），建議：
  1. 以分析師共識作為方向性參考，但須搭配估值與基本面分析。
  2. 將內部人淨賣出視為風險因子，特別是董事集中在 $55 附近賣出的紀錄。
  3. 將社群情緒視為短期波動來源，而非中長期趨勢指標。
  4. 留意空單比例高所帶來的軋空風險與反轉風險。

### 5.2 風險提示

- 本報告使用的部分社群數據（AltIndex、Stocktwits 相對日期）時效性不足，應視為趨勢參考。
- 本次 WebSearch 未取得 2026-11-20 至 2026-11-24 之間的即時情緒資料，也未取得 IONQ 最新收盤價，因此**無法確認當前估值位置**。
- 本報告僅為情緒分析，不構成投資建議。

---

## 6. 資料來源

- yfinance：`python3 pipeline/tools/yf.py IONQ rec_summary | recommendations | major_holders | inst_holders | insider`
- WebSearch：
  - Stocktwits：IonQ 相關報導（Elisity 收購、SDT 合作、RGTI/QBTS/INFQ/IONQ 比較等）
  - AltIndex：`altindex.com/ticker/ionq/stocktwits-mentions`、`altindex.com/ticker/ionq/x-mentions`
  - Motley Fool：`fool.com/investing/2026/11/19/why-ionq-stock-popped-today`
  - Yahoo Finance：`IonQ Tripled Revenue but Its Stock Is Down 22%`、`federal backing triggered rally ionq`
  - Barchart：`federal backing triggered a rally in ionq stock a short squeeze could take it even higher`
