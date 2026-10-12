# Fundamentals — TLN (Talen Energy Corporation) as of 2026-10-13

資料說明: 本報告以 2026-10-13 為分析基準日。yfinance 工具在本沙箱以 repo cache 回傳 (source: cache, cached_at 2026-10-12), 未見 2026-10-13 之後的資料。價格以 2026-10-12 收盤價 388.55 (prices/TLN.csv 與 ta snapshot) 為準; info 欄位中的 386.36 為 10-12 盤中快照, 兩者差異屬正常。財報為 FY2025 (12/31) 年報與 2026 Q1、Q2 季報。yfinance 季度/年度資料對部分欄位內部不一致, 已在相關段落標註。

## Executive summary
TLN 目前財務體質偏弱: TTM GAAP 淨利為 -185M USD、淨負債 (net debt) 於 2026-06-30 升至 9,341M USD (2025-12-31 為 6,122M), 流動比率 0.78, 且 Q2 2026 營業現金流轉為 -434M USD, 利息保障倍數 (EBIT/利息) TTM 約 0.75x。估值方面, 以 consensus forward EPS 30.75 計算 forward P/E 約 12.6x 偏低, 但以 trailing 與 EV/EBITDA (約 47x) 衡量則偏高, 估值吸引力高度取決於 2027 年獲利兌現 (forward EPS 與 current-year EPS 22.26 差距大, 需保留)。股價 388.55 位於 52 週區間上段 (-13.6% 距 52 週高點), RSI14 71.5 處於超買區, 技術面與基本面訊號並不一致。

## Revenue & profitability
**營收趨勢**
- 年度營收 (USD M): 2021 1,775 / 2022 2,412 / 2024 2,073 / 2025 2,626。2023 年度資料在 yfinance 缺漏 (DATA_UNAVAILABLE)。
- 2025 YoY: 2,626 / 2,073 - 1 = **+26.7%**。
- 4 年 CAGR (2021-2025): **約 10.3%** (以 1,775 至 2,626 計算)。3 年 CAGR (2022-2025): **約 2.9%**。2022 年為營收高點之一, 2023-2025 年間之資料缺口使中間年度趨勢無法完整判讀。
- 季度營收 (USD M): 2025-06 454 / 2025-09 770 / 2025-12 771 / 2026-03 1,241 / 2026-06 959。Q2 2026 YoY 為 959 / 454 - 1 = **+111%**, 與 info.revenueGrowth 1.112 一致。TTM 營收 3,741 (五個季度中四個季度加總: 959+1,241+771+770)。
- 營收大幅增長的來源未在 yfinance 中標示; 2025 年現金流量表顯示 Purchase of Business 為 -3,793M USD, 可能與併購相關, 但 yfinance 未提供分部 (segment) 資料, 無法拆分來源貢獻。segment mix: n/a。

**獲利能力 (毛利 / 營業 / 淨利)**

| 期間 | 毛利率 | 營業利益率 | 淨利率 |
|---|---|---|---|
| 2024 (FY) | 32.0% (664/2,073) | 8.0% (165/2,073) | 48.1% (998/2,073), 含 1,398M 資產出售效應 |
| 2025 (FY) | 38.1% (1,001/2,626) | 0.6% (16/2,626) | -8.3% (-219/2,626) |
| TTM (至 2026-06) | 42.1% (1,575/3,741) | 12.5% (以季度 Operating Income 加總 469/3,741), 但 info.operatingMargins = -4.8% | -4.9% (-185/3,741), 與 info.profitMargins 一致 |

- 毛利率由 2021 年 13.6% (241/1,775) 持續改善至 TTM 42.1%, 趨勢正向。
- 營業利益率在 TTM 口徑上存在衝突: 季度 Operating Income 加總為正 (469M), 但 info.operatingMargins 為 -4.8%。原因未在資料中說明, 需以 10-Q 原文核對。
- 2025 年 Special Income Charges 為 +34M, Total Unusual Items -72M, 非經常項目對淨利影響有限; 2025 年淨利為負主要是營業面與利息費用共同造成 (利息 2025 年 302M, 2026 Q2 單季 214M)。

**ROE / ROIC**
- ROE: -12.8% (info.returnOnEquity)。ROA: 0.9%。
- ROIC: yfinance 未提供。粗估 2025 年 NOPAT (EBIT 136 × (1-21%) ≈ 107) / 平均 invested capital (2025 年末 7,904) ≈ 1.4%, 僅供參考, 標註為 estimate。

