# 技術分析 — AVGO 截至 2026-07-20

## 數據可用性狀態

**PRICE_DATA_UNAVAILABLE**

### 問題說明

無法取得 AVGO 的價格和技術指標數據。根據代理層日誌，組織的出口政策目前禁止訪問以下數據源：

- **fc.yahoo.com:443** (Yahoo Finance) — 網關回應 403 (政策拒絕)
- **ws.api.cnyes.com:443** (鉅亨網 API) — 網關回應 403 (政策拒絕)

此限制在組織代理層面實施，無法通過重試或迂迴方式解決。

### 影響範圍

無法執行以下分析：
- 價格快照及移動平均線 (MA20/MA50/MA200)
- 動量指標 (MACD, RSI14, 布林帶)
- 波動率分析 (ATR14, 20日年化波動率)
- 支撐/阻力位計算
- 多時間框架動量回報 (1m/3m/6m/12m)

---

## 建議行動

請聯繫系統管理員或 Anthropic 支援確認組織出口政策，並在策略允許後重新執行掃描。

**MARKET REPORT INCOMPLETE — PRICE_DATA_UNAVAILABLE**
