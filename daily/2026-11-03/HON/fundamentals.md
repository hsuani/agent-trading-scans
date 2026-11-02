# Fundamentals — HON as of 2026-11-03

## Executive summary
Honeywell (HON) 的財務體質在 2026 年經歷大幅資產剝離後明顯去槓桿: 總負債自 YE25 的 58.65B USD 降至 2026-09-30 的 30.44B USD, 淨負債自 22.09B USD 降至 10.90B USD, 但 GAAP 盈餘被一次性的資產出售利益與減損嚴重扭曲, 2026 年前三季 FCF 僅約 0.37B USD, 遠低於 2025 年全年的 5.42B USD. 估值面以 FY25 GAAP EPS 計 P/E 約 15.2x、EV/EBITDA 約 8.9x (info 口徑)、forward P/E 22.7x, 相對工業類股屬於中性偏合理; 但多個 yfinance 欄位互相矛盾 (見 Red flags), 下列數字需以原始 10-Q/10-K 核對後才能作為決策依據。

資料基準: 價格與市值取自 info (cached 2026-11-02 15:33 UTC, 收盤價 224.05 USD); fast_info 另回報 222.95 USD (cnyes feed), 兩者差距約 0.5%, 以 info 為準。財報為 FY2025 (年報) 與 2026 Q1–Q3 (季報); 2026-09-30 為最新資料季, 無資料晚於 DATE 的情形。

## Revenue & profitability
**營收趨勢 (B USD, 年報, 來源 financials)**

| 年度 | 營收 | YoY | 毛利 | 毛利率 | 營業利益 | 營業利益率 | 淨利 (含非持續營運) | 淨利率 | 稀釋 EPS |
|---|---|---|---|---|---|---|---|---|---|
| FY2022 | 35.47 | n/a | 13.12 | 37.0% | 6.43 | 18.1% | 4.97 | 14.0% | 14.54 |
| FY2023 | 33.01 | -6.9% | 12.37 | 37.5% | 6.11 | 18.5% | 5.66 | 17.1% | 16.94 |
| FY2024 | 34.72 | +5.2% | 13.36 | 38.5% | 6.67 | 19.2% | 5.71 | 16.4% | 17.42 |
| FY2025 | 37.44 | +7.8% | 13.83 | 36.9% | 6.57 | 17.5% | 4.73 | 12.6% | 14.72 |

- 3 年 CAGR (FY2022→FY2025): 約 +1.8%。FY2021 資料為 null, 無法計算 4–5 年 CAGR。
- FY2025 營收年增 +7.8%, 但 FY2025 同時有 Impairment of Capital Assets 0.994B USD 與 Special Income Charges -1.483B USD, 營業利益僅小幅下滑 (-1.5%), 毛利率下降 1.5 個百分點 (38.5%→36.9%), 顯示成長並未轉化為獲利改善。
- FY2025 GAAP 淨利 4.73B USD, YoY -17.1%, EPS 14.72 USD, YoY -15.5%。驗算: 14.72 × 321.4M 稀釋股數 ≈ 4.73B USD, 與 Diluted NI 吻合。
- info 的 revenueGrowth 為 +1.3% (TTM 口徑), 與年報 +7.8% 有明顯差異, 顯示 TTM 與年報涵蓋範圍不同 (疑似資產剝離後的 continuing ops 差異)。

**季度趨勢 (B USD, 來源 quarterly_fin)**

| 季度 | 營收 | 營業利益 | 淨利 | 稀釋 EPS (GAAP) | 備註 |
|---|---|---|---|---|---|
| 2025-09 | 4.93 | 0.41 | 1.83 | 5.71 | 含 discontinued ops |
| 2025-12 | 6.86 | 0.71 | -0.12 | 0.92 | 減損 0.979B 等 |
| 2026-03 | 9.14 | 1.74 | 0.82 | 2.58 | |
| 2026-06 | 9.72 | 1.79 | 5.68 | 17.83 | gain on sale of business 約 5.92B USD |
| 2026-09 | 4.99 | 0.74 | 0.66 | 2.08 | 營業利益率約 14.8% |

