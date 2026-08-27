# 基本面分析 — POET 截至 2026-07-21

## 執行摘要

**資料可用性狀態：DATA_UNAVAILABLE**

截至 2026-07-21，由於代理伺服器政策限制（403 拒絕），無法從 Yahoo Finance 存取 POET Technologies (POET) 的基本面資料。所有財務指標、估值數據、內部人交易記錄及持股濃度資訊均無法取得。建議等候資料來源恢復或使用替代資料管道。

---

## 營收與獲利能力

**狀態：DATA_UNAVAILABLE**

- 3-5年 CAGR：DATA_UNAVAILABLE
- 年度營收同比增長：DATA_UNAVAILABLE
- 毛利率走勢：DATA_UNAVAILABLE
- 營業利潤率走勢：DATA_UNAVAILABLE
- 淨利潤率走勢：DATA_UNAVAILABLE
- ROE (股東權益報酬率)：DATA_UNAVAILABLE
- ROIC (投資資本報酬率)：DATA_UNAVAILABLE

**故障原因：** 代理伺服器拒絕連接至 Yahoo Finance (fc.yahoo.com:443)，無法檢索年度及季度損益表資料。

---

## 現金流與資產負債表

**狀態：DATA_UNAVAILABLE**

- 自由現金流 (FCF) 邊際率：DATA_UNAVAILABLE
- FCF / 淨收入比率：DATA_UNAVAILABLE
- 淨債務水位：DATA_UNAVAILABLE
- 流動比率：DATA_UNAVAILABLE
- 債務/權益比：DATA_UNAVAILABLE
- 現金及等價物餘額：DATA_UNAVAILABLE

**故障原因：** 無法存取年度及季度現金流表、資產負債表資料。

---

## 資本配置與內部人訊號

**狀態：DATA_UNAVAILABLE**

- 資本支出 (CapEx) 走勢：DATA_UNAVAILABLE
- 股票回購計畫：DATA_UNAVAILABLE
- 股利覆蓋率：DATA_UNAVAILABLE
- 近 6 個月內部人買賣淨額：DATA_UNAVAILABLE
- 內部人交易相對市值之幅度：DATA_UNAVAILABLE

**故障原因：** 無法檢索內部人交易紀錄及股利歷史資料。

---

## 估值

**狀態：DATA_UNAVAILABLE**

- 尾隨本益比 (Trailing P/E)：DATA_UNAVAILABLE
- 遠期本益比 (Forward P/E)：DATA_UNAVAILABLE
- EV/EBITDA：DATA_UNAVAILABLE
- 本益比自由現金流 (P/FCF)：DATA_UNAVAILABLE
- 本益比銷售收入 (P/S)：DATA_UNAVAILABLE
- 當前股價：DATA_UNAVAILABLE
- 市值：DATA_UNAVAILABLE
- 貝塔係數 (Beta)：DATA_UNAVAILABLE

**故障原因：** 代理伺服器阻止對 Yahoo Finance 的存取，無法取得即時報價及估值指標。

---

## 關鍵催化劑

**狀態：DATA_UNAVAILABLE**

- 下次財報公佈日期：DATA_UNAVAILABLE
- 近期公司指引變化：DATA_UNAVAILABLE
- 每股盈餘 (EPS) 預估值：DATA_UNAVAILABLE
- 近期 EPS 意外超越/不達預期記錄：DATA_UNAVAILABLE
- 業務部門移動或策略轉變：DATA_UNAVAILABLE

**故障原因：** 無法存取財報日期表及分析師預測資料。

---

## 指標表

| 指標 | 最新值 | 年度環比 | 行業中位數 (估計) | 評語 |
|---|---|---|---|---|
| 營收 CAGR (3-5年) | DATA_UNAVAILABLE | - | - | 無法取得 |
| 毛利率 | DATA_UNAVAILABLE | - | - | 無法取得 |
| 營業利潤率 | DATA_UNAVAILABLE | - | - | 無法取得 |
| 淨利潤率 | DATA_UNAVAILABLE | - | - | 無法取得 |
| ROE | DATA_UNAVAILABLE | - | - | 無法取得 |
| ROIC | DATA_UNAVAILABLE | - | - | 無法取得 |
| FCF 邊際率 | DATA_UNAVAILABLE | - | - | 無法取得 |
| FCF / NI 比率 | DATA_UNAVAILABLE | - | - | 無法取得 |
| 淨債務 | DATA_UNAVAILABLE | - | - | 無法取得 |
| 流動比率 | DATA_UNAVAILABLE | - | - | 無法取得 |
| 債務/權益比 | DATA_UNAVAILABLE | - | - | 無法取得 |
| 尾隨 P/E | DATA_UNAVAILABLE | - | - | 無法取得 |
| 遠期 P/E | DATA_UNAVAILABLE | - | - | 無法取得 |
| EV/EBITDA | DATA_UNAVAILABLE | - | - | 無法取得 |
| P/FCF | DATA_UNAVAILABLE | - | - | 無法取得 |
| P/S | DATA_UNAVAILABLE | - | - | 無法取得 |
| 股價 | DATA_UNAVAILABLE | - | - | 無法取得 |
| 市值 | DATA_UNAVAILABLE | - | - | 無法取得 |
| 貝塔 | DATA_UNAVAILABLE | - | - | 無法取得 |

---

## 風險警示

- **資料完全不可用：** 代理伺服器政策限制阻止對 Yahoo Finance 的所有連接 (403 Forbidden on fc.yahoo.com:443 & ws.api.cnyes.com:443)
- **分析難以進行：** 無法評估 POET 的財務狀況、獲利能力、現金流健全度或估值吸引力
- **建議行動：** 
  1. 等候資料來源連線恢復
  2. 聯繫基礎設施團隊解決代理伺服器限制
  3. 使用替代資料管道 (如現場記者資源、公開申報文件)
  4. 重新排程分析至資料可用時

---

## 系統級故障詳情

**代理伺服器狀態 (截至 2026-07-21 00:49:20 UTC)：**

```
狀態：已啟用，連接埠 35723
CA 束：/root/.ccr/ca-bundle.crt
最近中斷：
  - fc.yahoo.com:443 (x12+) — 連接拒絕，403 (政策拒絕或上游故障)
  - ws.api.cnyes.com:443 (x2+) — 連接拒絕，403 (政策拒絕或上游故障)
```

**yfinance 工具執行結果：**
- `yf POET info` — ProxyError：隧道連接失敗，curl (56)
- `yf POET fast_info` — ProxyError：隧道連接失敗，curl (56)
- `yf POET financials` — 空陣列 []
- `yf POET quarterly_fin` — 空陣列 []
- `yf POET balance_sheet` — 空陣列 []

---

**報告產生時間：** 2026-07-21 00:49:25 UTC  
**分析狀態：** 無法進行 — 等候資料恢復  
**建議：** 不應在此時基於本報告進行交易決策

---
