# Fundamentals — CBRS (Cerebras Systems Inc.) as of 2026-10-19

資料來源: pipeline/tools/yf (yfinance 快取, 因 live feed 受阻, 報價取自 prices/yf/CBRS.json 快取)。報價時間戳記為 2026-10-17 (regularMarketTime), 該日為週六, 與交易日曆不符, 需以交易所正式收盤價再確認。沒有 2026-10-19 之後的財務或內部人資料; 下一次財報 2026-11-10 尚未發生。

## Executive summary

CBRS 是 2026 年 5 月上市的 AI 推論晶片公司, 營收成長快 (MRQ YoY +74.3%, TTM 營收 680.7M USD), 但仍處於大幅虧損與高資本支出階段: TTM FCF 為 -680.2M USD, 且 2026-06 季 (Q2) 出現 GAAP 每股虧損 -2.98 與 Gross margin 驟降至 14.2%。資產負債表因 IPO 募資而非常強勁 (現金與短期投資 7.92B USD, 總負債 1.49B USD, current ratio 5.83x), 財務上並不急迫。估值面以 forward P/E 約 99.9x、EV/Revenue 34.9x 計算, 明顯高於半導體板塊的估計中位數; 分析師平均目標價 291.6 USD 隱含 +129% 空間, 但過去 6 個月內部人合計賣出約 408M USD, 股價較 52 週高點下跌 67%, 且已跌破 50 日與 200 日均線。

## Revenue & profitability

**營收與成長**
- FY2022 24.6M → FY2023 78.7M → FY2024 290.3M → FY2025 510.0M USD。FY2025 YoY +75.7%; FY2022–FY2025 3 年 CAGR 約 +175% (只有 4 個年度資料點, 無法算 5 年 CAGR)。
- 季度趨勢: 2025-03 季 99.5M, 2025-06 季 103.3M, 2026-03 季 (Q1) 193.4M (YoY +94.4%), 2026-06 季 (Q2) 180.1M (YoY +74.3%, QoQ -6.9%)。Q2 營收首次出現環比下滑, 需確認是否為客戶出貨時點或收入認列造成。
- TTM 營收 680.7M USD (由 H2 2025 + Q1 2026 + Q2 2026 合計推得, 與 yfinance TTM 值一致)。
- 分部 (segment) 資料: n/a。yfinance longBusinessSummary 只描述 AI compute 系統 (晶圓級引擎 + 機櫃 + 軟體), 未提供客戶集中度, 地區或產品線拆分。

**毛利率 (Gross margin)**
- FY2022 11.7% → FY2023 33.5% → FY2024 42.3% → FY2025 39.0%。
- Q1 2026 44.6%, Q2 2026 14.2% (COGS 154.6M, 營收 180.1M, 毛利僅 25.6M)。Q2 毛利率單季崩跌 30 個百分點以上, 工具資料無法解釋原因 (可能為存貨減值, 產品組合, 或一次性成本, 需看 10-Q)。
- TTM gross margin (yfinance) 34.9%。

**營業利益率 (Operating margin)**
- FY2022 -726.5% → FY2023 -170.1% → FY2024 -35.0% → FY2025 -28.6%, 持續改善但仍為大幅虧損。
- Q1 2026 -7.8%; Q2 2026 -265.0% (營業費用 502.8M, 較 Q1 的 101.2M 增加約 5 倍; 其中 R&D 320.2M, SG&A 182.6M)。
- Q2 SBC 為 377.0M USD (約為營收的 2.1 倍), 推測為 IPO 相關的股權獎酬認列, 是營業費用暴增的主要原因。扣除 SBC 後的營業虧損粗估約 -100M USD (推算值, 非工具直接輸出)。

**淨利率與 EPS**
- FY2025 淨利 237.8M USD (淨利率 +46.6%), 但這是由 363.3M USD 的非營業投資處分利益 (Gain on sale of security) 所推動, 營業面仍為虧損。FY2024 淨利率 -166.0%, FY2023 -161.5%。
- Q2 2026 淨利 -450.5M USD (淨利率 -250.2%); Net Income Common Stockholders 為 -901.1M USD, 差額來自 IPO 前優先股相關的分配項目 (Otherunder Preferred Stock Dividend 等), 需以 10-Q 確認。
- Q2 GAAP diluted EPS -2.98, Q1 -0.07, FY2025 diluted +0.42 (受利益影響)。
- 財報日曆 (earnings_dates) 所列的 EPS (2026-06-23 報告值 -0.04 vs 估 -0.15; 2026-08-12 報告值 -0.05 vs 估 -0.18) 與 GAAP 數字口徑不同, 很可能是調整後 (non-GAAP) EPS, 來源未標示。
- trailing EPS -5.14, forward EPS 1.27, 本年度 EPS 估計 -0.47。

