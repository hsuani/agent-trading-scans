# 技術分析 — 6515.TW (穎崴科技) | 2026-07-25

## 價格數據狀態

**PRICE_DATA_UNAVAILABLE**

無法取得 6515.TW (穎崴科技，台灣 TWSE) 之價格數據。

**原因：** 代理伺服器政策禁止存取 Yahoo Finance (fc.yahoo.com:443 返回 403 Forbidden)。

**嘗試工具：**
- `python3 pipeline/tools/ta.py 6515.TW snapshot` → RuntimeError: no history for 6515.TW
- `python3 pipeline/tools/yf.py 6515.TW fast_info` → ProxyError: CONNECT tunnel failed, response 403

**代理狀態：** fc.yahoo.com 連線遭拒（connect_rejected），gateway 回應 403 (policy denial or upstream failure)

---

## 技術指標

無可用數據。無法計算 RSI14、MACD、移動平均線、Bollinger Bands、ATR 等指標。

---

## 支撐/阻力位

無可用數據。

---

## 技術信號摘要

因網路代理政策限制，無法執行本次技術分析。建議：
1. 確認代理規則是否允許 Yahoo Finance 存取
2. 使用替代數據源 (Taiwan TWSE 直接 API、Bloomberg、Wind 等)
3. 待網路連線恢復後重新掃描

---
MARKET REPORT COMPLETE
