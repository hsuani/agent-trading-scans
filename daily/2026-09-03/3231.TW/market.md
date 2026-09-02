# 3231.TW 技術分析報告 — 2026-09-03

## PRICE_DATA_UNAVAILABLE

Yahoo Finance 端點被代理封鎖（403 CONNECT tunnel failure），無法取得即時價格資料。

**影響：** 
- RSI14、MACD、MA20/50/200、布林通道、支撐/阻力位均無法計算
- 無法判定趨勢強度、超買超賣狀態、動量加速減速
- 無法定位本地高低點與關鍵阻力/支撐位

**狀態：** 
技術面訊號缺失；下游分析不得給出入場/止損/目標價位（PRICE_DATA_UNAVAILABLE）。

**代理狀態詳情：**
```
curl: (7) CONNECT tunnel failed, response 403
```

建議檢查 `/root/.ccr/README.md` 與代理設定。
