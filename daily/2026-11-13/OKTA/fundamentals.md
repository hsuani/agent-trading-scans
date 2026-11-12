# Fundamentals — OKTA as of 2026-11-13

資料來源: pipeline/tools/yf（OKTA info / fast_info / financials / quarterly_fin / balance_sheet / quarterly_bs / cashflow / quarterly_cf / earnings_dates / insider / major_holders / inst_holders）。上述多數欄位皆為 `source: cache`（live feed 失敗後回退至 prices/yf 快取，屬預期行為），快取時間戳為 2026-11-12 15:01–15:06 UTC。
單位: 財報金額為 USD M（百萬美元）；市值與企業價值為 USD B（十億美元）。財年 FY 以 yfinance 財年結束日標示（Okta 財年結束於 1 月 31 日，例如 FY2026 = 截至 2026-01-31）。
資料時點檢查: 最新財報季為截至 2026-07-31 之季度（yfinance 日期標示）；最新價格為 2026-11-12 快取。未發現晚於 2026-11-13 的資料被採用。下次財報 2026-12-01 為未來排程，非已發生資料。

## Executive summary
Okta 已由 GAAP 虧損轉為穩定獲利（FY2026 淨利 USD 235M、TTM 淨利 USD 296M），毛利率升至 78%、FCF 率約 31%，淨現金約 USD 2.25B，財務體質健康；但 GAAP 獲利大量依賴利息收入與低稅率，且 SBC 佔營收約 16%，GAAP P/E 高達 107.8x。估值以 forward non-GAAP P/E 約 40.9x、P/S 10.2x 計算仍屬高檔，分析師共識目標均價 USD 214.7 高於現價 USD 179.03，但 2026-11-12 股價已自 52 週高點 USD 235.0 回落約 24%。

## Revenue & profitability

**營收成長**
- 營收（USD M）: FY2023 1,858 → FY2024 2,263 → FY2025 2,610 → FY2026 2,919。
- YoY: FY2024 +21.8%、FY2025 +15.3%、FY2026 +11.8%，成長動能逐年放緩。
- 3 年 CAGR（FY2023–FY2026）約 16.3%。yfinance 年度資料不含 FY2022 營收（欄位為 null），因此無法計算 5 年 CAGR，列為 DATA_UNAVAILABLE。
- 季度趨勢（USD M）: 2025-07 季 728 → 2025-10 季 742 → 2026-01 季 761 → 2026-04 季 765 → 2026-07 季 805；2026-07 季 YoY +10.6%（對應 info revenueGrowth 0.106）。TTM 營收 USD 3,073M（與 info totalRevenue 3,072.999936M 一致）。
- 業務組合: yfinance 不提供分部營收，業務描述來自 info.longBusinessSummary（身分認證平台：SSO、Adaptive MFA、Universal Directory、Identity Governance、Auth0 / AI Agents 等）。分部營收佔比 DATA_UNAVAILABLE。

**利潤率趨勢**（以 yfinance 「Operating Income」列計算）

| 指標 | FY2023 | FY2024 | FY2025 | FY2026 | TTM（至 2026-07） |
|---|---|---|---|---|---|
| 毛利率 | 70.6% | 74.3% | 76.3% | 77.4% | 78.1%（2026-07 季 79.6%） |
| 營業利益率 | -42.1% | -20.3% | -2.4% | 5.2% | 7.7% |
| 淨利率 | -43.9% | -15.7% | 1.1% | 8.1% | 9.6% |
| 研發 / 營收 | 33.4% | 29.0% | 24.6% | 21.9% | n/a |
| 銷售與行銷 / 營收 | 57.4% | 45.8% | 37.0% | 34.9% | n/a |
| 一般管理 / 營收 | 22.0% | 19.9% | 17.2% | 15.3% | n/a |

