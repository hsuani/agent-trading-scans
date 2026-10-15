# Fundamentals — AXTI as of 2026-10-15

## Executive summary
AXTI（AXT, Inc.，NASDAQ: AXTI）在 2023–2025 年持續虧損、TTM 自由現金流為 -19.6M USD，財務體質過去偏弱；但 2026 Q2 營收單季達 47.6M USD（YoY +164.8%），毛利率回升至 44.9%，並單季轉為淨利 11.1M USD，同時完成大規模股權募集，期末現金 417.2M USD、淨現金約 331M USD。估值方面，TTM P/E（1539.75x）與 TTM EV/EBITDA（275.6x）已失去參考意義，以 Yahoo 共識 Forward EPS 2.25 計算 Forward P/E 約 27.4x，但共識樣本僅 5 家且股價較 52 週高點 143.16 已回落約 57%，資料可信度與盈餘可持續性仍需 Q3 財報（預計 2026-10-29）驗證。

## Revenue & profitability

**營收趨勢**
- 年度營收：FY2022 141.1M → FY2023 75.8M → FY2024 99.4M → FY2025 88.3M USD。FY2022–FY2025 3 年 CAGR 為 -14.5%（FY2021 資料為 null，無法計算 4–5 年 CAGR）。FY2025 YoY 為 -11.1%。
- 季度營收：2025Q2 18.0M、2025Q3 28.0M、2025Q4 23.0M、2026Q1 26.9M、2026Q2 47.6M USD。2026Q2 YoY +164.8%，為近 5 季最高。
- TTM 營收（2025Q3–2026Q2 加總）為 125.5M USD，與 info 之 totalRevenue 125.509M 一致。
- 分部（產品線）營收拆分：DATA_UNAVAILABLE。工具僅提供 longBusinessSummary 之產品描述（磷化銦 InP 用於資料中心光連接、砷化鎵 GaAs 用於 Wi-Fi/IoT/衛星、鍺基板用於太陽能電池、高純度鎵等），未提供各產品線營收金額。依產品描述推論，2026Q2 營收暴增與資料中心光通訊相關需求有關，但此為推論，工具資料未直接證實。

**獲利能力**
- 毛利率（年度）：FY2022 36.9% → FY2023 17.6% → FY2024 24.0% → FY2025 12.7%。
- 毛利率（季度）：2025Q2 8.0%、2025Q3 22.3%、2025Q4 20.9%、2026Q1 29.6%、2026Q2 44.9%，呈明顯上升趨勢。TTM 毛利率 32.2%（info grossMargins 0.32184 一致）。
- 營業利益率：FY2022 10.1% → FY2023 -25.1% → FY2024 -12.6% → FY2025 -23.3%。2026Q2 營業利益 10.4M（營業利益率 21.9%），為單季明顯改善；TTM 營業利益 5.2M，TTM 營業利益率 4.2%。
- 注意：info 之 operatingMargins（0.219）實為 2026Q2 單季數字，非 TTM，不宜直接當作全年營業利益率。
- 淨利率：FY2022 11.2%、FY2023 -23.6%、FY2024 -11.7%、FY2025 -24.1%；2026Q2 淨利 11.1M（淨利率 23.4%）；TTM 淨利 4.05M（淨利率 3.2%，info profitMargins 0.0323 一致）。
- 2026Q2 淨利品質：營業利益 10.4M 加上淨利息收入 4.7M、權益法投資收益 0.4M 等，稅前淨利 15.1M，所得稅 2.1M。淨利息收入推估主要來自募集後之大額現金，屬非營業收益，其可持續性需於後續季度觀察。
- EPS：FY2025 diluted EPS -0.49；2026Q2 diluted EPS 0.17（損益表）／0.19（earnings_dates 報告值），兩者差異為資料來源不同，均以正數為準、需以正式 10-Q 核對。TTM EPS（info）0.04。
- ROE：info returnOnEquity 0.01012（約 1.0%，TTM）；以 FY2025 年底權益計算 ROE 約 -7.8%（淨利 -21.4M / 權益 273.3M）。
- ROIC：工具未直接提供。以 TTM 營業利益 5.2M × (1-21%) 除以 (權益 887.3M + 總負債所含有息負債 86.0M - 現金 417.2M) 估算，約 0.7%（估算值，方法為本報告推算）。
- 研發與費用：FY2025 R&D 9.0M（佔營收 10.2%）、SG&A 24.2M（佔營收 27.4%）。2026Q2 R&D 3.7M、SG&A 7.3M，合計營運費用 10.9M，佔營收 23.0%，費用率已大幅下降。

