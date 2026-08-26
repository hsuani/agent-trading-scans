# 技術分析 — SH (ProShares Short S&P 500) 至 2026-08-22

## 數據狀態
**PRICE_DATA_UNAVAILABLE**

無法取得即時價格數據。代理機構的 HTTPS 代理在 2026-08-21 17:50+ 時段持續封鎖 Yahoo Finance (fc.yahoo.com:443) 的連接，回傳 403 政策拒絕。ta.py 和 yf.py 數據工具因此無法檢索 SH 的歷史行情及技術指標。

## 影響範圍
無法計算下列指標：
- MACD、RSI14、Bollinger Bands、ATR14
- MA20、MA50、MA200
- 支撐/阻力位 (Local highs/lows)
- 52週高低點
- 成交量分析
- 動量指標 (1m/3m/6m/12m return)

## 分析推遲
待網路連接恢復後，建議重新執行完整技術掃描。

---

**MARKET REPORT INCOMPLETE — PRICE_DATA_UNAVAILABLE**
