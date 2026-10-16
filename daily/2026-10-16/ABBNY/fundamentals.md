# Fundamentals — ABBNY (ABB Ltd ADR) as of 2026-10-16

資料說明: 價格與 info 欄位來自 repo 快取 (source: cache, cached_at 2026-10-16T11:11:49Z)，屬預期的快取回退。最新已報告季度為 2026-06-30 (Q2 2026)。本報告未發現 2026-10-16 之後的資料。金額以 USD 計，「億」= 1 億 USD，原始 JSON 為百萬 (M)。TTM 採 FY2025 年報加季度資料反推，Q3 2025 由年度減去 Q1、Q2、Q4 推算 (quarterly_fin 缺 2025-09 欄位)；反推之 TTM 營收 357.5億 與 info totalRevenue 35,752M 吻合，可信度高。

## Executive summary
ABB 財務體質健全: FY2025 營收 332.2億 (YoY +8.6%)、淨利 47.3億 (YoY +20.3%)、FCF 44.7億，FCF/NI 為 0.94，TTM 淨負債/EBITDA 約 0.6x，2026 上半年營收同比維持雙位數 (Q1 +18.3%、Q2 +14.2%)。估值明顯偏貴: trailing P/E 33.7x、自算 EV/EBITDA 約 24x、TTM P/FCF 34.4x，且近兩季 EPS 皆低於分析師預期 (Q1 -6.6%、Q2 -4.9%)。整體結論: 基本面品質佳、估值不便宜，後續需確認 Q3 財報是否延續 EPS miss 與毛利率同比下滑的趨勢。

## Revenue & profitability

**營收與成長**
- 年度營收: FY2022 294.5億、FY2023 322.4億、FY2024 305.8億、FY2025 332.2億 USD。
- YoY: FY2023 +9.5%、FY2024 -5.1%、FY2025 +8.6%。
- 3 年 CAGR (FY2022 至 FY2025): 約 4.1%。2021 年報表為 null，無法計算更長期 CAGR。
- 季度趨勢加速: Q2 2025 82.95億 → Q2 2026 94.75億 (YoY +14.2%)；Q1 2025 73.82億 → Q1 2026 87.34億 (YoY +18.3%)。Q4 2025 90.52億，Q3 2025 反推 84.91億。info revenueGrowth 0.142 與計算一致。
- TTM 營收 357.5億。
- 分部: info.longBusinessSummary 列出 Electrification、Motion、Automation 三大分部，工具未提供分部營收與占比，無法量化分部結構，判定為 DATA_UNAVAILABLE。

**獲利能力**
- 毛利率 (Gross Profit / Total Revenue): FY2022 33.0%、FY2023 34.8%、FY2024 39.2%、FY2025 41.1%，三年持續擴張。
- 但 2026 季度同比轉弱: Q1 2026 39.4% (Q1 2025 為 42.3%，-2.9pp)；Q2 2026 40.0% (Q2 2025 為 40.5%，-0.5pp)。TTM info grossMargins 為 40.2%。
- 營業利益率 (Operating Income / Revenue): FY2022 11.6%、FY2023 13.5%、FY2024 15.5%、FY2025 17.2%。Q2 2026 17.9% (Q2 2025 為 16.5%，+1.4pp)，營業層面仍在擴張。TTM info operatingMargins 16.9%。
- 淨利率: FY2022 8.4%、FY2023 11.6%、FY2024 12.9%、FY2025 14.3%。TTM info profitMargins 14.1%；Q2 2026 13.0%。
- EPS (稀釋): FY2025 2.59 (YoY +21.6%)；季度 Q1 2025 0.60、Q2 2025 0.63、Q3 2025 反推 0.66、Q4 2025 0.70、Q1 2026 0.73、Q2 2026 0.68。Q2 2026 EPS YoY +7.9%，淨利 YoY +7.0%，EPS 成長明顯慢於營收。
- ROE: info returnOnEquity 32.6% (TTM)；FY2025 以平均股東權益計 31.0%，以期末計 29.4%。
- ROIC (估算): FY2025 NOPAT = EBIT 63.05億 x (1 - 25.2% 稅率) 約 47.2億，除以平均投入資本 (2024 年 213.6億、2025 年 243.9億，平均 228.8億)，約 20.6%；若採 Operating Income 57.29億計算約 18.7%。

