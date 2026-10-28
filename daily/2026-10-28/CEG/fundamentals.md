# Fundamentals — CEG (Constellation Energy Corporation) as of 2026-10-28

## Executive summary
CEG 的財務體質在 2026 上半年明顯轉弱：GAAP 淨負債由 FY25 年底 5.35B USD 升至 2026-06-30 的 24.00B USD，流通股數由 312.3M 增至 355.3M，TTM 自由現金流僅約 0.31B USD，不足以覆蓋 TTM 股利現金支出 0.55B USD。估值面，trailing GAAP P/E 25.3x、EV/EBITDA 14.6x 相對一般 IPP 同業估計區間偏高，forward P/E 19.4x 與 2026E 共識 P/E 21.3x 則相對合理，但需要併購整合與盈餘品質（GAAP 與 adjusted EPS 差異大）獲得驗證。分析師共識 23 家、平均目標價 339.07 USD（相對最新價 +30.9%），本報告不提供交易建議。

**資料時效說明**：價格與 info 欄位來自 cache（info cached_at 2026-10-28 12:39 UTC；fast_info cached 12:37 UTC），屬正常 cache fallback。yfinance 即時通道（cookie/crumb）失敗，所有數字以 cache 為準。技術指標（ta）as_of 為 2026-10-27。財報資料最新一期為 2026-06-30 季報。唯一的「未來」日期是 2026-11-09 的預定財報日（earnings_dates，isEarningsDateEstimate=false），屬已排定事件而非已發布資料，在 as-of 之後尚未發生。

**幣別單位**：本報告為 USD，依規定以 B（十億美元）與 M（百萬股）表示，全文未使用「億」。

## Revenue & profitability

### 年度趨勢（USD B，FY 為 12 月底年度）
| 項目 (USD B) | FY22 | FY23 | FY24 | FY25 |
|---|---|---|---|---|
| 營收 Total Revenue | 24.44 | 24.92 | 23.57 | 25.53 |
| 營收 YoY | n/a | +2.0% | -5.4% | +8.3% |
| 毛利 Gross Profit (Yahoo 定義) | 2.14 | 3.23 | 5.99 | 4.69 |
| 毛利率 | 8.7% | 13.0% | 25.4% | 18.4% |
| 營業利益 Total Operating Income As Reported | 0.495 | 1.610 | 4.352 | 3.086 |
| 營業利益率（as reported） | 2.0% | 6.5% | 18.5% | 12.1% |
| 淨利 Net Income | -0.160 | 1.623 | 3.749 | 2.319 |
| 淨利率 | -0.7% | 6.5% | 15.9% | 9.1% |
| 稀釋 EPS (USD, GAAP) | -0.49 | 5.01 | 11.89 | 7.40 |

- **3 年營收 CAGR（FY22→FY25）約 1.5%**，成長極緩。2021 年資料在 yfinance 中為 null，無法計算 5 年 CAGR，標示為 DATA_UNAVAILABLE。
- FY25 營收 YoY +8.3%，但 FY25 GAAP 淨利 YoY 為 -38.1%、稀釋 EPS YoY 為 -37.8%，獲利下滑幅度遠大於營收。
- 毛利率在 FY24 達 25.4% 後 FY25 回落至 18.4%；營業利益率由 18.5% 降至 12.1%。
- Yahoo 衍生的 Operating Income（FY25 為 4.198B）與 as reported 營業利益（3.086B）存在定義差異，本報告以 as reported 為主，請下游注意。

