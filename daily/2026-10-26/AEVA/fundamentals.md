# Fundamentals — AEVA (Aeva Technologies, Inc.) as of 2026-10-26

> 資料時點說明：分析基準日為 2026-10-26。工具快取時間為 2026-10-25（UTC 11:11–11:15），最新報價 10.17 USD 對應 regularMarketTime 換算之 2026-10-23 交易資料（ta 工具 as_of 亦為 2026-10-23）。財務數據最新為 2026-06-30 季報（Q2 FY2026）。未發現晚於 2026-10-26 的資料。下一次財報日 2026-11-04 為基準日之後的事件。
> 單位：本報告金額統一為 USD M（百萬美元）；每股數據為 USD；比率為 %、x。

## Executive summary
Aeva 目前仍處於大幅虧損與持續燒錢階段：FY2025 營收 18.1M USD（+99.4% YoY）但營業利益率約 −706%，TTM 營業現金流為 −111.5M USD，2026-06-30 現金加短期投資 177.9M USD 以目前燒錢速度推算僅約可支撐 1.5 年，且股數 YoY 增加 23.9%，財務健康度屬高風險。2026Q2 毛利率已由 2025Q2 的 −49.4% 轉為 +35.7%，流動比率提升至 7.85x，財務結構在融資後明顯改善，但 TTM 獲利指標皆為負，無法以 P/E 或 EV/EBITDA 衡量，現價對應 P/S 32.8x、EV/Revenue 29.3x，估值明顯依賴未來營收規模化的假設。

## Revenue & profitability

**年度趨勢（USD M）**

| 年度 | 營收 | YoY | 毛利 | 毛利率 | 營業利益 | 營業利益率 | 淨利 | 淨利率 |
|---|---|---|---|---|---|---|---|---|
| FY2022 | 4.2 | n/a | −4.3 | −101.5% | −152.0 | −3,625% | −147.3 | −3,514% |
| FY2023 | 4.3 | +2.9% | −5.9 | −136.5% | −147.8 | −3,427% | −149.3 | −3,463% |
| FY2024 | 9.1 | +110.2% | −3.8 | −41.8% | −146.9 | −1,620% | −152.3 | −1,680% |
| FY2025 | 18.1 | +99.4% | −0.7 | −3.7% | −127.6 | −706% | −145.4 | −804% |

- 營收 3 年 CAGR（FY2022→FY2025）為 62.8%；FY2021 營收為 null，無法計算 5 年 CAGR。
- 營業利益列採 yfinance `Operating Income`（= 毛利 − 營業費用）。FY2024 另有 `Total Operating Income As Reported` 為 −158.4M，與前者不一致，見紅旗。
- 毛利率自 FY2022–FY2024 長期為負，FY2025 大幅改善至 −3.7%，2026 年進一步轉正。

**季度趨勢（USD M）**

| 季度 | Q2'25 | Q3'25 | Q4'25 | Q1'26 | Q2'26 |
|---|---|---|---|---|---|
| 營收 | 5.5 | 3.6 | 5.6 | 6.3 | 6.1 |
| 毛利率 | −49.4% | 12.0% | 23.5% | 31.0% | 35.7% |
| 營業利益 | −34.9 | −33.2 | −29.1 | −35.1 | −34.6 |
| 營業利益率 | −634% | −927% | −518% | −561% | −563% |
| 淨利（GAAP） | −192.7 | +107.5 | −25.3 | −35.0 | −79.6 |
| 稀釋 EPS（GAAP） | −3.49 | −0.52 | −0.42 | −0.56 | −1.23 |

