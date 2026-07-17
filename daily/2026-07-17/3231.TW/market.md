# 技術分析 — 3231.TW 於 2026-07-17

## 資料狀態

**PRICE_DATA_UNAVAILABLE**

無法連接 Yahoo Finance 以取得 3231.TW (緯創資通) 的價格與技術指標數據。

### 錯誤詳情
- 代理連線失敗: HTTP 403 CONNECT tunnel failed
- 兩個數據源 (pipeline/tools/ta.py 與 pipeline/tools/yf.py) 均無法取得歷史行情
- 無法計算移動平均線、MACD、RSI 等技術指標

### 後續建議
請檢查：
1. 代理伺服器連接狀態
2. Yahoo Finance 對台灣股票 (TW) 資料的可用性
3. 網路連線設置 (/root/.ccr/README.md)

**報告無法完成**——未發明任何價格數據，符合規範。

---

MARKET REPORT INCOMPLETE — PRICE_DATA_UNAVAILABLE
