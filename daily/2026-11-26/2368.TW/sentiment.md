# Sentiment — 2368.TW 金像電 as of 2026-11-26

## Analyst consensus
9 buy / 0 hold / 0 sell（含 1 strong buy + 8 buy）。近四個月（0m 至 -3m）分布完全相同，未見評級升降級紀錄。
Recent moves: 資料工具未回傳 target price 變動與個別券商評等異動。新聞面有一家外資券商表態正面（11/11），預估 4Q 營收季增約 7%，並看好 Amazon Trainium 3 PCB 供應份額提升（評等與目標價未揭露）。另有法人估 EPS 最高 83.62 元，老客戶 AI 伺服器新產品預計 2027 年陸續量產。
注意：本次未取得 target price 共識值，無法計算目標價上行空間。

## Retail social
- Reddit: 本次無法取得。r/wallstreetbets 與 r/stocks 搜尋皆遭拒（Claude Code 無法連線 www.reddit.com），無樣本可引用，無法判斷多空傾向。
- StockTwits / X: StockTwits 無法解析網域（api.stocktwits.com 未在本次 session 允許網域內），無資料。X 側僅有新聞型搜尋結果，無可量化的留言樣本。
- 聲量（buzz volume）：無法量化對比基準，僅能由新聞量判斷媒體關注度偏高（10 月營收公布後多篇報導）。
- Themes（取自新聞面，非散戶留言）:
  - AI ASIC 市占提升，Trainium 3 PCB 供應
  - AI 伺服器占比高（報導指 3Q 營收約 77% 來自伺服器）
  - 10 月營收 99.13 億 TWD，年增約 76%，但較市場預期低約 8.9%（單月遜於預期，前 10 月累計略優於預期）
  - 2027 年老客戶新 AI 伺服器板卡量產
- 盤中參考價：11/11 外資報導當日盤中約 1,035 TWD（非收盤價，僅供時點參考）。

## Insider activity
Net 6mo: 資料缺失。`insider` 工具回傳空陣列，無法判定 6 個月內淨買賣金額，亦無法辨識 CEO / CFO 等個別申報人。
注意：空陣列可能代表無申報，也可能代表資料源缺漏，兩者在本報告中無法區分，故不視為「無內部人交易」的確切證據。
Notable: 無。

## Ownership shifts
- 內部人持股比例：約 30.3%（insidersPercentHeld）
- 機構持股比例：約 38.9%；占流通股比例約 55.7%
- 機構家數：248 家
- 趨勢：工具僅回傳當期快照，無歷史序列，無法判斷集中度是增加或減少。

## Net sentiment score
Composite: **bullish（信心：中低）**

- 分析師面：強烈偏多（9 buy、0 hold、0 sell，四個月持平）。
- 新聞面：偏正面（AI 需求、營收成長、2027 量產預期），但 10 月單月營收低於預期是主要近期負面點。
- 散戶面：無資料。
- 內部人面：無資料。

信心偏低的原因：散戶與內部人兩項主要訊號缺失，且分析師評等為整體共識，缺乏目標價與近期評等變動的細節。

Divergence flag: **無法判定（no）** — 散戶傾向資料缺失，無法與分析師傾向比對。若後續補齊 Reddit / StockTwits 資料，需重新評估是否出現散戶與分析師背離。

資料來源狀態：
- yf recommendations / rec_summary：成功
- yf insider：回傳空陣列
- yf major_holders：成功
- Reddit (r/wallstreetbets, r/stocks)：無法連線
- StockTwits：DNS 無法解析，需於 session 網路設定允許 api.stocktwits.com
- WebSearch 新聞：成功（來源：finance.technews.tw 2026/11/06 10 月營收報導；uanalyze.com.tw 相關文章；ltn.com.tw 焦點股分析）

SENTIMENT REPORT COMPLETE
