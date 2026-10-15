# Technical — MSFT as of 2026-10-15

## 狀態

**PRICE_DATA_UNAVAILABLE**

無法取得 MSFT 的可用價格資料，因此本報告不提供任何價格位階、均線數值、RSI、MACD、布林通道或支撐壓力數字。

## 資料來源檢查

- `pipeline/tools/ta MSFT snapshot --period 2y`：失敗，yfinance 連線遭 403 拒絕（CONNECT tunnel failed），無 history 回傳。
- `pipeline/tools/yf MSFT fast_info`：所有欄位皆為 null，年高年低為 NaN。
- `pipeline/tools/ta MSFT levels --period 1y`：失敗，同樣無 history。
- `pipeline/tools/ta MSFT series --period 1y`：失敗，同樣無 history。
- 本地快取 `prices/MSFT.csv`：不存在。
- 本地快取 `prices/yf/MSFT.json`：不存在。
- 全機搜尋 MSFT 相關檔案，僅找到過往日期的 `daily/2026-08-xx/MSFT/` 報告，屬於歷史分析而非 2026-10-15 的價格來源，故未採用其中任何價位。

## 影響

- 無法計算 Trend、Momentum、Key levels、Volatility profile 與 Setup。
- 無法判斷 MSFT 目前是否處於多頭、空頭或盤整結構。
- 無法給出停損參考位，亦無法給出 ATR 或年化波動率。

## 建議

- 待連線恢復，或 `prices/yf/MSFT.json`（或 `prices/MSFT.csv`）由 refresh-cache 流程補上後，重新執行本分析。
- 在資料補齊前，相關交易決策應視為缺乏技術面依據。

## Indicators table

| Indicator | Value | Reading |
|---|---|---|
| Price | N/A | PRICE_DATA_UNAVAILABLE |
| MA20 / MA50 / MA200 | N/A | 無資料 |
| RSI14 | N/A | 無資料 |
| MACD hist | N/A | 無資料 |
| BB %B | N/A | 無資料 |
| ATR14 / 20d vol | N/A | 無資料 |
| Volume vs 10d avg | N/A | 無資料 |

MARKET REPORT COMPLETE
