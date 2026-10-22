# Fundamentals — ASML as of 2026-10-22

## Executive summary
ASML 財務體質強：FY2025 毛利率 52.8%、營業利益率 34.6%、FCF 約 EUR 11.0B，帳上淨現金約 EUR 5.6B（2026-06-30）。估值仍偏高，以 TTM P/E 41.3x、P/FCF 約 62x 計算明顯高於半導體設備同業估計中位數，但以 forward P/E 26.7x 與 PEG 0.92 看，市場已定價大部分 EPS 成長。主要風險是 2026 上半年應收帳款與營運現金流急劇惡化（Q1'26 FCF 為 EUR -2.6B，AR 自 2025-12 的 EUR 3.0B 增至 2026-06 的 EUR 7.3B），以及 cache 財報落後一季（缺 2026-Q3 財報）。

## 資料來源與品質說明（先讀）
- 數據日期：分析 as-of 2026-10-22。最新收盤價為 2026-10-21 收盤 USD 1,676.69（pricefeed 歷史快取）。
- 工具狀態：本機對 Yahoo 的 live 連線遭 403 阻擋（CONNECT tunnel failed），`pipeline/tools/yf` 與 `pipeline/tools/pricefeed.py` 大多回退至 repo cache `prices/yf/ASML.json`（`_refreshed_at` 2026-10-22 11:39 UTC）。pricefeed 報價來源為 cnyes cache。
- **資料矛盾警示**：`pipeline/tools/yf ASML financials / balance_sheet / cashflow / quarterly_*` 的 live 輸出數值與 repo cache 及 `info` 嚴重不一致（例如 2025 Total Revenue 為 509,991,000，cache 為 EUR 32,667.3M；2025 年末 Total Debt 為 261.8M，cache 為 EUR 4,390.9M；股數約 215M，info 為 385.4M）。本報告一律採用 repo cache 財報數值，**不採用** live 財報輸出。
- 幣別：財報為 EUR（info 之 financialCurrency = EUR）；`info` 估值欄位（市值、TTM EPS、TTM 營收等）為 USD。比率類數字不受影響，絕對金額會註明幣別。
- `info` 中有明顯錯誤欄位，本報告排除：`enterpriseValue` = 35.7 兆（不合理）、`enterpriseToEbitda` = 2,204.7x、`priceToBook` = 1,440.8x（bookValue 1.16/股 與股東權益不符）、`enterpriseToRevenue` = 903.8x。EV 與 P/B 改以自行計算並標示。
- 財報落後：cache 季度財報最新至 2026-06-30（Q2'26）；`earnings_dates` 顯示 2026-10-14 已公告 Q3'26 EPS 11.82，但 Q3'26 完整損益表／資產負債表／現金流量表 cache 中 DATA_UNAVAILABLE。Q2'26 現金流量表在 cache 中亦缺。
- 同業中位數（sector median）工具未提供，表中數字為估計值（基於一般市場認知的粗估，非工具輸出）。

## Revenue & profitability

**營收（EUR M，cache 年度）**
- 2022 21,173.4 → 2023 27,558.5 → 2024 28,262.9 → 2025 32,667.3
- YoY：2023 +30.2%、2024 +2.6%、2025 +15.6%
- 3 年 CAGR（2022–2025）約 15.6%。2021 年財報為 null，無法計算 5 年 CAGR。
- 季度（EUR M）：Q2'25 7,691.7 → Q3'25 7,516.0 → Q4'25 9,718.1 → Q1'26 8,766.9 → Q2'26 9,326.5
- Q2'26 YoY +21.2%（對 Q2'25 7,691.7）；TTM 營收（Q3'25–Q2'26）約 EUR 35,327.5M
- 分部：`info.longBusinessSummary` 僅描述產品線（EUV、DUV 浸潤式/乾式、量測與檢測、YieldStar、HMI 電子束、computational lithography、翻新升級與服務），無分部營收數字，**segment 營收占比 DATA_UNAVAILABLE**。

