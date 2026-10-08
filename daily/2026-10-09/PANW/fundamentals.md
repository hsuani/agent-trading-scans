# Fundamentals — PANW as of 2026-10-09

## Executive summary
PANW 財務體質屬「營收高成長、獲利與現金流被併購與股權激勵稀釋」：FY26（2026-07 財年）營收 114.8 億美元、年增 24.5%，但 GAAP 淨利僅 3.07 億美元（FY25 為 11.34 億），且 Q3、Q4 連續兩季 GAAP 虧損；FCF 仍有 41.1 億美元，但 SBC 達 17.7 億美元，扣除 SBC 後 FCF 利潤率約 20%。資產負債表以淨現金（現金 30.7 億、有息負債 25.0 億）為主，流動比率 0.87 屬於 deferred revenue 結構性偏低，商譽與無形資產佔總資產約 60%，有形淨值為負。估值極度昂貴：TTM P/E 1,014x（GAAP EPS 僅 0.40）、forward P/E 83x、P/FCF 約 78x、EV/Revenue 28.9x，分析師平均目標價 396.92 美元（現價 405.57 美元，略高於目標均價），內部人 6 個月淨賣出約 4,817 萬美元、無公開市場買入。

## Revenue & profitability
**營收趨勢（yfinance annual income statement，財年於 7 月結束）**
- FY23 68.93 億 → FY24 80.27 億（+16.5%）→ FY25 92.21 億（+14.9%）→ FY26 114.80 億（+24.5%）
- 3 年 CAGR（FY23→FY26）約 18.6%；2 年 CAGR（FY24→FY26）約 19.6%（以上為依 JSON 數值自行計算）
- 季度趨勢：2025-10 季 24.74 億、2026-01 季 25.94 億、2026-04 季 30.02 億、2026-07 季 34.10 億。Q4 FY26 年增 34.5%（yfinance revenueGrowth 0.345），QoQ 約 +13.6%。Q3 FY26 起營收跳升，與 goodwill 與 purchase of business 大幅增加同步出現，推測為併購併表效應，但 tool 輸出中未列出併購標的名稱，此點 n/a 需人工確認。
- 分部（segment）營收：tool 未提供分部拆分，僅 longBusinessSummary 列出 Prisma Access、Strata、Prisma AIRS、Cortex（XSIAM/XDR/XSOAR/Xpanse）、Unit 42 等產品線，分部營收 n/a。

**獲利能力**
- 毛利率：FY23 72.3% → FY24 74.3% → FY25 73.4% → FY26 70.4%。Q4 FY26 為 67.6%，對比 Q4 FY25 的 73.2%，年減約 5.6 個百分點，為明確惡化訊號。
- 營業利益率：FY23 5.6% → FY24 8.5% → FY25 13.5% → FY26 6.1%。Q4 FY26 為 5.0%（Q4 FY25 為 19.6%），Q3 FY26 營業損失 1.83 億美元（-6.1%）。
- 淨利率：FY25 12.3%，FY26 2.7%（淨利 3.07 億）。Q3 FY26 淨損 1.77 億，Q4 FY26 淨損 2.82 億（-8.3%）。FY24 的 32.1% 淨利率含 15.9 億美元所得稅利益（tax provision -15.9 億），不具可比性。
- GAAP diluted EPS：FY25 1.60 → FY26 0.40（-75%）；Q4 FY26 為 -0.35。
- Q4 FY26 非營業項目約 -5.3 億美元（Other Income Expense -530M，其中 unrealized loss 約 5.24 億，見 cash flow 調節項），是當季由營業轉虧為盈的主因之一，實際原因 tool 未揭露。
- ROE（yfinance）1.74%；ROIC 為依 JSON 自算：FY26 EBIT 5.36 億 × (1-40%) / 平均投入資本約 185 億 ≈ 1.7%；FY25 約 16%。FY26 ROIC 大幅下滑與投入資本由 78 億增至 293 億（併購）有關。
- Earnings surprise 歷史穩定：近 8 季 non-GAAP-like EPS 多數優於共識 3%–10%（2026-09-01 公布 1.02 vs 預估 0.98，+4.35%；2026-06-02 0.85 vs 0.80，+6.62%；2026-02-17 1.03 vs 0.94，+9.88%）。

