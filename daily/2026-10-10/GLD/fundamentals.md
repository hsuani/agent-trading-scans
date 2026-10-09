# Fundamentals — GLD (SPDR Gold Shares) as of 2026-10-10

## Executive summary
GLD 是追蹤現貨黃金 (gold bullion) 的實體黃金信託 ETF，本身沒有營收、利潤或資產負債表，公司財務指標不適用。最新可用收盤價 378.62 (2026-10-08)，較 52 週高點 509.70 回落 25.7%，價格位於 20/50/200 日均線之下，MACD 為負向、RSI14 為 39.9，技術面偏弱。基金規模約 1,417 億美元、費用率 0.40%，依 yfinance 的 navPrice 計算折溢價約 +0.85%；但資金流、AUM 趨勢與持倉明細在工具中皆無資料，無法驗證基金層級的健康度。

## Instrument profile (取代公司概況)
- 名稱 / 類型：SPDR Gold Shares (GLD)，ETF，類別 Commodities Focused，交易所 NYSEArca (PCX)，幣別 USD。
- 發行人 / 基金家族：State Street Investment Management。
- 成立日：2004-11-18 (由 yfinance fundInceptionDate 換算)。
- 投資目標 (依 longBusinessSummary)：信託持有金條，目標是讓基金份額反映黃金現貨價格表現，扣除信託費用後的報酬。Sponsor 認為此為投資人持有黃金的低成本方式。
- 持倉型態：100% 實體黃金條塊 (physical gold bullion)，由信託持有；工具未提供金庫/保管人或持倉重量、純度等明細，相關欄位為 DATA_UNAVAILABLE。

## Revenue & profitability (不適用，改為基金層級指標)
- 信託無營收與利潤結構，income statement 工具回傳為空陣列，financials / quarterly_fin 皆無資料。
- yfinance 的 epsTrailingTwelveMonths 為 -9.394，此數字源自信託的會計 (未實現黃金價格變動的處理)，不具備一般公司獲利能力的解讀意義，不採用。
- 配息：trailingAnnualDividendRate 與 yield 皆為 0.0，信託不配息。
- 報酬表現 (yfinance 提供)：
  - YTD return：-3.34%
  - 3 個月 trailing return：+3.63% (NAV 基礎亦為 +3.63%)
  - 3 年平均年報酬 (threeYearAverageReturn)：+0.30%
  - 5 年平均年報酬 (fiveYearAverageReturn)：+0.18%
  - 52 週變動 (fiftyTwoWeekChangePercent)：+2.57%
- 價格動能 (ta 工具，以收盤價計算)：1 個月 -6.13%，3 個月 +0.43%，6 個月 -13.54%，12 個月 +3.37%。12 個月數字與 yfinance 52 週數字略有差異，係計算窗口不同所致。

## Cashflow & balance sheet (不適用，改為基金層級指標)
- 信託沒有傳統 FCF 與資產負債表。cashflow / balance_sheet / quarterly_cf / quarterly_bs 工具皆回傳空陣列，FCF/NI、淨負債、流動比率、負債權益比等均為 n/a。
- 規模 (AUM)：yfinance totalAssets 與 netAssets 皆為 141,702,414,336 美元 (約 1,417 億美元)。
- 流通股數：sharesOutstanding 260,300,000 股。
- 資料一致性問題：netAssets / sharesOutstanding 約為每股 544 美元，與 navPrice 375.43 美元明顯不符；另 bookValue 為 170.017，與 navPrice 亦不一致。yfinance 的 sharesOutstanding、bookValue、priceToBook (2.23) 可能來自不同時點或不同口徑，本報告不以 priceToBook 作為估值依據，AUM 僅採用 netAssets 的絕對金額。
- 費用率 (netExpenseRatio)：0.40%，為持有 GLD 的年化成本，這是基金層級最明確的成本指標。
- 波動與風險參數 (ta 工具)：
  - 20 日年化波動率 20.52%
  - ATR14 6.42 美元，約佔價格 1.70%
  - 3 年 beta：0.44 (相對大盤)

## Capital allocation & insider signal (不適用)
- 資本配置：信託不進行再投資、不配息，不回購股份；創建/贖回 (creation/redemption) 由授權參與者 (AP) 以金條與基金份額交換進行。工具未提供創建/贖回量。
- 內部人交易：insider 工具回傳空陣列。信託沒有傳統意義的內部人與管理團隊 (companyOfficers、executiveTeam 皆為空)，此項不適用。
- 機構持股：inst_holders 與 major_holders 皆為空陣列，持有者集中度為 DATA_UNAVAILABLE。
- 資金流 (fund flows)：工具未提供，DATA_UNAVAILABLE。
- AUM 趨勢：工具僅提供單一時點的 netAssets，無歷史序列，AUM 趨勢為 DATA_UNAVAILABLE。

## Valuation (基金層級)
- P/E：trailing EPS 為負且不具意義，判定 不適用。forward P/E 無資料。
- EV/EBITDA、P/FCF、P/S：不適用於信託結構。
- NAV 溢價 / 折價：
  - 最新收盤價 378.62 (2026-10-08，regularMarketPrice)。
  - navPrice 375.43 (yfinance)。
  - 溢價 = (378.62 - 375.43) / 375.43 ≈ **+0.85%**。
  - 注意：navPrice 的時點未在工具中明示，溢價數字僅供參考。
  - bid 383.56 / ask 383.64 與收盤價不在同一交易時段 (屬盤前或其他時段報價)，不採用於溢價計算。
