# Sentiment — MRVL as of 2026-11-16

資料說明: 系統今日日期為 2026-11-15, 本報告依指定 as-of 日期 2026-11-16 標示。yf 工具回傳與搜尋結果的最新可見價格為 2026-11-09 (Trefis), 11/10 至 11/16 的盤後資料未驗證。Reddit 與 StockTwits 直接端點不可用 (Reddit 無法連線, StockTwits DNS 無法解析), 散戶面以 WebSearch 摘要替代。

## Analyst consensus

工具 (`rec_summary`, 0m 快照): 7 strong buy / 31 buy / 5 hold / 0 sell / 0 strong sell, 共 43 位分析師。Buy 類合計 38, 佔比約 88%。

| 期間 | Strong Buy | Buy | Hold | Sell | 合計 | Buy 類佔比 |
|---|---|---|---|---|---|---|
| 0m (最新) | 7 | 31 | 5 | 0 | 43 | 88% |
| -1m | 8 | 35 | 4 | 0 | 47 | 91% |
| -2m | 8 | 32 | 6 | 0 | 46 | 83% |
| -3m | 8 | 31 | 5 | 0 | 44 | 89% |

近一個月 Buy 類淨減 5 家, Hold 增 1 家, 無賣出評等。工具未提供個別分析師升降評等明細 (`recommendations` 只回傳彙總計數), 因此無法列出逐家 upgrade/downgrade。

Recent moves (來自搜尋摘要, 日期混雜, 未逐一核對原始報告):
- 2026-11-02 MRVL 宣布以全股票方式收購 Lumentum (約 115B USD), 股價當日跌約 13%。
- B. Riley 目標價由 365 降至 275 USD, 維持 Buy。
- Cantor Fitzgerald 目標價由 350 降至 225 USD, 維持 Neutral。
- Oppenheimer 重申 Buy, 目標價 325 USD。
- TD Cowen 維持 Hold, 目標價 245 USD。
- 來源衝突: MarketBeat 11/2 摘要為 8 SB / 32 B / 6 H (共 46 家), Barchart 稱 36 家 Strong Buy 共識; 與工具計數 (43 家) 不一致, 以工具數字為準。
- 2026-03-02 有 MarketBeat 「shares down 1% after analyst downgrade」標題, 細節未取得。

## Retail social

- Reddit: 直接 JSON 端點無法連線, 本輪無法取樣 r/wallstreetbets 與 r/stocks 的近期貼文。搜尋摘要提到 2026-06 的 r/wallstreetbets 熱門貼文 (買在 82 USD、討論是否在 325 USD 賣出), 屬於舊資料。SentiSense 2026-11-08 的 30 日讀數將 Reddit 列為中性。
- StockTwits / X: StockTwits API 無法解析 (DNS), 需在 session 網路設定允許 api.stocktwits.com 後才能取樣。搜尋摘要引用的 StockTwits 文章 (「MRVL Stock Slides Overnight After Record Close: Retail Traders Keep The Faith」) 與「extremely bullish」描述均為 6 月前後的情緒, 非本週。X 未取得可用資料。
- SentiSense 2026-11-08: 30 日整體偏多 (bullish), 但較一個月前降溫; News、X、YouTube 偏多, Reddit 中性。這是目前最新的散戶面讀數。
- Buzz 量: 無法量化提及次數。搜尋結果顯示 11/2 併購公告後話題量明顯增加, 但多為新聞與分析文, 散戶原生討論量無資料。以定性判斷為「高於平常, 以新聞驅動」。
- 散戶傾向: 整體偏多但降溫 (mixed to bullish, cooling)。併購公告後, 搜尋中未找到針對 Lumentum 交易的散戶專項調查。

Themes (主要議題):
1. AI 資料中心與光學互連 (optical) 的長期成長敘事, 是多頭核心論點。
2. 併購稀釋疑慮: 全股票交易讓 Lumentum 股東持有合併後約三分之一股權, 被市場視為主要賣壓來源。
3. 估值與漲幅: 2026 年上半段大幅上漲後, 部分人認為估值偏高, 「是否獲利了結」是反覆出現的問題。
4. 中國審查與交割時程: 交割預計 2028 上半年, 中國審查可能需 12 至 18 個月, 不確定性高。

## Insider activity

6 個月窗口 (2026-05-16 至 2026-11-15, 工具原始資料):
- 公開市場買入: 0 筆, $0。
- 公開市場賣出 (有價格的交易): 11 筆, 合計約 $18.9M。
- 其餘 18 筆無價格紀錄, 多為 RSU/選擇權歸屬或稅務代扣, 或 Stock Gift (0 價格), 未計入上述金額。

