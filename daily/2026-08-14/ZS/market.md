# 技術分析 — ZS (Zscaler) 截至 2026-08-14

## 資料可用性狀態

**PRICE_DATA_UNAVAILABLE**

無法取得 ZS 的價格資料和技術指標。

### 原因

- 所有資料源 (pipeline/tools/ta.py、pipeline/tools/yf.py) 均無法連接到 Yahoo Finance
- 代理閘道拒絕連線至 fc.yahoo.com:443 (政策限制/上游故障)
- 所有請求均返回 CONNECT tunnel 403 錯誤

### 嘗試的資料取得方式

1. ✗ `ta ZS snapshot --period 2y` — 失敗 (連線被拒)
2. ✗ `yf ZS fast_info` — 失敗 (連線被拒)
3. ✗ `ta ZS levels --period 1y` — 失敗 (連線被拒)
4. ✗ `ta ZS series --period 1y` — 失敗 (連線被拒)

### 結論

無法執行 ZS 的技術分析。需要代理設定調整或替代資料來源才能繼續。

---

**市場報告不可完成** — 資料連線故障
