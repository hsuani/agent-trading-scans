# 技術分析 — PWR（2026-09-08）

## 資料狀態

**PRICE_DATA_UNAVAILABLE**

無法檢索 PWR（Quanta Services）的市場數據。代理程序防火牆政策已封鎖 Yahoo Finance 伺服器的連線（fc.yahoo.com、query2.finance.yahoo.com），導致無法存取實時價格數據與技術指標。

## 診斷訊息

- yfinance 查詢失敗：連線被拒（403 政策拒絕）
- ticker 可能已退市或資料不可用（2 年期間內無歷史記錄）
- Pipeline/tools/ta.py 無法執行快照分析
- Pipeline/tools/yf.py 無法執行快速資訊查詢

---

**MARKET REPORT COMPLETE**
