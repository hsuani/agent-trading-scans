# 技術分析 — SO (南方公司) 截至 2026-08-11

## 狀態報告

**PRICE_DATA_UNAVAILABLE**

## 詳細說明

無法取得 SO (Southern Company) 的實時價格資料。

### 原因
組織出站政策已阻止連線至 Yahoo Finance (fc.yahoo.com:443)，返回 403 (policy denial)。已嘗試多次重試，均遭拒。備用資料來源 (CNYES API) 亦遭同一政策阻止。

### 技術細節
- 主要資料源: `yfinance` → Yahoo Finance — **已被政策阻止**
- 備用資料源: CNYES 公開 API — **已被政策阻止**
- 重試次數: 5 次 (指數退避: 1.5s, 3s, 4.5s, 6s, 7.5s)
- 所有嘗試都返回 HTTP 403 Forbidden

### 無法提供的指標
- 價格 (Price)
- 移動平均線 (MA20, MA50, MA200)
- RSI14
- MACD (線, 訊號線, 柱狀圖)
- 布林帶 (Bollinger Bands) 與 %B
- ATR14
- 動量 (1m/3m/6m/12m 報酬)
- 支持與阻力位
- 成交量確認

## 建議行動

1. 聯繫組織網路/政策管理員，要求解除對 Yahoo Finance 的出站政策阻止
2. 確認 fc.yahoo.com 是否在組織允許清單中
3. 待政策解除後重新執行技術分析報告

---

**市場報告已完成** — 等待資料來源存取權恢復。
