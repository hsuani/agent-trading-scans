# Fundamentals — 3260.TW 威剛 (ADATA Technology) as of 2026-11-23

資料狀態：**DATA_UNAVAILABLE**。本次無法完成財務健康度與估值判斷。原因是 yfinance 財務三表、季報、內部人交易、股東結構與財報日期全部回傳空陣列或被代理層 403 拒絕，`info` 僅含 `trailingPegRatio: null`。以下只呈現可用的價格資料，不含任何基本面推論數字。

## Executive summary
威剛的營收、獲利、現金流、資產負債與估值在本次全部無法取得 (n/a)，因此財務健康度與估值吸引力都無法判定。價格面明顯轉弱：2026-11-23 盤中價 249.0 TWD，較 2026-03-19 歷史收盤高點 525.0 TWD 仍低約 52.6%，近 60 個交易日報酬約 -43.2%，股價位於 MA20 / MA50 / MA200 下方。在財報資料補齊前，不應把價格下跌解讀為基本面變化。

## Revenue & profitability
- 營收、毛利、營業利益、淨利、ROE、ROIC：n/a。`financials` 與 `quarterly_fin` 回傳 `[]`。
- 3-5 年 CAGR、YoY 趨勢、分部營收占比：n/a。`info.longBusinessSummary` 未取得。

## Cashflow & balance sheet
- FCF、FCF/NI、經營現金流、資本支出：n/a。`cashflow` 與 `quarterly_cf` 回傳 `[]`。
- 淨負債、流動比率、負債權益比、現金部位：n/a。`balance_sheet` 與 `quarterly_bs` 回傳 `[]`。

## Capital allocation & insider signal
- 資本支出趨勢、庫藏股、股利覆蓋率：n/a。
- 內部人交易 (近 6 個月)：n/a。`insider` 回傳 `[]`，無法判定淨買賣方向，也無法換算相對市值比例。
- 大股東與法人持股：n/a。`major_holders`、`inst_holders` 回傳 `[]`。

## Valuation
- 市值、股本、trailing / forward P/E、EV/EBITDA、P/FCF、P/S：n/a (`fast_info` 的 `market_cap`、`shares` 為 null)。
- 產業中位數比較：n/a。
- 可用價格資料 (本地 `prices/3260.TW.csv`，共 332 筆，2025-07-11 至 2026-11-23)：
  - 2026-11-23 價格列為 open 231、high 251.5、low 230.5、close 249.0、volume 4,529。cnyes 快取於 UTC 02:00 (台北 10:00) 更新，發生於收盤前，因此 249.0 應視為盤中價，並非確認收盤。
  - 前一交易日 2026-11-20 收盤 235.5 TWD，2026-11-19 收盤 254.0 TWD。
  - MA20 302.7、MA50 346.7、MA200 379.7 TWD (自算，含 11-23 盤中列)。
  - 近 5 / 20 / 60 日報酬：-10.4% / -24.1% / -43.2%。
  - 距 2026-03-19 收盤高點 525.0 TWD：-52.6%。
- 上述為技術面資訊，無法換算為估值水準。

## Key catalysts
- 下次財報日與 EPS 驚喜歷史：n/a。`earnings_dates` 回傳 403 (CONNECT tunnel failed)。
- 近期法說指引、營收月報：本次未取得。
- 價格事件：2026-11-20 單日由 254.0 跌至 235.5 (約 -7.3%)，2026-11-23 盤中自 235.5 回升至 249.0 (約 +5.7%，盤中)。兩日波動成因無法由本報告判定，需由 news 與 market 報告補充。

## Metrics table
單位：價格為 TWD。市值、營收、淨利、現金流若可得應以 億 TWD 表示，本次無任何金額資料，全部 n/a。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 收盤 / 盤中價 (TWD, 2026-11-23) | 249.0 (盤中) | n/a | n/a | 價格可用，非確認收盤 |
| 前收 (TWD, 2026-11-20) | 235.5 | n/a | n/a | 參考 |
| 近 60 日報酬 (%) | -43.2 | n/a | n/a | 技術面弱勢 |
| MA20 / MA50 / MA200 (TWD, 自算) | 302.7 / 346.7 / 379.7 | n/a | n/a | 股價位於三線下方 |
| 距歷史高點 525.0 TWD (%) | -52.6 | n/a | n/a | 技術面弱勢 |
| 營收 (億 TWD) | n/a | n/a | n/a | DATA_UNAVAILABLE |
| 毛利率 / 營業利益率 / 淨利率 (%) | n/a | n/a | n/a | DATA_UNAVAILABLE |
| ROE / ROIC (%) | n/a | n/a | n/a | DATA_UNAVAILABLE |
| FCF margin / FCF÷NI | n/a | n/a | n/a | DATA_UNAVAILABLE |
| 淨負債 (億 TWD) / 負債權益比 | n/a | n/a | n/a | DATA_UNAVAILABLE |
| 流動比率 / 現金部位 | n/a | n/a | n/a | DATA_UNAVAILABLE |
| 市值 (億 TWD) | n/a | n/a | n/a | DATA_UNAVAILABLE |
| 近 6 個月內部人淨買賣 | n/a | n/a | n/a | DATA_UNAVAILABLE |
| Trailing P/E / Forward P/E | n/a | n/a | n/a | DATA_UNAVAILABLE |
| EV/EBITDA / P/FCF / P/S | n/a | n/a | n/a | DATA_UNAVAILABLE |

## Red flags
- 財務三表、現金流、資產負債、內部人、持股與估值資料全部缺失，財務健全度無法評估。這是本報告最大的資料缺口。
- Yahoo 相關端點遭代理層 403 (CONNECT tunnel failed, response 403) 拒絕，屬於 sandbox 政策阻擋，本報告不嘗試繞過。阻擋的主機為 Yahoo Finance 相關主機，需由 policy 或工具端修復。
- 連續多日下跌：近 60 日 -43.2%，股價位於 MA20、MA50、MA200 之下，且均線呈空頭排列。這是技術面與情緒風險，不是基本面證據。
- 2026-11-23 的 249.0 為盤中快照，非確認收盤，下游使用前需確認。
- 本次 as-of 為 2026-11-23，本地價格列無超出 as-of 日期的資料。
- 前一版 2026-11-20 與 2026-11-22 報告同樣為 DATA_UNAVAILABLE，屬持續性資料缺口，並非單日暫時性失敗。
- 補救建議：修復 yfinance 對 3260.TW 的存取 (或改用允許的公開資訊來源，如 MOPS) 後重跑，優先補齊三表、`earnings_dates`、`insider`、`major_holders`。

FUNDAMENTALS REPORT COMPLETE (DATA_UNAVAILABLE)
