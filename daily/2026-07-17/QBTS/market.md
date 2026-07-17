# 技術分析 — QBTS (2026-07-17)

## 狀態
**PRICE_DATA_UNAVAILABLE**

無法取得實時價格數據。

## 問題描述
- 代理伺服器 (Proxy Gateway) 對 Yahoo Finance (fc.yahoo.com) 返回 403 政策拒絕
- 多次重試均失敗
- 技術工具 (`ta.py`, `yf.py`) 無法連接數據源
- QBTS 可能已下市或無可用的歷史數據

## 數據來源狀態
| 工具 | 狀態 | 錯誤 |
|---|---|---|
| `ta snapshot` | 失敗 | CONNECT tunnel failed 403 |
| `yf fast_info` | 失敗 | ProxyError: gateway 403 |
| `ta series` | 失敗 | no history for QBTS |

## 無法進行的分析
無價格數據，無法進行以下技術分析：
- 趨勢評估 (MA20/MA50/MA200, 金叉/死叉)
- 動量指標 (MACD, RSI14, 一月/三月/六月/十二月報酬)
- 波動性分析 (ATR14, 20日年化波動率)
- 支撐/阻力位水平
- 布林帶 (%B) 分析
- 成交量確認

---

**MARKET REPORT INCOMPLETE — PRICE_DATA_UNAVAILABLE**
