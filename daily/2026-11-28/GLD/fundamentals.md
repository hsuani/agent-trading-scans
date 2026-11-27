# Fundamentals — GLD as of 2026-11-28

註：本報告依 2026-11-28 為分析基準日。工具取得的資料均為 2026-11-27 盤中快取（info 的 regularMarketTime 對應 2026-11-27 約 16:35 UTC，即美東 11:35 左右），屬於基準日之前的資料，未見 2026-11-28 之後的資料。yfinance 多個端點因連線被擋（403 CONNECT tunnel failed）而回傳空值或快取，下文以 DATA_UNAVAILABLE 標示。

## Executive summary
GLD 為 SPDR Gold Shares 實物黃金信託（ETF，非公司），費用率 0.40%、無負債、無股息、無盈餘可分析，基本面評估以淨資產規模、折溢價與費用為主。以 2026-11-27 盤中價 332.16 USD 計，價格較 52 週高點 509.70 USD 低 34.8%，且位於 MA20 / MA50 / MA200 之下，MACD 為負、RSI14 為 35.6，技術面偏弱。報價相對資訊快取內 navPrice 317.58 USD 呈 +4.6% 溢價，與 GLD 通常緊貼 NAV 的特性不符，此差異需先行核實，不能直接當作真實折溢價。

## Revenue & profitability（ETF 不適用）
- 本信託無營收、毛利或營業利益概念。yfinance 的 financials 端點回傳空陣列，故營收 CAGR、利潤率趨勢均為 DATA_UNAVAILABLE。
- info 的 epsTrailingTwelveMonths 為 -9.394 USD，此數字對 grantor trust 無經濟意義（信託不課稅前盈餘，淨值變動不經損益表認列），不納入判斷。
- 報酬率（info）：YTD -9.46%、近 3 月 -2.91%、近 1 年 -15.58%、3 年平均年化 20.85%、5 年平均年化 14.40%。注意：ta 工具算出的 3 個月動能為 -18.79%，與 info 的 trailingThreeMonthReturns 不一致（計算窗口或價格基準不同），兩者並列供參考，不擇一。

## Cashflow & balance sheet（信託結構）
- 現金流量表、資產負債表端點皆回傳空陣列，DATA_UNAVAILABLE。
- 信託本身無舉債（info 未見 debt 欄位，且結構上為實物黃金持有）；無經營現金流，FCF 不適用。
- 淨資產（netAssets / totalAssets）：約 131.01B USD（131,009,642,000 USD）。

## Capital allocation & insider signal
- 股息：trailingAnnualDividendRate 0.0、yield 0.0，信託不派息，不適用股息覆蓋率。
- 買回：信託不買回股份，申購與贖回以實物黃金（Baskets）進行，故無 buyback 概念。
- 內部人交易：insider 端點回傳空陣列，ETF 無內部人申報，不適用。
- 機構持股：major_holders、inst_holders 皆為空，持股集中度 DATA_UNAVAILABLE。
- 資金流（fund flow / 申贖淨額）：工具未提供，DATA_UNAVAILABLE。
- 黃金持有量（噸 / 盎司）：工具未提供，且無即時金價可換算，DATA_UNAVAILABLE。
- 規模趨勢（AUM 歷史序列）：僅有單一時點快照，無法計算 AUM 趨勢，DATA_UNAVAILABLE。
- 成交量：盤中 3.87M 股（不完整日）、10 日均量 13.05M、3 個月均量 9.77M、近期交易量相對偏高，但盤中量尚未完整。

## Valuation（ETF 估值方式）
- 本信託不適用 P/E、EV/EBITDA、P/FCF、P/S；info 的 priceToBook 1.95 係以 bookValue 170.017 計算，但 bookValue 與 navPrice 317.58 明顯不一致，P/B 不採信。
- 費用率 netExpenseRatio 0.40%（即年化費用 0.40%，對 131B 規模相當於每年約 0.52B USD 費用，屬估算，非 yfinance 直接欄位）。
- 折溢價（以 info 數字計算）：
  - 市價 332.16 相對 navPrice 317.58 為 +4.59% 溢價。
  - 買賣價差：bid 331.63 / ask 331.66，價差約 0.03 USD（約 0.01%），流動性極佳。
  - 但 GLD 一般折溢價趨近於 0，4.6% 異常。可能性：(a) navPrice 為較早時點之舊值；(b) 盤中 NAV 未同步更新；(c) 快取時間差。需以官方 NAV 核實後才能採信。
- 價格基準不一：info regularMarketPrice 332.16、fast_info last_price 331.64（cnyes 來源）、ta 最新收盤 332.05。三者差距約 0.5 USD，屬不同來源與時點，以 info 332.16 為盤中參考價。
- 數值一致性：sharesOutstanding 260.3M，但 netAssets 131.01B 除以 260.3M 得 503.3 USD/股，與 navPrice 317.58 不符；反推 131.01B / 317.58 約 4.125 億股（412.5M）。兩者相差約 58%，sharesOutstanding 可能過時或口徑不同，本報告不採用此股數做市值推算。

