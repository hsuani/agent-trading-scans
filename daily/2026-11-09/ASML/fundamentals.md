# Fundamentals — ASML as of 2026-11-09

資料說明：ASML 財報以 EUR 計價（info.financialCurrency = EUR）；股價與市值以 USD 計（NasdaqGS ADR，1 ADR = 1 普通股）。本報告財務數字一律以 **B EUR**（十億歐元）或 **M EUR** 標示；市值與股價以 **USD** 標示。EUR/USD 隱含匯率以 info.trailingEps（40.64 USD）÷ 季報 TTM 稀釋 EPS（35.00 EUR）推得約 1.161，僅作換算參考。資料來源為 yf 工具，本次全部為 `source: cache`（cnyes 股價、cache 財報），屬正常備援，非錯誤。股價為 2026-11-06（週五）收盤附近資料（regularMarketTime），未見 2026-11-09 之後的實際資料。

## Executive summary

ASML 基本面強健：2026 Q3 營收 11.66B EUR（YoY +55.2%）、毛利率 57.5%、營業利益率 44.4%，TTM 淨現金約 10.8B EUR，流動比率 1.49。估值層面，trailing P/E 35.1x、EV/EBITDA（TTM，推算）約 28.5x、P/FCF（TTM，推算）約 22.5x 明顯高於一般半導體設備股估計水準，forward P/E 22.5x 與 PEG 0.74 則顯示市場押注 2027 年獲利大幅成長；分析師平均目標價 2137.25 USD 較現價高約 50%。須留意 Q3 獲利含約 5.1 億 EUR 一次性權益法/其他收益，且 Q3 現金流受約 70 億 EUR 營運資金釋放支撐，判讀時應保守，不宜直接外推。

## Revenue & profitability

**營收趨勢（B EUR）**

| 年度 | 營收 | YoY | 毛利率 | 營業利益率 | 淨利率 |
|---|---|---|---|---|---|
| FY2022 | 21.17 | — | 50.5% | 30.7% | 26.6% |
| FY2023 | 27.56 | +30.2% | 51.3% | 32.8% | 28.4% |
| FY2024 | 28.26 | +2.6% | 51.3% | 31.9% | 26.8% |
| FY2025 | 32.67 | +15.6% | 52.8% | 34.6% | 29.4% |

- 3 年營收 CAGR（FY2022–FY2025）為 **15.6%**；2 年 CAGR（FY2023–FY2025）為 **8.9%**。yfinance 年度財報僅到 FY2025（FY2021 欄位為 null）。
- 季度動能明顯加速：2025-09 季營收 7.52B、2025-12 季 9.72B、2026-03 季 8.77B、2026-06 季 9.33B、2026-09 季 11.66B。Q3 2026 營收 YoY +55.2%（info.revenueGrowth = 0.552 一致）。Q1/Q2 2026 的 YoY 因季度資料自 2025-09 起，無法計算（DATA_UNAVAILABLE）。
- TTM（2025-12 至 2026-09 四季加總）營收 39.47B EUR，與 info.totalRevenue 39,473.5M 吻合。

**獲利能力**

- 毛利率趨勢：2025-09 季 51.6% → 2025-12 季 52.2% → 2026-03 季 53.0% → 2026-06 季 54.0% → 2026-09 季 57.5%。TTM 毛利率 54.3%（info.grossMargins = 0.54337 一致）。
- 營業利益率：Q3 2026 為 44.4%（Q3 2025 為 32.8%），TTM 為 38.6%（TTM 營業利益 15.22B EUR）。
- 淨利率：Q3 2026 為 42.5%，TTM 為 34.1%（TTM 淨利 13.47B EUR，與 info.netIncomeToCommon 13,474M 吻合）。Q3 淨利受一次性項目加成，見下方說明。
- EBITDA：TTM 16.24B EUR，EBITDA 利潤率 41.1%（info.ebitda 16,181M 相符，差異來自季度加總取位）。
- R&D：FY2025 為 4.70B EUR（占營收 14.4%），TTM R&D 4.90B EUR（占營收 12.4%）。R&D 絕對金額仍持續增加，但占比隨營收大幅成長而下降。
- **一次性項目注意**：Q3 2026 稅前利潤含 "Other Income Expense / Earnings From Equity Interest" 5.10 億 EUR（稅前，yfinance 未說明來源），Q3 稅率 16.1%。扣除此項（稅後約 4.28 億）後，Q3 淨利約 45.3 億 EUR、稀釋 EPS 約 11.82，與 earnings_dates 的 Reported EPS 11.82 完全吻合（推算，見 Red flags）。

