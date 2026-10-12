# Sentiment — 1519.TW (華城) as of 2026-10-13

資料限制：本報告以 2026-10-13 為基準日，但能取得的最新市場資料僅到 2026 年 9 月（月收盤）與 2026 年 8 月初（評等快照）。Yahoo Finance cookie/crumb 取得失敗，yf 工具以無 crumb 模式回傳，數值需保守看待。Reddit 與 StockTwits 無法連線（Reddit 無法抓取、StockTwits DNS 解析失敗）。

## Analyst consensus
yf rec_summary（當前）：8 buy（strongBuy 3 / buy 5）、0 hold、0 sell。
近 3 個月分布：-1m 與 -2m 同為 8 buy；-3m 為 6 buy（strongBuy 2 / buy 4）。評等數量近 3 個月由 6 升至 8，無任何 hold 或 sell。

Recent moves：
- yf recommendations 只回傳彙總計數，沒有逐筆升降評等事件，無法確認個別券商動作。
- 二手來源（investing.com 彙整，經 WebSearch 摘要）記載：花旗於 2026 年 4 月把評等升為買入，目標價 1150 元。另有投顧於 2026 年 3 月維持買進，目標價由 1000 元上調至 1050 元，理由為訂單能見度已到 2028 年、AI 資料中心（AIDC）訂單超過 150 億元。
- 同一來源列出 12 個月平均目標價 963.6 元，最高 1150 元，最低 800 元。此數字日期不一，部分為 2025 年底或 2026 年初的預測，未必反映 10 月狀態。
- investing.com 共識為 6 buy / 0 hold / 0 sell，與 yf 的 8 buy 不一致，應視為不同彙整源的差異。

## Retail social
- Reddit（r/wallstreetbets、r/stocks）：DATA_UNAVAILABLE。WebFetch 無法連線 www.reddit.com。
- StockTwits：DATA_UNAVAILABLE。api.stocktwits.com DNS 解析失敗。此標的在 StockTwits 上的覆蓋本來也偏薄。
- 台股社群（CMoney 股市爆料同學會、PTT Stock 板）：WebSearch 找到 CMoney 華城討論區，內容多空並存。樂觀留言提到重電族群走強，悲觀留言關注外資與投信連日賣超。貼文日期不明，無法確認屬於 2026 年 9 月或 10 月。PTT 未能直接抓取。
- 聲量（buzz volume）：無可量化的提及次數。WebSearch 結果顯示的繁中新聞與討論頁數量有限，相對重電族群（如士電、華城同類股）聲量屬低至中等，屬定性判斷，信心低。
- 代表性觀點（WebSearch 摘要，未能逐篇驗證）：「重電族群走強」（樂觀）、「外資投信連日賣超」（悲觀）。
- Themes：
  1. AI 資料中心（AIDC）與電網擴充訂單，為看多主軸。
  2. 外資與投信賣超、短線走勢偏弱，為看空主軸。
  3. 2025 年獲利創歷史新高（稅後純益 44.19 億元，EPS 13.99 元），估值與獲利面仍被引用。
  4. 股價自 2026 年 4 月前後高點回落（52 週區間約 526 至 1,115 元），是散戶最常提及的風險點。

Retail tilt：mixed（多空並存，偏向觀望）。信心低，因為樣本不足且日期不明。

## Insider activity
Net 6mo：DATA_UNAVAILABLE。
- yf insider 回傳空陣列，無內部人交易紀錄。
- 台灣董監持股增減需依公開資訊觀測站（MOPS）申報，本次未取得 2026 年資料。
- Yahoo 股市大戶籌碼頁顯示 2025/12/12 董監持股 17.80%，2025 年 9 月底至 12 月中的每週紀錄未變動。
- cnyes 董監持股頁的個別明細為 2023 年 8 月資料，已過時，不可用於判斷 2026 年的買賣方向。
- Notable：無法判定。

## Ownership shifts
- yf major_holders：insidersPercentHeld 43.48%、institutionsPercentHeld 13.09%、institutionsFloatPercentHeld 23.16%、institutionsCount 176。
- 警告：yf 的 insidersPercentHeld（43.48%）與 Yahoo 股市的董監持股（17.80%）差距很大，兩者定義或統計範圍不同，不能直接並列解讀。
- 趨勢：無歷史時序資料，無法判斷法人集中度是升或降。法人持股以 institutionsFloatPercentHeld 23.16% 計，屬中等。
- 外資與投信近期偏賣超（來源為散戶論壇與 WebSearch 摘要，未能取得正式買賣超數字）。

## Net sentiment score
Composite：**bullish（分析師面）/ neutral（散戶面）/ 整體 neutral-to-bullish（信心低）**

- 分析師面 bullish：8 buy、0 hold、0 sell，近 3 個月評等數增加。權重最高，但 yf 與 investing.com 數字不一致，且目標價日期混雜。
- 散戶面 neutral：多空並存，聲量定性為低至中等，Reddit 與 StockTwits 缺資料。
- 內部人面 DATA_UNAVAILABLE，不計入分數。
- 籌碼面偏弱：外資與投信近期賣超（未量化）。

Confidence：low-to-medium。主要原因為散戶與內部人資料缺漏、最新資料僅到 2026 年 9 月、以及 yf crumb 失效。

Divergence flag：**yes**。分析師面偏多，散戶與籌碼面偏觀望至偏空，方向相反，值得留意。但因散戶樣本過少，此分歧訊號的可靠度有限。

## Metrics

| 指標 | 數值 | 說明 |
|---|---|---|
| 分析師 buy / hold / sell（yf 當前） | 8 / 0 / 0 | strongBuy 3、buy 5 |
| 分析師 buy 數（3 個月前） | 6 | strongBuy 2、buy 4 |
| 分析師 buy 數變化（3 個月） | +2 | 無 hold、無 sell |
| 分析師 buy / hold / sell（investing.com，二手） | 6 / 0 / 0 | 與 yf 不一致 |
| 平均目標價（二手，日期混雜） | 963.6 元 | 最高 1150、最低 800 |
| 最新評等事件（二手） | 花旗 2026/04 升買入，目標 1150 元 | 無法於 yf 驗證 |
| Reddit 提及數 | DATA_UNAVAILABLE | WebFetch 無法連線 |
| StockTwits 訊息數 | DATA_UNAVAILABLE | DNS 失敗 |
| 台股社群多空傾向 | mixed | 樣本少，日期不明 |
| 聲量相對水準 | 低至中等（定性） | 信心低 |
| 內部人 6 個月淨買賣 | DATA_UNAVAILABLE | yf insider 空陣列 |
| 董監持股（Yahoo 股市，2025/12） | 17.80% | 2025 年 9 月底至 12 月未變動 |
| insidersPercentHeld（yf） | 43.48% | 與 Yahoo 股市定義不同 |
| institutionsPercentHeld（yf） | 13.09% | |
| institutionsFloatPercentHeld（yf） | 23.16% | |
| 機構家數（yf） | 176 | |
| 最新月收盤（2026/09，二手） | 699 元 | 8 月為 729 元 |
| 52 週區間（二手） | 526.00 至 1,115.00 元 | |
| 綜合情緒分數 | neutral-to-bullish | 信心低至中 |
| 方向分歧 | yes | 分析師偏多，散戶與籌碼偏觀望至偏空 |

SENTIMENT REPORT COMPLETE
