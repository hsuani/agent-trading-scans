# Sentiment — ABBNY as of 2026-11-20

注意事項：Reddit 與 StockTwits 無法取得，零售情緒部分為缺漏。

## Analyst consensus
yf rec_summary（當期，0m）：0 strong buy / 0 buy / 5 hold / 0 sell / 1 strong sell，共 6 家，判讀為 neutral 偏保守。

3 個月趨勢（yf recommendations）：
| 期間 | Buy 系 | Hold | Sell 系 | 合計 |
|---|---|---|---|---|
| 0m（當期） | 0 | 5 | 1 strongSell | 6 |
| -1m | 0 | 5 | 1 strongSell | 6 |
| -2m | 0 | 3 | 2 strongSell | 5 |
| -3m | 0 | 3 | 2 strongSell | 5 |

趨勢：strongSell 由 2 降至 1，hold 由 3 升至 5，評級分布有小幅改善，但仍無任何 buy。

近期動作（網路搜尋，來源未完全交叉驗證）：
- Investing.com 顯示 Evercore ISI 於 2026-10-23 升至 buy，但 yf 當期無 buy，兩者矛盾，列為未驗證。
- Erste Group 於 2026-08 降至 hold。
- TD Cowen 2026-09 維持 hold，目標價 USD 100。
- 目標價：Investing.com 平均約 USD 93（略低於現價，約 -5.8%）；StockAnalysis 約 USD 85.25，但資料停在 2026-05，已過期。
- TipRanks 顯示 Moderate Sell，僅 2 家，無日期。

## Retail social
- Reddit（r/wallstreetbets、r/stocks）：無法取得，WebFetch 被拒（無法連線 www.reddit.com）。
- StockTwits：無法解析 api.stocktwits.com（DNS 失敗，主機不在允許網域內）。
- X / 新聞：未找到 2026-11 的專門意見文章。PriceTargets.com 新聞情緒分數為 0.73（範圍 -2 至 +2），僅反映 30 天標題情緒，與分析師觀點未必一致。
- 聲量：無法量化（無 Reddit、StockTwits 資料）。
- 主題：無法萃取，因來源缺漏。

## Insider activity
Net 6mo：資料不可用。yf insider 回傳空陣列，無任何交易紀錄。空值可能代表真的無申報，也可能是資料源缺漏（yf 的 cookie/crumb 取得失敗），因此不能直接判為零交易。Notable：無。

## Ownership shifts
yf major_holders：insidersPercentHeld = 0.0；institutionsPercentHeld = 0.00151（即約 0.15%）；institutionsCount = 85。
- 0.15% 的機構持股比例明顯偏低，ABBNY 為 OTC ADR，此數值可能是資料源 ADR 對應錯誤，不宜作為結論。
- 無歷史趨勢可比較，因此無法判斷機構集中度變化。

## Net sentiment score
Composite：neutral（信心：低）
- 分析師面：偏中性至略偏保守（0 buy、5 hold、1 strong sell；3 個月趨勢小幅改善）。
- 零售面：無資料。
- 內部人面：無資料。
- 新聞情緒：PriceTargets 0.73，偏正面，但只是標題情緒，權重低。

Divergence flag：無法判斷（no）。零售端無資料，無法比較零售與分析師傾向是否相反。

資料缺口與後續建議：
1. 允許 api.stocktwits.com 與 Reddit 相關網域後重跑，補上零售面。
2. 核對 Evercore 升評是否屬實，以及 yf 與 Investing.com 的評級差異。
3. insider 與 major_holders 資料需以其他來源（如 SEC 或 OTC 資料源）交叉確認。

SENTIMENT REPORT COMPLETE
