# 技術面分析 — GFS 截至 2026-07-27

## 資料狀態

**PRICE_DATA_UNAVAILABLE**

無法獲取 GFS (GlobalFoundries) 之價格與技術指標數據。

### 原因

代理伺服器已阻止連接至 Yahoo Finance (fc.yahoo.com:443)，返回 HTTP 403 政策拒絕。經過 5 次重試及退避後仍無法取得資料。

### 影響

以下技術面分析無法進行:
- 即時股價與 52 週高低價
- 移動平均線 (MA20, MA50, MA200)
- 相對強弱指數 (RSI14)
- MACD 動能指標
- 波林傑帶 (Bollinger Bands)
- 平均真實波幅 (ATR14)
- 支撐/阻力價位
- 波動率與動能指標

## 建議

- 請核實 GFS 代碼有效性
- 確認市場資料連線狀態
- 待代理政策更新後重新執行掃描

---

**MARKET REPORT COMPLETE**

報告日期: 2026-07-27
資料狀態: PRICE_DATA_UNAVAILABLE
