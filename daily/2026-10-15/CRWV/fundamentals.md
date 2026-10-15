# Fundamentals — CRWV as of 2026-10-15

## Executive summary
CoreWeave (CRWV) 的財務體質偏弱: TTM (2025Q3–2026Q2) 營收 7,590M USD、營收 YoY 約 +112% (2026Q2 對 2025Q2), 但 TTM 淨利 -1,928M、TTM FCF 約 -13,655M (OCF 6,911M 減 capex 20,566M), 淨負債約 29.5B, Debt/Equity 約 10.3x, 流動比率 0.455。估值上, EV/Revenue 10.85x、EV/EBITDA 21.7x、P/S 4.78x, trailing 與 forward P/E 皆為負值 (n/m), 估值是否具吸引力高度依賴未來成長兌現與融資成本, 工具資料無法單獨支撐結論。股價 65.78 較 52 週高點 150.4 低約 56%, 同期 6 個月內內部人士合計賣出約 1.28B USD、無任何買入紀錄。

資料說明: 本次 yf 即時來源失敗 (CONNECT tunnel 403), 全部數據來自本地 cache (source: "cache", cached_at 2026-10-15 11:16–11:19 UTC), 屬預期行為。報價最後交易時點為 regularMarketTime 2026-10-14 20:00 UTC; 內部人交易資料最晚至 2026-10-13; 機構持股為 2026-06-30 季報資料; 財務報表最新至 2026-06-30 季。未超出 {DATE} 的資料只有 2026-10-14 報價與 2026-10-13 內部人交易, 屬 as-of 前一日, 無 post-date 問題。

## Revenue & profitability

**營收與成長**
- 年度營收 (Total Revenue): 2022 16M → 2023 229M → 2024 1,915M → 2025 5,131M。2024 YoY +736%, 2025 YoY +168%。2023–2025 兩年 CAGR 約 +373%; 2022 基期極小, 三年 CAGR (約 +585%) 不具參考意義。工具資料僅覆蓋 2022–2025 四個年度, 無法計算 3–5 年可靠 CAGR。
- 季度營收: 2025Q2 1,212M → 2025Q3 1,365M (QoQ +12.6%) → 2025Q4 1,572M (+15.2%) → 2026Q1 2,078M (+32.2%) → 2026Q2 2,575M (+23.9%)。2026Q2 對 2025Q2 YoY 約 +112.5%, 與 info.revenueGrowth 1.125 一致。
- TTM 營收 7,590M, 與 info.totalRevenue 一致。
- 分部 (segment) 營收: DATA_UNAVAILABLE。longBusinessSummary 只以產品線描述 (GPU compute、CPU compute、networking、managed services、Weights & Biases 等), 未提供分部營收占比。

**毛利 / 營業利益 / 淨利率趨勢**
- 毛利率 (Gross Profit / Revenue): 2023 約 69.9%、2024 約 74.3%、2025 約 71.7%。季度: 2025Q2 74.2% → 2025Q3 73.0% → 2025Q4 67.6% → 2026Q1 65.5% → 2026Q2 65.9%。毛利率自 2025 上半年約 74% 下滑至約 66%, 高於 info.grossMargins (0.674) 的 TTM 口徑相近。
- 營業利益率 (Operating Income / Revenue): 2024 約 16.9%, 2025 約 -0.9% (-46M)。季度: 2025Q2 +1.6% → 2025Q3 +3.8% → 2025Q4 -5.7% → 2026Q1 -6.9% → 2026Q2 -1.9% (-49M)。TTM 營業利益約 -231M, 營業利益率約 -3.0%。注意: info.operatingMargins (-0.019) 等於 2026Q2 單季數值, 非 TTM。
- 淨利率: 2024 -45.1% (-863 / 1,915), 2025 -22.7% (-1,167 / 5,131)。TTM 淨利 -1,928M, 淨利率 -25.4%, 與 info.profitMargins (-0.254) 一致。季度淨利: 2025Q2 -290M、2025Q3 -110M、2025Q4 -452M、2026Q1 -740M、2026Q2 -626M。
- 每股盈餘 (diluted EPS): 2025 全年 -2.81; 季度 2025Q2 -0.60、2025Q3 -0.22、2025Q4 -0.89、2026Q1 -1.40、2026Q2 -1.14。2026Q2 實際 EPS -1.14 優於 EPS estimate -1.47 (surprise +22.45%); 2026Q1 -1.40 劣於 -1.20 (surprise -16.26%)。

