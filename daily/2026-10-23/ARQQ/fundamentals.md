# Fundamentals — ARQQ as of 2026-10-23

## Executive summary
Arqit Quantum Inc. (ARQQ, NasdaqCM) 財務體質目前屬於高風險等級: FY2025 (截至 2025-09-30) 營收僅 USD 0.53M、營業虧損 USD 35.2M、經營現金流 USD -29.6M，屬於典型的研發階段燒錢型態。資產負債表以現金為主 (2026-03-31 現金 USD 28.9M、總負債 USD 2.2M)，短期償債能力不是問題，但以近期 TTM 營業現金流 USD -42.7M 推算，現金跑道可能只剩約 8 個月，後續增資或稀釋風險很高。估值方面，P/E、P/FCF、EV/EBITDA 皆為負值無意義，P/S 高達約 253x (TTM)，以基本面來看估值缺乏支撐。

## Revenue & profitability
- **營收規模與趨勢**: 依 yfinance annual income statement (USD)，營收 FY2022 為 USD 7.21M，FY2023 為 USD 0.64M，FY2024 為 USD 0.29M，FY2025 為 USD 0.53M。
  - 3 年營收 CAGR (FY2022 至 FY2025): 約 -58%。
  - FY2025 YoY: 約 +81% (由 USD 0.293M 增至 USD 0.530M)，但基數極低，不足以代表商業化趨勢改善。
  - info 欄位 `revenueGrowth` 為 8.299 (即約 +830%)，與年度數字口徑不同，推測為季度或 TTM 口徑，本報告不採用，標示為口徑不一致。
  - TTM 營收 (info `totalRevenue`): USD 1.086M。
- **業務組成**: info.longBusinessSummary 描述為 QuantumCloud 平台 (PaaS 加密金鑰服務)，透過衛星與地面平台提供服務，另有維護支援與專業服務。yfinance 無分部營收資料，segment mix: DATA_UNAVAILABLE。
- **毛利**: info `grossMargins` 為 49.7%，`grossProfits` 為 USD 0.54M (TTM)。年度毛利明細 DATA_UNAVAILABLE。
- **營業利益與淨利**: FY2025 Operating Income 為 USD -35.17M，FY2024 為 USD -37.37M，FY2023 為 USD -67.46M。FY2025 Net Income 為 USD -35.34M，FY2024 為 USD -56.82M，FY2023 為 USD -74.53M。
  - 營業利益率與淨利率 (對營收) 皆超過 -6,000%，數字已失去經濟意義，不做比較。
  - info `operatingMargins` 為 -49.3 (即 -4,932%)，同樣僅作為燒錢強度指標。
  - FY2022 淨利 USD +65.08M 與 FY2022 營業虧損 USD -50.23M 不一致，推測包含非營業項目 (例如認股權證公允價值變動)，需以 10-K 原文確認，本報告標示為 n/a 不做解讀。
- **ROE / ROA / ROIC**: info `returnOnEquity` 為 -220.2%，`returnOnAssets` 為 -95.5%。以 FY2025 年末權益 USD 27.24M 反算，淨利/權益約 -130%。ROIC 無法由 yfinance 直接取得，以 EBIT 及投入資本反算 (FY2025 EBIT USD -37.57M / Invested Capital USD 27.24M) 約 -138%，僅供參考。
- **每股盈餘**: FY2025 Diluted EPS USD -2.56 (驗算: -2.56 × 13.79M 加權股數 ≈ -35.3M，與淨利一致)；FY2024 USD -11.23；FY2023 USD -14.17。TTM EPS USD -3.21；forward EPS USD -1.06。
- **季度損益表**: yfinance quarterly_fin 回傳空陣列，季度損益 DATA_UNAVAILABLE。

## Cashflow & balance sheet
- **現金流量**:
  - FY2025 經營現金流 USD -29.55M (FY2024 USD -34.13M，FY2023 USD -32.83M)。
  - FY2025 資本支出 USD -0.55M，自由現金流 USD -30.10M (FY2024 USD -37.45M，FY2023 USD -48.95M)。
  - info TTM: 經營現金流 USD -42.75M、自由現金流 USD -19.70M。兩者數字不一致 (TTM 經營現金流惡化但自由現金流較小，隱含資本支出為正值，不合理)，應視為資料口徑問題，建議以 quarterly_cf 或 10-Q 驗證。quarterly_cf 回傳空陣列，無法驗證。
  - FCF margin (FY2025): 約 -5,680% (營收過小)，無實質意義。
  - FCF / NI: 淨利為負，比率 n/a。
  - 品質判定: 營運現金流與淨利同方向為負，現金流 "品質" 並非問題重點，問題在於收入無法覆蓋成本。
