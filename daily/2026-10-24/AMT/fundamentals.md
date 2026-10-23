# Fundamentals — AMT (American Tower) as of 2026-10-24

## Executive summary
AMT 的營收與 EBITDA 穩定成長（FY2025 營收 USD 10.64B，YoY +5.1%；operating margin 46.3%），FCF 對股利覆蓋約 1.2x，財務體質屬於「高槓桿、低流動性但現金流穩定」的 REIT 型態：淨負債/EBITDA 約 5.0x，短期債務 USD 5.23B 高於現金 USD 1.76B，有形淨值為負。估值方面，TTM P/E 約 25.0x、forward P/E 約 26.0x、EV/EBITDA 約 19.1x，相對於一般 REIT 估計中位數屬於偏高；FFO/AFFO 官方數字在資料源中缺漏，以下 FFO 為估算代理值，僅供趨勢參考。

資料時點說明：報告 as-of 2026-10-24；價格與 fast_info 來自 cache（cached_at 2026-10-23T11:26 UTC），屬正常 cache 回退，未出現晚於 2026-10-24 的資料。下一次財報為 2026-10-27，尚未發布。

## Revenue & profitability

**營收（USD B，年度）**

| 年度 | 營收 | YoY | Gross margin | Operating margin (reported) | 淨利（普通股） | Net margin |
|---|---|---|---|---|---|---|
| FY2022 | 9.645 | n/a | 73.4% | 30.3% | 1.766 | 18.3% |
| FY2023 | 10.012 | +3.8% | 74.4% | 35.3% | 1.483 | 14.8% |
| FY2024 | 10.127 | +1.1% | 74.6% | 45.5% | 2.255 | 22.3% |
| FY2025 | 10.645 | +5.1% | 74.2% | 46.3% | 2.530 | 23.8% |

- 3 年營收 CAGR（FY2022→FY2025）：約 3.3%。feed 中 FY2021 營收為 null，無法計算 3–5 年 CAGR 的完整區間，此處以 3 年為上限。
- 季度營收（USD B）：Q2'25 2.627、Q3'25 2.717、Q4'25 2.738、Q1'26 2.738、Q2'26 2.749；Q2'26 YoY 約 +4.7%，與 info 的 revenueGrowth 0.047 一致。注意 Q4'25 與 Q1'26 營收完全相同（2,737.5M），疑似資料重複，需人工確認。
- 營收結構：feed 的 longBusinessSummary 僅描述為「超過 148,000 座通訊站點」與美國 data center 資產，未提供分部營收拆分，**segment mix: DATA_UNAVAILABLE**。
- 獲利率：Operating margin 由 FY2022 的 30.3% 升至 FY2025 的 46.3%，主要因 FY2023 有較大的減損與特殊項目（Impairment 280M 等）；FY2024 淨利含已終止營運損失 -978.3M 與 Sale of Business 現金流入 2,158.8M，FY2024 淨利屬於非經常性項目混雜，不宜直接外推。
- EBITDA（yfinance 標準）：FY2025 6.445B（EBITDA margin 60.5%）；normalized EBITDA 7.338B（68.9%）；TTM EBITDA 7.044B。
- EBIT：FY2025 4.404B（pretax 3.044B + interest expense 1.359B）。
- ROE：info 顯示 33.9%，但普通股權益僅 USD 3.72B（2026-06-30），受負的留存盈餘與大額資本回收影響，ROE 數字不具參考性。
- ROIC（估算）：NOPAT = EBIT × (1 − 13.7% 有效稅率) ≈ 3.80B，除以 FY2025 invested capital 40.87B，約 9.3%。資料未提供 WACC，無法判斷是否超過資本成本。

**EPS（GAAP diluted）**：FY2022 3.82、FY2023 3.18、FY2024 4.82、FY2025 5.40。TTM GAAP EPS 為 7.27，高於 FY2025 的 5.40，主因 Q2'25 單季 EPS 僅 0.78（含特殊項目）已滾出 TTM 窗口。

