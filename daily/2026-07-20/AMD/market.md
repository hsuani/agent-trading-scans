# 技術分析 — AMD 截至 2026-07-20

## 資料可用性狀態

**PRICE_DATA_UNAVAILABLE**

### 原因

無法擷取 AMD 的價格及技術指標資料。嘗試連接 Yahoo Finance (fc.yahoo.com) 時被組織代理防火牆阻止 (HTTP 403 政策拒絕)。

### 影響

- 無法取得即時或歷史價格資料
- 無法計算技術指標 (MA20, MA50, MA200, RSI14, MACD, ATR14, BB %B)
- 無法識別支撐/阻力位置
- 無法評估動量、波動率或超買/超賣狀態

### 建議

1. 聯繫組織代理管理員，要求解除 fc.yahoo.com 的 403 政策限制
2. 檢查是否有替代資料來源可用 (公司內部市場資料庫、其他金融 API)
3. 待代理限制解除後，重新執行分析

### 資料可用性檢查時間

```
2026-07-19T21:52:42Z - 最後一次代理狀態查詢
- 阻止連接至 fc.yahoo.com:443 (10+ 次連續失敗)
- 錯誤代碼: CONNECT tunnel failed, response 403
- 原因: gateway answered 403 to CONNECT (policy denial or upstream failure)
```

---

**技術分析報告無法完成。請確保 Yahoo Finance 存取權限已解除後重新提交請求。**

## MARKET REPORT COMPLETE (資料不可用)
