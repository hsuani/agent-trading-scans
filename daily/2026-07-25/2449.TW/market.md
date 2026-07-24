# 技術分析 — 2449.TW (京元電子) | 2026-07-25

## 價格數據狀態

**PRICE_DATA_UNAVAILABLE**

無法取得 2449.TW 的價格數據。代理伺服器對 Yahoo Finance (fc.yahoo.com) 的連線遭到閘道拒絕（HTTP 403）。這屬於上游政策限制或連線故障，並非本機設定問題。

數據工具無法完成下列呼叫：
- `python3 pipeline/tools/ta.py 2449.TW snapshot` → RuntimeError: no history for 2449.TW
- `python3 pipeline/tools/yf.py 2449.TW fast_info` → ProxyError: CONNECT tunnel failed, response 403

**技術分析無法進行**。無任何指標可計算。

---

## 技術指標 (RSI, MACD, MA, Bollinger, ATR)

| 指標 | 值 | 讀數 |
|---|---|---|
| RSI14 | N/A | 資料不可用 |
| MACD 線 | N/A | 資料不可用 |
| MACD 信號 | N/A | 資料不可用 |
| MACD 直方圖 | N/A | 資料不可用 |
| MA20 | N/A | 資料不可用 |
| MA50 | N/A | 資料不可用 |
| MA200 | N/A | 資料不可用 |
| BB %B | N/A | 資料不可用 |
| ATR14 | N/A | 資料不可用 |
| 年化波動率 | N/A | 資料不可用 |

---

## 支撐/阻力位

無法識別支撐與阻力位。缺乏價格歷史數據。

---

## 技術信號摘要

由於代理伺服器對外部數據來源的連線限制，無法完成對 2449.TW 的技術分析。建議：

1. **檢查代理政策**：確認 Yahoo Finance 是否已被列入允許清單。
2. **驗證 Ticker 格式**：確認 2449.TW 是否為正確的 Yahoo Finance Ticker 代碼。
3. **重新嘗試**：待代理連線恢復後再執行分析。

---

MARKET REPORT COMPLETE
