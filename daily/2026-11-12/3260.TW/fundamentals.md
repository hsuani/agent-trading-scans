# Fundamentals — 3260.TW (威剛) as of 2026-11-12

## Executive summary
DATA_UNAVAILABLE：本次以 `pipeline/tools/yf` 重新呼叫 info、fast_info、財務三表、季報、EPS 公告、內部人交易與股東資料，Yahoo 連線全部遭 403 拒絕（CONNECT tunnel），repo cache `prices/yf/3260.TW.json` 的財務相關欄位亦皆為空陣列，僅 fast_info 有價格。因此財務健康度與估值吸引力**無法判斷**，所有 P/E、EV/EBITDA、P/FCF、P/S、ROE、FCF、負債等指標皆為 n/a。可確認的事實僅限價格結構：最新收盤 304.0 TWD（2026-11-11），前收 304.5，近 5 個交易日在 295–323 區間整理，較 repo 技術快照所列 52 週高點 525.00 回落約 42%。基本面結論需待財務資料補齊後重跑。

## Revenue & profitability
DATA_UNAVAILABLE。`financials`、`quarterly_fin` 皆回傳空陣列，無營收、毛利、營業利益、淨利、ROE、ROIC，無法計算 3-5 年 CAGR、YoY 或 margin 趨勢。`info.longBusinessSummary` 未取得，無法拆解產品（DRAM 模組、NAND 儲存等）或地區營收組合，此段皆 n/a。

## Cashflow & balance sheet
DATA_UNAVAILABLE。`cashflow`、`quarterly_cf`、`balance_sheet`、`quarterly_bs` 皆為空，無法計算 FCF margin、FCF÷NI、net debt、current ratio、debt/equity 或現金部位。

## Capital allocation & insider signal
- 內部人交易（`insider`）：空陣列，淨買賣金額與占市值比例 n/a。
- 股東結構（`major_holders`、`inst_holders`）：空陣列，n/a。
- 資本支出、買回、股利：財務報表缺失，覆蓋比率 n/a。
- 市值（market_cap）與股本（shares）：yfinance 回傳 null，n/a。

## Valuation
- 無 trailing / forward P/E、EV/EBITDA、P/FCF、P/S（缺 EPS、EBITDA、FCF、股本），無法與行業中位數比較，sector median 標示 n/a。
- 價格參考（fast_info，source: cache，feed: cnyes，cached_at 2026-11-11 14:00 UTC）：last 304.0 TWD，previous close 304.5，day high 305.0，day low 295.0。`fifty_day_average`、`two_hundred_day_average` 為 null；repo 技術報告（`daily/2026-11-12/3260.TW/market.md`）所列 MA50 約 368.90、MA200 約 380.31 僅供技術面參考，本報告不以其推估估值水準。
- 結論：價格無法與任何獲利或現金流量指標連結，估值吸引力不予判定。

## Key catalysts
- 下次財報日期（`earnings_dates`）：cache 回傳 null，live 呼叫連線失敗，n/a。
- 近期 guidance、法說、產品或客戶資訊：repo 內無可用資料，n/a。
- 價格事件（非基本面催化劑，僅供參考，來自 `prices/3260.TW.csv`）：
  - 2026-11-06 盤中跳空低開至 270.0，收盤回至 299.5。
  - 2026-11-09 至 11-11 收盤 305.0 / 304.5 / 304.0，量能萎縮（11-11 成交量 4,466，前幾日約 7,000–9,000）。
- 上述為價格與量能事件，不得解讀為基本面變化；財報與 guidance 缺失時不應推論營運狀況。

## Metrics table
| Metric (單位) | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 (TWD 億) | n/a | n/a | n/a | DATA_UNAVAILABLE |
| 毛利率 (%) | n/a | n/a | n/a | DATA_UNAVAILABLE |
| 營業利益率 (%) | n/a | n/a | n/a | DATA_UNAVAILABLE |
| 淨利率 (%) | n/a | n/a | n/a | DATA_UNAVAILABLE |
| ROE / ROIC (%) | n/a | n/a | n/a | DATA_UNAVAILABLE |
| FCF margin / FCF÷NI | n/a | n/a | n/a | DATA_UNAVAILABLE |
| Net debt (TWD 億) | n/a | n/a | n/a | DATA_UNAVAILABLE |
| Current ratio / D/E | n/a | n/a | n/a | DATA_UNAVAILABLE |
| 市值 (TWD 億) | n/a | n/a | n/a | DATA_UNAVAILABLE |
| Trailing / Forward P/E | n/a | n/a | n/a | DATA_UNAVAILABLE |
| EV/EBITDA, P/FCF, P/S | n/a | n/a | n/a | DATA_UNAVAILABLE |
| 內部人淨買賣 (6mo) | n/a | n/a | n/a | DATA_UNAVAILABLE |
| 收盤價 (TWD) | 304.0 (2026-11-11) | n/a (YoY 價格序列未於本次取得) | n/a | 價格資料可用 |
| 52 週高 / 低 (TWD, ta 快照) | 525.00 / 171.50 | n/a | n/a | 價格資料，來源 ta 快照 |

## Red flags
- 財務三表、季報、EPS、現金流、資產負債表、內部人與股東資料全部缺失，本報告無法完成基本面判斷，與 2026-11-05 報告狀態一致（仍為 DATA_UNAVAILABLE）。
- Yahoo 連線持續被 403 拒絕，`info` 與 `fast_info` 為 cache 回傳，市值、股本、MA50/MA200、52 週高低在 fast_info 中為 null 或 NaN。
- 價格自 52 週高點大幅回落，屬技術面風險訊號而非基本面證據，不應以此推論獲利惡化或營運惡化。
- 資料時點：cache 於 2026-11-11 14:00 UTC 更新，最新價格為 2026-11-11，早於本報告 as-of 日 2026-11-12，無超出 as-of 之資料。
- 本報告未引用其他 daily/<date> 報告中的財務數字；2026-11-05 報告同樣為空值，無可延續之基本面數據。

FUNDAMENTALS REPORT COMPLETE