## Cashflow & balance sheet

**現金流品質**
- OCF: FY2022 12.9億、FY2023 42.9億、FY2024 46.8億、FY2025 54.7億。TTM OCF 59.05億 (與 info operatingCashflow 5,905M 一致)。
- Capex: FY2022 7.6億、FY2023 7.7億、FY2024 8.0億、FY2025 10.0億 (YoY +25.3%)，占營收 3.0% (FY2024 為 2.6%)。TTM Capex 10.3億。
- FCF (OCF - Capex): FY2023 35.2億、FY2024 38.8億、FY2025 44.7億；TTM 48.7億。FCF margin: FY2025 13.4%、FY2024 12.7%、TTM 13.6%。
- FCF / NI: FY2023 0.94、FY2024 0.99、FY2025 0.94、TTM 0.97，均高於 0.9 健康門檻。FY2022 僅 0.21 (當年 OCF 大幅下滑)，顯示現金流有週期性波動。
- OCF / NI: FY2025 1.16。
- 季度 FCF: Q1 2025 5.0億、Q2 2025 8.6億、Q3 2025 反推 15.7億、Q4 2025 15.4億、Q1 2026 8.5億、Q2 2026 9.1億。
- 資料不一致: info freeCashflow 為 1.57B，但該數字與反推的 Q3 2025 單季 FCF (1.57B) 完全相同，明顯是單季值誤植，TTM FCF 應為 48.7億。本報告採用報表推算值。

**資產負債表 (Q2 2026，2026-06-30)**
- 總資產 457.4億；流動資產 263.5億；流動負債 184.4億；股東權益 158.99億；現金與約當現金 38.7億；現金與短期投資 58.6億。
- 總債務: FY2025 90.9億；info totalDebt 91.5億 (最新)。
- 淨負債 (Yahoo Net Debt 定義): FY2024 26.1億、FY2025 36.6億、Q1 2026 48.7億、Q2 2026 43.1億。以 info totalDebt - totalCash 計約 32.9億，兩種定義差距約 10 億，判斷為定義差異 (租賃或其他負債)，本報告以 Yahoo Net Debt 43.1億為保守口徑。
- 淨負債/EBITDA: TTM 約 0.60x (43.1億 / 71.5億)，低槓桿。
- 流動比率: FY2025 1.56，Q2 2026 降至 1.43 (流動負債 2025 年底至 2026 年中增加 12.3%，流動資產僅增 3.0%)。速動比率 info quickRatio 0.82。
- 負債權益比: info debtToEquity 55.8% (約 0.56x)，與 Total Debt / 股東權益 (91.5 / 159.0 = 57.5%) 接近。
- 有形帳面價值: FY2025 53.3億，Q2 2026 51.9億。商譽 FY2025 為 96.4億，占總資產約 21%，減損風險需留意。

## Capital allocation & insider signal

**資本配置**
- 股利: FY2025 現金股利支出 19.1億 (FY2024 17.7億，+7.8%)；FY2025 股利占 NI 40.3%，info payoutRatio 43.4%。FCF / 股利 覆蓋 2.34x。
- 2026 上半年股利現金流出 21.6億 (Q1 16.1億、Q2 5.5億)，季度分布不規則，建議以年度數字判讀。
- 股利殖利率: info dividendYield 1.29%，5 年平均 1.89%。
- 回購: FY2025 普通股回購 15.0億 (FY2024 12.5億，+20%)，占目前市值約 0.9%。2026 上半年回購 4.7億 (Q1 2.5億、Q2 2.3億)。
- 股東回報合計 (股利 + 回購) FY2025 為 34.1億，占 FCF 約 76%，仍保留約 24% FCF 作再投資與去槓桿空間。
- 股數: 稀釋加權股數由 FY2022 19.10億降至 FY2025 18.31億 (年均約 -1.4%)，淨縮股效果明確。info sharesOutstanding 18.09億。
- 負債: FY2025 償還債務 4.3億、新增債務 10.8億；2026 年中淨負債較年底增加約 6.5億，槓桿小幅上升。