- Q2'26 營收 6.1M，YoY +11.3%（與 info `revenueGrowth` 0.113 一致），QoQ −2.0%。
- Q2'26 毛利 2.2M、毛利率 35.7%；Q2'25 毛利為 −2.7M。TTM 毛利 5.9M、TTM 毛利率 27.2%（與 info `grossMargins` 0.27225 一致）。
- Q1'25 季度資料為 null；由 FY2025 營收 18.1M 扣除 Q2–Q4'25 三季合計 14.7M 推算 Q1'25 約 3.4M（推算值）。
- Q3'25 淨利為 +107.5M，但營業利益僅 −33.2M，差額來自 Total Unusual Items（+68.5M）。Q2'26 淨利 −79.6M 含 Total Unusual Items −44.7M。淨利受非營業項目（yfinance 未說明細項，疑似衍生性負債公允價值變動）大幅影響，不宜以單季淨利判斷經營趨勢。
- 營運費用：FY2025 總營業費用 126.9M，較 FY2024 的 143.1M 下降 11.3%；但 Q2'26 營業費用 36.7M，YoY +14.1%。FY2025 R&D 85.4M（相當於營收 472%）、SG&A 41.5M（相當於營收 230%）；Q2'26 R&D 24.9M（406%）、SG&A 11.9M（193%）。
- TTM 淨利 −32.4M（Q3'25–Q2'26 合計，與 info `netIncomeToCommon` −32.422M 一致），TTM 淨利率 −150.1%（與 info `profitMargins` −1.50116 一致）。TTM EBITDA 為 −126.7M（info `ebitda`）。
- 營收結構：yfinance 未提供分部營收。依 longBusinessSummary，產品線包括 Aeva Atlas（長距離 FMCW 4D LiDAR，車規）、Atlas Ultra（SAE L3/L4 自駕）、Aeva Omni（短距離 4D LiDAR）、CityOS（交通 AI 作業系統）、Eve1（工業雷射位移感測器）及光連接（optical connectivity）業務。各產品線營收占比：DATA_UNAVAILABLE。
- 獲利能力指標：ROE（FY2025 年末）= −145.4 / 13.2 ≈ −1,100%，因權益基數極小，數值無實質意義（n/m）。ROIC（TTM 營業利益 −132.0 / Q2'26 Invested Capital 124.4 ≈ −106%，未計稅，僅供方向性參考）為負。

## Cashflow & balance sheet

**現金流（USD M）**

| 年度 | OCF | Capex | FCF | FCF 利潤率 |
|---|---|---|---|---|
| FY2022 | −109.9 | −7.4 | −117.4 | n/a |
| FY2023 | −118.8 | −6.1 | −124.9 | n/a |
| FY2024 | −106.9 | −5.1 | −112.0 | n/a |
| FY2025 | −115.1 | −4.6 | −119.7 | −662% |

- FCF / 淨利比：FY2025 為 −119.7 / −145.4 = 0.82，但分子分母皆為負，此比率不具健康度判讀意義（n/m；標準 >0.9 不適用）。
- 季度 FCF：Q2'25 −31.2、Q3'25 −33.6、Q4'25 −23.7、Q1'26 −28.1、Q2'26 −31.4；TTM 合計 −116.7M，FCF 利潤率 TTM 約 −540%。
- info 的 `freeCashflow` 為 −139.5M，與季度 FCF 加總（−116.7M）不一致，見紅旗。TTM OCF 合計 −111.5M 與 info `operatingCashflow` −111.476M 一致。
- Capex 由 FY2022 的 7.4M 逐年降至 FY2025 的 4.6M（−38%），但 Capex 占營收仍達 25.5%（FY2025）；Capex 相對 D&A（FY2025 為 8.5M）為 0.54x。

**資產負債表（USD M）**

| 科目 | 2026-06-30 (Q2'26) | 2025-12-31 (FY25) | 2025-06-30 (Q2'25) |
|---|---|---|---|
| 現金及約當現金 | 43.2 | 72.3 | 21.7 |
| 現金及短期投資合計 | 177.9 | 121.9 | 49.8 |
| 總負債（Total Debt） | 102.4 | 102.4 | 1.8 |
| 淨現金（現金+短投 − 總債務，本報告計算） | +75.5 | +19.5 | +48.0 |
| 流動資產 | 203.7 | 153.5 | 68.3 |
| 流動負債 | 26.0 | 35.9 | 105.7 |
| 流動比率 | 7.85x | 4.28x | 0.65x |
| 股東權益 | 27.5 | 13.2 | −118.2 |
| 負債/權益 | 3.72x | 7.75x | n/m（負權益） |
| 總資產 | 227.8 | 179.7 | 91.1 |
| 總負債 | 200.3 | 166.5 | 209.3 |

