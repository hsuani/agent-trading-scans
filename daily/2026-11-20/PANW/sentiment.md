# Sentiment — PANW as of 2026-11-20

## Analyst consensus
Yahoo rec_summary（當期 0m，共 54 位分析師）: Strong Buy 10 / Buy 32 / Hold 11 / Sell 1 / Strong Sell 0。買方合計 42 (約 78%)，持有 11 (約 20%)，賣方 1 (約 2%)。

近 3 個月趨勢（-3m → 0m）:
| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell |
|---|---|---|---|---|---|
| -3m | 11 | 33 | 9 | 1 | 1 |
| -2m | 10 | 32 | 11 | 1 | 1 |
| -1m | 10 | 32 | 12 | 1 | 0 |
| 0m | 10 | 32 | 11 | 1 | 0 |

趨勢: 買方由 44 降至 42，持有由 9 增至 11，強烈賣出由 1 降為 0。整體仍偏多，但評級有小幅向持有收斂的跡象。

近期評級變動: 工具只回傳彙總計數，沒有個別升降評事件，無法列出具體 upgrade/downgrade。網路資料顯示 Jefferies 曾調降目標價，當日股價下跌約 5%（日期未能確認）；KeyBanc 在 11/18 財報前轉為偏多（來源為摘要，日期未確認）。目標價的完整時間序列未取得。

資料注意: web 摘要引用的另一組數字為 54 位中 40 Strong Buy / 3 Moderate Buy / 11 Hold，與 Yahoo 分類不同，兩者未能對齊，本報告以 Yahoo 為準。

## Retail social
- Reddit (r/wallstreetbets, r/stocks): 資料無法取得（WebFetch 回報 "unable to fetch from www.reddit.com"，已軟失敗）。
- StockTwits: 資料無法取得（api.stocktwits.com DNS 解析失敗，需在 session 網路設定中允許該網域；未重試）。
- X / 新聞: web 搜尋可見的散戶相關文章包括 StockTwits 的 "retail chatter" 報導與 pandaforecast 的 KeyBanc 轉多文章，但多數結果為 2024–2025 年舊文，無法確認近期聲量。
- 聲量 (qualitative): 無法量化，目前只能判定為資料缺口。
- 代表性標題 (≤15 字): TIKR 於 11/14 報導 "Palo Alto Networks sank nearly 10 in a day"，主旋律為 CEO 仍看好 AI 長期需求，屬偏多論述在股價重挫後的延續。
- 主題（由 web 摘要歸納，非社群原文）: 估值偏高（Trefis: 約 88x 遠期 P/E，高於 5 年平均 57x）、股價自 10 月高點回落約 26.5%、財報前選擇權隱含波動約 11%、AI 需求為主要多方論點。

## Insider activity
統計區間: 2026-05-20 至 2026-11-20（近 6 個月）。

Net 6mo: 買入 $0M（區間內無公開市場買入）/ 賣出約 $67.8M（21 筆）。
- 最近一次公開市場買入: CEO Nikesh Arora，2026-03-27，約 $10.0M，價格約 $146.9–147.5（已超出 6 個月區間）。
- 其餘在 2026-10-30 的股票授予（CFO、President、CTO、Officer）為 $0 價格配發，不計入買賣淨額。

依人員的賣出金額（M USD）:
| 人員 | 職位 | 6mo 賣出 (M USD) | 近期交易 |
|---|---|---|---|
| William D. Jenkins Jr. | President | 19.9 | 2026-11-02/04，約 $342–367 |
| Lee Klarich | CTO | 16.3 | 2026-05-22，約 $250–261 |
| Dipak Golechha | CFO | 12.2 | 2026-09-24 $10.8M；06-23 $1.4M |
| James J. Goetz | 董事（間接持有） | 13.1 | 2026-09-17、06-12 |
| John P. Key | 董事 | 3.0 | 2026-09-14、06-12 |
| Joshua D. Paul | Officer | 1.5 | 多筆小額，2026-10-01 最近 |
| Aparna Bawa | 董事（間接持有） | 1.5 | 多筆小額，2026-09-24 最近 |
| Helle Thorning-Schmidt | 董事 | 0.2 | 2026-07-07 |

Notable: Jenkins（President）於 2026-11-02 至 11-04 在約 $342–367 區間賣出約 $19.9M 合計，是區間內最近且金額最大的一組。CFO 與 CTO 在 9 月及 5 月亦有大額賣出。賣出多伴隨選擇權行使（例如 Klarich 的 Conversion of Exercise 後隨即賣出），部分可能屬 10b5-1 計畫，但資料無法確認。內部人持股僅 0.66%。

## Ownership shifts
- 機構持股 84.3%（機構數 4,070），浮動股機構持股 84.9%。
- 趨勢: 工具只提供單一快照，無歷史序列，無法判定集中度是增加或減少。

## Net sentiment score
Composite: **中性偏空 (信心: 低)**。

- 分析師: 偏多（買方約 78%，但近 3 個月買方略減、持有略增）。
- 內部人: 偏空（6 個月淨賣約 $67.8M、0 筆公開市場買入，價格區間高於 3 月 CEO 買入時的約 $147）。
- 散戶: 無資料，不納入計分。
- 外部事件: 股價自高點回落約 26.5%，財報於 11/18 公布，但本次搜尋無法取得實際財報結果與市場反應。

Divergence flag: **無法判定（散戶資料缺口）**。
分析師與內部人方向分歧: **是**。分析師多數偏多，內部人持續大額賣出，此分歧需於辯論中追蹤。

資料缺口與風險:
1. 11/18 財報實際結果未確認（web 搜尋僅回傳 2025 年及 2026 年 5 月的舊資料）。若財報結果已公布，綜合評分可能顯著改變，需以主要來源（PANW 投資人關係頁或財經媒體）覆核。
2. Reddit 與 StockTwits 均無法取得，散戶面向為空白。
3. 分析師評級歷史的個別升降事件未取得。
4. 單位說明: 所有金額皆為 USD，以 M USD 標示；已抽樣驗算 Jenkins 2026-11-04 交易（37,992 股 × 約 $352 ≈ $13.4M，與工具值 $13.38M 相符）。

SENTIMENT REPORT COMPLETE
