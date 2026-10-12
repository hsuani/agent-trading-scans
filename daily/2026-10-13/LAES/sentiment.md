# Sentiment — LAES (SEALSQ) as of 2026-10-13

資料截止：2026-10-13。之後的資料視為未知。

## Analyst consensus
2 buy / 0 hold / 0 sell（yf rec_summary，0m 與 -1m 快照一致；strongBuy 1、buy 1）。樣本只有 2 位分析師，代表性有限。

Recent moves:
- Cantor Fitzgerald 於 2025-12-18 以 $7 初始覆蓋（Overweight）。
- 2026-04-02 目標價由 $7 下調至 $4，維持 Overweight（來源：Benzinga、Investing.com 轉述）。
- 未找到 2026 年具名的評級升級或降級。一篇 AAII 文章（2026-09）提到「有分析師降級、有分析師升級」，但沒有列出機構與目標價，且與兩位分析師的覆蓋數不一致，列為未驗證。
- 目標價共識彼此衝突（快照日期不同）：Benzinga 約 $5；Fintel 平均 $6.12（2026-06，高點 $8.40）；Investing.com 平均 $6.00（可能早於 4 月下修）；VCP Scanner $8.00（2026-06-25，可能已過時）。

## Retail social
- Reddit: DATA_UNAVAILABLE。r/wallstreetbets 與 r/stocks 的 search.json 抓取被工具拒絕（無法存取 reddit.com 網域）。WebSearch 也沒有找到 LAES 相關的 r/wallstreetbets 討論串，因此無法量化 Reddit 的情緒傾向或討論量。
- StockTwits / X: StockTwits 抓取失敗（api.stocktwits.com DNS 解析失敗），列為 DATA_UNAVAILABLE。X 端的 WebSearch 沒有找到 2026-10 的可用貼文。
- 新聞與論壇代理指標（非散戶社群原始資料）:
  - MarketBeat 新聞情緒分數 0.37 至 0.81（-2 至 +2 量表），多數快照低於或接近同業平均。
  - StockScan 技術面摘要：0 個買進訊號、11 個賣出訊號、6 個中性訊號，偏空。
  - 義大利投資論壇一則貼文把 LAES 描述為抗量子加密晶片與加密方案的標的（屬零星單篇，代表性低）。
- 討論量（相對常態）: 無法量化。以搜尋結果數量看，2026 年的獨立討論來源稀少，屬低可見度標的，但這只是間接推論。
- Themes（來自新聞與論壇，非社群原始貼文）:
  - 抗量子（post-quantum）與量子安全晶片的敘事：是主要的多方論述來源。
  - 稀釋風險：有一則報導提到可售出最多 $100M 股份的交易，市場視其為主要風險。
  - 2026-06 的策略動作：投資 Quobly Series A、取得 WeCan 多數股權，以及「純量子平台」定位。
  - 獲利能力：2025 年初步營收約 $18M，仍未獲利，依賴股權募資；估值高度依賴量子敘事是否持續。
  - 股價動能：AAII 指出 2026-09 初的年初至今跌幅約 36%。

Retail tilt: 無法可靠判定（社群資料缺漏）。以代理指標推估偏中性至偏空。

## Insider activity
Net 6mo（2026-04-13 至 2026-10-13）：$0 公開市場買進；約 $0.77M 賣出（yf insider 的 Value 欄位加總，為毛額）。
另有多筆衍生性證券以 $0.01 行權後賣出，屬行權後變現，不計為買進。

