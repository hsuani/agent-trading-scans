# Sentiment — 6515.TW (穎崴 WinWay Technology) as of 2026-10-31

## Executive summary

穎崴的分析師評級高度一致偏多：yfinance 快照顯示 12 位分析師中 4 位 Strong Buy、8 位 Buy，無 Hold 與 Sell，過去三個月覆蓋家數由 10 增至 12。散戶與社群情緒本次無法量化：Reddit 與 StockTwits 皆被阻擋，WebSearch 只取得少數無日期的 CMoney 論壇片段，語氣分歧，偏悲觀的留言提到近期跌幅與法規風險，也有偏樂觀的留言。內部人交易資料為空，無法判斷。綜合判斷為「偏多（以分析師為主）」，信心低，主要因為散戶與內部人兩項缺資料，且分析師資料多為 2026 年 8 月前後的快照，不是 10 月。

## Retail / social sentiment

- **Reddit（r/wallstreetbets、r/stocks）**：DATA_UNAVAILABLE。WebFetch 回傳 "Claude Code is unable to fetch from www.reddit.com"，無法取得貼文樣本與情緒比例。
- **StockTwits**：DATA_UNAVAILABLE。api.stocktwits.com 無法解析（host 不在本 session 允許網域內），需在 session 網路設定中放行後才能重試。
- **X / 新聞與論壇（WebSearch）**：
  - CMoney 股市爆料同學會（cmoney.tw/forum/stock/6515）留言分歧。偏空留言認為近期跌幅很大，關注風險與法規問題；偏多留言的代表語句例如「來個5連漲喔」。這些留言沒有標示日期，無法確認是否屬於 2026 年 10 月。
  - 籌碼面的留言提到外資買進、投信賣出，顯示資金方向不一，但未附日期與張數，只能作為定性參考。
  - 無法從搜尋結果取得可信的正負面比例，因此本報告不給出任何情緒百分比。
- **Retail 聲量**：無法與歷史基準做量化比較（DATA_UNAVAILABLE）。
- **主要主題（定性）**：
  1. 近期股價回檔與跌幅幅度（偏空）。
  2. 法規與風險事件的疑慮（偏空，細節未能確認）。
  3. AI / HPC 產業上行周期下的長期成長期待（偏多）。主要來源是較早的高盛報告，時間點早於 10 月。
  4. 基本面營收創高（偏多）。nStock 10 月 13 日頁面列示 2026 年 9 月營收約 12.5億 TWD（月增約 -26.69%、年增約 87.72%，頁面稱為十年單月同期新高）。
- **資料一致性警示**：同一 nStock 網站不同頁面的股價差距大（10 月 13 日頁面 6,025 元；6 月 27 日頁面 8,190 元）。股價以證交所即時行情為準，本報告不採用其中任一價格判斷情緒。

## Analyst consensus

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 合計 |
|---|---|---|---|---|---|---|
| 目前（0m） | 4 | 8 | 0 | 0 | 0 | 12 |
| -1m | 4 | 7 | 0 | 0 | 0 | 11 |
| -2m | 4 | 7 | 0 | 0 | 0 | 11 |
| -3m | 4 | 6 | 0 | 0 | 0 | 10 |

（來源：`pipeline/tools/yf 6515.TW rec_summary` 與 `recommendations`，兩者數據相同。數據單位為家數，非金額。）

- **近期評級變動**：`recommendations` 只提供計數，沒有逐家券商的升降評等紀錄，因此無法確認個別升降級事件。以計數變化看，3 個月內無降評，Buy 家數由 6 增至 8，有新增覆蓋。
- **個別券商動態（WebSearch 聚合資料，非 yfinance）**：
  - Nomura 於 2026 年 7 月 24 日首次覆蓋，評等 Buy，目標價 8,315 元。
  - Citi 於 2026 年 5 月 28 日維持 Buy，目標價 13,000 元。
  - 高盛較早報告目標價 15,000 元（時間點早於 10 月，僅供參考）。
- **目標價共識（聚合來源，TWD 元/股）**：平均約 12,012 至 12,534 元，依來源而異；高點 15,000 元，低點 8,315 元。不同聚合站的平均數不一致，不應視為精確值。
- **資料缺口**：yfinance 計數為 12 家，S&P Global 聚合為 10 家，家數口徑不同。目標價與股價的時間點大多在 2026 年 5 月至 8 月，並非 10 月 31 日的即時數據。投資人需以券商研究報告與證交所行情為準。

## Institutional / insider activity

- **內部人交易（insider）**：DATA_UNAVAILABLE。`pipeline/tools/yf 6515.TW insider` 回傳空陣列，無法判斷為「無交易」或「資料缺失」，因此不作「無內部人交易」的結論。6 個月淨買賣金額無法計算。
- **台灣公開資訊觀測站董監持股申報**：未能於本次取得（tw.stock.yahoo.com 無法解析），需於 session 放行後再補查。
- **大股東與機構持股（major_holders）**：
  - 內部人持股比例約 29.38%（`insidersPercentHeld`）。
  - 機構持股比例約 30.26%（`institutionsPercentHeld`），占流通股約 42.85%（`institutionsFloatPercentHeld`）。
  - 機構家數 114 家（`institutionsCount`）。
  - 本工具只提供單一時點快照，無法判斷機構持股的趨勢是增加或減少，此項標記為趨勢 DATA_UNAVAILABLE。
- **外資與投信買賣超**：僅有 CMoney 留言片段提到外資買、投信賣，無日期與張數，不作為量化依據。

## Overall sentiment verdict

| 面向 | 判斷 | 信心 |
|---|---|---|
| 分析師評級 | 偏多（12 家中 12 家 Buy 或以上，0 Hold、0 Sell） | 中（家數少、快照非當日） |
| 散戶與社群 | 無法量化，語氣分歧，偏空與偏多留言並存 | 低 |
| 內部人 | DATA_UNAVAILABLE | — |
| 機構持股 | 持股比例高，趨勢未知 | 低 |

**綜合情緒：偏多（以分析師為主），信心低。**

**分歧旗標（divergence flag）：無法判定。** 分析師端明確偏多，散戶端的 CMoney 片段語氣分歧且無日期，無法確認兩者是否方向相反。若後續取得 Reddit 或 StockTwits 資料，需重新檢查是否出現「分析師偏多、散戶偏空」的背離。

**缺口與後續**：
1. Reddit 與 StockTwits 需放行網域後重試（或改用其他公開來源）。
2. 內部人交易需以台灣公開資訊觀測站或證交所資料補查。
3. 分析師目標價與評級需更新至 10 月份的券商報告。
4. 股價口徑需以證交所即時行情統一，避免使用 nStock 不同頁面的歷史快照。

SENTIMENT REPORT COMPLETE
