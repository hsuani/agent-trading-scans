# 技術面 — IREN (截至 2026-07-20)

## 資料狀態

PRICE_DATA_UNAVAILABLE

代理程式無法通過代理伺服器連接至行情數據來源 (curl 403 CONNECT tunnel failed)。技術分析無法進行。

## 問題說明

- 嘗試執行 `ta.py IREN snapshot` 失敗
- 嘗試執行 `yf.py IREN fast_info` 失敗
- 兩次請求均返回代理錯誤 (curl: (56) CONNECT tunnel failed)
- IREN 可能已除牌或數據源無法存取

## 建議

請檢查網路連線或代理設定。待連線恢復後重新執行分析。

---

MARKET COMPLETE