**獲利能力（cache）**
- 毛利率：2022 50.5%、2023 51.3%、2024 51.3%、2025 52.8%；Q2'26 54.0%（Q1'26 53.0%）
- 營業利益率：2022 30.7%、2023 32.8%、2024 31.9%、2025 34.6%；Q2'26 37.1%（Q1'26 36.0%）
- 淨利率：2022 26.6%、2023 28.4%、2024 26.8%、2025 29.4%；Q2'26 31.3%
- EBITDA（reported, 2025）EUR 12,550.3M，EBITDA margin 38.4%
- 研發費用率：2025 14.4%（2024 15.2%），Q2'26 13.7%；R&D 絕對額 2025 EUR 4,698.8M，逐年增加
- 淨利（2025）EUR 9,609.4M，diluted EPS 24.71（2024 19.24）；3 年 EPS CAGR（2022–2025）約 15.6%，淨利 CAGR 約 19.6%
- ROE（FY2025，平均股東權益）約 50.5%（年末口徑 49.0%）；2024 同口徑約 47.4%。`info.returnOnEquity` 為 65.6%（Yahoo TTM 口徑，數值較高）。
- ROIC（估算）：NOPAT = EBIT × (1 − 有效稅率 17.6%) ≈ EUR 9,307M；以（股東權益 + 總負債）為分母 EUR 24,003M，ROIC 約 38.8%（2024 同口徑約 31.7%）。若扣除現金作為分母，ROIC 會更高。
- 2025 有效稅率 = 2,013.4 / 11,406.1 = 17.6%。

## Cashflow & balance sheet

**現金流量（EUR M）**
- 營運現金流（OCF，推算 = FCF + Capex）：2025 約 12,658.5；2024 約 11,166.2
- FCF：2022 7,167.5、2023 3,247.2、2024 9,083.1、2025 11,027.3
- FCF margin：2025 33.8%、2024 32.1%、2023 11.8%、2022 33.9%
- FCF / NI：2025 1.15x、2024 1.20x、2023 0.41x、2022 1.27x（>0.9 健康，2023 偏低）
- 季度波動大：Q2'25 FCF 318.8、Q3'25 243.7、Q4'25 10,939.9、Q1'26 −2,607.9。Q1'26 OCF −2,185.6，FCF/NI 約 −0.95x。TTM FCF（Q2'25–Q1'26）約 EUR 8,894.5M。Q4'25 大幅正向現金流與 Q1'26 負向呈現明顯的客戶預付款與收款時點效應，年度 FCF 較具代表性。
- Q2'26 現金流量表 cache 缺漏，**Q2'26 OCF/FCF DATA_UNAVAILABLE**。
- Capex：2022 1,319.3、2023 2,196.2、2024 2,083.1、2025 1,631.2；capex/revenue 由 2024 的 7.4% 降至 2025 的 5.0%。Q1'26 capex 422.3。

**資產負債表（EUR M）**
| 項目 | 2025-12-31 | 2026-03-31 | 2026-06-30 |
|---|---|---|---|
| 現金及短期投資 | 13,321.9 | 8,376.3 | 7,581.5 |
| 總負債（有息） | 4,390.9 | 2,705.6 | 1,984.4 |
| 淨現金 | 8,931.0 | 5,670.7 | 5,597.1 |
| 股東權益 | 19,612.2 | 20,829.5 | 21,825.4 |
| 總資產 | 50,566.6 | 48,060.5 | 50,214.8 |
| 流動比率 | 1.26x | 1.36x | 1.33x |
| Debt / Equity | 22.4% | 13.0% | 9.1% |
| 存貨 | 11,429.3 | 11,711.2 | 11,739.5 |
| 應收帳款 | 3,023.0 | 4,402.9 | 7,252.6 |

