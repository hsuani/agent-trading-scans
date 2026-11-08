# Fundamentals — NVDA as of 2026-11-09

> **資料來源與完整性聲明（必讀）**
> - `pipeline/tools/yf NVDA info` 與 `fast_info` 的即時輸出為 **AMD 的資料**（website 為 amd.com、長篇描述為 Advanced Micro Devices，`fast_info` 價格 449.04 亦為 AMD 價格；`financials` 的 FY2025 營收 346.4 億美元與 AMD 相符）。本報告**未採用** yf 工具對 NVDA 的 info / fast_info / financials 輸出。
> - 改為直接讀取 repo 快取 `prices/yf/NVDA.json`（`symbol` = NVDA，`_refreshed_at` = 2026-11-08T13:16:49Z，`_misses` 為空）。以 `regularMarketPrice` 186.64 × `sharesOutstanding` 24.147B ≈ 4,506.8B 與 `marketCap` 4,506.8B 相符，身分與單位已交叉驗證；TTM 淨利 / 稀釋股數 ≈ 7.91 EPS 與 `trailingEps` 7.91 相符。
> - `yf NVDA balance_sheet` 工具輸出為空（0 bytes），資產負債表改以快取 `balance_sheet` / `quarterly_bs` 欄位計算。
> - 下游注意：yf 工具對 NVDA 的 `info` / `fast_info` / `financials` 路由疑似錯誤，請勿以該輸出作為 NVDA 價格或財報來源，直到修復為止。
> - 單位：NVDA 為 USD，本報告以 **USD B（十億美元）** 標示，全篇不混用 億。
> - 資料期間：年報至 FY2026（截至 2026-01-31）；季報至 2026-07-31（FY2027 Q2）。無 as-of 之後已發生的財報資料；唯一未來事件為下次財報日 2026-11-17。
> - 價格基準：`regularMarketPrice` 186.64，快取未明確標示收盤基準日，以快取時間 2026-11-08 為準。

## Executive summary
NVDA 財務健康度極強：FY2026 營收 USD 215.9B（YoY +65.5%），TTM 營收 USD 303.0B、TTM 淨利 USD 192.9B（淨利率 63.7%），淨現金約 USD 23.6B；唯一明顯紅旗是 2026-07 季總債務自 USD 12.3B 跳升至 USD 38.4B（原因未在資料中），以及 TTM FCF / 淨利僅 0.66。估值方面，trailing P/E 23.6x、forward P/E 11.7x、EV/EBITDA 22.2x，以成長調整後偏便宜（PEG 0.23）；股價 186.64 低於 50 日（219.8）與 200 日（204.7）均線，52 週績效 -6.2%，分析師平均目標價 327.1（較現價 +75%）。同業中位數 DATA_UNAVAILABLE，無法做正式相對估值。

## Revenue & profitability

**年度損益（USD B）**

| 會計年度 | 營收 | YoY | 毛利率 | 營業利益率 | 淨利 | 淨利率 |
|---|---|---|---|---|---|---|
| FY2023（1/2023） | 27.0 | n/a | 56.9% | 20.7% | 4.4 | 16.2% |
| FY2024（1/2024） | 60.9 | +125.9% | 72.7% | 54.1% | 29.8 | 48.8% |
| FY2025（1/2025） | 130.5 | +114.2% | 75.0% | 62.4% | 72.9 | 55.8% |
| FY2026（1/2026） | 215.9 | +65.5% | 71.1% | 60.4% | 120.1 | 55.6% |
| TTM（至 2026-07） | 303.0 | n/a | 74.7% | 65.2% | 192.9 | 63.7% |

- 3 年營收 CAGR（FY2023 → FY2026）= **100.0%**。FY2022 年度欄位在快取為 null，4 年 CAGR 為 DATA_UNAVAILABLE。
- 營收加速後動能仍在：FY2027 Q2（2026-07）營收 USD 96.2B，YoY **+105.9%**，QoQ +17.9%（季度序列：Q3 FY26 57.0 → Q4 FY26 68.1 → Q1 FY27 81.6 → Q2 FY27 96.2）。
- 毛利率自 FY2024 高點 75.0%（FY2025）回落至 FY2026 71.1%，但 Q2 FY27 回升至 75.0%（毛利 USD 72.1B）；營業利益率 Q2 FY27 為 66.2%（營業利益 USD 63.7B）。
- 研發費用 FY2026 USD 18.5B（占營收 8.6%），FY2025 為 USD 12.9B（9.9%）；Q2 FY27 研發 USD 7.05B。
- 有效稅率 FY2026 約 15.1%（稅費 USD 21.4B / 稅前 USD 141.5B），FY2025 約 13.3%。
- 分部營收占比：快取 `longBusinessSummary` 僅描述兩大分部（Compute & Networking、Graphics），未提供分部營收數字，**分部占比為 DATA_UNAVAILABLE**。

