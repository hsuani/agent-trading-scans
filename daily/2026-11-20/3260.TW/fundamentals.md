# Fundamentals — 3260.TW (威剛) as of 2026-11-20

**資料狀態：DATA_UNAVAILABLE。本次無法完成基本面判斷。** yfinance 的財務三表、季報、財報日期、內部人交易、股東結構、市值與股本全部回傳空值或連線被拒（curl 7，CONNECT tunnel failed，response 403）。`info` 只回傳 cache 且僅含 `trailingPegRatio: null`。`fast_info` 僅提供價格（feed: cnyes，source: cache），`fifty_day_average` 與 `two_hundred_day_average` 為 null。本報告不沿用 2026-11-05 或其他日期報告的任何基本面數字。

## Executive summary
本次 yfinance 財務資料全部缺失，無法判斷威剛的營收、獲利、現金流、資產負債與估值，財務健康度與估值吸引力均為 n/a。價格面已明顯轉弱：2026-11-20 收盤 234.0 TWD，前收 254.0，較 2026-03-19 歷史高點 525.0 回落約 55.4%，近 60 個交易日報酬約 -44.6%。在財報資料補齊前，不應把價格下跌解讀為基本面變化。

## Revenue & profitability
DATA_UNAVAILABLE。`financials` 與 `quarterly_fin` 皆回傳空陣列，無營收、毛利、營業利益、淨利、ROE、ROIC 數據，無法計算 3-5 年 CAGR、YoY 或利潤率趨勢。`info.longBusinessSummary` 未取得，無法拆解產品或區域營收組合。

## Cashflow & balance sheet
DATA_UNAVAILABLE。`cashflow`、`quarterly_cf`、`balance_sheet`、`quarterly_bs` 皆為空，無法計算 FCF margin、FCF/NI、淨負債、流動比率、負債權益比或現金部位。

## Capital allocation & insider signal
- 內部人交易（`insider`）：空陣列，淨買賣金額與占市值比例 n/a。
- 股東結構（`major_holders`、`inst_holders`）：空陣列，n/a。
- 資本支出、買回、股利覆蓋：財務報表缺失，n/a。
- 市值與股本：`market_cap`、`shares` 為 null，n/a。

## Valuation
- trailing / forward P/E、EV/EBITDA、P/FCF、P/S 皆 n/a（缺 EPS、EBITDA、FCF、股本）。
- 無法與產業中位數比較，sector median 標示 n/a。
- 價格結構（來自 `prices/3260.TW.csv` 本地序列，共 334 筆，2025-07-08 至 2026-11-20，與 fast_info 收盤一致）：MA20 306.6 TWD、MA50 349.9 TWD、MA200 379.8 TWD。收盤位於三條均線下方，均線呈空頭排列。此為技術面資訊，不能換算為估值水準。

## Key catalysts
- 下次財報日期（`earnings_dates`）：連線被拒（403），n/a。
- 近期 guidance、法說或產品資訊：本次無可用資料，n/a。
- 價格事件（非基本面催化劑）：近 5 / 20 / 60 / 120 日報酬分別為 -22.5% / -29.6% / -44.6% / -43.3%。2026-11-20 單日由 254.0 跌至 234.0（-7.9%），當日區間 234–250。

## Metrics table
| Metric（單位） | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收（TWD 億） | n/a | n/a | n/a | DATA_UNAVAILABLE |
| 毛利率（%） | n/a | n/a | n/a | DATA_UNAVAILABLE |
| 營業利益率（%） | n/a | n/a | n/a | DATA_UNAVAILABLE |
| 淨利率（%） | n/a | n/a | n/a | DATA_UNAVAILABLE |
| ROE / ROIC（%） | n/a | n/a | n/a | DATA_UNAVAILABLE |
| FCF margin / FCF÷NI | n/a | n/a | n/a | DATA_UNAVAILABLE |
| 淨負債（TWD 億） | n/a | n/a | n/a | DATA_UNAVAILABLE |
| 流動比率 / 負債權益比 | n/a | n/a | n/a | DATA_UNAVAILABLE |
| 市值（TWD 億） | n/a | n/a | n/a | DATA_UNAVAILABLE |
| Trailing / Forward P/E | n/a | n/a | n/a | DATA_UNAVAILABLE |
| EV/EBITDA、P/FCF、P/S | n/a | n/a | n/a | DATA_UNAVAILABLE |
| 內部人淨買賣（6 個月） | n/a | n/a | n/a | DATA_UNAVAILABLE |
| 收盤價（TWD） | 234.0（2026-11-20） | 近 120 日 -43.3% | n/a | 價格資料可用 |
| MA20 / MA50 / MA200（TWD，自算） | 306.6 / 349.9 / 379.8 | n/a | n/a | 股價位於三線下方 |
| 距歷史高點 525.0（2026-03-19） | -55.4% | n/a | n/a | 技術面弱勢 |

## Red flags
- 財務三表、季報、EPS、現金流、資產負債表、內部人與股東資料全部缺失，基本面結論無法成立。
- yfinance 對 3260.TW 的 CONNECT 連線遭 403 拒絕，`info` 與 `fast_info` 為 cache 回傳，市值、股本、52 週高低與 MA 欄位為 null。
- 價格 3 個月內由 525.0 跌至 234.0，近 60 日報酬 -44.6%，均線空頭排列。這是技術面與情緒風險，不是基本面證據。
- 資料時點：分析 as-of 2026-11-20，價格 cache 於 2026-11-20 02:37 UTC 更新，未見超出 as-of 的資料。
- 補救建議：修復 yfinance 對 3260.TW 的連線（或改用其他可用來源）後重跑，優先補齊三表、`earnings_dates`、`insider`。

FUNDAMENTALS REPORT COMPLETE
