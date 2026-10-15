# Fundamentals — NEE as of 2026-10-15

## Executive summary
NEE 的營收與獲利仍有成長動能（TTM 營收 28.70B、YoY +12.4%；FY2025 調整後 EPS 3.71、YoY +8.2%），但自由現金流極薄（TTM FCF 3.05B，僅覆蓋 TTM 股息 4.95B 的 0.62x），資本支出與股息需仰賴大量舉債與增資支應。槓桿與流動性是主要風險：總負債由 FY2022 的 64.97B 升至 Q2'26 的 110.20B，淨負債/EBITDA 約 6.1x–7.4x，TTM EBIT/利息約 3.0x，流動比率僅 0.53。估值方面，trailing / forward P/E 約 17.9x 屬公用事業合理區間，但 EV/EBITDA 19.3x、P/B 2.86x、P/FCF 53.6x 偏高，綜合判定為財務健康度中性偏弱、估值不便宜但未到極端。

資料時點說明：財務報表最新至 Q2'26（期末 2026-06-30）；股價為 2026-10-14 收盤快取值 78.37；內部人交易資料最新僅到 2026-03-13；下一個事件為 2026-10-21 的 Q3 2026 財報（尚未發生）。

## Revenue & profitability

**營收趨勢（USD，年度報表）**
- FY2022 20.96B → FY2023 28.11B（+34.2%）→ FY2024 24.75B（−12.0%）→ FY2025 27.41B（+10.7%）。
- 3 年 CAGR（FY2022–FY2025）= 9.4%；2 年 CAGR（FY2023–FY2025）= −1.2%；5 年 CAGR：DATA_UNAVAILABLE（FY2021 欄位為 null）。
- Q2'26 營收 7.53B，YoY +12.4%（Q2'25 為 6.70B）；Q1'26 營收 6.70B，因 Q1'25 季度資料缺失，無法計算 YoY。
- TTM 營收 28.70B（與 info totalRevenue 28.70B 一致），info revenueGrowth 為 +12.4%。
- 營收波動幅度大（FY2023 +34%、FY2024 −12%）。依 longBusinessSummary，NEE 含 NEER 批發市場、能源交易與天然氣等業務，營收波動性與此相關（推論，非工具直接數據）。

**分部與業務規模**
- 分部營收（FPL / NEER）：DATA_UNAVAILABLE（yfinance 未提供分部數字，僅有文字描述）。
- 截至 2025-12-31：淨發電容量約 35,963 MW；輸配電線路約 93,000 circuit miles；服務約 600 萬客戶帳戶（longBusinessSummary）。

**利潤率**

| 口徑 | FY2022 | FY2023 | FY2024 | FY2025 | TTM |
|---|---|---|---|---|---|
| 毛利率（Gross Profit / 營收） | 48.4% | 63.9% | 60.1% | 62.3% | 61.0% |
| 營業利益率（Operating Income / 營收） | 17.0% | 35.0% | 28.8% | 29.3% | 28.3% |
| 淨利率（NI to common / 營收） | 19.8% | 26.0% | 28.1% | 24.9% | 32.4% |

- TTM 營業利益率 28.3% 由季度加總計算；info operatingMargins 31.5% 為 Yahoo 自訂口徑，未採用。
- TTM 淨利率 32.4% 受 Q2'26 一次性因素推升（見下方 GAAP 與調整後 EPS 差異）。

**盈餘品質與 EPS**
- GAAP diluted EPS：FY2025 3.28（YoY −2.7%，FY2024 為 3.37）。
- 調整後 EPS（earnings_dates 的 Reported EPS，推定為共識口徑）：FY2025 合計 3.71（YoY +8.2%，FY2024 合計 3.43）。
- 最近四季調整後 EPS YoY：Q3'25 1.13（+9.7%，vs 1.03）、Q4'25 0.54（+1.9%，vs 0.53）、Q1'26 1.09（+10.1%，vs 0.99）、Q2'26 1.15（+9.5%，vs 1.05）。
- Q2'26 GAAP diluted EPS 1.50 高於調整後 EPS 1.15，價差 0.35 來自非經常項目：Gain on sale of security 293M、Earnings from equity interest 333M，以及 tax benefit −84M（quarterly_fin 欄位）。判定 GAAP 盈餘含一次性收益，應以調整後口徑看趨勢。

