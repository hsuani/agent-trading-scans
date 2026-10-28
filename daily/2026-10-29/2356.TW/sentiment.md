# Sentiment — 2356.TW (英業達) as of 2026-10-29

資料時效說明：yfinance 分析師與內部人資料為 2026-10-28 抓取之快照；網路搜尋結果日期混雜（2026 年 3 月至 10 月），未能確認 10/29 當日報價。Reddit 與 StockTwits 本次無法取得（見下方「資料缺口」）。

## Analyst consensus

| 評級 | 0m（目前） | -1m | -2m | -3m |
|---|---|---|---|---|
| Strong Buy | 2 | 2 | 2 | 2 |
| Buy | 1 | 1 | 1 | 1 |
| Hold | 7 | 7 | 7 | 5 |
| Sell | 0 | 0 | 0 | 1 |
| Strong Sell | 0 | 0 | 0 | 0 |
| 合計家數 | 10 | 10 | 10 | 9 |

目前 10 家：3 buy（含 2 strong buy）/ 7 hold / 0 sell。

Recent moves: 過去三個月彙總顯示，Sell 由 1 降為 0，Hold 由 5 增為 7，家數由 9 增為 10。彙總表無法判斷是單一券商由 Sell 轉 Hold，或是舊評等除名加上新增 Hold，個別評等異動工具未提供。近一個月無評級數字變化。

目標價：本次工具未提供目標價歷史。搜尋摘要提及某聚合站平均目標價約 49.47 TWD、區間 36.36 至 63.00 TWD，但該站股價與日期不一致，無法確認，本報告不採用。

## Retail social

- Reddit：無法取得。r/wallstreetbets 與 r/stocks 的 search.json 經 agent proxy 回應 403 CONNECT（政策拒絕），本次跳過，未有樣本。
- StockTwits / X：StockTwits 網域無法解析（DNS 失敗，session 網路未允許 api.stocktwits.com），跳過。X 未有可用搜尋結果。
- 網路論壇（CMoney 股市討論區）：僅由搜尋摘要得知，未直接開啟頁面。摘要描述為意見分歧，有人看好 AI 伺服器題材與外資買超，也有人提醒短線風險與投信進出頻繁。此為二手摘要，樣本量與聲量無法量化。
- 聲量：無法量化（缺 Reddit 與 StockTwits），定性判斷為低可見度，僅有少量論壇討論。
- 散戶傾向：混合（mixed），信心低。
- 主要主題（依搜尋摘要）：AI 伺服器需求、外資與投信買賣動向、短線波動風險。

## Insider activity

Net 6mo: 資料缺口。yfinance insider 工具回傳空陣列，無法區分「無交易」與「資料未覆蓋」。台股內部人申報資料通常不在此來源，故不能推論為零買賣。建議改查台灣公開資訊觀測站（MOPS）董監事持股異動申報。

Notable: 無。

## Ownership shifts

- 內部人持股（Yahoo 定義）：約 28.5%
- 機構持股（佔總股本）：約 25.1%；佔流通股約 35.1%
- 機構家數：157
- 單一快照，無歷史趨勢，無法判斷集中度是增加或減少。

## Net sentiment score

Composite: **中性（neutral），信心低**。

依據：
- 分析師端：偏中性。10 家中 7 家 Hold、0 家 Sell，Buy 佔 3 家，近三個月 Sell 歸零、Hold 增加，略偏正面的方向性變化，但幅度小。
- 散戶端：混合，樣本不足，無法量化。
- 內部人：無資料，不納入評分。
- 基本面背景（搜尋摘要，未逐項驗證）：2026 年 5 月月營收約 828.08 億 TWD、年增約 35.3%；近四季 EPS 約 3.1 TWD，本益比約 19 倍（與 59 TWD 收盤價換算一致）。

Divergence flag: **無法判定（no）**。分析師傾向為中性偏持有，散戶傾向為混合，兩者並無明確反向。若日後取得 Reddit 或 StockTwits 資料，且散戶明顯偏多而分析師維持 Hold，應重新評估背離旗標。

## 資料缺口與可靠性

1. Reddit（r/wallstreetbets、r/stocks）：proxy 政策拒絕（403 CONNECT）。
2. StockTwits：session 網路未允許 api.stocktwits.com。
3. yfinance 內部人交易：回傳空值，無法確認。
4. 目標價與個別評等異動：工具未提供，搜尋來源不一致。
5. 年度營收共識（搜尋摘要標示 777.43B）與月營收 828.08 億 TWD 的量級不一致，單位未核實，故未納入本報告。
6. 股價：搜尋摘要中 10/16 收盤約 59 TWD，8 月約 65 至 69 TWD，6 月歷史高點約 88.6 TWD；10/29 當日價未確認。
7. Yahoo cookie/crumb 取得失敗，但數據端點仍有回傳，故分析師與持股數字可用，但建議以其他來源交叉確認。

SENTIMENT REPORT COMPLETE
