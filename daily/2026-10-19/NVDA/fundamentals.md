# Fundamentals — NVDA as of 2026-10-19

## Executive summary
NVDA 獲利與現金創造能力仍屬頂尖：TTM 營收 302.97B（最新單季 YoY +105.9%）、營業利益率 65.2%、TTM FCF 127.0B，且現金與短期投資 62.47B 高於總債務（Total Debt） 38.35B，流動比率 4.59。估值面 trailing P/E 27.1x、forward P/E 13.5x，以 forward 盈餘看偏便宜，但以 P/S 17.1x、P/FCF 約 40.7x 計算仍明顯高於半導體一般水準（估計）。主要風險在於 2026 Q2（Jul-26）單季 FCF/NI 僅 0.36（應收帳款與存貨大增），以及總債務（Total Debt）一季內由 12.35B 跳升至 38.35B，用途在工具資料中未揭露，需進一步查證。

**資料時效與品質說明**
- 最新價 214.13 為 2026-10-16 收盤（yfinance `regularMarketTime`），前收 217.23；2026-10-17 與 10-18（美東）收盤未包含在工具資料中，故以 10-16 收盤作為最後已知價。工具回傳來源為 repo cache（cached_at 2026-10-18 10:55 UTC），符合任務說明的 fallback 情況。
- 本報告未使用任何 2026-10-19 之後的資料。下次財報日 2026-11-17 位於 as-of 之後，僅列為 catalyst 預期，不計入現況判斷。
- yfinance 內部數值有多處不一致（見 Red flags 第 4 點），本報告以季度損益表與資產負債表加總為主要計算來源，並於表格中註明與 info 欄位的差異。
- 「Sector median」欄位為依一般半導體產業經驗之估計值，非工具資料，僅供參考。

## Revenue & profitability

**營收規模與成長**
- 年度營收（yfinance `financials`，會計年度止於 1 月）：FY23 26.97B、FY24 60.92B、FY25 130.50B、FY26 215.94B。FY22 欄位為 null，故無法計算 4 年以上 CAGR；FY23→FY26 三年 CAGR 約 100%（基期低，數字偏高）。
- 季度營收（`quarterly_fin`）：Jul-25 46.74B → Oct-25 57.01B（QoQ +22.0%）→ Jan-26 68.13B（+19.5%）→ Apr-26 81.62B（+19.8%）→ Jul-26 96.22B（+17.9%）。最新單季 YoY +105.9%，與 info `revenueGrowth` 1.059 一致。
- 成長動能未見減速跡象：連續四季 QoQ 維持在 +18% 至 +22% 區間。
- 分部營收：yfinance 未提供分部拆分。`longBusinessSummary` 僅說明兩大分部為 Compute & Networking 與 Graphics，無金額，**segment mix 為 n/a**。

**毛利、營業利益與淨利趨勢**
- 季度毛利率：Jul-25 72.4% → Oct-25 73.4% → Jan-26 75.0% → Apr-26 74.9% → Jul-26 75.0%，穩定在 75% 附近。
- 季度營業利益率：Jul-25 60.8% → Oct-25 63.2% → Jan-26 65.0% → Apr-26 65.6% → Jul-26 66.2%，逐季擴張。
- 年度毛利率：FY23 56.9%、FY24 72.7%、FY25 75.0%、FY26 71.1%。FY26 全年低於 FY25 主要是 FY26 第一季（Apr-25 季）推算毛利率僅約 60.5%（由年度數字扣除其餘三季推算，非直接揭露數字），之後三季已回升至 73% 以上。
- 年度營業利益率：FY23 20.7%、FY24 54.1%、FY25 62.4%、FY26 60.4%。
- TTM 淨利 192.88B、淨利率 63.7%（info `profitMargins` 63.66%）。最新單季淨利 59.69B，YoY +125.9%。
- 研發費用：Jul-26 單季 R&D 7.05B，YoY +64.4%，TTM 約占營收 7.8%；SG&A 規模小（FY26 4.58B，約占營收 2.1%）。