**ROE / ROIC**
- ROE：FY2025 12.5%（NI to common 6.835B ÷ 期末 common equity 54.61B）；TTM GAAP 約 16.3%（9.30B ÷ 57.13B，受 Q2 一次性因素推升）；info returnOnEquity 為 11.7%（Yahoo 口徑未明）。
- ROIC（推算，採 FY2025 有效稅率 25.57%）：FY2025 NOPAT ≈ 9.10B × (1 − 25.57%) = 6.77B；÷ Invested Capital 150.23B ≈ 4.5%。TTM 約 4.6%（10.45B EBIT 計算）。
- ROIC 低於一般公用事業 WACC 估計區間（約 6%–7%，為分析師估計），資本效率偏低，與高資本支出一致。

## Cashflow & balance sheet

**現金流量（USD）**

| 項目 | FY2022 | FY2023 | FY2024 | FY2025 | TTM（至 Q2'26） |
|---|---|---|---|---|---|
| Operating Cash Flow | 8.26B | 11.30B | 13.26B | 12.49B | 13.80B |
| Capital Expenditure | −9.74B | −9.55B | −8.51B | −9.27B | −10.76B |
| Free Cash Flow（OCF − Capex） | −1.48B | 1.75B | 4.75B | 3.21B | 3.05B |
| FCF margin | −7.1% | 6.2% | 19.2% | 11.7% | 10.6% |
| FCF / NI（common） | n/a | 24% | 68% | 47% | 33% |

- FCF / NI 門檻 > 0.9：FY2025（0.47）與 TTM（0.33）均未達標。
- OCF / NI（TTM）= 1.48，顯示營運現金流本身支撐，問題在於資本支出規模。
- Capex / D&A（FY2025）= 9.27 ÷ 6.94 = 1.34x；Capex / OCF：FY2025 74%、TTM 78%。
- info freeCashflow 為 −17.77B，與季度與年度現金流量表推算的 TTM FCF 3.05B 不一致，本報告採報表推算值，並將 info 值列為資料品質紅旗。

**資產負債表（Q2'26，期末 2026-06-30，USD）**
- Total debt 110.20B（YE2025 95.62B，6 個月 +15.2%；FY2022 64.97B，累計 +69.6%）。
- Current debt 11.41B（YE2025 6.06B）；Commercial paper 1.74B（Q1'26 為 5.36B）。
- Cash 2.87B；Net debt 107.33B（YE2025 92.81B，+15.7%；Q2'25 為 91.46B，YoY +17.3%）。
- 淨負債 / EBITDA：6.1x（報表 TTM EBITDA 17.70B）、6.4x（Normalized EBITDA 16.65B）、7.4x（info EBITDA 14.59B）。
- Total debt / 總權益（含 NCI 68.16B）= 1.62x（Yahoo 161.7%）；Total debt / common equity（57.13B）= 1.93x。
- 流動比率 0.53（15.47B ÷ 28.97B），YE2025 為 0.60；quick ratio 0.35（info）；Working capital −13.51B。
- 利息保障（EBIT / 利息）：TTM 2.98x（10.45B ÷ 3.51B）；FY2025 1.99x（9.10B ÷ 4.57B）。Yahoo 季度與年度利息資料不完全一致，以年度值作保守參考。
- Net PPE 170.45B（FY2022 為 111.06B）；Total assets 232.81B；Total liabilities 164.65B；Goodwill 及無形資產 5.15B。
- 結論：負債擴張速度快於 EBITDA 成長，短期債務占比上升（Current debt 由 YE2025 的 6.06B 升至 11.41B），再融資與利率風險需持續追蹤。

## Capital allocation & insider signal

**股息與股東回報**
- 現金股息支付：FY2022 3.35B、FY2023 3.78B、FY2024 4.24B、FY2025 4.68B（YoY +10.5%）；TTM 4.95B。
- 每股股息：trailing 2.379（trailingAnnualDividendRate）；最近一季 0.623；股息殖利率 3.19%（5 年平均 2.48%）；payout ratio 53.5%（info）。
- 股息覆蓋：TTM OCF / 股息 = 2.79x；TTM FCF / 股息 = 0.62x；FY2025 FCF / 股息 = 0.69x。
- 資金缺口：FY2025 OCF 12.49B − Capex 9.27B − 股息 4.68B = −1.47B，由淨借款 13.72B 與股權發行 2.04B 支應。
- 買回：現金流量表無 repurchase 項目，本期視為無買回（資料顯示）。

