# 技術分析 — 6217.TWO 截至 2026-08-29

## 資料狀態

**PRICE_DATA_UNAVAILABLE**

yfinance 連接失敗 (HTTP 403)。無法取得 6217.TWO 的價格數據。

### 診斷

- `python3 pipeline/tools/ta.py 6217.TWO snapshot` 返回：
  - 「$6217.TWO: possibly delisted; no price data found」
  - 運行時錯誤：「no history for 6217.TWO」
  
- `python3 pipeline/tools/yf.py 6217.TWO fast_info` 返回：
  - ConnectionError (CONNECT tunnel failed, response 403)
  - 代理連接被拒 (connect_rejected)

### 可能原因

1. **股票已下市** — 6217.TWO 可能已從台灣 TPEx 刪除清單
2. **代理政策** — 出站連接被組織策略阻擋
3. **數據源服務中斷** — Yahoo Finance 暫時不可用或該行情不支援

## 行動項目

- 驗證 6217.TWO 在台灣 TPEx 上的當前上市狀態
- 確認該股票代碼格式是否正確
- 檢查替代數據來源 (TW 交易所、證交所 API)

---

**無法進行技術指標分析 (MACD, RSI14, MA20/50/200, Bollinger, 成交量)** — 缺少基礎價格數據。

MARKET REPORT COMPLETE
