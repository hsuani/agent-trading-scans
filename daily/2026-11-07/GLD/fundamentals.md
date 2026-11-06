# Fundamentals — GLD (SPDR Gold Shares) as of 2026-11-07

本報告為商品信託 ETF，不是公司。依任務要求，「Revenue & profitability」改為標的與規模概況，「Cashflow & balance sheet」不適用。資料全部來自 repo 快取（`pipeline/tools/yf GLD info`、`fast_info`、`prices/GLD.csv`、`pipeline/tools/ta GLD snapshot`）。最新收盤價為 2026-11-05（USD 375.49），快取時間戳為 2026-11-06 14:09 UTC，未出現晚於 2026-11-07 的數據。

## Executive summary
GLD 為 100% 實體黃金持有的信託 ETF，費用率 0.40%，資產淨值（netAssets）約 USD 131.0B，規模大、流動性充足（10 日平均量 9.51M 股）。截至 2026-11-05 收盤價 375.49 較 NAV 約 -0.38% 折價，屬正常小幅折價範圍，但 NAV 時間戳未明確。技術面上價格位於 MA20 之上、MA50 與 MA200 之下，距 52 週高點 509.7 約 -26.3%，YTD 報酬 -9.46%，趨勢偏弱但短線動能中性（RSI14 50.2）。估值概念不適用（無 EPS、無 P/E），本報告不給交易建議。

## Revenue & profitability（不適用，改為標的與規模概況）
- 標的性質：信託持有金條（gold bars），依 `info.longBusinessSummary` 其目標為反映黃金現貨價格扣除費用後的表現。持倉集中度：100% 實體黃金，無衍生品、無股票部位。
- 管理人 / 基金家族：State Street Investment Management（`fundFamily`）。類別：Commodities Focused。交易所：NYSEArca（PCX）。
- 成立日：`fundInceptionDate` = 2004-11（由時間戳換算，約）。
- 規模：`totalAssets` = USD 131.01B（131,009,642,496）；`netAssets` = USD 131.01B。
- 年費率：`netExpenseRatio` = 0.40%。以 USD 131.0B 計，年化費用約 USD 0.52B（由 AUM × 費率換算，非 API 直接欄位）。
- 績效（快取欄位）：YTD -9.46%；3 個月 -2.91%；3 年平均報酬欄位值 0.2632、5 年平均報酬欄位值 0.1731（單位未於快取註明，疑為小數，未換算定稿）；3 年 Beta 0.47。
- 歷史價格區間：52 週 354.67–509.7；歷史最高（allTimeHigh）509.7，即 52 週高點；歷史最低欄位 41.02（應為早期未調整或拆股前數據，僅供參考）。

## Cashflow & balance sheet（不適用）
- 信託無營運現金流、無負債、無 EPS；`financials`、`balance_sheet`、`cashflow`、`quarterly_*` 工具回傳皆為空陣列 `[]`，無可用資料。
- `epsTrailingTwelveMonths` = -9.394 為快取欄位，對信託無意義（信託不以 EPS 計價），不採用。
- `bookValue` = 170.017、`priceToBook` = 2.21：信託以成本基礎記帳，帳面值與市價不可比，不採用。
- `yield` / `dividendYield` / `trailingAnnualDividendRate` = 0.0，GLD 不配息。

## Capital allocation & insider signal
- 資本配置（創建 / 贖回）：`sharesOutstanding` = 260.3M 股（快取欄位）。但以 `netAssets` ÷ NAV 推算約 347.6M 股，兩者不一致（見 Red flags），本報告不採用股數變化推論。
- 基金資金流（fund flow）：DATA_UNAVAILABLE。快取中無每日或每週申購 / 贖回數據，無法判斷近期資金是流入或流出。
- 內部人交易（insider）：`pipeline/tools/yf GLD insider` 回傳 Yahoo 連線錯誤（403 CONNECT 失敗），DATA_UNAVAILABLE。對 ETF 而言內部人交易本來意義有限，不影響判斷。
- 持有人結構：`major_holders` 與 `inst_holders` 皆回傳空陣列 `[]`，DATA_UNAVAILABLE。
- 公司治理、管理層（`companyOfficers`、`executiveTeam`）為空，不適用。

## Valuation
- 信託無 P/E、EV/EBITDA、P/FCF、P/S，不適用。快取的 `trailingPE`、`forwardPE` 無此欄位。
- 價格與 NAV 關係（主要估值指標）：
  - 市價（收盤 2026-11-05）：USD 375.49（`regularMarketPrice`，`fast_info.last_price` 為 375.51，差 0.02，屬報價時點差異）。
  - NAV：USD 376.91（`navPrice`，時間戳未於快取註明）。
  - 折溢價：375.49 ÷ 376.91 - 1 = **約 -0.38%（折價）**。
- 規模換算：`netAssets` USD 131.0B vs 股數 × NAV（260.3M × 376.91 ≈ USD 98.1B）不一致，見 Red flags。
- 相對估值（黃金 vs 同類）：同業費用率與折溢價的 sector median 無快取資料，標示 n/a，不估計。

