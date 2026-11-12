# Fundamentals — MP as of 2026-11-13

資料來源: `pipeline/tools/yf` 即時 feed 連線失敗 (ConnectionError), 全部欄位改由 repo cache (`prices/yf/MP.json`, cached_at 2026-11-12T15:06 UTC) 提供, 即 source: cache。cache 內 `_misses` 為空。最新財報季為 2026-09-30 (Q3 2026), 最近一次財報日 2026-11-05。未使用 2026-11-13 之後的資料。單位: USD 以 B/M 標示, 無 TWD/KRW 金額。

## Executive summary
MP Materials 目前仍是營收快速放大但尚未獲利的稀土材料公司: 最近四季 (Q4'25 至 Q3'26, TTM) 營收約 US$399.5M, TTM GAAP 淨損 US$-39.6M, TTM 自由現金流 US$-537.3M, 且 2026 年 CapEx 大幅擴張。財務健康度評為「偏弱、需依賴現有現金支應」: 現金及短期投資 US$1,337.9M, 流動比率 6.75x, 但以 TTM 現金消耗速度推算約 2.3 年 (自行推算)。估值上 forward P/E 77.5x、P/S (TTM) 約 16x、P/B 3.3x, 估值已大幅反映未來成長預期; 16 位分析師均值目標價 US$67.5 高於現價 US$36.165 約 87% (資料呈現, 非投資建議)。

## Revenue & profitability

**營收 (Total Revenue, USD M, 年度)**

| 年度 | Total Revenue | YoY | 毛利率 | 營業利益率 | 淨利率 |
|---|---|---|---|---|---|
| 2022 | 527.5 | n/a | 79.0% | 63.5% | 54.8% |
| 2023 | 253.4 | -52.0% | 41.4% | 1.4% | 9.6% |
| 2024 | 203.9 | -19.5% | -32.8% | -80.3% | -32.1% |
| 2025 | 224.4 | +10.0% | -25.7% | -64.7% | -38.3% |

- 3 年 CAGR (2022-2025): **-24.8%**。2021 年度資料為 n/a, 無法計算 4-5 年 CAGR。
- 2026 季度 Total Revenue: Q4'25 52.7 / Q1'26 90.6 / Q2'26 108.5 / Q3'26 147.7 (M USD)。Q3'26 對比 Q3'25 (53.6) YoY 約 +175.6%; Operating Revenue 口徑 Q3'26 119.6 vs Q3'25 52.8, YoY 約 +126.5%。
- TTM 營收 (季度加總) US$399.5M, 相較 2025 全年 US$224.4M 明顯放大。

**季度獲利能力 (M USD)**

| 季度 | Total Revenue | Gross Profit | 毛利率 | Operating Income | 營業利益率 | Net Income | Diluted EPS |
|---|---|---|---|---|---|---|---|
| Q3'25 | 53.6 | -17.4 | -32.5% | -65.6 | -122% | -41.8 | -0.24 |
| Q4'25 | 52.7 | -17.0 | -32.3% | -2.6 | -4.9% | +9.4 | +0.05 |
| Q1'26 | 90.6 | -15.7 | -17.3% | -18.2 | -20.1% | -8.0 | -0.04 |
| Q2'26 | 108.5 | 0.8 | 0.7% | -17.6 | -16.2% | -20.3 | -0.11 |
| Q3'26 | 147.7 | 25.9 | 17.5% | -7.9 | -5.3% | -20.7 | -0.12 |

- 毛利率由 2026 Q1 的 -17.3% 連續改善至 Q3 的 17.5%, 但仍為正值僅一季; 營業利益率 Q3 收斂至 -5.3%。
- TTM (Q4'25-Q3'26): Operating Income US$-46.3M (營業利益率約 -11.6%), Net Income US$-39.6M (淨利率約 -9.9%)。
- 2026 Q3 Operating Expense 33.8M, 其中 SG&A 38.0M、R&D 1.9M。R&D 歷史 (Q3'25 19.0M 對 Q3'26 1.9M) 波動大, 需確認口徑。
- ROE (TTM): 約 -2.0% (NI -39.6M / 股東權益 1,950.1M, 自行計算); info 欄位 returnOnEquity = -1.67%。
- ROIC (近似, 自行計算, 稅前): TTM 營業利益 -46.3M / (總負債 936.3M + 股東權益 1,950.1M - 現金與短期投資 1,337.9M) ≈ -3.0%。
- 利息費用 TTM 約 US$38.8M (Q4'25 9.9 / Q1'26 9.8 / Q2'26 9.7 / Q3'26 9.4), 目前 EBIT 為負, 利息保障倍數 n/a。

