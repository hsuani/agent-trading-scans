# 技術分析 — QUBT (2026-07-21)

## 市場數據狀態

**PRICE_DATA_UNAVAILABLE**

無法取得 QUBT 的價格及技術指標數據。fc.yahoo.com 連線故障（HTTP 403）。

### 故障詳情
- 連線嘗試返回 CONNECT tunnel failed，HTTP 403
- yfinance 無法檢索 QUBT 的歷史數據
- MACD、RSI14、Bollinger %B、MA20/50/200、ATR14、支撐/阻力水位無法計算

### 影響指標
所有技術分析指標暫時無法提供：
- 移動平均線 (MA20, MA50, MA200)
- 相對強弱指數 (RSI14)
- MACD 及其柱狀圖
- 布林帶 %B
- 平均真實波幅 (ATR14)
- 動量 (1m/3m/6m/12m returns)
- 支撐/阻力水位
- 成交量確認

### 建議
請稍後重試。若問題持續，可能需要檢查網路連線或數據提供商的服務狀態。

---

MARKET REPORT COMPLETE
