# 基本面分析 — WDC (Western Digital) 截至 2026-08-10

## 執行摘要

**PRICE_DATA_UNAVAILABLE**

Yahoo Finance 因組織政策被代理伺服器阻止（403 CONNECT tunnel failed），無法取得 WDC 的財務數據。所有嘗試檢索收入聲明、資產負債表、現金流量及股票行情皆失敗。本報告無法依據實際財務數據提供基本面分析。

---

## 數據可用性狀態

| 數據類型 | 狀態 | 備註 |
|---|---|---|
| 公司資訊 (info) | ❌ 不可用 | 403 Policy denial - fc.yahoo.com blocked |
| 股票行情 (fast_info) | ❌ 不可用 | Yahoo Finance + cnyes/TWSE 皆無法存取 |
| 年度財務報表 (financials) | ❌ 不可用 | 403 Policy denial |
| 季度財務報表 (quarterly_fin) | ❌ 不可用 | 403 Policy denial |
| 年度資產負債表 (balance_sheet) | ❌ 不可用 | 403 Policy denial |
| 季度資產負債表 (quarterly_bs) | ❌ 不可用 | 403 Policy denial |
| 年度現金流量 (cashflow) | ❌ 不可用 | 403 Policy denial |
| 季度現金流量 (quarterly_cf) | ❌ 不可用 | 403 Policy denial |

---

## 預期分析框架 (如數據可用)

若 Yahoo Finance 資料恢復可用，以下為本分析應涵蓋之核心領域：

### 營收與成長性
- 3-5 年複合年均成長率 (CAGR)
- 逐年成長率趨勢
- SNDK 分拆後的 HDD 獨立業務營收軌跡
- 雲端超大規模計算廠商 nearline HDD 需求驅動

### 獲利能力
- 毛利率 / 營業利益率 / 淨利率趨勢
- 淨資產報酬率 (ROE)
- 投入資本報酬率 (ROIC)

### 現金流與資產負債表品質
- 自由現金流 (FCF) 邊際率
- FCF / 淨利比率 (>0.9 為健康)
- 淨負債狀況
- 流動比率
- 負債/股權比率
- 現金部位

### 資本配置與內部人信號
- 資本支出 (Capex) 趨勢
- 回購動向
- 股息覆蓋率
- 過去 6 個月內部交易活動 (淨買進/賣出)

### 估值指標
- 本益比 (P/E) - 尾隨及前瞻
- EV/EBITDA
- P/FCF (本金流倍數)
- P/S (本益比)
- 與 HDD 產業中位數對標

### 關鍵催化劑
- 下次財報公告日期
- 近期指引變化
- 業務結構調整
- AI 訓練需求環境

---

## 代理狀態診斷

**代理阻止詳情：**
```
Host: fc.yahoo.com:443
Response: 403 CONNECT tunnel failed
Reason: Gateway policy denial or upstream failure
Timestamp: 2026-08-10T00:23:54+00:00
```

**故障類別：** 組織外出政策 (Organization egress policy denial)

根據代理文檔，403/407 回應表示目的地主機不被允許通過本會話的組織外出政策。建議不進行重試或迴避，應向管理員或 Anthropic 支援回報該阻止。

---

## 建議行動

1. **與 IT/管理員確認：** 檢查組織政策是否允許存取 Yahoo Finance (fc.yahoo.com)
2. **替代資料來源：** 若政策允許，可嘗試：
   - SEC EDGAR (美國上市公司財務申報)
   - 公司投資者關係網站之財務報表
   - Bloomberg Terminal (如有訪問權)
3. **重試時機：** 待網路/政策變更後重新執行分析

---

## 指標表

無可用數據 - 無法生成指標表

---

**FUNDAMENTALS ANALYSIS COMPLETE**

*報告狀態：數據不可用 - 待組織代理政策調整*
