# Sentiment — POET as of 2026-10-18

資料時效聲明：Yahoo cookie/crumb 取得失敗，yf 工具回傳之數據可能來自快取，未逐欄驗證。Reddit 與 StockTwits 直連不可用，僅能以 WebSearch 取得間接資料，且多為 2026 年 4 月至 6 月的舊文，**無法取得 2026-10 的即時社群數據**。最近股價為 2026-10-12 收盤，各來源不一致：Yahoo 報 $6.41（跌 8.03%），24/7 Wall St 報 $6.56。

## Analyst consensus

- 評級分布：DATA_UNAVAILABLE。`rec_summary` 與 `recommendations` 皆回傳全 0 筆。（備註：任務指定的 `ratings` 子命令不存在，已改用上述兩個有效子命令。）
- 覆蓋度極薄。2026-10 可查到的目標價僅一筆：$14.75（24/7 Wall St 2026-10-15 引用，Bullstory 2026-10-06 亦同），以 2026-10-12 股價計約 +125%，且文中註明只來自單一分析師。
- 評級分歧：
  - Northland（2025-12）Sell，目標 $8.00（MarketBeat 1 月頁面）。
  - TipRanks 顯示單一 Hold，目標 $8.00（日期不明）。
  - 24/7 Wall St 另一篇文章 Sell，目標 $10.38（日期不明）。
  - StockAlarm 顯示 Buy，目標 $5.75，僅兩位分析師且日期不明。
- 近期調整：2026-10 無可驗證的評等升降級紀錄，DATA_UNAVAILABLE。
- 解讀：分析師面為**極少樣本、評等互相矛盾**，不宜視為共識。

## Retail social

- **Reddit（r/wallstreetbets、r/stocks）**：本輪 WebSearch 未取得 2026-10 的任何討論串，DATA_UNAVAILABLE。可得的間接資料如下：
  - 247WallStreet（2026-05-28）引用 Reddit 情緒數據：4 月 28 至 29 日為極度看空（very_bearish 分數 8 至 12），5 月 15 日情緒分數達 94，與一則「大幅獲利」的爆紅貼文有關。
  - 德文媒體報導 WSB 推動的短線炒作，文中指出股價波動並非由公司新聞驅動（日期不明）。
  - 可代表性的引言（已改寫為摘要，未逐字轉載）：散戶認為股票「沒有消息也會一直漲」（StockTwits 文章引述）。
- **StockTwits**：直連 API 未嘗試（任務指示 WebFetch 在此環境被阻擋），僅得間接來源。一篇 StockTwits 文章（發布日期不明，內容對應 2026-05-15 前後）稱散戶情緒 24 小時內由看空轉為看多，訊息量增加逾 58%。
- **X**：Photon Capital（光子研究機構）於 5 月在 X 上表態懷疑，認為 POET 必須證明其價值。2026-10 無可用貼文，DATA_UNAVAILABLE。
- **討論量（buzz volume）**：定量數據 DATA_UNAVAILABLE。定性判斷為目前無明顯熱度峰值的證據；上一個已知高峰在 5 月中。
- **主要主題**（依出現頻率排序）：
  1. PFIC 稅務身分與集體訴訟：2026-04-29 起訴，涵蓋 4/1 至 4/27 買入者；Wolfpack Research 4/14 做空報告提出此論點。訴訟指控為未經證實之主張。
  2. Lumilens 合約：$500M、五年期供應協議，首批採購單 $50M，屬正面催化劑。
  3. Marvell / Celestial AI：2026-04-27 Marvell 取消全部訂單，單日暴跌約 47%（$7.15），是 4 月看空情緒的主因。
  4. 估值爭議：5 月文章引述市值約 $2.27B 相對於營收基礎，被視為看多論點的主要反駁。
  5. 公司治理：2026-06-26 股東大會就redomicile（遷冊至美國）投票，結果未查得（DATA_UNAVAILABLE）。
  6. 下次財報：預計 2026-11-12 盤前公布。

## Insider activity

查詢區間 2026-04-18 至 2026-10-18（6 個月）。來源為 `yf insider`，共 41 筆區間內紀錄。

- **公開市場買入**：0 筆。
- **公開市場賣出**：約 $5.10M（以 `Disposition in the public market` 紀錄之申報金額加總）。
- **行權後賣出**：多筆 `Exercise of options` 後立即於公開市場賣出，屬於行權即賣，非新增持股。
- **14 筆無文字說明之紀錄**（如 2026-08-07 多位高管的 Shares 紀錄）性質未確定，可能為授予或其他異動，DATA_UNAVAILABLE，未計入金額。