**ROE / ROIC**
- ROE：info `returnOnEquity` 117.2%。以 TTM 淨利除以最新權益（Jul-26 228.98B）計算約 84.2%。權益基數快速擴大，ROE 數字受權益增長拉低，但仍屬極高水準。
- ROIC（估算，本報告自算）：TTM 營業利益 197.58B × (1 − 16.5% 稅率) ≈ NOPAT 165.0B。投入資本以「總債務（Total Debt） + 權益 − 現金與短期投資」計約 204.9B，ROIC 約 80%；若不扣除現金則約 62%。結論：ROIC 位於 60% 至 80% 區間，資本效率極高。

**EPS**
- TTM diluted EPS 7.91（季度加總，與 info `trailingEps` 一致）；FY26 diluted EPS 4.90。
- Forward EPS 15.91（info `forwardEps`），隱含 forward 盈餘較 TTM 成長約 101%。

## Cashflow & balance sheet

**現金流品質**
- TTM 營運現金流 134.36B、資本支出 7.35B，TTM FCF 127.0B，FCF margin 41.9%。
- FCF/NI：TTM 0.66；FY24 0.91、FY25 0.83、FY26 0.81。TTM 與近年均低於 0.9 健康門檻。
- 最新單季（Jul-26）：OCF 24.08B、NI 59.69B、FCF 21.4B，FCF/NI 僅 0.36。主因為營運資金變動 −30.71B（應收帳款 −22.35B、存貨 −5.78B），季度 OCF 較 Apr-26 季（50.34B）大幅下滑。
- 注意：info `freeCashflow` 為 41.81B、`operatingCashflow` 為 134.36B；後者與季度加總一致，前者與季度 FCF 加總 127.0B 不一致，本報告以季度加總為準（見 Red flags）。

**資產負債表（最新 Jul-26）**
- 現金與短期投資：62.47B（Apr-26 為 80.57B，單季減少 18.1B；其中現金及約當現金 22.44B、較前季增加）。
- 總債務（Total Debt）：38.35B（Apr-26 為 12.35B，Jan-26 為 11.04B）；其中長期負債 32.37B（Apr-26 為 7.47B）。
- 淨現金（自算）：現金與短期投資 − 總債務（Total Debt） = +24.12B。Jul-25 同口徑約 +43.4B，淨現金規模在一年內縮減。
- yfinance 的 `Net Debt` 欄位為 10.92B，與上述自算口徑不符，無法從工具資料解釋，列為資料品質問題。
- 流動比率：4.59（Jan-26 為 3.90；Jul-25 為 4.21）。Quick ratio 2.92（info）。
- 負債權益比：0.17x（info `debtToEquity` 16.97%，即 0.17x；Jul-25 約 0.11x）。
- 權益：228.98B（Jan-26 為 157.29B，半年增加約 46%，主要來自獲利留存）。
- 應收帳款 63.06B，較 Jan-26（38.47B）增加 63.9%；以季營收估算 DSO 約 59.6 天，Jan-26 約 51.4 天。
- 存貨 31.58B，較 Jan-26（21.40B）增加 47.5%；以季營業成本估算 DIO 約 119 天，Jan-26 約 114 天。
- 總資產 320.27B（Jan-26 為 206.80B）。

## Capital allocation & insider signal

**資本支出**
- 年度 CapEx：FY23 1.83B → FY24 1.07B → FY25 3.24B → FY26 6.04B，FY26 較 FY25 增加約 87%。
- TTM CapEx 7.35B，占營收約 2.4%，資本強度低。Jul-26 單季 CapEx 2.68B，YoY +41%。

