# Sentiment — FANUY (Fanuc Corp ADR) as of 2026-10-22

## Analyst consensus
ADR (FANUY, Yahoo rec_summary): 0 buy / 2 hold / 0 sell（當月與前一個月相同，覆蓋極薄）。
Tokyo 母公司 (6954) 券商評等（Investing.com，2026-04 至 05 的紀錄，非 ADR）：約 8 buy / 10 hold / 2 sell。
近期動向：
- 未找到 2026 年 ADR 層級的升評或降評紀錄。
- Tokyo 個別券商（2026-04 至 05）：Goldman Sachs Sell（目標 5,600 JPY，05/28 維持）、Nomura Buy（8,500 JPY，05/14）、CLSA Hold（6,400 JPY，04/27）、Macquarie Buy（8,000 JPY，04/27）、Citi Buy（7,600 JPY，04/23）。
- 目標價：Investing.com ADR 平均 12 個月目標 21.72 USD（2026-08 快照，高 22.81 / 低 20.63），相對最近價位約 18.44 USD（MarketScreener，10/16 收盤）隱含約 +18% 上行空間。Tokyo 平均目標約 7,424.5 JPY。
- 注意：ADR 與 Tokyo 的評等樣本與時間窗不同，不可直接合併比較。

## Retail social
- Reddit: 以 WebSearch 搜尋 r/wallstreetbets、r/stocks 與 site:reddit.com 皆無 FANUY 相關討論串命中。Reddit 直接 JSON 端點依任務指示未以 WebFetch 呼叫，因此無法取樣本，此來源記為 DATA_UNAVAILABLE。
- StockTwits / X: StockTwits 頁面僅見新聞標題（多為 Zacks 文章），無可讀取的情緒分數或訊息流。其中一則標題提到 FANUY 因獲利預期樂觀而升至 Zacks Rank #2（Buy）。X 無可用結果。
- 聲量（定性）：偏低。FANUY 為 OTC ADR，未見散戶熱議跡象；此判斷為缺乏直接社群數據下的推論，信心低。
- 情緒傾向：無直接社群樣本，無法判定散戶多空傾向。新聞與評級層面的語氣偏中性至溫和正面。
- 主要主題（來自新聞與評論，非散戶貼文）：
  - 「實體 AI」（physical AI）題材：與 NVIDIA 合作開發 AI 驅動工業機器人，2025 年底消息後股價大漲（單日約 18%，Simply Wall St 報導）。
  - 美國回流製造：2026-03 宣布於密西根州投資約 90 百萬美元興建機器人廠，預計 2027 年底完工。
  - 估值疑慮：Investing.com 顯示 P/E 約 31.3x，同業中位數約 22.3x；Simply Wall St 亦提到估值高於同業。
  - 技術面偏弱：Investing.com 技術訊號曾為 Strong Sell（快照日期不明）；Trade-Ideas（2026-09-29）顯示 Neutral，股價距歷史高點 30.42 USD 約 38%。
  - 空單：MarketBeat 舊快照曾顯示空單部位增加約 201%，但日期陳舊，僅供參考。

## Insider activity
DATA_UNAVAILABLE。yf insider 回傳空清單，無法計算 6 個月淨買賣金額。
- 高階主管名單（yf info）可見 CEO Kenji Yamaguchi、CFO Ryuji Sasuga 等，但 exercisedValue / unexercisedValue 皆為 0，此欄位不是交易紀錄，不能當作無內部人交易的證據。
- 結論：內部人情緒無法評估。

## Ownership shifts
- yf major_holders：insidersPercentHeld 0.0，institutionsPercentHeld 約 0.229%，機構數 27。數值偏低，對 ADR 而言可能是資料來源口徑問題，不宜直接解讀為機構持股極低。
- inst_holders（2026-06-30 與 2026-09-30 申報）前 10 名：
  - 增持：Rhumbline（+10.6%）、Front Row（+18.4%）、Gamma Investing（+12.3%，9/30 申報）、Salomon & Ludwin（+37.9%）、Atlas（+100%，部位極小）、Sankala（新增或大幅增加，pctChange 1.0）。
  - 減持：Aristotle Capital（-5.8%，最大持有人，約 356 萬股）、Hantz（-9.6%）、PNC（-0.06%）、Sterling（-69.7%，部位極小）。
- 解讀：增減互現，多為小型部位，無明顯集中化或撤離趨勢。最大持有人 Aristotle 小幅減持。

## Net sentiment score
Composite: **neutral**（信心：低）

依據：
- 分析師（ADR 0/2/0，樣本極少）：中性。
- Tokyo 券商分布（約 8 買 / 10 持有 / 2 賣）與目標價隱含上行：偏正面，但樣本不同。
- 散戶社群：無有效數據，無法評分。
- 新聞語氣：正面主題（physical AI、美國產能）與負面估值、技術面並存。
- 機構持股：增減互現，無明確方向。
- 內部人：無數據。

Divergence flag: **no（無法判定）**。散戶面無數據，無法與分析師方向比較。分析師面本身 ADR 與 Tokyo 口徑不一，建議以 Tokyo 樣本作為更完整的參考。

## Data quality and gaps
- yf 即時 feed 遭 Yahoo cookie / crumb 阻擋，改用 prices/yf/FANUY.json 快取（刷新時間 2026-10-22 11:40 UTC），快取與 tool 輸出一致。
- 下次財報日：yf earnings_dates 為 2026-10-30（EPS 預估 0.13）；WebSearch 的 Investing.com 快照列為 2026-10-22（當日），兩者不一致，以 yf 為準但需再確認。
- Reddit 與 StockTwits 無有效社群樣本；X 無可用結果。
- 搜尋結果的日期分散（2025-12 至 2026-10），部分快照陳舊，已在內文標示。

## Sources
- Investing.com FANUY: https://www.investing.com/equities/fanuc-corporation
- Investing.com Fanuc Corp. (6954) consensus (UK): https://uk.investing.com/equities/fanuc-corp.-consensus-estimates
- Trade-Ideas FANUY: https://www.trade-ideas.com/stock-info/FANUY/
- MarketScreener FANUY: https://ca.marketscreener.com/quote/stock/FANUC-CORPORATION-120791928/
- StockTwits FANUY news: https://stocktwits.com/symbol/FANUY/news
- TipRanks FANUY: https://www.tipranks.com/stocks/fanuy/stock-news
- Simply Wall St (physical AI, Nvidia): https://simplywall.st/stocks/jp/capital-goods/tse-6954/fanuc-shares/news/why-fanuc-tse6954-is-up-180-after-announcing-nvidia-powered
- TechNews (US robot plant, 2026-03-24): https://technews.tw/2026/03/24/fanuc-plans-to-boost-robot-production-in-the-us/
- MarketBeat FANUY: https://www.marketbeat.com/stocks/OTCMKTS/FANUY
- 本地快取：/home/user/agent-trading-scans/prices/yf/FANUY.json

SENTIMENT REPORT COMPLETE
