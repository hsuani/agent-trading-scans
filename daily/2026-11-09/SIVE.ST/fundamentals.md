# Fundamentals — SIVE.ST as of 2026-11-09

## Executive summary
Sivers Semiconductors (SIVE.ST, Stockholm) 財務體質偏弱：2025 年營收 3.07 億 SEK（+39.8% YoY），但營業利益 -1.78 億 SEK、FCF -1.06 億 SEK，TTM 淨利 -2.94 億 SEK；2026 年 Q2 營收 0.54 億 SEK 年減 12.2%，單季 FCF -0.79 億 SEK，期末現金僅 0.63 億 SEK，主要靠增資（Q2 2026 發行股票所得 1.30 億 SEK）與借款維持營運。估值上 P/S 約 17.8x、P/B 約 5.1x，EV/EBITDA 與 P/E 因 EBITDA、EPS 為負而不適用；唯一可見的 2 位分析師目標價均值 7.7 SEK，低於現價 16.2 SEK，估值相對基本面明顯偏高。資料面有多處內部不一致（見紅旗），本報告結論信心中等。

**資料時效說明**：現價 16.2 SEK 來自快取（cached_at 2026-11-08T13:17 UTC，市場時間戳 2026-11-06），即時報價失敗，非 2026-11-09 收盤價。財報為 yfinance 快取，最新季為 2026-06-30（Q2 2026）。2026-11-09 之後的資料未使用。

## Revenue & profitability
**營收（單位：億 SEK）**
- 2022：1.33；2023：2.36；2024：2.19；2025：3.07；TTM（info.totalRevenue）：2.78。
- 3 年 CAGR（2022→2025）約 32.2%，2 年 CAGR（2023→2025）約 13.9%。但年度序列波動大：2024 年 YoY -7.2%，2025 年 YoY +39.8%。
- 季度趨勢轉弱：2026 Q1 營收 0.62 億（年減 21.5%），2026 Q2 營收 0.54 億（年減 12.2%）。info.revenueGrowth 為 -12.4%，與季度趨勢一致。
- 分部：info.longBusinessSummary 列 Wireless 與 Photonics 兩個分部，工具未提供分部營收，**分部營收為 DATA_UNAVAILABLE**。
- 注意：2023 年 Cost of Revenue 僅 0.09 億、2022 年為負值，與 2024 年 2.15 億相比不合理，屬分類或資料錯誤，故 2022–2023 毛利率數字不採信。

**獲利能力**
- 毛利（Gross Profit）：2024 為 0.04 億（毛利率 1.9%），2025 為 -0.02 億（毛利率 -0.7%）；2026 Q2 毛利 -0.20 億（毛利率約 -36.6%）。info.grossMargins 為 -7.6%（TTM）。
- 營業利益（Operating Income）：2023 -1.59 億（營益率 -67.1%）、2024 -1.94 億（-88.6%）、2025 -1.78 億（-58.0%）；2026 Q2 -1.17 億，營益率約 -217%。
- 淨利（Net Income）：2023 -1.57 億、2024 -1.84 億、2025 -2.23 億（淨利率 -72.6%）；TTM -2.94 億（淨利率 -105.8%，與 info.profitMargins -1.058 吻合）。
- ROE（info）-28.6%，ROA -12.3%。以 2025 營業利益 -1.78 億 / 投入資本 10.52 億計，ROIC 約 -17%。
- 2025 年 Diluted EPS -0.81 SEK，與淨利 / 約 275 百萬股加權股數大致吻合（-2.23 億 / 0.81 ≈ 275 百萬股）。TTM EPS -0.74 SEK。
- 研發費用：2024 為 1.03 億，2025 為 0.36 億，2026 Q2 為 0.25 億（季度數據與年度加總不完全一致，見紅旗）。

