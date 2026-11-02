# Sentiment — ETN as of 2026-11-03

資料截止：yf 工具回傳與網路搜尋結果最新約至 2026-08 (部分來源)；未取得 2026-10 / 11 月的分析師或內部人交易更新。Q3 財報預計約 2026-11-03 公布 (未經公司正式確認)。

## Analyst consensus

yf `rec_summary` (0m)：**28 家** — 5 strongBuy / 18 buy / 4 hold / 0 sell / 1 strongSell。
- 買進類 (strongBuy + buy) 23 家，占 82%；持有 4 家 (14%)；賣出類 1 家 (4%)。
- 2 個月前 (-2m)：5 / 17 / 4 / 0 / 1 = 27 家。近兩個月 buy 類 +1 家，hold 不變，屬小幅正向漂移。
- yf `recommendations` 的歷史升降評等 (upgrade/downgrade 明細) 回傳空陣列，無法驗證個別評等變動。

近期動作 (來自次要網路來源，日期為 2026 年 7–8 月附近)：
- Bernstein 維持 Buy，目標價 $534。
- JPMorgan 維持 Overweight，目標價由 $406 上調至 $445。
- Barchart 報導 25 家中 16 Strong Buy / 2 Moderate Buy / 7 Hold；Walnut 報導 8 月時 22 buy / 4 hold / 1 sell；MarketBeat 平均目標價 $420.95，Walnut 平均目標價 $457.75，Barchart 平均目標價 $414.67。
- **資料落差**：各來源家數與目標價不一致 (yf 28 家 vs Barchart 25 家；平均目標價 $414–458)，原因為統計來源與截止日不同。以 yf 為主、網路數字僅作參考。

## Retail social

- **Reddit (r/wallstreetbets、r/stocks)**：本次未取得 ETN 相關討論串。以 "Eaton ETN reddit wallstreetbets" 搜尋，結果全為新聞與報價頁，無 Reddit 內容。未直接抓取 Reddit JSON 端點 (依指示避免直接 WebFetch 社群站)，因此**無法判定 Reddit 傾向**。
- **StockTwits**：搜尋結果僅見頁面快照 (價格約 $418.56、52 週區間 $311.92–$436.74)，未見多空比例 (bull/bear %)，快照日期不明。**無法量化**。
- **TipRanks 散戶指標 (次要)**：Investor Sentiment 評為 "Very Positive"；30 天內 17.9% 的散戶改變持股。屬第三方彙整，未能核對原始貼文。
- **MarketBeat (次要)**：提及 short interest 增加，且新聞情緒分數 1.37；兩者方向不一致，無法作為散戶傾向的明確依據。
- **X / 新聞**：可見的新聞論述多為正向 (Q2 財報後股價大漲 7.3%、股價年初至今約 +41.8%)，但也有評論認為估值偏高、股價震盪。
- 整體：**散戶量能與傾向均缺乏可靠資料，無法與去年同期比較**，此區塊信心低。

Themes (來自新聞與分析師評論，非社群原文)：
- 電力管理 / AI 資料中心需求帶動成長 (正向主軸)
- 估值偏高、股價震盪 (主要保留意見)
- Q3 財報結果與指引 (近期變數)

## Insider activity

yf `insider` 回傳空陣列，**本工具無法提供 6 個月內部人交易資料**。`major_holders` 中 insidersPercentHeld 為 0.072%，內部人持股比例極低。

次要來源 (quantisnow / MarketBeat 搜尋摘要，未逐筆核對 EDGAR)：
- 過去 13 個月約 8 筆賣出、合計約 $22.6M；4 筆買進、合計約 $0.48M。
- 個別可見的賣出：Ruiz Sternadt Paulo (officer) 約 $4.18M (2026 年 2 月附近)；Monesmith Heath B. 約 $7.51M；Galvao Antonio (officer) 亦有 2026 年賣出紀錄；Wadecki Adam 於 2026-08-04 賣出。
- 搜尋結果中未找到 "Paolo Pelletier" 相關申報，原提示的人名可能有誤；未在 EDGAR 驗證。
- 6 個月淨值估計：**賣出明顯多於買進** (以 13 個月數字推估，6 個月區間內需 EDGAR 確認)。
- 2026-08 之後的 Form 4 未見於搜尋結果，可能缺漏。

## Ownership shifts

- institutionsPercentHeld：87.84%；institutionsFloatPercentHeld：87.91%；institutionsCount：3,503。
- 機構持股高度集中；未取得季度間變化趨勢 (無前後期比較資料)，**趨勢無法判定**。
- 一則網路摘要稱過去三個月買進評等占比上升，與 yf 的 +1 buy 方向一致，但來源不明。

## Net sentiment score

**Composite：偏多 (bullish)，信心：中低。**

- 分析師面 (權重高、資料最可靠)：偏多。28 家中 82% 買進類，評等與目標價近期小幅上修。
- 散戶面：資料不足，僅 TipRanks 單一指標顯示 "Very Positive"，無法交叉驗證，權重低。
- 內部人面：偏空。次要來源顯示賣出金額遠高於買進，主要為 officer 出售；但部分賣出可能屬選擇權行權後的例行處分，需對照 EDGAR 判斷。
- 扣除資料缺口後，偏多主要依據分析師共識與機構持股穩定。

**Divergence flag：無法判定 (retail 資料不足)。**
- 分析師與 TipRanks 散戶指標方向一致 (皆偏多)；內部人淨賣出則是與分析師方向不同的訊號，值得留意。
- 若取得 Reddit / StockTwits 原始多空比後，應重新評估是否背離。

## 資料缺口與後續建議

1. 內部人交易：yf insider 回傳空，需查 EDGAR Form 4 (CIK 1551182) 補齊 6 個月明細與金額。
2. Reddit / StockTwits：本次未取得原始資料；可於可存取時補查。
3. Q3 財報 (約 2026-11-03)：公布後分析師評等與目標價可能大幅變動，本報告的 as-of 數據可能很快過時。
4. 評等歷史：yf recommendations 無升降明細，需另行確認近期 upgrade / downgrade。

SENTIMENT REPORT COMPLETE