## Cashflow & balance sheet
**現金流品質**
- OCF：FY23 27.8 億 → FY24 32.6 億 → FY25 37.2 億 → FY26 45.5 億；Q4 FY26 OCF 13.6 億。
- FCF（OCF - capex）：FY23 26.3 億 → FY24 31.0 億 → FY25 34.7 億 → FY26 41.1 億。FCF 利潤率 FY26 35.8%（FY25 37.6%，FY24 38.6%），呈輕度下滑。
- FCF/NI：FY26 為 13.4x（NI 被非現金與非營業項目壓低，此比率失真）；FY25 為 3.1x。以 FCF/NI 判斷現金流品質為「健康（>0.9）」，但 FY26 NI 基數低，應搭配 FCF-SBC 看。
- SBC（stock-based compensation）：FY25 12.95 億（佔營收 14.0%）→ FY26 17.74 億（佔營收 15.5%，年增 37%）。FCF 扣除 SBC 後為約 23.4 億，利潤率約 20.4%。這是本報告最重要的現金流品質警示。
- Working capital 變動：FY26 +5.79 億（主要來自 deferred revenue 與應付帳款增加）。Q4 FY26 應收帳款變動 -9.4 億，為季度內拖累項目。

**資產負債表（2026-07-31）**
- 現金及約當現金 + 短期投資：30.71 億（FY25 為 29.04 億）。
- 總有息負債：25.00 億（長期負債 17.74 億 + 資本租賃 7.26 億；FY25 僅 3.38 億）。
- 淨現金（net cash）：約 +5.7 億（現金 30.71 - 有息負債 25.00）。
- Current ratio 0.87、quick ratio 0.735；流動資產 86.43 億、流動負債 99.23 億；流動負債中 current deferred revenue 77.47 億，屬訂閱制預收款，負債結構性偏高屬常態，但仍使 working capital 為負（-12.80 億）。
- Debt/equity（yfinance debtToEquity 9.337，單位為百分比）約 9.3%，槓桿極低。
- 股東權益 274.92 億（FY25 78.24 億）；每股帳面價值 33.73 美元，P/B 12.0x。
- 商譽 220.10 億、無形資產 70.17 億（合計 290.27 億，佔總資產 484.6 億的約 60%）。Tangible book value -15.35 億（FY25 為正 24.94 億）。
- 資產負債表擴張主因：goodwill and intangibles 由 53.3 億增至 290.3 億，屬大型收購（FY26 purchase of business 46.63 億，FY25 為 10.54 億）。

## Capital allocation & insider signal
**資本配置**
- 資本支出：FY23 1.46 億 → FY24 1.57 億 → FY25 2.47 億 → FY26 4.40 億（佔營收 3.8%，FY25 為 2.7%）。Capex/D&A 約 0.51，維持成本以下。
- 併購：FY26 purchase of business 46.63 億美元，為 FY26 主要現金支出，遠高於 FCF 的一半以上。
- 買回：FY26 repurchase 10.0 億美元（FY25 為 0，FY24 為 5.67 億）。但股本仍大幅稀釋，普通股股數 8.15 億（FY25 為 6.68 億，年增 22%），Q4 FY26 稀釋後加權股數 8.17 億（Q4 FY25 為 7.09 億，年增約 15%）。股本增加與收購股權對價一致，需人工確認。
- 股利：無（dividendYield 0）。
- 債務：FY26 償還 1.6 億，新增 0.1 億；長期負債新增 17.7 億（併購融資或承接）。

**內部人交易（yfinance insider，回溯 6 個月：2026-04-08 至 2026-10-08）**
- 共 21 筆，其中 20 筆為賣出，合計約 4,817 萬美元、約 15.7 萬股；買進 0 筆；1 筆為 RSU 授予（7,211 股，無現金價值）。
- 主要賣出：Lee Klarich（CTO）2026-05-22 賣出 62,904 股，約 1,627 萬美元；James Goetz（董事）2026-06-12 與 2026-09-17 合計約 1,313 萬美元；Dipak Golechha（CFO）2026-06-23 與 2026-09-24 合計約 1,222 萬美元；John Key（董事）合計約 331 萬美元；Joshua Paul（CAO）合計約 153 萬美元；Aparna Bawa（董事）合計約 147 萬美元。
- 淨賣出金額佔市值（331.76 億美元）約 0.015%，絕對金額小、但方向一致（全為賣出，且集中於股價 250–400 美元區間）。Insider 持股占比 0.75%（heldPercentInsiders）。
- 解讀：無公開市場買入，且高管與董事在股價接近歷史高位（52 週高點 432.33）時持續減持，屬偏負面的 insider signal，但金額相對市值極小，不宜過度解讀。