## Cashflow & balance sheet
**現金流（單位：億 SEK）**
- 營運現金流（OCF）：2023 -1.06、2024 -0.48、2025 -0.39；TTM（info.operatingCashflow）-1.20。
- 資本支出（Capex）：2023 0.54、2024 0.42、2025 0.67（2025 年 Capex 佔營收 21.9%）。
- 自由現金流（FCF）：2023 -1.60、2024 -0.91、2025 -1.06；2026 Q1 -0.61、Q2 -0.79；TTM（info.freeCashflow）-0.83。
- FCF margin：2025 年 -34.5%；TTM 約 -29.8%。
- FCF / NI：2025 年 0.47（分子分母皆為負值，比率不具經濟意義，**視為 n/a**）。以絕對值判斷，現金流為持續性燒錢，未達「FCF/NI > 0.9」的健康門檻。

**資產負債表（2026-06-30 季末，單位：億 SEK）**
- 現金：0.63（2025 年底 0.30）。
- 總負債（Total Debt）：1.82；淨負債（Net Debt）：1.00（2025 年底 0.73）。淨負債佔市值約 2.0%，但相對 EBITDA 為負，淨負債 / EBITDA 不適用。
- 股東權益：9.49；總資產 14.18；商譽 3.84（佔總資產 27%）；有形帳面價值（TBV）為 -1.10，即扣除商譽後為負值。
- 流動比率（Current Ratio）：1.64（流動資產 2.86 / 流動負債 1.74），速動比率（Quick）1.25。短期償債能力尚可，但依賴 2026 Q2 增資。
- 負債權益比（D/E）：0.19x（info.debtToEquity 19.2%）。
- 現金跑道：以 2026 Q2 單季 FCF -0.79 億計，期末現金僅能支撐不到一季；以 TTM FCF -0.83 億計，約 9 個月。實際需再融資，屬本報告推論。

## Capital allocation & insider signal
**資本配置**
- 股利：無（dividendYield 0.0）。
- 庫藏股：2025 年買回 0.08 億（Repurchase of Capital Stock，2025 Q2 同額）；2026 年無買回紀錄。庫藏股股數由 2025 年底 16.3 百萬股增至 2026 Q2 底 30.2 百萬股，增加原因工具未揭露，**標記為 DATA_UNAVAILABLE（用途）**。
- 股本稀釋：普通股流通股數由 2024 年底 237.6 百萬股增至 2026 Q2 底 304.5 百萬股，增加約 28.2%。權益籌資：2024 年 0.20 億、2025 年 2.11 億、2026 Q2 單季 1.30 億（SEK）。融資主導，股東稀釋為主要資本配置特徵。
- 債務：2025 年借款 1.18 億、還款 1.58 億，淨償還 0.40 億；2026 Q1 單季還款 1.04 億、借款 1.53 億，顯示債務滾動較頻繁。
- Capex 佔營收比例高（2025 年約 22%），在現金為負的情況下屬於持續投入，效益需待營收回升驗證。

**內部人活動**
- insider 工具於過去 6 個月回傳空陣列（[]），**無可用內部人交易紀錄**，無法判斷淨買入或淨賣出；因工具可能缺漏，視為 DATA_UNAVAILABLE，而非「零交易」的確認。
- 內部人持股比例 21.3%（heldPercentInsiders / major_holders），機構持股 17.9%，機構數量 57 家。
- 市值 49.3 億 SEK，若無內部人交易資料則無法計算交易金額佔市值比例。

