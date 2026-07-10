# 技術面分析 — IRM 截至 2026-07-11

## 狀態

**PRICE_DATA_UNAVAILABLE**

無法取得 IRM 價格數據。技術分析工具嘗試從 Yahoo Finance 和相關數據源檢索價格資訊時遭代理政策阻止 (gateway 403 policy denial)。

## 錯誤詳情

- 工具: `pipeline/tools/ta.py` 和 `pipeline/tools/yf.py`
- 連接錯誤: CONNECT tunnel failed (403)
- 影響的主機: fc.yahoo.com, ws.api.cnyes.com
- 結果: 無法獲得以下指標數據：
  - 當前價格
  - 移動平均線 (MA20, MA50, MA200)
  - MACD 和信號線
  - RSI14
  - Bollinger Bands
  - 支撐/阻力位
  - 成交量數據
  - 52 週高低點

## 分析無法執行

由於缺乏基礎市場數據，本日期無法完成 IRM 的技術分析。

---

**報告完成** (受限於數據可用性)

生成時間: 2026-07-11
