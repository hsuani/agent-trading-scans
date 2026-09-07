# 基本面分析 — ARQQ 截至 2026-09-08

## 執行總結

**DATA_UNAVAILABLE**

yfinance 資料源被組織網際網路政策封鎖（HTTP 403 gateway 拒絕連接 query2.finance.yahoo.com 及 guce.yahoo.com）。無法取得基本面財務數據。本報告標記為不可用狀態。

---

## 營收與獲利能力

**DATA_UNAVAILABLE**

- 年收入趨勢（3-5年CAGR）：不可用
- 年度營收：不可用
- 毛利率、營業利潤率、淨利潤率：不可用
- 淨利潤（年度）：不可用
- ROE、ROIC：不可用

無法從 yfinance 驗證公司公開披露的 ~$1-5M 營收規模及虧損狀況。

---

## 現金流與資產負債表

**DATA_UNAVAILABLE**

- 自由現金流（FCF）：不可用
- FCF 利潤率：不可用
- FCF / 淨利潤比率：不可用
- 淨債務：不可用
- 流動比率：不可用
- 債務/權益比：不可用
- 現金及等價物：不可用

無法評估燒錢速率、流動性或債務結構。

---

## 資本配置與內部人交易信號

**DATA_UNAVAILABLE**

- 過去6個月內部人交易（淨買入/賣出）：不可用
- 交易規模相對市值：不可用
- 資本支出趨勢：不可用
- 回購活動：不可用
- 股利覆蓋率：不可用

無法從內部人行為或資本分配判斷管理層信心。

---

## 估值

**DATA_UNAVAILABLE**

- 追蹤型本益比 (Trailing P/E)：不可用
- 遠期本益比 (Forward P/E)：不可用
- EV/EBITDA：不可用
- P/FCF：不可用
- P/S（相對產業中位數）：不可用
- 市場資本化：不可用
- 當前股價：不可用

無法評估相對估值或絕對估值吸引力。

---

## 關鍵催化劑

**DATA_UNAVAILABLE**

- 下次財報公告日期：不可用
- 最近指引更新：不可用
- 業務部門轉變：不可用
- 量子加密/QKD/衛星密鑰分發相關里程碑：不可用

無法從 yfinance 取得近期財報日期或公司指引。

---

## 指標表

| 指標 | 最新數據 | 年度同比 | 產業中位數（估計） | 評論 |
|---|---|---|---|---|
| 營收 (年度) | n/a | n/a | n/a | DATA_UNAVAILABLE |
| 淨利潤率 | n/a | n/a | n/a | DATA_UNAVAILABLE |
| FCF 利潤率 | n/a | n/a | n/a | DATA_UNAVAILABLE |
| 淨債務 | n/a | n/a | n/a | DATA_UNAVAILABLE |
| 流動比率 | n/a | n/a | n/a | DATA_UNAVAILABLE |
| 本益比 (Trailing) | n/a | n/a | n/a | DATA_UNAVAILABLE |
| EV/EBITDA | n/a | n/a | n/a | DATA_UNAVAILABLE |
| P/FCF | n/a | n/a | n/a | DATA_UNAVAILABLE |
| ROE | n/a | n/a | n/a | DATA_UNAVAILABLE |
| 股價 | n/a | n/a | n/a | DATA_UNAVAILABLE |

---

## 紅旗警示

基於不可用的資料，無法識別紅旗指標。

---

## 技術備註

**問題根源：** 組織網際網路政策透過 CONNECT tunnel 拒絕 query2.finance.yahoo.com:443 及其他 Yahoo Finance 端點之連接。

**嘗試的工具：**
- `yf.py ARQQ info`：失敗
- `yf.py ARQQ financials`：失敗
- `yf.py ARQQ quarterly_fin`：失敗
- `yf.py ARQQ balance_sheet`：失敗
- `yf.py ARQQ quarterly_bs`：失敗
- `yf.py ARQQ cashflow`：失敗
- `yf.py ARQQ quarterly_cf`：失敗
- `yf.py ARQQ earnings_dates`：失敗
- `yf.py ARQQ insider`：失敗
- `yf.py ARQQ major_holders`：失敗
- `yf.py ARQQ inst_holders`：失敗

**替代資源：** Bash/Read/Write 工具集無法存取替代財務資料來源（Bloomberg、FactSet、Capital IQ、公司 IR 網站）。

---

**背景資訊（來自任務描述）：**
- ARQQ (Arqit Quantum) 專注於量子加密/QKD/衛星型密鑰分發
- 營收規模極小（~$1-5M）
- 高度虧損狀態（heavy burn）

**報告狀態：** ❌ DATA_UNAVAILABLE

---

FUNDAMENTALS REPORT COMPLETE
