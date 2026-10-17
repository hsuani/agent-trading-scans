# Fundamentals — ALAB as of 2026-10-18

## Executive summary
Astera Labs (ALAB) 財務體質極佳: 2026-06-30 現金及短期投資 1,253.0M USD、無有效負債 (info totalDebt 44.4M), 流動比率 10.05x, TTM 營收 1,202.0M USD (YoY 約 +104%), TTM 營業利益率約 22.7%。然而估值極端: trailing P/E 140.8x, forward P/E 44.6x (依 forwardEps 6.40), EV/Sales 40.3x, EV/EBITDA 169.5x, 且 過去六個月 (2026-04-18 至 2026-10-18) 共有約 628M USD 的內部人 (以共同創辦人 CEO/President 為主) 出售。結論: 財務健康度強, 成長與獲利動能明確, 但估值對任何營運不如預期的情境都極度敏感; 在財務面 (不含技術與市場情緒) 評估為「體質佳、估值昂貴」。

資料時點說明: 價格為最近交易日 2026-10-16 收盤 (依 regularMarketTime 推算; 本次 cache 寫入時間 2026-10-17 10:32 UTC, 2026-10-18 為週日), 財報最新至 2026-06-30 季 (FY2026 Q2, 2026-08-04 公布), 內部人交易最新至 2026-10-01。未見超過 {DATE} 的財務資料。資料來源為 cache fallback (source: cache), 屬預期行為。

## Revenue & profitability

**營收成長**
- 年度營收 (M USD): FY2022 79.9 → FY2023 115.8 → FY2024 396.3 → FY2025 852.5。
- FY2025 YoY +115.1%; FY2023-2025 2 年 CAGR 約 +171%; FY2022-2025 3 年 CAGR 約 +120%。
- 季度營收 (M USD): 2025-06 quarter 191.9 → 2025-09 230.6 → 2025-12 270.6 → 2026-03 308.4 → 2026-06 392.4。
- 2026-06 季 YoY +104.5% (vs 191.9); QoQ +27.2%; 連續四季 QoQ 成長率為 +20.2% / +17.3% / +14.0% / +27.2%。
- TTM 營收 = 1,201.9M (與 info totalRevenue 1,201.9M 相符)。
- 業務組合: info.longBusinessSummary 列出的產品線為 PCIe/CXL smart DSP retimers 與 cable modules、Ethernet smart cable modules、CXL memory connectivity controllers、smart fabric switches, 以及 COSMOS 軟體。**分產品線營收占比: DATA_UNAVAILABLE** (工具未提供 segment revenue)。

**毛利 / 營業利益 / 淨利率趨勢**

| 期間 | 毛利率 | 營業利益率 | 淨利率 (GAAP) |
|---|---|---|---|
| FY2022 | 73.5% | -75.3% | -73.0% |
| FY2023 | 68.9% | -25.5% | -22.7% |
| FY2024 | 76.4% | -29.3% | -21.0% |
| FY2025 | 75.7% | 20.3% | 25.7% |
| 2025-06 Q | 75.9% | 20.7% | 26.7% |
| 2025-09 Q | 76.2% | 24.0% | 39.5% |
| 2025-12 Q | 75.6% | 24.8% | 16.6% |
| 2026-03 Q | 76.2% | 20.0% | 26.0% |
| 2026-06 Q | 73.3% | 22.7% | 39.0% |

- 毛利率在 2025-2026 維持 73-76%, 2026-06 季降至 73.3% (QoQ 約 -2.9pp), 需追蹤是否為產品組合或存貨調整影響。
- 2026-06 季淨利率 39.0% 含一次性稅務利益: pretax 102.8M, 淨利 153.1M, 差額約 +50.3M (yfinance Tax Provision = -50.3M)。若以 pretax 計, 淨利率約 26.2%。2026-03 季亦有 +6.9M 稅務利益。
- R&D 費用: 2026-06 季 135.9M (營收占比 34.6%), 2025-06 季 66.7M (34.8%)。SG&A 62.4M (15.9%)。
- 利息收入: FY2025 44.7M; 2026-06 季 13.6M, 為淨利的重要組成, 不屬核心營運。

**ROE / ROIC**
- ROE 25.8%, ROA 10.7% (info, TTM 口徑)。
- ROIC 為估算值: TTM EBIT 273.4M × (1 - 25.57%) = NOPAT 約 203.5M; 以 (股東權益 1,725.7M + 有息負債 44.4M) 為分母, 約 11.5%。若扣除超額現金 (現金及 STI 1,253.0M) 後的營運資本基礎, 約 39%。(兩者皆為本報告計算值, 非工具直接提供)

