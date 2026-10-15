# Fundamentals — AMZN as of 2026-10-15

## Executive summary
AMZN 的營收規模與獲利能力持續擴張: FY2025 營收 716.9B USD (YoY +12.4%)、營業利益率由 2022 年的 2.4% 提升至 2025 年的 11.2%, 2026Q1 營收 YoY 達 +16.6%。然而現金流品質明顯轉弱: FY2025 資本支出 131.8B USD (占營收 18.4%) 使 FCF 僅 7.7B USD (FCF margin 1.1%, FCF/NI 0.10), 2026Q1 單季 FCF 為 -18.2B USD, 且總負債在一季內由 153.0B 升至 209.9B USD。估值方面, trailing P/E 20.8x、forward P/E 24.3x、EV/EBITDA 17.0x 看似合理, 但 trailing EPS 含 2026Q2 一次性非營業利得 (EPS 5.75 對 預估 1.83), 若以 FY2025 正常化 EPS 估算 P/E 約 42x, 估值吸引力取決於資本支出回收速度, 財務健康度屬於「獲利強、現金流緊」的組合。

## Revenue & profitability

**營收成長**
- 年度營收: FY2022 513.98B / FY2023 574.79B / FY2024 637.96B / FY2025 716.92B USD。
- 3 年 CAGR (FY2022→FY2025): 11.7%; 2 年 CAGR (FY2023→FY2025): 11.7%。
- FY2025 YoY: +12.4%。
- 季度營收 (USD): 2025Q1 155.67B / 2025Q2 167.70B / 2025Q3 180.17B / 2025Q4 213.39B / 2026Q1 181.52B。2026Q1 YoY +16.6%。
- 2026Q2 營收: DATA_UNAVAILABLE (quarterly_fin 中 2026-06-30 營收欄位為 null)。info 中 TTM totalRevenue 為 775.68B USD, revenueGrowth 0.196 (19.6%), 但定義與期間未在工具中明確標示。
- 分部結構 (North America / International / AWS): 工具無分部營收數據, 僅 longBusinessSummary 列出三大分部, 分部營收占比 DATA_UNAVAILABLE。

**獲利能力 (依年度財報計算)**

| 年度 | 毛利率 | 營業利益率 | 淨利率 (GAAP) |
|---|---|---|---|
| FY2022 | 43.8% | 2.4% | -0.5% |
| FY2023 | 47.0% | 6.4% | 5.3% |
| FY2024 | 48.9% | 10.7% | 9.3% |
| FY2025 | 50.3% | 11.2% | 10.8% |

- FY2025 淨利 77.67B 含 15.32B 「Total Unusual Items」(主要為證券處分利得); 正常化淨利 (Normalized Income) 65.35B, 正常化淨利率約 9.1%。
- 2026Q1 營業利益 23.85B, 營業利益率 13.1% (2025Q1 為 11.8%)。2026Q1 淨利 30.26B 含 15.68B 證券處分利得, 正常化淨利 18.34B, 正常化淨利率約 10.1%。
- ROE 30.6% (info.returnOnEquity), ROA 6.6% (info.returnOnAssets)。ROE 受一次性利得與槓桿影響, 不宜直接外推。
- ROIC (估算, 非工具直接提供): FY2025 NOPAT ≈ 80.0B × (1 − 19.6% 有效稅率) ≈ 64.3B; 以期末 Invested Capital 476.7B 計算約 13.5%, 以期初期末平均 407.6B 計算約 15.8%。
- EBITDA: FY2025 EBITDA 165.3B (本地 EBITDA 欄位), 正常化 EBITDA 150.0B; info.ebitda (TTM) 168.9B, EBITDA margin 21.8%。

## Cashflow & balance sheet

**現金流品質**
- 營業現金流 (OCF): FY2022 46.75B / FY2023 84.95B / FY2024 115.88B / FY2025 139.51B USD; FY2025 OCF margin 19.5%。
- 資本支出 (Capex): FY2022 63.6B / FY2023 52.7B / FY2024 83.0B / FY2025 131.8B USD; 占營收 FY2025 為 18.4% (FY2023 為 9.2%)。Capex/D&A (FY2025) 約 2.0x; Capex/OCF 約 94%。
- 自由現金流 (FCF): FY2022 -16.9B / FY2023 32.2B / FY2024 32.9B / FY2025 7.7B USD。FY2025 FCF margin 1.1%。
- FCF / NI: FY2025 0.10 (以 GAAP NI 計); 以正常化 NI 計約 0.12; FY2024 0.55; FY2023 1.06。低於 0.9 健康門檻, 2025 年為最弱的一年。
- 季度 FCF (USD): 2025Q1 -8.0B / 2025Q2 0.3B / 2025Q3 0.4B / 2025Q4 14.9B / 2026Q1 -18.2B。2026Q1 Capex 44.2B (占營收 24.4%, YoY +77%), OCF 26.0B。
- 過去四季 (2025Q2–2026Q1) 本地 FCF 合計 -2.5B USD; info.freeCashflow TTM 為 3.22B USD。兩者差異來自 2026Q2 現金流數據缺口 (quarterly_cf 無 2026-06-30 列), 2026Q2 現金流 DATA_UNAVAILABLE。
- SBC: FY2025 19.5B USD (占營收 2.7%), 較 FY2024 的 22.0B 下降。

