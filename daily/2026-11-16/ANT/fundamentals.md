# Fundamentals — ANT as of 2026-11-16

**狀態：DATA_UNAVAILABLE（財務基本面無法評估）**

## Executive summary
ANT（Anthropic, PBC）在 yfinance 顯示為「預計 2026-11-19 於 Nasdaq 新掛牌」的標的。本次 `info` 只回傳公司簡介與 corporate action（source 為 cache，cached_at 2026-11-15T13:53:55+00:00）。`fast_info`、損益表、資產負債表、現金流量表、財報日曆、內部人交易、機構持股皆為空陣列或連線失敗（CONNECT tunnel 403，屬環境代理限制）。因此無法判斷財務健康度與估值吸引力，本報告不提供任何推估數字。

## 工具輸出摘要
- `info`：shortName Anthropic, PBC；exchange NAS；ipoExpectedDate 2026-11-19；corporateActions 為 NEW_LISTING（Nasdaq，2026-11-19）。上市日晚於 as-of 2026-11-16，屬 post-date 資訊。
- `fast_info`：last_price、market_cap、shares、50/200 日均線皆為 null，year_high/low 為 NaN。
- `financials` / `quarterly_fin` / `balance_sheet` / `quarterly_bs` / `cashflow` / `quarterly_cf`：皆為 `[]`。
- `earnings_dates`、`insider`、`inst_inst_holders`：皆為 `[]`。`major_holders` 回傳 403 連線錯誤。

## 各面向結論
- 營收與獲利（營收、毛利率、營業利益率、淨利率、ROE、ROIC）：n/a。
- 現金流與資產負債（FCF、FCF/NI、淨負債、流動比率、負債權益比）：n/a。
- 資本配置與內部人訊號：n/a。`insider` 為空陣列，不能解讀為「無內部人交易」。
- 估值（Trailing/Forward P/E、EV/EBITDA、P/FCF、P/S、市值）：n/a。尚無可用市價，任何估值數字都屬捏造，本報告不採用。
- 催化劑：上市日 2026-11-19（Nasdaq，post-date）。首次財報日與近期指引：n/a。

## Red flags
- 財務報表完全缺失，無法驗證獲利或現金流品質。
- 尚未掛牌，無市價、市值與成交量。
- 股東結構與內部人交易資料缺失。
- 資料來源為本地快取，且 Yahoo 即時連線被代理阻擋。
- 本次未使用其他日期的 daily 報告數字。

建議：待 ANT 正式揭露財報（S-1 或上市後首份 10-Q）或 yfinance 資料可用後，再重跑本分析。

FUNDAMENTALS REPORT COMPLETE