## Cashflow & balance sheet
**現金流品質**
- 2025 年 OCF 704M, Capex 206M, FCF 498M, FCF margin 19.0% (498/2,626)。
- FCF / NI: 2025 年淨利為負 (-219M), 比率 **n/a** (不具意義)。
- 季度 TTM (2025-09 至 2026-06): OCF = 489+280+461-434 = **796M** (與 info.operatingCashflow 796M 一致); Capex = 65+40+69+178 = 352M; FCF = 424+240+392-612 = **444M** (FCF margin 11.9%)。
- **衝突**: info.freeCashflow 為 1,262M, 明顯高於 TTM OCF 796M 減去季度 Capex 後之 444M, 無法以 yfinance 內部資料解釋, 本報告以季度加總值 444M 為準。
- Q2 2026 OCF 為 -434M, 單季 FCF -612M, 是近期現金流品質的主要紅旗; yfinance 未揭露營運資金變動細節, 原因需以 10-Q 確認。

**資產負債表 (2026-06-30 為最新季)**

| 項目 | 2025-12-31 | 2026-03-31 | 2026-06-30 |
|---|---|---|---|
| Cash & equivalents (M) | 689 | 1,025 | 231 |
| Total debt (M) | 6,811 | 6,807 | 9,572 |
| Net debt (M) | 6,122 | 5,782 | 9,341 |
| Stockholders equity (M) | 1,093 | 1,073 | 1,616 |
| Current assets (M) | 1,349 | 1,509 | 1,028 |
| Current liabilities (M) | 1,050 | 1,210 | 1,316 |

- 流動比率 (current ratio): 2026-06 為 1,028/1,316 = **0.78** (與 info.currentRatio 0.781 一致); 2025-12 為 1.28。
- 負債權益比 (debt/equity): 2026-06 為 9,572/1,616 = **5.9x** (info.debtToEquity 為 584%, 一致)。
- 現金: 2026-06 僅 231M, 較 2026-03 下降 794M。
- 總債務自 2024 年末 3,004M 升至 2026-06 的 9,572M, 約增加 3.2 倍。
- 利息保障: 季度 EBIT 加總 TTM 375M / 利息 TTM 499M (214+119+99+67) ≈ **0.75x**。2026-06 單季 EBIT 85M / 利息 214M ≈ 0.40x。
- Net debt / EBITDA: 以季度 EBITDA 加總 770M 計算約 **12.1x**; 以 info.ebitda 582M 計算約 16.1x。yfinance EBITDA 口徑不一致, 以區間表述。

## Capital allocation & insider signal
**資本配置**
- 股利: 無 (dividendRate n/a, payoutRatio 0)。
- 買回: 2024 年 1,958M (大規模), 2025 年 103M, 2026 Q1 100M、Q2 198M (TTM 約 298M)。
- 2026 年 Q2 買回 198M 同時期 OCF 為負, 買回由 Q2 資產負債表 (現金 1,025 → 231, 債務 +2,765M) 支應的推論成立, 但需以 10-Q 確認資金來源。
- 股本: 2025-12 45.7M 股 → 2026-06 47.9M 股 (+4.8%); 股東權益同期由 1,093M 升至 1,616M。資料顯示有股權增加, 但 yfinance 未揭露發行明細; 與 Q2 買回同時存在, 需確認。
- Capex: 2024 189M / 2025 206M / TTM 352M, 2025 年 Capex 占營收 7.8%, TTM 占 9.4%, 呈上升趨勢。

**內部人與大股東訊號 (6 個月窗口: 2026-04-13 至 2026-10-13)**
- 公開市場買入: 無。
- 公開市場賣出: Director Gizman I. Abbas 於 2026-06-15 賣出 2,600 股, 價格 380.00, 金額約 988K USD。
- 其他 2026-05-22 與 2026-07-15 紀錄 (CEO McFarland 354,865 股、CFO Muller 62,862 股等) 無交易金額 (Value = null), 性質 (授予、歸屬或持股申報) 在 yfinance 中未標示, 本報告不計入淨買賣。
- 淨買賣: 約 -0.99M USD vs 市值 18.27B USD, 占比約 0.005%, 規模可忽略。
- 歷史大股東: Rubric Capital Management (>10% 股東) 於 2024-12 出售約 4.89M 股 (約 1.0B USD, 價格 204.35); 2025-06 再出售 388,530 股 (約 114M USD, 價格 288.55-298.14)。2025-03 董事 Horton 買入 1,000 股 (約 191K USD)。
- 持股結構: 內部人持股 1.38%; 機構持股 "102.8%" (超過 100%, 屬資料口徑問題, 不可直接採用); 機構數 809。
- 空單: 最新 short interest 2.50M 股 (yfinance dateShortInterest 對應 2026-09 下旬), 占流通股 (floatShares 38.1M) 約 5.94%, short ratio 3.0 日。前一報告期為 2.44M 股, 小幅增加。

