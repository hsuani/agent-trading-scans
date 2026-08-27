# 技術面分析 — CEG 截至 2026-07-28

## 狀態報告

**PRICE_DATA_UNAVAILABLE**

無法獲取 CEG 股票的實時價格數據與技術指標。

### 故障詳情

- **數據來源**: yfinance (Yahoo Finance) 與備用來源 (cnyes API)
- **問題**: 代理閘道對 fc.yahoo.com 與 ws.api.cnyes.com 的連接被策略拒絕（403 CONNECT 故障）
- **重試次數**: 已進行多次重試（1.5s 退避策略），均失敗
- **時間戳**: 2026-07-27 22:58 UTC

### 無法計算的指標

以下技術指標因數據不可用而無法計算：

| 指標 | 狀態 |
|---|---|
| 當前價格 (Price) | 無可用數據 |
| MA20 / MA50 / MA200 | 無可用數據 |
| RSI14 | 無可用數據 |
| MACD / MACD Signal / MACD Histogram | 無可用數據 |
| Bollinger Bands (上軌 / 中線 / 下軌) | 無可用數據 |
| Bollinger Bands %B | 無可用數據 |
| ATR14 | 無可用數據 |
| 52週高 / 52週低 | 無可用數據 |
| 成交量 (Volume) | 無可用數據 |
| 20日年化波動率 | 無可用數據 |
| 1個月 / 3個月 / 6個月 / 12個月動量 | 無可用數據 |

### 支撐 / 阻力位

無法識別，因為缺乏歷史價格數據。

## 下一步行動

請在網絡連通性恢復後重新執行此分析。代理的掛號可能需要調整，以允許對外部金融數據源的訪問。

---

**報告狀態**: PRICE_DATA_UNAVAILABLE (網絡故障)  
**生成日期**: 2026-07-28  
**數據檢索工具**: pipeline/tools/ta.py (snapshot/levels) | pipeline/tools/yf.py (fast_info/history)  
**技術分析報告完成**
