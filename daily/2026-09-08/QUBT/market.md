# 技術面分析 — QUBT (2026-09-08)

## 資料狀態

**PRICE_DATA_UNAVAILABLE**

### 錯誤詳情

Yahoo Finance 無法取得 QUBT 的市場數據。連線失敗的詳情如下：

- **代理連線狀態**: 組織政策拒絕連接至 query2.finance.yahoo.com、fc.yahoo.com、guce.yahoo.com
- **HTTP 狀態碼**: 403 (Forbidden)
- **curl 錯誤代碼**: (7) CONNECT tunnel failed
- **重試次數**: 多次重試均失敗，無法取得行情、技術指標、支撐/阻力位

### 可能原因

1. **股票可能已下市**: 工具輸出提示 "possibly delisted"
2. **資料服務中斷**: Yahoo Finance 端點暫時無法訪問
3. **網路政策限制**: 代理伺服器組織政策阻止對 Yahoo Finance 的連接

### 後續建議

- 確認 QUBT 的交易所上市狀態
- 檢查替代資料來源的可用性
- 待網路連線恢復後重新執行分析

---

**MARKET REPORT COMPLETE**
