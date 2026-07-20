# 技術分析 — 2301.TW (光寶科技) 2026-07-21

## PRICE_DATA_UNAVAILABLE

### 資料取得狀態
目前無法從 Yahoo Finance 取得 2301.TW 的價格數據。外部數據源返回 HTTP 403 Forbidden 錯誤，導致技術指標無法計算。

**嘗試的操作：**
- MACD、RSI14、Bollinger %B、MA20/50/200 計算失敗
- 支撐/阻力水位無法識別
- ATR14、動量、成交量確認無法評估

### 可能原因
1. 股票代碼 (2301.TW) 可能已下市或數據源中不可用
2. proxy 連線限制 (CONNECT tunnel failed 403)
3. Yahoo Finance 對該台灣代碼的數據供應中斷

### 後續行動
請在以下情況下重試：
- 確認股票代碼正確（台灣交易所格式應為 XXXX.TW）
- 檢查網路連線或 proxy 設定
- 確認 2301.TW 在交易所是否仍為有效上市代碼

---

**MARKET REPORT COMPLETE**
