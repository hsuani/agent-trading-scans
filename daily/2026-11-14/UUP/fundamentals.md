# Fundamentals — UUP as of 2026-11-14

> 注意：UUP 為 Invesco DB US Dollar Index Bullish Fund（ETF，非營運公司）。本報告不含營收、獲利率、分部、EPS、內部人交易等公司財務指標，相關欄位一律標示 n/a。資料時間點為工具快取 2026-11-13 約 14:30 UTC，未見晚於 2026-11-14 的資料。

## Executive summary
UUP 是追蹤美元指數（DX 期貨多頭）的被動式商品型 ETF，費用率 0.75%，淨資產約 4.81 億 USD（481,364,192 USD），股價 29.4339 USD 逼近 52 週高點 29.4482，YTD 報酬 +7.13%。此檔不適用公司型估值（P/E、EV/EBITDA、P/FCF），僅能以 NAV 溢價、均線位置與流動性評估。資料缺口多（持股明細、資金流、歷史財報類欄位皆因 Yahoo 連線被 proxy 403 而取不到），結論需保守看待。

## Revenue & profitability
- 營收、毛利率、營業利益率、淨利率、ROE、ROIC：**n/a**（ETF 無營運損益表；yfinance `financials` 回傳連線錯誤，且此類欄位對基金無意義）。
- 基金層級的對應指標為「報酬表現」：
  - YTD 報酬：+7.13%（`ytdReturn` 7.12966）
  - 近 3 個月：+3.02%（`trailingThreeMonthReturns` 3.01954）
  - 近 52 週：+4.66%（`fiftyTwoWeekChangePercent` 4.6602607）
  - 3 年年化平均報酬：+4.19%（`threeYearAverageReturn` 0.0418642）
  - 5 年年化平均報酬：+5.92%（`fiveYearAverageReturn` 0.059244）
- 價格區間：52 週 26.40–29.4482 USD；歷史最高 30.76、歷史最低 20.84 USD。

## Cashflow & balance sheet
- FCF、淨負債、流動比率、負債權益比、現金部位：**n/a**（基金無自由現金流與資產負債表概念；`balance_sheet` / `cashflow` 工具取得失敗）。
- 基金的「資產負債」對應項目為淨資產與期貨部位：
  - 淨資產（netAssets）：481,364,192 USD（約 481.4M USD）
  - 持股明細（USD 期貨多頭 vs 六種籃子貨幣）：**工具未提供，n/a**。下列為 Invesco 公開規格中的歷史權重，僅供參考，未經本次工具驗證：歐元約 57.6%、日圓約 13.6%、英鎊約 11.9%、加幣約 9.1%、瑞典克朗約 4.2%、瑞士法郎約 3.6%。實際權重請以 Invesco 當期持股報表為準。
- 集中度判讀：若上述權重仍成立，UUP 報酬高度集中於歐元（約 58%），實質上是「做多美元 vs 歐元」的單邊曝險。

## Capital allocation & insider signal
- 資本支出、買回、股利覆蓋率：**n/a**（ETF 不做資本配置，不回購股票）。
- 配息：yield 欄位為 3.2%（`dividendYield` 3.2、`yield` 0.032），但 `trailingAnnualDividendRate` 與 `trailingAnnualDividendYield` 皆為 0.0，兩者互相矛盾，**疑為資料異常，未採用**；需以 Invesco 配息公告核對。
- 內部人交易（insider）：**n/a**。ETF 無內部人申報制度；`insider` 工具取得失敗。
- 機構持股（`inst_holders`、`major_holders`）：工具回傳空陣列，**n/a**。
- 資金流（creation/redemption、淨申購）：工具未提供，**n/a**。可由 AUM 與 shares 變化推估，但本次無股數資料，無法推估。

## Valuation
- P/E、Forward P/E、EV/EBITDA、P/FCF、P/S：**n/a**（ETF 無盈餘與營收）。
- 可用的估值概念為 **NAV 溢價/折價**：
  - 市價 29.4339 USD（`regularMarketPrice`），NAV 29.34 USD（`navPrice`）
  - 溢價 = (29.4339 − 29.34) / 29.34 ≈ **+0.32%**，屬正常範圍，無明顯折溢價。
  - 注意：`navPrice` 為快取值，時間點可能與市價不同步。
