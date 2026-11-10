# Fundamentals — AMD as of 2026-11-10

資料來源: `pipeline/tools/yf` (repo cache `prices/yf/AMD.json`, refreshed 2026-11-10 14:46:54 UTC, 無 cache miss)。金額單位: USD, 以 B (十億美元) / M (百萬美元) 標示, 不使用 億。價格為盤中報價 (2026-11-10 14:46 UTC, 美東約 09:46), 非收盤價。

## Executive summary
AMD 的財務體質明顯改善: FY2025 營收 34.64B USD (YoY +34.3%), Q3 2026 營收 13.38B USD (YoY +44.7%), 期末現金及短期投資 15.78B USD 大於總債務 8.92B USD, 流動比率 2.73。然而估值極度昂貴, trailing P/E 110.8x、EV/EBITDA 74.3x、P/S 18.7x, 只有 forward P/E 29.3x 與分析師一致預期 (strong_buy, 48 位) 能支撐, 估值依賴 EPS 大幅成長兌現。Q3 2026 GAAP 盈餘品質與營運資金 (inventory +56.8% YoY) 及新增 4.73B USD 長期債需追蹤; 6 個月內內部人淨賣出 248.8M USD (占市值約 0.03%), 無買進。

## Revenue & profitability

**營收成長**
- FY2022 23.60B → FY2023 22.68B (-3.9%) → FY2024 25.79B (+13.7%) → FY2025 34.64B USD (+34.3%)。
- 3 年 CAGR (FY2022–FY2025): 約 13.6%。yfinance 無 FY2021 數據, 5 年 CAGR 為 n/a。
- 最近季度 YoY: Q3 2026 13.38B vs Q3 2025 9.25B, 約 +44.7%。TTM 營收 45.44B USD (與 info totalRevenue 45.44B 吻合)。
- 業務分部: 依 longBusinessSummary 為 Data Center、Client and Gaming、Embedded 三大分部。分部營收與毛利 yfinance 未提供, 標記 DATA_UNAVAILABLE。

**獲利結構 (由 financials / quarterly_fin 手算)**

| 年度 | 毛利率 | 營業利益率 | 淨利率 | R&D / 營收 | SG&A / 營收 |
|---|---|---|---|---|---|
| FY2022 | 44.9% | 5.4% | 5.6% | 21.2% | 9.9% |
| FY2023 | 46.1% | 1.8% | 3.8% | 25.9% | 10.2% |
| FY2024 | 49.4% | 7.4% | 6.4% | 25.0% | 10.6% |
| FY2025 | 49.5% | 10.7% | 12.5% | 23.4% | 12.0% |
| TTM (Q4'25–Q3'26) | 53.7% | 17.7% | 16.8% | — | — |

- 毛利率趨勢: 由 FY2022 44.9% 提升至 TTM 53.7%, 近兩季分別為 Q2 2026 53.8%、Q3 2026 53.9%。
- 營業利益率: Q3 2026 營業利益 2.83B USD, 營業利益率 21.2%, YoY 約 +123%。TTM 17.7%。
- FY2025 淨利 4.335B USD (continuing ops 4.269B USD), 其中 Total Unusual Items +366M USD (Gain on sale of security), 正常化淨利 (Normalized Income) 約 3.997B USD。
- **ROE**: info returnOnEquity 11.96%; 手算 TTM 淨利 7.62B / 平均股東權益 64.59B = 11.8%。FY2025 手算 7.2%。
- **ROIC (估計)**: TTM 營業利益 8.05B × (1 − 25.6%) / 投入資本 61.53B (Q3 2026 總債務 + 股東權益 − 現金與短期投資) ≈ 9.7%。此為手算估計, 非 yfinance 欄位。
- **EPS**: FY2025 diluted GAAP EPS 2.65 (4.335B / 1.636B shares, 手算吻合); FY2024 1.00; FY2023 0.53; FY2022 0.84。TTM diluted EPS 季度加總 4.60, info trailingEps 4.68 (兩者差異 0.08, 以 info 為準並標註)。
- Q3 2026 diluted GAAP EPS 1.46 (YoY 約 +95%, 相對 Q3 2025 0.75)。非 GAAP EPS (earnings_dates) 2.09, 高於分析師預估 1.95 (+7.44%)。

