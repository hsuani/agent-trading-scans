# 技術面 — QLYS (Qualys) 至 2026-07-17

## ⚠️ PRICE_DATA_UNAVAILABLE

取價工具於 2026-07-17 無法存取 QLYS 價格資料。嘗試過：
- `python3 pipeline/tools/ta.py QLYS snapshot`
- `python3 pipeline/tools/yf.py QLYS fast_info`

返回結果：
- 網路錯誤：curl (56) CONNECT tunnel failed, response 403
- 工具回報：possibly delisted; no price data found
- 無足夠歷史資料可進行技術分析

## 結論

無法取得 QLYS 的實時價格、指標或移動平均線資料。建議：
1. 確認 QLYS 未被下市或暫停交易
2. 檢查 API 服務連線狀態
3. 稍後重試

技術分析報告無法完成。

---
**報告時間**: 2026-07-17  
**狀態**: 資料不可用 (DATA UNAVAILABLE)
