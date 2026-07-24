# 技術面分析 — SH 截至 2026-07-25

## 數據可用性

**PRICE_DATA_UNAVAILABLE**

無法取得 SH 價格數據。proxy gateway 對 Yahoo Finance (fc.yahoo.com:443) 連接遭拒 (policy denial / upstream failure)。

技術分析工具 (`ta.py` 和 `yf.py`) 依賴 Yahoo Finance 作為數據來源。由於代理設置限制對該主機的連接，目前無法檢索以下內容：

- 當前價格和 52 週範圍
- MACD 信號和直方圖
- RSI-14 數值
- 移動平均線 (MA20, MA50, MA200)
- 布林帶
- 成交量數據
- 支撐/阻力水平

## 報告停滯原因

```
gateway answered 403 to CONNECT (policy denial or upstream failure)
host: fc.yahoo.com:443
```

代理狀態顯示多個拒絕來自 fc.yahoo.com 的連接，導致 yfinance 無法檢索任何時間段的歷史數據。

---

**市場報告完成，但受限於數據可用性。**
