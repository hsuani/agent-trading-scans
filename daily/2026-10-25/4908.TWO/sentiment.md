# Sentiment — 4908.TWO (前鼎光電 APAC Opto Electronics) as of 2026-10-25

> 資料截止說明：系統日期為 2026-10-24，任務指定 DATE=2026-10-25。價格資料為 yfinance 快照與第三方頁面混合，時間點不一致（見下方），本報告以「資料不足」為主要結論。

## Analyst consensus
0 buy / 0 hold / 0 sell（yfinance 無分析師覆蓋資料：`recommendationKey=none`、`numberOfAnalystOpinions=null`，`rec_summary` 與 `recommendations` 皆為空）。
近期升降評、目標價變動：無可查資料。網路搜尋未找到 2026 年 10 月的券商評等或目標價。
判定：覆蓋度極低，分析師端不構成可用訊號。

## Retail social
- Reddit（r/wallstreetbets、r/stocks）：WebFetch 被拒（無法連線 www.reddit.com），本來源跳過，無樣本。
- StockTwits：DNS 解析失敗（api.stocktwits.com 無法連線），本來源跳過。
- 台股社群（CMoney 股市爆料同學會，經搜尋摘要）：聲量低，偏謹慎至偏空。代表性看法（摘要改寫，非原文）：「缺乏主力資金支撐，股價信心偏弱，籌碼面偏空」；另有「213 元以上有買盤撐住」的反方意見。
- 聲量（定性）：未取得可量化的提及次數，以搜尋結果數量判斷屬低聲量標的。PTT 股板未找到相關文章。
- X / 新聞：未找到有效的 X 討論樣本。
- Themes（重複出現的議題）：
  1. 主力支撐不足、籌碼偏空
  2. 「轉型、不做光通」消息的負面反應
  3. 估值過高（本益比約 87 倍，statementdog 頁面）
  4. 通信網路 / AI 需求受惠的正面敘事（Yahoo 股市新聞標題「受惠 AI 需求熱」）
  5. 曾多次被櫃買中心列為注意股（四月與七月初，七月引述漲幅 164.33%），投機屬性受關注
  6. 營收基本面正面：2026 年 6 月營收約 0.91 億 TWD，年增約 29.7%，為十年同期單月新高

## Insider activity
Net 6mo: 資料不足。yfinance `insider` 回傳空值，網路搜尋未找到 2026 年董監事持股申報或轉讓明細。
Notable: 無可確認的個別交易紀錄。
持股結構參考：Yahoo `heldPercentInsiders` 為 44.18%（內部人持股集中度高，屬持股比例而非買賣方向）。
建議交叉查核：公開資訊觀測站（mops.twse.com.tw）「內部人持股轉讓事前申報」與「董事、監察人持股變動」公告。

## Ownership shifts
- Yahoo `major_holders`：institutionsPercentHeld 約 0.9%、institutionsCount 5，法人持股比例極低。
- 無法取得期間變化（僅單一快照），趨勢判斷不可得。
- 法人買賣超資料停留在 2026 年 1 月（Yahoo 頁面），無近期籌碼數據。

## Price / market-cap reference（單位：TWD 億，市值以 yfinance 股數 × 股價重算核對）
| 項目 | 數值 | 來源 / 備註 |
|---|---|---|
| 股價（yfinance currentPrice） | 197.0 TWD | yfinance 快照，時點未標示 |
| 流通股數 | 78,217,000 股 | yfinance `sharesOutstanding` |
| 市值 | 154.1 億 TWD | 核對：78,217,000 × 197 ≈ 15,408,749,000 TWD = 154.1 億 |
| 2026/10/13 收盤 | 219 TWD（單日 -9.88%） | statementdog 頁面 |
| 2026/07 前後股價 | 約 135–141 TWD | MONEY LINK / histock 頁面，時點不一 |
| 本益比 | 約 87 倍 | statementdog 頁面 |
| 2026/06 月營收 | 約 0.91 億 TWD（年增 29.7%） | nStock 頁面 |
| 2026/1–6 累計營收 | 約 5.21 億 TWD（年增 24.5%） | nStock 頁面 |

注意：各來源股價差異大（135 至 219 TWD），應以交易所或櫃買中心當日收盤為準。

## Data quality notes
- 初次搜尋誤把 4908.TWO 對應到昇貿（3305），已更正：4908 為前鼎光電，櫃買中心上櫃，Yahoo longName 為 APAC Opto Electronics Inc.。
- yfinance 的 cookie/crumb 取得失敗，多數端點回傳空值；需要時可重試或改用 TWSE/TPEx 官方公告。
- Dashboard（L0 Monitor，2026-10-24 18:51）將本標的列為 STOP BREACHED，價格 197.00。本報告僅作情緒面引用，不做交易建議。

## Net sentiment score
Composite: **偏空（neutral-to-bearish 傾向）**，信心：**低**。
- 散戶（台股社群）：偏謹慎至偏空，主題集中於籌碼與估值。
- 分析師：無覆蓋，無法形成方向性判斷。
- 內部人：無可用交易資料。
- 基本面（營收）：年增正向，但市場主要敘事為估值與籌碼。
- 樣本量極小，主要依賴單一社群摘要，結論可信度低。

Divergence flag: **無法判定**（分析師端無評等，無法比較散戶與分析師方向是否相反）。

SENTIMENT REPORT COMPLETE
