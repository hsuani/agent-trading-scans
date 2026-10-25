# Fundamentals — AMD (Advanced Micro Devices) as of 2026-10-26

資料說明：本報告以 2026-10-26 為分析基準日。yfinance 工具以快取模式回傳（info 快取時間 2026-10-25T11:14 UTC，價格為快取時點之最新收盤價，約為 2026-10-24 收盤）。財報為 FY2025（2025-12-31）年度與 2026 年 Q2（期末 2026-06-27）季度資料。2026-11-03 的 Q3 財報日為尚未發生之預定事件，僅作為催化劑列示，不作為已實現資料。單位：USD 以 B（十億美元）或 M（百萬美元）表示，本報告無 TWD/KRW 金額。

## Executive summary
AMD 財務體質已明顯改善：FY2025 營收 34.64B USD（YoY +34.3%）、淨利 4.34B USD、FCF 6.74B USD（FCF margin 19.4%），且淨現金約 6.7B USD，資產負債表穩健。估值則處於極端高位，trailing P/E 131.8x、P/S 20.4x、EV/EBITDA 87.3x、P/FCF 約 95x，市場定價高度依賴 forward EPS 15.76 USD（forward P/E 32.8x）的兌現。股價 β 2.454、距 52 週高點 658.52 USD 回落約 21.5%，內部人於過去 6 個月持續減持（合計約 2.60 億 USD，約占市值 0.03%），但並無公開市場買進。

## Revenue & profitability

**營收趨勢（USD，B）**

| 年度 | 營收 | YoY | 毛利率 | 營業利益率 | 淨利率 |
|---|---|---|---|---|---|
| FY2022 | 23.60 | n/a | 44.9% | 5.4% | 5.6% |
| FY2023 | 22.68 | -3.9% | 46.1% | 1.8% | 3.8% |
| FY2024 | 25.79 | +13.7% | 49.3% | 8.1% | 6.4% |
| FY2025 | 34.64 | +34.3% | 49.5% | 10.7% | 12.5% |

- 3 年營收 CAGR（FY2022→FY2025）約 13.7%；yfinance 欄位顯示最早年度為 2021 但數值為 null，故無法計算 4-5 年 CAGR。
- 季度營收（B）：Q2'25 7.69 → Q3'25 9.25 → Q4'25 10.27 → Q1'26 10.25 → Q2'26 11.54。Q2'26 YoY 約 +50.1%，與 info 之 revenueGrowth 0.501 一致，為營收加速最強的季度。
- 分部營收：info 僅提供業務摘要（Data Center、Client and Gaming、Embedded 三個分部），未提供分部營收數字，**分部營收占比 DATA_UNAVAILABLE**。
- 獲利能力：FY2025 營業利益 3.69B USD（YoY 約 +77%）、淨利 4.34B USD（YoY +164%）、diluted EPS 2.65 USD（FY2024 為 1.00 USD）。Q2'26 季度毛利率約 53.8%（6.20/11.54）、營業利益率約 17.3%（1.99/11.54），較 Q2'25 之毛利率 39.8%、營業利益率 -1.7% 大幅改善。
- 盈餘品質：FY2025 淨利 4.34B 含有利因素：(1) 證券出售利益 366M USD；(2) 所得稅利益 -103M USD（實際稅率 tax rate for calcs 25.6%，但稅費列為負值）；(3) 停業部門淨利 66M USD。yfinance 之 normalized income 為 4.00B USD，故經常性淨利低於帳面淨利約 8%。
- ROE：info 之 TTM ROE 為 10.2%；以 FY2025 年末權益 63.0B USD 計算約 6.9%（FY2024 約 2.9%）。
- ROIC（估算，EBIT×(1-稅率)／（權益＋總債務－現金及短期投資））：FY2025 約 5.6%，FY2024 約 3.1%。此為本報告估算值，非工具直接提供。
- EBITDA：FY2025 EBITDA 7.28B USD（yfinance）、TTM normalized EBITDA 9.56B USD（info）。

## Cashflow & balance sheet

**現金流（USD，B）**

| 年度 | 營運現金流 (OCF) | 資本支出 (Capex) | FCF | FCF margin | FCF / 淨利 |
|---|---|---|---|---|---|
| FY2022 | 3.57 | 0.45 | 3.12 | 13.2% | 2.36x |
| FY2023 | 1.67 | 0.55 | 1.12 | 4.9% | 1.31x |
| FY2024 | 3.04 | 0.64 | 2.41 | 9.3% | 1.47x |
| FY2025 | 7.71 | 0.97 | 6.74 | 19.4% | 1.55x |