**獲利能力指標**

- ROE（info）**117.2%**；ROA 53.6%。權益基期快速膨脹（2026-07 股東權益 USD 229.0B，2025-07 為 USD 100.1B），故 ROE 高估的成分需留意。
- ROIC（本報告估算）≈ 81.9%：TTM 營業利益 USD 197.6B × (1 − 15.1%) ÷ [股東權益 229.0 + 總債務 38.4 − 現金與短期投資 62.5]（USD B，2026-07 期末）。此為本報告推算，非工具欄位。

## Cashflow & balance sheet

**現金流量（USD B）**

| 期間 | 營運現金流 | 資本支出 | FCF | FCF 利潤率 | FCF / 淨利 |
|---|---|---|---|---|---|
| FY2024 | 28.1 | 1.1 | 27.0 | 44.4% | 0.91 |
| FY2025 | 64.1 | 3.2 | 60.9 | 46.6% | 0.83 |
| FY2026 | 102.7 | 6.0 | 96.7 | 44.8% | 0.81 |
| TTM（至 2026-07） | 134.4 | 7.4 | 127.0 | 41.9% | 0.66 |

- 季度變化劇烈：Q1 FY27（2026-04）營運現金流 USD 50.3B、FCF 48.6B；Q2 FY27（2026-07）營運現金流驟降至 USD 24.1B、FCF 21.4B（Q2 淨利 USD 59.7B，OCF / 淨利 僅 0.40）。
- 快取 `info.freeCashflow` 為 USD 41.8B，與季度 FCF 加總的 USD 127.0B 明顯不一致；本報告採用季度加總值，並以 OCF 134.4B（與 info `operatingCashflow` 134.4B 吻合）反推，`freeCashflow` 欄位列為**待核對**。
- FCF / 淨利 TTM 0.66，低於 0.9 健康門檻；FY2026 年度為 0.81，亦未達門檻。原因需追查營運資本（存貨、應收帳款，應收資料在快取中未取得）。

**資產負債表（USD B，2026-07-31）**

| 項目 | 數值 | 備註 |
|---|---|---|
| 總資產 | 320.3 | Jan-26 為 206.8 |
| 流動資產 / 流動負債 | 197.4 / 43.0 | 流動比率 4.59x（info 4.589） |
| 現金及約當現金 | 22.4 | |
| 現金與短期投資 | 62.5 | info `totalCash` 62.47 |
| 總債務 | 38.4（季度）/ 38.9（info） | Apr-26 為 12.3；Jan-26 為 11.0 |
| 淨現金（現金與短期投資 − 總債務） | ≈ +23.6 | 以 info totalCash / totalDebt 計 |
| 股東權益 | 229.0 | Jul-25 為 100.1 |
| 負債 / 權益 | 16.7%（0.17x） | info debtToEquity 16.97（百分比表示） |
| 存貨 | 31.6 | YoY +111%；DIO 約 119 天（本報告估算） |
| 商譽＋無形資產 | 24.1（Jan-26） | Jan-25 為 6.0，FY2026 增加約 4 倍 |

- **總債務 Q2 FY27 單季增加 USD 26.0B**（2026-04 的 12.3 → 2026-07 的 38.4）。季度現金流量表未列出發債或還債明細（`Repayment Of Debt` 為 None，`Issuance Of Debt` 無季度值），**原因為 DATA_UNAVAILABLE**。
- 快取 quarterly_bs 的 `Net Debt` 欄位為 USD 10.9B，與「總債務 − 現金與短期投資」的淨現金 +23.6B 方向相反，兩者定義不同，本報告不採用該欄位。

## Capital allocation & insider signal

**資本配置**
- 股票買回：FY2026 USD 40.1B（占 FY2026 FCF 41.5%），FY2025 USD 33.7B，FY2024 USD 9.5B；Q2 FY27 單季 USD 19.7B。
- 股利：FY2026 USD 0.97B（占 FCF 約 1%），info `dividendYield` 0.54%、`payoutRatio` 0.035；股利覆蓋率（FCF / 股利）約 99 倍，無覆蓋疑慮。
- 資本支出占營收：FY2024 1.8% → FY2025 2.5% → FY2026 2.8%，呈上升趨勢，但仍遠低於 FCF 規模。
- 股數：Jan-26 為 24.30B 股、Jul-26 為 24.15B 股，半年減少 0.65%；稀釋後平均股數 Q2 FY27 為 24.29B。
- SBC FY2026 USD 6.4B（占營收 3.0%），Q2 FY27 單季 USD 2.0B。