**FFO / AFFO**：yfinance 資料源未提供 **FFO / AFFO 官方數字（DATA_UNAVAILABLE）**。
- 估算代理值（非公司公告口徑）：FY2025 淨利（普通股）2.530B + 折舊攤銷 2.042B ≈ 4.571B，除以 diluted 股數 468.8M，約 USD 9.75/股。此值未扣除 Gain on Sale of Security（IS 項目 -809.4M）與 Impairment（100.7M）等調整，且折舊攤銷包含非不動產無形資產，僅作趨勢參考。
- 以估算 FFO 計：P/FFO 約 18.6x；股利 USD 7.16 / 估算 FFO 約 73%（覆蓋約 1.36x）。

## Cashflow & balance sheet

**現金流（USD B）**

| 年度 | 營業現金流 (CFO) | 資本支出 (Capex) | FCF (CFO − Capex) | FCF margin | FCF / 淨利 | 股利支付 | FCF / 股利 |
|---|---|---|---|---|---|---|---|
| FY2022 | 3.696 | 1.874 | 1.823 | 18.9% | 1.03x | 2.630 | 0.69x |
| FY2023 | 4.722 | 1.798 | 2.924 | 29.2% | 1.97x | 2.949 | 0.99x |
| FY2024 | 5.291 | 1.590 | 3.701 | 36.5% | 1.64x | 3.075 | 1.20x |
| FY2025 | 5.464 | 1.680 | 3.784 | 35.5% | 1.50x | 3.157 | 1.20x |
| TTM（Q2'25 起算至 Q2'26，季度加總） | — | 1.815 | 3.960 | 36.2% | 1.16x | 3.234 | 1.22x |

- FCF/淨利 在 FY2025 為 1.50x，高於 0.9 健康門檻；但淨利受大額折舊攤銷（D&A 2.04B）壓抑，用 FCF/NI 判斷品質需保留。
- info 的 freeCashflow（TTM）為 2.920B，與季度現金流表加總的 3.960B 差距約 1.04B，**兩者口徑不一致，待確認**；若採用 2.920B，TTM FCF margin 約 26.7%，P/FCF 約 29.0x（以 3.960B 計約 21.4x）。
- 經營現金流 FY2025 5.464B，較 FY2024 的 5.291B 增加 3.3%。

**資產負債表（USD B，2026-06-30 為最新季）**

| 項目 | 2026-06-30 | 2025-12-31 | 說明 |
|---|---|---|---|
| Total assets | 63.300 | 63.190 | |
| Goodwill + intangibles | 26.162 | 26.786 | 佔總資產約 41% |
| Cash & equivalents | 1.763 | 1.475 | 季增 |
| Total debt | 44.980 | 44.964 | 季間持平 |
| Current debt（含 current portion） | 5.227 | 3.388 | 短期債務上升 |
| Net debt | 35.427 | 35.746 | 微幅降低 |
| Common stockholders' equity | 3.720 | 3.653 | |
| Minority interest (NCI) | 6.533 | 6.703 | |
| Tangible book value | -22.442 | -23.134 | 有形淨值為負 |
| Current ratio | 0.35x | 0.40x（由 2,741.8 / 6,913.8 計） | 流動資產低於流動負債 |

- 淨負債 / EBITDA（TTM）：35.43 / 7.04 ≈ 5.0x；FY2025 normalized 約 4.9x。
- 總負債 / 權益（info 口徑，含 NCI）：438.7%（即 4.39x）。
- 利息覆蓋（EBIT / 利息費用，FY2025）：4.404 / 1.359 ≈ 3.2x。
- 短期債務覆蓋：現金 1.763B / current debt 5.227B ≈ 0.34x，需依賴再融資或循環信貸。
- 股本：2026-06-30 流通股數 465.96M，較 FY2025 減少約 0.1%（diluted 平均股數 FY2025 468.8M，FY2024 468.1M，年增約 0.1%）。

## Capital allocation & insider signal

