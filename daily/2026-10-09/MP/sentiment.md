# Sentiment — MP (MP Materials) as of 2026-10-09

## Analyst consensus
目前 19 位分析師：5 strongBuy / 13 buy / 1 hold / 0 sell / 0 strongSell（yf rec_summary，0m 期）。共 18 Buy、1 Hold、0 Sell，以 Buy 為主。

- 近四個月趨勢：sell 始終為 0；hold 由 0 增至 1（大約在 -2m 至 -1m 之間出現一筆 Hold），Buy 家數持平於 13，strongBuy 持平於 5。
- 近期變動：yf recommendations 只提供彙總計數，無個別券商升降級明細，因此無法確認每一筆 upgrade/downgrade。
- 次要來源（Benzinga 9/18 快照）：9/16 有一筆 Hold 初次覆蓋，目標價 $57；8/24 DA Davidson Buy。與 yf 的 hold 增加時點吻合。
- 目標價：Benzinga 平均共識目標價 $65（9/18 快照）；Fintel 平均一年目標價 $78.28（8/28 快照）。兩者日期與樣本不同，差距大，需以原始資料再確認。

## Retail social
- **Reddit (r/wallstreetbets, r/stocks)**: 資料缺失。WebFetch 無法連線，curl 經 proxy 回傳 CONNECT 403，判定為出口政策封鎖，已 soft-fail，未嘗試繞過。
- **StockTwits**: 資料缺失。同樣 proxy 403，無法取得訊息量與 bullish/bearish 標籤。
- **X / 新聞 / 第三方聚合（WebSearch，非原始貼文）**:
  - LunarCrush 頁面：social sentiment 約 88% positive，屬於以互動量計算的短期指標，日期不明，可信度低。同頁提到股價上漲 9.1% 至 $60.10，歸因於 DoD 磁鐵訂單與政府持股。
  - Benzinga 9/18 快照：short float 19.6%，標示為上升中的 bearish 訊號。
  - Stockscan 技術面摘要：Strong Sell，但無日期，且 2027 目標價遠低於其他來源，權重應打折。
- **Buzz 量**: 無法量化（無 Reddit/StockTwits 計數），無法與歷史基準比較，記為未知。
- **Themes（從次要來源歸納）**: (1) 美國國防部磁鐵訂單與政府股權，被視為利多；(2) 連續多季營業虧損，成本上升（Zacks/Nasdaq 文章指出 Q1 2026 cost of sales 年增 52%）；(3) short interest 上升；(4) 中長期稀土價值鏈定位的估值爭論。

## Insider activity
Net 6mo: 無資料。yf insider 回傳空陣列，無法確認是無交易或是資料缺口，因此不能判定為 $0 淨買或淨賣。
- Notable: 無可引用的 CEO/CFO 或其他董監事交易紀錄。
- 持股結構參考（非交易資料）：insidersPercentHeld 19.6%。此數字為持股比例，不代表交易方向。

## Ownership shifts
- 機構持股 77.7%（占流通股 96.6%），機構家數 970。
- 單期快照，無法判定近期增減趨勢。
- 機構持股比例高，流通籌碼多在機構手中，這也解釋了為何 short float 與機構持倉可以同時偏高。

## Net sentiment score
**Composite: 偏多（bullish-leaning），信心：低**

- 分析師面：強偏多（18/19 Buy，0 Sell，目標價均值高於現價快照）。權重高，但屬於滯後指標。
- 零售面：無原始資料，僅有第三方指標偏多（88% positive，但來源可信度低）。
- 空方面：short float 19.6% 且上升，技術面彙總偏空（但來源不明）。
- 內部人：無資料，無法納入。
- 基本面：持續虧損，屬於風險因子，但不直接是情緒指標。

信心偏低的原因：Reddit、StockTwits 與 insider 皆為缺口，且 DATE 與資料時點錯位。

**Divergence flag: 無法判定（inconclusive）**
- 無可靠的零售 tilt，無法直接判斷零售與分析師是否反向。
- 能觀察到的是分析師（偏多）與 short interest / 技術彙總（偏空）之間的分歧。這種分歧在本次資料中可見，但不能等同於零售與分析師分歧。

## Upcoming catalyst
Investing.com 列出下次財報日為 2026-10-29，屬於近期最大的情緒觸發點。

SENTIMENT REPORT COMPLETE
