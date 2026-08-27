# 技術分析 — FCX (2026-08-28)

## 資料狀態

**PRICE_DATA_UNAVAILABLE**

無法獲取 FCX 的價格資料。代理伺服器政策阻止了對 Yahoo Finance 數據來源的連接（fc.yahoo.com、query2.finance.yahoo.com、guce.yahoo.com 連接被拒，HTTP 403 政策否決）。

### 技術細節
- `ta.py FCX snapshot --period 2y` 失敗：未發現歷史價格數據
- `yf.py FCX fast_info` 失敗：ConnectionError，CONNECT 隧道失敗（響應 403）
- `ta.py FCX levels --period 1y` 失敗：無 FCX 的歷史記錄

### 影響
無法進行以下分析：
- 即時價格與移動平均線（MA20、MA50、MA200）比較
- 技術指標（RSI14、MACD、Bollinger Bands）
- 支持/阻力位級別
- 動量與波動率分析
- 成交量確認

### 建議步驟
1. 檢查代理政策設置以允許訪問 Yahoo Finance
2. 確認 FCX 是否已從市場退市（工具報告"possibly delisted"）
3. 確認代理連接恢復後重新運行分析

---

**分析報告無法完成 — 價格數據不可用**

MARKET REPORT INCOMPLETE — PRICE_DATA_UNAVAILABLE
