# Fundamentals — 6274.TWO 台燿科技 (Taiwan Union Technology) as of 2026-11-06

資料來源: `pipeline/tools/yf.py 6274.TWO`，`"source": "cache"` (repo 快取 `prices/yf/6274.TWO.json`，cached_at 2026-11-06T14:08Z)。金額單位統一為 TWD，以 億 表示 (1 億 = 100,000,000 TWD)，全文不使用 B 或 M。標示 DATA_UNAVAILABLE 者為工具未回傳，未作估計。

## Executive summary
台燿科技 (6274.TWO) 2026 年損益面大幅改善: FY2025 營收 303.4億 (YoY +31.5%)，2026Q2 單季營收 143.01億 (YoY +110.9%)，營業利益率由 Q2'25 的 12.6% 升至 Q2'26 的 23.5%。現金流與營運資金明顯轉弱，FY2025 FCF 為 -13.91億 (FCF/NI -0.41)，2026 上半年 FCF 累計 -39.24億，應收帳款與存貨較 2025 年底分別增加 50% 與 36%；負債於 2026Q2 降至 65.46億 (2025 年底 84.45億)，但 2025 年配息 17.97億 高於當年營業現金流 5.96億。估值方面，以 info 之 trailing P/E 46.7x 看屬偏高，以 epsCurrentYear 40.91 計約 22.1x，股價 906 TWD 較 52 週高點 1920 下跌約 53%；工具資料內部存在多處不一致 (見 Red flags)，估值倍數僅供參考。

## Revenue & profitability

**營收成長**
- FY 營收 (億 TWD): FY2022 184.72 → FY2023 160.03 (YoY -13.4%) → FY2024 230.7 (YoY +44.2%) → FY2025 303.4 (YoY +31.5%)。
- 3 年 CAGR (FY2022–FY2025): 18.0%；2 年 CAGR (FY2023–FY2025): 37.7%。FY2021 資料為 null，無法計算 4–5 年 CAGR。
- 季度營收 (億 TWD): Q2'25 67.8 → Q3'25 80.63 → Q4'25 91.25 → Q1'26 100.54 → Q2'26 143.01。Q2'26 YoY +110.9%，QoQ +42.3%。Q1'25 資料為 null，Q1'26 YoY 為 n/a。
- 2026Q3 財報: earnings_dates 顯示 2026-10-28 已公布 Reported EPS 12.88，對預估 11.33 之 surprise +13.69%。但 quarterly_fin / quarterly_bs / quarterly_cf 僅到 2026-06-30，Q3'26 營收與損益明細 DATA_UNAVAILABLE。
- 業務組合: info `longBusinessSummary` 描述產品為高頻、超低損耗 CCL、預浸材 (prepreg)、PCB 及大量壓合服務，應用於射頻、高速數位、高密度互連 (HDI)、汽車與基板。工具未提供分部營收，segment 占比 DATA_UNAVAILABLE。

**獲利能力 (FY 與季度)**

| 期間 | 營收 (億) | 毛利率 | 營業利益率 | 淨利率 | 淨利 (億) |
|---|---|---|---|---|---|
| FY2022 | 184.72 | 18.4% | 8.1% | 6.8% | 12.61 |
| FY2023 | 160.03 | 19.7% | 8.9% | 5.1% | 8.23 |
| FY2024 | 230.7 | 23.2% | 14.4% | 11.3% | 26.04 |
| FY2025 | 303.4 | 22.7% | 14.3% | 11.2% | 34.09 |
| Q2'25 | 67.8 | 21.2% | 12.6% | 9.6% | 6.52 |
| Q3'25 | 80.63 | 23.8% | 15.7% | 12.4% | 10.03 |
| Q4'25 | 91.25 | 22.1% | 14.1% | 11.9% | 10.83 |
| Q1'26 | 100.54 | 25.2% | 18.2% | 12.5% | 12.60 |
| Q2'26 | 143.01 | 29.7% | 23.5% | 16.4% | 23.42 |

- FY2025 毛利 68.98億、營業利益 43.44億、稅前 45.19億、所得稅 11.09億 (有效稅率約 24.6%，與 tax rate for calcs 0.2455 一致)。
- 毛利率在 FY2025 略降 0.5 pt，但 2026 年季度毛利率連續上升，Q2'26 來到 29.7%。驅動因素 (產品組合、價格或稼動率) 工具未揭露，需以產業資料佐證。