- Q2 2026 淨利 5.68B USD 幾乎全數來自 gain on sale of business (5.92B USD), 屬一次性, 不代表營運獲利。
- 2026-06 至 2026-09 營收由 9.72B 驟降至 4.99B USD, 且 2025-09 營收僅 4.93B USD, 顯示各季資料基準 (continuing vs. 含剝離業務) 不一致, 不能直接相加為 TTM。
- 季報 adjusted EPS (earnings_dates): 2026-10-22 公布 Q3 2026 EPS 2.27 USD, 對比預估 2.16 USD, beat +4.9%。

**Segment mix**: info.longBusinessSummary 列出三大部門: Industrial Automation、Building Automation、Energy and Sustainability Solutions (含 UOP)。yfinance 無分部營收數字, 無法量化各部門占比; 季度資料顯示 goodwill 自 YE25 21.08B 降至 2026-09 的 17.56B USD, 且 2026-06 有 2.37B USD 的 assets held for sale, 顯示有資產剝離, 但 yfinance 未提供剝離標的名稱, 需以公告確認。

**獲利能力比率**
- 毛利率 FY2025 36.9%, 營業利益率 17.5%, 淨利率 12.6% (GAAP)。
- ROE: info 44.4%, 但此為低權益基數 (YE25 股東權益僅 13.90B USD) 造成的膨脹值, 不宜當作品質指標。
- ROA: info 7.1%。
- ROIC (估算): NOPAT = EBIT 6.82B × (1 − 稅率 18.4%) ≈ 5.56B USD; 平均投入資本 (YE24 49.66B、YE25 48.48B) ≈ 49.07B USD, ROIC ≈ 11.3%。此為本報告自行估算。

## Cashflow & balance sheet
**現金流 (B USD, 來源 cashflow)**

| 年度 | 營運現金流 OCF | 資本支出 Capex | FCF | FCF 利潤率 | FCF / NI |
|---|---|---|---|---|---|
| FY2022 | 5.27 | 0.77 | 4.51 | 12.7% | 0.91 |
| FY2023 | 5.34 | 0.74 | 4.60 | 13.9% | 0.81 |
| FY2024 | 6.10 | 0.87 | 5.23 | 15.1% | 0.92 |
| FY2025 | 6.41 | 0.99 | 5.42 | 14.5% | 1.15 |

- FY2025 FCF/NI 1.15x, 高於 0.9 健康門檻, 但分子包含 D&A (depreciation 1.39B + amortization 0.84B) 的非現金回沖, 且 NI 已扣除 1.4B USD 級別的一次性項目, 品質尚可但需看 2026 年走勢。
- 2026 年 YTD 轉弱: 2026-Q1 FCF -0.87B、Q2 +0.96B、Q3 +0.29B, 9M 合計約 0.37B USD (YoY 無法精確比較, 2025 Q1、Q2 季度資料為 null)。
- 2026-Q3 營運現金流 (Operating Cash Flow 欄) 僅 0.12B USD, 但 Cash Flow From Continuing Operating Activities 欄為 0.31B USD, 兩者口徑不同, 未能釐清。

**資產負債表 (B USD, 來源 balance_sheet / quarterly_bs)**

| 項目 | FY2024 (YE) | FY2025 (YE) | 2026-09-30 | 備註 |
|---|---|---|---|---|
| 總資產 | 75.20 | 73.68 | 53.10 | 剝離後下降 |
| 股東權益 | 18.62 | 13.90 | 22.42 | Q3 大幅回升, 來自 Q2 gain |
| 總負債 | 56.04 | 58.65 | 30.44 | |
| 總債務 Total Debt | 32.08 | 35.56 | 16.59 | 2026 年償還約 19B |
| 現金及約當現金 | 9.91 | 12.49 | 5.69 | |
| 淨負債 Net Debt | 21.13 | 22.09 | 10.90 | 2026-06 為 25.24 |
| 商譽 Goodwill | 21.02 | 21.08 | 17.56 | |
| 有形帳面淨值 TBV | -9.02 | -13.91 | n/a | 負值 |

