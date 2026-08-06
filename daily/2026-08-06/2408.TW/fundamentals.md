# 基本面分析 — 2408.TW (南亞科技) — 2026-08-06

## 執行摘要

**DATA_UNAVAILABLE**: 由於代理伺服器政策限制 (HTTP 403)，Yahoo Finance 資料來源目前無法存取。本分析無法獲得南亞科技的財務報表、公司指標、內部人交易及分析師評級。完整基本面分析需要恢復 Yahoo Finance 連線或使用替代資料來源。

---

## 資料取得狀況

### 嘗試的資料查詢

| 命令 | 結果 | 狀態 |
|------|------|------|
| `financials` | 空陣列 [] | 失敗 |
| `balance_sheet` | 空陣列 [] | 失敗 |
| `cashflow` | 空陣列 [] | 失敗 |
| `quarterly_fin` | 空陣列 [] | 失敗 |
| `quarterly_bs` | 空陣列 [] | 失敗 |
| `quarterly_cf` | 空陣列 [] | 失敗 |
| `info` | HTTP 403 CONNECT tunnel failed | 被代理伺服器阻止 |
| `fast_info` | HTTP 403 CONNECT tunnel failed | 被代理伺服器阻止 |
| `insider` | HTTP 403 CONNECT tunnel failed | 被代理伺服器阻止 |
| `rec_summary` | HTTP 403 CONNECT tunnel failed | 被代理伺服器阻止 |

**代理錯誤詳情**: `curl: (7) CONNECT tunnel failed, response 403` — fc.yahoo.com 被代理閘道拒絕 (政策禁止或上游故障)

---

## 財務概覽

**無法取得以下指標**:
- 營業收入 (Revenue)
- 年增率 (YoY Revenue Growth)
- 毛利率 (Gross Margin)
- 營業利潤率 (Operating Margin)
- 淨利率 (Net Margin)
- 淨收入 (Net Income)

---

## 資產負債表

**無法取得以下指標**:
- 現金及現金等價物 (Cash & Equivalents)
- 總資產 (Total Assets)
- 總負債 (Total Liabilities)
- 股東權益 (Shareholders' Equity)
- 負債比率 (Debt-to-Equity Ratio)
- 流動比率 (Current Ratio)
- 淨負債 (Net Debt)

---

## 現金流量

**無法取得以下指標**:
- 營運現金流 (Operating Cash Flow)
- 資本支出 (CapEx)
- 自由現金流 (Free Cash Flow, FCF)
- FCF 邊際率 (FCF Margin)
- FCF / 淨收入比 (FCF/NI Ratio)

---

## 估值指標

**無法取得以下指標**:
- 追蹤本益比 (Trailing P/E)
- 前瞻本益比 (Forward P/E)
- 本淨比 (P/B Ratio)
- EV/EBITDA
- 本益銷售比 (P/S)
- 市場資本化 (Market Cap)

---

## 內部人交易信號

**無法取得以下資訊**:
- 內部人買賣交易紀錄 (最近 6 個月)
- 內部人淨買賣立場
- 交易金額相對市值比例

---

## 分析師評級

**無法取得以下資訊**:
- 分析師推薦評級 (買進/持平/賣出)
- 目標價格
- 評級共識

---

## 基本面評估

無法基於財務數據進行評估。完整的基本面分析需要：

1. **恢復 Yahoo Finance 連線** — 聯絡系統管理員解除 fc.yahoo.com 的代理政策限制
2. **替代資料來源** — 考慮使用：
   - 臺灣證交所 (TWSE) 申報資訊平台
   - 南亞科技官方投資者關係報告
   - Bloomberg / FactSet (付費資料庫)
   - 其他臺股財務資料聚合器

---

## 公司背景 (已知資訊)

根據任務指示，南亞科技 (Nanya Technology, 2408.TW) 具有以下特徵：

- **主要股東**: 南亞塑膠 (1303.TW) / 台塑集團持有 28%
- **業務範圍**: 臺灣最大獨立 DRAM 製造商
- **產品**: DDR4 / DDR5 商用及專用 DRAM
- **競爭對手**: Micron、Samsung、SK Hynix
- **產業**: TW 記憶體 (DRAM/NAND) 供應鏈

---

## 關鍵指標表

| 指標 | 數值 | 說明 |
|------|------|------|
| 營業收入成長率 YoY | DATA_UNAVAILABLE | 需要財務報表 |
| 毛利率 | DATA_UNAVAILABLE | 需要財務報表 |
| 淨利率 | DATA_UNAVAILABLE | 需要財務報表 |
| 營運現金流 | DATA_UNAVAILABLE | 需要現金流量表 |
| FCF / NI | DATA_UNAVAILABLE | 需要現金流量表 |
| 負債比率 D/E | DATA_UNAVAILABLE | 需要資產負債表 |
| 本益比 Forward P/E | DATA_UNAVAILABLE | 需要公司資訊 |
| 分析師共識 | DATA_UNAVAILABLE | 無法取得推薦評級 |

---

## 紅旗項目

- **無法取得完整財務數據** — 無法評估收入成長、獲利能力、現金流健全性
- **無法進行估值分析** — 無法計算相對同業估值吸引力
- **無法評估內部人信心** — 無法判斷管理層看法信號
- **分析不完整** — 本報告無法達成基本面研究目標

---

## 後續步驟

1. 確認代理伺服器配置，恢復 Yahoo Finance 存取
2. 若 Yahoo Finance 無法恢復，考慮臺灣在地資料來源 (TWSE API、公司申報資訊)
3. 重新執行完整基本面分析流程

---

**報告日期**: 2026-08-06  
**資料狀態**: 無可用財務數據  
**分析狀態**: 待資料恢復

FUNDAMENTALS REPORT COMPLETE