## Valuation
**市場與估值（單位：億 SEK）**
- 股價：16.2 SEK（快取，市場時間戳 2026-11-06）；前收 15.1 SEK；52 週區間 2.85–110.0 SEK。
- 市值：49.3 億 SEK（16.2 × 304.5 百萬股，與 info.marketCap 4,933 百萬 SEK 吻合）。
- 企業價值（EV）：49.8 億 SEK（info.enterpriseValue 4,975 百萬 SEK）。
- 相對均線：現價較 50 日均線（27.07）低 40.2%，較 200 日均線（33.47）低 51.6%。
- P/E（trailing）：EPS 為負，**n/a**。P/E（forward）：info.forwardPE -81.0，EPS 預估為 -0.20，**n/a**。
- EV/EBITDA：info.enterpriseToEbitda -22.8（TTM EBITDA -2.18 億），**n/a**。
- P/S（TTM）：17.75x；EV/Sales 17.9x。
- P/B：5.1x（bookValue 3.166 SEK/股）。
- P/FCF：FCF 為負，**n/a**。
- 同業中位數：工具未提供，**Sector median 為 DATA_UNAVAILABLE**；以下僅為粗估（不引用為事實）：大型半導體股 P/S 中位數通常遠低於 17.8x，小型 RF/光子公司估值區間寬，17.8x 明顯偏高。
- 分析師：僅 2 位（numberOfAnalystOpinions 2），目標價均值 7.7 SEK、最高 8.0、最低 7.4，全部低於現價；recommendationKey 為 none。覆蓋過少，參考價值有限。

## Key catalysts
- 下次財報：2026-11-26（earnings_dates 與 info.earningsTimestampStart 一致；isEarningsDateEstimate = True，為估計日期），距 as-of 日 17 天。
- 近期公司事件：2026-11-07 名稱由 Sivers IMA Holding AB (publ) 變更為 Sivers Semiconductors AB（info.nameChangeDate）。
- 近期營運動態：2026 Q2 增資 1.30 億 SEK，股本增至 304.5 百萬股；營收連續兩季年減。
- 指引（guidance）：工具未提供管理層指引，**DATA_UNAVAILABLE**。
- 分部動態：Wireless 與 Photonics 分部營收與毛利工具未提供，**DATA_UNAVAILABLE**。
- 盈餘公告歷史：過去 EPS 多數低於預期（如 2026-02-26 公告 Reported EPS -0.04 對比估計 -0.11（驚喜 +63%），但該公告日與 quarterly_fin 季度 EPS 對應不明，見紅旗）。

## Metrics table
單位：營收、淨利、現金流、資產、市值以「億 SEK」表示；比率與股價以原單位表示。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收（億 SEK，2025 年） | 3.07 | +39.8% | DATA_UNAVAILABLE | 年度回升，但季度轉弱 |
| 營收（億 SEK，2026 Q2 單季） | 0.54 | -12.2% | DATA_UNAVAILABLE | 轉弱 |
| 營收 TTM（億 SEK） | 2.78 | -12.4%（info.revenueGrowth） | DATA_UNAVAILABLE | 轉弱 |
| 毛利率（2025 年） | -0.7% | 由 +1.9% 降至 -0.7% | 15%–50%（粗估） | 不合格 |
| 營益率（2025 年） | -58.0% | 由 -88.6% 改善 | 10%–25%（粗估） | 不合格 |
| 淨利率（TTM） | -105.8% | n/a | 5%–20%（粗估） | 不合格 |
| ROE（TTM） | -28.6% | n/a | 10%–20%（粗估） | 不合格 |
| ROIC（以 2025 營業利益估） | 約 -17% | n/a | 10%–15%（粗估） | 不合格 |
| OCF（億 SEK，2025 年） | -0.39 | 由 -0.48 改善 | DATA_UNAVAILABLE | 持續負值 |
| FCF（億 SEK，2025 年） | -1.06 | 由 -0.91 惡化 | DATA_UNAVAILABLE | 持續燒錢 |
| FCF margin（2025 年） | -34.5% | n/a | 5%–15%（粗估） | 不合格 |
| FCF / NI | n/a（分子分母皆負） | n/a | 大於 0.9 為健康 | 不適用 |
| 現金（億 SEK，2026 Q2） | 0.63 | 較 2025 年底 +111% | DATA_UNAVAILABLE | 偏低，依賴增資 |
| 淨負債（億 SEK，2026 Q2） | 1.00 | 較 2025 年底 +37% | DATA_UNAVAILABLE | 可控但上升中 |
| 流動比率 | 1.64 | n/a | 1.5–2.5（粗估） | 尚可 |
| 負債權益比（D/E） | 0.19x | n/a | 0.3–0.6x（粗估） | 偏低 |
| 有形帳面價值（億 SEK） | -1.10 | n/a | 正值 | 不合格 |
| 普通股股數（百萬股） | 304.5 | +28.2%（自 2024 年底） | DATA_UNAVAILABLE | 高度稀釋 |
| 內部人交易 6 個月淨額 | DATA_UNAVAILABLE（空陣列） | n/a | n/a | 無法判斷 |
| 內部人持股 | 21.3% | n/a | DATA_UNAVAILABLE | 持股集中 |
| 市值（億 SEK） | 49.3 | n/a | DATA_UNAVAILABLE | 相對營收偏高 |
| P/E（trailing / forward） | n/a / n/a（EPS 為負） | n/a | 15x–30x（粗估） | 不適用 |
| EV/EBITDA | n/a（EBITDA 為負） | n/a | 15x–25x（粗估） | 不適用 |
| P/S（TTM） | 17.75x | n/a | 2x–6x（粗估） | 明顯偏高 |
| P/B | 5.1x | n/a | 2x–4x（粗估） | 偏高 |
| 分析師目標價均值 | 7.7 SEK（現價 16.2，低 52%） | n/a | n/a（2 位分析師） | 偏低，覆蓋不足 |

