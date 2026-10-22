# Fundamentals — AVGO as of 2026-10-22

## Executive summary
Broadcom 財務體質強健：2026-07 季 (FQ3 FY26) 單季營收 296 億美元、YoY +85.5%，TTM FCF 約 394 億美元 (FCF margin 44.2%)，淨負債僅 354 億美元 (約 0.68x EBITDA)。估值面分歧明顯：以 forward EPS 19.40 計 forward P/E 17.4x 相對便宜，但以 GAAP trailing EPS 7.83 計 P/E 43.1x、EV/EBITDA 31.5x、P/FCF 40.9x 仍屬高檔，且股價距 52 週高點 495.00 仍低 31.8%、位於 50 日與 200 日均線之下。近六個月內部人淨賣出約 2.84 億美元，但僅占市值 0.018%，訊號強度有限；下一次財報預計為 2026-12-09。

資料說明：本次 yfinance 即時呼叫的 financials / balance_sheet / cashflow 類輸出與 AVGO 不符 (疑似混入 TSMC 之 NT$ 規模、12 月 FYE 資料)，已全數棄用；所有財務數字改採 repo 快取 `prices/yf/AVGO.json` (refreshed 2026-10-22T11:39:42Z，_misses 為空，FYE 10 月末，與 AVGO 一致)。詳見文末紅旗。

## Revenue & profitability
**營收成長**
- 年度營收 (FY, 10 月末)：FY2022 332.0 億、FY2023 358.2 億、FY2024 515.7 億、FY2025 638.9 億 (美元)。
- 3 年 CAGR (FY2022→FY2025)：約 24.4%。YoY：FY2023 +7.9%、FY2024 +44.0%、FY2025 +23.9%。
- 季度動能加速：FQ3 FY25 159.5 億 → FQ4 FY25 180.2 億 → FQ1 FY26 193.1 億 → FQ2 FY26 221.9 億 → FQ3 FY26 295.9 億。FQ3 YoY +85.5%，與 info 之 revenueGrowth 0.855 一致。
- TTM 營收 891.0 億 (由四季加總，與 info totalRevenue 89,104 百萬一致)。
- 分部：yfinance 未提供分部營收；依 info.longBusinessSummary，兩大分部為 Semiconductor Solutions (網路連接、定製 ASIC、伺服器與儲存 等) 與 Infrastructure Software (VMware 相關 private cloud 軟體組合)。分部比重：DATA_UNAVAILABLE。

**獲利能力 (由季度/年度報表計算)**

| 期間 | 毛利率 | 營業利益率 | 淨利率 |
|---|---|---|---|
| FY2022 | 66.5% | 43.0% | 34.6% |
| FY2023 | 68.9% | 45.9% | 39.3% |
| FY2024 | 63.0% | 29.1% | 11.4% |
| FY2025 | 67.8% | 40.8% | 36.2% |
| TTM (至 FQ3 FY26) | 68.8% | 48.5% | 42.9% |

- FY2024 獲利率明顯下滑 (淨利 58.95 億，稅率 37.8%，營業利益率 29.1%)，FY2025 恢復；TTM 營業利益率 48.5% 為近年新高。
- 季度趨勢：營業利益率由 FQ4 FY25 的 42.5% 升至 FQ3 FY26 的 54.3%；淨利率由 38.1% (FQ1 FY26) 升至 44.2%。
- ROE：info 之 returnOnEquity 為 44.2%；以 TTM 淨利 382.65 億除以 FQ3 FY26 股東權益 996.90 億計算約 38.4%。
- ROIC (估計)：TTM 營業利益 432.37 億 × (1 − 25.6% FY25 有效稅率) ÷ FQ3 FY26 投入資本 1,591.09 億 ≈ 20.2%。
- EPS：GAAP 稀釋 EPS FY2025 4.77、TTM 7.83；info epsForward (分析師共識 NTM) 19.40，epsCurrentYear 11.66。

