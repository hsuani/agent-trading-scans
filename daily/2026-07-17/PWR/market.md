# 市場技術分析 — PWR（Quanta Services）截至 2026-07-17

## 狀態：PRICE_DATA_UNAVAILABLE

代理政策封鎖 Yahoo Finance (fc.yahoo.com:443)，無法獲取即時價格數據。技術指標（RSI、MACD、MA50/200、布林通道、支撐/阻力位）均無法計算。

## 影響工具

- `ta.py PWR snapshot` — 失敗（代理 403 CONNECT tunnel failed）
- `yf.py PWR fast_info` — 失敗（ProxyError 403）

## 技術信號評估

按照價格數據完整性規則，不得虛構任何價格水準或技術指標。

**市場信號：N/A**（無真實數據）

---

根本原因：組織出站政策封鎖 Yahoo Finance，非 PWR 股票問題。
