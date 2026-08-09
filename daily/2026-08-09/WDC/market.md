# 技術面 — WDC 截至 2026-08-09

## 狀態

**PRICE_DATA_UNAVAILABLE**

無法取得 WDC 的價格數據。連接錯誤（HTTP 403 代理回應）。

### 技術詳情

- 數據來源：pipeline/tools/ta.py (snapshot) 和 pipeline/tools/yf.py (fast_info)
- 錯誤類型：CONNECT tunnel failed, curl error (7)
- 代理狀態：403 Forbidden
- 結論：無法檢索任何價格水平、技術指標或支撐/阻力位

未生成的分析項目：
- 快照（當前價格、MA20、MA50、MA200、RSI14、MACD）
- 趨勢判斷
- 動量指標
- 關鍵價位
- 波動率分析
- 設置評估
- 指標表

---

**MARKET REPORT INCOMPLETE — PRICE_DATA_UNAVAILABLE**