## Cashflow & balance sheet

**現金流量 (cashflow / quarterly_cf)**

| 指標 | FY2024 | FY2025 | TTM (Q4'25–Q3'26) | Q3 2026 |
|---|---|---|---|---|
| Operating CF (B USD) | 3.04 | 7.71 | 9.12 | 1.20 |
| Capex (B USD) | 0.64 | 0.97 | 2.07 | 0.65 |
| Free CF (B USD) | 2.41 | 6.74 | 7.06 | 0.55 |
| FCF margin | 9.3% | 19.4% | 15.5% | 4.1% |
| FCF / NI | 1.47 | 1.55 | 0.93 | 0.23 |
| SBC (B USD) | 1.41 | 1.64 | 2.00 | 0.52 |

- FY2025 FCF/NI 1.55, 遠高於 0.9 健康門檻; TTM 降至 0.93, 剛好在門檻附近; Q3 2026 僅 0.23。
- Q3 2026 營運現金流 1.20B USD 低於淨利 2.43B USD, 主因營運資金變動 −3.36B USD: Inventory 變動 −3.00B, Receivables 變動 −1.93B, 但 Accounts Payable 大幅增加。
- info freeCashflow 7.357B 與本報告手算 TTM FCF 7.056B 不同 (yfinance 定義差異), 本報告以手算為準。
- FCF − SBC: FY2025 5.10B USD (SBC 占營收 4.7%), 扣除 SBC 後 FCF 利潤率仍有 14.7%。

**資產負債表 (quarterly_bs, Q3 2026 = 2026-09-30)**

| 指標 | Q3 2026 | Q3 2025 | 變化 |
|---|---|---|---|
| Cash & 短期投資 (B USD) | 15.78 | 7.24 | +118% |
| Total Debt (B USD) | 8.92 | 3.87 | +130% |
| Long-term debt (B USD) | 7.08 | 2.35 | +202% |
| Net cash (B USD) | +6.86 | +3.37 | 仍為淨現金 |
| Current ratio | 2.72 | 2.31 | 改善 |
| Debt / Equity (book) | 13.0% | 6.4% | 槓桿上升 |
| Inventory (B USD) | 11.46 | 7.31 | +56.8% |
| Accounts Receivable (B USD) | 9.21 | 6.20 | +48.5% |
| Accounts Payable (B USD) | 7.76 | 3.48 | +122.7% |
| Goodwill (B USD) | 25.47 | 25.08 | 占總資產 26.9% |
| Total Assets (B USD) | 94.81 | 76.89 | +23.3% |
| Stockholders' Equity (B USD) | 68.39 | 60.79 | +12.5% |

- 2026 年 Q3 單季新增長期債 4.73B USD (cashflow Issuance of Debt 4,726M), 同期另償還 875M 流動債務。利息費用由 Q2 37M 升至 Q3 62M。
- 淨現金仍為正, 流動性充足; 但總債務在一季內增加一倍以上, 屬於資本結構的實質改變。
- info debtToEquity 13.469 為百分比單位 (即 13.5%), 非倍數。
- info totalDebt 9.21B (含租賃等) 與報表 Q3 total debt 8.92B 不同, 本報告以報表為準。

## Capital allocation & insider signal

**資本配置**
- 股利: 無配息 (dividendYield 0, payoutRatio 0)。
- 買回 (Repurchase of Capital Stock): FY2022 4.11B / FY2023 1.41B / FY2024 1.59B / FY2025 1.92B USD; TTM 2.22B USD, 其中 Q3 2026 單季 1.50B USD 為近期大幅提升。
- Capex: FY2022 0.45B → FY2025 0.97B (YoY +53%), 占營收 2.8%; TTM 2.07B 占營收 4.5%; Q3 2026 0.65B 為 Q3 2025 0.26B 的 2.5 倍。
- 股本稀釋: 買回未能抵銷 SBC。Q3 2026 稀釋後平均股數 1,661M, 較 Q3 2025 1,641M 增加 +1.2%; 基本股數 1,640M, YoY +0.7%。
- 資本配置總結: 買回 + 增加資本支出 + 4.73B 新債, 同時 FCF 單季下滑。

