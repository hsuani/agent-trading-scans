# 基本面分析 — POWL（2026-07-28 截至）

## 執行摘要

無法完成 POWL (Powell Industries) 的基本面分析。yfinance 數據管道因組織出口政策限制而無法連接 Yahoo Finance。建議由上遊管理員解除 fc.yahoo.com:443 的訪問限制，或採用替代數據源進行分析。

## 數據可用性問題

### 根本原因
- **代理拒絕**：組織出口政策（HTTPS_PROXY 通道）被設置為拒絕對 fc.yahoo.com:443 的 CONNECT 請求
- **政策狀態**：403 CONNECT tunnel failed
- **時間戳**：2026-07-27 19:20:49 UTC 至 19:21:39 UTC 期間多次嘗試均失敗

### 受影響的數據類別
以下基本面數據無法取得：

| 數據類別 | API 端點 | 狀態 |
|---|---|---|
| 公司基本信息 | info | 代理拒絕 403 |
| 快速行情 | fast_info | 代理拒絕 403 |
| 年度財報（所得表） | financials | 空返回 |
| 季度所得表 | quarterly_fin | 空返回 |
| 年度資產負債表 | balance_sheet | 空返回 |
| 季度資產負債表 | quarterly_bs | 空返回 |
| 年度現金流量表 | cashflow | 空返回 |
| 季度現金流量表 | quarterly_cf | 空返回 |
| 盈利發布日期 | earnings_dates | 代理拒絕 403 |
| 內部人交易 | insider | 代理拒絕 403 |
| 主要持股者 | major_holders | 代理拒絕 403 |
| 機構持股者 | inst_holders | 代理拒絕 403 |

### 嘗試的方法

1. **直接 yfinance 工具呼叫**：失敗，代理政策拒絕
2. **緩存檢查**：未發現本地緩存的 POWL 基本面數據
3. **替代目錄查詢**：無可用的歷史 POWL 報告

## 無法提供的分析

由於數據不可用，以下基本面分析無法進行：

- **營收與增長**：無法計算 3-5 年 CAGR、同比趨勢、業務分部構成
- **盈利能力**：無毛利率、營業利潤率、淨利潤率趨勢數據；無 ROE、ROIC 計算
- **現金流質量**：無 FCF 邊際率、FCF/NI 比率評估
- **資產負債表**：無淨債務、流動比率、債務/權益比、現金頭寸分析
- **資本配置**：無資本支出趨勢、股票回購、股息覆蓋率信息
- **內部人信號**：無過去 6 個月的內部人買賣活動、交易規模對比市值分析
- **估值**：無尾隨/前瞻 P/E、EV/EBITDA、P/FCF、P/S 對比行業中位數計算
- **催化劑**：無下次盈利發布日期、最近指導、業務分部轉變信息

## 建議後續步驟

1. **網路政策調整**：請聯絡組織網路管理員，解除對 fc.yahoo.com:443 的訪問限制
2. **替代數據源**：考慮使用 Alpha Vantage、IEX Cloud 或其他 API 供應商（需確認代理白名單）
3. **本地數據導入**：如機構內部已有 POWL 的財務數據，可上傳至本地快取，手動導入分析
4. **重試時間**：代理狀態確認網路限制為實時政策決定，建議待管理員確認後重試

## 代理狀態詳情

```json
{
  "proxy_status": "enabled",
  "port": 34337,
  "ca_bundle": "/root/.ccr/ca-bundle.crt",
  "recent_failure_host": "fc.yahoo.com:443",
  "failure_type": "connect_rejected",
  "failure_detail": "gateway answered 403 to CONNECT (policy denial or upstream failure)",
  "failure_count_last_minute": 20
}
```

## 評分表 — 不適用

由於數據不可用，無法填充以下評分表：

| 指標 | 最新值 | 同比 | 行業中位數（估計值） | 評論 |
|---|---|---|---|---|
| 營收 CAGR (3-5y) | n/a | n/a | n/a | 數據不可用 |
| 毛利率 | n/a | n/a | n/a | 數據不可用 |
| 營業利潤率 | n/a | n/a | n/a | 數據不可用 |
| 淨利潤率 | n/a | n/a | n/a | 數據不可用 |
| ROE | n/a | n/a | n/a | 數據不可用 |
| ROIC | n/a | n/a | n/a | 數據不可用 |
| FCF 邊際率 | n/a | n/a | n/a | 數據不可用 |
| FCF / 淨收入 | n/a | n/a | n/a | 數據不可用 |
| 淨債務 | n/a | n/a | n/a | 數據不可用 |
| 流動比率 | n/a | n/a | n/a | 數據不可用 |
| 債務/權益比 | n/a | n/a | n/a | 數據不可用 |
| 尾隨 P/E | n/a | n/a | n/a | 數據不可用 |
| 前瞻 P/E | n/a | n/a | n/a | 數據不可用 |
| EV/EBITDA | n/a | n/a | n/a | 數據不可用 |
| P/FCF | n/a | n/a | n/a | 數據不可用 |
| P/S | n/a | n/a | n/a | 數據不可用 |

## 紅旗 — 不適用

因數據不可用，無法識別潛在的紅旗或風險因子。建議待基本面數據可用後重新評估。

---

FUNDAMENTALS REPORT COMPLETE

**注：** 本報告因組織出口政策限制無法提供完整分析。yfinance 工具的 POWL 數據請求因 fc.yahoo.com:443 403 CONNECT 拒絕而失敗。建議由系統管理員調查並解決網路政策問題。
