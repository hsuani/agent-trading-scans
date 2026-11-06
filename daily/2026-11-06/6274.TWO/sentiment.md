# Sentiment — 6274.TWO 台燿科技 as of 2026-11-06

> 資料品質警示：yfinance live feed 大部分連線被 proxy 擋下，以下 analyst 數字來自 repo cache（`yf.py` 回傳），`info` 的部分欄位（現價 906、prevName / nameChangeDate）與網路上的股價報導明顯不一致，需先確認。`ratings` / `holders` 不是 `yf.py` 的合法 subcommand，改用 `recommendations`、`rec_summary`、`major_holders`、`inst_holders`。

## Analyst consensus

**15 家：5 Strong Buy / 10 Buy / 0 Hold / 0 Sell，BUY 比例 100%（Strong Buy 33%）。** `recommendationMean` 1.33，Yahoo 標示 `strong_buy`。

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell |
|------|-----------|-----|------|------|-------------|
| 目前 (0m) | 5 | 10 | 0 | 0 | 0 |
| -1m | 5 | 10 | 0 | 0 | 0 |
| -2m | 4 | 10 | 0 | 0 | 0 |

近兩個月 Strong Buy 由 4 升至 5，無降評紀錄，評級結構穩定偏多。

目標價（cache，單位 TWD 元）：mean 2,323、median 2,170、high 3,515、low 1,770。

網路上的券商目標價（日期不一，僅供參考）：
- Nomura 2,115（2026-06-30）
- CLSA 1,600（2026-05-07）
- Goldman Sachs 1,165（2026-04-20）與 1,015（2026-03-23），較舊
- 外資一家 2,860，買進（UDN 報導 6 月營收，來源未標明券商）
- FactSet 15 家調查中位數 EPS 2026 約 23.63 元，目標價 900 元出現在某篇 cnyes 報導，日期不明

注意：cache 的 `targetLowPrice` 1,770 高於 `info` 內的現價 906，且網路股價報導為 1,420（10/22）與 1,615（10/16）。目標價低點高於現價的情況需要人工確認現價是否為過期或錯誤值。

## Retail social

- **Reddit (r/wallstreetbets, r/stocks)**：DATA_UNAVAILABLE。直接 fetch 被擋，未取得可用 thread。
- **StockTwits**：DATA_UNAVAILABLE。未嘗試直接 API，因為 WebSearch 已顯示主要來源為台股站點。
- **台股論壇 / CMoney 社群（WebSearch 摘要）**：討論偏分歧。摘要內容為平台自動整理，並非原始貼文，只能當作方向參考。
  - 偏空論點：基本面與資本壓力疑慮，留言語氣如「連台燿財報都救不了」（代表性引述，已截斷）。
  - 偏多論點：銅箔基板（CCL）跟著供應鏈漲價、AI 資料中心與高階交換機需求題材。
- **討論量**：無法取得可靠的提及次數，無法與歷史基準比較，標示為「定性：中等偏低，樣本不足」。
- **估值爭議**：StatementDog 顯示 P/E 約 85 倍，玩股網 8/28 資料為 P/E 約 73 倍，是散戶爭論的核心。

### 主要主題

1. AI 資料中心 / 高階交換機帶動 CCL 需求（多方）
2. 銅箔基板漲價循環（多方）
3. 本益比偏高、獲利能見度（空方）
4. 資本支出與資金壓力（空方）

## Insider activity

Net 6mo：DATA_UNAVAILABLE。`insider` 回傳空陣列 `[]`，這可能代表「無申報」，也可能代表 cache 或 feed 不完整，無法確認是否真為零。

台灣 insider 申報需透過公開資訊觀測站（MOPS）的「董監事持股餘額」與「內部人持股轉讓事前申報」查詢，本次 WebSearch 未取得 2026 年的具體增減持數字。

## Ownership shifts

- 機構持股比例 `institutionsPercentHeld`：44.32%
- 機構佔流通股比例 `institutionsFloatPercentHeld`：50.55%
- 內部人持股比例 `insidersPercentHeld`：12.33%
- 機構數量 `institutionsCount`：136

**趨勢方向：DATA_UNAVAILABLE。** `inst_holders` 回傳空陣列，只有單一時點快照，無法判斷機構是加碼還是減碼。WebSearch 找到 WantGoo 的分點與外資買賣頁面，但未能取得完整時間序列。

## Net sentiment score

**Composite：偏多（analyst）／ 分歧（retail）。整體信心：低到中等。**

- 分析師面：強烈偏多，15 家全部 Buy，目標價中位數高於 cache 內的現價，但現價本身需要確認。
- 散戶面：分歧偏空，主要擔心估值與基本面品質，缺乏可量化的樣本。
- 機構流向：DATA_UNAVAILABLE，無法判斷方向。
- 內部人：DATA_UNAVAILABLE。

**Divergence flag：yes（中等強度，低信心）。** 分析師 100% Buy 與散戶對估值的疑慮方向相反，但散戶樣本只來自摘要頁，且多數來源日期為 2026 年中以前，此旗標僅供參考，不應當成趨勢判斷。

**不提供交易建議。**

## 摘要行

analyst consensus 100% BUY（15 家，0 Hold / 0 Sell）；機構資金流向 DATA_UNAVAILABLE（僅有持股比例快照 44.3%，無趨勢）；散戶情緒 分歧偏空（估值與基本面疑慮 vs. CCL 漲價與 AI 需求題材）。

SENTIMENT REPORT COMPLETE
