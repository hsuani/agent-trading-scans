# 基本面分析 — 3653.TW（健策精密）截至 2026-08-09

## 執行摘要

**數據不可用**。Yahoo Finance 資料工具因代理連線障礙（403 隧道錯誤）無法取得 3653.TW 的財務資料。無法產製完整的基本面評估。

## 資料狀態

| 項目 | 狀態 |
|---|---|
| 財務報表（年度） | 無法取得 |
| 快速資訊（價格/MA） | 無法取得 |
| 公司概況 | 無法取得 |
| 資產負債表 | 無法取得 |
| 現金流量表 | 無法取得 |

## 根本原因

- **連線錯誤**：HTTPS 代理隧道失敗（curl 錯誤 7）
- **影響範圍**：Yahoo Finance API 全部端點不可達
- **建議**：待代理服務恢復後重新執行分析

## 記錄

```
時間：2026-08-09 分析執行
工具：yfinance.py
錯誤代碼：ConnectionError - CONNECT tunnel failed, response 403
代碼片段：Failed to perform, curl: (7) CONNECT tunnel failed
```

---

**無法完成基本面分析** — 待數據源恢復可用性。

FUNDAMENTALS REPORT COMPLETE
