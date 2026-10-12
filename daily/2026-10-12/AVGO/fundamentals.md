# Fundamentals — AVGO as of 2026-10-12

## Executive summary
以 `yf info` 區塊的 TTM 數據來看，AVGO 獲利能力極強（毛利率 75.5%、營業利益率 54.3%、淨利率 42.9%、ROE 44.2%），營收 YoY +85.5%，FCF 約 306 億美元，財務體質尚可（流動比率 2.50，淨負債約 354 億美元，約佔市值 2.1%）。估值上，trailing P/E 46.2x、EV/EBITDA 33.7x、P/FCF 約 56x 明顯高於一般半導體水準，但 forward P/E 僅 18.6x，顯示市場以大幅成長的 forward EPS（19.39）定價。**重要限制：** 年度與季度報表的數字（營收 81.9 億、總負債 47.9 億、股數 8.47 億）與 `info` 區塊（營收 891 億、總負債 594 億、股數 47.7 億）無法對帳，屬量級不一致，本報告的估值與獲利結論以 `info` 為主，信心程度為中低，下游使用前需先核對原始 10-K/10-Q。

## Revenue & profitability
- **營收（info 區塊，TTM）：** totalRevenue 891.04 億美元，revenueGrowth（YoY）+85.5%。
- **營收（年度報表，FY 標示 2026-01-31）：** 81.95 億美元；FY2025 為 57.67 億，YoY +42.1%；2023→2026 三年 CAGR 約 11.5%（由 59.20 億計算）。此序列與 info 區塊不一致，CAGR 信心低。
- **季度營收：** `quarterly_fin` 回傳空白（無資料），季度 YoY 無法驗證。
- **分部結構：** longBusinessSummary 描述兩大部門：Semiconductor Solutions（網路連接、伺服器與儲存、寬頻、工業）與 Infrastructure Software（VMware Cloud Foundation、大型主機軟體、資安等）。分部營收數字：n/a。
- **毛利率：** grossMargins 75.5%（info）。年度報表 gross profit 41.81 億 / 營收 81.95 億 = 51.0%，與 info 不一致。
- **營業利益率：** operatingMargins 54.3%（info）。年度報表 operating income 13.38 億 / 81.95 億 = 16.3%。
- **淨利率：** profitMargins 42.9%（info）。年度報表淨利 26.70 億 / 81.95 億 = 32.6%。
- **EPS：** trailingEps 7.83；forwardEps 19.39；年度報表 diluted EPS 3.07（FY2026-01 標示）。EPS 基礎不一致。
- **ROE / ROA：** ROE 44.2%，ROA 15.4%（info）。ROIC：n/a（無直接欄位；年度報表 invested capital 187.8 億，無法直接對照 info）。
- **EBITDA：** info ebitda 522.6 億；年度報表 EBITDA 45.4 億。

## Cashflow & balance sheet
- **現金流（info）：** operatingCashflow 406.5 億美元、freeCashflow 306.0 億美元。FCF margin = 306.0 / 891.0 = **34.3%**。
- **FCF / NI：** 淨利以 profitMargins × 營收推算 = 382.6 億，FCF/NI = **0.80**，低於 0.9 的健康門檻。
- **隱含資本支出：** OCF − FCF = 100.6 億美元，約佔營收 11.3%（由 info 推算，非直接欄位）。
- **年度報表現金流：** OCF 17.51 億、FCF 13.92 億、capex 3.59 億，與 info 量級不符，不採用。
- **季度現金流（2026-07-31 為最新季）：** OCF 6.06 億、FCF 4.74 億、capex 1.31 億；同樣與 info 量級不一致。
- **淨負債：** info totalDebt 594.2 億 − totalCash 240.0 億 = **淨負債約 354.4 億美元**（佔 EV 約 2.0%）。
- **流動性：** currentRatio 2.50、quickRatio 2.15。季度資產負債表（2026-07-31）：流動資產 79.19 億、流動負債 24.99 億，流動比率約 3.17（報表基礎）。
- **負債權益比：** debtToEquity 59.6（yfinance 單位為百分比，即約 0.60x）。每股淨值 bookValue 20.88，P/B 17.3x。
- **現金水位：** info totalCash 239.8 億；季度報表現金及約當現金 39.33 億（2026-07-31），不一致。
- **商譽：** 季度報表商譽 138.74 億（2026-07-31），較 2026-01 的 110.62 億增加。
- **資產負債表量級問題：** 季度報表 total debt 52.86 億 vs info 594.2 億；季度報表股數 8.99 億 vs info sharesOutstanding 47.74 億。此為資料源或換算錯誤的高度可能性，需人工確認。