**資產負債表**
- 2026Q1 (最新本地 BS): 現金及短期投資 143.1B; 總負債 (含租賃) 209.9B; 長期債務 119.1B (YE2025 為 65.6B, 一季增加 81%); 股東權益 441.9B; 總資產 916.6B。
- 季度發債: 2026Q1 Issuance of Debt 59.5B USD, Financing Cash Flow +52.8B。
- 淨負債 (本地計算, 總負債 − 現金與短期投資): 2026Q1 為 66.8B; FY2025 為 30.0B。Yahoo 欄位 Net Debt 2026Q1 為 17.3B, 與本地計算差異大, 定義不同 (疑似排除部分租賃負債或採不同現金口徑), 本報告以本地計算為準並標示差異。
- info (較新期間, 疑似 2026Q2): totalDebt 251.6B, totalCash 123.0B, 淨負債約 128.6B; enterpriseValue 2,869.2B 與此一致。
- Debt/Equity: 2026Q1 為 47.5% (本地計算, 含租賃); FY2025 為 37.2%。info debtToEquity 為 45.6%。
- 流動比率: 2026Q1 1.18x / FY2025 1.05x (本地計算); info currentRatio 1.03, quickRatio 0.84。
- 利息保障倍數: FY2025 EBIT 99.6B / 利息支出 2.27B ≈ 43.8x; 2026Q1 約 50.8x。償債能力本身無虞, 壓力來自債務增速。
- 每股帳面價值 51.16 USD, P/B 4.97x。

## Capital allocation & insider signal

**資本配置**
- 股息: 無 (dividendYield 0, trailingAnnualDividendRate 0)。
- 買回: FY2022 6.0B, FY2023–FY2025 皆為 0 (FY2025 欄位為 null), 近三年無實質買回。
- 股本稀釋: 稀釋後平均股數 FY2022 10.19B → FY2025 10.83B (3 年 +6.3%, 年化約 2%); 2026Q2 稀釋股數 10.90B, YoY +0.9%。
- 資本支出為主要資金用途 (FY2025 131.8B), 並以債務融資部分支應 (FY2025 發債 25.0B, 還債 15.3B; 2026Q1 發債 59.5B)。

**內部人交易 (最近六個月, 2026-04-15 至 2026-10-15)**
- 公開市場賣出合計 約 1.46M 股, 約 411.7M USD。
- 主要賣方: Jeffrey Bezos 約 1.21M 股 (346.5M USD)、Andrew Jassy 約 102K 股 (27.0M USD)、Douglas Herrington 約 54K 股 (14.4M USD)、Matthew Garman 約 41K 股 (10.9M USD)、David Zapolsky 約 31K 股 (8.1M USD)、其餘高階主管合計約 30K 股。
- 另有 Bezos 贈與 (Stock Gift) 約 1.67M 股, 無市場成交金額。
- 公開市場買入: 0 股。六個月內無內部人買進紀錄。
- 規模: 賣出金額 411.7M USD 占市值 2.74T USD 約 0.015%, 量級極小, 且多數屬高階主管定期出售 (可能含 10b5-1 或 RSU 歸屬後出售, 工具未標示交易計畫類型, 不作定論)。
- 內部人持股 8.85% (heldPercentInsiders)。
- 機構持股 68.7% (heldPercentInstitutions), 機構數 7,881; 前幾大持股: BlackRock 6.94% (748.4M 股)、Vanguard 5.89%、State Street 3.68%、FMR 3.39% (截至 2026-06-30)。
- 空方: 放空股數 86.7M (占流通 0.88%), short ratio 2.49 日, 較前月 92.1M 下降約 6%。

## Valuation

以 2026-10-14 收盤價 254.08 USD (regularMarketPrice, 盤前 249.15 USD) 計算, 市值 2,740.6B USD, EV 2,869.2B USD。

