FINAL TRANSACTION PROPOSAL: **BUY**

---

# Trade proposal — SNDK as of 2026-07-20

## 資料完整性警告

| 資料源 | 狀態 | 影響 |
|---|---|---|
| market.md 即時報價 | PRICE_DATA_UNAVAILABLE（Yahoo Finance Proxy 403） | 無法給出任何進出場或停損價位 |
| fundamentals.md 主體認定 | 混淆風險：分析師誤將 SNDK 等同於 2016 年被 WDC 收購的舊 SanDisk，忽略 SNDK 已於 2025-02-24 以獨立閃存事業從 WDC 分拆重新上市 | 財務指標需以 investment_plan.md 所引用之分拆後數據為準 |

> 依照「CRITICAL PRICE INTEGRITY RULE」：market.md 報告 PRICE_DATA_UNAVAILABLE，**本提案不設定任何具體進場價、停損價或目標價**，以「無即時價格，暫不給進出場價位」替代。

---

## Direction
**LONG（戰術性做多）**
Conviction：MEDIUM

---

## Setup

**Entry：** 無即時價格，暫不給進出場價位
**Stop：** 無即時價格，暫不給進出場價位
**Target 1：** 無即時價格，暫不給進出場價位
**Target 2：** 無即時價格，暫不給進出場價位
**R:R：** 無法計算（缺乏即時報價）

> 一旦即時報價恢復，應以 investment_plan.md 所標示之「年高點 28% 回撤位」為技術參考建立進場區間，以季線或前期重要支撐為停損錨點，以財報後分析師目標價中值及投資者日公佈 LTA 管道規模為定價 Target 1 / Target 2。

---

## Sizing

**Small（0.5% of portfolio NAV）— 催化劑前初始倉位**
事件驗證後條件性升至 **Medium（1.5% of portfolio NAV）**

**定倉邏輯：**
- Conviction：MEDIUM → 不宜全倉，半倉至六成倉為基準
- ATR：無即時數據，但 investment_plan.md 已記錄該股日波幅 10–20%，屬極高波動性
- 年化波動率估計：基於 10–20% 日波幅推算 annualized vol 遠超 150%，單一持倉需嚴格設倉位上限
- 升倉條件（達成任一即可考慮加碼）：
  1. 2026-08-05 財報 Non-GAAP EPS 超越指引上限 $33，且管理層給出正向 FY2027 指引
  2. 2026-08-13 投資者日量化 LTA 已簽約管道超過 $10B，顯示收入能見度跨越兩年以上

---

## Time horizon

**1–4 週**（戰術性催化劑窗口：2026-08-05 財報 + 2026-08-13 投資者日）

催化劑落地後需以以下數據重新評估是否續持或出場：
- NAND 合約均價趨勢（TrendForce 月報）
- 三星、SK Hynix NAND 資本支出動向
- Q1 FY2027 管理層指引措辭

---

## Trigger

**分步執行策略：**

| 階段 | 條件 | 動作 |
|---|---|---|
| 現在 | 即時報價恢復後，於合理整理區間逢低建立 | Small（0.5%）初始倉 |
| 2026-08-05 財報後 | EPS ≥ $33 + 正向 FY2027 指引 | 加碼至 Medium（1.5%） |
| 2026-08-13 投資者日後 | LTA 管道 > $10B 已量化公佈 | 視情況維持或升至 Large（3%） |
| 上述催化劑未達標 | EPS 低於指引中值或指引保守 | 維持 Small 或平倉 |

---

## Invalidation

以下任一事件發生即視為論點失效，應立即檢討持倉或出場：

1. **供給端逆轉**：Samsung 或 SK Hynix 宣佈恢復大規模 NAND 資本支出
2. **需求端崩潰**：任何大型雲端客戶（Amazon、Microsoft、Google）傳出訂單取消或減量
3. **定價趨勢反轉**：NAND 合約均價連續兩季環比下滑（TrendForce 數據為準）
4. **財報不及預期**：Non-GAAP EPS 低於指引下限 $30，或管理層對 Q1 FY2027 給出保守指引
5. **高管賣出加速**：財報前後出現額外開放市場大量賣出（疊加現有 ~$8M 淨賣出訊號）

---

## Catalyst calendar

| 日期 | 事件 | 重要性 |
|---|---|---|
| 2026-08-05 | Q4 FY2026 財報發布（Non-GAAP EPS 指引中值 $31.5；Q4 營收指引 $7.75B–$8.25B） | 高 — 核心定價催化劑 |
| 2026-08-13 | 投資者日（預計首次量化 LTA 管道金額，提供多年期收入能見度） | 高 — 估值重新錨定機會 |
| 每月持續 | TrendForce NAND 合約均價月報（SLC NAND 及企業 SSD 追蹤） | 中 — 論點維持/失效核心監控點 |

---

> **附注**：空方論點中「峰值盈利低 P/E」商品陷阱（參照 2022 年韓國記憶體股 6–8x 峰值後崩潰案例）及高管集體淨賣出（~$8M，零買入）為本提案最大不確定性因子，是 Small 起倉而非 Medium/Large 起倉的主要理由。催化劑未能驗證可持續性前，不宜重倉。

TRADE PROPOSAL COMPLETE
