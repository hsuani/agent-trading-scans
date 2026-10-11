# Sentiment — GFS (GlobalFoundries) as of 2026-10-11

資料可得性說明: yf 工具 cookie/crumb 取得失敗, 全部結果來自 cache fallback (屬預期情況)。Reddit 與 StockTwits 直接抓取在此沙盒被封鎖, 改用 WebSearch, 未重試被封網站。X 無獨立抓取, 僅有一般新聞搜尋結果。

## Analyst consensus
yf rec_summary (cache, 期間標示 0m, 實際快照日期 DATA_UNAVAILABLE): 3 strongBuy / 10 buy / 9 hold / 0 sell / 1 strongSell, 共 23 位分析師。換算為 13 buy / 9 hold / 1 sell。

歷史 4 期趨勢 (0m → -3m): strongBuy 3→4→4→3, buy 10→10→9→9, hold 9→8→8→9, strongSell 恆為 1。整體評級分布幾乎持平, 未見明顯上調或下調趨勢。

第三方彙整 (WebSearch, 來源不一致):
- MarketBeat: 19 位, Hold 共識 (8 buy / 9 hold / 2 sell), 平均目標價約 $75.11。
- Investing.com: 21 位, Buy 共識, 平均目標價約 $80.24。
- Benzinga (2026-08 快照): 19 位, Neutral 共識, 平均目標價 $63。

近期評級變動:
- 2026-10-06: Arete 上調, 目標價 $95 (僅 Investing.com 單一來源, 未交叉驗證)。
- 2026-08 前後: TD Cowen 維持 Buy, 目標價由 $85 降至 $75; UBS 維持 Neutral, 目標價由 $61 降至 $55 (Benzinga)。MarketBeat 另有 2026-08-06 降至 Neutral、目標 $55 (由 $61 下修) 的紀錄, 券商名稱 DATA_UNAVAILABLE。
- 2026-05: Cantor Fitzgerald 由 Neutral 升至 Overweight (2026-05-04); Susquehanna 由 Neutral 升至 Positive (2026-05-06)。
- 2025 下半年: Wedbush 由 Outperform 降至 Neutral (目標 $40, 2025-12-31); Jefferies 降至 Hold (2025-10); BofA 降至 Underperform (目標 $35, 2025-10), 為所見最悲觀評級。

觀察: 目標價在 2026 年內大幅變動 (Fintel 4 月平均約 $52, 之後多數來源升至 $63–80 區間), 但 8 月起多家目標下修, 且各家平均值差異大, 不宜單獨採信任一數字。

## Retail social
- Reddit (r/wallstreetbets, r/stocks): DATA_UNAVAILABLE。WebSearch 未回傳任何 GFS 相關 Reddit 討論串, 無法評估樣本與 tilt。
- StockTwits: 部分可得。WebSearch 摘要顯示 "Bearish Sentiment" 標籤, 股價約 $58.50, 52 週區間 $31.51–$92.55; 快照日期與投票數 DATA_UNAVAILABLE。此快照可能早於 2026-09 的價格下跌, 時效性低。
- X: DATA_UNAVAILABLE (未取得可引用貼文)。
- Options flow (Benzinga 2026-08 快照): P/C 比 0.31, 買權多於賣權, 偏多訊號; 時效性同樣有限。
- Short interest: 約 15.0% of float (Benzinga, 2026-08 快照), 報告稱較前期下降。
- Buzz 量: DATA_UNAVAILABLE (無可靠提及次數, 無法與歷史基準比較)。

Themes (依 WebSearch 摘要 / TipRanks 公開多空論點, 非 Reddit 原文):
- 多方: 設計導入 (design-win) 動能, 產能擴充 (Barchart 報導 capacity expansion 面臨首次實際需求檢驗), 長期成長敘事。
- 空方: 晶圓平均售價 (ASP) 下滑, 2026-08 Q2 前預期 EPS 年減, 股價自 6 月高點 (約 $83–87) 回落至 9 月約 $43–49。

## Insider activity
資料區間: 2026-04-11 至 2026-10-11 (6 個月)。
Net 6mo: $0 buys, **$3,495,537 sells** (37 筆 open-market 賣出)。無公開市場買進紀錄。

依內部人彙總賣出金額:
| 內部人 | 職稱 (yf) | 賣出金額 | 備註 |
|---|---|---|---|
| HOGAN MICHAEL JAMES | Officer | $1,398,263 | 最大賣方, 多次小量分批賣出並伴隨 Stock Gift |
| VICARI SAMUEL | Officer | $657,289 | 2026-05-11 單筆 8,692 股 @ $75.62 |
| AZAR SAMAK L | Officer | $522,954 | 約每週一筆 335–500 股, 持續性賣出 |
| DORCHAK GLENDA MARY | Director | $466,720 | 2026-04-20 與 2026-07-20 各 4,000 股 |
| RAMAN PRADHEEPA | Officer | $450,311 | 2026-08-18 6,760 股 @ $51.12; 2026-09-28 2,145 股 @ $48.83 |

Notable:
- 2026-09-28 RAMAN PRADHEEPA (Officer) 賣出 2,145 股 @ $48.83, 為最近一筆交易。
- 2026-07-28 董事年度股票獎勵 (Stock Award) 共 5 筆 (RAO、HALAWA、OBEID、LANGUILLE、ANTAKI), 屬薪酬性質, 非市場買入。
- 內部人持股比例 (yf) 約 0.06%, 內部人對股價的直接利益連結有限。
- 各內部人職稱僅 yf 提供的 Officer / Director 分類; CEO / CFO 身分 DATA_UNAVAILABLE, 不做推論。
- 賣出多為分批小量, 是否為 10b5-1 計畫 DATA_UNAVAILABLE。

## Ownership shifts
- institutionsPercentHeld: 100.2% (yf 數值超過 100%, 屬資料口徑問題, 應視為接近全數機構持有, 不適合作為精確比較)。
- institutionsCount: 598 (yf 快照, 日期 DATA_UNAVAILABLE)。
- insidersPercentHeld: 0.058%。
- 季度間機構持股變化趨勢: DATA_UNAVAILABLE (本次僅取得單一快照, 無歷史序列)。

## Net sentiment score
**Composite: 中性偏空 (信心: 低)**

分項:
- 分析師 (yf 23 位): 中性偏多 (13 buy / 9 hold / 1 sell), 評級分布近幾期持平。信心: 中。
- MarketBeat / Benzinga 彙整: 中性 (Hold / Neutral 共識)。分歧來源多, 信心: 低。
- 零售 (StockTwits 單一快照, Reddit/X 缺漏): 偏空, 但時效不明。信心: 低。
- 內部人 (6 個月): 淨賣 $3.5M, 無買進, 偏空。信心: 中 (賣出多屬分批、常見於例行計畫, 但完全無買進仍具參考性)。
- 選擇權 (Benzinga 8 月快照): 偏多。信心: 低 (時效不足)。

Divergence flag: **是 (低信心)**
- 分析師 yf 數據偏多 vs StockTwits 偏空 → 零售與分析師方向相反。
- 內部人淨賣出與分析師中性偏多亦不一致。
- 解讀受限於多個資料點時間不一致 (8 月至 10 月), 且 Reddit/X 缺漏, 此分歧訊號的可靠度有限。

Data gaps: Reddit 量與 tilt、X 聲量、StockTwits 快照日期與投票數、機構持股季度趨勢、內部人職稱、yf rec_summary 快照日期、Arete 評級之單一來源驗證。

本報告僅呈現情緒資料與彙整, 不構成交易建議。

SENTIMENT REPORT COMPLETE
