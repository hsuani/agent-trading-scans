# Fundamentals — SH (ProShares Short S&P500) as of 2026-10-10

> 資料時效說明：本次為 cache 資料。最新價格時間戳對應 2026-10-08 收盤（regularMarketPrice 31.97，cache 寫入時間 2026-10-09 13:07 UTC）。報告 as-of 日期 2026-10-10 尚未有資料，未使用任何 post-date 數據。yfinance 即時端點多數被 403 阻擋，財務報表、持股、內部人交易、earnings 等欄位回傳空陣列或錯誤，以下標示 DATA_UNAVAILABLE。

## Executive summary
SH 是 ProShares 發行的 -1x 每日反向 S&P 500 ETF，屬於避險工具而非營運公司，不適用傳統營收、獲利、估值框架。以 2026-10-08 收盤 31.97 計，股價位於 MA20 / MA50 / MA200 下方（MA200 距離 -6.96%），RSI14 為 42.45、MACD 柱狀體為負，技術面偏弱，這反映的是底層 S&P 500 在近期偏強（推論，因 SPY 即時資料不可得）。費用率 0.88%、資產規模約 10.15 億美元，結構性拖累（費用加每日再平衡複利損耗）是持有時間拉長後的主要成本，與基本面「好壞」無關。

## Revenue & profitability（不適用，改為工具結構分析）
- 追蹤標的：S&P 500 指數的每日 -1x 反向報酬（longBusinessSummary：「inverse exposure to at least 80% of its total assets in components of the index or in instruments with similar economic characteristics」，non-diversified）。
- 實現方式：目錄文字未明確列出 swap 或 futures 的占比，此部分標示為 DATA_UNAVAILABLE（僅知結構上使用衍生性工具與類似經濟特性的資產）。
- 報酬表現（yfinance info）：
  - 1 年價格報酬 fiftyTwoWeekChangePercent = -15.31%
  - YTD return = -7.96%
  - 3 個月 trailing = -0.88%
  - 3 年年化平均 = -14.04%；5 年年化平均 = -8.62%
- beta3Year = -0.95，顯示與 S&P 500 近乎完全反向，避險方向性正確。
- 追蹤差異（tracking difference）與實際費用後報酬：DATA_UNAVAILABLE（缺基準指數 SPY 即時資料，無法比對）。

## Cashflow & balance sheet（不適用）
- SH 為基金，無自身損益表、資產負債表、現金流量表。financials / balance_sheet / cashflow 三端點回傳空陣列，依規定標示 DATA_UNAVAILABLE。
- 基金層面的資產端：totalAssets = 1,015,440,704 美元，netAssets = 1,015,440,700 美元（約 10.15 億美元）。
- 持有的衍生性部位（swap / futures 名目金額、交易對手風險、抵押品品質）：DATA_UNAVAILABLE。
- 每日再平衡與複利損耗（decay）分析（估算，非 yfinance 直接輸出）：
  - 以 SH 自身 20 日年化波動 vol_20d_annualized = 9.65% 作為 S&P 波動的代理，σ² ≈ 0.93%/年。
  - 對 -1x 工具，再平衡造成的路徑相依損耗約為 σ²T（推導：L(L-1)/2 = 1），即年化約 -0.9%，波動放大時損耗線性增加（σ 加倍，損耗約 4 倍）。
  - 此為粗估，未計入融資成本與 swap 利差。
  - 目前低波動環境下 decay 本身不大，但 0.88% 費用率的持續性拖累大於 decay。

## Capital allocation & insider signal
- 資本配置（buyback / dividend / capex）：不適用於 ETF。
- 股息：info 欄位 dividendYield = 3.92%、yield = 0.0392，但 SH 結構上不以配息為目的，此數值疑似 distribution 紀錄或資料異常，需人工核實，本報告不以此作為收益依據。
- 內部人交易：insider 回傳空陣列；ETF 無內部人交易概念，標示為 n/a / DATA_UNAVAILABLE。
- 基金流向（fund flows / creations-redemptions）：DATA_UNAVAILABLE。歷史 AUM 趨勢也無法取得，僅有單點 totalAssets。
- 機構持有人與持股集中度（inst_holders / major_holders）：回傳空陣列，DATA_UNAVAILABLE。

## Valuation
ETF 不適用 P/E、EV/EBITDA、P/FCF、P/S 指標，以下為工具相關的估值與交易指標：
- 現價 regularMarketPrice = 31.97；前收 31.82；盤中區間 31.84 – 32.11。
- NAV（navPrice）= 31.8201，現價相對 NAV 溢價約 +0.47%（31.97 / 31.8201 - 1）。溢價幅度小，流動性尚可。
- 52 週區間 31.64 – 39.20；距 52 週高點 -18.44%，距 52 週低點 +1.04%，股價貼近年度低檔。
- 均線：MA20 32.316（-1.07%）、MA50 32.371（-1.24%）、MA200 34.363（-6.96%），股價位於所有主要均線下方。
- 技術指標（ta snapshot，as_of 2026-10-08）：RSI14 = 42.45；MACD = -0.168、signal = -0.122、histogram = -0.046；布林 %B = 0.268（BB 中軌 32.316、上軌 33.062、下軌 31.570）；ATR14 = 0.281（約 0.88% of price）。
- 動能：1 個月 -2.17%、3 個月 -2.32%、6 個月 -11.90%、12 個月 -13.22%。
- 成交量：當日 9,319,919 股；10 日均量 9,654,750；3 個月均量 7,871,042，成交量高於均值。
- 支撐 / 壓力（ta levels）：壓力 34.42（2026-06-09）、33.96（2026-07-29）、33.27（2026-09-16）；支撐 32.71（2026-06-01）、32.70（2026-07-10）、31.83（2026-08-13）。
- 資料異常：allTimeHigh = 843.52、allTimeLow = 11.24 明顯為未經拆股調整的歷史價格，不可用於分析。