- 技術位置（價格相對均線）：
  - 50 日均線 28.771（`fiftyDayAverage`），市價高於約 +2.3%（`fiftyDayAverageChangePercent` 0.0230）
  - 200 日均線 28.018（`twoHundredDayAverage`），市價高於約 +5.1%（`twoHundredDayAverageChangePercent` 0.0505）
  - 市價距 52 週高點僅 −0.05%，處於區間頂部。
- Beta：`beta3Year` 為 −7.93，**數值明顯異常**（一般美元指數 ETF 對 S&P 500 的 beta 不會達到此量級），疑為資料錯誤，不採用。
- 費用率：0.75%（`netExpenseRatio`），為 UUP 之固定成本，會持續拖累報酬。

## Key catalysts
- 下次財報：**n/a**（ETF 無財報；`earnings_dates` 取得失敗）。
- 驅動因子為宏觀面而非公司面，無法由本工具取得具體事件日期。一般影響 DXY 的因素包括：Fed 利率決議與點陣圖、美國與歐元區 / 日本通膨與央行政策分歧、美國公債殖利率、地緣政治避險需求。這些為一般性分析框架，非本次工具數據。
- 流動性：10 日平均量 1,492,560 股、3 個月平均量 1,547,181 股；報告快照當日成交量 38,939 股（盤中或快取截點，不具代表性）。

## Metrics table
| Metric | Latest（USD / %） | YoY / 區間 | 同類基準（估計） | Verdict |
|---|---|---|---|---|
| 股價 | 29.4339 | 52 週 26.40–29.4482 | n/a | 接近 52 週高點 |
| 淨資產 NAV | 29.34 | n/a | n/a | 與市價差 +0.32%，正常 |
| 淨資產規模 AUM（netAssets） | 481.4M USD | n/a（無歷史序列） | n/a | 中小型 ETF，流動性尚可 |
| 費用率 | 0.75% | n/a | 美元指數類 ETF 約 0.3–0.8%（估計） | 偏高但屬同類常態 |
| YTD 報酬 | +7.13% | — | n/a | 強勢 |
| 近 3 個月報酬 | +3.02% | — | n/a | 偏多 |
| 近 52 週報酬 | +4.66% | — | n/a | 正報酬 |
| 3 年年化報酬 | +4.19% | — | n/a | 正報酬 |
| 5 年年化報酬 | +5.92% | — | n/a | 正報酬 |
| 股價 vs 50 日均線 | +2.3% | — | n/a | 短中期趨勢偏多 |
| 股價 vs 200 日均線 | +5.1% | — | n/a | 長期趨勢偏多 |
| 股利殖利率 | 3.2%（yield 欄位） | 近 12 月配息 0.0（矛盾） | n/a | 資料異常，待核對 |
| Beta（3 年） | −7.93 | — | n/a | 資料異常，不採用 |
| 10 日平均量 | 1,492,560 股 | 3M 平均 1,547,181 股 | n/a | 流動性尚可 |
| 持股集中度（歐元權重） | 約 57.6%（歷史規格，未驗證） | n/a | n/a | 單一貨幣集中，需以當期持股確認 |
| P/E、EV/EBITDA、P/FCF、P/S | n/a | n/a | n/a | 不適用 ETF |
| 內部人交易、資金流 | n/a | n/a | n/a | 工具未提供 |

## Red flags
- 資料完整度低：持股明細、資金流、財報類、內部人、機構持股、歷史 AUM 序列皆無法取得（Yahoo 連線 403），本報告大量欄位為 n/a。
- `beta3Year` −7.93 明顯異常，不可用於風險建模。
- 配息欄位內部矛盾（殖利率 3.2% vs 近 12 月配息 0.0），需以 Invesco 公告核對。
- 價格貼近 52 週高點且 YTD +7.13%、位於 50/200 日均線之上，短線已有相當漲幅；若美元走弱，UUP 將直接承受回檔，單邊風險集中。
- 歐元權重高（歷史規格約 58%），歐元區政策或歐元反彈即會快速拖累 UUP。
- 費用率 0.75% 與無配息的組合，長期報酬需持續超過成本才能維持正報酬。
- 快照成交量 38,939 股遠低於 10 日平均，屬盤中或快取截點數據，不應解讀為流動性枯竭。

FUNDAMENTALS REPORT COMPLETE
