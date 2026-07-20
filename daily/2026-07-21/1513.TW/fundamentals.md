# 基本面分析 — 1513.TW 截至 2026-07-21

## FUNDAMENTALS_DATA_UNAVAILABLE

### 資料蒐集狀態

本分析無法完成，原因如下：

**代理伺服器政策阻止**
- fc.yahoo.com:443 — CONNECT 連接被拒 (狀態碼 403) — 策略限制或上游故障
- mis.twse.com.tw:443 — CONNECT 連接被拒 (狀態碼 403) — 策略限制或上游故障

**受影響的資料集**
- Yahoo Finance API (yfinance) — 無法存取財務報表、資產負債表、現金流量表
- 台灣證券交易所 TWSE API — 無法存取即時報價、官方財務資料

**嘗試的資料源**
- yf.py info — 失敗
- yf.py fast_info — 失敗
- yf.py financials — 無法嘗試 (upstream 已失敗)
- yf.py balance_sheet — 無法嘗試
- yf.py cashflow — 無法嘗試
- yf.py insider — 無法嘗試

### 建議行動

1. 待代理伺服器政策更新，允許 fc.yahoo.com 與 mis.twse.com.tw
2. 重新執行本分析以取得完整財務指標
3. 若緊急，考慮通過本地 VPN 或替代數據源直接查詢

---

**報告日期**：2026-07-21  
**資料可用性**：不可用  
**分析狀態**：待延期

