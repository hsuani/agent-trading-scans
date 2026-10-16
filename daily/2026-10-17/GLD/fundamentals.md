# Fundamentals — GLD (SPDR Gold Shares) as of 2026-10-17

註：GLD 為實體黃金信託 ETF，非營運公司。本報告以持倉、AUM、費用率、流動性與淨值溢折價取代營收與獲利分析。數據時點：yfinance 快取 2026-10-16 11:15 UTC（盤前），最近一個正常交易日收盤為 2026-10-15（依 regularMarketTime 推定）。尚無 2026-10-17 之後的資料。

## Executive summary
GLD 為單一資產（實體金條）信託，無槓桿、無負債、費用率 0.40%，財務結構簡單，「財務健康」主要體現在淨資產規模 1,417 億美元與高流動性（近 3 個月均量 9.28M 股）。價格 382.71 美元相對淨值 374.84 美元溢價約 2.10%，且低於 50 日均線（397.34）與 200 日均線（415.06），52 週高點 509.70 美元回落約 25%，距 52 週低點 360.12 美元僅高約 6.3%。估值面不適用 P/E、EV/EBITDA 等公司指標，評價應以淨值溢折價與持有成本為主；本次工具無法取得持倉變動與申贖資料，資金流向結論缺乏直接證據。

## Revenue & profitability（信託收益與費用結構）
- 投資目標：信託持有的黃金追蹤金價表現，扣除信託費用（info.longBusinessSummary）。無營收、毛利、營業利益與淨利率概念；yfinance 利潤表與資產負債表查詢皆回傳錯誤或空值（financials / balance_sheet / cashflow 皆無資料）。
- 唯一可用的「獲利」代理指標為績效：年初至今 ytdReturn -3.34%；三個月 trailingThreeMonthReturns +3.63%；52 週 fiftyTwoWeekChangePercent -3.47%；三年年化 threeYearAverageReturn 0.28%；五年年化 fiveYearAverageReturn 0.17%。
- 費用拖累：netExpenseRatio 0.40%。以 AUM 1,417 億美元估算，年度信託費用約 5.7 億美元（推估，非資料直接值）。
- epsTrailingTwelveMonths = -9.394 不具經濟意義，信託不以盈餘為目標，此數值屬會計口徑，不作為估值依據。

## Cashflow & balance sheet（資產端與結構）
- 持倉集中度：100% 實體黃金（單一資產類別，無股票、債券或衍生品部位）。yfinance 未提供金條重量（盎司）、保管機構或分類明細，此部分 n/a。
- 負債與槓桿：信託無借款（資料未列示負債）；無股利，dividendYield 與 trailingAnnualDividendRate 皆為 0。FCF、FCF/NI 不適用。
- 規模：totalAssets = netAssets = 141,702,414,336 美元（約 1,417 億美元）。
- 每股淨值 navPrice = 374.84 美元。
- 隱含黃金價格（推估）：若每股約對應 0.1 盎司黃金（此為信託設計假設，非資料欄位），則隱含金價約 3,750 美元/盎司（已扣除累積費用，屬粗略估計）。資料中無現貨金價欄位，無法直接核對。
- 資料一致性問題：sharesOutstanding = 260.3M 股，乘以淨值約 975 億美元，與 netAssets 1,417 億美元不符（netAssets / navPrice 約 378.0M 股）。股數欄位可能過期，本報告以 netAssets 為準。
- bookValue = 170.017 與 priceToBook = 2.25 不可用（與 navPrice 不一致，且信託不以帳面價值衡量）；改以價格對淨值比（P/NAV）判讀，約 1.02 倍（382.71 / 374.84）。

## Capital allocation & insider signal（申贖、流動性與內部人）
- 申贖資金流（creation/redemption units）：本工具無法取得 ETF 申購與贖回單位資料，無法判斷近期淨流入或淨流出。此為重大資料缺口。
- AUM 趨勢：僅單一時點快照，無歷史 AUM 序列，無法計算 YoY 或季度變化。
- 流動性：當日成交量 8,522,745 股（約 32.6 億美元，依 382.71 估算）；10 日均量 7,494,520 股（約 28.7 億美元）；3 個月均量 9,278,844 股。成交量近 10 日較 3 個月均量低約 19%，屬縮量。
- 內部人交易：insider 回傳空值。ETF 無內部人持股申報概念，不適用。
- 機構持有人：inst_holders 與 major_holders 回傳空值，無法評估持有人集中度。

## Valuation（估值與淨值溢折價）
- 不適用 P/E、EV/EBITDA、P/FCF、P/S 等公司估值指標（epsTrailingTwelveMonths 為負且無 forwardPE）。
- 價格與淨值比：
  - 最新價 regularMarketPrice = 382.71 美元（10/15 收盤推定）；盤前 fast_info last_price = 380.83 美元（cnyes 來源，10/16 11:11 UTC）。
  - 淨值 navPrice = 374.84 美元（前一日淨值）。
  - 溢價 = 382.71 / 374.84 - 1 ≈ +2.10%。
  - 溢價為正且不大，顯示市價略高於實體黃金價值，屬常見區間；大幅溢價通常反映短期買盤集中，本資料無法確認。
