# 技術面 — NBIS (Nebius Group) 截至 2026-07-17

## 數據可用性通知

**PRICE_DATA_UNAVAILABLE**

技術分析無法進行。Yahoo Finance 資料源因代理 HTTP 403 Forbidden 錯誤而被阻擋。系統嘗試多次從以下來源檢索 NBIS (Nebius Group) 的價格和技術指標數據，但均失敗：

- `ta NBIS snapshot --period 2y` — 失敗
- `ta NBIS series --period 1y` — 失敗
- `ta NBIS levels --period 1y` — 失敗
- `yf NBIS fast_info` — 失敗
- `yf NBIS history --period 1y` — 失敗

錯誤訊息：`curl: (56) CONNECT tunnel failed, response 403`

## 可用的數據

無。

## 無法提供的分析

以下分析項目無法完成，因缺乏即時市場數據：

| 指標 | 數據 | 備註 |
|---|---|---|
| 現價 | PRICE_DATA_UNAVAILABLE | - |
| MA20 | PRICE_DATA_UNAVAILABLE | - |
| MA50 | PRICE_DATA_UNAVAILABLE | - |
| MA200 | PRICE_DATA_UNAVAILABLE | - |
| RSI14 | PRICE_DATA_UNAVAILABLE | - |
| MACD 直線 vs 信號 | PRICE_DATA_UNAVAILABLE | - |
| MACD 柱狀圖 | PRICE_DATA_UNAVAILABLE | - |
| ATR14 | PRICE_DATA_UNAVAILABLE | - |
| 布林帶 %B | PRICE_DATA_UNAVAILABLE | - |
| 年化波動率 | PRICE_DATA_UNAVAILABLE | - |
| 52周高 | PRICE_DATA_UNAVAILABLE | - |
| 52周低 | PRICE_DATA_UNAVAILABLE | - |
| 支撐位 | PRICE_DATA_UNAVAILABLE | - |
| 阻力位 | PRICE_DATA_UNAVAILABLE | - |

## 趨勢分析

無法進行。缺乏 OHLCV 數據和技術指標以評估價格對移動平均線的相對位置。

## 動能分析

無法進行。缺乏 MACD、RSI 和多時間框架收益率數據。

## 關鍵價位

無法識別。本地高點和低點分析需要完整的歷史價格序列。

## 波動率概況

無法計算。缺乏 ATR14 和歷史價格區間數據。

## 技術面設置

無法確定。缺乏足夠的市場數據進行方向性或模式分析。

---

**報告狀態**：技術分析報告無法完成。數據檢索失敗。

**MARKET REPORT COMPLETE** (不完整 - 數據源不可用)

---

*報告生成時間*：2026-07-17  
*代理人*：技術/市場分析師  
*系統*：Agent Trading Scans 技術分析管線
