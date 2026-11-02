# Sentiment — HON as of 2026-11-03

資料說明：yf 工具為 2026-11-02 前後快照（最新內部人交易為 2026-10-26）。WebSearch 結果多停留在 2026-08 以前，零售情緒資料明顯偏舊，本報告信心需打折。Reddit / StockTwits 未直接取得貼文內容（依指示未 WebFetch 社群站）。

## Analyst consensus

分析師評級分布（yf rec_summary，24 位分析師）：

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 合計 |
|------|-----------|-----|------|------|-------------|------|
| 當月 (0m) | 3 | 11 | 9 | 0 | 1 | 24 |
| 上月 (-1m) | 3 | 11 | 9 | 0 | 1 | 24 |
| 兩月前 (-2m) | 3 | 12 | 8 | 0 | 1 | 24 |

目前約 14 買 / 9 持有 / 1 賣（Buy 側占 58%，Hold 占 38%，Sell 側僅 1 位 Strong Sell）。

近期變化：從兩月前到上月，有 1 位分析師由 Buy 降為 Hold；上月到當月無變動。yf `recommendations` 工具回傳的是同一份期間彙總，沒有個別評級變動明細，因此無法列出具體 upgrade / downgrade 券商名稱。

目標價（WebSearch 第三方彙整，日期偏舊，僅供參考）：
- MarketBeat（2026-07）：均價目標約 $259.67，13 Buy / 10 Hold / 2 Sell。
- Benzinga（2026-08）：均價目標 $260。
- TipRanks：均價目標 $250.64，Moderate Buy（11 位）。
- Bank of America：升評至 Neutral，目標價 $265（日期未明）。
- 內部人成交價 $220.99 – $221.18（2026-10-26），低於上述均價目標約 15%。
- 一則 Barchart 數字（均價目標 $457）明顯異常，已排除。

## Retail social

- Reddit：未找到 r/wallstreetbets 或 r/stocks 的 HON 直接貼文。第三方 AltIndex 估計每日提及約 2 次，較其近期均值下降約 53%，Reddit 情緒分數 76/100（偏多），但頁面未標示更新時間。
- StockTwits / X：StockTwits 符號頁無可用情緒讀數。AltIndex 綜合情緒 98/100（偏多）；SentiSense 30 日分數為中性，且自 2026-08-09 起轉弱。一個期權流向頁面標示「bearish」，日期為 2026-09-01，來源不明，權重低。
- 聲量：低於一般水準（qualitative，約每日個位數提及）。
- 語氣：混合偏中性。多數第三方工具偏多，但樣本薄且時效舊。
- 主要議題（從新聞與第三方摘要歸納，非貼文原文）：
  1. 拆分 / 分割執行（spin-off）與激進股東（Elliott）要求拆分的後續。
  2. 航太部門（Aerospace）逆風，Barclays 認為該部門「還需努力爭取投資人信任」。
  3. Q2 指引低於市場預期，並提及中東衝突的影響。
  4. 估值相對 5 年歷史均值持平，部分人認為被低估（Jim Cramer 2026-04 評論）。
  5. 股息 $1.19 / 季，作為防禦性持有理由。
- 原始貼文引述：本次未取得可直接引用的散戶貼文，故不引述。

## Insider activity

6 個月窗口（2026-05-03 至 2026-11-03），依 yf insider 資料，以 USD 計：

| 類別 | 筆數 | 金額（USD M） | 備註 |
|------|------|--------------|------|
| 公開市場買入 | 0 | 0.00 | 窗口內無買入紀錄 |
| 公開市場賣出 | 4 | 6.31 | 以 Sale at price 記載 |
| 衍生性證券行權（Conversion） | 3 | 4.76 | 以行權價計價，非市價，不算買入 |

Net 6mo（公開市場）：買入 $0.00M，賣出 $6.31M，淨賣出 $6.31M。

主要交易：
- Vimal M. Kapur（CEO）：2026-10-26 行權 8,684 股（行權價 $114.44），同日以 $220.99 賣出 6,459 股，金額約 $1.43M。行權後賣出為典型 exercise-and-sell，未必代表看空。
- Su Ping Lu（General Counsel）：2026-10-26 行權 4,033 股，同日以 $221.18 賣出 2,943 股，金額約 $0.65M。
- Kenneth J. West（Officer）：2026-07-27 行權 17,032 股後，以 $243.77 全數賣出，金額約 $4.15M，為窗口內最大單筆。另有 2026-08-03 賣出 316 股，約 $0.08M。
- Michal Stepniak（CFO）：2026-07-16、07-30、07-31 有多筆股份異動，Value 欄位為空，多為授予 / 代扣性質（推測，工具未提供交易代碼）。
- 董事（Director）：2026-04-15 各有約 625 股異動，Value 欄位為空，推測為年度董事股權授予。

觀察：窗口內無 CEO / CFO 以外的公開市場買入，高階主管以賣出為主；但多數賣出伴隨行權，屬常見的選擇權變現模式，對看空訊號的強度應打折。

## Ownership shifts

- 機構持股比例 84.6%，持有機構 2,821 家。
- 內部人持股比例 0.08%，持股集中度低。
- yf 工具僅提供當期快照，無歷史序列，無法判斷機構集中度的趨勢方向。

## Net sentiment score

綜合判斷：中性（信心：中低）

- 分析師面：偏多。Buy 側占 58%，無 Sell 評級（僅 1 位 Strong Sell），近月有 1 位降為 Hold。
- 內部人面：偏空。窗口內 $6.31M 公開市場賣出、$0 買入，但多數伴隨行權，訊號強度有限。
- 零售面：中性偏多，樣本薄、時效舊，信心低。

Divergence flag：有限度的分歧。分析師偏多與內部人淨賣出方向不一致；零售面資料不足，無法確認是否與分析師方向相反，故此旗標不成立，僅標註為「待更新資料確認」。

資料缺口：
1. 個別評級變動與券商名稱（yf recommendations 僅回傳彙總）。
2. 即時目標價（yf 無此欄位，僅有第三方過時數據）。
3. Reddit / StockTwits 直接貼文與情緒讀數。
4. 2026-10 Q3 相關新聞與股價反應（搜尋結果僅到 2026-07 Q2 財報）。
5. 機構持股歷史趨勢。

## 來源

- yf 工具：`pipeline/tools/yf HON recommendations | rec_summary | insider | major_holders`
- [MarketBeat — HON BMO 股價預測](https://www.marketbeat.com/instant-alerts/honeywell-international-nasdaqhon-stock-price-expected-to-rise-bmo-capital-markets-analyst-says-2026-07-27/)
- [TipRanks — HON 預測](https://www.tipranks.com/stocks/hon/forecast)
- [AltIndex — HON Reddit 提及量](https://altindex.com/ticker/hon/reddit-mentions)
- [AltIndex — HON 情緒](https://altindex.com/ticker/hon/sentiment)
- [Benzinga — HON 情緒](https://www.benzinga.com/quote/HON/sentiment)
- [Barchart — HON Q2 2026 財報前瞻](https://www.barchart.com/story/news/3098477/honeywell-international-s-q2-2026-earnings-what-to-expect)
- [MarketBeat — HON Q3 2026 指引（2026-07-23）](https://www.marketbeat.com/instant-alerts/honeywell-international-nasdaqhon-updates-q3-2026-earnings-guidance-2026-07-23/)

SENTIMENT REPORT COMPLETE
