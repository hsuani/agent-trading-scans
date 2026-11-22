# Fundamentals — 3260.TW 威剛 (ADATA Technology) as of 2026-11-22

## Executive summary
狀態: DATA_UNAVAILABLE。本次重試 (2026-11-22) 仍無法取得任何財務報表、現金流、資產負債、內部人交易、持股或估值數據: 直連 yfinance 回傳空陣列或被代理層 403 拒絕，repo 快取 `prices/yf/3260.TW.json` 同樣為空陣列 (`financials`, `balance_sheet`, `cashflow`, `insider`, `major_holders`, `inst_holders` 皆 `[]`，`info` 僅含 `trailingPegRatio: null`)。因此無法判斷財務健全度與估值吸引力，本報告不含任何推論性數字。唯一可用資料為價格快取 (最新收盤 235.5 TWD，2026-11-20)。

## Revenue & profitability
- 營收、毛利、營業利益、淨利、ROE、ROIC: n/a。yfinance `financials` / `quarterly_fin` 回傳 `[]`，快取亦為空。
- 3-5 年 CAGR、YoY 趨勢、分部營收占比: n/a。`info.longBusinessSummary` 本次未取得 (info 欄位缺漏)。

## Cashflow & balance sheet
- FCF、FCF/NI、經營現金流、資本支出: n/a (`cashflow` / `quarterly_cf` 回傳 `[]`)。
- 淨負債、流動比率、負債權益比、現金部位: n/a (`balance_sheet` / `quarterly_bs` 回傳 `[]`)。

## Capital allocation & insider signal
- 資本支出趨勢、庫藏股、股利覆蓋率: n/a。
- 內部人交易 (近 6 個月): n/a (`insider` 回傳 `[]`)。不能判定淨買或淨賣，也無法換算相對市值比例。
- 大股東 / 法人持股: n/a (`major_holders`、`inst_holders` 回傳 `[]`)。

## Valuation
- 目前可用的僅有價格: 最新價 235.5 TWD (cnyes feed, 快取)，前收 254.0 TWD，當日區間 232.5–250.0 TWD。以 2026-11-19 收盤 254 對 2026-11-20 收盤 235.5 計算，單日跌幅約 -7.3%。
- 市值、股數、52 週高低、50/200 日均線: n/a (`fast_info` 中相關欄位為 null 或 NaN)。
- P/E、forward P/E、EV/EBITDA、P/FCF、P/S 及產業中位數比較: n/a。

## Key catalysts
- 下次財報日與 EPS 驚喜歷史: n/a (`earnings_dates` 無資料)。
- 近期法說指引、營收月報: 本次未取得。
- 單日 -7.3% 急跌的成因 (財報、產業、指數或其他) 本報告無法判定，需由新聞 / 市場面報告補充。

## Metrics table
單位: 價格為 TWD；市值 / 營收 / 現金流若可得應以 億 TWD 表示 (本次全部 n/a)。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 最新收盤價 (TWD, 2026-11-20) | 235.5 | n/a | n/a | 僅價格，無基本面判斷 |
| 前收 (TWD, 2026-11-19) | 254.0 | n/a | n/a | 參考 |
| 單日漲跌幅 (%) | -7.3 | n/a | n/a | 急跌，成因未知 |
| 營收 (億 TWD) | n/a | n/a | n/a | DATA_UNAVAILABLE |
| 毛利率 / 營業利益率 / 淨利率 | n/a | n/a | n/a | DATA_UNAVAILABLE |
| ROE / ROIC | n/a | n/a | n/a | DATA_UNAVAILABLE |
| FCF margin / FCF÷NI | n/a | n/a | n/a | DATA_UNAVAILABLE |
| 淨負債 (億 TWD) / 負債權益比 | n/a | n/a | n/a | DATA_UNAVAILABLE |
| 流動比率 / 現金部位 | n/a | n/a | n/a | DATA_UNAVAILABLE |
| 近 6 個月內部人淨買賣 | n/a | n/a | n/a | DATA_UNAVAILABLE |
| Trailing P/E / Forward P/E | n/a | n/a | n/a | DATA_UNAVAILABLE |
| EV/EBITDA / P/FCF / P/S | n/a | n/a | n/a | DATA_UNAVAILABLE |

## Red flags
- 基本面資料完全缺漏 (財報、現金流、資產負債、內部人、持股、估值皆為空)，財務健全度無法評估，這本身即是最大的風險揭露缺口。
- 近期單日 -7.3% 急跌 (254.0 → 235.5 TWD)，成因未知，不應在缺乏基本面與新聞佐證下推論為基本面惡化或市場情緒所致。
- 價格快取最新為 2026-11-20 收盤，2026-11-21 與 2026-11-22 的價格未見於 `prices/3260.TW.csv`；數據時點落後，使用前需確認。
- 本次未嘗試 TWSE / MOPS 公開資訊觀測站等替代來源 (sandbox 無外網權限)。建議下游在補齊 yfinance 或公開資訊來源後重跑本報告。
- 資料來源注意: yfinance 對台股財務覆蓋本就較薄；本次同樣 ticker 的其他端點 (例如 000660.KS 的財報) 可正常回傳，顯示問題集中於 3260.TW 本身的快取與抓取，而非整體 yfinance 服務中斷。

FUNDAMENTALS REPORT COMPLETE (DATA_UNAVAILABLE)
