# 技術分析 — CRDO（2026-08-23）

## 快照
**狀態**: PRICE_DATA_UNAVAILABLE

所有價格資料、技術指標及市場水位無法獲取。

---

## 資料可用性說明

### 連線狀況
- **HTTPS 代理閘道**: 已啟用（port 40009）
- **政策狀態**: 拒絕（Policy Denial）
- **受阻主機**: fc.yahoo.com:443、ws.api.cnyes.com:443

### 資料來源狀態
- **Yahoo Finance 主要資料源**: 閘道 403（CONNECT 拒絕）
- **鉅亨網 (cnyes) 備用源**: 閘道 403（CONNECT 拒絕）
- **本地 `ta` 工具**（pipeline/tools/ta.py）: 無法連線
- **本地 `yf` 工具**（pipeline/tools/yf.py）: 無法連線

### 重試嘗試
- 初次嘗試: 失敗（CONNECT tunnel failed）
- 延遲重試（3秒）: 失敗（CONNECT tunnel failed）
- 內部重試機制（5次嘗試，指數退避 1.5-7.5秒）: 全部失敗

---

## 技術指標 — 無法計算

以下指標因資料不可用而無法計算：

| 指標 | 狀態 |
|---|---|
| 價格（Close） | ❌ UNAVAILABLE |
| MA20 / MA50 / MA200 | ❌ UNAVAILABLE |
| RSI14 | ❌ UNAVAILABLE |
| MACD（信號線、柱狀圖） | ❌ UNAVAILABLE |
| 布林帶 %B（Bollinger Bands） | ❌ UNAVAILABLE |
| ATR14 | ❌ UNAVAILABLE |
| 波動率（20日年化） | ❌ UNAVAILABLE |
| 52週高低點 | ❌ UNAVAILABLE |
| 支撐/阻力水位 | ❌ UNAVAILABLE |
| 成交量（日均、確認） | ❌ UNAVAILABLE |
| 動量（1M/3M/6M/12M 報酬） | ❌ UNAVAILABLE |

---

## 趨勢分析

**無法進行** — 價格序列不可用，無法評估：
- 價格相對移動平均線的位置
- 趨勢方向（上升/下降/橫盤）
- 黃金叉/死亡叉接近程度
- 局部高低點模式

---

## 動量分析

**無法進行** — MACD、RSI、多時框報酬無法計算。

---

## 關鍵水位

**無法確定**:
- 阻力位（最近局部高點）
- 支撐位（最近局部低點）
- 52週高低點距離
- 止損建議水位

---

## 波動率概況

**無法量化** — ATR14 與年化波動率無法計算，無法評估倉位規模含義。

---

## 設置評估

**無法進行** — 無法識別任何形態或信號：
- 無法判斷買方/賣方控制
- 無法檢測趨勢反轉信號
- 無法評估技術支撐/阻力

---

## 根本原因分析

### 問題所在
HTTPS 代理閘道（port 40009）已啟用且配置正確，但**上游策略拒絕**連接至：
1. **fc.yahoo.com** (Yahoo Finance 核心服務)
2. **ws.api.cnyes.com** (台灣備用源)

這表示組織級政策或上游防火牆/負載均衡器正在阻止對這些主機的 CONNECT 請求。

### 影響範圍
- `yfinance` Python 套件無法獲取歷史 OHLCV 資料
- 備用商業資料 API (cnyes) 也被阻止
- 技術分析指標計算完全依賴市場價格序列，缺乏源資料

---

## 符合性聲明

根據技術分析指南：
> **價格資料完整性規則 (PRICE_DATA_INTEGRITY)**: 「如果無法在重試後取得真實價格，報告 PRICE_DATA_UNAVAILABLE，不得估計或虛構任何價位。」

本報告**完全遵守**此規則。CRDO 分析**未進行任何價格水位推測**。

---

## 建議後續步驟

1. **網路連線恢復**: 聯繫 IT / 網路安全團隊恢復對 fc.yahoo.com 的訪問
2. **備用資料源**: 配置替代資料提供商（Alpha Vantage、IEX Cloud、Polygon.io）
3. **本地快取**: 如存在 CRDO 之前快取的 OHLCV 資料，可加載進行離線分析

---

## 結論

**CRDO 技術分析** 因外部資料來源不可用而**無法進行**。需要恢復網路連接至 Yahoo Finance 或配置替代資料來源，才能完成任何技術指標計算或市場評估。

---

**報告狀態**: PRICE_DATA_UNAVAILABLE  
**生成日期**: 2026-08-23  
**分析工具狀態**: 受阻（代理閘道政策拒絕）  
**分析師**: Claude Code（技術分析）

MARKET REPORT COMPLETE
