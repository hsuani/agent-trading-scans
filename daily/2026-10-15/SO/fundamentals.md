# Fundamentals — SO (Southern Company) as of 2026-10-15

## Executive summary
SO 的獲利能力穩定但現金流結構偏弱: TTM 營收 30,178M USD、TTM 淨利 4,657M USD（淨利率 15.4%），但 FY2025 FCF 為 -2,935M USD，TTM FCF 約 -3,269M USD，且 TTM 股利支出 3,100M USD 完全由舉債與股權募資支應。資產負債表槓桿偏高（Net debt / EBITDA 約 5.1x，mrq 利息保障約 2.3–2.6x），且公司 6 個月內股本增加約 2.7%，目前不具備靠自由現金流支撐股利與資本支出的條件。估值上 trailing P/E 21.2x、forward P/E 18.2x、EV/EBITDA 12.6x，相對公用事業同業估計中位數屬於略高或中性區間；分析師目標價中位數 99 USD 高於現價 89.38 USD，但 consensus 評級僅 "hold"（2.61/5）。整體判讀: 財務體質 **中性偏弱**（盈利穩、現金流與槓桿是主要風險），估值 **中性，無明顯折價**。本報告不提供交易建議。

資料說明: yfinance 即時來源被阻擋，所有數值來自本地快取（`"source": "cache"`），價格為 2026-10-14 收盤價（regularMarketTime 2026-10-14 20:00 UTC），2026-10-15 盤前報價 90.30 USD。財報最新期間為 2026-06-30（Q2 2026，於 2026-07-30 公布），無 DATA_UNAVAILABLE 以外的 post-date 財務數據。

## Revenue & profitability

**營收趨勢（年度，USD 百萬）**

| 年度 | Total Revenue | YoY | Gross margin | Operating margin (報表) | Net margin |
|---|---|---|---|---|---|
| FY2022 | 29,279 | n/a | 36.3% | 18.3% | 12.1% |
| FY2023 | 25,253 | -13.8% | 46.6% | 23.1% | 15.7% |
| FY2024 | 26,724 | +5.8% | 50.0% | 26.4% | 16.5% |
| FY2025 | 29,553 | +10.6% | 48.5% | 24.7% | 14.7% |

- 3 年營收 CAGR（FY2022→FY2025）: +0.3%，但 FY2022 受燃料與電力成本轉嫁影響基期偏高；2 年 CAGR（FY2023→FY2025）為 +8.2%，較具參考性。5 年 CAGR 因 yfinance 2021 欄位為 null，為 n/a。
- 最近一季（Q2 2026，截至 2026-06-30）: Total Revenue 6,977M，較 Q2 2025 的 6,973M 幾乎持平（+0.06%）；Operating Revenue 6,652M。yfinance `revenueGrowth` 為 0.001，與此一致。
- Q2 2026 淨利 1,174M，較 Q2 2025 的 880M 增加 33.4%；GAAP diluted EPS 1.03，較 0.79 增加 30.4%。
- TTM（Q3 2025–Q2 2026）: Total Revenue 30,178M（與 info `totalRevenue` 30,179M 吻合）; 淨利 4,657M; 淨利率 15.4%（與 info `profitMargins` 0.15435 吻合）。
- 季度 GAAP 獲利波動大: Q4 2025 淨利僅 416M（diluted EPS 0.38），Q3 2025 為 1,711M（EPS 1.54），Q1 2026 為 1,356M（EPS 1.20）。公用事業季節性與一次性項目（Total Unusual Items 2025 年度 340M）可能是主因，報表未提供細項說明。
- 獲利率口徑差異: yfinance `operatingMargins` 為 29.6%，但由 Operating Income 報表計算之 TTM 營業利益率為 24.2%（7,305 / 30,178）。兩者定義不同，本報告以報表計算值為準，並標註差異。
- ROE: yfinance `returnOnEquity` 11.5%；以 FY2025 淨利 4,341 與平均普通股權益（36,016 與 33,208）計算約 12.5%。ROA（info）3.3%。
- ROIC（自算，近似）: NOPAT = EBIT 8,237 × (1 − 16.6% tax rate) ≈ 6,870；平均 Invested Capital（108,607 與 98,032）約 103,320，ROIC 約 6.6%（期末值 6.3%）。此數值接近一般公用事業資本成本區間，代表超額報酬空間有限（同業中位數為估計，見 Metrics table）。
- 分部 (segment) 營收: yfinance 未提供分部資料，`longBusinessSummary` 僅描述業務範圍（零售與批發電力、天然氣配銷於 IL/GA/VA/TN、電池儲能、微電網、電信投資）。分部營收占比: DATA_UNAVAILABLE。

