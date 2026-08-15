# 技術分析 — GFS (GlobalFoundries) 截至 2026-08-16

## 資料狀態

**PRICE_DATA_UNAVAILABLE**

技術分析無法完成。資料取得工具遇到代理連接錯誤 (HTTP 403 CONNECT tunnel failed)，yfinance 與本地 TA 工具無法連線至數據源。

### 診斷資訊
- 命令: `python3 pipeline/tools/ta.py GFS snapshot` 
- 錯誤: `curl: (7) CONNECT tunnel failed, response 403`
- 狀態: 價格資料不可用
- 建議: 待網絡連接恢復後重試

## 可用的技術指標

| 指標 | 數值 | 狀態 |
|---|---|---|
| 現價 | N/A | 無法取得 |
| MA20 | N/A | 無法取得 |
| MA50 | N/A | 無法取得 |
| MA200 | N/A | 無法取得 |
| RSI14 | N/A | 無法取得 |
| MACD histogram | N/A | 無法取得 |
| 20日平均成交量 | N/A | 無法取得 |
| ATR14 | N/A | 無法取得 |
| Bollinger Bands %B | N/A | 無法取得 |

## 趨勢分析

無法進行。缺乏現價與移動平均線數據。

## 動能

無法評估。無 MACD、RSI 或多周期報酬率數據。

## 關鍵水位

- 阻力位: N/A
- 支撐位: N/A
- 止損建議: N/A

## 波動性概況

無法計算。缺乏 ATR 與歷史波動率數據。

## 技術設置

無法判斷。資料不足。

## 結論

GFS 的技術分析因網絡連接故障而中止。應重新嘗試資料取得。若問題持續，可能表示該證券資料源不可用或已下市。

---

**市場報告無法完成 — 缺乏價格資料**