## Key catalysts
- 下次財報：ETF 無財報，earnings_dates 端點回傳錯誤（CONNECT 403），DATA_UNAVAILABLE，且不適用。
- 影響價格的主要變數在於黃金現貨價格與美元、實質利率、央行購金等宏觀因素，工具未提供這些數據，不作量化。
- 技術位（ta levels）：
  - 壓力：380.18（2026-11-09 高點）、429.42（2026-08-24 高點）。
  - 支撐：363.32（2026-06-24）、363.60（2026-07-17）。
  - 現價 332 已跌破前述兩個支撐，原支撐轉為上方壓力區。
- 布林通道：%B = 0.219，中軌 352.21、上軌 388.11、下軌 316.32。
- ATR14 = 8.32 USD（約 2.5% 價格），20 日年化波動率 34.5%。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 市價 (USD, info 盤中) | 332.16 | n/a | n/a | 參考價 |
| 淨資產 netAssets (USD B) | 131.01B | n/a（僅單點） | n/a | 規模大、流動性佳 |
| 費用率 netExpenseRatio | 0.40% | n/a | n/a（同類 n/a） | 中等偏低，實物金 ETF 常見水準 |
| 官方 NAV navPrice (USD) | 317.58（時點未確定） | n/a | n/a | 需核實 |
| 折溢價 (市價 vs navPrice) | +4.59% | n/a | 約 0% | 異常，待核實 |
| 買賣價差 | 約 0.01% | n/a | n/a | 流動性佳 |
| 52 週區間 (USD) | 313.96 – 509.70 | n/a | n/a | 距高點 -34.8%，距低點 +5.8% |
| YTD 報酬 | -9.46% | n/a | n/a | 弱勢 |
| 1 年報酬 | -15.58% | n/a | n/a | 弱勢 |
| 3 年平均年化報酬 | 20.85% | n/a | n/a | 長期正報酬，波動大 |
| 5 年平均年化報酬 | 14.40% | n/a | n/a | 長期正報酬 |
| 股息殖利率 | 0.0% | n/a | n/a | 不適用 |
| Beta (3Y) | 0.47 | n/a | n/a | 與股市相關性偏低 |
| RSI14 | 35.6 | n/a | n/a | 偏弱，未達超賣 30 |
| MACD / signal / hist | -12.61 / -10.30 / -2.32 | n/a | n/a | 空方動能 |
| MA20 / MA50 / MA200 (USD) | 352.21 / 369.72 / 403.16 | n/a | n/a | 價格低於三條均線 |
| BB %B | 0.219 | n/a | n/a | 位於下半部 |
| ATR14 (USD) | 8.32 | n/a | n/a | 約 2.5% 價格 |
| 20 日年化波動率 | 34.5% | n/a | n/a | 高波動 |
| 成交量（盤中 / 10 日均 / 3 月均） | 3.87M / 13.05M / 9.77M | n/a | n/a | 盤中量未完整 |
| 持股集中度 / 機構持股 | DATA_UNAVAILABLE | n/a | n/a | n/a |
| 申贖資金流 | DATA_UNAVAILABLE | n/a | n/a | n/a |
| 黃金持有量（噸/盎司） | DATA_UNAVAILABLE | n/a | n/a | n/a |
| AUM 歷史趨勢 | DATA_UNAVAILABLE（僅單點） | n/a | n/a | n/a |
| 營收 / 利潤率 / FCF / 負債 | 不適用（信託） | n/a | n/a | 不適用 |
| 內部人交易 | 不適用（無申報） | n/a | n/a | 不適用 |
| 下次財報 | 不適用 | n/a | n/a | 不適用 |

## Red flags
- 折溢價異常：市價對 navPrice 溢價 4.59%，與 GLD 正常應貼近 NAV 的特性不符，需核實 NAV 時點與來源。
- 股數與淨值不一致：sharesOutstanding 260.3M 與 netAssets 131.01B、navPrice 317.58 無法同時成立（隱含股數約 412.5M），bookValue 170.017 亦與 NAV 不符，相關估值指標不採信。
- 技術面全面轉弱：價格低於 MA20 / MA50 / MA200，MACD 空方，已跌破 363 附近支撐。
- 持股、資金流、黃金實物量、AUM 歷史皆 DATA_UNAVAILABLE，無法驗證申贖趨勢或持有量變化，判斷能力受限。
- 資料來源為快取（多數端點 CONNECT 403 後回退 cache），三個價格來源有約 0.5 USD 差異，需以下游交易平台即時報價為準。
- 尚未取得官方 2026-11-28 之後資料，本報告僅以 2026-11-27 盤中快照為依據。

FUNDAMENTALS REPORT COMPLETE