**獲利品質**
- 2025 年 GAAP 淨利 219.1M 中, 利息收入 44.7M 約占 20%; 2025 年稅務幾乎為 0 (Tax Provision -1.0M)。

## Cashflow & balance sheet

**現金流**

| 指標 | FY2024 | FY2025 | TTM (至 2026-06) |
|---|---|---|---|
| 營業現金流 (OCF) | 136.7M | 319.3M | 335.8M |
| 資本支出 (Capex) | -34.2M | -37.5M | -59.1M |
| FCF (OCF - Capex) | 102.4M | 281.8M | 276.7M |
| FCF margin | 25.8% | 33.1% | 23.0% |
| FCF / NI | n/m (NI 為負) | 1.29x | 0.75x |
| OCF / NI | n/m | 1.46x | 0.91x |

- TTM FCF 276.7M 為季度 CF 表加總 (Q3'25 65.9 + Q4'25 76.6 + Q1'26 67.0 + Q2'26 67.2), 與 quarterly_cf 的 Free Cash Flow 列一致。
- FCF / NI TTM 0.75x 低於 0.9 門檻, 主因 TTM NI 369.5M 含 Q2 稅務利益與利息收入。
- **2026-06 季營運資本大幅吸收現金**: 營運資本變動 -142.5M (Q1 為 -59.1M), 該季 OCF 87.7M 低於淨利 153.1M。
- 2026-06 季 SBC 為 64.0M, 若扣除 SBC, TTM FCF 約 81.7M (276.7 - 195.0), 占營收約 6.8%。

**資產負債表 (2026-06-30)**
- 現金及現金等價物 111.5M; 短期投資 1,141.5M; 合計 1,253.0M (info totalCash 1,252.96M, 每股 7.22 USD)。
- 有息負債: 季度資產負債表未列 Total Debt (null); FY2025 Total Debt 4.1M (為 capital lease); info totalDebt 為 44.4M。兩者口徑不一致, 報告以 info 44.4M 保守計算。
- 淨現金 (保守計算) = 1,253.0 - 44.4 = 1,208.6M, 約占市值 2.4%。
- 流動比率 10.05x (流動資產 1,651.9M / 流動負債 164.3M); 速動比率 9.16x (info)。
- 負債/權益 (info debtToEquity 2.574, 單位為 %) 即約 0.03x。
- 總資產 1,931.5M, 股東權益 1,725.7M (2026-06)。
- **營運資本警訊**: 應收帳款 192.5M (2026-03 為 134.8M, +43% QoQ); DSO 估算約 44 天 (2025-12 約 28 天); 存貨 113.8M (2026-03 為 60.2M, +89% QoQ), 存貨天數估算約 99 天 (2025-12 約 82 天)。其他流動資產中含 Taxes Receivable 60.3M。
- 2026-03 季有 65.0M 企業併購現金支出, 2026-06 季商譽及無形資產 91.6M (併購對象 DATA_UNAVAILABLE)。

## Capital allocation & insider signal

**資本配置**
- 股利: 無 (dividendYield 0)。
- 買回: FY2024 1.1M, FY2025 0。沒有實質買回計畫。
- 融資: FY2024 普通股發行 672.2M (大型股權融資), FY2025 無。
- Capex 趨勢: FY2024 34.2M (營收占比 8.6%) → FY2025 37.5M (4.4%) → TTM 59.1M (4.9%); 2026-06 季 20.5M 較前季 7.6M 明顯加速, 顯示產能/基礎建設投資正在擴張。
- 股數增加: 期末 Ordinary Shares 2024 162.0M → 2025 170.2M (+5.1%) → 2026-06 173.5M (1H26 +1.9%); 主因為 SBC。
- SBC: FY2025 160.0M (營收占比 18.8%); TTM 195.0M (占 TTM 營收 16.2%); 為主要稀釋來源。

**內部人交易 (6 個月: 2026-04-18 至 2026-10-18)**
- 公開市場出售: 26 筆, 合計 2,424,675 股, 估計金額 628.0M USD, 約占市值 49.6B 的 1.27%, 約占流通股 (173.5M) 的 1.4%。
- 主要出售人:
  - GAJENDRA SANJAY (共同創辦人、President/COO): 1,136,966 股, 292.0M USD
  - MOHAN JITENDRA (共同創辦人、CEO): 801,857 股, 169.5M USD
  - ALBA MANUEL (董事, 間接持有): 366,000 股, 132.5M USD
  - DYCKERHOFF STEFAN A (董事): 87,493 股, 24.4M USD
  - MAZZARA PHILIP (General Counsel): 21,673 股, 5.8M USD
