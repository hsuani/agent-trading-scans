# Fundamentals — S (SentinelOne, Inc., NYSE) as of 2026-10-16

## Executive summary
SentinelOne 財務健康度屬「流動性充足、無實質負債、但獲利能力仍弱」的型態: TTM 營收 1,098.7M USD、YoY +20.6%，淨現金約 640M USD，但 FY26 GAAP 淨利率 -45.0%，SBC 佔營收 29.7%，扣除 SBC 後的 FCF 明顯為負。估值面以 EV/Revenue 6.6x 來看不算極端，但 P/FCF 約 150x 以上、forward P/E 49.5x（基準不明），以現金流與 SBC 調整角度看偏貴。整體判讀: 財務體質中性偏弱，估值吸引力偏低，但非財務危機型態。（本段僅為基本面評估，不構成交易建議。）

## Revenue & profitability

**營收與成長**
- 年度營收 (FY 結束於 1 月底): FY23 422.2M → FY24 621.2M → FY25 821.5M → FY26 1,001.3M USD。
- FY26 YoY +21.9%；3 年 CAGR (FY23→FY26) 約 33.4%；2 年 CAGR (FY24→FY26) 約 27.0%。成長率呈逐年放緩: FY24 YoY 約 +47.1%、FY25 約 +32.2%、FY26 約 +21.9%。
- 季度營收: Q3 FY26 (Oct-25) 258.9M → Q4 FY26 (Jan-26) 271.2M → Q1 FY27 (Apr-26) 276.7M → Q2 FY27 (Jul-26) 292.0M USD。Q2 FY27 YoY 為 +20.6% (Q2 FY26 242.2M)。QoQ 成長: +6.9% / +4.7% / +2.0% / +5.5%，Q1 FY27 的序列成長明顯放緩。
- info.revenueGrowth = 0.206，與 Q2 FY27 YoY 一致。
- 分部: info.longBusinessSummary 僅描述產品線 (Singularity Platform、Purple AI、SIEM、Endpoint、Cloud、Identity、Exposure 等)，無分部營收數字，**分部營收 n/a**。

**獲利能力**
- 毛利率 (GAAP): FY23 65.9% → FY24 71.1% → FY25 74.3% → FY26 74.1%。Q2 FY27 為 72.1%，相較 Q2 FY26 的 75.0% 下降約 2.9 個百分點，為需追蹤的警訊。
- 營業利益率 (GAAP): FY23 -95.4% → FY24 -59.8% → FY25 -40.1% → FY26 -30.9%。Q2 FY27 為 -22.7%，Q2 FY26 為 -31.7%，YoY 改善約 9 個百分點。
- 自行估算 (非官方 non-GAAP): FY26 營業利益 -309.0M + SBC 297.6M + D&A 54.9M = +43.5M，約 4.3% 營業利益率；Q2 FY27 同方法約 15.3%。此為本報告自行加回計算，非公司揭露口徑。
- 淨利率 (GAAP): FY25 -35.1% → FY26 -45.0%，淨虧損由 -288.4M 擴大至 -450.7M。主因為 FY26 稅費 171.0M（在稅前虧損 -279.7M 的情況下），以及 FY26 Q2 FY27 的其他費用 -26.8M 與特殊費用 (Special Income Charges) -24.4M，性質資料中未揭露。**FY26 稅費 171.0M 的性質 (估值備抵、海外稅或一次性) 資料中未揭露，需於 10-K 內確認。**
- 每股盈餘 (GAAP diluted): FY23 -1.36 / FY24 -1.15 / FY25 -0.92 / FY26 -1.37。TTM EPS -1.01 (4 季加總: -0.27 / -0.23 / -0.33 / -0.18，與 info.trailingEps 吻合)。
- ROE -23.0%；ROA -7.6% (info)。ROIC 以 EBIT / 期末 Invested Capital 近似: -309.0M / 1,437.1M ≈ -21.5%，為本報告估算。

## Cashflow & balance sheet