- FCF / 淨利 FY2025 為 1.55x，高於 0.9 之健康門檻；但此比率受 SBC 非現金費用（FY2025 為 1.64B USD，占營收 4.7%）與營運資金變動推升，宜搭配 SBC 扣除後觀察：(FCF − SBC) = 5.10B USD，margin 約 14.7%。
- TTM OCF 10.08B USD，TTM FCF 8.84B USD（info）。
- Capex FY2025 0.97B USD（占營收 2.8%），較 FY2024 之 0.64B USD 增加約 53%，顯示擴產或 AI 相關投資增加。

**資產負債表（USD，B）**

| 項目 | FY2024 | FY2025 | 變化 |
|---|---|---|---|
| 現金及等價物 | 3.79 | 5.54 | +46% |
| 現金及短期投資 | 5.13 | 10.55 | +106% |
| 總債務 | 2.21 | 3.85 | +74% |
| 淨現金（現金及短期投資－總債務） | 2.92 | 6.71 | +130% |
| 流動資產 | 19.05 | 26.95 | +41% |
| 流動負債 | 7.28 | 9.46 | +30% |
| 流動比率 | 2.62x | 2.85x | — |
| 總資產 | 69.23 | 76.93 | +11% |
| 總負債 | 11.66 | 13.93 | +19% |
| 股東權益 | 57.57 | 63.00 | +9% |
| 債務／權益 | 0.04x | 0.06x | — |

- 最新（info，TTM 期末）：現金及短期投資合計 13.11B USD、總債務 4.28B USD，淨現金約 8.84B USD；info 之 debtToEquity 欄位 6.361 為百分比形式（即約 0.06x）。current ratio 2.61、quick ratio 1.69。
- 注意：FY2025 總債務增加 1.64B USD，其中 2025 年發行債務 2.44B USD、償還 0.95B USD，即以舉債方式增加現金部位。債務規模仍低，但應於後續追蹤其用途。
- 利息支出 FY2025 為 131M USD，相對 EBIT 4.27B USD 負擔極低（利息保障倍數約 33x，為本報告估算）。

## Capital allocation & insider signal

**資本配置**
- 股票買回：FY2025 買回 1.92B USD（FY2024 為 1.59B USD），占 FCF 約 28.5%。
- 股息：DATA_UNAVAILABLE，info 顯示 dividendYield 0.0、payoutRatio 0.0，公司目前無配息。
- 稀釋控制：FY2025 diluted 股數 1.636B、FY2024 1.637B，基本上持平，買回大致抵銷 SBC 稀釋（basic 股數 1.624B vs 1.620B，+0.2%）。
- 總流通股數 info 為 1.632B（sharesOutstanding）。

**內部人交易（過去約 6 個月，2026-04-25 至 2026-10-25）**
- 賣出：18 筆，共 547,410 股，金額約 259.6M USD，占市值（843.6B USD）約 0.03%。
  - Lisa Su（CEO）4 筆合計約 168.6M USD（主要為每次 125,000 股的分批賣出，2026-05-13、2026-06-10、2026-09-10 等；另有 2026-09-10 之 35,000 股贈與）。
  - Forrest Norrod（Officer）4 筆合計約 34.4M USD（含選擇權行使後賣出）。
  - Mark Papermaster（CTO）4 筆合計約 23.9M USD（另有 2026-08-19 等贈與）。
  - Paul Grasby（Officer）2 筆合計約 18.6M USD；Jean Hu（CFO）1 筆約 7.1M USD（2026-08-25）；Nora Denzel、Ava Hahn 之小額賣出。
- 買進（公開市場 Purchase）：過去 6 個月為 0 筆。最近一次公開市場買進為 2025-05-20（Philip Guido，約 1.0M USD）。
- 其他：有多筆贈與（Stock Gift）及選擇權行使（Conversion of Exercise，行使價 84.85／34.19／19.10 USD）。本工具未標示交易是否屬於預先排定之 10b5-1 計畫，**是否為預定交易計畫 DATA_UNAVAILABLE**。
- 判讀：絕對金額小，占市值比例極低；減持頻率高，但與 2026 年 3 月約 200 USD 至 10 月 500 USD 以上之大幅上漲同步，屬獲利了結與高層薪酬多元化性質的可能性較高，無法單憑此資料判定為看空訊號。

