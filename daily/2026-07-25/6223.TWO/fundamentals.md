# 基本面分析 — 6223.TWO (旺矽科技) | 2026-07-25

## 價格數據狀態

**PRICE_DATA_UNAVAILABLE**

所有 Yahoo Finance 數據來源已被網路代理政策攔截，返回 HTTP 403 Forbidden。嘗試檢索的資料包括：

- `financials` — 無資料 (empty response)
- `balance_sheet` — 無資料 (empty response)
- `cashflow` — 無資料 (empty response)
- `fast_info` — 連線被拒 (CONNECT tunnel failed)
- `info` — 連線被拒 (CONNECT tunnel failed)
- `insider` — 連線被拒 (CONNECT tunnel failed)
- `major_holders` — 連線被拒 (CONNECT tunnel failed)

**根本原因**：代理網關對 fc.yahoo.com:443 和 ws.api.cnyes.com:443 的 CONNECT 請求返回 403（政策拒絕或上游故障）。

---

## 財務摘要

**無可用資料**

由於 Yahoo Finance 連線被攔截，無法取得：
- 營收 (Revenue) 和成長率 (CAGR)
- 毛利率、營運利潤率、淨利率
- 稅後淨利
- 每股盈餘 (EPS)

---

## 資產負債表

**無可用資料**

無法取得：
- 總資產 (Total Assets)
- 總負債 (Total Liabilities)
- 股東權益 (Shareholders' Equity)
- 流動比率 (Current Ratio)
- 淨負債 (Net Debt)
- 債務/股權比 (Debt/Equity Ratio)
- 現金與等價物 (Cash & Equivalents)

---

## 現金流

**無可用資料**

無法取得：
- 營運現金流 (Operating Cash Flow)
- 自由現金流 (Free Cash Flow, FCF)
- FCF 利潤率 (FCF Margin)
- FCF / 淨利比 (FCF / NI Ratio)
- 資本支出 (Capex)

---

## 估值指標

**無可用資料**

無法計算：
- 本益比 (Trailing P/E)
- 遠期本益比 (Forward P/E)
- EV/EBITDA
- P/FCF (Price/Free Cash Flow)
- 本淨比 (P/B Ratio)
- 本銷比 (P/S Ratio)

**當前股價**：無資料
**市值 (Market Cap)**：無資料
**52週高/低**：無資料

---

## 內部人交易

**無可用資料**

無法取得過去六個月的：
- 內部人買賣交易
- 內部人淨買/淨賣金額
- 交易相對於市值的量級

---

## 風險標誌

1. **資料可用性風險 (Critical)**：所有 Yahoo Finance 來源被代理網關攔截。無法驗證公司財務狀況。

2. **台灣中小型股特性**：6223.TWO 在台灣櫃買中心掛牌，yfinance 對台灣非主板股票的涵蓋深度有限。

3. **替代資料來源缺乏**：無法從 Yahoo Finance 轉向其他可用管道。建議：
   - 直接查閱 TWSE/TPEx 官方公告 (https://mops.twse.com.tw)
   - 公司法說會資料
   - 本地台灣投資研究平臺

---

## 指標摘要表

| 指標 | 最新值 | YoY | 產業中位數 (預估) | 評論 |
|---|---|---|---|---|
| Revenue | n/a | n/a | n/a | 無可用資料 |
| Revenue CAGR (3y) | n/a | n/a | n/a | 無可用資料 |
| Gross Margin | n/a | n/a | n/a | 無可用資料 |
| Operating Margin | n/a | n/a | n/a | 無可用資料 |
| Net Margin | n/a | n/a | n/a | 無可用資料 |
| ROE | n/a | n/a | n/a | 無可用資料 |
| ROIC | n/a | n/a | n/a | 無可用資料 |
| FCF Margin | n/a | n/a | n/a | 無可用資料 |
| FCF / NI | n/a | n/a | 0.9+ (健康) | 無可用資料 |
| Net Debt | n/a | n/a | n/a | 無可用資料 |
| Current Ratio | n/a | n/a | n/a | 無可用資料 |
| Debt/Equity | n/a | n/a | n/a | 無可用資料 |
| Trailing P/E | n/a | n/a | n/a | 無可用資料 |
| Forward P/E | n/a | n/a | n/a | 無可用資料 |
| EV/EBITDA | n/a | n/a | n/a | 無可用資料 |
| P/FCF | n/a | n/a | n/a | 無可用資料 |
| Current Price | n/a | n/a | n/a | 連線被拒 |
| Market Cap | n/a | n/a | n/a | 無可用資料 |

---

## 建議後續步驟

1. **等待代理網路恢復**：確認代理政策設定，允許 Yahoo Finance 連線。

2. **替代資料來源**：
   - 台灣證交所公開資訊觀測站
   - 公司官網投資人關係頁面
   - 台灣本地證券研究平台

3. **下游分析暫停**：在完整財務資料可得之前，無法進行可靠的價值評估或交易信號生成。

---

**分析日期**：2026-07-25  
**資料狀態**：PRICE_DATA_UNAVAILABLE  
**報告完成時間**：同日

FUNDAMENTALS REPORT COMPLETE
