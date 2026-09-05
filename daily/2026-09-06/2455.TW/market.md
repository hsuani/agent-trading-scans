# 技術分析 — 2455.TW 截至 2026-09-06

## 資料狀態

**PRICE_DATA_UNAVAILABLE**

ta.py 嘗試從 Yahoo Finance 檢索 2455.TW（全新 Formosa Epitaxy）的歷史行情資料時遭遇連線失敗。代理層返回 HTTP 403 CONNECT tunnel failed，表示對 Yahoo Finance 的出站存取已被組織政策封鎖。

系統無法取得以下資料：
- 即時報價與移動平均線（MA20、MA50、MA200）
- 技術指標（RSI14、MACD histogram、ATR14）
- 本地高低點與支撐/阻力位
- 波動率與成交量統計

## 分析暫停

由於缺乏有效的市場數據，無法進行可靠的技術分析。建議：
1. 檢查代理連線狀態
2. 驗證 2455.TW 股票是否仍於交易中（可能已下市）
3. 重試資料連線

---

MARKET REPORT COMPLETE