**機構持股**
- 機構持股比例 75.3%（institutionsPercentHeld），機構數 5,139 家，內部人持股 0.42%。
- 前十大（資料日期 2026-06-30）：BlackRock 9.21%（150.3M 股，較前期 +3.3%）、Vanguard Capital Management 6.52%（106.5M 股）、State Street 4.56%、Invesco 3.26%（+5.4%）、JPMorgan 2.47%（+66.2%）、Geode 2.42%、Vanguard Portfolio Management 2.32%、T. Rowe Price 2.20%（+24.6%）、FMR 1.57%（+67.2%）、Morgan Stanley 1.49%。
- 近期持股增加的機構包括 JPMorgan、FMR、T. Rowe Price，顯示主動型基金持續加碼；被動型基金為主要持有人。

## Valuation

以 USD、2026-10-25 快取價 516.79 USD、市值 843.6B USD、EV 834.8B USD 計算：

| 指標 | 數值 | 說明 |
|---|---|---|
| Trailing P/E（GAAP，TTM EPS 3.92） | 131.8x | 含一次性利益，偏高 |
| Forward P/E（forward EPS 15.76） | 32.8x | 依分析師一致預期 |
| 本年度 P/E（epsCurrentYear 7.59） | 68.1x | info 之 priceEpsCurrentYear |
| PEG（trailing） | 1.12x | info 之 trailingPegRatio |
| P/S（TTM 營收 41.31B） | 20.4x | |
| EV/EBITDA（TTM normalized EBITDA 9.56B） | 87.3x | |
| P/FCF（TTM FCF 8.84B，市值／FCF） | 約 95x | 本報告估算 |
| P/B（BVPS 41.19） | 12.5x | |

- 分析師共識：50 位分析師，評級 strong_buy（平均 1.5），目標價均值 637.61 USD（+23.4% 相對快取價）、最高 1,250 USD、最低 365 USD。目標價為外部共識，非本報告之投資建議。
- 股價位置：52 週區間 188.22–658.52 USD；現價低於 50 日均線 542.28 USD、高於 200 日均線 402.08 USD。
- 風險：β 2.454，波動度遠高於大盤。
- 相對同業中位數（估計值，非工具資料）：以半導體產業一般水準估計，trailing P/E 約 35–40x、forward P/E 約 25–30x、EV/EBITDA 約 25–30x、P/S 約 6–8x、P/B 約 5–7x。AMD 估值倍數明顯高於估計同業中位數，溢價主要反映 AI 加速器成長預期。

## Key catalysts
- **2026-11-03（預定）Q3 2026 財報**：一致預期 EPS 1.93 USD（非 GAAP）。前幾季非 GAAP EPS 實績為 Q1'26 1.37（預估 1.29）、Q2'26 1.66（預估 1.61），連續超預期，但 2025-08 季度曾小幅不及（-3.5%）。
- **EPS 軌跡**：FY2025 GAAP diluted EPS 2.65，TTM 3.92；forward EPS 15.76 USD 隱含顯著獲利增幅，為估值之核心變數。
- **營收動能**：Q2'26 營收 YoY +50.1%，為最近季度主要動能；能否維持將決定 forward EPS 之兌現。
- **資本支出**：FY2025 capex 年增約 53%，後續資本支出與 FCF 轉換率需追蹤。
- **業務指引（guidance）**：DATA_UNAVAILABLE，本工具未提供公司正式財測或指引數字。
- **分部結構**：DATA_UNAVAILABLE（分部營收數字未提供）。

## Metrics table

