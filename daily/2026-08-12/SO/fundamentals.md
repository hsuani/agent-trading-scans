# 基本面分析 — SO 截至 2026-08-12

## 執行摘要

**資料收集失敗 - 網絡政策阻止**

本分析無法完成。組織的出境代理政策目前阻止了對 Yahoo Finance (fc.yahoo.com:443) 的所有存取，該服務是取得 SO (Southern Company) 財務數據的必要資源。根據代理配置文檔，403 政策拒絕不應繞過或重試——應改報告此阻止。

## 收益與成長

無法分析。需要以下數據：

- 5 年年度收益趨勢及 CAGR
- 年度百分比成長率 (YoY growth)
- 按部門分類的收益組合
- 季度收益成長軌跡

**資料來源狀態**：yf.py SO financials、quarterly_fin 端點皆返回空結果或連接失敗。

## 獲利能力

無法分析。所需指標：

- 毛利率 (Gross margin) 趨勢 (年度、季度)
- 營業利潤率 (Operating margin)
- 淨利潤率 (Net margin) 3-5 年趨勢
- ROE (Return on Equity)
- ROIC (Return on Invested Capital)

**資料來源狀態**：所有財務語句端點無法存取。

## 現金流與資產負債表

### 現金流質量

無法分析。所需指標：

- 年度及季度自由現金流 (FCF)
- FCF 保證金率
- FCF / NI 比率 (健康水平 >0.9)
- 營運現金流趨勢

**資料來源狀態**：yf.py SO cashflow、quarterly_cf 失敗。

### 資產負債表狀況

無法分析。所需指標：

- 淨債務 (Net debt)、總債務、現金餘額
- 流動比率 (Current ratio)
- 負債/權益比率 (Debt-to-equity)
- 長期負債趨勢

**資料來源狀態**：yf.py SO balance_sheet、quarterly_bs 無數據返回。

## 資本配置與內部人信號

### 資本配置

無法分析。所需項目：

- 資本支出 (CapEx) 年度趨勢
- 股票回購 (Buyback) 規模及頻率
- 股息支付及覆蓋率 (Dividend coverage)
- 資本配置優先順序信號

**資料來源狀態**：cashflow 端點無法存取。

### 內部人活動

無法分析。所需數據：

- 過去 6 個月內部人淨買賣 (net buying/selling)
- 相對於市值的交易規模量級
- 內部人信心信號

**資料來源狀態**：yf.py SO insider 連接失敗。

## 估值

無法分析。所需指標：

- 尾隨 P/E (Trailing P/E)
- 遠期 P/E (Forward P/E)
- EV/EBITDA
- P/FCF (Price-to-Free-Cashflow)
- P/S (Price-to-Sales)
- 相對於公用事業部門中位數的相對估值

**資料來源狀態**：yf.py SO info、fast_info 無法完成。

## 關鍵催化劑

無法確認。所需信息：

- 下次財報公佈日期
- 近期管理層指導 (Forward guidance)
- 監管或部門轉變信號

**資料來源狀態**：yf.py SO earnings_dates 連接失敗。

## 指標表

| 指標 | 最新 | YoY | 部門中位數 | 判決 |
|---|---|---|---|---|
| 收益增長 YoY | n/a | n/a | n/a | **UNABLE_TO_ASSESS** |
| 毛利率 | n/a | n/a | n/a | **UNABLE_TO_ASSESS** |
| FCF/NI | n/a | n/a | n/a | **UNABLE_TO_ASSESS** |
| Net Debt / EBITDA | n/a | n/a | n/a | **UNABLE_TO_ASSESS** |
| Forward P/E | n/a | n/a | n/a | **UNABLE_TO_ASSESS** |
| Trailing P/E | n/a | n/a | n/a | **UNABLE_TO_ASSESS** |
| ROE | n/a | n/a | n/a | **UNABLE_TO_ASSESS** |
| 整體基本面信號 | **BLOCKED** | n/a | n/a | **FAIL** |

## 紅旗警告

- **網絡政策阻止**：fc.yahoo.com:443 返回 403 CONNECT 拒絕 (policy denial / upstream failure)
- **無完整數據集**：無法收集年度或季度財務語句
- **無估值基準**：無法與行業同儕比較或計算內在價值
- **無內部人信號**：無法評估管理層信心
- **無催化劑預測**：無法確認近期事件風險

## 技術詳情

### 代理狀態
- 本地代理：http://127.0.0.1:41545
- 上游代理政策：CONNECT 隧道至 fc.yahoo.com:443 被拒絕
- 錯誤代碼：403 (policy denial / upstream failure)
- 時間戳：2026-08-11T21:53:33 至 21:54:00 (多次重試)

### 失敗的資料來源
所有 yfinance 端點調用失敗或返回空結果：
- SO info (公司資料、P/E、市值、部門)
- SO fast_info (現價、50/200日均線)
- SO financials (年度損益表)
- SO quarterly_fin (季度損益表)
- SO balance_sheet (年度資產負債表)
- SO quarterly_bs (季度資產負債表)
- SO cashflow (年度現金流)
- SO quarterly_cf (季度現金流)
- SO earnings_dates (下次財報日期、EPS 驚喜)
- SO insider (內部人交易)
- SO major_holders (主要股東集中度)
- SO inst_holders (機構股東名單)

### 政策限制
根據 `/root/.ccr/README.md` 第 52-55 行：
> 「403 / 407 來自代理：目的地主機不允許您組織的出境政策用於此會話。不要重試或繞過它 — 報告被阻止的主機。」

## 結論

無法進行基本面分析。需要組織網絡管理員解除對 fc.yahoo.com 的政策限制，或提供替代的財務數據源 (如企業直接披露、SEC EDGAR API、或許可的第三方數據服務)。

---

**FUNDAMENTALS REPORT COMPLETE**

報告狀態：**NETWORK BLOCKED - 無法收集數據**
分析日期：2026-08-12
