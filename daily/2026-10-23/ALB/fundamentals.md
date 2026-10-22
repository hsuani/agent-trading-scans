# Fundamentals — ALB (Albemarle) as of 2026-10-23

## Executive summary
Albemarle 的財務體質在 2024–2025 年經歷大幅惡化 (FY2025 營收 5.14B USD, 年減 4.4%; FY2025 GAAP 淨損 -0.51B USD)，但 2026 年上半年明顯翻轉：Q2'26 營收 1.74B USD (年增 +31.1%)、毛利率回升至 33.9%，TTM FCF 達 1.33B USD，負債由 2025 年底 3.30B USD 降至 2026 年 6 月底 1.88B USD。估值上，以 2026 年共識 EPS 推算 forward P/E 僅約 8.7x，但 TTM EPS 只有 0.27 USD、trailing P/E 高達 350x，公司獲利仍高度依賴週期性的鋰價復甦與非經常性項目，且股價仍低於 50 日與 200 日均線、距 52 週高點 221.00 USD 已回落約 57%。

## Revenue & profitability

**營收趨勢 (單位: USD B)**

| 年度 | 營收 | YoY |
|---|---|---|
| FY2022 | 7.32 | n/a |
| FY2023 | 9.62 | +31.4% |
| FY2024 | 5.38 | -44.1% |
| FY2025 | 5.14 | -4.4% |

- 3 年 CAGR (FY2022→FY2025) 約 **-11.1%**；FY2021 資料為 null，無法計算 4–5 年 CAGR。
- 季度趨勢：Q3'25 1.31B、Q4'25 1.43B、Q1'26 1.43B、Q2'26 1.74B。TTM 營收 5.91B，與 info 的 totalRevenue 5.908B 相符。Q2'26 對 Q2'25 (1.33B) 年增 +31.1%，與 info revenueGrowth 0.311 一致。Q1'25 季度資料為 null，無法計算 Q1 YoY。
- 分部營收 (Energy Storage / Specialties / Ketjen)：yfinance 未提供分部數字，僅能由 longBusinessSummary 得知三大分部架構，**分部營收占比為 n/a**。

**獲利能力**

| 指標 | FY2022 | FY2023 | FY2024 | FY2025 | TTM (Q3'25–Q2'26) |
|---|---|---|---|---|---|
| 毛利率 | 42.0% | 12.3% | 1.2% | 13.0% | 24.0% (info grossMargins 0.2396) |
| 營業利益率 | 33.9% (Operating Income 2.48B) | 2.0% (Operating Income 0.19B) | -11.9% | 1.3% | 27.7% (info operatingMargins) |
| 淨利率 (NI 含非控制權益) | 36.7% | 16.4% | -21.9% | -9.9% | 3.8% (info profitMargins) |
| 淨利率 (歸屬普通股) | 36.7% | 16.4% | -24.5% | -13.2% | 1.0% (NI to common 57.4M) |

- 營業利益率的 FY2025 數字採 yfinance `Operating Income` 行 (67.3M)；同一報表另一行 `Total Operating Income As Reported` 為 -367.1M，兩者定義不同，本報告以前者為準並標註差異。
- 季度毛利率明顯回升：Q4'25 13.9% → Q1'26 35.1% → Q2'26 33.9%；營業利益率 Q1'26 24.8%、Q2'26 26.4%。
- **ROE 2.65%、ROA 3.17%** (info)。以 EBIT 估算 ROIC：TTM EBIT 344.5M × (1-21%) ÷ Q2'26 投入資本 9.92B ≈ **2.7%** (估計值，稅率 21% 為假設)。
- 盈餘品質警示：FY2025 `Earnings From Equity Interest Net Of Tax` 為 243.7M，FY2024 為 715.4M，非營業的權益法投資收益占 GAAP 淨利比重高；FY2025 `Total Unusual Items` 為 -434.4M。

