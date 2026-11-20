# Sentiment — 6515.TW (穎崴 WinWay Technology) as of 2026-11-20

本次資料的主要缺口是 Reddit、StockTwits 與內部人交易。

## Analyst consensus
目前 12 buy / 0 hold / 0 sell (strongBuy 4、buy 8)，來源為 yf rec_summary，期間 0m。

| 期間 | strongBuy | buy | hold | sell | strongSell | 買方合計 |
|---|---|---|---|---|---|---|
| 0m (目前) | 4 | 8 | 0 | 0 | 0 | 12 |
| -1m | 4 | 8 | 0 | 0 | 0 | 12 |
| -2m | 4 | 7 | 0 | 0 | 0 | 11 |
| -3m | 4 | 7 | 0 | 0 | 0 | 11 |

- 近 3 個月沒有降評，也沒有出現 hold 或 sell。買方家數從 11 增至 12，增幅為 1 家。
- 近一個月沒有評級變動。
- 目標價: yf 工具沒有提供目標價歷史。網頁快照 (investing.com 與 stockanalysis.com，日期約為 2026 年 8 至 10 月，彼此不一致) 顯示平均 12 個月目標價約 11,093 TWD，家數在 10 至 11 之間。這些數字無法對應到 11 月 20 日。
- 近期事件: 網頁資料顯示下次財報日為 2026-11-06，這一天已經過去，但沒有找到財報後的分析師修正資料。這是本次最大的時間缺口。

## Retail social
- Reddit (r/wallstreetbets、r/stocks): 無法取得。WebFetch 回應 "Claude Code is unable to fetch from www.reddit.com"，兩個子版都失敗，因此沒有討論串、分數或 tilt 可引用。
- StockTwits: 無法取得。api.stocktwits.com DNS 解析失敗 (ENOTFOUND)，需要在工作階段網路設定中允許此網域後才能重試。
- X / 新聞討論: WebSearch 沒有找到 2026 年 11 月的散戶意見。搜尋結果主要是券商與資料站的技術面、共識與目標價頁面，不是散戶貼文。
- 聲量: 無法量測，因此無法與平常水準比較。
- Tilt: 無法判定。
- Themes: 無資料。

## Insider activity
Net 6mo: 無資料。yf insider 回傳空陣列 `[]`。空陣列可能代表近 6 個月沒有內部人交易，也可能代表資料來源缺漏，兩者無法從這個工具區分。目前也沒有 CEO、CFO 或其他人員的交易紀錄。

## Ownership shifts
來源為 yf major_holders，為單一時點快照，沒有趨勢資料。
- 內部人持股: 約 29.4%
- 機構持股 (佔流通股): 約 42.3%
- 機構持股 (佔總股本): 約 29.9%
- 機構家數: 118
目前無法判斷機構是加碼還是減碼。

## Net sentiment score
Composite: **偏多 (bullish)**，信心 **低**。

判斷依據:
- 分析師面偏多: 12 買 / 0 賣，近 3 個月沒有降評，這部分信心較高。
- 散戶面無資料，無法納入。
- 內部人面無資料，無法納入。
- 因為兩個重要來源缺漏，整體信心只能給低。

Divergence flag: **無法判定**。散戶 tilt 沒有取得，因此無法確認是否與分析師方向相反。

## 資料品質與缺口摘要
1. Reddit: 失敗 (WebFetch 無法連線)。
2. StockTwits: 失敗 (DNS 無法解析，需要網路白名單)。
3. 內部人交易: 空陣列，無法確認是真的沒有交易還是資料缺漏。
4. 分析師家數在 yf (12) 與網頁 (10 至 11) 之間有差距，yf 是本次採用的數字。
5. 網頁資料日期介於 8 至 10 月，沒有 11 月資料。財報 (11/06) 後的修正未找到。

SENTIMENT REPORT COMPLETE