- 債務結構：2025 年新增長期債務約 100M（現金流量表 Issuance Of Debt 100.0M）；2026-06-30 長期債務 96.9M，資本租賃 5.5M。利率、到期日、契約條款：DATA_UNAVAILABLE。Q2'26 利息費用 1.2M。
- 淨現金定義：本報告以現金+短期投資減總債務計算為 +75.5M，與 info `enterpriseValue`（633.4M）= 市值（708.9M）− 淨現金（75.5M）完全吻合，故採此定義。yfinance 季度 `Net Debt` 欄位為 53.7M，與上述不一致，見紅旗。
- 現金跑道（推算，非工具直接輸出）：Q2'26 現金+短投 177.9M ÷ 近兩季平均 OCF 燒錢（Q1'26 −25.8、Q2'26 −31.2，平均 −28.5/季）≈ 6.2 季 ≈ 1.5 年；以 TTM OCF −111.5M/年計約 1.6 年。Q2'26 融資現金流入 109.3M 使現金回升，後續是否需再融資為關鍵變數。
- 股東權益於 2026-03-31 曾為 −12.4M（有形帳面價值 −13.0M），Q2'26 因融資回正至 27.5M。
- 營運資本 2026-06-30 為 177.7M；存貨 5.8M（FY2025）、應收帳款 3.7M（Q2'26），營運資產規模小。
- 累計虧損（Retained Earnings）2026-06-30 為 −871.9M；APIC 899.5M。
- Derivative Product Liabilities（FY2025）29.7M（FY2024 為 8.3M），性質未在工具輸出中說明，但與非營業損益波動相符，需後續確認。

## Capital allocation & insider signal

**資本配置**
- 股息：無（dividendYield 0.0）。
- 庫藏股：年度與季度現金流未見回購科目，判定為無回購。
- 股權融資：2023 年發行股票 21.5M；2025 年 Q3 發行 32.5M；2026 年 Q2 融資現金流入 109.3M，但該季 `Issuance Of Capital Stock` 欄位為 null，融資來源無法由工具確認（DATA_UNAVAILABLE）。
- 股數：普通股 2022 年底 43.7M → 2025 年底 61.6M（+40.8%，3 年）；2025-06-30 55.4M → 2026-06-30 68.7M（YoY +23.9%）；info sharesOutstanding 69.7M。稀釋壓力持續。
- 稀釋加權股數 Q2'26 64.7M，YoY +17.2%。
- 一次 reverse split：1:5（2024-03-19，info lastSplitDate），歷史股價需注意調整。

**內部人交易（yfinance insider，近 6 個月 2026-04-25 至 2026-10-25）**
- 公開市場賣出（SALE）合計 1,403,105 股，金額 32.25M USD（平均約 22.99 USD/股，價格區間 14.83–27.09），占市值 708.9M 約 4.6%，占流通股數約 2.0%。
- 公開市場買進：無。
- 其他：獎勵授予（Stock Award）合計 444,554 股（多數為董事或大股東之 0 價格授予，Sylebra 另有 149,998 USD 授予項）；CEO 2026-05-28 贈與（Stock Gift）200,000 股。
- 主要賣方（金額）：CEO Soroush Salehian Dardashti 約 16.25M USD（696,656 股）；CTO Mina Rezk 約 12.94M USD（552,514 股）；CFO Saurabh Sinha 約 2.92M USD（148,451 股）；董事 Katherine Motlagh、Stephen Zadesky 合計約 0.14M USD。
- 疑似重複申報：2026-07-08（64,821 股）與 2026-07-27（10,304 股）兩筆 CEO 與 CTO 數字完全相同，可能為同一筆間接持股交易的重複列示。若扣除，賣出量約 1,327,980 股、金額約 30.7M USD。
- 解讀：內部人持續且規模大的賣出，無公開市場買進，為偏空訊號。賣出是否屬 10b5-1 計畫或稅務代扣，yfinance 的 Transaction 欄位為空，DATA_UNAVAILABLE。
- 大股東：Sylebra Capital LLC 持股 30.1%（16.2M 股，2026-06-30）；Canaan Partners XI 6.7%；BlackRock 4.4%。機構持股 67.5%（272 家）；內部人持股 17.5%。

## Valuation

