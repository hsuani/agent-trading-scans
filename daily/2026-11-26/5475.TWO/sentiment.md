# Sentiment — 5475.TWO（德宏） as of 2026-11-26

> 資料完整度低：Yahoo 分析師與內部人資料抓取失敗、Reddit 與 StockTwits 無法存取，本報告大部分結論只能依新聞與營收數據推論。以下「0 筆」代表資料未取得，不代表無人覆蓋或無人交易。

## Analyst consensus
0 buy / 0 hold / 0 sell（資料未取得）。`rec_summary` 與 `recommendations` 皆回傳空陣列，且 Yahoo cookie/crumb 取得失敗（ConnectionError），因此無法判斷是無資料還是抓取問題。
Recent moves：無可驗證的升評、降評或目標價變動。網路搜尋找不到 2026 年 11 月的目標價或券商評等。

## Retail social
- Reddit：無法存取（r/wallstreetbets 與 r/stocks 的 JSON 搜尋皆被擋）。無法判斷討論量或多空傾向。
- StockTwits / X：StockTwits 因網路白名單限制無法解析（api.stocktwits.com 未開放），需在 session 網路設定中允許該網域。X 無有效搜尋結果。
- 新聞面（替代指標）：11/17 收盤 166.50 TWD，單日 -9.76%，一週約跌 10%，但年初至今仍大幅上漲（來源：報價頁摘要，時間點為 11/17，非 11/26 最新價）。
- Buzz 量：無法量化，定性判斷為中低（僅少量新聞與報價頁，未見散戶論壇大量討論）。
- Themes（來自新聞，非散戶討論）：
  - NVIDIA Rubin 平台可能要求 M9 等級材料與石英纖維布，市場將德宏視為相關供應鏈題材。
  - 10 月營收 3.87 億 TWD，月增 19.6%、年增 388%，公司表示受價格與需求量同時上漲帶動。
  - 中國玻纖布漲價支撐毛利，上半年毛利率約 33.4%（來源：優分析報導，數字未交叉驗證）。
  - 董事長 2026 年初表示全年獲利樂觀，11 月未見更新表態。

## Insider activity
Net 6mo：無法取得（insider 工具回傳空陣列）。
Notable：無。
參考：內部人持股比例約 27.9%（`major_holders`，來源 yfinance 快照，未標明日期）。
另有公開報導指出 9/16 獨立董事逝世解任（屬董監異動，不是內部人買賣），與 6 個月內買賣無直接關係。
法人買賣報導數字互相矛盾：一篇寫近 5 日三大法人賣超 799 張，另一篇寫賣超 1,763 張，日期與內文月份無法確認，不採信為事實。

## Ownership shifts
- 機構持股比例約 2.7%（`institutionsPercentHeld`），流通股中機構占比約 3.8%，機構數 7 家。此數字對台股偏低，疑為 yfinance 對 .TWO 標的覆蓋不全。
- 趨勢：只有單一快照，無法判斷集中度是上升或下降。
- 可補充來源：公開資訊觀測站、Goodinfo 等法人買賣明細（需人工或其他工具抓取）。

## Net sentiment score
Composite：neutral（信心：低）。
- 基本面與題材偏多：營收爆發性成長、AI 材料供應鏈題材。
- 短線情緒偏弱：11/17 單日大跌約 10%，並有法人賣超報導（數字存疑）。
- 分析師與內部人端缺資料，無法給出可信的多空權重。

Divergence flag：無法判定（no）。分析師端與散戶端皆無有效資料，不能確認兩者是否背離。若日後補到分析師評等與論壇討論，再重新評估。

## Data gaps / follow-up
1. Yahoo recommendations 與 insider 空回傳，需確認 yfinance 對 .TWO 標的是否支援，或改用其他來源（如公開資訊觀測站、券商研究報告）。
2. Reddit 與 StockTwits 無法存取，需確認網路白名單或改用替代來源。
3. 股價引用為 11/17，與報告日 11/26 相隔數日，需補最新報價。
4. 名稱確認：5475 依搜尋結果為德宏，查詢時誤寫為德碁，搜尋結果確認兩者不同公司，本報告以 5475 德宏為準。

SENTIMENT REPORT COMPLETE
