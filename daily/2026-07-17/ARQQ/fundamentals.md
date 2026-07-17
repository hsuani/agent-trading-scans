# 基本面分析 — ARQQ 截至 2026-07-17

## 執行摘要

**PRICE_DATA_UNAVAILABLE**

無法完成基本面分析。代理網關阻止對 Yahoo Finance（fc.yahoo.com:443）的連接，返回 403 政策拒絕。所有數據收集工具皆因此失敗。

## 數據可用性狀況

| 組件 | 狀態 | 錯誤信息 |
|---|---|---|
| yf.py ARQQ info | ❌ | ProxyError - CONNECT tunnel failed (403) |
| yf.py ARQQ financials | ❌ | 無返回數據 |
| yf.py ARQQ balance_sheet | ❌ | ProxyError - CONNECT tunnel failed (403) |
| yf.py ARQQ cashflow | ❌ | 無返回數據 |
| yf.py ARQQ insider | ❌ | ProxyError - CONNECT tunnel failed (403) |
| yf.py ARQQ fast_info | ❌ | ProxyError - CONNECT tunnel failed (403) |

## 未能執行的分析

根據既定方法論，以下分析無法執行：

1. **營收與增長** — 無法獲取 3-5 年 CAGR、YoY 趨勢、業務分部組合
2. **獲利能力** — 無法計算毛利率、營業利率、淨利率趨勢、ROE、ROIC
3. **現金流品質** — 無法評估 FCF 利率、FCF / NI 比率
4. **資產負債表健康** — 無法分析淨債務、流動比率、債務股權比、現金頭寸
5. **資本配置** — 無法追蹤資本支出趨勢、回購、股息覆蓋率
6. **內部人士信號** — 無法獲取過去 6 個月內部人士交易、淨買賣活動
7. **估值** — 無法計算尾部/前瞻 P/E、EV/EBITDA、P/FCF、P/S
8. **催化劑** — 無法獲取下次財報日期、近期指引、業務分部變動

## 根本原因

代理政策當前阻止對 Yahoo Finance 主機的 CONNECT 隧道：

```
Gateway Policy Denial
Host: fc.yahoo.com:443
Response: 403
Time: 2026-07-17T05:01:59Z
```

此限制影響所有依賴 yfinance 庫的數據工具。

## 建議的解決方案

1. 聯繫網絡安全團隊申請解除對 `fc.yahoo.com` 的代理限制
2. 檢查 `/root/.ccr/README.md` 了解特定工具的代理配置
3. 考慮使用替代數據提供商（Bloomberg、FactSet、Reuters）
4. 待連接恢復後重新執行 `python3 pipeline/tools/yf.py ARQQ [kind]`

---

**基本面報告狀態：資料不可用 - 無法提供分析**

FUNDAMENTALS REPORT COMPLETE