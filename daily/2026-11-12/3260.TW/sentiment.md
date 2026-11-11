# Sentiment — 3260.TW 威剛 as of 2026-11-12

> 資料完整度低。yf 工具四項查詢（recommendations / rec_summary / insider / major_holders）皆回傳空陣列，原因是 Yahoo cookie/crumb 取得失敗（ConnectionError）。Reddit 與 StockTwits 無法連線。本報告的情緒判斷主要依賴一則搜尋摘要，無法獨立驗證，置信度低。

## Analyst consensus
資料不可得。rec_summary 與 recommendations 皆回傳空值，無法列出買進 / 持有 / 賣出家數，也無法確認近期升降評與目標價變動。

搜尋摘要提到 2025 年 11 月有法人降評、目標價 200 元的報導，但該資料屬 2025 年舊聞，與 2026 年現況不符，本報告不採用。

## Retail social
- Reddit: 無法取得（r/wallstreetbets、r/stocks 搜尋皆連線失敗，未重試）。
- StockTwits / X: StockTwits 網域無法解析，未取得訊息流。X 端無直接資料，以下為一般新聞搜尋結果。
- 新聞面（2026-11-06 法說會相關報導，取自搜尋摘要，未能開啟原文）:
  - 第四季營收預期較第三季略為下滑，原因是年底客戶庫存結算。
  - 管理層對記憶體產業後市維持正向看法，認為 DRAM 全年缺貨，2027 年缺貨可能更嚴重；NAND Flash 漲幅可能趨緩但價格仍看漲。
  - 搜尋摘要另列 10 月營收 170.6 億元（月增 8.5%、年增 28.22%），累計前 10 月 1,343.68 億元（年增 222.73%）。
  - 最近可查到的股價為 2026-10-30 的 346.5 元（當日跌 4.28%）。摘要未提供 11 月股價，無法判斷近期走勢。
- Buzz 量: 無法量化（無 Reddit / StockTwits 計數）。新聞面可見的討論集中在法說會後的季增預期。
- Tilt: 從新聞論調看偏多（產業供需與價格），但對 Q4 營收季減有保留。散戶端無資料，無法判斷。
- Themes（新聞面）: DRAM 缺貨延續至 2027、高庫存在價格上行期是優勢、價格若反轉則庫存轉為風險、Q4 季減。

## Insider activity
資料不可得（yf insider 回傳空值）。6 個月內部人買賣淨額、CEO / CFO 等動向均無法確認。

## Ownership shifts
資料不可得（yf major_holders 回傳空值）。機構持股集中度趨勢無法判斷。

## Net sentiment score
Composite: 無法評分（neutral，置信度低）。
- 新聞面偏多（產業供需與管理層看法），但 Q4 季減與高庫存反轉風險提供平衡。
- 分析師端、散戶社群端、內部人端皆無資料，綜合判斷不具可靠性。

Divergence flag: 無法判定（缺少分析師與散戶端資料，無法比較兩者方向）。

## 資料來源與限制
- yf 四項查詢：皆空值，Yahoo cookie/crumb 取得失敗。
- Reddit（r/wallstreetbets、r/stocks）：連線失敗，未重試。
- StockTwits：api.stocktwits.com 網域無法解析，需於 session 網路設定中放行。
- uanalyze.com.tw 原文：網域無法解析，無法開啟，未能核實搜尋摘要中的數字。
- 搜尋摘要為二手整理，數字（營收、EPS、股價）未經原始來源驗證，使用時需謹慎。

## 待補資料（下次執行）
1. yf recommendations / rec_summary / insider / major_holders 需恢復 Yahoo 連線後重跑。
2. 放行 api.stocktwits.com 與 Reddit 的存取。
3. 確認 2026-11-06 法說會原文與 11 月股價。

SENTIMENT REPORT COMPLETE
