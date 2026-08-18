# 技術面分析 — TSM 截至 2026-08-19

## 狀態

**PRICE_DATA_UNAVAILABLE**

無法取得 TSM 的價格數據。代理 (proxy) 已阻止對 Yahoo Finance 的連接請求，收到策略拒絕回應 (HTTP 403)。

## 資料取得嘗試

`ta.py TSM snapshot --period 2y` 和 `ta.py TSM levels --period 1y` 都因為以下原因失敗：

```
Failed to get ticker 'TSM' reason: Failed to perform, curl: (7) CONNECT tunnel failed, response 403
```

代理狀態顯示：
- Gateway answered 403 to CONNECT (policy denial or upstream failure)
- Host: fc.yahoo.com:443

## 後續行動

無法進行技術分析，因為：
- 無 OHLCV 數據
- 無移動平均線 (MA20, MA50, MA200)
- 無動量指標 (MACD, RSI14)
- 無支撐/阻力位
- 無波動率指標

技術分析團隊無法在此時提供市場報告。

---

MARKET REPORT COMPLETE