**估值（以現價 10.17 USD 計）**
- 市值（marketCap）708.9M USD；企業價值（EV）633.4M USD。市值 = 10.17 × 69.7M 股，與 info 吻合。
- P/E（TTM）：n/m（TTM EPS −2.72）。P/E（forward）：n/m（forward EPS −1.608；info forwardPE −6.32 為負值）。
- EV/EBITDA（TTM）：n/m（TTM EBITDA −126.7M）。
- P/S（TTM）：32.8x（info priceToSalesTrailing12Months 32.82）；EV/Revenue（TTM）：29.3x（info enterpriseToRevenue 29.33）。
- P/FCF：n/m（FCF 為負）。P/B：25.4x（每股帳面價值 0.401 USD）。
- 同業（sector median）估值中位數：DATA_UNAVAILABLE（本次工具輸出未提供同業估值資料，不估計）。

**分析師與價格位置**
- 分析師 5 家；目標價平均 29.0 USD、中位數 27.0 USD、最高 42.0、最低 15.0；recommendationKey 為 none。平均目標價相對現價 +185%，此數字僅反映分析師預期分散度，不構成結論。
- 價格位置：52 週區間 8.83–31.30 USD，現價距低點 +15.2%、距高點 −67.5%；52 週漲跌幅 −41.0%；beta 2.41。
- 技術面（ta snapshot，僅作上下文）：MA20 12.45、MA50 14.87、MA200 17.14，現價分別低於 −18.3%、−31.6%、−40.7%；RSI(14) 30.4；MACD −1.48 低於 signal −1.33，柱狀體 −0.16 持續偏弱；BB %B 0.20；ATR(14) 0.94（約 9.3% 現價）；20 日年化波動 73.5%。
- 空頭：short interest 8.96M 股，占流通股 18.6%，short ratio 5.9 日；較上月 6.10M 股增加 46.9%。

## Key catalysts
- 下一次財報：2026-11-04（earnings_dates，EPS 預估 −0.43）。此日期為基準日之後事件。
- 上一次財報（2026-08-05）：調整後 EPS −0.41，對比預估 −0.43，超出 4.1%。過去 8 季中多數為正向 surprise（2025-11 為 −2.2% 小幅未達，2026-02 +10.1%，2026-05 +5.4%）。注意 Yahoo 的 reported EPS 與 GAAP 稀釋 EPS（Q2'26 −1.23）口徑不同。
- 管理層與治理：CFO 身分在資料間不一致（insider 資料 2026 年仍列 Saurabh Sinha 為 CFO；info companyOfficers 列 Rupesh Maheshwari 為 Interim CFO，資料截至 FY2025），需確認是否有人事異動。治理風險分數：overallRisk 10（最高）、compensationRisk 10、boardRisk 9、shareHolderRightsRisk 8、auditRisk 7。
- 公司指引（guidance）：DATA_UNAVAILABLE（工具未提供管理層指引或分部營收預測）。
- 業務催化劑：產品線（Atlas Ultra 車用 L3/L4、CityOS、Eve1 工業感測、光連接業務）之量產與客戶合約進展，工具資料未涵蓋，DATA_UNAVAILABLE。
- 融資與稀釋：Q2'26 融資流入 109.3M 後，任何新增股權或債務發行均為近期重要事件。

## Metrics table

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 TTM（M USD） | 21.6 | +11.3%（Q2'26 vs Q2'25） | n/a | 成長但規模小 |
| 營收 FY2025（M USD） | 18.1 | +99.4% | n/a | 高成長（低基期） |
| 毛利率（Q2'26） | 35.7% | 較 Q2'25 −49.4% 改善 85.1 pp | n/a | 明顯改善 |
| 毛利率 TTM | 27.2% | n/a | n/a | 偏弱 |
| 營業利益率 TTM | −611% | n/a | n/a | 極差 |
| 淨利率 TTM | −150.1% | n/a | n/a | 虧損 |
| ROE（FY2025） | −1,100% | n/m | n/a | n/m（權益基數小） |
| ROIC（TTM 營業基礎） | −106% | n/m | n/a | 負 |
| OCF TTM（M USD） | −111.5 | n/a | n/a | 持續燒錢 |
| FCF TTM（M USD，季度加總） | −116.7 | n/a | n/a | 持續燒錢 |
| FCF / 淨利 | n/m（兩者為負） | n/a | >0.9 | 不適用 |
| 現金+短期投資（M USD） | 177.9 | 3.6x（vs Q2'25 49.8） | n/a | 改善，但有跑道壓力 |
| 總債務（M USD） | 102.4 | 較 Q2'25 1.8 大增 | n/a | 偏高 |
| 淨現金（M USD，本報告計算） | +75.5 | 較 Q2'25 +48.0 | n/a | 尚可 |
| 流動比率 | 7.85x | Q2'25 0.65x | n/a | 強 |
| 負債/權益 | 3.72x | Q2'25 為負權益 | n/a | 偏高 |
| 普通股股數（百萬股） | 68.7 | +23.9% | n/a | 高稀釋 |
| Capex FY2025（M USD） | 4.6 | −9.7% | n/a | 低 |
| 內部人淨買賣（近 6 月） | 淨賣 1.40M 股 / 32.3M USD | n/a | n/a | 偏空 |
| 空頭占流通股 | 18.6% | 上月 SI 增 46.9% | n/a | 偏高 |
| P/E（TTM / forward） | n/m / n/m | n/a | n/a | n/m |
| EV/EBITDA（TTM） | n/m | n/a | n/a | n/m |
| P/S（TTM） | 32.8x | n/a | n/a | 偏貴 |
| EV/Revenue（TTM） | 29.3x | n/a | n/a | 偏貴 |
| P/FCF | n/m | n/a | n/a | n/m |
| P/B | 25.4x | n/a | n/a | 偏高 |
| Beta | 2.41 | n/a | n/a | 高波動 |

