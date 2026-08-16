# 技術分析 — APD（截至 2026-08-14）

## 數據可用性狀態

**PRICE_DATA_UNAVAILABLE**

### 技術詳情

無法取得 APD 的價格數據。代理 gateway 拒絕連接至 Yahoo Finance (fc.yahoo.com:443)，返回 403 政策拒絕。

多次嘗試透過代理連接失敗，顯示上游故障或政策阻擋。

### 影響

- 無法取得最新報價
- 無法計算技術指標（MA20、MA50、MA200、RSI14、MACD 等）
- 無法識別支撐/阻力位
- 無法進行趨勢分析或動量評估

### 建議後續行動

待網路連接恢復後重新執行分析。

---

**市場報告無法完成**

報告生成時間：2026-08-14 02:12 UTC  
代理 Status：連接拒絕 (policy denial / upstream failure)