## Cashflow & balance sheet

**現金流（USD 百萬）**

| 年度 | Operating CF | Capex | FCF | FCF margin | FCF / NI | Cash dividends |
|---|---|---|---|---|---|---|
| FY2022 | 6,302 | 7,923 | -1,621 | -5.5% | -0.46 | 2,907 |
| FY2023 | 7,553 | 9,095 | -1,542 | -6.1% | -0.39 | 3,035 |
| FY2024 | 9,788 | 8,955 | 833 | 3.1% | 0.19 | 2,954 |
| FY2025 | 9,802 | 12,737 | -2,935 | -9.9% | -0.68 | 3,015 |
| TTM (至 Q2 2026) | 10,651 | 13,920 | -3,269 | -10.8% | -0.70 | 3,100 |

- FCF / NI 連續多年低於 0.9 健康門檻（FY2025 為 -0.68，僅 FY2024 轉正且只有 0.19）。OCF / NI 約 2.2–2.3x，表示營運現金流強，但被高資本支出吞噬。
- 資本支出 FY2025 為 12,737M，較 FY2024 的 8,955M 增加 42.2%，約為折舊攤提 6,030M 的 2.1 倍，屬於大規模電網與發電擴張期。
- 股利覆蓋: FY2025 OCF / 股利 = 3.25x（營運現金流尚可覆蓋），但 FCF / 股利 為負，股利實際上由舉債與股權募資支應。TTM 股利 3,100M 與 TTM FCF -3,269M 合計，外部融資需求約 6,400M/年化。
- 淨負債: 2025-12-31 Net debt 70,952M（較 FY2024 的 63,754M 增加 11.3%）; 2026-06-30 Net debt 72,598M，Total Debt 77,087M。
- 負債指標: Net debt / EBITDA 約 5.1x（info EBITDA 14,258M 為基準；FY2025 Normalized EBITDA 13,927M 計算結果同為 5.1x）。Debt / Equity（yfinance `debtToEquity` 182.06%，以 Total Equity 含少數股權計算，與 Q2 2026 數據吻合）。以普通股權益計算為 1.95x。
- 流動性: 2026-06-30 `currentRatio` 0.787，`quickRatio` 0.441。FY2025 Working Capital 為 -5,971M（流動比率 0.65 以 FY2025 報表計算）。現金 Q2 2026 期末 2,990M（現金流量表 End Cash Position），2025 年底為 1,640M。公用事業短期負債（商業本票等）滾動依賴，為典型結構，但流動性餘裕有限。
- 利息保障: FY2025 EBIT 8,237 / Interest Expense 3,238 = 2.54x；TTM EBIT 8,472 / Interest 3,224 = 2.63x。（TTM EBIT 以 EBIT 季度數加總計算，口徑與年度 EBIT 略異。）利息支出 FY2025 較 FY2022 的 2,022M 成長 60%。
- 總資產 FY2025 155,720M；Total Liabilities 116,853M；普通股權益 36,016M；Tangible Book Value 30,555M。Book value per share 34.40 USD，現價 P/B 2.60x。

## Capital allocation & insider signal

**資本配置**

