# 技術分析 — GFS（2026-07-12）

## PRICE_DATA_UNAVAILABLE

本環境網路政策阻擋 `fc.yahoo.com:443` 與 `ws.api.cnyes.com:443`，無法取得即時或歷史價格資料。ta.py 與 yf.py 工具均無法連接數據源。

### 重試狀態
- 嘗試 5 次重試（間隔 1.5, 3, 4.5, 6, 7.5 秒）
- 所有嘗試皆收到代理 403 CONNECT 拒絕
- 原因：組織出口政策禁止

### 資料來源狀態
| 來源 | 狀態 | 備註 |
|------|------|------|
| yfinance (fc.yahoo.com) | ✗ 阻擋 | CONNECT tunnel failed, 403 |
| cnyes API (ws.api.cnyes.com) | ✗ 阻擋 | CONNECT tunnel failed, 403 |
| TWSE MIS API | 未測試 | 不適用於 GFS（US ticker）|

### 技術分析無法進行
由於無法獲得以下數據，本報告無法完成技術分析：

- 價格 (OHLCV)
- 移動平均線 (MA20, MA50, MA200)
- 技術指標 (RSI14, MACD, Bollinger Bands, ATR14)
- 支撐/阻力位
- 波動率數據
- 動能指標 (1m/3m/6m/12m 回報)

## 建議

請聯絡系統管理員，請求允許訪問 `fc.yahoo.com:443` 以獲取美股價格數據，或提供替代數據源。

**無技術分析報告** — PRICE_DATA_UNAVAILABLE