**EPS**
- GAAP 稀釋 EPS：FY2022 22.84 → FY2023 13.36 → FY2024 -11.20 → FY2025 -5.76。
- 季度：Q2'25 -0.16、Q3'25 -1.72、Q4'25 -3.87、Q1'26 +2.34、Q2'26 +3.52。TTM = 0.27 USD (與 info trailingEps 0.27 相符)。
- 手算驗證：Q2'26 基本 EPS 3.72 × 基本股數 117.96M ≈ 438.7M，與 Net Income Common Stockholders 438.3M 吻合。

## Cashflow & balance sheet

**現金流 (單位: USD B)**

| 年度 | 營業現金流 | 資本支出 | FCF | FCF/NI | FCF 利潤率 |
|---|---|---|---|---|---|
| FY2022 | 1.91 | 1.26 | 0.65 | 0.24x | 8.8% |
| FY2023 | 1.33 | 2.15 | -0.83 | n/m (NI 為正但 FCF 為負) | -8.6% |
| FY2024 | 0.69 | 1.68 | -0.99 | n/m (NI 為負) | -18.5% |
| FY2025 | 1.28 | 0.59 | 0.69 | n/m (NI 為負) | 13.5% |
| TTM | 1.80 | 0.46 | 1.33 | 5.95x (對 NI 224.2M 續營) | 22.6% |

- FCF/NI 健康值 >0.9：FY2025 因 GAAP 淨損，比率無意義；TTM 比率 5.95x 高於門檻，但分子受 D&A (FY2025 658.7M) 與資本支出大幅縮減驅動，分母 NI 含權益法收益，**不應解讀為盈餘品質優異**。以歸屬普通股 NI 計算 TTM 比率高達 23x，同樣不具代表性。
- 季度 FCF：Q2'25 -0.13B、Q3'25 0.22B、Q4'25 0.23B、Q1'26 0.25B、Q2'26 0.64B。

**資產負債表 (單位: USD B)**

| 項目 | FY2022 | FY2023 | FY2024 | FY2025 | Q2'26 (2026-06-30) |
|---|---|---|---|---|---|
| 總負債 (Total Debt) | 3.32 | 4.28 | 3.62 | 3.30 | 1.88 |
| 淨負債 (Net Debt) | 1.72 | 3.28 | 2.32 | 1.58 | 0.25 |
| 現金 | 1.50 | 0.89 | 1.19 | 1.62 | 1.63 |
| 股東權益 (不含非控制權益) | 7.98 | 9.41 | 9.96 | 9.53 | 10.28 |

