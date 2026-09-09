# 基本面分析 — WDC 截至 2026-09-02

## 資料狀態
**DATA_UNAVAILABLE**

無法從 Yahoo Finance 取得 WDC 財務資料。系統代理連線被拒絕 (CONNECT tunnel failed 403)。

## 問題說明

### 代理政策限制
- 連線目標主機: query2.finance.yahoo.com, fc.yahoo.com, guce.yahoo.com
- HTTP 狀態碼: 403 (Forbidden)
- 錯誤類型: CONNECT tunnel failed — gateway denied CONNECT request
- 原因: Organization policy — egress proxy denied the CONNECT request

### 受影響的資料類別

| 資料類別 | 狀態 |
|---|---|
| 公司基本資訊 (P/E、Beta、市值、產業) | DATA_UNAVAILABLE |
| 年度財務報表 (收入、淨利) | DATA_UNAVAILABLE |
| 季度財務報表 | DATA_UNAVAILABLE |
| 資產負債表 (負債、現金、權益) | DATA_UNAVAILABLE |
| 現金流量表 (營運現金流、自由現金流) | DATA_UNAVAILABLE |
| 本益比、股價移動平均線 | DATA_UNAVAILABLE |
| 內部人交易活動 | DATA_UNAVAILABLE |
| 主要股東持股集中度 | DATA_UNAVAILABLE |

## 無法完成的分析項目

由於缺乏必要的財務數據，以下分析無法執行：

1. **收入與成長性** (Revenue & Growth)
   - 3-5 年 CAGR
   - 同比增長趨勢
   - 事業部門混合

2. **獲利能力** (Profitability)
   - 毛利率、營運利益率、淨利率趨勢
   - ROE (股東權益報酬率)
   - ROIC (投資資本回報率)

3. **現金流與資產負債表** (Cashflow & Balance Sheet)
   - FCF 利益率
   - FCF / NI 比率
   - 淨債務、流動比率
   - 負債/股權比率

4. **資本配置與內部人活動** (Capital Allocation)
   - 資本支出趨勢
   - 股票回購與股利覆蓋率
   - 內部人淨買進/拋售信號

5. **估值** (Valuation)
   - 本益比 (Trailing / Forward)
   - EV/EBITDA
   - P/FCF、P/S vs 產業中位數

6. **催化劑** (Catalysts)
   - 下一個財報日期
   - 最近財報指引
   - 事業部門轉變

## 技術上的根本原因

WDC yfinance 工具無法連接到 Yahoo Finance API 端點，原因是：

```
HTTPS 代理政策限制：
- 組織代理網關拒絕對以下主機的 CONNECT 請求:
  * query2.finance.yahoo.com:443 (財務 API)
  * fc.yahoo.com:443 (Cookie/身份驗證)
  * guce.yahoo.com:443 (GUCE 同意管理)
```

此限制是組織層級的 egress 代理策略決定，無法在此環環境中繞過。

## 報告結論

無法為 WDC 生成完整的基本面分析報告。所有财務指標、估值數據與內部人活動信號均標記為不可用。

---

## 信號評估

| 信號 | 狀態 |
|---|---|
| **Revenue growth signal** | FAIL (DATA_UNAVAILABLE) |
| **FCF signal** | FAIL (DATA_UNAVAILABLE) |
| **Valuation signal** | FAIL (DATA_UNAVAILABLE) |

- **Revenue growth signal**: FAIL — 無法確定 YoY 收入成長是否 > 15%
- **FCF signal**: FAIL — 無法計算 FCF/NI 比率
- **Valuation signal**: FAIL — 無法取得 Forward P/E 或 EPS 成長催化劑數據

---

**FUNDAMENTALS REPORT COMPLETE**