**內部人交易 (insider, 2026-05-10 至 2026-11-10 六個月內)**
- 公開市場賣出 (Text 為 "Sale at price") 共 17 筆, 合計 523,034 股, 金額 248.76M USD。
- 買進 (open-market purchase): 0 筆。
- 其他 (期權轉換 / 贈與 / 授予) 未計入淨買賣。

| 內部人 | 職位 | 6 個月賣出筆數 | 股數 | 金額 (M USD) |
|---|---|---|---|---|
| Lisa T. Su | Chair, President & CEO | 4 | 360,000 | 168.6 |
| Forrest E. Norrod | EVP & GM, Data Center | 4 | 71,271 | 34.4 |
| Mark D. Papermaster | CTO & EVP | 4 | 48,180 | 23.9 |
| Paul Darren Grasby | EVP, Chief Sales Officer | 1 | 15,000 | 7.7 |
| Jean X. Hu | EVP, CFO | 1 | 15,000 | 7.1 |
| Nora M. Denzel | Director | 1 | 10,447 | 5.5 |
| Ava M. Hahn | Director | 2 | 3,136 | 1.5 |

- 相對市值: 248.76M / 850.45B = 約 0.03%, 規模小。
- 解讀: 全部為賣出, 且集中於 CEO 與主要高階主管; 數據中無法確認是否為 10b5-1 預定計畫, 須以 SEC Form 4 進一步確認。
- 內部人持股比例 heldPercentInsiders 0.42%。

**機構持股**: heldPercentInstitutions 75.0% (5,218 家)。前五大: BlackRock 9.16%, Vanguard 6.49%, State Street 4.53%, Invesco 3.24%, JPMorgan 2.46% (以 2026-06-30 報告為主)。

**做空**: shortPercentOfFloat 2.33% (38.1M 股), 空方回補天數 (short ratio) 1.74 天, 空方壓力低。

## Valuation

**絕對估值 (info 與手算並列, 以 USD 計)**

| 指標 | 數值 | 手算/來源 | 說明 |
|---|---|---|---|
| 價格 | 518.54 | info regularMarketPrice | 盤中; fast_info 508.58 (cache 14:44) 為較早快照, 以 info 為準 |
| 市值 | 850.45B | info marketCap = 518.54 × 1,640.1M 股 | 手算吻合 |
| 企業價值 EV | 827.55B | info enterpriseValue | 手算 (市值 + 債 − 現金) = 843.9B, 差異來自 yfinance 現金定義 |
| Trailing P/E | 110.8x | info (518.54 / 4.68) | 以 GAAP TTM EPS 計 |
| Forward P/E | 29.3x | info (518.54 / forwardEps 17.69) | forwardEps 期間未標示, 推測為下一完整財年 |
| FY2026 EPS 估計 | 8.08 | info epsCurrentYear | P/E 約 64.1x |
| PEG | 0.40 | info pegRatio | |
| EV/EBITDA | 74.3x | info (827.55B / 11.14B) | 手算 EBITDA = TTM 營業利益 8.05B + D&A 3.05B = 11.10B, EV/EBITDA 約 76x |
| P/S (TTM) | 18.7x | info (850.45B / 45.44B) | 手算吻合 |
| P/FCF (TTM) | 120.5x | 手算 (850.45B / 7.056B) | info 以 7.357B 計為 115.6x |
| P/B | 12.4x | info (518.54 / BVPS 41.70) | |

**與同業中位數比較**: yfinance 未提供產業中位數, 以下為估計值 (大型半導體股的一般區間, 非工具數據):
- Trailing P/E 估計 35–45x → AMD 110.8x 明顯溢價。
- Forward P/E 估計 25–30x → AMD 29.3x 約相當。
- EV/EBITDA 估計 20–30x → AMD 74x 明顯溢價。
- P/S 估計 8–10x → AMD 18.7x 溢價。

