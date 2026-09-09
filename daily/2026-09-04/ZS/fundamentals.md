# 基本面分析 — ZS （Zscaler）| 2026-09-04

## 執行總結

**狀態：分析無法進行**

無法完成 ZS 基本面分析。根本原因：組織的出口政策封鎖了 Yahoo Finance（所有連結皆收到 HTTP 403 拒絕）。該公司財務數據的唯一數據來源 yfinance 仍然無法訪問。

---

## 資料訪問障礙

### 網路限制

代理伺服器拒絕訪問以下 Yahoo Finance 域名（HTTP 403 — 組織政策拒絕）：
- `query2.finance.yahoo.com:443`
- `guce.yahoo.com:443`
- `fc.yahoo.com:443`

**根本原因：** 組織的出口代理應用了 CONNECT 政策禁令，阻止訪問 Yahoo Finance

### 可用工具限制

- `yfinance` v1.7.0（唯一配置的財務數據 CLI）需要 Yahoo Finance 訪問
- 無可用的備用數據源或本地快取
- 之前的 ZS 分析（2026-07-28）報告相同的封鎖狀態

---

## 可收集數據（原計畫）

以下指標無法檢索：

| 指標類別 | 所需數據 | 狀態 |
|---|---|---|
| **收入與成長** | 3-5 年年複合成長率（CAGR）、YoY 趨勢、分部組成 | ❌ 無法訪問 |
| **獲利能力** | 毛利率/營業利潤率/淨利率、ROE、ROIC | ❌ 無法訪問 |
| **現金流質量** | FCF、FCF/NI 比率 | ❌ 無法訪問 |
| **資產負債表** | 淨債務、流動比率、債務/權益比率 | ❌ 無法訪問 |
| **資本配置** | 資本支出趨勢、回購、股息覆蓋率 | ❌ 無法訪問 |
| **內部人士活動** | 過去 6 個月的買賣淨額 | ❌ 無法訪問 |
| **估值指標** | P/E（尾隨/前瞻）、EV/EBITDA、P/FCF、P/S | ❌ 無法訪問 |
| **觸發因素** | 下次財報日期、指導意見、分部變化 | ❌ 無法訪問 |

---

## 建議行動

1. **聯絡IT/安全團隊**：請求將 `query2.finance.yahoo.com`、`guce.yahoo.com`、`fc.yahoo.com` 添加至出口許可清單
2. **替代方案**：集成不同的財務數據提供商（如 Alpha Vantage、IEX Cloud、Finnhub）或本地數據快取
3. **重試**：一旦網路訪問恢復，重新運行分析

---

## 中止原因代碼

```
NETWORK_BLOCKED_BY_POLICY
Root: HTTP 403 Forbidden (egress proxy)
Affected: yfinance → Yahoo Finance connectivity
Impact: All financial metrics unavailable
```

---

**報告日期：** 2026-09-04  
**分析狀態：** ⛔ 阻止（資料訪問）  

---

FUNDAMENTALS REPORT COMPLETE
