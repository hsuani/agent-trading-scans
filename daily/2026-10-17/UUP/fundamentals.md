# Fundamentals — UUP (Invesco DB US Dollar Index Bullish Fund) as of 2026-10-17

> 資料完整度警示：本次 Yahoo Finance 端點多數被 egress proxy 以 403 policy denial 拒絕（`finance.yahoo.com`、`query2.finance.yahoo.com`、`fc.yahoo.com`、`guce.yahoo.com`）。可用資料僅限 `info` 與 `fast_info` 的快取版本（cache timestamp 2026-10-16 11:16 UTC）。`financials`、`balance_sheet`、`cashflow`、`insider`、`major_holders`、`inst_holders`、`earnings_dates` 全部無法取得，以下一律標示 n/a。本報告未繞過 proxy 政策。資料最新日期為 2026-10-15 常規交易時段收盤附近，尚無 2026-10-17 的資料，屬於 as-of 日之前的快照。

## Executive summary
UUP 是 Invesco 發行的美元多頭指數 ETF，以 DX 美元指數期貨追蹤「做多美元對六大貨幣籃子」的報酬，費用率 0.75%，最新快照顯示總資產約 4.31 億美元（totalAssets 431,136,608），股價 29.00 美元，位於 50 日均線 28.39 與 200 日均線 27.83 之上，YTD 報酬 +6.28%。作為工具而非公司，本報告不適用營收、利潤率與資產負債表分析；基本面判讀的重點在於費用結構、規模與流動性、追蹤誤差與資料可靠性。由於 AUM 歷史、資金流向、持倉明細與分配紀錄全部無法取得，無法對資金流向給出結論，且快照中若干欄位（殖利率、beta）前後矛盾，應降低其權重。

## 標的性質與結構（工具描述）
- 基金全名：Invesco DB US Dollar Index Bullish Fund（shortName: Invesco DB USD Index Bullish Fu）。
- 追蹤指數：Invesco DB US Dollar Index Bullish Index（DBUSBUL），由 info.longBusinessSummary 確認「投資於期貨合約以追蹤指數，指數反映 DX Contracts 多方部位的市值變動」。
- 組成（背景知識，未由本次工具驗證）：DX 期貨隱含的六大貨幣權重約為 EUR 57.6%、JPY 13.6%、GBP 11.9%、CAD 9.1%、SEK 4.2%、CHF 3.6%。因此 UUP 實質上是「做多美元 vs 歐元為主的籃子」，與美元走強方向正相關。
- 基金成立：fundInceptionDate 為 2007-02-20；firstTradeDate 為 2007-03-01。
- 交易所：NYSE Arca（exchange: PCX）；幣別 USD；category: Trading--Miscellaneous；fundFamily: Invesco。
- 無公司管理團隊資料（companyOfficers、executiveTeam 皆為空）。
- 無 longBusinessSummary 以外的揭露，因此無分部或產品組合可拆解。

## 績效與價格結構（取代營收與獲利）
| 指標 | 數值 | 來源欄位 |
|---|---|---|
| 最新價 | 29.00 | regularMarketPrice |
| 前收 | 29.12 | regularMarketPreviousClose |
| 當日變動 | -0.41% | regularMarketChangePercent |
| 日高 / 日低 | 29.04 / 28.965 | dayHigh / dayLow |
| NAV | 29.13 | navPrice（折價約 -0.45%） |
| 52 週區間 | 26.40 - 29.25 | fiftyTwoWeekRange |
| 歷史高 / 低 | 30.76 / 20.84 | allTimeHigh / allTimeLow |
| 50 日均線 | 28.39 | fiftyDayAverage |
| 200 日均線 | 27.83 | twoHundredDayAverage |
| YTD 報酬 | +6.28% | ytdReturn |
| 52 週報酬 | +4.50% | fiftyTwoWeekChangePercent |
| 近 3 個月報酬 | +1.27% | trailingThreeMonthReturns |
| 3 年平均年化報酬 | +3.81% | threeYearAverageReturn |
| 5 年平均年化報酬 | +6.01% | fiveYearAverageReturn |

價格相對 52 週高點約 -0.85%，相對 52 週低點約 +9.8%，處於區間上緣。

