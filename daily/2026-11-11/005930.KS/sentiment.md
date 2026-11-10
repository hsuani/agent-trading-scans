# Sentiment — 005930.KS (Samsung Electronics) as of 2026-11-11

資料完整度: 低。Reddit 與 StockTwits 無法取得 (見下方), 內部交易資料為空, 僅分析師評級可用。綜合判斷信心偏低。

## Analyst consensus

目前 36 位分析師: 12 Strong Buy / 24 Buy / 0 Hold / 0 Sell (yf rec_summary, 0m 期)。
近三個月變化: 三個月前為 11 Strong Buy / 25 Buy / 1 Hold (共 37 位)。一位 Hold 消失, 另有一位分析師不再計入 (總數 37 → 36), Strong Buy 由 11 增至 12。整體評級仍維持極度偏多, 並略為增強。

Recent moves: yf recommendations 回傳的是月度彙總, 沒有逐筆升降評等紀錄, 無法列出具體 upgrade/downgrade 事件。

目標價 (來自 WebSearch 摘要, 非 yf 原始資料, 未經驗證, 單位 KRW/股):
- S&P Global 彙整 (2026-06 快照): 37 位分析師, 平均目標價約 ₩389,965
- Daishin Securities (2026-06): Buy, 目標價 ₩560,000
- Hyundai Motor Securities (2026-06 底): Buy, 目標價 ₩440,000
- Mirae Asset Securities (2026-08 底): Buy, 目標價 ₩370,000, 認為近期跌幅是對總體經濟疑慮的過度反應
- Morningstar: 公允價值 ₩310,000, 財報後股價下跌約 5%

注意: 上述價格來源彼此矛盾 (同一頁面顯示 2026-06-05 收盤約 ₩329,000, 另一頁顯示 ₩191,200 並標示 Strong Sell 技術訊號), 本報告不採用任何單一股價作為現價。需以即時報價核對。

## Retail social

- Reddit (r/wallstreetbets, r/stocks): 無法取得。WebFetch 回報 "Claude Code is unable to fetch from www.reddit.com", 本次未能抽樣任何討論串, 無法判定 tilt。
- StockTwits: 無法取得。api.stocktwits.com DNS 解析失敗 (ENOTFOUND), 需在 session 網路設定中允許該網域後才能重試。
- X / 新聞輿情: WebSearch 僅回傳 2026 年中至晚期的舊文章, 找不到 2026-11 的相關討論。這些是研究機構與媒體文章, 不屬於散戶情緒, 無法代表 retail tilt。
- 提及量 (buzz volume): 無法量化, 無資料。
- Themes: 無法從本次資料歸納散戶主題。從 WebSearch 摘要可見的機構論述主軸為: (1) 總體經濟與跌幅是否過度反應; (2) 估值是否已反映 AI / 半導體循環; (3) 財報後股價反應。這些屬於機構面, 不是散戶面。

## Insider activity

Net 6mo: 無資料。yf insider 回傳空陣列, 無法確認是「無交易」還是「資料缺漏」(Yahoo cookie/crumb 取得失敗, 可能是原因之一)。不得據此推論內部人無買賣。
Notable: 無。

## Ownership shifts

- 內部人持股比例: 9.69%
- 機構持股比例: 46.80% (流通股口徑 51.82%)
- 機構數量: 755
- 單一時點快照, 無歷史序列, 無法判斷集中度趨勢。

## Net sentiment score

Composite: **偏多 (bullish), 信心低**。
- 分析師面: 強烈偏多 (36 Buy 類, 0 Hold, 0 Sell), 信心高。
- 散戶面: 無資料。
- 內部人面: 無資料。
- 只有單一面向可用, 故綜合分數主要反映分析師端, 不能視為完整的市場情緒判斷。

Divergence flag: **無法判定** (no data)。散戶 tilt 缺失, 無法與分析師 tilt 比較。待 Reddit / StockTwits 可存取後, 或取得 2026-11 的散戶資料後, 再重新評估背離訊號。

## Data gaps and next steps

1. api.stocktwits.com 需加入 session 允許網域清單。
2. Reddit 需允許 www.reddit.com 或改用其他代理方式, 目前無法抽樣。
3. yf insider 回傳空值, 建議確認 Yahoo cookie/crumb 連線, 或以其他來源 (如 KRX 內部人交易公告 / DART 申報) 補查。
4. WebSearch 結果日期偏舊, 且價格彼此矛盾, 需以即時報價與 2026-11 的分析師清單核對後再使用。

SENTIMENT REPORT COMPLETE
