# 市場技術面分析 — 3017.TW 奇鋐科技
**分析日期**: 2026-09-09  
**分析師**: Market Analyst  

---

## PRICE_DATA_UNAVAILABLE

> yfinance 因 egress proxy 封鎖（connect_rejected / 403）無法取得即時或歷史價格數據。  
> `python3 pipeline/tools/ta.py 3017.TW snapshot` → error: no history  
> `python3 pipeline/tools/yf.py 3017.TW fast_info` → ConnectionError 403  
> 本報告所有技術指標（RSI、MACD、MA、Bollinger Band）均無法計算。  
> 下游交易員（Trader）**不得**捏造進出場價位。

---

## 技術面評分

| 指標 | 狀態 |
|------|------|
| RSI14 < 72 | SKIP（無數據） |
| MACD 非深度負值 | SKIP（無數據） |
| Price > MA50 | SKIP（無數據） |

**市場訊號**: SKIP（PRICE_DATA_UNAVAILABLE）

---
*價格數據不可用，技術指標跳過評分*