| 內部人 | 職位 | 6 個月賣出 (M USD) | 主要交易 |
|---|---|---|---|
| Christopher Koopmans | President | 8.5 | 每月約 10,000 股, 2026-07-01 at $281.92, 2026-11-02 at $186.97 |
| Matthew Murphy | CEO | 7.3 | 7,500 股, 2026-06-15 at $298.76, 2026-09-15 at $223.39 |
| Sandeep Bharathi | Officer | 2.5 | 2026-06-16 at $299.13, 2026-07-16 at $199.24 |
| Daniel Durn | CFO | 0.6 | 2026-06-23 at $281.01 |

Notable: CEO Murphy 自 2026-04 至 09 幾乎每月固定賣出 7,500 股 (4/15、5/13、6/15、7/15、8/17、9/15), 10 月無紀錄, 疑似 10b5-1 排程, 未經 SEC 文件驗證。President Koopmans 2026-11-02 的 10,000 股賣出是最新一筆, 價格 186.97 USD, 較 7 月的 281.92 USD 低約 34%。2026 年 4 月前後有大量 RSU 歸屬相關的無價格交易 (例如 Murphy 938,324 股, 標示為非市價交易), 屬例行性質的可能性高, 但需 Form 4 確認。

解讀: 內部人 6 個月全為賣出, 無買入, 且賣價由 300 USD 附近降至 187 USD 附近。買入信號缺席, 賣出規模約 18.9M USD, 相對於約 877M 股流通量 (由 BlackRock 持股比例推算), 占比極小, 但方向一致。

## Ownership shifts

- 機構持股: 79.96%, 機構數 3,068 家。內部人持股: 1.23%。
- 前十大機構 (工具 `inst_holders`, 報告日期分屬 2026-06-30 與 2026-09-30):

| 機構 | 持股比例 | 持股數 (M 股) | 持股市值 (B USD) | 持股變動 |
|---|---|---|---|---|
| BlackRock | 9.77% | 85.6 | 13.4 | +34.1% |
| Vanguard Capital Mgmt | 6.60% | 57.9 | 9.1 | +48.1% |
| State Street | 4.75% | 41.6 | 6.5 | -0.5% |
| FMR (Fidelity) | 4.50% | 39.4 | 6.2 | -30.8% |
| Invesco | 3.84% | 33.7 | 5.3 | +11.2% |
| Geode | 2.47% | 21.7 | 3.4 | +2.6% |
| Vanguard Portfolio Mgmt | 2.40% | 21.0 | 3.3 | -36.7% |
| Goldman Sachs | 1.68% | 14.7 | 2.3 | +30.7% |
| Norges Bank | 1.62% | 14.2 | 2.2 | +34.8% |
| T. Rowe Price | 1.58% | 13.8 | 2.2 | +714% (低基期) |

趨勢: 被動與大型指數機構多數增持 (BlackRock、Vanguard CM、Invesco、Norges、Goldman), 主動型基金 FMR 明顯減碼。Vanguard 兩個實體的變動方向相反, 可能是申報主體切換所致, 不宜單獨解讀。報告日期多為 Q2 與 Q3 (6/30 與 9/30), 2026-11-14 前後的 Q3 13F 更新尚未納入, 持股變化的時效性有限。

## Net sentiment score

Composite: **中性 (neutral)**, 信心: 中低。

分項判斷:
- 分析師面: 偏多 (高)。43 家中 38 家 Buy 類, 無賣出, 但近月目標價下調, Buy 類淨減 5 家。
- 散戶面: 偏多但降溫 (中低信心)。最新量化讀數為 SentiSense 11/8 偏多, Reddit 中性; StockTwits 與 Reddit 直接資料缺失。
- 內部人面: 偏空 (中)。6 個月 0 買入、約 18.9M USD 賣出, 賣價區間明顯下移; 多為計畫性賣出, 不宜過度解讀。
- 機構面: 中性偏多。前十大中被動機構多數增持, 主動 FMR 減持。

Divergence flag: **否** (散戶與分析師方向相同, 皆偏多)。
需注意的是「分析師 vs 內部人」的分歧: 分析師維持 Buy 類多數評等, 內部人持續在較低價位賣出。此分歧不是散戶 vs 分析師的分歧, 但是另一類值得追蹤的訊號。

Caveats:
- 散戶面資料時效不足, 最新可量化讀數 (SentiSense 11/8) 之外, 其他為 6 月前後資料。
- 目標價與評等變動來自搜尋摘要, 日期與原始報告未逐一核對。
- 股價基準: 最新可見價格約 142 USD (11/9, Trefis), 與 11/2 內部人賣價 186.97 USD 相比, 反映併購公告後的跌幅。

SENTIMENT REPORT COMPLETE
