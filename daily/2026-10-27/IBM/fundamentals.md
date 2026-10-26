# Fundamentals — IBM as of 2026-10-27

## Executive summary
IBM 財務體質屬「獲利改善、現金流穩定、但槓桿偏高」：2025 年營收 67.54B USD（+7.6% YoY）、GAAP 稀釋 EPS 11.17、FCF 11.46B USD，TTM 股利 FCF 覆蓋約 2 倍。隱憂在於 2026 年大舉併購（前三季 Purchase Of Business 合計約 11.36B USD）使淨負債由 YE2025 的 47.67B USD 升至 2026-09-30 的 54.58B USD，流動比率僅 0.85x。估值以 TTM P/E 21.6x、Forward P/E 19.2x、EV/EBITDA 17.8x 計，相對 IT 服務同業屬中性，但 P/B 6.7x 偏高，且股價較 52 週高點低約 24%；分析師共識目標均價 257.2 USD（23 位，buy）。本報告僅呈現財務事實與估值水準，不做交易建議。

> 單位說明：本報告金額統一以 USD 表示，大額用 B（十億美元）、小額用 M（百萬美元），全文未使用 億 單位。
> As-of 說明：分析基準日 2026-10-27；價格 253.56 USD 來自 fast_info cache（cached_at 2026-10-26T12:44 UTC），若 10-27 收盤價不同需以實際價格重算估值。最新財報為 2026-09-30 季（FY Q3 2026，2026-10-21 公布），未見超出分析日期之資料。

## Revenue & profitability

**營收與成長（USD B）**
- 年度營收（statement）：2022 60.53 → 2023 61.86（+2.2%）→ 2024 62.75（+1.4%）→ 2025 67.54（+7.6%）。
- 3 年 CAGR（2022–2025）約 3.7%。yfinance 2021 年欄位為 null，無法計算 5 年 CAGR，標記為 n/a。
- 季度營收：2025-Q3 16.33、2025-Q4 19.69、2026-Q1 15.92、2026-Q2 17.16、2026-Q3 17.10。2026-Q3 YoY +4.7%（與 info.revenueGrowth 0.047 吻合）。TTM 營收 69.87B。
- 業務結構（依 info.longBusinessSummary）：Software（混合雲與 AI 平台）、Consulting（策略與技術服務）、Infrastructure（伺服器與儲存）、Financing（客戶融資）。各分部營收與佔比於工具資料中未提供，標記為 n/a。

**毛利 / 營業利益 / 淨利率趨勢（statement 推算）**

| 年度 | 毛利率 | 營業利益率 | 淨利率 |
|---|---|---|---|
| 2022 | 54.0% | 13.5% | 2.7% |
| 2023 | 55.4% | 15.2% | 12.1% |
| 2024 | 56.7% | 16.1% | 9.6% |
| 2025 | 58.2% | 18.5% | 15.7% |

- 毛利率與營業利益率連續三年改善，顯示軟體與顧問組合提升。
- 2025 年淨利率 15.7% 受稅務利益影響偏高：2025 全年稅費為 -0.242B USD（Tax Provision -242M），其中 Q4 單季為 -1.435B USD。Yahoo 的 Normalized Income 為 11.34B USD，對應正規化淨利率約 16.8%。
- Q3 2026 季度毛利率 56.8%（9.71B / 17.10B），Q3 2025 為 57.3%（9.36B / 16.33B），季度內略有下滑。
- 營業利益率（statement 口徑）Q3 2026 為 16.9%；info.operatingMargins 為 16.97%，與 statement 推算的 TTM 營業利益率 18.3%（12.81B / 69.87B）有差異，屬 Yahoo 欄位口徑不一致，需注意。

**EPS 與 ROE / ROIC**
- GAAP 稀釋 EPS：2022 1.80、2023 8.14、2024 6.43、2025 11.17。TTM EPS（info.trailingEps）11.72；四季 GAAP 加總 11.73，與之吻合。
- Q3 2026 GAAP 稀釋 EPS 2.30，但 yfinance earnings_dates 的 Reported EPS 為 2.95（調整後口徑），GAAP 與調整後差距約 28%，屬品質警示。
- ROE：info.returnOnEquity 34.8%；以 2025 淨利 10.59B / 平均股東權益約 29.98B 計算約 35.3%。
- ROIC（自行估算）：2025 EBIT 12.26B × (1 - 25.57% 稅率) ≈ NOPAT 9.13B，除以平均 Invested Capital 88.09B，約 10.4%。此為估算值，非 Yahoo 提供。
- ROA（info）5.3%。

