# Sentiment — TSM as of 2026-10-26

資料基準：yf info 快取時點 2026-10-25（現價 $418.51 為快取之 regularMarketPrice）。2026-10-26 之後的資料視為未知。單位：金額皆為 USD，以 M（百萬）或 B（十億）標示；ADR 股數以 M 標示。

## Analyst consensus

| 項目 | 數值 | 來源 |
|---|---|---|
| 評等分布（0m） | 6 Strong Buy / 14 Buy / 1 Hold / 0 Sell / 0 Strong Sell（共 20 筆） | yf rec_summary |
| 近 3 個月趨勢 | Buy 由 12 增至 14（-2m 至 -1m 區間），Strong Buy 維持 6，Hold 維持 1，Sell 始終為 0 | yf rec_summary / recommendations |
| Yahoo 綜合評等 | recommendationMean 1.38（strong_buy，1 為最強買入） | yf info |
| 目標價（Yahoo） | 平均 $584.39 / 中位數 $557.5 / 最高 $1,000 / 最低 $440 | yf info |
| 目標價相對現價（$418.51） | 平均隱含上行約 +39.6%；中位數約 +33.2%；最低目標價約 +5.1% | 計算 |
| 個別券商升降評 | DATA_UNAVAILABLE（yf recommendations 僅回傳彙總計數，無個別券商日期與動作） | yf |

近期動作（搜尋補充，皆非 2026-10 當月資料）：
- D.A. Davidson 於 2026-07 將目標價上調至 $500（搜尋來源，未經 yf 交叉確認）。
- 24/7 Wall St. 於 2026-09 下旬給出 BUY，目標價約 $524（獨立估值，非券商評等）。
- TD Cowen 於 2026-07 維持 Hold（搜尋來源）。
- 2026-10 當月之評等升降：DATA_UNAVAILABLE。

來源衝突提醒：
- 分析師家數不一致：yf 為 20 筆；搜尋所見 TickerLeague 為 25 筆；Benzinga 為 8 至 9 筆。本報告以 yf 20 筆為準。
- 目標價區間不一致：yf 為 $440 至 $1,000；Benzinga 為 $210 至 $650（最低值 Barclays）；TickerLeague 為 $480 至 $700。$1,000 高點與 $210 低點疑似離群值，不宜單獨引用。

## Retail social

- Reddit（r/wallstreetbets、r/stocks）：DATA_UNAVAILABLE。依指示不直接抓取 Reddit；WebSearch 亦未回傳 2026-10 之 Reddit 討論串。無法給出討論串樣本或板塊語氣。
- StockTwits：DATA_UNAVAILABLE（依指示以 WebSearch 取代，未取得直接貼文）。
- X / 新聞與意見型網站（WebSearch 結果，多為 2026-02 至 2026-09）：
  - Benzinga 情緒頁（2026-08 至 09 資料）描述整體為正向。
  - Naga 轉載之 TipRanks 情緒分數為正向。
  - 選擇權情緒頁（2026 年初資料，來源品質偏低）描述多空交替、偏中性，常提到 AI 晶片需求與價格支撐/壓力位。
  - 2026-07 一篇報導指出，即使單季財報強勁，股價仍受 AI 支出疑慮、地緣政治與擴廠成本拖累。
- 聲量（mention count）：DATA_UNAVAILABLE（無量化來源，僅能定性判斷為大型權值股，討論量屬常態）。
- 可引用之直接貼文原文：無（本次未取得可核對之原始貼文，故不引述）。

主要論述主題（搜尋彙整，非原始貼文）：
1. AI 與 HPC 需求：正面主軸，多數看多論述圍繞此點。
2. 資本支出：報導提及 2026 年資本支出可能上看 $640 億（需以公司正式公告為準）。
3. 估值：yf 顯示 trailing P/E 約 27.1，forward P/E 約 17.9，PEG 約 0.76，部分人認為估值合理。
4. 風險敘事：海外廠毛利壓力、美國政治要求產能回流、地緣政治、AI 支出是否延續。
5. 股價位置：現價 $418.51 位於 52 週區間（$266.82 至 $487.47）中段偏高；50 日均線 $434.12 高於現價，200 日均線 $397.63 低於現價。

## Insider activity

6 個月窗口：2026-04-26 至 2026-10-26。