## Cashflow & balance sheet

**現金流量**
- 經營現金流（OCF）：FY2022 -8.8M、FY2023 +3.4M、FY2024 -12.1M、FY2025 -12.8M；TTM -5.8M（info operatingCashflow -5.761M 一致）。2026Q2 OCF 10.8M 為近 5 季最高，2026Q1 為 -11.7M。
- 資本支出（capex）：FY2022 28.5M、FY2023 10.5M、FY2024 5.8M、FY2025 6.0M；TTM 13.8M；2026Q2 單季 7.2M 為近 5 季新高，顯示擴產或設備投入恢復。
- 自由現金流（FCF = OCF - capex）：FY2022 -37.2M、FY2023 -7.1M、FY2024 -17.9M、FY2025 -18.8M；TTM -19.6M（由季度 CF 加總）。TTM FCF margin 為 -15.6%；FY2025 FCF margin 為 -21.3%。近 5 季僅 2025Q4（+1.3M）與 2026Q2（+3.6M）為正值，2026Q2 為近期最強單季。
- 注意：info freeCashflow 為 -44.4M，與季度 CF 推算之 -19.6M 不一致，本報告採用季度 CF 推算值，並標註差異。
- FCF / 淨利比：FY2025 與 TTM 淨利皆為負或接近零，比值無意義（n/m）。
- 折舊攤銷（D&A）：FY2025 9.1M；capex / D&A 比率 FY2025 為 0.66，顯示 2024–2025 年投資低於折舊，但 2026Q2 capex 已升至 D&A 約 2.9 倍（7.2 / 2.5）。
- 股份基礎報酬（SBC）：FY2025 3.3M，佔營收 3.7%。

**資產負債表（2026Q2，即 2026-06-30）**
- 總資產 1,097.2M USD（FY2025 年底為 433.8M，半年內增加約 153%）。
- 現金及約當現金 417.2M USD（2026Q1 為 107.1M，2025Q2 為 27.0M）。
- 總有息負債 86.0M USD（info totalDebt 為 101.5M，兩者差異於 info 欄位定義不同，報告以季度 BS 為主）。
- 淨現金：417.2M - 86.0M = 約 331.2M USD（以季度 BS 計算）。
- 流動比率 4.77（流動資產 598.8M / 流動負債 125.7M；info currentRatio 4.765 一致）。2025Q2 流動比率約 1.82，改善顯著。
- 負債權益比：有息負債 / 股東權益 = 86.0M / 887.3M = 9.7%；info debtToEquity 為 10.67（%）。
- 股東權益 887.3M（FY2025 年底 273.3M，2025Q2 179.7M）；每股淨值（BVPS）約 13.5 USD（以 2026Q2 股東權益與期末股數 65.57M 計算），info bookValue 為 13.767。
- 少數股東權益 64.6M（工具未細分其來源）。
- 存貨 96.3M USD（2025Q2 80.1M），存貨金額高於 2025Q2，需關注庫存周轉；存貨佔總資產比例於 2026Q2 約 8.8%。
- 應收帳款：FY2025 26.8M（FY2024 25.6M），無明顯惡化跡象，但帳齡資料 DATA_UNAVAILABLE。
- 負債結構：流動負債 125.7M 佔總負債 145.3M 之約 86%；長期負債極少（FY2025 長期借款與租賃合計 1.4M）。

## Capital allocation & insider signal

**資本配置**
- 股利：普通股未配發股利（dividendYield 0）。特別股股息 FY2025 為 177K USD/年（特別股 883K 股），金額極小。
- 買回：FY2022–FY2025 無顯著買回（僅 FY2021 有 -1.1M 之股票買回）。
- 股權募集（最關鍵之資本配置行為）：
  - 股數（Ordinary Shares）：FY2024 年底 45.36M → FY2025 年底 55.34M（+22.0%）→ 2026Q1 底 55.58M → 2026Q2 底 65.57M。
  - 2026Q2 融資現金流為 +621.4M USD，股權淨值由 2026Q1 的 274.9M 增至 887.3M，屬大規模權益募集。募集方式（公開增發、私募或其他）工具資料未明確標示，此處僅依 BS 與 CF 推估。
  - 股數 YoY（2025Q2 46.08M → 2026Q2 65.57M）增加 +42.3%，對既有股東每股盈餘與股權結構稀釋顯著。
