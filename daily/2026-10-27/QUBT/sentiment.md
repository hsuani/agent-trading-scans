# Sentiment — QUBT as of 2026-10-27

> 資料時效警示: 系統當前日期為 2026-10-26, 本報告以指定的 DATE=2026-10-27 標註。Reddit、StockTwits 皆無法取得, 社群情緒無有效樣本, 整體結論信心偏低。

## Analyst consensus
yf `rec_summary` 回傳 4 buy / 2 hold / 0 sell / 0 strongBuy / 0 strongSell (期間 0m 至 -3m 數值完全相同, 疑為快取或未更新的資料)。
MarketBeat 網頁摘要 (2026 年中) 為 4 buy / 2 hold / 1 sell, 共 7 位分析師, 平均 12 個月目標價 $18.33 (區間 $10.00–$30.00)。兩來源的 sell 數量不一致, 需以 MarketBeat 或券商原始報告再核對。

Recent moves: yf `recommendations` 在 4 個月區間內無評等變動, 無可辨識的升級或降級紀錄。目標價變動無法從現有來源確認。

量化評等 (Equibles, 約 2026-08-20 快照, 股價約 $8.14): 整體 Sell, 技術面 strong sell, 聰明錢情緒偏 bullish。
Technical 分析 (Traders Union, 2026 年中): 反彈技術面脆弱, 若未站上 $8.32 有回測 $7.28 或更低的風險。

## Retail social
- Reddit: 無法取得。r/wallstreetbets 與 r/stocks 的 search.json 皆被 proxy 擋下 (WebFetch 無法連線; 直接 curl 回 CONNECT 403)。無貼文樣本、分數與留言數可引用。
- StockTwits / X: StockTwits API 因 DNS 解析失敗無法連線, 本輪無資料。X 無可用的即時貼文。
- Retail 替代訊號: Investing.com 使用者投票 (2026-07 底至 08 初) 多空接近持平, 價位集中在 $7.50–$8.30, 屬非正式樣本, 參考價值低。
- 聲量 (buzz volume): 無法量化, 無法與歷史基準比較。
- Themes: 目前無法從可取得資料中歸納出可靠主題。web 摘要提到的反覆議題包括: 公司營收相對估值偏小、股價自 2026 年高點回落約 65%、空單比例偏高 (Equibles 估約 28% of float, 未經證實)、Q2 財報前後的情緒性反彈。這些是媒體與分析文章的觀點, 不代表散戶論壇情緒。

Retail tilt: 無法判定 (bullish / bearish / mixed 皆無足夠依據)。

## Insider activity
資料來源: yf `insider`。統計區間 2026-04-27 至 2026-10-27 (近 6 個月)。

Net 6mo: $0 公開市場買入, $0 公開市場賣出 (以 open-market Sale / Purchase 計)。
非現金交易: 2026-08-20 CEO HUANG YUPING 獲得股票獎勵 (Stock Award) 約 584,897 股, 申報價 $8.14–$8.95 (約 $4.8M–$5.2M 估值, 原始資料中同一筆有多列重複申報, 實際股數需以 SEC Form 4 核對); 2026-05-28 CEO、COO、Officer 各有約 24,774–58,558 股之 $0 價格獎勵。

Notable:
- CEO HUANG YUPING (CEO): 2026-08-20 股票獎勵及衍生性證券轉換, 屬薪酬性質, 非主動買入。
- 近 6 個月 無 CFO / 董事之公開市場買賣紀錄。
- 前期對照 (超出 6 個月, 僅作背景): 2026-03-11 General Counsel ROBERTS 出售 78,262 股 @ $7.85 (約 $0.6M); 2025-09 CEO 與 董事有大額出售 (例如 2025-09-04 CEO 出售 1,000,000 股 @ $14.42, 約 $14.4M)。2026 年 4 月董事各獲 22,123 股獎勵。
- 解讀: 近期內部人以獎勵為主, 無明顯的主動買進, 也無明顯集中出脫。與 2025 年下半年的大額出售相比, 方向偏中性。

## Ownership shifts
- insidersPercentHeld: 12.2%
- institutionsPercentHeld: 47.9% (float 口徑 54.5%), 機構數 412
- 本輪工具僅回傳單一快照, 無法計算近幾季的機構持股變化趨勢, 無法判定集中度是增加或減少。

## Net sentiment score
Composite: NEUTRAL (信心: 低)
- 分析師面: 多數 buy / hold, 無 sell (yf) 但 MarketBeat 有 1 sell, 且量化評等為 Sell。整體偏中性至略偏空, 資料過時。
- 內部人面: 近 6 個月無公開市場交易, 中性。
- 散戶面: 無有效樣本, 無法評分。
- 技術與市場敘事 (web, 2026 年中至夏季): 偏空至中性。

Divergence flag: NO (無法判定) — 因散戶面無資料, 無法確認散戶與分析師是否方向相反。若後續取得 Reddit 或 StockTwits 資料, 應重新評估此項。

資料缺口與後續建議:
1. 價格與近期新聞為 2026 年夏季快照, 須在 10-27 當日重新抓取 (財報前後的情緒最易改變)。
2. yf 分析師資料呈現異常的靜態值, 需以其他來源 (MarketBeat、券商原始評等) 交叉核對。
3. Reddit 與 StockTwits 在本環境無法存取, 需替代來源或 proxy 白名單處理後再補跑。

SENTIMENT REPORT COMPLETE
