# Sentiment — NBIS as of 2026-11-16

資料說明: 系統日期為 2026-11-15，報告以 2026-11-16 為 as-of。yf 工具最新內部人交易為 2026-10-29，機構持股為 2026-09-30 申報期。Reddit、StockTwits 無法連線 (見下方), 散戶面向僅能以新聞搜尋替代。

## Analyst consensus
目前 (period 0m) 共 22 家: 15 buy (含 2 strongBuy) / 6 hold / 1 sell (strongSell 0)。買進比例約 68%。

趨勢 (yf rec_summary 四期快照):

| 期間 | strongBuy | buy | hold | sell | strongSell | 合計 |
|---|---|---|---|---|---|---|
| 0m (現在) | 2 | 13 | 6 | 1 | 0 | 22 |
| -1m | 2 | 13 | 6 | 1 | 0 | 22 |
| -2m | 2 | 12 | 5 | 1 | 1 | 21 |
| -3m | 1 | 10 | 6 | 0 | 1 | 18 |

Recent moves: yf 工具只提供計數快照，沒有逐筆升降評等紀錄，無法確認個別券商的 upgrade/downgrade。買進 (含 strongBuy) 由 -3m 的 11 增至現在的 15；賣出 (含 strongSell) 由 -2m 的 2 降至現在的 1，整體評等上調。

目標價 (來自 WebSearch 新聞，未經 yf 驗證，且日期不一致): 
- 平均目標價約 USD 281 (S&P Global 彙整，22 家，截至 10/29)
- Morgan Stanley Equal Weight，USD 144
- Piper Sandler Neutral，USD 185
- Citigroup Buy，USD 265
- Bank of America Buy，USD 310

新聞中的股價約 USD 154 (11/11 盤前反彈後)，前一收盤約 USD 134 (11/10)。這兩個價格來自搜尋摘要，未以行情資料核對。

## Retail social
- Reddit (r/wallstreetbets, r/stocks): 無法取得。WebFetch 被封鎖 ("unable to fetch from www.reddit.com")，無貼文樣本、無提及次數、無情緒傾向數據。
- StockTwits: 無法取得。api.stocktwits.com 解析失敗 (ENOTFOUND)，該主機可能不在本 session 允許清單內。
- X / 新聞搜尋 (WebSearch, 替代來源): 近期 11 月文章偏多的分析師觀點，同時有空頭論點。可取的標題例: 「Nebius Lost 35% Last Month As Contagion Spikes」(247wallst, 2026-11-02)，標題屬空頭語氣，內文卻引用買方分析師看多目標。
- 提及量 vs 常態: 無法量化。僅能說明 11 月初有明顯的股價回檔新聞 (月跌約 35%)，這類事件通常會拉高討論量，但沒有資料可證實。
- 散戶傾向: 無法判定 (bullish / bearish / mixed 皆不下結論)。

Themes (僅來自新聞，非散戶原文):
1. AI 基礎設施需求與資本支出: 新聞多以 AI 資料中心擴張為多方論點。
2. 稀釋與可轉換債風險: 空方論點集中於資本支出、可轉債與股份稀釋。
3. 現金部位: 約 USD 4.8B 現金被引用為可撐數季的依據。
4. Q3 財報預期: 營收預估約 USD 907M，YoY 約 +521%，EPS 預估虧損約 USD 0.60–0.70。這些數字來自單一來源，未核對實際財報，文中亦未找到實際結果。
5. 同業連動: CoreWeave 財報強勁帶動 AI 基礎設施股反彈。

## Insider activity
過去 6 個月 (2026-05-16 至 2026-11-15，去除獎勵授予與重複列) :
- 買進: USD 0.26M (全部為董事 GRIMME ARNE，2026-10-19 至 10-28，價位約 USD 154–170)
- 賣出: USD 196.7M
- 淨額: 約 USD -196.5M (以賣出為主)

主要交易:

