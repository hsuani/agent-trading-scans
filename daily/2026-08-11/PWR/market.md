# 技術分析 — PWR 截至 2026-08-11

## 資料狀態

**PRICE_DATA_UNAVAILABLE**

### 原因

無法取得 PWR (Quanta Services) 的價格資料。技術分析工具 (ta.py / yf.py) 對 Yahoo Finance 的連接遭到代理伺服器拒絕 (403 policy denial)。已進行多次重試，但連接持續失敗。

### 技術細節

- 工具嘗試次數：3 次重試已內建在 ta.py
- 錯誤訊息：「Failed to perform, curl: (7) CONNECT tunnel failed, response 403」
- 上游資料源：Yahoo Finance (fc.yahoo.com)
- 代理狀態：enabled，但 fc.yahoo.com 連接被網關拒絕

### 可用數據

無法檢索以下指標：
- MACD、RSI14、Bollinger Bands
- MA50、MA200
- 支撐/阻力位置 (S/R levels)
- 交易量資料
- 動量指標
- 52週高低位

---

**技術分析報告完成**

報告生成時間：2026-08-11
分析象徵：PWR
狀態：資料不可用
