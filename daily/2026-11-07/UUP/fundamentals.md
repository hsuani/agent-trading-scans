# Fundamentals — UUP (Invesco DB US Dollar Index Bullish Fund) as of 2026-11-07

資料說明：本次 Yahoo 即時端點全數失敗（fast_info / earnings_dates / financials / balance_sheet / cashflow / insider / holders 皆為 ConnectionError 或空陣列），以下數據來自 repo 快取 `prices/yf/UUP.json`（refreshed 2026-11-06 14:11 UTC）與 `prices/UUP.csv`（最後一筆為 2026-11-05 收盤）。最新已確認收盤為 2026-11-05，2026-11-06 收盤缺漏。無資料者標示 DATA_UNAVAILABLE 或 n/a。

## Executive summary
UUP 為 ICE 美元指數（DXY）的做多 ETF，結構上是以 ICE US Dollar Index 期貨多頭追蹤「美元相對六種主要貨幣」的價值，無公司營收、獲利或現金流可評估。截至 2026-11-05 收盤價 USD 28.92，與快取 NAV 28.92 持平（折溢價 0.00%），規模約 USD 481.4M，費用率 0.75%，價格位於 MA20 / MA50 / MA200 之上方或附近，RSI14 為 51.4（中性），MACD 柱狀體為負，短線動能偏中性。估值不適用；從 ETF 結構與技術面看，無折溢價風險，但費用率偏高、規模偏小，且缺少本次資金流與持倉資料，無法完整判斷資金面。

## Revenue & profitability（不適用，改為標的與規模概況）
- 標的：Invesco DB US Dollar Index Bullish Fund，NYSEArca 代碼 UUP，ETF 類型，Invesco 發行，基金成立日 2007-02-20（fundInceptionDate 換算）。
- 追蹤指數與結構：`longBusinessSummary` 明載「投資於期貨合約以追蹤指數，指數反映 DX Contracts 多頭部位的市值變化」。即持有 ICE US Dollar Index（DX）期貨多頭，非現貨外匯。
- 貨幣籃組成（非本次工具輸出，依 ICE DXY 公開規格，未經本次工具驗證）：歐元約 57.6%、日圓約 13.6%、英鎊約 11.9%、加幣約 9.1%、瑞典克朗約 4.2%、瑞士法郎約 3.6%。DXY 上升代表美元對此籃走強，UUP 上漲。
- 規模：totalAssets / netAssets = 481,364,192 USD，即 USD 481.4M（約 0.48B）。
- 流動性：20 日平均成交量約 1.56M 股（CSV 計算），10 日平均 1,594,350 股（info.averageVolume10days），2026-11-05 成交量 1,945,600 股。
- 報酬（以 CSV 收盤價計算）：1 個月 -0.24%、3 個月 +2.95%、YTD +6.99%、1 年 +2.08%。Yahoo 欄位 ytdReturn 為 +7.13%，與 CSV 計算差異屬於不同基準（NAV 與收盤價），以 CSV 為準。
- 52 週範圍：Yahoo 日內高/低 USD 29.25 / 26.40；CSV 收盤高/低 29.13（2026-10-12）/ 26.47（2026-01-27）。
- 長期報酬：自 2024-11-06 收盤 29.56 至 2026-11-05 收盤 28.92，約 -2.2%（兩年，未年化）。3 年報酬 Yahoo 欄位 threeYearAverageReturn 為 3.92%（年化平均，定義需確認）；5 年 fiveYearAverageReturn 為 5.79%。

## Cashflow & balance sheet（不適用）
- financials / balance_sheet / cashflow 皆為空陣列（DATA_UNAVAILABLE）。ETF 不以營運現金流衡量。
- 功能性替代指標：基金資產主要為期貨保證金與 T-bill 類抵押品，實際利息收入與展期（roll）損益需看 Invesco 每日持倉與年報，本次無法取得。
- 規模對應：totalAssets USD 481.4M，淨資產與價格一致（NAV 28.92）。

## Capital allocation & insider signal
- 分配：trailingAnnualDividendRate = 0.0，trailingAnnualDividendYield = 0.0；但 dividendYield 欄位為 3.2（即 3.2%）、yield 為 0.032。兩者不一致，無法確認近 12 個月是否有分配，需以 Invesco 公告為準。一般此類 DB 基金於年底前分配利息收入，屬推定，未經本次資料確認。
- 內部人交易：ETF 無內部人（insider 為空陣列，DATA_UNAVAILABLE），不適用。
- 機構持股：inst_holders / major_holders 為空陣列，DATA_UNAVAILABLE。
- 資金流（申購 / 贖回、淨流入）：本次工具無此欄位，DATA_UNAVAILABLE。可用的代理指標僅為成交量與價格走勢，無法判斷實際淨流入方向。

## Valuation
- P/E、EV/EBITDA、P/FCF、P/S：不適用（ETF 無盈餘）。
- 折溢價：price 28.92（2026-11-05 收盤）vs navPrice 28.92，折溢價 0.00%。注意 NAV 的日期與來源未在快取明載，僅能視為與收盤價同期。
- 盤前指標：preMarketPrice 29.1368（2026-11-06 盤前約 14:06 UTC），較前收 +0.73%。此為盤前參考，非 2026-11-06 收盤，不納入估值。
- bid / ask 皆為 29.08，且 bid=ask 與收盤價差距 +0.16，判斷為陳舊或非成交報價，不可採信。
- 技術面（ta snapshot，as_of 2026-11-05）：
  - MA20 28.9955（價格距 -0.26%）、MA50 28.6646（距 +0.89%）、MA200 27.9576（距 +3.44%）。
  - RSI14 51.35（中性）；MACD 0.0668、信號線 0.1011、柱狀體 -0.0343（動能偏弱）。
  - BB %B 0.245（位於下帶附近）；ATR14 0.111，約 0.38% 價格。
  - 距 52 週高點 -1.13%，距 52 週低點 +9.55%。
  - 20 日年化波動 4.24%（ta）；CSV 計算 1 年年化波動約 6.63%。