- 淨負債/EBITDA (FY2025, 年報 EBITDA 8.21B): 約 2.7x; 以 normalized EBITDA 9.64B 計約 2.3x。
- 流動比率 (current ratio): FY2025 1.30x, 2026-09-30 降至 0.96x (info 亦回報 0.96); quick ratio 0.76。營運資金 2026-09 為 -0.60B USD。
- 負債/權益 (info debtToEquity 76.1%, 約對應 2026-09 季報 74%); FY2025 口徑為 2.56x。
- 利息保障倍數 (FY2025 EBIT 6.82B / 利息費用 1.34B): 約 5.1x, 尚屬健康。
- 現金部位: 2026-09 現金及約當現金 5.69B USD, 相較 YE25 下降 6.8B USD。

## Capital allocation & insider signal
**資本支出與股東回報 (B USD)**
- 資本支出: FY2025 0.99B USD, YoY +13.2%; 資本支出/折舊攤銷約 0.44x (0.99 / 2.23), 屬偏低的維護型投資節奏。2026 年 Q1–Q2 有 0.22B、0.32B USD 的 capex, 其餘季度資料不完整。
- 買回 (Repurchase of Capital Stock): FY2025 3.80B USD (FY2024 1.66B, YoY +130%); 2026 年 Q1 買回 1.00B USD, Q2、Q3 為 0, 買回節奏在 2026 下半年明顯停頓。
- 流通股數: 年底 ordinary shares 由 2022 年的 333.8M 降至 2025 年的 317.65M (-4.8%); info sharesOutstanding 316.94M。稀釋股數 2022 341.55M → 2025 321.4M (-5.9%)。
- 股利: 每季 0.70 USD, 年化 2.80 USD; 殖利率 1.28% (5 年平均 2.12%); info payoutRatio 38.9%。FY2025 股利支付 2.98B USD, 以 FCF 計覆蓋 1.82x, 以 GAAP NI 計 1.59x, 覆蓋充足。
- 下一次除息日 (ex-date): 2026-11-13, 金額 0.70 USD (info corporateActions)。
- 2026-Q3 股利支付僅 0.24B USD, 低於 Q1、Q2 的約 0.78–0.80B USD, 季度資料不一致, 需核對。

**內部人交易 (last 6 months, 約 2026-05-03 至 2026-11-02, 來源 insider)**
- 公開市場賣出 (Sale) 共 4 筆, 合計約 26,750 股, 約 6.31M USD:
  - Vimal M. Kapur (CEO): 2026-10-26 賣出 6,459 股, 約 1.43M USD (@220.99)。
  - Su Ping Lu (General Counsel): 2026-10-26 賣出 2,943 股, 約 0.65M USD (@221.18)。
  - Kenneth J. West (Officer): 2026-07-27 賣出 17,032 股, 約 4.15M USD (@243.77), 同日行使衍生性證券 17,032 股。
  - Kenneth J. West (Officer): 2026-08-03 賣出 316 股, 約 0.08M USD (@245.47)。
- 期間內無公開市場買進 (Buy) 紀錄。
- 另有多筆 Value 為 None 的交易 (多為董事年度股票配予 2026-04-15、員工歸屬或稅務扣繳等, 性質無法由 yfinance 確認)。
- 規模: 賣出總額約 6.31M USD, 相對市值 71.01B USD 約 0.009%, 屬極小幅度; 內部人持股比率 heldPercentInsiders 僅 0.08%, 訊號強度低。
- 6 個月外的 2026 年初亦有 Mailloux (約 3.7M USD) 與 Lieblein (約 1.4M USD) 等賣出, 合計仍屬小額; 整體無內部人集中買進的看多訊號。

## Valuation
**估值指標 (來源 info, 價格 224.05 USD, 市值 71.01B USD, EV 80.58B USD)**