| 日期 | 姓名 | 職稱 | 方向 | 股數 | 金額 (USD M) |
|---|---|---|---|---|---|
| 2026-10-05 | NAVE OPHIR | COO | 賣出 @ ~231–244 | 500,000 | 117.8 |
| 2026-10-01 | VOLOZH ARKADY | CEO | 賣出 @ 234.16 | 37,778 | 8.8 |
| 2026-10-01 | KOROLENKO ANDREY | Officer | 賣出 @ 234.16 | 29,090 | 6.8 |
| 2026-10-01 | SHTAN DANILA | CTO | 賣出 @ 234.16 | 14,546 | 3.4 |
| 2026-08-14 | RYAN CHARLES E | 董事 | 賣出 @ 263–270 | 50,000 | 13.3 |
| 2026-10-28 至 10-19 | GRIMME ARNE | 董事 | 買進 (4 筆) | 1,570 | 0.26 |
| 2026-09-01 | ALONSO SANCHEZ MARIA DEL DADO | CFO | 賣出 @ 196.00 | 470 | 0.09 |

核對: VOLOZH 37,778 股 × 234.16 ≈ USD 8.85M，與 yf 申報值 USD 8,846,096 相符。

觀察:
- 金額最大的一筆為 NAVE 2026-10-05 (50 萬股，USD 117.8M)，約佔 6 個月賣出總額的六成；第二大為 RYAN 2026-08-14 (USD 13.3M)。注意: KOROLENKO 2026-05-13 的 50 萬股賣出 (USD 101.6M) 落在 6 個月窗口之前，未計入上表與淨額。
- 多數 CEO / CTO / Officer 的賣出集中在季初 (3/31、4/1、7/1、10/1)，且金額相近，可能是既定計畫或歸屬後的例行賣出，需查 Form 4 的 10b5-1 註記才能確認，本報告無法確定。
- 唯一的買進來自一位董事，且金額很小。
- 9/1 有多位董事與高管的股票獎勵授予 (1,352 股，無現金流)，不計入淨額。

## Ownership shifts
- 機構持股: 67.1% (佔流通股 70.4%)，機構數 1,485 家。
- 內部人持股: 4.7%。
- 前十大機構 (申報期變動):
  - 增持: Goldman Sachs +218% (6/30)、Bank of America +310% (6/30)、Situational Awareness LP +100% (6/30)、BlackRock +16% (6/30)、Invesco +10% (9/30)、State Street +8% (9/30)
  - 減持: Orbis Allan Gray -22% (6/30)、Fred Alger -40% (6/30)、UBS -3% (9/30)
  - 持有量最大: BlackRock 5.25%、Goldman 4.47%
- 趨勢: 機構持股比重的歷史序列不可得，只能看到單一快照。前十大中增持與減持的家數接近，且增持多為大型券商的交易部位，難以判斷長期配置方向。

## Net sentiment score
Composite: **中性偏多 (信心: 低)**

依據:
- 分析師: 偏多 (68% buy，近三月評等上調)
- 內部人: 明顯偏空 (6 個月賣出約 USD 196.7M 對 買進約 USD 0.26M)
- 散戶: 無資料
- 新聞: 多空並陳，AI 需求為多方主軸，稀釋與資本支出為空方主軸

信心偏低的原因: 散戶來源全數失效，且內部人與分析師方向相反，僅能以分析師評等為主要依據。

Divergence flag: **是** — 分析師偏多與內部人大量賣出方向相反。散戶傾向無法判定，因此無法確認散戶是否與分析師相反。

## Source notes
- Reddit: 封鎖，無法取得
- StockTwits: 主機不可解析，無法取得
- yf (recommendations / rec_summary / insider / major_holders / inst_holders): 可用，但 yahoo cookie / crumb 取得失敗，且 query2.finance.yahoo.com 被 agent proxy 拒絕，資料來源為已快取的回傳值
- WebSearch 新聞: 部分結果日期與內容不符 (例如含 2025 年或更早內容)，已排除，只採用 2026 年 11 月初文章。引用來源:
  - https://247wallst.com/investing/2026/11/02/nebius-lost-35-last-month-as-contagion-spikes-one-wall-street-pro-says-165-gains-are-coming/
  - https://beinsure.com/news/nebius-nasdaq-nbis-stock-price-forecast-wall-street-targets-281/
  - https://www.marketbeat.com/instant-alerts/nebius-group-nv-nasdaqnbis-given-average-recommendation-of-moderate-buy-by-analysts-2026-03-08/ (僅作為 rating 背景，日期為 3 月)

SENTIMENT REPORT COMPLETE
