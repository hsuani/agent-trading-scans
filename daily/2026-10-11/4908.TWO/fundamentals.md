# Fundamentals — 4908.TWO (前鼎 APAC Opto Electronics) as of 2026-10-11

## Executive summary
前鼎 (4908.TWO) 財務體質穩健: 2026-06-30 現金及短期投資 NT$1,217.9M、有息負債僅 NT$0.5M，淨現金約 NT$1,217M，流動比率 4.78，TTM 毛利率約 45%、淨利率約 21%。然而獲利在 2025 年明顯下滑 (EPS 由 2.81 降至 1.97，營收 YoY -13.0%)，2026 年 Q2 營收雖回升至 YoY +24%，但估值已遠高於基本面支撐 (trailing P/E 97.4x、EV/EBITDA 80.2x、P/B 10.7x，ROE 約 11.5%)，股價 52 週漲幅約 +196%。整體結論: 財務健康度佳，估值吸引力低，價格主要反映 2026 年以來的快速重估，基本面需更多季度驗證。

資料時點說明: 所有數據皆 ≤ 2026-10-11，無資料超出分析日期。最新可得股價 NT$243.5 為 regularMarketTime 換算之最近交易時點 (約 2026-10-08 收盤，台北時間)。yfinance 之 fast_info 來源為 cache (cached_at 2026-10-11T12:35 UTC)，Yahoo cookie/crumb 取得失敗，部分欄位以 info 為準。

## Revenue & profitability

**營收與成長**
- 年度營收 (NT$M): 2022 884.8 → 2023 941.4 → 2024 936.2 → 2025 814.7
- 2022-2025 3 年 CAGR: 約 -2.7%。2025 YoY: -13.0%。
- 季度營收 (NT$M): 2025Q2 205.8、2025Q3 213.7、2025Q4 182.9、2026Q1 265.4、2026Q2 255.3
- 2026Q2 vs 2025Q2 YoY: +24.0% (與 info revenueGrowth 0.24 一致)。2026Q1 與 2025Q1 因 quarterly_fin 資料為 null 無法比較。
- TTM 營收: NT$917.3M (與 info totalRevenue 917.3M 相符)。
- 業務組合: longBusinessSummary 描述為光纖傳輸元件 (光收發模組、銅纜收發器、AOC/DAC、TO-CAN OEM 等)，yfinance 未提供分部營收，segment mix 為 DATA_UNAVAILABLE。

**獲利能力**

| 年度 | 毛利率 | 營業利益率 | 淨利率 | Diluted EPS |
|---|---|---|---|---|
| 2022 | 44.8% | 26.0% | 29.5% | 3.29 |
| 2023 | 42.6% | 22.0% | 21.8% | 2.61 |
| 2024 | 44.4% | 21.7% | 23.5% | 2.81 |
| 2025 | 47.3% | 21.5% | 19.0% | 1.97 |

- 2025 毛利率回升 (+2.9pp) 但營業利益率持平，淨利率下滑 4.5pp，主因 2025 年 Other Non Operating 為 NT$-18.1M (2024 為 +31.8M)，且 2025Q2 單季 Other Non Operating 為 NT$-36.6M，單季淨利僅 NT$10.8M (淨利率 5.2%)，屬一次性或非營業項目影響，需在後續財報確認。
- 季度趨勢: 毛利率 2025Q2 45.9% / 2025Q3 42.3% / 2025Q4 46.4% / 2026Q1 46.9% / 2026Q2 45.6%，維持在 42-47% 區間。營業利益率 2026Q2 23.5%、2026Q1 24.7%，為近五季高點區間。
- 2026Q2 淨利 NT$52.2M，EPS 0.67 (2025Q2 為 0.14)。
- ROE: 2025 年末以年度淨利/平均權益計算約 9.0%；info returnOnEquity (TTM) 為 11.5%。
- ROIC (自算): 2025 NOPAT ≈ EBIT 177.9 × (1 - 稅率 13.1%) ≈ NT$154.5M，除以 Invested Capital NT$1,726.7M 約 8.9%。若扣除淨現金 (2025 年末 現金及短期投資 NT$1,146.2M)，營業資本約 NT$580M，ROIC 約 26.6%，顯示事業本身資本效率高、但帳上大量現金拉低整體 ROIC。

## Cashflow & balance sheet

**現金流品質**