金額單位：USD（B = 十億美元，M = 百萬美元）。YoY 為 FY2025 vs FY2024 或 Q2'26 vs Q2'25（已註明）。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收（FY2025，USD B） | 34.64 | +34.3% | n/a | 強勁成長 |
| 營收（Q2'26，USD B） | 11.54 | +50.1% | n/a | 加速成長 |
| 毛利率（FY2025） | 49.5% | +0.2 pt | 約 55% | 中性偏低，逐季改善 |
| 毛利率（Q2'26） | 53.8% | +14.0 pt（vs Q2'25 39.8%） | 約 55% | 改善中 |
| 營業利益率（FY2025） | 10.7% | +2.6 pt | 約 20% | 偏低，持續改善 |
| 淨利率（FY2025） | 12.5% | +6.1 pt | 約 15% | 中性 |
| ROE（FY2025，年末權益計） | 6.9% | +4.0 pt | 約 15% | 偏低 |
| ROE（info TTM） | 10.2% | n/a | 約 15% | 偏低 |
| ROIC（估算） | 5.6% | +2.5 pt | 約 10% | 偏低 |
| Diluted EPS（FY2025，USD） | 2.65 | +165% | n/a | 大幅改善 |
| FCF（FY2025，USD B） | 6.74 | +180% | n/a | 強勁 |
| FCF margin（FY2025） | 19.4% | +10.1 pt | 約 15–20% | 良好 |
| FCF / 淨利（FY2025） | 1.55x | +0.08x | 約 1.0x | 健康（含 SBC 與營運資金影響） |
| 營運現金流（FY2025，USD B） | 7.71 | +154% | n/a | 強勁 |
| 資本支出（FY2025，USD B） | 0.97 | +53% | n/a | 增加中 |
| 流動比率（FY2025） | 2.85x | +0.23x | 約 2.0x | 健康 |
| 債務／權益（FY2025，BS） | 0.06x | +0.02x | 約 0.3x | 極低 |
| 淨現金（FY2025，USD B） | 6.71 | +130% | n/a | 穩健 |
| 總債務（FY2025，USD B） | 3.85 | +74% | n/a | 增速快但規模低 |
| 買回（FY2025，USD B） | 1.92 | +21% | n/a | 抵銷 SBC 稀釋 |
| 股息殖利率 | 0.0% | n/a | 約 0.5–1% | 無配息 |
| SBC（FY2025，USD B） | 1.64 | +16% | n/a | 占營收 4.7%，偏高 |
| Trailing P/E | 131.8x | n/a | 約 35–40x | 高估（含一次性因素） |
| Forward P/E | 32.8x | n/a | 約 25–30x | 溢價 |
| EV/EBITDA（TTM） | 87.3x | n/a | 約 25–30x | 顯著溢價 |
| P/S（TTM） | 20.4x | n/a | 約 6–8x | 顯著溢價 |
| P/FCF（TTM） | 約 95x | n/a | 約 30–35x | 顯著溢價 |
| P/B | 12.5x | n/a | 約 5–7x | 溢價 |
| Beta | 2.454 | n/a | 約 1.2–1.5 | 波動偏高 |
| 內部人 6 個月淨賣出（USD M） | 約 260（賣出）／0（買進） | n/a | n/a | 持續減持，金額占市值約 0.03% |
| 機構持股比例 | 75.3% | n/a | 約 70–80% | 正常 |
| 分析師目標價均值（USD） | 637.61 | n/a | n/a | 上行 +23.4%（外部共識） |

## Red flags
- **估值極端**：trailing P/E 131.8x、EV/EBITDA 87.3x、P/S 20.4x，forward P/E 32.8x 高度依賴 forward EPS 15.76 USD 之兌現，任何營收或毛利不及預期將引發重估風險。
- **盈餘品質**：FY2025 淨利含 366M USD 證券利益、稅費利益與 66M USD 停業部門淨利；經常性淨利約 4.00B USD（較帳面少約 8%）。
- **高波動**：β 2.454，股價距 52 週高點回落 21.5%，且低於 50 日均線。
- **SBC 偏高**：FY2025 SBC 1.64B USD（占營收 4.7%），扣除 SBC 後 FCF margin 降至約 14.7%。
- **舉債增加**：FY2025 總債務增加 74% 至 3.85B USD，其中新增發債 2.44B USD，需追蹤資金用途。
- **內部人持續減持**：6 個月內 CEO、CTO、CFO 及多位高階主管出售股票，合計約 260M USD，且無公開市場買進；部分為預定計畫，但無法由工具資料確認。
- **資料缺口**：分部營收、正式財測指引、股息細節、10b5-1 計畫標示皆為 DATA_UNAVAILABLE；info 之 TTM 毛利率（55.7%）與營業利益率（17.3%）與年度數字存在口徑差異（TTM 為季度加總，年度為 FY2025 年報），本報告分別標示。
- **治理風險分數**：Yahoo 治理評分 overallRisk 5、auditRisk 10、compensationRisk 8（評分尺度為 1–10，數值越高風險越大）；審計風險分數 10 為最高，需留意。
- **財報口徑**：earnings_dates 之 EPS 為非 GAAP 口徑（如 Q2'26 1.66），quarterly_fin 之 GAAP diluted EPS 為 1.38，兩者差異約 20%，比較時需統一口徑。

FUNDAMENTALS REPORT COMPLETE
