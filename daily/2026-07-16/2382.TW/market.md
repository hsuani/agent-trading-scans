# 技術分析 — 2382.TW（廣達電腦）2026年7月16日

## 資料狀態

**PRICE_DATA_UNAVAILABLE**

無法取得技術分析數據。Yahoo Finance 外部連線被阻止（HTTP 403 Proxy 錯誤）。pipeline/tools/ta.py 和 pipeline/tools/yf.py 均無法連接到遠端數據源。

### 故障詳情
- **錯誤代碼**: curl (56) CONNECT tunnel failed, response 403
- **影響範圍**: 無法獲得價格、移動平均線、技術指標、支撐阻力位等任何市場數據
- **工具狀態**: 
  - `python3 pipeline/tools/ta.py 2382.TW snapshot` → 失敗
  - `python3 pipeline/tools/yf.py 2382.TW fast_info` → 失敗

## 分析不可行

由於無法取得以下核心數據，技術分析無法進行：
- 最新成交價與移動平均線（MA20, MA50, MA200）
- 相對強度指數（RSI14）與威廉指標（MACD）
- 布林通道與ATR波動率指標
- 52週高低點與支撐阻力位

## 建議後續步驟

1. 檢查網路連線與代理設定
2. 確認 Yahoo Finance API 端點可達性
3. 考慮使用本地數據源或備用數據供應商
4. 待連線恢復後重新執行分析

---

**技術報告生成失敗。** 無法產出有效的交易信號與技術研判。

