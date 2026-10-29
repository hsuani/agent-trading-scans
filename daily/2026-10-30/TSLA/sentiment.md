# Sentiment — TSLA as of 2026-10-30（實際資料截至 2026-10-29）

> 注意事項：系統日期為 2026-10-29，指定的 DATE 為 2026-10-30。以下所有資料最晚只到 2026-10-29，沒有 10-30 當日資料。Reddit 與 StockTwits 無法取得，零售情緒部分為缺口。

## Analyst consensus

**43 家：19 buy（含 5 strongBuy）/ 22 hold / 2 sell（0 strongSell）**（來源：`pipeline/tools/yf TSLA rec_summary`，期間 0m）

| 期間 | strongBuy | buy | hold | sell | strongSell | Buy 合計 | Sell 合計 |
|---|---|---|---|---|---|---|---|
| 0m（目前） | 5 | 14 | 22 | 2 | 0 | 19 | 2 |
| -1m | 4 | 15 | 21 | 2 | 2 | 19 | 4 |
| -2m | 6 | 16 | 20 | 3 | 2 | 22 | 5 |
| -3m | 6 | 17 | 19 | 4 | 2 | 23 | 6 |

趨勢：過去三個月 Buy 由 23 家降至 19 家，Sell 由 6 家降至 2 家，Hold 由 19 家升至 22 家。整體往中性集中，看空評等減少比看多評等減少更明顯。

近期評等變動（WebSearch 結果，日期不完整，未能驗證 10 月內的調整）：
- 2026 年 7 月 Q2 財報後：Cantor Fitzgerald 維持 Overweight，目標價由 $510 降至 $485；Morgan Stanley 維持 Equal-Weight，目標價由 $417 降至 $400。
- 同期 UBS、Mizuho、Truist、Canaccord 的目標價約在 $370–$485 區間（資料日期與價格不完全一致）。
- 看空極端值：JPMorgan Underweight，目標價 $145（2026 年 4 月資料）。
- 看多極端值：Wedbush 的 Dan Ives 維持 $600。
- 平均目標價：Fintel 顯示約 $383（日期不明）；MarketBeat 1 月快照為 $410.71（已過時）。
- 工具 `recommendations` 歷史評等事件與 `rec_summary` 數字一致，沒有提供個別事件的日期細節。

## Retail social

- **Reddit（r/wallstreetbets、r/stocks）**：無法取得。WebFetch 回傳無法連線 www.reddit.com。目前沒有可引用的近期討論串，無法判定 10 月的語氣。
- **StockTwits**：無法取得。api.stocktwits.com DNS 解析失敗，需在 session 網路設定中允許此網域後再試。
- **X / 新聞聲量**：WebSearch 結果中，historicaloptiondata 9 月 3 日的 X 摘要描述為「mixed」。此來源為選擇權分析網站，不是散戶社群原文，可信度有限。
- **最近一筆可引用的散戶情緒讀數**：2026 年 2 月，一篇文章引用二手資料指 Reddit 情緒分數在一個月內由 32.3 滑落，之後回升至 38.0，整體偏空。此資料距今約 8 個月，且無法驗證原始來源，僅供背景參考。
- **聲量（mention count）**：無可靠數據，無法與平常水準比較。
- **選擇權端情緒**：historicaloptiondata 9 月分析偏多（其中一則標示 Conviction High），另一則提醒股價接近上軌，可能超買。這不是散戶社群情緒，只能作為技術面與選擇權面的旁證。

主要題材（依可取得的資料）：
- 股價約在 $354–$357 區間，Tickeron 指 30 日持平、年初至今約跌 21%，距 52 週高點約 $499 有明顯落差。
- MACD 於 10 月 6 日轉正（Tickeron）。
- 第二代 Roadster 發表會據報由 10 月 1 日延至 10 月 15 日（Tickeron，未能用其他來源交叉確認）。

## Insider activity

USD M 計價。統計區間：2026-04-30 至 2026-10-29（約 6 個月）。

| 日期 | 內部人 | 職位 | 類型 | 股數 | 金額（USD M） |
|---|---|---|---|---|---|
| 2026-04-30 | Kathleen Wilson-Thompson | Director | 賣出 @ $369–$384 | 26,409 | 9.99 |
| 2026-05-13 | Vaibhav Taneja | CFO | 賣出 @ $450 | 3,000 | 1.35 |
| 2026-06-08 | Vaibhav Taneja | CFO | 賣出 @ $402.20 | 2,605 | 1.05 |
| 2026-09-08 | Vaibhav Taneja | CFO | 賣出 @ $360.13 | 2,605 | 0.94 |

- **6 個月淨額：買入 $0M，賣出約 $13.3M（已將 4/30 的 Wilson-Thompson 賣出納入區間邊界）。**
- **公開市場買入**：區間內無任何 Purchase 紀錄。
- **選擇權行使（Conversion of Exercise，非市場交易）**：CEO Elon Musk 於 2026-06-16 行使 303,960,630 股衍生性證券（行使價 $23.34），帳面金額約 $7.09B。此金額為行使價乘以股數，不是市價，且不代表賣出或買入股票。若納入淨額計算會嚴重失真，故排除在淨額之外，但在敘事上要明列。
- Taneja 的 CFO 賣出呈規律性（每季前後一次，約 2,600 股），較像預先安排的計畫性出售。
- 過去 12 個月有一筆 CEO 公開市場買入：2025-09-12，2,568,732 股，約 $1.00B（@ $371.90–$396.36）。這是本次統計區間之外的事件，但屬於最近一次 CEO 的市場買入，可作為歷史對照。

## Ownership shifts

- 機構持股約 43.7%（機構數 5,297 家）；內部人持股約 17.8%（yf major_holders）。
- 機構持股變動的時間序列資料未取得，無法判斷集中度趨勢。
- 內部人持股比例高，主要來自 CEO 的大量股權，因此內部人比例不能直接解讀為看多訊號。

## Net sentiment score

**綜合：中性（Neutral），信心低。**

- 分析師面：中性偏正。Buy 佔 44%、Sell 佔 5%，Hold 為多數；近三個月看空評等明顯減少。但目標價多在 $400 附近，與現價約 $355 相比仍有上行空間，不過部分券商在 7 月後已下修。
- 內部人面：偏空（弱）。6 個月無公開市場買入，約 $13.3M 賣出，且主要來自 CFO 的計畫性出售。CEO 的大額選擇權行使不計入淨額。
- 散戶面：無法判定。Reddit 與 StockTwits 不可用，最近一筆可參考的讀數為 2026 年 2 月的偏空，已過時。
- 選擇權與技術面（旁證）：9 月偏多，但股價接近上軌。

**背離判定：無法確認（否）。** 因散戶資料缺失，無法判斷散戶語氣是否與分析師語氣相反。目前唯一的可比對組合是分析師中性偏正與內部人偏空，兩者方向不同，但這不是散戶與分析師之間的背離。

## 資料缺口與來源

- Reddit（r/wallstreetbets、r/stocks）：無法連線，已略過。
- StockTwits：DNS 失敗，需在 session 網路設定允許 api.stocktwits.com。
- 分析師目標價：最近可靠的日期為 2026 年 7 月，10 月的調整未能驗證。
- 來源（WebSearch / 工具）：Tickeron、Fintel、TipRanks、historicaloptiondata、FN2、MarketBeat、yf 工具（rec_summary / insider / major_holders / recommendations）。

本報告僅描述情緒與資料，不含交易建議。

SENTIMENT REPORT COMPLETE