**內部人活動 (6 個月)**
- insider 工具回傳空清單，major_holders 之 insidersPercentHeld 為 0.0%、institutionsPercentHeld 為 0.2%。此為 OTC (PNK) ADR 的資料覆蓋不足，判定為 DATA_UNAVAILABLE，不可解讀為「內部人零交易」。
- info.companyOfficers 之 exercisedValue 與 unexercisedValue 皆為 0；CEO Morten Wierod FY2025 總薪酬 503.5萬 USD，屬薪酬資料而非交易訊號。
- 淨買賣金額與市值比: 無法計算 (DATA_UNAVAILABLE)。

## Valuation

以現價 92.68 USD (cache) 計算，市值 1,676.7億 USD，流通股數 18.09億:

- Trailing P/E: 33.7x (info trailingEps 2.75；季度加總 TTM EPS 約 2.77，P/E 約 33.5x)。
- Forward P/E: 25.3x (info forwardEps 3.66)。注意: 上半年 EPS 實績 1.41，若 forwardEps 為 FY2026 估計，則 H2 2026 需 EPS 約 2.25，遠高於 H2 2025 的 1.36，隱含成長幅度不合理，forward P/E 可信度低，建議以 trailing 與實際成長率交叉判讀。
- EV/EBITDA: info enterpriseValue 6,766.5億與 enterpriseToEbitda 94.7x 與市值及負債不符，判定為資料錯誤。自算 EV = 市值 1,676.7億 + 總債務 91.5億 - 現金 58.6億 + 少數股東權益 5.1億 = 約 1,714.7億；TTM EBITDA 71.5億，EV/EBITDA 約 24.0x。
- EV/Revenue (TTM): 約 4.8x。
- P/S (TTM): 4.69x (info priceToSalesTrailing12Months)。
- P/FCF: TTM 約 34.4x (FCF yield 2.9%)；FY2025 為 37.5x (FCF yield 2.7%)。
- P/B: info priceToBook 42.3x 所依據之 bookValue 2.19 與報表權益/股數 (約 8.76 USD/股) 不一致，判定為資料錯誤。以市值 / 股東權益計約 10.5x。
- PEG: info pegRatio 1.28。
- 價格位置: 52 週區間 67.24 - 110.20，現價距高點 -15.9%、距低點 +37.8%。fast_info 之 50/200 日均線為 null，判定為 n/a。
- 分析師: targetMeanPrice 93.32 USD (5 位分析師)，相較現價 +0.7%；recommendationKey 為 none，共識強度不足。
- 行業中位數 (估計): 以下為模型依一般認知之估計值，非工具資料，僅供量級參考: 電氣設備與自動化同業 trailing P/E 約 28x、forward P/E 約 22x、EV/EBITDA 約 16x、P/S 約 2.5x、P/FCF 約 30x。ABB 於多數估值指標上有 15% 至 100% 的溢價，但 ROE、ROIC、FCF margin 優於估計中位數，溢價有一定基本面支撐。

## Key catalysts

