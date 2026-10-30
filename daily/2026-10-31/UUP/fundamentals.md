# Fundamentals — UUP (Invesco DB US Dollar Index Bullish Fund) as of 2026-10-31

> 資料時點注意：本次工具回傳皆為 repo 快取（`"source": "cache"`，快取時間 2026-10-30 12:45 UTC），最新行情對應 2026-10-29 收盤（ta snapshot `as_of` 為 2026-10-29）。分析基準日為 2026-10-31，故價格資料落後分析日約一個交易日，未包含 2026-10-30 之後的任何數據。Yahoo 財務報表、持股、內部人交易等端點全數以 403 / 空陣列回傳，視為 DATA_UNAVAILABLE。

## Executive summary

UUP 為 Invesco 發行的美元指數多頭期貨型 ETF，追蹤 DX 期貨（long 美元指數），本身不是營運公司，無法以營收、獲利、自由現金流或資產負債表評估財務健康度；本報告改以基金結構、費用率、規模、淨值溢折價與價格技術面為主要觀察。截至 2026-10-29 快取資料，價格 29.04 USD 與淨值 navPrice 29.04 USD 幾乎一致（溢折價約 0%），年初至今報酬 +6.28%，價格位於 52 週區間上緣（距 52 週高點 -0.72%），RSI14 為 59.1，MACD 柱狀體為負，短線動能偏中性偏多。淨費用率 0.75%，淨資產約 4.31 億 USD，規模偏小，流動性尚可但非頂級；估值概念不適用於本標的。

## Revenue & profitability（不適用，改為標的與規模概況）

本節不適用於 ETF 本體，改列標的結構與規模資訊。

- 基金全名：Invesco DB US Dollar Index Bullish Fund（NYSE Arca，代碼 UUP，交易所代碼 PCX）。
- 基金類型：Exchange Traded Fund，category 為 `Trading--Miscellaneous`，發行商 Invesco。
- 投資標的：工具回傳的 longBusinessSummary 指出「投資於期貨合約以追蹤指數，指數反映 DX 合約多頭部位之市值變化」。成分細節（如六種貨幣權重）工具未回傳，本報告不列數字。
- 成立時間：fundInceptionDate 對應約 2007 年 2 月，firstTradeDate 對應約 2007 年 3 月。
- 規模：netAssets / totalAssets 皆為 431,136,608 USD，即約 431.1M USD（4.31 億 USD 量級，以 USD M 表示）。
- 規模趨勢（YoY）：工具未提供歷史 AUM 序列，YoY 為 DATA_UNAVAILABLE。
- 報酬紀錄：ytdReturn 6.28%；trailingThreeMonthReturns 1.27%；threeYearAverageReturn 約 3.69%；fiveYearAverageReturn 約 6.12%（欄位為小數換算，已依慣例換成百分比）。
- 歷史極值：allTimeHigh 30.76 USD，allTimeLow 20.84 USD；52 週 26.40–29.25 USD。

## Cashflow & balance sheet（不適用）

ETF 不以自由現金流或資產負債表衡量。工具回傳：

- financials、balance_sheet、cashflow、quarterly_fin、quarterly_bs、quarterly_cf：皆回傳空陣列 `[]`，視為 DATA_UNAVAILABLE。
- 基金層級的槓桿、期貨保證金與抵押品（collateral）狀況工具未回傳，DATA_UNAVAILABLE。
- 唯一與資金相關的數字為淨資產 431.1M USD 與淨費用率 0.75%（費用由基金淨值內扣除）。

## Capital allocation & insider signal

- 分配（distribution）：yield 欄位為 3.22%，dividendYield 欄位同為 3.22，但 trailingAnnualDividendRate 與 trailingAnnualDividendYield 皆為 0.0。兩組數據互相矛盾，本報告不採信 3.22% 作為確定配息率，標註為資料不一致，配息歷史 DATA_UNAVAILABLE。
- 買回 / 增減資：ETF 不適用；shares outstanding 工具回傳 null，無法驗證規模是否因申購贖回變動，DATA_UNAVAILABLE。
- 內部人交易（insider）：Yahoo 端點 403，回傳 `[]`。依規定不視為「無內部人交易」，標註為 DATA_UNAVAILABLE。本標的亦無公司管理層，companyOfficers 與 executiveTeam 皆為空陣列，內部人概念本身不適用。
- 機構持股（inst_holders）與大股東（major_holders）：分別回傳 `[]` 與 CONNECT 403 錯誤，DATA_UNAVAILABLE。
- 成交量流向：當日成交量 1,413,586 股，10 日平均 1,491,360 股，3 個月平均 1,626,026 股，當日量低於近期均量，無明顯放量訊號。

## Valuation

ETF 不適用本益比、EV/EBITDA、P/FCF、P/S 等公司估值指標。以下改列價格相對淨值與技術位置：