**ROE / ROIC (依 yfinance 資料粗估)**
- 股東權益: 2025-12 為 -578.7M USD (負值), 2026-03 為 -194.7M, 2026-06 為 9,154.6M (IPO 後)。FY2025 ROE 不具意義 (分母為負)。
- TTM 淨利 -512.4M / 期末權益 9,154.6M ≈ ROE -5.6% (粗估)。
- TTM 營業利益約 -552M (由 H2 2025 推算), 投入資本 10.07B, 粗估 ROIC ≈ -5.5%。結論: 目前沒有任何有意義的正報酬。

## Cashflow & balance sheet

**現金流品質**
- OCF: FY2022 -164.4M, FY2023 -79.0M, FY2024 +452.0M (主要由營運資金流入 443.5M 驅動, 其中 "Change in Other Working Capital" 為 +678.5M, 不具持續性), FY2025 -10.1M。
- Capex: FY2022 10.5M, FY2023 6.6M, FY2024 23.4M, FY2025 382.7M (為 FY2024 的 16.3 倍), 佔 FY2025 營收 75%。H1 2026 capex 548.9M (Q1 132.0M, Q2 416.9M)。TTM capex 約 746.5M。
- FCF (OCF - capex): FY2024 +428.5M (一次性營運資金受惠), FY2025 -392.8M, Q1 2026 -119.6M, Q2 2026 -476.7M, TTM -680.2M。
- FCF margin: FY2025 -77.0%, TTM -99.9%。
- FCF / NI: FY2025 為負值 (NI 為正但 FCF 為負, 比值不具意義), TTM NI 為負, 比值不具意義。以盈餘品質判斷, FY2025 淨利主要來自非營業利益, OCF 為負, 盈餘品質偏低。
- SBC: FY2023 26.6M, FY2024 58.6M, FY2025 49.8M (9.8% 營收), Q2 2026 377.0M。

**資產負債表 (2026-06-30 季末)**
- 現金及約當現金 6.74B USD; 現金與短期投資合計 7.92B USD (2026-03 為 2.23B)。
- 總負債 2.47B USD (2026-03 為 5.14B; 下降主要應為 IPO 時優先股轉換為普通股), 總債務 (Total debt) 1.49B USD (2026-03 為 1.36B), 其中長期負債 662.6M (含租賃等, 需 10-Q 拆分)。
- 淨現金 (cash + ST investments - total debt) 約 6.43B USD (粗估)。
- 流動比率 (current ratio) 5.83x (2026-03 為 2.51x)。
- 負債權益比 (debt/equity) 約 0.16x (2026-06); 2026-03 因權益為負, 不具意義。
- 營運資金 (working capital) 7.56B USD。存貨 32.7M, 應收帳款 123.4M。
- 流動性評估: 以 Q2 單季 FCF 燃燒速度 (-477M) 估算, 現金可支撐約 16 季; 以 TTM 平均燃燒速度 (-170M/季) 估算約 46 季。兩者都未計入持續上升的 capex 計畫, 僅供參考。

## Capital allocation & insider signal

**資本配置**
- 股利: 無 (dividendYield 0)。
- 回購: FY2025 -38.1M (疑為員工股權獎酬的稅款代扣, 非公開回購), FY2024 -0.1M。
- 股權發行: 2026-03 季優先股發行 1.01B USD 與短期債務 1.00B USD; 2026-06 季普通股發行現金流 6.23B USD (推測為 IPO 募資, 需以 S-1/10-Q 確認)。
- 股數 (Ordinary shares, 資產負債表): 2025-12 與 2026-03 均為 215.1M, 2026-06 為 228.2M (+6.1% 季度增加)。
- 股數資料不一致: info.sharesOutstanding 112.2M、impliedSharesOutstanding 237.6M、floatShares 109.9M、資產負債表 228.2M。yfinance marketCap 30.22B 是以 237.6M 股計算, 本報告採用此值, 但市值數字存在 ±5% 的不確定性。
- 依 capex 與 FCF 趨勢判斷, 公司在 2026 年仍需大量外部資金 (或持續稀釋), 資本配置為成長擴張型, 不是現金回饋型。

