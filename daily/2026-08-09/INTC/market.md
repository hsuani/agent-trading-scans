# 技術面 — INTC (截至 2026-08-09)

## 狀態

**PRICE_DATA_UNAVAILABLE**

無法取得 INTC 價格數據。數據工具連接到 Yahoo Finance (fc.yahoo.com) 時遭到代理政策拒絕 (HTTP 403)。已進行多次重試，但連接持續被阻擋。

## 診斷信息

- **錯誤類型**: 代理連接拒絕 (gateway answered 403 to CONNECT)
- **數據源**: Yahoo Finance
- **重試次數**: 多次（工具自動重試機制）
- **代理狀態**: 已啟用，但對指定數據源有政策限制

## 無法提供的分析

以下指標無法計算，因為缺乏價格數據：
- 快照數據 (當前價格、MA20/MA50/MA200、RSI14、MACD histogram)
- 技術級別 (支撐/阻力)
- 歷史系列數據 (1年期間的 OHLCV + 指標)
- 波動性分析 (ATR14、年化波動率)
- 動量分析 (MACD 走勢、多時段報酬)
- 成交量分析

## 後續步驟

需要解決代理政策限制或使用替代數據源才能完成技術分析。

---

**數據報告無法完成** | PRICE_DATA_UNAVAILABLE