## Cashflow & balance sheet
**現金流品質**
- FY2025 營業現金流 275.4 億、資本支出 6.2 億、FCF 269.1 億；FCF margin 42.1%；FCF / 淨利 1.16x。
- TTM 營業現金流 406.5 億 (與 info operatingCashflow 40,653 一致)、資本支出 12.5 億、FCF 394.0 億；TTM FCF margin 44.2%；TTM FCF / 淨利 1.03x (>0.9，健康)。
- info 之 freeCashflow 為 305.96 億，與報表加總之 394.0 億不一致，本報告採報表加總值。
- SBC：TTM 約 84.8 億美元，占營收 9.5%。SBC 為非現金費用，本報告之 FCF 定義未扣除 SBC，若以扣除 SBC 之自由現金流計算，FCF margin 約為 34.7%。

**資產負債表 (FQ3 FY26，2026-07 季末)**
- 現金及約當現金 239.75 億；總負債 594.19 億；淨負債 354.44 億。
- 淨負債 / TTM EBITDA (523.49 億) ≈ 0.68x。
- 流動比率 2.50x；速動比率 2.15x。
- 負債 / 股東權益 59.6%；股東權益 996.90 億，每股帳面價值 20.88 美元。
- 負債期間趨勢：總負債由 FY2025 末 651.36 億降至 FQ3 FY26 594.19 億；淨負債由 489.58 億降至 354.44 億，償債能力持續改善。

## Capital allocation & insider signal
**資本配置**
- 資本支出：FY2022 4.2 億、FY2023 4.5 億、FY2024 5.5 億、FY2025 6.2 億 (占營收約 1%，屬 fabless 模式)；TTM 12.5 億，近季上升 (FQ3 FY26 單季 5.32 億)。
- 股利：每股季配息 0.65 美元 (dividendRate 2.60，殖利率 0.77%)；TTM 現金股利 120.8 億。
  - 股利覆蓋：TTM FCF / 股利 3.26x；TTM 淨利 / 股利 3.17x。配息覆蓋充足。
  - exDividendDate 約 2026-09-21 (已過)；dividendDate (支付日) 約 2026-09-30 (依 yfinance epoch 轉換，需以官方公告為準)。
- 買回：FY2022 84.6 億、FY2023 76.9 億、FY2024 123.9 億、FY2025 63.1 億；TTM 84.5 億 (FQ1 FY26 78.5 億、FQ2 FY26 6.0 億)；FQ3 FY26 為零買回。
- 股本：流通股數由 FQ4 FY25 的 47.41 億增至 FQ3 FY26 的 47.74 億 (+0.7%)，買回尚不足以抵銷 SBC 稀釋。
- 債務：FY2025 還債 184.8 億、借債 156.7 億；FQ3 FY26 還債 56.3 億、未新增借債，顯示轉向去槓桿。

**內部人交易 (近 6 個月，2026-04-22 至 2026-10-22)**
- 公開市場賣出 (Sale)：約 740,885 股，金額約 2.837 億美元。主要賣方：Mark Brazeal (多筆 25,000 股賣出，約 97 萬至 1,003 萬美元一筆)、Henry Samueli (董事，2026-06-24 賣出 654,241 股，約 2.50 億美元)、Gayla Delly (董事)、Justine Page (董事)。
- 公開市場買進 (Purchase)：Harry You 於 2026-06-11 買進 1,000 股，約 37.4 萬美元。
- 其他：Stock Gift (贈與) 與 Stock Award (授予) 多筆，不計入買賣淨額；CFO Amie O'Toole 2026-06-15 獲授 50,000 股。
- 淨額：約 -2.833 億美元，占市值 1,612.5 億美元之 0.018%，訊號強度低。內部人持股僅 1.92%，未見高階主管 (CEO Hock Tan) 在此區間之公開市場賣出，但 2025 年 12 月至 2026 年 1 月 Tan 曾有大額賣出紀錄 (屬更早期間)。
- 注意：yfinance 資料無法確認交易是否屬 10b5-1 預設計畫，需以 SEC Form 4 逐筆核對。
- 空方部位：short interest 542.0 萬股 (占流通 1.16%)，short ratio 2.01 日，較上月 504.5 萬股增加。