## Valuation
- 最新價 405.57 美元（當日 -3.42%，前收 419.91）；市值 3,317.6 億美元；EV 3,312.5 億美元；52 週區間 139.57–432.33 美元，52 週漲幅 +88.5%（S&P 500 同期 +15.8%）；50 日均線 367.30、200 日均線 253.72。
- Trailing P/E 1,013.9x（GAAP EPS 0.40，不具參考價值）。
- Forward P/E 83.1x（forwardEps 4.879）；PEG 2.14。
- EV/Revenue（TTM）28.9x；EV/EBITDA（TTM EBITDA 15.6 億）212x；P/S 28.9x；P/FCF（TTM FCF 42.4 億）約 78x，以 FY26 FCF 41.1 億計約 81x。
- 行業中位數（估計，非 tool 直接提供）：大型資安與軟體基礎設施 EV/Revenue 約 10–12x、forward P/E 約 35–45x、P/FCF 約 30–40x、EV/EBITDA 約 40–50x。PANW 各項估值倍數約為中位數的 2–3 倍（P/E、EV/EBITDA 差距更大，但 GAAP 基數偏低使其失真）。
- 分析師共識（50 位）：recommendationMean 1.71（Buy）；目標價均值 396.92、中位數 412.5、最高 475、最低 190。現價相對均值目標價高約 2.2%，相對中位數高約 -1.7%。
- Beta 0.933；short interest 2,187 萬股，佔流通股 2.69%，short ratio 3.39 日。

## Key catalysts
- 下次財報：2026-11-19（yfinance 標示為估計日期，isEarningsDateEstimate = true）；下季 EPS 共識 0.97。
- 上次財報：2026-09-01（FY26 Q4），EPS 1.02 vs 預估 0.98，+4.35%；但 GAAP 淨損，且 Q4 毛利率與營業利益率明顯下滑。
- 公司指引（FY27 guidance）：tool 未提供，n/a。
- 併購整合：goodwill 與 purchase of business 大幅增加，後續整合成本、毛利率恢復與 SBC 走勢為關鍵觀察點。
- 機構持股：84.4%（3,849 家機構），Q2 2026 機構新增持股多，但個別持股比例 pctHeld 欄位與股數不一致（例如 BlackRock 股數 7,575 萬股，佔 815M 股約 9.3%，而 pctHeld 顯示 77.8%），疑為 yfinance 欄位錯誤，本報告以股數計算為準。
- 治理風險（yfinance）：overallRisk 9、boardRisk 9、compensationRisk 10、shareHolderRightsRisk 9（滿分 10，數值越高風險越大）。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收（FY26，億美元） | 114.80 | +24.5% | 約 +15%–20%（估計） | 優於同業，成長動能強 |
| Q4 FY26 營收年增 | 34.10（億） | +34.5% | n/a | 併購貢獻明顯 |
| 毛利率（FY26） | 70.4% | -3.0 pp | 約 75%–80%（估計） | 偏弱，Q4 降至 67.6% |
| 營業利益率（FY26） | 6.1% | -7.5 pp | 約 15%–25%（估計） | 偏弱 |
| 淨利率（FY26） | 2.7% | -9.6 pp | 約 10%–20%（估計） | 偏弱，Q3、Q4 為虧損 |
| GAAP diluted EPS（FY26） | 0.40 | -75% | n/a | 偏弱 |
| ROE | 1.7% | 下滑 | 約 10%–15%（估計） | 偏弱 |
| ROIC（自算） | 約 1.7% | 由 約 16% 降 | 約 10%（估計） | 偏弱（併購稀釋） |
| FCF 利潤率 | 35.8% | -1.8 pp | 約 25%–30%（估計） | 優 |
| FCF/NI | 13.4x（NI 被壓低） | n/a | >0.9 健康 | 形式健康，但 NI 基數失真 |
| FCF - SBC 利潤率 | 約 20.4% | n/a | 約 10%–15%（估計） | 中上 |
| SBC / 營收 | 15.5% | +1.5 pp | 約 8%–12%（估計） | 偏高，稀釋風險 |
| 淨現金 | 約 +5.7 億 | 由 淨負債 3.4 億 轉淨現金 | n/a | 優 |
| Current ratio | 0.87 | 由 0.94 降 | 約 1.2–1.5（估計） | 偏弱（deferred revenue 結構） |
| Debt/Equity | 9.3% | 由 4.3% 升 | 約 20%–40%（估計） | 優 |
| 有形淨值 | -15.35 億 | 由 +24.94 億 降 | n/a | 偏弱（商譽占比高） |
| Capex / 營收 | 3.8% | +1.1 pp | 約 3%–5%（估計） | 中性 |
| 股數增加 | +22%（普通股） | n/a | 約 2%–5%（估計） | 偏弱（稀釋） |
| 股利 | 無 | n/a | 視情況 | 中性 |
| Trailing P/E | 1,013.9x | n/a | 約 30x–40x（估計） | 不適用（GAAP 基數低） |
| Forward P/E | 83.1x | n/a | 約 35x–45x（估計） | 昂貴 |
| EV/EBITDA（TTM） | 212x | n/a | 約 40x–50x（估計） | 昂貴 |
| P/FCF（TTM） | 約 78x | n/a | 約 30x–40x（估計） | 昂貴 |
| EV/Revenue（TTM） | 28.9x | n/a | 約 10x–12x（估計） | 昂貴 |
| 內部人 6 個月淨賣出 | 約 4,817 萬美元，0 買進 | n/a | n/a | 偏負面（金額小） |
| 分析師共識 | Buy（1.71），目標均價 396.92 | n/a | n/a | 中性偏多 |

