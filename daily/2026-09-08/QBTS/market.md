# 技術分析 — QBTS 截至 2026-09-08

## 狀態

**PRICE_DATA_UNAVAILABLE**

Yahoo Finance 無法取得價格數據。請求返回 403 Forbidden 錯誤。

### 診斷
- Cookie/Crumb 取得失敗（ConnectionError）
- 多次嘗試 query2.finance.yahoo.com、fc.yahoo.com、guce.yahoo.com 被代理拒絕
- QBTS 可能已從 Yahoo Finance 下市或不可用

### 後續步驟
無法生成技術分析。請確認：
1. QBTS 代碼是否正確
2. Yahoo Finance 是否可訪問
3. 股票是否仍在交易

---

MARKET REPORT INCOMPLETE — PRICE_DATA_UNAVAILABLE
