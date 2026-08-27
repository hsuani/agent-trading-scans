# 技術面分析 — CRDO (2026-07-19)

## PRICE_DATA_UNAVAILABLE

無法取得 CRDO 的定價數據。

### 錯誤詳情

嘗試使用 `ta CRDO snapshot --period 2y` 與 `yf CRDO fast_info` 工具後，系統回報：

```
$CRDO: possibly delisted; no price data found (period=2y)
Failed to perform, curl: (56) CONNECT tunnel failed, response 403
```

### 根本原因

1. **代理網關限制**: 代理網關正拒絕與 `fc.yahoo.com:443` 的 CONNECT 連線，狀態碼 403（政策否決或上游失敗）
2. **可能的除牌狀態**: 系統建議 CRDO 可能已被除牌，Yahoo Finance 無法提供歷史或即時數據

### 可用操作

無法進行技術分析。建議：
1. 確認 CRDO 是否仍在交易（檢查上市狀態）
2. 檢查代理網關的政策設定
3. 確認行情資料源可用性

---

**報告日期**: 2026-07-19  
**狀態**: PRICE_DATA_UNAVAILABLE
