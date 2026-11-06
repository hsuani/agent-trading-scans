# Fundamentals — SH (ProShares Short S&P500) as of 2026-11-07

資料基準：最近一個完整交易日收盤 2026-11-05（ta snapshot as_of 2026-11-05；yf info regularMarketTime 對應 2026-11-05）。yfinance 快取寫入時間為 2026-11-06 14:11 UTC（美東盤前），未使用任何 2026-11-07 之後的資料。本次為 repo 快取結果，財務報表 / 持股 / 基金資金流向等 yfinance 端點皆為空，依規定以 DATA_UNAVAILABLE 標示。

## Executive summary
SH 為 ProShares 發行的 -1x 每日反向 S&P 500 ETF，不是一般公司，無營收、獲利、現金流或資產負債表可評估；基金規模約 9.50 億 USD（950.4M USD）、費用率 0.88%，市價 33.83 USD 與 NAV 33.8381 USD 幾乎等價（折溢價約 -0.02%）。近 1 個月上漲 6.3%、YTD -6.6%，但 1 年期已實現波動約 13.6%，且每日重設與複利耗損使其適合作為短線避險或方向性工具而非長期持有之價值資產。估值面不適用，本報告的判斷重點是結構成本、折溢價、基金規模與技術位置，而非公司基本面。

## Revenue & profitability（不適用，改為標的與規模概況）
- 標的：ProShares Short S&P500（SH），類別 `Trading--Inverse Equity`，NYSE Arca 掛牌，基金家族 ProShares，法律型態 Exchange Traded Fund，成立日（fundInceptionDate）對應 2006-06-19。
- 投資目標（yfinance longBusinessSummary）：透過金融工具組合，使每日報酬約為 S&P 500 每日報酬的 -1 倍；正常情況下至少 80% 總資產為指數成分或具相似經濟特性工具的反向曝險；基金為非分散型（non-diversified）。
- 規模：totalAssets = 950,363,712 USD，netAssets = 950,363,710 USD，即約 950.4M USD（約 0.95B USD）。
- 費用率：netExpenseRatio = 0.88%。
- 績效（ta snapshot / yf info，以 SH 本身價格計）：
  - 1 個月 mom_1m = +6.32%
  - 3 個月 mom_3m = +5.49%
  - 6 個月 mom_6m = -0.09%
  - 12 個月 mom_12m = -7.67%（ta 以收盤價計）；yf info fiftyTwoWeekChangePercent = -8.39%（口徑不同，以 ta 為主）
  - YTD ytdReturn = -6.63%
  - 3Y 平均年報酬 threeYearAverageReturn = -13.31%；5Y 平均年報酬 fiveYearAverageReturn = -7.11%
- 指數敏感度：beta3Year = -0.92（yfinance）。以快取中 SPY 日報酬對照（重疊區間約 2025-10 至 2026-10-15，SPY 快取僅到 2026-10-15，已過期），SH 對 SPY 日報酬迴歸 beta 約 -0.99，1 年期累積報酬 SH -13.8% vs 反向 SPY -14.2%，差距約 0.4 個百分點，與費用率及每日重設耗損方向一致。

## Cashflow & balance sheet（不適用）
- 財務報表（financials / balance_sheet / cashflow 及季報）：yfinance 回傳空陣列，DATA_UNAVAILABLE。ETF 不適用 FCF、ROE、負債比等指標。
- 基金層級的替代指標：
  - 淨資產 netAssets = 950.4M USD。
  - 每股淨值 navPrice = 33.8381 USD。
  - 最近交易日成交量 22,716,297 股（2026-11-05），20 日平均成交量 10.54M 股，60 日平均 8.88M 股，3 個月平均成交量 averageVolume(3M) = 8.77M 股。
  - 盤前買賣報價 bid 33.75 / ask 33.76（價差 0.01 USD，約 0.03%），為盤前報價，非當日收盤數據。
- 持股與交易對手（swap / futures 組合、抵押品、交易對手名單）：yfinance 無此欄位，DATA_UNAVAILABLE。報告中「每日 -1x 曝險工具」之描述係依基金目標描述與任務設定，未能由資料驗證實際工具組成。

## Capital allocation & insider signal
- 內部人交易（insider）：ETF 無內部人持股申報，yfinance 回傳空陣列，n/a。
- 機構持股（major_holders / inst_holders）：yfinance 回傳空陣列，DATA_UNAVAILABLE。
- 資金流向（creation/redemption、shares outstanding、週/月資金流）：工具未提供，DATA_UNAVAILABLE。無法判斷近期是淨流入或淨流出。
- 分配（distribution）：info 同時出現 yield = 0.0387、dividendYield = 3.87，但 trailingAnnualDividendRate = 0.0、trailingAnnualDividendYield = 0.0，兩者互相矛盾。目前無可靠的近 12 個月配息紀錄，SH 之股息數據視為不可靠，不以其計算收益率。
- 結論：無法從本次資料判斷資金面或內部人訊號。

## Valuation
- P/E、forward P/E、EV/EBITDA、P/FCF、P/S：不適用於 ETF，n/a。
- 折溢價（premium / discount to NAV）：
  - 收盤價 regularMarketPrice = 33.83 USD（2026-11-05）
  - navPrice = 33.8381 USD（yfinance info，未附日期，快取時間 2026-11-06）
  - 折溢價 = 33.83 / 33.8381 - 1 ≈ -0.02%，屬於幾乎無折價。
  - 另有 fast_info 來源（cnyes feed）last_price = 33.82，與 33.83 差 0.01 USD，屬來源差異，不影響結論。
