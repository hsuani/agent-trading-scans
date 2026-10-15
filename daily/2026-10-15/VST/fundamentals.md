# Fundamentals — VST as of 2026-10-15

## Executive summary
VST 在 2026 年上半年出現結構性財務變化: 2026-06-30 Total Debt 達 247.0 億美元 (2025-12-31 為 89.9 億)、Stockholders Equity 達 319.8 億美元 (2025-12-31 為 145.2 億)、普通股由約 3.12 億股增至 3.55 億股，工具資料顯示這是大型資本化交易所致，但交易名稱與條款無法由工具確認 (DATA_UNAVAILABLE)。2025 全年獲利仍為正 (淨利率 9.1%、ROE 約 16.8%)，但 2026-Q2 Operating Income 轉為 -0.47 億美元，TTM FCF 僅約 3.1 億美元，TTM 股利 (約 5.5 億) 只有約 0.56 倍被 FCF 覆蓋，財務體質目前處於槓桿與稀釋升高的過渡期。估值面以 forward P/E 14.6x 與 PEG 0.45 看，相對 trailing P/E 27.4x 有明顯落差，代表市場接受獲利回升的前提，但 Q2 EPS surprise 為 -54.2%，2026 年整合與獲利兌現的不確定性仍高。

資料時效: 本報告所有數字取自本地快取 (source: cache, cached_at 2026-10-15T11:21:43Z)，最新價格為 2026-10-14 收盤 (regularMarketTime 2026-10-14 20:00 UTC)，未見 2026-10-15 之後的資料。最近一季財報為 2026-06-30 季度。

## Revenue & profitability

### 營收趨勢 (年度, 百萬美元)
| 年度 | Total Revenue | YoY | Gross Profit | Operating Income | Net Income |
|---|---|---|---|---|---|
| 2022 | 24,440 | n/a | 2,137 | -408 | -160 |
| 2023 | 24,918 | +2.0% | 3,232 | 2,386 | 1,623 |
| 2024 | 23,568 | -5.4% | 5,990 | 4,848 | 3,749 |
| 2025 | 25,533 | +8.3% | 4,693 | 4,198 | 2,319 |

- 3 年 CAGR (2022→2025): 約 +1.5%。2021 年資料為 null，無法計算 5 年 CAGR。
- 2026-Q2 Total Revenue 7,504 百萬，YoY +23.0% (對比 2025-Q2 的 6,101 百萬)。2026-Q1 為 11,122 百萬，但 2025-Q1 為 null，無法計算 YoY。
- 2026-Q1 營收 (11,122) 與 Gross Profit (2,990)、Operating Income (2,266) 明顯高於其他季度，工具資料未說明原因，需以 SEC 10-Q 核對 (DATA_UNAVAILABLE)。
- Segment mix: 工具未提供分部營收 (DATA_UNAVAILABLE)。公司業務描述列出五個分部: Retail、Texas、East、West、Asset Closure；發電容量約 44,000 MW，服務約 500 萬客戶。
- 資料衝突: info 的 totalRevenue 為 19,212 百萬，與四季加總 TTM 31,270 百萬不一致，本報告以損益表原始數字為準。

### 獲利率趨勢
| 年度 | Gross Margin | Operating Margin | Net Margin |
|---|---|---|---|
| 2022 | 8.7% | -1.7% | -0.7% |
| 2023 | 13.0% | 9.6% | 6.5% |
| 2024 | 25.4% | 20.6% | 15.9% |
| 2025 | 18.4% | 16.4% | 9.1% |

- 2026-Q2 Operating Income -47 百萬 (margin -0.6%)；Normalized Income -224 百萬。
- ROE (NI / 平均 Stockholders Equity): 2025 約 16.8%，2024 約 31.1%。info 的 returnOnEquity 為 42.96%，與報表計算不一致，本報告不採用。
- ROIC (近似, EBIT x (1 - 有效稅率) / 平均 Invested Capital): 2025 約 15.0%，2024 約 19.5%。
- 2025 年 Net Income 由 2024 的 3,749 降至 2,319 百萬 (-38%)，主要因 Gain On Sale Of Security 由正轉負 (2025 為 -304 百萬) 等非營業項目影響。

## Cashflow & balance sheet

