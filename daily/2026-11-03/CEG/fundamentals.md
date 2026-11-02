# Fundamentals — CEG as of 2026-11-03

## Executive summary
Constellation Energy (CEG) 的獲利與估值面有亮點：Q2 2026 調整後 EPS 2.55 優於預估 2.28 (+11.7%)，以 fast_info 現價約 266.6 計算，forward P/E 約 19.9x、EV/EBITDA 約 14.8x。然而財務健全度在 2026 年上半年明顯轉弱：總負債 (Total Debt) 由 2025-12-31 的 8.99B 跳升至 2026-06-30 的 24.70B，淨負債 (Net Debt) 由 5.35B 增至 24.00B，現金僅剩 0.70B；TTM FCF 僅約 0.31B，FCF/NI 約 0.09，股本同期增加約 13.8%。綜合判斷：獲利動能與估值尚可接受，但資產負債表擴張與自由現金流缺口是主要風險，財務健全度評為「中性偏弱」。

資料時點說明：yfinance 最新季度為 2026-06-30 (Q2 2026)，價格來源為 fast_info 快取 (cached_at 2026-11-02 15:30 UTC)。下一次財報為 2026-11-09，除息日約為 2026-11-16（由 exDividendDate 換算，為估計），兩者皆為 as-of 之後的未來事件，非資料外洩。

## Revenue & profitability
**營收 (USD B，yfinance annual / quarterly)**

| 期間 | 營收 (USD B) | YoY |
|---|---|---|
| FY2022 | 24.44 | n/a |
| FY2023 | 24.92 | +2.0% |
| FY2024 | 23.57 | -5.4% |
| FY2025 | 25.53 | +8.3% |
| Q2 2025 | 6.10 | n/a |
| Q3 2025 | 6.57 | n/a |
| Q4 2025 | 6.07 | n/a |
| Q1 2026 | 11.12 | n/a (Q1 2025 資料為 null) |
| Q2 2026 | 7.50 | +23.0% |

- 3 年 CAGR (FY2022→FY2025)：約 +1.5%。yfinance 未提供 2021 年資料，無法計算 4-5 年 CAGR。
- TTM 營收 (Q3'25 至 Q2'26) 合計約 31.27B，明顯高於 FY2025 的 25.53B。Q1 2026 營收 11.12B 為單季高點，資產、股本與負債在 2026Q1 同步大幅跳升，**推測為併購或大型交易完成所致，但 yfinance 未提供交易公告，需由基本面研究者以公司公告再行確認。**
- 業務組成：yfinance 僅提供 longBusinessSummary，描述五大區段 (Mid-Atlantic、Midwest、New York、ERCOT、Other Power Regions)，裝置容量約 31,676 MW，涵蓋核能、風能、太陽能、天然氣與水力。**區段營收與毛利明細：n/a。**

**獲利能力**