**股本稀釋**
- 股權發行（Issuance of capital stock）：FY2022 1.51B、FY2023 4.51B、FY2024 0.05B、FY2025 2.04B（其中 Q3'25 為 2.01B）。
- 流通股數：FY2022 1,987M → FY2025 2,083M → Q2'26 2,085.3M，自 FY2022 累計 +4.9%，YoY（Q2'25 2,059.3M）+1.3%。

**內部人交易（最近 6 個月）**
- 2026-04-15 至 2026-10-15 之區間：快取最新紀錄為 2026-03-13，此區間資料 DATA_UNAVAILABLE。
- 可得期間（2025-10 至 2026-03）公開市場賣出（Text 為 Sale）合計約 USD 31.98M，買入 0 筆。
- 其中 2026-02 至 2026-03 賣出合計約 USD 16.99M，包括 CEO Ketchum 2026-02-09 賣出 99,603 股（約 USD 8.90M），同日行使選擇權 99,603 股；Director Pimentel 2025-11-17 賣出 145,140 股（約 USD 12.18M），亦伴隨選擇權行權。多數賣出與選擇權行權相關，屬例行性質。
- 規模：USD 31.98M ÷ 市值 163.45B ≈ 0.02%；內部人持股比例 0.117%（約 2.44M 股）。
- 判定：賣出規模相對市值極小，無內部人買入，訊號中性偏弱，不構成顯著警訊。

**機構持股**
- 機構持股比例 87.0%，機構數 3,839。前幾大持股：BlackRock 8.96%（較前期 +4.5%）、Vanguard Capital Management 6.53%、State Street 5.70%、JPMorgan 5.56%（+3.6%）、Morgan Stanley 3.04%。Norges Bank 較前期 −8.5%。

**空頭部位**
- Short interest 59.32M 股，占流通股 2.85%，short ratio 4.93 日；前一期 49.84M，增加 +19.0%（資料日期約 2026-09-30）。

## Valuation

**股價與區間**
- 價格 78.37（2026-10-14 收盤快取；盤前 79.24 為 2026-10-15 盤前資料，未採用）。
- 52 週區間 74.41–98.75：現價距 52 週低點 +5.3%，距高點 −20.6%；52 週漲跌 −8.6%，同期 S&P 500 +15.7%（info SandP52WeekChange）。
- 50 日均線 81.39（現價低 3.7%）；200 日均線 87.30（現價低 10.2%）。
- 市值 163.45B；EV 281.83B；流通股 2,085.6M；Beta 0.64。

**估值倍數**
- P/E（trailing，GAAP 口徑）17.85x（info；78.37 ÷ 4.39）。以四季 GAAP diluted EPS 加總 4.45 計算為 17.6x。
- P/E（trailing，調整後口徑，TTM 3.91）：約 20.0x。
- Forward P/E 17.91x（forwardEps 4.376）；以 FY2026 共識 EPS 4.02 計算為 19.5x（priceEpsCurrentYear 19.50）。
- PEG 1.60（Yahoo pegRatio）。
- EV/EBITDA 19.3x（info，EBITDA 14.59B）；若以報表 TTM EBITDA 17.70B 計算為 15.9x，以 Normalized EBITDA 16.65B 計算為 16.9x。
- P/FCF（TTM）= 163.45 ÷ 3.05 = 53.6x。
- P/S（TTM）5.70x（info）；EV/Revenue 9.82x。
- P/B 2.86x（bookValue 27.39）。

**分析師共識（19 位）**
- recommendationMean 1.86（對應 buy）；目標價平均 97.00（+23.8%）、中位數 100（+27.6%）、最高 114（+45.5%）、最低 56（−28.5%）。

**與同業中位數比較**
- 同業中位數為分析師估計值（非工具回傳，DATA_UNAVAILABLE 於工具層）。以美國受監管電力公用事業的一般經驗區間估計：P/E 約 16x–18x、EV/EBITDA 約 12x–14x、P/B 約 1.8x–2.2x、股息殖利率約 3.5%–4.0%、ROE 約 9%–11%、淨負債/EBITDA 約 5x–6x。
- 判定：Forward P/E 位於或接近估計區間；EV/EBITDA、P/B、P/S、P/FCF 高於估計區間。估值不屬便宜，但分析師目標價中位數顯示市場共識認為有修復空間（分析師估計偏樂觀的可能性需自行評估）。