## Valuation
以股價 337.80 美元 (cnyes 快取，2026-10-22 盤中/盤前價位；前收 334.37) 與市值 1,612.5 億美元計算：
- Trailing P/E：43.1x (GAAP TTM EPS 7.83)。
- Forward P/E：17.4x (共識 forward EPS 19.40)；PEG (info pegRatio) 0.33。
- EV / EBITDA：31.5x (EV 1,648.0 億，EBITDA 523.5 億)。
- EV / 營收 (TTM)：18.5x；P/S (TTM)：18.1x。
- P/FCF (TTM)：40.9x；P/B：16.2x。
- 行業中位數：本報告無即時產業資料，下列為估計值：大型半導體 forward P/E 約 25–30x、EV/EBITDA 約 20–25x、P/S 約 10–12x、P/FCF 約 30–35x。依此估計，AVGO 在 forward P/E 與 P/S 以外多數指標為溢價。
- 分析師共識：47 位，recommendationMean 1.26 (strong_buy)；strong buy 7 / buy 40 / hold 3 / sell 0。目標價均值 527.59、中位數 535.00、最高 660.00、最低 215.88 (離散度大)。相對現價之上行空間：均值 +56.2%、中位數 +58.4%。
- 股價位置：52 週區間 289.96–495.00；現價距高點 -31.8%、距低點 +16.5%；52 週變動 -1.9% (同期 S&P 500 +15.8%)；50 日均線 360.54、200 日均線 368.04，現價位於兩線之下；beta 1.476。

## Key catalysts
- 下次財報：2026-12-09 (yfinance 標示，isEarningsDateEstimate = False)，對應 FQ4 FY26；共識 EPS 估計 3.83 (非 GAAP 口徑，依 yfinance earnings_dates 之 EPS 慣例)。
- 前一季財報：2026-09-02 (FQ3 FY26)。EPS 估計 3.24，但快取之 Reported EPS 為空 (DATA_UNAVAILABLE)；GAAP 稀釋 EPS 為 2.68 (非 GAAP，無法與 3.24 直接比較)。
- 營收動能：FQ3 FY26 營收 YoY +85.5%、QoQ +33.3%，是近期最主要的基本面催化劑；後續需觀察 FQ4 FY26 指引與 AI 相關營收占比 (DATA_UNAVAILABLE：yfinance 未提供指引與分部細項)。
- 股利：每季 0.65 美元，除息日依公告。
- 資本配置：FQ3 FY26 買回為零，後續買回節奏與 SBC 稀釋是 EPS 成長的變數。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 (TTM, 百萬美元) | 89,104 | +85.5% (FQ3 單季) / +23.9% (FY25) | n/a | 強勁 |
| 3 年營收 CAGR (FY22–25) | 24.4% | n/a | 約 10–15% (估計) | 優於同業 |
| 毛利率 (TTM) | 68.8% | FY25 67.8% vs FY24 63.0% | 約 55–60% (估計) | 優 |
| 營業利益率 (TTM) | 48.5% | FY25 40.8% vs FY24 29.1% | 約 25–35% (估計) | 優 |
| 淨利率 (TTM) | 42.9% | FY25 36.2% vs FY24 11.4% | 約 20–25% (估計) | 優 |
| ROE | 44.2% (info) / 38.4% (計算) | n/a | 約 20–25% (估計) | 優 |
| ROIC (估計) | 約 20.2% | n/a | 約 12–15% (估計) | 優 |
| FCF margin (TTM) | 44.2% | FY25 42.1% | 約 25–30% (估計) | 優 |
| FCF / 淨利 (TTM) | 1.03x | FY25 1.16x | 約 0.8–1.0x (估計) | 健康 (>0.9) |
| 淨負債 (百萬美元) | 35,444 | 由 48,958 降低 | n/a | 健康 |
| 淨負債 / EBITDA | 0.68x | n/a | 約 0.5–1.0x (估計) | 健康 |
| 流動比率 | 2.50x | n/a | 約 1.5–2.0x (估計) | 健康 |
| 負債 / 股東權益 | 59.6% | 由 FY25 末 80.1% 降低 | 約 40–60% (估計) | 中性 |
| 資本支出 / 營收 (TTM) | 1.4% | FY25 1.0% | 約 3–8% (估計) | 輕資產 |
| 股利覆蓋 (FCF / 股利, TTM) | 3.26x | n/a | n/a | 充足 |
| 股本變動 (FQ3 vs FQ4 FY25) | +0.7% | n/a | n/a | 輕微稀釋 |
| SBC / 營收 (TTM) | 9.5% | n/a | 約 3–6% (估計) | 偏高 |
| 內部人淨買賣 (6 個月) | 約 -2.83 億美元 | 占市值 0.018% | n/a | 中性 (訊號弱) |
| Trailing P/E | 43.1x | n/a | 約 35x (估計) | 偏貴 |
| Forward P/E | 17.4x | n/a | 約 25–30x (估計) | 相對便宜 |
| EV / EBITDA (TTM) | 31.5x | n/a | 約 20–25x (估計) | 偏貴 |
| P / FCF (TTM) | 40.9x | n/a | 約 30–35x (估計) | 偏貴 |
| P / S (TTM) | 18.1x | n/a | 約 10–12x (估計) | 偏貴 |
| 分析師目標價均值上行空間 | +56.2% | n/a | n/a | 共識正面 |
| 股價 vs 200 日均線 | -8.2% | n/a | n/a | 技術面偏弱 |