**ROE / ROIC (依財報計算)**
- ROE FY2025: 淨利 34.09 / 平均股東權益 164.76 (2024 143.37 與 2025 186.14 平均) = 20.7%；FY2024 為 20.1%。info `returnOnEquity` 為 38.5% (TTM 基礎，與本節計算口徑不同，僅供參考)。
- ROIC FY2025 (近似): 營業利益 43.44 × (1 - 24.55%) = 32.77 億 NOPAT，除以平均投入資本 229.0 (2024 187.5 與 2025 270.6 平均) = 14.3%；以期末投入資本計為 12.1%。FY2024 為 15.5%。

## Cashflow & balance sheet

**現金流品質**

| 年度 | 營業現金流 (億) | 資本支出 (億) | FCF (億) | FCF margin | FCF/NI | OCF/NI |
|---|---|---|---|---|---|---|
| FY2022 | 23.26 | 3.85 | 19.41 | 10.5% | 1.54 | 1.84 |
| FY2023 | 11.20 | 6.34 | 4.85 | 3.0% | 0.59 | 1.36 |
| FY2024 | 6.77 | 12.00 | -5.23 | -2.3% | -0.20 | 0.26 |
| FY2025 | 5.96 | 19.87 | -13.91 | -4.6% | -0.41 | 0.17 |

- FCF/NI 遠低於 0.9 的健康門檻，且 FY2024 起連續為負。
- 季度: Q1'26 OCF -15.68 億、FCF -22.67 億；Q2'26 OCF -7.15 億、FCF -16.57 億。2026 上半年 OCF 合計 -22.83 億，FCF 合計 -39.24 億。
- 負值主因為營運資金膨脹: 應收帳款 (AR) 由 2025 年底 128.91 億升至 2026Q2 193.83 億 (+50.4%)；存貨由 74.05 億升至 100.77 億 (+36.1%)。以季營收換算的 DSO 約為 123 天 (Q2'26) 與 129 天 (Q4'25)，應收週轉天數大致持平，但絕對金額快速擴張，收款與存貨去化是後續需追蹤的重點。
- 2026Q2 淨利 23.42 億，但 OCF 為負，獲利轉現金的效率明顯落後。

**資產負債表 (期末)**

| 項目 | 2025-12-31 | 2026-06-30 | 變化 |
|---|---|---|---|
| Total debt (億) | 84.45 | 65.46 | -22.5% (2026Q1 高點 95.26) |
| Cash & equivalents (億) | 51.65 | 55.13 | +6.7% |
| Cash + STI (億) | 106.02 | 67.55 | -36.3% |
| Net debt, Yahoo 定義 (億) | 32.8 | 10.32 | 下降 |
| Stockholders' equity (億) | 186.14 | 241.54 | +29.8% |
| Total assets (億) | 397.41 | 469.43 | +18.1% |
| Current ratio (計算) | 2.21 | 2.05 | 仍高於 2 |
| Quick ratio (計算) | 1.71 | 1.51 | |
| Debt / Equity (計算) | 45.4% | 27.1% | 明顯下降 |

- 2026Q2 淨負債 (以 Yahoo 定義) 為 10.32 億，對 TTM EBITDA 比率約 0.1x (以 info EBITDA 126.1 億計約 0.08x)，槓桿不高。
- 利息保障倍數 FY2025: EBIT 46.07 億 / 利息費用 0.887 億 (約 8,868 萬 TWD) = 約 52x；2026Q2 為 EBIT 34.74 億 / 利息費用 0.468 億 = 約 74x。Interest expense 與 2025 年平均有息負債推算利率約 1.4%，屬低成本借款結構 (推算值，工具未直接提供利率)。
- 2025 年舉債 76.2 億 (Issuance of debt)，還款 9.6 億，淨借款顯著增加；2026Q2 還款 32.3 億，負債由高點回落。
- info 之 `currentRatio` 2.142、`quickRatio` 1.643、`debtToEquity` 39.8 與上表計算值不同，應為不同期間或口徑，已以季度資產負債表為準。

## Capital allocation & insider signal

