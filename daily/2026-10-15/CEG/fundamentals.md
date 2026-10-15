# Fundamentals — CEG as of 2026-10-15

## Executive summary
CEG 的獲利能力在 2026 年上半年因大型收購而明顯失真: TTM 營收 31.27B、TTM 淨利 3.47B (淨利率 11.1%), 但 2026 Q2 營業利益為 -47M, 且 net debt 由 2025-12-31 的 5.35B 升至 2026-06-30 的 24.0B。以 TTM 數字計算, 自由現金流 (FCF) 僅約 309M, 不足以覆蓋股利 (TTM 約 551M)。估值方面, trailing P/E 27.3x 偏高, forward P/E 21.0x 與 EV/EBITDA 15.5x 處於中高區間, 分析師平均目標價 341.5 (較參考價 279.54 上漲約 22%), 整體屬於「獲利回升但槓桿與現金流壓力同步上升」的狀態, 估值吸引力取決於收購資產能否在後續季度產生預期的現金流。

資料說明: 本報告所有數字來自 `pipeline/tools/yf.py` 的輸出, 其中 info 與 fast_info 皆為 `"source": "cache"` (本地快取, 非即時), info 快取時間 2026-10-15T11:19:33Z, fast_info 快取時間 2026-10-15T11:16:58Z。即時 Yahoo 連線於本次執行遭 403 阻擋, 工具輸出中的 "possibly delisted" 與 "CONNECT tunnel failed" 為連線錯誤, 不代表 CEG 下市 (info 中 quoteType 為 EQUITY, 交易所 NasdaqGS)。參考價 279.54 為 2026-10-14 正常交易時段收盤價 (與 `prices/CEG.csv` 一致); info 另列 2026-10-15 盤前價 274.02 (cache 時點)。

## Revenue & profitability

**營收與成長**
- 年度營收 (yf financials, 十億美元換算為 M): 2022 24,440M → 2023 24,918M → 2024 23,568M → 2025 25,533M。
- 2022-2025 三年 CAGR 約 1.5%; 2025 YoY +8.3%。yfinance 只提供 2022-2025 年度資料, 無法計算 3-5 年 CAGR (2021 欄位為 null)。
- 季度營收: 2025 Q2 6,101M, Q3 6,570M, Q4 6,074M, 2026 Q1 11,122M, Q2 7,504M。TTM 營收 31,270M (與 info totalRevenue 一致)。2026 Q1 營收跳升, 與收購併表時點相符 (推論, 未經 yfinance 證實交易細節)。
- info revenueGrowth = 0.23 (+23%), 為 yfinance 計算之季度 YoY 口徑, 與年度 CAGR 不可直接比較。

**分部結構**
- 業務摘要 (info.longBusinessSummary) 列出五大分部: Mid-Atlantic, Midwest, New York, ERCOT, Other Power Regions; 發電容量約 31,676 MW (核能、風電、太陽能、天然氣、水力)。yfinance 未提供分部營收與利益, 分部占比為 DATA_UNAVAILABLE。

**獲利能力趨勢 (年度, 由 yf financials 計算)**

| 年度 | 毛利率 | 營業利益率 | 淨利率 |
|---|---|---|---|
| 2022 | 8.7% | -1.7% | -0.7% |
| 2023 | 13.0% | 9.6% | 6.5% |
| 2024 | 25.4% | 20.6% | 15.9% |
| 2025 | 18.4% | 16.4% | 9.1% |

- 2025 淨利 2,319M 較 2024 的 3,749M 下滑 38%; 2025 稅率 (Tax Rate For Calcs) 33.8%, 2024 為 17.1%, 稅務因素是 2025 淨利下降的重要部分。
- 2025 年 Total Unusual Items 為 -304M (2024 為 +82M), 非經常項目影響明顯。
- TTM 指標: 毛利 (yf info grossProfits) 6,913M, 毛利率 22.1%; 營業利益率 8.7% (info operatingMargins); 以季度加總計算的 TTM 營業利益 4,484M, 營業利益率約 14.3%。兩者口徑不同, 報告以季度加總為準並註明差異。
- 2026 Q2 營業利益 -47M、Normalized Income -224M, 但 GAAP 淨利 513M, 獲利品質波動大。
- EPS: 2026 Q1 GAAP diluted EPS 4.49, Q2 GAAP diluted EPS 1.42; earnings_dates 記錄之已公布 EPS (Q2 2.55 vs 預估 2.28, 超出 +11.7%) 與 GAAP EPS 數字不同, 推論為調整後口徑, 三者需分開理解。TTM diluted EPS 10.23 (info trailingEps)。

