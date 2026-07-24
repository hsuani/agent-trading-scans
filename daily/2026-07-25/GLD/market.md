# 技術分析 — GLD (2026-07-25)

## 資料可用性狀態

**PRICE_DATA_UNAVAILABLE**

無法取得 GLD 的價格數據。系統代理網閘阻止與 Yahoo Finance (fc.yahoo.com:443) 的連接，返回 403 政策拒絕錯誤。pipeline/tools/ta.py 和 pipeline/tools/yf.py 工具均無法檢索數據。

### 嘗試的操作

- `python3 pipeline/tools/ta.py GLD snapshot --period 2y` — 失敗
- `python3 pipeline/tools/ta.py GLD series --period 1y` — 失敗
- `python3 pipeline/tools/ta.py GLD levels --period 1y` — 失敗
- `python3 pipeline/tools/yf.py GLD fast_info` — 失敗

### 代理狀態

- 代理啟用: 是
- 最近中繼故障: fc.yahoo.com:443 連接被拒 (2026-07-24 17:51:20 - 17:51:42 UTC)
- 原因: 網閘答覆 403 至 CONNECT (政策拒絕或上游故障)

## 無法提供的分析

因為缺乏價格數據，以下分析無法完成:

- 當前價格、52週範圍
- MACD (信號線、直方圖趨勢)
- RSI-14 (超買/超賣)
- 移動平均線: MA20、MA50、MA200 及價格關係
- 布林帶寬度及位置
- 成交量趨勢 vs 20日平均
- 關鍵支撐/阻力位
- 短期 vs 長期動量
- 黃金特定: 與現貨黃金及 GDX 比率對比

## 後續行動

需要解決代理連接問題或使用替代數據源以重新嘗試分析。

---

**MARKET REPORT COMPLETE**