**資本支出**
- 資本支出 (億): FY2022 3.85 → FY2023 6.34 → FY2024 12.00 → FY2025 19.87 (YoY +65.6%)。資本支出占營收由 2.1% 升至 6.5%。FY2025 折舊攤提 4.59 億，資本支出為折舊 4.3 倍，屬擴產期。
- 2026 上半年資本支出 16.43 億 (Q1 7.00、Q2 9.43)，占 H1 營收 243.55 億約 6.7%。

**股利與股本**
- 股利現金支出 (億): FY2022 13.47 → FY2023 10.77 → FY2024 10.90 → FY2025 17.97 (YoY +64.9%)。
- FY2025 股利支出 17.97 億為 OCF 5.96 億的約 3.0 倍，且 FCF 為負；股利實際由舉債與既有現金支應。FY2025 以 NI 計的現金配息率為 53%。
- info `dividendRate` 7.51 TWD、`dividendYield` 0.75% (以 906 計)、`payoutRatio` 0.3865 (TTM 口徑)。2026 季度 cash dividends 欄位為 null/0，當年度配息節奏 DATA_UNAVAILABLE。
- 買回 (buyback): 財報無 Repurchase 項目，判定無買回紀錄 (以工具欄位為準)。
- 股本 (百萬股): 2023 年底 271.18 → 2024 年底 275.97 → 2025 年底 288.70 → 2026Q2 288.78。2023 至 2025 股本增加約 6.5%，2025 年底至 2026Q2 持平。增資或轉換來源工具未揭露，DATA_UNAVAILABLE。發行股本現金收入極小 (2025 年 0.39 億)。

**內部人與機構持股**
- insider (近 6 個月交易): 工具回傳空陣列 `[]`，無法判斷淨買入或淨賣出。依規則不視為「無交易」，記為 DATA_UNAVAILABLE。
- info `companyOfficers` 之 exercisedValue / unexercisedValue 均為 0，無法由此推論。
- insidersPercentHeld 12.33%；institutionsPercentHeld 44.32%；institutionsFloatPercentHeld 50.55%；機構數 136。
- inst_holders 前幾大機構名單 DATA_UNAVAILABLE。
- 內部人淨買賣金額與市值之比: DATA_UNAVAILABLE。

## Valuation

**價格位置 (info / fast 快取)**
- 價格 906 TWD (較前收 1005 下跌 -9.85%，當日區間 905–928)。
- 市值 2,616 億 TWD；企業價值 (EV) 3,016 億 TWD。
- 52 週區間 377–1920 TWD，現價距高點 -52.8%，距低點 +140%。
- 50 日均線 1453.1 TWD (現價低於 -37.6%)，200 日均線 1185.8 TWD (現價低於 -23.6%)。
- beta 2.416，屬高波動股。

**倍數**

| 倍數 | 數值 | 計算基礎 |
|---|---|---|
| Trailing P/E | 46.7x | 906 / trailingEps 19.42 (info) |
| Current-year P/E (FY2026E) | 22.1x | 906 / epsCurrentYear 40.91 (info priceEpsCurrentYear 22.15) |
| Forward P/E | 10.4x | 906 / forwardEps 87.08，與 epsCurrentYear 不一致，不採信 |
| EV/EBITDA (info) | 23.9x | EV 3,016 億 / EBITDA 126.1 億 |
| P/S (TTM, info) | 5.1x | 市值 2,616 億 / 營收 514.3 億 |
| P/S (statement TTM, Q3'25–Q2'26) | 6.3x | 市值 2,616 億 / 營收 415.4 億 |
| P/FCF | n/a | TTM FCF 為負 (Q3'25–Q2'26 合計 -59.24 億) |
| P/B (info) | 9.6x | info priceToBook |
| P/B (2026Q2 計算) | 約 10.8x | BVPS 約 83.6 TWD (241.54 億 / 288.78 百萬股) |
| 股利殖利率 | 0.75% | info dividendYield |

- 同業中位數: 工具未提供，DATA_UNAVAILABLE。本報告不估計產業中位數，僅作絕對水準描述。
- 分析師: 15 家，recommendationMean 1.33 (strong buy)，rec_summary 最新期為 strongBuy 5 / buy 10 / hold 0 / sell 0。目標價 平均 2,323 / 中位 2,170 / 最高 3,515 / 最低 1,770 TWD，平均目標較現價 +156%。分析師目標價為外部觀點，不代表本報告結論。
- 估值解讀: 以 trailing 數字 (P/E 46.7x、EV/EBITDA 23.9x) 看估值偏高；以 FY2026E EPS 40.91 計 P/E 約 22x，且 2026 上半年實際 EPS 為 11.98 (Q1 4.22 + Q2 7.76)，加上 Q3'26 12.88 合計 24.86，若要達 40.91 則 Q4'26 需約 16.05，為推算值，需對照 Q4 實績。估值是否合理取決於 Q4 與 2027 獲利延續性。