## Red flags
- 資料品質：本次 yfinance 即時呼叫之 financials / balance_sheet / cashflow / quarterly 系列回傳 TSMC 規模 (NT$ 計價、12 月 FYE、revenue 約 3.8 兆) 的資料，且 info 輸出末端附帶 "Advanced Micro Devices" 之殘留區塊；已全數棄用，改用 `prices/yf/AVGO.json` 快取。上游快取或工具路徑需排查。
- info 與報表不一致：info grossProfits 672.87 億 vs 報表四季加總 612.77 億；info freeCashflow 305.96 億 vs 報表加總 394.03 億；本報告採報表加總值。
- GAAP 與非 GAAP 混用：trailing P/E 以 GAAP EPS 7.83 計算，而 forward EPS 19.40 為共識 (非 GAAP) 口徑，兩者差距大，trailing P/E 偏高不宜單獨解讀。
- 估值偏高：EV/EBITDA 31.5x、P/FCF 40.9x、P/S 18.1x，遠高於一般半導體中位數 (估計)；估值依賴 AI 營收持續高速成長。
- 營收波動大：FY2024 淨利率僅 11.4%，FY2023 營收成長僅 7.9%，顯示獲利與營收週期性仍明顯。
- SBC 稀釋：TTM SBC 占營收 9.5%，流通股數仍增加 0.7%；FQ3 FY26 買回為零。
- 內部人大額賣出：6 個月內賣出約 2.84 億美元 (以董事 Samueli 單筆 2.50 億美元為主)；金額占市值極小，但仍需追蹤是否為 10b5-1 計畫。
- 股價弱於大盤與均線：52 週 -1.9% vs S&P 500 +15.8%；股價低於 50 日與 200 日均線；short ratio 由 50.5 百萬股升至 54.2 百萬股。
- 財報缺口：2026-09-02 之 Reported EPS (非 GAAP) 於快取中為空，FQ3 FY26 實際 vs 估計無法驗證；分部營收與 FQ4 FY26 指引為 DATA_UNAVAILABLE。
- 價格為盤中/盤前快照 (fast_info 來源 cache，cached_at 2026-10-22T11:36:58Z；info marketState = PRE)，非收盤價；分析應以收盤價更新。
- 資料時效：無 2026-10-22 之後的資料被使用；下次財報 2026-12-09 為未來事件。

FUNDAMENTALS REPORT COMPLETE
