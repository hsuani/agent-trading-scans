# Sentiment — GOOGL (Alphabet) as of 2026-11-23

**資料完整度: 低。** 即時 yf 呼叫因 Yahoo cookie/crumb 失敗而回傳空值。repo 快取 `prices/yf/GOOGL.json`（2026-11-21 更新）的 recommendations、rec_summary、insider、major_holders、inst_holders 皆為空陣列，因此分析師分布、內部人交易、持股結構無法由結構化來源取得。Reddit（r/wallstreetbets、r/stocks）與 StockTwits 皆無法連線，**軟失敗**。以下僅使用 WebSearch 聚合的次級來源，數值多為間接引用，未能逐筆核實 SEC 原始文件。未借用 daily/ 下舊報告的數字。

## Analyst consensus
次級來源（StockAnalysis / MarketBeat / Benzinga，日期不一）: 整體評等偏多，約 58 位分析師給予 "Strong Buy"（StockAnalysis）；MarketBeat 為 Buy 共識。**確切的 buy / hold / sell 家數無法取得**（rec_summary 快取為空）。

平均目標價來源差異: StockAnalysis 約 400.37 USD、MarketBeat 約 412.51 USD、Benzinga 約 405 USD（30 位，高 485 / 低 300）、TipRanks 約 400.47 USD（高 490 / 低 300）。

近期動作（需注意日期）:
- Wells Fargo（2026-11-02）: 目標價由 371 降至 365 USD，維持 Overweight，理由為 AI Overviews 壓抑搜尋廣告。
- JPMorgan（2026-11-09）: 移出 Analyst Focus List，維持 Overweight，理由為 AI 搜尋變現放慢與 AI 基礎建設支出高。
- Citigroup（2026-10-30，Benzinga 列表）: 目標價由 447 降至 375 USD，維持 Buy。
- Wolfe Research: 目標價由 390 降至 360 USD，維持 Outperform。
- Mizuho: 目標價由 410 升至 420 USD，理由為 Anthropic 合作與雲端成長。
- Raymond James: 升至 Strong Buy，目標 400 USD（由 315 升），日期不明。
- Zacks Research: 降至 Hold（MarketBeat 網址日期 2026-08-13，評等文字未驗證）。
- Loop Capital 升 Buy、目標 320 USD 的消息為 **2025-11-18**，不計入當前動作。

股價參考: 次級來源顯示 2026-11-06 收 284.78 USD、2026-11-12 收 293.45 USD。這些價格與 2026-11-23 當日價不同，僅供參考。

## Retail social
- Reddit（r/wallstreetbets、r/stocks）: **無法連線（軟失敗）**，無法計算提及量與多空傾向。
- StockTwits: **無法連線（DNS 無法解析 api.stocktwits.com，需於 session 網路設定允許該網域）**，軟失敗。
- X / 新聞聊天: 搜尋結果以媒體與聚合站為主，未見可量化的社群提及數。定性來看，散戶與媒體敘事偏分歧: 一方認為 AI 布局領先（Mizuho 觀點、ARK 於 11 月初小幅買進約 2 M USD），另一方聚焦財報失利與股價自高點回落約 20%（自 2026-07-31 起）。
- 提及量相對基準: **無法判定**（缺 Reddit/StockTwits 數據）。
- 主題（由搜尋結果歸納）: AI 搜尋對廣告的衝擊、AI 基礎建設資本支出、雲端與 Anthropic 合作、FQ3 財報 EPS 失利、集體訴訟（主告人截止 2026-12-01）、估值偏高（Zacks 指 forward P/S 9.93x 對產業 7.45x，但該文章可能早於近期跌幅）。
- 財報背景（repo 快取 earnings_dates）: 2026-10-28 報告 EPS 2.12，對比預估 3.01，差距 -29.54%。

## Insider activity
快取無內部人交易資料。第三方聚合站（Stock Titan、Portfolio Savvy、ARINCEN）顯示:
- CEO Sundar Pichai: 2026-02-18 起有 Class C 股票 10b5-1 計畫賣出（約 9.9 M USD 淨賣出，價約 302–305 USD）；3 月初與 3 月中另有賣出，價約 306–310 USD。
- 10 月的 Pichai 與 President Ruth Porat 紀錄主要為稅務代扣與 "Other"，非公開市場交易。
- 有一聚合站稱 Pichai 近 12 個月無公開市場賣出，與上述 Form 4 矛盾，判定為過期資料。

**Net 6mo（2026-05-23 至 2026-11-23）: 無法可靠計算。** 找到的公開市場賣出集中在 2026 年 2–3 月，落在 6 個月視窗外。視窗內未找到可驗證的 CEO / CFO 買入或賣出。無公開市場買入紀錄。需至 SEC EDGAR 核對 Form 4。

## Ownership shifts
- 2026-06-30 snapshot（聚合站，數字不一致）: 機構持有者約 5,708 家；BlackRock 約 4.61 億股、Vanguard 約 3.83 億股、FMR 約 2.51 億股。
- 機構持股比例約 27–28.5%（來源不一）。
- 2026 Q2 季度流向（Holdings Channel 樣本）: 增持 26 檔、減持 23 檔、新進 1 檔，樣本太小，不具代表性。
- 整體趨勢: 無法確定明確的集中或分散方向。數據來源與股份類別（GOOGL 對 GOOG）不一致，僅供參考。

## Net sentiment score
**Composite: 偏多（分析師側）、中性（散戶側，資料缺失）、整體 neutral-to-bullish，信心低。**
- 分析師: 評等共識偏多，但近期目標價連續下修（Wells、Citi、Wolfe），JPM 降低關注度，偏多強度減弱。
- 內部人: 無可驗證的近 6 個月公開市場買入；CEO 的賣出屬於 2–3 月的 10b5-1 計畫，且在視窗外，中性偏空的弱訊號。
- 散戶: 無法量化。
- 信心低，原因為 Reddit、StockTwits 與 yf 結構化欄位皆不可用。

**Divergence flag: 無法判定（資料不足）。** 分析師側偏多，散戶側無數據，因此不能確認是否背離。若 Reddit/StockTwits 恢復，應重跑。

## 資料限制與後續
1. 修復 Yahoo cookie/crumb 或等待下次 `yf.py refresh-cache` 更新 recommendations、insider、major_holders 欄位。
2. 允許 api.stocktwits.com 網域，並重試 Reddit JSON。
3. 以 SEC EDGAR 核對 Pichai 與 Porat 的 Form 4，確認 6 個月淨額。

Sources（WebSearch 聚合站，部分為未核實的二手來源）:
- https://stockanalysis.com/stocks/googl/
- https://finance.yahoo.com/news/alphabet-upgraded-micron-initiated-wall-143731735.html
- https://247wallst.com/investing/2026/11/09/jpmorgan-just-removed-alphabet-from-its-analyst-focus-list/
- https://www.benzinga.com/quote/GOOGL/sentiment
- https://www.marketbeat.com/instant-alerts/zacks-research-downgrades-alphabet-nasdaqgoogl-to-hold-2026-08-13/
- https://portfoliosavvy.com/report/000119312526061632-pichai-sundar-2026-02-18
- https://fintel.io/so/mx/googl/geode-capital-management-llc
- https://www.earningswhispers.com/whales/GOOGL

SENTIMENT REPORT COMPLETE
