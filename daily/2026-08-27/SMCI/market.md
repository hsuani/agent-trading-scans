# 技術分析 — SMCI 截至 2026-08-27

## 資料狀態

**PRICE_DATA_UNAVAILABLE**

無法取得 SMCI 的即時價格數據。雅虎財經 API (Yahoo Finance API) 的連線在代理層被政策拒絕 (HTTP 403)。技術分析所需的 OHLCV、移動平均線、MACD、RSI14、布林帶、ATR 等指標無法計算。

### 嘗試過的方法
- 透過 yfinance 連接 Yahoo Finance：失敗（fc.yahoo.com 403 policy denial）
- 自動重試機制（退避）：全部嘗試均失敗

### 影響
無法提供以下分析：
- 即時價格與 MA20/MA50/MA200 的關係
- MACD 柱狀圖與信號線的動態
- RSI14 超買/超賣狀態
- 布林帶 %B 和位置
- ATR14 波動率
- 支撐與阻力位
- 多時間框架動能 (1m/3m/6m/12m)
- 52 周高低與距離分析

## 建議

代理政策需調整或者使用替代數據源（例如鉅亨網、台灣證券交易所 API）以恢復 SMCI 的技術分析能力。

---

**市場報告未完成 — 無可用數據**