- 營業利益 USD M: FY2023 -783 → FY2024 -460 → FY2025 -63 → FY2026 153；TTM 236。
- 淨利 USD M: FY2023 -815 → FY2024 -355 → FY2025 28 → FY2026 235；TTM 296。
- 稀釋 EPS（GAAP）: FY2026 1.31；TTM 1.66（info trailingEps 1.66）。手算核對: FY2026 EPS 1.31 × 稀釋股數 179.29M ≈ USD 234.9M，與淨利 235 吻合。
- 注意: 營業利益率由負轉正主要來自 S&M 與 G&A 佔比下降；FY2026 GAAP 淨利中，利息收入 USD 110M（net interest income 106M）與 7.9% 有效稅率為重要貢獻。FY2026 稅前利潤 255M，稅費僅 20M。
- ROE（info returnOnEquity）4.3%；以 FY2026 淨利 / 平均股東權益 (6,999 + 6,405)/2 估算約 3.5%。ROA（info）1.6%。
- ROIC: yfinance 無直接欄位。以 TTM 營業利益 USD 236M / 2026-07 投入資本 USD 6,973M 估算稅前 ROIC 約 3.4%（估算值，非工具直接提供）。

## Cashflow & balance sheet

**現金流品質**（USD M）

| 指標 | FY2023 | FY2024 | FY2025 | FY2026 | TTM（至 2026-07） |
|---|---|---|---|---|---|
| 營業現金流 | 86 | 512 | 750 | 884 | n/a |
| 資本支出 | -23 | -24 | -20 | -21 | 季度合計約 -25 |
| 自由現金流（FCF） | 63 | 488 | 730 | 863 | 959 |
| FCF 率 | 3.4% | 21.6% | 28.0% | 29.6% | 31.2% |
| FCF / 淨利 | NM | NM | 26.1x | 3.67x | 3.24x |
| SBC（股權激勵） | 677 | 684 | 565 | 544 | 503 |
| SBC / 營收 | 36.4% | 30.2% | 21.6% | 18.6% | 16.4% |
| FCF 減 SBC（估算） | n/a | n/a | n/a | 319 | 456（率 14.8%） |

- FCF / 淨利 遠高於 0.9 的健康門檻，但分子為 FCF 而分母為被利息收入與低稅率墊高的 GAAP 淨利，此比率的品質解讀需保留。yfinance info freeCashflow 為 USD 1,037.6M，與季度 FCF 加總 959M 的定義不同，本報告以季度加總值為主、info 值為對照。
- SBC 在 FCF 中的佔比仍高（TTM SBC 為 TTM FCF 的 52%）。若以 FCF 扣除 SBC 計，TTM 率約 14.8%，仍屬正值。

**資產負債表**（USD M）

| 項目 | 2026-01（FY2026 年末） | 2026-04 | 2026-07 |
|---|---|---|---|
| 現金及短期投資 | 2,553 | 2,589 | 2,299 |
| 總負債（debt，含租賃） | 422 | 411 | 53 |
| 淨現金（現金及短投 - total debt） | 2,131 | 2,178 | 2,246 |
| 流動資產 | 3,644 | 3,306 | 3,089 |
| 流動負債 | 2,554 | 2,312 | 2,025 |
| 流動比率 | 1.43 | 1.43 | 1.53 |
| 股東權益 | 6,999 | 6,899 | 6,973 |
| 商譽 | 5,487 | 5,487 | 5,487 |
| 有形帳面淨值 | 1,421 | 1,334 | 1,406 |
| 遞延收入（流動） | 1,875 | 1,729 | 1,751 |

- 淨現金: 以 2026-07 現金及短投 USD 2,299M（info totalCash 2,299M）扣除總負債 USD 53M，淨現金約 USD 2,246M。yfinance 的 Net Debt 欄位在不同期間口徑不一致（例如 2025-01 列 449M 與 total debt 952M 減現金不符），本報告不採用，改以上述自算值。
- 負債: 2026-07 總負債 USD 53M（僅剩租賃負債），前一季仍有 USD 350M 流動債務（2025-07 為 USD 859M）。債務已大幅清償；清償細節（現金或轉換）工具未提供，列為 DATA_UNAVAILABLE。
- info debtToEquity 為 0.76（以百分比表示，即 0.76%），以 53 / 6,973 計算約 0.008x，與之一致。
- 流動比率 info 1.525、quick ratio 1.376，短期流動性充足。
- 商譽 USD 5.49B 佔總資產 9,138M 約 60%，有形淨值僅 USD 1.41B，資產負債表以無形資產為主。
- 應收帳款 USD 469M（2026-07），YoY +12.5%（2025-07 為 417M）；流動遞延收入 USD 1,751M，YoY +13.0%（2025-07 為 1,550M），可作為訂閱續約的領先指標，顯示營收動能仍在。

