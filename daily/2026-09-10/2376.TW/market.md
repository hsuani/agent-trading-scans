# 技術面分析 — 2376.TW（技嘉科技）至 2026-09-10

## 資料狀態

**PRICE_DATA_UNAVAILABLE**

### 失敗原因
出口代理伺服器阻止 Yahoo Finance 連線 (HTTP 403)：
- query2.finance.yahoo.com:443 — connect_rejected
- guce.yahoo.com:443 — connect_rejected  
- fc.yahoo.com:443 — connect_rejected

`ta.py` 工具無法獲取 2376.TW 的歷史價格與技術指標數據。

### 技術分析無法進行

無足夠的價格數據計算以下內容：
- 移動平均線（MA20、MA50、MA200）
- RSI14、MACD、布林帶等技術指標
- 支撑/阻力位
- 動量與波動率指標

### 建議

請驗證：
1. 代理配置與 Yahoo Finance 連接狀態
2. 2376.TW 在 Yahoo Finance 上的上市狀態
3. 替代數據來源的可用性

---

**技術分析報告 - 無法完成**

MARKET REPORT UNAVAILABLE — PROXY_EGRESS_BLOCKED