### 現金流 (年度, 百萬美元)
| 年度 | Operating CF | Capex | FCF | FCF Margin | FCF / NI |
|---|---|---|---|---|---|
| 2022 | -2,353 | -1,689 | -4,042 | n/a | n/a |
| 2023 | -5,301 | -2,422 | -7,723 | n/a | n/a |
| 2024 | -2,464 | -2,565 | -5,029 | n/a | n/a |
| 2025 | 4,237 | -2,949 | 1,288 | 5.0% | 0.56x |

- 2022–2024 FCF 皆為負，2025 首次轉正。FCF/NI 2025 為 0.56x，低於 0.9 的健康門檻；OCF/NI 為 1.83x，顯示差距主要來自資本支出 (capex 佔 OCF 約 70%)。
- 2026 上半年季度: Q1 OCF 425、Capex -1,275、FCF -850；Q2 OCF 1,128、Capex -1,246、FCF -118。H1 2026 FCF 合計 -968 百萬。
- TTM (2025-Q3 至 2026-Q2) 以四季加總: OCF 4,206、Capex -3,897、FCF 約 +309 百萬。info 的 freeCashflow 為 37.1 百萬，同方向但數字不同。

### 資產負債表 (百萬美元)
| 指標 | 2024-12 | 2025-12 | 2026-03 | 2026-06 |
|---|---|---|---|---|
| Total Assets | 52,926 | 57,249 | 96,911 | 98,253 |
| Total Debt | 8,412 | 8,992 | 22,466 | 24,700 |
| Long Term Debt | 7,384 | 7,250 | 16,994 | 19,111 |
| Net Debt | 5,390 | 5,351 | 21,666 | 24,003 |
| Cash & Equivalents | n/a | 3,641 | 800 | 697 |
| Stockholders Equity | 13,166 | 14,517 | 33,483 | 31,977 |
| Current Assets | 10,776 | 12,119 | 18,009 | 18,965 |
| Current Liabilities | 6,846 | 7,944 | 13,215 | 13,032 |

- Current ratio: 2025-12 為 1.53x，2026-06 為 1.46x (由報表計算)。info 的 currentRatio 0.973 與報表不一致，本報告不採用。
- Debt / Equity (Total Debt / Stockholders Equity): 2025-12 為 0.62x，2026-06 為 0.77x。info 的 debtToEquity 為 373.28 (%)，與報表不一致，本報告不採用。
- Net Debt / EBITDA: 2025 年度為 0.85x (5,351 / Normalized EBITDA 6,263)；以 2026-06 TTM Normalized EBITDA 6,932 計算約 3.46x。TTM EBITDA 含 2026-Q1 之一次性高值，數字僅供參考。
- Interest coverage: 2025 年 EBIT 4,022 / Interest Expense 511 = 約 7.9x。2026-Q2 Interest Expense 283 百萬，較 2025-Q2 的 118 百萬增加約 140%；TTM Interest Expense 約 783 百萬。
- Goodwill 與無形資產僅 420 百萬，商譽風險低。
- 現金水位: 2026-06 現金 697 百萬，較 2025-12 的 3,641 百萬大幅下降，流動性緩衝變薄。info 的 quickRatio 為 0.258。

## Capital allocation & insider signal

### 資本配置
- Capex: 2022 為 1,689、2023 為 2,422、2024 為 2,565、2025 為 2,949 百萬，逐年增加，2025 佔營收約 11.5%。
- 股利: Cash Dividends Paid 2022 為 185、2023 為 366、2024 為 444、2025 為 486 百萬。2025 年 FCF 股利覆蓋倍數為 2.65x，NI 覆蓋 4.8x。但 TTM 股利約 551 百萬 (2025-Q3 至 2026-Q2 季度加總) 相對 TTM FCF 約 309 百萬，覆蓋僅約 0.56x。
- 股利殖利率: info dividendYield 0.57%，trailingAnnualDividendRate 0.91 美元，最近一季股利 0.23 美元；5 年平均殖利率 0.98%。
- 買回: 2023 為 992、2024 為 999、2025 為 400 百萬；2026 上半年季度資料為 null (視為無法確認，非 0)。
- 負債與股本: 2026 上半年季度 Debt Issuance 合計約 12,087 百萬、Debt Repayment 合計約 8,852 百萬；Investing CF 合計 -5,101 百萬 (Capex 約 2,521 百萬，其餘約 2,580 百萬為非 capex 投資支出，性質工具未揭露)。
- 股本稀釋: Ordinary Shares 由 2025-12 的 312.3 百萬股增至 2026-06 的 355.3 百萬股 (+13.8%)；Diluted Average Shares 由 2025 年 314 百萬增至 2026-Q2 的 360 百萬 (+14.6%)。info 的 sharesOutstanding 為 335.6 百萬股 (時點不同)。