Notable:
- CFO John Charles O'Hara：窗口內賣出約 $0.30M（2026-04-17 至 2026-06-05，多筆，價格 $3.5 附近至 $2.7 附近）。窗口內最大的單一賣方之一。
- CEO Carlos Creus Moreira：窗口內賣出約 $0.11M（2026-05-29 與 2026-06-03）。最後一筆為 2026-06 初。
- Officer Jean-Pierre Enguent：窗口內賣出約 $0.30M，節奏規律，約每月 15,000 股行權後賣出（2026-07、08、09、10 月）。最近一筆 2026-10-06 以 $2.46 賣出 35,000 股。規律性可能來自事先安排的交易計畫，但資料無法證實是否屬 10b5-1 計畫。
- Officer Franck Jean Buonanno：2026-05-14 以 $2.90 賣出 20,000 股，窗口內約 $0.06M。
- Director Peter Ward：2026-06-16 行權 366,746 股（$0.01），無賣出紀錄。
- 解讀：窗口內以高階主管的持續賣出為主，沒有任何公開市場買進。賣出價格由 2026-06 的約 $3.5 下滑至 2026-10 的約 $2.4 至 $2.5。

Ownership: 內部人持股 2.69%；機構持股 6.66%（float 口徑 6.84%），機構數 129。歷史趨勢 DATA_UNAVAILABLE（僅有單一快照，無法判斷集中度變化方向）。

## Net sentiment score
Composite: 偏空（bearish-leaning neutral）。信心：低。

依據與權重:
- 分析師（n=2，全為 Buy）：偏多，但樣本少，且 4 月已下修目標價。
- 內部人：窗口內無公開市場買進，賣出持續，偏空。
- 技術面與新聞情緒代理：偏空至中性。
- 散戶社群：DATA_UNAVAILABLE，無法納入計分。

Divergence flag: 條件性是。分析師為 2 Buy / 0 Sell 的多方，與內部人持續賣出、技術面與新聞情緒偏空的方向相反。但因為散戶社群資料缺漏，無法確認「散戶 vs 分析師」的正式背離，此旗標以代理指標判定，僅供參考。

Data gaps:
- Reddit、StockTwits：DATA_UNAVAILABLE。
- 分析師目標價在不同來源上衝突，且多為過時快照。
- 空方比率（short interest）各來源衝突：Benzinga 約 5.9% float，MarketBeat 快照約 7% 至 14%。
- 新聞與技術面數據多為非 2026-10 的快照，時間點不一。

## Metrics

| 指標 | 數值 | 來源 / 備註 |
|---|---|---|
| 分析師評級（Buy / Hold / Sell） | 2 / 0 / 0 | yf rec_summary（0m） |
| 強力買進 / 買進 | 1 / 1 | yf rec_summary |
| 最近目標價變動 | $7 → $4（2026-04-02，Cantor） | Benzinga、Investing.com |
| 目標價共識範圍 | $5 至 $8（快照不一） | 多來源，部分過時 |
| 窗口內公開市場買進（6mo） | $0 | yf insider |
| 窗口內賣出（6mo，毛額） | 約 $0.77M | yf insider，Value 加總 |
| 窗口內 CFO 賣出 | 約 $0.30M | yf insider |
| 窗口內 CEO 賣出 | 約 $0.11M | yf insider |
| 最近內部人賣出價 | $2.46（2026-10-06） | yf insider |
| 內部人持股 | 2.69% | yf major_holders |
| 機構持股 | 6.66%（float 6.84%） | yf major_holders |
| 機構數 | 129 | yf major_holders |
| 機構持股趨勢 | DATA_UNAVAILABLE | 單一快照 |
| MarketBeat 新聞情緒 | 0.37 至 0.81（-2 至 +2） | WebSearch 轉述，快照不一 |
| 技術面訊號（買 / 中 / 賣） | 0 / 6 / 11 | StockScan，偏空 |
| Reddit 討論量與傾向 | DATA_UNAVAILABLE | 抓取被拒 |
| StockTwits 訊息與傾向 | DATA_UNAVAILABLE | DNS 失敗 |
| 綜合情緒 | 偏空（信心低） | 本報告推定 |
| 背離旗標 | 條件性是 | 以代理指標判定 |

SENTIMENT REPORT COMPLETE
