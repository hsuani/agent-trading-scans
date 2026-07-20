# Fundamentals — QUBT as of 2026-07-21

## FUNDAMENTALS_DATA_UNAVAILABLE

### 錯誤摘要

無法取得 QUBT (Quantum Computing Inc) 的基本面財務數據。Yahoo Finance API 返回 HTTP 403 Proxy 錯誤，yfinance 資料端點均未返回有效數據。

### 嘗試過的數據端點

| 端點 | 狀態 |
|---|---|
| info | 403 Proxy Error |
| fast_info | 403 Proxy Error |
| financials (annual) | Empty [] |
| quarterly_fin | Empty [] |
| balance_sheet (annual) | Empty [] |
| quarterly_bs | Empty [] |
| cashflow (annual) | Empty [] |
| quarterly_cf | Empty [] |
| earnings_dates | 403 Proxy Error |
| insider | 403 Proxy Error |

### 影響評估

無法評估以下關鍵指標:
- 營收趨勢與增長率 (Revenue CAGR, YoY)
- 現金持位與燃燒率 (Cash runway)
- 自由現金流 (FCF) 品質
- EV/Revenue 估值倍數
- 內部人交易信號

### 建議後續行動

1. 重試 Yahoo Finance 連線（fc.yahoo.com:443 代理可能暫時不可用）
2. 聯繫資料提供方確認 API 狀態
3. 考慮使用替代數據源（如 CNYES、Bloomberg 終端）

---

**資料截至**: 2026-07-21  
**工具**: pipeline/tools/yf.py  
**狀態**: DATA UNAVAILABLE - Proxy 403 Error

