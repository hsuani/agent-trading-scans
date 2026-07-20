# 技術分析 — PWR (2026-07-21)

## 狀態

**PRICE_DATA_UNAVAILABLE**

無法取得市場數據。

## 原因

組織出口網路政策阻止存取所需的市場數據源：

- Yahoo Finance (fc.yahoo.com:443) — 403 Policy Denial
- CNYES API (ws.api.cnyes.com:443) — 403 Policy Denial

這是組織級別的網路政策限制，不是暫時性故障。`ta.py` 和 `yf.py` 無法透過代理連線到任何合適的行情提供商。

## 技術指標

無法計算任何指標（MACD、RSI14、MA50/MA200、Bollinger Bands、ATR14）因為缺少基礎價格數據。

## 設置

無法評估。

## 建議

等待組織網路政策更新，允許存取市場數據源。

---

MARKET REPORT INCOMPLETE — PRICE_DATA_UNAVAILABLE
