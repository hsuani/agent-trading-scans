# Sentiment — TLN as of 2026-10-28

## Analyst consensus
yf rec_summary（0m，即當期）：**20 家** — 6 Strong Buy / 12 Buy / 2 Hold / 0 Sell / 0 Strong Sell，即 18 Buy 類、2 Hold、0 Sell。

近期變化（yf recommendations，各期合計 Buy 類 / Hold / Sell）：

| 期間 | Strong Buy | Buy | Hold | Sell | 合計 |
|---|---|---|---|---|---|
| 0m（當期） | 6 | 12 | 2 | 0 | 20 |
| -1m | 6 | 9 | 2 | 0 | 17 |
| -2m | 6 | 10 | 2 | 0 | 18 |
| -3m | 6 | 9 | 2 | 0 | 17 |

- 最近三個月 Buy 類家數在 17–20 之間，Sell 始終為 0，Hold 穩定在 2。yf 工具只提供計數，無法辨識個別券商的升降評等。
- 目標價（二手來源，未經 yf 驗證）：
  - Jefferies 在 7 月將目標價由 $453 下修至 $422，評等 Hold（來源：Walnut Invest 摘要）。
  - Wells Fargo 在 7 月底將目標價上調至 $482（同上）。
  - MarketBeat 10 月初快照：平均目標價約 $460.08，共 8 Buy / 3 Hold / 1 Sell，與 yf 計數不一致。
  - TipRanks 平均目標價約 $437.30；Valueinvesting.io 區間 $310–$625。
- 來源計數不一致：Google Finance 為 12 家（10 Buy 類 / 2 Hold），24/7 Wall St 為 17 家（15 Buy / 2 Hold），以 yf 20 家為主要數據。
- 獨立評等：24/7 Wall St 給 HOLD、目標價 $356.86，為少數偏保守的聲音（二手來源）。

## Retail social
- **Reddit（r/wallstreetbets、r/stocks）**：DATA_UNAVAILABLE。WebFetch 回傳 "Claude Code is unable to fetch from www.reddit.com"，無法取得貼文標題、分數、留言數。WebSearch 也未找到 TLN 相關 r/wallstreetbets 討論串。
- **StockTwits**：DATA_UNAVAILABLE。api.stocktwits.com DNS 解析失敗（ENOTFOUND），需在 session 網路設定中允許該網域後才能重試。
- **X / 新聞與論壇（WebSearch）**：主要為媒體與分析師內容，缺乏真正的散戶貼文樣本。
  - 懷疑聲音：Jim Cramer 表示「That's Not for Me」，認為其他 AI 相關股票可能有更高上行空間、下行風險較低（來源：Yahoo Finance）。
  - 股價波動：不同快照顯示年初至今曾下跌約 23%，另一快照顯示一年漲幅約 70.8%。兩者日期不同，僅作背景參考。
  - Simply Wall St 社群頁顯示「No trending discussion available」。
- **聲量（相對一般水準）**：DATA_UNAVAILABLE。無 Reddit / StockTwits 計數，無法做量化比較。
- **散戶傾向**：DATA_UNAVAILABLE（無可靠樣本）。
- **Themes（僅就可取得的媒體內容歸納）**：AI 資料中心電力需求、核能供電合約、估值是否已反映利多，以及股價大幅波動本身。這些是媒體論述，不代表散戶共識。

## Insider activity
查詢區間：2026-04-28 至 2026-10-28（6 個月）。yf insider 資料中，多數 Form 4 的 `Value` 與 `Text` 為空，無法判斷是公開市場買賣或獎勵股（RSU / 年度董事授予）。

| 日期 | 申報人 | 職稱 | 性質 | 股數 | 金額（USD M） |
|---|---|---|---|---|---|
| 2026-06-15 | ABBAS GIZMAN I. | Director | 賣出 @ $380.00 | 2,600 | 0.99 |
| 2026-07-15 | NUTT TERRY L | President | 性質未標示（Ownership D） | 8,312 | 無數據 |
| 2026-05-22 | 多位董事與高管（MCFARLAND MARK ALLEN CEO、MULLER COLE CFO、BERRYMAN BRAD COO 等） | 多職 | 性質未標示，多筆股數相近，疑為年度授予 | 數千至約 35 萬股不等 | 無數據 |

- **Net 6mo**：已確認公開市場**買入 $0 M**；已確認公開市場**賣出約 $0.99 M**（1 筆，Director）。
- 其餘 May 22 與 Jul 15 申報項目性質不明，UNCLASSIFIED，不計入淨額。
- 過去一年的 RUBRIC CAPITAL MANAGEMENT（10% 以上持股人）賣出紀錄（2024-12 與 2025-06）超出 6 個月窗口，僅作背景。
- 6 個月內無 CEO / CFO 的已確認公開市場買入。

## Ownership shifts
- yf major_holders 快照：內部人持股 1.38%，機構持股 103.17%，機構家數 820。
- 機構持股超過 100%，屬資料異常（可能是多重計算或 float 口徑差異），本報告不採用該絕對數字。
- 機構持股趨勢（季度變化）：DATA_UNAVAILABLE。yf 僅提供單一快照，無時間序列。

## Net sentiment score
- **分析師面**：偏多（bullish），信心中高。20 家中 18 家為 Buy 類，0 家 Sell，近三個月無轉向跡象；但目標價分歧大（約 $310–$625 區間，24/7 Wall St 為 $356.86）。
- **內部人面**：中性偏弱（neutral-to-bearish），信心低。6 個月僅一筆已確認公開市場賣出（約 $0.99 M），無買入；多數申報性質不明。
- **散戶面**：DATA_UNAVAILABLE（Reddit 與 StockTwits 皆無法取得）。
- **綜合**：偏多（bullish），信心中等。綜合結論只能代表分析師與媒體面，無法反映散戶情緒，因此信心受限。

**Divergence flag：無法判定（DATA_UNAVAILABLE）**。散戶傾向缺失，無法確認是否與分析師傾向相反。在取得 Reddit / StockTwits 資料前，不應解讀為「無背離」。

## 資料缺口與來源說明
- yf：`recommendations`、`rec_summary`、`insider`、`major_holders` 均回傳資料；Yahoo cookie / crumb 取得失敗（ConnectionError），但仍有回傳，已依 cache fallback 規則使用。
- Reddit：WebFetch 被阻擋，DATA_UNAVAILABLE。
- StockTwits：DNS 失敗，DATA_UNAVAILABLE；需 session 網路允許 api.stocktwits.com。
- WebSearch 來源（二手，日期多為 2026-07 至 2026-10 初）：
  - stockanalysis.com、MarketBeat（2026-07-30、2026-10-06 快照）、Walnut Invest、TipRanks、Valueinvesting.io、247wallst、Simply Wall St、Yahoo Finance（Jim Cramer 文章）、Benzinga sentiment（9 月快照，short interest 5.0% of float，已過時）。
- 股價參考：最近一筆找到的收盤價為 $378.57（2026-10-09，二手來源，未經 yf 驗證）。本報告未使用任何 2026-10-28 之後的資料。

SENTIMENT REPORT COMPLETE