**內部人交易 (2026-04-19 至 2026-10-19, 依 yfinance insider 表)**
- 公開市場賣出 (Sale at price) 合計約 408M USD, 約 1.98M 股:
  - 2026-06 (6/25–6/30): 約 20.7M USD, 約 117.5K 股, 價格區間 161–189 USD。
  - 2026-08 (8/14–8/21): 約 245.3M USD, 約 1.17M 股, 價格區間 196–250 USD。其中 Sean Lie 於 8/21 賣出 151.1M USD, Andrew Feldman 於 8/21 賣出 47.3M USD。
  - 2026-09 (9/4–9/29): 約 142.4M USD, 約 0.69M 股, 價格區間 195–213 USD。其中 Dhiraj Mallick 於 9/29 賣出 80.8M USD。
- 董事 (Vassallo、Vishria) 亦有間接持股賣出: 合計約 26.4M USD。
- 公開市場買入: 0 筆。
- 贈與 (Stock Gift) 多筆, 價值為 0, 不計入金額。
- 規模: 408M USD 約佔市值 30.22B 的 1.35%, 約佔自由流通股 (109.9M) 的 1.8%。
- 價格面: 賣出均價約在 196–250 USD, 現價 127.21 USD 較這些成交價低約 35%–49%, 內部人在高點附近持續賣出, 而非在低點買進。
- 另外 2026-05-15 有多筆 Benchmark、Foundation Capital、Vassallo 關聯實體的優先股轉換 (Conversion of derivative security, 轉換價 279.72 USD, 合計約 43.4M 股), 屬 IPO 相關的機械性轉換, 不視為市場賣出; 但這些大股東的成本基礎顯著高於現價, 未來是否有賣壓需留意。
- 持股結構: 內部人持股 9.6%, 機構持股 80.4% (539 家), 機構流通股比重 88.9%。前 10 大機構合計約 46.9%: Eclipse Operations 10.2%、FMR 7.5%、Altimeter 6.4%、Coatue 6.3%、Capital World 3.5%、Morgan Stanley 2.9%、Atreides 2.8%、JPMorgan 2.8%、Tiger Global 2.7%、Vy Capital 1.9%。持股資料為 2026-06-30, pctChange 欄位全部為 1.0, 判定為資料欄位異常, 不作為加減碼依據。
- 做空: 做空股數 14.1M, 佔自由流通股 12.6%, short ratio 2.22 天; 相較上月 (13.3M) 增加 5.9%。

## Valuation

- 現價 127.21 USD (2026-10-17 快取, 前收 142.17, 單日 -10.5%); 盤後 126.70。52 週區間 126.05–386.34 USD, 目前位於 52 週低點附近 (+0.9%)。52 週漲跌 -59.1%, 相對 S&P 500 同期 +13.7%。
- 50 日均線 192.0 USD (現價低於 -33.7%), 200 日均線 206.6 USD (現價低於 -38.4%)。
- 市值 30.22B USD, EV 23.79B USD (EV = 市值 + 總債務 - 現金與短期投資, 數字與 yfinance 一致)。

**倍數**
- Trailing P/E: NM (trailing EPS -5.14)。
- Forward P/E: 99.9x (forward EPS 1.27); 本年度 EPS -0.47, 本年度 P/E NM。
- EV/Revenue (TTM): 34.9x; P/S (TTM): 44.4x。
- EV/EBITDA (TTM): -49.1x, 因 TTM EBITDA 為負, 不具意義。
- P/FCF: NM (TTM FCF 為負)。
- P/B: 3.16x (price/bookValue 40.27 USD/股)。
- 板塊中位數 (估計, 非工具資料): 成熟半導體 forward P/E 約 25–35x、EV/Sales 約 8–12x; AI 基礎設施高成長同業 forward P/E 約 35–60x。CBRS 的 forward P/E 與 EV/Sales 都在這些區間的上緣或以上, 估值仍需高成長兌現。