**現金流品質**
- 營運現金流 (OCF): FY23 -193.3M → FY24 -68.4M → FY25 +33.7M → FY26 +76.6M。
- 資本支出 (Capex): FY26 -24.9M，佔營收約 2.5%；FY25 -27.1M。
- FCF (OCF - Capex，yfinance 口徑): FY23 -212.1M → FY24 -87.1M → FY25 +6.6M → FY26 +51.7M。FY26 FCF margin 5.2%，FY25 為 0.8%。
- FCF / NI: NI 為負，比率 n/m。
- **資料不一致**: info.freeCashflow = 296.9M，但 FY26 年報 FCF = 51.7M、以季度加總 (Q3 FY26 ~ Q2 FY27 FCF 列) 的 TTM FCF 約 30.9M，info.operatingCashflow 57.3M 則與季度加總吻合。本報告採用季度/年報推算值，不採 info 的 296.9M。
- 季度 FCF 波動大 (Q1 FY27 +30.7M、Q2 FY27 -13.3M)，Q1 FY27 的 FCF 包含應收帳款回收約 +108M 的時序影響，非穩定結構性改善。
- **SBC 負擔**: FY26 SBC 297.6M，佔營收 29.7% (FY25 為 32.6%，比率略降但仍極高)。FCF - SBC = 51.7 - 297.6 = -245.9M（FY26）。Q2 FY27 SBC 92.1M，佔營收 31.5%。

**資產負債表**
- Q2 FY27 (2026-07-31): 現金及約當現金 201.0M + 短期投資 454.3M = 現金與短期投資合計 655.2M USD (Q2 FY26 為 810.8M，YoY -19.2%)。
- 負債: FY26 總債務 15.0M (全為租賃負債)；Q2 FY27 的債務欄位為 null (yfinance 未揭露)。info.totalDebt = 0，與 FY26 年報 15.0M 不一致，**以年報 15.0M 為準**。
- 淨現金 (估算): 655.2M - 15.0M ≈ 640M USD。info.enterpriseValue 7,287M = marketCap 7,942M - cash 655M，與此一致。
- 流動比率 1.45 (Q2 FY27: 流動資產 998.3M / 流動負債 688.8M)；速動比率 1.27 (info)；營運資金 309.5M。
- 負債/股東權益: 總負債 933.0M / 股東權益 1,448.5M = 0.64 (Jan-26 為 0.70)；有息債務/權益約 1%。
- 股東權益 1,448.5M；每股淨值 4.19 USD (info.bookValue)；P/B 5.45x。
- 商譽 912.7M + 無形資產 108.1M = 1,020.8M，佔股東權益約 70%；有形帳面淨值 (TBV) 427.7M。FY26 收購現金支出 249.0M (Q3 FY26 單季 244.7M)，商譽由 629.6M (Jul-25) 升至 911.8M (Oct-25)。
- 遞延收入: 流動 500.5M + 非流動 77.0M = 577.6M (Jul-26)。流動遞延收入 YoY: 457.2M (Jul-25) → 500.5M (Jul-26)，僅 +9.5%，明顯慢於營收 +20.6%，為需追蹤的先行指標訊號。
- 應收帳款 219.9M (Jul-26)，YoY +22.6% (Jul-25 為 179.3M)。
- 累積虧損 (Retained Earnings): -2,078.2M (Jan-26) → -2,247.8M (Jul-26)。

## Capital allocation & insider signal

**資本配置**
- 股利: 無 (dividendYield 0)。
- 回購: FY26 回購 200.0M USD；季度資料顯示 Q4 FY26 (Jan-26) 回購 98.1M、Q3 FY26 (Oct-25) 回購 49.2M，合計 147.3M；其餘約 52.7M 落在季度表中為 null 的較早季度。Q2 FY27 無回購現金流列示。
- **回購未能抵銷稀釋**: 流通股數 (Ordinary Shares) Jan-25 325.6M → Jan-26 337.8M (+3.7%)；Jul-26 進一步升至 346.0M。加權基本股數 Q2 FY27 341.5M，較 Q2 FY26 330.9M 增加 3.2%。
- 股票選擇權行使現金流入: FY26 39.3M。
- 併購: FY26 現金支出 249.0M，商譽大幅增加，併購效益需以後續營收與毛利率驗證。

