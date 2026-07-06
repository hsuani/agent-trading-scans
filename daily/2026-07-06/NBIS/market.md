# 技術面分析 — NBIS (Nebius Group) 截至 2026-07-06

## 數據可用性

市場技術數據無法取得。yfinance 工具嘗試連線 Yahoo Finance (finance.yahoo.com) 被組織出口代理政策拒絕 (HTTP 403 CONNECT tunnel failure)。未找到本地 NBIS 緩存數據。

市場技術面分析代理未能完成分析。

## PASS/FAIL 評估

| 條件 | 要求 | 現狀 | 結果 |
|---|---|---|---|
| RSI14 < 72 | ✓ | 無數據 | ✗ |
| MACD 非深度負值 | ✓ | 無數據 | ✗ |
| 價格 > MA50 | ✓ | 無數據 | ✗ |

```
PASS/FAIL: FAIL
原因：市場數據不可取得，無法評估任何技術指標條件
```

**MARKET REPORT COMPLETE**
