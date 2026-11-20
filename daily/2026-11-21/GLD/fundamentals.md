# Fundamentals — GLD as of 2026-11-21

註：GLD 為 SPDR Gold Shares 實物黃金信託 ETF（NYSE Arca），非公司。傳統營收、獲利率、資產負債表、內部人交易、本益比等指標不適用。以下以基金結構（實物金條持有、費用率、基金規模、價格與淨值關係）取代。資料截止為 2026-11-20 盤中快照（快取時間 2026-11-20 約 10:18–10:22 ET），尚無 2026-11-21 收盤資料。

## Executive summary

GLD 本質上是追蹤金價的被動式實物金信託，費用率 0.40%，基金規模約 131.0 B USD，財務健康度的判斷應轉為「金價走勢與基金資金流」而非企業財報。截至 2026-11-20 盤中，GLD 報 325.36 USD（TA 快照），較 52 週高點 509.7 USD（2026-01-29）回落約 36%，RSI14 為 24.5 進入超賣區，價格位於 MA20/50/200 之下，MACD 仍為負值；價格與淨值（NAV 339.88）之間存在約 -4.3% 至 -4.6% 的折價，但該 NAV 數值疑似陳舊，需謹慎解讀。基金創設與贖回（資金流）資料本次無法取得，無法判斷資金面是流入或流出。

## Revenue & profitability（信託結構與費用）

- 標的與結構：依 info.longBusinessSummary，信託持有金條（gold bars），目標為讓股價反映金價表現，扣除信託費用後的報酬。發行人為 State Street Investment Management（fundFamily）。
- 費用率：netExpenseRatio = 0.4（%），即每年約 0.40% 的持有成本，是 ETF 報酬的唯一長期拖累項目，且為固定成本。
- 收益：yield = 0.0，trailingAnnualDividendRate = 0.0，ETF 不配息，無股息收入。
- 營收、毛利、營業利益、淨利：不適用。yfinance financials 回傳空陣列。epsTrailingTwelveMonths = -9.394 為信託會計口徑下的數值，不具估值意義，不採用。
- 報酬表現（yfinance info 與 CSV 快取比對）：
  - ytdReturn（info）：-9.46%
  - fiftyTwoWeekChangePercent（info）：-10.44%
  - trailingThreeMonthReturns（info）：-2.91%
  - 以 prices/GLD.csv 自行計算：2025-12-31 收盤 396.31 至 2026-11-20 快照 325.36，YTD 約 -17.9%；2025-11-20 收盤 374.85 至 325.36，近一年約 -13.2%。
  - 注意：info 的 ytdReturn（-9.46%）與 CSV 自算 YTD（-17.9%）差距大，兩者基準不同（可能為 NAV 口徑或調整後價格），本報告以 CSV 自算值與 info 並列揭示，不擅自取捨。

## Cashflow & balance sheet（基金資產與淨值）

- 基金規模（totalAssets / netAssets）：131,009,642,496 USD ≈ 131.0 B USD。
- 流通股數（sharesOutstanding）：260,300,000 股。
- 數字一致性檢查：netAssets 131.0 B ÷ 流通股數 260.3 M ≈ 503.2 USD/股，與 navPrice 339.88 USD 明顯不符；且 bookValue = 170.017 也與兩者皆不符。推測 sharesOutstanding 或 netAssets 其中之一為陳舊值或不同時點資料，本報告不採用由此推導的任何每股淨值，僅將 navPrice 作為參考並標註為待核實。
- 資產組成：信託持有實物黃金（physical gold bullion）。持有盎司數、純度、保管機構（custodian）等明細 DATA_UNAVAILABLE（工具未回傳）。
- 負債、流動比率、負債權益比、淨負債、現金部位：不適用於信託結構，均不計算。
- 持有集中度：major_holders 與 inst_holders 皆回傳空陣列，DATA_UNAVAILABLE。

## Capital allocation & insider signal（資金流與持有人）

- 創設與贖回（creations / redemptions）：DATA_UNAVAILABLE。工具與快取均未提供每日或每週申購、贖回股數或金額，無法判斷資金面淨流入或淨流出。
- 基金規模趨勢：僅有單一時點 totalAssets，無歷史序列，無法計算 AUM 趨勢。若以價格代理，金價下跌約 13% 至 18% 區間內，基金規模變動大部分來自價格效應，非確定的資金流。
- 內部人交易（insider）：回傳空陣列，ETF 不適用內部人申報，判定為不適用。
- 成交量：
  - info.averageVolume（3 個月）：9,611,646 股；averageVolume10days：9,695,560 股。
  - 近 20 個交易日（CSV）平均成交量約 9.39 M 股。
  - 2026-11-20 快照成交量 5,717,191 股（盤中，非全日量），不宜與全日量直接比較。
  - 近期（2026-11-18 至 2026-11-20）成交量放大，與價格急跌同步，但資金流方向未知。

## Valuation（淨值與折溢價）

- 本益比（trailing / forward P/E）：不適用（EPS 為負，且信託無盈餘概念）。
- P/B（priceToBook）：1.91，但 bookValue 數值本身有內部矛盾，本報告不採用。
- EV/EBITDA、P/FCF、P/S：不適用。
- 折溢價（以 info 數值計算）：
  - 價格 324.385（info.regularMarketPrice，前一交易時段或同日盤中）對 navPrice 339.88 → 約 -4.56%。
  - 價格 325.36（TA 快照）對 navPrice 339.88 → 約 -4.27%。
  - 價格 327.36（fast_info，cnyes 來源）對 navPrice 339.88 → 約 -3.68%。
  - 一般實物黃金 ETF 的折溢價通常在小數點後一位至兩位內，若屬實則 -4% 以上的折價屬異常，更可能是 navPrice 為陳舊值。本報告不以此折價作為交易訊號。