- Trailing P/E: 20.8x (info, TTM EPS 12.21)。注意: TTM EPS 含 2026Q2 EPS 5.75 (預估 1.83, 驚喜 +214.9%) 之非營業利得, 不宜直接作為估值基準。
- FY2025 GAAP P/E: 35.4x (EPS 7.17)。以正常化淨利 65.35B / 稀釋股數 10.83B 估算正常化 EPS 約 6.04, P/E 約 42.1x (估算)。
- Forward P/E: 24.3x (forwardEps 10.45); 當年度 EPS 估計 8.31, P/E 30.6x。consensus forward EPS (10.45) 低於 TTM EPS (12.21), 反映 TTM 含一次性利得。
- PEG: 1.5 (info.pegRatio)。
- EV/EBITDA: 17.0x (info, TTM EBITDA 168.9B); 以正常化 FY2025 EBITDA 計為 19.1x (估算)。
- EV/Revenue: 3.7x。P/S: 3.5x。
- P/FCF: 不具參考價值 (TTM FCF 僅 3.2B, 市值/FCF 約 851x; FY2025 約 356x), 受 Capex 高峰扭曲。改用 P/OCF: 17.0x (TTM OCF 161.4B)。
- 分析師共識: 58 位分析師, recommendationMean 1.33 (strong_buy); 目標價平均 331.20 USD (中位數 329.5), 最高 405.0, 最低 230.0。相對現價, 平均目標價隱含 +30.4% 上行空間, 最低目標價為 −9.5%。
- 股價位置: 52 週區間 196.0–287.2 USD, 現價位於區間約 64% 位置; 較 50 日均線 257.88 低 1.5%, 較 200 日均線 242.53 高 4.8%。
- Beta 1.456。

## Key catalysts
- 下一次財報: 2026-10-29 (盤後, Yahoo 時間戳 20:00 UTC; info.isEarningsDateEstimate 為 true, 日期為預估)。EPS 預估 1.95 (earnings_dates)。
- 上一季 (2026Q2, 2026-07-30 公布) EPS 5.75 vs 預估 1.83, 驚喜 +214.9%, 但主因為非營業利得, 核心營運改善需以營業利益與 OCF 確認; 2026Q2 營收與 Capex 數據 DATA_UNAVAILABLE。
- 資本支出動向: 2026Q1 Capex 44.2B (YoY +77%), 全年 Capex 指引 DATA_UNAVAILABLE (工具無管理層指引)。若 Q1 節奏延續, 年化約 177B; 此為 FCF 能否回升的關鍵變數。
- 融資動向: 2026Q1 發債 59.5B, 長期債務 +53.4B QoQ; 後續債券發行或還債節奏需追蹤。
- 分部變化: 工具無分部數據, AWS / 廣告 / 國際分部的營收與利潤變化 DATA_UNAVAILABLE。
- 內部人交易: Bezos 與高階主管於 2026-08 至 2026-10 持續出售, 需與財報後的 Form 4 交易一併觀察。
- 資料時效註記: 價格與 info 數據 (含 52 週區間、分析師共識) 來自 2026-10-15 之本地快取 (cached_at 2026-10-15T11:16 UTC, source: cache); 季度 BS 最新至 2026-03-31, 季度 CF 最新至 2026-03-31, 與 info 中疑似 2026Q2 的 TTM 欄位存在期間不一致。無 post-date 數據 (所有引用事件日期皆早於 2026-10-15)。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 (FY2025, USD) | 716.9B | +12.4% | 估計 YoY 約 +5–10% (非工具數據) | 優於同業 |
| 營收 2026Q1 YoY | 181.5B | +16.6% | n/a | 加速成長 |
| 營收 3 年 CAGR (FY22–25) | 11.7% | n/a | n/a | 穩健 |
| 毛利率 (FY2025) | 50.3% | +1.4 pt | 估計 約 40% | 優 |
| 營業利益率 (FY2025) | 11.2% | +0.4 pt | 估計 約 6–8% | 優 |
| 營業利益率 (2026Q1) | 13.1% | +1.3 pt (vs 2025Q1 11.8%) | n/a | 改善中 |
| 淨利率 (FY2025 GAAP) | 10.8% | +1.5 pt | 估計 約 5–7% | 含一次性利得, 需正常化 |
| 正常化淨利率 (FY2025) | 9.1% | n/a | n/a | 良好 |
| ROE | 30.6% | n/a | 估計 約 15% | 優 (受槓桿與利得影響) |
| ROIC (估算) | 13.5%–15.8% | n/a | 估計 約 10% | 略優 |
| OCF margin (FY2025) | 19.5% | +1.0 pt (vs FY2024 18.2%) | 估計 約 10–12% | 優 |
| FCF margin (FY2025) | 1.1% | −4.1 pt | 估計 約 4–6% | 劣 (Capex 高峰) |
| FCF / NI (FY2025) | 0.10 | 由 0.55 降至 0.10 | 健康門檻 > 0.9 | 紅旗 |
| Capex / 營收 (FY2025) | 18.4% | +5.4 pt | 估計 約 5–8% | 偏高, 屬投資期 |
| 2026Q1 Capex YoY | 44.2B | +77% | n/a | 紅旗 (加速) |
| 淨負債 (2026Q1, 本地計算) | 66.8B | 由 30.0B (FY25) 增加 | n/a | 上升中 |
| Debt/Equity (2026Q1, 含租賃) | 47.5% | 由 37.2% (FY25) 上升 | 估計 約 30–50% | 中性偏警示 |
| 流動比率 (2026Q1) | 1.18x | 由 1.05x (FY25) 上升 | 估計 約 1.1–1.5x | 中性 |
| 利息保障倍數 (FY2025) | 43.8x | n/a | n/a | 優 |
| 股息 / 殖利率 | 無 / 0% | n/a | 估計 約 0.5–1% | 不發股息 |
| 買回 (FY2023–FY2025) | 0 | 上一次 2022 年 6.0B | n/a | 無回購 |
| 稀釋股數 (FY22→FY25) | 10.83B | +6.3% (3 年) | n/a | 溫和稀釋 |
| 內部人 6 個月淨買賣 | 賣出 411.7M USD, 買入 0 | n/a | n/a | 偏賣出 (規模小, 占市值 0.015%) |
| Trailing P/E | 20.8x | n/a | 估計 約 25–30x | 低於同業 (含一次性利得, 需謹慎) |
| 正常化 P/E (FY2025 估算) | 42.1x | n/a | 估計 約 25–30x | 高於同業 |
| Forward P/E | 24.3x | n/a | 估計 約 25–30x | 略低於同業 |
| EV/EBITDA (TTM) | 17.0x | n/a | 估計 約 15–18x | 合理 |
| P/S (TTM) | 3.5x | n/a | 估計 約 1.0–1.5x | 偏高 |
| P/OCF (TTM) | 17.0x | n/a | n/a | 合理 |
| P/FCF (TTM) | 約 851x | n/a | n/a | 不具參考價值 (Capex 扭曲) |
| P/B | 5.0x | n/a | 估計 約 3–5x | 中性 |
| PEG | 1.5 | n/a | n/a | 中性 |
| 分析師平均目標價 | 331.2 USD (+30.4%) | n/a | n/a | 偏多 (58 位分析師) |
| 機構持股比 | 68.7% | n/a | n/a | 高 |
| 空方持股比 (占流通) | 0.88% | 較前月 −5.9% | n/a | 低 |

