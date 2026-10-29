# Fundamentals — ZS as of 2026-10-30

資料來源: pipeline/tools/yf (ZS info / financials / quarterly_fin / balance_sheet / quarterly_bs / cashflow / quarterly_cf / earnings_dates / insider / major_holders / inst_holders)。財年截止 2026-07-31 (FY26)。金額單位: 公司以 USD 報告，表格標示 USD M 或 USD B，全文不混用億。

## Executive summary
ZS 營收維持約 25% 高成長 (FY26 營收 USD 3.35B，YoY +25.4%)，毛利率 76.8%，現金及短期投資 USD 3.47B 高於總債務 USD 1.86B，FY26 FCF 為正 USD 779M (FCF margin 23.2%)，財務體質穩健。但 GAAP 仍虧損 (FY26 淨損 USD -63M)，SBC 高達 USD 822M (佔營收 24.5%)，扣除 SBC 後 FCF 為 USD -43M，且股本每年稀釋約 3%。估值方面，前瞻 P/E 45.5x、P/S 12.4x、P/FCF 約 54x (FY26)，顯著高於一般軟體基礎設施同業估計中位數，且分析師平均目標價 USD 235 低於現價 USD 255.8，估值吸引力偏低。

## Revenue & profitability

**營收與成長**
- 年度營收 (USD M): FY23 1,617.0 → FY24 2,167.8 → FY25 2,673.1 → FY26 3,352.5。
- YoY: FY24 +34.1%、FY25 +23.3%、FY26 +25.4%。成長率在 FY25 回落後 FY26 回升。
- 3 年 CAGR (FY23→FY26) 約 27.5%。FY22 資料為 null，無法計算 3–5 年 CAGR，以 3 年為準。
- 季度趨勢 (USD M): 2025-10 季 788.1 → 2026-01 季 815.8 → 2026-04 季 850.5 → 2026-07 季 898.2。Q4 FY26 YoY +24.9%，QoQ +5.6%，成長節奏穩定。
- 分部營收: yfinance 無分部資料。依 longBusinessSummary，產品線包括 Zero Trust SASE、ZIA、ZPA、Zero Trust Branch/Cloud、資料安全 (DSPM、DLP)、Security for AI、Agentic Security Operations 等，但無各產品營收數字，無法量化產品組合變化。

**獲利能力 (依 FY 財報數字計算)**

| 年度 | 毛利率 | 營業利益率 (GAAP) | 淨利率 | 標準化 EBITDA 利潤率 |
|---|---|---|---|---|
| FY23 | 77.6% | -14.5% | -12.5% | n/a (EBITDA 為負) |
| FY24 | 78.0% | -5.6% | -2.7% | 2.8% |
| FY25 | 76.9% | -4.8% | -1.6% | 4.1% |
| FY26 | 76.8% | -3.6% | -1.9% | 5.7% |

- 營業虧損由 FY23 USD -235M 收斂至 FY26 USD -121M，營業利益率連續三年改善。
- Q4 FY26 GAAP 營業損益 USD -3.4M (前年同季 USD -30.9M)，已接近損益平衡。
- 毛利率微幅下滑約 0.8 個百分點 (FY24 78.0% → FY26 76.8%)，同時 Cost of Revenue 增速 (FY26 +25.8%) 與營收增速接近，暫無明顯結構性壓力。
- ROE (FY26, 淨損 / 平均股東權益): -2.9%。ROIC (稅前估算，營業損益 / 平均投入資本): 約 -3.1%。兩者皆為負值，ROIC 尚未覆蓋資本成本。
- SBC 佔營收: FY23 27.5%、FY24 24.3%、FY25 24.7%、FY26 24.5%，高位持平。SBC 是 GAAP 虧損的主要驅動因素之一。

## Cashflow & balance sheet

**現金流 (USD M)**

