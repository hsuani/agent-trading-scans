# 技術分析 — FN（Fabrinet）於 2026-07-29

## 資料不可用

**PRICE_DATA_UNAVAILABLE**

## 狀態

無法取得技術分析資料。yfinance 已被組織出口政策封鎖（HTTP 403），且無可用之 WebSearch/WebFetch 工具進行替代資料取得。

### 試圖方法

1. 直接 yfinance 呼叫 → HTTP 403 Proxy Error（目標主機被組織出口政策阻止）
2. ta.py CLI 工具 → 依賴 yfinance，同樣失敗
3. yf.py CLI 工具 → 同樣 Proxy 403 錯誤
4. 直接 curl 請求 → 無回應或被代理阻止

### 需求

- 需要啟用 yfinance 存取權限，或
- 提供替代資料來源（WebSearch API、財務資料 webhook、本地快取資料），或  
- 提供 WebSearch/WebFetch MCP 工具以繞過 yfinance 限制

---

**未能生成技術分析報告**

無法計算以下指標：
- 價格、MA20/MA50/MA200
- RSI14、MACD、Bollinger Bands
- ATR14、歷史波動率
- 支撐/阻力水位
- 動量指標（1m/3m/6m/12m return）

建議由人工進行手動行情查詢或由其他系統提供實時報價資料。

---

MARKET REPORT COMPLETE
