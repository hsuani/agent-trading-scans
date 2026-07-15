# 技術面 — 2356.TW (英業達) 截至 2026-07-16

## 資料狀態

**PRICE_DATA_UNAVAILABLE**

取得 2356.TW 的價格數據失敗。代理伺服器 (HTTPS 閘道) 拒絕連線至 Yahoo Finance (fc.yahoo.com) 和台灣金融數據來源 (ws.api.cnyes.com)，回傳 403 政策拒絕。

### 故障詳情

- **工具呼叫**: `ta 2356.TW snapshot` 和 `yf 2356.TW fast_info`
- **錯誤類型**: CONNECT 隧道失敗，網關政策拒絕
- **重試次數**: 已重試多次，仍無法恢復
- **影響**: 無法取得最新價格、技術指標 (RSI、MACD、MA20/MA50/MA200、ATR) 和支撐阻力位

### 建議行動

1. 檢查代理伺服器和網路連線狀態
2. 確認是否有對台灣證交所或特定財務資料源的訪問限制
3. 待連線恢復後重新執行技術面掃描

---

**MARKET REPORT INCOMPLETE — PRICE_DATA_UNAVAILABLE**
