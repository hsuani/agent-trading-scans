# Sentiment — CBRS as of 2026-10-26

> 資料時效說明：yf 的報價時戳約為 2026-10-24（UTC），為最近一次可得報價；分析師分布為目前快照。Reddit / StockTwits 直接抓取依指示未執行，零售情緒僅能以 WebSearch 摘要補充，且多數來源停留在 2026 年 8 月至 9 月。2026-10-26 之後的資料一律視為未知。

## Analyst consensus

目前分布（rec_summary，0m 快照）：**11 buy / 0 hold / 0 sell**（其中 strongBuy 3、buy 8）。

| 期間 | strongBuy | buy | hold | sell | strongSell |
|---|---|---|---|---|---|
| 0m（目前） | 3 | 8 | 0 | 0 | 0 |
| -1m | 3 | 7 | 1 | 0 | 0 |
| -2m | 3 | 7 | 1 | 0 | 0 |
| -3m | 3 | 7 | 1 | 0 | 0 |

- 近一個月的變化：唯一一名 hold 評等轉為 buy 或被移除，無 sell 出現，整體評等朝樂觀方向收斂。
- 個別券商升降評、逐筆評等日期：DATA_UNAVAILABLE（yf recommendations 只回傳彙總分布，未含逐家機構事件）。
- 目標價：info 顯示 mean $282.55 / median $300 / high $330 / low $175（共 11 家分析師）。以目前價 $110.82 計算，mean 隱含約 +155% 上行空間。目標價的歷史修正軌跡：DATA_UNAVAILABLE。
- recommendationMean 1.27（1 = 強烈買進，5 = 強烈賣出），屬高度一致的買方共識。

## Retail social

- **Reddit（r/wallstreetbets、r/stocks）**：直接抓取依指示未執行，當前貼文與多空比例 DATA_UNAVAILABLE。
  - 間接指標（AltIndex，WebSearch 摘要）：Reddit 提及量 90 日內下降 33.3%，約 8 則/日；2026-09-04 單日提及量暴增 250%。整體聲量偏低。
- **StockTwits / X**：
  - StockTwits 於 2026-08-26 前後報導 CBRS 情緒為 bullish。
  - StockTwits 後續標題為「CBRS 股價接近第四個月下跌」，並提到 ARK（Cathie Wood）買入約 $17M，語氣轉為價格導向。
  - 2026-10 之後的 StockTwits 情緒讀數：DATA_UNAVAILABLE。
- **Sentiment 第三方彙整**：SentiSense 30 日情緒為 neutral，新聞面 100% bullish（樣本為 mentions，數量有限）。
- **資料品質警示**：historicaloptiondata.com 的頁面價格前後不一、EPS 數字與其他來源不符，已排除不採信。
- **Retail 總體語氣**：已知資料（8 月至 9 月）為中性偏多，但 10 月以後無可靠零售資料，無法確認目前語氣。

### 主要主題（依 WebSearch 摘要歸納，非逐篇貼文）

1. 基本面與 AI 晶片敘事：對 wafer-scale 推論晶片的成長性仍有支持。
2. 股價走弱：股價從 9 月約 $200 以上下跌至目前 $110 附近，多數討論轉向「為何下跌」。
3. 內部人出售：散戶解讀內部人出售為負面訊號。
4. 空頭部位：short float 約 12.6%（info: shortPercentOfFloat 0.1258）。

## Insider activity

統計區間：2026-04-26 至 2026-10-26（6 個月）。金額單位 USD（M = 百萬美元）。

- **公開市場出售（Sale 且有價格）合計**：約 **$408.4M**（9 月 $142.4M、8 月 $245.3M、6 月 $20.7M）。
- **公開市場買入**：無紀錄（**$0**）。
- **淨額**：約 **-$408.4M**（純賣出）。
- 股票贈與（Gift，價值 0）與獎勵授予（Award）未計入金額。
- 衍生性證券轉換（2026-05-15，Benchmark、Foundation、Vassallo 等 10% 股東 / 董事相關實體）以 $279.72 計價，合計約 $12.1B 名目值，屬轉換而非市場出售，**未計入上述淨額**，僅列為背景。