**分析師共識 (11 位分析師)**
- 評級分布: Strong Buy 3, Buy 8, Hold 0, Sell 0 (近 3 個月共識穩定, 1 個月前有 1 位 Hold)。
- 目標價: 平均 291.6 USD、中位數 300 USD、最高 330 USD、最低 209 USD。相對現價的平均隱含空間 +129%, 最低目標價仍有 +64%。
- 推薦平均值 1.27 (1 為 Strong Buy)。
- 注意: 分析師目標價在股價跌 67% 後仍未下修 (最低 209 USD 仍高於現價 64%), 目標價與市價落差大, 參考價值需保守看待。

## Key catalysts

- 上次財報: 2026-08-12 (Q2 2026); EPS 報告值 -0.05 vs 估 -0.18 (surprise +74.6%)。此為 yfinance 調整後口徑, GAAP 數字為 -2.98。
- 下次財報: 2026-11-10 (earnings_dates 列表所示, 尚未發生; info 的 isEarningsDateEstimate 為 false, 但 info 內 earningsTimestamp 仍指向 2026-08-12, 故日期可信度中等); 分析師估計 EPS -0.14。這將是首份包含 IPO 後完整季度的 Q3 2026 數據 (9 月底季)。
- 內部人賣出集中在 2026-08-14 之後, 與 IPO (約 2026-05-14/15) 約 90 天的鎖定期到期時點接近, 屬推論, 需以 S-1/招股書確認實際鎖定期條款。鎖定期後的持續賣出是短期股價壓力的來源之一。
- 催化劑 (工具資料無法提供): 管理層財測與指引 (guidance) n/a; 客戶集中度 n/a; 訂單積壓 (backlog) n/a; 新產品或新客戶公告 n/a; capex 計畫與資金來源 n/a。需以 10-Q 與公司公告補充。
- 事件面資料: 2026-10-19 之後無任何財務或內部人資料。

## Metrics table

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 (Revenue, FY2025) | 510.0M USD | +75.7% | 成長型半導體估計 +20–40% | 高成長, 但基數低 |
| 營收 (Revenue, TTM) | 680.7M USD | MRQ YoY +74.3% | n/a | 成長強勁 |
| 營收季增 (Q2 2026 QoQ) | 180.1M USD | -6.9% QoQ | n/a | 需追蹤 |
| Gross margin (FY2025) | 39.0% | FY2024 42.3% (-3.3pt) | 成熟半導體 50–60% (估計) | 偏低, 惡化 |
| Gross margin (Q2 2026) | 14.2% | Q1 2026 44.6% | 同上 | 紅旗, 原因不明 |
| Operating margin (FY2025) | -28.6% | FY2024 -35.0% (+6.4pt) | 成熟半導體 20–30% (估計) | 虧損, 改善中 |
| Operating margin (Q2 2026) | -265.0% | Q1 2026 -7.8% | n/a | SBC 驅動, 紅旗 |
| Net margin (FY2025) | +46.6% | FY2024 -166.0% | 同上 | 非營業利益驅動, 盈餘品質低 |
| Net margin (TTM) | -75.3% | n/a | 同上 | 虧損 |
| EPS (trailing) | -5.14 | n/a | n/a | 虧損 |
| EPS (forward) | 1.27 | n/a | n/a | 依賴成長兌現 |
| ROE (TTM, 粗估) | -5.6% | n/a | 半導體 15–25% (估計) | 負值 |
| ROIC (TTM, 粗估) | -5.5% | n/a | 半導體 10–20% (估計) | 負值 |
| FCF (TTM) | -680.2M USD | FY2024 +428.5M | n/a | 紅旗 |
| FCF margin (TTM) | -99.9% | FY2025 -77.0% | 半導體 15–25% (估計) | 紅旗 |
| FCF / NI | NM | NM | 健康值 >0.9 | 不具意義 (NI 與 FCF 方向相反) |
| Capex (FY2025) | 382.7M USD | 16.3x FY2024 | n/a | 大幅擴張, 壓縮 FCF |
| Cash & ST investments (2026-06) | 7.92B USD | 2026-03 2.23B | n/a | 強 |
| Total debt (2026-06) | 1.49B USD | 2026-03 1.36B (+9.2%) | n/a | 可控 |
| Net cash (粗估) | 約 6.43B USD | n/a | n/a | 強 |
| Current ratio | 5.83x | 2026-03 2.51x | 半導體 2–3x (估計) | 強 |
| Debt / Equity | 0.16x | n/a (2026-03 權益為負) | 半導體 0.2–0.5x (估計) | 健康 |
| Shares outstanding (BS) | 228.2M | 2026-03 215.1M (+6.1%) | n/a | 稀釋中 |
| Insider net flow (6 個月) | 約 -408M USD (賣出) | 0 筆公開買入 | n/a | 偏空 |
| Insider sales / market cap | 約 1.35% | n/a | n/a | 中等規模 |
| Institutional ownership | 80.4% | n/a | 大型股 70–85% (估計) | 正常 |
| Short interest / float | 12.6% (short ratio 2.2 天) | 月增 +5.9% | n/a | 偏高 |
| Price | 127.21 USD | 52w -59.1% | n/a | 接近 52 週低點 |
| Price vs 200DMA | -38.4% | n/a | n/a | 弱勢 |
| Market cap | 30.22B USD | n/a | n/a | 股數口徑不一致 |
| EV | 23.79B USD | n/a | n/a | 與 yfinance 一致 |
| Trailing P/E | NM | n/a | 半導體 25–40x (估計) | 不適用 |
| Forward P/E | 99.9x | n/a | 半導體 25–35x (估計) | 估值過高 |
| EV/Revenue (TTM) | 34.9x | n/a | 半導體 8–12x (估計) | 估值過高 |
| EV/EBITDA (TTM) | -49.1x | n/a | 半導體 20–30x (估計) | NM (EBITDA 為負) |
| P/S (TTM) | 44.4x | n/a | 半導體 5–8x (估計) | 估值過高 |
| P/B | 3.16x | n/a | 半導體 3–6x (估計) | 合理偏高 |
| P/FCF | NM | n/a | 半導體 25–40x (估計) | NM (FCF 為負) |
| 分析師平均目標價 | 291.6 USD (+129%) | n/a | n/a | 共識偏多, 與市價落差大 |
| 分析師評級 | Strong Buy 3 / Buy 8 / Hold 0 / Sell 0 | 1 個月前 Hold 1 | n/a | 共識 Buy |

