# GLD 技術分析 — 2026-08-22

## PRICE_DATA_UNAVAILABLE

Yahoo Finance (fc.yahoo.com) 出站連線被組織政策 403 封鎖，無法取得 GLD 即時價格數據及技術指標。

**代理政策狀態：** fc.yahoo.com:443 連線被拒絕（gateway policy denial）
**可用工具：** ta.py snapshot / series / levels、yf.py fast_info
**數據來源：** Yahoo Finance API（無法存取）

### 無法計算的指標

| 指標 | 狀態 | 原因 |
|---|---|---|
| RSI14 | N/A | 缺少價格數據 |
| MACD | N/A | 缺少歷史日線 |
| MA50 / MA200 | N/A | 缺少移動平均基礎 |
| Bollinger Bands | N/A | 缺少波動率計算 |
| 支撐 / 阻力位 | N/A | 缺少本地極值分析 |
| 52 週高低 | N/A | 缺少年度範圍數據 |
| 成交量趨勢 | N/A | 缺少成交量序列 |

### 技術信號狀況

- **趨勢方向：** 無法判斷（無價格走勢）
- **動量強度：** 無法計算（無指標）
- **超買/超賣：** 無法評估（RSI、BB %B 不可計算）
- **波動率特徵：** 無法分析（ATR、年化波動率不可得）
- **整固 vs 趨勢：** 無法區分（缺少形態分析基礎）

### 建議

下游 Trader / Portfolio Manager 不得基於此報告發明進出場價位或停損水位。final_decision 應標記「**無即時價格數據，暫不給進出場建議**」。

---

**MARKET REPORT COMPLETE** — 受網路政策限制
