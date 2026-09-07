# 技術面分析 — RGTI (2026-09-08)

## 資料狀態

**PRICE_DATA_UNAVAILABLE**

Yahoo Finance 連線失敗（HTTP 403 - 代理政策拒絕連線）。多次重試均無法取得 RGTI 的歷史價格資料。系統指示該代號可能已下市或無法訪問。

## 無法進行分析

由於無法取得價格資料，以下指標無法計算：
- 即時價格 (Price)
- 移動平均線 (MA20, MA50, MA200)
- 相對強弱指數 (RSI14)
- MACD 及其信號線
- 波林傑帶 (Bollinger Bands)
- ATR 波動率
- 支撐與阻力位
- 其他技術指標

## 建議

請驗證：
1. 代號 RGTI 是否在交易所上市
2. 該公司是否已下市或更改代號
3. 代理連線設定是否需要調整

---
**MARKET REPORT INCOMPLETE - DATA UNAVAILABLE**
