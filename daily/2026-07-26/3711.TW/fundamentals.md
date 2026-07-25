# 基本面分析 — 3711.TW 截至 2026-07-26

## 執行摘要

**DATA_UNAVAILABLE**

由於代理閘道政策拒絕，無法存取 Yahoo Finance 及台灣股票交易所 (TWSE) 資料來源。本報告無法完成對日月光投控 (3711.TW) 的全面財務分析。關鍵財務指標（營收成長、毛利率、自由現金流、負債權益比、本益比）均未能取得。

## 資料擷取狀態

| 資料來源 | 狀態 | 備註 |
|---|---|---|
| yfinance info | 失敗 | CONNECT tunnel failed (403) |
| yfinance fast_info | 失敗 | CONNECT tunnel failed (403) |
| yfinance financials | 空陣列 | 無資料回傳 |
| yfinance balance_sheet | 空陣列 | 無資料回傳 |
| yfinance cashflow | 空陣列 | 無資料回傳 |
| yfinance insider | 失敗 | CONNECT tunnel failed (403) |
| yfinance major_holders | 失敗 | CONNECT tunnel failed (403) |
| Yahoo Finance 端點 (fc.yahoo.com) | 遭攔截 | 403 policy denial |
| 台灣股票交易所 (mis.twse.com.tw) | 遭攔截 | 403 policy denial |

## 公司概述

**代碼**: 3711.TW  
**公司名稱**: 日月光投控股份有限公司 (ASE Technology Holding Co., Ltd.)  
**產業**: 半導體封測 (OSAT — Outsourced Semiconductor Assembly and Test)  
**市場定位**: 全球最大封測廠商，專精於先進封裝技術（CPO/光子學、高頻射頻、微凸點）  
**交易所**: 台灣證券交易所 (TWSE)

## 分析需求 — 無法完成

以下分析範疇因資料無法取得而無法進行：

1. **營收與成長** — 缺少3-5年CAGR、年度趨勢、業務段構成
2. **獲利能力** — 缺少毛利率、營業利益率、淨利率趨勢、ROE、ROIC
3. **現金流質量** — 缺少自由現金流邊際、FCF/NI比率
4. **資產負債表** — 缺少淨債務、流動比率、負債權益比、現金部位
5. **資本配置** — 缺少資本支出趨勢、回購、股利覆蓋率
6. **內部人士活動** — 缺少過去6個月買賣信號、相對市值規模
7. **估值** — 缺少本益比 (trailing/forward)、EV/EBITDA、P/FCF、P/S 與產業中位數比較
8. **觸發事件** — 缺少下次財報日期、近期指引、業務段轉變

## 技術問題根本原因

代理閘道配置已阻止對以下主機的連接：
- **fc.yahoo.com:443** (Yahoo Finance API) — 403 gateway policy denial
- **mis.twse.com.tw:443** (Taiwan Stock Exchange) — 403 gateway policy denial
- **ws.api.cnyes.com:443** (CMoney Taiwan) — 403 gateway policy denial

根據 `HTTPS_PROXY/__agentproxy/status` 回報，這些是政策等級拒絕，非暫時性故障。yfinance 針對台灣上市公司（尤其是 .TW 代碼）依賴這些來源進行資料擷取。

## 建議後續步驟

1. **網路政策例外申請** — 向系統管理員申請對 TWSE 與 Yahoo Finance 台灣端點的存取權限
2. **替代資料來源** — 考慮直接整合台灣本地資料商（如 TWSE API、Multicharts Taiwan、元大寶來等）
3. **延後分析** — 待網路連接恢復後重新執行資料擷取

## 指標表

| 指標 | 最新數據 | YoY | 產業中位數估計值 | 判定 |
|---|---|---|---|---|
| 營收 (年) | n/a | n/a | n/a | 無資料 |
| 淨利率 | n/a | n/a | n/a | 無資料 |
| 毛利率 | n/a | n/a | n/a | 無資料 |
| 營業利益率 | n/a | n/a | n/a | 無資料 |
| ROE | n/a | n/a | n/a | 無資料 |
| ROIC | n/a | n/a | n/a | 無資料 |
| 自由現金流 (FCF) | n/a | n/a | n/a | 無資料 |
| FCF 邊際 | n/a | n/a | n/a | 無資料 |
| FCF/NI 比率 | n/a | n/a | 0.9+ (健康) | 無資料 |
| 淨債務 | n/a | n/a | n/a | 無資料 |
| D/E 比率 | n/a | n/a | n/a | 無資料 |
| 流動比率 | n/a | n/a | n/a | 無資料 |
| 本益比 (P/E) | n/a | n/a | n/a | 無資料 |
| EV/EBITDA | n/a | n/a | n/a | 無資料 |
| P/FCF | n/a | n/a | n/a | 無資料 |
| P/S | n/a | n/a | n/a | 無資料 |
| 目前股價 | n/a | n/a | n/a | 無資料 |
| 52週高/低 | n/a | n/a | n/a | 無資料 |
| 50日移動平均 | n/a | n/a | n/a | 無資料 |
| 200日移動平均 | n/a | n/a | n/a | 無資料 |

## 紅旗 / 風險警示

由於資料無可取得，無法進行風險評估。

---

## 報告狀態

**FUNDAMENTALS REPORT INCOMPLETE — DATA_UNAVAILABLE**

日期: 2026-07-26  
來源: yfinance (無法連接)  
分析員工作: 無法執行  
修復條件: 代理存取權限已排除至 Yahoo Finance 與 TWSE 端點
