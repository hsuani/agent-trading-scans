# 技術分析 — TSM 截至 2026-07-20

## 資料狀態

**PRICE_DATA_UNAVAILABLE**

無法取得 TSM 技術分析資料。

### 原因

遠端代理伺服器當前對 Yahoo Finance API 及其相關終端的連線已被網關政策阻止 (HTTP 403 CONNECT tunnel failed)。所有五次重試嘗試均未成功。替代資料來源 (cnyes、TWSE) 亦無法透過同一代理存取。

### 影響

無法計算以下指標：
- 價格及移動平均線 (MA20, MA50, MA200)
- MACD、RSI14、Bollinger Bands、ATR14
- 動量指標 (1m/3m/6m/12m 報酬)
- 支撐 / 阻力位
- 波動率統計

### 建議

等待網絡連線恢復或代理政策更新。

---

**MARKET REPORT COMPLETE**
