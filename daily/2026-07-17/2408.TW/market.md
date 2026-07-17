# 技術面 — 2408.TW (南亞科技) 截至 2026-07-17

## 快照 (Snapshot)

**PRICE_DATA_UNAVAILABLE**

Yahoo Finance 資料來源因代理伺服器 HTTP 403 限制而無法存取。無法取得以下指標：
- 現價 (Price)
- MA20、MA50、MA200
- RSI14、MACD、布林線指標
- ATR14、20日波動率
- 52週高低點
- 動量指標 (1m/3m/6m/12m returns)

## 趨勢 (Trend)

**PRICE_DATA_UNAVAILABLE** — 無法分析價格相對於移動平均線的位置，無法判斷趨勢方向 (上升/下降/橫盤) 或強度。

## 動量 (Momentum)

**PRICE_DATA_UNAVAILABLE** — MACD 訊號、RSI 水準及多時間軸報酬率無法取得。

## 關鍵水位 (Key Levels)

由於技術面資料無法存取，無法識別以下支撐與阻力水位：
- **阻力**: PRICE_DATA_UNAVAILABLE
- **支撐**: PRICE_DATA_UNAVAILABLE
- **停損建議**: PRICE_DATA_UNAVAILABLE

## 波動率波段 (Volatility Profile)

**PRICE_DATA_UNAVAILABLE** — ATR14 隱含每日波動幅及年化波動率無法計算。

## 設定 (Setup)

**PRICE_DATA_UNAVAILABLE** — 無法判斷看漲/看跌/中性觀點，無法識別技術型態 (如更高高點、破位支撐、區間盤整)。

## 指標表格 (Indicators Table)

| 指標 | 數值 | 讀數 |
|---|---|---|
| RSI14 | PRICE_DATA_UNAVAILABLE | — |
| MACD 直方圖 | PRICE_DATA_UNAVAILABLE | — |
| % 距 MA200 | PRICE_DATA_UNAVAILABLE | — |
| BB %B | PRICE_DATA_UNAVAILABLE | — |
| ATR14 | PRICE_DATA_UNAVAILABLE | — |
| 20日年化波動率 | PRICE_DATA_UNAVAILABLE | — |
| 1月報酬率 | PRICE_DATA_UNAVAILABLE | — |
| 3月報酬率 | PRICE_DATA_UNAVAILABLE | — |
| 6月報酬率 | PRICE_DATA_UNAVAILABLE | — |
| 12月報酬率 | PRICE_DATA_UNAVAILABLE | — |

## 診斷

**資料來源故障** — Yahoo Finance API 因代理限制無法連接 (curl 錯誤 56, HTTP 403 CONNECT tunnel failed)。yfinance 重試機制已耗盡 (5 次嘗試)，未能取得 2408.TW 的任何歷史價格資料。

建議次步：
1. 驗證代理設定 (`/root/.ccr/README.md`)
2. 確認 2408.TW 在 Yahoo Finance 上的可用性
3. 嘗試備用資料來源 (例：臺灣證交所、鉅亨網等)

---

**市場報告完成**

*分析日期: 2026-07-17*
*資料狀態: PRICE_DATA_UNAVAILABLE*
