# 基本面分析 — QBTS 截至 2026-07-21

## FUNDAMENTALS_DATA_UNAVAILABLE

### 資料取得狀態

yfinance 代理連線失敗 (HTTP 403 CONNECT tunnel failed)。無法獲取以下資料：

- **Company Info**: 商業概況、市場資本、部門信息
- **Price & Moving Averages**: 當前價格、50日/200日移動平均線
- **Annual Financials**: 年度收入、毛利率、營業利潤、淨利
- **Quarterly Financials**: 季度損益表
- **Balance Sheet**: 年度資產負債表、流動比率、淨債務
- **Quarterly Balance Sheet**: 季度資產負債表
- **Cashflow**: 年度現金流、自由現金流 (FCF)
- **Quarterly Cashflow**: 季度現金流
- **Earnings Dates & Surprises**: 下次財報日期、EPS 驚喜歷史
- **Insider Transactions**: 內部人士交易 (過去6個月)
- **Major Holders**: 主要股東集中度

### 分析影響

缺少以下核心指標，無法進行完整基本面評估：

| 指標 | 狀態 |
|---|---|
| 營收及成長 (3-5年CAGR) | 不可用 |
| 現金跑道 (Cash Runway) | 不可用 |
| 自由現金流 (FCF) | 不可用 |
| EV/Revenue | 不可用 |
| 內部人交易淨額 | 不可用 |
| P/E 比率 | 不可用 |
| 負債/權益比 | 不可用 |

### 後續步驟

建議待以下條件滿足後重新分析：

1. 確認代理服務連線正常 (fc.yahoo.com:443)
2. 驗證 yfinance 服務可用性
3. 檢查 QBTS 報價數據源

---

**報告生成日期**: 2026-07-21  
**狀態**: FUNDAMENTALS_DATA_UNAVAILABLE  
**數據源**: yfinance (代理不可達)