## Capital allocation & insider signal

**資本配置**
- 資本支出極低（FY2026 USD 21M，佔營收約 0.7%），資本密集度低。
- 股票回購: FY2026 年度現金流量表 USD 73M；2026-04 季 USD 248M，2026-07 季 USD 124M，最近兩季合計 USD 372M（約為目前市值的 1.2%）。2025-07 之前的季度回購為 0。
- 股本: 普通股 2023-01 為 161.3M 股、2026-01 為 177.4M、2026-07 為 174.8M，2026 年起由淨稀釋轉為淨縮減。稀釋加權平均股數 FY2023 158.0M → FY2026 179.3M（三年增加約 13.5%），其中 SBC 為主要稀釋來源。
- 股利: 無（info dividendYield 0.0，trailingAnnualDividendRate 0.0）。股利覆蓋率 n/a。
- 併購: FY2026 收購現金支出 USD 56M（Purchase of Business）。

**內部人交易**（2026-05-13 至 2026-11-13，共 10 筆公開市場賣出，買入 0 筆）
- 賣出總額 USD 46.0M，約為市值 USD 31.3B 的 0.15%。
- 依人員: Tighe Brett（CFO）USD 20.5M、McKinnon Todd（CEO）USD 19.6M、Schwartz Larissa（Officer）USD 3.6M、Kelleher Eric（President）USD 2.1M、Archambeau Shellye（Director）USD 0.2M。
- 其他非市場交易: 贈與 3 筆、授予 1 筆、衍生性證券轉換 1 筆；另有 15 筆無說明文字的交易（多為 RSU 歸屬或稅款扣繳，性質 DATA_UNAVAILABLE，未列入賣出統計）。
- 解讀: 無內部人買入，且 CEO 與 CFO 在 2026-07 至 2026-09 期間於 USD 145–198 區間有大額賣出，屬於需要注意的訊號。不過內部人持股比例僅 0.51%，佔市值比例亦低，訊號強度中等。
- 機構持股: 機構持股 96.6%（1,307 家）。前十大包括 BlackRock 11.2%、FMR 8.0%（2026-09-30 季較前期減持 18.2%）、Vanguard 合計約 9.9%。
- 空頭: 空單 6.59M 股，佔流通股 4.4%，days to cover 2.05；空單較前月減少約 16.9%。

**治理風險評分**（info，1–10，10 為最高風險）: overallRisk 10、shareHolderRightsRisk 10、compensationRisk 9、boardRisk 9、auditRisk 1。治理風險分數偏高，應列為注意事項。

## Valuation

**價格基礎**: info currentPrice / regularMarketPrice USD 179.03（2026-11-12，previousClose 182.25，當日 -1.77%）。fast_info 快取 last_price 為 USD 176.70（feed: cnyes，15:01 UTC），與 info 相差約 1.3%，本報告以 info 為主。
- 市值 USD 31.30B（info marketCap）。以 179.03 × 隱含股數 174.8M 核對 ≈ USD 31.30B，吻合。info sharesOutstanding 167.1M 為較舊口徑，未採用。
- 企業價值 USD 29.62B（info enterpriseValue）。以市值減淨現金自算約 USD 29.05B，差異 USD 0.56B 來源 DATA_UNAVAILABLE。

**估值倍數**
- 追蹤 P/E（GAAP）: 107.8x（179.03 / 1.66）。
- Forward P/E（non-GAAP 一致預估）: 40.9x（179.03 / forwardEps 4.378）；PEG 1.3。
- 注意: trailingPE 採 GAAP，forwardPE 採 non-GAAP（季度 EPS 比對 earnings_dates 的 Reported EPS 為 non-GAAP，例如 2026-07 季 1.05），兩者基礎不同，不宜直接比較。
- EV / EBITDA（TTM）: 92.3x（info ebitda USD 321M，EV/EBITDA 欄位 92.26）。EBITDA 為 GAAP 口徑且 SBC 未扣除，此倍數參考性有限。
- P/S（TTM）: 10.2x；EV/Revenue 9.6x。
- P/FCF（TTM）: 32.6x（市值 / TTM FCF 959M）；以 info freeCashflow 計為 30.2x。
- P/B: 4.5x（市值 / 股東權益 6,973M）。
- 同業中位數: yfinance 不提供同業資料，列為 DATA_UNAVAILABLE。下表「估計」欄為分析師依軟體基礎設施與身分安全類股之粗估，非工具資料，僅供參考。

