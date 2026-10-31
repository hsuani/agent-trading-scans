# Sentiment — POET as of 2026-11-01

## 資料可用性

- Reddit (r/wallstreetbets、r/stocks): 抓取失敗, Claude Code 無法連線 www.reddit.com。本次無貼文樣本。
- StockTwits: api.stocktwits.com 解析失敗 (不在本 session 允許網域內)。需在 session 網路設定允許該網域後再補抓。
- yfinance 分析師端點 (`recommendations`、`rec_summary`): cookie/crumb 取得失敗, 回傳全為 0。無法區分「無覆蓋」與「資料失敗」, 本報告不將其解讀為零位分析師。
- yfinance `insider`、`major_holders`: 雖有 cookie 警告, 仍回傳資料。
- X / 新聞: 以 WebSearch 取得替代來源 (媒體與部落格), 品質參差, 權重較低。

## Analyst consensus

yfinance 計數: 0 buy / 0 hold / 0 sell (疑為資料缺漏, 不採信)。

網路來源 (MarketBeat 2026-08 初): 0 buy / 0 hold / 1 sell (Sell 評級, 平均目標價 USD 8.00)。

| 來源 | 日期 | 評級 | 目標價 (USD) | 備註 |
|---|---|---|---|---|
| MarketBeat | 2026-08 初 | Sell (1 家) | 8.00 | 當時股價約 USD 6.97, 50 日均線約 USD 10.27 |
| Weiss Ratings | 2026-07 | sell (d-) | — | 重申評級 |
| 24/7 Wall St. | 2026-08-12 | Buy | 21.14 | 媒體模型輸出, 非 sell-side 共識, 未核實 |
| 24/7 Wall St. (引用) | 日期不明 | Sell | 10.38 | 引述證券訴訟與 PFIC 稅務議題 |
| Seeking Alpha | 日期不明 | 下調至 Hold | 長期價值 USD 42 | 以估值為由 |
| Craig-Hallum | 2024-09 | — | 3.50 | 已過時 |

Recent moves: 未找到 2026-10 的評級上下調紀錄。聚合網站的共識目標價 (Benzinga USD 6.25、TickFlow USD 5.75) 疑為過時資料。

整體: 可查的 sell-side 樣本極少且分歧, 偏向 Sell。Buy 目標來自媒體模型, 不納入計數。

## Retail social

- Reddit: 無資料 (連線失敗)。
- StockTwits: 無資料 (DNS 失敗)。
- X: 未取得直接貼文。
- 聲量 (buzz volume): 無法量化, 無與歷史基準比較的依據。
- 散戶傾向: 無法直接判定。替代來源敘事偏負。

主要主題 (來自替代來源):
1. 稅務與法律風險: 一份 2026-04 的 short report (Wolfpack Research, 由 WebSearch 摘要引述) 稱公司為推廣型股票並有稅務問題, 另有 PFIC 稅務身分與證券訴訟的討論。
2. 商業化證明: Seeking Alpha 2026-05 文章標題指股價進入 "brutal proof phase", 焦點在 Lumilens 能否兌現。
3. 估值與基本面落差: 24/7 Wall St. 文章指 2026 年初至今約 133% 的漲幅超過基本面表現。
4. 技術面: Tradestie 自動化頁面 (2026-10-16) 顯示短期動能偏弱, 近期下跌 9.7%, 底部型態分數 25/100。此為量化分數, 權重低。

代表性標題 (媒體, 非散戶原文): "Prediction: POET Stock's Outlook Just Turned Bleak" (Yahoo Finance)。

## Insider activity

觀察期: 2026-05-01 至 2026-10-31。資料最後一筆為 2026-08-19, 之後 2.5 個月無紀錄, 需確認是 feed 落後或確實無交易。

Net 6mo: 公開市場買入 USD 0; 公開市場賣出約 USD 5.1M (18 筆)。扣除選擇權行使成本 (約 USD 0.4M) 後仍為淨賣出。