**庫藏股與股利**
- 年度回購：FY23 10.04B、FY24 9.53B、FY25 33.71B、FY26 40.09B。TTM 回購約 55.3B（約占 TTM FCF 的 43.6%）。
- 流通股數：24.304B（Jan-26）→ 24.147B（Jul-26），半年減少約 0.6%，回購有實際縮減股本效果。
- 股利：info `dividendRate` 1.00（forward）、`dividendYield` 0.47%、`payoutRatio` 3.5%。股利覆蓋度極高。
- 注意：Jul-26 季度 `Common Stock Dividend Paid` 為 6.05B，遠高於前幾季約 0.24B 的常態水準；info `lastDividendValue` 為 0.25，ex-date 為 2026-09-10，與 forward `dividendRate` 1.00 一致，但與季度現金流的時點不完全對應。性質（特別股利或股利政策調整）工具資料無法確認，需查證。

**內部人交易（2026-04-19 至 2026-10-19，yfinance `insider`）**
- 公開市場賣出：9 筆，合計約 6.20M 股、約 1,370.5M USD。其中董事 Mark A. Stevens 佔 5 筆、約 1,353.7M USD（2026-06-04 至 2026-09-18），其餘為 General Counsel Timothy Teter（約 13.3M USD）、董事 Stephen Neal（3.3M USD）與 John Dabiri（0.1M USD）。
- 公開市場買進：0 筆。
- 其他：股票贈與（Tench Coxe 三筆 500k 股、Jen-Hsun Huang 2026-06-16 贈與 400k 股，皆 0 USD）、董事與高管股票授予（2026-06-25、2026-08-10、2026-09-09）。
- 規模評估：1,370.5M USD 相當於目前市值 5.17T 的約 0.03%，對市場衝擊有限，但方向一致（全部為賣出，無買進）。近期 Stevens 賣出價位約 209.70 至 234.00 USD，目前價 214.13 位於該區間內。
- 內部人持股比例 4.0%（info `heldPercentInsiders`）。

## Valuation

**相對估值（本報告自算數字以 214.13 USD、市值 5.17T、EV 5.14T 計）**
- Trailing P/E 27.1x（info）；以 TTM EPS 7.91 計算一致。
- Forward P/E 13.5x（info，以 forward EPS 15.91 計算）。PEG 0.26（info `pegRatio`）。
- EV/EBITDA：info 25.5x（以 info `ebitda` 201.27B 計）；以季度 EBITDA 加總 233.89B 自算約 22.0x。兩者差異來自 EBITDA 定義不一致，本報告以 22x 至 26x 區間呈現。
- P/S（TTM）：17.1x（info 17.07x，與 TTM 營收 302.97B 一致）。
- P/FCF（TTM）：約 40.7x（市值 / 季度加總 FCF 127.0B）。若採 info FCF 41.8B 則約 124x，本報告不採用此數字。
- P/B：22.6x（info）。
- 與半導體產業中位數比較（估計）：trailing P/E 估計約 30x，NVDA 略低；forward P/E 估計約 22x，NVDA 明顯偏低；P/S 估計約 8x，NVDA 為 2 倍以上；P/FCF 估計約 30x，NVDA 偏高。
- 結論：以 forward 盈餘看估值不貴，但以營收與自由現金流倍數看仍屬高溢價，估值隱含高成長持續的假設。

**分析師共識（info / `recommendations`，僅供參考，非建議）**
- 推薦評等：10 家 strongBuy、49 家 buy、2 家 hold、1 家 sell、0 家 strongSell（合計 62 家）；recommendationMean 1.29（strong buy）。
- 目標價：均值 328.72、中位數 315.00、最高 515.00、最低 180.00；相對現價隱含上行空間分別約 +53.5%、+47.1%。
- 股價位置：52 週區間 164.27 至 243.37，現價距高點 −12.0%、距低點 +30.4%；50 日均線 223.08（現價 −4.0%）、200 日均線 202.97（現價 +5.5%）。Beta 2.22，屬高波動標的。

