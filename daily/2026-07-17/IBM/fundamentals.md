# 基本面分析 — IBM 截至 2026-07-17

## PRICE_DATA_UNAVAILABLE

### 報告狀態

**分析日期**: 2026-07-17  
**標籤**: PRICE_DATA_UNAVAILABLE  
**原因**: 代理伺服器政策拒絕 Yahoo Finance 連線

### 技術障礙詳情

**網路連線失敗**
- 時間戳: 2026-07-17 05:02 UTC
- 目標主機: fc.yahoo.com:443
- HTTP 回應碼: 403 Forbidden
- 錯誤類型: CONNECT tunnel failed
- 重試次數: 20+ 次（所有連接均被拒絕）

**影響的資料端點**
1. `IBM info` — 公司基本資訊、估值、sector
2. `IBM financials` — 年度損益表
3. `IBM quarterly_fin` — 季度損益表
4. `IBM balance_sheet` — 年度資產負債表
5. `IBM quarterly_bs` — 季度資產負債表
6. `IBM cashflow` — 年度現金流量表
7. `IBM quarterly_cf` — 季度現金流量表
8. `IBM insider` — 內部人士交易
9. `IBM major_holders` — 主要持股人
10. `IBM inst_holders` — 機構持股人

### 預期分析項目（無法執行）

根據標準分析框架，本報告原應包含：

| 分析項目 | 預期内容 | 狀態 |
|---------|--------|------|
| 營收與成長 | 3-5年 CAGR、YoY 趨勢、事業部門組合 | ❌ 無數據 |
| 獲利能力 | 毛利率、營業利益率、淨利率、ROE、ROIC 趨勢 | ❌ 無數據 |
| 現金流品質 | FCF 利潤率、FCF/NI 比、資本效率 | ❌ 無數據 |
| 資產負債表 | 淨債務、流動比、債權比、現金部位 | ❌ 無數據 |
| 資本配置 | 資本支出趨勢、股票回購、股利覆蓋率 | ❌ 無數據 |
| 內部人士訊號 | 過去6個月淨買/賣、相對市值規模 | ❌ 無數據 |
| 估值 | 本益比、EV/EBITDA、P/FCF、P/S vs sector median | ❌ 無數據 |
| 催化劑 | 下次財報日、最近指引、事業部門變化 | ❌ 無數據 |

### 合規聲明

按照分析框架指引：
- **不虛構數據**: 本報告未包含任何假設、估計或虛構的財務指標
- **不提供交易建議**: 缺乏數據基礎，無法進行基本面評估或價值判斷
- **標記不可用狀態**: 已標示 PRICE_DATA_UNAVAILABLE

### 後續步驟

待下列任一條件滿足後，請重新執行分析：
1. 代理伺服器政策調整，允許 Yahoo Finance 存取
2. 使用替代資料來源（例如：企業披露、彭博終端、FactSet）
3. 網路連線恢復並通過 TLS 驗證

---

FUNDAMENTALS REPORT COMPLETE
