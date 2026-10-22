# Sentiment — ABBNY (ABB Ltd ADR) as of 2026-10-22

資料狀態摘要: 分析師評級可取得 (yfinance 與網路彙整互有出入); 內部人交易回傳空值 (未必代表無交易); 機構持股比例數據明顯異常; Reddit / StockTwits 未取得有效內容 (依指示未使用 WebFetch, WebSearch 亦未找到相關貼文)。整體可信度偏低。

## Analyst consensus
yfinance `rec_summary` (本月, 0m): 0 strong buy / 0 buy / 5 hold / 0 sell / 1 strong sell (共 6 家)。
前月 (-1m 至 -3m): 0 buy / 3 hold / 2 strong sell (共 5 家)。
網路彙整 (Investing.com、Walnut Invest, 日期不一): 0 buy / 3 hold / 2 sell。MarketBeat 共識評級為 Hold。

Recent moves (網路彙整, 多數為 2026 年 7 月或無日期, 未能確認 10 月內的評級變動):
- Pareto 升評至 Buy (目標 CHF 96.40, MarketBeat 標示 2026-07-16); 先前有降評至 Hold 的紀錄, 順序不明。
- DNB Carnegie 升評至 Buy (日期不詳)。
- Handelsbanken 降評至 Underperform, 目標 $67 (日期不詳)。
- Barclays 重新給予 Equal Weight, 目標 CHF 76。
- JPMorgan 目標由 CHF 70 升至 CHF 80, 維持 Neutral。
- Citi 目標由 CHF 78 升至 CHF 85, 維持 Neutral。
- RBC 目標由 CHF 81 升至 CHF 83, 維持 Sector Perform。

目標價平均值: Walnut 約 $93.32; Investing.com 約 $92.60; MarketBeat 顯示 $58, 但與其列出的股價不一致, 不採用。
注意: yfinance 的 0 buy 與 Pareto、DNB Carnegie 的升評 Buy 有衝突, 可能是日期或評級機構覆蓋範圍不同, 需人工核對。

## Retail social
- Reddit: 未取得有效資料。依指示未用 WebFetch 讀取 r/wallstreetbets 與 r/stocks 的 JSON 端點; WebSearch 未回傳任何 Reddit 貼文 (結果多為 Seeking Alpha、分析師頁面與報價頁)。
- StockTwits / X: 未取得 StockTwits 資料 (搜尋無結果)。X 端未找到可用的 ABBNY 近期討論。
- 討論量 (buzz volume): 無法量化。從搜尋結果看, ABBNY 為大型工業股 ADR, 散戶社群覆蓋度似乎偏低, 但這是定性判斷, 無實際計數支持。
- Seeking Alpha 留言 (2026 年 2 至 3 月, 較舊): 有留言者認為 ABBNY 為長期持有標的, 另有人比較 PRYMY、HUBB、MLI 等同業。這是較早期的散戶意見, 不代表當前情緒。
- 其他非散戶來源 (供參考, 非社群情緒): TipRanks 技術面共識 Buy (約 2025 年 10 月資料); Zacks Rank #2 (Buy); Investing.com 技術訊號 Strong Buy; TipRanks 新聞情緒為中性 (約 50%)。
- Themes (由有限來源歸納): 資料中心與電網需求 (data center、electrification); 高壓直流 (HVDC) 技術; 近期 Rotork 收購案; 估值偏高; Motion 部門利潤率壓力; Automation 訂單年減。

## Insider activity
yfinance `insider` 回傳空陣列, 無法確認 6 個月內的買賣金額。空值未必代表沒有內部人交易; ABB 為瑞士公司 ADR, 內部人申報資料在 Yahoo 類來源中常見缺漏, 需向 SEC 或瑞士 SIX 申報資料另行核實。
Net 6mo: 資料不足 (無法計算 $ 買入或賣出)。Notable: 無。

