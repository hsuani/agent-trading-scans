# Sentiment — VRT as of 2026-10-21

注意事項：
- 任務指定的 `yf.py VRT ratings` 與 `yf.py VRT holders` 不存在，改用 `rec_summary`、`recommendations`、`major_holders`、`inst_holders`。
- Reddit、StockTwits 直連不可用，零售情緒只能依 WebSearch 摘要與第三方彙整站。

## Analyst consensus

yf `rec_summary`（0m）：3 Strong Buy / 23 Buy / 4 Hold / 0 Sell / 0 Strong Sell，共 30 家。近 3 個月趨勢：Buy 由 21 升至 23，Hold 持平在 4，Sell 持續為 0。

評等變動：
- 2026-08-07：GLJ Research 由 Hold 升為 Buy，目標價 $381。
- 2026-07-30：RBC Capital 目標價由 $418 降至 $337，維持 Outperform。
- 2026-09-05：Wall Street Zen 由 Buy 降為 Hold（此為評級網站，不屬於傳統券商）。
- 2026-05 至 2026-08 期間，TD Cowen $387（5/20）、Mizuho $380（5/21）。
- 2026-10 月：未找到評等變動紀錄。這是搜尋缺口，不代表沒有變動。
- 較早的 JPMorgan 與 Barclays 降目標價紀錄，日期不明，未採計。

共識目標價：Investing.com 約 $338（26 家，24 Buy / 4 Hold，高 $427、低 $236）；MarketBeat 約 $358。各來源樣本與日期不同，以 yf 的評等分布為主。

## Insider activity（近 6 個月，2026-04-21 至 2026-10-21）

- 淨公開市場買進：$0。
- 公開市場賣出：約 $3.88M，僅 1 筆。Director Edward L. Monser 於 2026-09-01 賣出 15,287 股，價格 $249.43–$256.36。該筆與 $11.50 選擇權行權（約 $176K）同日發生，屬行權後賣出。
- 其他事件（非公開市場買賣）：
  - CEO Giordano Albertazzi 於 2026-09-08 贈與 118,523 股（Stock Gift，無金額）。
  - Officer Michael Resha 於 2026-10-05 獲配 3,193 股，價格 $253.62，約 $810K（Grant）。
  - 2026-06-25 有多名高管與董事例行授予股票（含 CEO、CFO Craig Chamberlin）。
- 歷史對照（窗口外）：2025-05 Officer Karsten Winther 賣出約 59,700 股，約 $5.7M，價格 $94–$96。
- 解讀：近 6 個月沒有內部人公開市場買進，賣出僅一筆且與行權相關；CEO 的贈與與高管授予不屬於買賣訊號。內部人持股僅 0.24%，訊號權重有限。

## Institutional ownership（截至 2026-06-30 之 13F，約 3.5 個月前）

- 機構持股比例 84.6%，機構數 2,696 家。
- 前幾大持股變動（QoQ）：
  - BlackRock 9.33%，減持 3.5%。
  - Vanguard Capital 6.52%，加碼 0.9%。
  - Vanguard Portfolio Mgmt 4.65%，持平。
  - State Street 4.29%，加碼 4.4%。
  - JPMorgan 2.61%，大增 65.9%（基數低）。
  - T. Rowe Price 2.37%，加碼 15.9%。
  - Geode 2.35%，減持 17.0%。
  - Invesco 1.44%，減持 15.4%。
- 趨勢：混合偏中性。指數型與大型被動機構多數持平或小幅變動，主動型中 T. Rowe 與 JPMorgan 加碼、Invesco 與 Geode 減持。沒有明顯集中或撤出訊號。

## Retail / social sentiment

- Reddit（r/wallstreetbets、r/stocks）：搜尋未找到相關討論串，無法取樣發文，也無法估計提及量。
- StockTwits：頁面快照的 "How do you feel about VRT?" 投票顯示 "Bearish Sentiment" 標籤與數字 32，但數字定義與擷取日期不明（推測為 7 月底前），可信度低。
- AltIndex：74/100，標示 bullish，但相較 30 日均值已轉弱。
- SentiSense：略偏多，30 日分數約 10，新聞提及以 bullish 為主。
- 提及量：無法量化。以新聞與彙整站數量判斷屬中等，無法與歷史基準比較。
- 主要主題：
  1. AI 資料中心需求與產品積壓（Barchart 引述約 $15B backlog）。
  2. 估值與動能過高（一年漲幅約 67.6%，遠高於 S&P 500）。
  3. 競爭疑慮（新聞標題提及 Microsoft 新冷卻系統、Vertiv 面臨冷卻競爭）。
  4. 短期技術面轉弱，長期指標仍偏多（Benzinga 摘要）。
  5. AI 泡沫風險的一般性警示。
- 股價脈絡：2026-07-29 Q2 財報後股價下挫；8 月末約 $257–$272；9-14 單日跌 7.6% 至約 $237.6（MarketBeat）。各來源價格不一致，請以即時報價為準。
- 引述：無可直接引用的發文。新聞標題「Unstoppable Growth Stocks to Invest In According to Reddit」僅顯示 Reddit 曾被引用，未描述討論內容。

## Earnings 日程（與 as-of 日期相關）

- Yahoo Finance 報價頁列出下次財報為 2026-10-21，但另一搜尋未能證實該日期。
- Q3 指引：EPS $1.77–$1.83（共識約 $1.79–$1.82），營收 $3.7B–$3.9B。
- Q2：EPS $1.52 優於預期 $1.43，但營收 $3.27B 低於預期 $3.38B。
- 請以公司公告為準。財報在 as-of 當日或隔日，零售與分析師情緒都可能因財報大幅改變。

## Net sentiment score

- 分析師面：偏多（Buy 26/30，Sell 0）。
- 零售面：偏多但弱（AltIndex 74、SentiSense 略偏多）；StockTwits 數據不可用於定論。
- 內部人面：中性偏弱（無公開市場買進，一筆與行權相關的賣出，約 $3.9M）。
- 機構面：中性。
- 綜合：偏多（bullish），信心度中低。扣分原因：Reddit 無資料、StockTwits 不可用、機構資料為 6 月底、分析師評等無 10 月更新、財報前後波動大。

Divergence flag：否。分析師與零售整體同向偏多。唯一不一致點是內部人無公開市場買進，但這與分析師偏多並不構成明顯背離。

SENTIMENT REPORT COMPLETE