- 風險指標：info.beta3Year = -7.93，數值明顯異常（DXY 相關 ETF 理論 beta 不應為極端負值），不採用。
- 費用率：netExpenseRatio 0.75%。以一般美元 / 外匯類 ETF 估計 0.2% 至 0.75%（估計），屬偏高端；DB 系列需承擔期貨展期成本。

## Key catalysts
- 財報：不適用（無公司財報）。
- 分配公告：年底前可能有利息收入分配（未經確認，需看 Invesco 公告）。
- 宏觀事件（未由工具驗證，屬一般性日曆）：美國 CPI、就業與 FOMC 利率決議會影響美元利率差，進而影響 DXY。具體日期需另行確認。
- 利率差與展期：期貨 contango / backwardation 會影響展期損益；利差收斂（美債利率相對歐元 / 日圓下行）通常不利於多頭，本次無實際曲線資料可驗證。
- 技術位：MA20 約 28.99–29.00 為近端阻力；52 週高 29.25 為上方關鍵位；MA50 28.66 為下方支撐。
- 資料缺口：2026-11-06 收盤未入快取，無法確認 11-06 走勢。

## Metrics table
單位：價格為 USD；AUM 為 USD M；成交量為股數；報酬與比率為 %。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 收盤價（USD） | 28.92（2026-11-05） | 1 年 +2.08%（CSV 收盤） | n/a | 中性偏多，位於 MA50/MA200 之上 |
| NAV（USD） | 28.92 | n/a | n/a | 與價格一致 |
| 折溢價（%） | 0.00 | n/a | ±0.1% 以內（估計） | 無折溢價風險 |
| AUM（USD M） | 481.4 | n/a | 數百 M 至數 B（估計） | 規模偏小，流動性尚可 |
| 費用率（%） | 0.75 | n/a | 0.2–0.75（估計） | 偏高 |
| 20 日平均成交量（股） | 約 1,560,895 | n/a | n/a | 流動性足夠 |
| 日成交量（股，2026-11-05） | 1,945,600 | 較 20 日均量 +25% | n/a | 當日量能放大 |
| RSI14 | 51.35 | n/a | 50（中性） | 中性 |
| MACD 柱狀體 | -0.0343 | n/a | 0 | 動能偏弱 |
| BB %B | 0.245 | n/a | 0.5（中性） | 偏下帶 |
| ATR14（USD / %） | 0.111 / 0.38% | n/a | n/a | 波動低 |
| 年化波動（1 年，CSV） | 6.63% | n/a | 6–10%（估計，外匯 ETF） | 低於一般外匯類 |
| 距 52 週高點（%） | -1.13 | n/a | n/a | 接近高點 |
| 距 52 週低點（%） | +9.55 | n/a | n/a | 距低點有緩衝 |
| YTD 報酬（CSV，%） | +6.99 | Yahoo ytdReturn +7.13 | n/a | 年內強勢 |
| 1 個月報酬（CSV，%） | -0.24 | n/a | n/a | 持平 |
| 3 個月報酬（CSV，%） | +2.95 | n/a | n/a | 偏多 |
| 3 年平均報酬（%） | 3.92 | n/a | n/a | 定義需確認 |
| beta3Year | -7.93 | n/a | 不適用 | 異常，不採用 |
| 殖利率（%） | 3.2（dividendYield） / 0.0（trailingAnnualDividendRate） | n/a | n/a | 欄位不一致，需確認 |
| 資金流 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | 無法判斷 |
| 持倉 / 機構持股 | DATA_UNAVAILABLE | n/a | n/a | 無法判斷 |
| 內部人交易 | 不適用（ETF） | n/a | n/a | 不適用 |
| P/E、EV/EBITDA、P/FCF、P/S | 不適用（ETF） | n/a | n/a | 不適用 |

## Red flags
- 即時 Yahoo 端點全部失敗，本次所有數據依賴快取，部分欄位可能陳舊。
- 2026-11-06 收盤未入快取，最新確認價為 2026-11-05 收盤；盤前 29.1368 不作為估值依據。
- bid / ask 皆為 29.08，且 bid=ask，屬不可靠報價。
- beta3Year = -7.93 數值異常，不可用於風險評估。
- dividendYield（3.2%）與 trailingAnnualDividendRate（0.0）互相矛盾，分配狀況未確認。
- AUM 僅約 USD 481.4M，規模偏小；若資金大幅流出，可能影響流動性與追蹤精度，需看資金流數據（本次缺失）。
- 費用率 0.75% 偏高，長期持有成本拖累明顯。
- 期貨展期成本與利差變化會造成 UUP 與現貨 DXY 的偏離，本次無法量化追蹤誤差。
- 貨幣籃權重（EUR 約 57.6%）為公開規格，未經本次工具驗證；UUP 的表現高度集中於歐元對美元走勢。

FUNDAMENTALS REPORT COMPLETE
