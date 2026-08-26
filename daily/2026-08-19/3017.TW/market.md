# 技術面分析 — 3017.TW 截至 2026-08-19

## PRICE_DATA_UNAVAILABLE

Yahoo Finance / yfinance 因代理封鎖（HTTP 403，gateway policy denial）無法取得即時市價及歷史價格數據。

**技術面信號：N/A**

無法計算 RSI14、MACD、MA20/MA50/MA200、Bollinger Bands、支撐/阻力位、ATR、相對強度或動能指標。

不提供技術面進出場建議。

### 通過條件檢查（PASS CRITERIA）

根據指定規則：**RSI14 < 72 AND MACD 非深度負值 AND 價格 > MA50**

| 條件 | 數據 | 狀態 |
|---|---|---|
| RSI14 < 72 | N/A | ❌ 無法評估 |
| MACD 非深度負值 | N/A | ❌ 無法評估 |
| 價格 > MA50 | N/A | ❌ 無法評估 |
| **整體通過** | — | ❌ **FAIL** |

### Phase 1 評分表

| 評分項 | 權重 | 得分 | 狀態 |
|---|---|---|---|
| 趨勢強度（price vs MA20/MA50/MA200） | 25% | N/A | 無數據 |
| 動能加速度（MACD histogram vs signal） | 20% | N/A | 無數據 |
| 相對強度（RSI14，<30 超賣，>70 超買） | 20% | N/A | 無數據 |
| 支撐/阻力位確認（volume profile） | 15% | N/A | 無數據 |
| 波動性健全性（ATR，日均波幅） | 10% | N/A | 無數據 |
| 成交量確認（vs 10d avg） | 10% | N/A | 無數據 |
| **Phase 1 綜合評分** | 100% | **N/A** | **無法計算** |

---

**報告日期**: 2026-08-19  
**數據來源**: 不適用（代理連線中斷）  
**下游 trader / portfolio-manager 不得基於此報告虛構任何價格水準。**

**MARKET REPORT COMPLETE**
