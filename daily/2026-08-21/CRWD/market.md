# 技術分析 — CRWD (2026-08-21)

## 資料可用性狀態

**PRICE_DATA_UNAVAILABLE**

### 問題說明

無法取得 CRWD (CrowdStrike Holdings) 的技術面分析資料。

**原因**: 代理伺服器 (proxy) 對 Yahoo Finance 資料源 (fc.yahoo.com:443) 返回 HTTP 403 政策拒絕。根據系統日誌，多次嘗試在 2026-08-20 17:49:50 至 17:50:29 UTC 期間連接均遭拒。

**重試狀態**:
- `ta CRWD snapshot --period 2y` ➜ 失敗 (連結超時)
- `ta CRWD levels --period 1y` ➜ 失敗 (連結超時)
- `ta CRWD series --period 1y` ➜ 失敗 (連結超時)
- `yf CRWD fast_info` ➜ 失敗 (連結超時)
- `yf CRWD history --period 1y` ➜ 失敗 (連結超時)

### 影響

無法提供以下指標分析:
- 價格、移動平均線 (MA20, MA50, MA200)
- RSI14、MACD、布林通道 (Bollinger Bands)
- 支撑/阻力位
- 成交量確認
- ATR 波動性分析
- 動量指標

---

**報告狀態**: 資料取得失敗
**生成日期**: 2026-08-21
**資料來源**: Yahoo Finance / technical-analysis-pipeline