## Red flags
- GAAP 獲利連續惡化：FY26 淨利 3.07 億（-73% YoY），Q3 與 Q4 FY26 連續淨損（-1.77 億、-2.82 億）；Q4 毛利率 67.6%、營業利益率 5.0%，皆低於去年同期。
- Q4 FY26 非營業損失約 5.3 億美元（unrealized loss 約 5.24 億），實際來源 tool 未揭露，需人工確認是否為投資部位減值或其他一次性項目。
- SBC 達 17.7 億美元（佔營收 15.5%，年增 37%），扣除後 FCF 利潤率約 20%；長期股權稀釋與 FCF 品質存疑。
- 股本稀釋：普通股股數年增 22%，買回 10 億美元仍無法抵銷，股東報酬率（ROE 1.7%）偏低。
- 商譽與無形資產佔總資產約 60%，有形淨值為負（-15.35 億），若後續併購減值，帳面淨值波動大。
- 有息負債由 3.4 億升至 25.0 億（含資本租賃），雖仍為淨現金，但資產負債表結構已改變。
- Current ratio 0.87、working capital -12.8 億，依賴 deferred revenue 循環，對現金流下滑的緩衝較薄。
- 估值極端：forward P/E 83x、EV/Revenue 28.9x、P/FCF 約 78x，相對行業估計中位數約 2–3 倍，市場需要持續高成長與毛利率回升才能支撐。
- 股價 52 週漲幅 +88.5%，已接近 52 週高點 432.33（現價距高點約 -6.2%），而 Q4 財報後股價當日 -3.4%。
- 內部人自 2026-04 起持續賣出（共 20 筆），無任何公開市場買入，且 CTO、CFO 皆有大額賣出。
- 治理風險評分偏高（overallRisk 9、compensationRisk 10）。
- 資料品質：yfinance 多個 endpoint 因 Yahoo cookie/crumb 失敗，部分數值取自 cache（cached_at 2026-10-08）；insider 與 holder 的 pctHeld 欄位與股數不一致；分部營收、FY27 guidance、併購標的皆無資料。

## Data notes
- 資料時點：tool 快取時間為 2026-10-08（regularMarketTime 對應 2026-10-08 盤中/收盤），與 as-of 2026-10-09 相差一日，無 post-date 資料；最新 insider 交易為 2026-10-01。
- 缺漏欄位（記為 n/a）：分部營收、FY27 guidance、併購標的與金額明細、ROIC 官方值（僅自算）、行業中位數（僅為估計）。

FUNDAMENTALS REPORT COMPLETE