- 2025Q4 亦有約 95M USD 之股票選擇權行權及股票發行收入（Q4 融資現金流 95.3M）。

**內部人交易（過去 6 個月，2026-04-15 至 2026-10-15）**
- 6 個月內 Form 4 申報之賣出合計約 29.8M USD（以 Yahoo 交易明細加總）。其中：
  - CEO Morris S. Young：2026-06-02 賣出 197,498 股，價格 112.39–113.33 USD，金額約 22.3M USD，為期間最大單筆。
  - 董事 Jesse Chen：2026-06-02 至 2026-06-12 多筆賣出，合計約 5.2M USD（含 22,000 股 @ 88.55–95.77）。
  - 董事 David C. Chang：2026-06-15 賣出 8,333 股，約 0.93M USD。
  - 董事 Leonard J. LeBlanc：2026-08-07、2026-08-17 賣出，合計約 0.6M USD。
- 6 個月內公開市場買入：0 筆。
- 6 個月內賣出合計 29.8M USD 佔市值（4,038.7M USD）約 0.74%，規模屬小；但全部賣出價格集中於 86–115 USD 區間，當前股價 61.59 USD 已低於該區間約 28–47%，賣出時點相對高點。
- 過去 24 個月（2024-10 至 2026-08）除 2025-02-25 CEO 一筆 30,000 股 @ 1.36 USD 之公開買入（約 40.9K USD）外，無其他公開市場買入紀錄。
- 注意：工具未揭露交易是否屬 10b5-1 預定計畫，亦未揭露 CEO 6/2 的行權（85,703 股 @ 5.21）與賣出是否相關，需以 SEC Form 4 核對。
- 內部人持股比例 3.98%（heldPercentInsiders）。

**股東結構**
- 機構持股 74.67%（357 家機構，institutionsCount 357）。
- 前幾大機構（2026-06-30 申報）：BlackRock 7.74%、Marex Group 5.43%（持股較前期增加約 444%）、Jane Street 5.38%、Vanguard Capital Management 4.15%、Shaw D.E. 3.43%。
- 空頭部位：流通空頭股數 10.79M，佔已發行股數約 16.5%，佔流通股 (float 61.6M) 約 17.2%；shortRatio 1.25（回補天數）。空頭比例高，波動放大風險。

## Valuation

- 現價 61.59 USD（regularMarketPrice；previousClose 64.63；當日 -4.70%；資料為 cache 快照，marketState 為 PRE）。
- 市值 4,038.7M USD（sharesOutstanding 65.57M）；企業價值 EV 3,706.3M USD（info enterpriseValue）。
- 本益比：
  - Trailing P/E 1,539.8x（TTM EPS 0.04）：數值極端，無參考價值（n/m）。
  - Forward P/E 27.4x（forwardEps 2.25，共識 5 家）。
  - 當年度 P/E 約 71.0x（epsCurrentYear 0.868）。
  - PEG 12.09（info pegRatio），僅供參考。
- EV/Revenue（TTM）29.5x；EV/EBITDA（TTM EBITDA 13.4M）275.6x，因 TTM EBITDA 基數小而無參考價值；若以 Forward 基準無 EBITDA 共識資料（DATA_UNAVAILABLE）。
- P/S（TTM）32.2x。
- P/FCF：TTM FCF 為負（-19.6M），n/m。
- P/B 4.47x（以 BVPS 13.77 計）。
- 分析師共識：mean target 91.6 USD、median 93.0、low 55.0、high 125.0，共 5 家，recommendationKey 為 none。以 mean 計算隱含上行空間約 +48.7%，但樣本數少、覆蓋不完整。
- 產業中位數（sector median）：DATA_UNAVAILABLE（工具未提供同業比較資料，故不提供估計值以免臆造）。定性上，AXTI 屬半導體設備與材料，同業通常以 Forward P/E 與 EV/Sales 比較，AXTI 目前 Forward P/E 27.4x 與 EV/Sales 29.5x（TTM）均屬高位，需以成長持續性支撐。
- 價格位置：52 週區間 4.35–143.16 USD；現價較 52 週高點回落 57.0%，較 50 日均線 71.49 低 13.8%，較 200 日均線 62.65 低 1.7%；52 週漲幅 +1,149%。Beta 1.86。