## Key catalysts
- 已公布: 2026-07-29 Q2'26 EPS 7.76 (對預估 8.49，-8.61% miss，但季營收與毛利大幅高於 Q1)；2026-10-28 Q3'26 EPS 12.88 (對預估 11.33，+13.69% beat)。
- 下次財報日: DATA_UNAVAILABLE (info earnings 時間戳仍為 2025-07 附近，已過時)。台灣慣例之年報多於次年 3 月前後公布，屬推論，非工具資料。
- 配息: info exDividendDate 2026-04-16 (已過)；下次除息日 DATA_UNAVAILABLE。
- 營運面追蹤重點: (1) 應收與存貨是否於 Q4'26 開始回收；(2) 毛利率 29.7% 能否維持；(3) 資本支出 (2026 H1 16.43 億) 是否持續放大而需更多舉債；(4) 2026Q3 之營收與現金流明細補齊。
- 指引 (guidance): 工具未提供管理層指引，DATA_UNAVAILABLE。

## Metrics table

金額單位: 億 TWD (倍數與比率無單位)。Sector median 欄位工具未提供，全部標為 DATA_UNAVAILABLE，不估計。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| Revenue FY2025 (億 TWD) | 303.4 | +31.5% (FY2024 230.7) | DATA_UNAVAILABLE | 成長強 |
| Revenue Q2'26 (億 TWD) | 143.01 | +110.9% (Q2'25 67.8) | DATA_UNAVAILABLE | 成長強 |
| Revenue 3Y CAGR FY22–25 | 18.0% | n/a | DATA_UNAVAILABLE | 中等 |
| Gross margin FY2025 | 22.7% | -0.5 pt | DATA_UNAVAILABLE | 中等 |
| Gross margin Q2'26 | 29.7% | +8.5 pt (Q2'25 21.2%) | DATA_UNAVAILABLE | 改善 |
| Operating margin FY2025 | 14.3% | -0.1 pt | DATA_UNAVAILABLE | 良好 |
| Operating margin Q2'26 | 23.5% | +10.9 pt (Q2'25 12.6%) | DATA_UNAVAILABLE | 改善 |
| Net margin FY2025 | 11.2% | -0.1 pt | DATA_UNAVAILABLE | 良好 |
| ROE FY2025 (計算) | 20.7% | +0.6 pt (FY2024 20.1%) | DATA_UNAVAILABLE | 良好 |
| ROIC FY2025 (計算, 平均 IC) | 14.3% | -1.2 pt (FY2024 15.5%) | DATA_UNAVAILABLE | 中上 |
| FCF FY2025 (億 TWD) | -13.91 | 惡化 (FY2024 -5.23) | DATA_UNAVAILABLE | 弱 |
| FCF / NI FY2025 | -0.41 | 惡化 (FY2024 -0.20) | 健康門檻 >0.9 | 弱 |
| FCF H1'26 (億 TWD) | -39.24 | n/a | DATA_UNAVAILABLE | 弱 |
| Total debt 2026Q2 (億 TWD) | 65.46 | -22.5% vs 2025-12-31 | DATA_UNAVAILABLE | 改善 |
| Net debt 2026Q2 (億 TWD, Yahoo 定義) | 10.32 | 下降 (2025-12-31 32.8) | DATA_UNAVAILABLE | 可控 |
| Debt / Equity 2026Q2 | 27.1% | -18.3 pt (2025-12-31 45.4%) | DATA_UNAVAILABLE | 良好 |
| Current ratio 2026Q2 | 2.05 | -0.16 (2025-12-31 2.21) | DATA_UNAVAILABLE | 良好 |
| Interest coverage FY2025 (EBIT/利息) | 約 52x | n/a | DATA_UNAVAILABLE | 良好 |
| Capex FY2025 (億 TWD) | 19.87 | +65.6% (FY2024 12.00) | DATA_UNAVAILABLE | 擴產中 |
| Dividends paid FY2025 (億 TWD) | 17.97 | +64.9% (FY2024 10.90) | DATA_UNAVAILABLE | 無法由 FCF 支應 |
| Trailing P/E | 46.7x | n/a | DATA_UNAVAILABLE | 偏高 |
| Current-year P/E (FY2026E) | 22.1x | n/a | DATA_UNAVAILABLE | 依賴 Q4 兌現 |
| Forward P/E (info, 不一致) | 10.4x | n/a | DATA_UNAVAILABLE | 不採信 |
| EV/EBITDA (info) | 23.9x | n/a | DATA_UNAVAILABLE | 偏高 |
| P/S (TTM, info) | 5.1x | n/a | DATA_UNAVAILABLE | 偏高 |
| P/FCF | n/a (FCF 為負) | n/a | DATA_UNAVAILABLE | 不適用 |
| P/B (info) | 9.6x | n/a | DATA_UNAVAILABLE | 偏高 |
| Dividend yield | 0.75% | n/a | DATA_UNAVAILABLE | 偏低 |
| Insider net activity 6mo (金額 / 股數) | DATA_UNAVAILABLE (空陣列) | n/a | n/a | 無法判定 |
| Insiders % held | 12.33% | n/a | DATA_UNAVAILABLE | 中性 |
| Institutions % held | 44.32% (136 家) | n/a | DATA_UNAVAILABLE | 中性 |
| Analyst mean target (TWD) | 2,323 (+156% vs 906) | n/a | DATA_UNAVAILABLE | 外部觀點 |