- 2026-08-17 CEO 與 President 各出售 90,630 股, 價格區間 333.60-352.11 USD, 數量完全相同, 疑似平行執行的計畫性出售。工具未提供 10b5-1 標記, 無法確認。
- 2026-05-22 Gajendra 有 226,189 股 Stock Gift (價格 0, 非市場交易)。
- 授予 (Stock Award) 合計 55,491 股, 金額約 0.1M, 為董事薪酬性質。
- 結論: 六個月內部人為淨賣出, 規模占市值約 1.3%, 金額大但占比不高; 出售價格區間涵蓋 273-468 USD, 現價 285.82 低於 7 月與 8 月的多數成交價。
- 持股: 內部人合計持有 10.32%, 機構持有 75.69% (機構數 1,334)。

## Valuation

| 指標 | 數值 | 計算 / 來源 |
|---|---|---|
| 價格 | 285.82 USD | regularMarketPrice (2026-10-16 收盤) |
| 市值 | 49.59B USD | info marketCap |
| 企業價值 EV | 48.38B USD | info enterpriseValue |
| Trailing P/E | 140.8x | 285.82 / TTM EPS 2.03 |
| Forward P/E | 44.6x | 285.82 / forwardEps 6.40 |
| FY2026 P/E (當年度 EPS 4.03) | 70.9x | priceEpsCurrentYear |
| EV / EBITDA (TTM 285.4M) | 169.5x | info enterpriseToEbitda |
| EV / Sales (TTM) | 40.3x | info enterpriseToRevenue |
| P / Sales (TTM) | 41.3x | info priceToSalesTrailing12Months |
| P / FCF (TTM FCF 276.7M) | 約 179x | 49.59B / 276.7M (本報告計算) |
| P / B | 28.7x | info priceToBook |

- 分析師: 22 位, 平均評級 1.88 (Buy); Strong Buy 7 / Buy 11 / Hold 8 / Sell 0。目標價: 平均 391.77, 中位數 425, 最高 500, 最低 190。以平均目標價計算潛在空間約 +37%, 以中位數約 +49%。(此為分析師共識數字, 不構成交易建議)
- 股價位置: 52 週區間 97.89-499.48, 現價距 52 週高點 -42.8%; 50 日均線 315.33, 200 日均線 249.81; 最近一日 -5.35% (前收 301.98)。
- Beta 3.69 (極高波動)。
- 估值與同業比較: 工具未提供 sector median, 下列為估計值, 非工具資料: 半導體 (大型) forward P/E 約 30-35x, EV/Sales 約 8-12x, EV/EBITDA 約 25-30x, P/FCF 約 30-40x。ALAB 各指標皆遠高於此估計區間, 溢價主要反映高成長 (TTM 營收 +100% 以上) 與 AI 連接需求預期。

