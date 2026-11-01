# Sentiment — AVGO as of 2026-11-02

## Analyst consensus

資料來源: `pipeline/tools/yf AVGO rec_summary`（工具快照，未標註日期）

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell |
|---|---|---|---|---|---|
| 0m（最新） | 8 | 41 | 2 | 0 | 0 |
| -1m | 7 | 40 | 3 | 0 | 0 |
| -2m | 8 | 37 | 4 | 0 | 0 |
| -3m | 7 | 37 | 4 | 0 | 0 |

最新分布: **49 buy / 2 hold / 0 sell**。過去三個月 Buy 家數由 44 增至 49，Hold 由 4 減至 2，評級持續上調，無賣方評級。

近期評級變動（WebSearch 聚合，單一來源或未交叉驗證，依可信度排列）:
- Macquarie 於 2026-09-03 升至 Outperform，目標價 $490（Yahoo Finance）。但 Benzinga 與 StreetInsider 記載 2026-06-04 Macquarie 為降至 Neutral、目標價 $437，兩者矛盾，此升評未獲第二來源證實。
- Erste Group 2026-07-07 由 Buy 降至 Hold（Benzinga、aktien.guide）。
- Seaport Global 2026-04 降至 Neutral（Benzinga）。
- Wells Fargo 2026-01 升至 Overweight，目標價 $430（Benzinga）。
- 未搜尋到 2026-10 月內的評級或目標價變動。
- 目標價（未標註日期，聚合站）: Goldman Buy $525、Citi Buy $500、KeyBanc $460（由 $420 上調）、BofA 上調至 $530（由 $450）、JPMorgan 上調至 $580（由 $500）、Jefferies 上調至 $550（由 $500）。聚合平均約 $515–525，區間約 $216–675（低端異常，疑為資料錯誤）。
- 來源不一致: 網頁聚合顯示 44 buy / 4 hold，與工具 49 / 2 / 0 不符。以工具數值為準。

## Retail social

- **Reddit**: 無法存取（WebFetch 回傳無法連線 www.reddit.com）。r/wallstreetbets 與 r/stocks 皆未取得樣本。WebSearch 亦未找到 Reddit 討論串。**無法判斷散戶傾向。**
- **StockTwits / X**: `api.stocktwits.com` DNS 解析失敗（需在 session 網路設定中允許此網域）。改以 WebSearch 聚合的二手報導判斷: 報導指 StockTwits 上 AVGO 情緒於 Q2 財報前後轉為 "extremely bullish"，訊息量大增（報導稱超過 700%/週）。另一篇報導於股價回檔時仍維持極度看多，有用戶稱下跌為過度反應。報導日期多集中於 2026 年 Q2（約 6 月），非 11 月當期。
- **X / 選擇權流**: 2026-02 的選擇權流分析顯示 call 部位偏多，但提到關稅疑慮與技術面偏弱。資料已過時。
- **Buzz 量**: 無法量化。依二手報導，Q2 財報前後聲量明顯高於平常，目前無可驗證數字。
- **Themes（僅來自二手報導）**: AI 客製晶片（Google TPU 需求）、財報後 AI 營收加速、競爭風險（Marvell 與 Google 的客製晶片合約曾使股價單日下跌約 4.6%）、關稅與估值。

## Insider activity

資料來源: `pipeline/tools/yf AVGO insider`。6 個月窗口為 2026-05-02 至 2026-11-02。

**注意: 工具回傳的最新一筆交易為 2026-07-10。窗口內 07-10 之後無任何紀錄，可能是資料延遲或更新中斷，需確認。**

| 類別 | 金額（M USD） | 筆數 |
|---|---|---|
| 賣出（窗口內） | 約 283.7 | 7 |
| 買入（窗口內） | 0.37 | 1 |
| 淨額 | 約 -283.3 | — |

明細（窗口內，M USD）:
- Henry Samueli（董事）2026-06-24 賣出 654,241 股，約 250.0M，為最大單筆。同日另有 336,893 股贈與（無金額）。
- Mark David Brazeal（Officer）2026-06-17 至 07-10 共 4 筆賣出，合計約 32.4M。
- Gayla J. Delly（董事）2026-07-08 賣出約 0.73M。Justine F. Page（董事）2026-06-29 賣出約 0.6M。
- Harry L. You（董事）2026-06-11 買入 1,000 股，約 0.37M，為窗口內唯一買入。
- CFO Amie O'Toole 2026-06-15 為 50,000 股獎勵（無現金交易）。
- CEO Hock E. Tan 窗口內無公開市場賣出（最後一次賣出為 2026-01-06，之後僅有 2026-04-08 贈與）。
- CFO Kirsten Spears 最後一次賣出為 2026-03-17。

趨勢: 2025 年全年均有持續性賣出（Samueli、Tan、Brazeal 為主），買入極少（僅 Harry You 數次小額）。賣出多集中於股價高點，但無法區分是否為 10b5-1 排程。

## Ownership shifts

- 內部人持股約 1.9%；機構持股約 79.9%；機構家數 6,273（工具單一快照）。
- 無歷史快照，無法判斷機構集中度趨勢。

## Net sentiment score

- **分析師面**: 偏多（49 buy / 2 hold / 0 sell，評級持續上調）。
- **散戶面**: 偏多，但資料薄弱（僅二手報導，Reddit 與 StockTwits 直連皆失敗）。
- **內部人面**: 偏空（6 個月淨賣約 283M USD，主要為董事大額賣出；買入極少）。但窗口末端資料可能不完整。

**綜合: 偏多（bullish），信心度中低。** 主要支撐為分析師一致性。內部人大額賣出與資料缺口拉低信心。

**Divergence flag: 否（散戶與分析師方向一致，皆為偏多，但散戶面證據不足）。** 內部人（偏空）與分析師（偏多）方向相反，此為需追蹤的訊號。

## 資料缺口與待辦
1. Reddit（r/wallstreetbets、r/stocks）無法存取，散戶面無一手資料。
2. `api.stocktwits.com` 需在 session 網路設定中允許後重試。
3. 內部人交易最新為 2026-07-10，需確認是否為資料延遲。
4. 分析師評級在 Macquarie 的 2026-09 升評有矛盾，未獲第二來源證實。

SENTIMENT REPORT COMPLETE