## Key catalysts
- **下次財報**：2026-11-17（yfinance `earnings_dates`，`isEarningsDateEstimate` 為 false），屬 as-of 之後事件。共識 EPS 2.47（Q3 FY27，即 Oct-26 季）。
- **過去 8 季 EPS surprise**：全部為正，平均約 +5.8%（2024-11 至 2026-08，依 `earnings_dates` 口徑）；最近一季（2026-08-26）實際 2.22 vs 估計 2.09，+6.16%。注意該口徑與季度 GAAP EPS 不一致（見 Red flags）。
- **指引（guidance）**：工具資料中未提供管理層指引文字，**guidance 為 n/a**，需補充財報新聞或 transcript。
- **分部與產業動態**：`longBusinessSummary` 提及與 Cisco 合作 USFP 光學模組、與 ChipAgents 合作 AI 晶片設計基準、與 MediaTek 策略聯盟建構下一代 AI 運算平台；屬定性資訊，未量化。
- **股東與做空**：空單 311.4M 股，占流通股 1.34%，short ratio 2.75 日（資料日期約 2026-09-30）；機構持股 71.4%，前四大為 BlackRock 8.06%、Vanguard 6.39%、FMR 4.26%、State Street 4.19%（2026-06-30 申報）。
- **股息**：ex-date 2026-09-10 已過；工具欄位 `dividendDate` 為 2026-10-01，性質待確認。

## Metrics table

本表「Sector median (estimate)」為依產業經驗之估計值，非工具資料；「YoY」在無對應資料時標示為 n/a 或以季度對比替代並註明。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 TTM | 302.97B | Jul-26 單季 +105.9% | 約 10% 至 15% 成長率 | 顯著優於 |
| 營收 3 年 CAGR（FY23→FY26） | 約 100% | n/a | n/a | 高成長但基期低 |
| 毛利率 TTM | 74.7% | Jul-26 單季 75.0% vs Jul-25 72.4%（+2.6pt） | 約 55% | 優異 |
| 營業利益率 TTM | 65.2%（info 66.2%） | Jul-26 單季 66.2% vs Jul-25 60.8%（+5.4pt） | 約 20% | 優異 |
| 淨利率 TTM | 63.7% | Jul-26 單季 62.0% vs Jul-25 56.5%（+5.5pt） | 約 15% 至 20% | 優異 |
| ROE | 117.2%（info）；自算 TTM NI/最新權益 84.2% | n/a | 約 20% | 優異（權益基數快速擴大） |
| ROIC（自算） | 約 62% 至 80% | n/a | 約 15% | 優異 |
| FCF TTM（季度加總） | 127.0B | n/a | n/a | 強勁 |
| FCF margin TTM | 41.9% | n/a | 約 10% | 優異 |
| FCF / NI TTM | 0.66 | Jul-26 單季 0.36 | 約 0.8 | 偏弱，低於 0.9 門檻 |
| 現金與短期投資 | 62.47B | 較 Jul-25 53.99B，+15.7% | n/a | 充裕但較 Apr-26 下降 |
| 總債務（Total Debt） | 38.35B | 較 Jul-25 10.60B，+262% | 約 0.3x D/E | 紅旗（需查證用途） |
| 淨現金（自算） | +24.12B | 較 Jul-25 約 +43.4B，下降約 44% | n/a | 仍為淨現金，但趨勢轉弱 |
| 流動比率 | 4.59 | Jul-25 4.21 | 約 2.5 | 健康 |
| 負債權益比 D/E | 0.17x | Jul-25 約 0.11x | 約 0.3x | 健康，但上升中 |
| CapEx TTM / 占營收 | 7.35B / 2.4% | Jul-26 單季 +41% | 約 5% 至 10% | 資本強度低 |
| 年度回購 FY26 | 40.09B | 較 FY25 33.71B，+18.9% | n/a | 穩定回購 |
| 股利覆蓋 | payout 3.5%、yield 0.47% | 股利 forward 1.00 | 約 20% 至 30% payout | 覆蓋極高（Jul-26 大額股利需查證） |
| 內部人 6 個月淨交易 | 淨賣出約 1,370.5M USD；買進 0 筆 | n/a | n/a | 中性偏警示（占市值約 0.03%） |
| Trailing P/E | 27.1x | n/a | 約 30x | 略低於產業 |
| Forward P/E | 13.5x | n/a | 約 22x | 明顯偏低 |
| PEG | 0.26 | n/a | n/a | 低（依 forward 成長） |
| EV/EBITDA | 25.5x（info）／約 22.0x（自算） | n/a | 約 20x | 略高 |
| P/S TTM | 17.1x | n/a | 約 8x | 顯著溢價 |
| P/FCF TTM | 約 40.7x | n/a | 約 30x | 偏高 |
| P/B | 22.6x | n/a | 約 6x | 偏高 |
| Beta | 2.22 | n/a | 約 1.2 | 高波動 |
| 分析師均值目標價 | 328.72 USD（+53.5%） | n/a | n/a | 共識偏多（非建議） |

