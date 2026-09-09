# 技術面分析 — 2344.TW（華邦電）於 2026-09-10

## 資料狀態

**PRICE_DATA_UNAVAILABLE**

經由目前代理伺服器無法存取 Yahoo Finance 的台灣股票行情資料（HTTP 403 拒絕存取）。

執行命令：
- `python3 /home/user/agent-trading-scans/pipeline/tools/ta.py 2344.TW snapshot --period 2y`
- `python3 /home/user/agent-trading-scans/pipeline/tools/yf.py 2344.TW fast_info`

結果：連接遭組織政策拒絕，query2.finance.yahoo.com、guce.yahoo.com、finance.yahoo.com 等 Yahoo Finance 端點無法訪問。

## 限制

由於無法取得即時價格數據，以下指標無法計算並報告：

- 現價 (Price)
- 移動平均線 (MA20, MA50, MA200)
- 相對強弱指標 (RSI14)
- MACD 及其信號線與柱狀圖
- 布林帶 (%B)
- 平均真實波幅 (ATR14)
- 本益比及其他基本面指標
- 支撐與阻力位
- 成交量確認

無法進行有效的技術面分析。

---

**MARKET REPORT COMPLETE**