**業務組合 (segment mix)**: longBusinessSummary 描述兩大部門 Materials (Mountain Pass 礦場與加工) 與 Magnetics (NdPr metal 與 NdFeB 永磁)。工具未提供分部營收與獲利, 分部佔比: DATA_UNAVAILABLE。

## Cashflow & balance sheet

**現金流 (USD M)**

| 期間 | Operating CF | CapEx | Free Cash Flow | FCF 占營收 | FCF / NI |
|---|---|---|---|---|---|
| 2022 (年) | 343.5 | 326.6 | 16.9 | 3.2% | 0.06 (NI 289.0) |
| 2023 (年) | 62.7 | 261.9 | -199.2 | -78.6% | n/m (NI 24.3) |
| 2024 (年) | 13.3 | 186.4 | -173.1 | -84.9% | n/m (NI -65.4) |
| 2025 (年) | -155.8 | 172.4 | -328.1 | -146.2% | n/m (NI -85.9) |
| TTM (Q4'25-Q3'26, 季度加總) | -54.7 | 482.6 | -537.3 | -134.5% | n/m (NI -39.6) |
| 9M 2026 (Q1-Q3) | -7.8 | 420.2 | -428.0 | n/a | n/m |

- 2026 季度 CapEx: Q4'25 62.4 / Q1'26 77.4 / Q2'26 230.3 / Q3'26 112.5 (M USD), 2026 前三季 CapEx 合計 420.2M, 已超過 2025 全年 172.4M。
- TTM OCF (-54.7M) 與 info operatingCashflow (-54.6M) 一致。info freeCashflow 為 -410.4M, 與季度加總 -537.3M 不符, 本報告採季度加總口徑。
- FCF/NI 比值在 NI 為負時無經濟意義 (n/m), 健康度標準 (>0.9) 不適用; 現金流品質判定為「未達標」。

**資產負債表 (2026-09-30, M USD; 季度資料)**

| 項目 | 2026-09 | 2026-06 | 2025-12 |
|---|---|---|---|
| 現金及等價物 | 260.3 | 429.1 | 1,166.0 |
| 現金 + 短期投資 | 1,337.9 | 1,452.6 | 1,830.3 |
| 總負債 (Total Debt) | 936.3 | 934.6 | 1,007.2 |
| Net Debt (工具值, 僅扣現金及等價物) | 675.9 | 505.5 | n/a |
| Net Debt (扣現金+短期投資, 自行計算) | -401.6 (淨現金) | -518.0 (淨現金) | -823.1 (淨現金) |
| 流動資產 | 1,654.8 | 1,745.4 | 2,165.8 |
| 流動負債 | 245.0 | 183.5 | 299.0 |
| 股東權益 | 1,950.1 | 1,957.3 | 1,978.8 |
| 淨 PP&E | 1,757.9 | 1,608.6 | 1,383.0 |

- 流動比率 6.75x (1,654.8 / 245.0, 與 info currentRatio 6.755 一致); quick ratio (info) 5.96x。
- Debt/Equity: 936.3 / 1,950.1 ≈ 0.48x (自行計算); info debtToEquity 欄位為 41.6 (百分比口徑, 即約 0.42x), 與 BS 不完全一致, 以 BS 計算為準。info totalDebt 983.6M 亦與季度 BS 936.3M 不同。
- 現金安全墊: 以 Q1-Q3 2026 FCF 平均年化 (-428.0 / 3 × 4 ≈ -570.7M) 推算, 現金+短期投資 1,337.9M 可支應約 2.3 年 (自行推算, 未計入外部融資或資產處分)。
- 總負債自 2025-12 的 1,007.2M 降至 2026-09 的 936.3M; 長期負債 (Long Term Debt) 2026-09 為 936.3M, 短期負債 (Current Debt) 2026 Q3 為 n/a (Q1 為 67.5M)。
- 存貨 176.1M, 應收帳款 (Accounts Receivable) 64.1M (2026-09)。