- 下一季財報 (Q3 2026): earnings_dates 最新紀錄為 2026-07-16 (Q2 2026 已報告)，工具資料中無 2026-10 之後的財報日，判定為 DATA_UNAVAILABLE。歷史 Q3 財報日為 2025-10-16、2024-10-17、2023-10-18、2022-10-20，慣例落在 10 月中旬，與本報告日期重疊，需以 IR 公告與當日新聞確認。
- 最近兩季盈餘: Q1 2026 EPS 0.73 vs 預估 0.78 (-6.55%)；Q2 2026 EPS 0.68 vs 預估 0.72 (-4.9%)。營收仍雙位數成長，但 EPS 未跟上，需確認是估計值過高或利潤率承壓。
- 盈餘歷史: 最近 9 季中 6 季 EPS 超預期，其中 2026 年兩季連續低於預期，為近期的負向轉折。
- 毛利率趨勢: 2026 年兩季毛利率同比下滑 (Q1 -2.9pp、Q2 -0.5pp)，與 FY2025 毛利率改善方向相反，為 Q3 財報的關鍵觀察點。
- Robotics 分部 (外部資訊，工具未涵蓋，需核實): info.longBusinessSummary 未提及 Robotics。依模型既有知識，ABB 曾於 2025 年宣布出售 Robotics 業務，交割時程與財務影響無法由工具資料驗證。若已完成剝離，FY2026 營收、毛利率與分部比較基礎都會改變，且本報告的歷史數字未反映 discontinued operations。
- 資本支出加速: FY2025 Capex 年增 25%，占營收由 2.6% 升至 3.0%，後續 FCF 轉換率需追蹤。
- 股東回報: 股利與回購節奏是否延續，直接影響股利覆蓋與淨負債變化。

## Metrics table

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| Revenue (FY2025) | 332.2億 USD | +8.6% | 約 +4% (估) | 優於 |
| Revenue growth (Q2 2026 MRQ) | 94.75億 USD | +14.2% | n/a | 優於 |
| Revenue growth (Q1 2026) | 87.34億 USD | +18.3% | n/a | 優於 |
| Revenue 3y CAGR (FY22-25) | 約 4.1% | n/a | 約 4% (估) | 持平 |
| Gross margin | 41.1% (FY2025) / 40.0% (Q2 2026) | FY +1.8pp / Q2 -0.5pp | 約 33% (估) | 優於，但 2026 季度下滑 |
| Operating margin | 17.2% (FY2025) / 17.9% (Q2 2026) | FY +1.7pp / Q2 +1.4pp | 約 13% (估) | 優於 |
| Net margin | 14.3% (FY2025) | +1.4pp | 約 9% (估) | 優於 |
| Diluted EPS | 2.59 (FY2025) / 0.68 (Q2 2026) | FY +21.6% / Q2 +7.9% | n/a | 成長放緩 |
| EPS surprise (last 2Q) | Q1 -6.55%, Q2 -4.9% | n/a | n/a | 警示 |
| ROE | 32.6% (TTM, info) / 31.0% (FY25 平均權益) | n/a | 約 13% (估) | 優於 |
| ROIC (估算) | 約 18.7%-20.6% (FY2025) | n/a | 約 10% (估) | 優於 |
| FCF margin | 13.4% (FY2025) / 13.6% (TTM) | FY +0.8pp | 約 9% (估) | 優於 |
| FCF / NI | 0.94 (FY2025) / 0.97 (TTM) | FY24 0.99 → FY25 0.94 | 約 0.85 (估) | 健康 (>0.9)，邊緣 |
| OCF / NI | 1.16 (FY2025) | n/a | n/a | 健康 |
| Current ratio | 1.43 (Q2 2026) | 1.56 (FY2025) | 約 1.5 (估) | 中性，略降 |
| Debt / Equity | 0.56x (info 55.8%) | n/a | 約 0.5x (估) | 中性 |
| Net debt / EBITDA | 約 0.60x (TTM) | 0.51x (FY2025) | 低於 1x 為低槓桿 | 健康 |
| Net debt (Yahoo 定義) | 43.1億 USD (Q2 2026) | 36.6億 (FY2025) | n/a | 小幅上升 |
| Trailing P/E | 33.7x | n/a | 約 28x (估) | 偏貴 |
| Forward P/E | 25.3x (info，可信度低) | n/a | 約 22x (估) | 偏貴，待確認 |
| EV/EBITDA (自算) | 約 24.0x (info 94.7x 為錯誤) | n/a | 約 16x (估) | 偏貴 |
| P/S (TTM) | 4.69x | n/a | 約 2.5x (估) | 偏貴 |
| P/FCF (TTM) | 約 34.4x (FY2025 為 37.5x) | n/a | 約 30x (估) | 偏貴 |
| P/B (自算) | 約 10.5x (info 42.3x 為錯誤) | n/a | 約 3x (估) | 偏貴 |
| FCF yield (TTM) | 2.9% | n/a | 約 3.3% (估) | 偏低 |
| Dividend yield | 1.29% (info) | 5 年平均 1.89% | 約 2% (估) | 中性 |
| Dividend payout (NI) | 40.3% (FY2025) / 43.4% (info) | n/a | 約 40% (估) | 健康 |
| FCF / dividends | 2.34x (FY2025) | n/a | n/a | 健康 |
| Capex / revenue | 3.0% (FY2025) | Capex +25.3% | 約 4% (估) | 投資加速 |
| Shareholder return / FCF | 76% (FY2025) | n/a | n/a | 健康 |
| Diluted share count | 18.31億 (FY2025) | -1.1% | n/a | 淨縮股 |
| Insider net activity (6 mo) | DATA_UNAVAILABLE (空清單) | n/a | n/a | 無法判定 |
| Analyst target (mean) | 93.32 USD (5 位) | 相對現價 +0.7% | n/a | 中性 |
| Next earnings date | DATA_UNAVAILABLE (歷史慣例 10 月中旬) | n/a | n/a | 待確認 |