| 指標 | FY23 | FY24 | FY25 | FY26 |
|---|---|---|---|---|
| 營運現金流 (OCF) | 462.3 | 779.8 | 972.5 | 1,129.7 |
| 資本支出 (Capex) | -128.7 | -194.9 | -245.8 | -350.5 |
| 自由現金流 (FCF = OCF - Capex) | 333.6 | 585.0 | 726.7 | 779.1 |
| FCF margin | 20.6% | 27.0% | 27.2% | 23.2% |
| SBC | 444.8 | 527.7 | 661.4 | 821.9 |
| FCF - SBC | -111.2 | 57.3 | 65.3 | -42.8 |

- FCF / NI: FY26 淨利為負 (USD -63.2M)，比率不具意義，改以 OCF / 營收 (33.7%) 與 FCF - SBC 衡量現金品質。
- 季度 FCF 走勢 (USD M): 2025-10 季 413.3 → 2026-01 季 169.1 → 2026-04 季 136.0 → 2026-07 季 60.8。連續三季下滑，主因是 Q4 Capex 跳升至 USD 218.5M (前一季 USD 62.1M)。Q4 OCF 為 USD 279.3M，仍穩健，但 FCF 轉弱需要追蹤。
- 營運資金: 應收帳款 FY26 USD 1,149.1M (YoY +15.8%)，遞延收入 USD 2,480.5M (YoY +20.7%)。遞延收入成長快於營收，代表訂閱預收款保持強勁。

**資產負債表 (USD M，FY26 年底 2026-07-31)**
- 現金及短期投資: 3,474.2 (現金 928.4 + 短期投資 2,545.8)。
- 總債務 (Total Debt): 1,855.8，其中長期債務 1,696.4、資本租賃 159.5 (長期 94.6 + 短期 64.9)。
- 淨現金 (現金 + 短期投資 - 總債務): 約 +1,618.4，即淨現金部位。
- 注意: yfinance 的 Net Debt 欄位為 768.0，與上列定義不一致。本報告採用 現金 + 短期投資 - 總債務 的定義，兩者差異需以 10-K 核對。
- 流動比率 1.70，速動比率 1.57，營運資金 USD 2,069.9M。
- 負債權益比: 約 71–72% (依 yfinance debtToEquity 71.9)。
- 股東權益 USD 2,598.3M (FY25 為 1,799.3)，每股帳面值 USD 15.94。
- 商譽 + 無形資產 USD 1,432.5M (FY25 為 465.1)，佔總資產約 18%。FY26 商譽增加 USD 800M，主要來自收購。

**收購**
- FY26 收購現金流出 USD 918.1M (Q1 USD 672.8M、Q3 USD 97.3M、Q4 USD 148.0M)。yfinance 未標示被收購標的名稱，無法判斷整合風險與業務貢獻。

## Capital allocation & insider signal

**資本配置**
- Capex 佔營收: FY23 8.0%、FY24 9.0%、FY25 9.2%、FY26 10.5%。Capex 逐年上升，FY26 PPE 購置 USD 277.3M 與資本化軟體 USD 73.2M 合計 USD 350.5M，用途未於 yfinance 中標示。
- 股票回購: 現金流量表無 repurchase 科目，FY23–FY26 未見回購。
- 股利: 無配息 (dividendYield 0.0)。
- 股本稀釋: 流通股數 FY23 147.2M → FY24 152.5M → FY25 158.3M → FY26 163.1M，3 年 CAGR 約 3.5%，FY26 年增 3.0%。SBC 持續發放導致股本持續擴張。
- 股票選擇權行使收入: FY26 USD 63.4M，約 FCF 的 8%，屬小幅現金回饋。