## Capital allocation & insider signal
- **股利：** dividendRate 2.60、dividendYield 0.72%、payoutRatio 32.4%（info）。以 info 股數與股利率推算年度股利約 124 億美元，FCF 覆蓋約 2.5x。年度報表的股利支出 2.05 億與此量級不符，不採用。
- **買回：** 年度報表 repurchase 2026-01 為 20.40 億，2025-01 為 7.25 億；季度報表 2025-10-31 季為 13.0 億，其餘季度約 2.0 億。此為報表數字，與 info 量級可能不一致，僅供趨勢參考。
- **資本支出趨勢：** 年度報表 capex 由 2023 的 2.17 億增至 2026-01 的 3.59 億，但量級疑慮同上。
- **內部人交易（6 個月，2026-04-12 至 2026-10-12）：** 共 41 筆（不含贈與），其中賣出 17 筆、共 209,386 股、約 3,577 萬美元；買進 0 筆。淨流出約 3,577 萬美元，佔市值約 0.002%。賣出人數 6 人（Bharathi、Casper、Durn、Koopmans、Meintjes、Murphy）。另有 6 筆贈與（約 42,116 股，無金額）。
- **內部人持股：** heldPercentInsiders 1.9%。
- **機構持股：** heldPercentInstitutions 79.8%，機構數 6,265。前幾大持股（2026-06-30）：Geode 2.44%、Capital Research Global 2.37%（減持 2.5%）、JPMorgan 1.99%（加碼 3.5%）、T. Rowe Price 1.74%（減持 1.9%）。
- **解讀：** 內部人為小額選擇性賣出（多為 10b5-1 性質之常態化出售，無法由資料確認），無公開市場買進。賣壓相對市值極小，不構成結構性訊號。

## Valuation
- **市值 / EV：** marketCap 1,725.9 億美元、EV 1,761.3 億美元。股價 361.54（fast_info last_price，cache 時間 2026-10-12 00:45 UTC），前收 360.14。
- **P/E：** trailing 46.2x、forward 18.6x。
- **EV/EBITDA：** 33.7x（EBITDA 522.6 億）。
- **EV/Revenue：** 19.8x；P/S（trailing）19.4x。
- **P/FCF：** 約 56.4x（市值 / FCF 306.0 億）。
- **PEG：** 0.36（yfinance 提供；以 forward 成長推算，成長假設不可直接驗證）。
- **P/B：** 17.3x。
- **股價位置：** 52 週高 495.00、低 289.96；現價較 52 週高低 27.0%，較低點高 24.7%。50 日均線 371.87、200 日均線 368.28，現價同時位於兩條均線下方（fast_info 的均線欄位為 null，取自 info）。
- **分析師共識：** targetMeanPrice 531.31（較現價 +46.9%），47 位分析師，recommendationKey 為 strong_buy。此為外部意見，不作為本報告結論。
- **同業中位數：** 無資料來源，以下為估計值（非 yfinance 數字）：semis trailing P/E 約 35x、forward P/E 約 25x、EV/EBITDA 約 20x、P/S 約 8x、P/FCF 約 30x。AVGO 在 trailing 與 P/S 面向溢價明顯，forward P/E 與同業相近或略低。
- **Beta：** 1.476（高於市場）。

## Key catalysts
- **下次財報：** 2026-12-09（yfinance 紀錄日期 2026-12-09，時間戳 20:00 UTC，時段未確認），EPS 一致預期 3.83。
- **資料缺口：** yfinance 另列 2026-09-02 為財報日（EPS 預期 3.24），但未有 reported EPS。以 2026-07-31 季報表存在推斷，該季財報可能已發布，cache 未更新，需確認。
- **近期 EPS 表現：** 最近 8 季全數 beat（surprise %：2024-09 +2.79、2024-12 +2.04、2025-03 +6.11、2025-06 +0.59、2025-09 +1.60、2025-12 +4.38、2026-03 +1.32、2026-06 +1.74），平均 surprise 約 +2.6%。2026-06 季 reported EPS 2.44 vs 預期 2.40。
- **指引（guidance）：** 無資料，n/a。
- **分部轉變：** 分部營收數字無資料，n/a。
- **其他：** 資料中無已確認之併購、產品或客戶公告。

