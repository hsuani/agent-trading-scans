# 技術分析 — TLN (Talen Energy) 截至 2026-07-21

## PRICE_DATA_UNAVAILABLE

### 狀態報告
無法取得實時價格數據。數據工具 (ta.py 與 yf.py) 連接 Yahoo Finance 時遭代理伺服器政策阻擋 (gateway 403 response on fc.yahoo.com:443)。

### 嘗試過程
- ta TLN snapshot --period 2y ❌ 代理連接被拒
- ta TLN series --period 1y ❌ 代理連接被拒
- ta TLN levels --period 1y ❌ 代理連接被拒
- yf TLN fast_info ❌ 代理連接被拒
- yf TLN history --period 1y ❌ 代理連接被拒

### 數據依賴性
無法進行技術分析，缺少必需的：
- 實時及歷史 OHLCV 數據
- MACD、RSI14、Bollinger Bands 指標計算
- 移動平均線 (MA20/MA50/MA200)
- 支撐/阻力位 (local extrema)
- 交易量分析
- 波動率指標 (ATR14)
- 52 週高/低點

### 建議
待代理政策允許 Yahoo Finance 訪問後，重新執行技術掃描。

---
**報告狀態**: 技術分析無法完成 — 缺乏價格數據

此報告不包含任何推測價格或指標值。
