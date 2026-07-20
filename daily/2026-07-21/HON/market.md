# 技術面 — HON 截至 2026-07-21

## PRICE_DATA_UNAVAILABLE

**狀態**: 價格數據不可用

**原因**: Yahoo Finance 返回 HTTP 403 (Proxy tunnel failed)

**受影響的計算**:
- MACD、RSI14、Bollinger %B
- MA20/MA50/MA200
- Support/Resistance 水平
- ATR14
- 動量指標 (1m/3m/6m/12m returns)

由於無法從資料來源取得 HON 的歷史價格數據，無法進行技術面分析。

建議在網絡連接恢復後重試。

---

MARKET REPORT COMPLETE
