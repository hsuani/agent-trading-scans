# 基本面分析 — MOD 截至 2026-07-08

## 資料取得限制

無法產生本日期間的基本面報告。原因如下：

### 網路存取限制

Yahoo Finance 資料來源 (fc.yahoo.com:443) 遭組織出站政策封鎖，導致無法取得即時財務資料。代理伺服器回應 HTTP 403 政策拒絕。

### 受影響的資料類別

下列資料無法透過標準管道取得：

- **公司基本資訊** (info) — 本益比 (P/E)、市值、貝他值、產業分類、公司簡介
- **快速報價** (fast_info) — 目前股價、50日/200日移動平均線
- **年度財務報表** (financials) — 收入、淨利、營業利潤、毛利率趨勢
- **季度財務報表** (quarterly_fin) — 近期季度財務表現
- **資產負債表** (balance_sheet) — 年度淨債務、流動比率、債權比、現金部位
- **季度資產負債表** (quarterly_bs) — 季度財務狀況
- **現金流量表** (cashflow) — 自由現金流 (FCF)、營運現金流、資本支出 (Capex)
- **季度現金流量表** (quarterly_cf) — 季度現金流量動向
- **估值指標** — P/E、Forward P/E、EV/EBITDA、P/FCF、P/S 比
- **內部人士交易資訊** (insider) — 高管買賣訊號
- **主要持股人資訊** (major_holders) — 股東集中度分析
- **機構投資人持股** (inst_holders) — 機構投資人佈局

### 技術細節

代理伺服器狀態檢查結果：
- **時間戳記**: 2026-07-07T21:37:36.728Z 起
- **錯誤類型**: connect_rejected
- **詳細訊息**: gateway answered 403 to CONNECT (policy denial or upstream failure)
- **受影響主機**: fc.yahoo.com:443

### 建議後續步驟

1. **等待代理政策更新** — 聯絡網路管理員，請求開放 Yahoo Finance 存取權限
2. **使用替代資料來源** — 若可行，查詢其他財務資料提供商（如 Bloomberg、FactSet、Capital IQ）
3. **重試分析** — 待網路存取恢復後重新執行掃描

---

FUNDAMENTALS REPORT COMPLETE
