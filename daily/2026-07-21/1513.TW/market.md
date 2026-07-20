# 技術分析 — 1513.TW 中興電工 (2026-07-21)

## 資料狀態

### PRICE_DATA_UNAVAILABLE

**原因**: fc.yahoo.com:443 連線失敗 (proxy 政策拒絕)

本報告無法取得 1513.TW 的即時價格資料及技術指標。遠端 Yahoo Finance 伺服器通過 HTTPS 代理連線時返回 403 (Forbidden) 回應，導致無法完成以下計算：

- 價格序列 (OHLCV) — 過去 12 個月
- 技術指標 — MACD、RSI14、Bollinger %B、MA20/50/200
- 支撐/阻力位 — 本地高/低點
- ATR14 波動率分析
- 動能確認 (1m/3m/6m/12m 回報率)
- 成交量確認

### 次要資料源嘗試

| 嘗試 | 結果 | 詳情 |
|---|---|---|
| ta snapshot (2y) | 失敗 | 連線遭拒; curl 56 (tunnel failed) |
| ta series (1y) | 失敗 | 連線遭拒; 無歷史記錄 |
| ta levels (1y) | 失敗 | 連線遭拒; 無歷史記錄 |

### 代理狀態

- 代理已啟用: ✓
- 最近連線失敗: fc.yahoo.com:443 (20+ 次於 2026-07-20 18:03)
- 政策狀態: 上游拒絕或政策限制

---

## 結論

**無法進行技術分析**

無法取得必要的市場資料，故無法計算任何指標。建議：
1. 確認 fc.yahoo.com 是否在允許列表中
2. 確認網路連線復原
3. 使用替代資料源 (台灣證交所 TWSE API、Bloomberg、其他本地資料提供商)

---

MARKET REPORT COMPLETE