**ROE / ROA / ROIC**
- ROE: info.returnOnEquity = -43.6% (負值, 口徑由 yfinance 提供)。
- ROA: info.returnOnAssets 為 -0.24%, 與以 TTM 淨利 / 期末總資產 (-1,928 / 77,070 = -2.5%) 計算結果不符, 數值需視為資料異常, 本報告採計算值 -2.5%。
- ROIC: TTM EBIT 約 -49M (以 yfinance EBIT 列計算), 期末 Invested Capital 40,092M, ROIC 約 0% 且為負 (非正常 NOPAT 口徑, 僅供方向判斷)。

## Cashflow & balance sheet

**現金流品質**
- 經營現金流 (OCF): 2023 1,833M → 2024 2,749M → 2025 3,058M。TTM OCF 6,911M, 與 info.operatingCashflow 一致; OCF margin TTM 約 91%。
- 資本支出 (Capex): 2023 2,943M → 2024 8,702M → 2025 10,309M。TTM Capex 20,566M (2025Q3 2,389M、2025Q4 4,060M、2026Q1 7,695M、2026Q2 6,422M)。TTM Capex / 營收 約 271%。
- 自由現金流 (FCF = OCF - Capex): 2023 -1,110M → 2024 -5,953M → 2025 -7,251M。TTM FCF 約 -13,655M, FCF margin TTM 約 -180%。2026Q2 單季 FCF -5,743M。注意: info.freeCashflow 為 -9,088M, 與季度加總 (-13,655M) 不一致, 本報告採季度加總。
- FCF / NI: 淨利與 FCF 皆為負值, 比率 n/m (not meaningful), 不能以此判定品質。FCF 為負, 是目前主要的現金流風險。

**資產負債表 (2026-06-30 季末)**
- 總資產 77,070M (2025-12-31 為 49,302M, 半年增加約 56%)。總負債 72,046M。股東權益 5,024M (權益/資產 約 6.5%)。
- 現金與約當現金 5,524M (含短期投資 5,539M), 2026-03-31 為 2,244M。
- 總負債 (Total Debt) 51,608M, 其中 Long Term Debt 27,555M、Current Debt 7,513M、Capital Lease Obligations 16,540M (2025-12-31 為 8,449M)。
- 淨負債 (Net Debt, yfinance 口徑) 29,544M, 2025-12-31 為 18,246M。淨負債 / TTM EBITDA 約 7.5x (以季度 Normalized EBITDA 加總 3,941M 計), 若用 info.ebitda 3,789M 則約 7.8x。
- Debt / Equity: 10.27x (info.debtToEquity 1,027 %), 2025-12-31 為 8.94x。
- 流動比率 (Current Ratio): 0.455 (流動資產 9,520M / 流動負債 20,917M), 與 info.currentRatio 一致; 2026Q1 為 0.315。速動比率 info.quickRatio 0.386。
- 營運資金 (Working Capital) -11,397M。
- 利息覆蓋: TTM 利息費用 (Interest Expense) 約 1,875M (2025Q3 311M、2025Q4 388M、2026Q1 536M、2026Q2 640M), TTM EBIT 為負, 利息覆蓋倍數為負 (n/m)。2025 全年利息費用 1,229M, 利息實付 (Interest Paid) 869M。
- 利率、到期結構、契約條款、GPU 資產抵押細節: DATA_UNAVAILABLE。

## Capital allocation & insider signal

