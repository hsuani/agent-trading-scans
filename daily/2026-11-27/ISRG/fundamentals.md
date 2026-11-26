# Fundamentals — ISRG (Intuitive Surgical, Inc.) as of 2026-11-27

資料說明: 價格為 cache 2026-11-26 (cnyes feed, source=cache, 屬正常)。財報為 FY2025 年度 (2025-12-31) 與 2026 Q1–Q3 季度 (最新至 2026-09-30)。TTM 以最近四季加總計算。單位: 美元 (USD), 大數以 B (十億美元) 表示, 季度以 M (百萬美元) 表示, 每股以 USD 表示。本報告未使用台幣或韓圜單位。

## Executive summary
ISRG 財務體質極佳: 無負債、現金與短期投資 USD 4.04B、流動比率 3.33, FY2022–FY2025 營收 CAGR 約 17.4%, Q3 2026 營業利益率升至 34.2%。估值明顯偏貴, trailing P/E 51.7x、EV/EBITDA 32.2x、P/S 12.8x, 遠高於醫療器材類股一般水準 (估計值, 見估值段)。Q3 2026 GAAP 淨利 USD 523M 年減 25.8%, 主因是工具資料中可見的 "Other Income Expense" -USD 450M 非營業項目, 其成因工具資料未提供 (DATA_UNAVAILABLE), 需在下一步研究中釐清。

## Revenue & profitability

**營收 (USD B)**
| 期間 | 營收 | YoY |
|---|---|---|
| FY2022 | 6.22 | n/a |
| FY2023 | 7.12 | +14.5% |
| FY2024 | 8.35 | +17.2% |
| FY2025 | 10.06 | +20.5% |
| TTM (至 Q3 2026) | 11.58 | n/a |

- 3 年 CAGR (FY2022→FY2025): 約 17.4%。工具只提供 4 個年度資料, 無法計算 5 年 CAGR (DATA_UNAVAILABLE)。
- 季度趨勢: Q3 2025 USD 2,505.1M → Q4 2025 2,866.2M → Q1 2026 2,770.8M → Q2 2026 2,892.3M → Q3 2026 3,048.7M, Q3 年增 +21.7%。TTM 11.578B 與 info 的 totalRevenue 11,578M 吻合。
- 分部營收 (da Vinci 與 Ion 等): yfinance 未提供分部拆分, 僅能從 info.longBusinessSummary 得知產品線為 da Vinci 手術系統、Ion 內視鏡系統與耗材/服務, 分部營收 DATA_UNAVAILABLE。

**利潤率趨勢**
| 指標 | FY2022 | FY2023 | FY2024 | FY2025 | Q3 2025 | Q3 2026 |
|---|---|---|---|---|---|---|
| Gross margin | 67.4% | 66.4% | 67.5% | 66.0% | 66.4% | 68.4% |
| Operating margin | 25.3% | 24.8% | 28.1% | 29.3% | 30.3% | 34.2% |
| Net margin (common) | 21.3% | 25.2% | 27.8% | 28.4% | 28.1% | 17.1% |

- Operating margin 持續擴張: FY2025 29.3%, TTM 約 32.3% (TTM 營業利益 USD 3,734.1M), Q3 2026 季增至 34.2%。Q3 2026 營業利益 USD 1,042.6M, 年增 +37.2%。
- Gross margin: 2026 年季度由 66.1% (Q1) 升至 68.4% (Q3), 但 FY2025 整年仍低於 FY2024 約 1.5 個百分點, 其原因工具資料未說明 (DATA_UNAVAILABLE)。
- R&D 占營收: FY2025 13.0% (USD 1,311.8M); Q3 2026 13.4%。SG&A 占營收: FY2025 23.7%; Q3 2026 20.8% (Q3 2025 為 22.9%), 顯示規模效應。
- Net margin 異常: Q3 2026 淨利 USD 522.8M (Q2 2026 為 818.1M), 較 Q2 下降 36%, 同時營業利益還升 7%。差異來自營業利益以下: 利息收入 USD 75.8M, 其他非營業項目 -USD 450.0M, 稅前利潤 USD 668.4M, 稅率 21.5%。若把 -450M 加回, 稅前約 USD 1,118M (本報告推算值, 非工具數據)。
- ROE 17.9% (info, TTM); ROIC 估計約 14.9% (推算: FY2025 EBIT 2,945.5M × (1 − 稅率 13.1%) ÷ 平均 invested capital 17,129M)。

