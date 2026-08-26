# Fundamentals — SIVE as of 2026-08-24

## Executive summary

SIVE 的股票代碼在 Yahoo Finance 資料源中無法取得。yfinance 系統回報符號可能已下市（delisted），所有財務資料欄位均為空或返回 404 錯誤。無法生成基本面分析報告。

## Data availability

**資料狀態：無法取得**

| 資料類別 | 狀態 | 備註 |
|---|---|---|
| 基本資料 | quoteType: NONE | tradeable: false |
| 股價 & 移動平均 | 無法找到 | 可能已下市 |
| 年度財報 | 空陣列 | 無收入、資產負債表、現金流資料 |
| 季度財報 | 空陣列 | 無季度財務數據 |
| 盈利日期 | 無法找到 | 無下次盈利公告 |
| 內部人交易 | 404 錯誤 | Quote not found for symbol: SIVE |
| 主要股東 | 404 錯誤 | Quote not found for symbol: SIVE |
| 機構持股 | 404 錯誤 | Quote not found for symbol: SIVE |

## 後續步驟

1. 確認 SIVE 的正確股票代碼
2. 驗證該公司是否已下市或更名
3. 確認是否在其他交易所掛牌（例如：粉紅單市場）
4. 聯絡資料供應商確認符號狀態

---

**報告生成時間：** 2026-08-24  
**資料來源：** yfinance  
**結論：** SIVE 無有效交易資料，無法進行基本面分析。

## Metrics table

| 指標 | 最新 | 年增 | 行業中位數估計 | 評價 |
|---|---|---|---|---|
| 股價 | n/a | n/a | n/a | 已下市 |
| P/E | n/a | n/a | n/a | n/a |
| 市值 | n/a | n/a | n/a | n/a |
| 收益成長率 (3y CAGR) | n/a | n/a | n/a | n/a |
| 毛利率 | n/a | n/a | n/a | n/a |
| 營業利率 | n/a | n/a | n/a | n/a |
| 淨利率 | n/a | n/a | n/a | n/a |
| ROE | n/a | n/a | n/a | n/a |
| FCF / NI | n/a | n/a | n/a | n/a |
| 淨債務 | n/a | n/a | n/a | n/a |
| 流動比率 | n/a | n/a | n/a | n/a |
| EV/EBITDA | n/a | n/a | n/a | n/a |

## Red flags

- **符號無效：** yfinance 無法識別 SIVE，所有 API 呼叫均返回無資料或 404 錯誤
- **交易狀態：** tradeable 標幟為 false，表示無法交易
- **財務數據缺失：** 無年度或季度財報可用
- **下市可能：** 所有特徵指向股票已從公開市場下市

