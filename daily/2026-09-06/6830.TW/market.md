# 技術分析 — 6830.TW (汎銓科技) 截至 2026-09-06

## 資料獲取失敗

**Market Signal: FAIL**

### 錯誤詳情

資料工具無法連接 Yahoo Finance 資料源。代理伺服器拒絕 HTTPS 連線：

- `ta.py 6830.TW snapshot --period 2y`: RuntimeError - "no history for 6830.TW"
- `yf.py 6830.TW fast_info`: ConnectionError - curl (7) CONNECT tunnel failed, response 403
- `ta.py 6830.TW levels --period 1y`: RuntimeError - "no history for 6830.TW"

### 失敗原因

組織代理政策阻擋對以下網址的 CONNECT：
- query2.finance.yahoo.com:443
- finance.yahoo.com:443
- guce.yahoo.com:443
- fc.yahoo.com:443

### 影響

**PRICE_DATA_UNAVAILABLE**

無法取得：
- 現價、移動平均線（MA20, MA50, MA200）
- 相對強度指數（RSI14）
- MACD 直方圖、訊號線
- ATR 波動率
- 支撐 / 阻力位
- 52 週高低點
- 任何技術指標或市場數據

### 建議行動

1. 聯繫系統管理員檢查代理設定與 Yahoo Finance 連接權限
2. 驗證 6830.TW 在 TWSE（台灣證券交易所）是否仍為有效代碼
3. 確認資料源是否有替代方案（如 TWSE 官方 API、其他資料提供商）

---

**市場報告無法完成** — 資料不可用，無法進行技術分析

MARKET REPORT COMPLETE — DATA UNAVAILABLE STATE