## Capital allocation & insider signal

- **CapEx 趨勢**: 2022 326.6 → 2023 261.9 → 2024 186.4 → 2025 172.4 (M USD), 2026 前三季 420.2M 明顯反轉向上, 擴產或建設投入加速 (依現金流數字判讀, 工具未提供專案說明)。
- **股東權益與股本**: 2025 年發行股權 (Issuance of Capital Stock) US$1,046.9M, 2025 年 Net Common Stock Issuance 716.4M (淨額); 2024 年買回股票 US$225.1M, 2025 年買回 US$31.1M。流通股 (ordinary shares) 由 2024-12 的 163.2M 增至 2025-12 的 177.4M (+8.7%), 2026-09 為 178.2M。股本稀釋已發生。
- **股利**: 無股利 (dividendYield 0.0, trailingAnnualDividendRate 0.0), 股利覆蓋率 n/a。
- **庫藏股**: 2026 季度無買回紀錄 (2026-09 n/a); 2025 Q4 買回 US$31.1M。
- **內部人交易 (近 6 個月)**: 工具 insider 欄位回傳空陣列 (cache 內 insider = []), 無法確認是否真的無交易或為資料缺漏 → **DATA_UNAVAILABLE**。insidersPercentHeld 為 19.6%, 規模上內部人持股比例高, 但無交易資料無法判讀淨買賣。
- **機構持股**: institutionsPercentHeld 79.2% (institutionsCount 968); 前十大持有人 (2026-06-30 / 2026-09-30 申報): Hancock Prospecting 8.34%、BlackRock 8.27%、State Street 4.36%、Vanguard (兩實體合計約 7.7%)、D.E. Shaw 3.27% (季度增 +85.1%)、Morgan Stanley 2.68%、UBS 2.62%、Van Eck 2.56%、Invesco 1.98%。
- **空頭**: sharesShort 35.77M, 占流動股 (float) 21.8%, short ratio 6.75 日 (2026-10-30 申報)。空頭部位占比偏高。

## Valuation

價格基準: info regularMarketPrice US$36.165 (2026-11-12 15:05 UTC, 前收 US$36.73, 日變動 -1.54%)。fast_info 的 last_price 為 US$36.965 (cnyes feed), 與 info 不一致; 本報告採 info 價格, 因其與 info marketCap (US$6,447.1M, = 36.165 × 178.27M 股) 一致。

| 指標 | 數值 | 計算/來源 |
|---|---|---|
| 市值 (Market Cap) | US$6.45B | info marketCap 6,447.1M |
| 企業價值 (EV) | US$6.61B | info enterpriseValue 6,607.1M |
| Trailing P/E | n/a (TTM EPS -0.20 為負) | info trailingEps |
| Forward P/E | 77.5x | info forwardPE, forwardEps 0.4665 |
| P/S (TTM) | 約 16.1x | 6,447 / TTM 營收 399.5 (自行計算); info priceToSalesTrailing12Months 12.4x 以 518.5M 營收計 |
| P/B | 3.31x | info priceToBook (與 6,447 / 1,950.1 一致) |
| EV/EBITDA | info 106.0x (EBITDA 62.3M); 季度 EBITDA TTM 107.4M 計約 61.5x | 口徑不一致, 見紅旗 |
| P/FCF | n/a (FCF 為負) | — |
| 52 週高 / 低 | US$76.80 / US$31.90 | info |
| 現價相對 52 週高 | -52.9% | 自行計算 |
| 50 日均線 / 200 日均線 | US$44.58 / US$53.98 | info (現價低於兩者, 分別 -18.9% / -33.0%) |
| 52 週漲跌幅 | -36.2% (S&P 500 同期 +13.1%) | info 52WeekChange / SandP52WeekChange |
| Beta | 2.11 | info beta |
| 分析師目標價 (mean / median / high / low) | US$67.50 / US$65.50 / US$100.00 / US$40.00 | info, 16 位分析師 |
| 分析師建議 | strong_buy (recommendationMean 1.26); 0m: 5 Strong Buy / 14 Buy / 0 Hold / 0 Sell | info, cache rec_summary |
| 同業中位數 (sector median) | DATA_UNAVAILABLE | 工具未提供同業估值中位數 |