## Key catalysts
- **2026-10-21 Q3 2026 財報**（Yahoo 時間戳，isEarningsDateEstimate = false）。Q3 EPS 共識 1.17，對比 Q3'25 調整後 EPS 1.13，預估 YoY +3.5%。
- **財報歷史表現**：earnings_dates 列出的 24 季（2020-10 起）皆為 EPS beat；最近 8 季平均 surprise +4.3%；Q2'26 surprise +3.8%。
- **股息**：最近一次除息日約 2026-08-28，每季 0.623。下一次除息日：DATA_UNAVAILABLE。
- **公司財測（guidance）**：DATA_UNAVAILABLE（工具未提供）。
- **分部結構變化**：分部財務數字 DATA_UNAVAILABLE；文字描述顯示業務涵蓋 FPL 受監管電力與 NEER 再生能源、儲能、天然氣基礎設施。
- **債務再融資**：Current debt 11.41B（Q2'26），到期與 CP 滾動安排 DATA_UNAVAILABLE；需追蹤 2026 下半年融資成本。
- **股權發行**：2025 Q3 發行 2.01B；後續增資計畫 DATA_UNAVAILABLE。

## Metrics table

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 TTM（USD） | 28.70B | +12.4%（info；Q2'26 YoY +12.4%） | n/a（公用事業營收波動不具可比性） | 成長動能正面 |
| 營收 FY2025 | 27.41B | +10.7% | n/a | 正面，但波動大 |
| 營收 3 年 CAGR（FY22–25） | 9.4% | n/a | n/a | 中性偏正面 |
| 毛利率 TTM | 61.0% | FY25 62.3% vs FY24 60.1%（+2.2pp） | n/a（口徑不可比） | 中性 |
| 營業利益率 TTM | 28.3% | FY25 29.3% vs FY24 28.8%（+0.5pp） | 約 20%–30% | 中性偏正面 |
| 淨利率 TTM | 32.4% | FY25 24.9% vs FY24 28.1%（−3.2pp） | 約 10%–15% | 含一次性收益，判定偏正面但不可持續 |
| 調整後 EPS FY2025 | 3.71 | +8.2% | n/a | 正面 |
| GAAP diluted EPS FY2025 | 3.28 | −2.7% | n/a | 中性偏弱 |
| ROE | 12.5%（FY25） | TTM GAAP 16.3%；info 11.7% | 約 9%–11% | 略高於估計區間，含一次性因素 |
| ROIC（推算） | 約 4.5%–4.6% | n/a | 約 5%–6% | 偏低 |
| FCF TTM | 3.05B | FY25 3.21B vs FY24 4.75B（−32.3%） | n/a | 偏弱 |
| FCF margin TTM | 10.6% | FY25 11.7% vs FY24 19.2% | n/a | 偏弱 |
| FCF / NI（TTM） | 0.33 | FY25 0.47 | 門檻 > 0.9 | 不達標 |
| OCF TTM | 13.80B | FY25 12.49B（−5.8%） | n/a | 正面 |
| Capex TTM | 10.76B | FY25 9.27B（+8.9%） | n/a | 高投資期 |
| 淨負債（Q2'26） | 107.33B | YoY +17.3% | n/a | 偏高 |
| 淨負債 / EBITDA | 6.1x–7.4x | n/a | 約 5x–6x | 偏高 |
| Total debt / 總權益 | 1.62x（Yahoo 1.62x） | 較 YE25 升高 | 約 1.2x–1.6x | 偏高 |
| 流動比率 | 0.53 | YE25 0.60 | 約 0.8x–1.0x | 偏低 |
| EBIT / 利息（TTM） | 2.98x | FY25 1.99x | 約 2.5x–3.5x | 偏低 |
| 股息殖利率 | 3.19% | 5 年平均 2.48% | 約 3.5%–4.0% | 略低於估計區間 |
| 股息覆蓋（FCF / 股息，TTM） | 0.62x | FY25 0.69x | 約 0.8x–1.0x（估計） | 不足，需舉債支應 |
| 股息覆蓋（OCF / 股息，TTM） | 2.79x | n/a | n/a | 正面 |
| 股息成長（FY25 現金股息） | 4.68B | +10.5% | n/a | 正面 |
| 流通股數（Q2'26） | 2,085.3M | YoY +1.3%；自 FY22 +4.9% | n/a | 輕度稀釋 |
| 內部人交易（2025-10 至 2026-03） | 賣出約 USD 31.98M，買入 0 筆 | 2026-04 至 10 月：DATA_UNAVAILABLE | n/a | 中性偏弱，規模小 |
| 機構持股比例 | 87.0% | n/a | n/a | 中性 |
| 空頭比例（占流通股） | 2.85%（4.93 日） | 前期 +19.0%（股數） | n/a | 中性偏警示 |
| P/E trailing（GAAP） | 17.85x | n/a | 約 16x–18x | 合理 |
| P/E trailing（調整後） | 約 20.0x | n/a | 約 16x–18x | 略偏高 |
| P/E forward | 17.91x | n/a | 約 16x–18x | 合理 |
| EV/EBITDA | 19.3x（info）；15.9x–16.9x（報表 / normalized） | n/a | 約 12x–14x | 偏高 |
| P/FCF（TTM） | 53.6x | n/a | 不具可比性（資本支出高） | 偏高 |
| P/S（TTM） | 5.70x | n/a | 約 2.5x–4.0x | 偏高 |
| P/B | 2.86x | n/a | 約 1.8x–2.2x | 偏高 |
| PEG | 1.60 | n/a | n/a | 中性 |
| 股價 vs 52 週區間 | 78.37（距低 +5.3%、距高 −20.6%） | 52 週 −8.6% vs S&P +15.7% | n/a | 弱勢 |
| 股價 vs 200 日均線 | 低 10.2%（87.30） | n/a | n/a | 弱勢 |
| Beta | 0.64 | n/a | 約 0.6–0.8 | 低波動 |
| 分析師目標價平均 | 97.00（+23.8%） | n/a | n/a | 共識正面（19 位） |
| 分部營收 | DATA_UNAVAILABLE | n/a | n/a | n/a |
| 公司財測 guidance | DATA_UNAVAILABLE | n/a | n/a | n/a |