**資本配置**
- 資本支出快速擴張: 2025 年 Capex 較 2024 成長約 +18.5%; 2026 上半年 Capex 合計約 14,117M (Q1 7,695M + Q2 6,422M), 已超過 2025 全年 (10,309M)。
- 融資結構以債務與股權並行: 2025 年 Long Term Debt Issuance 11,829M、Issuance of Capital Stock 1,491M; TTM 債務發行約 24,180M, 其中 2026Q2 單季 13,457M。
- 股本稀釋: 稀釋加權股數 (Diluted Average Shares) 由 2025Q2 487M 增至 2026Q2 551M (+13%); 期末 Share Issued 由 2025-06-30 的 495M 增至 2026-06-30 的 551M (+11.3% YoY)。
- 股利與回購: 普通股無股利 (Cash Dividends Paid 2025 為 -29M, 與 Preferred Stock Dividends 29M 相符; TTM 為 0)。回購: 2024 -1M、2023 -32M、2025 n/a, 目前無實質回購。股利覆蓋率: n/a (無普通股股利)。
- 股份基礎報酬 (SBC): 2025 年 630M (約營收 12.3%); TTM 約 619M。

**內部人交易 (2026-06-15 至 2026-10-13, 約 6 個月)**
- 總筆數 150 筆, 其中 81 筆明確標示為 Sale, 合計 13,259,766 股、約 1,281M USD; 買入 0 筆。另有 64 筆 Text 空白、2 筆 derivative conversion、2 筆 stock award、1 筆 gift, 未納入 sale 計算。
- 主要賣方: Magnetar Financial (4,683,392 股、約 512M USD, 屬 10% 大股東但列入內部人)、Michael N. Intrator (CEO, 5,076,558 股、約 455M)、Brannin McBee (2,543,008 股、約 225M)、Brian M. Venturo (302,152 股、約 30M)、Nitin Agrawal (CFO, 261,405 股、約 24M)、Kristen J. McVeety (259,606 股、約 22M)。
- 平均隱含賣出價約 96.6 USD (1,281M / 13.26M 股), 高於現價 65.78 約 47%。
- 規模: 1,281M 占 yfinance market cap 36,280M 約 3.5%。淨內部人買賣為 -1,281M, 無任何買入抵消。
- 內部人持股比例 (heldPercentInsiders): 18.6%。

**機構持股 (2026-06-30 季報)**
- 機構持股合計 76.9%, 機構數 1,305。前十大持股約 48.5%: Magnetar 11.35% (持股 -24.1% QoQ)、NVIDIA 10.29% (持平)、BlackRock 5.25% (+157%)、Goldman Sachs 3.95%、Vanguard (兩個實體合計約 7.2%)、Jane Street 3.03%、Invesco 2.70% (+1,149%)、Alyeska 2.37%、Value Aligned 2.37%。
- 空頭部位: sharesShort 59.95M 股, 占 float 19.2%, shortRatio 2.08 天, 較前月 55.57M 增加約 7.9%。

## Valuation

- 價格與市值: 現價 65.78 USD (regularMarketPrice, 2026-10-14 收盤時點), 前收 77.81, 日內 -15.5%。市值 36,280M (info.marketCap), 企業價值 EV 82,354M (= 市值 + 總負債 51,608M - 現金 5,539M, 與 info.enterpriseValue 一致)。
- P/E: trailing 為 n/m (TTM EPS 為負); info.trailingEps -3.12 與季度 diluted EPS 加總 -3.65 不一致, 兩者皆為負。forward P/E -35.87 (forwardEps -1.83), n/m。
- EV/EBITDA: 21.7x (info.enterpriseToEbitda, 以 ebitda 3,789M 計); 以季度 normalized EBITDA 加總 3,941M 計約 20.9x。
- EV/Revenue: 10.85x (info.enterpriseToRevenue)。
- P/S (TTM): 4.78x。
- P/B: 7.21x (bookValue per share 9.118)。
- P/FCF 與 FCF yield: n/m (FCF 為負, TTM FCF yield 約 -37.6%)。
- Beta: DATA_UNAVAILABLE (info 未提供 beta 欄位)。
- 股價位置: 52 週高 150.4 / 低 60.55; 現價較 52 週低點高約 8.6%, 較 52 週高點低約 56.3%; 低於 50 日均線 87.92 約 25.2%、低於 200 日均線 92.53 約 28.9%。All-time high 187.0。
- 分析師預期: 38 位, 平均目標價 141.47 USD (高 278、低 39), 較現價隱含 +115%; recommendationMean 1.83 (averageAnalystRating "1.8 - Buy")。分析師目標價為賣方預測, 非本報告結論。
- 同業中位數: 工具不提供 sector median。下表 "Sector median (estimate)" 欄位為分析師經驗估計值 (Software-Infrastructure / AI 雲端基礎設施同業), 非工具資料, 僅供方向對照。

