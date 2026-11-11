# Sentiment — 4958.TW (臻鼎-KY) as of 2026-11-12

資料完整度提醒: 本次僅取得分析師共識 (yf) 與新聞型態的法人/媒體敘述。Reddit 與 StockTwits 無法連線, 內部人交易資料為空陣列 (未能確認是真的零交易或來源缺漏)。yf 的 cookie/crumb 取得失敗, 但仍回傳數值; 快照時點無法從工具輸出確認。以下結論信心偏低。

## Analyst consensus
10 buy / 0 hold / 0 sell (其中 strongBuy 2, buy 8; 單位: 家數)。

| 期間 | strongBuy | buy | hold | sell | strongSell |
|---|---|---|---|---|---|
| 0m (當期) | 2 | 8 | 0 | 0 | 0 |
| -1m | 2 | 8 | 0 | 0 | 0 |
| -2m | 2 | 8 | 0 | 0 | 0 |
| -3m | 2 | 7 | 0 | 0 | 0 |

- 近四個月評等結構幾乎沒有變化, 只有 -3m 時點少一家 buy, 之後維持 10 家, 未見評等下調。
- 工具 `recommendations` 回傳的是評等家數的期間序列, 不含逐筆升降評等紀錄, 因此無法列出個別券商的 upgrade/downgrade 事件。
- 目標價: 依 WebSearch 摘要, FactSet 13 位分析師中位數 2026 EPS 預估由 13.85 元上修至 14.46 元, 目標價中位數 560 元 (TWD)。另有 UDN 報導指稱分析師在 Q3 獲利優於預期後上修獲利與目標價 (未取得各家目標價明細)。
- 管理層於 10 月法說指引 2026 年營收再創新高 (摘要寫 "400–500 billion NT dollars", 單位疑為 億 而非 billion, 需以原始法說資料核對後才可引用)。

## Retail social
- Reddit (r/wallstreetbets, r/stocks): 無法連線 (WebFetch 回傳 "unable to fetch"), 本次無樣本, 無法判斷散戶傾向。
- StockTwits: 無法解析 (api.stocktwits.com DNS 解析失敗, 需於 session 網路設定允許該網域), 本次無樣本。
- X / 新聞 chatter: WebSearch 僅取得媒體與法人文章, 無可靠的散戶貼文樣本。
- 緩和說明: 媒體摘要中 MoneyWeekly 提及融資餘額約三倍成長、外資短期偏空賣超、靜態 P/E 約 62 倍, 這些屬於 "市場觀點" 而非散戶社群資料, 不能直接當成散戶情緒。
- Buzz 量: 無法量化, 無 Reddit/StockTwits 計數可與常態比較。
- 主題 (取自媒體文章, 非散戶貼文): (1) AI 高階應用帶動獲利, 法人預估 AI 營收 2027 年占比超過 30%; (2) 估值偏高 (靜態 P/E 約 62 倍) 與融資籌碼放大; (3) 600 元關卡壓力; (4) 鴻海釋股事件被部分報導視為已反映 (利空出盡)。

## Insider activity
yf `insider` 回傳空陣列, 未取得 6 個月內董監或經理人申報交易。台股董監持股變動依規定申報, 但 yfinance 對台股覆蓋不完整, 因此此欄位為 "資料不可得", 不可解讀為零交易。
Net 6mo: 資料不可得 (buys: 未知, sells: 未知)。Notable: 無。

## Ownership shifts
- 內部人持股比例 (insidersPercentHeld): 26.9%
- 機構持股比例 (institutionsPercentHeld): 29.4%
- 機構持股占流通股比例 (institutionsFloatPercentHeld): 40.3%
- 機構家數 (institutionsCount): 213
- 趨勢: 工具僅提供單一時點快照, 無法判斷集中度變化方向。
- 媒體提及鴻海 (Hon Hai) 處分持股一事 (10 月初報導), 屬於大股東減持事件, 但摘要未給出確切股數與比例, 無法換算金額。

## Fundamentals context (僅供對照, 非情緒資料)
- 2026 年 10 月營收 271.97 億 TWD, 月增 3.2%, 年增 40.0% (來源: TechNews 2026/11/05 報導)。
- 2026 年 1–10 月累計營收 1,809.80 億 TWD, 年增 24.8%。
- 手算檢核: 10 月 271.97 億 ÷ (1+40.0%) ≈ 194.3 億 (去年同月), 9 月約 263.5 億 (271.97 ÷ 1.032), 數量級合理。

## Net sentiment score
**Composite: 偏多 (bullish), 信心: 低 (low)**
- 分析師面: 強烈偏多 (10/10 buy, 近四月無下調, EPS 預估上修)。
- 散戶面: 無資料, 不計分。
- 內部人面: 無資料, 不計分。
- 媒體/法人敘述: 基本面偏多, 但估值與籌碼 (融資、外資賣超、股價短線走弱) 為明顯反方論點。WebSearch 摘要提到 11/6 前後股價五日跌幅約 23% (Goodinfo 快照), 與早期偏多報導不一致, 此數字未經即時報價驗證, 不應直接採用。

**Divergence flag: 無法判定 (no)**
- 因為缺少散戶與內部人資料, 無法確認散戶傾向是否與分析師傾向相反。
- 若日後補齊 Reddit/StockTwits 資料, 應重新檢查此欄位。

**本報告不含交易建議。**

## Data gaps and follow-up
1. Reddit (r/wallstreetbets, r/stocks) 無法連線; 需於 session 網路設定允許 reddit.com 或改用其他可用來源。
2. StockTwits 網域解析失敗, 需允許 api.stocktwits.com。
3. yf insider 空陣列: 建議以台灣公開資訊觀測站董監持股申報資料補查。
4. 10 月法說指引 "400–500" 的單位需以原文核對 (億 vs B)。
5. 股價快照時點未知, 「5 日跌 23%」需以即時報價確認。

SENTIMENT REPORT COMPLETE
