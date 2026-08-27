# 技術分析 — APD 截至 2026-08-28

## 快照
**狀態**: PRICE_DATA_UNAVAILABLE

無法取得價格數據。yfinance 連線被代理伺服器阻擋 (HTTP 403)。所有依價格的指標無法計算。

## 趨勢
無法判定趨勢。缺乏價格數據，無法與 MA20、MA50、MA200 進行比較或判斷上升/下降/盤整狀態。

## 動能
無法評估動能。MACD、RSI14 及多時間框架報酬無法計算。

## 關鍵水位
- 阻力：PRICE_DATA_UNAVAILABLE
- 支撐：PRICE_DATA_UNAVAILABLE
- 止損建議：無法判定

## 波動率檔案
ATR14 及年化波動率無法計算。風險評估受阻。

## 設置
無法確定。缺乏價格行為數據，無法識別型態。

## 指標表
| 指標 | 數值 | 讀數 |
|---|---|---|
| RSI14 | N/A | PRICE_DATA_UNAVAILABLE |
| MACD 直方圖 | N/A | PRICE_DATA_UNAVAILABLE |
| 相對 MA200 % | N/A | PRICE_DATA_UNAVAILABLE |
| BB %B | N/A | PRICE_DATA_UNAVAILABLE |
| 現價 | N/A | PRICE_DATA_UNAVAILABLE |
| MA20 | N/A | PRICE_DATA_UNAVAILABLE |
| MA50 | N/A | PRICE_DATA_UNAVAILABLE |
| MA200 | N/A | PRICE_DATA_UNAVAILABLE |
| ATR14 | N/A | PRICE_DATA_UNAVAILABLE |
| 年化波動率 | N/A | PRICE_DATA_UNAVAILABLE |

## 市場信號分數
**結果**: FAIL

**原因**: 價格數據無法取得。無法驗證必要條件:
- RSI14 < 72 ❌ 無法確定
- MACD 非深度負數 ❌ 無法確定  
- 現價 > MA50 ❌ 無法確定

代理伺服器阻擋 yfinance 連線，導致完整分析無法進行。

---

**MARKET REPORT COMPLETE**