**分析師預期**: 48 位分析師, recommendationMean 1.38 (strong_buy), 近四個月 Strong Buy + Buy 占大多數, 無 Sell。targetMeanPrice 657.49 (+26.8%), targetMedianPrice 650.00, 最高 1,250.00, 最低 525.00 (高於現價)。

**價格位置**: 現價 518.54 較 50 日均線 547.67 低 5.3%, 較 200 日均線 417.22 高 24.3%, 較 52 週高點 658.52 低 21.3%, 52 週低點 188.22 (52 週漲幅 +114%)。beta 2.54, 屬高波動。

## Key catalysts
- **下次財報**: yfinance earningsTimestamp 指向 2027-02-02 (isEarningsDateEstimate = true), 該季 EPS 預估 2.93 (非 GAAP)。注意: 2026-11-03 為上一季 (Q3 2026) 財報日, 已公布 EPS 2.09。
- **最近一季**: Q3 2026 非 GAAP EPS 2.09 vs 預估 1.95 (beat +7.44%)。近 8 季 EPS 7 季超預期, 僅 Q2 2025 小幅未達 (−3.48%)。Q4 2025 beat 高達 +15.53%。
- **指引 (guidance)**: 工具輸出未包含公司官方季度指引文字, 標記 DATA_UNAVAILABLE。
- **分部變化**: 分部營收與毛利未提供, 標記 DATA_UNAVAILABLE。可由 Q3 營收 YoY +44.7% 與毛利率穩定於 53–54% 間接推論成長動能, 但無法拆分 Data Center 與 Client/Gaming 貢獻。
- **結構性事件**: Q3 2026 新增 4.73B USD 長期債與 1.50B USD 買回, 屬資本配置變化; 用途未在數據中說明。

## Metrics table

金額單位: USD B/M。「Sector median (estimate)」為分析師估計值, 非工具數據。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| Revenue, FY2025 (B USD) | 34.64 | +34.3% | n/a | 強 |
| Revenue, TTM (B USD) | 45.44 | Q3 YoY +44.7% | n/a | 強 |
| Revenue 3Y CAGR FY22–25 | 13.6% | — | 估計 10–12% | 優於同業 |
| Gross margin, TTM | 53.7% | FY25 49.5% vs FY24 49.4% | 估計 55–60% | 略低, 穩定 |
| Operating margin, TTM | 17.7% | FY25 10.7% vs FY24 7.4% | 估計 20% | 改善中 |
| Net margin, TTM | 16.8% | FY25 12.5% vs FY24 6.4% | 估計 15% | 尚可 |
| ROE, TTM | 11.8% | FY25 7.2% | 估計 15–20% | 偏低 |
| ROIC, TTM (手算) | 9.7% | — | 估計 12% | 偏低 |
| Diluted EPS, FY2025 | 2.65 | FY24 1.00 (+165%) | n/a | 強 |
| Operating CF, TTM (B USD) | 9.12 | FY25 7.71 | n/a | 強 |
| FCF, TTM (B USD) | 7.06 | FY25 6.74 vs FY24 2.41 | n/a | 強 |
| FCF margin, TTM | 15.5% | FY25 19.4% | 估計 15–20% | 中等 |
| FCF / NI, TTM | 0.93 | FY25 1.55; Q3 26 0.23 | >0.9 健康 | 邊緣, Q3 轉弱 |
| Current ratio | 2.73 | Q3 25 2.31 | 估計 2.0 | 健康 |
| Net cash (B USD) | +6.86 | Q3 25 +3.37 | — | 仍為淨現金 |
| Total debt (B USD) | 8.92 | +130% | — | 槓桿上升, 需注意 |
| Debt / Equity (book) | 13.0% | Q3 25 6.4% | 估計 30% | 低 |
| Inventory (B USD) | 11.46 | +56.8% (DIO 約 184 天 vs 166 天) | n/a | 警示 |
| Accounts Receivable (B USD) | 9.21 | +48.5% (DSO 約 63 天 vs 61 天) | n/a | 留意 |
| Capex, TTM (% revenue) | 4.5% | FY25 2.8% | 估計 5% | 持續增加 |
| Buyback, TTM (B USD) | 2.22 | FY25 1.92 (+21%) | n/a | 中等 |
| Dividend | 無 | — | n/a | 無配息 |
| Diluted shares, Q3 26 (M) | 1,661 | +1.2% YoY | n/a | 仍稀釋 |
| SBC, TTM (% revenue) | 4.4% | FY25 4.7% | n/a | 偏高 |
| Insider net flow, 6M | 賣出 248.8M USD, 0 買進 | 占市值約 0.03% | n/a | 偏負向, 規模小 |
| Trailing P/E | 110.8x | — | 估計 35–45x | 極度昂貴 |
| Forward P/E | 29.3x | — | 估計 25–30x | 接近同業 |
| EV/EBITDA | 74.3x | — | 估計 20–30x | 極度昂貴 |
| P/S (TTM) | 18.7x | — | 估計 8–10x | 昂貴 |
| P/FCF (TTM) | 120.5x | — | 估計 30x | 昂貴 |
| P/B | 12.4x | — | 估計 6–8x | 偏高 |
| Analyst mean target | 657.49 USD (+26.8%) | — | n/a | 偏多 |
| Beta | 2.54 | — | 估計 1.2–1.5 | 高波動 |
| Short % of float | 2.33% | — | n/a | 低 |