主要人員與重大交易：
- **Barnes (Kevin)**，Senior Officer：2026-05-20 公開市場賣出約 $1.23M（14.69 與 14.22 美元）；2026-06-05 賣出約 $571K；2026-08-10 賣出約 $131K（8.93 美元）。
- **Mika (Thomas R)**，Senior Officer：2026-08-07 賣出約 $409K（8.93 美元）。
- **Jinyu (Mo)**，Senior Officer：2026-06-03 賣出約 $440K（14.65 美元）；2026-06-05 賣出約 $649K（10.82 美元）。
- **James (Lee)**，Director 或高階主管（其他類別）：2026-06 行權後分批賣出，共約 $1.09M（14.17 至 14.68 美元）。
- **Kankipati (Venkata Rama Raju)**，Senior Officer：2026-08-07 賣出約 $208K（8.93 美元）。
- **Riley (Glen)**，Director：2026-08-19 賣出約 $103K（9.45 美元）。
- **Malinge (Jean-Louis)**，Director：區間外（2026-04-18 之前）賣出約 $1.34M，未計入 6 個月統計。

判讀：高階與董事在 6 個月內持續賣出，且 6 月高價區（約 $14 至 $15）與 8 月低價區（約 $9）皆有出貨。無任何公開市場買入紀錄。內部人持股比例僅約 0.07%（`insidersPercentHeld`），對股價影響有限，但方向性訊號明確偏空。

## Ownership shifts

- 機構持股比例 20.4%，共 188 家機構（`major_holders`，資料期間為 2026-06-30 季報）。
- 前十大持股（2026-06-30）：
  - Cloudalpha Capital（香港）：2.51%
  - Renaissance Technologies：2.26%
  - IMC-Chicago：1.76%（季增 27.6%）
  - Goldman Sachs：1.50%（季增 24.9%）
  - Arrowstreet Capital：1.10%（季增 84.1%）
  - Elequin Capital：1.07%
  - National Bank of Canada：0.97%（季增 4.0%）
  - Morgan Stanley：0.89%（持平）
  - Trexquant Investment：0.82%
  - Citadel Advisors：0.69%（季減 0.58%）
- 前十大多為量化與做市商，持股分散，無單一長線大戶。
- 多季趨勢：DATA_UNAVAILABLE，僅有單一季度快照。`pctChange` 欄位的單位與定義未確認，上表以原始數值呈現。

## Net sentiment score

- **分析師面：中性偏多，信心低。** 唯一的 2026-10 目標價 $14.75 指向大幅上漲，但樣本僅一位分析師；其他評等偏空（Sell $8 至 $10.38）。
- **內部人面：偏空，信心中。** 6 個月無公開市場買入，高階與董事分批賣出約 $5.1M，且涵蓋 6 月高點與 8 月低點。
- **散戶面：無法判定（DATA_UNAVAILABLE）。** 最近可得資料為 5 月的看多翻轉，但 4 月為極度看空，且資料已過時約五個月。
- **股價背景：** 自 5 月約 $14 至 $15 回落至 10 月約 $6.4，跌幅約 55%。
- **綜合：偏空（neutral-to-bearish）**，信心低。主要依據為內部人持續賣出與股價結構性下跌，並非來自即時散戶數據。

**Divergence flag：無法判定**。分析師的唯一 2026-10 目標價偏多，內部人偏空，散戶現況無資料，因此無法確認散戶與分析師是否方向相反。

## 資料缺口彙總

| 項目 | 狀態 |
|---|---|
| 分析師評等分布（buy/hold/sell 筆數） | DATA_UNAVAILABLE（全 0） |
| 2026-10 評等升降級 | DATA_UNAVAILABLE |
| Reddit 2026-10 討論 | DATA_UNAVAILABLE |
| StockTwits 直連資料與即時情緒 | DATA_UNAVAILABLE |
| X 即時貼文 | DATA_UNAVAILABLE |
| 定量討論量 | DATA_UNAVAILABLE |
| 14 筆無說明內部人紀錄之性質 | DATA_UNAVAILABLE |
| 多季機構持股趨勢 | DATA_UNAVAILABLE |
| 股東大會 redomicile 投票結果 | DATA_UNAVAILABLE |

## 資料來源（WebSearch 間接資料）

- https://247wallst.com/investing/2026/05/28/jim-cramer-wont-touch-poet-the-reddit-crowd-thinks-hes-wrong-somebodys-about-to-lose-a-lot-of-money/
- https://stocktwits.com/news-articles/markets/equity/poet-stock-has-seen-its-biggest-jump-in-a-month-how-much-more-upside-does-wall-street-see/cZZ2uyNR7AI
- https://247wallst.com/investing/2026/10/15/poet-technologies-could-be-sitting-on-a-much-bigger-opportunity-than-investors-realize/
- https://www.tipranks.com/stocks/POET/forecast
- https://finance.yahoo.com/markets/stocks/articles/prediction-poet-stock-outlook-just-164656289.html
- https://www.rgrdlaw.com/cases-poet-technologies-inc-class-action-lawsuit-poet.html

SENTIMENT REPORT COMPLETE
