# 技術分析 — 8021.TW (尖點科技) — 2026-08-31

## 資料狀態
**PRICE_DATA_UNAVAILABLE**

### 詳情
無法取得 8021.TW 的價格數據。根據工具執行結果：
- yfinance 連線被代理伺服器阻止 (connect_rejected，組織政策限制)
- Yahoo Finance 端點（query2.finance.yahoo.com, guce.yahoo.com, fc.yahoo.com）均無法連接
- 系統回傳：「$8021.TW: possibly delisted; no price data found (period=1y)」

### 技術指標狀態
由於無可用的歷史價格數據，以下指標無法計算：
- MACD、Signal、MACD histogram
- RSI14
- 布林帶（Bollinger Bands）與 %B
- 移動平均線（MA20, MA50, MA200）
- ATR14 與波動率
- 局部支撐/阻力水位

### 建議
請確認：
1. **代碼有效性**：8021.TW 是否為有效的台灣上市股票代碼
2. **網路連接**：代理設定是否允許 Yahoo Finance 連線
3. **交易狀態**：該股是否已下市或停牌

---

**技術報告無法完成 — 缺少必要的價格數據**  
MARKET REPORT INCOMPLETE