## Red flags
- 現金流為負: FY2025 FCF -13.91 億、OCF 僅 5.96 億 (FCF/NI -0.41)；2026 上半年 FCF -39.24 億、OCF -22.83 億。
- 營運資金膨脹: 2026Q2 應收帳款 193.83 億 (較 2025 年底 +50.4%)、存貨 100.77 億 (+36.1%)，獲利與現金流出現背離。
- 股利超過現金來源: FY2025 股利支出 17.97 億為 OCF 之 3.0 倍，且 FCF 為負，股利由舉債與既有現金支應。
- 舉債擴張後回落: 2025 年舉債 76.2 億，2026Q1 總負債高點 95.26 億，2026Q2 降至 65.46 億；債務期限與利率結構 DATA_UNAVAILABLE。
- 工具資料不一致 (需對帳):
  - info `totalRevenue` 514.3 億與 `netIncomeToCommon` 85.4 億，明顯高於由季度報表推算之 TTM (營收 415.4 億、淨利 56.9 億)。info `mostRecentQuarter` 為 2026-09-30，且 earnings_dates 含 Q3'26 EPS 12.88，推測 info TTM 已納入 Q3'26，而 quarterly 報表尚未更新。
  - info `trailingEps` 19.42 與季度 EPS 加總不一致，本報告 trailing P/E 採 info 數字，僅供參考。
  - info `forwardEps` 87.08 與 `epsCurrentYear` 40.91 相差約 2.1 倍，forward P/E 10.4x 不採信。
  - info `bookValue` 93.95 TWD 與 2026Q2 股東權益計算之 BVPS 約 83.6 TWD 不一致。
  - info `debtToEquity` 39.8 與 2026Q2 計算值 27.1% 不一致。
- 估值偏高: trailing P/E 46.7x、EV/EBITDA 23.9x、P/B 約 9.6x–10.8x；估值的前提是 2026 Q4 與 2027 獲利延續，若毛利率由 29.7% 回落，倍數將重估。
- 股價大幅回落: 現價 906 TWD 較 52 週高點 1920 TWD 下跌約 53%，低於 50 日與 200 日均線；當日跌幅 -9.85%；beta 2.416。工具未揭露下跌原因，需由其他來源補充。
- 內部人與股東資料缺口: insider 空陣列、inst_holders 空陣列，無法驗證內部人買賣與主要機構動向。
- 股本增加: 2023 至 2025 年股本增加約 6.5%，來源 DATA_UNAVAILABLE，需確認是否涉及增資或可轉債。
- 資料異常: info `prevName` 為 "Old Bitcoin Erc"、`nameChangeDate` 為 2026-11-06，明顯為資料來源雜訊，不影響財務數字，但應視為快取品質問題。

FUNDAMENTALS REPORT COMPLETE