- 資本支出: 見上表。FY2025 資本支出激增，且為舉債與股權募資所支應。
- 股權募資 (dilution): 普通股 Ordinary Shares 由 2025-12-31 的 1,120.2M 增至 2026-06-30 的 1,150.4M（+2.7%，半年）。現金流量表顯示 Issuance Of Capital Stock: FY2025 1,623M，Q1 2026 535M，Q2 2026 2,061M。Diluted average shares Q2 2026 1,141M，較 Q2 2025 的 1,108M 增加 3.0%。
- 股票回購: FY2022 為 -298M（實為 preferred stock 贖回，yfinance 欄位 Repurchase Of Capital Stock 為 -298M），FY2023–FY2025 為 0 或 null。目前無實質普通股回購。
- 股利: 2026-08-17 除息（yfinance `exDividendDate`），2026-09-08 發放（`dividendDate`），季股利 0.76 USD，trailing 12M dividend rate 2.98 USD。股利殖利率 3.45%（yfinance `dividendYield`，5 年平均 3.55%）。`payoutRatio` 71.8%（以 EPS 計）。下一個除息日: DATA_UNAVAILABLE（預估為 2026 年 11 月下旬，需確認）。
- 併購: FY2025 Net Business Purchase And Sale -634M（Purchase Of Business -635M），規模小。

**內部人交易（2026-04-15 至 2026-10-15，約 6 個月）**

- 共 9 筆公開市場賣出（Sale）: 總股數 9,599 股，總金額約 870,608 USD。賣方為 KIM MATTHEW M.（Chief Accounting Officer，7 筆合計 2,000 股，多數為每筆 100 股）、SENA PETER P III（1 筆 4,266 股，約 377,925 USD）、SPAINHOUR STERLING A. JR.（1 筆 3,333 股，約 313,369 USD）。
- 無任何公開市場買進（Purchase）紀錄。
- 另有無金額欄位之交易 8,374 股（CEO WOMACK 7,662 股於 2026-05-22、SENA 712 股於 2026-06-26），性質（授予/股份歸屬或稅款代扣）無法從 yfinance 判定，視為 unclassified。
- 規模: 賣出總金額 870,608 USD 佔市值 102,819M USD 約 0.0008%，幅度極小，屬例行性質。是否屬於 10b5-1 計畫: DATA_UNAVAILABLE。
- 機構持股: 74.2%（`heldPercentInstitutions`），2026-06-30 最大持有人 BlackRock 8.08%，Vanguard 6.40%，State Street 5.63%。Capital World Investors 季增 11.2%，T. Rowe Price 季增 27.4%，JPMorgan 季減 24.4%。內部人持股僅 0.095%。
- 空單: short ratio 4.63 天，short % float 2.55%（2026-09-30 日期資料），屬低空單水準。

## Valuation

- 價格: 89.38 USD（2026-10-14 收盤，regularMarketChange +1.27，+1.44%）。52 週區間 81.69–100.84 USD，現價距高點 -11.4%、距低點 +9.4%。50 日均 87.93 USD（現價 +1.7%），200 日均 92.16 USD（現價 -3.0%）。Beta 0.301。
- 市值 102,819M USD；企業價值 EV 179,694M USD；流通股 1,147.6M（float）。
- P/E（trailing）: 21.2x（yfinance `trailingPE`，以 EPS TTM 4.21 計）。以 GAAP diluted EPS TTM 4.15 計算為 21.5x。
- P/E（forward）: 18.2x（`forwardPE`，`epsForward` 4.92）；`epsCurrentYear` 4.59 → 19.5x。
- EV/EBITDA: 12.6x（`enterpriseToEbitda`；EBITDA 14,258M）。EV / Revenue 5.95x。
- P/S: 3.41x（TTM）。P/B: 2.60x。
- P/FCF: 不適用（TTM FCF 為負，n/m）。P/OCF（TTM）: 9.7x（市值 / TTM OCF 10,651M）。
- 分析師目標價: 平均 97.08、中位 99.00、高 112.00、低 74.00 USD（19 位分析師）。相對現價，平均目標價隱含 +8.6% 上行空間。consensus `recommendationKey` = hold，mean 2.61（1 為 strong buy，5 為 sell）。
- 與公用事業產業中位數比較: 以下為估計值（非 yfinance 數據，見 Metrics table），SO 的 trailing P/E、EV/EBITDA 與 P/B 大致在同業區間內，但殖利率略低於產業典型水準，而槓桿與負 FCF 使其在 quality 面不占優。