- 相對 52 週區間：52w 高 39.20 USD、52w 低 31.64 USD。現價 33.83 距 52w 高 -13.7%，距 52w 低 +6.9%。
- 相對均線（ta）：MA20 32.40（+4.4%）、MA50 32.39（+4.5%）、MA200 34.03（-0.6%）。現價在 MA200 下方一點，但站上 MA20 與 MA50。
- 歷史高點：info allTimeHigh = 843.52 USD，明顯不是同一口徑（可能為未調整之歷史序列），不可與現價比較，不採用。快取日線收盤區間 2024-11-06 至 2026-11-05 的最高收盤為 49.94（2025-04-08），最低為 31.74（2026-10-06）。
- 技術位置（ta snapshot，供 trader 參考，非估值）：RSI14 = 66.997；MACD 0.2131、signal 0.0875、hist 0.1256；布林 %B = 1.237（收盤位於上軌 33.37 之上）；ATR14 = 0.4338 USD（約 1.28% 現價）；20 日年化已實現波動 19.8%，1 年期年化已實現波動 13.6%。

## Key catalysts
- 下次財報：不適用（ETF 無財報）。
- 基金層面事件：Trading--Inverse Equity 類別的主要驅動為 S&P 500 指數走勢與波動度，並非公司事件。
- 單日異動：2026-11-05 SH 大漲 +4.38%（收盤 33.83 vs 前收 32.41），量 22.7M 股，約為 20 日平均量的 2.2 倍，推論為當日 S&P 500 大幅下跌或風險偏好驟降（指數本身資料未取得，未經驗證）。當日事件原因未在工具資料中，DATA_UNAVAILABLE。
- 分配日：無確定的近期分配資料（見上方股息矛盾說明）。
- 其他：無法取得 FOMC、CPI、財報季等具體日期，需由 news / market 報告補充，本報告不臆測日期。

## Metrics table
| Metric | Latest（金額單位：USD；規模以 M USD 標示） | YoY / 區間 | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 基金淨資產 netAssets（M USD） | 950.4 | n/a（無歷史序列） | n/a | 規模足夠，流動性佳 |
| 費用率 netExpenseRatio | 0.88% | n/a | n/a（無同類中位數資料） | 中等偏高，持有成本需計入 |
| 市價 regularMarketPrice（USD，2026-11-05） | 33.83 | 1 年 mom_12m -7.67% | n/a | 反映 S&P 500 下跌之反向報酬 |
| NAV navPrice（USD） | 33.8381 | n/a | n/a | 與市價幾乎相同 |
| 折溢價 Premium/Discount to NAV | -0.02% | n/a | n/a | 無顯著折溢價 |
| YTD 報酬 ytdReturn | -6.63% | — | n/a | 反向基金 YTD 下跌（大盤 YTD 方向未以指數資料驗證） |
| 1 個月報酬 mom_1m | +6.32% | — | n/a | 近期反向獲利 |
| 3 年平均年報酬 | -13.31% | 3Y | n/a | 長期持有侵蝕明顯 |
| 5 年平均年報酬 | -7.11% | 5Y | n/a | 同上 |
| Beta（3Y） beta3Year | -0.92（yfinance）；快取對 SPY 約 -0.99 | — | n/a | 符合 -1x 反向定位 |
| 1 年期已實現波動（年化） | 13.6% | 20 日 19.8% | n/a | 近期波動升高 |
| 52w 區間位置 | 距高點 -13.7%、距低點 +6.9% | — | n/a | 中性偏高檔 |
| RSI14 | 67.0 | — | n/a | 偏熱，超買區邊緣 |
| 布林 %B | 1.24 | — | n/a | 收盤位於上軌之外，短線過熱 |
| ATR14（USD） | 0.43 | — | n/a | 日內波動約 1.3% |
| 平均日成交量（20 日，股） | 10.54M | 3M 平均 8.77M | n/a | 流動性充足 |
| 盤前價差 bid/ask | 0.01 USD（約 0.03%） | — | n/a | 價差小，交易成本低 |
| 股利 yield / trailing 股利 | yield 3.87% vs trailing 0.0 | — | n/a | 資料矛盾，不採用 |
| 持股 / 交易對手 / 資金流 | DATA_UNAVAILABLE | — | n/a | 無法驗證 |

## Red flags
- 每日重設與複利耗損（daily-reset / compounding decay）：SH 目標為「單日」-1x，持有超過一日的報酬可能偏離 -1 倍 S&P 500 累積報酬，波動越高、趨勢不明時偏離越大。長期持有者需承擔耗損風險。
- 費用率 0.88% 加上 3Y/5Y 平均年報酬皆為負值，顯示長期持有成本明顯。
- 股利資料矛盾：yield 3.87% 與 trailing 股利 0.0 不一致，任何以股息為依據的判斷都不可靠。
- 資金流向與持股結構無資料，無法確認基金是否有大量贖回或交易對手風險。
- 歷史高點 allTimeHigh 843.52 不可比，避免被誤用為「跌幅」依據。
- 技術過熱：RSI14 約 67、布林 %B 1.24，當日收盤位於上軌之外，短線回檔或反轉風險升高（僅為技術面觀察，不構成交易建議）。
- 資料時效：SPY 快取僅到 2026-10-15，用於 beta 與追蹤誤差的對照已過期；fast_info 與 info 收盤價差 0.01 USD。
- 盤前 bid/ask 與 navPrice 皆非當日收盤，未附時間戳記的 navPrice 應視為近似值。

FUNDAMENTALS REPORT COMPLETE