## Red flags
- **單季現金流轉弱**：Jul-26 單季 OCF 24.08B、FCF 21.4B、FCF/NI 0.36，營運資金變動 −30.71B。若應收帳款持續擴張，獲利的現金轉換率將持續承壓。
- **應收與存貨快速累積**：應收帳款較 Jan-26 增加 63.9%（DSO 約 51 天升至約 60 天），存貨增加 47.5%（DIO 約 119 天）。需追蹤是否為需求前置或收款期拉長。
- **總債務（Total Debt）一季內大增**：總債務（Total Debt）由 Apr-26 的 12.35B 跳升至 Jul-26 的 38.35B，長期負債由 7.47B 增至 32.37B。以現金流倒推，Jul-26 季淨舉債約 +19.6B（推算值，非直接揭露）。工具資料未說明用途（併購、融資或其他），需查 10-Q 或公告。
- **資料一致性問題（需查證）**：
  1. info `freeCashflow` 41.81B 與季度 FCF 加總 127.0B 不符。
  2. info `ebitda` 201.27B 與季度 EBITDA 加總 233.89B 不符。
  3. yfinance `Net Debt` 10.92B 與「總債務（Total Debt） − 現金與短期投資 = −24.12B」不符。
  4. `earnings_dates` 的 Reported EPS（2026-05-20 為 1.87、2026-08-26 為 2.22）與季度 GAAP diluted EPS（Apr-26 為 2.39、Jul-26 為 2.46）不符，可能為 non-GAAP 與 GAAP 口徑混用。
  5. info 的 `prevName` 為 "Usual Stablecoin"、`nameChangeDate` 為 2026-10-18，與 NVIDIA 公司身分明顯不符，疑似資料錯誤。
  6. info `numberOfAnalystOpinions` 為 59，與 `recommendations` 合計 62 家不一致（評等口徑差異）。
- **股利異常**：Jul-26 季度股利現金支出 6.05B，遠高於常態約 0.24B，與 info `lastDividendValue` 0.25 的時點不完全對應，性質待查。
- **估值溢價**：P/S 17.1x、P/FCF 約 40.7x、P/B 22.6x，估值高度依賴高成長持續。
- **高波動**：Beta 2.22，且股價位於 50 日均線下方（−4.0%）。
- **內部人持續賣出**：6 個月內 Stevens 等董事共 9 筆公開市場賣出，合計約 1.37B USD，無公開市場買進。金額占市值比例極小，但方向一致。
- **治理風險評分偏高**：info `overallRisk` 8（滿分 10）、`boardRisk` 10，為外部評分，僅供參考。
- **價格資料時效**：最新價為 2026-10-16 收盤，10-17 與 10-18 收盤未納入，對 2026-10-19（台北）的即時判斷有時間落差。
- **分部與指引資料缺口**：segment mix 與管理層 guidance 工具資料均為 n/a。

FUNDAMENTALS REPORT COMPLETE
