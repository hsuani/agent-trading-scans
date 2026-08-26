# 技術分析 — 2408.TW (南亞科技) 截至 2026-08-27

## 數據狀態

**PRICE_DATA_UNAVAILABLE**

### 原因

無法從 Yahoo Finance 獲取即時數據。系統嘗試了多次重試（指數退避：1.5 秒、3 秒、4.5 秒、6 秒、7.5 秒），但所有請求都被代理閘道拒絕。

**錯誤詳情:**
- 錯誤碼: HTTP 403 (Forbidden)
- 主機: fc.yahoo.com:443
- 原因: 網關政策拒絕或上游故障

### 影響

由於無法獲取歷史 OHLCV 數據，以下技術指標無法計算:
- 移動平均線 (MA20, MA50, MA200)
- 相對強度指數 (RSI14)
- MACD 與訊號線
- Bollinger Bands
- ATR14 與波動率
- 動量指標 (1m/3m/6m/12m returns)
- 支撐/阻力位
- 52 周高低

## 建議

建議在以下情況下重新嘗試此分析:
1. 檢查代理/網路連線狀態
2. 確認 Yahoo Finance 服務是否恢復
3. 考慮使用替代數據來源 (如本地快取或其他財務 API)

---

**MARKET ANALYSIS COMPLETE**
