# 技術分析 — HON 於 2026-07-28

## 狀態

**PRICE_DATA_UNAVAILABLE**

無法取得實時價格數據。

## 根本原因

代理網關於 2026-07-27 至 2026-07-28 期間持續阻止對 fc.yahoo.com:443 的連接，返回 403 策略拒絕。這是上游政策限制，無法繞過。

## 影響

無法取得以下數據：
- 現價 (PRICE)
- 移動平均線 (MA20, MA50, MA200)
- 相對強度指數 (RSI14)
- MACD 及信號線
- 布林帶指標 (Bollinger Bands, %B)
- 均量 (ATR14, volume)
- 52 週高低點
- 支撐與阻力水位
- 所有技術指標

## 結論

無法進行 HON 技術分析，直到價格數據連接恢復。

---

**MARKET REPORT INCOMPLETE — DATA UNAVAILABLE**
