# Sentiment — S (SentinelOne) as of 2026-11-06

資料來源狀態: yfinance 工具可用 (analyst、insider、ownership)。Reddit 經代理回 403, StockTwits 網域無法解析 (DNS 失敗), X/新聞僅能用 WebSearch, 且搜尋結果多為 2026 年中以前的頁面, 沒有 11 月的即時資料。本報告的零售端資料因此缺漏。

## Analyst consensus

工具回傳的 analyst 分布 (共 34 位, 單位為家數):

| 時點 | Strong Buy | Buy | Hold | Sell | Strong Sell | 合計 Buy 側 / Hold / Sell 側 |
|---|---|---|---|---|---|---|
| 0m (目前) | 3 | 15 | 16 | 0 | 0 | 18 / 16 / 0 |
| -1m | 3 | 15 | 15 | 0 | 1 | 18 / 15 / 1 |
| -2m | 3 | 16 | 15 | 0 | 0 | 19 / 15 / 0 |
| -3m | 3 | 18 | 14 | 0 | 0 | 21 / 14 / 0 |

目前為 18 Buy / 16 Hold / 0 Sell, 偏多但評等偏向 Hold 的趨勢在上升: 3 個月內 Buy 側由 21 降到 18, Hold 由 14 升到 16。

- 個別升降評等與目標價變動: `recommendations` 工具回傳的內容與 `rec_summary` 相同, 沒有逐筆事件, 無法列出誰升評、誰降評, 也沒有目標價歷史。
- 網路搜尋的補充 (未註明日期, 信心較低): MarketBeat 顯示 17 Buy / 11 Hold / 1 Sell, 與工具數字不一致, 不採用。另有 Piper Sandler、D.A. Davidson 維持 Hold、目標價 $20 的 2026 年 8 月資料, 同樣無法確認是否為最新。

## Retail social

- Reddit (r/wallstreetbets、r/stocks): 無法取得 (代理 403)。
- StockTwits: 無法取得 (api.stocktwits.com 無法解析)。需要在 session 網路設定允許該網域才能重試。
- X / 新聞: WebSearch 未找到 2026 年 11 月的散戶意見文章。網路上較新的描述為「情緒轉冷」 (Simply Wall St 提到 trailing one-year 報酬約 -37%), 但該頁面日期不明。
- 散戶聲量相對一般水準: 無法量化。
- 主題: 無法萃取。因為沒有任何 Reddit / StockTwits 貼文, 本報告不引用任何散戶原文。
- 散戶傾向: 無法判定 (資料缺漏)。

## Insider activity

期間: 2026-05-06 至 2026-11-06 (6 個月)。

- 公開市場買入: 0 筆, $0。
- 公開市場賣出: 29 筆, 合計約 $28.4M。
  - CEO Tomer Weingarten: 約 $22.2M, 分散在多次出售中。最大一筆是 2026-10-05 以 $25.26 賣出約 $13.3M, 同日有 500,000 股衍生性證券行使 (行使價 $9.74)。
  - CFO Sonalee Parekh: 約 $2.3M (2026-07-06、07-27、09-08、10-06 各一批)。
  - 其他: President Barry Padgett、Ana Pinczuk (Officer and Director)、Robin Tomasello、Keenan Conder 等, 合計約 $6.2M。
- 集中在 2026-10-05/06 的賣出價約 $25.26–25.33, 是樣本內最高價。工具資料無法確認這些交易是否屬於 10b5-1 計畫。
- 獎勵發放 (Stock Award, 價格 0) 與 2026-06-25、2026-04-15 的董事獎勵, 不計入賣出。
- 6 個月以前的唯一公開市場買入: 董事 Mark Peek 2025-12-16 以 $14.89 買入約 $0.6M。

解讀: 內部人在股價由 2026 年 3–4 月的約 $13 升至 10 月約 $25 的過程中持續賣出, 沒有買入。

## Ownership shifts

- 機構持股: 86.2% (流通股 86.9%), 機構數 658 家。
- 內部人持股: 0.89%。
- 本次只有單一時點快照, 無法判斷機構集中度的趨勢。

## Net sentiment score

- 分析師: 偏多 (信心中)。0 Sell, 18 Buy; 但 Buy 側近 3 個月減少 3 家, Hold 增加。
- 內部人: 偏空 (信心中高)。6 個月內 $28.4M 賣出、0 買入, 而且集中在股價高點。
- 零售: 無資料, 不計入綜合分數。
- 綜合: 中性 (信心低-中)。分析師端偏多, 內部人端偏空, 兩者不一致, 但沒有零售資料支持判斷。

Divergence flag: 無法判定。零售端缺資料, 無法檢查零售與分析師是否反向。分析師與內部人之間的反向訊號 (分析師多半 Buy/Hold、內部人高價大量賣出) 值得留意。

SENTIMENT REPORT COMPLETE