### 季度趨勢與 TTM（USD B）
| 項目 (USD B) | Q3'25 | Q4'25 | Q1'26 | Q2'26 | TTM (至 Q2'26) |
|---|---|---|---|---|---|
| 營收 | 6.570 | 6.074 | 11.122 | 7.504 | 31.27 |
| 營收 YoY | n/a | n/a | n/a | +23.0% (vs 6.101) | n/a |
| 淨利 (GAAP) | 0.930 | 0.432 | 1.590 | 0.513 | 3.465 |
| 稀釋 EPS (GAAP, USD) | 2.97 | 1.38 | 4.49 | 1.42 | 10.23 (info trailingEps) |
| Adjusted EPS (earnings_dates, USD) | 3.04 | 2.30 | 2.74 | 2.55 | 10.63 (加總) |

- TTM 營收 31.27B 與 info totalRevenue 31.27B 一致；TTM 淨利 3.465B 與 info netIncomeToCommon 3.465B 一致（已核對）。
- Q2'26 營收 YoY +23.0%，與 info revenueGrowth 0.23 相同，因此 info 的 23% 是單季 YoY，不是 TTM 成長率。
- Q1'25 季度資料為 null，Q1'26 無法計算 YoY。
- **GAAP 與 adjusted EPS 差異巨大**：Q1'26 GAAP 4.49 vs adjusted 2.74；Q2'26 GAAP 1.42 vs adjusted 2.55。GAAP 盈餘包含大額非經常項目（Q2'26 Total Unusual Items 1.228B、Gain On Sale Of Security 1.226B，Q1'26 為 0.098B），盈餘品質需要拆解。
- Q2'26 Yahoo 衍生 Operating Income 為 -0.047B（as reported 為 0.580B），本季核心營運偏弱。

### 利潤率與報酬
- TTM 毛利率（info grossMargins）22.1%；TTM 淨利率（info profitMargins）11.1%；TTM EBITDA 利潤率（info ebitdaMargins）25.4%。
- ROE（info）15.1%。以 FY25 淨利 2.319B / 期末股東權益 14.517B 計算為 16.0%（已核對）。2026-06-30 股東權益增至 31.98B，後續 ROE 會被稀釋。
- ROIC（估計）：FY25 EBIT 4.022B × (1 - 33.8% 稅率) ≈ 2.66B，除以 FY25 Invested Capital 23.509B ≈ 11.3%。2026-06-30 Invested Capital 增至 56.68B，若以同樣稅率假設估算，TTM 報酬率明顯被稀釋（估計約 7-8%，此為本報告推算，非工具直接輸出）。

## Cashflow & balance sheet

### 現金流（USD B）
| 項目 (USD B) | FY22 | FY23 | FY24 | FY25 | TTM (至 Q2'26) |
|---|---|---|---|---|---|
| 營運現金流 OCF | -2.353 | -5.301 | -2.464 | 4.237 | 4.206 |
| 資本支出 Capex | 1.689 | 2.422 | 2.565 | 2.949 | 3.897 |
| 自由現金流 FCF (OCF - Capex) | -4.042 | -7.723 | -5.029 | 1.288 | 0.309 |
| FCF 利潤率 | -16.5% | -31.0% | -21.3% | 5.0% | 1.0% |
| FCF / 淨利 | n/m | n/m | n/m | 0.56x | 0.09x |
| OCF / 淨利 | n/m | n/m | n/m | 1.83x | 1.21x |

- **FCF / 淨利 FY25 為 0.56x，TTM 僅 0.09x，遠低於 0.9 的健康門檻**。
- OCF 在 FY22 至 FY24 連續為負，FY24 的 Change In Other Working Capital 為 -10.878B，屬大幅營運資金波動。原因在工具輸出中未說明，可能與抵押品或衍生品相關，屬推測，需以 10-K/10-Q 驗證。
- Capex 連續增加：FY22 1.689B → FY25 2.949B（FY25 YoY +15.0%），FY25 Capex / D&A（1.937B）為 1.52x，屬擴張期投資。
- **info freeCashflow 為 -6.625B，與報表 TTM FCF +0.309B 明顯矛盾**。本報告以報表計算值為準，info 欄位的 FCF 不採用。

### 資產負債表（USD B）
| 項目 (USD B) | 2022-12-31 | 2023-12-31 | 2024-12-31 | 2025-12-31 | 2026-06-30 |
|---|---|---|---|---|---|
| 總負債 Total Debt | 5.768 | 9.261 | 8.412 | 8.992 | 24.700 |
| 淨負債 Net Debt | 5.346 | 8.893 | 5.390 | 5.351 | 24.003 |
| 股東權益 Stockholders Equity | 11.018 | 10.925 | 13.166 | 14.517 | 31.977 |
| 總資產 Total Assets | 46.909 | 50.758 | 52.926 | 57.249 | n/a |
| 流通股數 (期末, M) | 327 (diluted avg) | 317 | 312.8 | 312.3 | 355.3 |

- **2026-06-30 淨負債為 24.00B，較 2025-12-31 的 5.35B 增加約 18.7B（+349%）**。總負債 24.70B，現金 0.697B（info totalCash）。
- 淨負債 / TTM EBITDA：info EBITDA TTM 7.952B，計算為 24.00 / 7.952 ≈ 3.0x（FY25 為 0.9x）。
- 流動比率 1.455（info），速動比率 0.471（info）；FY25 流動比率以 12.119 / 7.944 計算為 1.53，屬健康水準。
- 負債 / 股東權益：info debtToEquity 76.4%；以 2026-06-30 總負債 24.70B / 普通股股東權益 31.98B 計算約 0.77x，FY25 為 0.62x。
- 利息保障倍數：TTM EBIT（報表 EBIT 列）5.895B / TTM 利息費用 0.783B ≈ 7.5x，仍在可接受範圍，但利息費用由 FY25 的 0.511B 上升至 TTM 0.783B（+53%）。
- Q1'26 Repayment of Debt 6.754B 與 Issuance of Debt 7.727B 同時發生，代表大規模再融資與債務重組。
- Goodwill 與無形資產僅 0.42B，帳面資產組合以實體發電資產為主（Net PPE FY25 22.474B）。

## Capital allocation & insider signal

### 資本配置
- **股利**：info dividendRate 1.71 USD（年化，最近一季 0.427 USD），殖利率 0.68%，5 年平均殖利率 0.56%，payoutRatio（以 trailing EPS 計）15.9%。
  - 股利現金支出：FY25 0.486B；TTM 0.551B（Q3'25 0.121 + Q4'25 0.121 + Q1'26 0.155 + Q2'26 0.154）。
  - **股利覆蓋率**：以 TTM FCF 計為 0.56x（不足覆蓋）；以 TTM 淨利計為 6.3x；以 TTM OCF 計為 7.6x。
- **回購**：FY22 0、FY23 0.992B、FY24 0.999B、FY25 0.400B（僅 Q2'25 單季）；2026 上半年無回購資料（季度為 null 或 0）。
- **股本變動（重大）**：流通股數 2025-12-31 312.29M → 2026-Q1 361.99M → 2026-06-30 355.30M。YTD 增加 43.0M 股（+13.8%）。Capital Stock 由 11.043B 升至 2026-Q1 的 28.574B。同期 Q1'26 有 Purchase of Business -2.537B。
  - 工具輸出未明示此次股本增加的交易名稱與結構，但時序與大額收購現金流吻合，屬本報告的推測，需以 10-Q 驗證。
  - Q2'26 股數減少約 6.7M 股，但 Repurchase 欄位為 null，原因未知（DATA_UNAVAILABLE）。
- **股東結構**（13F，截至 2026-06-30）：機構持股 82.9%（2,477 家）；內部人持股 0.34%；做空比例 3.75%（sharesShort 11.89M，short ratio 2.96 天）。
  - 前十大持有人：BlackRock 6.93%、Vanguard Capital Management 5.94%、State Street 5.48%、Vanguard Portfolio Management 4.47%、ECP ControlCo 4.06%（季減 34.8%）、Capital International 3.57%、Invesco 3.14%、Morgan Stanley 2.55%、Geode 2.12%、FMR 1.85%（季減 35.8%）。
  - ECP ControlCo 與 FMR 的大幅減持值得留意，工具輸出未標示 ECP 身份，不作推論。

### 內部人交易（近 6 個月：2026-04-28 至 2026-10-28）
| 日期 | 人員 | 類型 | 股數 | 價格 (USD) | 金額 (USD M) |
|---|---|---|---|---|---|
| 2026-04-28 | 11 位董事（各 556 股） | Stock Award 授予 | 6,116 合計 | 305.71 | 1.87 合計 |
| 2026-08-04 | Roger W. Crandall（董事） | Stock Award 授予 | 462 | 267.25 | 0.123 |
| 2026-08-11 | Roger W. Crandall（董事） | **Purchase 公開市場買入** | 1,500 | 278.62 | 0.418 |

- **近 6 個月公開市場買入合計 0.418M USD（1 筆，Crandall），公開市場賣出為 0**（工具輸出中未見）。
- 買入金額對市值（91,758.5M USD）比重約 0.0005%，規模極小，不具方向性訊號。
- 2026-02 的主管 Form 4 紀錄（如 Dominguez 191,817 股、Hanson 53,507 股等）與 2026-01-07 的 Novotny 298,853 股授予均在 6 個月窗口之外，且 value 為 null，性質未標示。本報告不將其計入買賣統計。
- 治理風險（info）：overallRisk 7、boardRisk 8、shareHolderRightsRisk 8、auditRisk 4、compensationRisk 3（10 分制，越高越差）。

## Valuation

### 價格與市值（USD）
- 最新價 258.98（info currentPrice；fast_info last_price 同值；前收 252.48）。
- 52 週區間 228.63 – 406.04；距 52 週高點 -36.2%，距 52 週低點 +13.3%。
- 50 日均線 273.21（-5.2%）；200 日均線 281.11（-7.9%）；價格低於兩條均線。
- 市值 91.76B USD；企業價值 EV 116.11B USD（市值 + 總負債 24.70B - 現金 0.697B + 少數股東權益 0.345B，已核對）。
- 流通股數 354.3M（info sharesOutstanding），floatShares 353.1M。

### 估值倍數
| 指標 | 數值 | 計算基礎 |
|---|---|---|
| P/E trailing（GAAP） | 25.3x | 258.98 / 10.23 |
| P/E trailing（Adjusted） | 24.4x | 258.98 / 10.63 |
| P/E forward（info） | 19.4x | 258.98 / 13.32（forwardEps） |
| P/E 2026E（共識 EPS 12.15） | 21.3x | 258.98 / 12.15 |
| EV/EBITDA（TTM） | 14.6x | 116.11 / 7.952 |
| EV/Revenue（TTM） | 3.71x | info enterpriseToRevenue |
| P/S（TTM） | 2.93x | info priceToSalesTrailing12Months |
| P/OCF（TTM） | 21.8x | 91.76 / 4.206 |
| P/FCF（TTM） | 297x | 91.76 / 0.309，數值不具參考性 |
| P/B | 2.88x | 258.98 / 每股帳面價值 89.999 |
| PEG | 3.74 | info pegRatio |

### 與同業比較
工具輸出未提供 sector median，以下「同業估計區間」為本報告依一般美國 IPP／公用事業經驗所做的粗估，**非工具資料**，僅供相對參考：
- P/E forward 同業約 15–20x；CEG 19.4x 位於高端。
- EV/EBITDA 同業約 10–13x；CEG 14.6x 偏高。
- P/B 同業約 1.5–2.5x；CEG 2.88x 偏高。
- 殖利率同業約 2–4%；CEG 0.68% 明顯偏低。

### 分析師共識（info，23 家）
- 推薦均值 1.56（"buy"，1 為最強買入、5 為賣出）。
- 目標價：平均 339.07、中位數 345.0、高 399.0、低 238.0 USD。以最新價計算，平均目標價隱含 +30.9%，最低目標價 238.0 低於現價 -8.1%。

### 技術面背景（ta，as_of 2026-10-27，僅供交叉參考）
- RSI(14) 44.3；MACD 柱狀體 -2.94（MACD -4.38、訊號線 -1.45），動能偏弱。
- 價格位於布林通道 %B 0.30（中軌 272.48、下軌 237.91、上軌 307.06）。
- ATR(14) 12.77 USD（約現價 4.9%）；20 日年化波動 67.1%。
- 動能：1 個月 -0.6%、3 個月 +0.4%、6 個月 -15.3%、12 個月 -33.5%。

## Key catalysts
- **2026-11-09 Q3'26 財報（已排定，EPS 共識 3.84 USD adjusted）**：為近期最重要事件。earnings_dates 顯示 CEG 過去 8 季有 6 季超過共識、2 季低於共識（Q3'25 -2.57%、Q2'25 -3.10%），最大單季超越為 Q2'26 的 +11.73%。財報將首次較完整反映收購後的盈餘與負債結構。
- **併購整合與負債去化**：淨負債由 5.35B 升至 24.00B，後續需關注再融資成本（TTM 利息費用 0.783B）與去槓桿進度。
- **FCF 轉正**：TTM FCF 僅 0.309B，Q4'25 與 Q1'26、Q2'26 為連續負值（-0.181B、-0.850B、-0.118B）。Q3'25 為 +1.458B。
- **股利**：最近一期 0.427 USD/季，除息日 2026-08-18、派息日約 2026-09-08（依 epoch 換算，皆已過期）。下一次除息日為 n/a。
- **營運面**：Q2'26 營收 YoY +23.0%，但 Q2 營業利益（as reported）YoY -39%（0.580B vs 0.951B）。
- **分析師目標價**：平均 339.07 USD，為 sell-side 的主要上行論點，但目標價隨盈餘調整可能下修，屬外部資料。
- 公司基本面：約 31,676 MW 發電容量（核能、風能、太陽能、天然氣、水力）；五個營運區段（Mid-Atlantic、Midwest、New York、ERCOT、Other Power Regions）。**區段收入與毛利：DATA_UNAVAILABLE**（工具輸出未提供分部數字）。

## Metrics table
單位：營收、淨利、現金流與股權金額為 USD B；股數為 M；倍數為 x；比率為 %。「同業估計」為本報告粗估，非工具資料。

| Metric | Latest | YoY | 同業估計 (粗估) | Verdict |
|---|---|---|---|---|
| 營收 TTM (USD B) | 31.27 | Q2'26 +23.0%；FY25 +8.3% | 同業估計成長 3–5% | 成長加速但與併購相關，需驗證有機成長 |
| 淨利 FY25 GAAP (USD B) | 2.319 | -38.1% | n/a | 下滑 |
| 淨利 TTM GAAP (USD B) | 3.465 | n/a | n/a | 中性 |
| 淨利率 TTM | 11.1% | FY25 9.1% vs FY24 15.9% | 8–12% | 中性 |
| 毛利率 TTM (info) | 22.1% | FY25 18.4% vs FY24 25.4% | n/a | 偏弱 |
| 營業利益率 FY25 (as reported) | 12.1% | FY24 18.5% (-6.4 pp) | 10–15% | 偏弱 |
| ROE (info) | 15.1% | FY25 計算 16.0% | 8–12% | 優於估計同業，但股本已稀釋 |
| ROIC FY25 (計算) | 11.3% | 2026 基礎估計約 7–8% | 6–9% | 併購後報酬下降 |
| FCF TTM (USD B) | 0.309 | FY25 1.288 (FY24 -5.029) | n/a | 極弱 |
| FCF 利潤率 TTM | 1.0% | FY25 5.0% | 5–10% | 偏弱 |
| FCF / 淨利 TTM | 0.09x | FY25 0.56x | >0.9 為健康 | 不健康 |
| OCF / 淨利 TTM | 1.21x | — | >1.0 | 健康 |
| 淨負債 (USD B, 2026-06-30) | 24.003 | 2025-12-31 為 5.351 (+349%) | n/a | 明顯惡化 |
| 淨負債 / EBITDA (TTM) | 3.0x | FY25 0.9x | 3–4x | 偏高，可接受 |
| 流動比率 | 1.46 (info) | FY25 計算 1.53 | 約 1.2 | 健康 |
| 負債 / 股東權益 | 0.77x | FY25 0.62x | n/a | 槓桿升高 |
| 利息保障倍數 TTM (EBIT / 利息) | 7.5x | FY25 7.9x | n/a | 仍可接受 |
| 資本支出 TTM (USD B) | 3.897 | FY25 2.949 (YoY +15.0%) | n/a | 擴張中 |
| 股利現金支出 TTM (USD B) | 0.551 | FY25 0.486 (YoY +9.5%) | n/a | 增加 |
| 股利覆蓋率 (TTM FCF) | 0.56x | — | >1.0x | 不足覆蓋 |
| 股利殖利率 | 0.68% | 5 年平均 0.56% | 2–4% | 偏低 |
| 股利 payoutRatio (EPS) | 15.9% | — | 60–80% (估計) | 低 |
| 回購 FY25 (USD B) | 0.400 | FY24 0.999 (-60%) | n/a | 下降，2026 H1 無 |
| 流通股數 (M) | 355.3 | 2025-12-31 為 312.3 (+13.8% YTD) | n/a | 明顯稀釋 |
| 內部人 6 個月淨交易 (USD M) | +0.418 (公開市場買入) | — | n/a | 規模極小 (占市值約 0.0005%)，無訊號 |
| P/E trailing (GAAP) | 25.3x | — | 18–22x | 偏貴 |
| P/E forward (info) | 19.4x | 2026E 共識 21.3x | 15–20x | 略貴 |
| EV/EBITDA (TTM) | 14.6x | — | 10–13x | 偏貴 |
| P/S (TTM) | 2.93x | — | 2–3x | 中性 |
| P/FCF (TTM) | 297x | — | n/a | 不具參考性 |
| P/B | 2.88x | — | 1.5–2.5x | 偏高 |
| PEG | 3.74 | — | 1–2 | 偏貴 |
| Beta (info) | 1.13 | — | 約 0.7–0.9 (估計) | 高於典型公用事業 |
| 分析師平均目標價 (USD) | 339.07 (+30.9%) | — | n/a | 分析師偏多 |
| 距 52 週高點 | -36.2% | 12 個月動能 -33.5% | n/a | 技術面弱勢 |
| 做空比例 (占流通股) | 3.75% | — | n/a | 中等偏低 |

## Red flags
- **自由現金流幾近於零**：TTM FCF 僅 0.309B USD，FCF / 淨利 0.09x；FY22 至 FY24 連續三年 FCF 為負（-4.0B、-7.7B、-5.0B）。
- **股利無法由自由現金流覆蓋**：TTM 股利 0.551B 相對 TTM FCF 0.309B，覆蓋率 0.56x。
- **負債急增**：淨負債由 5.35B（2025-12-31）升至 24.00B（2026-06-30），淨負債 / EBITDA 約 3.0x；TTM 利息費用增至 0.783B。
- **股本大幅稀釋**：流通股數 YTD +13.8%，Q1'26 Capital Stock 增加約 17.5B USD；EPS 與 ROE 被稀釋。
- **GAAP 與 adjusted 盈餘差距大**：Q1'26 GAAP EPS 4.49 vs adjusted 2.74；Q2'26 GAAP 1.42 vs adjusted 2.55，盈餘品質需拆解。
- **獲利下滑**：FY25 GAAP 淨利 YoY -38.1%，info earningsGrowth -46.8%、earningsQuarterlyGrowth -38.9%；Q2'26 Yahoo 衍生營業利益為負（-0.047B）。
- **資料矛盾**：info freeCashflow -6.625B 與報表 TTM FCF +0.309B 不一致；info operatingMargins 8.7% 與報表 TTM 營業利益率（約 14–15%）不一致，定義需確認。
- **大股東減持**：ECP ControlCo 季減 34.8%、FMR 季減 35.8%（13F，2026-06-30）。
- **股價趨勢弱**：低於 50 日與 200 日均線，距 52 週高點 -36.2%，12 個月動能 -33.5%，MACD 柱狀體為負。
- **估值偏高**：trailing P/E 25.3x、EV/EBITDA 14.6x、P/B 2.88x，相對估計同業區間偏貴；殖利率 0.68%。
- **治理風險指標偏高**：boardRisk 8、shareHolderRightsRisk 8、overallRisk 7（info，10 分制）。
- **資料缺口（DATA_UNAVAILABLE）**：區段營收與毛利、2021 年財報、Q1'25 季度資料、2026 年股本變動的交易結構與金額、2026-Q2 股數減少的原因、2026-06-30 完整現金餘額（僅有 info totalCash 0.697B）、sector median 同業數字、Q3'26 以外的前瞻營收與盈餘預測。

FUNDAMENTALS REPORT COMPLETE
