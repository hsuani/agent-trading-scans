# 技術分析 — VST（Vistra Corp）截至 2026-07-21

## 資料可用性

**PRICE_DATA_UNAVAILABLE**

無法擷取 VST 技術分析數據。代理伺服器政策阻止連接到 Yahoo Finance 數據源（fc.yahoo.com），所有資料擷取嘗試均返回 HTTP 403 CONNECT tunnel failed。

### 發生詳情

- 工具：`ta.py VST snapshot --period 2y`
- 錯誤：CONNECT tunnel failed, response 403
- 重試次數：3 次
- 狀態：無法取得歷史價格數據

### 無法進行的分析

由於缺乏實時價格和歷史 OHLCV 數據，無法提供以下技術指標分析：

- 價格 vs MA20/MA50/MA200 移動平均線
- MACD、RSI14、布林帶 %B 指標
- ATR 波動率分析
- 技術支撐/阻力位
- 動量確認（1m/3m/6m/12m 回報）

### 建議後續行動

1. 檢查代理伺服器政策設置，允許對 Yahoo Finance API 的訪問
2. 確認 VST 股票代碼是否有效且在交易所掛牌
3. 重試資料擷取，或改用替代數據源

---

**報告完成狀態：PRICE_DATA_UNAVAILABLE - 無法執行技術分析**
