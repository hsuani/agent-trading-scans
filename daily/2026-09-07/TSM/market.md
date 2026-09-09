# 技術分析 — TSM 截至 2026-09-07

## 資料可用性狀態

**PRICE_DATA_UNAVAILABLE**

本次技術分析報告無法完成，原因如下：

### 數據檢索失敗詳情

在多次重試後，技術分析工具無法從 Yahoo Finance 檢索 TSM 的價格數據。代理連接被組織政策阻止：

- **代理狀態**: 已啟用 (http://127.0.0.1:46281)
- **連接失敗原因**: 網關拒絕 CONNECT 請求 (403 - 政策拒絕)
- **阻止的端點**: 
  - guce.yahoo.com:443
  - query2.finance.yahoo.com:443
  - fc.yahoo.com:443

### 影響

無法收集以下指標：
- 當前價格 (Current Price)
- 移動平均線 (MA20, MA50, MA200)
- 相對強度指數 (RSI14)
- MACD 及直方圖
- 布林帶 (Bollinger Bands) 與 %B
- 平均真實波幅 (ATR14)
- 支撑/阻力位 (Support/Resistance Levels)
- 52 週高/低點
- 成交量數據

### 建議行動

為完成 TSM 的技術分析，需要：
1. 解除組織政策對 Yahoo Finance 的限制
2. 配置代理以允許金融數據來源的出站連接
3. 或使用替代數據提供商配置

---

**報告狀態**: 數據不可用 - 無法進行技術分析

MARKET REPORT COMPLETE
