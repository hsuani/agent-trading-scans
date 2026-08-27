# 技術分析 — IRM 截至 2026-07-25

## 數據可得性

**PRICE_DATA_UNAVAILABLE**

### 檢索狀態
- `python3 pipeline/tools/ta.py IRM snapshot` — 失敗
- `python3 pipeline/tools/yf.py IRM fast_info` — 失敗

### 失敗原因
多次重試後，無法從 Yahoo Finance 檢索 IRM 價格數據。代理連接錯誤（curl: CONNECT tunnel failed, 403）導致所有嘗試均失敗。系統報告 IRM 可能已退市。

### 結論
因價格數據不可用，無法計算技術指標（MACD、RSI14、移動平均線、布林帶、ATR）或識別支撐/阻力位。未以數據為基礎的估計進行報告。

---

**市場報告完成**
