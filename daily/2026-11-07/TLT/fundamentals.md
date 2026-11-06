# Fundamentals — TLT as of 2026-11-07

資料說明：本次為 iShares 20+ Year Treasury Bond ETF 基金標的，非營運公司。Yahoo 即時連線於沙箱中失敗 (403 CONNECT tunnel)，所有數據來自 repo 快取 (`prices/yf/TLT.json`, `prices/TLT.csv`, `ta TLT snapshot`)。最新價格 bar 為 2026-11-05 收盤；快取更新時間 2026-11-06 14:11 UTC。未使用 2026-11-07 之後的任何資料。

## Executive summary
TLT 為追蹤 ICE 20 年期以上美國公債指數的長天期國債 ETF，AUM 約 47.5B USD、淨費用率 0.15%，2026-11-05 收盤 81.93 USD 與 NAV 81.90 USD 幾乎等價 (溢價約 +0.03%)，基金本身的成本與折溢價結構無異常。「財務健康」與本益比等公司層級指標不適用，本標的的核心風險為利率曲線長端變動；技術面上股價位於 MA50 (80.40) 與 MA20 (80.52) 之上，但仍低於 MA200 (84.50) 約 3.05%，屬偏中性、短線偏多、長線未收復的格局。估值吸引力無法以傳統倍數衡量，目前可用資料不足以判斷殖利率相對 (實際存續期間、持股明細、資金流向皆為 DATA_UNAVAILABLE)。

## Revenue & profitability (不適用，改為標的與規模概況)
- 標的性質：ETF，無營收、毛利、營業利益或淨利概念，EPS 與 P/E 不適用。Yahoo 回傳之 `epsTrailingTwelveMonths` (-12.586) 與 `forwardPE` (-4096.5) 對基金無意義，不採用。
- 規模：`totalAssets` / `netAssets` = 47,518,568,448 USD，約 47.5B USD (USD 以 B 標示)。
- 報酬表現 (vendor 提供)：
  - YTD 報酬 -2.92%
  - 近 12 個月 (`fiftyTwoWeekChangePercent`) -8.53%
  - 近 3 個月 (`trailingThreeMonthReturns`) +0.72%
  - 3 年平均年化 (`threeYearAverageReturn`) +1.99%
  - 5 年平均年化 (`fiveYearAverageReturn`) -7.79%
- 追蹤指數：剩餘年期 >20 年、面額 3 億 USD 以上之美國公債 (排除 Fed 持有部分)；基金至少 90% 資產投資於美國公債。
- 成立日：fundInceptionDate 對應 2002 年 (firstTradeDate 1028035800000 ms)；`allTimeHigh` 179.7 為歷史高點，`allTimeLow` 76.43 與目前 52 週低點相同。

## Cashflow & balance sheet (不適用)
- 基金無現金流量表與資產負債表意義上的 FCF、淨負債、流動比率，yfinance 的 financials / balance_sheet / cashflow 皆為空陣列。
- 替代觀察：基金淨資產 (NAV) 與市價之間的折溢價是本標的最重要的「健康度」指標。最新快取：
  - 市價 (2026-11-05 收盤) 81.93 USD
  - NAV (`navPrice`) 81.90298 USD
  - 折溢價 = 81.93 / 81.90298 - 1 ≈ +0.03%，屬正常範圍，無明顯折溢價風險
  - 注意：`navPrice` 之日期欄位未提供，無法確認是否為 2026-11-05 收盤 NAV，需以 iShares 官網每日 NAV 核對
- 流動性：近 3 個月平均日成交量 `averageVolume` 39,525,664 股；10 日平均 34,105,130 股；2026-11-05 成交量 50,197,900 股 (CSV)。買賣價差 bid 82.92 / ask 82.97 (快取，時點不明)，價差約 0.06%，流動性充足。
- 殖利率：
  - 趨勢殖利率 (trailing) = 2.152 / 81.93 ≈ 2.63% (與 `trailingAnnualDividendYield` 0.02632 一致)
  - Yahoo `yield` / `dividendYield` 欄位為 4.76%，與 trailing 數值不一致，疑為不同定義 (可能為 SEC yield 或其他口徑)，本報告以 trailing 2.63% 為主，4.76% 僅列為參考且需核對
