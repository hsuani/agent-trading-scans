# 技術面分析 — 8046.TW 截至 2026-08-06

## 資料狀態

**PRICE_DATA_UNAVAILABLE**

Yahoo Finance 連線失敗 (HTTP 403)。無法取得價格資料。

## 影響範圍

下列所有價格相關指標無法計算：

- 快照價格 (Snapshot price)
- 移動平均線 (MA20, MA50, MA200)
- RSI14, MACD, 布林帶 (Bollinger Bands)
- ATR14, 成交量分析
- 支撐/阻力位 (Support/Resistance levels)
- 52週高/低點
- 年化波動率

## 建議

無法在無有效價格資料的情況下進行技術面分析。請待 Yahoo Finance 連線恢復後重試。

---

MARKET REPORT COMPLETE