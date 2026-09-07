# 技術面分析 — 1513.TW（中興電工）截至 2026-09-08

## 數據狀態

**PRICE_DATA_UNAVAILABLE**

### 問題描述
無法取得 1513.TW 的價格數據及技術指標。

- Yahoo Finance 連線失敗：HTTP 403 (CONNECT tunnel failed)
  - query2.finance.yahoo.com:443 — connect_rejected
  - guce.yahoo.com:443 — connect_rejected  
  - fc.yahoo.com:443 — connect_rejected
  
- 多次重試後仍無法連接（Cookie/crumb fetch failed）

- ta.py 回報：「possibly delisted; no history for 1513.TW」

### 無法提供之分析項目
- 當前價格 (Current Price)
- 移動平均線 (MA20, MA50, MA200)
- 相對強弱指數 (RSI14)
- MACD 指標
- ATR 波動率
- 支撐/阻力位階
- 技術形態評估

### 建議行動
1. 確認 1513.TW 是否在臺灣證券交易所 (TWSE) 仍有交易
2. 檢查網路連線與代理設定
3. 待連線恢復後重新執行數據蒐集

---

**報告無法完成 — 數據層級故障**