**內部人交易（近 6 個月，2026-05-09 至 2026-11-09；快取最新交易日 2026-09-21）**

| 類別 | 筆數 | 股數（M） | 金額（USD M） |
|---|---|---|---|
| 賣出（Sale） | 9 | 6.20 | 1,370.5 |
| 贈與（Gift，價格 0） | 5 | 2.21 | 0 |
| 獎勵授予（Award） | 13 | 0.41 | 0 |

- 賣出金額高度集中：Mark Stevens（董事）USD 1,353.7M，Timothy Teter（總法律顧問）USD 13.3M，Stephen Neal（董事）USD 3.3M，John Dabiri（董事）USD 0.1M。
- 賣出金額占市值 USD 4,506.8B 僅約 **0.03%**，相對規模極小；內部人持股 4.0%。
- 解讀：淨賣出（無買進），但幅度相對市值微小，且主要來自單一董事，屬於個人規劃性質的可能性高，不構成強烈負面訊號（本段為事實陳述，非交易建議）。

## Valuation

以現價 186.64 計算（市值 USD 4,506.8B，EV USD 4,474.4B）：

| 指標 | 數值 | 計算依據 |
|---|---|---|
| Trailing P/E | 23.6x | 186.64 ÷ TTM EPS 7.91 |
| Forward P/E | 11.7x | 186.64 ÷ forward EPS 15.91 |
| EV/EBITDA（TTM） | 22.2x | EV 4,474.4 ÷ EBITDA 201.3（info） |
| P/FCF（TTM） | 35.5x | 市值 4,506.8 ÷ FCF 127.0（季度加總） |
| P/S（TTM） | 14.9x | 市值 4,506.8 ÷ 營收 303.0 |
| P/B | 19.7x | 186.64 ÷ BVPS 9.48 |
| PEG | 0.23 | info `pegRatio` |
| 同業中位數 | DATA_UNAVAILABLE | 工具未提供同業組，無法給出正式中位數 |

- 估值呈現「獲利高速成長下 forward P/E 低、trailing P/E 中等」的結構。forward EPS 15.91 相對 TTM EPS 7.91 隱含約 +101% 的 EPS 成長預期。
- 股價走勢：現價較 52 週高點 243.37 低 23.3%，較 50 日均線低 15.1%，較 200 日均線低 8.8%；52 週績效 -6.2%，同期 S&P 500 為 +8.0%（info `SandP52WeekChange`）。beta 2.25。
- 分析師目標價：平均 327.1、中位 315.0、高 515.0、低 180.0（58 位分析師）。平均目標價較現價 +75.3%；最低目標價 180.0 低於現價。評級分布（0m）：Strong Buy 10、Buy 49、Hold 2、Sell 1、Strong Sell 0；recommendationMean 1.29（strong_buy）。

## Key catalysts
- **下次財報**：2026-11-17（快取 `earnings_dates` 與 info `isEarningsDateEstimate = False`，日期為確認值；時間 21:00 UTC，即美東下午 4 點）。距 as-of 日 8 天。
- **財報一致預期 EPS**：2.47（`earnings_dates` 首筆）。
- **歷史 EPS 驚喜**：近 8 季皆為正向，驚喜幅度 +3.5% 至 +8.0%；最近一季（2026-08-26）預估 2.09、報告 2.22、驚喜 +6.2%。注意：快取報告 EPS（2.22）與 GAAP 淨利 ÷ 稀釋股數推算（Q2 FY27 約 2.46）口徑不同，本報告未能確認 `earnings_dates` 的 EPS 口徑。
- **近期指引（guidance）**：快取無指引文字，**DATA_UNAVAILABLE**。
- **分部轉變**：快取無分部營收，**DATA_UNAVAILABLE**。
- **潛在變數**：FY2026 商譽與無形資產四倍增加（併購細節 DATA_UNAVAILABLE）、2026-07 單季發債（用途 DATA_UNAVAILABLE）、存貨年增 111%，財報中皆應檢視。

## Metrics table

