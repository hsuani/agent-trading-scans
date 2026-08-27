# 基本面分析 — GFS 至 2026-07-29

## 執行摘要

**DATA_UNAVAILABLE** — 外部代理伺服器政策限制阻擋了 Yahoo Finance 數據源的存取（fc.yahoo.com 回傳 403 Forbidden）。無法擷取任何財務數據。建議稍後重試或聯繫系統管理員。

## 收入與獲利能力

| 指標 | 數值 | 說明 |
|---|---|---|
| 年營收 (Latest Year) | DATA_UNAVAILABLE | 代理伺服器政策限制 |
| 年營收 YoY 增長 | DATA_UNAVAILABLE | 代理伺服器政策限制 |
| 3-5年 CAGR | DATA_UNAVAILABLE | 代理伺服器政策限制 |
| 毛利率 | DATA_UNAVAILABLE | 代理伺服器政策限制 |
| 營運利率 | DATA_UNAVAILABLE | 代理伺服器政策限制 |
| 淨利率 | DATA_UNAVAILABLE | 代理伺服器政策限制 |
| ROE | DATA_UNAVAILABLE | 代理伺服器政策限制 |
| ROIC | DATA_UNAVAILABLE | 代理伺服器政策限制 |

## 現金流與資產負債表

| 指標 | 數值 | 說明 |
|---|---|---|
| 自由現金流 (FCF) | DATA_UNAVAILABLE | 代理伺服器政策限制 |
| FCF 利率 | DATA_UNAVAILABLE | 代理伺服器政策限制 |
| FCF / 淨收入比率 | DATA_UNAVAILABLE | 代理伺服器政策限制 |
| 流動比率 | DATA_UNAVAILABLE | 代理伺服器政策限制 |
| 淨債務 | DATA_UNAVAILABLE | 代理伺服器政策限制 |
| 債務/權益比 | DATA_UNAVAILABLE | 代理伺服器政策限制 |
| 現金部位 | DATA_UNAVAILABLE | 代理伺服器政策限制 |

## 資本配置與內部人士信號

| 指標 | 數值 | 說明 |
|---|---|---|
| 資本支出趨勢 | DATA_UNAVAILABLE | 代理伺服器政策限制 |
| 股票回購 | DATA_UNAVAILABLE | 代理伺服器政策限制 |
| 股息覆蓋率 | DATA_UNAVAILABLE | 代理伺服器政策限制 |
| 內部人士淨買入/賣出 (過去6個月) | DATA_UNAVAILABLE | 代理伺服器政策限制 |
| 內部人士交易規模 (相對於市值%) | DATA_UNAVAILABLE | 代理伺服器政策限制 |

## 估值

| 指標 | 數值 | 產業中位數 (估計) | 評價 |
|---|---|---|---|
| 本益比 (P/E) — 尾隨 | DATA_UNAVAILABLE | n/a | 無法評估 |
| 本益比 (P/E) — 預期 | DATA_UNAVAILABLE | n/a | 無法評估 |
| EV/EBITDA | DATA_UNAVAILABLE | n/a | 無法評估 |
| P/FCF | DATA_UNAVAILABLE | n/a | 無法評估 |
| P/S (本益銷售比) | DATA_UNAVAILABLE | n/a | 無法評估 |
| 當前股價 | DATA_UNAVAILABLE | n/a | 無法評估 |
| 52週高位/低位 | DATA_UNAVAILABLE | n/a | 無法評估 |

## 關鍵催化劑與事件

| 事件 | 日期 | 說明 |
|---|---|---|
| 下次財報發佈 | DATA_UNAVAILABLE | 代理伺服器政策限制 |
| 最近指引更新 | DATA_UNAVAILABLE | 代理伺服器政策限制 |
| 業務部門變化 | DATA_UNAVAILABLE | 代理伺服器政策限制 |
| 管理層變動 | DATA_UNAVAILABLE | 代理伺服器政策限制 |

## 關鍵指標匯總表

| 指標 | 最新數據 | 年度變化 | 產業中位數 (估計) | 評價 |
|---|---|---|---|---|
| 營收 YoY | DATA_UNAVAILABLE | n/a | n/a | 無法評估 |
| 自由現金流 | DATA_UNAVAILABLE | n/a | n/a | 無法評估 |
| 本益比 (P/E) | DATA_UNAVAILABLE | n/a | n/a | 無法評估 |
| 淨債務 | DATA_UNAVAILABLE | n/a | n/a | 無法評估 |
| ROE | DATA_UNAVAILABLE | n/a | n/a | 無法評估 |
| ROIC | DATA_UNAVAILABLE | n/a | n/a | 無法評估 |

## 風險警示與紅旗

- **代理伺服器政策限制**：外部代理伺服器（http://127.0.0.1:44625）的組織政策阻擋了對 Yahoo Finance（fc.yahoo.com）的存取，回傳 403 Forbidden 錯誤。此為政策層級限制，不應繞過。
- **無可用數據**：因代理伺服器政策，無法從 yfinance 取得任何財務或市場數據。
- **分析延遲**：基本面分析無法進行，直到代理伺服器政策允許對 Yahoo Finance 的存取。

## 技術詳情

**錯誤日期**：2026-07-29 00:22 UTC

**執行的命令**：
```bash
python3 /home/user/agent-trading-scans/pipeline/tools/yf.py GFS financials
python3 /home/user/agent-trading-scans/pipeline/tools/yf.py GFS info
python3 /home/user/agent-trading-scans/pipeline/tools/yf.py GFS insider
python3 /home/user/agent-trading-scans/pipeline/tools/yf.py GFS quarterly_fin
python3 /home/user/agent-trading-scans/pipeline/tools/yf.py GFS balance_sheet
python3 /home/user/agent-trading-scans/pipeline/tools/yf.py GFS cashflow
python3 /home/user/agent-trading-scans/pipeline/tools/yf.py GFS fast_info
```

**代理伺服器狀態**：
- 本地代理：http://127.0.0.1:44625
- CA 證書：/root/.ccr/ca-bundle.crt
- 最近失敗：fc.yahoo.com:443（connect_rejected，403 政策拒絕）

**建議行動**：
1. 聯繫系統管理員檢查代理伺服器政策
2. 驗證 Yahoo Finance 域名存取是否已在白名單上
3. 稍後重試數據擷取
4. 如問題持續，使用替代數據源（如 Alpha Vantage, IEX Cloud 等）

---

**基本面分析報告完成** — 受代理伺服器政策限制，無法進行完整分析
