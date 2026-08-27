# 技術分析 — TSEM (2026-07-27)

## 狀態報告

**PRICE_DATA_UNAVAILABLE**

無法從 Yahoo Finance 擷取 TSEM 的價格資料。資料連線返回 HTTP 403 CONNECT tunnel failed，表示 proxy 層級阻擋或服務不可達。

根據資料工具回饋，TSEM 可能已下市 (delisted)，或暫時無法取得歷史行情資料。

## 技術分析無法進行

無可用的：
- 快照（Snapshot）資料
- 價格、移動平均線（MA20/MA50/MA200）
- 技術指標（RSI14、MACD、ATR14、Bollinger Bands）
- 支撐/阻力位
- 波動率量化

## 後續步驟

建議：
1. 確認 TSEM 股票代碼是否正確
2. 查詢該股票是否已被下市或更名
3. 檢查代理連線設定（/root/.ccr/README.md）
4. 待連線恢復後重新運行掃描

---

**MARKET REPORT COMPLETE**