- 淨現金：Q2'26 EUR 5,597M，對比 Q2'25 EUR 3,550M，YoY 約 +58%。
- 2026 上半年有息負債自 EUR 4,390.9M 降至 EUR 1,984.4M（約 −2.4B），主要為償還到期債務；現金同期減少約 EUR 5.7B。
- 應收帳款急速上升：Q2'26 AR 7,252.6，YoY +45%（Q2'25 為 4,996.9）；以 91 天估算 DSO 由 Q2'25 約 59 天升至 Q2'26 約 71 天；2025-12 更低（約 28 天）。這是本期最需要追蹤的營運資金訊號。
- 存貨 Q2'26 EUR 11,739.5M，相當於 2025 年營業成本（EUR 15,409M）的約 76%（約 278 天），庫存水位偏高，需留意後續減值或週轉風險。
- 商譽 EUR 4,588.6M（穩定，無變動）。
- 流動比率 1.33x（Q2'26），對比 Q2'25 的 1.43x 略降。`info.currentRatio` 1.487（Yahoo 口徑）。
- 整體償債能力強：淨現金、低槓桿，無短期流動性壓力跡象。

## Capital allocation & insider signal

**股東回報（EUR M）**
- 股利：2022 2,559.8、2023 2,348.3、2024 2,452.9、2025 2,550.3；2025 股利覆蓋率 FCF 4.3x、淨利 3.8x；`info.payoutRatio` 22.3%
- 買回：2022 4,639.7、2023 1,000、2024 500、2025 5,950.0（大幅增加）；2025 季度買回 Q1 2,592.6、Q2 1,485.2、Q3 172.2、Q4 1,700.0；2026-Q1 1,000
- 2025 股東回報合計 EUR 8,500M，占 FCF 約 77%（2024 約 33%）。
- 股數：普通股 2024-12 393.3M → 2025-12 385.4M（−2.0%）；2026-06 384.1M。Diluted 平均股數 2025 388.9M，YoY −1.2%。
- 股息：`info.dividendRate` USD 9.08，殖利率 0.54%；`corporateActions` 顯示已宣告現金股息 USD 2.108，除息日 2026-10-27（為 as-of 之後的事件）。

**內部人交易**
- `pipeline/tools/yf ASML insider` 回傳空陣列 `[]`，**6 個月內部人交易 DATA_UNAVAILABLE**，無法判斷淨買或淨賣。
- 內部人持股比例 `heldPercentInsiders` 約 0.008%，持股占比極低，即使有交易，對市值的相對份量也有限。

**機構持股**
- 機構持股占比 20.3%（2,971 家機構）。
- 前五大：FMR LLC（5.48M 股，1.41%，2026-06-30 季報，較前期增加 74%）、Fisher Asset Management（4.74M，1.22%）、Capital World Investors（3.73M，0.96%）、Invesco（3.14M，0.81%）、State Farm（2.76M，0.71%）。持股相當分散，無單一大股東集中風險。
- 空單：短期空單股數 1.45M，占流通股 0.38%，days to cover 1.1，空方壓力很低。

## Valuation

**市場報價**
- 收盤（2026-10-21）USD 1,676.69；前一日（10-20）收盤 USD 1,630.84，日變動 +2.8%
- 50 日均線 USD 1,733.25（價格低於 50 日 3.3%）；200 日均線 USD 1,584.68（價格高於 200 日 5.8%）
- 52 週區間 USD 946.11 – 1,999.96，現價距高點 −16.2%，52 週漲幅 +65.8%
- `info.beta` 1.302
- 注意：`info.fulldayPrice` 為 1,629.83，與歷史快取 10-21 收盤 1,676.69 不一致，本報告以歷史快取為準。

**估值倍數**
- 市值（info，USD）646.2B；流通股約 385.4M
- Trailing P/E 41.3x（TTM EPS USD 40.64）；Forward P/E 26.7x（forward EPS USD 62.79）；PEG 0.92
- EV（自算）≈ 市值 646.2B − 淨現金（info totalCash 12,735.1M − totalDebt 1,963.0M = 10,772.1M USD）≈ USD 635.5B
- EV/EBITDA（TTM，info EBITDA USD 16.18B）≈ 39.3x（自算；info 的 enterpriseToEbitda 排除）
- P/FCF（TTM FCF USD 10.37B）≈ 62.3x；P/OCF（TTM OCF USD 22.73B）≈ 28.4x
- P/S（TTM 營收 USD 39.47B）16.4x
- P/B：info 的 1,440.8x 排除；以 Q2'26 股東權益 EUR 21,825M 估算，約 25–30x（需假設 EUR/USD 匯率，屬粗估）
- 分析師共識：17 位，推薦均值 1.37（strong_buy 區間）；rec_summary 目前 7 strongBuy / 31 buy / 2 hold / 1 sell / 0 strongSell
- 目標價：均值 USD 2,142.9（較現價 +27.8%）；中位數 2,301.0（+37.2%）；最高 2,846.8（+69.8%）；最低 866.6（−48.3%）

