# 技術面 — NBIS 截至 2026-07-27

## 資料狀態
**PRICE_DATA_UNAVAILABLE**

無法從 Yahoo Finance 取得 NBIS 的價格數據。系統傳回 HTTP 403 連線隧道失敗錯誤，並指示該代碼可能已下市。

## 數據收集嘗試
- `ta NBIS snapshot --period 2y` — 失敗：未取得歷史數據
- `yf NBIS fast_info` — 失敗：代理錯誤 (HTTP 403)

## 結論
無法進行技術分析。建議確認 NBIS 的上市狀態及資料供應商的可用性。

---

MARKET REPORT COMPLETE