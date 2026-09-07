# 技術面 — LAES（截至 2026-09-08）

## 狀態

**PRICE_DATA_UNAVAILABLE**

資料獲取失敗。Yahoo Finance 返回代理 403 連線拒絕，同時系統檢測不到該代碼的價格數據，可能已經下市。

### 錯誤詳情
- CONNECT tunnel failed (response 403) — 代理政策阻擋連線
- "$LAES: possibly delisted; no price data found (period=1y)" — 過去一年無數據
- "no history for LAES" — 技術指標無法計算

### 無法進行分析
由於無法取得基礎價格數據，技術分析無法進行：
- 無 OHLCV 數據
- 無移動平均線（MA20, MA50, MA200）
- 無動能指標（MACD, RSI14）
- 無波動率度量（ATR14, 標準差）
- 無支撐 / 阻力水位

## 建議

請確認 LAES（SEALSQ Corp.）的股票代碼和交易狀態。如代碼有誤或公司已下市，需使用正確的代碼重新分析。

---

**技術報告完成**