**ROE / ROIC**

- ROE：info.returnOnEquity = 65.6%（yfinance 計算值）。以 Q3 2026 期末股東權益 22.06B EUR 反算，TTM 淨利/期末權益約 61%，方向一致。
- ROIC（推算，非工具直接輸出）：TTM EBIT 15.22B × (1 − 約 17% 稅率) ≈ 12.6B EUR，除以（股東權益 22.06B + 有息負債 1.96B）≈ 24.0B EUR，約 **52%**，屬極高資本報酬水準。

**Segment 組合**：yfinance 未提供分部營收（DATA_UNAVAILABLE）。longBusinessSummary 僅定性描述產品線（EUV/DUV 微影、量測與檢測、電腦微影、服務與翻新），無數字拆分。

## Cashflow & balance sheet

**現金流（B EUR）**

| 指標 | FY2022 | FY2023 | FY2024 | FY2025 | TTM（至 2026-09） |
|---|---|---|---|---|---|
| 自由現金流 FCF | 7.17 | 3.25 | 9.08 | 11.03 | 21.00（推算） |
| FCF margin | 33.9% | 11.8% | 32.1% | 33.8% | 53.2% |
| FCF / 淨利 | 1.27 | 0.41 | 1.20 | 1.15 | 1.56 |
| 資本支出 CapEx | 1.32 | 2.20 | 2.08 | 1.63 | 1.73 |

- TTM FCF 以 OCF 22.73B − CapEx 1.73B = 21.00B 推算（與 quarterly_cf 各季 FCF 加總一致）。info.freeCashflow = 10.37B 與此不符，已列入 Red flags。
- 季度波動大：2026-03 季 FCF −2.61B（營運資金增加 −5.16B），2026-06 季 +1.32B，2026-09 季 +11.35B（營運資金釋放 +7.01B）。2026 年前三季累計 FCF 約 10.06B EUR，對應淨利 10.64B，**YTD FCF/淨利 ≈ 0.95**，略低於 0.9 門檻上緣，但已接近健康水準；全年 FCF/淨利 1.56 的 TTM 數字被 Q3 WC 釋放拉高，不宜作為常態。
- 2023 年 FCF/淨利僅 0.41（營運資金增加 −3.66B、CapEx 2.20B），顯示 ASML 現金流本身有周期性波動。

**資產負債表（Q3 2026，M EUR；比較 FY2025 年末）**

| 項目 | 2026-09-30 | 2025-12-31 |
|---|---|---|
| 現金及約當現金 + 短期投資 | 12,735 | 13,322 |
| 有息負債 Total Debt | 1,963 | 4,391 |
| 淨現金（現金 − 負債） | +10,772 | +8,931 |
| 股東權益 | 22,064 | 19,612 |
| 總資產 | 58,981 | 50,567 |
| 流動資產 / 流動負債 | 37,026 / 24,904 | 30,616 / 24,264 |
| 流動比率 | 1.49 | 1.26 |
| 速動比率（info） | 0.93 | — |
| 負債/股東權益（info.debtToEquity 8.897 = 8.9%，即 0.089x） | 0.09x | 0.22x |
| 存貨 | 11,907 | 11,429 |
| 應收帳款 AR | 9,253 | 3,023 |
| 非流動遞延收入 | 9,301 | 3,366 |

