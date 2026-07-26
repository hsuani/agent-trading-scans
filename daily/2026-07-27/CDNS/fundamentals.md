# 基本面分析 — CDNS (截至 2026-07-27)

## 數據蒐集失敗報告

### 執行摘要

無法完成 CDNS 基本面分析。組織網路政策阻擋了所有連至 Yahoo Finance 的連線。

### 網路限制詳情

**代理狀態:**
- 啟用代理服務器: http://127.0.0.1:34973
- CA 束位置: /root/.ccr/ca-bundle.crt
- 代理端口: 34973

**阻擋的主機:**
- fc.yahoo.com:443 - 403 policy denial
- query1.finance.yahoo.com:443 - 403 policy denial
- ws.api.cnyes.com:443 - 403 policy denial

**最後連線嘗試時間:** 2026-07-26 17:52:32 UTC 至 17:52:59 UTC

**錯誤訊息:**
```
Failed to perform, curl: (56) CONNECT tunnel failed, response 403.
gateway answered 403 to CONNECT (policy denial or upstream failure)
```

### 嘗試的資料蒐集方法

| 方法 | 狀態 | 備註 |
|------|------|------|
| `yf.py CDNS financials` | 失敗 | 代理 403 阻擋 |
| `yf.py CDNS balance_sheet` | 失敗 | 代理 403 阻擋 |
| `yf.py CDNS cashflow` | 失敗 | 代理 403 阻擋 |
| `yf.py CDNS info` | 失敗 | 代理 403 阻擋 |
| `yf.py CDNS insider` | 失敗 | 代理 403 阻擋 |
| Python yfinance 直接呼叫 | 失敗 | 代理 403 阻擋 |
| curl Yahoo Finance API | 失敗 | 代理 403 阻擋 |

### 根本原因

根據代理狀態輸出和 /root/.ccr/README.md:

> "The destination host is not allowed by your organization's egress policy for this session. Do not retry or route around it — report the blocked host."

目標主機 Yahoo Finance 已被組織出站政策明確禁止。

### 解決方案

下列任一方案可恢復分析能力:

1. **聯絡網路管理員** - 請求將 fc.yahoo.com 和 query1.finance.yahoo.com 加入出站允許清單
2. **提供替代資料源** - 若有其他財務資料 API (Bloomberg、FactSet、Refinitiv 等) 已獲准
3. **本地數據** - 若有離線財務數據庫或 CSV 檔案可用

### 無法完成的分析項目

以下部分無法完成，因缺少基礎財務數據:

- 財務概況 (Revenue & profitability)
- 資產負債表分析 (Balance sheet metrics)
- 現金流量質量 (Cashflow analysis)
- 內部人交易信號 (Insider activity)
- 估值分析 (Valuation metrics)
- 關鍵催化劑 (Catalyst identification)
- 指標表格 (Metrics table)
- 風險旗標 (Red flags)

---

**報告日期:** 2026-07-27  
**分析代碼:** CDNS  
**狀態:** ❌ 失敗 - 網路政策限制