**資本配置**
- 資本支出：FY2022 1.874B → FY2023 1.798B → FY2024 1.590B 逐年下降，FY2025 回升至 1.680B（YoY +5.7%）；TTM 1.815B，約為 D&A 的 0.9x。
- 股利：年化 USD 7.16（每季 USD 1.79），殖利率 3.94%。FY2025 股利支付 3.157B，對 FCF 覆蓋 1.20x，對 GAAP 淨利 0.80x（以股利 USD 7.16 / GAAP diluted EPS 5.40 計，支付率約 133%）。info 的 payoutRatio 0.96 與 trailing EPS 7.27 之計算基礎不同，本報告以 FCF 與估算 FFO 為主判斷覆蓋。
- 買回：FY2025 回購 0.365B，FY2024 與 FY2023 為 0，FY2022 為 0.019B。回購規模小，主要資本用於股利與債務償還。
- 債務操作：FY2025 發行 9.078B、償還 9.450B，淨償還約 0.37B；2026 年前半季度債務總額穩定於 45B 左右。

**內部人交易（過去 6 個月，2026-04-23 至 2026-10-23）**

| 日期 | 人員 | 職位 | 類型 | 股數 | 金額 (USD M) |
|---|---|---|---|---|---|
| 2026-04-29 | Ruth T. Dowling | General Counsel | 賣出 @177.54–178.48 | 972 | 0.173 |
| 2026-07-29 | Robert J. Meyer Jr. | Officer | 賣出 @178.89 | 5,000 | 0.894 |
| 2026-07-29 | Ruth T. Dowling | General Counsel | 賣出 @169.54–174.96 | 1,791 | 0.310 |
| 2026-08-21 | Rajesh Kalathur | Director | 買入 @177.00 | 2,829 | 0.501 |

- 6 個月內公開市場賣出合計 USD 1.38M，買入合計 USD 0.50M，淨賣出約 USD 0.88M，佔市值（USD 84.60B）約 0.001%，規模極小，不構成明顯訊號。
- 其他為 2026-03-10 與 2026-10-01 之例行股票授予（price 0），以及 2026-05-28 的股票贈與，不計入交易淨額。
- 6 個月窗口以外的參考：2026-02-17 至 2026-03-04 期間 CEO Steven Vondran、COO Eugene Noel、CFO Rodney Smith 有選擇權行使後賣出，合計賣出金額約 USD 20.8M（CEO 6.31M、COO 7.87M、CFO 6.60M，價格約 188–193），屬行使後出售，非 6 個月窗口內交易。
- 內部人持股比例 0.08%（insidersPercentHeld）；機構持股 96.9%，機構數 2,387。前幾大持股：BlackRock 9.83%（2026-06-30，季增 +1.87%）、Vanguard 合計約 12.5%、State Street 4.74%。JPMorgan 持股季減 41.5%。

## Valuation

| 指標 | 數值 | 計算基礎 |
|---|---|---|
| 股價（cache） | USD 181.57 | yfinance fast_info / info |
| 市值 | USD 84.60B | info |
| 企業價值 (EV) | USD 134.35B | info |
| Trailing P/E（TTM EPS 7.27） | 25.0x | info |
| Trailing P/E（FY2025 GAAP EPS 5.40） | 33.6x | 181.57 / 5.40 |
| Forward P/E（forward EPS 6.98） | 26.0x | info |
| EV / EBITDA（TTM） | 19.1x | info |
| P / FCF（TTM，statement 口徑 3.960B） | 21.4x | 84.60 / 3.960 |
| P / FCF（TTM，info 口徑 2.920B） | 29.0x | 84.60 / 2.920 |
| P / FFO（估算代理） | 18.6x | 181.57 / 9.75 |
| P / S（TTM） | 7.7x | info |
| P / B | 22.7x | info |
| 股利殖利率 | 3.94% | info |
| 分析師目標價（均值，23 位） | USD 215.74（較現價 +18.8%） | info |