- 相對均線的價格位置 (ta)：
  - 相對 20 日均線 388.72：-2.60%
  - 相對 50 日均線 396.88：-4.60%
  - 相對 200 日均線 415.77：-8.94%
- 52 週區間：360.12 至 509.70，現價距低點 +5.14%、距高點 -25.72%。
- 同業/板塊中位數：工具未提供 hedge 板塊或黃金 ETF 同業數據，sector median 為 DATA_UNAVAILABLE。
- 估值結論：以基金結構而言，GLD 的價值主要由黃金現貨價格決定，「估值便宜或昂貴」不適用此框架；可參考的只有 NAV 溢價 (+0.85%，屬小幅溢價) 與 0.40% 的費用率。

## Key catalysts
- 財報 / 盈餘日期：不適用 (信託無盈餘公告)。earnings_dates 工具回傳連線錯誤，無資料。
- 基金層級事件：工具未提供 sponsor 公告、持倉變動或創建/贖回資料，DATA_UNAVAILABLE。
- 價格結構 (ta levels)：
  - 上方阻力：437.42 (2026-05-07)、429.42 (2026-08-24)
  - 下方支撐：413.28 (2026-05-04)、363.32 (2026-06-24)、363.60 (2026-07-17)
- 近期價格走勢 (prices/GLD.csv)：2026-09-25 收於 393.41，2026-09-28 單日下跌至 377.91 (成交量 14.84M，為近期高量)，之後在 375.88 至 384.59 區間震盪，2026-10-08 收於 378.62。
- 宏觀驅動因素 (定性，非工具數據)：黃金價格通常受實質利率、美元走勢與央行購金等因素影響，本報告未納入這些數值，需由其他 agent 以獨立來源補充。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 收盤價 (2026-10-08) | 378.62 | 52 週變動 +2.57% | n/a | 技術面偏弱，低於 20/50/200 日均線 |
| 日變動 | +0.73% (375.88 → 378.62) | n/a | n/a | 中性 |
| 52 週區間 | 360.12 – 509.70 | 距高點 -25.72% | n/a | 位於區間中下段 |
| 相對 200 日均線 | -8.94% | n/a | n/a | 偏弱 |
| RSI14 | 39.88 | n/a | n/a | 接近弱勢區，未達超賣 |
| MACD (macd / signal / hist) | -5.81 / -4.64 / -1.17 | n/a | n/a | 負向 |
| BB %B | 0.205 | n/a | n/a | 位於下軌附近區段 |
| ATR14 | 6.42 (1.70%) | n/a | n/a | 波動中等 |
| 20 日年化波動率 | 20.52% | n/a | n/a | 中等 |
| 3 年 beta | 0.44 | n/a | n/a | 與大盤相關性低 |
| 總資產 / netAssets | 1,417.02 億美元 | 歷史序列 DATA_UNAVAILABLE | n/a | 規模大，流動性充足 |
| 流通股數 | 260.3 百萬股 | n/a | n/a | 與 netAssets 不一致，僅供參考 |
| 費用率 (netExpenseRatio) | 0.40% | n/a | n/a | 屬被動實體黃金 ETF 常見水準 (estimate) |
| NAV 溢價 | +0.85% | n/a | n/a | 小幅溢價 |
| 日均成交量 (3 個月) | 9.26M 股 | 10 日均量 8.18M | n/a | 流動性充足 |
| 股利殖利率 | 0.00% | n/a | n/a | 信託不配息，符合預期 |
| YTD 報酬 | -3.34% | n/a | n/a | 年內表現偏弱 |
| 3 年平均年報酬 | +0.30% | n/a | n/a | 中性 |
| trailing EPS | -9.394 | n/a | n/a | 不適用 |
| P/E、EV/EBITDA、P/FCF、P/S | n/a | n/a | n/a | 不適用 (信託結構) |
| priceToBook | 2.23 | n/a | n/a | 不採用 (與 NAV 資料不一致) |
| 資金流 / AUM 趨勢 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | 無法評估 |
| 持倉集中度 / 持倉明細 | DATA_UNAVAILABLE | n/a | n/a | 僅知為實體黃金條塊 |
| 內部人交易 | 不適用 (空陣列) | n/a | n/a | 信託無內部人 |
| 下次財報日 | 不適用 | n/a | n/a | 信託無盈餘公告 |

## Red flags
- 基金基本面指標大多不適用：無營收、無利潤、無 FCF，無法以公司財務框架評估「財務健康」。
- 資料一致性：sharesOutstanding (260.3M) × navPrice (375.43) ≈ 977 億美元，與 netAssets 1,417 億美元不符；bookValue 170.02 與 navPrice 亦不符。priceToBook 與部分規模數字不採用。
- 報價時段不一致：bid/ask (383.56 / 383.64) 與 fulldayPrice (382.90) 不屬於 2026-10-08 收盤交易時段，已排除於溢價計算之外。
- 資料時點：最新可用收盤為 2026-10-08；報告日為 2026-10-10，2026-10-09 的交易資料未在快取中。yfinance info 的 cached_at 為 2026-10-09 13:06 UTC，屬於報告日之前的快取。
- 資料缺口：資金流、AUM 歷史、持倉明細、持有者集中度、財報/盈餘日期均為 DATA_UNAVAILABLE 或空值，部分工具 (yfinance 即時端點) 因網路封鎖回傳 403 並改用快取，此為本沙箱環境的預期行為。
- 技術面偏弱：價格低於 20/50/200 日均線，MACD 負向，6 個月動能 -13.54%，為本報告最主要的警示訊號。

FUNDAMENTALS REPORT COMPLETE