## Cashflow & balance sheet

**現金流量**（USD B）

| 項目 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|
| 營業現金流 OCF | 10.44 | 13.93 | 13.45 | 13.19 |
| 資本支出 Capex | 1.97 | 1.81 | 1.69 | 1.74 |
| 自由現金流 FCF | 8.46 | 12.12 | 11.76 | 11.46 |
| FCF margin | 14.0% | 19.6% | 18.7% | 17.0% |
| FCF / NI | 5.16x（NI 基數低） | 1.62x | 1.95x（NI 基數低） | 1.08x |

- 2025 FCF / NI 1.08x，高於 0.9 的健康門檻；2024 年比值因淨利基數偏低而偏高，不宜單獨解讀。
- TTM FCF 有兩種口徑：info.freeCashflow 12.35B USD；季度 FCF 加總（2025-Q4 ~ 2026-Q3）為 14.02B USD。兩者差約 1.67B USD，工具資料無法確認差異來源，此處同時列出。
- TTM OCF 15.83B USD（與 info.operatingCashflow 吻合），TTM Capex 1.81B USD。
- 2025 年 Capex / D&A 僅 0.35x（D&A 5.02B USD），屬資本輕量化，資產再投資需求低。

**資產負債表**（最新季 2026-09-30，USD B）
- 總負債 Total Debt 67.14（長期 56.80 + 流動 7.01，含資本租賃約 3.3）。
- 現金與短期投資 11.06（現金及約當 9.23）。
- 淨負債 Net Debt 54.58。YE2025 為 47.67，前三季淨負債增加約 6.9B。
- 淨負債 / TTM EBITDA（info.ebitda 16.63B）約 3.3x。
- 利息保障倍數（2025 EBIT / 利息費用 1.94B）約 6.3x。
- 流動比率 0.85x（流動資產 31.19 / 流動負債 36.49），速動比率 0.68x（info）。營運資金為 -5.29B USD（2026-09-30）。
- 普通股東權益 35.54，含非控制權益 36.21；有形帳面淨值為 -52.98B USD（商譽與無形資產占比高）。
- 負債權益比 info.debtToEquity 185%；以 Q3 2026 總負債 / 股東權益計算約 189%。
- 現金水位相對負債偏低，短期償債依賴持續的經營現金流與再融資。

## Capital allocation & insider signal

**資本配置**
- 股利：每股年化 6.76 USD（季 1.69），殖利率 2.67%（5 年平均 3.47%），info.payoutRatio 57.5%。
- 股利現金支出：2025 年 6.26B USD，TTM 約 6.34B USD。2025 年股利覆蓋率（FCF / 股利）1.83x，TTM（季度 FCF 口徑）約 2.2x，覆蓋尚可。
- 買回：2025 年 1.02B USD（Repurchase Of Capital Stock），2026 年前三季合計 0.82B USD。
- 股數仍增加：普通股股數 YE2024 926.3M → YE2025 937.0M → 2026-09-30 945.1M，較 2025-Q3（934.7M）增加約 1.1%。買回未能抵銷股權激勵稀釋（SBC 2025 年 1.72B USD，TTM 約 1.97B USD）。
- 併購：Purchase Of Business 2024 年 3.29B、2025 年 8.30B、2026 年前三季 11.36B USD（Q1 單季 10.47B，Q3 單季 0.88B）。2026-Q1 同期發債（Issuance Of Debt 7.44B USD），併購以舉債為主要資金來源，為本期最重要的資本配置變化。
- 總體而言，2025 年股利約佔 FCF 55%；2026 年併購支出已超過全年 FCF 規模，淨負債因此上升。

**內部人交易（6 個月窗口：2026-04-27 至 2026-10-27）**
- 公開市場賣出：THOMAS ROBERT DAVID（Senior VP of IBM Software & Chief Commercial Officer，Officer）2026-08-26 賣出 25,000 股，價格 230.32 USD，金額約 5.76M USD。
- 公開市場買入：窗口內無。最近幾筆買入均在窗口之外：2026-02-25 董事 Michelle Howard（50 股，約 11.9K USD）與 Michael Miebach（434 股，約 101.3K USD），2026-01-30 David Farr（1,000 股，約 304K USD）。
- 窗口內淨交易：約 -5.76M USD（淨賣出）。占市值 239.6B USD（info.marketCap）比例約 0.0024%，規模極小。
- 其他列為 Gift、RSU/股權授予或稅款扣繳（value 為 null 或 0）之紀錄，不計入買賣判斷。
- 內部人持股 0.105%（major_holders.insidersPercentHeld）。CEO Arvind Krishna 的 unexercisedValue 約 33.8M USD（info.companyOfficers），窗口內無公開市場買賣。

