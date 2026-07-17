# 技術分析 — QUBT 截至 2026-07-17

## PRICE_DATA_UNAVAILABLE

### 資料取得失敗

代理閘道對 fc.yahoo.com (Yahoo Finance) 的 CONNECT 請求被拒絕 (403 政策限制)。技術分析工具無法檢索 QUBT 的價格歷史記錄。

### 嘗試方法
- `ta QUBT snapshot` - 失敗
- `ta QUBT series --period 6m` - 失敗  
- `yf QUBT fast_info` - 失敗

所有請求均返回代理層級的連線拒絕，無法取得交易資料。

MARKET REPORT COMPLETE
