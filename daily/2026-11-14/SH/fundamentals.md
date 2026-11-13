# Fundamentals — SH (ProShares Short S&P500) as of 2026-11-14

> 資料截至 2026-11-13（yfinance info 快取 14:32 UTC，fast_info 快取 14:26 UTC），早於分析日期 2026-11-14，無超出日期的資料。

## Executive summary
SH 是 -1x 反向 S&P 500 ETF，不是營運公司，企業財務指標（營收、獲利、現金流、資產負債表、內部人交易、估值倍數）皆不適用，報告以基金規模、費用率、價格與流動性及追蹤結構為主。基金淨資產約 USD 950.36M，費用率 0.88%，3 年 beta -0.92，與 S&P 500 呈反向關係，作為對沖工具的功能符合定位。價格 USD 32.69 位於 200 日均線（USD 33.96）下方，但高於 50 日均線（USD 32.44），且 10 日平均成交量明顯高於 3 個月平均，短期交易活動升溫。

## Revenue & profitability
n/a。SH 為 ETF，無營收、毛利、營業利益或淨利報表。yfinance `financials` / `quarterly_fin` 回傳空陣列。`longBusinessSummary` 僅說明基金以金融工具（期貨、交換等）取得 S&P 500 反向報酬，每日目標報酬為 -1x，至少 80% 資產投入反向曝險。

Fund performance（yfinance info，均為報酬率）：
- YTD: -6.63%
- 3 個月（trailing）: -1.10%
- 52 週: -11.14%
- 3 年年化平均: -12.72%
- 5 年年化平均: -7.08%

## Cashflow & balance sheet
n/a。`cashflow`、`quarterly_cf`、`balance_sheet`、`quarterly_bs` 皆回傳空陣列，FCF、淨負債、流動比率、負債權益比等不適用於基金結構。可得的資產端指標只有淨資產（netAssets）USD 950.36M，與 totalAssets 相同。

## Capital allocation & insider signal
- 股息: info 顯示 yield 3.87%，屬基金配息，非公司回購或配息政策。corporateActions 為空。
- 回購 / 資本支出: n/a。
- 內部人交易: n/a。`insider` 回傳空陣列；ETF 無內部人申報。
- 持有人集中度: `major_holders` 與 `inst_holders` 皆為空陣列，無法取得機構持有比例或前幾大持有人。
- 基金流量（fund flows / creation-redemption）: n/a，工具未提供。
- 持倉結構（S&P 500 期貨/交換部位集中度）: 工具無持倉明細，僅能由 longBusinessSummary 推知基金以反向 S&P 500 指數曝險為主，無個股持倉集中度問題。

## Valuation
公司估值倍數（P/E、EV/EBITDA、P/FCF、P/S）皆不適用於 ETF，標示 n/a。可用的價格相關指標如下：
- 市價（regularMarketPrice）: USD 32.69（info）；fast_info last_price 為 USD 32.78（cnyes feed），兩來源相差約 0.3%，屬不同快取時點。
- 基金淨值（navPrice）: USD 32.7846 → 以 info 市價計算，折價約 -0.28%。
- 50 日均線 USD 32.44（市價高於約 +0.76%）；200 日均線 USD 33.96（市價低於約 -3.75%）。
- 52 週區間: USD 31.64 – 39.20；市價位於區間低段（距低點 +3.3%，距高點 -16.6%）。
- beta（3 年）: -0.92。
- 注意: allTimeHigh 843.52 與 allTimeLow 31.64 的歷史數值疑似未經除權/併股調整，與現價不可直接比較，不應用於判斷歷史位階。

## Key catalysts
- 下次財報: n/a（ETF 無財報）。`earnings_dates` 因連線被代理拒絕回傳錯誤，無法取得。
- 對 SH 影響較大的是 S&P 500 指數走勢本身與聯準會、總體經濟數據等，非 SH 公司事件；工具中無相關公告資料。
- 成交量: 今日成交 735,389 股，10 日平均 12,648,430 股，3 個月平均 9,094,990 股；10 日均量約為 3 個月均量的 1.39 倍，顯示近期交易活動升溫。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 淨資產 (netAssets, USD M) | 950.36 | n/a | n/a | 規模中等，流動性足夠 |
| 費用率 (netExpenseRatio) | 0.88% | n/a | n/a | 對反向 ETF 屬一般水準，持有成本偏高 |
| 股息殖利率 (yield) | 3.87% | n/a | n/a | 基金配息，非公司政策 |
| 3 年 beta | -0.92 | n/a | n/a | 與 S&P 500 強反向，符合定位 |
| YTD 報酬 | -6.63% | n/a | n/a | 年內表現偏弱（對 SH 而言即大盤上漲） |
| 52 週報酬 | -11.14% | n/a | n/a | 近一年負報酬 |
| 3 年年化平均報酬 | -12.72% | n/a | n/a | 長期結構性拖累（波動損耗與反向持有成本） |
| 價格 vs 200 日均線 | -3.75% | n/a | n/a | 位於長期均線下方 |
| 價格 vs 50 日均線 | +0.76% | n/a | n/a | 短期均線上方，短期偏穩 |
| 折溢價 (市價 vs NAV) | -0.28% | n/a | n/a | 接近淨值，無明顯折溢價 |
| 3 個月平均成交量 (股) | 9,094,990 | n/a | n/a | 流動性高 |
| 10 日平均成交量 (股) | 12,648,430 | 較 3 個月均量 +39% | n/a | 近期交易活動升溫 |
| 財報 / 內部人 / 持有人 / 基金流量 | n/a | n/a | n/a | 資料源無此欄位，不適用或未取得 |

## Red flags
- 結構性拖累: 3 年年化平均報酬 -12.72% 顯示反向 ETF 長期持有損耗明顯，不適合作為長期持有的基本面標的。
- 費用率 0.88% 加上每日重設的 -1x 曝險，長期持有與基準指數會出現偏離。
- 歷史價格資料（allTimeHigh 843.52）疑似未調整，不可用於歷史位階判斷。
- 資料缺口: 持有人、基金流量、財報與歷史財務報表皆無資料，本報告無法評估基金的實際持倉集中度與資金流向。
- 快取時點不一: info 與 fast_info 價格差約 0.3%，以最新即時資料為準。

FUNDAMENTALS REPORT COMPLETE