## Key catalysts
- 下次財報: 2026-11-03 (earnings_dates; isEarningsDateEstimate = False), Q3 FY2026 EPS 一致預估 1.19 (non-GAAP 口徑)。
- 近期財報紀錄: 過去 11 季 EPS 全數超出預期。最近一季 (2026-08-04) 報告 EPS 0.80 vs 預估 0.69 (+15.6%); 2026-05 季 0.61 vs 0.54 (+13.5%); 2026-02 季 0.58 vs 0.51 (+12.6%)。(報告 EPS 為工具之 non-GAAP 口徑; 同季 GAAP 稀釋 EPS 為 0.83。)
- FY2026 EPS 一致預估 4.03 (priceEpsCurrentYear 70.86x 為價格除以此數); 隱含 Q4 約 1.43 (依 Q1 0.61 + Q2 0.80 + Q3 1.19 推算)。
- 公司指引 (guidance) 具體數字: DATA_UNAVAILABLE (工具無此欄位)。
- 分產品線或客戶集中度: DATA_UNAVAILABLE。
- 併購: 2026-03 季 65.0M 現金併購, 對象與效果 DATA_UNAVAILABLE。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 TTM (M USD) | 1,201.9 | 2026-06 季 YoY +104.5% | n/a | 高速成長 |
| 營收 FY2025 (M USD) | 852.5 | +115.1% | n/a | 高速成長 |
| 毛利率 (2026-06 Q) | 73.3% | 2025-06 Q 75.9% (-2.6pp) | 約 55-60% (估計) | 優於同業, 略降需追蹤 |
| 營業利益率 TTM | 約 22.7% (2026-06 Q) | 2025-06 Q 20.7% (+2.0pp) | 約 20-25% (估計) | 合理 |
| 淨利率 TTM (GAAP) | 30.7% (info profitMargins, 含稅務利益與利息收入) | 數據不可直接比較 | 約 15-20% (估計) | 偏高, 含一次性因素 |
| ROE | 25.8% | n/a | 約 15-20% (估計) | 優 |
| ROIC (估算) | 約 11.5% (含現金基礎) | n/a | 約 10-15% (估計) | 中等 |
| FCF margin TTM | 23.0% | FY2025 33.1% | 約 20-25% (估計) | 合理 |
| FCF / NI TTM | 0.75x | FY2025 1.29x | >0.9 為健康 | 偏弱 |
| SBC / 營收 TTM | 16.2% | FY2025 18.8% | 約 5-10% (估計) | 偏高 |
| 淨現金 | 約 1,208.6M | n/a | n/a | 優 |
| 流動比率 | 10.05x | n/a | 約 2-3x (估計) | 極佳 |
| 負債/權益 | 約 0.03x (info 2.574%) | n/a | 約 0.3-0.5x (估計) | 極佳 |
| Capex / 營收 TTM | 4.9% | FY2024 8.6% → FY2025 4.4% | n/a | 投資擴張中 |
| 股息 / 買回 | 無 / 無 | n/a | n/a | 無資本回饋 |
| 股數變化 1H26 | +1.9% (170.2M → 173.5M) | 2025 年 +5.1% | 約 0-2% (估計) | 稀釋中 |
| 內部人淨賣出 (6 個月) | 628.0M USD (約 1.3% 市值) | n/a | n/a | 偏空訊號 |
| Trailing P/E | 140.8x | n/a | 約 25-35x (估計) | 極度昂貴 |
| Forward P/E | 44.6x | n/a | 約 30-35x (估計) | 偏貴 |
| EV / EBITDA TTM | 169.5x | n/a | 約 25-30x (估計) | 極度昂貴 |
| EV / Sales TTM | 40.3x | n/a | 約 8-12x (估計) | 極度昂貴 |
| P / FCF TTM | 約 179x | n/a | 約 30-40x (估計) | 極度昂貴 |
| Beta | 3.69 | n/a | 約 1.0-1.5 (估計) | 波動極高 |
| 分析師平均目標價 | 391.77 (+37%) | n/a | n/a | 共識偏多 |

## Red flags
- 估值極端: EV/Sales 40x、trailing P/E 141x、EV/EBITDA 170x。任何成長不如預期或毛利率下滑, 估值壓縮風險都很大。
- 內部人大額出售: 6 個月約 628M USD, 主要為共同創辦人 CEO 與 President; 2026-08-17 兩人同日同量出售, 需確認是否為 10b5-1 計畫 (工具無此欄位)。
- 2026-06 季獲利品質: 淨利 153.1M 高於 pretax 102.8M, 含約 50M 稅務利益; 淨利率 39% 不具可持續性。
- 營運資本惡化: 2026-06 季應收 +43%、存貨 +89% QoQ, 營運資本吸收 142.5M, OCF 低於淨利。
- SBC 高: TTM 195M (16% 營收), 扣除 SBC 後 FCF 約 82M, 股數持續稀釋。
- 毛利率 2026-06 季降至 73.3% (QoQ -2.9pp)。
- 併購: 2026-03 季 65M 併購支出, 商譽與無形資產升至 91.6M, 併購內容未揭露。
- 資料不一致 (已標記, 未自行修正):
  - info totalDebt 44.4M vs 季度 BS 為 null, FY2025 BS 為 4.1M。
  - info freeCashflow 91.9M vs 由 CF 表推算 TTM FCF 276.7M。
  - info operatingCashflow 335.7M 與 CF 表推算 335.8M 一致。
- 治理風險分數 (yfinance overallRisk 7, shareHolderRightsRisk 8, 滿分 10 制): 偏高。
- Beta 3.69, 52 週價格振幅 98-499 USD, 極高波動。
- 工具覆蓋缺口: 分產品線營收、公司指引、客戶集中度皆為 DATA_UNAVAILABLE。

## 工具使用備註
- 本次任務指定的 kinds (statements / ratings / holders) 並非 `pipeline/tools/yf.py` 的合法參數。改用等效 kinds: financials + quarterly_fin + balance_sheet + quarterly_bs + cashflow + quarterly_cf (statements), rec_summary (ratings), major_holders (holders), insider, earnings_dates, info。
- 指令路徑為 `python3 pipeline/tools/yf.py ALAB <kind>`。所有資料皆為 source: cache。

FUNDAMENTALS REPORT COMPLETE