**EPS 與盈餘驚喜**
- GAAP 稀釋 EPS: FY2025 USD 7.87 (FY2024 6.42, +22.6%); Q3 2026 USD 1.49 (Q3 2025 1.95, 年減 23.6%); TTM 8.27 (與 info trailingEps 吻合)。
- 驗算: FY2025 淨利 USD 2,856.0M ÷ 稀釋股數 362.7M ≈ USD 7.87, 與 EPS 一致。
- Yahoo earnings_dates 記載的 Q3 2026 Reported EPS 為 USD 3.00 (consensus 2.64, 驚喜 +13.6%), 該數字應為非 GAAP 基礎, 與 GAAP 1.49 的差距即為 -450M 非營業項目與其他調整。兩者口徑差異需於報告中分開標示。
- 近 10 次財報 EPS 驚喜皆為正, 平均約 +14.6% (依 earnings_dates 資料計算)。

## Cashflow & balance sheet

**現金流 (USD M 為主)**
| 指標 | FY2022 | FY2023 | FY2024 | FY2025 | TTM |
|---|---|---|---|---|---|
| Operating CF | 1,490.8 | 1,813.8 | 2,415.0 | 3,030.5 | 4,089.5 |
| Capex | -532.4 | -1,064.2 | -1,111.2 | -539.8 | -491.5 |
| FCF (OCF − Capex) | 958.4 | 749.6 | 1,303.8 | 2,490.7 | 3,598.0 |
| FCF margin | 15.4% | 10.5% | 15.6% | 24.7% | 31.1% |
| FCF / 淨利 | 0.72 | 0.42 | 0.56 | 0.87 | 1.22 |

- TTM OCF 4,089.5M 與 info operatingCashflow 吻合。info freeCashflow 為 USD 3,434.8M, 與季度加總 3,598.0M 有差異 (口徑不同, 兩者皆列出)。
- FCF / NI: FY2025 0.87, 低於 0.9 健康門檻; TTM 為 1.16–1.22, 達標。FY2022–FY2024 長期低於 0.9, 主因 2023–2024 大幅擴建產能 (capex 占營收 13–15%)。
- Stock-based compensation: FY2025 USD 788.2M (占營收 7.8%); TTM 約 USD 835M (推算)。SBC 占比偏高, 會稀釋 FCF 的實際股東收益。
- Working capital 變化 FY2025 為 -USD 1,272.3M, 主要來自存貨增加 (-1,063.4M)。

**資產負債表 (USD B)**
| 項目 | FY2025 (12/31) | Q3 2026 (9/30) |
|---|---|---|
| Cash + 短期投資 | 5.93 | 4.04 |
| 長期投資 (Investments And Advances) | 3.10 | 2.76 |
| 總負債 | 2.52 | 3.23 |
| 股東權益 | 17.82 | 15.99 |
| 存貨 | 1.84 | 2.13 |
| 流動比率 | 4.87 (推算) | 3.33 |

- Total debt: info 回報 0, 季度資料無有息負債, 視為無負債。FY2021 有 USD 87M 資本租賃, 之後無。Net cash (僅現金+短期投資): USD 4.04B; 含長期投資: 約 USD 6.80B (推算)。
- Current ratio: info 3.33 與 Q3 流動資產 8.43B ÷ 流動負債 2.53B = 3.33 吻合。Quick ratio 2.32 (info)。
- Debt/Equity: 無負債, info debtToEquity 為 n/a。
- 現金下降: 由 FY2025 的 USD 5.93B 降至 Q3 2026 的 4.04B, 減少 32%, 主要因為 2026 年回購股份 (見下節)。
- 存貨: Q3 2026 USD 2.13B, 較 FY2025 增加 15.7%, 較 Q3 2025 增加 19.4%, 與營收年增 21.7% 大致同步, 未見異常堆貨。

## Capital allocation & insider signal

**資本配置**
- Capex: FY2022 532.4M, FY2023 1,064.2M, FY2024 1,111.2M, FY2025 539.8M (5.4% of 營收), TTM 491.5M (4.2%)。2025 年後資本支出明顯回落, 釋出較多現金流。
- 股票回購: FY2022 2,607.4M, FY2023 416.3M, FY2024 0, FY2025 2,295.3M, TTM 4,620.2M (其中 Q3 2026 單季 2,975.7M)。TTM 回購約為市值的 3.1%。
- TTM 回購 (4.62B) 高於 TTM FCF (3.60B), 差額由現金與短期投資支應。
- 股本: 年底 2025 為 355.1M 股, Q3 2026 為 353.3M 股, info 目前流通股數為 346.6M (與季度資料有差異, 可能反映 Q3 後回購, 口徑未明)。
- 股利: 無 (dividendYield 0, payoutRatio 0)。股利覆蓋率不適用。