**ROE / ROIC / ROA**
- ROE: info returnOnEquity 15.1% (TTM)。以 2025 年度數字估算, 淨利 2,319M / 平均權益 13,842M = 16.8%。
- ROA: info returnOnAssets 3.9%。
- ROIC (估算, 2025 年度): 營業利益 4,198M × (1 - 33.8%) / Invested Capital 23,509M ≈ 11.8%。Invested Capital 於 2026-06-30 升至 56,677M, 新增資產尚未貢獻完整報酬, 以 2026 年資本基礎計算的 ROIC 會明顯低於 2025 年水準 (未能精確計算, 標示為估計)。

## Cashflow & balance sheet

**現金流品質**
- 年度 OCF: 2022 -2,353M, 2023 -5,301M, 2024 -2,464M, 2025 +4,237M。2025 為 2022 年以來首度正值 OCF 的年度 (由 yf 年度資料可見)。
- 年度 CapEx: 2022 -1,689M, 2023 -2,422M, 2024 -2,565M, 2025 -2,949M。2025 FCF = OCF - CapEx = 1,288M (yf Free Cash Flow 欄位一致)。2025 FCF margin = 1,288 / 25,533 = 5.0%。
- FCF / NI (2025): 1,288 / 2,319 = 0.56x, 低於 0.9 健康門檻。
- 季度 OCF: 2025 Q2 1,477M, Q3 1,848M, Q4 805M, 2026 Q1 425M, Q2 1,128M。季度 CapEx 2026 Q1 -1,275M, Q2 -1,246M; 季度 FCF 2026 Q1 -850M, Q2 -118M。
- TTM (季度加總): OCF 4,206M, CapEx -3,897M, FCF 約 +309M, FCF margin 約 1.0%, FCF / NI (TTM NI 3,465M) 約 0.09x。
- **資料矛盾**: info.freeCashflow 為 -6,625M, 與季度 CF 加總的 +309M 不一致, 原因未由 yfinance 揭示 (可能為口徑差異或資料時點差異)。本報告以季度加總為主要參考, 並將 -6,625M 列為待核對項目。

**資產負債表 (yf balance_sheet / quarterly_bs)**

| 項目 | 2025-12-31 | 2026-03-31 | 2026-06-30 |
|---|---|---|---|
| Total Assets | 57,249M | 96,911M | 98,253M |
| Total Debt | 8,992M | 22,466M | 24,700M |
| Cash & Equivalents | 3,641M | 800M | 697M |
| Net Debt | 5,351M | 21,666M | 24,003M |
| Goodwill | 420M | 11,527M | 11,527M |
| Stockholders Equity | 14,517M | 33,483M | 31,977M |
| Current Assets / Current Liabilities | 12,119 / 7,944M | 18,009 / 13,215M | 18,965 / 13,032M |

- 2026 Q1 出現 Purchase Of Business -2,537M (現金), 商譽由 420M 增至 11,527M, 股數由 312.3M (2025-12-31) 增至 362.0M (2026-03-31), 2026-06-30 為 355.3M。以上為大型收購並以股權部分支付的跡象 (推論), yfinance 未提供交易名稱、條款與收購對象, 需以 10-Q/8-K 核實。
- 淨負債 / TTM EBITDA (info EBITDA 7,952M) = 24,003 / 7,952 = 3.0x。
- Debt / Equity: info debtToEquity 76.4% (yf 口徑)。2026-06-30 以 Total Debt / Stockholders Equity 估算為 77.2%。
- Current ratio 1.46 (info 1.455, 與 2026-06-30 BS 計算一致); Quick ratio 0.47。
- 現金位置: 2026-06-30 現金 697M, 相較 2025-12-31 的 3,641M 大幅下降。
- 利息保障倍數 (TTM 營業利益 / TTM 利息費用): 4,484 / 783 = 5.7x (利息費用 2026 Q1 253M, Q2 283M, 2025 全年 511M)。利息費用隨負債增加明顯上升。

## Capital allocation & insider signal

