# Fundamentals — 3260.TW (威剛科技 ADATA Technology) as of 2026-10-15

## Executive summary
本次基本面資料抓取失敗，yfinance 端點（finance.yahoo.com / query2.finance.yahoo.com / fc.yahoo.com / guce.yahoo.com）遭 agent proxy 以 403 policy denial 拒絕連線，財務報表、資產負債表、現金流量表、內部人交易、法人持股與估值欄位全部無法取得。目前僅有 fast_info 的快取報價（cnyes feed，快取時間 2026-10-14T11:38:30Z），因此**無法對財務健康度與估值吸引力作出有根據的判斷**。本報告不推估任何財務數字，相關欄位一律標示 n/a；下游研究員與交易員在基本面資料恢復前，應將基本面維度視為「資料缺失」而非「正面或負面」。

## Revenue & profitability
- 營收、CAGR、YoY、毛利率、營業利益率、淨利率、ROE、ROIC：全部 n/a。
- `financials` 與 `quarterly_fin` 回傳空陣列 `[]`，伴隨 Yahoo cookie/crumb 取得失敗訊息。
- 業務組成（segment mix）：`info` 端點未回傳 longBusinessSummary，無法從 yfinance 取得。
- 資料缺口：本次無法驗證任何損益趨勢。

## Cashflow & balance sheet
- FCF、FCF/NI、淨負債、流動比率、負債權益比、現金部位：全部 n/a。
- `balance_sheet`、`quarterly_bs`、`cashflow`、`quarterly_cf` 均回傳空陣列 `[]`。
- 資料缺口：無法判斷現金流量品質或償債能力。

## Capital allocation & insider signal
- 資本支出趨勢、買回、股利覆蓋率：n/a。
- 內部人交易（`insider`，近 6 個月）：端點失敗，無法計算淨買賣與相對市值規模。
- 大股東集中度（`major_holders`）與法人持股（`inst_holders`）：皆回傳空陣列 `[]`，n/a。
- 資料缺口：無內部人或籌碼面訊號可用，不應解讀為「無內部人交易」。

## Valuation
- Trailing / forward P/E、EV/EBITDA、P/FCF、P/S：全部 n/a（`info` 僅回傳 trailingPegRatio: null）。
- 市值（market_cap）與流通股數（shares）：null，`fast_info` 亦註記 Yahoo share count 請求失敗。
- 可用價格資料（fast_info，來源 cnyes，快取）：
  - 最新價 367.5 TWD，前收 363.0 TWD，當日高 367.5 / 低 360.5 TWD。
  - 50 日與 200 日均線：null，52 週高低：NaN，無法計算趨勢位置。
  - 此為快取資料（2026-10-14T11:38:30Z），非 2026-10-15 盤中或收盤價；2026-10-15 之後的資料一律視為未知，本報告未使用。
- 與產業中位數比較：n/a（無財務數據可比，本報告不提供估計值）。

## Key catalysts
- 下次財報日與 EPS surprise 歷史：`earnings_dates` 回傳空陣列 `[]`，n/a。
- 近期法說會、管理層財測指引、產品或產能轉型：yfinance 無資料；本報告不從外部網頁補充。
- 提醒：ADATA 為台股上市公司，yfinance 對 .TW 代碼的財務覆蓋本來就較薄，即使 proxy 放行，仍建議以公開資訊觀測站（MOPS）月營收與季報補足。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 最新價 (TWD, 快取) | 367.5 | n/a（前收 363.0，日漲幅約 +1.2%） | n/a | 僅供參考 |
| 營收 | n/a | n/a | n/a | 資料缺失 |
| 毛利率 | n/a | n/a | n/a | 資料缺失 |
| 營業利益率 | n/a | n/a | n/a | 資料缺失 |
| 淨利率 | n/a | n/a | n/a | 資料缺失 |
| ROE / ROIC | n/a | n/a | n/a | 資料缺失 |
| FCF 與 FCF/NI | n/a | n/a | n/a | 資料缺失 |
| 淨負債 / 現金 | n/a | n/a | n/a | 資料缺失 |
| 流動比率 | n/a | n/a | n/a | 資料缺失 |
| 負債權益比 | n/a | n/a | n/a | 資料缺失 |
| 資本支出 / 股利 / 買回 | n/a | n/a | n/a | 資料缺失 |
| 內部人淨買賣 (6 個月) | n/a | n/a | n/a | 資料缺失 |
| Trailing / Forward P/E | n/a | n/a | n/a | 無法評估 |
| EV/EBITDA、P/FCF、P/S | n/a | n/a | n/a | 無法評估 |
| 50 日 / 200 日均線 | n/a | n/a | n/a | 資料缺失 |
| 下次財報日 | n/a | n/a | n/a | 資料缺失 |

## Red flags
- 資料源阻斷：yfinance 所有財務端點因 agent proxy 403 policy denial 失敗，被阻斷的主機包括 finance.yahoo.com、query2.finance.yahoo.com、fc.yahoo.com、guce.yahoo.com。依 proxy 規範，本次未重試或繞道，僅回報。
- 基本面完全缺失：無法判斷獲利能力、現金流、負債或估值，此為本報告最大的風險。
- 股價快取時效：fast_info 價格為 2026-10-14 快取值，非 2026-10-15 即時資料，且 50/200 日均線與 52 週高低缺失，技術面與基本面皆不完整。
- 籌碼面盲區：內部人與法人持股資料缺失，無法排除大股東或內部人重大動向。
- 本報告不含交易建議，交易決策需待基本面資料恢復後重新執行本階段。

FUNDAMENTALS REPORT COMPLETE