- 技術位置（價格相對均線）：
  - 較 50 日均線 397.34 美元：約 -3.7%。
  - 較 200 日均線 415.06 美元：約 -7.8%。
  - 52 週區間 360.12 至 509.70 美元，位於區間約 25% 位置（由低點往上）。
  - 歷史高點 allTimeHigh = 509.70 美元，較現價回落約 25%。
- 風險特徵：beta3Year = 0.44，低於大盤相關性，但黃金價格波動本身仍高。

## Key catalysts（催化因子）
- 本工具未提供 ETF 財報或除息日（earnings_dates 查詢失敗）。GLD 無財報，不適用。
- 宏觀驅動（非來自資料工具，屬一般市場框架，需由總體分析師確認當期數據）：
  - 實質利率與美元走勢：通常與黃金價格負相關。
  - 央行黃金購買與地緣政治風險：支撐需求面。
  - 美國聯準會利率政策路徑與通膨數據。
- 信託本身事件：發行人 sponsor 或費用結構變更、保管安排變動，目前資料無顯示相關公告（corporateActions 為空）。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 最新價 (regularMarketPrice) | 382.71 美元 | n/a | 不適用 | 中性，低於 50/200 日均線 |
| 每股淨值 (navPrice) | 374.84 美元 | n/a | 不適用 | 作為估值基準 |
| 溢折價 (P/NAV) | +2.10%（約 1.02 倍） | n/a | 同類金屬 ETF 通常 ±0.5% 以內（估計） | 略溢價，可接受 |
| 淨資產 (netAssets) | 1,417 億美元 | n/a（單點） | 同類 ETF 規模差異大（估計） | 規模大、流動性充足 |
| 費用率 (netExpenseRatio) | 0.40% | n/a | 約 0.25%-0.40%（估計） | 偏高，但為主要黃金 ETF 常見區間 |
| 持倉集中度 | 100% 實體黃金 | n/a | 不適用 | 單一資產風險 |
| 槓桿 / 負債 | 無（資料未列） | n/a | 不適用 | 結構簡單 |
| 股利 (dividendYield) | 0% | n/a | 不適用 | 無配息 |
| 年初至今報酬 (ytdReturn) | -3.34% | n/a | 不適用 | 偏弱 |
| 3 年年化報酬 | 0.28% | n/a | 不適用 | 長期報酬低，費用拖累 |
| 5 年年化報酬 | 0.17% | n/a | 不適用 | 長期報酬低 |
| Beta (3Y) | 0.44 | n/a | 不適用 | 與大盤相關性低 |
| 價格 vs 50 日均線 | 約 -3.7% | n/a | 不適用 | 短期偏弱 |
| 價格 vs 200 日均線 | 約 -7.8% | n/a | 不適用 | 中期偏弱 |
| 52 週位置 | 高點下方約 25% | n/a | 不適用 | 處於區間中下部 |
| 10 日均量 | 7.49M 股（約 28.7 億美元） | n/a | 不適用 | 流動性充足，較 3M 均量縮量 |
| 申贖資金流 | n/a | n/a | n/a | 資料缺口 |
| 持倉金重 / 盎司 | n/a | n/a | n/a | 資料缺口 |
| 財務報表（損益、資產負債、現金流） | n/a | n/a | 不適用 | 信託不適用 |

## Red flags
- 資料缺口大：申贖資金流、持倉金重、AUM 歷史序列、機構持有人、財務報表與財報日期皆無法取得，無法做資金流向判斷。
- 股數與淨資產不一致：sharesOutstanding 260.3M 與 netAssets / navPrice 約 378.0M 差異約 45%，需以更新資料源核對。
- 價格來源不一致：info 的 regularMarketChangePercent 為 +1.79%，fulldayChangePercent 與 fast_info 數據為盤前數據（約 -0.78% 至 -0.8%），不宜混用解讀當日漲跌。
- bookValue 與 priceToBook 欄位與淨值脫鉤，不應用於估值。
- 績效偏弱：YTD -3.34%，價格低於 50 與 200 日均線，52 週高點回落約 25%；長期年化報酬接近零，費用率 0.40% 持續侵蝕持有報酬。
- 單一資產集中：100% 黃金，無分散化，報酬與金價高度綁定。
- 資料時點：本報告基於 2026-10-16 盤前快取，非 2026-10-17 當日資料，使用時需重新確認最新價與淨值。
- 工具環境：多數 Yahoo 端點於本次執行回傳 403 或連線錯誤（fast_info、financials、balance_sheet、earnings_dates、holders、insider），僅 info 與部分快取資料可用。

FUNDAMENTALS REPORT COMPLETE