- 淨現金 10.8B EUR，負債低，短期償債能力無虞。有息負債由 FY2025 的 4.39B 降至 Q3 2026 的 1.96B。
- 營運資金變化值得留意：應收帳款 Q3 較年末增加約 206%（3.02B → 9.25B），非流動遞延收入增加約 176%（3.37B → 9.30B）。前者反映 Q3 出貨/認列集中，後者可能為客戶預付款或長期訂單，兩者組合顯示訂單能見度提升，但需追蹤收款與預付款認列節奏。
- 存貨僅增 4.2%（11.43B → 11.91B），相對營收 +55% 的增速，存貨控制良好。

## Capital allocation & insider signal

**資本配置（M EUR）**

| 項目 | FY2022 | FY2023 | FY2024 | FY2025 | 2026 YTD（Q1–Q3） | TTM |
|---|---|---|---|---|---|---|
| 股票回購 | 4,640 | 1,000 | 500 | 5,950 | 6,149 | 7,849 |
| 現金股利 | 2,560 | 2,348 | 2,453 | 2,550 | 2,376 | 2,995 |

- CapEx 自 FY2023 高點 2.20B 降至 FY2025 1.63B，但 Q3 2026 季度 CapEx 回升至 0.45B；TTM CapEx 占營收約 4.4%，屬輕資產設備商特徵。
- 股利覆蓋：TTM FCF / 股利 ≈ 7.0x；TTM 淨利 / 股利 ≈ 4.5x。info.payoutRatio = 22.3%。股利殖利率 0.65%（dividendRate 9.31 USD），股利政策保守，主要現金回饋來自回購。
- 回購力道：2026 前三季回購 6.15B EUR，其中 Q3 單季 4.07B EUR，為近年高點。TTM 股東回報（回購 + 股利）約 10.8B EUR，占 TTM FCF 約 52%。
- 股本：稀釋加權股數 Q3 2026 為 383.5M，較 Q3 2025 的 387.6M 減少 1.1%；期末流通股數約 385M（Q3 2026 資產負債表），與 FY2025 年末 385.4M 基本持平。回購主要抵消員工股票相關稀釋。

**內部人交易（6 個月）**

- yfinance `insider` 回傳空陣列。依工具定義，此為 **DATA_UNAVAILABLE**，不代表無交易：ASML 為荷蘭上市公司，歐洲 MAR 規範的 PDMR 申報未必被此來源完整收錄。
- info.companyOfficers 顯示 CEO Fouquet、CFO Dassen 等高管 exercisedValue / unexercisedValue 皆為 0，此欄位亦不足以判斷近期買賣。
- insidersPercentHeld = 0.008%（major_holders），內部人持股比例極低，即使有交易，相對市值（約 549B USD）的影響也微乎其微。

**機構持股**：institutionsPercentHeld 約 20.4%（3,002 家機構，依 13F 申報計算，對歐洲持股覆蓋不完整）。前十大機構合計約 7.9%，最大持股 FMR 1.41%（截至 2026-06-30，季增 +0.74%）。無明顯集中風險。

## Valuation

價格基準：現價 1424.75 USD（2026-11-06 收盤），市值 549.1B USD（與 385.4M 股 × 1424.75 USD 吻合）。

| 估值指標 | 數值 | 計算說明 |
|---|---|---|
| Trailing P/E | 35.1x | info.trailingPE（USD EPS 40.64） |
| Forward P/E | 22.5x | info.forwardPE（forwardEps 63.40 USD） |
| PEG | 0.74 | info.pegRatio |
| EV（推算） | 約 462.2B EUR | 市值 549.1B USD ÷ 1.161 ≈ 473.0B EUR，加有息負債 1.96B、減現金 12.74B |
| EV/EBITDA（TTM，推算） | 約 28.5x | 462.2B ÷ TTM EBITDA 16.24B EUR |
| EV/Sales（TTM，推算） | 約 11.7x | 462.2B ÷ TTM 營收 39.47B EUR |
| P/S（TTM，同幣別） | 約 12.0x | 473.0B EUR ÷ 39.47B EUR（info.priceToSalesTrailing12Months 13.9 為 USD 市值 ÷ EUR 營收，幣別不一致） |
| P/FCF（TTM，推算） | 約 22.5x | 473.0B EUR ÷ TTM FCF 21.00B EUR |
| 股利殖利率 | 0.65% | info.dividendYield |

