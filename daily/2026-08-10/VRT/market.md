# 技術分析 — VRT 截至 2026-08-10

## 狀態
**PRICE_DATA_UNAVAILABLE**

無法取得即時價格數據。代理代理伺服器封鎖對 Yahoo Finance (fc.yahoo.com) 的連線，傳回 403 政策拒絕。

已進行五次連線重試（含指數退避），所有嘗試均失敗。

## 已嘗試的資料來源
- `ta VRT snapshot --period 2y` → RuntimeError: no history for VRT
- `ta VRT levels --period 1y` → RuntimeError: no history for VRT
- `yf VRT fast_info` → ConnectionError: CONNECT tunnel failed 403

## 無法產生之指標
由於缺乏即時價格數據，以下技術分析無法計算：
- 現價 (Current Price)
- 移動平均線 (MA20, MA50, MA200)
- 相對強弱指數 (RSI14)
- MACD 柱狀圖 (MACD Histogram)
- 布林帶 (Bollinger Bands)
- 支撐/阻力位 (Support/Resistance Levels)
- 成交量分析 (Volume Analysis)
- 動量指標 (Momentum)
- ATR14 波動性
- 52 週高/低

## 建議行動
- 驗證代理伺服器設定與 fc.yahoo.com 的連線許可
- 等待代理伺服器恢復對 Yahoo Finance 的存取
- 重新執行掃描以獲取即時技術數據

---

**市場報告狀態**: 數據取得失敗 | **報告日期**: 2026-08-10
