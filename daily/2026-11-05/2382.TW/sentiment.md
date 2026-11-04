# Fundamentals — 2382.TW (廣達) as of 2026-11-05

注意事項: 系統日期為 2026-11-04，分析日期 2026-11-05 晚一天。本次能取得的資料多為較早或無日期來源，以下結論須以「資料不足」為前提閱讀。

## 資料來源狀態
| 來源 | 狀態 |
|---|---|
| yf recommendations / rec_summary | 成功，但三個期間數字完全相同，疑似過期或未更新 |
| yf insider | 回傳空陣列，無法確認是否真的無交易 |
| yf major_holders | 成功 |
| Reddit r/wallstreetbets、r/stocks | 失敗，WebFetch 無法連線 www.reddit.com |
| StockTwits | 失敗，api.stocktwits.com DNS 解析失敗，需在 session 網路設定中允許該網域 |
| X / 新聞搜尋 | 部分成功，搜尋結果未找到 2026 年 11 月的相關報導 |

## Analyst consensus
| 評等 | 家數（yf rec_summary，最新期 0m） |
|---|---|
| Strong Buy | 5 |
| Buy | 12 |
| Hold | 1 |
| Sell | 0 |
| Strong Sell | 1 |

合計約 19 家，其中買進方 17 家、持有 1 家、賣出 1 家（含 Strong Sell）。Investing.com 的三個月統計為 16 買 / 2 持有 / 1 賣，與 yf 略有出入，可能是統計窗口或家數不同。

近期變動: yf 三個期間（0m、-1m、-2m）數字完全相同，無法判斷近期有無升降評等。目標價未取得可靠數字。聚合網站提到平均目標價約有 17% 至 22% 上行空間，但日期不明，不建議採信。MarketScreener 提到分析師過去一年持續上修營收預估，方向偏正面。

## Retail social
- Reddit: 無資料（連線遭拒）。無法取樣代表性討論串，也無法判斷情緒傾向。
- StockTwits: 無資料（DNS 失敗）。
- X / 新聞聊天: 搜尋結果以行情聚合頁為主，缺乏可引用的散戶貼文，無法量化討論量。
- 討論量: 無法與平時基準比較，只能標示為未知。
- 主題（來自聚合頁，非散戶原文，僅供參考）: 殖利率（部分頁面顯示約 4.5% 至 5.8%）、技術面評級偏多（部分頁面為 Strong Buy）、估值與市值規模。
- 價格資料不一致: 各頁顯示約 NT$284 至 NT$340。最新有日期的報價為 NT$300.50（2026-08-04），距分析日已超過三個月，不可作為 as-of 價格。

## Insider activity
Net 6mo: 資料不足（yf 回傳空陣列，無法區分「無交易」與「資料缺漏」）。
Notable: 無可確認的交易紀錄。

## Ownership shifts
- 內部人持股比例約 29.7%（yf major_holders，為整體持股，非交易訊號）。
- 機構持股比例約 34.1%，佔流通股約 48.6%，機構家數 305。
- 歷史快照不足，無法計算機構持股的趨勢方向。

## Net sentiment score
Composite: 偏多（neutral-to-bullish），信心: 低。
依據僅為分析師評等偏買進（17/19 家買進方）與聚合網站的技術面偏多訊號。散戶端與內部人端都沒有可用資料，因此複合分數主要反映分析師端。

Divergence flag: 無法判定。散戶傾向缺資料，無法與分析師傾向比較，故不標示背離。

資料缺口（建議補強）:
1. 允許 api.stocktwits.com 與 Reddit 網域後重試。
2. 確認 yf insider 對 TW 上市股票是否有資料（或改由公開資訊觀測站取得董監持股申報）。
3. 取得 yf recommendations 的完整歷史，以確認近期評等變動。

SENTIMENT REPORT COMPLETE
