# Fundamentals — CRDO as of 2026-07-29

## Executive Summary

本報告無法完成 CRDO 之基本面分析。所有來自 yfinance 之財務數據、公司資訊、內部人交易等關鍵資料均無法取得，主要原因為代理服務器與 Yahoo Finance (fc.yahoo.com) 連接失敗，代理返回 403 policy denial。建議等待網絡連接恢復後重新分析，或使用替代資料來源進行驗證。

---

## Revenue & Profitability

**DATA_UNAVAILABLE**

無法取得下列指標：
- 年收入及 YoY 成長率
- 毛利率、營業利益率、淨利率趨勢
- ROE、ROIC
- 業務段分析

**原因**：yfinance financials、quarterly_fin 端點返回空值。

---

## Cashflow & Balance Sheet

**DATA_UNAVAILABLE**

無法取得下列指標：
- 自由現金流 (FCF) 及 FCF margin
- FCF / NI 比率
- 淨債務、流動比率、負債/權益比
- 現金部位

**原因**：yfinance cashflow、quarterly_cf、balance_sheet 端點返回空值。

---

## Capital Allocation & Insider Signal

**DATA_UNAVAILABLE**

無法取得下列指標：
- Capex 趨勢
- 股票回購和股息支付
- 內部人交易活動（過去 6 個月淨買入/賣出）
- 交易規模相對於市值

**原因**：yfinance insider 端點連接失敗（代理 403），major_holders 端點返回空值。

---

## Valuation

**DATA_UNAVAILABLE**

無法取得下列指標：
- Trailing P/E、Forward P/E
- EV/EBITDA
- P/FCF
- P/S (相對於行業中位數)
- 當前股價、52 週高/低、50/200 日移動平均

**原因**：yfinance info、fast_info 端點連接失敗（代理 403）。

---

## Key Catalysts

**DATA_UNAVAILABLE**

無法取得下列資訊：
- 下次財報發佈日期及 EPS 預估
- 最近指導性意見
- 業務段轉變

**原因**：yfinance earnings_dates 端點返回空值或連接失敗。

---

## Metrics Table

| 指標 | 最新值 | YoY | 行業中位數估計 | 評論 |
|---|---|---|---|---|
| Revenue (年) | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | 無法取得 |
| Revenue YoY Growth | DATA_UNAVAILABLE | — | n/a | 無法計算 |
| Gross Margin | DATA_UNAVAILABLE | — | n/a | 無法取得 |
| Operating Margin | DATA_UNAVAILABLE | — | n/a | 無法取得 |
| Net Margin | DATA_UNAVAILABLE | — | n/a | 無法取得 |
| ROE | DATA_UNAVAILABLE | — | n/a | 無法計算 |
| ROIC | DATA_UNAVAILABLE | — | n/a | 無法計算 |
| FCF Margin | DATA_UNAVAILABLE | — | n/a | 無法取得 |
| FCF / NI Ratio | DATA_UNAVAILABLE | — | n/a | 無法計算 |
| Net Debt / EBITDA | DATA_UNAVAILABLE | — | n/a | 無法計算 |
| Current Ratio | DATA_UNAVAILABLE | — | n/a | 無法取得 |
| Debt / Equity | DATA_UNAVAILABLE | — | n/a | 無法計算 |
| Trailing P/E | DATA_UNAVAILABLE | — | n/a | 無法取得 |
| Forward P/E | DATA_UNAVAILABLE | — | n/a | 無法取得 |
| EV/EBITDA | DATA_UNAVAILABLE | — | n/a | 無法計算 |
| P/FCF | DATA_UNAVAILABLE | — | n/a | 無法計算 |
| Current Price | DATA_UNAVAILABLE | — | n/a | 無法取得 |
| 52-Week High/Low | DATA_UNAVAILABLE | — | n/a | 無法取得 |
| Insider Net Activity (6mo) | DATA_UNAVAILABLE | — | n/a | 無法取得 |

---

## Red Flags

1. **網絡連接失敗**：代理服務器無法連接至 Yahoo Finance，所有基本面數據無法檢索。

2. **完全數據缺失**：yfinance 返回空值或連接被拒，無法進行有意義的財務分析。

3. **無法驗證公司狀況**：無營收、盈利能力、現金流、估值或內部人交易數據，無法判斷公司財務健康狀況。

---

## Technical Notes

**數據檢索嘗試**：
- `yf.py CRDO financials` → 返回 `[]`
- `yf.py CRDO info` → 代理 403 (fc.yahoo.com 連接被拒)
- `yf.py CRDO insider` → 代理 403 (fc.yahoo.com 連接被拒)
- `yf.py CRDO cashflow` → 返回 `[]`
- `yf.py CRDO balance_sheet` → 返回 `[]`
- `yf.py CRDO fast_info` → 代理 403 (fc.yahoo.com 連接被拒)
- `yf.py CRDO quarterly_fin` → 返回 `[]`
- `yf.py CRDO quarterly_cf` → 返回 `[]`

**代理狀態**：代理被配置但上游 gateway 對 fc.yahoo.com 返回 403 policy denial。

---

**報告生成時間**：2026-07-29 UTC  
**數據可用性狀態**：DATA_UNAVAILABLE  
**下一步建議**：待網絡連接恢復或使用替代資料源後重新分析

