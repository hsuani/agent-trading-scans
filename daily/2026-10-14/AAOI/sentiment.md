# Sentiment — AAOI (Applied Optoelectronics) as of 2026-10-14

資料來源狀態: yfinance 即時抓取失敗 (Cookie/crumb ConnectionError), 本次全部改用 repo cache (`prices/yf/AAOI.json`, `_refreshed_at` 2026-10-14 11:40 UTC)。Reddit 與 StockTwits 無法取得 (見下方「Retail social」)。

## Analyst consensus
6 位分析師 (rec_summary): 2 strongBuy / 1 buy / 3 hold / 0 sell。近三個月 (0m, -1m, -2m) 評等分布完全相同, 即 yfinance 顯示期間內無評等淨變動。平均評等 recommendationMean 2.33 (介於 buy 與 hold 之間, 偏買方)。

目標價 (cache info): 平均 $163.40, 最高 $220.00, 最低 $109.00, 對照 cache 現價 $97.78, 所有目標價皆高於現價。

近期評等動作 (WebSearch, 來源日期為 2026-02-27, 非 cache 資料): Northland 由 Outperform 降至 Market Perform, 目標 $55; B. Riley 由 Sell 升至 Neutral, 目標 $54。這兩個目標價與目前 cache 平均目標 $163 差距極大, 顯示搜尋來源的目標價資料已過時或與其他來源口徑不一致, 不宜單獨引用。StreetInsider 12 個月平均目標 $179.67 (最高 $220 Rosenblatt, 最低 $129 B. Riley)。

## Retail social
- Reddit: 無法取得。r/wallstreetbets 與 r/stocks 的 search.json 抓取皆回傳 "unable to fetch" 錯誤, 依規則 soft-fail, 無貼文樣本、無 tilt 判定。
- StockTwits: 無法取得。api.stocktwits.com DNS 解析失敗 (ENOTFOUND), 無訊息計數。
- X / 新聞 (WebSearch, 品質參差):
  - MarketBeat 新聞情緒分數 0.91 (範圍 -2 至 2), 偏正面。但同站 short interest 方向描述前後矛盾。
  - Investing.com 散戶情緒表 (2026 年 10 月初) 有內容但無法驗證細節。
  - historicaloptiondata.com 的 2026 年 5 至 6 月選擇權報告 (put 量約 65.8%, 6 月 bearish bias 60%) 立場不一, 且各頁價格不一致, 可信度低。
  - parameter.io 報導 $600M 增發後, 散戶情緒「快速轉為悲觀」(日期不明)。
  - 未找到 Reddit 貼文; 社群聲量無法與歷史基準比較。
- 聲量 (buzz volume): 無可靠量化資料, 無法判定相對於歷史常態的高低。
- Tilt: 無法可靠判定。新聞與選擇權訊號混合, 偏負面線索 (增發、6 月 bearish 報告) 與偏正面線索 (新聞情緒分數) 並存。
- Themes (從新聞與報導歸納, 非貼文樣本): AI 基礎設施營收題材 (管理層指引 2026 年營收可超過 $10 億)、高估值與波動 (52 週區間 $18.50 至 $233.67)、增發稀釋與 GAAP 虧損 (2025 年淨虧損 $38.2M)、空單比率偏高 (cache 顯示 short % of float 16.9%)。

## Insider activity
統計區間: 2026-04-14 至 2026-10-14 (6 個月)。排除 Stock Award 與 Stock Gift。
- 公開市場買入: $0 (0 筆)
- 公開市場賣出: $94.2M (26 筆)
- 淨額: 約 -$94.2M

重點人物 (6 個月賣出金額):
- CEO Lin Chih-Hsiang Thompson: $19.9M。2026-06-12 以 $166.53 賣出 59,000 股; 2026-05-19 以 $173.26 賣出 58,000 股。
- Chang Hung-Lun Fred (Officer): $22.7M。最近一筆 2026-09-08 以 $110.21 賣出 32,172 股 ($3.5M)。
- Yeh Shu-Hua Joshua (Officer): $17.0M。最近一筆 2026-10-05 以 $120.03 賣出 6,000 股, 為本區間最新一筆 insider 交易。
- CFO Murry Stefan J: $14.0M。約每月固定一筆 4,000 股的賣出 (2026-07-10、2026-08-10、2026-09-10 皆為此規模), 規律性高。
- Director Delaney Cynthia: $10.7M, 2026-05-26 以 $189.23 單筆賣出。
- Officer Kuo David C.: $8.2M (2026-06-12 等)。
- Director Chen Min-Chu Mike: $1.7M (2026-06-02)。

脈絡:
- 上述賣出價格多數落在 $105 至 $204, 現價 (cache) $97.78 低於多數賣出價。
- 最後一次 insider 公開市場買入為 2025-08-14 (CEO 與數位董事於 $21 至 $23 買入), 距今超過 12 個月。
- 資料未標示各筆是否屬 10b5-1 預定交易計畫, 無法區分計畫性與主動性賣出。
- 第三方 Equibles 聲稱 90 天內 insider 淨賣約 $45.9M, 與 yfinance 推算值不一致, 以 yfinance 為準。