## Key catalysts

- 下次財報: 2026-11-11 (earnings_dates 首列, EPS estimate -1.53); info.isEarningsDateEstimate 為 False。上次財報 2026-08-11 (2026Q2 EPS -1.14 優於估計)。
- 管理層指引 (guidance): DATA_UNAVAILABLE (工具不提供公司指引與 backlog / RPO 資料)。
- 分部與客戶集中度: DATA_UNAVAILABLE。NVIDIA 為第二大股東 (10.29%), 但工具無法確認其是否為主要客戶或供應商, 不做推論。
- 融資事件: 2026Q2 債務發行 13,457M 單季, 為後續利息與到期壓力的主要變數; 具體融資條款 DATA_UNAVAILABLE。
- 毛利率走向: 2026Q2 毛利率 65.9%, 若後續季度持續低於 2025 上半年約 74% 水準, 將影響盈利改善路徑。
- 內部人與大股東持續減持: Magnetar 在 2026Q2 已減持 24.1%, 上述 6 個月內部人賣出是否延續需觀察後續 Form 4。

## Metrics table

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 TTM (Total Revenue) | 7,590M | 2026Q2 YoY +112.5% | 估計 YoY 約 +10–20% | 高成長, 但基數效應與融資依賴需留意 |
| 年度營收 2025 | 5,131M | +168% (2024 1,915M) | n/a | 成長極快 |
| 毛利率 (Gross Margin) 2026Q2 | 65.9% | -8.3 pp (2025Q2 74.2%) | 估計 約 70% | 偏弱, 呈下滑趨勢 |
| 營業利益率 (Operating Margin) TTM | -3.0% | 2025 全年 -0.9% vs 2024 +16.9% | 估計 約 10–15% | 劣於同業 |
| 淨利率 (Net Margin) TTM | -25.4% | 2025 -22.7% vs 2024 -45.1% | 估計 約 5–10% | 虧損, 雖有改善但仍深度為負 |
| ROE | -43.6% | n/a | 估計 約 10–15% | 劣於同業 |
| ROA (計算值) | -2.5% | n/a | 估計 約 3–5% | 劣於同業 |
| ROIC (TTM, 近似) | 約 0% (負) | n/a | 估計 約 8–12% | 資本報酬為負 |
| 經營現金流 OCF TTM | 6,911M | 2025 3,058M (2024 2,749M) | 估計 OCF margin 約 20–30% | OCF 為正但占營收比仍不足以支撐 Capex |
| 自由現金流 FCF TTM | -13,655M | 2025 -7,251M vs 2024 -5,953M | 估計 FCF margin 約 +10–15% | 嚴重為負, 高風險 |
| FCF margin TTM | -180% | 2025 -141% | 估計 +10–15% | 劣於同業 |
| FCF / NI | n/m (兩者皆負) | n/a | 估計 約 1.0 | 無法判讀, 以 FCF 絕對值為準 |
| Capex TTM | 20,566M | 2025 +18.5% | 估計 Capex/Revenue 約 10–20% | 投資強度極高 |
| 淨負債 (Net Debt) | 29,544M | 2025-12-31 18,246M (+62%) | n/a | 槓桿快速擴張 |
| 淨負債 / TTM EBITDA | 約 7.5–7.8x | 2025 年約 7.4x (18,246 / 2,468) | 估計 約 1–3x | 槓桿偏高 |
| Debt / Equity | 10.27x | 2025-12-31 8.94x | 估計 約 1.0x | 極度偏高 |
| Current Ratio | 0.455 | 2026Q1 0.315 | 估計 約 1.5x | 短期償付壓力 |
| 現金 (含短期投資) | 5,539M | 2025-12-31 3,161M (+75%) | n/a | 現金增加但仍遠低於債務 |
| 利息覆蓋 (EBIT / Interest) | 負值 (n/m) | 2025 EBIT 14M / 利息 1,229M | 估計 約 5–10x | 不具覆蓋能力 |
| 股本稀釋 (Share Issued YoY) | +11.3% (551M) | 2025-12-31 509M | 估計 約 0–2% | 持續稀釋 |
| 股利 / 回購 | 無 / 無實質回購 | n/a | 估計 股利覆蓋率 n/a | 不適用 |
| 內部人淨買賣 (6 個月) | -1,281M (0 筆買入) | n/a | n/a | 偏負面 |
| 內部人賣出占市值 | 約 3.5% | n/a | 估計 <1% | 規模偏大 |
| 空頭占流通股 (Short % Float) | 19.2% | 前月 SI +7.9% | 估計 約 3–5% | 空頭部位偏高 |
| Trailing P/E | n/m (EPS 為負) | n/a | 估計 約 25–35x | 無法比較 |
| Forward P/E | n/m (-35.9x) | n/a | 估計 約 25–35x | 無法比較 |
| EV/EBITDA | 21.7x (info) / 20.9x (季度加總) | n/a | 估計 約 20–25x | 與同業相近, 但 EBITDA 基礎薄 |
| EV/Revenue | 10.85x | n/a | 估計 約 6–10x | 偏高 |
| P/S (TTM) | 4.78x | n/a | 估計 約 6–8x | 相對 P/S 偏低, 但基本面為負 |
| P/B | 7.21x | n/a | 估計 約 3–5x | 偏高 |
| P/FCF | n/m (FCF 為負) | n/a | 估計 約 25–35x | 無法比較 |
| Beta | DATA_UNAVAILABLE | n/a | n/a | 無法判定 |
| 分析師平均目標價 | 141.47 (+115% vs 現價) | n/a | n/a | 賣方一致偏多, 與基本面背離 |

