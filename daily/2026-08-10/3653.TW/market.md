# 技術分析 — 3653.TW (健策) 2026年8月10日

## 狀態

**PRICE_DATA_UNAVAILABLE**

### 數據取得失敗原因

代理防火牆政策阻止對 Yahoo Finance (fc.yahoo.com) 的連接，返回 403 狀態碼。

```
gateway answered 403 to CONNECT (policy denial or upstream failure)
```

### 影響

- 無法執行即時技術指標計算 (MACD, RSI14, ATR14, Bollinger Bands, etc.)
- 無法取得當日OHLCV數據
- 無法計算移動平均線 (MA20, MA50, MA200)
- 無法判斷近期動量及關鍵價位

### 備註

健策 (3653.TW) 為台灣 TWSE 上市之熱管散熱股票 (Vera Rubin 供應鏈：AI 伺服器熱管、熱管室)。市場數據源於外部政策限制而無法載入，需待網路連接恢復方可執行分析。

---

MARKET ANALYSIS COMPLETE
