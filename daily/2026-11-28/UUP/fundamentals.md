# Fundamentals — UUP as of 2026-11-28

## Executive summary
UUP 是 Invesco DB US Dollar Index Bullish Fund（美元指數多頭 ETF），不是operating company，因此不適用營收、利潤率、估值倍數等公司財務框架。截至 2026-11-27 的快照顯示基金規模約 $481.4M、費用率 0.75%、市價略高於 NAV（溢價約 +0.42%），價格位於 52 週高點附近（距高點 -0.42%）且站上 20/50/200 日均線，RSI14 為 67.6，技術面偏強但接近超買區。持有權重、資金流向與 AUM 歷史等關鍵資料工具未提供，無法確認基金內部部位與資金動向。

## Revenue & profitability
本節不適用。UUP 為 ETF，沒有營收、毛利、營業利益或淨利。基金的「經營結果」對應為淨值（NAV）表現與標的指數（DX，ICE US Dollar Index）的走勢：
- YTD 報酬：+7.13%（yfinance `ytdReturn`）
- 近三個月報酬：+3.02%（`trailingThreeMonthReturns`）
- 52 週報酬：+4.93%（`fiftyTwoWeekChangePercent`）
- 3 年平均年化報酬：+5.23%；5 年平均年化報酬：+5.74%（`threeYearAverageReturn` / `fiveYearAverageReturn`）
- 價格區間：52 週 26.40–29.84，歷史高點 30.76、歷史低點 20.84（`allTimeHigh` / `allTimeLow`）

「營收成長 CAGR、毛利率、ROE、ROIC」均為 n/a（不適用於 ETF）。

## Cashflow & balance sheet
本節不適用。ETF 沒有公司層級的現金流量表與資產負債表。yfinance 的 `financials` / `balance_sheet` / `cashflow` 回傳空陣列，這是 ETF 結構使然，不是資料缺漏。

基金層級的資產與負債以可得的快照數字表示：
- 淨資產（netAssets）：481,364,192 USD，約 $481.4M
- 基金為期貨部位結構（DX 期貨多頭），無債務槓桿報告欄位
- 期貨保證金、抵押品與現金配置：DATA_UNAVAILABLE

## Capital allocation & insider signal
- 股息：`trailingAnnualDividendRate` 與 `trailingAnnualDividendYield` 皆為 0.0，但 `yield` / `dividendYield` 欄位顯示 3.2%。兩者互相矛盾，且 UUP 為 DX 期貨多頭基金，理論上不以配息為主要報酬來源。此處不採用 3.2%，標示為資料不一致。
- 買回：不適用（ETF 不回購）。
- 內部人交易：不適用（ETF 無內部人）。`insider` 回傳空陣列。
- 持股人（major_holders / inst_holders）：回傳空陣列，DATA_UNAVAILABLE。
- 基金費用：費用率（netExpenseRatio）0.75%。以 AUM $481.4M 估算，年化費用約 $3.6M（0.75% × $481.4M，為推算值）。
- 資金流向（creations / redemptions）與 AUM 歷史：DATA_UNAVAILABLE。只有單日快照 AUM，無時間序列，無法判斷近期是淨申購還是淨贖回。
- 股數：yfinance 未提供 `sharesOutstanding`。以 netAssets / navPrice 推算約 16.27M 股（29.59 為 NAV 推算值，非工具直接輸出）。

## Valuation
本節不適用公司估值倍數（P/E、EV/EBITDA、P/FCF、P/S）。ETF 的估值對照方式為「市價 vs NAV」與「價格相對均線」：

- 市價（regularMarketPrice）：29.715 USD
- 淨值（navPrice）：29.59 USD（標示為工具回傳值，可能為前一交易日 NAV，未確認時點）
- 溢價：+0.42%（(29.715 / 29.59) − 1）。溢價幅度小，套利機制通常會維持在窄幅區間。
- Bid / Ask：29.71 / 29.72，價差約 0.03%，流動性尚可。
- 成交量：當日 349,097 股（盤中快照，不完整），10 日均量 1,809,400 股，3 月均量 1,703,015 股。當日量僅為均量的約 19%，原因可能是盤中時點未收盤，此數字不宜直接與均量比較。