## Key catalysts

- 下次財報：2026-10-29（earnings_dates 標示為 20:00 UTC 之預估時點，isEarningsDateEstimate 為 false）；共識 EPS 估計 0.31 USD。
- 上一季（2026-07-30 公布）：EPS 0.19 vs 估計 0.07，超預期 +163.9%；營收 47.6M USD（YoY +164.8%）。
- 過去 EPS 超預期紀錄：近 16 季中 EPS 超預期 11 季；2025 年 2 月、5 月、7 月三次財報不及預期（Surprise 分別為 -138.1%、-37.7%、-11.9%）。
- 股權募集後之資本用途（擴產、研發或償債）：工具未揭露 use of proceeds，DATA_UNAVAILABLE。
- 2026Q2 capex 7.2M 之增長是否延續為擴產訊號：需以後續季度觀察。
- 產品組合轉移：InP 用於資料中心光通訊之描述，與 2026Q2 營收暴增之時序吻合，但工具未提供分部數據，無法量化。
- 內部人賣出（6/2 CEO 大額賣出）與空頭比例 16.5%，為短期情緒面催化劑來源。
- 管理層與分析師指引（guidance）：工具未提供，DATA_UNAVAILABLE。

## Metrics table

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 (2026Q2) | 47.6M USD | +164.8% | DATA_UNAVAILABLE | 強勁成長，但單季基數低、不確定是否延續 |
| 營收 TTM | 125.5M USD | n/a（前期 TTM 資料不足） | DATA_UNAVAILABLE | 規模仍小 |
| 營收 FY2025 | 88.3M USD | -11.1% (vs FY2024) | DATA_UNAVAILABLE | 年度衰退，2025 下半年起回升 |
| 3Y Revenue CAGR (FY2022–FY2025) | -14.5% | n/a | DATA_UNAVAILABLE | 長期負成長 |
| 毛利率 (2026Q2) | 44.9% | +36.9 pt (vs 2025Q2 8.0%) | DATA_UNAVAILABLE | 明顯改善 |
| 毛利率 TTM | 32.2% | n/a | DATA_UNAVAILABLE | 中等，仍受週期影響 |
| 營業利益率 (2026Q2 單季) | 21.9% | 由 -37.5% 轉正 | DATA_UNAVAILABLE | 單季轉正，TTM 僅 4.2% |
| 淨利率 TTM | 3.2% | n/a | DATA_UNAVAILABLE | 微利 |
| ROE (TTM, info) | 1.0% | n/a | DATA_UNAVAILABLE | 偏低 |
| ROIC (估算) | 約 0.7% | n/a | DATA_UNAVAILABLE | 偏低，估算值 |
| OCF TTM | -5.8M USD | n/a | DATA_UNAVAILABLE | 負向 |
| FCF TTM | -19.6M USD | n/a | DATA_UNAVAILABLE | 負向，2026Q2 單季 +3.6M |
| FCF margin TTM | -15.6% | FY2025 -21.3% | DATA_UNAVAILABLE | 仍為負 |
| FCF / 淨利 | n/m | n/a | DATA_UNAVAILABLE | 無參考價值 |
| Capex (2026Q2) | 7.2M USD | 2025Q2 0.3M（YoY 顯著增加） | DATA_UNAVAILABLE | 投資回升 |
| 現金 (2026Q2) | 417.2M USD | +1,445% (vs 2025Q2 27.0M) | DATA_UNAVAILABLE | 強化，源自股權募集 |
| 有息負債 (2026Q2) | 86.0M USD | +47.8% (vs 2025Q2 58.2M) | DATA_UNAVAILABLE | 可控但增加 |
| 淨現金 (2026Q2) | 約 331.2M USD | n/a | DATA_UNAVAILABLE | 財務彈性提升 |
| 流動比率 | 4.77 | 1.82 (2025Q2) | DATA_UNAVAILABLE | 強 |
| 負債權益比 (有息負債/股東權益) | 9.7% | 2025Q2 約 32.4% | DATA_UNAVAILABLE | 低 |
| 股東權益 (2026Q2) | 887.3M USD | +393.7% (vs 2025Q2 179.7M) | DATA_UNAVAILABLE | 因募集大增 |
| 流通股數 | 65.57M | +42.3% (vs 2025Q2 46.08M) | DATA_UNAVAILABLE | 高度稀釋 |
| 股利殖利率 | 0.0% | n/a | DATA_UNAVAILABLE | 無股利 |
| 買回 | 無 (FY2022–FY2025) | n/a | DATA_UNAVAILABLE | 無 |
| 內部人 6 個月賣出 | 約 29.8M USD | n/a | DATA_UNAVAILABLE | 偏負向，佔市值 0.74% |
| 內部人 6 個月公開買入 | 0 筆 | n/a | DATA_UNAVAILABLE | 無買入訊號 |
| 空頭比例 (佔流通股) | 17.2% | n/a | DATA_UNAVAILABLE | 偏高 |
| Trailing P/E | 1,539.8x | n/a | DATA_UNAVAILABLE | n/m，無參考價值 |
| Forward P/E | 27.4x | n/a | DATA_UNAVAILABLE | 偏高，視成長兌現而定 |
| EV/EBITDA (TTM) | 275.6x | n/a | DATA_UNAVAILABLE | n/m，EBITDA 基數過小 |
| P/S (TTM) | 32.2x | n/a | DATA_UNAVAILABLE | 高 |
| P/FCF | n/m (FCF 為負) | n/a | DATA_UNAVAILABLE | n/m |
| P/B | 4.47x | n/a | DATA_UNAVAILABLE | 偏高 |
| 分析師目標價 (mean) | 91.6 USD | 隱含上行 +48.7% | DATA_UNAVAILABLE | 樣本 5 家，參考性有限 |
| Beta | 1.86 | n/a | DATA_UNAVAILABLE | 高波動 |

