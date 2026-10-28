# Fundamentals — VST (Vistra Corp.) as of 2026-10-28

資料來源與時效: yfinance 即時 feed 失敗 (CONNECT 403)，`fast_info` 與多數欄位來自 repo cache（fast_info 快取時間 2026-10-28 12:37 UTC）。`ta snapshot` 的 as_of 為 2026-10-27。所有數字取自工具 JSON，衍生值以括號註明「自算」。無資料日期晚於 2026-10-28；唯一未來事件為 2026-11-06 的 Q3 財報（屬預定事件，非資料錯誤）。
單位: 美元 (USD)，金額以 B（十億美元）、M（百萬美元）表示；未混用億。

## Executive summary
VST 財務體質為「獲利與現金流同步走弱、槓桿偏高」: FY2025 營收 17.74B（YoY +3.0%），歸屬普通股淨利 0.75B（YoY -69.5%），FY2025 FCF 1.32B（YoY -47%）；Q2'26 淨負債 19.46B、TTM net debt/EBITDA 約 2.9x、流動比率 0.97x。估值上 trailing P/E 24.7x 偏高（EPS 波動大），forward P/E 14.0x 與 EV/EBITDA 10.8x 處於可接受區間，分析師平均目標價 208.23（較現價 +42%）；近 6 個月內部人淨賣出 USD 24.7M（約市值 0.05%）。整體結論: 財務健康度中性偏弱，估值是否有吸引力取決於 2026-11-06 Q3 財報能否證明獲利回穩。

## Revenue & profitability

### 營收與獲利歷史（FY，單位 USD B）
| 年度 | Total Revenue | Gross Profit | 毛利率(自算) | Operating Income (reported) | 營業利益率(自算) | NI 歸屬普通股 | 淨利率(自算) | Diluted EPS |
|---|---|---|---|---|---|---|---|---|
| 2022 | 13.728 | 1.682 | 12.3% | -1.177 | -8.6% | -1.377 | -10.0% | -3.15 |
| 2023 | 14.779 | 5.520 | 37.4% | 2.661 | 18.0% | 1.343 | 9.1% | 3.58 |
| 2024 | 17.224 | 7.525 | 43.7% | 4.081 | 23.7% | 2.467 | 14.3% | 7.00 |
| 2025 | 17.738 | 5.834 | 32.9% | 1.906 | 10.7% | 0.752 | 4.2% | 2.22 |

- 營收 CAGR（自算）: 2022–2025 三年 8.9%；2023–2025 兩年 9.6%。FY2025 YoY +3.0%（17.738 vs 17.224）。
- 2022 另有 Operating Revenue 15.631B 口徑，與 Total Revenue 不同，本報告統一採 Total Revenue。
- 獲利趨勢: 2024 為高基期（EPS 7.00），2025 毛利率由 43.7% 降至 32.9%，營業利益率由 23.7% 降至 10.7%。Gross profit 下滑幅度大於營收，成本端壓力明顯（Cost of Revenue 由 9.70B 增至 11.90B）。
- TTM（Q3'25–Q2'26，由季度加總，自算）: 營收 19.21B；毛利 7.30B（毛利率 38.0%）；營業利益(reported) 3.56B（營業利益率 18.5%）；淨利 2.22B；NI 歸屬普通股 2.03B（與 info netIncomeToCommon 2.027B 一致）。
- 季度近況: Q2'26 營收 4.017B vs Q2'25 4.250B，YoY -5.5%（與 info revenueGrowth -0.055 吻合）；Q2'26 營業利益 0.553B vs Q2'25 0.515B（+7.4%）；Q2'26 NI 歸屬普通股 0.258B vs 0.280B（-7.9%）。Q1'25 營收與 Q4'25 diluted EPS 為 null，無法計算該期 YoY。
- 報酬率: info ROE 42.96%、ROA 5.89%。ROE 數字因普通股權益僅 3.0B（2026-06-30，Common Stock Equity）而被放大，不宜作為獲利品質指標。FY2025 以 NI 歸屬普通股 / 年末股東權益（5.097B，含特別股）自算約 14.8%。
- ROIC（自算，FY2025）: NOPAT = EBIT 2.105B × (1 − 稅率 15.9%) = 1.77B；平均 Invested Capital (20.142+22.689)/2 = 21.42B；ROIC ≈ 8.3%。FY2024 同法約 18.8%。ROIC 大幅下降。
- 分部: 業務描述列出五個分部（Retail、Texas、East、West、Asset Closure），但 yfinance 未提供分部營收與獲利，分部占比為 DATA_UNAVAILABLE。

## Cashflow & balance sheet

### 現金流（USD B）
| 項目 | 2022 | 2023 | 2024 | 2025 | TTM（自算） |
|---|---|---|---|---|---|
| Operating Cash Flow | 0.485 | 5.453 | 4.563 | 4.070 | 5.121 |
| Capex | 1.301 | 1.676 | 2.078 | 2.752 | 2.866 |
| FCF（OCF − Capex） | -0.816 | 3.777 | 2.485 | 1.318 | 2.255 |
| FCF 利潤率（/營收） | n/m | 25.6% | 14.4% | 7.4% | 11.7% |
| FCF / NI 歸屬普通股 | n/m | 2.81x | 1.01x | 1.75x | 1.11x |

