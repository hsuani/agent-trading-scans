# Fundamentals — 3260.TW (威剛) as of 2026-11-05

## Executive summary
DATA_UNAVAILABLE：本次 yfinance 財務三表（損益表、資產負債表、現金流量表）、季報、EPS 公告日、內部人交易、大股東與機構持股皆為空值或連線被拒（403 CONNECT tunnel），repo cache `prices/yf/3260.TW.json` 亦僅有空陣列。因此無法判斷財務健康度與估值（P/E、EV/EBITDA、P/FCF 均為 n/a）。僅能由 cache 價格序列提供技術面與價格結構的補充事實：最新收盤 318.0 TWD（2026-11-04），較 2026-03-19 高點 525.0 TWD 回落約 39%，近 60 個交易日報酬約 -19.7%。基本面結論需待財務資料補齊後重跑。

## Revenue & profitability
DATA_UNAVAILABLE。`financials`、`quarterly_fin` 皆回傳空陣列，無營收、毛利、營業利益、淨利、ROE、ROIC 等數據，無法計算 3-5 年 CAGR、YoY 或margin 趨勢。`info.longBusinessSummary` 亦未取得，無法拆解產品或區域營收組合。

## Cashflow & balance sheet
DATA_UNAVAILABLE。`cashflow`、`quarterly_cf`、`balance_sheet`、`quarterly_bs` 皆為空，無法計算 FCF margin、FCF/NI、net debt、current ratio、debt/equity 或現金部位。

## Capital allocation & insider signal
- 內部人交易（`insider`）：空陣列，淨買賣金額與占市值比例 n/a。
- 股東結構（`major_holders`、`inst_holders`）：空陣列，n/a。
- 資本支出、買回、股利：財務報表缺失，n/a。
- 市值（market_cap）與股本（shares）：yfinance 回傳 null，n/a。

## Valuation
- 本次無 trailing/forward P/E、EV/EBITDA、P/FCF、P/S（皆缺 EPS、EBITDA、FCF、股本）。
- 無行業中位數可對照，sector median 僅能標示為 n/a。
- 價格參考（fast_info，source: cache，feed: cnyes）：last 318.0 TWD，當日 high 324.0 / low 300.0；`fifty_day_average`、`two_hundred_day_average` 為 null，改以 repo CSV 自算 MA50 = 380.6、MA200 = 379.8（TWD）。價格與估值倍數無法相連，此處不推估估值水準。

## Key catalysts
- 下次財報日期（`earnings_dates`）：連線失敗（ConnectionError），n/a。
- 近期 guidance、產品或法說資訊：本次 repo 內無可用資料，n/a。
- 價格結構事實（來自 `prices/3260.TW.csv`，共 333 筆，2025-06-23 至 2026-11-04，2026-02-11 至 2026-02-23 有一段缺漏）：
  - 歷史高點 525.0 TWD（2026-03-19），歷史低點 89.2 TWD（2025-07-22）。
  - 2025-11-21 低點 173.5 TWD 為近一年低點區間內之低點。
  - 月均收盤：2026-03 約 365.4、2026-06 約 419.3、2026-09 約 396.8、2026-10 約 356.8 TWD。
  - 近 5 / 20 / 60 / 120 日報酬：-12.5% / -16.8% / -19.7% / -30.4%。
  - 年化波動率：20 日約 57.1%，60 日約 43.4%。
- 上述為價格事件，不代表基本面催化劑，財報補齊前不應解讀為基本面變化。

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
| 收盤價 (TWD) | 318.0 (2026-11-04) | 近 120 日 -30.4% | n/a | 價格資料可用 |
| MA50 / MA200 (TWD, 自算) | 380.6 / 379.8 | n/a | n/a | 股價位於兩均線下方 |
| 年化波動率 20d / 60d (%) | 57.1 / 43.4 | n/a | n/a | 波動偏高 |

## Red flags
- 財務三表、季報、EPS、現金流、資產負債表、內部人與股東資料全部缺失，本報告無法完成基本面判斷。
- yfinance 連線遭 403 拒絕（CONNECT tunnel），fast_info 與 info 為 cache 回傳，部分欄位 null（市值、股本、MA、52 週高低）。
- 價格 3 個月內由 525.0 回落至 318.0（約 -39%），近 60 日報酬 -19.7%，年化波動率高，屬技術面風險訊號而非基本面證據。
- 資料時點：cache 於 2026-11-04 14:17 UTC 更新，分析 as-of 為 2026-11-05，cache 最新一筆價格為 2026-11-04，無明顯超出 as-of 之資料，但 as-of 日晚於 sandbox 當前日期 2026-11-04，需留意。
- 本報告未使用其他 daily/<date> 報告之任何數字。

FUNDAMENTALS REPORT COMPLETE