## Red flags
- **估值極端**: trailing P/E 110.8x、EV/EBITDA 74.3x、P/FCF 約 120x, 估值完全依賴 forward EPS 成長 (FY2026 EPS 8.08 → forward 17.69) 兌現。
- **Q3 2026 GAAP 盈餘品質**: 稅前淨利 1.87B USD 低於淨利 2.43B USD, 因 tax provision 為 −555M USD (有效稅率約 −30%); 同季 Other Income Expense −902M USD。單季 GAAP EPS 1.46 含一次性項目, 不宜直接外推。
- **營運資金擴張**: Inventory 11.46B USD (QoQ +35.4%, YoY +56.8%), DIO 約 184 天; AP 同期 +122.7% 支撐營運現金流 (Q3 OCF 1.20B vs NI 2.43B)。若 AP 回落, 現金流壓力將顯現。
- **Q3 FCF 大幅下滑**: Q3 2026 FCF 0.55B USD, FCF/NI 0.23, 僅為 TTM 平均的一小部分。
- **負債快速上升**: 單季新增 4.73B USD 長期債, 總債務 YoY +130%, 利息費用 Q3 62M USD (前季 37M)。目前仍為淨現金, 但資本結構趨勢需監控。
- **股本稀釋**: SBC TTM 2.00B USD, 買回 2.22B USD 仍不足以抵銷; 稀釋後股數 YoY +1.2%。
- **內部人持續賣出**: CEO Lisa Su 6 個月內 4 筆賣出共 168.6M USD; 高階主管合計 248.8M USD, 無買進。金額相對市值小, 但方向一致。
- **資料品質**: (a) info grossProfits 25.44B 與季度加總 24.41B 不符; info operatingMargins 21.2% 與季度加總 17.7% 不符, 本報告以季度手算為準; (b) quarterly EBITDA 欄位於 Q3 2026 為 2.70B USD, 低於營業利益加 D&A (3.11B), 定義似為稅前法; (c) fast_info 價格 508.58 與 info 518.54 不一致 (時間差); (d) yfinance 無 FY2021 數據, 5 年 CAGR 無法計算。
- **資料缺口 (DATA_UNAVAILABLE)**: 分部營收與毛利、官方季度/全年指引、產業中位數 (本報告所列為估計)、內部人交易是否為 10b5-1 計畫。
- **資料時點**: 所有財報資料截至 2026-09-30 (Q3 2026), 未見晚於 2026-11-10 之實際財報數據; 2027-02-02 為預估財報日, 非已發生事件。

FUNDAMENTALS REPORT COMPLETE
