# 技術分析報告 — 3231.TW (緯創資通)
**分析日期**: 2026-08-27

## PRICE_DATA_UNAVAILABLE

無法完成技術分析。

### 連線障礙

組織出口政策阻止：
- **fc.yahoo.com:443** (Yahoo Finance) — 403 連線拒絕
- **ws.api.cnyes.com:443** (CNYES) — 403 連線拒絕

分析工具 (`ta.py`、`yf.py`) 依賴這些端點取得 OHLCV 價格數據及技術指標 (RSI、MACD、Bollinger Bands、ATR 等)。

### 替代估值參考 (V = valuation-anchored)

根據情緒分析：分析師平均目標價 **TWD 262.36**，相較最近報價 TWD 193.50，潛在漲幅 **35.59%**。

- **估值錨定支撐 (V)**: TWD 185–195 (近期報價區間)
- **估值錨定目標 (V)**: TWD 262 (分析師平均目標價)

所有技術指標 (RSI14、MACD、MA50/MA200、布林通道、ATR、成交量) 均無法計算。

### 下游注意事項

交易員與投資組合經理不得使用本報告產生入場/停損/目標價位，因無即時市場數據支撐。

**MARKET ANALYSIS COMPLETE**
