# 技術面分析 — 2449.TW 京元電子 截至 2026-08-08

## 快照

**數據可用性狀態**: PRICE_DATA_UNAVAILABLE

由於代理網關對 Yahoo Finance 伺服器 (fc.yahoo.com) 連線被限制 (403 政策阻擋)，無法取得價格數據。工具回傳 "possibly delisted; no price data found"，表明無法建立遠端連接。

| 欄位 | 數值 | 備註 |
|---|---|---|
| 現價 | PRICE_DATA_UNAVAILABLE | 代理連線失敗 |
| MA20 | PRICE_DATA_UNAVAILABLE | 無法計算 |
| MA50 | PRICE_DATA_UNAVAILABLE | 無法計算 |
| MA200 | PRICE_DATA_UNAVAILABLE | 無法計算 |
| RSI14 | PRICE_DATA_UNAVAILABLE | 無法計算 |
| MACD 直方圖 | PRICE_DATA_UNAVAILABLE | 無法計算 |
| ATR14 | PRICE_DATA_UNAVAILABLE | 無法計算 |
| 52 週高點 | PRICE_DATA_UNAVAILABLE | 無法取得 |
| 52 週低點 | PRICE_DATA_UNAVAILABLE | 無法取得 |

## 趨勢判讀

無法進行趨勢分析。由於無法取得 OHLCV 數據，無法評估相對於 MA20/MA50/MA200 的價格位置，以及是否形成黃金交叉或死亡交叉。

## 動能指標

無法計算。MACD、RSI14、以及多時間框架報酬均無法在無基礎價格數據的情況下推導。

## 關鍵水位

無法識別支持與阻力。無法利用本地最小值/最大值分析來確定價格走勢的關鍵阻力與支持水位。

## 波動率概況

無法評估。ATR14 與年化波動率無法在數據缺失的狀態下計算，因此無法推估日均波幅與風險敞口意涵。

## 設置評估

**狀態**: 無法進行技術設置判讀

由於完全缺乏價格歷史數據，無法判斷下列要素:
- 形態 (上升高點/下降低點、區間、突破等)
- 趨勢強度與方向
- 支持位突破或反彈確認
- 買賣信號與超買/超賣狀況

## 指標表

| 指標 | 數值 | 讀數 |
|---|---|---|
| RSI14 | PRICE_DATA_UNAVAILABLE | 無法計算 |
| MACD 直方圖 | PRICE_DATA_UNAVAILABLE | 無法計算 |
| MACD 信號線 | PRICE_DATA_UNAVAILABLE | 無法計算 |
| % 距 MA200 | PRICE_DATA_UNAVAILABLE | 無法計算 |
| Bollinger Bands %B | PRICE_DATA_UNAVAILABLE | 無法計算 |
| 1 個月報酬 | PRICE_DATA_UNAVAILABLE | 無法計算 |
| 3 個月報酬 | PRICE_DATA_UNAVAILABLE | 無法計算 |
| 6 個月報酬 | PRICE_DATA_UNAVAILABLE | 無法計算 |
| 12 個月報酬 | PRICE_DATA_UNAVAILABLE | 無法計算 |
| 最近 10 日平均成交量 | PRICE_DATA_UNAVAILABLE | 無法計算 |
| 最新成交量 | PRICE_DATA_UNAVAILABLE | 無法取得 |

## 根本原因

**連線阻擋**: 代理網關於 2026-08-07 19:43:55 UTC 起多次拒絕對 fc.yahoo.com:443 的 CONNECT 請求，原因為 "gateway answered 403 to CONNECT (policy denial or upstream failure)"。此限制防止資料工具取得任何市場數據。

---

**市場報告完成**。

*無法提供技術面分析。請確認網路連接狀態或代理政策配置。*