| 年度 | OCF (NT$M) | Capex (NT$M) | FCF (NT$M) | FCF margin | FCF / NI |
|---|---|---|---|---|---|
| 2022 | 289.5 | 7.2 | 282.3 | 31.9% | 1.08 |
| 2023 | 151.4 | 19.8 | 131.7 | 14.0% | 0.64 |
| 2024 | 317.0 | 32.3 | 284.7 | 30.4% | 1.29 |
| 2025 | 213.0 | 31.5 | 181.5 | 22.3% | 1.17 |

- TTM (2025Q3 至 2026Q2) 由季度現金流加總: OCF NT$167.1M、Capex NT$26.0M、FCF NT$141.1M，FCF margin 15.4%，FCF / TTM NI (196.1) = 0.72，低於 0.9 健康門檻，主因 2025Q3 FCF 僅 NT$3.3M 與 2026Q1-Q2 營運資金增加。
- 注意: info freeCashflow 為 NT$26.5M，與季度加總的 NT$141.1M 不一致，本報告採用季度現金流表計算值，yfinance 口徑差異列入 Red flags。

**資產負債表 (2026-06-30 季末)**
- 現金及約當現金: NT$198.4M；現金及短期投資合計: NT$1,217.9M (與 info totalCash 相符)。2026Q2 現金下降主因購入投資 NT$230.0M (investing CF -259.5M)。
- 有息負債 (Total Debt): NT$0.5M (2026Q1 為 NT$0.04M)，實質為無負債。
- 淨現金: 約 NT$1,217M，約 NT$15.6/股 (以 78.2M 股計)。
- 流動比率: 4.78 (2026Q2)；速動比率 4.12 (info)。2025 年末流動比率 8.40，2026Q2 下降主因流動負債由 NT$186.8M 增至 NT$345.8M。
- 負債/權益: 約 0.03% (info debtToEquity 0.029)。
- 總負債: 2026Q2 NT$347.7M，較 2026Q1 NT$188.4M 大增約 85%，需於 Q3 財報釐清 (應付帳款、預收或其他流動負債)。
- 營運資金指標: 應收帳款 2026Q2 NT$199.6M (較 2025 年末 138.2M 增 44%)；存貨 NT$217.3M (較 2025 年末 182.3M 增 19%，較 2026Q1 170.6M 增 27%)。以季度 COGS 年化估算，存貨週轉天數約 143 天 (2025 年約 155 天)，應收帳款週轉天數約 71 天。存貨與應收帳款增速快於營收，為需追蹤的品質訊號。

## Capital allocation & insider signal

**資本配置**
- 資本支出: 2022 NT$7.2M → 2023 NT$19.8M → 2024 NT$32.3M → 2025 NT$31.5M；2025 Capex / 營收 3.9%，Capex / D&A (26.9M) 約 1.17，屬維持性加上小幅擴張。
- 股本: 2021-2026 股數持平 78.217M 股，無買回紀錄 (buyback 為 0)。
- 股利:
  - 2023 年現金股利 NT$234.7M，FCF NT$131.7M，覆蓋率 0.56x，當年以現金部位支應 (年末現金由 418.6M 降至 113.9M，2022 年末至 2023 年末)。
  - 2024 年現金股利 NT$187.7M，FCF 覆蓋率 1.52x。
  - 2025 年現金股利 NT$136.9M，佔 NI 約 89%，FCF 覆蓋率 1.33x。
  - info dividendRate 1.0 TWD/股，殖利率 0.41%，payoutRatio 0.70；5 年平均殖利率 2.32%。
  - 2026Q2 權益變動推算: 保留盈餘由 NT$907.1M 降至 NT$881.0M，NI 52.2M 下推算股利約 NT$78M，約合 NT$1.0/股，與 info 之 dividendRate 一致 (此為由資產負債表推算，非直接揭露)。
  - 2026 年 Q3 之實際現金股利支付資料 DATA_UNAVAILABLE。

**內部人與機構持股**
- insider (近 6 個月交易紀錄): 回傳為空陣列 [] ，淨買賣金額 DATA_UNAVAILABLE (空陣列不代表零交易，需以公開資訊觀測站確認)。
- companyOfficers 所列 exercisedValue / unexercisedValue 皆為 0。
- heldPercentInsiders 44.2%；institutionsPercentHeld 0.9%，機構 5 家，inst_holders 為空。
- 流通股數 45.8M 股 (約佔總股本 58.5%)，機構覆蓋度極低，市值 NT$19.0B 相對於 institutional 持股過低。

## Valuation

以 2026-10-08 收盤價 NT$243.5 計算 (市值 NT$19,046M，EV NT$17,828M)。