## Key catalysts
- 財報：不適用（ETF 無財報）。`earnings_dates` 工具回傳錯誤，下一次事件日：DATA_UNAVAILABLE。
- 價格驅動（定性，無快取數值佐證）：實質利率、美元強弱、央行黃金購買、地緣政治避險需求，會直接影響 NAV。
- 價格動能（快取技術指標，截至 2026-11-05）：
  - 20 日均線 373.39（價格 +0.56% 高於）；50 日均線 385.96（價格 -2.71%）；200 日均線 411.64（價格 -8.78%）。
  - MACD -5.15、訊號線 -5.78、柱狀 +0.64（MACD 仍在零軸下方，柱狀剛轉正）。
  - RSI14 50.2；布林 %B 0.56；ATR14 6.63（約價格 1.77%）；20 日年化波動 25.6%。
  - 動能：1 個月 -0.10%、3 個月 -5.77%、6 個月 -13.02%、12 個月 +3.63%。
- 近期價格（prices/GLD.csv）：2026-10-30 收 355.78；11-02 收 361.65；11-03 收 359.26；11-04 收 372.49；11-05 收 375.49。
- 年比：2025-11-05 收 366.51，2026-11-05 收 375.49，YoY 約 +2.45%。

## Metrics table
單位：價格為 USD（每股）；AUM 為 USD B；費率為 %；其餘比率為 %。無 億 單位（本標的為美元計價，不涉及 TWD / KRW）。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 收盤價（USD，2026-11-05） | 375.49 | +2.45%（對 366.51） | n/a | 中性 |
| 前收盤（USD，2026-11-04） | 372.49 | n/a | n/a | 參考 |
| NAV（USD） | 376.91 | n/a | n/a | 時間戳未明 |
| 折溢價 | -0.38% | n/a | n/a | 小幅折價，屬正常 |
| 規模 netAssets（USD B） | 131.01 | n/a | n/a | 大型，流動性佳 |
| 規模 totalAssets（USD B） | 131.01 | n/a | n/a | 與 netAssets 一致 |
| 股數 sharesOutstanding（M 股） | 260.3 | n/a | n/a | 與 AUM/NAV 不一致，存疑 |
| 年費率（%） | 0.40 | n/a | n/a | 偏高（相對費率低的同類）；同類數據 n/a |
| 年化費用估算（USD B） | 約 0.52 | n/a | n/a | 由 AUM × 費率推算 |
| 3 年 Beta | 0.47 | n/a | n/a | 與股市相關性低 |
| YTD 報酬（%） | -9.46 | n/a | n/a | 偏弱 |
| 3 個月報酬（%） | -2.91 | n/a | n/a | 弱 |
| 6 個月動能（%） | -13.02 | n/a | n/a | 弱 |
| 12 個月動能（%） | +3.63 | n/a | n/a | 持平偏正 |
| 距 52 週高點（%） | -26.33 | n/a | n/a | 仍在修正區 |
| 距 52 週低點（%） | +5.87 | n/a | n/a | 接近低點區 |
| MA20 / MA50 / MA200（USD） | 373.39 / 385.96 / 411.64 | n/a | n/a | 站上 MA20、受壓於 MA50/200 |
| RSI14 | 50.2 | n/a | n/a | 中性 |
| MACD 柱狀 | +0.64 | n/a | n/a | 轉正，趨勢尚未確認 |
| BB %B | 0.56 | n/a | n/a | 中軸偏上 |
| ATR14（USD） | 6.63 | n/a | n/a | 約 1.77% 日波幅 |
| 20 日年化波動（%） | 25.6 | n/a | n/a | 中高 |
| 基金資金流 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | 無法判斷 |
| 內部人交易 | DATA_UNAVAILABLE | n/a | n/a | 不適用於 ETF |
| 持有人結構 | DATA_UNAVAILABLE（空陣列） | n/a | n/a | 無資料 |
| 下一事件日 | DATA_UNAVAILABLE | n/a | n/a | 無 |

## Red flags
- 股數與規模不一致：快取 `sharesOutstanding` 260.3M 股 × NAV 376.91 ≈ USD 98.1B，與 `netAssets` USD 131.0B 差約 34%。可能是股數欄位過期（fast_info 股數查詢失敗，有 "Yahoo web request for share count failed" 紀錄）或 AUM 欄位時點不同。在取得官方資料前，不應以單一數字做規模或申贖判斷。
- NAV 時間戳未知：`navPrice` 未標示日期，折價 -0.38% 的精確性受限。
- 資金流與持有人資料缺失：fund flow、insider、institutional holders 皆 DATA_UNAVAILABLE，無法驗證近期資金方向。
- 趨勢偏弱：價格低於 MA50（-2.71%）與 MA200（-8.78%），6 個月動能 -13.02%，距 52 週高點 -26.3%。
- 報價時點差：`fast_info.last_price` 375.51 與 `info.regularMarketPrice` 375.49 不同；`info` 另含 2026-11-06 盤前價 369.95，屬 2026-11-06 盤前資料（早於 DATE，但非收盤）。以 2026-11-05 收盤 375.49 為準。
- 費率 0.40%：對現貨黃金 ETF 屬於偏高水準，長期持有的拖累明顯（年化約 USD 0.52B）；同類費率數據 n/a，無法量化相對排名。
- 3 年平均報酬欄位單位未明（快取值 0.2632），不作為結論依據。

FUNDAMENTALS REPORT COMPLETE