註: 「Sector median (estimate)」為分析師先驗估計, 非工具數據, 僅供相對比較; 所有 Latest / YoY 數字均來自 pipeline/tools/yf 輸出。

## Red flags
- 現金流轉弱: FY2025 FCF 僅 7.7B, FCF/NI 0.10, 遠低於 0.9 健康門檻; 2026Q1 單季 FCF −18.2B。
- Capex 加速: 2026Q1 Capex 44.2B, YoY +77%, 占營收 24.4%; 資本支出回收期間, 獲利與現金流之間的落差可能持續。
- 負債快速上升: 總負債 2026Q1 較 YE2025 增加 37% (153.0B → 209.9B), 長期債務增加 81%; 一季發債 59.5B。
- 獲利品質: FY2025 淨利含 15.3B 證券處分利得; 2026Q1 淨利 30.3B 中 15.7B 為非營業利得; 2026Q2 EPS 5.75 亦屬一次性利得主導。Trailing P/E 20.8x 因而低估真實估值。
- Net Debt 定義不一致: Yahoo 報告 2026Q1 Net Debt 17.3B 與本地計算 66.8B 差異 49.5B, 需確認 (可能與租賃負債定義有關)。
- 資料缺口: 2026Q2 營收與現金流 DATA_UNAVAILABLE; 分部營收 DATA_UNAVAILABLE; 管理層資本支出指引 DATA_UNAVAILABLE; 最新 BS/CF 僅至 2026Q1, info 之 TTM 欄位為較新期間, 部分指標存在期間錯配。
- 內部人持續賣出: 六個月內 Bezos 與多位高階主管出售合計 411.7M USD, 無買進紀錄。規模對市值影響極小, 但方向一致。
- 無股息、無回購: 股東回報完全依賴股價增值; 股本仍每年溫和稀釋約 2%。
- 估值依賴盈利改善假設: 以正常化 EPS 估算 P/E 約 42x, 高於估計同業中位數, 估值吸引力高度依賴 AWS 與廣告等高毛利分部持續成長。

FUNDAMENTALS REPORT COMPLETE
