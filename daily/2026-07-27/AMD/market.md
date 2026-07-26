# 技術分析 — AMD 截至 2026-07-27

## 狀態
**PRICE_DATA_UNAVAILABLE**

### 原因
無法從 Yahoo Finance (fc.yahoo.com) 及備用來源 (cnyes, TWSE) 獲取價格數據。代理閘道對所有數據源返回 403 政策拒絕。數據採集工具 ta.py 和 yf.py 在 5 次重試後均告失敗。

- fc.yahoo.com:443 — 403 CONNECT 被拒
- ws.api.cnyes.com:443 — 403 CONNECT 被拒
- TWSE API — 不適用 (AMD 非台灣股票)

### 技術條款
無法計算以下指標：
- 價格、MA20、MA50、MA200
- RSI14、MACD、BB %B
- ATR14、52週高點/低點
- 1m/3m/6m/12m 動能
- 20日年化波幅
- 支撐/阻力位

### 規程遵守
按照指示，**未發明價格或技術指標**。無法生成有效的技術分析報告。

---

**MARKET REPORT INCOMPLETE — PRICE DATA UNAVAILABLE**