**估值評論**
- 絕對倍數偏高，TTM P/E 41x、P/FCF 62x、P/S 16x，明顯高於半導體設備同業估計中位數。
- 以 forward 口徑看（forward P/E 26.7x，PEG 0.92），估值較可接受，代表市場假設 EPS 持續大幅成長（forward EPS 較 TTM 高約 54%）。
- 近四季 EPS 持續超標：Q3'25 +2.1%、Q4'25 −2.7%、Q1'26 +8.0%、Q2'26 +9.1%、Q3'26 +9.9%（11.82 vs 預估 10.76）。

## Key catalysts
- **已發生**：2026-10-14 Q3'26 財報，EPS 11.82（預估 10.76，超標 +9.9%；對比 Q3'25 EPS 5.49，YoY 約 +115%）。此數字與 cache 財報尚未同步，**Q3'26 營收、毛利、訂單、客戶出貨分布 DATA_UNAVAILABLE**，需等 cache 更新後複核。
- **即將發生**：2026-10-27 除息，每股現金股息 USD 2.108（ex-date，屬 as-of 之後事件）。
- **下一次財報**：`earnings_dates` 顯示 2027-01-27，EPS 預估 15.39（日期為表列值，未確認為正式公告）。
- **指引（guidance）**：工具未提供 management guidance 原文，**DATA_UNAVAILABLE**。
- **營運資金追蹤**：Q2'26 AR 與 DSO 大增，需確認 Q3'26 收款是否回落；Q2'26 現金流量表補齊後可判斷負向 FCF 來源（應收、存貨或預付款轉換）。
- **資本回報節奏**：2025 買回金額大幅增加（EUR 5.95B），2026 H1 買回金額 DATA_UNAVAILABLE（Q2 缺）；股本由 393.3M 股降至 384.1M 股，後續買回規模是股東回報主要變數。
- **股價事件**：52 週區間寬（946–2,000），股價波動大（beta 1.30）。