| 指標 | 數值 | 說明 |
|---|---|---|
| Trailing P/E | 97.4x | 以 TTM EPS 2.50 計 |
| Forward P/E | DATA_UNAVAILABLE | info 無 forward EPS，recommendationKey = none |
| EV/EBITDA | 80.2x | info enterpriseToEbitda，EBITDA 口徑 NT$222.3M |
| EV/EBITDA (季度加總自算) | 約 69x | 季度 EBITDA 加總 NT$258.3M，兩口徑差異見 Red flags |
| P/FCF (TTM) | 約 135x | 市值 / TTM FCF NT$141.1M |
| P/S (TTM) | 20.8x | info priceToSalesTrailing12Months |
| P/B | 10.7x | 每股淨值 NT$22.67 (info bookValue) |
| 股價位置 | 52 週區間 68.7-312.5 | 現價較 52 週高點 -22%，較 52 週低點 +254%，較 50 日均 +23.6%，較 200 日均 +55.6% |

- 估值判讀: 以歷史 EPS 看，2022 年 EPS 3.29，當前股價對應 2022 年 EPS 約 74x；2025 年 EPS 1.97，對應約 124x。在 ROE 約 9-11% 下，P/B 10.7x 需要極高的未來獲利成長才能合理化。
- 同業中位數 (估計，非 yfinance 資料): 台灣通訊設備 / 光通訊元件同業一般 trailing P/E 約 20-35x、EV/EBITDA 約 12-20x、P/S 約 2-5x、P/B 約 2-5x。本股各項估值倍數皆顯著高於估計同業中位數。

## Key catalysts
- 下一次財報日期: DATA_UNAVAILABLE。earnings_dates 僅回傳 2007-2015 歷史資料，無未來日期。依台灣上市櫃公司財報申報規定 (第三季財報需於季後 45 日內公告)，2026Q3 財報預期於 2026-11-14 前公告，此為規範推算，非 yfinance 資料。
- EPS 驚喜歷史: 歷史資料 (2007-2015) 波動大，最近可得 EPS 資料為 2025Q2 0.14、2025Q3 0.49、2026Q1 0.75、2026Q2 0.67，無 consensus estimate 比較。
- 近期營運訊號: 2026Q2 營收 YoY +24%、營業利益率回升至 23.5%；同時存貨與應收帳款顯著增加、總負債大增，後續 Q3 財報需確認是否為屬需求提前拉貨或收入認列時點所致。
- 股利: 2026 年 8 月之 NT$1.0 股利 (lastDividendDate 2026-08-20 附近) 已完成除息，後續股利政策與 Q3 盈餘相關。
- 指引 (guidance) 與分部變化: DATA_UNAVAILABLE (yfinance 不提供管理層指引；業務組合資料缺乏)。