金額單位標示於欄位：USD B；比率為 %、x。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收（TTM, USD B） | 303.0 | n/a（季度 Q2 FY27 YoY +105.9%） | DATA_UNAVAILABLE | 極強 |
| 營收 3 年 CAGR（FY23–FY26） | 100.0% | n/a | DATA_UNAVAILABLE | 極強 |
| 毛利率（TTM） | 74.7% | FY26 71.1%（FY25 75.0%） | DATA_UNAVAILABLE | 高，穩定 |
| 營業利益率（TTM） | 65.2% | FY26 60.4%（FY25 62.4%） | DATA_UNAVAILABLE | 極高 |
| 淨利率（TTM） | 63.7% | FY26 55.6%（FY25 55.8%） | DATA_UNAVAILABLE | 極高 |
| ROE（info） | 117.2% | n/a | DATA_UNAVAILABLE | 高（權益基期膨脹，留意） |
| ROIC（本報告估算） | ≈ 81.9% | n/a | DATA_UNAVAILABLE | 極高 |
| FCF 利潤率（TTM, USD B 為 127.0） | 41.9% | FY26 44.8% | DATA_UNAVAILABLE | 高，但季度下滑 |
| FCF / 淨利（TTM） | 0.66 | FY26 0.81 | DATA_UNAVAILABLE（健康門檻 >0.9） | 黃燈 |
| 流動比率 | 4.59x | n/a | DATA_UNAVAILABLE | 極健全 |
| 負債 / 權益 | 16.7% | n/a | DATA_UNAVAILABLE | 低 |
| 淨現金（USD B） | ≈ +23.6 | Q2 總債務 +26.0 QoQ | DATA_UNAVAILABLE | 中性，需追查負債 |
| 存貨（USD B） | 31.6 | YoY +111% | DATA_UNAVAILABLE | 黃燈（DIO 約 119 天） |
| 股票買回（FY26, USD B） | 40.1 | FY25 33.7（+19%） | DATA_UNAVAILABLE | 積極 |
| 股利覆蓋率（FCF / 股利） | 約 99x | n/a | DATA_UNAVAILABLE | 無疑慮 |
| 資本支出 / 營收（FY26） | 2.8% | FY25 2.5% | DATA_UNAVAILABLE | 溫和上升 |
| 內部人賣出（近 6 月, USD M） | 1,370.5 | n/a | DATA_UNAVAILABLE | 相對市值 0.03%，低 |
| Trailing P/E | 23.6x | n/a | DATA_UNAVAILABLE | 中等 |
| Forward P/E | 11.7x | n/a | DATA_UNAVAILABLE | 偏低 |
| EV/EBITDA（TTM） | 22.2x | n/a | DATA_UNAVAILABLE | 中等偏高 |
| P/FCF（TTM） | 35.5x | n/a | DATA_UNAVAILABLE | 中等 |
| P/S（TTM） | 14.9x | n/a | DATA_UNAVAILABLE | 高 |
| PEG | 0.23 | n/a | DATA_UNAVAILABLE | 成長調整後偏低 |
| 股價 vs 200 日均線 | -8.8% | n/a | DATA_UNAVAILABLE | 弱於長期趨勢 |
| 52 週績效 | -6.2%（S&P +8.0%） | n/a | DATA_UNAVAILABLE | 落後大盤 |
| 分析師平均目標價 vs 現價 | +75.3% | n/a | DATA_UNAVAILABLE | 分析師共識正向 |

## Red flags
- **資料來源污染**：yf 工具對 NVDA 的 info / fast_info / financials 回傳 AMD 資料，須修復路由；本報告以 repo 快取 NVDA.json 替代（已交叉驗證）。
- **總債務跳升**：2026-07 單季總債務由 USD 12.3B 增至 USD 38.4B（+26.0B），用途與條款 DATA_UNAVAILABLE，為本期最需追查的資產負債表變化。
- **現金轉換走弱**：TTM FCF / 淨利 0.66，Q2 FY27 營運現金流 / 淨利 僅 0.40；Q2 OCF 較 Q1 下滑 52%。
- **存貨快速累積**：存貨 USD 31.6B，YoY +111%，DIO 約 119 天；存貨跌價風險需在後續財報觀察。
- **商譽與無形資產四倍**：FY2026 由 USD 6.0B 增至 USD 24.1B，併購資料 DATA_UNAVAILABLE，減損風險待評估。
- **資料內部不一致**：info `freeCashflow` 41.8B 與季度 FCF 加總 127.0B 不符；quarterly_bs `Net Debt` 與淨現金定義不符；`earnings_dates` 報告 EPS 與 GAAP 推算值口徑不同。
- **股價技術弱勢**：現價低於 50 日與 200 日均線，較 52 週高點 -23.3%，beta 2.25，波動性高。
- **集中內部人賣出**：單一董事賣出 USD 1.35B（金額絕對值大，但占市值僅約 0.03%）。

FUNDAMENTALS REPORT COMPLETE