**資本配置**
- CapEx: 2025 年 2,949M (占營收 11.5%); TTM 3,897M (占 TTM 營收 12.5%), 2026 年資本支出進入高峰。
- 買回: 2023 992M, 2024 999M, 2025 400M (僅 2025 Q2 一筆); 2026 Q1、Q2 無 yfinance 可見的買回資料 (n/a)。
- 股利: 2025 年 Cash Dividends Paid 486M; 2026 Q1 155M, Q2 154M。info dividendYield 0.58%, trailingAnnualDividendRate 1.629, payoutRatio 15.9%。
- 股利覆蓋: 以 2025 年數字, FCF / 股利 = 1,288 / 486 = 2.65x, 淨利 / 股利 = 4.8x; 以 TTM 季度加總, FCF / 股利 = 309 / 551 = 0.56x, 股利在 2026 年由 FCF 覆蓋不足, 需依賴負債或股權發行支應。
- 股權稀釋: 年初至 2026-06-30 流通股數增加約 13.8% (312.3M → 355.3M), 與收購期間股權發行一致 (推論)。
- 借款: 2026 Q1 Issuance Of Debt 7,727M, Q2 4,360M, 兩季合計約 12.1B 新增借款, 為本期資本配置的主要資金來源。

**內部人交易 (yf insider, 2026-04-15 至 2026-10-15)**
- 賣出 (Sale, 十筆): 約 163,254 股, 金額約 25.9M USD (主要為 Hudson Scott A 與 Moldovan Kristopher E 於 2026 年 9-10 月的賣出, 另有 Helm Scott Bradford 2026-06-16 賣出 25,000 股, 約 4.0M)。
- 買進 (Purchase, 三筆): Burke James A. (CEO) 合計 8,665 股, 約 1.17M; Director Crandall Roger W. 1,500 股, 約 0.42M。買進合計約 1.59M。
- 淨額: 約 -24.3M USD (淨賣出), 占市值 99.04B 的約 0.025%。占 354.3M 流通股約 0.046%。規模小, 但方向為淨賣出。
- 2026-05-15 與 2026-03-05 的股票獎勵 (Stock Award) 未計入買賣統計。
- **資料一致性警示**: 2026 年 6 月至 10 月多筆交易價格落在 135–170 美元, 與 info 的 52 週低點 228.63 與現價 279.54 不一致; 2026-08-11 Crandall 買進價 278.62 則與現價接近。insider 的價格欄位可能有錯置或時間戳問題, 上述金額與方向可信度降低, 報告僅做方向性參考, 不以其量化結論。
- 內部人持股 heldPercentInsiders 0.34%, 內部人持股比例低。

**機構持股 (yf major_holders / inst_holders)**
- 機構持股比例 82.97%, 機構數 2,456 家。
- 前十大持有人 (2026-06-30): BlackRock 6.93%, Vanguard Capital Management 5.94%, State Street 5.48%, Vanguard Portfolio Management 4.47%, ECP ControlCo 4.06% (持股變動 -34.8%), Capital International 3.57%, Invesco 3.14%, Morgan Stanley 2.55%, Geode 2.12%, FMR 1.85% (持股變動 -35.8%)。
- ECP ControlCo 與 FMR 的持股在最近一期申報中大幅減少, 原因未由 yfinance 揭示, 需以 13F/13D 核實。

**空頭部位**
- sharesShort 11.84M, 占流通股 (float) 3.74%, short ratio 4.04 日。空頭比例不高。

## Valuation

**價格基礎**
- 參考價 279.54 (2026-10-14 收盤); 2026-10-13 收盤 295.79; 當日跌幅 -5.49%。
- 盤前 (info preMarket) 274.02 (cache 時點, 較前收 -7.4%)。
- 52 週區間 228.63 – 411.69; 現價距 52 週高點 -32.1%, 距 52 週低點 +22.3%; 52 週漲跌幅 -25.4%, 同期 S&P 500 +15.7% (info SandP52WeekChange)。
- 50 日均線 275.04 (現價高於 +1.6%), 200 日均線 285.46 (現價低於 -2.1%)。
- Beta 1.129。
- 市值 99.04B (price × 354.3M 流通股, 與 info marketCap 一致); EV 123.39B (info enterpriseValue)。

**估值倍數**

| 指標 | 數值 | 計算/來源 |
|---|---|---|
| Trailing P/E | 27.3x | 279.54 / TTM EPS 10.23 |
| Forward P/E | 21.0x | 279.54 / forwardEps 13.32 |
| EV/EBITDA (TTM) | 15.5x | info enterpriseToEbitda 15.517 (EBITDA 7,952M) |
| EV/Revenue (TTM) | 3.9x | info enterpriseToRevenue 3.946 |
| P/S (TTM) | 3.2x | info priceToSalesTrailing12Months 3.17 |
| P/OCF (TTM) | 23.5x | 市值 / TTM OCF 4,206M |
| P/FCF (TTM, 季度加總) | 約 320x | 市值 / TTM FCF 309M (FCF 近乎為零, 倍數無實際參考意義) |
| P/FCF (info freeCashflow 口徑) | n/a (負值) | info freeCashflow -6,625M, 與季度加總矛盾 |
| P/B | 3.1x | info priceToBook 3.11 (bookValue 90.0) |
| PEG | 3.7x | info pegRatio 3.74 |