註: 「Sector median (estimate)」為模型依一般認知之估計值，非工具資料，僅供量級參考。

## Red flags
- 估值偏貴: trailing P/E 33.7x、TTM P/FCF 34.4x、自算 EV/EBITDA 約 24x，對成長放緩的容錯率低。
- 盈餘連續 miss: Q1 2026 (-6.55%) 與 Q2 2026 (-4.9%) EPS 低於預期，且 Q2 EPS 0.68 低於 Q1 的 0.73；營收成長 (+14% 至 +18%) 與 EPS 成長 (+8%) 明顯背離。
- 毛利率同比下滑: Q1 2026 下降 2.9pp，Q2 下降 0.5pp，與 FY2025 改善趨勢相反。
- Q1 2026 淨利品質: 淨利與營業利益的落差需以年報或財報附註確認，本報告未逐項驗證非營業科目。
- 流動負債上升: Q2 2026 流動負債較 FY2025 增加 12.3%，流動比率由 1.56 降至 1.43。
- 淨負債上升: 年底 36.6億 → Q2 2026 43.1億 (Q1 峰值 48.7億)，主因 H1 股利與回購現金流出。
- 資本支出加速: FY2025 Capex 年增 25%，Capex/revenue 由 2.6% 升至 3.0%。
- 歷史 FCF/NI 波動: FY2022 FCF/NI 僅 0.21，現金流有週期性。
- 商譽比重: 商譽 96.4億 占總資產約 21%，若業務剝離或減損，帳面數字會有大幅調整。
- 工具端資料品質問題:
  - enterpriseValue (6,766.5億) 與市值不符，enterpriseToEbitda 94.7x 為錯誤。
  - bookValue 2.19 與報表股東權益/股數不符，priceToBook 42.3x 為錯誤。
  - info freeCashflow 1.57B 為單季值誤植，TTM FCF 應為 48.7億。
  - forwardEps 3.66 隱含的 H2 2026 EPS 不合理，forward P/E 可信度低。
  - info totalDebt - totalCash 約 32.9億，與 Yahoo Net Debt 43.1億定義不同。
  - quarterly_bs 之 Other Non Current Liabilities 在 2025-12 為 2.33億、2025-06 為 21.75億，序列跳動異常，需以年報為準。
  - quarterly_fin 與 quarterly_cf 缺少 2025-09 欄位，Q3 2025 數字為反推值。
- 交易所與流動性: 工具回傳 exchange 為 PNK (Pink, OTC)，平均成交量約 22.1 萬股、10 日均量約 19.9 萬股。ADR 流動性與資料覆蓋度有限，大額部位執行與資料判讀都需留意。
- 內部人與機構持股資料缺口: insider 空清單、institutionsPercentHeld 僅 0.2%，無法判斷內部人或機構的增減持方向。
- 分析師覆蓋: 僅 5 位分析師，recommendationKey 為 none，目標價 (93.32) 幾乎等於現價，缺乏上行共識。

FUNDAMENTALS REPORT COMPLETE
