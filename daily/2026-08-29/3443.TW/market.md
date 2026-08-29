# 技術面分析 — 3443.TW（截至 2026-08-29）

## 狀態

**PRICE_DATA_UNAVAILABLE**

無法取得 3443.TW 的價格數據。yfinance 連接失敗（代理 403 CONNECT tunnel failed），data provider 無法返回歷史 OHLCV 數據或即時行情。

## 原因

1. 代理網路限制：對 Yahoo Finance endpoints（query2.finance.yahoo.com, guce.yahoo.com, fc.yahoo.com）的連接被拒絕
2. Cookie/crumb 驗證失敗
3. 無法檢索股票歷史報價

## 無法完成的分析項目

- 快照數據（當前價格、MA20/MA50/MA200、RSI14、MACD）
- 52 週高低點
- 技術指標（Bollinger Bands、ATR、成交量分析）
- 支撑/阻力位

## 建議

等待網路連接恢復後重新執行分析。3443.TW（創意電子）可能需要透過不同的數據源（如台灣證交所直接 API、本地數據庫或替代金融 data provider）取得報價。

---

**MARKET REPORT COMPLETE** — 無可用市場數據