## Ownership shifts
- 機構持股 63.58%, 機構數 634 家; 內部人持股 9.78%。
- 2026-06-30 季報前十大 (單期快照, pctChange 為相較前期變化):
  - BlackRock 7.63%, 股數減 10.3%
  - Invesco 4.04%, 增 69.5%
  - Vanguard Capital Management 3.98%, 增 9.9%
  - Marex Group 3.35%, 增 878.8% (由極低基數大增)
  - Vanguard Portfolio Mgmt 3.14%, 增 47.2%
  - UBS 2.50%, 增 117.5%
  - Oberweis 2.12%, 減 23.8%
  - Geode 1.98%, 增 3.1%
  - Value Aligned Research 1.89%, 增 25.8%
  - Goldman Sachs 1.88%, 增 46.3%
- 判讀: 前十大中多數為加碼, 僅 BlackRock 與 Oberweis 減碼。僅有單季資料, 無法確認連續趨勢。

## Net sentiment score
Composite: **中性偏空 (信心: 低)**

依據:
- 分析師 (偏多, 中等信心): 無 sell 評等, 平均 2.33, 目標價全數高於 $97.78 現價。但評等三個月未變動, 且目標價離散度大。
- 內部人 (偏空, 高信心): 6 個月 $94.2M 公開市場賣出, 零買入, 且賣出分布於多位高階主管, 賣出價多數高於現價。
- 散戶 (無法判定): Reddit 與 StockTwits 皆無資料。可用的新聞與選擇權線索互相矛盾。
- 機構 (偏多): 前十大多數加碼, 機構持股比例高。

信心偏低的主因是散戶資料缺口, 應視為部分結論。

Divergence flag: **無法判定 (資料不足)**。分析師 tilt 為偏多, 但散戶 tilt 無可靠樣本, 因此無法判斷是否背離。若後續補上散戶資料, 應重新評估。

資料限制與待補:
- Reddit 與 StockTwits 需於可連線環境重抓, 補上樣本與聲量基準。
- 分析師目標價在 cache 與搜尋來源之間不一致 (cache 平均 $163, 搜尋來源 $55 至 $54 為 2 月資料), 應以 Benzinga 或 MarketBeat 當期頁面或券商原文確認。
- 現價 $97.78 來自 cache (2026-10-14 11:40 UTC 更新), 但 Oct 5 insider 成交價為 $120.03, 盤中價格以即時報價為準。

## 指標表

| 指標 | 數值 | 來源 / 備註 |
|---|---|---|
| 分析師評等分布 | 2 strongBuy / 1 buy / 3 hold / 0 sell | yf rec_summary (cache) |
| 平均評等 recommendationMean | 2.33 | yf info (cache) |
| 目標價 平均 / 最高 / 最低 | $163.40 / $220.00 / $109.00 | yf info (cache), 現價 $97.78 |
| 近期評等變動 | 無 (0m, -1m, -2m 分布相同) | yf rec_summary |
| 2026-02 評等動作 | Northland 降至 Market Perform ($55); B. Riley 升至 Neutral ($54) | WebSearch, 日期 2026-02-27 |
| 6 個月 insider 公開市場買入 | $0 (0 筆) | yf insider 計算 |
| 6 個月 insider 公開市場賣出 | $94.2M (26 筆) | yf insider 計算 |
| 6 個月 insider 淨額 | -$94.2M | yf insider 計算 |
| 最後一次 insider 買入 | 2025-08-14 | yf insider |
| 最近一次 insider 賣出 | 2026-10-05, Yeh Shu-Hua Joshua, $120.03, 6,000 股 | yf insider |
| 空單占流通股 (short % of float) | 16.92% | yf info (cache); MarketBeat 另報 19.56%, 口徑不一 |
| 機構持股比例 | 63.58% (流通股 70.48%) | yf major_holders (cache) |
| 內部人持股比例 | 9.78% | yf major_holders (cache) |
| 機構家數 | 634 | yf major_holders (cache) |
| 前十大機構季度變化 | 7 家加碼, 2 家減碼 (BlackRock, Oberweis) | yf inst_holders, 2026-06-30 快照 |
| MarketBeat 新聞情緒 | 0.91 (範圍 -2 至 2) | WebSearch |
| Reddit 貼文數 / tilt | 無資料 | WebFetch 失敗 (soft-fail) |
| StockTwits 訊息數 / tilt | 無資料 | DNS 失敗 (soft-fail) |
| 散戶 tilt | 無法判定 | 資料不足 |
| 綜合情緒 | 中性偏空, 信心低 | 本報告判定 |
| 背離旗標 | 無法判定 | 散戶資料缺口 |

SENTIMENT REPORT COMPLETE