| 日期 | 內部人 | 職位 | 方向 | 股數 | 金額 (USD) |
|---|---|---|---|---|---|
| 2026-04-28 | TIEN BOR-ZEN | Officer | 買入 | 20 | 約 7,760 |
| 2026-05-20 | TIEN BOR-ZEN | Officer | 買入 | 17 | 約 6,718 |
| 2026-07-20 | TIEN BOR-ZEN | Officer | 買入 | 10 | 約 4,050 |
| 2026-07-28 | TIEN BOR-ZEN | Officer | 買入 | 15 | 約 5,850 |

Net 6mo：約 $0.02M 買入（合計 $24,378）；賣出 0 筆（yf 回傳清單中無賣出紀錄）。

窗口外參考：2026-03-31 獨立董事 URSULA M. BURNS 買入 1,000 股，約 $322,050（約 $0.32M），不列入 6mo 淨額，但為本批資料中金額最大之一筆。

觀察：
- 買入股數極小（10 至 20 股），金額以千美元計，較像定期或小額累積，訊號強度低。
- 搜尋來源提及 Shyue-Shyh Lin 副總亦有買入，但 yf 清單未見該筆，判定為 DATA_UNAVAILABLE（未能於 yf 核對）。
- CEO C.C. Wei 與 CFO Jen-Chau Huang 於 yf 資料中無買賣紀錄。

## Ownership shifts

- 機構持股比例：15.52%（institutionsPercentHeld）；機構數 4,688。
- 內部人持股比例：0.013%。
- 前十大機構（最新為 2026-06-30 之 13F，2026-09-30 季報截至 2026-10-26 尚未揭露，故 Q3 變動：DATA_UNAVAILABLE）：

| 機構 | 持股 (M 股) | 佔比 | 季變動 |
|---|---|---|---|
| FMR, LLC | 58.9 | 1.14% | -2.4% |
| Capital World Investors | 34.4 | 0.66% | +4.5% |
| Sanders Capital | 26.1 | 0.50% | -6.8% |
| JPMorgan Chase | 23.8 | 0.46% | -0.6% |
| BlackRock | 20.1 | 0.39% | +10.4% |
| Fisher Asset Management | 18.9 | 0.36% | +1.3% |
| Van Eck | 17.2 | 0.33% | -10.7% |
| Morgan Stanley | 15.8 | 0.31% | +7.3% |
| Goldman Sachs | 16.1 | 0.31% | +71.5% |
| Bank of America | 15.3 | 0.29% | +8.3% |

- 前十大合計約 246.6 M 股，約佔流通股數（5,186 M）之 4.8%。
- 增減比：前十大中 6 家增持、4 家減持；增持幅度最大為 Goldman Sachs（+71.5%，但基期小）。整體屬分散、無明顯集中加碼趨勢。
- 空單：短期空單 30.49 M 股，佔流通浮動股 0.63%，回補天數 3.14 天；較前月 29.84 M 增加約 2.2%。空單比例極低，無明顯擠空或壓空結構。

## Net sentiment score

- 分析師：偏多（高信心）。20 筆評等 0 賣出，平均評等 1.38，目標價中位數隱含約 33% 上行。
- 內部人：小幅淨買（低信心）。金額極小，且無賣出紀錄。
- 機構：中性偏多（中信心）。前十大增減互現，無明顯撤退。
- 散戶：中性偏多（低信心）。可得來源少且偏舊；正面以 AI 需求為主，負面以估值、AI 支出與地緣風險為主；選擇權情緒偏中性。

綜合：**偏多（bullish），信心中等**。主要依據為分析師一致性與機構持股無撤退，散戶端證據薄弱，故不以其作為主要加權依據。

Divergence flag：**否**（信心低）。依現有證據，散戶語氣未與分析師方向相反；但散戶端資料缺口大（Reddit、StockTwits 皆為 DATA_UNAVAILABLE），無法排除散戶端偏空情緒被遺漏的可能。若後續補到 Reddit 或 StockTwits 資料，應重新檢視此旗標。

## 資料缺口彙整

- Reddit 直接抓取：DATA_UNAVAILABLE（依指示禁止直接抓取，且 WebSearch 無 2026-10 結果）
- StockTwits：DATA_UNAVAILABLE
- 散戶聲量量化：DATA_UNAVAILABLE
- 個別券商 2026-10 升降評：DATA_UNAVAILABLE
- 2026-09-30 季度機構持股變動：DATA_UNAVAILABLE（尚未揭露）
- Shyue-Shyh Lin 買入紀錄於 yf 核對：DATA_UNAVAILABLE

SENTIMENT REPORT COMPLETE
