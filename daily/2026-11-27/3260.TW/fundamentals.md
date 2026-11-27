# Fundamentals — 3260.TW as of 2026-11-27

## Executive summary
本次 yfinance 財務資料全數無法取得: 即時 Yahoo 端點全部被 egress proxy 拒絕 (403), repo 快取 `prices/yf/3260.TW.json` 中 financials / balance_sheet / cashflow / earnings_dates / insider / holders 等欄位皆為空值或 null, 因此無法判斷財務健康度與估值是否合理 (基本面結論: 資料不足, 無法判定)。唯一可用的資料為 cnyes 快取報價 (TWD 262.0, 前收 263.0), 以及新聞來源的法說會摘要與單一券商 2027E EPS 預估 (未經原始來源核對)。若要做基本面判斷, 需先補齊 Yahoo 財務報表資料或改用 TWSE / MOPS 來源重抓。

## Data status and gaps
- 本次執行: `pipeline/tools/yf 3260.TW` 所有 live 呼叫皆回傳 `Cookie/crumb fetch failed` 與 `CONNECT tunnel failed, response 403`; proxy 紀錄 finance.yahoo.com、query2.finance.yahoo.com、fc.yahoo.com 等 host 被拒。這屬於 sandbox 出口政策限制, 不是 3260.TW 下市或無資料 (工具回傳的 "possibly delisted" 訊息為誤導)。依 proxy 規則不重試、不繞過。
- `info`: 僅回傳 `trailingPegRatio: null`, 其餘欄位 (P/E、beta、市值、sector、profile) 皆 n/a。
- `financials` / `quarterly_fin` / `balance_sheet` / `quarterly_bs` / `cashflow` / `quarterly_cf`: 空陣列 `[]`, 無任何營收、獲利、資產負債或現金流數字。
- `earnings_dates`: null, 下次財報日 n/a。
- `insider` / `major_holders` / `inst_holders` / `recommendations` / `rec_summary`: 空值, 內部人交易與法人持股 n/a。
- `fast_info`: 快取報價可用 (cnyes feed), `fifty_day_average` / `two_hundred_day_average` / `market_cap` / `shares` 皆 null。
- 幣別單位: 本報告所有金額欄位皆無數據, 故未換算。若後續取得資料, 需以 TWD 億元 (1 億 = 100,000,000) 呈現, 不與 B 混用。
- 公司識別: 依 `daily/2026-11-27/3260.TW/sentiment.md`, 3260.TW 為威剛 (ADATA)。

## Revenue & profitability
n/a。營收 CAGR、YoY、毛利率 / 營業利益率 / 淨利率、ROE、ROIC 皆因財務報表為空而無法計算。

定性資訊 (來源: `sentiment.md` 所引用的新聞搜尋摘要, 未經 MOPS 原始公告核對):
- 2026-11-06 法說會: 第四季營收預期較第三季略降 (年底客戶庫存結算, 12 月備貨偏保守)。
- 法人認為第三季表現低於預期, 原因是成本上升壓低毛利。
- 管理層預期 2027 年 DRAM 缺貨可能較 2026 年更嚴重, NAND 價格可望維持高檔。
- 玉山投顧預估 2027 年毛利率回落至 28.64%。

## Cashflow & balance sheet
n/a。FCF、FCF/NI、淨負債、流動比率、負債權益比、現金部位皆無數據, 無法評估現金流品質與資產負債表。

## Capital allocation & insider signal
- 資本支出、買回、股利覆蓋率: n/a。
- 內部人交易 (近 6 個月): 工具回傳空值, 無法計算淨買賣與相對市值比例。判定為資料缺口, 不代表無內部人交易。

## Valuation
- 市價 (cnyes 快取, 盤中非確認收盤): TWD 262.0, 前收 263.0, 當日高 264.5、低 258.5。
- trailing P/E、forward P/E、EV/EBITDA、P/FCF、P/S: n/a (缺 EPS、EBITDA、FCF、營收、股數)。
- 同業 / 產業中位數: n/a。不做估計, 因為缺乏公司自身基準。
- 單一參考 (僅供核對量級, 非估值依據): 玉山投顧 2027E EPS 84.15 元, 若成立則 262 / 84.15 ≈ 3.1x 2027E 本益比。此數字為單一券商預估, 且記憶體產業景氣高點的盈餘可能不可持續, 不可直接據以判斷估值便宜。
- 目標價參考: 玉山 420 元; Investing.com 頁面 12 個月目標價均值 455 元 (僅列一位分析師、未註明日期, 僅供參考)。兩者皆為第三方資料, 未經核對。

## Key catalysts
- 下次財報日: n/a (earnings_dates 為 null)。台股公司年度財報一般於次年第一季公布, 需由 MOPS 公告確認。
- 最近一次法說會: 2026-11-06 (已發生, 內容見上節)。
- 月營收: 台股公司通常於次月前期限內公布, 需由 MOPS 確認實際日期與數字 (本次無資料)。
- 產業面: 2027 年 DRAM / NAND 價格走勢與缺貨程度, 為盈餘預估的主要變數 (來自法說會管理層說法與新聞摘要)。

## Metrics table
單位: 價格為 TWD; 財務金額欄位無數據, 故以 n/a 表示 (未換算億元)。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 股價 (TWD, cnyes 快取, 盤中) | 262.0 | n/a | n/a | 僅供參考, 非確認收盤 |
| 前收 (TWD) | 263.0 | n/a | n/a | n/a |
| 營收 (億 TWD) | n/a | n/a | n/a | 資料缺口 |
| 毛利率 | n/a | n/a | n/a | 資料缺口 (新聞提及 2027E 約 28.64%, 單一來源) |
| 營業利益率 / 淨利率 | n/a | n/a | n/a | 資料缺口 |
| ROE / ROIC | n/a | n/a | n/a | 資料缺口 |
| FCF / FCF 利潤比 | n/a | n/a | n/a | 資料缺口 |
| 淨負債 / 負債權益比 / 流動比率 | n/a | n/a | n/a | 資料缺口 |
| 資本支出 / 股利 / 買回 | n/a | n/a | n/a | 資料缺口 |
| 內部人淨買賣 (6 個月) | n/a | n/a | n/a | 資料缺口 |
| Trailing / Forward P/E | n/a | n/a | n/a | 資料缺口 |
| 2027E P/E (單一券商 EPS 84.15 估計) | ≈3.1x | n/a | n/a | 第三方單點估計, 不可單獨採信 |
| EV/EBITDA, P/FCF, P/S | n/a | n/a | n/a | 資料缺口 |

## Red flags
- 基本面資料完全缺失 (Yahoo 403 + 快取空值), 無法排除財務風險, 也無法確認估值。
- 新聞摘要顯示第三季毛利低於預期 (成本上升), 第四季營收預期季減, 短期獲利動能偏弱。
- 2027 年毛利率估計 (玉山 28.64%) 若為回落, 代表目前盈餘高點可能已過; 以 2027E EPS 計算的低 P/E 可能是景氣高點的假象。
- 技術面 (`market.md`) 與新聞面均顯示股價大幅回檔: 1m -27.6%, 3m -37.4%, 距 52 週高點 -50.1%。市場可能已反映部分盈餘下修, 但無財務數據可驗證。
- 目標價與 EPS 來源為新聞摘要與單一券商, 未經原始報告核對, 可信度低。
- 內部人與法人持股資料缺失, 無法評估籌碼面的基本面訊號。

FUNDAMENTALS REPORT COMPLETE