## Valuation
**價格基準**: 388.55 (2026-10-12 收盤, ta/prices cache)。市值 18.27B USD (info, 47.3M 股口徑)。企業價值 EV 27.5B USD (info, 與市值 + Q2 net debt 9.34B 吻合)。

| 倍數 | 數值 | 說明 |
|---|---|---|
| Trailing P/E | n/a | trailing EPS -4.13, 不具意義 |
| Forward P/E | 12.6x | 386.36 / forwardEps 30.75 |
| Current-year P/E | 17.4x | priceEpsCurrentYear 17.35 (epsCurrentYear 22.26) |
| EV/EBITDA | 47.3x | info.enterpriseToEbitda, 以 ebitda 582M 計 |
| EV/EBITDA (季度 TTM) | 約 35.7x | EV 27.5B / 季度 EBITDA 加總 770M |
| EV/Revenue | 7.35x | info.enterpriseToRevenue |
| P/S (trailing) | 4.89x | info.priceToSalesTrailing12Months |
| P/FCF | 約 41x (季度 TTM FCF 444M) / 約 14.5x (info FCF 1,262M) | 兩者衝突, 以前者為保守值 |
| P/B | 11.45x | bookValue 33.74 / 股 |

- 與 sector 比較 (estimate, 非來自工具資料, 僅供參考): 美國 IPP 板塊 forward P/E 中位數約 15-18x; EV/EBITDA 中位數約 11-13x; P/S 中位數約 2-3x; P/B 約 1.5-2.5x。TLN 的 forward P/E 低於估計中位數, 但 EV/EBITDA、P/S、P/B 皆明顯高於估計中位數, 估值結論不一致。
- 分析師: 17 位, recommendationMean 1.59 (buy)。目標價平均 455.65、中位 449、最高 560、最低 307。相對 388.55 之隱含上行約 +17.3% (平均目標價)。

