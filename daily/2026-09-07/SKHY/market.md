# 技術分析 — SKHY (2026-09-07)

## 狀態

**PRICE_DATA_UNAVAILABLE**

Yahoo Finance 無法取得 SKHY 的價格數據。連接遭拒（HTTP 403 CONNECT tunnel failed），且該股票可能已下市或不存在於資料庫中。

## 原因

1. Yahoo Finance 代理被組織政策阻止 (`query2.finance.yahoo.com:443` — connect_rejected)
2. SKHY 可能已下市或證券代碼無效
3. 無法檢索歷史價格數據 (period=2y)

## 結論

無法執行技術分析。未能獲得 OHLCV 數據、移動平均線、MACD、RSI、布林帶或 ATR 等指標。

---

**MARKET COMPLETE**