## Ownership shifts
- yfinance `major_holders`: insidersPercentHeld 0.0; institutionsPercentHeld 0.00202 (0.2%); institutionsCount 89。0.2% 的機構持股比例明顯不合理, 疑為 ADR 資料覆蓋不完整的問題, 不宜採信。
- `inst_holders` (2026-06-30 申報, 前幾大): Northeast Investment Management 687,273 股 (較前期 -1.07%); Kornitzer Capital 305,030 股 (-12.58%); O'Brien Greene 88,747 股 (+6.36%); Royal Palms Capital 31,333 股 (-25.96%); Great Lakes Advisors 39,538 股 (+0.68%); Rhumbline Advisers 60,575 股 (+7.92%); PNC 23,809 股 (-8.6%); Front Row Advisors 74,150 股 (-5.35%)。另有 2026-09-30 申報的 Henry James International 等。
- 趨勢: 前幾大持股者多為小幅減持, 無明顯集中化或撤出訊號; 持股量相對 ABB 全球流通股數而言極小, 此數據僅能反映美國 ADR 側的申報, 代表性有限。

## Net sentiment score
Composite: **neutral** (信心度: 低)

理由:
- 分析師面: 多數為 Hold (yfinance 5 hold / 1 strong sell), 無 Buy 共識, 目標價平均約 $92-93, 與近期股價 (約 $91 至 $106, 依來源與日期不同) 接近, 上行空間有限; 但 2026 年 7 月起有數家機構升目標價, 且有 Pareto、DNB Carnegie 升評, 偏向中性偏正面的修正方向。
- 基本面新聞面 (非散戶): Q2 訂單成長約 28%, 資料中心與電網需求強勁, 指引上修; 但 Q2 EPS 低於市場預期 (0.66 對 0.74, 來源為 Walnut Invest)。
- 散戶面: 無有效資料, 無法形成可靠的散戶傾向判斷。
- 內部人與機構面: 內部人資料缺失; 機構持股變動以小幅減持為主, 無明顯方向性。

Divergence flag: **無法判定** (資料不足)。若以目前可得資料看, 分析師傾向偏中性, 散戶傾向無資料, 因此無法確認兩者是否相反。

資料限制與待辦:
1. 重新抓取 Reddit 與 StockTwits (需使用者確認是否允許 WebFetch 讀取這些 JSON 端點)。
2. 核對 yfinance 評級計數與各券商 10 月內的實際評級行動。
3. 核實 ABBNY 股價 (來源快照價格差異大, 從 $91 到 $106 不等)。
4. 以 SEC 或 SIX 申報資料補查內部人交易。
5. 機構持股比例 (0.2%) 疑似資料錯誤, 需以其他來源驗證。

## Sources
- [Walnut Invest ABBNY forecast](https://walnutinvest.com/stocks/abbny/forecast)
- [Walnut Invest ABBNY](https://walnutinvest.com/stocks/abbny)
- [Investing.com ABB Ltd ADR](https://www.investing.com/equities/abb-ltd-adr)
- [MarketBeat ABBNY forecast](https://www.marketbeat.com/stocks/OTCMKTS/ABBNY/forecast/)
- [MarketBeat instant alert, Pareto/DNB Carnegie coverage](https://www.marketbeat.com/instant-alerts/abb-nyseabbny-raised-to-strong-sell-at-bnp-paribas-2025-10-03)
- [StockAnalysis ABB](https://stockanalysis.com/stocks/ABB)
- [StockAnalysis ABBNY OTC](https://stockanalysis.com/quote/otc/ABBNY/)
- [TipRanks Handelsbanken downgrade](https://www.tipranks.com/news/the-fly/abb-downgraded-to-underperform-from-market-perform-at-handelsbanken)
- [TipRanks ABBNY](https://www.tipranks.com/stocks/abbny)
- [Seeking Alpha ABBNY comments](https://seekingalpha.com/symbol/ABBNY/comments)
- [Suredividend ABBNY Q2 2026 note (2026-07-16)](https://www.suredividend.com/wp-content/uploads/2026/07/ABBNY-2026-07-16.pdf)
- [Nasdaq/Zacks ABBNY peer comparison](https://www.nasdaq.com/articles/is-abb-abbny-stock-outpacing-its-industrial-products-peers-this-year-0)
- [Simply Wall St ABB narrative](https://www.simplywall.st/narratives/fqlz0u7x-global-protectionism-and-rising-cost-burdens-will-erode-margins)

SENTIMENT REPORT COMPLETE
