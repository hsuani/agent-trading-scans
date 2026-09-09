# 技術分析 — ZS 2026年9月4日

## 資料狀態

**PRICE_DATA_UNAVAILABLE**

代理伺服器對 Yahoo Finance 主要數據源返回 HTTP 403 政策拒絕。無法取得 ZS 的即時價格與歷史 OHLCV 數據。

## 原因

```
Error (ta.py snapshot --period 2y):
  Failed to perform, curl: (7) CONNECT tunnel failed, response 403
  
Blocked hosts:
  - fc.yahoo.com:443 (connect_rejected — policy denial)
  - query2.finance.yahoo.com:443 (connect_rejected — policy denial)
  - guce.yahoo.com:443 (connect_rejected — policy denial)
```

重試 5 次（指數級退避：1.5s, 3s, 4.5s, 6s, 7.5s）後仍無法連線。

## 無法生成的指標

| 類別 | 指標 | 狀態 |
|---|---|---|
| **即時行情** | Price | ✗ 無數據 |
| **移動平均** | MA20 | ✗ 無數據 |
| | MA50 | ✗ 無數據 |
| | MA200 | ✗ 無數據 |
| **動量** | MACD 線 | ✗ 無數據 |
| | MACD 信號線 | ✗ 無數據 |
| | MACD 柱狀圖 | ✗ 無數據 |
| | RSI14 | ✗ 無數據 |
| **波動率** | Bollinger Bands | ✗ 無數據 |
| | ATR14 | ✗ 無數據 |
| | 20日年化波動率 | ✗ 無數據 |
| **支撐阻力** | Resistance | ✗ 無數據 |
| | Support | ✗ 無數據 |
| **長期勢態** | 52週高 / 低 | ✗ 無數據 |
| | 12個月動能 (mom_12m) | ✗ 無數據 |
| | 6個月動能 (mom_6m) | ✗ 無數據 |
| **成交量** | 日成交量 | ✗ 無數據 |
| | 10日平均成交量 | ✗ 無數據 |

## 結論

因為外部數據源因組織政策而無法訪問，**無法完成 ZS 的技術面分析**。

- ❌ **無法評估技術偏見**（Bullish / Bearish / Neutral）
- ❌ **無法識別進出場水平**
- ❌ **無法計算風險指標**（ATR / 波動率）
- ❌ **無法判斷趨勢強度**（MA 夾角、MACD 加速度）

## 建議

1. 聯繫系統管理員解除對 Yahoo Finance (fc.yahoo.com, query2.finance.yahoo.com) 的出口政策限制
2. 或提供替代數據源（例如彭博、路透、本地行情 API）
3. 在數據源恢復前，ZS 技術分析無法進行

---

**MARKET REPORT COMPLETE** — 但因數據不可用而無法生成分析結果