## Red flags
- 持續燒錢：TTM OCF −111.5M、TTM FCF −116.7M，現金跑道約 1.5–1.6 年，未來仍需融資，稀釋風險高（股數 YoY +23.9%）。
- 獲利能力：TTM 營業利益率 −611%，TTM 淨利率 −150.1%，R&D 占營收 400% 以上；盈利轉正時點無工具資料可判斷。
- 權益結構脆弱：2026-03-31 股東權益為 −12.4M，Q2'26 回正僅靠大額融資；負債/權益 3.72x。
- 債務：總債務 102.4M（2025 年新增 100M），利率與到期結構 DATA_UNAVAILABLE。
- 內部人大量賣出：近 6 個月公開市場賣出 1.40M 股（約 32.3M USD），主要為 CEO、CTO，無公開市場買進。
- 空頭與技術面：short interest 占流通股 18.6%、較上月增加 46.9%；股價低於 MA200 約 40.7%，52 週跌幅 −41.0%。
- 治理：overallRisk 10（最高）、compensationRisk 10、boardRisk 9。
- 非營業損益波動大：單季淨利可由 +107.5M（Q3'25）到 −79.6M（Q2'26），EPS 判讀需排除非營業項目。
- 管理層資訊不一致：CFO 身分在 insider 與 info 資料之間不同，需確認。

**資料品質旗標（工具輸出問題）**
1. `info` 輸出內含一段 Alphabet Inc.（GOOGL）報價區塊（shortName/longName/regularMarketPrice 320.21 等）。AEVA 數據僅採用 symbol=AEVA 區塊的欄位，並已以市值、EV、TTM EPS 與季度加總交叉驗證。此為快取/資料混淆問題，應回報工具維護者。
2. `fast_info` 多數欄位為 null，stderr 有 Yahoo 連線 403（CONNECT tunnel failed）與「possibly delisted」訊息；價格取自 cache（10.17 USD），非即時報價。
3. 自由現金流定義不一致：info `freeCashflow` −139.5M，季度 FCF 加總 −116.7M。本報告採季度加總。
4. 淨負債定義不一致：yfinance 季度 `Net Debt` 53.7M，與計算之淨現金 +75.5M 方向相反，本報告採計算值（與 info EV 吻合）。
5. 季度 EPS 口徑不一致：Q2'26 GAAP 稀釋 EPS −1.23 vs earnings_dates Reported EPS −0.41（應為調整後）。Q3'25 基本 EPS +1.86 與稀釋 EPS −0.52 並存，且與該季淨利 +107.5M 的方向不一致，屬資料異常。
6. FY2024 營業利益：`Operating Income` −146.9M 與 `Total Operating Income As Reported` −158.4M 不一致。
7. Q2'26 融資現金流 109.3M，但 `Issuance Of Capital Stock` 為 null，融資性質無法確認。
8. Sector median 估值、分部營收、管理層指引均未由工具提供，已標示 n/a 或 DATA_UNAVAILABLE，未以估計值取代。

FUNDAMENTALS REPORT COMPLETE