- 存續期間 (duration)、凸性 (convexity)：DATA_UNAVAILABLE。依指數定義屬長天期 (剩餘年期 >20 年)，實際 modified duration 數值未取得，不可估算。

## Capital allocation & insider signal
- 內部人交易：ETF 無內部人申報制度，`insider` 回傳空陣列，判定為 n/a。
- 機構持有：`major_holders` 與 `inst_holders` 皆回傳空陣列，持有人集中度 DATA_UNAVAILABLE。
- 資金流向 (fund flows / creations-redemptions)：DATA_UNAVAILABLE，目前工具鏈未提供。
- 分配政策：
  - 配息：`trailingAnnualDividendRate` 2.152 USD/年 (未取得個別配息明細與配息頻率，不作進一步推論)
  - 股份數：`sharesOutstanding` = 109,700,000，與 AUM 47.5B USD 及價格 81.9 USD 推算之約 580M 股明顯不符，疑為資料錯誤或過時，本報告不採用
- 資本支出、回購、股利覆蓋率等公司指標不適用。

## Valuation
- 本益比 (trailing P/E)：`trailingPE` 未提供，n/a
- 遠期本益比：forwardPE -4096.5 無意義，不採用
- P/B：`priceToBook` 0.55 係以 `bookValue` 148.865 計算，但對債券 ETF 而言 bookValue 欄位與 NAV 81.9 不一致，屬資料定義問題，不作為估值依據；以 NAV 為準，折溢價約 +0.03%
- EV/EBITDA、P/FCF、P/S：不適用
- 風險指標 (vendor 與計算值)：
  - `beta3Year` 2.30 (對股市 beta；對國債 ETF 而言數值偏高，需以 vendor 定義核對，不作直接解讀)
  - 20 日年化波動率 10.8% (ta)
  - ATR14 0.78 USD，占股價 0.95%
- 技術位置 (ta snapshot, as_of 2026-11-05)：
  - 價格 81.93；MA20 80.52；MA50 80.40；MA200 84.50
  - 相對 MA200 -3.05%，相對 MA50 +1.90%，相對 MA20 +1.75%
  - RSI14 61.2 (未達超買，接近中性偏強)；MACD 0.560 高於 signal 0.387，柱狀體 +0.173 (偏多)
  - BB %B 0.76 (布林通道上半部)，上軌 83.22、下軌 77.82
  - 52 週區間 76.43–90.86；距 52 週高點 -9.83%，距 52 週低點 +7.20%
  - 動能：1 個月 +6.20%、3 個月 -1.00%、6 個月 -4.34%、12 個月 -8.91%
- 同類中位數 (sector median)：無可靠數據，n/a。不以估計值代替。
- 綜合：以 ETF 常用評價方式 (折溢價、費用率、流動性) 看，估值面無異常；以殖利率與利率情境評價，本次無法定量判斷。

## Key catalysts
- 財報：不適用 (ETF 無財報)；`earnings_dates` 工具回傳 ConnectionError，無資料
- 指數與成分變動：指數重新平衡 (rebalance) 日期與成分變動未在快取中提供，DATA_UNAVAILABLE
- 總體利率催化劑 (需以外部行事曆確認，本報告未取得具體日期)：
  - FOMC 利率決議與點陣圖
  - 美國 CPI、PCE 等通膨數據
  - 美國財政部公債拍賣 (尤其 20 年期與 30 年期) 與再融資公告 (quarterly refunding)
  - 美國聯邦政府債務上限與財政赤字相關新聞
- 價格位置催化點：MA200 (84.50) 為中期壓力位；52 週高點 90.86 為遠端位置；前低 76.43 為 52 週支撐

## Metrics table
單位說明：標的為 USD ETF，AUM 以 USD B 標示；股數以 M 股標示；價格以 USD 標示。本表未出現 億 / B 混用。

