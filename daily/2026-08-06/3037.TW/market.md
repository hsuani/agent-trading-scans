# 技術面分析 — 3037.TW (欣興) 截至 2026-08-06

## 資料狀態

**PRICE_DATA_UNAVAILABLE**

Yahoo Finance 連線失敗 (HTTP 403 CONNECT tunnel failed)。無法取得價格資料、技術指標及歷史數據。

### 失敗詳情
- `ta.py 3037.TW snapshot` — 連線超時，無歷史資料可用
- `yf.py 3037.TW fast_info` — 連線錯誤 (CURL 7)

## 無法提供之分析項目

由於價格資料完全不可得，以下項目無法計算：

| 項目 | 狀態 |
|---|---|
| 現價 | UNAVAILABLE |
| MA20 / MA50 / MA200 | UNAVAILABLE |
| RSI14 | UNAVAILABLE |
| MACD 線 / 信號線 / 直方圖 | UNAVAILABLE |
| ATR14 / 年化波動率 | UNAVAILABLE |
| 52 週高位 / 低位 | UNAVAILABLE |
| 支撐位 / 阻力位 | UNAVAILABLE |
| BB %B | UNAVAILABLE |
| 多時段報酬 (1m/3m/6m/12m) | UNAVAILABLE |

## 建議後續行動

1. 確認 3037.TW 在 Yahoo Finance 上是否可用或已除牌
2. 檢查網絡連線與代理設定
3. 嘗試其他資料來源或重試連線

---

**MARKET REPORT COMPLETE**