註: 「Sector median (estimate)」欄位為依一般半導體與 AI 基礎設施板塊經驗的估計區間, 不是由工具輸出, 僅供相對比較使用。

## Red flags

- 2026-06 季 gross margin 14.2% (Q1 44.6%), 原因工具資料無法解釋, 可能為存貨或一次性成本, 需 10-Q 確認。
- 營收季增 -6.9% (Q2 vs Q1), 高成長是否持續存疑。
- TTM FCF -680.2M USD, capex 由 FY2025 的 382.7M 持續擴張, 公司需持續依賴外部資金。
- 盈餘品質低: FY2025 淨利 237.8M USD 幾乎全數來自 363.3M 非營業投資利益, 同年 OCF 為 -10.1M。
- Q2 SBC 377.0M USD 造成 GAAP EPS -2.98, 股權稀釋 (股數 +6.1% 季度增加) 與 SBC 同時發生。
- 內部人 6 個月公開賣出約 408M USD, 0 筆公開買入, 集中在 8–9 月; 賣出均價約 196–250 USD, 高於現價 35–49%。
- 股價 52 週跌幅 -59.1%, 現價低於 50 日與 200 日均線, 單日 -10.5%。
- 做空比率 12.6% of float, 且月增 5.9%。
- Forward P/E 99.9x 與 EV/Revenue 34.9x 處於極高估值區間, 估值對成長兌現的容錯空間很小。
- 資料一致性問題: 股數 (112.2M / 215.1M / 228.2M / 237.6M) 不統一, 導致市值不確定 ±5%; 報價時間戳記為週六; 單日漲跌 (-14.96 vs -15.47) 兩個欄位不一致; EPS 來源口徑 (調整後 vs GAAP) 不明。
- 資料缺口: 客戶集中度、segment、guidance、backlog、capex 計畫、債務到期結構、IPO 鎖定期條款 — 全部 n/a, 需 S-1 與 10-Q 補充。

FUNDAMENTALS REPORT COMPLETE
