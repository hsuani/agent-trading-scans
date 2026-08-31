# 技術分析 — RGTI（2026年9月1日）

## 快照
**PRICE_DATA_UNAVAILABLE** — 無法從數據源取得價格資訊

所有價格欄位均無法擷取：
- 現價：PRICE_DATA_UNAVAILABLE
- MA20：PRICE_DATA_UNAVAILABLE
- MA50：PRICE_DATA_UNAVAILABLE
- MA200：PRICE_DATA_UNAVAILABLE
- RSI14：PRICE_DATA_UNAVAILABLE
- MACD 直方圖：PRICE_DATA_UNAVAILABLE

## 趨勢
由於無法連接數據源（HTTP 403 — 代理政策限制），無法判定當前價格趨勢。無法比較價格與移動平均線（MA20/MA50/MA200）的相對位置，故無法判定上升、下降或盤整趨勢。

## 動量指標
無法計算以下動量指標：
- MACD 線、信號線與直方圖
- RSI14 水準（超買/超賣判定）
- 1個月、3個月、6個月、12個月回報率

## 關鍵水位
- 阻力：PRICE_DATA_UNAVAILABLE
- 支撐：PRICE_DATA_UNAVAILABLE
- 52週高低點：PRICE_DATA_UNAVAILABLE
- 建議止損水位：PRICE_DATA_UNAVAILABLE

## 波動率特徵
- ATR14 日平均波幅：PRICE_DATA_UNAVAILABLE
- 年化波動率：PRICE_DATA_UNAVAILABLE
- 預期日內移動幅度：PRICE_DATA_UNAVAILABLE

## 設置評估
無法進行技術面設置評估。數據源不可用導致無法判定以下因素：
- 價格形態（高點升高、低點升高、突破等）
- 上升或下降趨勢的強度
- 技術面超買或超賣狀況

## 指標表
| 指標 | 數值 | 讀數 |
|---|---|---|
| RSI14 | PRICE_DATA_UNAVAILABLE | 無法判定 |
| MACD 直方圖 | PRICE_DATA_UNAVAILABLE | 無法判定 |
| 距 MA200 百分比 | PRICE_DATA_UNAVAILABLE | 無法判定 |
| BB %B | PRICE_DATA_UNAVAILABLE | 無法判定 |
| 成交量（10日均值對比） | PRICE_DATA_UNAVAILABLE | 無法判定 |

## 資料狀況報告
- **錯誤代碼**：HTTP 403 CONNECT tunnel failed
- **原因**：代理政策限制對 Yahoo Finance 服務的連接（query2.finance.yahoo.com、guce.yahoo.com、fc.yahoo.com）
- **影響**：無法取得 RGTI 的歷史價格數據或即時報價
- **時間戳記**：2026-09-01

---

MARKET ANALYSIS COMPLETE