- **資產負債表 (年末 FY2025, 2025-09-30)**:
  - 現金及約當現金 USD 36.98M，總負債 USD 15.62M，總負債含短期負債 USD 0.72M (Total Debt)。
  - 總資產 USD 42.85M，股東權益 USD 27.24M。
  - 流動資產 USD 40.02M，流動負債 USD 14.90M，流動比率約 2.69x。
  - 淨現金 (現金 - 總債務): 約 USD +36.3M。
- **資產負債表 (最新季 2026-03-31)**:
  - 現金 USD 28.86M，總債務 USD 2.17M，淨現金約 USD +26.7M。
  - 流動資產 USD 32.16M，流動負債 USD 6.59M，流動比率 4.88x (與 info `currentRatio` 一致)。
  - 股東權益 USD 28.51M，Debt/Equity 約 7.6% (yfinance `debtToEquity` 7.62 為百分比口徑)。
  - 股本: 2026-03-31 普通股 16.58M 股 (FY2025 年末為 15.29M 股)。
  - 2025-09-30 至 2026-03-31 現金下降 USD 8.12M (-22%)。
- **現金跑道推估 (本報告推算，非官方數字)**:
  - 以 TTM 經營現金流 USD -42.75M 年化，月均燒錢約 USD 3.56M，Mar-31 現金 USD 28.86M 約可支撐約 8 個月，即約至 2026 年 11 月底至 12 月初。
  - 以 FY2025 經營現金流 USD -29.55M 年化，月均約 USD 2.46M，約可支撐約 11.7 個月，即約至 2027 年 3 月。
  - 2026-03-31 至 2026-10-23 之間已有約 7 個月燒錢，若無新增融資，現金可能已降至 USD 10M 以下。實際數字需等 FY2026 10-K 或 2026 Q4 公告確認。
  - 股數由 2026-03-31 的 16.58M 增至 info `sharesOutstanding` 17.40M (+0.82M，約 +4.9%)，顯示期間可能有增發、ATM 或股權激勵，但無法確認金額。
- **負債品質**: 總債務極低 (USD 0.7M 至 2.2M)，無利息負擔問題。FY2025 利息費用 USD 0.05M，利息收入 USD 1.23M。

## Capital allocation & insider signal
- **資本支出**: 持續縮減，FY2022 USD -24.43M，FY2023 USD -16.12M，FY2024 USD -3.33M，FY2025 USD -0.55M。顯示公司已大幅收縮資本投入。
- **股利與回購**: 無股利 (Cash Dividends Paid 為 0)，無回購紀錄。股利覆蓋率 n/a。
- **融資來源 (主要現金來源)**:
  - 股票發行所得: FY2025 USD 37.18M，FY2024 USD 13.08M，FY2023 USD 45.08M，FY2022 USD 0。
  - 股權融資是公司維持營運的主要資金來源，持續稀釋股東。
