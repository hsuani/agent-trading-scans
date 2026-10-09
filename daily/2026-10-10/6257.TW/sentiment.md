# Sentiment — 6257.TW（矽格） as of 2026-10-10

> 註：執行當下系統日期為 2026-10-09，本報告依任務指定之 as-of 日期 2026-10-10 標示。資料時點以各來源實際發布日為準。

## Analyst consensus
資料可信度低，無法給出可靠的買進/持有/賣出分布。

- `yf 6257.TW rec_summary` 與 `recommendations` 回傳 0m、-1m、-2m 皆為 1 strongBuy、0 buy/hold/sell/strongSell。此結果疑似為 Yahoo 連線失敗（cookie/crumb fetch 失敗）下的殘留或不完整資料，且樣本數僅 1，不足以代表整體評等分布。判定為 DATA_UNAVAILABLE（分布）。
- `yf SPIL rec_summary` 連線被 403 阻擋，無法作為替代來源。
- 近期法人動向（WebSearch，來源為經濟日報/鉅亨轉載）:
  - 「AI等三大訂單動能強勁 法人調高矽格目標價」：法人將目標價調升近四成，理由為 AI、ASIC、矽光子與高速運算測試需求吃緊，預估 2026 年營收逐季走高。原文未列出新舊目標價數字與發布投顧名稱。來源: https://money.udn.com/money/story/5607/9614835
  - 同一批搜尋結果提到一份 2026 年 9 月底的法人追蹤名單，列矽格目標價 304 元。來源未明，數字未經交叉驗證，僅作參考。
  - 2025 年 12 月本土法人曾調升評等至買進，外資當時持續買超（來源: https://www.ctee.com.tw/news/20251226700828-430201 ）。此為較舊資料。
- 目標價變動方向：近期均為上調，但無法量化具體幅度與各家投顧明細。

## Retail social
- Reddit（r/wallstreetbets、r/stocks）：WebFetch 被阻擋（"unable to fetch from www.reddit.com"），本次無法取得。DATA_UNAVAILABLE。
- StockTwits：未嘗試。以 WebFetch 取得金融網站屬於任務限制外，且該來源以美股為主，覆蓋台股 6257 的可能性低。DATA_UNAVAILABLE。
- PTT / Dcard：WebSearch 未回傳任何 PTT Stock 板或 Dcard 討論串，無法計算聲量。DATA_UNAVAILABLE。
- X / 新聞聲量（WebSearch）：搜尋結果以新聞、財經網站與個股資料頁為主，未見散戶討論內容。無法做出可靠的聲量對比。
- 聲量（定性）：無法與歷史基準比較。以媒體報導數量觀察，7 月至 10 月間營運新聞頻繁（月營收創高、法說、資本支出上修），屬基本面話題為主。
- 情緒傾向（僅就新聞語氣，非散戶意見）：偏多。
- 主要題材（來自新聞，非散戶原文）：
  - AI / ASIC / 矽光子 / CPO 測試需求
  - 湖口二廠產能開出、竹東中興新廠 2027 年第一季量產
  - 資本支出由 59 億元上修至 88 億元（約 +49%）
  - 測試價格調漲，大部分客戶簽訂一年以上產能保障協議（2026 年 10 月 6 日法說）
  - 獲利創高（2026 上半年 EPS 4.65 元）
- 代表性新聞語句（≤15 字）：「AI等三大訂單動能強勁」（經濟日報標題，來源同上）。

## Insider activity
Net 6mo: DATA_UNAVAILABLE。

- `yf 6257.TW insider` 兩次回傳皆為空陣列 `[]`，且伴隨 Yahoo cookie/crumb 連線失敗，無法判斷是「無內部人交易」還是「資料來源失敗」。
- WebSearch 查詢董監事持股轉讓申報未找到 2026 年相關資料。
- 建議直接查詢公開資訊觀測站之「董監事持股轉讓事前／事後申報」以確認。
- Notable: 無法判定。

## Ownership shifts
- `yf 6257.TW major_holders`（可取得）:
  - 內部人持股比例 (insidersPercentHeld): 7.87%
  - 機構持股比例 (institutionsPercentHeld): 17.92%
  - 機構佔流通股比例 (institutionsFloatPercentHeld): 19.45%
  - 機構家數 (institutionsCount): 77
- 趨勢（時間序列）: DATA_UNAVAILABLE。工具僅回傳當期快照，無法比較季度變化。
- 注意：此為 Yahoo 資料，來源可能不反映台股實際外資/投信持股細項。

## Net sentiment score
Composite: 偏多（bullish lean），信心中低（low-to-medium）。

依據：
- 新聞與法人端（可量化程度低）：偏多，目標價上調、營運創高、產能與資本支出擴張。
- 內部人：無資料，無法納入。
- 散戶社群：無資料，無法納入。
- 分析師評等分布：資料不可靠，無法納入。

信心受限於：散戶與內部人資料全數缺失，分析師分布數據品質不足，目前結論幾乎完全依賴新聞媒體語氣，不等同於市場實際情緒。

Divergence flag: 無法判定（no）。缺乏散戶與分析師可信分布，無法比較兩者方向是否相反。

## Data gaps
- Yahoo Finance（yf）連線失敗（cookie/crumb 取得失敗），影響 rec_summary、recommendations、insider 的可信度。
- Reddit WebFetch 被阻擋。
- StockTwits 未嘗試。
- PTT / Dcard 無結果。
- 台股內部人申報、分析師評等分布需改用 公開資訊觀測站、券商研究報告或鉅亨網/Goodinfo 等來源補查。

## Sources (WebSearch)
- https://money.udn.com/money/story/5607/9614835 （法人調升目標價）
- https://www.ctee.com.tw/news/20251226700828-430201 （2025/12 評等與外資買超）
- https://uanalyze.com.tw/articles/5372456601 （AI 客戶長約、光通訊）
- https://www.ctee.com.tw/news/20260806701504-430201 （2026 上半年獲利創高）
- https://wantrich.chinatimes.com/news/20260806900321-420101 （2026/8 營運與股價）

SENTIMENT REPORT COMPLETE