### 內部人交易 (2026-04-15 至 2026-10-14，約 6 個月)
| 日期 | 人員 | 職位 | 方向 | 股數 | 金額 (美元) |
|---|---|---|---|---|---|
| 2026-10-07 | Kristopher E. Moldovan | CFO (間接持有) | 賣出 @165.00 | 20,000 | 3,300,000 |
| 2026-10-06 | Scott A. Hudson | Officer | 賣出 @160.14 | 22,222 | 3,558,631 |
| 2026-09-08 | Scott A. Hudson | Officer | 賣出 @150.97–152.56 | 44,444 | 6,747,545 |
| 2026-09-08 | Kristopher E. Moldovan | CFO | 賣出 @151.03 | 20,000 | 3,020,600 |
| 2026-09-01 | James A. Burke | CEO | 買進 @135.25–135.99 | 6,665 | 903,069 |
| 2026-08-24 | James A. Burke | CEO | 買進 @135.00 | 2,000 | 270,000 |
| 2026-06-18 | John R. Sult | Director | 賣出 @170.00 | 6,500 | 1,105,000 |
| 2026-06-18 | Arcilia C. Acosta | Director | 賣出 @165.04–170.00 | 15,000 | 2,512,800 |
| 2026-06-16 | Scott Bradford Helm | Director | 賣出 @160.00 | 25,000 | 4,000,000 |
| 2026-06-15 | Paul M. Barbas | Director | 賣出 @147.93–153.00 | 488 | 73,427 |
| 2026-06-02 | Margaret M. Montemayor | Officer | 賣出 @160.00 | 4,600 | 736,000 |
| 2026-05-27 | Margaret M. Montemayor | Officer | 賣出 @164.96 | 5,000 | 824,800 |

- 公開市場賣出: 10 筆，合計 163,254 股，金額約 25.88 百萬美元。
- 公開市場買進: 2 筆 (皆為 CEO)，合計 8,665 股，金額約 1.17 百萬美元。
- 淨賣出約 24.7 百萬美元，占 Market Cap (50,946 百萬美元) 約 0.05%，規模小。
- 2026-05-15 董事 Stock Award (Grant) 共 10 筆，屬非現金配發，未計入。
- 賣出多集中於 150–170 美元區間，CEO 則在 135–136 美元區間買進，兩者價位不同，但樣本少，訊號強度有限。
- 持股結構: insidersPercentHeld 0.77%，institutionsPercentHeld 91.97% (1,879 家機構)。前幾大機構: BlackRock 8.66%、Vanguard Capital Management 6.37%、Vanguard Portfolio Management 5.05%、State Street 5.02%、FMR 4.22% (季度持股變動 -10.4%)。

## Valuation

以 2026-10-14 收盤價 151.79 美元計算。Market Cap 50,946 百萬美元 (info, 以 335.6 百萬股計)；Enterprise Value 73,507 百萬美元 (info)。

- Trailing P/E: 27.4x (info, trailingEps 5.54)。
- Forward P/E: 14.6x (info, forwardEps 10.42)；以 epsCurrentYear 8.78 計算約 17.3x。
- PEG: 0.45 (info)。
- EV/EBITDA: 11.06x (info, EBITDA 6,646 百萬)；以 2025 年 Normalized EBITDA 6,263 百萬計算，約 11.7x。
- P/S (trailing): 2.65x (info)；EV/Revenue 3.83x (info)。
- P/FCF: 以 2025 FCF 1,288 百萬計約 39.6x；以 TTM FCF 約 309 百萬計約 165x，數字失真，參考價值低。
- P/B: 以 2026-06 Stockholders Equity 31,977 百萬計約 1.59x。info 的 priceToBook 為 16.97x 與報表不一致，本報告不採用。
- 同業中位數: 工具未提供 (DATA_UNAVAILABLE)。定性上，此類 IPP 股的 P/E 與 EV/EBITDA 需與同業比較，本報告不以數字估計同業中位數。
- 分析師共識 (20 位): 平均評級 1.33 (Strong Buy)；目標價平均 210.25 美元 (相對現價 +38.5%)、中位 211.00、最低 106.00 (-30.2%)、最高 305.00 (+100.9%)。
- 技術位置: 52 週區間 132.66–217.10 美元，現價位於區間下段 (距低點 +14.4%、距高點 -30.1%)；50 日均線 144.40 (現價高於 +5.1%)、200 日均線 154.68 (現價低於 -1.9%)。最近一日 -6.51% (162.36 → 151.79)。Beta 1.384；52 週股價變化 -28.0%，同期 S&P 500 為 +15.7%。
- 空方部位: Shares Short 10.48 百萬股，占 Float (313.0 百萬股) 約 3.35%；上月為 10.78 百萬股。