## Red flags

- 歷史獲利與現金流長期為負：FY2023 淨損 -17.9M、FY2024 -11.6M、FY2025 -21.3M；FY2022–FY2025 FCF 合計為負。
- 2026Q2 獲利改善之可持續性存疑：單季 EBIT 10.4M 為近 5 季最高，且約 4.7M 淨利息收入（推估來自募集後現金）佔稅前淨利之可觀比重，TTM 營業利益僅 5.2M。
- 股權大幅稀釋：流通股數 YoY +42.3%；2026Q2 融資現金流 +621.4M，募集用途工具未揭露。
- 內部人大額賣出：6 個月內約 29.8M USD，含 CEO 2026-06-02 單筆約 22.3M USD；期間無公開市場買入。
- 估值極端：Trailing P/E 1,539.8x、EV/EBITDA 275.6x、P/S 32.2x，Forward P/E 27.4x 之前提為共識 EPS 2.25（僅 5 家），盈餘預測風險高。
- 空頭比例高：空頭股數佔流通股 17.2%，加上 Beta 1.86，股價波動風險大。
- 股價自 52 週高點回落約 57%，較 50 日均線低 13.8%，趨勢面轉弱。
- 資料一致性問題（已依來源分別標註，不作為事實結論）：
  - info operatingMargins 0.219 實為 2026Q2 單季值，非 TTM；
  - info freeCashflow -44.4M 與季度 CF 推算 -19.6M 不一致；
  - info totalDebt 101.5M 與季度 BS 86.0M 不一致；
  - info ebitda 13.4M 與季度 EBITDA 加總 14.7M 不一致；
  - info TTM EPS 0.04 與季度 diluted EPS 加總 0.02 不一致；
  - Q2 EPS 0.17（損益表）與 0.19（earnings_dates）不一致。
- 資料快取時效：source 為 cache（cached_at 2026-10-15T11:16–11:19 UTC），價格為 PRE 狀態快照；fulldayPrice 57.52 與 regularMarketPrice 61.59 不同，以 regularMarketPrice 為準。報告日 2026-10-15 之後的資料未使用（下次財報 2026-10-29 為未來事件）。
- 資料缺口：分部營收、客戶集中度、管理層指引、募集用途、產業中位數、ROIC 官方值均為 DATA_UNAVAILABLE。

FUNDAMENTALS REPORT COMPLETE