**Insider 活動 (近 6 個月，2026-04-30 至 2026-10-30；資料最新交易日 2026-10-26)**
- 公開市場交易僅見 Sale，共 22 筆，合計 USD 14.69M。無 open-market 買入紀錄。
- 其他: 3 筆 Stock Award (無現金價值)、1 筆選擇權行使 (USD 5.14M 價值，隨即賣出)。
- 賣出主力: Adam Geller USD 8.33M (含 2026-10-12 賣出 25,000 股，約 USD 5.65M)、Kevin Rubin (CFO) USD 2.13M、Robert Schlossman USD 1.94M、Michael Rich USD 1.32M、CEO Jagtar Singh Chaudhry USD 0.91M。
- 規模: 賣出總額 USD 14.69M 相當於市值 USD 41.7B 的約 0.035%，絕對與相對規模都很小。但 「無買入、多位高管持續賣出」 是偏負面的訊號。
- 股權結構: 內部人持股 34.7%、機構持股 53.3%。最大機構 BlackRock 6.07% (2026-06-30 資料，較前期 +15.4%)，Vanguard 合計約 6.8%。空單占流通股 5.6% (空單股數 5.95M)。

## Valuation

以現價 USD 255.8 (yfinance info.currentPrice)，市值 USD 41.7B，EV USD 40.1B。

| 指標 | 數值 | 說明 |
|---|---|---|
| Trailing P/E | n/a | GAAP TTM EPS 為 -0.39 |
| Forward P/E | 45.5x | 前瞻 EPS 5.62 (yfinance forwardEps，為非 GAAP 估計) |
| P/S (TTM) | 12.4x | 市值 / TTM 營收 USD 3.35B |
| EV / Revenue | 12.0x | EV / FY26 營收 |
| EV / EBITDA | 約 225x | EV / FY26 EBITDA USD 178.5M (yfinance info TTM ebitda 僅 USD 43.9M，定義不同，不採用) |
| P/FCF | 約 54x | 市值 / FY26 FCF USD 779M (yfinance info freeCashflow USD 1,075M 對應約 39x，定義不同) |
| P/B | 16.1x | 股價 / 每股帳面值 USD 15.94 |

**與 sector 比較 (estimate)**: yfinance 未提供同業中位數。依一般認知，軟體基礎設施/資安同業前瞻 P/E 約 30–40x、EV/Revenue 約 8–10x、P/FCF 約 30–40x，此為估計值，未經資料源驗證。以此估計，ZS 各項估值倍數高於同業約 20–50%，其中 EV/EBITDA 因利潤率低而失真，參考價值有限。

**分析師觀點**: 45 位分析師，評級 buy。目標價 平均 USD 235.19 / 最高 USD 298 / 最低 USD 164.75。平均目標價低於現價約 8%，最高目標價高於現價約 17%。

**股價位置**: 52 週區間 USD 114.6–337.0，現價位於區間中上段，距 52 週高點 -24%，較 52 週低點 +123%。50 日均線 USD 201.7、200 日均線 USD 166.6，現價高於兩者，近期趨勢偏強，但 52 週股價變動 -20.6%，仍顯著低於年初高點。Beta 0.936。

## Key catalysts

- 上次財報: 2026-09-03 (FY26 Q4)，非 GAAP EPS USD 1.19，預估 USD 1.09，超出 9.2%。
- 下次財報: 2026-11-24 (本報告基準日之後的預定事件)，EPS 預估 USD 1.16。
- 近 8 季 EPS 超預期幅度約 7%–23%，近四季平均約 10.1%，超預期紀錄穩定 (2024-09 季曾達 27%)。
- 公司正式財測 (guidance) 數字: yfinance 無資料，n/a。
- 下季關注點: (1) Q4 Capex 跳升 USD 218.5M 是否延續；(2) FY26 收購的整合與營收貢獻；(3) SBC 佔營收是否下降；(4) GAAP 營業利益是否轉正；(5) 遞延收入成長是否維持 20% 以上。

## Metrics table