## Red flags
- **營運現金流轉負**：Q1'26 OCF EUR −2,185.6M、FCF EUR −2,607.9M，FCF/NI 約 −0.95x；Q2'26 現金流量表缺漏，無法確認是否延續。
- **應收帳款快速上升**：AR 自 2025-12 的 EUR 3,023M 增至 2026-06 的 EUR 7,252.6M，DSO 由約 28 天升至約 71 天。
- **存貨水位高**：EUR 11.7B，約 278 天營業成本，有減值與週轉風險。
- **估值偏高**：TTM P/E 41x、EV/EBITDA 約 39x、P/FCF 約 62x、P/S 16x；倍數對景氣或訂單節奏變化的敏感度高。
- **資料不一致**：live 財報輸出與 cache 數值矛盾；`info` 中 EV、EV/EBITDA、P/B、bookValue 等欄位錯誤；`fulldayPrice` 與歷史收盤不一致。下游若直接使用 live 財報或 info 的 EV 類欄位，會得到錯誤結論。
- **財報落後**：cache 缺 Q3'26 完整財報與 Q2'26 現金流量表，最新財務狀況與 EPS 超標之間存在缺口。
- **內部人交易資料缺漏**：insider 回傳空陣列，無法確認內部人是否有買賣訊號。
- **股息與買回的現金壓力**：2025 股東回報占 FCF 約 77%；若 2026 FCF 持續為負，股東回報將依賴淨現金（目前約 EUR 5.6B）。
- **短期現金消耗**：2026 H1 現金減少約 EUR 5.7B（含還債約 EUR 2.4B），需追蹤 Q3 現金變化。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| Revenue FY2025 (EUR M) | 32,667.3 | +15.6% | n/a（估計同業營收成長約 +5–10%） | 強 |
| Revenue Q2'26 (EUR M) | 9,326.5 | +21.2% | n/a | 強 |
| Revenue 3Y CAGR 2022–2025 | 15.6% | n/a | n/a（估計 8–12%） | 優 |
| Gross margin FY2025 | 52.8% | +1.6pp | 約 45% | 優 |
| Operating margin FY2025 | 34.6% | +2.7pp | 約 25% | 優 |
| Net margin FY2025 | 29.4% | +2.6pp | 約 18% | 優 |
| ROE FY2025（平均股東權益） | 50.5% | +3.1pp（2024: 47.4%） | 約 20% | 優 |
| ROIC FY2025（估算，equity+debt 口徑） | 38.8% | +7.1pp（2024: 31.7%） | 約 15% | 優 |
| FCF margin FY2025 | 33.8% | +1.7pp | 約 15% | 優 |
| FCF / NI FY2025 | 1.15x | 2024: 1.20x | 約 0.9x | 健康 |
| FCF Q1'26（季） | EUR −2,607.9M | n/a | n/a | 警示 |
| 應收帳款 AR（Q2'26, EUR M） | 7,252.6 | +45%（Q2'25: 4,996.9） | n/a | 警示 |
| DSO（Q2'26，91 天估算） | 約 71 天 | 約 +12 天（Q2'25: 約 59 天） | 約 50–60 天（估計） | 警示 |
| 淨現金（Q2'26, EUR M） | 5,597.1 | +58%（Q2'25: 3,550.0） | n/a | 強 |
| Current ratio（Q2'26） | 1.33x | −0.10x（Q2'25: 1.43x） | 約 1.5–2.0x（估計） | 尚可 |
| Debt / Equity（Q2'26） | 9.1% | −11.9pp（Q2'25: 21.0%） | 約 30–50%（估計） | 強 |
| Capex / Revenue FY2025 | 5.0% | −2.4pp（2024: 7.4%） | 約 8%（估計） | 中性 |
| 股東回報 / FCF FY2025 | 77%（EUR 8,500M） | 2024: 33% | n/a | 中性 |
| 股利覆蓋率（FCF）FY2025 | 4.3x | n/a | n/a | 健康 |
| 股數變化 FY2025 | 385.4M | −2.0%（2024: 393.3M） | n/a | 正向 |
| 內部人淨買賣（6 個月） | DATA_UNAVAILABLE | n/a | n/a | 無法判斷 |
| Institutional ownership | 20.3%（2,971 家） | n/a | n/a | 分散 |
| Short interest / float | 0.38%（days to cover 1.1） | n/a | n/a | 低 |
| Trailing P/E（TTM） | 41.3x | n/a | 約 25–30x（估計） | 偏貴 |
| Forward P/E | 26.7x | n/a | 約 20–25x（估計） | 略貴 |
| PEG | 0.92 | n/a | n/a | 合理 |
| EV/EBITDA（TTM，自算） | 約 39.3x | n/a | 約 20x（估計） | 偏貴 |
| P/FCF（TTM） | 62.3x | n/a | 約 30–35x（估計） | 貴 |
| P/OCF（TTM） | 28.4x | n/a | n/a | 偏貴 |
| P/S（TTM） | 16.4x | n/a | 約 6–8x（估計） | 貴 |
| P/B（自算，匯率假設） | 約 25–30x | n/a | n/a | 貴（粗估） |
| Dividend yield | 0.54% | n/a | n/a | 低 |
| Analyst mean target | USD 2,142.9（+27.8%） | n/a | n/a | 市場共識偏多 |
| Beta | 1.30 | n/a | 約 1.2（估計） | 中性偏高 |
| Next earnings（表列） | 2027-01-27（EPS est 15.39） | n/a | n/a | 待確認 |

FUNDAMENTALS REPORT COMPLETE