**內部人交易 (過去 6 個月，2026-04-15 至 2026-10-15)**
- 公開市場出售 (Form 4 "Sale") 合計約 32.0M USD（本報告加總 yfinance insider 列表中 Value 有值之 Sale 紀錄）。
  - CEO Tomer Weingarten: 約 25.8M USD，佔合計約 81%。2026-10-05 單日賣出 527,368 股 (13.3M USD，@25.26)，另有 500,000 股選擇權行使 (@9.74，約 4.9M USD，非賣出現金)。多筆為約 57,941 股的重複出售，形態具規律性，可能屬 10b5-1 計畫，需以 Form 4 footnote 確認。
  - CFO Sonalee Parekh: 約 2.6M USD（含 2026-10-06 單日 1.31M USD，@25.33）。
  - President Barry Padgett: 約 0.86M USD。
  - Ana Pinczuk (President of Product & Technology, Director): 約 0.82M USD。
  - Robin Tomasello: 約 1.0M USD。
  - Keenan Conder: 約 0.90M USD。
- 公開市場買入: 視窗期間內**無**。最近一次 open-market 買入為 Director Mark Peek 於 2025-12-16 買入 40,000 股 (約 0.60M USD)，已在視窗外。
- 相對市值: 6 個月合計賣出 32.0M / 市值 7,942M ≈ 0.40%。
- 視窗期間另有董事與高管的 RSU/股票獎勵 (Grant @0)，屬非現金薪酬，已排除於賣出統計外。
- 判讀: 絕對金額不大、佔市值比例極低，但集中於 CEO 且 9-10 月與 10 月初股價在 19-25 USD 區間時密集出售；近期 2026-10-05/06 賣出價 25.26-25.33 接近 52 週高點 26.50。

**持股結構**
- 機構持股 86.7% (647 家)，內部人持股 0.89%。
- 前十大機構合計約 38.1%: AQR 6.82% (季增 +18.0%)、BlackRock 6.75% (+3.4%)、Vanguard Portfolio Management 5.70% (-10.0%)、Vanguard Capital Management 4.27% (-2.3%)、First Trust 3.20% (+20.7%)、Legal & General 2.85%、Redpoint Management 2.55% (持平)、Caprock 2.26%、State Street 1.88%、Voya 1.84%。
- 做空: 空單 19.0M 股，佔浮動股數 5.6%，回補天數 2.13 天；較前月 18.2M 增加約 4.2%。

## Valuation

以 currentPrice 22.82 USD (快取時間 2026-10-15 11:21 UTC，為最近一個常規交易時段的收盤價附近報價) 計算:
- 市值 7,942M USD；企業價值 EV 7,287M USD。
- P/S (TTM) 7.23x；EV/Revenue (TTM) 6.63x。
- EV/EBITDA: EBITDA TTM -237.8M，**n/m**。
- P/E (trailing): EPS TTM -1.01，**n/m**。
- Forward P/E 49.5x (forwardEps 0.461)。注意 forwardEps 與 GAAP TTM EPS 的口徑不同，forward 很可能為 non-GAAP 基準，**兩者不可直接比較**。
- P/FCF: FY26 FCF 51.7M 對應約 154x；季度加總 TTM FCF 約 30.9M 對應約 257x。以 info 的 296.9M 計算為約 27x，但該數字與其他資料不一致，不採用。
- P/B 5.45x。
- 分析師: 30 位，recommendationMean 2.06 (Buy)；目標價均值 24.65 USD (+8.0%)、中位數 25.00、最高 31.00 (+35.9%)、最低 17.50 (-23.3%)。
- 技術位置 (info): 現價高於 50 日均線 22.49 與 200 日均線 17.10；52 週區間 11.81-26.50；52 週漲幅 +35.4%；單日 -4.96% (前收 24.01)。
- 同業中位數: 資料中未提供同業資料，以下 sector median 為**估計值**，僅供參考。資安軟體同業估計 EV/Revenue 約 6-9x、P/FCF 約 30-40x、non-GAAP forward P/E 約 30-40x、毛利率約 75-80%、營收成長約 12-18%。
- 判讀: 以營收倍數看與同業落在接近區間，但以 FCF 與 SBC 調整後的角度偏貴；估值依賴營收持續高成長與 GAAP 獲利轉正的時程。

