# Sentiment — 2356.TW (英業達) as of 2026-11-12

資料完整度提醒: 本次 Reddit 與 StockTwits 無法取得 (見下方), Yahoo 內部人資料為空陣列且 cookie/crumb 取得失敗, 整體置信度偏低。分析師數據與機構持股為 yfinance 回傳值, 時間戳不明。

## Analyst consensus
目前 (period 0m) 共 10 家: Strong Buy 2 / Buy 1 / Hold 7 / Sell 0 / Strong Sell 0, 即約 3 買 / 7 持有 / 0 賣。

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell |
|---|---|---|---|---|---|
| 0m (當期) | 2 | 1 | 7 | 0 | 0 |
| -1m | 2 | 1 | 7 | 0 | 0 |
| -2m | 2 | 1 | 7 | 0 | 0 |
| -3m | 2 | 1 | 7 | 0 | 0 |

Recent moves: 過去四個期間的評級分布完全相同, 代表近三個月無評級升降級被記錄; `recommendations` 工具也未回傳個別升降級事件或目標價變動, 因此無法確認近期 upgrade/downgrade 或 target price 調整。需注意: 四期完全一致可能是資料未更新, 不宜當作確定的「無變動」。

法人觀點的文字面 (可得的最新一筆, 2026-05 前後, GS 報告): 維持中立, 理由為估值相對合理; 同時看好 AI 伺服器出貨成長, 但提醒記憶體與 CPU 供應短缺是出貨下行風險。此為 5 月資料, 距今已逾半年, 不代表 11 月時點的評級。

## Retail social
- Reddit: 無法取得。WebFetch 回報 "Claude Code is unable to fetch from www.reddit.com", r/wallstreetbets 與 r/stocks 的搜尋皆失敗, 本次無法評估散戶語氣與貼文數量。
- StockTwits / X: StockTwits 因 `api.stocktwits.com` DNS 解析失敗無法連線 (需於 session 網路設定允許該網域)。X 本次未額外搜尋 (WebSearch 回傳為新聞/法說類結果, 非社群貼文)。
- 聲量 (Buzz volume): 無法量化, 無社群樣本可比對一般水準。
- 散戶語氣: 無樣本, 無法判定 bullish / bearish / mixed。
- 替代訊號 (非社群, 僅供參考): 搜尋結果中的公開新聞與法說報導聚焦於伺服器業務成長與獲利改善 (見下方 Themes), 屬媒體/法人語境, 不等同散戶情緒。
- Themes (從新聞與法說文字歸納, 非社群): (1) AI 伺服器佔比提升、為主要成長動能; (2) 2026 年 8 月營收年增約 35.8% 創十年同期新高 (營收 832.68億 TWD); (3) 獲利改善 (2026Q2 EPS 1.09 TWD, 年增約 78.7%); (4) 估值與記憶體/CPU 供應短缺為主要疑慮; (5) 管理層強調應看整體獲利金額而非僅毛利率。

## Insider activity
Net 6mo: 資料不可得。`insider` 工具回傳空陣列 (且同時 cookie/crumb 取得失敗), 無法判定為「無交易」或「資料缺漏」, 因此不列出 $ 買賣金額, 亦不指定 CEO/CFO 交易。建議以台灣公開資訊觀測站 (MOPS) 的董監持股申報人工核對。

## Ownership shifts
- 內部人持股 (insidersPercentHeld): 28.5%
- 機構持股 (institutionsPercentHeld): 25.4%; 占流通股 (institutionsFloatPercentHeld): 35.6%
- 機構家數 (institutionsCount): 162
- 趨勢: 單一快照, 無歷史比較, 無法判斷機構集中度是上升或下降。

## Net sentiment score
Composite: **中性偏謹慎 (neutral, low confidence)**
- 分析師面: 偏中性 (3 買 / 7 持有 / 0 賣, 無賣方評級), 但 5 月的文字觀點對估值持保留態度。
- 散戶面: 無資料, 無法評分。
- 內部人面: 無資料, 無法評分。
- 整體信心: 低, 主要因社群與內部人資料缺漏, 分析師資料時效不明。

Divergence flag: **無法判定 (no)**。因散戶端無樣本, 無法確認是否與分析師傾向相反。

資料缺口 (待補):
1. Reddit (r/wallstreetbets, r/stocks) 本次無法連線。
2. StockTwits 因網域未允許無法連線。
3. Yahoo insider 資料為空且 cookie/crumb 失敗, 需確認是否真為零交易。
4. 分析師評級四期完全相同, 需確認資料是否過期; 目標價資料缺失。
5. 新聞搜尋未回傳 2026 年 10–11 月的報導, 最新資訊約停在 2026 年 9 月前後。

SENTIMENT REPORT COMPLETE
