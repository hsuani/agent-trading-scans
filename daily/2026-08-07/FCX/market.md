# 技術面 — FCX as of 2026-08-07

## 資料狀態
**PRICE_DATA_UNAVAILABLE**

無法取得實時價格數據。Yahoo Finance API（fc.yahoo.com:443）被代理攔截，返回 HTTP 403 錯誤。技術分析所需之 OHLCV 數據、移動平均線、RSI14、MACD 及關鍵支撐阻力位無法計算。

## 影響
此報告無法提供：
- 價格快照（Price、MA20/50/200）
- 超買/超賣指標（RSI14、BB %B）
- 動能指標（MACD、多時間軸 momentum）
- 技術位（支撐/阻力位、52週高低點）
- 波動率概況（ATR14、年化波動率）
- 交易設置評估

## 建議
1. 檢查代理設置或等待 Yahoo Finance 存取權恢復
2. 若需緊急分析，建議改用其他獲批的數據來源
3. 待數據恢復後重新執行掃描

---

MARKET REPORT COMPLETE
