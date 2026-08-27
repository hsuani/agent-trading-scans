# 技術分析 — 2308.TW（台達電）2026-08-18

## 狀態

**PRICE_DATA_UNAVAILABLE**

### 資料蒐集失敗

兩個資料工具均無法連接：

1. `ta.py snapshot` — 連接失敗：curl (7) CONNECT tunnel failed, 403
2. `yf.py fast_info` — 連接失敗：curl (7) CONNECT tunnel failed, 403

### 代理伺服器狀態

代理網關拒絕 fc.yahoo.com 的連接（政策拒絕或上游故障），時間戳 2026-08-18T01:40:53 至 2026-08-18T01:41:06 共 20 次連接嘗試遭拒。

無法取得價格、技術指標（RSI14、MACD、MA50/MA200、ATR14、Bollinger Bands）及支撐/阻力位。

### 結論

無法產生技術報告。請檢查網路連線及代理設定。

---

**報告完成時間**：2026-08-18  
**技術分析狀態**：資料不可得
