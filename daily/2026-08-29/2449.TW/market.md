# 技術分析 — 2449.TW (京元電子 KYEC) 截至 2026-08-29

## 狀態

**PRICE_DATA_UNAVAILABLE**

yfinance 無法連接到雅虎財經數據源，超時回覆 403 (proxy 拒絕連接)。  
無法獲取：
- 當前價格
- 技術指標快照 (MACD, RSI14, Bollinger Bands, MA20/50/200)
- 52 週高低
- 成交量數據
- 多時段動能指標

### 錯誤訊息
```
Failed to perform, curl: (7) CONNECT tunnel failed, response 403
Cookie/crumb fetch failed (ConnectionError)
$2449.TW: possibly delisted; no price data found (period=2y)
```

## 後續行動

1. 確認 2449.TW 是否仍在台灣證交所掛牌 (TWSE)
2. 檢查代碼格式 (應為 NNNN.TW)
3. 待連接復原後重新執行快照分析
4. 考慮使用台灣本地財經數據源作為備份

---

**MARKET REPORT COMPLETE** (資料無法獲取)
