# 技術分析 — QBTS 截至 2026-07-21

## PRICE_DATA_UNAVAILABLE

無法取得 QBTS (D-Wave Quantum) 的市場數據。

**原因**：proxy 返回 HTTP 403 CONNECT tunnel failed 錯誤，fc.yahoo.com 無法訪問。

**嘗試方法**：
- 執行 `ta QBTS snapshot --period 2y` → 失敗
- 執行 `ta QBTS levels --period 1y` → 失敗
- 執行 `yf QBTS fast_info` → 失敗

所有 yfinance 請求都被 proxy 攔截，無法檢索任何技術指標、價格、移動平均線、支撐/阻力位或動量數據。

## 技術指標狀態

| 指標 | 狀態 |
|---|---|
| Price (最新) | N/A |
| MA20 | N/A |
| MA50 | N/A |
| MA200 | N/A |
| RSI14 | N/A |
| MACD histogram | N/A |
| Bollinger %B | N/A |
| ATR14 | N/A |
| 支撐位 | N/A |
| 阻力位 | N/A |
| 1m/3m/6m/12m momentum | N/A |

## 趨勢判讀

無可用數據。

## 動能分析

無可用數據。

## 關鍵位點

無可用數據。

## 波動率概況

無可用數據。

## 圖形設置

無可用數據。

---

**報告狀態**：PRICE_DATA_UNAVAILABLE

**日期**：2026-07-21

MARKET REPORT COMPLETE
