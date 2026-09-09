# 技術分析 — GFS（2026-08-30）

## 資料狀態

**PRICE_DATA_UNAVAILABLE**

無法取得 GFS 技術指標與價格數據。組織政策已在代理層級阻止對 Yahoo Finance 端點的連接（guce.yahoo.com、query2.finance.yahoo.com、fc.yahoo.com 返回 403 Policy Denial）。

使用的工具：
- `pipeline/tools/ta.py GFS snapshot --period 2y` — 連接失敗
- `pipeline/tools/yf.py GFS fast_info` — 連接失敗

### 原因
代理伺服器網關拒絕了所有 Yahoo Finance 連接：
- guce.yahoo.com:443 — connect_rejected (policy denial)
- query2.finance.yahoo.com:443 — connect_rejected (policy denial)
- fc.yahoo.com:443 — connect_rejected (policy denial)

### 影響
無法提供下列分析：
- 快照資料（價格、MA20/MA50/MA200、RSI14、MACD、ATR14）
- 系列資料（過去 60 根柱狀體的 OHLCV 和指標）
- 本地支撐/阻力水位
- 原始 OHLCV 歷史數據

---

**MARKET REPORT COMPLETE** — 數據不可用，無法進行技術分析。