## Red flags
- 獲利下滑: 2025 EPS 由 2.81 降至 1.97 (-29.9%)，營收 -13.0%，FCF -36.2%；2025 年 ROE 僅約 9%。
- 估值過高: trailing P/E 97.4x、EV/EBITDA 80.2x、P/B 10.7x，與 ROE 約 9-11% 不匹配。股價 52 週內由 68.7 升至 312.5 後回落至 243.5，波動極大。
- 營運資金惡化: 2026Q2 存貨 +27% QoQ (170.6 → 217.3)、應收帳款 +7% QoQ，存貨週轉天數仍高 (約 143 天)。
- 負債激增: 總負債 2026Q1 NT$188.4M → 2026Q2 NT$347.7M (+85%)，流動負債 +85%，需確認來源。
- FCF 品質: TTM FCF / NI 為 0.72，低於 0.9 門檻。2023 年股利覆蓋率僅 0.56x。
- 股利覆蓋: 2025 年股利約佔 NI 89%，若 2026 年獲利未回升，股利 (約 NT$1.0/股) 覆蓋將承壓。
- 資料口徑不一致: info freeCashflow NT$26.5M vs 季度加總 NT$141.1M；info EBITDA NT$222.3M vs 季度加總 NT$258.3M。本報告以季度表為準，需於 Q3 財報核對。
- 內部人與機構: insider 資料回傳為空 (DATA_UNAVAILABLE)，機構持股僅 0.9%，市場參與結構以散戶與內部人為主 (內部人 44.2%)。
- 2025Q2 單季一次性非營業損失 NT$36.6M，導致淨利率單季劇烈波動。
- 資料缺口: 分部營收、forward EPS、下一次財報日期、管理層指引、analyst 評等 (recommendationKey = none) 均為 DATA_UNAVAILABLE；台灣標的 yfinance 覆蓋度有限，部分欄位取自 cache。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 (TTM, NT$M) | 917.3 | 2026Q2 vs 2025Q2 +24.0%；FY2025 -13.0% | DATA_UNAVAILABLE | 成長不穩，年度下滑、近季回升 |
| 毛利率 (FY2025 / TTM) | 47.3% / 45.4% | FY +2.9pp | 約 30-40% (估計) | 高於估計同業，穩定 |
| 營業利益率 (FY2025 / 2026Q2) | 21.5% / 23.5% | FY -0.2pp；Q2 +1.7pp | 約 10-15% (估計) | 偏高，近季改善 |
| 淨利率 (TTM) | 21.4% | FY -4.5pp | 約 8-12% (估計) | 高，但受一次性項目影響 |
| Diluted EPS (FY2025) | 1.97 | -29.9% | DATA_UNAVAILABLE | 下滑 |
| ROE (TTM info) | 11.5% | FY2025 自算 9.0% | 約 10-15% (估計) | 中性偏弱 |
| ROIC (自算, 含現金 / 扣除淨現金) | 8.9% / 26.6% | DATA_UNAVAILABLE | DATA_UNAVAILABLE | 事業資本效率佳，帳上現金拉低整體 |
| FCF margin (TTM) | 15.4% | FY2025 22.3% (FY2024 30.4%) | 約 10-15% (估計) | 尚可，較前幾年下滑 |
| FCF / NI (TTM) | 0.72 | FY2025 1.17 | >0.9 健康 | 偏弱，低於門檻 |
| 淨現金 (NT$M, 2026Q2) | 1,217.4 | 2025 年末 1,146.1 (+6.2%) | 不適用 | 強勁 |
| 流動比率 (2026Q2) | 4.78 | 2025 年末 8.40 | 約 1.5-2.5 (估計) | 極佳，但較前期下降 |
| 負債/權益 | 約 0.03% | 2025 年末約 0.01% | 約 30-80% (估計) | 極低，無槓桿風險 |
| 總負債 (NT$M, 2026Q2) | 347.7 | QoQ +85% | DATA_UNAVAILABLE | 需追蹤 |
| 存貨 (NT$M, 2026Q2) | 217.3 | QoQ +27%；YoY (vs 2025Q2 173.1) +25% | DATA_UNAVAILABLE | 增速快於營收，警示 |
| 應收帳款 (NT$M, 2026Q2) | 199.6 | QoQ +7%；YoY (vs 2025Q2 146.9) +36% | DATA_UNAVAILABLE | 增速快於營收，警示 |
| Capex / 營收 (FY2025) | 3.9% | 2025 vs 2024 -2.5% | 約 3-6% (估計) | 正常 |
| 股利覆蓋 (FY2025, FCF/股利) | 1.33x | 2024 1.52x | >1.0 佳 | 尚可，但 NI 覆蓋僅約 1.13x |
| 股利殖利率 | 0.41% | 5 年平均 2.32% | 約 2-3% (估計) | 偏低 |
| Trailing P/E | 97.4x | DATA_UNAVAILABLE | 約 20-35x (估計) | 顯著偏高 |
| Forward P/E | DATA_UNAVAILABLE | DATA_UNAVAILABLE | 約 18-30x (估計) | DATA_UNAVAILABLE |
| EV/EBITDA | 80.2x | DATA_UNAVAILABLE | 約 12-20x (估計) | 顯著偏高 |
| P/FCF (TTM) | 約 135x | DATA_UNAVAILABLE | 約 15-30x (估計) | 顯著偏高 |
| P/S (TTM) | 20.8x | DATA_UNAVAILABLE | 約 2-5x (估計) | 顯著偏高 |
| P/B | 10.7x | DATA_UNAVAILABLE | 約 2-5x (估計) | 顯著偏高 |
| 股價 vs 52 週區間 | 243.5 (區間 68.7-312.5) | 52 週漲幅約 +196% | DATA_UNAVAILABLE | 位於區間中上段，波動大 |
| 內部人淨買賣 (近 6 月) | DATA_UNAVAILABLE | DATA_UNAVAILABLE | DATA_UNAVAILABLE | 無資料 |
| 機構持股比例 | 0.9% | DATA_UNAVAILABLE | 通常數十% (估計) | 極低，參與度不足 |
| 下次財報日期 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | 規範約 2026-11-14 前 (推算) | 需人工確認 |

FUNDAMENTALS REPORT COMPLETE