| Metric (單位) | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 收盤價 (USD, 2026-11-05) | 81.93 | 12M -8.53% | n/a | 位於 52 週區間偏中段，低於 MA200 |
| NAV (USD) | 81.90 | n/a | n/a | 與市價接近 |
| 折溢價 (%) | +0.03% | n/a | n/a | 正常，無折溢價風險 |
| 淨費用率 (%) | 0.15% | n/a | n/a | 低費用，成本面友善 |
| AUM (USD B) | 47.5 | n/a | n/a | 規模大，基金存續風險低 |
| 3M 平均日成交量 (M 股) | 39.5 | n/a | n/a | 流動性充足 |
| Bid / Ask (USD) | 82.92 / 82.97 | n/a | n/a | 價差約 0.06%，時點不明 |
| 趨勢殖利率 (%) | 2.63% | n/a | n/a | 與 vendor 4.76% 不一致，需核對 |
| Yahoo 殖利率欄位 (%) | 4.76% | n/a | n/a | 口徑不明，僅參考 |
| 存續期間 (duration) | DATA_UNAVAILABLE | n/a | n/a | 無法評估利率敏感度 |
| 持股集中度 (前十大) | DATA_UNAVAILABLE | n/a | n/a | 指數型 (公債)，無法量化 |
| 資金流向 (creation/redemption) | DATA_UNAVAILABLE | n/a | n/a | 無法判斷資金動向 |
| 內部人交易 | n/a | n/a | n/a | ETF 不適用 |
| Trailing P/E | n/a | n/a | n/a | 基金不適用 |
| P/B (vendor) | 0.55 | n/a | n/a | 定義不符，不採用 |
| Beta 3Y (vendor) | 2.30 | n/a | n/a | 數值偏高，需核對定義 |
| 20 日年化波動率 (%) | 10.8% | n/a | n/a | 中等偏低 |
| ATR14 (USD / % 股價) | 0.78 / 0.95% | n/a | n/a | 日內波動溫和 |
| RSI14 | 61.2 | n/a | n/a | 中性偏強，未超買 |
| MACD 柱狀體 | +0.173 | n/a | n/a | 偏多 |
| BB %B | 0.76 | n/a | n/a | 上半部 |
| 相對 MA200 (%) | -3.05% | n/a | n/a | 長線仍偏弱 |
| 相對 MA50 (%) | +1.90% | n/a | n/a | 中線偏多 |
| YTD 報酬 (%) | -2.92% | n/a | n/a | 年內表現偏弱 |
| 3Y 平均年化報酬 (%) | +1.99% | n/a | n/a | 中長期接近持平 |
| 5Y 平均年化報酬 (%) | -7.79% | n/a | n/a | 長期受利率上升拖累 |

## Red flags
- 利率風險高：追蹤剩餘年期 >20 年之公債，依指數定義屬長天期，對殖利率上行極為敏感；12 個月報酬 -8.53%，5 年平均年化 -7.79%，顯示長期持有者已承受明顯價格損失。
- 股價仍低於 MA200 約 3.05%，中期趨勢尚未翻正，52 週高點 90.86 與現價差距約 9.8%。
- 資料缺口：存續期間、持股明細、資金流向、同類中位數皆為 DATA_UNAVAILABLE，無法完整驗證利率敏感度與資金面。
- 股份數資料異常：`sharesOutstanding` 109.7M 與 AUM 47.5B USD 不符 (隱含約 580M 股)，疑為 vendor 錯誤，不可用於市值或份額計算。
- 殖利率口徑不一：trailing 2.63% 對比 vendor 4.76%，相差近一倍，需以 iShares 官網 SEC yield 或 distribution yield 核對後再用於收益判斷。
- Beta 3Y 2.30 對國債 ETF 異常偏高，若用於風險模型需先確認定義，避免錯誤放大組合風險。
- 快取時效：價格為 2026-11-05 收盤，快取更新於 2026-11-06；bid/ask 與 NAV 時點不明。本報告以 2026-11-07 為 as-of 日期，但實際最新交易資料為 2026-11-05。
- 外部連線失敗：Yahoo 即時資料在本沙箱不可用，所有數值皆為快取，無法驗證當日盤中變化。

FUNDAMENTALS REPORT COMPLETE
