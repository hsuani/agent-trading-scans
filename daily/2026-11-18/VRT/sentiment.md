# Sentiment — VRT as of 2026-11-18

> 資料時點注意：執行日為 2026-11-17，報告指定日為 2026-11-18。分析師與持股資料取自 yf 工具（ratings / info / insider / holders），抓取時點為執行當下；零售輿情來自 WebSearch 彙整，最新可辨識的讀數為 2026-11-08 前後。未引用任何舊日期 daily 報告的內容。

## Analyst consensus

**分析師分布（yf rec_summary，0m）：31 家中 Strong Buy 3 / Buy 23 / Hold 5 / Sell 0 / Strong Sell 0**，買進佔 84%（26/31）。

| 期間 | Strong Buy | Buy | Hold | Sell | 合計 |
|---|---|---|---|---|---|
| 0m（目前） | 3 | 23 | 5 | 0 | 31 |
| -1m | 3 | 23 | 4 | 0 | 30 |
| -3m | 3 | 21 | 4 | 0 | 28 |

- 趨勢：買進家數近三個月由 24（Buy + Strong Buy）增至 26；Hold 由 4 增至 5（最近一個月）。整體仍偏多，但最新一個月出現一家轉為中立。
- 目標價（yf info，30 位分析師）：平均 $334.29 / 中位數 $333.5 / 最高 $427 / 最低 $240；現價 $186.43，對平均目標價隱含約 +79%。
- 近期評等變動（WebSearch，需與原始來源再核對）：
  - GLJ Research 於 2026-10 首次給予 Sell，目標價 $188，11 月初調降至 $187。此為唯一明確看空評等，但**未反映在 yf 的 Sell 計數中（yf 顯示 0）**。
  - JPMorgan 於 11-11 設定謹慎目標價 $240。
  - Oppenheimer 維持 Buy，目標價上調至 $195；Evercore 維持 Buy，目標價上調至 $210（兩者日期未在來源中明確標示）。
  - Wall Street Zen 於 2026-10-31 上調評等（MarketBeat 快訊標題）。
- 數據不一致：yf 目標價平均 $334 明顯高於近期個別券商目標價（$187–$240），疑似目標價統計未更新，請以券商原始報告為準。

## Retail social

- **Reddit（r/wallstreetbets、r/stocks）**：依指示未直接抓取 Reddit JSON（已被封鎖），改以 WebSearch 查詢。本次搜尋未找到可辨識的 r/wallstreetbets 或 r/stocks 個別討論串，**提及量 DATA_UNAVAILABLE**。
- **StockTwits / X**：StockTwits 即時讀數 DATA_UNAVAILABLE（搜尋未取得 2026-11 的實時數字）。可用的間接指標：
  - AltIndex 綜合情緒分數 74/100，標示為偏多；但相較 30 日均值已走弱（來源為 NLP 彙整 Reddit、StockTwits 與論壇）。
  - SentiSense 截至 2026-11-08：30 日情緒為偏多但較前一個月降溫。
  - QuiverQuant AI 摘要：討論焦點為 AI 資料中心散熱業務與財報超預期、上調指引；部分聲音提及近期股價回檔與利率擔憂。
- **Retail buzz 音量**：無可靠量化數字，定性判斷為中等，有 AI 題材與財報話題支撐，但未見異常暴增。
- **Retail 傾向**：混合偏多（aggregator 層級），較分析師共識偏弱。
- **主要主題（依搜尋摘要歸納）**：
  1. AI 資料中心散熱與電源需求（多頭主軸）。
  2. Q3 營收大幅成長與全年指引上修（多頭）。
  3. 股價自 2026-05 高點（$376.23 收盤）回落約 44%（半年），估值倍數壓縮之疑慮（空頭）。
  4. 利率與期中選舉相關的總體風險（空頭）。
- 代表性標題（非貼文原文，僅來源標題）：「Retailers Maintain Bullish Outlook」（StockTwits 新聞標題，年份不明）；「Retail's Divided」（StockTwits 新聞標題，年份不明）。

## Insider activity

