# Sentiment — 6669.TW (緯穎 Wiwynn) as of 2026-11-26

> 資料完整度偏低：Reddit、StockTwits 無法存取，內部人交易資料為空。本報告的情緒判斷主要依賴分析師評級，散戶面向缺口很大。

## Analyst consensus

目前共 20 位分析師：6 Strong Buy / 14 Buy / 0 Hold / 0 Sell（rec_summary，0m 期）。

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell |
|------|-----------:|----:|-----:|-----:|------------:|
| 本期 (0m) | 6 | 14 | 0 | 0 | 0 |
| -1m | 6 | 14 | 0 | 0 | 0 |
| -2m | 5 | 14 | 0 | 0 | 0 |
| -3m | 5 | 14 | 0 | 0 | 0 |

- 近三個月評級分布沒有變動，Strong Buy 由 5 增至 6，屬於小幅加強。
- yfinance 的 recommendations 工具只回傳彙總計數，沒有個別券商的升降評等紀錄，因此無法確認近期是否有具名的 upgrade 或 downgrade。
- 目標價：WebSearch 找到的數字互相衝突。一頁顯示平均目標價約 TWD 7,290/股（高 9,000、低 6,000）；另一頁列出 JPMorgan Buy 目標 9,000、Goldman Sachs Buy 目標 4,000，但日期不一致。這些數字都不能當作確定值，需以券商原始報告核對。
- 股價資料也有矛盾：一頁顯示 11/09 收盤約 1,645 TWD，另一頁顯示 7 月約 5,300–5,700 TWD。可能是股票分割或資料錯誤，本報告不採用任何絕對價位判斷。

## Retail social

- Reddit (r/wallstreetbets、r/stocks)：無法存取（WebFetch 回報 unable to fetch）。無法取得樣本貼文、分數或留言傾向。
- StockTwits：無法解析 api.stocktwits.com（DNS 失敗）。需要在工作階段網路設定中允許此網域後才能重試。
- X / 新聞 chatter：一次 WebSearch 未找到中文或近期散戶討論，只有 Investing.com 等彙總頁面與分析師數據。無法判斷提及量。
- 提及量（相對典型水準）：無資料，無法評估。
- 散戶傾向：無法判斷（bullish / bearish / mixed 皆無依據）。
- 主題：無可靠樣本，無法歸納。

## Insider activity

Net 6mo：無資料。yfinance insider 工具回傳空陣列，這不等於「沒有內部人交易」。台灣上市公司的董監事持股變動是依 MOPS 申報，未必會進入 yfinance。若要判斷，需另查公開資訊觀測站的董監申報。

## Ownership shifts

- 內部人持股：約 43.9%（insidersPercentHeld）
- 機構持股：約 29.7%（institutionsPercentHeld），占流通股約 52.9%
- 機構家數：350（institutionsCount）
- 只有單一時點快照，無法判斷機構集中度的趨勢方向。

## Net sentiment score

Composite：**bullish（信心：低）**

- 唯一有資料的面向是分析師評級，全數為 Buy 以上，沒有 Hold 或 Sell，且 Strong Buy 數量近三個月略增。這一面明確偏多。
- 散戶面、內部人面都無資料，綜合分數主要來自單一來源，因此信心只能給低。
- 目標價與股價資料互相矛盾，不應用來支持或反駁多方判斷。

Divergence flag：**無法判定（no data）**。散戶傾向沒有可靠資料，無法確認散戶與分析師是否方向相反。

## 資料缺口與後續建議

1. 允許 api.stocktwits.com 網域後重試 StockTwits。
2. Reddit 無法存取，需確認網路設定或改用其他來源。
3. 以 MOPS 核對近六個月董監持股申報，補足內部人交易面向。
4. 目標價與股價以 TWSE 或財經終端核對，釐清 1,645 與 5,300–5,700 TWD 的差異是否來自股票分割或資料錯誤。

SENTIMENT REPORT COMPLETE
