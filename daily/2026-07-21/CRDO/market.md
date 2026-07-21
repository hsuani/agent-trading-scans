# 技術分析 — CRDO (2026-07-21)

## 資料可用性狀態

**PRICE_DATA_UNAVAILABLE**

資料工具 (pipeline/tools/ta.py 及 pipeline/tools/yf.py) 在嘗試檢索 CRDO 的歷史價格數據時，遇到 HTTP 403 CONNECT tunnel 錯誤。Yahoo Finance 代理連接失敗，無法取得：
- 快照數據 (snapshot)
- 快速信息 (fast_info)
- 歷史 OHLCV
- 技術指標

## 訊息

該錯誤可能表示：
1. **代理連接問題** — 數據工具無法通過配置的代理建立安全連接
2. **股票代碼問題** — CRDO 可能已被下市或無可用的即時數據

## 無法進行的分析項目

由於缺少價格數據，以下分析無法進行：
- 趨勢判斷 (MA20, MA50, MA200)
- 動量指標 (MACD, RSI14, BB %B)
- 支撐/阻力位識別
- 波動率分析 (ATR, 年化波動率)
- 52 週高低點
- 技術設置評估

## 後續建議

1. 驗證 CRDO 代碼有效性及上市狀態
2. 檢查代理配置和網路連接
3. 確認 Yahoo Finance 資料可用性
4. 若代碼有效，稍後重試資料檢索

---

**MARKET ANALYSIS COMPLETE**
