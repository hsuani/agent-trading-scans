# Fundamentals — GFS as of 2026-07-27

## Executive Summary

無法取得財務數據。代理proxy伺服器拒絕連接到Yahoo Finance與備用數據來源（fc.yahoo.com:443 與 ws.api.cnyes.com:443 返回HTTP 403政策拒絕）。

無法進行基本面分析，因為所有數據源均不可用。

建議重新嘗試或檢查網路連線政策。

## Revenue & Profitability

| 指標 | 狀態 |
|---|---|
| 過去5年營收年複合成長率 (CAGR) | PRICE_DATA_UNAVAILABLE |
| 最近年度營收 | PRICE_DATA_UNAVAILABLE |
| 營收年增長率 (YoY) | PRICE_DATA_UNAVAILABLE |
| 毛利率 (Latest) | PRICE_DATA_UNAVAILABLE |
| 營業利潤率 (Operating Margin) | PRICE_DATA_UNAVAILABLE |
| 淨利潤率 (Net Margin) | PRICE_DATA_UNAVAILABLE |
| ROE (股東權益報酬率) | PRICE_DATA_UNAVAILABLE |
| ROIC (投資資本報酬率) | PRICE_DATA_UNAVAILABLE |

## Cashflow & Balance Sheet

| 指標 | 狀態 |
|---|---|
| FCF Margin | PRICE_DATA_UNAVAILABLE |
| FCF / NI Ratio | PRICE_DATA_UNAVAILABLE |
| 淨債務 (Net Debt) | PRICE_DATA_UNAVAILABLE |
| 流動比率 (Current Ratio) | PRICE_DATA_UNAVAILABLE |
| 負債股權比 (Debt/Equity) | PRICE_DATA_UNAVAILABLE |
| 現金部位 | PRICE_DATA_UNAVAILABLE |

## Capital Allocation & Insider Signal

| 指標 | 狀態 |
|---|---|
| 資本支出趨勢 (Capex Trend) | PRICE_DATA_UNAVAILABLE |
| 回購活動 (Buyback) | PRICE_DATA_UNAVAILABLE |
| 股利覆蓋率 (Dividend Coverage) | PRICE_DATA_UNAVAILABLE |
| 內部人交易 (過去6個月) | PRICE_DATA_UNAVAILABLE |
| 內部人淨買賣與市值比例 | PRICE_DATA_UNAVAILABLE |

## Valuation

| 指標 | 狀態 |
|---|---|
| 本益比 (Trailing P/E) | PRICE_DATA_UNAVAILABLE |
| 本益比 (Forward P/E) | PRICE_DATA_UNAVAILABLE |
| EV/EBITDA | PRICE_DATA_UNAVAILABLE |
| P/FCF (本益比相對自由現金流) | PRICE_DATA_UNAVAILABLE |
| P/S (本淨比) | PRICE_DATA_UNAVAILABLE |
| 同業中位數對比 | PRICE_DATA_UNAVAILABLE |
| 當前股價 | PRICE_DATA_UNAVAILABLE |
| 50日移動平均線 (50D MA) | PRICE_DATA_UNAVAILABLE |
| 200日移動平均線 (200D MA) | PRICE_DATA_UNAVAILABLE |

## Key Catalysts

| 項目 | 狀態 |
|---|---|
| 下次財報發布日期 | PRICE_DATA_UNAVAILABLE |
| 近期指引變化 | PRICE_DATA_UNAVAILABLE |
| 業務部門變動 | PRICE_DATA_UNAVAILABLE |
| 分析師預期變化 | PRICE_DATA_UNAVAILABLE |

## Comprehensive Metrics Table

| 指標 | 最新值 | YoY變化 | 同業中位數 (估計) | 評論 |
|---|---|---|---|---|
| 營收成長率 | PRICE_DATA_UNAVAILABLE | PRICE_DATA_UNAVAILABLE | n/a | 數據不可用 |
| 毛利率 | PRICE_DATA_UNAVAILABLE | PRICE_DATA_UNAVAILABLE | n/a | 數據不可用 |
| 營業利潤率 | PRICE_DATA_UNAVAILABLE | PRICE_DATA_UNAVAILABLE | n/a | 數據不可用 |
| 淨利潤率 | PRICE_DATA_UNAVAILABLE | PRICE_DATA_UNAVAILABLE | n/a | 數據不可用 |
| ROE | PRICE_DATA_UNAVAILABLE | PRICE_DATA_UNAVAILABLE | n/a | 數據不可用 |
| ROIC | PRICE_DATA_UNAVAILABLE | PRICE_DATA_UNAVAILABLE | n/a | 數據不可用 |
| FCF Margin | PRICE_DATA_UNAVAILABLE | PRICE_DATA_UNAVAILABLE | n/a | 數據不可用 |
| 負債股權比 | PRICE_DATA_UNAVAILABLE | PRICE_DATA_UNAVAILABLE | n/a | 數據不可用 |
| 流動比率 | PRICE_DATA_UNAVAILABLE | PRICE_DATA_UNAVAILABLE | n/a | 數據不可用 |
| P/E Ratio | PRICE_DATA_UNAVAILABLE | PRICE_DATA_UNAVAILABLE | n/a | 數據不可用 |
| EV/EBITDA | PRICE_DATA_UNAVAILABLE | PRICE_DATA_UNAVAILABLE | n/a | 數據不可用 |
| P/FCF | PRICE_DATA_UNAVAILABLE | PRICE_DATA_UNAVAILABLE | n/a | 數據不可用 |

## Red Flags

- **數據完全不可用 (Critical)**: 代理伺服器拒絕所有到Yahoo Finance與替代數據源的連接（HTTP 403）
- **無法進行基本面分析 (Critical)**: 無法取得財務報表、現金流、資產負債表或任何歷史數據
- **無法評估營運狀況 (Critical)**: 無法獲得營收、利潤、現金流等核心財務指標
- **無法進行內部人追蹤 (Critical)**: 無法取得內部人交易與大股東部位數據
- **無法進行估值分析 (Critical)**: 無法計算本益比、EV/EBITDA或其他相對估值指標
- **無法追蹤股價與技術指標 (Critical)**: 無法取得當前股價、移動平均線或其他技術數據

## 數據可用性狀態

**報告日期**: 2026-07-27  
**數據來源**: Yahoo Finance (yfinance)  
**數據狀態**: 不可用  
**失敗原因**: HTTP 403 - 代理政策拒絕 (gateway denied CONNECT to fc.yahoo.com:443 and ws.api.cnyes.com:443)

---

**無法產生完整的基本面分析**。所有關鍵財務數據、估值指標、現金流指標、與內部人動向均無法獲取。

建議：
1. 檢查網路連線政策是否允許訪問Yahoo Finance API
2. 確認代理伺服器組態是否需要更新
3. 嘗試使用替代數據源（如 CNYES 或台灣交易所API）
4. 等待數據連線恢復後重新執行分析

