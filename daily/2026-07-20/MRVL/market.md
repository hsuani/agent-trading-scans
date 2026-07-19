# 技術分析 — MRVL 截至 2026-07-20

## 資料可用性

**狀態：PRICE_DATA_UNAVAILABLE**

### 檢索失敗詳情

無法取得 MRVL 的技術數據。多次重試後，所有資料來源連線均遭網路閘道阻止。

- **根本原因**：代理網路閘道對 fc.yahoo.com:443 返回 403 政策拒絕
- **影響**：無法檢索歷史 OHLCV 數據、技術指標、支撐/阻力位
- **嘗試的工具**：
  - `ta.py MRVL snapshot --period 2y`
  - `ta.py MRVL series --period 1y`
  - `ta.py MRVL levels --period 1y`
  - `yf.py MRVL fast_info`

### 分析時間

- **報告日期**：2026-07-20
- **資料截至**：N/A（無資料）

### 結論

未能進行 MRVL 的技術分析。建議在網路連線恢復後重新執行掃描。

---

**MARKET REPORT COMPLETE**
