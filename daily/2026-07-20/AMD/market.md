# 技術面 — AMD 截至 2026-07-20

## 資料狀態

**PRICE_DATA_UNAVAILABLE**

代理網關政策拒絕連線至 Yahoo Finance (fc.yahoo.com:443)，無法取得 AMD 價格數據。技術分析工具無法檢索過去 2 年的 OHLCV 資料、指標數據或支撐阻力位。

## 故障排查

- 工具呼叫: `ta.py AMD snapshot --period 2y` → RuntimeError: no history
- 工具呼叫: `ta.py AMD series --period 1y` → RuntimeError: no history  
- 工具呼叫: `ta.py AMD levels --period 1y` → RuntimeError: no history
- 工具呼叫: `yf.py AMD fast_info` → ProxyError: connect_rejected
- 代理網關最近拒絕: 20 筆連接嘗試至 fc.yahoo.com (2026-07-19 17:50-17:51)

## 結論

無法進行技術分析，因為價格數據不可用。無法生成趨勢、動量、關鍵位或波動率分析。

---

**市場報告完成** — 資料不可用

