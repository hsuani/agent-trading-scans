# 技術分析 — WDC (西部數據) 2026-07-22

## 資料狀態

**PRICE_DATA_UNAVAILABLE**

無法獲取 WDC 價格數據。Yahoo Finance 連線遭代理網關拒絕 (403 政策限制)。技術分析工具無法連接 fc.yahoo.com:443 以檢索歷史價格、成交量及技術指標數據。

### 診斷詳情
- **連線狀態**: 代理網關拒絕 CONNECT
- **錯誤代碼**: 403 (policy denial or upstream failure)
- **受影響主機**: fc.yahoo.com
- **資料源**: yfinance (Yahoo Finance)

## 無法計算之指標

由於缺乏基礎價格數據，以下指標無法計算:

| 指標 | 狀態 |
|---|---|
| 最新收盤價 | 無法取得 |
| MA20 / MA50 / MA200 | 無法計算 |
| RSI14 | 無法計算 |
| MACD / Signal / Histogram | 無法計算 |
| Bollinger Bands | 無法計算 |
| ATR14 | 無法計算 |
| 支撐/阻力水位 | 無法計算 |
| 成交量分析 | 無法取得 |
| 52周高/低 | 無法取得 |

## 建議行動

1. 等候代理網關恢復 Yahoo Finance 連線
2. 檢查防火牆/政策設定
3. 稍後重新執行分析

---

**市場分析不完整** - 無可用數據

MARKET ANALYSIS COMPLETE
