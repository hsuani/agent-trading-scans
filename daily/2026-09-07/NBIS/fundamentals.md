# 基本面分析 — NBIS 截至 2026-09-07

## 資料可用性

**DATA_UNAVAILABLE**

### 原因
Yahoo Finance 遭到組織政策封鎖（HTTP 403 CONNECT 拒絕）。

查詢 NBIS 的財務資料時，以下域名遭到代理政策否決：
- query2.finance.yahoo.com:443
- guce.yahoo.com:443
- fc.yahoo.com:443

### 嘗試的工具
- yfinance (Python)
- pipeline/tools/yf.py

### 建議
請聯絡系統管理員或 Anthropic 支援以解除對 Yahoo Finance 的政策限制，或使用替代財務資料提供商。

---

**無法完成基本面分析。** 下游研究人員與交易員無法獲得所需的財務數據用於決策。

