# Sentiment — WDC as of 2026-11-18

資料說明: yf 資料為快取回退 (cookie/crumb 取得失敗, 屬預期行為)。Reddit 直接抓取被封鎖, StockTwits 網域無法解析 (DNS ENOTFOUND)。散戶與社群部分以 WebSearch 聚合站資料替代, 時間戳記多在 2026 年 7–8 月, 不代表當前狀態。未引用任何舊日期 daily 報告。

## Analyst consensus

目前 26 位分析師: 5 Strong Buy / 17 Buy / 4 Hold / 0 Sell / 0 Strong Sell。買進方 (含 Strong Buy) 共 22 位 (約 85%), 賣出方為 0。

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell |
|---|---|---|---|---|---|
| 當月 (0m) | 5 | 17 | 4 | 0 | 0 |
| 前 1 月 (-1m) | 4 | 17 | 5 | 0 | 0 |
| 前 2 月 (-2m) | 4 | 17 | 5 | 0 | 0 |
| 前 3 月 (-3m) | 4 | 17 | 5 | 0 | 0 |

近一個月變化: Strong Buy +1, Hold -1, 其餘不變。

Recent moves (來源為 WebSearch 聚合站, 未經一手公告核實):
- Summit Insights 於 2026-08-06 由 Buy 降為 Hold。
- Cantor Fitzgerald 於 2026-10-23 目標價由 $900 調降至 $625。
- Evercore ISI 目標價調高至 $575 (由 $410), 該次股價約上漲 9%, 日期未確認。
- Goldman Sachs 維持 Neutral, 目標價據報由 $400 調高至 $650, 來源為社群摘要, 待核實。
- Bernstein 升評為 Outperform, 目標價 $340 (由 $170), 日期不明。

限制: `yf recommendations` 僅回傳各期計數, 無逐筆升降評與目標價變動明細, 逐筆評等歷史為 DATA_UNAVAILABLE。

## Retail social

- Reddit (r/wallstreetbets, r/stocks): DATA_UNAVAILABLE。直接 JSON 抓取被封鎖。聚合站 (AltIndex) 顯示 2026-02 曾出現高峰 (該週情緒指數 81, 極度看多), 7 月前後提及量約每日 12 則, 較近期平均低 46%, 情緒 82/100 偏多。此為 7 月前資料, 不代表 11 月狀態。
- StockTwits / X: StockTwits DNS 無法解析, DATA_UNAVAILABLE。X 未取得可靠樣本。WebSearch 聚合摘要整體語氣偏空 (近期 11 月股價大跌與降評、期權偏空、空單比率 5.7% 且上升), 但來源時間混雜, 信心低。
- 討論量 (定性): 無當前數據, 無法與常態比較, 判定 DATA_UNAVAILABLE。
- 主要題材 (依聚合來源歸納, 非原始貼文): AI 儲存與 HDD 需求 (產能被超額預訂)、超大規模雲端客戶占比、估值 (P/E 高於歷史均值) 與高位追價風險、內部人持續賣出、分析師降評與目標價調降。
- 散戶傾向: 當前無法判定。歷史上偏多, 近期聚合來源偏空, 兩者不可相互取代。

## Insider activity

Net 6mo (2026-05-18 至 2026-11-18): $0 買進 / 約 $26.6M 賣出 (18 筆公開市場賣出; 已排除 Stock Award / Stock Gift 等非市場交易)。

| 內部人 | 職位 | 6mo 賣出 (USD M) | 最近一筆 |
|---|---|---|---|
| TAN IRVING | CEO | 15.07 | 2026-11-13, 20,000 股, 約 $305–311 |
| COLE MARTIN I | Director | 3.87 | 2026-07-28, 約 $424–465 |
| TREGILLIS CYNTHIA LOCK | Officer | 2.61 | 2026-10-21, 807 股, $380 |
| STREETER STEPHANIE A | Director (間接持股) | 2.52 | 2026-09-01, 5,600 股, 約 $447–455 |
| GUBBI VIDYADHARA K | Officer | 2.21 | 2026-09-04, 1,795 股, $459.87 |
| KIDDOO BRUCE E | Director | 0.40 | 2026-05-28, 750 股, $528.52 |

