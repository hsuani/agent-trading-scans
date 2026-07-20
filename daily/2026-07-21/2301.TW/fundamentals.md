# 基本面分析 — 2301.TW 截至 2026-07-21

## FUNDAMENTALS_DATA_UNAVAILABLE

### 資料來源故障

無法取得 2301.TW（光寶科技 Lite-On Technology）的基本面數據。

**技術原因**：
- Yahoo Finance 資料服務（fc.yahoo.com:443）目前透過代理返回 HTTP 403 Forbidden
- 政策層級網關拒絕，無法迴避或重試
- 替代公開資料源（cnyes、台灣電子所等）未在本管道實裝

**嘗試的資料提取**：
- `yf.py 2301.TW info` — 403 Proxy Block
- `yf.py 2301.TW financials` — 403 Proxy Block
- `yf.py 2301.TW quarterly_fin` — 403 Proxy Block
- `yf.py 2301.TW balance_sheet` — 403 Proxy Block
- `yf.py 2301.TW cashflow` — 403 Proxy Block
- `yf.py 2301.TW insider` — 403 Proxy Block
- `yf.py 2301.TW earnings_dates` — 403 Proxy Block

### 可用替代方案

1. **代理政策調整**：請確認 fc.yahoo.com:443 的訪問政策
2. **替代資料源**：
   - 台灣證券交易所（twse.com.tw）財務報告
   - 公司投資人關係網站（光寶科技 IR）
   - Bloomberg Terminal / FactSet（如機構訪問可用）
3. **延遲重試**：資料可能在 24-48 小時後可用

---

## 部分可用背景資訊（非即時）

**公司簡述**：光寶科技是臺灣大型 ODM/OEM 電子製造商，主要業務包括消費電子、工業電腦、光儲存等。

**市場資訊**（截至最後已知日期）：
- 上市交易所：台灣電子所（TWSE）
- 主要產業：電子設備製造業（Electronics Manufacturing）
- 估計市值：數十億新臺幣（精確數字不可用）

---

## 無法計算的指標

由於資料缺失，以下指標無法驗證或計算：

| 指標 | 狀態 | 原因 |
|---|---|---|
| 營收成長 YoY | ❌ 不可用 | 無財務報表 |
| 淨收入 | ❌ 不可用 | 無財務報表 |
| 自由現金流 (FCF) | ❌ 不可用 | 無現金流數據 |
| FCF/NI 比率 | ❌ 不可用 | 無基礎數據 |
| 向前 P/E | ❌ 不可用 | 無估值數據 |
| EV/EBITDA | ❌ 不可用 | 無估值數據 |
| 淨槓桿率 | ❌ 不可用 | 無資產負債表 |
| 內部人交易 | ❌ 不可用 | 無交易紀錄 |

---

## 建議後續步驟

1. **聯絡資料提供商**：確認 Yahoo Finance 對臺灣股票 ADR/本地掛牌的服務可用性
2. **使用本地資料源**：直接存取 TWSE 公開申報或公司年報
3. **重新排程分析**：在資料連線恢復後重新執行此報告
4. **交叉驗證**：如果取得其他來源數據，務必確認數據頻率和記帳基礎（IFRS vs GAAP）

---

**報告生成時間**：2026-07-21 (UTC+8)
**資料狀態**：FUNDAMENTALS_DATA_UNAVAILABLE
**建議重試**：24-48 小時後或在代理政策更新後