**分析師共識**（17 位，info）：recommendationMean 1.37（strong_buy）；目標價平均 2137.25 USD（+50.0%）、中位數 2288.98 USD（+60.6%）、最高 2831.92 USD（+98.7%）、最低 862.09 USD（−39.5%）。

**價格結構**：52 週區間 946.11–1999.96 USD，現價距高點 −28.8%、距低點 +50.6%；52 週漲幅 +37.2%，同期 S&P 500 為 +8.0%（info.SandP52WeekChange）。現價低於 50 日均線 1677.25（−15.1%）與 200 日均線 1600.15（−11.0%）。Beta 1.33。

**估值判讀**：以 forward P/E 22.5x 看，相較於 TTM P/E 35.1x 有明顯 EPS 成長假設（forwardEps 63.40 USD vs trailing EPS 40.64 USD，約 +56%）；但 forwardEps 與 epsCurrentYear（41.41 USD）之間的跨期差距很大，需以 ASML 官方指引與分析師明細核對。

**同業中位數**：本次工具未提供 semi equipment 同業資料。以下「Sector median (estimate)」為分析師估計、未經工具驗證，僅供參考：trailing P/E 約 30x、forward P/E 約 25x、EV/EBITDA 約 22x、P/FCF 約 30x、毛利率 約 45%、營業利益率 約 30%、ROE 約 25%。

## Key catalysts

- **最近一次財報**：2026-10-14（earnings_dates）。Q3 2026 稀釋 EPS 報 11.82（consensus estimate 10.76，beat +9.9%）。注意：財務報表計算的 Q3 稀釋 EPS 為 12.93，兩者差異見 Red flags。
- **下次財報**：2027-01-27（earnings_dates，isEarningsDateEstimate = false）。EPS 估計 15.39（earnings_dates 欄位，幣別未標示，推測為 EUR；DATA_UNAVAILABLE 以確認）。
- **股利**：依 info 的 exDividendDate 換算約 2026-10-27，dividendDate 約 2026-11-04，皆已過，屬已發生事件。
- **近期指引（guidance）**：yfinance 未提供，DATA_UNAVAILABLE。
- **產品/訂單能見度**：Q3 非流動遞延收入增至 9.30B EUR（+176% vs 年末），為訂單/預付款的間接訊號，需以公司 Q3 2026 新聞稿與法說會內容確認（本次工具無法取得）。
- **分部組合變化**：DATA_UNAVAILABLE。
- **成長情境**：分析師 forward EPS 隱含 2027 年大幅成長；Q4 2026 季度營收/毛利率能否延續 Q3 水準，為下一次財報的關鍵檢驗點。

## Metrics table

