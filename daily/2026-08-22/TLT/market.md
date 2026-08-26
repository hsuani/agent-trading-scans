# 技術分析 — TLT (截至 2026-08-22)

## 資料可用性狀態

**PRICE_DATA_UNAVAILABLE**

無法獲取 TLT (iShares 20+ Year Treasury Bond ETF) 的實時價格數據。

### 問題

代理網絡政策限制了對 Yahoo Finance (fc.yahoo.com:443) 的連接存取。已執行多次重試，但均遭到 HTTP 403 拒絕。

### 技術詳情

- 資料源：pipeline/tools/ta.py 和 pipeline/tools/yf.py（需連接 Yahoo Finance API）
- 錯誤信息：`curl: (7) CONNECT tunnel failed, response 403`
- 代理狀態：gateway answered 403 to CONNECT (policy denial or upstream failure)

### 無法進行的分析

由於價格數據不可用，以下技術分析項目無法完成：

- MACD 動量指標 (line, signal, histogram)
- RSI14 相對強度指數
- 移動平均線 (MA20, MA50, MA200)
- 布林帶 (Bollinger Bands) 與 %B 指標
- 動量分析 (1M/3M/6M/12M 報酬率)
- 支撐/阻力位準 (S/R levels)
- 交易量分析 (volume vs 10d average)
- ATR14 波動率指標
- 52 週高低價位

### 建議

- 檢查網絡/代理設定是否允許存取 Yahoo Finance
- 於網絡連接恢復後重新執行分析
- 考慮使用替代數據源若代理政策無法修改

---

**報告完成時間**：2026-08-22
**資料狀態**：無法取得即時市場數據
