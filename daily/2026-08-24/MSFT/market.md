# 技術分析 — MSFT 於 2026-08-24

## 資料狀態

**PRICE_DATA_UNAVAILABLE**

無法取得 MSFT 的價格資料。

### 問題說明

數據工具嘗試透過 Yahoo Finance (fc.yahoo.com) 取得歷史 OHLCV 資料與技術指標，但代理伺服器返回 HTTP 403 連線失敗。

- `python3 pipeline/tools/ta.py MSFT snapshot` ：多次重試後均失敗 (CONNECT tunnel failed)
- `python3 pipeline/tools/yf.py MSFT fast_info` ：連線被代理伺服器拒絕 (HTTP 403)

### 影響

無法進行以下技術分析：
- 價格與移動平均線對比（MA20、MA50、MA200）
- 動量指標（RSI14、MACD）
- 波隆帶 (Bollinger Bands) ％B
- 支撐與阻力位
- 波動率檔案
- ATR 計算

## 建議

待代理伺服器恢復與 Yahoo Finance 的連線後，重新執行技術分析。

---

MARKET REPORT COMPLETE
