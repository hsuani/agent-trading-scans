# 技術分析 — 3163.TWO 截至 2026-09-06

## 資料狀態

**PRICE_DATA_UNAVAILABLE**

### 原因

- Yahoo Finance 被代理伺服器阻止（HTTP 403，connect_rejected）
- 無法連接至 query2.finance.yahoo.com、guce.yahoo.com、fc.yahoo.com
- 組織政策禁止對 TPEX（台灣櫃買中心）之連線
- ta.py 無法獲取 3163.TWO 之歷史價格資料

### 無法進行分析

由於無法獲取實時價格及技術指標數據，以下分析無法進行：

- 當前價格（Price）
- 移動平均線（MA20、MA50、MA200）
- 相對強弱指數（RSI14）
- MACD 指標與信號線
- 布林帶（Bollinger Bands）指標
- ATR 波動率指標
- 本地支撐與阻力位
- 52 週高點/低點
- 技術設定評估（Setup）

### 建議

1. 檢查組織代理設定，確認是否可解除對台灣市場資料源之限制
2. 確認 3163.TWO（波若威 Broadex Technologies）是否仍在台灣櫃買中心上市
3. 待連線恢復後重新運行分析

---

**MARKET REPORT COMPLETE**
