# Technical — ANT as of 2026-11-16

**狀態：PRICE_DATA_UNAVAILABLE**

## Snapshot
Price 無資料, MA20 無資料, MA50 無資料, MA200 無資料, RSI14 無資料, MACD hist 無資料

本次 `ta snapshot`、`ta series`、`ta levels` 與 `yf fast_info` 皆回傳 "no history for ANT"。Yahoo 連線遭 403 阻擋 (CONNECT tunnel failed)，yfinance 回報 "possibly delisted; no price data found"。

## Trend
無法判定。沒有任何價格歷史可計算 MA20 / MA50 / MA200，也無法判斷上升、下降或盤整。

## Momentum
無法評估。MACD、RSI14 與 1m / 3m / 6m / 12m 報酬皆無資料。

## Key levels
- Resistance: 無資料 (ta levels 無輸出)
- Support: 無資料 (ta levels 無輸出)
- Stop-loss suggestion: 無法提供，因無價格與支撐資料。

## Volatility profile
無法計算。ATR14 與 20 日年化波動度皆無資料。

## Setup
無法判定 (Bullish / Bearish / Neutral 均不作結論)。

## Indicators table
| Indicator | Value | Reading |
|---|---|---|
| Price | 無資料 | PRICE_DATA_UNAVAILABLE |
| MA20 / MA50 / MA200 | 無資料 | 無歷史價格 |
| RSI14 | 無資料 | 無法計算 |
| MACD hist | 無資料 | 無法計算 |
| BB %B | 無資料 | 無法計算 |
| ATR14 | 無資料 | 無法計算 |
| 20d 年化波動度 | 無資料 | 無法計算 |
| 52w 高 / 低 | NaN | 無資料 |
| 成交量 vs 10d 均量 | 無資料 | 無法計算 |
| 1m / 3m / 6m / 12m 報酬 | 無資料 | 無法計算 |

## 資料來源備註
- repo 快取 `prices/yf/ANT.json` 存在，但僅含基本資訊 (info) 與基本面類別欄位，不含價格歷史或即時報價欄位 (無 last price、無 OHLCV)，因此無法用於技術指標計算，未採用。
- 日期備註：本次 as-of 日期 2026-11-16 晚於執行當日 2026-11-15，且 yfinance 回報該代號可能已下市或無價格資料，建議先確認 ANT 代號是否正確且有交易中的上市證券，再重新執行。
- 未重試被阻擋的主機，未以舊 daily 報告補數字。

MARKET REPORT COMPLETE
