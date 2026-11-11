# Sentiment — 2376.TW（技嘉）as of 2026-11-12

> 資料時效聲明：今日系統日期為 2026-11-11，報告日期為 2026-11-12。可取得的最新新聞約為 2026-11-05（10 月營收），下一次財報預定 2026-11-13，尚未公布。本報告的分析師與散戶資料皆為截至取得當下的快照，不包含財報後反應。

## Analyst consensus

yfinance rec_summary（目前期）：12 位分析師中 3 位 Strong Buy、6 位 Buy、3 位 Hold、0 位 Sell、0 位 Strong Sell。換算買進評級約 75%（9/12），無賣出評級。

評級分布在 0m、-1m、-2m 三個期間完全相同，過去兩個月沒有可見的升評或降評。

目標價（來自網路搜尋，來源日期不一，需留意）：
- 某頁面平均 12 個月目標價 311.10 TWD，該頁面顯示股價 399 TWD，目標價低於股價。
- 某 FactSet 相關報導指中位數目標價由 350 元降至 315 元，降幅約 10%。報導日期未確認。
- 另一頁面列出 19 位分析師、STRONGBUY 共識，與 yfinance 的 12 位數字不一致，以 yfinance 為準。

Recent moves：沒有明確的近期評級變動。目標價下修的方向與評級維持買進的狀態有落差，值得留意。

## Retail social

- Reddit：r/wallstreetbets 與 r/stocks 的搜尋端點被 proxy 拒絕（403），無法取得樣本。標記為資料缺漏。
- StockTwits：api.stocktwits.com 同樣被 proxy 拒絕（403），無法取得樣本。標記為資料缺漏。
- 中文財經媒體（替代來源）：搜尋未找到 2026 年 11 月的散戶討論或情緒指標。最近可查到的評論多為 2026 年前幾個月的內容，包括理財周刊的「股價位階相對低、可分批布局」看法，屬媒體評論而非散戶樣本。
- X：未取得可用樣本。
- 聲量：無法量化，無法與平常水準比較。

Themes（依媒體與搜尋結果歸納，非散戶原文）：
- AI 伺服器（GB300 放量、伺服器營收占比逾八成、訂單能見度至 2026 年底）
- 本益比偏低（董事長曾表示 PE 掉到 13 倍以下，認為股價受委屈）
- Computex 題材帶動的量價表現（4 月股價一度攻上 291.5 元）
- 2025 年 12 月的營運目標傳聞，公司已在公開資訊觀測站澄清為媒體臆測，此點可視為對市場傳聞的風險提示

Retail tilt：無法判定。現有可查資料偏向正面（AI 伺服器與低估值論點），但這些是媒體與法人觀點，不能代表散戶情緒。

## Insider activity

Net 6mo：無法確認。yfinance insider 工具回傳空陣列，但同一批呼叫中 cookie/crumb 取得失敗，因此空陣列可能是資料缺漏，不能直接解讀為「六個月內無內部人交易」。需要重新抓取確認。

Notable：無可驗證的交易紀錄。

## Ownership shifts

- 內部人持股比例（insidersPercentHeld）：18.9%
- 機構持股比例（institutionsPercentHeld）：37.4%，流通股口徑 46.1%
- 機構家數：179
- 只有單一時點快照，無法判斷機構集中度的變化趨勢。

## Net sentiment score

Composite：**偏多（neutral-to-bullish），信心低**

依據：
- 分析師面：偏多。12 位中 9 位買進以上，無賣出評級，但目標價資料互相矛盾，且來源日期不一。
- 散戶面：無資料。Reddit、StockTwits 皆被擋，中文社群樣本缺乏。
- 內部人面：無法判定，資料可能不完整。
- 基本面背景：10 月合併營收 670.36 億 TWD，年增 136.7%；1–10 月累計營收 4,710.19 億 TWD，年增 70.7%。此為營運動能的正面訊號，但不屬於情緒資料，僅作背景參考。

Confidence：低。主要因為散戶與內部人兩個來源缺失，且分析師目標價資料日期不明。

Divergence flag：**無法判定**。散戶情緒缺乏樣本，無法與分析師傾向比較。若 11-13 財報後能取得 Reddit 或 StockTwits 的資料，應重新評估是否出現背離。

## Data gaps（需補抓）

1. Reddit 與 StockTwits 端點需在 proxy 允許名單內，否則無法取得散戶樣本。
2. yfinance insider 需重試（cookie/crumb 失敗導致資料可能不完整）。
3. 目標價來源需以同一日期的快照統一比對。

SENTIMENT REPORT COMPLETE

## Sources

- [技嘉 10 月營收報導（technews，2026-11-05）](https://finance.technews.tw/2026/11/05/gigabyte-2376-202610-financial-report/)
- [技嘉 AI 伺服器訂單能見度（Yahoo 股市）](https://tw.stock.yahoo.com/news/%E6%8A%80%E5%98%89-%E7%BA%8C%E6%8B%9A%E9%9B%99%E4%BD%8D%E6%95%B8%E6%88%90%E9%95%B7-ai%E4%BC%BA%E6%9C%8D%E5%99%A8%E8%A8%82%E5%96%AE%E7%9C%8B%E5%88%B02026%E5%B9%B4%E5%BA%95-105314544.html)
- [FactSet 最新調查（Yahoo 股市）](https://tw.stock.yahoo.com/news/%E9%89%85%E4%BA%A8%E9%80%9F%E5%A0%B1-factset-%E6%9C%80%E6%96%B0%E8%AA%BF%E6%9F%A5-%E6%8A%80%E5%98%89-2376-041026658.html)
- [焦點股：技嘉 Computex 激勵（自由時報）](https://ec.ltn.com.tw/article/breakingnews/5410593/print)
- [理財周刊：技嘉股價與本益比](https://www.moneyweekly.com.tw/_Article?AID=208433)
- [Investing.com 技嘉共識預估](https://www.investing.com/equities/gigabyte-tech-consensus-estimates)
- [StockAnalysis 2376 預測](https://stockanalysis.com/quote/tpe/2376/forecast/)