## Key catalysts
- **下一次財報**: 2026-11-04 (earningsTimestampStart), 本季 (Q3 2026) EPS consensus 7.37。
- **上一次財報**: 2026-08-05, adjusted EPS 2.37, 相較 consensus 3.39 **未達預期 -29.98%**。前幾季: 2026-05-05 4.38 vs 4.26 (+2.9%); 2026-02-26 4.38 vs 4.33 (+1.2%); 2025-11-05 3.29 vs 3.67 (-10.3%)。
- **注意**: 季度 GAAP diluted EPS 與 earnings_dates 的 adjusted EPS 口徑不同 (例: 2026-06 季 GAAP diluted EPS -2.00, 淨利 -92M)。
- **Guidance**: yfinance 未提供管理層指引, guidance: n/a。
- **Segment shifts**: 分部資料 n/a。info 僅描述公司擁有約 13.1 GW 發電資產, 燃料含核能、天然氣、煤與油。
- **資本結構事件**: 2026 年 Q2 債務大幅增加 (較 2026-03 增加 2,765M), 後續再融資與利息支出 (2026 Q2 單季 214M) 為觀察重點。
- **技術面參考**: 52 週區間 279.77-449.84; MA50 322.9; MA200 351.7; ATR14 17.2 (約 4.4%); 20 日年化波動 55%; beta 1.617。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 (FY2025, USD M) | 2,626 | +26.7% | 成長約 3-5% | 優於板塊 (併購驅動) |
| 營收 CAGR (2021-2025) | 10.3% | n/a | 約 3-5% | 優於板塊, 但波動大 |
| 毛利率 (TTM) | 42.1% | 2025 FY 38.1% | 約 30-40% | 中上 |
| 營業利益率 (TTM, 季度加總) | 12.5% (info: -4.8%) | 2025 FY 0.6% | 約 10-15% | 口徑衝突, 待核對 |
| 淨利率 (TTM) | -4.9% | 2025 FY -8.3% | 約 5-10% | 偏弱 |
| ROE | -12.8% | n/a | 約 8-10% | 偏弱 |
| ROIC | 約 1.4% (粗估) | n/a | 約 6-8% | 偏弱 |
| FCF margin (TTM, 季度) | 11.9% | 2025 FY 19.0% | 約 10-15% | 中性, Q2 轉負 |
| FCF / NI | n/a (淨利為負) | n/a | 約 0.9-1.2 | 無法評估 |
| 流動比率 (2026-06) | 0.78 | 2025-12 1.28 | 約 1.0-1.2 | 偏弱 |
| 負債權益比 (2026-06) | 5.9x | 2024 末 2.2x (3,004/1,387) | 約 1.5-2.0x | 明顯偏高 |
| 淨負債 (2026-06, USD M) | 9,341 | 2025-06 2,937 | n/a | 快速惡化 |
| 淨負債 / EBITDA (TTM) | 約 12.1x (季度) / 16.1x (info) | n/a | 約 4-5x | 明顯偏高 |
| 利息保障 (EBIT/利息, TTM) | 約 0.75x | n/a | 約 3-5x | 紅旗 |
| 股利殖利率 | 0% | n/a | 約 2-4% | 無股利 |
| 買回 (TTM, USD M) | 約 298 | 2025 FY 103 | n/a | 規模小於 2024 |
| Capex / 營收 (TTM) | 9.4% | 2025 FY 7.8% | 約 8-12% | 中性 |
| 內部人淨買賣 (6 個月) | 約 -0.99M USD (僅一筆公開市場賣出) | n/a | n/a | 占市值 0.005%, 可忽略 |
| Forward P/E | 12.6x | n/a | 約 15-18x | 偏低 (依賴 forward EPS) |
| EV/EBITDA | 47.3x (info) | n/a | 約 11-13x | 明顯偏高 |
| P/S (trailing) | 4.89x | n/a | 約 2-3x | 偏高 |
| P/B | 11.45x | n/a | 約 1.5-2.5x | 偏高 |
| 分析師平均目標價 | 455.65 (隱含 +17.3%) | n/a | n/a | 共識偏多 |
| 空單占流通股 | 5.94% | 最新 2.50M 股, 前期 2.44M 股 | n/a | 中性偏高 |

註: "Sector median (estimate)" 為分析師依一般 IPP 板塊經驗之粗估值, 非來自工具資料, 僅作方向性參考。

## Red flags
- **利息保障倍數低於 1x**: TTM EBIT 約 375M 無法覆蓋 TTM 利息 499M, 2026-06 單季 EBIT 僅 85M 對上利息 214M。
- **債務快速攀升**: 總債務由 2024 末 3,004M 升至 2026-06 的 9,572M; 淨負債 9,341M, 淨負債/EBITDA 約 12x 以上。
- **流動性收緊**: 現金由 2026-03 的 1,025M 降至 231M; 流動比率 0.78。
- **現金流轉負**: 2026 Q2 OCF -434M, 單季 FCF -612M。
- **GAAP 獲利為負**: TTM 淨利 -185M, 2026 Q2 淨損 -92M; ROE -12.8%。
- **季度 EPS 未達預期**: 2026-08-05 adjusted EPS 2.37 vs 3.39 (-29.98%)。
- **資料內部衝突**: (1) TTM 營業利益率 info -4.8% vs 季度加總 +12.5%; (2) info FCF 1,262M vs TTM 季度 FCF 444M; (3) forward EPS 30.75 vs current-year EPS 22.26; (4) 機構持股合計 102.8%; (5) 買回 198M (Q2 2026) 與股本增加 (+4.8%) 同時出現。以上需以 10-Q/10-K 原文核對後再使用。
- **大股東歷史大額出售**: Rubric Capital 2024-12 與 2025-06 合計出售約 1.1B USD。
- **估值對獲利假設高度敏感**: forward P/E 12.6x 是以 forward EPS 30.75 計; 若 2027 年獲利未達成, 估值優勢消失, 而 EV/EBITDA 已達 35-47x。
- **資料缺口**: 2023 年財報、分部營收、管理層指引、ROIC 原始值皆為 DATA_UNAVAILABLE 或 n/a。

FUNDAMENTALS REPORT COMPLETE
