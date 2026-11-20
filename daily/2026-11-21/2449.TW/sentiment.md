# Sentiment — 2449.TW 京元電 as of 2026-11-21

## 資料來源狀態
- yf 工具：Yahoo 端點於本次執行時回傳 403 / ConnectionError，部分結果來自 repo cache，cache 的抓取時間未標示，無法確認與 2026-11-21 的時間差。
- insider、inst_holders 回傳空陣列。因 Yahoo 連線失敗，無法區分「確實無交易」與「抓取失敗」，因此以 DATA_UNAVAILABLE 處理。
- Reddit（r/wallstreetbets、r/stocks）與 StockTwits 未實際抓取。這兩個平台以美股為主，對台股個股的討論量很低，本次略過，並非遭封鎖。
- 散戶討論以 WebSearch 摘要為主。未能直接讀取 PTT Stock 或 Dcard 原文，無法取得帖文數量的實際統計。

## Analyst consensus
16 位分析師中，5 位 strongBuy、11 位 buy，hold 與 sell 皆為 0。
- 近四個月分布：當期與前一月為 strongBuy 5 / buy 11；前二、三個月為 strongBuy 4 / buy 11。買進評等數量沒有變化，strongBuy 在近兩個月增加 1 位。
- 目標價變動（來自 WebSearch 新聞摘要，非 yf 結構化資料）：富邦投顧將目標價由 350 元下修至 300 元，維持「買進」；富邦下修理由是目標本益比由 23 倍降至 20 倍，2027 年 EPS 預估變動不大。凱基投顧重申 300 元目標價。
- 升評降評的逐筆明細：DATA_UNAVAILABLE（yf recommendations 只回傳月度彙總，沒有逐筆紀錄）。
- 注意：分析師家數與期間標籤來自 cache，抓取日期不明。

## Retail social
- Reddit：未抓取，台股個股在 r/stocks 與 r/wallstreetbets 幾乎無討論，本次不作為訊號來源。
- StockTwits：未抓取。
- PTT / Dcard / 社群頁面（WebSearch 摘要）：
  - CMoney 股市社群頁顯示，近期留言悲觀者較多，認為股價轉弱、短線賣壓抬頭；同時也有看好 AI 題材的正面留言。多空並存，偏向謹慎。
  - poorstock.com 的留言板以短評為主，多數偏空，談股價下跌與外資賣超，帖文跨度為 2019 至 2026 年。
  - Mobile01 有數篇個股討論串，主題為是否續抱至下一季財報，語氣偏觀望。
  - 玩股網分析文指出大戶持股約 55%、散戶持股約 30%，股東人數持續增加，認為這組背離在股價仍在高檔時就已出現。
- 討論量：DATA_UNAVAILABLE（無法取得帖文計數，只能定性判斷為中等，且搜尋結果的時間分布集中於 11 月初）。
- 代表性觀點（短引用）：
  - 偏空：「股價轉弱、短線賣壓抬頭」（CMoney 社群摘要改寫，非原文）
  - 偏多：「AI 題材持續、投信加碼」（CMoney 社群摘要改寫，非原文）

### 主要主題
1. 股價與跌停事件：11 月 6 日封測族群重挫，京元電早盤一度跌停、來到 212.5 元，之後收於 206 元（跌幅 9.85%）。
2. 毛利率壓力：2026 年第 3 季毛利率降至 37.6%，電費與擴產折舊是主要因素。
3. AI 測試需求：市場傳聞 Rubin 放量延至 2027 年上半年，原因為 HBM4 供應瓶頸或主機板翹曲，輝達未證實。傳聞本身對情緒有影響。
4. 籌碼面：借券賣出在 10 月下旬增加，11 月後小幅回補，但融券餘額同日跳升；投信有 +892 張的增持報導，日期不明。
5. 大戶與散戶持股背離：大戶持股比例下降、股東人數增加。

## Insider activity
Net 6mo: DATA_UNAVAILABLE（yf insider 回傳空陣列，且 Yahoo 連線失敗，無法確認是否真的沒有交易）。
Notable: DATA_UNAVAILABLE。

## Ownership shifts
- yf major_holders（cache）：內部人持股 8.83%，機構持股 35.68%，機構流通股占比 39.13%，機構家數 219。
- 機構持股的時間序列：DATA_UNAVAILABLE（inst_holders 空陣列）。
- 大戶與散戶比例（玩股網文章）：大戶約 55%、散戶約 30%，股東人數增加。文章未說明大戶的定義（集保分級門檻），此數字僅供參考。

## Net sentiment score
Composite: **偏多（分析師）／偏空至中性（散戶）**，整體為分歧狀態。信心度：中低。
- 分析師面：16 位全部買進，屬強烈偏多，但 cache 日期不明，且 11 月 6 日後的目標價調整只有富邦一家公開下修。
- 散戶面：社群摘要多數偏空或觀望，樣本量少，來源多為彙整摘要，無法確認帖文時間與數量。
- 籌碼面：借券與融券數字同時出現增減，無明確方向。
- 基本面數據校驗：2026 年第 3 季營收 121.42 億元，毛利率 37.6%，推算毛利約 45.7 億元（121.42 × 37.6%），與文中數據一致，單位為 TWD 億。目標價以 TWD 元計。

Divergence flag: **yes**。分析師全數買進，散戶與股價走勢偏弱，兩者方向相反。由於散戶樣本少，此訊號的參考價值有限，需要 PTT 或 Dcard 原文與完整 yf 資料補強後再確認。

## 來源
- https://www.wantgoo.com/blog/407988/post/805
- https://www.cmoney.tw/follow/channel/stock-2449
- https://goodinfo.tw/tw/StockDetail.asp?STOCK_ID=2449
- https://wantrich.chinatimes.com/news/20261106900180-420101
- https://hao.cnyes.com/hot/newest/2449京元電子
- https://udn.com/news/story/7253/9573912
- https://www.ctee.com.tw/news/20260529701098-430201
- https://poorstock.com/board/2449
- https://www.mobile01.com/tag.php?tag=2449
- https://money.udn.com/industry/company/2449
- https://stock.wearn.com/a2449.html
- https://tw.stock.yahoo.com/quote/2449/institutional-trading

SENTIMENT REPORT COMPLETE
