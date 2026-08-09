# 技術分析 — LITE 截至 2026-08-10

## 資料可用性

**PRICE_DATA_UNAVAILABLE**

無法檢索 LITE (Lumentum Holdings) 的實時價格數據。

### 錯誤詳情

嘗試透過以下工具獲取價格數據失敗：
- `ta.py snapshot --period 2y` — 連線失敗 (proxy 403)
- `yf.py fast_info` — 連線失敗 (proxy 403)

**root cause**: 代理伺服器將 fc.yahoo.com:443 的 CONNECT 請求拒絕 (policy denial 或 upstream failure)

### 影響

無法產生以下分析：
- 快照：最新價格、MA20/MA50/MA200、RSI14、MACD histogram
- 趨勢：價格相對均線的位置，上升/下降/橫盤判斷
- 動能：MACD 姿態、RSI 水平、多時間框架報酬
- 關鍵水位：支撐/阻力位，52 週高低點
- 波動率概況：ATR 日波幅、年化波動率

## 建議

- 待網路連線恢復後重新執行技術分析
- 確認代理伺服器設定可正常存取 Yahoo Finance 資料源

---

**MARKET REPORT INCOMPLETE** — 因缺乏價格數據而無法完成
