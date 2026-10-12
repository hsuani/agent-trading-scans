# Sentiment — CEG as of 2026-10-13

資料基準: pipeline/tools/yf 快取 (prices/yf/CEG.json, refreshed 2026-10-12 15:12 UTC)，現價 $295.00 (前收 $298.07)。即時 Yahoo cookie/crumb 取得失敗，已改用快取，屬預期情況。

## Analyst consensus
22 位分析師: 6 Strong Buy / 13 Buy / 3 Hold / 0 Sell (rec_summary 合計 19 BUY / 3 HOLD / 0 SELL)。info 欄位顯示 numberOfAnalystOpinions = 20，兩者計數口徑不同，以 22 為準列示。recommendationMean 1.55 (接近 Buy)。

目標價: 平均 $341.53、中位數 $345.50、最高 $395、最低 $290。以均價計算相對現價上行約 15.8%。

近 4 個月評級分布穩定 (0m 至 -3m 皆為 6 Strong Buy、3 Hold、0 Sell；Buy 由 13 增至 14 出現在 -3m 點位)。recommendations 工具僅回傳月度彙總，無逐筆升降評等紀錄。

近期券商動作 (WebSearch 彙整，屬二手來源，未逐一核對原始報告):
- 7/28 UBS 目標價 $388 → $380 (維持 Buy)
- 7/28 Barclays 目標價 $358 → $324
- 7/31 J.P. Morgan 目標價 $386 → $385 (維持 Buy)
- 8/10 Argus 維持 Buy，目標價 $325
- 8/11 Mizuho 維持 Hold，目標價 $290 (為 8 月列表中最低目標價)
- 8/17 Bernstein 維持 Buy，目標價 $296；DBS 維持 Buy，目標價 $350
- 8/19 Exane BNP Paribas 維持 Buy，目標價 $374
- 8/21 Morgan Stanley 維持 Buy，目標價 $364

8 月未見正式升評或降評，主要為目標價下修與維持評等。

## Retail social
- Reddit: 本次以 WebSearch 檢索 r/wallstreetbets、r/stocks 相關討論，未找到可引用的 CEG 近期討論串，無法取樣高讚貼文或計算多空比例。WebSearch 無法直接讀取 Reddit 搜尋 JSON，此來源 DATA_UNAVAILABLE。
- StockTwits / X: AltIndex 頁面顯示 StockTwits 情緒 100/100 (Bullish)，日均提及約 41 次，較三個月前成長 128%，但頁面未標示日期，僅能視為可能過時的參考值，信心低。X 端未取得可引用的近期貼文。
- SentiSense 30 日情緒分數 11 (輕度偏多)，日均提及約 11 次，Reddit 僅占提及量約 10%，多數聲量來自新聞。
- 聲量判讀: 兩個來源的提及量差距很大 (41 vs 11)，無法確定基準，只能定性為「中等、來源不一致」。
- Tilt: 偏多 (輕度)，但樣本薄弱、日期不一，置信度低。

Themes (依 WebSearch 結果彙整):
- 政策風險: 2026-01-20 因川普提議緊急批發電力拍賣與要求科技巨頭分攤電價上漲，股價單日重挫逾 9%，仍是市場記憶點。
- 併購整合: Calpine 收購已完成，形成全美最大電力生產商的定位，受到正面討論。
- 獲利與指引: Q2 EPS $2.55 (高於預估 $2.28)，營收 $7.5B，全年調整後營運獲利指引上修至 $11.50–$12.50。
- 重啟機組: Crane Clean Energy Center 併網時程受 PJM 影響，有報導指可能要到 2031 年才能重新併網，屬負面話題。
- 股價落後: 2026 年迄今跌幅各來源不一 (約 -18% 至 -25%)，市場多以「基本面佳、股價弱」描述。
- 下次財報: 快取資料顯示 2026-11-09 (EPS 預估 $3.75)。

## Insider activity
Net 6mo (2026-04-13 至 2026-10-13): 公開市場買入 $417,931 (1 筆)，賣出 $0 (無紀錄)。

Notable:
- Roger W. Crandall (Director): 2026-08-11 買入 1,500 股，成交價 $278.62，合計 $417,931。為本期唯一公開市場買入，也是區間內最明確的內部人正面訊號。
- 董事 (10 位) 2026-04-28 獲發 556 股限制性股票，每股 $305.71，單人約 $170K，屬薪酬授予，非市場買入。
- Crandall 2026-08-04 另有 462 股薪酬授予 ($123,470)。
- 高階主管 (CEO Joseph Dominguez、CFO Daniel Eggers 等) 於 2026-02-09 有大量交易紀錄，但已超出 6 個月窗口，且 yfinance 未提供金額欄位，不計入。