- 技術面位置（ta snapshot，as_of 2026-10-22）：價格高於 MA50 (174.39) 約 4.1%、高於 MA200 (176.98) 約 2.6%，距 52 週高點 196.08 約 −7.4%，距 52 週低點 160.06 約 +13.4%。此段僅為估值背景，非交易建議。
- 估值判讀：以 FFO 估算值計 P/FFO 約 18.6x，但 EV/EBITDA 19.1x 與 forward P/E 26.0x 偏高；相較一般 REIT 估計中位數（見下方表格，屬粗略估計），AMT 估值屬偏高區間，需仰賴營收與 AFFO 成長維持倍數。

## Key catalysts

- **下一次財報：2026-10-27**（feed 時間 12:00 UTC），EPS 估計 1.63（Q3'26）。資料源未標明此估計的 GAAP 或調整口徑，需與 FFO/AFFO 區分。
- 近四季 EPS 表現（feed 與季度損益表一致，為 GAAP diluted 口徑）：Q3'25 1.82 vs 1.65（+10.1%）、Q4'25 1.75 vs 1.47（+19.1%）、Q1'26 1.84 vs 1.57（+17.0%）、Q2'26 1.86 vs 1.55（+20.7%），近四季平均超預期約 16.7%。2025 年 Q2 則為 0.78 vs 1.66（−53.0%），屬特殊項目，列為紅旗。
- 近期指引（guidance）：**DATA_UNAVAILABLE**，feed 未提供公司年度 AFFO 或營收指引。
- 股利：最近一次每股 USD 1.79（季）；feed 的 exDividendDate 為 1790726400（Unix 時間，換算約 2026-09-30），下次股利資訊需以公司公告為準。
- 資產面：feed 的 CF 顯示 FY2024 Sale of Business 現金流入 2.159B；FY2025 資本支出回升至 1.680B，財報中 AFFO 與資本支出指引為觀察重點。

## Metrics table

以下欄位單位：營收、淨利、現金流、資產、負債、市值為 USD B 或 USD M（表頭已標示），**全報告未使用 億**。Sector median 為估計值，非資料源數字，僅供粗略參照。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 (USD B) | 10.645（FY2025） | +5.1% | 約 +4%–6%（估計） | 中性偏正向 |
| 營收 3 年 CAGR (FY22–25) | 3.3% | n/a | 約 4%–6%（估計） | 偏慢 |
| Gross margin | 74.2%（FY2025） | −0.4 pt | 約 70%–80%（估計） | 優 |
| Operating margin (reported) | 46.3%（FY2025） | +0.8 pt | 約 35%–45%（估計） | 優 |
| Net margin (GAAP) | 23.8%（FY2025） | +1.5 pt | 約 15%–25%（估計） | 中性 |
| EBITDA margin (yf 標準) | 60.5%（FY2025） | −10.1 pt（FY2024 為 70.6%） | 約 55%–65%（估計） | 中性 |
| FFO / AFFO | DATA_UNAVAILABLE（估算 FFO/股 USD 9.75） | n/a | n/a | 無法判斷 |
| ROE | 33.9%（TTM，info） | n/a | 約 8%–12%（估計） | 不具參考性（權益基數小） |
| ROIC（估算） | 9.3%（FY2025） | n/a | 約 5%–7%（估計） | 中性偏正向，無 WACC 比對 |
| FCF (USD B) | 3.960（TTM，statement）；2.920（info） | n/a | n/a | 口徑待確認 |
| FCF margin | 35.5%（FY2025）/ 36.2%（TTM） | −1.0 pt（FY） | 約 25%–35%（估計） | 優 |
| FCF / 淨利 | 1.50x（FY2025） | n/a | 約 0.9x 以上為健康 | 健康 |
| 淨負債 / EBITDA | 5.0x（TTM） | −0.1x（normalized 口徑：FY24 5.0x → FY25 4.9x） | 約 5.5x–6.5x（估計） | 中性（槓桿略低於同業估計） |
| Current ratio | 0.35x（2026-06-30） | 較 FY2025 的 0.40x 下降 | 約 1.0x（估計） | 偏弱 |
| 負有形淨值 (TBV, USD B) | −22.44（2026-06-30） | 略改善（由 −23.13） | 正值為常態（估計） | 偏弱 |
| 總負債 / 權益（含 NCI） | 438.7%（info） | n/a | n/a | 偏高，受權益基數影響 |
| 利息覆蓋 (EBIT / 利息) | 3.2x（FY2025） | n/a | 約 3x–4x（估計） | 中性偏弱 |
| 短期債務 / 現金覆蓋 | 0.34x（2026-06-30） | n/a | n/a | 偏弱 |
| 資本支出 (USD B) | 1.680（FY2025） | +5.7% | n/a | 2024 低點後回升 |
| 股利 (年化 USD/股) | 7.16 | 不變（季 1.79） | 約 3.5%–4.0% 殖利率（估計） | 中性 |
| 股利殖利率 | 3.94% | n/a | 約 3.5%–4.0%（估計） | 中性 |
| 股利 / FCF 覆蓋 | 1.20x（FY2025）；1.22x（TTM） | 持平 | 約 1.2x–1.5x（估計） | 尚可 |
| 股利 / 估算 FFO 覆蓋 | 約 1.36x | n/a | 約 1.2x–1.3x（估計） | 尚可 |
| 內部人 6 個月淨交易 (USD M) | −0.88 | n/a | n/a | 中性（規模極小） |
| 內部人持股 | 0.08% | n/a | 約 0.1%–1%（估計） | 偏低 |
| 機構持股 | 96.9%（2,387 家） | n/a | n/a | 高度機構化 |
| Trailing P/E | 25.0x | n/a | 約 20x–25x（估計，REIT 含 FFO 口徑差異大） | 偏高 |
| Forward P/E | 26.0x | n/a | 約 20x–25x（估計） | 偏高 |
| EV / EBITDA (TTM) | 19.1x | n/a | 約 18x–20x（估計） | 中性偏高 |
| P / FFO（估算） | 18.6x | n/a | 約 15x–18x（估計） | 中性偏高 |
| P / FCF (TTM) | 21.4x（statement）；29.0x（info） | n/a | 約 18x–25x（估計） | 中性 |
| P / S (TTM) | 7.7x | n/a | 約 6x–8x（估計） | 中性偏高 |
| 分析師目標價均值 | USD 215.74（+18.8%） | n/a | n/a | 參考（非本報告建議） |

