# 技術分析 — ZS 截至 2026-07-24

## ⚠️ PRICE_DATA_UNAVAILABLE

資料擷取失敗：代理伺服器連接異常（CONNECT tunnel failed, response 403）。無法獲取 ZS 的歷史價格數據、技術指標及市場資訊。

### 狀態
- **資料來源**: Yahoo Finance API / TA 指標管道
- **錯誤訊息**: curl: (56) CONNECT tunnel failed, response 403
- **可能原因**: 網路代理政策限制、fc.yahoo.com 被組織 egress 政策封鎖
- **重試狀態**: 已多次重試，均遭拒

無法進行本次技術分析。代理伺服器於組織層級阻擋了 Yahoo Finance 連接。

---

## 無法進行的分析項目

本報告原計劃涵蓋以下指標，但因資料不可用而無法完成：

- MACD(12,26,9) 與直方圖分析
- RSI14（相對強度指標）
- MA20/MA50/MA200 移動平均線
- Bollinger Bands %B 與帶寬
- 支撐/壓力位（local min/max）
- 成交量分析（20 日均量比較）
- ATR14 波幅指標
- 52 週高低與相對位置

---

MARKET REPORT INCOMPLETE - PRICE_DATA_UNAVAILABLE