## Key catalysts

- **下一次財報**: 2026-11-05（yfinance `earningsTimestamp` 2026-11-05 12:30 UTC；`isEarningsDateEstimate` = false），Q3 2026 EPS 共識估計 1.67（`earnings_dates`）。
- **近四季 EPS surprise**: 2026-07-30 Q2 +11.82%（adjusted EPS 1.13 vs 估計 1.01）; 2026-04-30 Q1 +8.87%（1.32 vs 1.21）; 2026-02-19 Q4 2025 -1.37%（0.55 vs 0.56）; 2025-10-30 Q3 2025 +6.04%（1.60 vs 1.51）。過去 5 年多數季度為正向 surprise（2023 年初至 2026 年共 15 季中 13 季高於估計，2 季低於估計: 2025-02 與 2026-02）。
- **注意**: `earnings_dates` 的 Reported EPS 為 adjusted（非 GAAP）口徑，與 quarterly_fin 的 GAAP diluted EPS（Q2 2026 為 1.03）不同，比較時需統一口徑。
- **公司指引（guidance）**: yfinance 未提供管理層指引，DATA_UNAVAILABLE。
- **資本市場事件**: 2026 年持續的股權募資（Q2 2026 發行 2,061M）與舉債（FY2025 發行 12,670M）顯示資本需求持續；後續 equity issuance 規模與時點需追蹤 10-Q/8-K，但本來源無法提供。
- **監管與費率**: 公用事業獲利主要取決於州級與聯邦費率案（如 Georgia Power、Alabama Power 的費率調整），本來源無資料，DATA_UNAVAILABLE。
- **股利**: 下次除息日（預估 2026 年 11 月）需確認；股利是否維持為市場關注焦點。