**機構持股**：機構持股 66.3%，機構數 4,390 家（major_holders）。前三大為 BlackRock 8.12%（2026-06-30 季較前季 -1.03%）、Vanguard Capital Management 6.49%（+0.89%）、State Street 5.93%（+2.66%）。Morgan Stanley（-11.1%）、JPMorgan（-32.9%）為近季減持幅度較大的機構，屬單季數據。

## Valuation

以 2026-10-26 cache 價 253.56 USD 計算（市值 239.6B USD，EV 296.4B USD）。

| 指標 | 數值 | 說明 |
|---|---|---|
| Trailing P/E | 21.6x | info.trailingPE；TTM EPS 11.72 |
| Forward P/E | 19.2x | info.forwardPE；Forward EPS 13.24 |
| EV/EBITDA（TTM） | 17.8x | info.enterpriseToEbitda；TTM EBITDA 16.63B |
| EV/Revenue | 4.24x | info.enterpriseToRevenue |
| P/S（TTM） | 3.43x | info.priceToSalesTrailing12Months |
| P/FCF | 19.4x（info FCF 12.35B）／17.1x（季度 FCF 加總 14.02B） | 自行計算 |
| P/B | 6.74x | info.priceToBook；每股淨值 37.6 USD |

- 相對 52 週區間：52 週高 332.46、低 199.19，目前約處於區間 41% 位置，較高點回檔 23.7%。
- 均線：50 日均 233.04（現價高於約 8.8%）、200 日均 250.45（現價高於約 1.2%）。
- 分析師共識：目標均價 257.22 USD（較現價 +1.4%），recommendationKey buy，23 位分析師。
- 同業中位數為本報告估計值（非工具輸出）：IT 服務族群 trailing P/E 約 22–25x、EV/EBITDA 約 15–20x、P/S 約 2–4x、P/FCF 約 18–25x。IBM 各項估值指標位於或略低於估計區間中段，但 P/B 6.7x 仍明顯偏高，反映無形資產與商譽占比大（有形淨值為負）。
- 估值判讀：以 Forward P/E 計，IBM 相較估計區間不屬極端高估；但 EV/EBITDA 與 P/FCF 已反映淨負債與併購後的槓桿，估值支撐主要來自獲利與 FCF 持續性，而非資產淨值。

## Key catalysts
- **最近一季財報**：2026-10-21 公布 FY Q3 2026。調整後 EPS 2.95 vs 估計 2.87（+2.7% 超標）；GAAP 稀釋 EPS 2.30；營收 17.10B USD（+4.7% YoY）。
- **EPS 歷史**：yfinance earnings_dates 最近 12 季中有 11 季為超標，2026-07（2.93 vs 2.93，-0.1%）為持平略低。2024–2026 大部分季度超標幅度在 3%–12%。
- **下次財報**：yfinance 列出 2027-01-27（Q4 2026 財報，日期待確認），Q4 EPS 估計 4.63（對照 2025-Q4 調整後 EPS 4.52，預估 YoY +2.4%）。
- **股利**：info.exDividendDate 的 epoch 1794268800 換算約為 2026-11-11（需以公司公告確認）。季股利 1.69 USD。
- **公司指引（guidance）**：工具資料未提供正式全年指引數字，標記為 n/a。需以 IBM 官方新聞稿或 earnings call 逐字稿補充。
- **併購整合**：2026 年大型收購的整合進度與綜效，將影響 Software 分部營收成長與負債去化速度，為後續需追蹤的主要變數。
- **分部變化**：各分部營收與毛利資料未於工具中提供，標記為 n/a。
- **夥伴關係（business summary）**：Arm Holdings 雙架構 AI 硬體合作、UK Ministry of Defence（Team ORION）合約，為非財報性質的長期催化劑，財務影響量化不明。

## Metrics table