**價格位置**
- 52 週區間 USD 62.66–235.00；現價較 52 週高點低 23.8%，較 52 週低點高 185.7%（52WeekChange +117.6%）。
- 50 日均線 USD 197.46（現價低於 9.3%）；200 日均線 USD 128.10（現價高於 39.8%）。
- Beta 0.72。

**分析師共識**（43 位，info）: recommendationKey buy，recommendationMean 1.66；目標價 均值 USD 214.7（較現價 +19.9%）、中位數 USD 225.0（+25.7%）、高 USD 250.0、低 USD 127.0（-29.1%）。此為市場共識摘要，不構成交易建議。

## Key catalysts
- **下次財報**: 2026-12-01（21:00 UTC；earnings_dates 與 info earningsTimestamp 一致，isEarningsDateEstimate = False）。Q3 FY2027 的 EPS 共識（non-GAAP）0.93。
- **近期 EPS 達成率**（non-GAAP，earnings_dates）: 2026-08-26 實際 1.05 對 0.96（+8.9%）；2026-05-28 0.91 對 0.85（+6.7%）；2026-03-04 0.90 對 0.85（+6.3%）；2025-12-02 0.82 對 0.76（+8.1%）。連續多季小幅超預期，但超預期幅度低於 2024 年（+14.8%–+19.1%）。
- **財測與指引**: yfinance 未提供近期管理層財測或全年指引數字，列為 DATA_UNAVAILABLE。
- **分部與產品動向**: info 業務描述提到 Okta for AI Agents、Auth0 for AI Agents、Identity Governance 等新產品線，但未提供各產品營收，成效 DATA_UNAVAILABLE。
- **股東行動**: 2026 年起重啟回購（H1 FY2027 USD 372M），後續回購節奏為觀察重點。
- **內部人交易**: CEO / CFO 在 2026 年下半年持續大額賣出，為需追蹤事項。