| 指標 | 數值 | 說明 |
|---|---|---|
| 追蹤 P/E (trailing, info EPS 20.17) | 11.1x | EPS 含 2026-Q2 gain, 不具代表性 |
| 追蹤 P/E (FY2025 GAAP EPS 14.72) | 15.2x | 本報告自算 |
| Forward P/E (forwardEps 9.85) | 22.7x | |
| P/E 本年度 (epsCurrentYear 8.44) | 26.5x | |
| EV/EBITDA (info, EBITDA 9.02B) | 8.9x | 以 FY2025 EBITDA 8.21B 計約 9.8x (本報告自算) |
| P/FCF (TTM, info FCF 7.02B) | 10.1x | info FCF 與 OCF 矛盾, 參考性低 |
| P/FCF (FY2025 FCF 5.42B) | 13.1x | 本報告自算 |
| P/S (trailing) | 1.88x | |
| P/B | 3.17x | 帳面值 70.64 USD/股 |
| PEG | 3.04 | |

- 分析師共識: 23 位, recommendationMean 2.0 (Buy); 目標價均值 253.91 USD, 中位數 254.0 USD, 區間 186–290 USD; 相對現價約 +13.3%。
- 價格位置: 52 週區間 195.87–260.28 USD, 現價位於區間 約 70% 位置; 50 日均線 211.63 USD, 200 日均線 230.74 USD (現價高於 50 日、低於 200 日)。
- Beta 0.878; 空單佔流通股 2.35%, shortRatio 2.68 天。

**相對同業 (sector median, 估計)**: Industrials/Conglomerates 類股經驗值 (非工具輸出, 僅供參考): forward P/E 約 20–22x、EV/EBITDA 約 13–16x、P/S 約 2.0x、P/FCF 約 20–25x。HON 在 P/E 與 P/S 上接近中性, EV/EBITDA 偏低, 但 forward P/E 偏高, 反映 2026 年 EPS 基準混亂。

## Key catalysts
- 下次財報: 2027-01-28 (yfinance 標示為估計值, isEarningsDateEstimate = true), EPS 預估 2.45 USD。前次 2026-10-22 公布 Q3 2026 adjusted EPS 2.27 USD, 已連續 24 季 (2021-01 至 2026-10 所有紀錄) EPS 優於預估, 平均 beat 約 3–5%。
- 股利除息: 2026-11-13 ex-date, 每股 0.70 USD。
- 資產剝離進度: 2026-06 gain on sale 5.92B USD、goodwill 與 held-for-sale 資產大幅下降, 後續是否還有剝離、以及 2026 年 Q4 的買回是否恢復, 是關鍵變數; yfinance 不提供公告文字, 需查證公司新聞稿。
- 管理層異動: info 顯示 CEO Vimal Kapur 與 CFO Michal Stepniak 任職中; 2026 年 CEO 有大量期權行使與賣出, 屬常態性行為但需留意。
- 分析師目標價調整: 中位數 254 USD 高於現價約 13%, 後續目標價修正將影響估值敘事。