| 指標 | 最新值 (FY26 / 2026-07) | YoY 或變化 | Sector 中位數 (estimate) | 判斷 |
|---|---|---|---|---|
| 營收 (USD B) | 3.35 | +25.4% | 約 +15–20% | 高於同業，成長強勁 |
| 毛利率 | 76.8% | -0.2pt (FY25 76.9%) | 約 70–75% | 優於同業，但略降 |
| 營業利益率 (GAAP) | -3.6% | +1.2pt | 約 -5% 至 +5% | 接近損益平衡，改善中 |
| 淨利率 (GAAP) | -1.9% | -0.3pt | 約 0% | 仍虧損 |
| 標準化 EBITDA 利潤率 | 5.7% | +1.6pt | 約 15–25% | 偏低 |
| ROE | -2.9% | 由 FY25 -2.7% | 約 5–10% | 不佳 |
| FCF margin | 23.2% | -4.0pt | 約 20–25% | 尚可 |
| FCF - SBC (USD M) | -42.8 | 由 +65.3 轉負 | 多數同業為正 | 紅旗 |
| SBC / 營收 | 24.5% | -0.2pt | 約 10–15% | 偏高 |
| 流動比率 | 1.70 | 由 FY25 2.01 | 約 1.5–2.5 | 健康 |
| 負債權益比 | 約 72% | 由 FY25 約 100% | 約 30–60% | 中等，淨現金 |
| 淨現金 (USD B) | +1.62 | 由 FY25 約 +1.78 | 不適用 | 穩健 |
| 股本年增率 | +3.0% | FY25 +3.8% | 約 1–2% | 稀釋偏高 |
| Forward P/E | 45.5x | 不適用 | 約 30–40x (estimate) | 偏貴 |
| P/S (TTM) | 12.4x | 不適用 | 約 8–10x (estimate) | 偏貴 |
| P/FCF (FY26) | 約 54x | 不適用 | 約 30–40x (estimate) | 偏貴 |
| 6 個月 insider 淨買入 (USD M) | -14.69 (純賣出) | 無買入 | 不適用 | 偏負面 |

註: sector 中位數全部為估計值，yfinance 未提供，僅供參考，需以 Bloomberg 或同業資料核對。

## Red flags
- SBC 偏高: FY26 SBC USD 821.9M (24.5% 營收)，扣除後 FCF 為 USD -42.8M，股東真實獲利能力仍為負。
- 股本持續稀釋: FY26 流通股增加 3.0%，無回購，稀釋抵銷部分獲利改善。
- 季度 FCF 惡化: 由 Q1 FY26 USD 413.3M 降至 Q4 USD 60.8M，Q4 Capex 跳升 USD 218.5M，需確認是否為一次性支出。
- 收購支出: FY26 收購 USD 918.1M，商譽 +USD 800M，整合與減損風險需追蹤。
- 估值偏高: 前瞻 P/E 45.5x、P/S 12.4x，分析師平均目標價低於現價約 8%。
- Insider 純賣出: 6 個月 USD 14.69M 賣出、無買入，包含 CEO 與 CFO。規模小，但方向一致。
- 資料缺口: 無公司 guidance 數字、無分部營收、無 sector 中位數資料、FY22 缺失無法計算 3–5 年 CAGR。
- 資料不一致 (需留意): (1) info.fulldayPrice 237.5 與 dayLow 254.29 / dayHigh 265.995 不一致，判定為盤後或快取殘值，不採用；(2) yfinance fast_info 價格 257.5 (cnyes 快取，2026-10-29 12:48 UTC) 與 info 價格 255.8 不同，本報告以 info 255.8 為準；(3) info TTM EBITDA USD 43.9M 與 FY26 年度 EBITDA USD 178.5M 定義不同；(4) yfinance Net Debt 欄位 768.0 與現金減總債務定義不一致；(5) GAAP EPS 與非 GAAP EPS (Yahoo earnings_dates) 不可直接比較。
- 資料時效: 最新交易資料為 2026-10-26 (insider)，價格為 2026-10-29 快取，均在 2026-10-30 分析基準日之前或當日。2026-11-24 財報為未來事件。

FUNDAMENTALS REPORT COMPLETE
