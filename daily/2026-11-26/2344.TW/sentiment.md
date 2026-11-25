# Sentiment — 2344.TW (華邦電 Winbond) as of 2026-11-26

> 今日系統日期為 2026-11-25，本報告依指定的 as-of 日期 2026-11-26 整理，資料來源以工具回傳為準。

## Analyst consensus
目前 8 位分析師：3 strongBuy / 4 buy / 1 hold / 0 sell / 0 strongSell，即 7 買進、1 持有、0 賣出。

近四個月趨勢（rec_summary）：

| 期間 | strongBuy | buy | hold | sell | 買進類合計 |
|---|---|---|---|---|---|
| 0m（本月） | 3 | 4 | 1 | 0 | 7 |
| -1m | 4 | 4 | 0 | 0 | 8 |
| -2m | 4 | 4 | 0 | 0 | 8 |
| -3m | 4 | 3 | 0 | 0 | 7 |

- 本月出現 1 檔 hold，且 strongBuy 由 4 降為 3。這是評級上的小幅降溫，但樣本只有 8 家。
- `recommendations` 端點只回傳彙總計數，沒有個別升降評等事件，無法列出具體 upgrade / downgrade 日期與券商。
- 網路搜尋提到 Morgan Stanley 於 2026-03 降為 Hold，但這與 rec_summary 的月度變化時點不吻合（hold 在 0m 才出現），此說法未驗證。
- 目標價資料互相矛盾：搜尋結果中 JPMorgan 目標價有 255 與 360 TWD 兩種，另有 51.51、97.54 TWD 的標題，數量級差異很大，疑為過期或不同來源。股價區間散見 99.9 至 155 TWD，無法確認現價。**目標價變動本報告無法可靠判定，需以券商原始報告或即時行情複核。**

## Retail social
- Reddit（r/wallstreetbets、r/stocks）：WebFetch 無法連線，本次未取得資料，無法提供樣本帖與情緒傾向。
- StockTwits：api.stocktwits.com 無法解析（DNS 失敗，疑為未列入本 session 允許網域）。依規定未重試。若需此來源，請在 session 網路設定中允許該網域後再跑。
- X / 新聞：僅有網路搜尋。Investing.com 使用者喊價板有 2026-11-13（目標 125）與 2026-11-16（目標 116）兩則個別留言，樣本極少，只能視為弱訊號，不足以代表市場整體情緒。
- 聲量（buzz volume）：無法量化，無法與平常水準比較。
- 主題：無可靠資料可歸納。
- Retail 傾向：**無法判定**（資料缺口）。

## Insider activity
`insider` 端點回傳空陣列。這不等於沒有內部人交易，可能是來源或工具缺漏。**Net 6mo：無資料**，無法計算 TWD 買賣金額，也無法指出 CEO/CFO 或其他人的交易。

## Ownership shifts
單一時點快照（無歷史趨勢）：
- insidersPercentHeld：28.8%（此數字偏高，可能含大股東集團，分類口徑未知）
- institutionsPercentHeld：26.4%；佔浮動股比 37.1%
- 機構持有家數：221

機構持股趨勢無法判定，需要下一期快照才能比較。

## Net sentiment score
- **分析師面：偏多（信心：中）**。7/8 為買進類，賣出為零。但本月出現 1 檔 hold，目標價資料不可靠，信心不宜過高。
- **散戶面：無法判定（信心：低）**。Reddit / StockTwits 皆不可用，僅有 2 則個別喊價。
- **內部人面：無資料**。
- **綜合：偏多（信心：低至中）**。主要依據為分析師共識，散戶與內部人兩側缺資料，不應視為完整結論。
- **背離旗標：無法判定**。散戶傾向資料缺失，無法確認是否與分析師傾向相反。

## 資料缺口與待辦
1. 允許 api.stocktwits.com 網域後重跑 StockTwits。
2. Reddit 來源需另找可連線的路徑（例如改用 Reddit 官方 API 或其他鏡像），本次未能取得。
3. 目標價與評等明細需以券商原始報告核對，搜尋來源數字互相矛盾。
4. insider 端點空資料需確認是否為工具問題。

## 來源
- 分析師彙總與內部人、持股資料：`pipeline/tools/yf 2344.TW rec_summary / recommendations / insider / major_holders`
- 網路搜尋參考：https://uk.investing.com/equities/winbond-scoreboard 、https://www.tipranks.com/stocks/tw:2344 、https://nasdaq.com/articles/winbond-electronics-twse-2344-price-target-increased-7314-5151 、https://www.nasdaq.com/articles/winbond-electronics-twse-2344-price-target-increased-4140-9754 （目標價與數字彼此矛盾，僅供參考）

SENTIMENT REPORT COMPLETE