## Ownership shifts
- 機構持股占比 82.97%，機構數 2,448 家；內部人持股 0.34%。
- Q2 2026 (6/30) 前幾大持股變動: BlackRock 6.93% (+4.4%)、Vanguard Capital 5.94% (+4.5%)、State Street 5.48% (+3.3%)、Capital International 3.57% (+9.0%)。
- 減持訊號: ECP ControlCo, LLC 持股 4.06%，季度減少 34.8%；FMR 1.85%，減少 35.8%。ECP ControlCo 的持股性質未在資料中說明，不做因果推論。
- 流通股數由 2025-12-31 的約 3.12 億股增至 2026-06-30 的約 3.55 億股 (快取 balance sheet)，股數增加與併購相關，會稀釋每股數字比較，需留意。

## Net sentiment score
Composite: **偏多 (bullish)**，置信度 **中等**。

- 分析師面 (權重最高，資料完整): 強烈偏多。19/22 為 Buy，0 Sell，目標均價高於現價約 16%，但 8 月起目標價以下修為主，動能略弱。
- 內部人面: 偏多但樣本小。一筆 $418K 公開市場買入，區間內無賣出。
- 機構面: 中性偏多。持股比例高，主要大型機構小幅加碼，但 ECP ControlCo 與 FMR 大幅減持。
- 散戶面: 輕度偏多但資料不足。StockTwits 數值過舊、SentiSense 分數低、Reddit 無法取樣。

Divergence flag: **否**。散戶與分析師方向一致 (皆偏多)。需注意的是股價 2026 年表現明顯落後，分析師正向評級與股價走勢存在背離，但這屬於估值與股價動能的差異，不是散戶與分析師情緒的背離。

Confidence 說明: 分析師與內部人資料可直接驗證；散戶資料來源不一、日期不明，應降低權重。本報告不提供交易建議。

## Metrics

| 指標 | 數值 | 備註 |
|---|---|---|
| 分析師評等 (Buy / Hold / Sell) | 19 / 3 / 0 | Strong Buy 6 + Buy 13；Hold 3；Sell 0 |
| 分析師總數 | 22 (info 顯示 20) | 計數口徑不同 |
| recommendationMean | 1.55 | 1 為 Strong Buy，5 為 Sell |
| 目標價 均價 / 中位數 | $341.53 / $345.50 | 快取 info |
| 目標價 高 / 低 | $395 / $290 | 快取 info |
| 相對現價上行 (均價) | +15.8% | 以現價 $295.00 計算 |
| 近期 8 月券商目標價變動 | 多為下修或維持 | 來自 WebSearch 二手彙整 |
| 6 個月內部人淨買入 | +$417,931 | 僅 1 筆公開市場買入 (Crandall, 2026-08-11) |
| 6 個月內部人賣出 | $0 | 區間內無紀錄 |
| 薪酬授予 (6 個月內) | 約 $1.82M | 10 位董事 556 股 + Crandall 462 股，不計入買賣 |
| 機構持股占比 | 82.97% | 2,448 家機構 |
| 內部人持股占比 | 0.34% | 快取 major_holders |
| 前幾大機構 2026-Q2 增減 | BlackRock +4.4%、Vanguard +4.5%；ECP ControlCo -34.8%、FMR -35.8% | 季度持股變化 |
| StockTwits 情緒 | 100/100 Bullish (日期不明) | AltIndex，置信度低 |
| SentiSense 30 日情緒分數 | 11 (輕度偏多) | 日均提及約 11 次 |
| Reddit 取樣 | DATA_UNAVAILABLE | WebSearch 無可引用的近期討論串 |
| 日均社群提及量 | 約 11 至 41 次 | 來源不一，定性判讀為中等 |
| 綜合情緒 | 偏多 | 中等置信度 |
| 背離旗標 | 否 | 散戶與分析師同向偏多 |

## 來源
- pipeline/tools/yf CEG rec_summary / recommendations / insider / major_holders (本地快取 prices/yf/CEG.json)
- [Barchart 分析師評等彙整](https://www.barchart.com/story/news/3720623/constellation-energy-stock-analyst-estimates-ratings)
- [Benzinga CEG Sentiment](https://www.benzinga.com/quote/CEG/sentiment)
- [Walnut Invest CEG Forecast](https://walnutinvest.com/stocks/ceg/forecast)
- [AltIndex CEG StockTwits mentions](https://altindex.com/ticker/ceg/stocktwits-mentions)
- [SentiSense CEG Sentiment](https://app.sentisense.ai/stocks/CEG/sentiment)
- [MarketBeat CEG price target](https://www.marketbeat.com/stocks/NASDAQ/CEG/price-target/)

SENTIMENT REPORT COMPLETE
