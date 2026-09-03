# 技術分析 — ZS (Zscaler) 截至 2026-09-04

## 資料狀態

**PRICE_DATA_UNAVAILABLE**

無法獲取 ZS 的實時價格數據。代理伺服器政策限制了對 Yahoo Finance 的連接 (403 Connect Rejected)。

### 錯誤詳情

- 資料來源：Yahoo Finance API 不可達
- 代理政策：組織策略拒絕連接至 query2.finance.yahoo.com, guce.yahoo.com, fc.yahoo.com
- 工具呼叫：pipeline/tools/yf.py 和 pipeline/tools/ta.py 均無法執行
- 重試狀態：已嘗試多次，無法解決連接問題

### 無法進行的分析

由於缺乏實時市場數據，無法提供以下指標：

- **快照資訊**：當前股價、MA20、MA50、MA200
- **動量指標**：RSI14、MACD、MACD 直方圖
- **波林傑帶**：%B、上軌、下軌
- **支撐/阻力位**：本地高點、本地低點
- **成交量**：10 日均量、最近成交量
- **波動率**：ATR14、年化波動率
- **趨勢分析**：移動平均線交叉、價格相對位置

---

## 建議

技術分析報告無法完成，直到能夠取得實時市場數據為止。請：

1. 檢查網路連接和代理設定
2. 確認組織政策是否允許訪問財務數據源
3. 或嘗試備用數據源（如支持的 API）

---

**MARKET REPORT INCOMPLETE — PRICE_DATA_UNAVAILABLE**