Notable:
- CEO Irving 在窗口內兩次大額賣出: 2026-08-11 (20,000 股, $8.90M) 與 2026-11-13 (20,000 股, $6.17M)。另 2026-09-01 有一筆 112,500 股的贈與 (Stock Gift), 不計入市場交易。
- 窗口外 (僅供背景, 未計入): CEO 2026-05-01 賣出 $8.24M。
- 多數內部人賣出的價格區間高於 2026-11-13 的 CEO 賣出價; 11/17 快取報價約 $279.55, 低於近期賣出價。
- 數據中無任何窗口內的公開市場買進。是否屬 10b5-1 預定計畫無法由資料判定。

## Ownership shifts

- 機構持股: 88.6% (2,405 家機構); 內部人持股 0.38%。
- 前十大持股 (2026-09-30 申報, 百分比為 QoQ 變動):

| 機構 | 持股比例 | 股數 (M) | 市值 (USD B) | QoQ 股數變動 |
|---|---|---|---|---|
| BlackRock | 9.09% | 34.04 | 9.39 | +3.3% |
| FMR, LLC | 8.43% | 31.57 | 8.71 | +21.5% |
| Vanguard Capital Mgmt | 6.16% | 23.07 | 6.36 | +2.5% |
| Capital World Investors | 5.75% | 21.52 | 5.94 | +29.7% |
| State Street | 4.47% | 16.73 | 4.62 | +2.8% |
| Invesco | 3.56% | 13.31 | 3.67 | -7.8% |
| JPMorgan Chase | 3.13% | 11.72 | 3.23 | -31.1% |
| Geode Capital | 2.38% | 8.92 | 2.46 | +6.1% |
| Morgan Stanley | 2.31% | 8.63 | 2.38 | +6.0% |
| Vanguard Portfolio Mgmt | 2.25% | 8.42 | 2.32 | -35.7% |

- 交叉檢查: BlackRock 市值 $9.39B ÷ 34.04M 股 ≈ $276/股, 與 9/30 價位相符; 由 9.09% 反推流通股約 374M 股。
- 趨勢: 主動型基金 (FMR、Capital World) 加碼, 部分指數與大型機構 (JPM、Vanguard PM) 減碼, 整體集中度高且略偏增持。持股變動為 13F 季報, 時效落後。

## Net sentiment score

Composite: **中性偏分歧** (信心: 低至中)

- 分析師 (偏多, 信心中高): 22 買 / 4 持有 / 0 賣, 近月 Strong Buy 增加。但個別機構近期降評與目標價調降 (Summit、Cantor) 顯示共識正在鬆動。
- 內部人 (偏空, 信心中高): 6 個月約 $26.6M 賣出, 零買進, CEO 於 11/13 再次大額賣出。
- 散戶 (無法判定, 信心低): Reddit、StockTwits、X 當前資料皆 DATA_UNAVAILABLE; 聚合來源為 7–8 月資料, 偏多轉偏空, 無法定論。
- 機構持股 (中性偏多): 前十大多數持續增持, 但部分大型持股減碼。

Divergence flag: **是** — 分析師 (偏多) 與內部人 (偏空) 方向相反; 散戶方向無當前資料, 無法判定與分析師是否背離。

資料缺口清單 (DATA_UNAVAILABLE):
- Reddit 當前貼文與情緒 (r/wallstreetbets、r/stocks)
- StockTwits 訊息流 (api.stocktwits.com 網域未允許)
- 逐筆分析師升降評與目標價歷史 (yf recommendations 僅回傳計數)
- 當前散戶討論量 (相對常態)

本報告不含交易建議。

SENTIMENT REPORT COMPLETE