## 費用、規模與流動性
- 費用率（netExpenseRatio）：0.75%，屬於 Invesco DB 系列標準費率，年化成本拖累明顯高於一般被動指數 ETF（多數 0.03% - 0.20%）。長期持有時，費用會直接侵蝕追蹤報酬。
- 總資產（totalAssets / netAssets）：約 4.31 億美元。規模屬於中小型 ETF，對一般交易部位流動性足夠，但遠低於 UUP 歷史高點期間的規模（無歷史資料，無法量化變化）。AUM 趨勢：n/a。
- 日均量：3 個月平均 1,672,265 股，10 日平均 1,898,150 股；以價格 29 美元估算，日均成交金額約 4,850 萬美元（推算值）。
- 當日量：1,488,634 股，低於 10 日均量。
- 買賣價差（快照）：bid 28.85 / ask 28.91，價差約 0.21%，此數值取自盤前或非交易時段快照，正式交易時段需重新確認。
- 股份數與每股 NAV 總量：n/a（sharesOutstanding 未提供）。
- 分配：trailingAnnualDividendRate 與 trailingAnnualDividendYield 皆為 0.0，但 yield 欄位為 0.0322（3.22%）且 dividendYield 為 3.22。兩者矛盾，判定為資料不一致，不採信。UUP 通常以年度分配為主，分配金額來源為 T-bill 利息收入，實際分配紀錄 n/a。

## 資金流向與持倉（全部 n/a）
- 資金流入/流出（fund flows）：n/a。
- 持倉明細（期貨部位、T-bill 抵押品）：n/a。
- 機構持有人（inst_holders）：n/a（Yahoo 端點被拒，回傳空陣列，不代表無機構持有）。
- 大股東集中度（major_holders）：n/a。
- 內部人交易：不適用（ETF 無內部人）。

## 風險與相關性
- beta3Year 欄位為 -11.39，數值量級明顯異常（一般 beta 介於 -2 至 +3），判定為資料錯誤，本報告不採用。
- 美元指數本身的方向性風險是 UUP 的主要風險，與 DX 組成貨幣（EUR、JPY）的政策利差與避險需求高度相關。
- 期貨滾動（roll）成本與 contango/backwardation 會造成追蹤偏差，本次無法量化，因缺乏 NAV 歷史與指數報酬對照。
- 費用率 0.75% 在低波動或美元盤整期間會顯著侵蝕報酬。
- 無法取得 2026 年內的 AUM 歷史，無法判斷規模是否在縮減。

## Key catalysts（工具無法取得官方事件日曆，僅列宏觀面）
- 下一次 earnings_dates：不適用（ETF 無財報）。
- 宏觀事件：美國與主要央行（Fed、ECB、BoJ、BoE）利率決議、CPI 與非農就業數據，會直接影響美元方向。具體日期未由工具確認。
- 快照顯示價格位於 50 日與 200 日均線之上，趨勢偏多，但此為技術面描述，非基本面結論。
- 分配日：通常為年底，確切日期 n/a。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 費用率 netExpenseRatio | 0.75% | n/a | 約 0.10%（被動 ETF 估計） | 偏高，持有成本劣勢 |
| 總資產 totalAssets | 431.1 百萬美元 | n/a | 規模中小 | 流動性足夠，規模風險中等 |
| 股價 vs 50 日均線 | +2.1% | n/a | n/a | 短期趨勢偏多 |
| 股價 vs 200 日均線 | +4.2% | n/a | n/a | 中期趨勢偏多 |
| 52 週報酬 | +4.50% | n/a | n/a | 正報酬 |
| YTD 報酬 | +6.28% | n/a | n/a | 年內表現正面 |
| 3 年平均年化報酬 | +3.81% | n/a | n/a | 中等 |
| 5 年平均年化報酬 | +6.01% | n/a | n/a | 中等偏正 |
| 日均量（3 個月） | 1,672,265 股 | n/a | n/a | 流動性尚可 |
| NAV 折溢價 | 約 -0.45%（折價） | n/a | 0% | 接近 NAV，偏差小 |
| 殖利率 yield | 3.22%（與 trailing 分配 0 矛盾） | n/a | n/a | 資料不一致，不採信 |
| beta3Year | -11.39 | n/a | n/a | 數值異常，不採信 |
| AUM 趨勢 | n/a | n/a | n/a | 無法評估 |
| 資金流向 | n/a | n/a | n/a | 無法評估 |
| 持倉 / 期貨部位 | n/a | n/a | n/a | 無法評估 |

Sector median 為估計值，非工具回傳。

## Red flags
- 費用率 0.75% 偏高，長期持有報酬拖累明顯。
- 資料源大面積失效：Yahoo 財務、持有人、資金流與分配端點皆被 proxy 拒絕，本報告的可驗證度有限。
- 快照欄位內部矛盾：殖利率 3.22% 與 trailing 分配 0.0；beta3Year -11.39 量級異常。
- 無 AUM 歷史與資金流，無法判斷是否有贖回壓力。
- 美元方向單邊風險：部位本質為單一宏觀押注，無基本面現金流支撐。
- 快照非 2026-10-17 當日資料，最新為 2026-10-15 收盤附近，使用前需重新確認。

FUNDAMENTALS REPORT COMPLETE
