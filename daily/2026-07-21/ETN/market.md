# 技術面 — ETN (2026-07-21)

## 資料狀態

**PRICE_DATA_UNAVAILABLE**

無法取得 ETN (Eaton Corp) 的價格資料。

### 故障詳情

在 2026-07-20 下午 17:51 UTC 時段，代理伺服器對 Yahoo Finance (fc.yahoo.com:443) 的所有連線要求均被拒絕，回覆代碼 403 (政策拒絕或上游故障)。

**嘗試方法：**
- `ta ETN snapshot --period 2y` — 失敗
- `ta ETN series --period 1y` — 失敗
- `yf ETN fast_info` — 失敗
- `ta ETN levels --period 1y` — 失敗

**curl 錯誤代碼：** `(56) CONNECT tunnel failed`

### 可用數據

無法計算以下指標：
- MACD、RSI14、布林帶 %B
- MA20、MA50、MA200
- 動能 (1m/3m/6m/12m 報酬)
- 支撐/阻力位
- 年化波動率、ATR14
- 成交量確認

---

## 建議

技術分析無法進行，直到：
1. 代理伺服器恢復與 Yahoo Finance 的連接
2. 價格資料流暢可得

**MARKET REPORT COMPLETE**