| 指標 | FY2022 | FY2023 | FY2024 | FY2025 | TTM (至 Q2'26) |
|---|---|---|---|---|---|
| 毛利率 (Gross Profit / Revenue) | 8.7% | 13.0% | 25.4% | 18.4% | 21.4% |
| 營業利益率 (Operating Income / Revenue) | -1.7%* | 9.6% | 20.6% | 16.4% | 14.3% |
| 淨利率 (Net Income / Revenue) | -0.7% | 6.5% | 15.9% | 9.1% | 11.1% |
| Diluted EPS (GAAP, USD) | -0.49 | 5.01 | 11.89 | 7.40 | 約 10.26 |

*FY2022 Operating Income 為 -0.408B / 24.44B = -1.7%。

- 毛利率 FY2024 的 25.4% 在 FY2025 回落至 18.4%，顯示成本端或價格端壓力；TTM 回升至 21.4%，主要來自 Q1 2026 毛利 2.99B。
- **Q2 2026 GAAP 營業利益為 -0.047B（負值），但毛利為 1.23B，EBIT 為 1.18B（含其他收益）。** 單季 GAAP 營業利益轉負值為需要留意的訊號。
- GAAP 與調整後 EPS 差距大：Q2 2026 GAAP Diluted EPS 1.42 vs earnings_dates 揭露的 reported EPS 2.55；Q1 2026 GAAP 4.49 vs 2.74。差異可能來自未實現損益、資產處分或其他非經常項目（yfinance Total Unusual Items Q1 2026 為 +0.098B，Q2 2026 為 +1.228B），**應以公司 non-GAAP 調節表為準。**
- ROE：FY2025 以期末股東權益計算為 16.0% (2.319 / 14.517)；TTM 淨利 3.465B 除以 2026-06-30 股東權益 31.98B 為 10.8%（期末權益因併購膨脹，數字偏低）。
- ROIC（估計）：FY2025 以 EBIT 4.02B × (1 - 33.8%) / Invested Capital 23.51B ≈ 11.3%；2026-06-30 Invested Capital 56.68B，以 TTM EBIT 5.90B 與 30% 假設稅率估計約 7.3%。

## Cashflow & balance sheet
**現金流量 (USD B)**

| 指標 | FY2022 | FY2023 | FY2024 | FY2025 | TTM (至 Q2'26) |
|---|---|---|---|---|---|
| 營運現金流 (OCF) | -2.35 | -5.30 | -2.46 | 4.24 | 4.21 |
| 資本支出 (Capex) | -1.69 | -2.42 | -2.57 | -2.95 | -3.90 |
| 自由現金流 (FCF) | -4.04 | -7.72 | -5.03 | 1.29 | 0.31 |
| FCF 利潤率 | n/a | n/a | n/a | 5.0% | 1.0% |
| FCF / 淨利 | n/a | n/a | n/a | 0.56x | 0.09x |
| OCF / 淨利 | n/a | n/a | n/a | 1.83x | 1.21x |

- FY2023、FY2024 的 OCF 為負值，導致 FCF 大幅為負。yfinance 未揭露原因（推測與營運資金、抵押品或能源交易部位有關，需查證）。FY2025 OCF 轉正為 4.24B，但 FCF/NI 僅 0.56x，低於健康門檻 0.9。
- 季度 FCF 波動劇烈：Q3 2025 +1.46B，Q4 2025 -0.18B，Q1 2026 -0.85B，Q2 2026 -0.12B。H1 2026 合計 FCF 為 -0.97B，表示 2026 年上半年的資本支出與營運資金需求超過營運現金流。

**資產負債表 (USD B)**

| 項目 | 2025-06-30 | 2025-12-31 | 2026-06-30 |
|---|---|---|---|
| 總負債 (Total Debt) | 8.31 | 8.99 | 24.70 |
| 現金及約當現金 | 1.97 | 3.64 | 0.70 |
| 淨負債 (Net Debt) | 6.34 | 5.35 | 24.00 |
| 股東權益 | 13.45 | 14.52 | 31.98 |
| 流動資產 | 9.23 | 12.12 | 18.97 |
| 流動負債 | 6.26 | 7.94 | 13.03 |
| 總資產 | 53.04 | 57.25 | 98.25 |

- 淨負債 / TTM EBITDA：約 2.9x（2026-06-30）；FY2025 為 0.9x。TTM EBITDA 以 quarterly_fin 加總約 8.23B 計算。
- 流動比率 (Current Ratio)：2026-06-30 為 1.46x，與 2025-06-30 的 1.48x 相近，短期償債能力尚可。
- 負債權益比 (Total Debt / Equity)：2026-06-30 為 0.77x，2025-06-30 為 0.62x。
- 利息保障倍數 (TTM EBIT / 利息費用)：約 7.5x（TTM 利息費用約 0.78B），FY2025 為 7.9x。利息覆蓋尚可，但利息支出自 FY2025 的 0.51B 增至 TTM 的 0.78B。
- 有形帳面價值 (Tangible Book Value)：2026-06-30 為 20.45B，低於 2026-03-31 的 21.96B。
- 現金水位：2026-06-30 現金僅 0.70B，較 2025-06-30 的 1.97B 下降約 65%，流動性緩衝明顯縮減。

## Capital allocation & insider signal
**資本配置**
- 資本支出：FY2025 為 2.95B（較 FY2024 增 15.0%），佔營收約 11.5%；TTM 為 3.90B，顯示投資強度持續上升。
- 股利：FY2025 現金股利 0.49B（較 FY2024 增 9.5%）；info 顯示 dividendRate 1.71、殖利率 0.65%、payoutRatio 15.9%。以 NI 覆蓋約 4.8x (FY2025)，但以 FCF 覆蓋 FY2025 為 2.65x、TTM 僅 0.56x（TTM 股利約 0.55B）。TTM 股利需部分由舉債支應。
- 買回：FY2023 0.99B、FY2024 1.00B、FY2025 0.40B（僅 Q2 2025 一筆）；H2 2025 與 H1 2026 無買回紀錄。
- 股本變動：流通股數由 2025-12-31 的 312.3M 增至 2026-03-31 的 362.0M，2026-06-30 為 355.3M，較年初增加約 13.8%。股本 (Capital Stock) 由 11.04B 增至 26.68B。**此為大規模股權發行，與上述負債跳升同期，推測與併購有關（需公告確認）。**
- 舉債：TTM 淨舉債合計約 3.9B（Q3'25 +0.72B、Q4'25 -0.04B、Q1'26 +0.97B、Q2'26 +2.26B）。

**內部人交易 (yfinance insider，以 2026-05-02 至 2026-11-02 為 6 個月視窗)**
- 6 個月內實際公開市場交易：董事 Roger W. Crandall 於 2026-08-11 買入 1,500 股，單價 278.62，金額約 0.42M USD。
- 6 個月內其他事件：2026-08-04 Crandall 董事股票授予 462 股（約 0.12M USD）；2026-04-28 其他董事 556 股授予（已超出 6 個月視窗）。
- 6 個月內**無公開市場賣出紀錄**。
- 規模：買入金額約 0.42M USD，占市值 94.59B 之 0.0004%，對估值幾乎無影響，僅屬象徵性買進訊號。
- 歷史參考：2025-02-20 Matthew Bauer 賣出 4,000 股，金額約 1.24M USD（超出視窗）。
- 內部人持股：heldPercentInsiders 0.34%。
- 機構持股：heldPercentInstitutions 82.9%，共 2,479 家機構。前十大包括 Blackrock 6.93%、Vanguard Capital Management 5.94%、State Street 5.48%、Vanguard Portfolio Mgmt 4.47%、ECP ControlCo 4.06%（2026-06-30 季報顯示持股較前期減少 34.8%）、Capital International 3.57%、Invesco 3.14%、Morgan Stanley 2.55%、Geode 2.12%、FMR 1.85%（持股減少 35.8%）。兩大大股東 ECP ControlCo 與 FMR 減持幅度大，需留意潛在籌碼壓力。
- 放空：sharesShort 11.89M，佔流通股 3.75%，short ratio 2.96 日；月增 1.3%。

## Valuation
- 價格基準：fast_info last_price 266.63（快取，2026-11-02）；info fulldayPrice 266.98；previousClose 262.38。市值 94.59B USD，企業價值 (EV) 117.31B USD（yfinance）。
- 股價位置：較 52 週高點 384.98 下跌約 30.7%；52 週漲跌 -30.5%，跑輸 S&P 500 同期 +10.6%；低於 50 日均線 272.64 與 200 日均線 280.04。Beta 1.13。

| 估值指標 | 數值 | 計算基礎 |
|---|---|---|
| Trailing P/E (GAAP TTM EPS 10.23) | 26.1x | info.trailingPE |
| Forward P/E (forwardEps 13.41) | 19.9x | info.forwardPE |
| EV / EBITDA | 14.8x (yfinance)；約 14.3x (TTM 自算 EBITDA 8.23B) | info.enterpriseToEbitda |
| P / S (TTM) | 3.0x | info.priceToSalesTrailing12Months |
| P / OCF (TTM OCF 4.21B) | 22.5x | 自算 |
| P / FCF (TTM FCF 0.31B) | 約 306x，不具參考價值 | 自算 |
| P / FCF (FY2025 FCF 1.29B) | 約 73x | 自算 |
| P / B | 3.0x | info.priceToBook |
| PEG | 3.74 | info.pegRatio |

- Trailing P/E 26.1x 因 GAAP 盈餘含非經常性項目，與調整後盈餘口徑不同，解讀時需保守。以 earnings_dates 揭露的 reported EPS 計算 TTM 調整後 EPS 約 10.63（3.04 + 2.30 + 2.74 + 2.55），對應 P/E 約 25.1x，forward P/E 之 forwardEps 口徑未在 yfinance 中揭露。
- 與產業中位數比較：yfinance 未提供產業中位數，以下為估計值 (estimate)，僅供參考：公用事業 IPP 族群 forward P/E 約 18x、EV/EBITDA 約 11x、P/S 約 2x、P/B 約 1.8x。CEG 相對估計值為溢價，主要因併購後獲利成長預期與核能資產稀缺性；但在 FCF 缺口之下，溢價缺乏現金流支撐。

## Key catalysts
- **下一次財報**：2026-11-09（Q3 2026）。EPS 預估 3.88，較 Q3 2025 調整後 EPS 3.04 成長約 27.6%。過去 8 季中有 5 季優於預估，最近 4 季有 3 季優於預估，Q2 2026 超出 +11.7%。
- **除息**：年化股息 1.71；exDividendDate 換算約 2026-11-16（估計）。
- **營收動能**：Q2 2026 營收 YoY +23.0%；但 Q1 2026 為單季高點，後續季度是否能維持需觀察併購貢獻的延續性。
- **FCF 轉正時點**：H1 2026 FCF 為 -0.97B，Q3 2026 財報將是檢驗營運現金流與資本支出是否回到正向的關鍵。
- **指引 (guidance)**：yfinance 未提供管理層指引，**n/a**。需由公司法說或 SEC filing 補充。
- **籌碼面**：ECP ControlCo 與 FMR 持股減少、放空比率 3.75%，若財報後出現大額減持將造成供給壓力。

## Metrics table
（表格單位：金額 USD B / USD M；比率與倍數為 x 或 %）

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 FY2025 (USD B) | 25.53 | +8.3% | n/a | 中性，成長回升 |
| 營收 TTM (USD B) | 31.27 | n/a (併購影響，推測) | n/a | 規模擴張，需確認併購貢獻 |
| 營收 Q2 2026 (USD B) | 7.50 | +23.0% | n/a | 正向 |
| 3Y 營收 CAGR (FY22-25) | +1.5% | n/a | n/a | 偏弱 |
| 毛利率 TTM | 21.4% | FY24 25.4% → FY25 18.4% | n/a | 中性偏弱 |
| 營業利益率 TTM | 14.3% | FY24 20.6% | n/a | 中性偏弱 |
| 淨利率 TTM | 11.1% | FY24 15.9% | 約 10% (estimate) | 中性 |
| Diluted EPS TTM (GAAP, USD) | 10.26 | FY25 7.40 vs FY24 11.89 (-37.8%) | n/a | 中性偏弱 |
| ROE FY2025 (期末權益) | 16.0% | FY24 28.5% (3.749/13.166) | 約 10-12% (estimate) | 正向（2025 後下滑） |
| ROIC FY2025 (估計) | 11.3% | n/a | 約 7-8% (estimate) | 正向 |
| FCF 利潤率 FY2025 | 5.0% | FY24 為負 | 約 5-10% (estimate) | 中性 |
| FCF 利潤率 TTM | 1.0% | n/a | 約 5-10% (estimate) | 負向 |
| FCF / NI FY2025 | 0.56x | n/a | 約 0.8x (estimate) | 偏弱（低於 0.9） |
| FCF / NI TTM | 0.09x | n/a | 約 0.8x (estimate) | 負向 |
| 淨負債 (USD B, 2026-06-30) | 24.00 | +279% (2025-06-30 為 6.34) | 約 4-5x EBITDA (estimate) | 負向 |
| 淨負債 / TTM EBITDA | 2.9x | FY25 為 0.9x | 約 3-4x (estimate) | 中性偏弱 |
| 流動比率 | 1.46x | 2025-06-30 為 1.48x | 約 1.2x (estimate) | 中性 |
| 負債權益比 (Total Debt / SE) | 0.77x | 2025-06-30 為 0.62x | 約 1.2x (estimate) | 正向（相對產業） |
| 現金 (USD B) | 0.70 | -65% (2025-06-30 為 1.97) | n/a | 負向 |
| 利息保障倍數 (TTM EBIT / 利息) | 7.5x | FY25 為 7.9x | 約 3-4x (estimate) | 正向 |
| 資本支出 TTM (USD B) | 3.90 | FY25 +15.0% | n/a | 投資強度高 |
| 股利 FY2025 (USD B) | 0.49 | +9.5% | n/a | 正向 |
| 股利殖利率 | 0.65% | n/a | 約 2-3% (estimate) | 偏低 |
| 股利 / FCF 覆蓋 TTM | 0.56x | FY25 為 2.65x | 約 1.5x+ (estimate) | 負向 |
| 買回 FY2025 (USD B) | 0.40 | -60% (FY24 為 1.00) | n/a | 中性（已縮減） |
| 流通股數 (M，2026-06-30) | 355.3 | +13.8% vs 2025-12-31 (312.3) | n/a | 負向（稀釋） |
| 內部人 6 個月淨買賣 (USD M) | 約 +0.42 (買入)，無賣出 | n/a | n/a | 中性（象徵性買進） |
| Trailing P/E (GAAP) | 26.1x | n/a | 約 20x (estimate) | 偏貴 |
| Forward P/E | 19.9x | n/a | 約 18x (estimate) | 中性偏貴 |
| EV / EBITDA | 14.8x (yf) / 14.3x (自算) | n/a | 約 11x (estimate) | 偏貴 |
| P / S (TTM) | 3.0x | n/a | 約 2x (estimate) | 偏貴 |
| P / OCF (TTM) | 22.5x | n/a | n/a | 中性偏貴 |
| P / B | 3.0x | n/a | 約 1.8x (estimate) | 偏貴 |
| 股價 vs 52 週高點 | -30.7% | 52 週漲跌 -30.5% | n/a | 負向（技術面弱勢，與基本面需分開看） |
| 股價 vs 200 日均線 | -4.7% | n/a | n/a | 中性偏弱 |
| 放空比率 (% float) | 3.75% | 月增 +1.3% (shares short) | n/a | 中性 |

## Red flags
- 淨負債在 6 個月內由 5.35B 增至 24.00B（+349%），現金僅 0.70B，財務彈性顯著下降。
- TTM FCF 僅 0.31B，FCF/NI 0.09；H1 2026 FCF 為 -0.97B，股利在 TTM 有部分由舉債支應（股利/FCF 0.56x）。
- Q2 2026 GAAP 營業利益為 -0.047B，GAAP EPS 1.42 遠低於調整後 2.55，盈餘品質與調節項目需要查證。
- 股本於 2026 年上半年增加約 13.8%，對每股盈餘形成稀釋，且 yfinance 未揭露交易結構。
- FY2023、FY2024 OCF 為負值，歷史現金流穩定性不足；FY2024 毛利率 25.4% 在 FY2025 回落至 18.4%。
- 大股東 ECP ControlCo 與 FMR 持股分別減少 34.8%、35.8%，需留意籌碼面壓力。
- 資料缺口：2025 年 Q1 季度資料為 null；區段營收、管理層指引、產業中位數 n/a；併購相關資訊需由公告補充。
- 數據一致性提醒：yfinance info 之 trailingEps (10.23) 與 quarterly_fin GAAP 加總 (10.26) 接近，但與 earnings_dates 之調整後 EPS 口徑不同，比較估值時須統一口徑。

FUNDAMENTALS REPORT COMPLETE