## Key catalysts
- 下次財報: 2026-11-06 (工具標示非估計日期)，EPS 預估 2.59 美元。
- 最近財報: 2026-08-10 公布之季度 Reported EPS 0.76 美元，對比預估 1.66 美元，surprise -54.2%。過去四季 EPS surprise: 2025-11 為 -10.5%、2026-02 為 -76.5%、2026-05 為 +53.4%、2026-08 為 -54.2%，波動大。
- 資料衝突: earnings_dates 的 Reported EPS (0.76 / 2.87 / 0.54 / 1.75) 與 quarterly_fin 的 Diluted EPS (2026-06 為 1.42、2026-03 為 4.49、2025-12 為 1.38、2025-09 為 2.97) 不一致，可能是 adjusted 與 GAAP 口徑不同，需以公司公告核對。
- 管理層指引 (guidance): 工具未提供 (DATA_UNAVAILABLE)。
- 併購或資本化交易: 2026 上半年資產負債表大幅擴張，但交易名稱、金額、交割狀態工具未揭露 (DATA_UNAVAILABLE)，需以 SEC 8-K 與 10-Q 確認。
- 股利: 2026-09-21 除息、2026-09-30 發放 (已過)；下次股利日期工具未提供。
- 內部人動向: CEO 於 2026-08-24 與 2026-09-01 買進，為本期唯一公開市場買進紀錄。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| Total Revenue (年度, 百萬美元) | 25,533 (2025) | +8.3% | DATA_UNAVAILABLE | 中性: 營收回升但 3 年 CAGR 僅 1.5% |
| Total Revenue (季度, 百萬美元) | 7,504 (2026-Q2) | +23.0% | DATA_UNAVAILABLE | 正向，但 Q1 基期異常，需核對 |
| Gross Margin | 18.4% (2025) | 由 25.4% 降 -7.0pt | DATA_UNAVAILABLE | 偏弱，波動大 |
| Operating Margin | 16.4% (2025) | 由 20.6% 降 -4.2pt | DATA_UNAVAILABLE | 中性偏弱；2026-Q2 轉為負 (-0.6%) |
| Net Margin | 9.1% (2025) | 由 15.9% 降 -6.8pt | DATA_UNAVAILABLE | 中性偏弱 |
| ROE | 16.8% (2025, 報表計算) | 由 31.1% 降 | DATA_UNAVAILABLE | 尚可，但較 2024 大幅下降 |
| ROIC (近似) | 15.0% (2025) | 由 19.5% 降 | DATA_UNAVAILABLE | 尚可 |
| FCF (年度, 百萬美元) | 1,288 (2025) | 由 -5,029 轉正 | DATA_UNAVAILABLE | 首次轉正，但幅度小 |
| FCF Margin | 5.0% (2025) | n/a | DATA_UNAVAILABLE | 偏低 |
| FCF / NI | 0.56x (2025) | n/a | DATA_UNAVAILABLE | 不健康 (低於 0.9) |
| TTM FCF (百萬美元) | 約 309 (2025-Q3 至 2026-Q2) | n/a | DATA_UNAVAILABLE | 弱 |
| Current Ratio | 1.46x (2026-06) | 由 1.53x (2025-12) 降 | DATA_UNAVAILABLE | 中性 |
| Total Debt (百萬美元) | 24,700 (2026-06) | +174.7% vs 2025-12 | DATA_UNAVAILABLE | 明顯惡化 |
| Net Debt (百萬美元) | 24,003 (2026-06) | 由 5,351 增 | DATA_UNAVAILABLE | 明顯惡化 |
| Debt / Equity | 0.77x (2026-06) | 由 0.62x 升 | DATA_UNAVAILABLE | 槓桿升高 |
| Net Debt / EBITDA (TTM) | 約 3.46x (2026-06) | 2025 年為 0.85x | DATA_UNAVAILABLE | 惡化 |
| Interest Coverage (EBIT / Interest, 2025) | 約 7.9x | n/a | DATA_UNAVAILABLE | 尚可 |
| Cash & Equivalents (百萬美元) | 697 (2026-06) | 由 3,641 (2025-12) 降 | DATA_UNAVAILABLE | 流動性緩衝變薄 |
| Capex (年度, 百萬美元) | 2,949 (2025) | +15.0% | DATA_UNAVAILABLE | 持續高資本支出 |
| Dividend Coverage (FCF, 2025) | 2.65x | n/a | DATA_UNAVAILABLE | 2025 尚可 |
| Dividend Coverage (TTM FCF) | 約 0.56x | n/a | DATA_UNAVAILABLE | 不足 |
| Diluted Shares (百萬股) | 360 (2026-Q2) | 較 2025 年 314 增 +14.6% | DATA_UNAVAILABLE | 稀釋明顯 |
| 內部人淨交易 (6 個月) | 賣 25.9 百萬 / 買 1.2 百萬 | n/a | DATA_UNAVAILABLE | 偏空，但占市值 0.05%，訊號弱 |
| Trailing P/E | 27.4x | n/a | DATA_UNAVAILABLE | 偏貴 |
| Forward P/E | 14.6x | n/a | DATA_UNAVAILABLE | 具吸引力 (前提為獲利回升) |
| EV/EBITDA | 11.06x (info) | n/a | DATA_UNAVAILABLE | 中性 |
| P/FCF (2025) | 39.6x | n/a | DATA_UNAVAILABLE | 偏貴 |
| P/S (trailing) | 2.65x | n/a | DATA_UNAVAILABLE | 中性 |
| P/B (2026-06 報表計算) | 1.59x | n/a | DATA_UNAVAILABLE | 中性 |
| PEG | 0.45 | n/a | DATA_UNAVAILABLE | 具吸引力 (依賴 info 的 forward EPS) |
| 分析師平均目標價 | 210.25 美元 (+38.5%) | n/a | DATA_UNAVAILABLE | 偏多 (20 位, Strong Buy) |
| EPS Surprise (最近一季) | -54.2% | n/a | DATA_UNAVAILABLE | 負向，波動大 |