## Red flags
- **自由現金流不足以覆蓋股息**：TTM FCF 3.05B 對 TTM 股息 4.95B，覆蓋率 0.62x；FY2025 OCF − Capex − 股息 = −1.47B，缺口由舉債與增資補足。
- **負債快速擴張**：Total debt 自 FY2022 的 64.97B 增至 Q2'26 的 110.20B（+69.6%）；6 個月內淨負債增加 14.5B（+15.7%）；Q2'26 單季淨負債增加 4.9B（Q1 102.41B → Q2 107.33B）。
- **利息保障與流動性偏弱**：TTM EBIT/利息 2.98x，FY2025 為 1.99x；流動比率 0.53；Current debt 半年內由 6.06B 增至 11.41B。
- **盈餘品質**：Q2'26 GAAP EPS 1.50 高於調整後 EPS 1.15，含 Gain on sale of security 293M、equity earnings 333M 與 tax benefit −84M；TTM GAAP 淨利率 32.4% 不宜外推。FY2025 GAAP EPS 較 FY2024 下降 2.7%。
- **股本稀釋**：自 FY2022 流通股增加 4.9%，FY2025 發行股權 2.04B，為資本支出與股息的部分資金來源。
- **估值溢價**：EV/EBITDA 19.3x、P/B 2.86x、P/S 5.70x 高於公用事業估計區間。
- **股價趨勢弱勢**：現價低於 50 日與 200 日均線；52 週績效 −8.6%，落後 S&P 500 約 24 個百分點；空頭部位 +19.0%（前期比較）。
- **資料品質問題（Yahoo info 與報表不一致）**：info freeCashflow −17.77B vs 報表推算 TTM FCF +3.05B；info operatingMargins 31.5% vs 報表推算 28.3%；Net income 分解中 Minority interest 符號與 NI to common 之關係不一致。本報告以報表推算值為主，info 值僅作參考。
- **資料缺口**：FY2021 欄位全部為 null（無法計算 5 年 CAGR）；Q1'25 季度資料缺失（無法計算 Q1'26 YoY 與 TTM 前期比較）；內部人交易資料最新僅到 2026-03-13；分部營收與公司財測 DATA_UNAVAILABLE。

## 資料來源與限制
- 工具：pipeline/tools/yf（NEE info、financials、quarterly_fin、balance_sheet、quarterly_bs、cashflow、quarterly_cf、earnings_dates、insider、major_holders、inst_holders、fast_info）。全部結果標記 source = cache（快取），屬預期內。
- Yahoo 即時連線失敗（ConnectionError / 403），fast_info 之 50/200 日均線與 market_cap 等欄位為 null，改採 info 欄位（fiftyDayAverage、twoHundredDayAverage）。
- 同業中位數為分析師估計區間，非工具回傳資料。
- 所有財務數字單位為 USD，除特別標示外為 Yahoo 報表原始值經換算的 B（十億）或 M（百萬）。
- 本報告僅為基本面分析，不含交易建議。

FUNDAMENTALS REPORT COMPLETE
