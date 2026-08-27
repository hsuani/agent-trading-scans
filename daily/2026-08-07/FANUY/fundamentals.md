# 基本面分析 — FANUY（截至 2026-08-07）

## 執行摘要

因代理政策限制（fc.yahoo.com 403 禁止），無法從 Yahoo Finance 檢索 FANUY（Fanuc Corp ADR）的實時價格數據和大部分財務報表。已報告 PRICE_DATA_UNAVAILABLE。建議下游分析師重新嘗試數據連接或尋求替代數據源以完成基本面評估。

## 數據連接狀態

**狀態**: PRICE_DATA_UNAVAILABLE

- `fast_info` (價格 + 移動平均線): **連接失敗** (CONNECT tunnel 403)
- `info` (公司資料、P/E、市值、Beta): **連接失敗** (CONNECT tunnel 403)
- `earnings_dates` (下次財報日期): **連接失敗** (CONNECT tunnel 403)
- `insider` (內部人士交易): **連接失敗** (CONNECT tunnel 403)
- `major_holders` (主要股東): **連接失敗** (CONNECT tunnel 403)
- `inst_holders` (機構股東): **連接失敗** (CONNECT tunnel 403)
- `financials` (年度所得): **無數據** (空響應)
- `quarterly_fin` (季度所得): **無數據** (空響應)
- `balance_sheet` (年度資產負債表): **無數據** (空響應)
- `quarterly_bs` (季度資產負債表): **無數據** (空響應)
- `cashflow` (年度現金流): **無數據** (空響應)
- `quarterly_cf` (季度現金流): **無數據** (空響應)

## 營收與獲利能力

**無法分析**。無年度及季度所得報表數據。無法計算：
- 3-5 年收入複合增長率 (CAGR)
- 毛利率、營業利率、淨利率趨勢
- ROE、ROIC

## 現金流與資產負債表

**無法分析**。無現金流表及資產負債表數據。無法評估：
- 自由現金流 (FCF) 比例及品質
- FCF / 淨利比率
- 淨債務、流動比率、債權人權益比
- 現金部位

## 資本配置與內部人士信號

**無法分析**。無內部人士交易、股份回購、股利覆蓋率數據。

## 估值

**無法分析**。無法取得：
- 股價 (PRICE_DATA_UNAVAILABLE)
- 本益比 (P/E)、預期本益比 (Forward P/E)
- EV/EBITDA
- P/FCF
- P/S
- 與行業中位數比較

## 主要催化劑

**無法確定**。缺少下次財報日期及最近指導數據。

## 指標表

| 指標 | 最新數據 | YoY | 行業中位數 (估算) | 評論 |
|---|---|---|---|---|
| 股價 | PRICE_DATA_UNAVAILABLE | n/a | n/a | 無法從 Yahoo Finance 取得 |
| 本益比 (P/E) | n/a | n/a | n/a | 缺少價格及收益數據 |
| Forward P/E | n/a | n/a | n/a | 缺少預期收益 |
| EV/EBITDA | n/a | n/a | n/a | 無財務報表 |
| P/FCF | n/a | n/a | n/a | 無現金流數據 |
| P/S | n/a | n/a | n/a | 無營收及股價 |
| 市值 | n/a | n/a | n/a | 連接失敗 |
| 淨債務 | n/a | n/a | n/a | 無資產負債表 |
| 流動比率 | n/a | n/a | n/a | 無流動資產/負債 |
| 債權人權益比 | n/a | n/a | n/a | 無負債/權益數據 |
| 毛利率 | n/a | n/a | n/a | 無所得報表 |
| 營業利率 | n/a | n/a | n/a | 無所得報表 |
| 淨利率 | n/a | n/a | n/a | 無所得報表 |
| ROE | n/a | n/a | n/a | 無淨利及股東權益 |
| ROIC | n/a | n/a | n/a | 無投資資本報酬 |
| FCF 比例 | n/a | n/a | n/a | 無現金流表 |
| Beta | n/a | n/a | n/a | 連接失敗 |

## 紅旗

- **連接失敗**: fc.yahoo.com 因代理政策禁止 (403)，無法存取任何實時價格及大部分財務數據
- **無財務數據**: 所有財報端點 (年度及季度) 返回空響應，無法進行基本面分析
- **無內部人士信號**: 無內部交易數據，無法評估管理層信心
- **無估值指標**: 缺少價格及 EBITDA 等關鍵指標，無法與同業比較估值吸引力

## 結論

因外部連接限制，無法對 FANUY 執行完整的基本面分析。建議：

1. 確認代理政策是否允許 Yahoo Finance 存取
2. 考慮使用替代數據源 (如 Alpha Vantage、Financial Modeling Prep、公司 IR 網站)
3. 待數據連接恢復後重新執行分析

---

**FUNDAMENTALS COMPLETE**
