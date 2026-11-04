# Sentiment — 3231.TW (緯創) as of 2026-11-05

**資料完整度警示：** 本次只取得分析師共識一項可靠資料。Reddit 與 StockTwits 無法存取，內部人交易工具回傳空陣列，Web 搜尋也找不到 2026 年 11 月的輿情內容。以下結論信心偏低。

## Analyst consensus
16 家券商（5 Strong Buy / 11 Buy / 0 Hold / 0 Sell）。
- 近三個期間（-2m、-1m、0m）Buy 數維持 11，Strong Buy 由 6 降為 5，總家數維持 16。此變化可能是評等下調，也可能是覆蓋家數或資料來源調整，無法從現有資料判斷。
- `recommendations` 指令回傳的內容與 `rec_summary` 相同，沒有個別券商的升降評等歷史，因此無法列出具體 upgrade / downgrade 事件。
- 目標價：Web 搜尋找到 Macquarie 買進、目標價 400.00（來源頁標示日期 2026-07-24）與 UBS 目標價 225 TWD 買進（無日期）。兩者差距極大，且 400 明顯偏離搜尋結果中的股價區間（約 NT$136 至 182），可能是過時資料或誤植，**未經確認，不應採用**。

## Retail social
- **Reddit (r/stocks、r/wallstreetbets)：** 無法存取，WebFetch 被拒（www.reddit.com 無法連線）。無法評估討論量與多空傾向。
- **StockTwits：** 無法解析 api.stocktwits.com（DNS 失敗，可能是 session 網路白名單未包含該網域）。
- **X / 新聞 Web 搜尋：** 搜尋結果未包含 2026 年 11 月的意見或情緒內容。可見的內容是過期快照，例如 Simply Wall St 10 月初提到「投資人情緒隨股價上漲 21% 改善」，以及 TradingView 快照顯示約一週跌 8%、一個月跌 13%（快照時間不明）。這些是價格變化描述，不代表散戶意見。
- **Buzz 量能：** 無資料，無法與常態比較。
- **主題：** 無可靠主題可歸納。
- 引述樣本：無（無可用貼文）。

## Insider activity
`insider` 工具回傳空陣列。這可能代表近 6 個月無申報交易，也可能是資料缺漏，無法區分。**6 個月淨買賣金額：無資料。** 不得解讀為「內部人無交易」。

## Ownership
- 內部人持股 4.77%
- 機構持股 33.35%（浮動股比 35.02%）
- 機構家數 248
- 工具只提供單一時點快照，沒有趨勢資料，無法判斷機構集中度的增減方向。

## Net sentiment score
**Composite: bullish（信心：低）**
- 分析師面：偏多。16 家全數買進或以上，沒有持有或賣出評等。
- 散戶面：無資料。
- 內部人面：無資料。
- 價格動能（非情緒來源，僅供參考）：快照顯示近期下跌，時間點不明。
- 整體結論只反映分析師共識。其他三個來源缺失，無法交叉驗證。

**Divergence flag: 無法判定。** 散戶傾向缺失，無法判斷是否與分析師方向相反。

## 後續補足建議
1. 將 `api.stocktwits.com` 加入 session 網路白名單後重試 StockTwits。
2. Reddit 公開 JSON 被阻擋，可改用其他來源或 Reddit 官方 API（需認證）。
3. 以中文查詢「緯創 目標價 2026年11月」或直接查 TWSE / 公開資訊觀測站 的內部人申報，確認 6 個月內部人交易。
4. 確認 rec_summary 的 Strong Buy 由 6 降為 5 是否對應具體評等下調。

## 來源
- [Wistron Corp (3231) 共識預估（Investing.com）](https://uk.investing.com/equities/wistron-corp-consensus-estimates)
- [Wistron Corporation（Simply Wall St 持股）](https://simplywall.st/stocks/tw/tech/twse-3231/wistron-shares/ownership)
- [WISTRON CORPORATION（MarketScreener）](https://uk.marketscreener.com/quote/stock/WISTRON-CORPORATION-190760487/)
- [TWSE 3231（TradingView）](https://www.tradingview.com/symbols/TWSE-3231/)
- [Wistron Corporation Stock Forecast & Analysis（Alpha-Lenz）](https://alpha-lenz.com/en/companies/wistron-corporation)

SENTIMENT REPORT COMPLETE