## Red flags
- **持續虧損且營益率惡化**：2026 Q2 營業利益 -1.17 億 SEK，營益率約 -217%，單季虧損超過 2025 全年平均每季水準。
- **現金燒錢與再融資依賴**：2025 年 FCF -1.06 億 SEK，2026 Q2 單季 FCF -0.79 億 SEK，期末現金僅 0.63 億 SEK。
- **股本大幅稀釋**：普通股自 2024 年底 237.6 百萬股增至 304.5 百萬股（+28.2%），2026 Q2 單季增資 1.30 億 SEK。
- **營收季度轉弱**：2026 Q1 年減 21.5%、Q2 年減 12.2%，與 2025 年的 +39.8% 形成反差，年度數字可能受一次性項目影響，需確認。
- **有形帳面價值為負**：TBV -1.10 億 SEK；商譽 3.84 億 SEK 佔總資產 27%，若商譽減損將進一步侵蝕權益。
- **估值與分析師目標價嚴重背離**：P/S 17.8x，分析師目標價均值 7.7 SEK 較現價低 52%，且僅 2 位分析師覆蓋。
- **股價技術位置**：現價低於 50 日與 200 日均線 40% 與 52%；52 週高點 110 SEK 與低點 2.85 SEK 的極端區間，需確認是否為股本變動或資料錯誤。
- **資料不一致（需人工覆核）**：
  - 2023 年 Cost of Revenue 與毛利（0.09 億 vs 2024 年 2.15 億；毛利 2023 年 96%）不合理。
  - Quarterly 合計與年度不一致：2025 年 Q3（2025-09-30）季度缺漏，quarterly_cf 2025 年 OCF 合計與年度 -0.39 億不符；info.totalRevenue TTM 2.78 億 SEK 與可得三季合計 1.96 億 SEK 差距需以缺漏的 Q3 解釋。
  - earnings_dates 的 Reported EPS（2026-05-29 為 -0.12，2026-02-26 為 -0.04）與 quarterly_fin 的 Diluted EPS（2026 Q2 為 -0.38，2026 Q1 為 -0.14）對不上，需確認季度對應。
  - info.revenueGrowth（-12.4%）與年度 2025 YoY（+39.8%）方向相反，需確認 TTM 定義。
  - beta 為 -0.609，對一般股票不合理，不採用。
  - fast_info 顯示 "possibly delisted"（即時來源失敗的錯誤訊息）與 info.exchange STO / marketState CLOSED 並存，上市狀態以 info 為準，但建議確認。
- **資料缺口**：分部營收、管理層指引、內部人交易、同業中位數皆為 DATA_UNAVAILABLE，對判斷影響大。

FUNDAMENTALS REPORT COMPLETE