## Key catalysts
- 下次 earnings：不適用（ETF 無財報）。earnings_dates 端點回傳 ConnectionError，DATA_UNAVAILABLE。
- 底層驅動：S&P 500 的宏觀事件（FOMC、CPI、就業數據、大型科技股財報季）會直接反向影響 SH。本次資料未提供這些事件的日期，DATA_UNAVAILABLE。
- 基金事件（分配、拆股、費用率調整、結構變更）：corporateActions = []，目前無已公告事件。
- 技術面關鍵價位：若 S&P 反彈推升 SH 收復 MA20（32.32）與 33.27 壓力，代表底層指數回落的訊號減弱；反之若跌破 31.83 支撐，代表 SH 創 52 週新低（需 31.64 以下），反向部位跌幅擴大。此為價格結構描述，不構成交易建議。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 現價（regularMarketPrice，2026-10-08 收盤） | 31.97 | -15.31%（52 週價格報酬） | n/a（無同類中位數） | 股價貼近 52 週低點 |
| NAV | 31.8201 | DATA_UNAVAILABLE | n/a | 溢價 +0.47%，正常範圍 |
| 費用率（netExpenseRatio） | 0.88% | DATA_UNAVAILABLE | n/a | 偏高，持有期拖累明顯 |
| 基金規模（totalAssets） | 約 10.15 億美元 | DATA_UNAVAILABLE（僅單點） | n/a | 規模中等，流動性足夠 |
| 歷史 AUM 趨勢 / 資金流向 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | 無法判斷 |
| YTD 報酬 | -7.96% | n/a | n/a | 與 S&P 反向，符合預期 |
| 3 年年化平均報酬 | -14.04% | n/a | n/a | 長期結構性下跌，符合 -1x 與費用拖累 |
| beta3Year（對 S&P） | -0.95 | n/a | n/a | 反向相關強，避險方向正確 |
| 20 日年化波動（SH 代理） | 9.65% | DATA_UNAVAILABLE | n/a | 波動低，decay 估算約 -0.9%/年 |
| 估算 decay（σ²T） | 約 -0.9%/年 | n/a | n/a | 粗估，低波動環境影響小 |
| RSI14 | 42.45 | n/a | n/a | 偏弱但未超賣 |
| MACD 柱狀體 | -0.046 | n/a | n/a | 空方動能 |
| 股價 vs MA200 | -6.96% | n/a | n/a | 長期趨勢偏弱 |
| 52 週位置（距高 / 距低） | -18.44% / +1.04% | n/a | n/a | 貼近低檔 |
| ATR14 占股價比 | 0.88% | n/a | n/a | 日內波動溫和 |
| 股息 / 殖利率（dividendYield） | 3.92%（疑異常） | DATA_UNAVAILABLE | n/a | 不採信，需核實 |
| 內部人交易 | DATA_UNAVAILABLE | n/a | n/a | ETF 不適用 |
| 機構持有人 / 持股集中度 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | 無法判斷 |
| 財務報表（營收 / 獲利 / 現金流 / 資產負債） | DATA_UNAVAILABLE | n/a | n/a | ETF 不適用 |
| earnings 日期 / EPS 驚喜 | DATA_UNAVAILABLE | n/a | n/a | ETF 不適用 |
| SPY 對照（基準即時資料） | DATA_UNAVAILABLE | n/a | n/a | 無法計算追蹤差異 |
| P/E、EV/EBITDA、P/FCF、P/S | n/a | n/a | n/a | ETF 不適用 |

## Red flags
- 結構性拖累：0.88% 年費率加上 -1x 每日再平衡，長期持有必然侵蝕價值。3 年年化 -14.04% 顯示此工具不適合作為長期部位。
- 資料缺口大：財務、持股、資金流、內部人、earnings、SPY 對照全部 DATA_UNAVAILABLE，無法驗證 AUM 趨勢與資金動向。
- 股息欄位異常：dividendYield 3.92% 與 SH 結構不符，需人工核實後才能採信。
- 歷史價格異常：allTimeHigh 843.52 / allTimeLow 11.24 未經調整，若下游程式直接使用會產生錯誤判斷。
- 底層方向風險：SH 與 S&P 500 反向，若 S&P 持續上漲，SH 將持續承壓（技術面目前偏弱即是此現象的反映）。
- 衍生性工具風險：swap / futures 交易對手與抵押品細節無法驗證。
- 時效性：資料為 cache，最新為 10-08 收盤，與 as-of 10-10 之間有間隔，且 yfinance 即時端點被阻擋，部分欄位來自 cnyes fallback，報價需與交易前即時資料再核對。

FUNDAMENTALS REPORT COMPLETE