估值解讀 (不構成交易建議): 獲利為負的情況下, 估值完全依賴遠期盈餘與營收成長, forward P/E 77.5x 與 EV/EBITDA 百倍級別對應的是尚未穩定的獲利結構。TTM P/S 約 16x 相對於仍為負毛利與負營業利益的營收品質, 估值溢價明顯。

## Key catalysts

- **最近一次財報**: 2026-11-05 (earnings_dates 記錄日期, 對應 Q3 2026)。工具 earnings_dates 記錄 Reported EPS 0.04 vs 預估 -0.01 (surprise +515.8%); 但同期 GAAP diluted EPS 為 -0.12 (quarterly_fin)。兩者差異推測為調整後 (adjusted) EPS, 工具未明示。
- **下一次財報**: 2027-02-25 (EPS 預估 -0.06), 為 earnings_dates 表內排程日期, 屬工具提供之預定值, 未經公司正式確認。
- **公司指引 (guidance)**: DATA_UNAVAILABLE (工具未提供管理層指引與數字)。
- **分部變化**: 工具未提供分部資料, DATA_UNAVAILABLE。
- **資本結構/融資事件**: 2025 年發行股權 US$1,046.9M 與 2026 年 CapEx 擴張是最重要的資金面事件; 2026 Q3 總負債與現金變動可觀察, 但工具未提供個別交易說明。
- **分析師目標價範圍**: US$40-100, 中位數 US$65.5。
- **資料時效**: 所有資料截至 2026-11-12 (cache), 早於 as-of 2026-11-13, 無未來資料混入。