## Key catalysts
- **下次財報**: earnings_dates 列表顯示 2026-12-03 (EPS 估計 0.09，尚未公布)。注意 info.earningsTimestamp 仍指向 2026-08-27，已為過期欄位。距 DATE 約 7 週。
- **上一季 (Q2 FY27, 2026-08-27 公布)**: GAAP EPS -0.27 vs 估計 -0.23，Miss -16.5%。營收 292.0M，YoY +20.6%。
- **歷史 EPS 驚喜 (近 8 季, GAAP 口徑)**: -16.5% / +2.8% / -79.2% / -2.9% / -15.0% / -166.6% / -5.3% / -22.3%。近 8 季中僅 1 季 beat，但 consensus 與 GAAP 口徑可能不一致，需保留判讀。
- **指引**: 資料中無公司 guidance 數字，**n/a**。
- **營收結構**: 分部營收 n/a；遞延收入成長 (+9.5%) 落後營收成長，需於下次財報確認 cRPO 與 billings。
- **併購整合**: FY26 收購 249M USD，商譽佔比高，後續需觀察整合效益與毛利率回穩 (Q2 FY27 毛利率 -2.9pp YoY)。
- **內部人持續出售**: 若 10b5-1 計畫持續，視為既有結構性賣壓，非新增訊號。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 TTM (USD M) | 1,098.7 | +20.6% (Q2 FY27) | 12-18% 成長 | 偏強 |
| 營收 FY26 (USD M) | 1,001.3 | +21.9% | — | 偏強 (成長放緩中) |
| 毛利率 GAAP (FY26) | 74.1% | 持平 (FY25 74.3%)；Q2 YoY -2.9pp | 75-80% | 中性偏弱 |
| 營業利益率 GAAP (FY26) | -30.9% | 改善 9.2pp (FY25 -40.1%) | 約 -10% 至 -20% | 偏弱 |
| 營業利益率 自算 non-GAAP (FY26) | +4.3% | Q2 FY27 15.3% | 估計 15-20% | 中性 |
| 淨利率 GAAP (FY26) | -45.0% | 惡化 9.9pp (FY25 -35.1%) | n/m | 弱 |
| ROE (info) | -23.0% | — | 估計 5-10% | 弱 |
| ROIC (EBIT/IC 近似) | -21.5% | — | — | 弱 |
| FCF margin (FY26) | 5.2% | 上升 (FY25 0.8%) | 估計 10-20% | 中性 |
| FCF / NI | n/m (NI < 0) | — | >0.9 | n/a |
| SBC / 營收 (FY26) | 29.7% | 下降 (FY25 32.6%) | 估計 10-15% | 弱 |
| FCF - SBC (FY26, USD M) | -245.9 | — | — | 弱 |
| 流動比率 (Q2 FY27) | 1.45 | Jan-26 1.39 | 估計 1.5-2.5 | 中性 |
| 負債/股東權益 (Q2 FY27) | 0.64 | Jan-26 0.70 | — | 中性 |
| 有息債務/權益 (FY26) | 1.0% | 下降 (FY25 1.1%) | — | 強 |
| 現金與短期投資 (Q2 FY27, USD M) | 655.2 | -19.2% (Jul-25 810.8) | — | 中性偏弱 |
| 淨現金 (估算, USD M) | ~640 | — | — | 強 |
| 加權基本股數 (Q2 FY27, M) | 341.5 | +3.2% | 估計 1-3% | 偏弱 |
| 應收帳款 (Jul-26, USD M) | 219.9 | +22.6% | — | 中性 |
| 流動遞延收入 (Jul-26, USD M) | 500.5 | +9.5% | 與營收同步 | 偏弱 (落後) |
| EV/Revenue (TTM) | 6.63x | — | 6-9x | 中性 |
| P/S (TTM) | 7.23x | — | 估計 6-9x | 中性 |
| EV/EBITDA | n/m (EBITDA -237.8M) | — | — | n/a |
| P/FCF | ~154x (FY26) / ~257x (TTM 季度) | — | 估計 30-40x | 偏貴 |
| Forward P/E | 49.5x | — | 估計 30-40x (non-GAAP) | 偏貴 |
| P/B | 5.45x | — | — | 中性 |
| 分析師目標價均值 | 24.65 (+8.0%) | — | — | 中性 |
| 內部人 6 個月淨賣出 (USD M) | ~32.0 (公開市場買入 0) | 占市值 0.40% | — | 偏弱 |
| 機構持股 | 86.7% | — | 估計 70-90% | 中性 |
| 空單佔浮動股數 | 5.6% | 空單 +4.2% MoM | — | 中性 |