技術面位置（來自 `ta snapshot`，as_of 2026-11-27）：
- 相對 MA20（29.350）：+1.24%
- 相對 MA50（29.068）：+2.22%
- 相對 MA200（28.155）：+5.54%
- 布林 %B：0.80；RSI14：67.6；MACD 柱狀體：+0.017（MACD 0.204 高於訊號線 0.187）
- ATR14：0.129 USD（約佔價格 0.43%）；20 日年化波動率：5.87%

## Key catalysts
- 下次財報：不適用（ETF 無財報）。`earnings_dates` 回傳工具錯誤。
- 宏觀催化因子（非工具輸出，屬定性說明）：美元指數受 Fed 利率路徑、美國與主要貿易夥伴的利差與經濟數據、地緣政治避險需求影響。這些是定性判斷，不含具體日期，工具未提供經濟日曆。
- 基金結構催化：DX 期貨滾倉（roll）與指數重新平衡會影響期貨曲線報酬，工具未提供滾倉時程。
- 資料時點提醒：本報告所有數字截至 2026-11-27，未使用 2026-11-28 之後的任何資料。

## Metrics table
單位說明：UUP 以 USD 計價，AUM 以 USD M 表示。本報告無 TWD 或 KRW 金額，不涉及 億 換算。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 市價 (USD) | 29.715 | 52 週報酬 +4.93% | n/a | 中性偏強 |
| 淨值 NAV (USD) | 29.59 | n/a | n/a | 時點未確認 |
| 溢價 / 折價 | +0.42% | n/a | n/a | 小幅溢價，正常 |
| 淨資產 AUM (USD M) | 481.4 | n/a（僅單點） | n/a | 規模中等，資金流 DATA_UNAVAILABLE |
| 費用率 Expense ratio | 0.75% | n/a | 同類 currency ETF 中位數 n/a | 偏高，屬主動期貨型結構 |
| YTD 報酬 | +7.13% | n/a | n/a | 強勢 |
| 3 個月報酬 | +3.02% | n/a | n/a | 正向 |
| 3 年平均年化報酬 | +5.23% | n/a | n/a | 正向 |
| 5 年平均年化報酬 | +5.74% | n/a | n/a | 正向 |
| 距 52 週高點 | -0.42% | n/a | n/a | 接近高點 |
| 距 52 週低點 | +12.56% | n/a | n/a | 區間上段 |
| 相對 MA200 | +5.54% | n/a | n/a | 長期趨勢向上 |
| RSI14 | 67.6 | n/a | n/a | 接近超買，留意 |
| 布林 %B | 0.80 | n/a | n/a | 偏上軌 |
| ATR14 (USD) | 0.129 | n/a | n/a | 日內波動約 0.43% |
| 20 日年化波動率 | 5.87% | n/a | n/a | 低波動 |
| 10 日均量（股） | 1,809,400 | n/a | n/a | 流動性充足 |
| Bid / Ask spread | 0.03% | n/a | n/a | 價差窄 |
| 股息率（yield 欄位） | 3.2% | n/a | n/a | 與 trailing 股息 0 矛盾，不採用 |
| Beta (3Y) | -7.93 | n/a | n/a | 異常值，不可採用 |
| 持股權重 / 期貨部位 | DATA_UNAVAILABLE | n/a | n/a | 無法評估 |
| 資金流向 / AUM 歷史 | DATA_UNAVAILABLE | n/a | n/a | 無法評估 |
| 財報 / 估值倍數 | 不適用 | n/a | n/a | ETF 不適用 |

## Red flags
- Beta (3Y) 為 -7.93，明顯不合理，系統不應使用此數字做風險計算。
- 殖利率資料矛盾：yield 欄位 3.2%，但 trailing 股息為 0。
- 持股權重、期貨部位組成、資金流向、AUM 時間序列全部 DATA_UNAVAILABLE，無法確認基金實際部位或申贖動態。
- 目前價格與 RSI14（67.6）接近超買區，短線回檔風險需留意（僅為技術面觀察，不構成交易建議）。
- 當日成交量為盤中不完整資料，不可直接與均量比較。
- 工具大量使用 repo cache（Yahoo 連線 403），`fast_info` 的價格來自 cnyes feed 快取。價格與 `info` 吻合（29.715），但 NAV 時點不明。
- 基金費用率 0.75% 偏高，長期持有時會侵蝕報酬。
- 溢價 +0.42% 雖小，但 NAV 來源時點未確認，實際溢價可能與快照有偏差。
- 歷史 CAGR 與 YoY 欄位對 ETF 的意義有限，表中已標示為 n/a。

FUNDAMENTALS REPORT COMPLETE