## Red flags
- 短期債務 USD 5.23B 遠高於現金 USD 1.76B（覆蓋 0.34x），current ratio 0.35x，依賴再融資與循環信貸。
- 有形淨值為負（TBV −USD 22.44B），商譽加無形資產佔總資產約 41%，資產減損風險需長期觀察。
- 淨負債 / EBITDA 約 5.0x，利息覆蓋約 3.2x；利息費用 FY2025 1.36B 佔 EBIT 約 31%。
- 營收成長緩慢（FY2022–25 CAGR 3.3%；FY2024 僅 +1.1%），FY2024 淨利含已終止營運損失 -978.3M，獲利波動大。
- 股利以 GAAP 淨利計支付率約 133%，雖以 FCF 與估算 FFO 覆蓋約 1.2x–1.4x，但若 AFFO 轉弱，覆蓋將縮小。
- FFO / AFFO 官方數字為 DATA_UNAVAILABLE，目前估值判斷僅能依賴估算值與 GAAP 指標，存在誤差。
- 資料一致性問題：(1) Q4'25 與 Q1'26 季度營收同為 2,737.5M，疑似重複；(2) TTM FCF 在 info（2.920B）與季度現金流表加總（3.960B）差距約 1.04B；(3) info 的 payoutRatio 0.96 與 trailing EPS 7.27 與 GAAP 口徑不一致。建議下游在引用前人工核對。
- 2026-02 至 2026-03 管理層大額選擇權行使後出售（合計約 USD 20.8M），雖在 6 個月窗口外，但屬高階主管集中賣出，值得留意。
- 估值偏高：forward P/E 26.0x、EV/EBITDA 19.1x，若營收與 AFFO 成長不及預期，倍數回落風險大。
- 2026-10-27 財報前，EPS 口徑（GAAP 或 AFFO）與指引資料缺漏，財報前不確定性高。

FUNDAMENTALS REPORT COMPLETE
