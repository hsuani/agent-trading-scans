# 技術分析 — WDC 截至 2026-09-02

## 資料狀態
**PRICE_DATA_UNAVAILABLE**

無法從 Yahoo Finance 取得 WDC 價格資料。系統代理連線被拒 (CONNECT tunnel failed 403)。

## 代理狀態
- 連線目標: query2.finance.yahoo.com, guce.yahoo.com, fc.yahoo.com
- 錯誤代碼: CONNECT tunnel failed (curl 403)
- 代理政策: egress proxy denied the CONNECT request

## 技術分析無法執行
缺少必要的價格資料，無法計算：
- 移動平均線 (MA20, MA50, MA200)
- RSI14, MACD, Bollinger Bands
- ATR, 波動率
- 支撐 / 阻力位
- 交易訊號

---

**Market signal: FAIL**

無法完成市場報告 — 資料源不可用。