單位：營收、利潤、現金流以 USD B 表示；比率以 % 或 x 表示。Sector median 為估計值，非工具輸出。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 TTM（USD B） | 69.87 | n/a（前一 TTM 缺） | n/a | 中性 |
| 季營收 2026-Q3（USD B） | 17.10 | +4.7% | 約 +4–6% | 中性 |
| 營收 3Y CAGR（2022–2025） | 3.7% | — | 約 4–6% | 偏弱 |
| 毛利率（2025） | 58.2% | +1.5 pt | 約 35–45%（IT 服務） | 優於同業（軟體組合） |
| 營業利益率（2025） | 18.5% | +2.4 pt | 約 12–15% | 優於同業 |
| 淨利率（2025，含稅益） | 15.7% | +6.1 pt | 約 10–12% | 優於同業，但含一次性稅益 |
| ROE（info） | 34.8% | — | 約 15% | 優（槓桿放大） |
| ROIC（自估） | 約 10.4% | — | 約 10–12% | 中性 |
| FCF margin（2025） | 17.0% | -1.7 pt | 約 12–15% | 良好 |
| FCF / NI（2025） | 1.08x | — | >0.9 健康 | 健康 |
| 淨負債（2026-09-30，USD B） | 54.58 | 較 YE25 +6.9 | n/a | 警示 |
| 淨負債 / TTM EBITDA | 3.3x | — | 約 2–3x | 偏高 |
| 負債權益比（info） | 185% | — | 約 60–80% | 偏高 |
| 流動比率 | 0.85x | — | 約 1.2–1.5x | 偏低 |
| 利息保障倍數（2025 EBIT/利息） | 6.3x | — | 約 8–12x | 中性偏弱 |
| 股利殖利率 | 2.67% | — | 約 1–2% | 偏高（收益吸引） |
| 股利 FCF 覆蓋率（2025） | 1.83x | — | 約 2x | 尚可 |
| 普通股股數 YoY | +1.1% | 稀釋 | 約 0% | 偏弱 |
| 併購支出（2026 YTD，USD B） | 11.36 | 已超過 2025 全年 8.30 | n/a | 警示（槓桿驅動） |
| P/E（TTM） | 21.6x | — | 約 22–25x | 中性 |
| P/E（Forward） | 19.2x | — | 約 20–24x | 中性偏低 |
| EV/EBITDA（TTM） | 17.8x | — | 約 15–20x | 中性 |
| P/S（TTM） | 3.43x | — | 約 2–4x | 中性 |
| P/FCF（TTM） | 17.1–19.4x | — | 約 18–25x | 中性偏低 |
| P/B | 6.74x | — | 約 3–5x | 偏高 |
| 內部人淨買賣（6 個月，USD M） | -5.76 | — | n/a | 小幅淨賣出，規模低 |
| 機構持股比例 | 66.3% | — | n/a | 高度機構化 |

## Red flags
- **淨負債持續上升**：淨負債由 YE2025 的 47.67B USD 增至 2026-09-30 的 54.58B USD；2026 年併購支出 11.36B USD 以舉債為主要資金來源，去槓桿路徑需以併購綜效與 FCF 追蹤驗證。
- **流動性偏緊**：流動比率 0.85x、速動比率 0.68x、營運資金為負，且有形淨值為 -52.98B USD，短期償債依賴再融資。
- **有機成長偏弱**：2022–2025 營收 CAGR 僅約 3.7%，2026-Q3 YoY +4.7%，成長主要依賴併購與價格/組合改善。
- **獲利品質**：2025 年淨利含 Q4 稅務利益（Q4 稅費 -1.435B USD），GAAP 淨利與 Normalized Income 有差異；2026-Q3 GAAP EPS 2.30 vs 調整後 2.95，差距約 28%，須留意非 GAAP 調整項目的規模。
- **股數仍在增加**：股數 YoY +1.1%，2026 前三季買回 0.82B USD 未能抵銷 SBC（TTM 約 1.97B USD）稀釋。
- **估值承擔高槓桿**：P/B 6.7x、EV/EBITDA 17.8x，估值對獲利與 FCF 持續性敏感。
- **內部人信號**：窗口內僅有一筆 5.76M USD 的高階主管賣出（2026-08-26），且無公開市場買入。金額相對市值小，但缺乏內部人加碼信號。
- **資料品質警示**：fast_info.market_cap、shares 等欄位為 null，Yahoo 的 cookie/crumb 驗證失敗，部分欄位取自 cache；info.operatingMargins（16.97%）與 freeCashflow（12.35B USD）與季度 statement 推算值存在差距；2021 年資料全部 null。本報告以 statement 為主、info 為輔，已分別標示來源。
- **分部與指引資料缺口**：分部營收、正式全年指引未由工具提供，相關判斷需補充官方資料。

FUNDAMENTALS REPORT COMPLETE
