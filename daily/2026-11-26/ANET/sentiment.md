# Sentiment — ANET as of 2026-11-26

## Analyst consensus
目前 30 家覆蓋中 30 家為 buy 等級（9 Strong Buy + 21 Buy）、0 hold、0 sell。
（來源：yf rec_summary，0m 期間）

近四個月趨勢（strongBuy / buy / hold / sell）：

| 期間 | Strong Buy | Buy | Hold | Sell | 合計 |
|---|---|---|---|---|---|
| 當期 (0m) | 9 | 21 | 0 | 0 | 30 |
| -1m | 7 | 24 | 1 | 0 | 32 |
| -2m | 7 | 24 | 1 | 0 | 32 |
| -3m | 8 | 23 | 0 | 0 | 31 |

- 近一個月變化：Strong Buy 由 7 升至 9，唯一一家 hold 消失，覆蓋家數由 32 降為 30。無賣方評級出現。hold 消失的原因（升評、剔除覆蓋或資料更新）工具資料無法判定。
- 評級變動明細（upgrade / downgrade 紀錄）與目標價：yf `recommendations` 只回傳聚合計數，未提供個別券商變動紀錄，目標價也無法從工具取得，本報告無法列出個別調評與目標價變化。
- 外部搜尋提到 Rosenblatt 曾升至 Buy（發布日期無法確認）；另有 2025 年 11 月的 Neutral 舊評等，已過時，不採信為當前評等。
- 外部搜尋提到估值爭議：一篇 Seeking Alpha 降評文章指 ANET 的 EV/EBITDA 超過 40x，高於同業（日期未確認）。
- 資料衝突：外部網站顯示的股價（約 $130 與約 $187）與內部人交易價格區間不一致，推估是不同時點擷取所致。本報告以 yf 內部人交易價格為準。

## Retail social
- Reddit（r/wallstreetbets、r/stocks）：WebFetch 回傳 "unable to fetch from www.reddit.com"，無法取得貼文樣本與情緒傾向。此來源失效，未納入評分。
- StockTwits：api.stocktwits.com DNS 解析失敗（ENOTFOUND），需於 session 網路設定中允許該網域後才能取得。未納入評分。
- X / 新聞聊天：WebSearch 結果以自動化追蹤站為主。AltIndex（截至 2026-10-16）估計 Reddit 每日提及約 1 次、低於近期平均約 52%，情緒分數 88/100（偏多）。該站為自動化估計，可信度低。Quiver 的 X 摘要提到部分發文者擔心營業利益率指引可能不如預期。
- 聲量：整體低於平常水準（依 AltIndex 估計，為定性判斷，無實際提及數可驗證）。
- 情緒傾向：依有限的外部追蹤，偏多（low confidence）。
- 主要主題（依外部摘要）：
  - AI 網路與超大規模資料中心需求，800G 向 1.6T 升級週期
  - 營業利益率指引是否達標的疑慮
  - 估值偏高（EV/EBITDA 40x 以上）與股價波動大（beta 約 2.2，來源為較舊的 Finimize 資料）
- 財報脈絡：Q3（截至 2026-09-30）於 11/3 盤後公布；11/4 股價收跌 2.6%（Barchart，外部來源）。

## Insider activity
區間：2026-05-26 至 2026-11-26（6 個月）。資料共 60 筆交易。

Net 6mo: $0 buys, $1.33B sells（不含 7 筆 derivative conversion 與 1 筆 CEO 的 890,000 股贈與，贈與無金額）。

| 內部人 | 職位 | 6mo 賣出金額（USD） | 賣出股數 | 筆數 |
|---|---|---|---|---|
| Andreas Bechtolsheim | 持股超過 10% 之受益人 | $702M | 3.92M | 14 |
| Jayshree Ullal | CEO | $580M | 2.86M | 11 |
| Kenneth Duda | President | $39.5M | 0.22M | 6 |
| Mark Templeton | 董事 | $2.8M | 15K | 3 |
| Charles Giancarlo | 董事 | $2.7M | 16K | 2 |
| Chantelle Breithaupt | CFO | $0.8M | 4.3K | 3 |
| Lewis Chew | 董事 | $0.5M | 2.5K | 1 |
| Kelly Battles | 董事 | $0.1M | 422 | 1 |

- 買進：6 個月內無任何公開市場買進紀錄。
- 近期動向：Bechtolsheim 於 11/18 賣出約 $56M（價格 $183.60–195.17），11/5–11/6 合計約 $87M。CEO Ullal 於 10/6–10/9 賣出約 $132M（價格約 $211–217），11/17 有 890,000 股贈與。
- 賣出價格區間：6 個月內約 $154–$217，近期（11 月）約 $140–$196。
- 本工具未標示交易是否屬 10b5-1 預定計畫，無法判斷賣出是否為計畫性、分散持股或主動減持。
- 解讀：大額、持續、單向的賣出，對應到的是高階主管與大股東，而非董事或一般員工，可視為偏空的內部人訊號。但缺乏買進紀錄與計畫標示，強度需保留。

## Ownership shifts
- 內部人持股：17.2%
- 機構持股：73.1%（浮動股中占 88.4%）
- 機構家數：3,311
- 工具只提供單一時點快照，無法判斷季度變化趨勢。機構集中度屬高，但趨勢欄位標示為無資料。

## Net sentiment score
Composite: **偏多，但內部人賣出是明顯反向訊號（信心：中）**

- 分析師：強烈偏多（30/30 buy 類，0 sell，近月 Strong Buy 增加）。信心高。
- 內部人：偏空（$1.33B 賣出、0 買進，賣方包含 CEO 與大股東）。信心中，因缺乏 10b5-1 標示。
- 散戶：低聲量、偏多（依自動化追蹤站）。信心低，Reddit 與 StockTwits 皆未能取得實際樣本。
- 整體：分析師與散戶方向一致偏多，內部人方向相反。

Divergence flag: **否** — 散戶傾向（偏多，低信心）與分析師傾向（偏多）方向一致，未出現兩者相反的情況。
附註：內部人賣出與分析師偏多方向相反，屬於另一種分歧，值得在後續辯論中檢視。

資料缺口：Reddit、StockTwits 皆無法取得；yf 不提供評級變動明細與目標價；機構持股無趨勢資料。以上缺口會降低散戶面的評分信心。

SENTIMENT REPORT COMPLETE
