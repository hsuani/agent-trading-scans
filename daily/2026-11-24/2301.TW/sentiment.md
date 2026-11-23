# Sentiment — 2301.TW (光寶科技 Lite-On Technology) as of 2026-11-24

> 資料注意: 系統今日日期為 2026-11-23，本報告以 2026-11-24 為標示日期，部分資料為 11/20 前後快照。yfinance 端點 (Yahoo cookie/crumb) 連線失敗，部分數據來自快取，`inst_holders` 與 `insider` 回傳空陣列，屬於資料缺漏而非「無交易」之確認。

## Analyst consensus

12 家覆蓋 (rec_summary 0m): 4 Strong Buy / 6 Buy / 2 Hold / 0 Sell / 0 Strong Sell，即 **10 買進 / 2 持有 / 0 賣出**。

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 合計 |
|---|---|---|---|---|---|---|
| 0m (現在) | 4 | 6 | 2 | 0 | 0 | 12 |
| -1m | 4 | 6 | 2 | 0 | 0 | 12 |
| -2m | 4 | 6 | 2 | 0 | 0 | 12 |
| -3m | 4 | 5 | 2 | 0 | 0 | 11 |

- 近三個月評等分布幾乎不變，僅 -3m 時一家 Buy 數量較少，未見明顯上調或下調潮。
- `recommendations` 端點只回傳彙總計數，**沒有逐筆評等變動 (upgrade/downgrade) 紀錄**，因此無法確認個別券商動作日期。
- 目標價 (WebSearch 彙整，來源日期不一致，僅供參考):
  - Investing.com 快照: 平均 12 個月目標價約 313 TWD，區間 242–400 TWD。
  - 另一快照: Nomura/Instinet Buy，目標價 354 TWD，日期標為 02/11/2026 (日期格式可能為 2 Nov 或 11 Feb，無法確認)。
  - 本土投顧 (11/2 報導): 「買進」，目標價由 370 元微調至 350 元。
  - StockAnalysis (6 月快照，S&P Global 來源): 7 家平均目標 215.43 USD，區間 176–285 USD，評等 Buy。
- 目標價離散度大，且多為過期或小樣本快照，不宜視為即時共識。

## Retail social

- **Reddit (r/wallstreetbets, r/stocks)**: 本次依指示未以 WebFetch 抓取，未取得樣本。依規範不視為「無討論」，僅為未覆蓋。
- **StockTwits**: 未檢查 (本次僅使用 WebSearch 作為零售來源)。
- **X / 新聞與論壇 (WebSearch)**: 繁中財經媒體與論壇有實質討論，主要內容如下:
  - 11/2 報導指出股價由 9 月初歷史高點 328 元回落至低點約 235 元，跌幅約兩成，市場焦點在評價修正。
  - 10/30 法說會後，市場關注美國資料中心用電需求與客戶拉貨節奏、800VDC 出貨時程，以及存貨與資金壓力。
  - 10 月合併營收 200.71 億元 (TWD)，月增 6.5%、年增 32.0%；1–10 月累計 1,736.30 億元 (TWD)，年增 26.8%。
  - 管理層表示 AI 相關營收占比今年超過 30%，明年目標 40%–50%。
  - 一篇 Dcard 文章認為公司已從零件廠轉型為 AI 能源相關公司，但建議追蹤 Power Rack 與液冷客戶驗證進度。
- **Tilt**: 基本面與 AI 題材偏多，但股價動能與散戶情緒偏空/觀望。代表性語句 (≤15 字改寫):
  - 「業績創高、股價卻回檔」— 市場在評價與存貨之間拉扯。
  - 「AI 能源轉型是否成立」— 以客戶驗證與液冷進度為主要追蹤點。
- **Buzz volume**: 定性判斷為中等，主要集中在法說會與月營收公布前後，非異常放大。
- **Themes**: 1) AI 營收占比與液冷/Power Rack 客戶; 2) 美國資料中心用電與拉貨節奏; 3) 股價自高點回落與評價; 4) 存貨與資本支出壓力。

## Insider activity

Net 6mo: 資料不可得 (`insider` 回傳空陣列，Yahoo 端點連線失敗，快取無資料)。**未確認 CEO/CFO 或其他董監事之買賣方向與金額，本節標記為 DATA_UNAVAILABLE。**

## Institutional / ownership shifts

- `major_holders` (Yahoo 快取):
  - 內部人持股 (insidersPercentHeld): 14.16%
  - 機構持股 (institutionsPercentHeld): 38.58%
  - 機構持股占流通股 (institutionsFloatPercentHeld): 44.94%
  - 機構數量 (institutionsCount): 275
- `inst_holders` 回傳空陣列，**無法確認前幾大機構名單與季度增減趨勢**，趨勢判斷 DATA_UNAVAILABLE。
- 單一時點快照，無法判斷增減持方向。

## Net sentiment score

- **Analyst tilt**: bullish (10 買 / 2 持有 / 0 賣，近三月穩定)。
- **Retail / social tilt**: neutral-to-bearish on price action (回檔、技術面偏弱)，但對基本面與 AI 題材偏多。
- **Insider tilt**: 無資料，不納入計分。
- **Composite**: **bullish，信心中低 (medium-low)**。分析師共識明確，但價格動能與零售情緒偏弱，且目標價與股價快照來源不一致，insider 與機構趨勢資料缺漏。
- **Divergence flag**: **部分分歧 (partial yes)** — 分析師與基本面評論偏多，但股價走勢與零售情緒偏空/觀望。並非完全相反，屬於「基本面樂觀、價格動能弱」的分歧。

### 價格快照一致性警示
WebSearch 取得的最新股價快照互相矛盾 (175.5 / 207.0 / 233.5 TWD，日期 11/10–11/20)，且與 11/2 報導低點 235 元不一致。**本報告未以任何單一股價作為計算基礎，使用前請以 TWSE 即時報價核對。**

## Summary table

| 面向 | 結果 | 信心 | 備註 |
|---|---|---|---|
| 分析師共識 | 10 買 / 2 持有 / 0 賣 (偏多) | 中高 | 近三月穩定，無逐筆升降評等紀錄 |
| 目標價 | 平均約 313 TWD (區間 242–400)，來源日期不一 | 低 | 快照混雜，需以彭博/TWSE 核對 |
| 零售社群 | 基本面偏多、股價動能偏弱 | 中 | Reddit/StockTwits 未覆蓋 |
| 聲量 | 中等，集中於法說與月營收 | 中 | 定性判斷 |
| 內部人交易 (6mo) | DATA_UNAVAILABLE | — | yfinance insider 空陣列 |
| 機構持股 | 內部人 14.16%、機構 38.58%、275 家 | 低 | 單點快照，無季度趨勢 |
| 綜合情緒 | Bullish (信心中低) | 中低 | 部分分歧: 基本面與分析師偏多，價格與零售偏弱 |

本報告為情緒彙整，不構成交易建議。

SENTIMENT REPORT COMPLETE