## Red flags
- GAAP 淨虧損擴大: FY26 淨利率 -45.0%，淨虧損 -450.7M，較 FY25 的 -288.4M 增加約 56%。
- SBC 負擔極高: FY26 SBC 297.6M = 營收 29.7%；扣除 SBC 後 FCF 為 -245.9M，獲利品質依賴股權稀釋。
- 股數持續稀釋: 回購 200M 仍無法阻止流通股數 +3.7% (FY26) 與加權股數 +3.2% (YoY)。
- 毛利率下滑: Q2 FY27 毛利率 72.1%，YoY -2.9pp，需於財報電話會確認成因 (定價、雲端成本或產品組合)。
- 遞延收入成長落後: 流動遞延收入 YoY +9.5% vs 營收 +20.6%，未來營收能見度需觀察。
- 季度營收序列成長放緩: QoQ 由 +6.9% 降至 +2.0% (Q1 FY27)，後於 Q2 FY27 回升至 +5.5%。
- 盈餘未達標頻率高: 近 8 季中多數季度 GAAP EPS 低於估計 (僅 1 季 beat)。
- 稅費異常: FY26 稅費 171.0M，成因資料中無法確認，若為估值備抵調整則不影響現金，但若為實際稅負則需追蹤。
- 併購後商譽佔比高: 商譽 + 無形資產佔股東權益約 70%；有形淨值僅 427.7M。
- 現金水位下滑: 現金與短期投資 YoY -19.2%，Q2 FY27 利息收入 6.2M，YoY -50% (Q2 FY26 12.2M)。
- 內部人持續出售: 6 個月約 32.0M，CEO 佔 81%，2026-10 初出售價接近 52 週高點。
- 估值偏貴: forward P/E 49.5x、P/FCF 約 150-250x，估值對成長假設高度敏感。

## Data gaps and notes
- 資料來源: yfinance 工具呼叫時 Yahoo cookie/crumb 取得失敗，info 與多數欄位來自快取 (info.cached_at 2026-10-15 11:21 UTC)。fast_info 部分欄位為 null 或 NaN (52 週高低、市值、50/200 日均線)，本報告採用 info 欄位。
- 價格時點: info.currentPrice 22.82 為最近一個常規交易時段附近的報價，marketState 為 PRE (盤前)，報告以此為 as-of 價格。
- 資料日期: 所有內部人交易 (最新 2026-10-06) 與財報 (最新 Q2 FY27, 2026-07-31) 均早於 DATE 2026-10-16；未見 DATE 之後的財務資料。
- 欄位不一致: info.freeCashflow (296.9M) 與年報/季度 FCF 不一致；info.totalDebt (0) 與 FY26 年報債務 (15.0M) 不一致；info.earningsTimestamp 為過期 (2026-08-27)。
- 缺口 (n/a): 分部營收、公司 guidance 數字、Q2 FY27 債務明細、同業中位數實際數據、FY26 稅費性質。
- 台灣或非美股不適用 (本標的為美股 NYSE)。

FUNDAMENTALS REPORT COMPLETE
