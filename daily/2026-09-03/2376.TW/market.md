# 2376.TW 技術分析報告 — 2026-09-03

## PRICE_DATA_UNAVAILABLE

Yahoo Finance 端點被代理封鎖（403 CONNECT tunnel failed），無法取得即時價格資料。

### 影響範圍
- RSI14、MACD、MA20/50/200、布林通道 — 無法計算
- 支撐/阻力位 — 無法識別
- ATR 波動率 — 無法評估
- 五日線、二十日線、五十日線、二百日線 — 無法對比
- 月度/季度/年度動量 — 無法量化

### 狀態
技術面訊號缺失；下游不得給出入場價位、止損建議、目標價位或風險承受建議（PRICE_DATA_UNAVAILABLE）。

---

**報告生成時間：** 2026-09-03  
**資料來源狀態：** 代理策略阻擋（Policy Deny 403）

MARKET REPORT COMPLETE
