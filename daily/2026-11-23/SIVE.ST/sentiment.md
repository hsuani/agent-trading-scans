# Sentiment — SIVE.ST（Sivers Semiconductors AB (publ)，Nasdaq Stockholm）as of 2026-11-23

資料時間：yf 快取 2026-11-22 14:32 UTC 更新；網路新聞為即時搜尋結果，多數無明確日期。本報告未借用任何過往 daily/<date>/ 報告數字。

資料來源狀態
- yfinance 即時呼叫失敗（Cookie/crumb 失敗），改用 repo 快取 `prices/yf/SIVE.ST.json`，無 `_misses`。
- Reddit（r/stocks、r/wallstreetbets）：WebFetch 被拒絕存取，soft-fail。
- StockTwits（api.stocktwits.com）：DNS 無法解析，soft-fail。需在 session 網路設定允許該網域後才可重試。
- 公司識別：WebSearch 確認 SIVE.ST = Sivers Semiconductors AB（Kista，瑞典；STO: SIVE；產業 Semiconductors）。

## Analyst consensus

2 buy / 0 hold / 0 sell（rec_summary 0m 與 -1m 皆為 1 buy，合計 1 家評等可見；yf 顯示 numberOfAnalystOpinions = 2，recommendationKey = none）。

| 指標 | 數值 | 備註 |
|---|---|---|
| 目標價均值 | 7.70 SEK | 快取值 |
| 目標價高 / 低 | 8.00 / 7.40 SEK | 僅 2 家 |
| 現價（快取） | 11.41 SEK | 與均值相比約 -33% |

Recent moves：快取 recommendations 無評等變動紀錄（只有 0m / -1m 彙總），無近期升降評。另一則 TradingView 來源的目標區間 5.80–8.00 SEK 疑為 2026 年較早資料，與快取不一致，未採用。

覆蓋面極薄（僅 2 家），分析師情緒的代表性有限。

## Retail social

- Reddit：未取得。soft-fail。
- StockTwits / X：StockTwits 無法連線。X 無直接取得，僅有新聞與德文財經站的散戶向評論。
- 聲量：無法量化與常態比較。以德文財經站文章數量估計，近期標題偏向下跌與做空相關，屬媒體敘事而非散戶貼文。
- Tilt：**無法判定**（社群來源全數缺失）。

新聞與媒體敘事（可作為替代參考）：
- 做空方向相互矛盾，有評論建議保持謹慎（finanztrends / boerse-global 系列標題，如「Leerverkäufer-Zoff」「Marble Bar wettet dagegen」）。
- 股價受半導體指數回檔與 Nvidia 相關疑慮拖累（單日約 -6%，媒體引述）。
- TipRanks 技術面評為負向，股價低於 50/100/200 日均線（頁面日期不明）。
- Simply Wall St：P/S 約 3.3x，同業均值約 7.9x（相對便宜的敘事，但與市場情緒相反）。
- 近期公司事件：與 WT Microelectronics 的分銷合作、LiDAR 客戶開出量產訂單（媒體引述，預計 Q4 2026 交貨）。

Themes（從新聞歸納，非散戶貼文）：
1. 做空與空方論戰（多空訊號分歧）。
2. 半導體族群回檔與 Nvidia 連動風險。
3. 估值「便宜」與「技術面弱」的對立。
4. CPO / LiDAR 題材與量產時程。

## Insider activity

yfinance insider 快取為空，無法計算完整 6 個月淨額。以下來自 WebSearch（placera / inderes 公告與媒體轉載），金額與日期不全：

- 2026 年 6 月股東會授權回購後，董事會成員（Bastani、Raj、Svancar、Thomson、Nideborn）與 CEO 陸續買入；公司於 2026-07-13 宣布完成。買入金額未取得完整數字。
- CEO Vickram Vathulya 買入 70,000 股，約 SEK 2.6M（隱含均價約 37 SEK），日期約為 2026 年 7 月前後，來源未標明確切日期。
- 董事 Todd Thomson 於 2026-07-21（鎖定期屆滿後）大量賣出，價格區間約 SEK 32–37。賣出股數與金額未取得。
- Kairos Ventures 持續減持，部分報導稱已全數出清（來源相互矛盾）。
- 2026 年 4 月定向增資的鎖定期於 2026-07-16 屆滿，後續允許部分董事與高管出售。
- 3 月有小額賣出（約 SEK 8–10）。

Net 6mo：**無法量化**（無可靠金額）。定性為：鎖定期屆滿後，董事層有大額賣出，而 CEO 與董事會在較早期段有買入；整體為「先買後賣」的混合訊號，且賣出規模大於已知買入金額的可能性較高，但此判斷信心低。

Notable：CEO Vickram Vathulya（買入 70,000 股）；董事 Todd Thomson（大額賣出，2026-07-21）。

## Ownership shifts

- 內部人持股 21.3%（insidersPercentHeld）。
- 機構持股 18.3%（占總股本），占流通股 23.2%，機構數 58 家。
- inst_holders 快取僅列 3 家，且合計持股 < 0.01%，無法判定集中度趨勢；僅能確認內部人持股比重高。
- 無歷史季度機構持股變化資料，無法判定增減趨勢。

## Market data cross-check

- 市值（快取推算）：304,523,687 股 × 11.41 SEK ≈ 3.47 B SEK，與快取 marketCap 3,474,615,040 SEK 吻合。
- 價格來源衝突未解決：yf 快取 11.41 SEK；WebSearch 其他來源分別為 24.14 SEK、9.96 SEK、20.64 SEK、約 1.32 EUR。下結論前需以即時報價核對。
- 財報日期衝突：yf earnings_dates 為 2026-11-30；德文媒體為 2026-11-26（Q3 Zwischenbericht）。

## Net sentiment score

**Composite：偏空（bearish），信心低（low）。**

依據與權重（定性）：
- 分析師：偏多（2/2 buy），但目標均價 7.70 SEK 低於現價 11.41 SEK，估值訊號偏空。覆蓋面薄，權重低。
- 散戶社群：無資料，不計分。
- 新聞敘事：偏空（做空論戰、技術面弱、半導體族群回檔）；少數正面（量產訂單、分銷合作、P/S 偏低）。
- 內部人：混合偏空（大額賣出在鎖定期後出現，買入資料不完整）。

Divergence flag：**無法判定（資料不足）**。分析師方向為 buy，但目標價低於現價，且內部人賣出與分析師評等方向相反，此為分析師內部的分歧，並非散戶與分析師之間的分歧。散戶 tilt 無法取得，因此無法做散戶與分析師的背離判斷。

主要不確定性：
1. 股價基準未對齊（11.41 vs 其他來源 9.96–24.14 SEK），影響估值與內部人價格比較。
2. Q3 財報日期待確認（11-26 或 11-30）。
3. 社群來源缺失（Reddit / StockTwits），散戶情緒無法驗證。

本報告為情緒彙整，不含交易建議。

SENTIMENT REPORT COMPLETE
