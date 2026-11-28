# Fundamentals — 3260.TW as of 2026-11-28

## Executive summary
本次基本面資料嚴重不足: `pipeline/tools/yf 3260.TW` 所有財務報表、財報日、內部人交易與持股端點皆回傳空值或 403 (Yahoo 出口被 proxy 拒絕), repo 快取 `prices/3260.TW.csv` 僅含 OHLCV, 無任何營收、獲利、資產負債或現金流數字。因此無法判定財務健康度, 也無法計算任何估值倍數 (P/E、EV/EBITDA、P/FCF、P/S 皆 DATA_UNAVAILABLE), 基本面結論為「資料不足, 無法判定」。可確認的僅有價格與技術面: 最新收盤 TWD 275.5 (2026-11-27), 距 52 週高點 525.0 跌 47.5%, 但 1 年動能仍為 +24.4%。

## Data status and gaps
- 執行環境: `pipeline/tools/yf 3260.TW` 之 live 呼叫皆失敗 (`Cookie/crumb fetch failed`, `CONNECT tunnel failed, response 403`)。工具回傳的 `possibly delisted; no price data found` 為誤導訊息, 與 proxy 出口限制有關, 並非確認下市。
- `info`: 僅回傳 `trailingPegRatio: null` (source: cache, cached_at 2026-11-28T03:33:41+00:00), 其餘欄位 (sector、profile、beta、市值、P/E) 皆 n/a。
- `fast_info`: `last_price` 275.5, `previous_close` 263.0, `day_high` 275.5, `day_low` 258.5, `feed` cnyes, `source` cache (cached_at 2026-11-28T03:32:40+00:00)。`market_cap`、`shares`、`fifty_day_average`、`two_hundred_day_average`、`as_of` 皆 null。
- `financials` / `quarterly_fin` / `balance_sheet` / `quarterly_bs` / `cashflow` / `quarterly_cf`: 空陣列 `[]`。
- `earnings_dates`: `ConnectionError` (403), 下次財報日 n/a。
- `insider` / `major_holders` / `inst_holders`: 空陣列 `[]`, 內部人買賣與持股集中度 n/a。空值不代表無內部人交易。
- `ta 3260.TW snapshot` 可用, `as_of` 2026-11-27 (與 CSV 最後一根 K 線一致, 非 2026-11-28 盤中資料)。
- 價格交叉核對: CSV 2026-11-26 收盤 263 (與 fast_info previous_close 263.0 一致), 2026-11-27 收盤 275.5 (與 last_price 一致)。
- 公司識別: 威剛科技 (ADATA), 記憶體模組廠, 屬 tw_memory 同業組 (2408.TW、2344.TW、8299.TWO、3260.TW)。
- 單位規範: 本報告無任何財務金額可換算, 故不使用億元或 B 數字。若後續補齊資料, 台幣金額應以「億 TWD」呈現, 不與 B 混用。
- 資料補充建議: 改由 MOPS (公開資訊觀測站) 抓取財報與內部人持股變動申報, 或待 Yahoo 端點恢復後重跑本報告。

## Revenue & profitability
DATA_UNAVAILABLE。營收 3-5 年 CAGR、YoY、毛利率、營業利益率、淨利率、ROE、ROIC 皆因財務報表為空而無法計算。不做估計。

前日報告 (`daily/2026-11-27/3260.TW/fundamentals.md`) 引用的定性資訊, 來源為新聞摘要且未經 MOPS 原始公告核對, 僅供參考:
- 2026-11-06 法說會: 第四季營收預期較第三季略降 (年底客戶庫存結算)。
- 第三季表現被認為低於預期, 原因為成本上升壓低毛利。
- 管理層認為 2027 年 DRAM 缺貨可能較 2026 年更嚴重, NAND 價格可望維持高檔。
- 單一券商估計 2027 年毛利率回落至 28.64%。

## Cashflow & balance sheet
DATA_UNAVAILABLE。FCF、FCF/NI、淨負債、流動比率、負債權益比、現金部位皆無數據, 無法評估現金流品質與資產負債表。

## Capital allocation & insider signal
- 資本支出、股利、買回、股利覆蓋率: DATA_UNAVAILABLE。
- 內部人交易 (近 6 個月): 工具回傳空陣列, 無法計算淨買賣與相對市值比例。判定為資料缺口。
- 籌碼面 (法人持股、大股東持股): DATA_UNAVAILABLE。