## Metrics table

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 TTM (USD M) | 399.5 (Q3'26 TTM) | TTM 相較 2025 全年 224.4 約 +78% (口徑比較, 非 YoY) | DATA_UNAVAILABLE | 成長強 |
| Q3'26 營收 (USD M) | 147.7 | +175.6% YoY (vs 53.6) | DATA_UNAVAILABLE | 成長強 |
| 3Y 營收 CAGR (2022-2025) | -24.8% | — | DATA_UNAVAILABLE | 弱 |
| 毛利率 (Q3'26) | 17.5% | 由 Q3'25 -32.5% 改善 | DATA_UNAVAILABLE | 改善中, 仍偏低 |
| 營業利益率 (TTM) | -11.6% | 2025 全年 -64.7% | DATA_UNAVAILABLE | 改善中, 仍為負 |
| 淨利率 (TTM) | -9.9% | 2025 全年 -38.3% | DATA_UNAVAILABLE | 虧損 |
| ROE (TTM) | -2.0% | info -1.67% | DATA_UNAVAILABLE | 弱 |
| ROIC (近似, 稅前) | -3.0% | — | DATA_UNAVAILABLE | 弱 |
| 營業現金流 TTM (USD M) | -54.7 | 2025 全年 -155.8 | DATA_UNAVAILABLE | 改善但為負 |
| FCF TTM (USD M) | -537.3 | 2025 全年 -328.1 | DATA_UNAVAILABLE | 弱 |
| FCF 占營收 (TTM) | -134.5% | — | DATA_UNAVAILABLE | 弱 |
| FCF / NI | n/m (NI 為負) | — | DATA_UNAVAILABLE | 不適用 |
| 現金 + 短期投資 (USD M) | 1,337.9 | 2025-12 1,830.3 (-26.9%) | DATA_UNAVAILABLE | 尚可, 逐季下降 |
| Net Debt (扣現金+STI, USD M) | -401.6 (淨現金) | 2025-12 淨現金 -823.1 | DATA_UNAVAILABLE | 淨現金但縮減 |
| 總負債 (USD M) | 936.3 | 2025-12 1,007.2 (-7.0%) | DATA_UNAVAILABLE | 中性 |
| Debt / Equity | 0.48x | — | DATA_UNAVAILABLE | 中性 |
| 流動比率 | 6.75x | — | DATA_UNAVAILABLE | 強 |
| CapEx TTM (USD M) | 482.6 | 2025 全年 172.4 | DATA_UNAVAILABLE | 大幅擴張 |
| 股利殖利率 | 0.0% | — | DATA_UNAVAILABLE | n/a |
| 股本 (流通股, M) | 178.3 | 2024-12 163.2 → +9.2% (2025 年增 +8.7%) | DATA_UNAVAILABLE | 稀釋 |
| 內部人淨買賣 (6 個月) | DATA_UNAVAILABLE | — | DATA_UNAVAILABLE | 無法判讀 |
| 市值 (USD B) | 6.45 | — | DATA_UNAVAILABLE | — |
| Trailing P/E | n/a | — | DATA_UNAVAILABLE | 不適用 (虧損) |
| Forward P/E | 77.5x | — | DATA_UNAVAILABLE | 偏高 |
| EV/EBITDA | 106.0x (info) / 約 61.5x (季度 EBITDA) | — | DATA_UNAVAILABLE | 偏高 |
| P/S (TTM) | 約 16.1x (自行) / 12.4x (info) | — | DATA_UNAVAILABLE | 偏高 |
| P/B | 3.31x | — | DATA_UNAVAILABLE | 偏高 |
| P/FCF | n/a | — | DATA_UNAVAILABLE | 不適用 |
| Beta | 2.11 | — | DATA_UNAVAILABLE | 高波動 |
| 空頭占流動股 | 21.8% | — | DATA_UNAVAILABLE | 偏高 |
| 分析師目標價均值 vs 現價 | US$67.5 vs US$36.165 (+86.6%) | — | DATA_UNAVAILABLE | 分析師看多 |

## Red flags
- **獲利與現金流皆為負**: TTM NI US$-39.6M, TTM FCF US$-537.3M, 且 2026 年前三季 FCF 已達 US$-428.0M, 持續依賴現有現金與外部融資。
- **毛利率曾為負**: 2024、2025 全年毛利率分別 -32.8%、-25.7%; 2026 Q1 仍為 -17.3%, 僅 Q2 (0.7%) 與 Q3 (17.5%) 轉正。
- **CapEx 大幅擴張**: 2026 前三季 CapEx US$420.2M 已超過 2025 全年 172.4M, 投資回收期未知。
- **股權稀釋**: 2025 年發行股權 US$1,046.9M, 流通股 +8.7%。
- **估值溢價**: forward P/E 77.5x、P/B 3.3x, 現價低於 50 日與 200 日均線, 52 週跌幅 -36.2%, 波動 (Beta 2.11) 與空頭占比 (21.8%) 偏高。
- **資料一致性問題 (需下游注意)**:
  - info totalRevenue 518.5M 與季度 TTM 營收 399.5M 不符; info grossMargins 46.5% 與季度 TTM 毛利約 -6.0M 不符; info EBITDA 62.3M 與季度 EBITDA TTM 107.4M 不符。本報告以季度財報加總為主。
  - fast_info last_price 36.965 與 info regularMarketPrice 36.165 不一致, 本報告採 36.165。
  - earnings_dates 的 Reported EPS 0.04 與季度 GAAP diluted EPS -0.12 不一致, 推測為 adjusted EPS。
  - Total Debt: info 983.6M 與季度 BS 936.3M 不符; info debtToEquity 與 BS 計算值亦不一致。
  - 季度 Operating Expense 2025-12 為 -14.4M (負值), R&D 2025-09 19.0M 與 2026-09 1.9M 差異極大, 疑似分類調整, 需確認。
  - info freeCashflow -410.4M 與季度 FCF 加總 -537.3M 不符。
- **內部人交易資料缺失**: insider 回傳空陣列, 無法判定 6 個月內部人淨買賣 (DATA_UNAVAILABLE)。
- **財報與指引資料缺失**: 管理層指引、分部營收與同業估值中位數均為 DATA_UNAVAILABLE。
- **資料來源為 cache**: 即時 feed 連線失敗, 所有數字來自 2026-11-12 15:06 UTC 的快取, 非即時數據。

FUNDAMENTALS REPORT COMPLETE