**分析師共識 (20 位)**
- 推薦均值 1.55 (info averageAnalystRating "1.5 - Buy"; recommendationKey "buy")。
- 目標價: 平均 341.53、中位數 345.5、最高 395.0、最低 290.0。相對現價: 平均 +22.2%、最低 +3.7%、最高 +41.3%。
- 最低目標價 290.0 高於現價, 但 2026-10-15 盤前價 274.02 已低於其下限。

**與同業中位數比較 (估計, 非工具資料)**
- 工具未提供同業 (美國 Utilities - Independent Power Producers) 中位數。以下為本報告基於產業常識的估計區間, 非精確數據, 僅供參考:
- P/E 約 18-25x; EV/EBITDA 約 11-14x; P/S 約 1.5-3x; ROE 約 8-12%; 淨負債 / EBITDA 約 3-5x。
- 相對估計中位數, CEG 的 trailing P/E 與 EV/EBITDA 偏高, forward P/E 接近區間上緣, P/S 接近上緣; 估值溢價主要反映核能資產與數據中心電力需求的成長預期 (此為產業敘述推論, 未由 yfinance 資料證實)。

## Key catalysts
- **下一次財報**: 2026-11-09 (yf earnings_dates, 狀態為正式日期而非估計; 該時點對應 Q3 2026)。Q3 EPS 預估 3.75 (earnings_dates EPS Estimate)。
- **最近財報結果**: 2026-08-06 公布 Q2 2026, 調整後 EPS 2.55, 高於預估 2.28 (+11.7%); GAAP 淨利 513M, 營業利益 -47M。
- **前次財報**: 2026-05-11 EPS 2.74 vs 預估 2.60 (+5.3%); 2026-02-24 EPS 2.30 vs 預估 2.25 (+2.4%)。連續三季調整後 EPS 小幅超預期。
- **收購整合**: 2026 Q1 起商譽與股數大幅變動, 整合進度與收購資產的併表獲利將是 Q3/Q4 2026 報表最需追蹤的變數。
- **債務與利率**: 短期債務 (Current Debt) 由 1,742M 增至 5,589M (2026-06-30); 再融資條件與利息費用變化會直接影響 EPS。
- **股利**: info dividendDate 對應約 2026-09-04 (由 Unix timestamp 換算), 股利金額 0.427 每股 (lastDividendValue), 為目前股利事件。
- **估值與監管面**: 最新 52 週漲跌幅與 insider 賣出集中於 2026 Q3, 相關市場面與政策 (如 FERC、DOE 相關電力市場規則) 不在本次 yfinance 資料範圍內, 標示為 DATA_UNAVAILABLE。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 (TTM) | 31,270M | n/a (TTM 前期不完整) | n/a | 規模明顯擴大, 受收購驅動 |
| 營收 YoY (年度 2025) | 25,533M | +8.3% | n/a | 溫和成長 |
| 營收 3Y CAGR (2022-2025) | 1.5% | n/a | n/a | 長期偏低 |
| 毛利率 (2025 年度) | 18.4% | 2024 為 25.4%, -7.0pt | n/a | 惡化 |
| 營業利益率 (2025 年度) | 16.4% | 2024 為 20.6%, -4.1pt | n/a | 惡化 |
| 淨利率 (TTM) | 11.1% | 2025 年度 9.1% | n/a | 回升中 |
| 營業利益 (2026 Q2) | -47M | 2025 Q2 為 +502M | n/a | 警示 |
| ROE (TTM, info) | 15.1% | 2025 估算 16.8% | 約 8-12% (估計) | 高於估計中位數 |
| ROIC (2025 估算) | 11.8% | n/a | 約 6-8% (估計) | 尚可, 2026 資本基礎後將下降 |
| FCF margin (TTM) | 約 1.0% | 2025 年度 5.0% | n/a | 偏弱 |
| FCF / NI (2025) | 0.56x | n/a | 健康門檻 >0.9 | 未達標 |
| FCF / NI (TTM) | 約 0.09x | n/a | 健康門檻 >0.9 | 未達標 |
| Net Debt (2026-06-30) | 24,003M | 2025-12-31 為 5,351M, +349% (半年) | n/a | 顯著惡化 |
| Net Debt / EBITDA (TTM) | 3.0x | n/a | 約 3-5x (估計) | 在估計區間內 |
| Current Ratio | 1.46 | 2025-12-31 為 1.53 | 約 1.0-1.3 (估計) | 流動性尚可 |
| Debt / Equity (info) | 76.4% | n/a | 約 100-150% (估計, 公用事業通常較高) | 相對較低 |
| 利息保障倍數 (TTM) | 5.7x | n/a | n/a | 尚可, 利息費用上升中 |
| 現金 (2026-06-30) | 697M | 2025-12-31 為 3,641M | n/a | 流動性緩衝降低 |
| CapEx (TTM) | 3,897M | 2025 年度 2,949M | n/a | 投資高峰 |
| 股利殖利率 | 0.58% | 5 年平均 0.56% | 約 3-4% (估計) | 偏低 |
| 股利覆蓋 (FCF / 股利, TTM) | 0.56x | 2025 年度 2.65x | n/a | 偏弱 |
| 流通股數 | 355.3M | 2025-12-31 為 312.3M, +13.8% | n/a | 股權稀釋 |
| 內部人淨買賣 (6 個月) | 淨賣出約 24.3M | n/a | n/a | 偏負向 (資料一致性待核) |
| 機構持股比例 | 82.97% | n/a | n/a | 高 |
| Short % of float | 3.74% | 空頭股數較上月 +2.3% (11.57M → 11.84M) | n/a | 低 |
| Trailing P/E | 27.3x | n/a | 約 18-25x (估計) | 偏高 |
| Forward P/E | 21.0x | n/a | 約 18-25x (估計) | 中性偏高 |
| EV/EBITDA (TTM) | 15.5x | n/a | 約 11-14x (估計) | 偏高 |
| P/S (TTM) | 3.2x | n/a | 約 1.5-3x (估計) | 偏高 |
| P/FCF (TTM) | 約 320x | n/a | n/a | 無參考意義 (FCF 接近零) |
| 分析師平均目標價 | 341.5 (+22.2%) | n/a | n/a | 上行空間 (分析師口徑) |
| 52 週漲跌幅 | -25.4% | S&P 500 +15.7% | n/a | 相對弱勢 |
| Beta | 1.13 | n/a | n/a | 略高於市場 |