**內部人交易 (近 6 個月, 2026-05-28 至 2026-11-27)**
- 共 26 筆 Sale 交易, 合計 62,650 股, 金額約 USD 27.36M。買進 0 筆。
- 占市值比例: 27.36M ÷ 市值 USD 148.08B = 約 0.02%, 規模小。
- 主要賣方: Mark Preston Brosius (多次小額賣出, 約 USD 0.02–0.1M 每筆), Gary Guthart (2026-10-23 約 USD 9.08M、2026-11-04 約 USD 4.57M、2026-08-11 約 USD 4.0M), Fredrik Widman (2026-10-30 約 USD 2.38M), Gary Loeb、Craig Barratt 等。
- 多筆 Sale 同時伴隨 "Conversion of Exercise of derivative security" (選擇權行權後賣出), 屬典型員工股權處置。是否為 10b5-1 計畫: DATA_UNAVAILABLE。
- 結論: 內部人淨賣出, 但金額與市值相比極小, 且無買進訊號。insidersPercentHeld 0.53%。

**機構持股 (inst_holders / major_holders)**
- 機構持股 88.7%, 機構數 3,144 家。
- 前幾大: BlackRock 8.53% (季減 -1.54%), Vanguard 6.67%, State Street 4.67%, Invesco 3.47%, T. Rowe Price 2.87% (季減 -11.65%), Capital World 2.44% (季增 +9.05%), Morgan Stanley 2.23% (季增 +18.06%)。

## Valuation

| 指標 | 數值 | 計算基礎 |
|---|---|---|
| 股價 (cache) | USD 427.18 | 2026-11-26 |
| 市值 | USD 148.08B | info marketCap |
| 企業價值 (EV) | USD 144.17B | info enterpriseValue |
| Trailing P/E | 51.7x | TTM GAAP EPS 8.27 |
| Forward P/E | 34.3x | forwardEps 12.47 (分析師口徑, 非 GAAP 明確定義) |
| EV/EBITDA | 32.2x | TTM EBITDA USD 4.47B (info) |
| P/S | 12.8x | TTM 營收 USD 11.58B |
| P/FCF | 43.1x (info FCF) / 41.2x (季度加總 FCF) | 市值 ÷ TTM FCF |
| P/B | 9.3x | info priceToBook |

- 股價 52 週區間 USD 328.57–603.88, 現價較 52 週高點低 29.3%。
- 50 日均線 426.32, 200 日均線 426.69, 現價貼近兩條均線之上 (與 200 日均線差 +0.1%)。
- Beta 1.44 (info)。
- 分析師: 31 位, 推薦 buy, 目標均價 USD 487.72 (較現價 +14.2%)。
- 類股中位數為估計值 (非工具資料): 醫療器材 (Medical Instruments & Supplies) 一般 trailing P/E 約 25–30x、forward P/E 約 20–25x、EV/EBITDA 約 15–20x、P/S 約 4–5x、P/FCF 約 25–30x。ISRG 在所有指標上均顯著溢價, 此溢價主要反映其 17% 級別的營收成長率與近 30% 的營業利益率, 估值是否合理需由後續研究判斷。

## Key catalysts
- 下次財報: 2027-01-21 (Yahoo earnings_dates, 尚未公布; 日期為估計)。EPS 估計 USD 2.95。
- 最近一次財報 (2026-10-20): 報告 EPS USD 3.00 (非 GAAP), 較 consensus 2.64 高 13.6%; GAAP EPS 1.49。
- 近期指引 (guidance) 與全年營收 / 手術量指引: DATA_UNAVAILABLE (工具未提供管理層指引原文)。
- 分部與產品 (da Vinci 機台裝機量、耗材、Ion 營收) 的季度變化: DATA_UNAVAILABLE。
- 需追蹤事項: (1) Q3 2026 的 -USD 450M 其他非營業項目性質 (一次性或持續性); (2) 2026 年回購是否持續 (TTM 回購高於 FCF); (3) 存貨與營收比例是否維持。