- 市價（regularMarketPrice）：29.04 USD；前收 29.06 USD；當日區間 29.01–29.125 USD，當日變動 -0.07%（-0.02 USD）。
- 淨值（navPrice）：29.04 USD；市價相對淨值溢折價約 0.00%（以快取 navPrice 計算），屬正常範圍。注意 navPrice 為快取時點數值，非盤中即時 iNAV，不能代表 2026-10-31 當日溢折價。
- 買賣價差：bid 28.91 / ask 28.98，價差 0.07 USD（約 0.24%，以中間價 28.945 計）。中間價相對淨值約 -0.3%，此為快取 bid/ask 且市場狀態為 PRE，僅供參考。
- 價格相對均線：相對 20 日均線（28.996）+0.15%；相對 50 日均線（28.563）+1.67%；相對 200 日均線（27.917）+4.02%。
- 52 週位置：距高點 -0.72%，距低點 +10.00%，位於區間上緣。
- 技術面（ta snapshot，as_of 2026-10-29）：RSI14 = 59.13；MACD = 0.117、Signal = 0.137、柱狀體 = -0.020（動能略弱化）；BB %B = 0.645（布林中上軌之間）；ATR14 = 0.115 USD（約 0.40% 價格，波動低）；20 日年化波動率 4.73%。
- 動能：1 個月 +0.94%、3 個月 +3.09%、6 個月 +6.14%、12 個月 +4.24%。
- Beta：beta3Year 回傳 -11.39，數值明顯不合理（非典型區間），本報告不採用，DATA_UNAVAILABLE。
- 同類中位數（sector median）：ETF 不具同類估值中位數，本報告不估計。

## Key catalysts

- 下一次財報：不適用（ETF 無財報）。earnings_dates 回傳 `[]`。
- 關鍵驅動因子：UUP 價格主要反映 DX 指數（美元對歐元、日圓、英鎊、加幣、瑞典克朗、瑞士法郎等）的變化。本報告未收錄 2026 年的利率、通膨、央行政策或地緣政治數據，故不列具體事件日期；交由宏觀與總經分析師補充。
- 基金層級事件：工具未回傳 corporateActions（回傳為空陣列），無分配、分割或管理變更公告。
- 資料時點風險：快取資料可能缺漏 2026-10-30 以後的美元指數走勢與 Fed 相關事件，使用者於決策前應以即時資料覆核。

## Metrics table

| Metric | Latest | YoY | 同類中位數（估計） | Verdict |
|---|---|---|---|---|
| 市價（USD） | 29.04 | n/a（無歷史序列） | 不適用 | 中性 |
| 淨值 navPrice（USD） | 29.04 | n/a | 不適用 | 中性 |
| 市價溢折價（快取） | ≈ 0.00% | n/a | 不適用 | 正常 |
| 淨資產 netAssets（USD M） | 431.1 | DATA_UNAVAILABLE | 不適用 | 規模偏小 |
| 淨費用率（netExpenseRatio） | 0.75% | n/a | 不適用（工具未提供同類費率） | 中性偏高（DX 類 ETF 常見區間，需與同類比較，本表不估計） |
| 年初至今報酬（ytdReturn） | +6.28% | n/a | 不適用 | 正向 |
| 3 個月報酬 | +1.27% | n/a | 不適用 | 正向 |
| 3 年平均報酬 | ≈ 3.69% | n/a | 不適用 | 正向 |
| 5 年平均報酬 | ≈ 6.12% | n/a | 不適用 | 正向 |
| 52 週位置（距高點） | -0.72% | n/a | 不適用 | 接近高點 |
| 相對 200 日均線 | +4.02% | n/a | 不適用 | 中長期偏多 |
| RSI14 | 59.13 | n/a | 不適用 | 中性偏多 |
| MACD 柱狀體 | -0.0197 | n/a | 不適用 | 動能弱化 |
| BB %B | 0.645 | n/a | 不適用 | 中性 |
| ATR14（USD / %） | 0.115 / ≈0.40% | n/a | 不適用 | 低波動 |
| 20 日年化波動率 | 4.73% | n/a | 不適用 | 低 |
| 當日成交量 / 10 日均量 | 1.41M / 1.49M 股 | n/a | 不適用 | 中性 |
| 殖利率（yield） | 3.22%（與 trailing 配息 0 矛盾） | n/a | 不適用 | 資料不一致，不採信 |
| 財務報表（營收 / 獲利 / 現金流 / 負債） | DATA_UNAVAILABLE | n/a | 不適用 | 不適用 |
| 內部人交易 | DATA_UNAVAILABLE | n/a | 不適用 | 不適用 |
| 機構 / 大股東持股 | DATA_UNAVAILABLE | n/a | 不適用 | 不適用 |
| Beta（beta3Year） | -11.39（數值不合理） | n/a | 不適用 | 不採用 |

## Red flags

- 資料時點落後：快取資料為 2026-10-29 收盤，分析基準日為 2026-10-31，兩日之間的美元走勢未納入。
- 財務與持股端點全數 403 或空陣列：營收、獲利、現金流、負債、內部人與機構持股均為 DATA_UNAVAILABLE，無法做完整基本面檢核。
- 配息資料矛盾：yield 3.22% 與 trailingAnnualDividendRate 0.0 不一致，不應以 3.22% 作為報酬假設。
- beta3Year 回傳 -11.39，數值異常，不應用於風險或相關性判斷。
- 規模偏小：淨資產約 4.31 億 USD，若遇大額贖回或價差擴大，流動性與跟蹤誤差風險相對較高。
- 費用率 0.75%：長期持有的拖累效應需與替代標的（如其他美元多空工具或直接期貨部位）比較，本報告未取得同類費率。
- 價格接近 52 週高點（-0.72%）且 MACD 柱狀體為負，短線動能有轉弱跡象，但 RSI 尚未過熱。
- 市場狀態為 PRE，bid/ask 與 fulldayPrice（28.96）與 regularMarketPrice（29.04）並存，部分欄位不一致，建議交易前以即時報價覆核。

FUNDAMENTALS REPORT COMPLETE