## Metrics table
單位: 營收、利潤、現金流、市值等 USD 金額以 B USD 表示; 比率為 %、x。Latest 為 FY2025 年報或 2026-09-30 季報 (註明者)。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 (B USD) | 37.44 (FY25) | +7.8% | n/a (估計 YoY +3–5%) | 成長穩定, 但受剝離影響 |
| 毛利率 | 36.9% | -1.5 pp | 約 30–35% | 中等偏上, 下滑 |
| 營業利益率 | 17.5% | -1.7 pp | 約 15% | 中等偏上, 下滑 |
| GAAP 淨利率 | 12.6% | -3.8 pp | 約 10–12% | 含一次性項目, 不具代表性 |
| 稀釋 EPS (USD) | 14.72 (FY25) | -15.5% | n/a | GAAP 下滑 |
| ROE (info) | 44.4% | n/a | 約 15% | 低權益基數膨脹, 不採信 |
| ROIC (本報告估算) | 約 11.3% | n/a | 約 10–12% | 中性 |
| FCF (B USD) | 5.42 (FY25) | +3.7% | n/a | 尚健康 |
| FCF 利潤率 | 14.5% | -0.6 pp | 約 12–15% | 中性 |
| FCF / NI | 1.15x | +0.2x | 約 1.0x | 健康 |
| 2026 YTD FCF (9M, B USD) | 0.37 | n/a | n/a | 轉弱, 需追蹤 |
| 淨負債 (B USD) | 10.90 (2026-09) | -50.7% vs YE25 | 約 2–3x EBITDA | 去槓桿明顯 |
| 淨負債/EBITDA | 約 2.7x (FY25) | 約 +0.2x | 約 2.5x | 中性 |
| 流動比率 | 0.96x (2026-09) | 1.30x → 0.96x | 約 1.4x | 偏弱, 留意 |
| 負債/權益 (info) | 76.1% | n/a | 約 60–80% | 中性 |
| 利息保障倍數 | 約 5.1x | n/a | 約 8–10x | 偏弱但可接受 |
| 股利殖利率 | 1.28% | n/a | 約 1.5% | 偏低 |
| 股利覆蓋 (FCF) | 1.82x | n/a | 約 1.5x | 健康 |
| 買回金額 (B USD) | 3.80 (FY25) | +130% | n/a | 2026 下半年停頓 |
| 資本支出 / 折舊攤銷 | 約 0.44x | n/a | 約 0.9–1.1x | 偏低, 需留意再投資不足 |
| 內部人淨買賣 (6 個月) | 淨賣出約 6.31M USD | n/a | 0 | 無集中買進, 訊號中性偏空 |
| P/E trailing (GAAP FY25) | 15.2x | n/a | 約 20x | 相對便宜 |
| Forward P/E | 22.7x | n/a | 約 20–22x | 中性偏貴 |
| EV/EBITDA (info) | 8.9x | n/a | 約 13–16x | 相對便宜 |
| P/FCF (FY25) | 13.1x | n/a | 約 20–25x | 相對便宜 |
| P/S | 1.88x | n/a | 約 2.0x | 中性 |
| P/B | 3.17x | n/a | 約 3–4x | 中性 |
| 分析師目標價均值 | 253.91 USD (+13.3%) | n/a | n/a | 偏多 |

## Red flags
- 資料一致性: info 的 TTM EPS (20.17) 與 FY25 GAAP EPS (14.72) 差異大, 主因為 2026-Q2 gain; 因此 info 的 trailing P/E 11.1x 不應直接使用。
- 季度營收基準不一致: 2026-06 (9.72B) 與 2026-09 (4.99B) 差距過大, 2025-06 與 2025-03 季度資料為 null, 無法可靠計算 TTM 或季度 YoY。
- info 的 freeCashflow (TTM 7.02B USD) 大於 operatingCashflow (TTM 1.95B USD), 在 capex 為正的前提下不合理, 此欄位不應採用。
- 2026 年現金流大幅轉弱: 9M FCF 約 0.37B USD, Q1 為負; 2025 全年 FCF 5.42B USD。
- 流動比率跌破 1.0 (0.96x), 營運資金為負 (-0.60B USD)。
- 有形帳面淨值為負 (-13.91B USD, YE25), 商譽佔總資產比重高 (2026-09 商譽 17.56B / 總資產 53.10B 約 33%)。
- GAAP 淨利品質低: FY2025 有 1.4B USD 級別的一次性項目, 2026-Q2 有 5.9B USD 的剝離利益; 2025-12 季度淨利為負 (-0.12B USD)。
- 有機成長不明: 營收成長 (年報 +7.8%) 與 info revenueGrowth (+1.3%) 差距大, 無法確認剝離後的 organic growth。
- 買回在 2026 年 Q2、Q3 停止, 且 2026-Q3 股利支付金額 (0.24B USD) 與前幾季不一致, 需確認是否為時點差異或政策變動。
- 內部人雖無大額賣出, 但 CEO 於 2026-10-26 同日行使期權並賣出, 屬常態但值得留意。
- 資產剝離與 gain 的具體標的、金額與未來剩餘剝離計畫, yfinance 無法提供, 需以公告與 10-Q 補充。

FUNDAMENTALS REPORT COMPLETE
