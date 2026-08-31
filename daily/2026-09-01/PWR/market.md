# 技術面分析 — PWR (Quanta Services)，截至 2026-09-01

## 數據可用性狀態

**PRICE_DATA_UNAVAILABLE**

### 原因

技術分析無法進行。管道工具無法連接到 Yahoo Finance 數據源。代理政策正在拒絕訪問以下主機：
- query2.finance.yahoo.com:443 (HTTP 403 policy denial)
- fc.yahoo.com:443 (HTTP 403 policy denial)  
- guce.yahoo.com:443 (HTTP 403 policy denial)

多次重試均失敗。

### 影響

缺乏實時價格、移動平均線、指標 (RSI14、MACD、ATR14、BB %B) 和支撑/阻力位數據。無法進行有效的技術分析。

---

## 下一步

- 確認代理網路政策以重新啟用 Yahoo Finance 訪問
- 重新執行分析工具以取得完整的技術快照和指標讀數

**技術分析報告待機**
