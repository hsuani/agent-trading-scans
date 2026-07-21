# 技術分析 — 3587.TWO 2026-07-21

## 市場信號狀態

**PRICE_DATA_UNAVAILABLE**

## 根本原因

資料無法取得。Yahoo Finance 通過代理層被阻擋 (HTTP 403 連線失敗)。

技術指標工具 (`ta` snapshot、`yf` fast_info) 均返回連線錯誤：
- `curl: (56) CONNECT tunnel failed, response 403`
- 沒有歷史價格數據（period=2y）
- 可能：3587.TWO 已下市或市場數據源無法訪問

## 分析結果

| 項目 | 狀態 |
|---|---|
| 價格 | 無法取得 |
| 移動平均線 (MA20/MA50/MA200) | 無法取得 |
| 技術指標 (RSI, MACD, ATR, BB) | 無法取得 |
| 支撐/阻力位 | 無法取得 |
| 交易量 | 無法取得 |
| 走勢判斷 | 無法評估 |
| 動能 | 無法評估 |

## 結論

無法執行技術面掃描。市場信號失敗。需要 Yahoo Finance 恢復連線或確認 3587.TWO 上市狀態。

---

**報告時間**：2026-07-21  
**報告完成**：MARKET REPORT COMPLETE