## Valuation
- 價格基準 (工具回傳, 非確認盤中價): 最新 275.5 TWD (2026-11-27 收盤, 與 prices CSV 一致)。
- trailing P/E、forward P/E、EV/EBITDA、P/FCF、P/S: DATA_UNAVAILABLE (缺 EPS、EBITDA、FCF、營收、股數、市值)。
- 產業中位數: 本報告不估計, 因缺少公司自身基準。
- 前日報告引用之單一券商 2027E EPS (84.15 元) 未經核對, 若採用僅可得約 3.3x 的粗略本益比 (275.5 / 84.15), 但此為景氣高點的單點盈餘預估, 不可單獨據以判斷估值便宜, 本報告不採用此數字作為結論。
- 技術面估值參照 (ta snapshot): 收盤 275.5 位於 MA20 285.25 之下 (-3.4%)、MA50 335.0 之下 (-17.8%)、MA200 378.4 之下 (-27.2%)。

## Key catalysts
- 下次財報日: n/a (`earnings_dates` 連線失敗)。台股公司年度財報一般於次年第一季公布, 需由 MOPS 確認。
- 最近一次法說會: 2026-11-06 (前日報告引用, 未核對)。
- 月營收: 台股公司通常於次月前期限內公布, 實際日期與數字 DATA_UNAVAILABLE。
- 產業面: 2027 年 DRAM / NAND 價格與缺貨程度, 為盈餘預估的主要變數。
- 技術面事件: 20 日均線 285.25 與 52 週區間 171.5 至 525.0 之間的位置, 為短期價格關注點 (僅為事實描述, 非交易建議)。

## Metrics table
單位: 價格為 TWD; 財務金額欄位皆無數據, 故不換算 (億 TWD 欄位保留為 n/a)。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 收盤價 (TWD, 2026-11-27) | 275.5 | 1y 動能 +24.4% (ta mom_12m) | n/a | 工具可用 |
| 前收 (TWD, 2026-11-26) | 263.0 | n/a | n/a | 工具可用 |
| 52 週高 / 低 (TWD) | 525.0 / 171.5 | 距高點 -47.5%, 距低點 +60.6% | n/a | 工具可用 |
| 1m / 3m / 6m 動能 | -23.9% / -34.2% / -32.8% | n/a | n/a | 短中期弱勢 |
| RSI14 / MACD hist | 43.6 / +1.0 | n/a | n/a | 中性偏弱 |
| 營收 (億 TWD) | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | 資料缺口 |
| 營收 CAGR (3-5y) | DATA_UNAVAILABLE | n/a | n/a | 資料缺口 |
| 毛利率 / 營業利益率 / 淨利率 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | 資料缺口 |
| ROE / ROIC | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | 資料缺口 |
| FCF / FCF 利潤比 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | 資料缺口 |
| 淨負債 / D/E / 流動比率 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | 資料缺口 |
| 資本支出 / 股利 / 買回 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | 資料缺口 |
| 內部人淨買賣 (6 個月) | DATA_UNAVAILABLE | n/a | n/a | 資料缺口 |
| Trailing / Forward P/E | DATA_UNAVAILABLE | n/a | n/a | 資料缺口 |
| EV/EBITDA, P/FCF, P/S | DATA_UNAVAILABLE | n/a | n/a | 資料缺口 |
| 市值 / 股數 | DATA_UNAVAILABLE | n/a | n/a | 資料缺口 |

## Red flags
- 基本面資料完全缺失 (yfinance 財務、財報日、內部人與持股端點皆空或 403), 無法排除財務風險, 也無法確認估值是否合理。
- 股價技術面弱勢: 距 52 週高點 -47.5%, 1 個月 -23.9%, 3 個月 -34.2%, 股價位於 MA20、MA50、MA200 之下。市場可能已反映盈餘下修, 但本報告無財務數據可驗證。
- 前日報告引用的新聞摘要指出第三季毛利低於預期、第四季營收季減, 若屬實則短期獲利動能偏弱; 此為未核對的第三方資訊。
- 2027 年毛利率與 EPS 相關估計皆來自單一來源, 未經原始報告核對, 可信度低。
- 內部人與法人持股資料缺失, 無法評估籌碼面的基本面訊號。

FUNDAMENTALS REPORT COMPLETE