### 依角色拆解（USD M）

| 角色 | 6 個月出售金額 | 主要筆數 |
|---|---|---|
| CTO Sean Lie | ~193.8 | 2026-08-21 出售 ~$151.1M（726,540 股，約 $203.78–212.64） |
| COO Dhiraj Mallick | ~103.6 | 2026-09-29 出售 ~$80.8M（396,000 股，約 $194.91–212.93） |
| CEO Andrew Feldman | ~64.3 | 2026-08-21 出售 ~$47.3M（237,559 股） |
| 董事（間接持股）Steven Vassallo、Eric Vishria | ~37.1 | Vishria 2026-08-17 約 $15.7M；Vassallo 2026-09-04 與 08-14 各約 $10.5M、$10.9M |
| CFO Robert Komin | ~6.6 | 2026-09-29 出售 32,500 股，約 $6.6M |
| 其他 Officer Yagnesh Patel | ~3.0 | 分散於 6 月至 9 月的小額出售 |

### 值得注意的事項

- 高價區間出售：8 月至 9 月出售價格大多在 $195–$250，目前股價約 $111，相較當時已跌約 45% 以上。
- 出售集中於 8 月至 9 月，6 月亦有大額 COO / CTO 出售，顯示管理層出售為持續行為，並非單次事件。
- 10b5-1 計畫與否、出售動機（稅務、多元化等）：DATA_UNAVAILABLE。
- 2026-06-11 Susan Lior 持有 13,466,197 股（間接，無價格、交易類型不明）：DATA_UNAVAILABLE。

## Ownership shifts

- 機構持股比例：80.4%（institutionsPercentHeld）；流通股中機構占比 88.9%；機構數 556 家。
- 內部人持股：9.6%。
- 前十大機構（2026-06-30 季報）合計約 46.9%：
  - Eclipse Operations 10.2%（11.45M 股）
  - FMR 7.5%
  - Altimeter Capital 6.4%
  - Coatue 6.3%
  - Capital World Investors 3.5%
  - Morgan Stanley 2.9%
  - Atreides 2.8%
  - JPMorgan 2.8%
  - Tiger Global 2.7%
  - Vy Capital 1.9%
- 機構持股變化趨勢：所有列出機構的 pctChange 皆為 1.0，資料欄位疑似異常，無法判讀增減方向，**標記 DATA_UNAVAILABLE**。Benchmark 與 Foundation 等 VC 股東在 2026-05-15 至 06-29 有大量轉換與申報，屬持股結構變動，但非買賣訊號。

## Net sentiment score

- **分析師（強）**：偏多，信心 **高**（11 家全數買進，mean 目標價遠高於現價）。
- **內部人 / 資金流（弱）**：偏空，信心 **高**（6 個月約 $408M 純出售，無買入，主要為 CEO / COO / CTO 出售）。
- **股價趨勢**：偏空。現價 $110.82 接近 52 週低點 $106.13，距 52 週高點 $386.34 約 -71%。
- **零售 / 社群**：中性，信心 **低**（僅有 8 月至 9 月數據，10 月資料缺失）。
- **綜合**：**中性偏空**，信心 **中**。分析師一致偏多與內部人大額出售、股價弱勢形成明顯分歧，綜合判斷應以資金流與價格為主要參考，分析師評等為次要參考。

**Divergence flag: 是**。分析師語氣（強烈偏多）與內部人出售流向及價格趨勢（偏空）相反，此分歧本身具參考價值。零售語氣與分析師是否相反，因 10 月資料缺失，**無法確認**。

## 資料缺口彙整

| 項目 | 狀態 |
|---|---|
| Reddit 當期貼文與多空比例 | DATA_UNAVAILABLE |
| StockTwits 2026-10 情緒讀數 | DATA_UNAVAILABLE |
| 逐家券商升降評與目標價修正歷史 | DATA_UNAVAILABLE |
| 機構持股增減方向（pctChange 異常） | DATA_UNAVAILABLE |
| 內部人 10b5-1 計畫資訊 | DATA_UNAVAILABLE |
| Susan Lior 2026-06-11 持股異動類型 | DATA_UNAVAILABLE |

SENTIMENT REPORT COMPLETE
