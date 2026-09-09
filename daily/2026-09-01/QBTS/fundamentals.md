# 基礎面分析 — QBTS 截至 2026-09-01

## 數據可用性狀態

**DATA_UNAVAILABLE**

本報告無法生成，原因如下：

### 問題說明

yfinance 數據工具在此環境中不可用。必要的財務數據來源（~/.claude/tools/trading/yf）未安裝或無法存取。

### 所需數據

本分析需要以下數據以完成全面的基礎面評估：

1. **公司資訊** (info)
   - P/E 比率、Beta、市值、行業分類
   - 公司概述與業務摘要

2. **價格與技術指標** (fast_info)
   - 當前股價
   - 50日和200日移動平均線

3. **財務報表** (financials, quarterly_fin)
   - 年度和季度收入聲明
   - 毛利、營運利潤、凈利潤

4. **資產負債表** (balance_sheet, quarterly_bs)
   - 流動資產與負債
   - 淨債務、現金頭寸

5. **現金流** (cashflow, quarterly_cf)
   - 自由現金流 (FCF)
   - 營運現金流

6. **盈利與內部人士活動** (earnings_dates, insider)
   - 下次盈利公告日期
   - 過去6個月內部人士交易

7. **持股結構** (major_holders, inst_holders)
   - 主要持股人濃度
   - 機構投資者前十大持股

### QBTS 公司背景

D-Wave Quantum (QBTS) 是量子退火技術領先者，專注於商業量子計算應用。

### 後續步驟

請確保下列條件滿足後重新運行此分析：

1. 安裝並配置 yfinance 數據工具
2. 確認網路連接和 API 授權
3. 驗證 ~/.claude/tools/trading/ 目錄結構

---

**分析日期**：2026-09-01  
**報告狀態**：待命 - 無法提供數據

基礎面分析無法進行，無法生成投資決策支持。