## Metrics table

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| Price (close 2026-10-14) | 89.38 USD | 52W 區間 81.69–100.84 | n/a | 中性 |
| Market Cap | 102,819M USD | n/a | n/a | 大型股 |
| Revenue (TTM) | 30,178M USD | +0.1% (Q2 2026 vs Q2 2025) | 估計 YoY 3–6% | 中性（持平） |
| Revenue CAGR (FY23–FY25) | +8.2% | n/a | 估計 4–6% | 優於估計 |
| Gross margin (FY2025) | 48.5% | -1.5pp vs FY2024 | 估計 n/a（報表定義差異大） | 中性 |
| Operating margin (TTM, 報表) | 24.2% | info 口徑 29.6% | 估計 20–25% | 中性 |
| Net margin (TTM) | 15.4% | FY2025 14.7% (FY2024 16.5%) | 估計 10–14% | 略優 |
| ROE | 11.5% (info) / 12.5% (自算) | n/a | 估計 9–11% | 略優 |
| ROIC（自算近似） | 6.6% | n/a | 估計 6–7% | 中性（接近資本成本） |
| OCF (TTM) | 10,651M USD | FY2025 9,802 vs FY2024 9,788 (+0.1%) | n/a | 中性 |
| FCF (FY2025) | -2,935M USD | 較 FY2024 +833M 轉負 | 估計 接近零或小幅負 | 偏弱 |
| FCF (TTM) | -3,269M USD | n/a | n/a | 偏弱 |
| FCF / NI (FY2025) | -0.68 | FY2024 0.19 | 健康門檻 > 0.9 | 不達標 |
| Capex (FY2025) | 12,737M USD | +42.2% | 估計 成長期 | 風險 |
| Net debt / EBITDA | 5.1x | FY2024 4.9x (63,754 / 13,003) | 估計 5–6x | 中性偏高 |
| Debt / Equity（含少數股權） | 182% (info) | n/a | 估計 150–180% | 中性偏高 |
| Current ratio (mrq) | 0.79 (info) | FY2025 0.65 | 估計 0.7–1.0 | 中性 |
| Interest coverage (EBIT / interest, TTM) | 2.6x | FY2025 2.5x | 估計 2.5–3.5x | 偏弱 |
| Dividend yield | 3.45% | 5Y avg 3.55% | 估計 3.5–4.5% | 略低於產業 |
| Dividend coverage (OCF / 股利, FY2025) | 3.25x | FY2024 3.31x | 估計 > 2x | 尚可 |
| Dividend coverage (FCF / 股利, FY2025) | 負（-0.97x） | n/a | 估計 > 1x | 不達標 |
| Payout ratio (EPS) | 71.8% | n/a | 估計 60–75% | 中性 |
| Shares outstanding 變化（2025-12 → 2026-06） | +2.7% | Q2 diluted +3.0% YoY | 估計 0–1% | 稀釋風險 |
| Insider net 6M | 9 筆賣出，870,608 USD，0 買進 | n/a | n/a | 中性（例行性賣出） |
| Trailing P/E | 21.2x | n/a | 估計 17–19x | 略高 |
| Forward P/E | 18.2x | n/a | 估計 16–18x | 中性 |
| EV/EBITDA (TTM) | 12.6x | n/a | 估計 11–13x | 中性 |
| P/FCF | n/m（FCF 為負） | n/a | 估計 n/m | 無法評估 |
| P/OCF (TTM) | 9.7x | n/a | 估計 8–10x | 中性 |
| P/S (TTM) | 3.41x | n/a | 估計 2.5–3.5x | 中性偏高 |
| P/B | 2.60x | n/a | 估計 1.8–2.2x | 偏高 |
| Analyst consensus mean target | 97.08 USD（+8.6%） | n/a | n/a | 中性 |
| Analyst recommendation | hold（2.61） | n/a | n/a | 中性 |
| Beta | 0.30 | n/a | 估計 0.4–0.7 | 低波動 |
| Institutional ownership | 74.2% | n/a | n/a | 正常 |

注: 「Sector median (estimate)」為分析師依公用事業（Utilities - Regulated Electric）一般區間之主觀估計，非來自 yfinance，僅供參考，不可作為精確比較基準。

## Red flags

- 自由現金流連續為負: FY2022、FY2023、FY2025 為負，TTM FCF -3,269M USD；股利 3,100M USD（TTM）完全依賴外部融資。
- 股權稀釋: 6 個月股本增加 2.7%（約 +30.1M 股），Q2 2026 單季股權募資 2,061M USD，且無普通股回購。
- 槓桿與債務成本上升: Total Debt 由 FY2022 59,135M 升至 77,087M（2026-06），利息支出 FY2022 2,022M 到 FY2025 3,238M（+60%）；利息保障 TTM 約 2.6x。
- 資本支出高峰: FY2025 Capex +42.2%，預期仍維持高檔，若費率案不及時反映，獲利與現金流壓力將延續。
- 季度 GAAP 獲利波動: Q4 2025 淨利 416M（EPS 0.38）較 Q3 2025 的 1,711M 劇烈下滑，需確認是否為一次性項目（Total Unusual Items 2025 年度 340M）。
- 估值接近中性偏高: P/B 2.60x、P/S 3.41x、trailing P/E 21.2x，在 FCF 為負的前提下估值支撐不強。
- 股價在 200 日均線下方（-3.0%），52 週高點 100.84 USD 回落 11.4%。
- 內部人持續例行賣出（6 個月 9 筆、約 870K USD），雖金額小，但無任何買進紀錄。
- 資料缺口: 分部營收、管理層指引、下次除息日、費率案進度、10b5-1 計畫資訊皆為 DATA_UNAVAILABLE；EBITDA 與 operating margin 在不同來源間存在口徑差異，已於正文註記。

FUNDAMENTALS REPORT COMPLETE