## Red flags
- Q3 2026 GAAP 淨利 USD 522.8M, 年減 25.8%, 主要因 -USD 450.0M 其他非營業項目 (成因 DATA_UNAVAILABLE)。這會使 GAAP P/E 與 FCF/NI 等比率在 Q3 失真。
- 估值溢價極高: trailing P/E 51.7x、EV/EBITDA 32.2x、P/S 12.8x、P/FCF 43x。若成長放緩, 估值壓縮風險大。
- 回購 TTM USD 4.62B 超過 FCF USD 3.60B, 現金與短期投資由 USD 5.93B 降至 4.04B (−32%), 後續回購能否持續需要觀察。
- FY2025 FCF/NI 0.87, 低於 0.9 門檻 (2025 年為近四年最高, 但仍未達標)。
- SBC 占營收約 7–8%, 會侵蝕 FCF 的股東實際收益。
- 內部人持續賣出 (26 筆 / 6 個月, 無買進), 金額雖小但方向一致。
- 股價較 52 週高點低 29%, 且 EPS 成長 (GAAP) 轉弱; 市場正在重新評估估值 (事實描述, 非交易建議)。
- 資料缺口: 分部營收、管理層指引、Q3 非營業項目細節、10b5-1 標記、類股中位數皆為 DATA_UNAVAILABLE 或估計值。
- 資料時點: 股價為 2026-11-26 cache; 財報截至 2026-09-30; 內部人交易最後一筆 2026-11-20。以上均早於或等於 as-of 2026-11-27, 無 as-of 後資料。下次財報 (2027-01-21) 為未來事件。

## Metrics table

單位: 營收、利潤、現金流、資產負債表為 USD B 或 USD M (表頭標示); 比率為 %、x。YoY 欄位定義見備註。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 TTM (USD B) | 11.58 | Q3 2026 季 +21.7% | n/a | 強 |
| 營收 3Y CAGR FY22–25 | 17.4% | n/a | 約 6–8% (估計) | 強 |
| Gross margin Q3 2026 | 68.4% | +2.0 pt (vs Q3 2025 66.4%) | 約 55–65% (估計) | 強 |
| Operating margin TTM | 32.3% | Q3 +3.9 pt (34.2% vs 30.3%) | 約 12–18% (估計) | 強 |
| Net margin Q3 2026 | 17.1% | −11.0 pt (vs Q3 2025 28.1%) | 約 10–15% (估計) | 注意 (非營業項目影響) |
| GAAP diluted EPS TTM (USD) | 8.27 | Q3 2026 −23.6% | n/a | 注意 |
| ROE | 17.9% | n/a | 約 10–14% (估計) | 強 |
| ROIC (推算) | 14.9% | n/a | 約 8–12% (估計) | 良好 |
| FCF TTM (USD B) | 3.60 | FY2025 +91% (2.49 vs 1.30) | n/a | 強 |
| FCF margin TTM | 31.1% | FY25 24.7% → TTM 31.1% | 約 10–15% (估計) | 強 |
| FCF / NI (TTM) | 1.22 | FY25 0.87 | 約 0.8–1.0 (估計) | 良好 (FY25 低於 0.9) |
| Net cash (cash + ST inv, USD B) | 4.04 | −31.9% vs FY2025 (5.93) | n/a | 良好 (下降來自回購) |
| Total debt | 0 | n/a | 約 0.5–1x EBITDA (估計) | 強 |
| Current ratio | 3.33 | n/a | 約 2.0–2.8 (估計) | 強 |
| Debt / Equity | 無負債 | n/a | 約 0.3–0.6 (估計) | 強 |
| Capex / 營收 TTM | 4.2% | FY24 13.3% → FY25 5.4% | 約 4–7% (估計) | 良好 |
| 回購 TTM (USD B) | 4.62 | FY25 2.30 | n/a | 注意 (高於 FCF) |
| 股息殖利率 | 0% | n/a | 約 1–2% (估計) | 不適用 (無配息) |
| 內部人淨買賣 (6 個月) | 淨賣 USD 27.36M, 0 筆買入 | n/a | n/a | 中性偏負 (規模小) |
| 機構持股比例 | 88.7% | n/a | 約 75–85% (估計) | 中性 |
| Trailing P/E | 51.7x | n/a | 約 25–30x (估計) | 偏貴 |
| Forward P/E | 34.3x | n/a | 約 20–25x (估計) | 偏貴 |
| EV/EBITDA (TTM) | 32.2x | n/a | 約 15–20x (估計) | 偏貴 |
| P/S (TTM) | 12.8x | n/a | 約 4–5x (估計) | 偏貴 |
| P/FCF (TTM) | 43.1x | n/a | 約 25–30x (估計) | 偏貴 |
| Beta | 1.44 | n/a | 約 1.0 (估計) | 波動偏高 |

備註:
- YoY 欄位: 若為季度, 指 Q3 2026 對比 Q3 2025; 若為年度, 指 FY2025 對比 FY2024; TTM 無法與前一 TTM 比較者以 n/a 標示。
- Sector median 欄位皆為估計值, 不是來自工具的數據, 只作相對比較用途。

FUNDAMENTALS REPORT COMPLETE