視窗：2026-05-18 至 2026-11-18（yf insider 最新一筆為 2026-10-05，之後無新申報於此資料源）。

**Net 6mo：$0 買入 / 約 $3.88M 賣出**（以 USD 計）

| 日期 | 人員 | 職務 | 交易 | 股數 | 金額（USD） |
|---|---|---|---|---|---|
| 2026-09-01 | MONSER EDWARD L | Director | 公開市場賣出（$249.43–$256.36） | 15,287 | 3.88M |
| 2026-09-01 | MONSER EDWARD L | Director | 行使衍生性證券（履約價 $11.50） | 15,287 | 0.18M（轉換，非買入） |
| 2026-09-08 | ALBERTAZZI GIORDANO | CEO | 贈與（Gift） | 118,523 | 0（非市價交易） |

- 其餘為 2026-06-25 與 2026-03-26 之例行股票獎勵（Stock Award），多數金額為 0 或極小股數，不計入淨買賣。
- 解讀：6 個月內無內部人公開市場買進；唯一顯著公開市場賣出為董事 Monser 的一次 $3.88M 出售，且同日伴隨選擇權行使，可能屬於行使後變現。CEO 贈與不屬於市場賣出。
- 與 WebSearch 來源的差異：QuiverQuant 摘要稱 6 個月內有 7 筆公開市場賣出，但 yf 資料源只見 1 筆，兩者未能調和，以 yf 原始申報為準。

## Ownership shifts

- 機構持股：83.3%（2,642 家機構）；內部人持股：0.25%。
- 前幾大持股（yf major_holders / inst_holders）：

| 機構 | 持股比例 | 股數（M） | 市值（USD B） | 季度變動 | 報告日 |
|---|---|---|---|---|---|
| BlackRock | 8.1% | 31.2 | 5.82 | -13.1% | 2026-09-30 |
| Vanguard Capital Mgmt | 6.5% | 25.2 | 4.70 | +0.4% | 2026-09-30 |
| Vanguard Portfolio Mgmt | 4.7% | 18.3 | 3.40 | +2.0% | 2026-09-30 |
| State Street | 4.3% | 16.6 | 3.09 | +0.4% | 2026-09-30 |
| JPMorgan | 2.85% | 11.0 | 2.04 | +9.0% | 2026-09-30 |
| T. Rowe Price | 2.37% | 9.1 | 1.70 | +15.9% | 2026-06-30 |
| Geode | 2.37% | 9.1 | 1.70 | +1.1% | 2026-09-30 |
| Bank of America | 2.15% | 8.3 | 1.54 | -1.6% | 2026-06-30 |
| Morgan Stanley | 2.13% | 8.2 | 1.53 | +18.9% | 2026-09-30 |

- 趨勢：主動型基金與大型券商（T. Rowe、JPMorgan、Morgan Stanley）近一季增持；BlackRock 減持 13%。整體屬機構持股高度集中、主動資金小幅加碼。
- 資料品質：市值欄位為 yf 以目前價格換算（BlackRock 31.2M 股 × $186.4 = $5.82B），非申報當日價格換算，僅供相對比較。

## Net sentiment score

**綜合判讀：偏多（bullish lean），信心中低**

- 分析師：偏多，買進佔 84%，但目標價統計可能過時，且有一家 Sell 未被 yf 計入。
- 零售：混合偏多（aggregator 分數 74/100，但動能降溫），無即時 StockTwits 或 Reddit 讀數。
- 內部人：偏空訊號但量小，6 個月無公開市場買進，約 $3.88M 單筆賣出。
- 機構：中性偏多，主動資金小幅增持。

**背離旗標：否**。零售傾向與分析師傾向同為偏多方向；唯一明顯反向訊號來自 GLJ Research 的 Sell 評等與內部人賣出，兩者為少數聲音。

**資料缺口摘要**：
- Reddit 提及量：DATA_UNAVAILABLE
- StockTwits 即時情緒讀數：DATA_UNAVAILABLE
- yf 目標價統計與 Sell 計數與 WebSearch 來源不一致，已標註

SENTIMENT REPORT COMPLETE
