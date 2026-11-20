# Sentiment — 6510.TWO (精測) as of 2026-11-20

Reddit 與 StockTwits 無法取得，零售情緒部分為缺漏資料。

## Analyst consensus
10 家：4 Strong Buy / 6 Buy / 0 Hold / 0 Sell（rec_summary 當期）。
近三個月趨勢（recommendations 聚合數）：
- -3m：9 家（4 SB / 5 B）
- -2m：9 家（4 SB / 5 B）
- -1m：10 家（4 SB / 6 B）
- 0m：10 家（4 SB / 6 B）

近期變化：約 -2m 至 -1m 間新增 1 家 Buy，未見降評。工具只回傳聚合數，未提供個別券商的升降評名稱，因此無法列出具名券商動向。目標價資料未取得。

新聞端的法人論述（UDN/經濟日報）稱獲利優於預期，並把 2026 年營收預估上修至約 72.6 億 TWD（年增約 51%），並提到與台灣手機客戶的 AI ASIC 新專案。該文章日期有不一致之處，需保守看待。

## Retail social
- Reddit（r/wallstreetbets、r/stocks）：無法取得，回傳錯誤 "Claude Code is unable to fetch from www.reddit.com"。無樣本貼文，無法判定 tilt。
- StockTwits：無法解析 api.stocktwits.com（DNS 失敗），需由 session 網路設定允許該網域後才能重試。
- X / 新聞討論：僅有單次搜尋，以台灣財經媒體為主，論調偏正面（營收成長、法人看好）。未找到可量化的社群提及數，無法與平常水準比較。
- Themes（僅依新聞與媒體）：HPC / AI 需求帶動、智慧型手機 AP 測試、AI ASIC 新客戶、估值偏高（P/E 約 65.7、P/B 約 10.3，來源為 wantgoo，日期未明）、股價波動大。
- 價格與資金流（nstock，約 11/13）：收盤 3,335 TWD，單日約 +4.4%；近十日外資賣超、投信買超。Goodinfo 另有一筆約下跌 5% 至約 2,910 TWD 的紀錄，日期不明，無法確定哪筆為最新。

## Insider activity
yfinance insider 回傳空陣列，無法取得 6 個月內的內部人買賣資料。淨買賣金額：未知（資料缺漏，非零）。

## Ownership shifts
- 內部人持股 36.8%
- 機構持股 27.7%（占流通股 43.8%），機構家數 74
- 僅有單一時點快照，無法判斷集中度趨勢。

## 資料品質備註
- 營收數字（單位 億 TWD）：2026/10 單月 7.02 億，年增約 72.7%；1–10 月累計 56.04 億，年增約 39.5%。11 月單月約 3.99 億（UDN 標題）。
- 手算檢核：若全年為 72.6 億，則需 12 月約 12.6 億，遠高於 10 月水準，與 11 月數字不協調。此「全年 72.6 億」應視為未驗證的法人預估，不宜直接採用。
- 價格日期有衝突（約 3,335 與約 2,910），未能確定最新報價。

## Net sentiment score
Composite：**偏多（bullish），信心低至中等**。
- 分析師端：偏多且一致（10/10 買進，無賣出或持有）。
- 零售端：無資料，無法評估。
- 資金流：外資偏賣、投信偏買，訊號混合。
- 估值：高（P/E 約 65，P/B 約 10）。

Divergence flag：**無法判定（no）**。零售 tilt 缺漏，無法與分析師端比較。待 Reddit 或 StockTwits 可用後，再重新評估背離。

SENTIMENT REPORT COMPLETE