## Metrics table
單位: 營收 / 利潤 / 現金流為 USD M；市值 / 企業價值為 USD B；倍數與比率為 x 或 %。「同業中位數（估計）」為粗估，非工具資料。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收（TTM，USD M） | 3,073 | +10.6%（2026-07 季） | n/a（DATA_UNAVAILABLE） | 成長穩定但減速（FY 成長 21.8% → 15.3% → 11.8%） |
| 營收 3 年 CAGR（FY23–FY26） | 16.3% | n/a | 估計約 10–15% | 高於多數同業中位數估計，屬正面 |
| 毛利率（TTM） | 78.1% | 2026-07 季 79.6%，FY 由 76.3% 升至 77.4% | 估計約 70–75% | 優良，持續擴張 |
| 營業利益率（TTM） | 7.7% | FY26 5.2% vs FY25 -2.4% | 估計約 5–15%（非 GAAP 更高） | 已轉正，但仍偏低 |
| 淨利率（TTM） | 9.6% | FY26 8.1% vs FY25 1.1% | 估計約 5–10% | 改善中，但受利息收入與低稅率支撐 |
| ROE | 4.3% | n/a | 估計約 10–15% | 偏弱 |
| ROIC（估算，稅前） | 3.4% | n/a | 估計約 8–12% | 偏弱，商譽佔資產約 60% |
| FCF 率（TTM） | 31.2% | FY26 29.6% vs FY25 28.0% | 估計約 20–25% | 優良 |
| FCF / 淨利（TTM） | 3.24x | n/a | 健康門檻 >0.9 | 健康，但分母偏低 |
| SBC / 營收（TTM） | 16.4% | FY26 18.6% vs FY25 21.6% | 估計約 10–15% | 偏高，持續下降 |
| FCF 減 SBC 率（TTM） | 14.8% | n/a | n/a | 仍為正，但低於 FCF 率 |
| 淨現金 | USD 2,246M（2026-07） | 2026-01 為 2,131M | n/a | 強 |
| 總負債 / 股東權益 | 0.76%（info 百分比） | n/a | 估計約 20–40% | 極低 |
| 流動比率 | 1.53x | 2026-01 為 1.43x | 估計約 1.5–2.5x | 合理 |
| 有形帳面淨值 | USD 1,406M | 2026-01 為 1,421M | n/a | 偏低，資產以商譽為主 |
| 資本支出 / 營收（FY26） | 0.7% | n/a | 估計約 1–3% | 極低，資本輕 |
| 股票回購（H1 FY27） | USD 372M | 2025 同期 0 | n/a | 新啟動，正面 |
| 流通股數（2026-07） | 174.8M | 2025-07 為 176.3M（-0.9%） | n/a | 開始縮減 |
| 股利殖利率 | 0.0% | n/a | n/a | 無配息 |
| 內部人淨賣出（6 個月） | USD 46.0M（10 筆，0 買入） | n/a | n/a | 負面訊號 |
| 內部人賣出佔市值 | 0.15% | n/a | n/a | 占比低 |
| 機構持股 | 96.6% | n/a | n/a | 高度機構化 |
| 空單佔流通股 | 4.4%（days to cover 2.05） | 空單月減 16.9% | n/a | 偏低 |
| 追蹤 P/E（GAAP） | 107.8x | n/a | 估計 30–50x | 偏貴 |
| Forward P/E（non-GAAP） | 40.9x | n/a | 估計 30–40x | 偏貴至中性 |
| EV/EBITDA（TTM） | 92.3x | n/a | 估計 25–40x | 偏貴（EBITDA 未扣 SBC） |
| P/S（TTM） | 10.2x | n/a | 估計 6–8x | 高於估計同業中位數 |
| P/FCF（TTM） | 32.6x | n/a | 估計 20–30x | 偏高 |
| P/B | 4.5x | n/a | 估計 4–6x | 中性 |
| 市值 | USD 31.30B | n/a | n/a | 中型股 |
| 企業價值 | USD 29.62B | n/a | n/a | n/a |
| 52 週股價漲跌幅 | +117.6% | 較 52 週高點 -23.8% | n/a | 高波動 |
| 分析師目標均價 | USD 214.7（+19.9%） | n/a | n/a | 共識偏多 |
| 分析師 Mean Rating | 1.66（Buy） | n/a | n/a | 偏多 |
| 治理風險 overallRisk | 10 / 10 | n/a | n/a | 高風險分數 |

## Red flags
- GAAP 獲利品質: FY2026 淨利 USD 235M 中，利息收入 USD 110M 與 7.9% 有效稅率貢獻明顯；營業利益僅 USD 153M，若不計利息與稅率效果，獲利基礎薄弱。
- SBC 負擔: TTM SBC USD 503M 為營收 16.4%、為 FCF 52%；稀釋加權股數 FY2023–FY2026 增加約 13.5%。
- 估值: GAAP P/E 107.8x、EV/EBITDA 92.3x、P/S 10.2x，估值對成長與利潤率持續擴張高度依賴。
- 營收減速: FY 成長率由 21.8% 連續降至 11.8%，2026-07 季 YoY 10.6%。
- 內部人賣出: 6 個月 USD 46.0M 公開市場賣出、0 買入；CEO 與 CFO 於 2026-07 至 2026-09 有大額賣出。
- 商譽與無形資產: 商譽 USD 5.49B 佔總資產約 60%，有形淨值僅 USD 1.41B，若未來出現減損風險需留意。
- 治理評分: overallRisk、shareHolderRightsRisk 均為 10（滿分 10），compensationRisk 9。
- 股價趨勢: 現價低於 50 日均線約 9.3%，較 52 週高點回落約 23.8%；2026-11-12 單日跌 1.77%。
- 資料缺口: 同業中位數、分部營收、管理層財測與全年指引、5 年 CAGR、ROIC 直接欄位、Net Debt 口徑、2026-07 季度債務清償細節均為 DATA_UNAVAILABLE；info sharesOutstanding（167.1M）與隱含股數（174.8M）不一致，已採用後者。

FUNDAMENTALS REPORT COMPLETE