## Red flags
- 資本結構快速擴張: Total Debt 由 2025-12 的 89.9 億增至 2026-06 的 247.0 億 (+174.7%)，Long Term Debt 由 72.5 億增至 191.1 億；Stockholders Equity 增 120%、股本增 13.8%，屬大型交易的稀釋與槓桿並存，交易細節工具無法確認。
- 現金流不足以覆蓋股利與資本支出: TTM FCF 約 3.1 億美元，TTM 股利約 5.5 億美元，覆蓋僅 0.56x；2026 上半年 FCF 合計 -9.7 億美元。
- 獲利轉弱: 2026-Q2 Operating Income -4,700 萬美元、Normalized Income -2.24 億美元，EPS surprise -54.2%；2025 年 Net Income 較 2024 下降 38%。
- 利息成本上升: 2026-Q2 Interest Expense 2.83 億美元，較去年同期增約 140%；TTM 約 7.83 億美元。
- 流動性下降: Cash 由 36.4 億降至 7.0 億美元，quickRatio (info) 為 0.258。
- 股價走弱: 52 週 -28.0%，最近一日 -6.51%，現價低於 200 日均線；內部人淨賣出 25.9 百萬美元 (CEO 小額買進除外)。
- 資料一致性: info 與報表多項比率不一致 (totalRevenue 19.2B vs TTM 31.3B、grossMargins 38.3% vs 18.4%、debtToEquity 373% vs 62–77%、currentRatio 0.97 vs 1.46–1.53、ROE 43.0% vs 16.8%、bookValue 8.95 vs 報表約 90 美元/股、freeCashflow 37 百萬 vs TTM 309 百萬)。本報告以報表計算值為主，info 值僅作參考，建議覆核。
- 2026-Q1 異常高值 (營收 111.2 億、Operating Income 22.7 億、Normalized EBITDA 29.5 億) 性質未知，若為一次性或 mark-to-market 項目，會扭曲 TTM 與估值比率。
- 同業與分部資料缺口: 分部營收、管理層指引、同業中位數均為 DATA_UNAVAILABLE，本報告無法完整驗證 segment shift 與相對估值。

FUNDAMENTALS REPORT COMPLETE