- 同業比較：sector median 不適用於信託個股估值；可比對象為同類實物金 ETF（如 IAU 等），本次工具未回傳其資料，DATA_UNAVAILABLE。
- 技術面估值參考（TA 快照，2026-11-20）：
  - MA20 360.55、MA50 374.95、MA200 405.84；價格分別低於 9.76%、13.23%、19.83%。
  - 距 52 週高點 509.7 為 -36.17%，距 52 週低點 325.34 僅 +0.01%（貼近年內低點）。
  - 布林通道 %B = -0.118（跌破下軌 332.06）。
  - ATR14 = 7.11 USD（約 2.2% 日波動），20 日年化歷史波動 30.3%。
  - 動量：1M -11.8%、3M -23.7%、6M -21.4%、12M -13.2%。

## Key catalysts

- 下一次財報：不適用（信託無季度財報；yfinance earnings_dates 回傳空陣列）。
- 金價驅動因子：GLD 報酬幾乎完全取決於現貨金價，本次工具未提供宏觀資料（利率、美元指數、央行購金等），無法在本報告內量化。
- 基金結構性事件（費率調整、發行人變更、保管機構變更）：本次資料未見公告，DATA_UNAVAILABLE。
- 資料時效：
  - 價格來源為快取（source: cache），info 快取於 2026-11-20T15:22 UTC，fast_info 快取於 2026-11-20T15:18 UTC，TA 快照 as_of 2026-11-20。
  - 本報告 as-of 2026-11-21，但最新可用價格為 2026-11-20 盤中，尚無收盤資料，屬於資料落後。
  - 無 2026-11-21 之後的資料，未發現未來資料污染。

## Metrics table

金額單位：USD（基金規模以 B USD 表示）；成交量以 M 股表示。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 價格（TA 快照，USD） | 325.36 | 近一年 -13.2%（CSV 自算） | n/a | 處於年內低點附近，弱勢 |
| 價格（info regularMarketPrice，USD） | 324.385 | n/a | n/a | 與 TA 快照時點不同，僅供參考 |
| 52 週高 / 低（USD） | 509.7 / 325.34 | 高點 2026-01-29 | n/a | 距高點 -36.2%，貼近低點 |
| 基金規模（totalAssets，B USD） | 131.0 | DATA_UNAVAILABLE（無歷史序列） | n/a | 大型流動性 ETF，規模充足 |
| 費用率（netExpenseRatio，%） | 0.40 | n/a | 實物金 ETF 同類約 0.1%–0.4%（估計） | 費率處於同類偏高區間 |
| 淨值 navPrice（USD） | 339.88 | n/a | n/a | 數值疑似陳舊，待核實 |
| 折溢價（以 325.36 對 NAV） | 約 -4.3% | n/a | 通常接近 0%（估計） | 異常，疑似 NAV 陳舊 |
| 流通股數（M 股） | 260.3 | DATA_UNAVAILABLE | n/a | 與 netAssets 不一致，待核實 |
| 創設 / 贖回淨額 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | 無法判斷資金流向 |
| 持有實物金（盎司） | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | 無法核對 |
| 平均成交量 3M（M 股） | 9.61 | n/a | n/a | 流動性極佳 |
| 近 20 日平均成交量（M 股，CSV） | 9.39 | n/a | n/a | 與 3M 均量接近，無異常縮量 |
| 本益比 P/E | n/a | n/a | n/a | 不適用（信託） |
| 股息殖利率 | 0.0% | n/a | n/a | 不適用（不配息） |
| RSI14 | 24.5 | n/a | 30 以下為超賣 | 超賣，短線偏弱 |
| MACD 柱狀體 | -3.45 | n/a | n/a | 空方動能 |
| 距 MA200 | -19.8% | n/a | n/a | 長期趨勢偏空 |
| 20 日年化歷史波動率 | 30.3% | n/a | n/a | 波動偏高 |
| 內部人交易 | n/a | n/a | n/a | 不適用（ETF） |

## Red flags

- 價格與金價相關的單一風險：GLD 無營運槓桿或資產負債表緩衝，報酬完全跟隨現貨金價，且 52 週內已回落約 36%。
- 費用率 0.40% 為持有成本拖累，在長期持有、金價橫盤時尤其明顯。
- NAV 與流通股數、基金規模三者數值互相矛盾（131.0 B ÷ 260.3 M ≈ 503 USD，非 NAV 339.88 USD），以及 bookValue 與 P/B 數值不可信，資料品質有疑慮，本報告所有依 NAV 的推論需以更新資料核實。
- info 的 ytdReturn（-9.46%）與 CSV 自算 YTD（-17.9%）不一致，報酬口徑需確認。
- 創設與贖回資金流資料缺失，無法判斷是否有大規模贖回壓力，此為本次研究的主要資料缺口。
- 價格資料為盤中快取（2026-11-20 約 10:18 ET），非收盤價，且 fast_info（327.36）、info（324.385）、TA 快照（325.36）三者價格不一致，需以收盤價校正。
- 持有人（major_holders、inst_holders）與內部人資料空白，無法評估大戶持有變動。

FUNDAMENTALS REPORT COMPLETE