## Red flags
- **FCF 口徑矛盾**: info.freeCashflow -6,625M 與季度 CF 加總 +309M 不一致; TTM FCF 接近零, 股利覆蓋不足 (0.56x)。
- **槓桿快速上升**: net debt 於 6 個月內由 5.35B 增至 24.0B; 2026 Q1–Q2 新增借款約 12.1B, 現金降至 697M。
- **收購與稀釋**: 商譽增加約 11.1B、流通股數增加約 13.8%; 收購資產的獲利貢獻與整合風險未由 yfinance 揭示。
- **Q2 2026 營業虧損**: 營業利益 -47M、Normalized Income -224M, GAAP 淨利 513M 與營業利益背離, 獲利品質需以 10-Q 核實。
- **利息費用上升**: 季度利息費用由 2025 Q2 的 118M 增至 2026 Q2 的 283M, 約 2.4 倍。
- **獲利與盈餘品質波動**: 2025 年淨利 -38% YoY; 2026 Q1 GAAP EPS 4.49 與 Q2 GAAP EPS 1.42 差距大; 調整後與 GAAP 口徑差異需分開解讀。
- **內部人淨賣出**: 6 個月淨賣出約 24.3M (約占市值 0.025%), 規模小但方向為賣出; 價格欄位存在與 52 週區間不一致的情況, 量化結論可信度降低。
- **大型機構減持**: ECP ControlCo (-34.8%) 與 FMR (-35.8%) 持股在最近申報期大幅減少, 原因未揭示。
- **估值偏高**: trailing P/E 27.3x、EV/EBITDA 15.5x、PEG 3.7x, 高於估計同業區間, 估值依賴 forward 獲利回升。
- **報價品質**: info 的 bid 290.0 高於 ask 283.08 (交叉報價), 且 regularMarketPrice 與盤前價格不同步; 本報告以收盤價 279.54 為準, 盤前價 274.02 僅作參考。
- **資料缺口 (DATA_UNAVAILABLE)**: 分部營收與利益、收購交易細節、2026 年股份回購、3-5 年 CAGR (2021 缺)、同業中位數 (本報告為估計)、監管與政策面影響。

FUNDAMENTALS REPORT COMPLETE