金額單位：財務數字為 B EUR 或 M EUR；市值與股價為 USD。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收（TTM, B EUR） | 39.47 | Q3 YoY +55.2% | n/a | 強 |
| 營收 3Y CAGR（FY22–25） | 15.6% | — | n/a | 強 |
| 毛利率（TTM） | 54.3% | Q3 57.5%（Q3'25 51.6%） | ~45% | 極強 |
| 營業利益率（TTM） | 38.6% | Q3 44.4%（Q3'25 32.8%） | ~30% | 極強 |
| 淨利率（TTM） | 34.1% | Q3 42.5%（含一次性） | ~20% | 強 |
| EBITDA 利潤率（TTM） | 41.1% | n/a | ~30% | 強 |
| ROE（info） | 65.6% | n/a | ~25% | 極強 |
| ROIC（推算） | 約 52% | n/a | ~15% | 極強 |
| FCF（TTM, B EUR，推算） | 21.00 | FY2025 11.03 | n/a | 強（但含 WC 釋放） |
| FCF margin（TTM） | 53.2% | FY2025 33.8% | ~15% | 強 |
| FCF / 淨利（TTM） | 1.56 | FY2025 1.15；YTD 0.95 | >0.9 健康 | 健康，留意季度波動 |
| CapEx / 營收（TTM） | 4.4% | FY2025 5.0% | ~5% | 中性 |
| 淨現金（Q3 2026, B EUR） | +10.77 | FY2025 +8.93 | n/a | 強 |
| 流動比率（Q3 2026） | 1.49 | FY2025 1.26 | ~2.0 | 中性偏低，無虞 |
| 負債/股東權益（Q3 2026） | 0.09x | FY2025 0.22x | ~0.2x | 強 |
| 股利覆蓋（TTM FCF / 股利） | 7.0x | n/a | n/a | 強 |
| 稀釋股數（Q3 2026, M） | 383.5 | YoY −1.1% | n/a | 中性偏正（回購） |
| 內部人交易（6 個月） | DATA_UNAVAILABLE（空陣列） | n/a | n/a | 無法判定 |
| 機構持股比例 | 20.4%（13F 口徑） | n/a | n/a | 中性 |
| Trailing P/E | 35.1x | n/a | ~30x | 偏貴 |
| Forward P/E | 22.5x | n/a | ~25x | 合理 |
| PEG | 0.74 | n/a | n/a | 有吸引力（依賴成長假設） |
| EV/EBITDA（TTM，推算） | 約 28.5x | n/a | ~22x | 偏貴 |
| P/FCF（TTM，推算） | 約 22.5x | n/a | ~30x | 中性 |
| P/S（TTM，同幣別） | 約 12.0x | n/a | n/a | 偏高 |
| 分析師平均目標價 | 2137.25 USD（+50.0%） | n/a | n/a | 共識偏多 |
| 52 週漲幅 vs S&P 500 | +37.2% vs +8.0% | — | n/a | 相對強勢 |

## Red flags

- **Q3 2026 EPS 口徑不一致**：財報報表計算稀釋 EPS 為 12.93（淨利 4,960.4M ÷ 383.5M 股），earnings_dates 的 Reported EPS 為 11.82。推算：扣除稅前 509.7M 一次性收益（稅後約 427.7M）後，淨利約 4,532.7M，÷ 383.5M ≈ 11.82，與 earnings_dates 完全吻合，因此 11.82 很可能是剔除一次性項目後的數字。此為推算，需以 ASML Q3 2026 新聞稿核對。
- **Q3 獲利品質**：稅前利潤含 5.1 億 EUR 權益法/其他收益（來源未標示）；Q3 CFO 另受營運資金釋放 +7.0B EUR 支撐。Q3 獲利與現金流皆非常態，不宜直接外推至 Q4。
- **FCF 數據不一致**：info.freeCashflow = 10.37B 與季度/年度 CF 加總的 TTM FCF 21.00B 差距約 2 倍，本報告採後者（OCF − CapEx）。
- **info 估值欄位不可直接使用**：enterpriseToEbitda 1873 與 enterpriseToRevenue 767.9 明顯與市值/EBITDA、營收不符（單位或計算口徑異常），本報告改以推算值取代；priceToSalesTrailing12Months 13.9 混用 USD 市值與 EUR 營收，已修正為約 12.0x。
- **EPS 幣別混用**：info.trailingEps 40.64 與 forwardEps 63.40 為 USD，季報 EPS 為 EUR，earnings_dates 的 EPS estimate 幣別未標示。跨來源比較時須先換算。
- **應收帳款與遞延收入大幅上升**：AR Q3 較年末 +206%，非流動遞延收入 +176%。若為收款延遲或客戶預付款集中，短期現金流可能出現波動（Q1 2026 FCF 已為 −2.6B EUR）。
- **估值偏高（以 TTM 計）**：trailing P/E 35.1x、EV/EBITDA 約 28.5x，且股價距 200 日均線 −11.0%、距 52 週高點 −28.8%，市場對於成長持續性的定價仍在調整中。
- **資料覆蓋缺口**：年度財報僅至 FY2025；季度資料自 2025-09 起，Q1/Q2 2026 無 YoY；無 segment、無公司指引、內部人交易為空陣列（DATA_UNAVAILABLE）。
- **資料來源**：股價為 cnyes cache（2026-11-06 收盤附近），財報為 cache；屬正常備援，並無 2026-11-09 之後的資料。

FUNDAMENTALS REPORT COMPLETE
