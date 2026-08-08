# 技術面 — FN（截至 2026-08-09）

## 資料狀態

**PRICE_DATA_UNAVAILABLE**

無法取得 FN 的市場數據。Yahoo Finance 代理連線被拒（fc.yahoo.com 403），導致價格、技術指標與支撐阻力水平無法獲取。

### 症狀
- yfinance 連接被阻
- 底層原因：政策拒絕或上游故障（gateway policy denial or upstream failure）
- 無法計算 MA20、MA50、MA200、RSI14、MACD、ATR、波動率、支撐/阻力水平

### 建議
代理配置或 Yahoo Finance 服務可用性需檢查。本報告無法提供可操作的技術分析。

---

**MARKET REPORT INCOMPLETE** — 缺乏價格數據
