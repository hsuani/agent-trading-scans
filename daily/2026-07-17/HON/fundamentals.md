# 基本面分析 — HON（截至 2026-07-17）

## 資料可用性狀況

**PRICE_DATA_UNAVAILABLE**

本分析無法完成。代理伺服器政策阻止存取 Yahoo Finance (fc.yahoo.com)，該平台為 yfinance 工具的必要資料來源。此為組織級別的出口政策限制（HTTP 403 錯誤），無法繞過。

### 被阻止的主機
- fc.yahoo.com:443 - Yahoo Finance 資料伺服器

### 影響範圍
以下資料無法取得：
- 公司基本資料（P/E、市值、行業、公司概況）
- 快速資訊（現價、50日/200日移動平均線）
- 年度財務報表（損益表、資產負債表、現金流）
- 季度財務數據
- 收益日期與 EPS 意外數據
- 內部人士交易活動（過去6個月）
- 主要持股人資訊

### 後續步驟
需要：
1. 聯繫系統管理員或 IT 部門解除對 fc.yahoo.com 的存取限制
2. 或使用替代的財務資料提供者（如：Bloomberg Terminal、FactSet、S&P Capital IQ 等）
3. 或透過已授權的內部資料庫或數據倉庫取得 HON 財務資料

### 分析時間戳記
- 分析日期：2026-07-17
- 報告生成時間：2026-07-17 05:01 UTC
- 資料狀態：不可用（代理政策限制）

---

## 預期分析內容（待資料可用性解決）

本報告原應涵蓋以下章節：

### 執行摘要
HON 的財務健全狀況、估值吸引力評估

### 營收與獲利能力
- 過去3-5年營收複合年成長率（CAGR）
- YoY 趨勢分析
- 毛利率、營業利益率、淨利率趨勢
- ROE、ROIC 指標

### 現金流與資產負債表
- FCF 邊際率
- FCF / 淨收入比率（>0.9 為健康）
- 淨債務、流動比率、債務/股權比
- 現金部位

### 資本配置與內部人士訊號
- Capex 趨勢
- 股票回購與股利配置
- 過去6個月內部人士交易活動（淨買入/賣出、相對市值規模）

### 估值
- 尾隨/前瞻 P/E
- EV/EBITDA、P/FCF、P/S 與行業中位數對比

### 關鍵催化劑
- 下次財報日期
- 最近指引變化
- Quantinuum（量子計算子公司，~54% 持股）業務進展

### 備註：Quantinuum 暴露度
分析應特別關注 HON 對 Quantinuum 的 54% 股權，評估：
- Quantinuum 的燒錢率與融資需求
- 母公司 HON 對 Quantinuum 的潛在資本挹注
- 量子計算市場前景對 HON 估值的潛在影響

## 指標表

| 指標 | 最新值 | YoY | 業界中位數（預估） | 評判 |
|---|---|---|---|---|
| 營收 (年度) | n/a | n/a | n/a | PRICE_DATA_UNAVAILABLE |
| 營收成長 YoY | n/a | n/a | n/a | PRICE_DATA_UNAVAILABLE |
| 營收 CAGR (3y) | n/a | n/a | n/a | PRICE_DATA_UNAVAILABLE |
| 毛利率 | n/a | n/a | n/a | PRICE_DATA_UNAVAILABLE |
| 營業利益率 | n/a | n/a | n/a | PRICE_DATA_UNAVAILABLE |
| 淨利率 | n/a | n/a | n/a | PRICE_DATA_UNAVAILABLE |
| ROE | n/a | n/a | n/a | PRICE_DATA_UNAVAILABLE |
| ROIC | n/a | n/a | n/a | PRICE_DATA_UNAVAILABLE |
| FCF 邊際率 | n/a | n/a | n/a | PRICE_DATA_UNAVAILABLE |
| FCF / 淨收入 | n/a | n/a | >0.9 | PRICE_DATA_UNAVAILABLE |
| 淨債務 | n/a | n/a | n/a | PRICE_DATA_UNAVAILABLE |
| 債務/股權 | n/a | n/a | n/a | PRICE_DATA_UNAVAILABLE |
| 流動比率 | n/a | n/a | n/a | PRICE_DATA_UNAVAILABLE |
| 現股價 | n/a | n/a | n/a | PRICE_DATA_UNAVAILABLE |
| 尾隨 P/E | n/a | n/a | n/a | PRICE_DATA_UNAVAILABLE |
| 前瞻 P/E | n/a | n/a | n/a | PRICE_DATA_UNAVAILABLE |
| EV/EBITDA | n/a | n/a | n/a | PRICE_DATA_UNAVAILABLE |
| P/FCF | n/a | n/a | n/a | PRICE_DATA_UNAVAILABLE |
| P/S | n/a | n/a | n/a | PRICE_DATA_UNAVAILABLE |
| 市值 | n/a | n/a | n/a | PRICE_DATA_UNAVAILABLE |
| Capex (% 營收) | n/a | n/a | n/a | PRICE_DATA_UNAVAILABLE |

## 紅旗警訊

- **資料完全不可用**：無法進行任何基本面分析
- **Quantinuum 風險**：無法評估母公司 HON 對量子計算子公司的財務影響

---

**分析狀態：無法完成**

分析無法進行，直到組織出口政策允許存取 Yahoo Finance 資料來源。

