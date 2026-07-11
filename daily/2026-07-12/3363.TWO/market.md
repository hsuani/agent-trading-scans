# 技術分析 — 3363.TWO 截至 2026-07-12

## PRICE_DATA_UNAVAILABLE

**資料狀態**: 無法取得即時市場報價

yfinance 無法連接到 Yahoo Finance 資料源（HTTP 403 CONNECT tunnel failed），導致無法擷取 3363.TWO（上詮）的歷史 OHLCV 資料及技術指標。

### 問題詳情
- **Ticker**: 3363.TWO
- **交易所**: TPEx（臺灣證券交易所櫃檯買賣中心）
- **業務**: 精密光學 FAU 製造商
- **取得失敗原因**: yfinance 連線逾時 (CONNECT tunnel failed)
- **重試機制**: 已執行 5 次重試 (延遲： 1.5s, 3s, 4.5s, 6s, 7.5s) 仍無返回資料

### 建議
1. 確認 3363.TWO 是否為有效的 Yahoo Finance ticker 代碼（台灣上市/櫃公司可能需要特殊格式）
2. 等待網路連線恢復，稍後重新執行分析
3. 查詢替代資料源（例：台灣證交所 API、本地財務資料庫）

**技術指標無法計算**
- MA20, MA50, MA200: N/A
- MACD histogram: N/A
- RSI14: N/A
- BB %B: N/A
- ATR14: N/A
- 52週高/低: N/A
- 多期動能 (1m/3m/6m/12m): N/A
- 支撐/阻力位: N/A

---

**報告狀態**: PRICE_DATA_UNAVAILABLE
**產生時間**: 2026-07-12
