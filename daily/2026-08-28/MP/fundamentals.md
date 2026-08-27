# 基本面分析 — MP 截至 2026-08-28

## 執行摘要

因組織代理政策封鎖 Yahoo Finance (HTTP 403 於 query2.finance.yahoo.com、fc.yahoo.com、query2.finance.yahoo.com)，無法取得財務數據。yfinance 連線已被上游政策否決。

**狀態：PRICE_DATA_UNAVAILABLE** — 財務基本面數據無法獲取

---

## 數據可用性狀態

| 資料類型 | 狀態 | 說明 |
|---------|------|------|
| 公司資訊 (info) | ❌ 不可用 | 代理 403 |
| 快速資訊 (fast_info) | ❌ 不可用 | 代理 403 |
| 年度財務 (financials) | ❌ 不可用 | 代理 403 |
| 季度財務 (quarterly_fin) | ❌ 不可用 | 代理 403 |
| 資產負債表 (balance_sheet) | ❌ 不可用 | 代理 403 |
| 季度資產負債表 (quarterly_bs) | ❌ 不可用 | 代理 403 |
| 現金流量 (cashflow) | ❌ 不可用 | 代理 403 |
| 季度現金流量 (quarterly_cf) | ❌ 不可用 | 代理 403 |
| 盈利日期 (earnings_dates) | ❌ 不可用 | 代理 403 |
| 內部人士交易 (insider) | ❌ 不可用 | 代理 403 |
| 主要持股人 (major_holders) | ❌ 不可用 | 代理 403 |
| 機構持股人 (inst_holders) | ❌ 不可用 | 代理 403 |

---

## 無法進行的分析

由於無法存取 yfinance 數據，以下分析無法進行：

### 營收與獲利能力
- 營收 3-5 年複合年增長率 (CAGR)：無法計算
- 毛利率、營業利潤率、淨利率趨勢：無法計算
- ROE、ROIC：無法計算
- 業務分部組成：無法取得

### 現金流與資產負債表
- 自由現金流 (FCF) 邊際率：無法計算
- FCF / 淨收入比率：無法計算
- 淨債務、流動比率、債權股權比：無法計算
- 現金持位：無法取得

### 資本配置與內部人士信號
- 資本支出 (CapEx) 趨勢：無法取得
- 股票回購：無法取得
- 股利覆蓋率：無法計算
- 內部人士買賣信號：無法取得

### 估值
- 本益比 (P/E, 尾隨及遠期)：無法計算
- EV/EBITDA：無法計算
- P/FCF、P/S：無法計算
- 與行業中位數比較：無法進行

### 催化劑
- 下次盈利公告日期：無法取得
- 最近指導：無法取得
- 業務分部變化：無法取得

---

## 紅旗評估

因無法存取財務數據，無法進行風險評估。

---

## 指標摘要表

| 指標 | 最新值 | YoY | 行業中位數估計 | 評判 |
|------|-------|-----|--------------|------|
| 營收 (TTM) | n/a | n/a | n/a | 無法評估 |
| 營收 CAGR (3y) | n/a | n/a | n/a | 無法評估 |
| 毛利率 | n/a | n/a | n/a | 無法評估 |
| 營業利潤率 | n/a | n/a | n/a | 無法評估 |
| 淨利潤率 | n/a | n/a | n/a | 無法評估 |
| ROE | n/a | n/a | n/a | 無法評估 |
| ROIC | n/a | n/a | n/a | 無法評估 |
| FCF 邊際率 | n/a | n/a | n/a | 無法評估 |
| FCF / NI | n/a | n/a | >0.9 健康 | 無法評估 |
| 淨債務 / EBITDA | n/a | n/a | n/a | 無法評估 |
| 流動比率 | n/a | n/a | n/a | 無法評估 |
| 債權股權比 | n/a | n/a | n/a | 無法評估 |
| P/E (尾隨) | n/a | n/a | n/a | 無法評估 |
| P/E (遠期) | n/a | n/a | n/a | 無法評估 |
| EV/EBITDA | n/a | n/a | n/a | 無法評估 |
| P/FCF | n/a | n/a | n/a | 無法評估 |
| P/S | n/a | n/a | n/a | 無法評估 |
| 當前價格 | n/a | PRICE_DATA_UNAVAILABLE | n/a | 無法評估 |
| 50 日 MA | n/a | PRICE_DATA_UNAVAILABLE | n/a | 無法評估 |
| 200 日 MA | n/a | PRICE_DATA_UNAVAILABLE | n/a | 無法評估 |

---

## 技術細節

**代理狀態：** HTTP CONNECT tunnel failed, response 403  
**來源：** yfinance 連線失敗 (ConnectionError)  
**時間：** 2026-08-28 分析時刻  
**政策阻擋主機：**
- fc.yahoo.com
- query2.finance.yahoo.com  
- guce.yahoo.com

---

**基本面報告無法完成** — 上游代理政策防止存取 Yahoo Finance 數據源。建議：
1. 確認組織政策是否允許 Yahoo Finance 存取
2. 尋求替代財務數據源 (如公開上市文件、公司 IR 網站)
3. 等待代理政策更新

FUNDAMENTALS REPORT COMPLETE