- **股本稀釋**: 普通股由 2024-09-30 的 11.55M 股增至 2025-09-30 的 15.29M 股 (+32%)，目前 info `sharesOutstanding` 為 17.40M，較 2025-09-30 再增約 +14%。FY2024 有 1:25 反向分割 (lastSplitDate 約 2024-09-25，lastSplitFactor "1:25")，股數歷史需以分割口徑閱讀。
- **股權結構**: 機構持股 82.6% (94 家機構)，內部人持股 2.8%。流通股 (floatShares) 僅 5.01M 股，為總股本的約 29%，流動性有限。
- **內部人交易 (最近 6 個月，yfinance insider 欄位)**:
  - 2026-10-06 多名內部人以 USD 24.19 賣出: Andrew Leaver (CEO) 2,398 股 (USD 58.0K)、Patrick Willcocks (General Counsel) 555 股 (USD 13.4K)、Paul Feenan 504 股 (USD 12.2K)、Nicholas Nilan 493 股 (USD 11.9K)、Ben Wilder (COO) 218 股 (USD 5.3K)、Garth Ritchie (Director) 118 股 (USD 2.9K)。
  - 2026-10-13 CEO Andrew Leaver 以 USD 16.40 賣出 2,573 股 (USD 42.2K)。
  - 2026-10-12 CEO Andrew Leaver 另有 5,209 股一筆，交易類型與金額欄位空白，性質未確認 (可能為税務扣繳或既有股份處分)。
  - 2026-10-16 三名董事 (Garth Ritchie 1,021 股、Manfredi Lefebvre d'Ovidio 817 股、Carlo Calabria 919 股) 有股份變動紀錄，欄位無交易說明，性質未確認 (可能為董事報酬股份發放)。
  - 已揭露的賣出合計約 6,859 股、約 USD 145.9K (依 yfinance 單價與金額欄位計算)，約佔市值 USD 275.1M 的 0.05%。
  - 本期間未見內部人買進紀錄。
  - 解讀: 絕對金額很小，但 CEO 在股價由 USD 24.19 回落至 USD 16.40 區間內賣出，且全部為賣出，不構成正面內部人信號。金額相對市值微小，不能單獨視為強烈看空訊號。
- **機構與空單**: info 顯示 `sharesShort` 2.26M 股 (前月 2.60M)，`shortRatio` 6.12 天，`shortPercentOfFloat` 17.8%。但依 sharesShort / floatShares 反算約 45%，與 yfinance 所列 17.8% 不一致，資料需再確認。

## Valuation
以 2026-10-23 盤前價 USD 15.81 (previous close USD 16.40，-3.6%) 計算:
- **市值與企業價值**: 市值 USD 275.1M，企業價值 (EV) USD 235.5M (yfinance 口徑)。
- **P/E**: TTM P/E 為 n/a (EPS 為負)。Forward P/E 為 -14.9x，因 forward EPS USD -1.06 為負，無實質意義，標示為 n/a。
- **EV/EBITDA**: TTM EBITDA USD -49.9M，EV/EBITDA 為 -4.7x，因 EBITDA 為負，標示為 n/a。
- **P/S**: TTM P/S 約 253x (info `priceToSalesTrailing12Months` 253.3；驗算 275.1M / 1.086M = 253.3)；EV/Revenue 約 216.8x。
- **P/FCF**: TTM FCF 為負，n/a。
- **P/B**: 約 9.2x (價格 USD 15.81 / BVPS USD 1.719)。
- **Sector median (估計)**: Software - Infrastructure 同業中位數估計 P/S 約 4-8x，forward P/E 約 25-40x (多數獲利公司)，EV/EBITDA 約 15-30x。以上為粗估，非 yfinance 提供。ARQQ 的 P/S 為同業數十倍，估值溢價缺乏營收與獲利支撐。
- **技術面參考 (非基本面，僅列示)**: 52 週區間 USD 11.52 至 49.33，目前價位距 52 週低點約 +37%，距高點約 -68%；50 日均線 USD 20.47，200 日均線 USD 18.47，股價位於兩條均線下方。52 週股價變化 -59.5%。Beta 2.79。

## Key catalysts
- **FY2026 年報 (財年截止 2026-09-30)**: 財年已於 2026-09-30 結束，年報預計 2026 年底前公布，為最近的基本面重要事件。info `nextFiscalYearEnd` 為 2027-09-30 (新財年)。
- **下一次財報日期**: yfinance earnings_dates 顯示 2026-12-09 (Earnings Date)，但 EPS estimate 與 reported EPS 均為 null，此日期屬預估，需以公司公告為準。
- **資金與稀釋事件**: 依現金跑道推估，融資 (股權或債務) 公告可能在近期出現，對股價與股權稀釋影響最大。目前無公開的融資條款資料，DATA_UNAVAILABLE。
- **營收與合約**: 無季度營收資料，無法驗證 TTM 營收 USD 1.09M 的組成與成長趨勢。近期合約宣布與客戶資料 DATA_UNAVAILABLE。
- **管理層與公司名稱**: info `nameChangeDate` 為 2026-10-23 (與 as-of 日同日)，`prevName` 為 Centricus Acquisition Corp. (SPAC 前身)，公司名稱或結構變更需以公告為準，未能確認。
- **資料時效**: 價格與 fast_info 資料來源為快取 (feed: cnyes, cached_at 2026-10-23T11:26 UTC)，info marketState 為 PRE，當日盤中價格可能與本報告不同。若有 2026-10-23 之後的資料，本報告以 as-of 日期為準不納入。

## Metrics table
單位: 金額一律 USD M (百萬美元)，美股 ADR 不使用 億 單位。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 (FY2025, USD M) | 0.53 | +81% (vs FY2024 0.29) | n/a (同業通常 >100M) | 極弱 |
| 營收 3Y CAGR (FY2022-FY2025, USD M) | -58% | n/a | 估計 +5% 至 +15% | 極弱 |
| TTM 營收 (USD M) | 1.09 | n/a | n/a | 極弱 |
| 毛利率 (TTM, info) | 49.7% | n/a | 估計 65% 至 75% | 偏弱 |
| 營業利益率 (FY2025) | 約 -6,636% (營收過小) | n/a | 估計 -10% 至 +20% | 不適用 |
| 淨利 (FY2025, USD M) | -35.34 | 較 FY2024 -56.82 改善約 38% | 估計為正或小幅負值 | 弱 |
| Diluted EPS (FY2025, USD) | -2.56 | 較 FY2024 -11.23 (分割前後口徑需注意) | n/a | 弱 |
| ROE (TTM, info) | -220% | n/a | 估計 +10% 至 +20% | 弱 |
| ROA (TTM, info) | -95.5% | n/a | n/a | 弱 |
| 經營現金流 (FY2025, USD M) | -29.55 | 較 FY2024 -34.13 改善約 13% | n/a | 弱 |
| 自由現金流 (FY2025, USD M) | -30.10 | 較 FY2024 -37.45 改善約 20% | n/a | 弱 |
| TTM 經營現金流 (info, USD M) | -42.75 | 與 FY2025 相比惡化 | n/a | 警示 |
| FCF / NI | n/a (淨利為負) | n/a | 估計 >0.9 為健康 | n/a |
| 現金 (2026-03-31, USD M) | 28.86 | 較 2025-09-30 的 36.98 下降 22% | n/a | 中性偏弱 |
| 總債務 (2026-03-31, USD M) | 2.17 | 較 2025-09-30 的 0.72 增加 | 估計 低 | 良好 |
| 淨現金 (2026-03-31, USD M) | +26.7 | 較 2025-09-30 的 +36.3 下降 | n/a | 中性 |
| 流動比率 (2026-03-31) | 4.88x | 較 2025-09-30 的 2.69x 上升 | 估計 1.5x 至 2.5x | 良好 |
| Debt / Equity (2026-03-31) | 約 7.6% | n/a | 估計 <50% | 良好 |
| 現金跑道 (推估, 月) | 約 8 (TTM 燒錢) 至 約 12 (FY2025 燒錢) | n/a | n/a | 紅旗 |
| 資本支出 (FY2025, USD M) | -0.55 | 較 FY2024 -3.33 下降 84% | n/a | 已大幅收縮 |
| 股票發行所得 (FY2025, USD M) | 37.18 | 較 FY2024 13.08 增加 | n/a | 依賴股權融資 |
| 普通股股數 (info, M 股) | 17.40 | 較 2025-09-30 的 15.29 增加約 14% | n/a | 稀釋 |
| 內部人賣出 (6 個月, USD K) | 約 145.9 (已揭露) | n/a | 市值占比約 0.05% | 中性偏負面 |
| 機構持股比例 | 82.6% | n/a | n/a | 中性 |
| 空單佔流通股 (yfinance) | 17.8% | n/a | n/a | 資料待確認 |
| P/E (TTM) | n/a (EPS 為負) | n/a | 估計 25x 至 40x | 不適用 |
| Forward P/E | n/a (forward EPS 為負) | n/a | 估計 25x 至 40x | 不適用 |
| EV/EBITDA (TTM) | n/a (EBITDA 為負) | n/a | 估計 15x 至 30x | 不適用 |
| P/S (TTM) | 約 253x | n/a | 估計 4x 至 8x | 極度昂貴 |
| P/FCF (TTM) | n/a (FCF 為負) | n/a | 估計 20x 至 40x | 不適用 |
| P/B | 約 9.2x | n/a | 估計 3x 至 6x | 偏貴 |
| Beta | 2.79 | n/a | 估計 1.0 至 1.3 | 波動極高 |

## Red flags
- 營收過小 (FY2025 USD 0.53M)，且 3 年 CAGR 約 -58%，商業化進展不足以覆蓋營運成本。
- 營業虧損連續多年 (FY2023 至 FY2025 皆超過 USD 35M)，營業利益率失去比較意義。
- 現金跑道偏短: 以 TTM 經營現金流推算約 8 個月，以 FY2025 推算約 12 個月；2026-03-31 後的現金餘額 DATA_UNAVAILABLE，存在近期融資或稀釋壓力。
- 股權融資為主要資金來源 (FY2025 USD 37.2M)，股數較 FY2025 年末增加約 14%，且 FY2024 曾有 1:25 反向分割。
- 流通股僅約 5.0M 股，流動性有限，加上 Beta 2.79 與 52 週 -59.5%，價格波動風險高。
- 估值 P/S 約 253x，與基本面 (營收規模) 嚴重脫節。
- 內部人在 2026-10-06 至 2026-10-13 期間持續賣出，包括 CEO 於 USD 16.40 賣出；雖金額小，但方向一致為賣出，未見內部人買進。
- 資料完整性問題: 季度損益與季度現金流 DATA_UNAVAILABLE；TTM 經營現金流 (-42.75M) 與自由現金流 (-19.70M) 數字不一致；空單比例 (17.8%) 與 sharesShort / floatShares 反算 (約 45%) 不一致；年度營收成長 (+81%) 與 info revenueGrowth (+830%) 口徑不同。Yahoo cookie/crumb 取得失敗，部分資料來自快取。以上數字在採用前需以 SEC 10-K / 10-Q 原文交叉驗證。
- 內部人 2026-10-12 CEO 5,209 股與 2026-10-16 三名董事股份變動的交易性質 (賣出、稅務扣繳或授予) 未能確認。
- 下一次財報日期 2026-12-09 為預估值，EPS 預期為 null，市場對 FY2026 數據缺乏共識。

FUNDAMENTALS REPORT COMPLETE