- FCF/NI 2025 為 1.75x，高於 0.9 健康門檻，但分子主要來自 D&A 2.95B 造成的非現金支出與低淨利基數，並非獲利改善。
- info 的 freeCashflow 欄位為 37.1M，與季度加總 OCF − Capex 的 TTM 2.255B 明顯不一致。本報告採季度加總值，info 值視為異常。
- Capex 連續三年增加（2022 1.30B → 2025 2.75B，2025 YoY +32%）。Capex/D&A 2025 為 0.93x（自算）。

### 資產負債表
| 項目 | FY2023 | FY2024 | FY2025 | Q2'26 (2026-06-30) |
|---|---|---|---|---|
| Cash & Equivalents | 3.485 | 1.188 | 0.785 | 0.435 |
| Total Debt | 14.677 | 17.048 | 20.068 | 19.895 |
| Net Debt | 10.917 | 15.860 | 19.283 | 19.460 |
| Stockholders Equity（含特別股） | 5.307 | 5.570 | 5.097 | 5.482 |
| Common Stock Equity（不含特別股） | 2.831 | 3.094 | 2.621 | 3.006 |
| Tangible Book Value | -1.616 | -1.926 | -2.624 | -2.090 |
| Current Ratio（自算） | 1.18x | 0.96x | 0.78x | 0.97x |

- Net debt/EBITDA: FY2025 為 3.7x（19.283 / Normalized EBITDA 5.230，自算）；TTM 為約 2.9x（19.460 / info ebitda 6.646，自算）。FY2024 為 2.3x。
- 利息覆蓋（自算）: FY2025 EBIT 2.105B / 利息費用 0.982B = 2.1x；TTM EBIT 3.769B / 利息 0.966B ≈ 3.9x。
- info debtToEquity 為 373.3%（即 3.7x），自算 Total Debt / Stockholders Equity（Q2'26）= 3.6x。
- Quick ratio 0.258（info）。營運資金 Q2'26 為 -0.28B。
- 有形帳面價值為負（-2.09B）；Goodwill 2.81B（FY2025）。
- 負債端: FY2025 發行債務 6.02B、償還 3.82B；Q2'26 單季發行 4.42B、償還 4.44B。淨負債自 2023 年底的 10.9B 增至 Q2'26 的 19.5B。
- 特別股: 帳列 2.476B，FY2025 特別股股利 0.192B，為普通股以外的固定支出。

## Capital allocation & insider signal

### 資本配置（USD B）
| 項目 | 2022 | 2023 | 2024 | 2025 | TTM（自算） |
|---|---|---|---|---|---|
| 股票回購 | 1.949 | 1.245 | 1.266 | 1.028 | 1.148 |
| 普通股股利 | 0.302 | 0.313 | 0.305 | 0.306 | 0.308 |
| 特別股股利 | 0.151 | 0.150 | 0.173 | 0.192 | 0.192 |
| 年末流通股數（M） | 389.8 | 351.5 | 339.8 | 338.1 | Q2'26: 336.0 |

- 股利覆蓋（自算）: FY2025 FCF / 總現金股利 (0.498B) = 2.6x；TTM = 2.255 / 0.500 = 4.5x。info payoutRatio 15.4%，dividendRate 0.92（季 0.23），殖利率 0.65%。覆蓋充足。
- 回購與股利合計 FY2025 為 1.53B，超過 FY2025 FCF 1.32B，差額由舉債支應，與同期淨負債增加 3.4B 一致。
- 股本由 2022 的 389.8M 降至 2025 的 338.1M（-13.3%），每股回報主要來自股數減少。
- Capex 占用的現金逐年增加，目前股東回報已壓縮到 FCF 的約 73%（TTM 自算）。

### 內部人交易（近 6 個月 2026-04-28 至 2026-10-28，自算）
| 日期 | 人員 | 職位 | 交易 | 股數 | 金額 (USD M) |
|---|---|---|---|---|---|
| 2026-10-07 | Moldovan Kristopher E. | Officer (CFO) | 賣出 @165.00 | 20,000 | 3.30 |
| 2026-10-06 | Hudson Scott A. | Officer | 賣出 @160.14 | 22,222 | 3.56 |
| 2026-09-08 | Moldovan Kristopher E. | CFO | 賣出 @151.03 | 20,000 | 3.02 |
| 2026-09-08 | Hudson Scott A. | Officer | 賣出 @150.97–152.56 | 44,444 | 6.75 |
| 2026-09-01 | Burke James A. | CEO | 買進 @135.25–135.99 | 6,665 | 0.90 |
| 2026-08-24 | Burke James A. | CEO | 買進 @135.00 | 2,000 | 0.27 |
| 2026-06 | Director 群（Sult、Acosta、Helm、Barbas） | Director | 賣出 | 47,988 | 8.33 |
| 2026-06 | Montemayor Margaret M. | Officer | 賣出 | 9,600 | 1.56 |