| 內部人 | 資料標示職位 | 賣出金額 (USD M) | 交易日 | 售價範圍 (USD) |
|---|---|---|---|---|
| Barnes, Kevin | Senior Officer | 1.94 | 05-20、06-05、08-10 | 8.93 – 14.69 |
| Jinyu, Mo | Senior Officer | 1.09 | 06-03、06-05 | 10.82 – 14.65 |
| James, Lee | Director or Senior Officer | 1.07 | 06-01 至 06-12 | 14.17 – 14.68 |
| Mika, Thomas R | Senior Officer | 0.41 | 08-07 | 8.93 |
| Kankipati, Venkata Rama Raju | Senior Officer | 0.29 | 06-16、08-07 | 8.93 – 14.73 |
| Riley, Glen | Director | 0.15 | 06-30、08-19 | 6.71 – 9.45 |
| Khan, Sohail A | Director | 0.06 | 07-08 | 5.84 |
| Ende, Theresa Lan | Director | 0.05 | 06-30 | 6.71 |
| Tirva, Robert Linas | Director | 0.04 | 06-30 | 6.71 |

Notable:
- Barnes (Kevin) 於 05-20 與 06-05 出現行使後隨即賣出的模式 (05-20 行使 85,625 股選擇權, 同日賣出 85,625 股)。Jinyu (Mo) 於 06-03 與 06-05 亦有類似模式。
- 賣出集中於 05-20 至 06-12 (股價約 USD 10.8–14.7) 與 08-07 至 08-19 (約 USD 8.9–9.5)。6 月底至 7 月股價低點約 USD 5.8–6.7 期間, 內部人賣出較少。
- 資料未標示 CEO 或 CFO 職稱, 無法辨識是否為最高層, 本報告僅以資料提供的職位標示呈現。
- 多筆 Value 為空白的股數變動 (例如 Venkatesan, Suresh 的 369,004 股與 170,073 股), 性質不明 (可能為授予、轉讓或其他非市場交易), 未計入金額。

Ownership (major_holders, 單一時點快照):
- 內部人持股: 0.07%。
- 機構持股: 20.14%, 機構數 185 家。
- 無歷史資料, 無法判定機構集中度的增減趨勢。

## Net sentiment score

Composite: **偏空 (bearish lean), 信心低**

- 內部人 (中等權重): 6 個月 0 筆公開買入、9 名內部人合計賣出約 USD 5.1M, 含行使後即賣的模式。偏空。
- 分析師 (低權重): 可查的 sell-side 評級僅 1 家 Sell, 目標 USD 8.00, 日期為 2026-08。yfinance 缺資料。偏空, 樣本過小。
- 散戶 (無法計權): Reddit、StockTwits 皆無資料。替代敘事偏負, 但來源非散戶。

Divergence flag: **無法判定**。散戶資料缺失, 無法與分析師傾向比較。分析師與內部人方向一致 (皆偏空), 不構成背離。唯一的 Buy 目標來自媒體模型, 未核實, 若其成立則需重新評估。

Data gaps (建議補抓):
1. 允許 api.stocktwits.com 網域後重抓 StockTwits。
2. 修復 yfinance cookie/crumb 後重抓 `rec_summary` 與 `recommendations`, 確認是否真的無覆蓋。
3. 確認 insider feed 自 2026-08-19 後是否確實無交易。
4. Reddit 連線恢復後補充 r/wallstreetbets 與 r/stocks 的樣本。

## Sources

- [Yahoo Finance: Prediction: POET Stock's Outlook Just Turned Bleak](https://finance.yahoo.com/markets/stocks/articles/prediction-poet-stock-outlook-just-164656289.html)
- [MarketBeat: POET Technologies to announce earnings (2026-08-03)](https://www.marketbeat.com/instant-alerts/poet-technologies-poet-to-announce-earnings-on-monday-2026-08-03/)
- [24/7 Wall St.: Big Cash, Bigger Ambitions (2026-08-12)](https://247wallst.com/investing/2026/08/12/big-cash-bigger-ambitions-poet-technologies-eyes-147-upside/)
- [24/7 Wall St.: Poet Faces Legal Risk and Tax Questions (2026-04-30)](https://247wallst.com/investing/2026/04/30/poet-faces-legal-risk-and-tax-questions-but-there-is-upside-potential/?.tsrc=rss)
- [Seeking Alpha: POET, I Was Too Early (Lumilens brutal proof phase)](https://seekingalpha.com/article/4906873-poet-i-was-too-early-but-lumilens-has-moved-the-stock-into-a-brutal-proof-phase)
- [Seeking Alpha: POET Technologies, Why I Locked In Profits (Downgrade)](https://seekingalpha.com/article/4905222-poet-technologies-why-i-locked-in-profits-and-where-i-am-re-buying-downgrade)
- [Tradestie: POET Stock Analysis](https://tradestie.com/apps/stockmarket/POET-analysis)
- [Benzinga: POET quote and consensus](https://www.benzinga.com/quote/poet)

SENTIMENT REPORT COMPLETE
