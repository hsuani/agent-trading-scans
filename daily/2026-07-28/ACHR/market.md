# PRICE_DATA_UNAVAILABLE

## 技術分析 — ACHR (Archer Aviation) 2026-07-28

### 資料取得失敗

無法獲取 ACHR 的即時價格資料。錯誤如下：

1. **網路連接問題**: 代理伺服器傳回 403 錯誤
   - 錯誤: `curl: (56) CONNECT tunnel failed, response 403`
   - 原因: 通過預設代理伺服器的連接失敗

2. **股票狀態**: ACHR 可能已下市
   - 工具回報: `ACHR: possibly delisted; no price data found (period=1y)`
   - 無可用的歷史價格資料

### 無法執行的分析

由於缺乏實時價格資料，無法計算以下指標：
- MACD (Moving Average Convergence Divergence)
- RSI-14 (Relative Strength Index)
- MA-20 / MA-50 / MA-200 (Moving Averages)
- Bollinger Bands
- ATR-14 (Average True Range)
- 支撐 / 阻力位
- 成交量分析
- 動量指標

### 建議行動

請確認：
1. ACHR 的股票代碼是否正確
2. 該股票是否仍在市場上交易
3. 網路連接和代理設定是否正常

**無法生成技術分析報告**

---

**報告日期**: 2026-07-28  
**資料狀態**: 不可用 (PRICE_DATA_UNAVAILABLE)
