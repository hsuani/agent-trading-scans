# Fundamentals — 3260.TW (威剛) as of 2026-10-22

## Executive summary
威剛為記憶體模組/SSD品牌商,屬記憶體供應鏈下游,yfinance對此檔的財務資料覆蓋極薄(`info`/`financials`/`rec_summary`/`insider`等多數欄位回傳空值),無法依標準化數據驗證獲利結構;依WebSearch取得之公開營收公告,2026年營收呈現數倍年增,但公開市場目標價分歧極大(200–556元)反映法人對其獲利延續性信心不一。整體財務健康度評等:資料不足,無法給出標準化評等;估值吸引力:無法由工具驗證。

## Revenue & profitability
- yfinance `financials`、`quarterly_fin`、`cashflow`、`balance_sheet`查詢均回傳空陣列([]),`info`欄位僅含`trailingPegRatio: null`,無P/E、營收、毛利率等任何標準化數據可供引用 — 為四檔標的中覆蓋度最薄弱者,此為台股中小型模組廠於yfinance常見的資料缺口,非公司基本面本身的負面訊號。
- 依WebSearch取得之公開法說/月營收公告(非yfinance工具產出,僅供news/sentiment脈絡參考,不計入本節標準化指標):2025年EPS達23.18元創歷史新高;2026年1月單月歸屬母公司淨利年增達3516倍(低基期效應);2026年4月營收年增約170%;2026年6月單月營收146.61億元(月增13.3%、年增212.1%),上半年累計營收642.72億元(年增183.3%)。
- 由於上述數字並非來自標準化財務工具,本報告對其真實性與計算口徑不做背書,僅作為方向性參考;正式營收成長率判定以「n/a(工具無資料)」處理。

## Cashflow & balance sheet
- n/a — yfinance `cashflow`、`balance_sheet`查詢均為空,FCF、Debt/Equity、Current Ratio等指標皆無法由工具驗證。

## Capital allocation & insider signal
- n/a — `insider`、`major_holders`查詢皆為空陣列,無內部人持股比例或買賣超資料。
- WebSearch提及公司於2026年初宣布實施庫藏股4,000張(非yfinance驗證數字,僅供參考)。

## Valuation
- n/a — yfinance `info`無trailingPE、forwardPE、targetMeanPrice等任何估值欄位(僅剩`trailingPegRatio: null`),無法由工具計算本益比或法人目標價隱含空間。
- WebSearch顯示法人目標價分歧極大:2025年11月某券商下修評等至「Trading Buy」、目標價砍至200元(原297.5元);另有2026年5月報告給予「買進」評等、目標價556元。此分歧本身即為風險訊號,顯示市場對其獲利能見度看法不一。

## Key catalysts
- 財報日:yfinance `earnings_dates`查詢回傳空值,無下次財報日資料,標記n/a。
- 產業面:若記憶體模組報價維持強勢(DRAM/NAND現貨價格上行),威剛作為下游品牌商可望受惠終端拉貨;但模組廠毛利結構上游原物料(DRAM顆粒、NAND晶圓)成本占比高,若上游漲價速度快於終端售價調整,存在毛利率被壓縮風險。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收成長 | n/a(工具無資料) | n/a | n/a | 資料不足 |
| 毛利率 | n/a | n/a | n/a | 資料不足 |
| FCF/NI | n/a | n/a | n/a | 資料不足 |
| Debt/Equity | n/a | n/a | n/a | 資料不足 |
| Trailing P/E | n/a | n/a | n/a | 資料不足 |
| Forward P/E | n/a | n/a | n/a | 資料不足 |
| 分析師買進比例 | n/a(rec_summary為空) | n/a | n/a | 資料不足 |

## Red flags
- yfinance標準化財務數據全面缺失(financials/cashflow/balance_sheet/rec_summary/insider皆為空),無法依本框架的量化指標對其財務健康度進行驗證式評等 — 這本身就是對position sizing的一個重要限制因素,須在交易員與風控階段特別註記。
- 公開市場法人目標價分歧達178%(200元至556元區間),顯示市場對其獲利能見度缺乏共識。
- 模組廠商業模式使其利潤率對上游DRAM/NAND顆粒採購成本波動較為敏感,屬於記憶體供應鏈中相對薄弱的一環。

FUNDAMENTALS REPORT COMPLETE