## Metrics table

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 TTM (info) | 891.0 億美元 | +85.5% | n/a（估計成長約 15-25%） | 成長強勁，但需核對 |
| 營收 FY2026-01 (報表) | 81.9 億美元 | +42.1% | n/a | 與 info 不一致，不採信 |
| 毛利率 | 75.5% | n/a | 約 55% | 優 |
| 營業利益率 | 54.3% | n/a | 約 25% | 優 |
| 淨利率 | 42.9% | n/a | 約 15% | 優 |
| ROE | 44.2% | n/a | 約 15% | 優 |
| ROA | 15.4% | n/a | 約 8% | 優 |
| ROIC | n/a | n/a | 約 12% | 資料不足 |
| FCF margin | 34.3% | n/a | 約 20% | 優 |
| FCF / NI | 0.80 | n/a | 約 0.85 | 略低於 0.9 門檻 |
| 淨負債 | 354.4 億美元 | n/a | 約 0.4x 淨負債/權益 | 可控（淨負債佔 EV 約 2%） |
| 流動比率 | 2.50 | n/a | 約 2.0x | 良好 |
| 負債權益比 | 0.60x（59.6%） | n/a | 約 0.4x | 偏高但可接受 |
| 現金及約當現金 | 239.8 億美元 | n/a | n/a | 充裕 |
| 股利殖利率 | 0.72% | n/a | 約 1.0% | 偏低，覆蓋良好（FCF 覆蓋約 2.5x） |
| 股利支付率 | 32.4% | n/a | n/a | 健康 |
| 隱含資本支出 / 營收 | 約 11.3% | n/a | 約 5-8% | 偏高（AI 基礎建設週期） |
| 內部人 6 個月淨交易 | 淨賣出約 3,577 萬美元 | n/a | n/a | 小幅淨賣，無買進，非強烈訊號 |
| 機構持股比例 | 79.8% | n/a | 約 70% | 高 |
| Trailing P/E | 46.2x | n/a | 約 35x | 偏貴 |
| Forward P/E | 18.6x | n/a | 約 25x | 與同業相近或略低 |
| EV/EBITDA | 33.7x | n/a | 約 20x | 偏貴 |
| P/S | 19.4x | n/a | 約 8x | 明顯偏貴 |
| P/FCF | 約 56.4x | n/a | 約 30x | 明顯偏貴 |
| P/B | 17.3x | n/a | 約 4x | 偏貴（ROE 高，部分合理） |
| PEG | 0.36 | n/a | 約 1.5 | 低（依 forward 成長假設） |
| Beta | 1.476 | n/a | 約 1.2 | 高於市場 |
| 股價 vs 52 週高 | -27.0%（361.54 vs 495.00） | n/a | n/a | 回檔區間 |
| 近 8 季 EPS 平均 surprise | +2.6%（8/8 beat） | n/a | n/a | 優 |

## Red flags
- **資料一致性（最重要）：** 年度與季度報表的營收、負債、股數、FCF、EPS 與 `info` 區塊量級不一致（例如 FY2026-01 營收 81.9 億 vs info TTM 891 億；股數 8.47 億 vs 47.7 億；trailing EPS 3.07 vs 7.83）。在核對前，任何依賴單一來源的結論皆有風險。
- **年度報表日期標示：** FY 標示為 2026-01-31，但 info 的 lastFiscalYearEnd 為 2025-11-02，期別對應不明。
- **Earnings 日期：** 2026-09-02 財報日無 reported EPS，可能為 cache 缺漏或財報已發布未更新。
- **估值偏貴：** trailing P/E、EV/EBITDA、P/S、P/FCF 與 P/B 均明顯高於一般同業估計值，估值擴張依賴 forward 獲利兌現。
- **FCF / NI 0.80：** 低於 0.9 健康門檻（由 info 推算，依賴淨利口徑）。
- **資本支出密度上升：** 隱含 capex 約佔營收 11%，對自由現金流有壓力。
- **股價在均線下方：** 現價 361.54 低於 50 日（371.87）與 200 日（368.28）均線；較 52 週高回檔 27%。
- **內部人持續出售：** 6 個月內 17 筆賣出、0 筆買進（金額小，但方向一致）。
- **Beta 1.476：** 波動度高於市場，對總體風險偏好變化敏感。
- **資料缺口：** 季度營收、分部營收、指引、ROIC 皆無資料。

FUNDAMENTALS REPORT COMPLETE
