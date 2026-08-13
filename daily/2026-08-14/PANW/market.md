# 技術分析 — PANW 截至 2026-08-14

## 資料狀態

**PRICE_DATA_UNAVAILABLE**

無法取得技術分析資料。Yahoo Finance 資料源被代理伺服器策略阻擋（HTTP 403）。管道工具 `ta.py` 和 `yf.py` 均無法連接至 fc.yahoo.com。

### 連線診斷

- **代理狀態**: 啟用
- **被阻擋主機**: fc.yahoo.com:443 (policy denial)
- **失敗時間戳**: 2026-08-13 21:54:16 UTC 至 2026-08-13 21:56:52 UTC (多次重試均失敗)
- **來源**: pipeline/tools/ta.py PANW snapshot --period 2y
- **備用來源**: pipeline/tools/yf.py PANW fast_info (亦不可用)

### 無法提供的指標

由於缺少價格數據，無法計算以下技術指標：

| 指標 | 狀態 |
|---|---|
| 現價 | 不可用 |
| MACD | 不可用 |
| RSI14 | 不可用 |
| 移動平均線 (MA20/MA50/MA200) | 不可用 |
| 布林帶 (%B, 寬度) | 不可用 |
| ATR14 | 不可用 |
| 支撐/阻力位 | 不可用 |
| 波動率 | 不可用 |

## 建議行動

1. 等待代理策略調整以允許 Yahoo Finance 連接
2. 採用替代資料源（如果可用）
3. 手動從金融網站取得 PANW 價格和技術數據，然後重新分析

---

**技術分析報告完成** — 資料不可用狀態