## Red flags

- FCF 嚴重為負: TTM FCF -13,655M, 2026Q2 單季 -5,743M, 資本支出 (TTM 20,566M) 大幅超過 OCF (6,911M), 擴張依賴外部融資。
- 槓桿高且快速增加: 總負債 51,608M (半年內自 29,822M 增加約 73%), Debt/Equity 10.27x, 淨負債 / EBITDA 約 7.5–7.8x, 利息費用 TTM 1,875M 且 EBIT 為負, 利息覆蓋不足。
- 短期流動性偏弱: 流動比率 0.455, 營運資金 -11,397M, 2026Q1 流動比率曾為 0.315。
- 毛利率下滑: 由 2025 上半年約 74% 降至 2026Q2 約 66%, 規模擴張尚未轉化為利潤率改善。
- 股權稀釋: 期末股數 551M, YoY +11.3%; 2025 年 Issuance of Capital Stock 1,491M。
- 內部人大量賣出、零買入: 6 個月約 1.28B USD, 平均隱含價約 96.6 USD, 高於現價約 47%。
- 大股東減持與空頭: Magnetar 2026Q2 持股 -24.1%; 空頭占流通股 19.2%, 且 SI 較前月增加。
- 資料品質與一致性問題 (需注意, 非結論性):
  - info.freeCashflow (-9,088M) 與季度加總 (-13,655M) 不一致。
  - info.returnOnAssets (-0.24%) 與計算值 (-2.5%) 不一致。
  - info.sharesOutstanding (458.9M) 與 marketCap / bookValue 推得的約 551M 股不一致, 市值計算採 info.marketCap。
  - info.fulldayPrice (63.11) 與 fast_info.last_price (65.78) 不一致, 報告採 regularMarketPrice 65.78。
  - info.trailingEps (-3.12) 與季度 EPS 加總 (-3.65) 不一致。
  - 2025 年 EBIT (14M) 與 Total Operating Income (-46M) 不一致。
  - info.operatingMargins 等於 2026Q2 單季值而非 TTM。
- 資料缺口 (DATA_UNAVAILABLE): 分部營收、公司指引、backlog / RPO、客戶集中度、債務利率與到期結構、Beta、sector median 工具數據、2025Q1 單季完整數據、2023 之前歷史。
- 以上所有數值僅為財務健康度與估值評估, 不構成交易建議。

FUNDAMENTALS REPORT COMPLETE