- 淨負債/EBITDA (Q2'26 淨負債 0.245B ÷ info EBITDA 1.48B) ≈ **0.17x**，槓桿已大幅降低。
- 總負債/股東權益 ≈ **0.19x** (info debtToEquity 18.98 為百分比表示)。
- 流動比率 **2.09x**、速動比率 1.25x (info)；營運資金 Q2'26 為 2.05B。
- 利息保障倍數 (TTM EBIT 344.5M ÷ TTM 利息費用 172.8M) ≈ **2.0x**，偏低，為主要風險點。
- 優先股：2025 年底 Preferred Stock Equity 2.24B；2024 年發行 2.24B 優先股 (現金流量表 Preferred Stock Issuance 2024 為 2.24B)。優先股股利每季約 41.7M，年約 166.8M，構成普通股前的固定請求權。
- 有形帳面價值 (Tangible Book Value) Q2'26 為 6.36B；每股帳面價值 68.14 USD，P/B 1.39x。
- 現金 Q2'26 為 1.63B，較 Q1'26 (1.09B) 增加。

## Capital allocation & insider signal

**資本配置**
- **資本支出**：FY2022 1.26B → FY2023 2.15B → FY2024 1.68B → FY2025 0.59B (年減 -64.9%)。占營收比 FY2025 為 11.5%，FY2024 為 31.3%。TTM 資本支出 0.46B。資本支出大幅收縮，有利短期 FCF，但可能限制未來產能擴張；若鋰價回升，產能開發延後為需追蹤的風險。
- **股息**：每股年配息 1.64 USD，殖利率 1.74%。FY2025 普通股股利 190.5M、優先股股利 166.8M，合計現金股利 357.3M。以 TTM FCF 1.33B 計，股息覆蓋倍數約 **3.7x**；以 FY2025 FCF 0.69B 計約 1.9x。info `payoutRatio` 為 6.0 (600%)，係以 GAAP EPS 計，不具參考性。
- **庫藏股**：現金流量表未見 repurchase 項目，**本期無回購**。
- **債務償還**：FY2025 淨償還債務 454.7M；Q1'26 單季償還 1.31B，為去槓桿主要動作。
- **股本**：普通股流通股數由 2022 年 117.17M 微增至 2026-06-30 的 117.99M；Q2'26 稀釋股數 136.2M (含優先股轉換)，稀釋 EPS 計算已反映。

**內部人交易 (近 6 個月，2026-04-22 至 2026-10-22)**

| 日期 | 內部人 | 職位 | 類型 | 股數 | 金額 (USD M) |
|---|---|---|---|---|---|
| 2026-05-15 | Jerry Kent Masters Jr. | CEO | 公開市場賣出 @ 183.12–184.52 | 16,393 | 3.01 |
| 2026-04-01 | Alejandro Daniel Wolff | 董事 | 股票獎勵 | 25 | 0 |
| 2026-07 (多筆) | 多位董事 (O'Connell、Cramer、Collins、Brlas、Steiner、Desalles、Wolff) | 董事 | 股票獎勵 | 合計 7,804 | 0 |
| 2026-09 (多筆) | Gagarinas、Mummert、Norris、Hood | 高階主管 | 股票獎勵 | 合計 23,646 | 0 |

- 6 個月內**公開市場買進 0 筆**；**公開市場賣出 1 筆** (CEO 16,393 股，約 3.01M USD)。
- 賣出金額相對市值 (info marketCap 11.15B USD) 僅約 **0.03%**，規模極小。內部人持股比例 heldPercentInsiders 僅 0.21%。
- 其餘均為例行股票獎勵，金額 0，非訊號。
- 2026-03 的 CEO 贈與 (30,716 股，5.00M USD，@162.79) 與賣出 (11,783 股，2.01M USD，@170.26–171.82) 落在 6 個月視窗之外，僅供參考。CEO 近期賣價約 183 USD，高於現價約 94 USD，該筆交易為賣在高點，不能解讀為對現價的負面或正面判斷。

**機構持股與空頭**
- 前三大機構：Capital World Investors 8.39%、BlackRock 8.05%、Vanguard Capital Management 6.53%。FMR (Fidelity) 季度增持 10.5%。
- 空頭部位 (yfinance 2026-09 數據)：shares short 11.76M 股，占流通股 11.37%，較前月 9.63M 增加約 22%；short ratio (days to cover) 4.53 天。空頭部位擴大為短期波動的風險因子。
- yfinance `institutionsPercentHeld` 為 101.8%，超過 100%，屬資料端的重複計算或定義問題，**不宜直接使用**。

## Valuation

**估值 (價格 94.47 USD，2026-10-22 盤後/收盤最後成交價)**

| 指標 | 數值 | 計算/來源 |
|---|---|---|
| 市值 | 11.15B USD | info marketCap；94.47 × 117.99M 股 ≈ 11.14B，吻合 |
| 企業價值 (EV) | 14.01B USD | info enterpriseValue；= 市值 11.15 + 總負債 2.00 − 現金 1.63 + 優先股 2.24 + 非控制權益 0.26 |
| Trailing P/E | 349.9x | 94.47 ÷ 0.27；受 GAAP 基期影響失真 |
| Forward P/E | **8.75x** | 94.47 ÷ forwardEps 10.80 |
| 2026 年本年度 P/E | 8.36x | 94.47 ÷ epsCurrentYear 11.29 |
| PEG | 0.79 | info pegRatio |
| EV/EBITDA | 9.45x | info enterpriseToEbitda；EBITDA 1.48B USD |
| P/S (trailing) | 1.89x | info priceToSalesTrailing12Months |
| P/FCF (TTM) | 8.4x | 11.15B ÷ TTM FCF 1.33B |
| P/B | 1.39x | 94.47 ÷ bookValue 68.14 |

- 分析師共識 (21 位)：recommendationMean 1.91 (Buy)；目標價均值 156.35 USD、中位數 161.00 USD、最高 211.00 USD、最低 83.28 USD。均值較現價高約 65%；最低目標價仍略低於現價。
- 技術位置：現價低於 50 日均線 117.25 USD 與 200 日均線 152.50 USD；52 週區間 88.01–221.00 USD，現價距 52 週低點約 +7.3%。
- 價格資料端注意：info `fulldayPrice` 為 92.17 USD (-2.43%)，`regularMarketPrice` 為 94.47 USD (-1.36%)，兩者不一致，本報告以 fast_info `last_price` 94.47 為準。fast_info 因 Yahoo 連線 403 改由 cnyes 快取供應。

**與板塊對比 (板塊中位數為估計值，非工具輸出)**
- 化工/基礎材料板塊的 forward P/E 估計約 15–20x，EV/EBITDA 估計約 10–12x，P/S 估計約 2x，P/FCF 估計約 15–20x。ALB 在 forward 基礎上估值偏低，但 trailing 基礎上不具可比性。

## Key catalysts
- **下次財報**：2026-11-04 (earnings_dates 列示，isEarningsDateEstimate = False)。Q3'26 共識 EPS 2.52 USD，距今約 12 天。
- **上季財報**：2026-08-05 公布 Q2'26 EPS 3.75 USD，優於共識 3.24 USD (+15.7%)。
- **歷史財報反應**：近 4 季 EPS 3 勝 1 負 (Q3'25 +78%、Q4'25 -8.6%、Q1'26 +125%、Q2'26 +16%)。Q1'26 的大幅超預期可能含一次性項目，不宜外推。
- **EPS 成長敘事**：共識 forward EPS 10.80 USD 相對 TTM 0.27 USD，隱含獲利大幅回升，主要驅動為鋰價與產能利用率 (屬於 tools 未提供的外部資料，**本報告無法驗證**)。
- **股息**：配息 1.64 USD/年，最近除息日約 2026-09 中旬 (exDividendDate 換算)，下一個股息日 dividendDate 約 2026-10-01 (epoch 換算)。
- **分部動態與管理層指引**：yfinance 未提供分部營收與公司指引文字，**n/a**，需由 news/sentiment 報告補足。

## Metrics table

單位：USD B / USD M (per share 為 USD)。

| Metric | Latest | YoY | Sector median (estimate, 非工具數據) | Verdict |
|---|---|---|---|---|
| 營收 (TTM, USD B) | 5.91 | FY2025 YoY -4.4%；Q2'26 YoY +31.1% | n/a (板塊估計 ~ 年增 0–5%) | 季度轉強，年度仍弱 |
| 毛利率 (TTM) | 24.0% | Q2'26 33.9% vs Q2'25 14.8% | 約 20–25% | 中性偏好 |
| 營業利益率 (TTM) | 27.7% | FY2025 1.3% | 約 10–15% | 季度強、基期低，需觀察持續性 |
| 淨利率 (TTM, 歸屬普通股) | 1.0% | FY2025 -13.2% | 約 5–8% | 偏弱，受非經常項目影響 |
| ROE | 2.65% | FY2024 負值 | 約 8–12% | 偏弱 |
| ROIC (EBIT 估算) | ≈ 2.7% | n/a | 約 7–10% | 偏弱 |
| FCF (TTM, USD B) | 1.33 | FY2025 0.69 (2024 -0.99) | n/a | 明顯改善 |
| FCF/NI (TTM, 續營 NI) | 5.95x | FY2025 n/m (NI 負) | > 0.9 為健康 | 數值高但失真，不採信 |
| FCF 利潤率 (TTM) | 22.6% | FY2025 13.5% | 約 8–12% | 優於板塊估計 |
| 淨負債/EBITDA | 0.17x | FY2025 約 2.1x (1.58/0.75) | 約 1.5–2.5x | 優 |
| 總負債/股東權益 | 0.19x | FY2024 0.36x | 約 0.5–0.8x | 優 |
| 流動比率 | 2.09x | n/a | 約 1.8–2.2x | 中性 |
| 利息保障倍數 (TTM EBIT/利息) | ≈ 2.0x | n/a | 約 5–8x | 弱 |
| 股息殖利率 | 1.74% | 5 年平均 1.00% | 約 1.5–2.5% | 中性 |
| 股息覆蓋 (TTM FCF/股利) | 3.7x | FY2025 1.9x | > 1.5x 為佳 | 健康 |
| 資本支出/營收 | 7.8% (TTM 0.46/5.91) | FY2025 11.5% vs FY2024 31.3% | 約 8–12% | 收縮中 |
| Trailing P/E | 349.9x | n/a | 約 20–25x | 失真，不採信 |
| Forward P/E | 8.75x | n/a | 約 15–20x | 估值偏低 |
| EV/EBITDA | 9.45x | n/a | 約 10–12x | 略低 |
| P/FCF (TTM) | 8.4x | n/a | 約 15–20x | 低 |
| P/S (trailing) | 1.89x | n/a | 約 2x | 中性 |
| P/B | 1.39x | n/a | 約 2–3x | 低 |
| 內部人淨買賣 (6 個月, USD M) | -3.01 (僅賣出) | n/a | n/a | 規模小，中性 |
| 空頭占流通股 | 11.37% | 月增 +22% | 約 3–5% | 偏高，風險 |
| EPS 季度 surprise (最近一季) | +15.7% | 近 4 季 3 勝 1 負 | n/a | 正向 |

## Red flags
- **獲利基礎不穩**：FY2024 淨損 -1.18B USD、FY2025 淨損 -0.51B USD (歸屬普通股 -0.68B USD)；TTM 歸屬普通股淨利僅 57.4M USD，獲利能力尚未確立。
- **營收年度下滑**：FY2023 峰值 9.62B USD 後，FY2024 -44.1%、FY2025 -4.4%，3 年 CAGR -11.1%。
- **盈餘依賴非營業項目**：權益法投資收益於 FY2024 為 715.4M USD、FY2025 為 243.7M USD；Q1'26 與 Q2'26 的大幅獲利轉正需檢視是否含一次性項目。
- **優先股與股息壓力**：優先股 2.24B USD，年股利約 166.8M USD，對普通股現金流構成固定支出。
- **利息保障偏低**：TTM 利息保障約 2.0x，若鋰價再度下行，償債彈性有限。
- **空頭部位擴大**：空頭占流通股 11.37%，月增 22%，且股價低於 50 日與 200 日均線。
- **治理風險分數偏高**：yfinance overallRisk 7、auditRisk 9、shareHolderRightsRisk 8 (量表 1–10，數值越高風險越高)。
- **估值依賴共識預估**：forward P/E 8.75x 建立在 forward EPS 10.80 USD 的分析師共識上，相對 TTM EPS 0.27 USD 落差極大，預估誤差風險高。
- **資料缺口**：分部營收、公司指引、鋰價與產能數據皆未由 yfinance 提供；institutionsPercentHeld 超過 100%；Yahoo crumb 多次連線失敗，部分欄位 (fast_info 的 50/200 日均線與 market cap) 改由快取或 info 補充。
- **資料時效**：價格為 2026-10-22 快取資料 (cached_at 2026-10-22T11:36–11:39 UTC)，早於分析基準日 2026-10-23 一天；無晚於 2026-10-23 的實際財務資料。

FUNDAMENTALS REPORT COMPLETE
