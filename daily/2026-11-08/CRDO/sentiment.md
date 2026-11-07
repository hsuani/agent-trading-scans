# Sentiment — CRDO as of 2026-11-08

資料狀態：Reddit（r/wallstreetbets、r/stocks）與 StockTwits 直接抓取全數失敗（Reddit 被沙箱擋下；api.stocktwits.com DNS 解析失敗，需在 session 網路設定允許該網域）。本報告的散戶情緒僅能依賴 WebSearch 找到的第三方彙整頁，時效性與樣本數都有限。分析師與內部人資料來自 yf 工具（數據為快取，最新內部人交易日為 2026-10-27）。

## Analyst consensus

rec_summary（最新期間 0m）：**5 Strong Buy / 14 Buy / 1 Hold / 0 Sell / 0 Strong Sell**，共 20 位分析師，Buy 類佔 95%。
- 1 個月前（-1m）分布相同；2 個月前（-2m）Strong Buy 為 4，其餘相同。近兩個月評等結構穩定，無降級跡象。
- 近期動作：Stifel（Tore Svanberg）於 2026-10-05 重申 Buy，目標價由 $350 下調至 $310（依 WebSearch 之 Benzinga 彙整頁）。
- 目標價共識：多篇 2026-10 月文章引用共識目標價約 $279（另一來源列 13 位分析師中位數 $270），屬於第三方彙整，未與 yf 原始欄位對照。
- 評等變動歷史：`recommendations` 工具只回傳期間彙總，未提供逐筆升降評等紀錄，無法列出具體 upgrade/downgrade 日期。

## Retail social

- **Reddit**：直接抓取被擋，無法取得 r/wallstreetbets 或 r/stocks 的實際貼文樣本，本節無法給出可靠的貼文傾向。WebSearch 也未找到 2026-10 以後的 WSB 討論串。
- **StockTwits / X**：StockTwits API 無法連線，無訊息流數據。WebSearch 的 StockTwits 文章為舊資料（描述散戶追蹤人數一年內大增約 460%），不代表當前狀況。
- **情緒聚合站**：AltIndex 情緒分數 87/100，判定為 bullish（彙整 Reddit、StockTwits 與論壇），但註明近期情緒相較 30 日均值轉弱。該頁面未標示確切更新日期，權重應打折。
- **討論量（相對）**：無法量化提及次數。依聚合站描述，散戶關注度處於高位，但近期有降溫跡象，定性判斷為「高於一般，但較前期回落」。
- **Retail tilt**：偏多（bullish-leaning），信心低，主要依賴單一聚合站。
- **Themes（定性，取自聚合與新聞彙整）**：
  - AI 資料中心與高速連線（SerDes、主動式電纜）需求成長，為多頭主軸。
  - 估值偏高與股價回檔的疑慮，為空方主軸。
  - 客戶集中度風險：據 24/7 Wall St. 報導，最大客戶占營收 33%、次大客戶 28%。
  - 股價波動劇烈：2026-10 月中報價約 $187–213，2026-10-27 內部人成交價約 $155–168，下跌趨勢與多頭敘事形成張力。
- 注意：某 eToro 貼文稱財報後盤後下跌超過 12%，另一來源列 2026 Q3 營收 $407M（年增 201%）。這兩項未經交叉驗證，本報告不採用為事實。

## Insider activity

6 個月窗口（2026-05-08 至 2026-11-08）：**淨買入 $0M / 賣出 $202.8M**（以 yf insider 明細加總；買入 0 筆）。
- 賣出主力（USD M，6mo）：
  - Cheng Chi Fung（CTO）：約 $98.6M，18 筆，約 458,602 股。為最大賣方，多數為每週至雙週一次、約 27,500 股的固定規模賣出，符合預定交易計畫的樣態（此為推論，yf 未標示是否為 10b5-1 計畫）。
  - Lam Yat Tung（COO）：約 $67.0M，4 筆，約 311,339 股（2026-07-15 與 2026-07-31 集中賣出；2026-09-25 另有 175,000 股贈與）。
  - William Joseph Brennan（CEO）：約 $17.5M，3 筆，約 88,322 股（另有 2026-07-13 贈與 150,000 股）。
  - Daniel W. Fleming（CFO）：約 $13.5M，3 筆，約 55,160 股。
  - James L. Laufman（Officer）：約 $4.4M，4 筆，約 20,000 股。
  - 其他董事（Hosein、Sutardja、Danesh 等）：合計約 $1.7M，多為小額賣出或 RSU 授予（授予無現金流）。
- 重點觀察：高階主管（CEO、CFO、COO、CTO）全數在 6 個月內為淨賣方，且無任何公開市場買入。
- 數據差異：Quiver Quantitative 聚合頁稱 6 個月內內部人交易達 301 筆、皆為賣出；本報告依 yf 明細僅計 52 筆（窗口內），筆數口徑不同，金額以 yf 為準。

## Ownership shifts

- insidersPercentHeld：9.15%
- institutionsPercentHeld：74.75%；institutionsFloatPercentHeld：82.27%
- institutionsCount：1,337
- 趨勢：yf 僅提供單一快照，無歷史序列，無法判斷機構持股增減方向。以機構占比約 75% 看，籌碼以機構為主，散戶影響力有限。

## Net sentiment score

- **分析師面**：偏多，信心高（20 位分析師中 95% 為 Buy 類，無 Sell）。
- **散戶面**：偏多但轉弱，信心低（僅單一聚合站，Reddit/StockTwits 無資料）。
- **內部人面**：偏空訊號，信心中（6 個月約 $202.8M 賣出、零買入，但 CEO/CFO 賣出規模與持股比例需結合股票報酬評估，不能單獨解讀為看空）。
- **綜合**：**中性偏多（neutral-to-bullish），信心低至中**。分析師與散戶聚合訊號偏多，內部人持續賣出抵銷部分多方訊號；資料缺口（Reddit、StockTwits）使散戶面信心受限。

**Divergence flag：否（retail 與 analyst 同向偏多）**。但有一項內部人與分析師的分歧：分析師全數 Buy，而高階主管持續賣出，此類 insider-vs-analyst 分歧值得在後續判斷中留意。

資料缺口與後續建議：補抓 Reddit 與 StockTwits（需沙箱允許網域）後，可重新評估散戶面；建議取得 yf 之評等變動歷史（若快取支援）以補足升降評等紀錄。

SENTIMENT REPORT COMPLETE
