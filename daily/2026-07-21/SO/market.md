# 技術分析 — SO (南方公司) 截至 2026-07-21

## 數據可用性狀態

**PRICE_DATA_UNAVAILABLE**

### 原因

無法連接至價格數據源。組織出境政策阻止了以下主機：
- `fc.yahoo.com` (Yahoo Finance)
- `ws.api.cnyes.com` (財經資料源)

`pipeline/tools/ta.py` 與 `pipeline/tools/yf.py` 工具因 403 Forbidden (政策拒絕) 而失敗，無法獲取實時價格、技術指標、支撐/阻力水平或成交量數據。

### 需要的數據

為完成 SO (南方公司) 的完整技術分析，需要以下數據：
- **快照** (Snapshot): 最新價格、MA20/MA50/MA200、RSI14、MACD、Bollinger Bands
- **系列數據** (Series): 過去 60 根柱線的 OHLCV + 所有技術指標
- **關鍵水位** (Levels): 1 年期內的本地支撐與阻力
- **基礎價格資訊** (Fast Info): 當前價格、50 日與 200 日均線、52 週高低點

### 後續步驟

1. 請聯繫網絡管理員，要求允許組織出境政策存取 `fc.yahoo.com` 與相關財經數據源
2. 或使用已獲授權的替代數據源進行技術分析
3. 待數據源可用後，可重新執行此分析

---

**報告生成時間**: 2026-07-21
**市場報告狀態**: DATA_UNAVAILABLE

