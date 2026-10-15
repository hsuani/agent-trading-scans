# Fundamentals — MSFT as of 2026-10-15

## Executive summary
本次基本面分析無法完成: `pipeline/tools/yf MSFT` 所有即時端點皆回傳 ConnectionError (curl 7, CONNECT tunnel failed, 403), 且 `prices/yf/MSFT.json` 快取檔不存在, 因此營收、獲利能力、現金流、資產負債表、內部人交易與估值倍數全部為 DATA_UNAVAILABLE。財務健康度與估值吸引力目前無法判斷, 不提供任何方向性結論。待 yfinance 連線恢復, 或 refresh-cache 流程產生 `prices/yf/MSFT.json` 後, 應重新執行本分析。

## 資料來源檢查
- `pipeline/tools/yf MSFT info`: 失敗, `ConnectionError`, curl (7) CONNECT tunnel failed, response 403。
- `pipeline/tools/yf MSFT fast_info`: 指令回傳 exit 0, 但所有欄位皆為 null (last_price, market_cap, shares 等), year_high / year_low 為 NaN, 屬於無效資料, 不採用。
- `pipeline/tools/yf MSFT financials / balance_sheet / cashflow / earnings_dates / insider / major_holders`: 皆失敗 (exit 1), 同一 403 錯誤。
- 本地快取 `prices/yf/MSFT.json`: 不存在 (`prices/yf/` 目錄內無 MSFT 檔案)。
- 本地價格快取 `prices/MSFT.csv`: 不存在。
- 其他日期的 `daily/2026-08-08/MSFT/fundamentals.md` 與 `daily/2026-08-24/MSFT/fundamentals.md` 存在, 但其中的營收、Azure、RPO、EPS、FCF 等數字多處標註為「假設」或「估計」, 來源不可追溯, 且屬於過往日期。本報告不沿用其中任何數字。
- 今日 `daily/2026-10-15/MSFT/market.md` 亦回報 PRICE_DATA_UNAVAILABLE, 與本次結果一致。

## Revenue & profitability
DATA_UNAVAILABLE。
- 3-5 年營收 CAGR: DATA_UNAVAILABLE (financials 無法取得)
- YoY 營收趨勢: DATA_UNAVAILABLE
- 分部營收比重: DATA_UNAVAILABLE (info.longBusinessSummary 無法取得, 無法從 yfinance 確認分部結構)
- 毛利率 / 營業利潤率 / 淨利率趨勢: DATA_UNAVAILABLE
- ROE / ROIC: DATA_UNAVAILABLE

## Cashflow & balance sheet
DATA_UNAVAILABLE。
- FCF 利潤率與 FCF / NI: DATA_UNAVAILABLE (cashflow 無法取得)
- 淨負債 (net debt): DATA_UNAVAILABLE
- Current ratio: DATA_UNAVAILABLE
- Debt / Equity: DATA_UNAVAILABLE
- 現金與約當現金: DATA_UNAVAILABLE

## Capital allocation & insider signal
DATA_UNAVAILABLE。
- 資本支出趨勢: DATA_UNAVAILABLE
- 買回與股利覆蓋率: DATA_UNAVAILABLE
- 內部人交易 (近 6 個月淨買賣與市值佔比): DATA_UNAVAILABLE (insider 端點失敗)
- 大股東與機構持股集中度: DATA_UNAVAILABLE (major_holders / inst_holders 未能取得)

## Valuation
DATA_UNAVAILABLE。
- Trailing P/E / Forward P/E: DATA_UNAVAILABLE (info 無法取得)
- EV/EBITDA: DATA_UNAVAILABLE
- P/FCF: DATA_UNAVAILABLE
- P/S: DATA_UNAVAILABLE
- 與行業中位數比較: 無實際數據基礎, 不估計
- 市值、股價、Beta: DATA_UNAVAILABLE (fast_info 欄位皆為 null)

## Key catalysts
- 下次財報日期 (next earnings date): DATA_UNAVAILABLE (earnings_dates 無法取得)
- 近期指引 (guidance): DATA_UNAVAILABLE
- 分部營收結構變化: DATA_UNAVAILABLE
- 注意: 以下事項僅為未經本次工具驗證的事件, 不能當作本次分析的數據依據, 僅供後續研究者核對: 無。本報告未引用任何過往報告中的催化劑描述。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| Revenue (latest quarter / TTM) | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | 無法判斷 |
| Revenue CAGR (3-5y) | DATA_UNAVAILABLE | n/a | n/a | 無法判斷 |
| Gross margin | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | 無法判斷 |
| Operating margin | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | 無法判斷 |
| Net margin | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | 無法判斷 |
| ROE | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | 無法判斷 |
| ROIC | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | 無法判斷 |
| FCF margin | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | 無法判斷 |
| FCF / NI | DATA_UNAVAILABLE | DATA_UNAVAILABLE | >0.9 為健康門檻 | 無法判斷 |
| Net debt | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | 無法判斷 |
| Current ratio | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | 無法判斷 |
| Debt / Equity | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | 無法判斷 |
| Capex trend | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | 無法判斷 |
| Insider net buy/sell (6mo) | DATA_UNAVAILABLE | n/a | n/a | 無法判斷 |
| Trailing P/E | DATA_UNAVAILABLE | n/a | n/a | 無法判斷 |
| Forward P/E | DATA_UNAVAILABLE | n/a | n/a | 無法判斷 |
| EV/EBITDA | DATA_UNAVAILABLE | n/a | n/a | 無法判斷 |
| P/FCF | DATA_UNAVAILABLE | n/a | n/a | 無法判斷 |
| P/S | DATA_UNAVAILABLE | n/a | n/a | 無法判斷 |
| Next earnings date | DATA_UNAVAILABLE | n/a | n/a | 無法判斷 |

## Red flags
- 資料缺口: yfinance 即時端點與本地快取皆無 MSFT 數據, 本次基本面無任何可驗證數字。
- 過往報告風險: `daily/2026-08-24/MSFT/fundamentals.md` 內多處數字標註為假設或估計, 不應被下游直接引用。
- 交易決策依據不足: 基本面與技術面 (market.md) 同時缺資料, 下游 researcher / trader 不應以本報告作為任何方向判斷的依據。
- 修復建議: 恢復 Yahoo 連線 (依 /root/.ccr/README.md 檢查代理狀態) 或由 GitHub Actions `yf.py refresh-cache` 產生 `prices/yf/MSFT.json` 後重跑。

FUNDAMENTALS REPORT COMPLETE