- 合計: 賣出 163,254 股 / USD 25.88M；買進 8,665 股 / USD 1.17M（全數為 CEO Burke）。淨賣出 USD 24.7M，占市值（49.22B）約 0.05%，規模小。
- 持股結構: insidersPercentHeld 0.77%，institutionsPercentHeld 92.4%。前幾大機構: BlackRock 8.66%、Vanguard 合計約 11.4%、State Street 5.02%、FMR 4.22%（季度減持 -10.4%）。
- 空頭: shares short 9.95M，占流通比 3.43%，shortRatio 1.42 日。

## Valuation

價格 146.66（fast_info，快取）；市值 49.22B；EV 71.79B（info）；流通股 335.6M。
- 乘數: trailing P/E 24.7x；forward P/E 14.0x（forwardEps 10.48）；FY2026 預估 epsCurrentYear 8.81 → P/E 16.6x。
- EV/EBITDA（TTM）10.8x。
- P/FCF（TTM，自算）21.8x；P/OCF（TTM）9.6x。
- P/S（TTM）2.56x；P/B 16.4x（受回購縮減權益影響，失真）。
- PEG 0.40（info），但 earningsGrowth 為 -6.2%，PEG 在負成長下無意義，不採用。
- 技術位置（ta snapshot, as_of 2026-10-27）: RSI14 48.7、MACD 柱 -1.56、BB %B 0.39、ATR14 7.53（約現價 5.1%）、距 MA50 +1.1%、距 MA200 -4.8%、12M 動能 -27.2%、52W 區間 132.66–203.66。
- 分析師: 22 位，recommendationMean 1.30（強烈買進），平均目標價 208.23（+42%），最高 305、最低 106。

## Key catalysts

- 2026-11-06（已排定）Q3'26 財報；EPS 預估 2.69。
- 上一季 Q2'26（2026-08-10）: 報告 EPS 0.76 vs 預估 1.66，未達 -54.2%。Q1'26 報告 2.87 vs 1.87，超出 +53.4%。Q4'25 報告 0.54 vs 2.30，未達 -76.5%。EPS 波動極大，需以調整後數字判讀。
- 管理層指引: DATA_UNAVAILABLE。
- 資本支出加速（2025 YoY +32%），對未來現金流與負債的影響需待 Q3 財報與指引確認。

## Metrics table

| Metric | Latest | YoY | Verdict |
|---|---|---|---|
| 營收 FY2025 (USD B) | 17.74 | +3.0% | 偏弱 |
| 營收 TTM (USD B) | 19.21 | Q2'26 YoY -5.5% | 偏弱 |
| 毛利率 FY2025 | 32.9% | -10.8pt | 中性 |
| 營業利益率 FY2025 | 10.7% | -13.0pt | 偏弱 |
| 淨利率 NI 歸屬普通股 FY2025 | 4.2% | -10.1pt | 偏弱 |
| ROIC FY2025（自算） | 8.3% | 2024 約 18.8% | 中性偏弱 |
| FCF TTM（USD B） | 2.255 | n/a | 中性 |
| Net debt / EBITDA | TTM 約 2.9x；FY2025 3.7x | FY2024 2.3x | 偏高 |
| Current ratio | 0.97x（Q2'26） | FY2024 0.96x | 偏弱 |
| 內部人淨買賣 6M (USD M) | -24.7 | 占市值 0.05% | 中性偏弱 |
| Trailing P/E | 24.7x | n/a | 偏高 |
| Forward P/E | 14.0x | n/a | 合理 |
| EV/EBITDA (TTM) | 10.8x | n/a | 中性 |
| 分析師平均目標價 | 208.23（+42%） | n/a | 正面 |
| Beta | 1.38 | n/a | 波動偏高 |

## Red flags

- EPS 與季度獲利劇烈波動: Q4'25 未達 -76.5%、Q1'26 超出 +53.4%、Q2'26 未達 -54.2%。
- 槓桿持續上升: 淨負債由 2023 年底 10.9B 升至 Q2'26 19.5B；FY2025 net debt/EBITDA 3.7x。
- 流動性偏薄: 現金僅 0.435B（Q2'26），流動比率 0.97x，營運資金為負，有形帳面價值為負（-2.09B）。
- 獲利與 FCF 下滑: FY2025 毛利率 -10.8pt、營業利益率 -13.0pt、FCF -47%；ROIC 由約 18.8% 降至 8.3%。
- 股東回報部分由舉債支應: FY2025 回購 + 股利 1.53B，高於 FCF 1.32B，同期負債淨增。
- 內部人淨賣出 USD 24.7M，主要為 CFO、Officer 於 9–10 月、價格 150–165 區間出售；CEO 買進規模僅 USD 1.17M。
- 資料品質: info freeCashflow（37.1M）與季度推算 TTM FCF（2.255B）不一致；部分季度欄位為 null。
- 管理層指引與分部資料為 DATA_UNAVAILABLE。

FUNDAMENTALS REPORT COMPLETE
