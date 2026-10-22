# Fundamentals — MU as of 2026-10-22

## Executive summary
MU 財務體質目前處於歷史最強階段: 最近一季 (FQ3 FY26, 2026-05-31) 營收 41.46B USD、毛利率 84.6%、淨利率 68.1%, 現金及短期投資 26.02B 高於總負債 6.38B, 淨現金約 19.6B。以 trailing P/E 12.3x、EV/EBITDA 9.1x、forward P/E 4.4x 計算, 估值相對半導體同業估計值明顯偏低, 但這是記憶體超級週期下的峰值獲利, 不能外推為常態。主要風險在於 (1) 應收帳款與資本支出急速擴張, 9M FY26 FCF/NI 僅約 0.55 (低於 0.9 健康門檻); (2) 近 6 個月內部人合計約 273M USD 公開市場出售, 無買進; (3) 產業週期反轉風險與 beta 2.23 的價格波動。

資料時點: 報告以 2026-10-22 為 as-of。財報明細最新只到 FQ3 FY26 (2026-05-31); FQ4 FY26 (2026-08-31, 2026-09-30 已公布 EPS 33.42) 之報表明細 yfinance 尚未提供, 僅能由 info 之 TTM 數字反推, 已於資料品質段落標註。

## Revenue & profitability

**營收趨勢 (年度, FY 結束於 8/31)**
- FY22 30.758B → FY23 15.540B (-49.5%) → FY24 25.111B (+61.6%) → FY25 37.378B (+48.8%)
- 3 年 CAGR (FY22→FY25): 約 +6.7%, 但受 FY23 谷底影響, 2 年 CAGR (FY23→FY25) 約 +55.1%。
- 季度 YoY 極端: FQ3 FY26 營收 41.456B vs FQ3 FY25 9.301B, YoY +345.7%。季度序列: FQ4 FY25 11.315B → FQ1 FY26 13.643B → FQ2 23.860B → FQ3 41.456B。
- info 之 TTM 營收 133.19B、revenueGrowth 3.793 (即約 +379%); 由 TTM 扣除前三季後, 推得 FQ4 FY26 營收約 54.2B (推算值, 非 yfinance 直接揭露)。

**業務結構**
- longBusinessSummary 描述四大事業單位: Cloud Memory (CMBU)、Core Data Center (CDBU)、Mobile and Client (MCBU)、Automotive and Embedded (AEBU)。產品為 DRAM (含 HBM)、NAND、NOR。
- 分部營收與分部獲利: DATA_UNAVAILABLE (yfinance 未提供分部數據, info 亦無分部金額)。

**毛利率 / 營益率 / 淨利率 趨勢**
- 毛利率 (年度): FY22 45.2% → FY23 -9.1% → FY24 22.4% → FY25 39.8%
- 毛利率 (季度): FQ3 FY25 37.7% → FQ4 FY25 44.7% → FQ1 FY26 56.0% → FQ2 74.4% → FQ3 84.6%
- 營益率 (FQ3 FY26, 依 Operating Income 33.318B): 80.4%; FY25 年度 26.2% (9.809B); FY23 為營業虧損 -5.4B。
- 淨利率: FY25 22.8% (8.539B); FQ3 FY26 68.1% (28.243B); FQ3 FY25 20.3%。
- EBITDA 率 (Normalized EBITDA, FQ3 FY26): 85.8%。
- R&D 費用: FY25 3.798B (10.2% 營收); FQ3 FY26 1.316B (3.2% 營收), 研發絕對金額持續增加但占比大幅下降。
- 稅率: FY25 有效稅率 11.8%; FQ3 FY26 季度有效稅率約 15.0%, 逐季上升。

**EPS**
- 稀釋 EPS: FY25 7.59 (FY24 0.70)。季度: FQ3 FY26 24.67 vs FQ3 FY25 1.68 (YoY +1,368%)。
- trailingEps (info) 74.33 與各季稀釋 EPS 加總 74.76 接近。
- Earnings surprise: 最近 5 季皆為 beat, 幅度 +5.0% 至 +33.2% (2026-03-18 季 +33.21%; 2026-06-24 季 +21.39%; 2026-09-30 季 +5.03%)。

**ROE / ROIC**
- ROE: info TTM 88.3%; FY25 以期末權益計 15.8% (8.539B / 54.165B)。
- ROIC (自行估算, 非 yfinance 直接數據): TTM 至 2026-05-31 之 EBIT 59.29B × (1 - 15%) = NOPAT 50.4B, 除以期末 Invested Capital 103.78B, 約 48.6%。FY25 同口徑約 13.6%。

## Cashflow & balance sheet

**現金流 (年度)**
- OCF: FY22 15.181B → FY23 1.559B → FY24 8.507B → FY25 17.525B
- Capex: FY22 12.067B → FY23 7.676B → FY24 8.386B → FY25 15.857B
- FCF (OCF - Capex): FY22 3.114B → FY23 -6.117B → FY24 0.121B → FY25 1.668B
- FY25 FCF margin 4.5%; FCF/NI 0.20 (遠低於 0.9)。

**現金流 (季度, 近期改善)**
- 9M FY26 (FQ1-FQ3) OCF 45.70B、Capex 19.60B、FCF 26.10B; 9M FCF margin 約 33.1% (FCF/營收 78.96B)。
- 9M FY26 FCF/NI = 26.10 / 47.27 = 0.55; FQ3 FY26 單季 FCF/NI 0.62; FQ2 0.40; FQ1 0.58。
- TTM (至 2026-05-31) FCF 約 26.17B, FCF/NI 約 0.52。
- info 之 TTM OCF 89.67B、FCF 29.14B (含 FQ4 FY26 推估, 見資料品質段落)。

**FCF 品質重點**
- FQ3 FY26 營運資金大幅吸收現金: Change in Receivables -11.655B、Change in Working Capital -5.787B, 部分由 Change in Other Current Liabilities +3.767B 與應付 +2.401B 抵銷。
- 應收帳款 (Accounts Receivable) 期末 26.89B, 較 FY25 期末 7.16B 增加約 +275%。以季度營收推算之 DSO 約 59 天, 與 FQ4 FY25 (約 58 天) 相近, 表示帳款增加主要跟隨營收成長, 但絕對規模已成為現金流主要風險。
- 存貨 8.57B (FY25 期末 8.36B), 以季度 COGS 推算之存貨天數約 122 天, 與 FY25 大致持平, 存貨並未隨營收同步膨脹。

**資產負債表 (2026-05-31, 最新季)**
- 總資產 134.11B (FY25 期末 82.80B); 股東權益 100.72B (FY25 54.17B, +86%, 主要來自保留盈餘增加 94.68B vs 48.58B)。
- 現金、約當現金及短期投資 26.02B (現金及約當 24.99B)。
- 總負債 33.39B; 總有息負債 (Total Debt) 6.38B (含 Capital Lease 3.32B); FY25 期末 15.28B, 9 個月內減少約 8.9B。
- 淨現金 (cash+ST inv - total debt) = 26.02 - 6.38 = 約 19.6B。FY25 期末淨負債 = 15.28 - 10.31 = 約 4.97B (自行計算)。
- 流動比率 3.42x (66.74 / 19.49, 自行計算); 速動比率約 2.98x。info 之 currentRatio 3.314、quickRatio 2.898 為較新期間值。
- 負債權益比 (Total Debt / Equity): 5/31 為 6.3%; info debtToEquity 3.743 (yfinance 以百分比表示, 即 3.7%)。
- 有形帳面價值 (Tangible BV) 99.10B, 每股帳面價值 (bookValue) 122.35。
- 淨負債 / EBITDA (FY25): 約 0.27x。

**資本支出趨勢**
- FY25 Capex 15.857B (營收占比 42.4%), FY24 33.4%, FY23 49.4%, FY22 39.2%。
- 季度 Capex 加速: FQ3 FY26 7.826B vs FQ3 FY25 2.938B (+166%); 9M FY26 Capex 19.60B。
- 淨 PP&E 由 FY25 期末 47.33B 增至 2026-05-31 之 57.11B (+20.7%, 三季內)。在建工程 (CIP) 10.94B, 較 FY25 期末 5.52B 翻倍, 顯示擴產進行中。
- 9M FY26 Capex/OCF = 19.60 / 45.70 = 43%。

## Capital allocation & insider signal

**股息**
- 每季股息約 0.15 USD (dividendRate 0.6 USD/年)。info dividendYield 0.07 (即 0.07%)、payoutRatio 0.0071 (0.71%)。
- 近 4 季股息現金支出合計約 567M USD; 相對 TTM FCF 約 26B 覆蓋倍數遠高於 40 倍, 股息占資本配置比重極低。
- 最近除息日 (依 yfinance timestamp 換算) 約 2026-10-14; 配息日 timestamp 對應 2026-11 初。

**買回 / 股本**
- FY24 買回 300M, FY25 買回 0; FY26 前三季買回 650M (FQ1 300M、FQ2 350M、FQ3 0)。
- 股本仍在增加: 發行股數 (Share Issued) 由 FY25 1.266B 增至 2026-05-31 之 1.275B; 流通股數 1.1314B (info sharesOutstanding)。
- 稀釋股數 (Diluted Average Shares): FQ3 FY25 1.125B → FQ3 FY26 1.145B (+1.8%)。SBC 加速 (FY25 972M, 9M FY26 約 0.95B 以上), 買回不足以抵銷稀釋。
- 資本配置偏向: (1) 大幅擴充資本支出; (2) 償還債務 (9M FY26 償還約 9.4B); (3) 保留現金, 股息與買回金額相對小。

**內部人交易 (近 6 個月, 2026-04-22 至 2026-10-22)**
- 公開市場 (有金額) 出售合計約 273.4M USD, 共 16 筆, 合計約 295,349 股。
- 其中 CEO Sanjay Mehrotra 合計出售 200,000 股 (約 182.3M USD), 其餘為 DeBoer、Sadana、Arnzen、Allen、Dugle、Bjorlin、Gomo、Ray 等。
- 買進: 近 6 個月 0 筆公開市場買進。最近一次公開買進為 LIU TEYIN MARK 於 2026-01-14 (23,200 股, 約 7.8M USD), 已超出 6 個月窗口。
- 規模比較: 273.4M / 市值 1,033.7B = 約 0.026%; 內部人持股 (heldPercentInsiders) 0.24%。交易規模相對市值很小, 但方向一致 (只賣不買)。
- 注意: yfinance 之交易資料不含 10b5-1 計畫旗標, 無法判斷各筆為預定計畫或主動賣出 (DATA_UNAVAILABLE)。

**機構持股**
- heldPercentInstitutions 80.1%, 機構數 5,040。
- 前幾大持股 (2026-06-30 申報): BlackRock 9.27%、Vanguard Capital 6.51%、State Street 4.43%、Invesco 3.21%、Capital World Investors 2.60% (季減 -29.9%)、Geode 2.45%、FMR 2.36% (季減 -16.7%)、JPMorgan 2.28% (季增 +63.8%)。
- 做空: 做空比例占流通股 2.31%, 短期回補天數 (shortRatio) 1.04; 做空股數由前月 29.7M 降至 26.0M。

## Valuation

- 價格: 913.67 USD (info/fast_info 快取; 2026-10-21 收盤前後)。盤前 886.00 (-3.03%)。前收 896.07。
- 52 週區間 192.59–1,255.00 (ATH 1,255.00); 較 50 日均線 985.27 為 -7.3%, 較 200 日均線 726.85 為 +25.7%。
- 市值 1,033.7B USD (sharesOutstanding 1.1314B); 企業價值 (EV) 995.5B USD (info)。
- Trailing P/E 12.3x (913.67 / TTM EPS 74.33)。
- Forward P/E 4.42x (forwardEps 206.85); 若採 epsCurrentYear 176.50, P/E 為 5.18x。注意 yfinance 未明確標示 forwardEps 之期間定義, 兩者期間可能不同。
- EV/EBITDA (info) 9.15x; EV/Revenue 7.47x。
- P/S (trailing) 7.76x; P/B 7.47x。
- P/FCF: 以 info TTM FCF 29.14B 計 35.5x; 以 TTM 至 2026-05-31 之 FCF 26.17B 計 39.5x。
- PEG (info) 0.16, 但 earningsQuarterlyGrowth 為 1,077.8% 的極端值, 此指標僅供參考。
- 分析師目標價: 平均 1,560.57、中位數 1,550.00、最高 3,000.00、最低 361.00 (46 位分析師, recommendationMean 1.37, 評級 Strong Buy)。平均目標價較現價 +70.8%; 最低目標價與最高目標價差距極大 (反映週期判斷分歧)。
- 估值評論: 以週期峰值獲利計價, 估值指標偏低; 若獲利在記憶體價格回落時大幅回縮, 目前的低 P/E 會快速失效。這是估值與風險的核心矛盾, 不構成交易建議。

## Key catalysts

- 下次財報: yfinance 預估 2026-12-23 (isEarningsDateEstimate = true, 時段 timestamp 對應 16:00 ET 附近)。FQ1 FY27 (2026-11-30 季) EPS 一致預估 38.28 USD。
- 最近一次財報: 2026-09-30 (FQ4 FY26), 稀釋 EPS 33.42 vs 預估 31.82, beat +5.03%。
- 指引 (guidance): DATA_UNAVAILABLE (工具未提供公司指引文字)。
- 資本支出擴張: CIP 與 Capex 加速, 後續季度 Capex 與折舊走勢為 FCF 關鍵。
- 股利: 除息 2026-10-14 已過, 下一次配息以公司公告為準。
- 分部結構 / HBM 占比 / 定價走勢: DATA_UNAVAILABLE (工具不提供)。
- 內部人交易持續性與是否有 10b5-1 計畫: DATA_UNAVAILABLE。

## Metrics table

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| Revenue (FQ3 FY26, 2026-05) | 41.46B USD | +345.7% (vs 9.30B) | 約 +8% 至 +12% (估計) | 極強, 但屬週期峰值 |
| Revenue (FY25, Aug) | 37.38B USD | +48.8% (FY24 25.11B) | 約 +8% (估計) | 強 |
| Revenue CAGR FY22–FY25 | +6.7% (3y) | — | 約 +8% (估計) | 中性, FY23 谷底拉低 |
| Gross margin (FQ3 FY26) | 84.6% | +46.9 pts (vs 37.7%) | 約 50% (估計) | 極強 |
| Operating margin (FQ3 FY26) | 80.4% | +57 pts (vs 23.3%) | 約 20%–25% (估計) | 極強 |
| Net margin (FQ3 FY26) | 68.1% | +47.8 pts (vs 20.3%) | 約 10%–15% (估計) | 極強 |
| Net margin (FY25) | 22.8% | +19.7 pts (FY24 3.1%) | 約 10%–15% (估計) | 強 |
| ROE (TTM, info) | 88.3% | — | 約 15%–20% (估計) | 極強 (權益基數快速擴大後仍高) |
| ROIC (TTM 至 2026-05, 自行估算) | 約 48.6% | FY25 約 13.6% | 約 12% (估計) | 強 |
| FCF margin (9M FY26) | 33.1% | FY25 4.5% | 約 10%–15% (估計) | 改善明顯 |
| FCF / NI (9M FY26) | 0.55 | FY25 0.20 | 約 0.8–0.9 (估計) | 低於 0.9 門檻, 紅旗 |
| OCF (FQ3 FY26) | 25.39B USD | +451% (vs 4.61B) | — | 強 |
| Net cash (2026-05-31) | 約 19.6B USD | FY25 淨負債約 4.97B | 淨負債/EBITDA 約 0.5x (估計) | 強 |
| Current ratio (2026-05-31, 自行計算) | 3.42x | info 3.31x (較新) | 約 2.0x (估計) | 健康 |
| Quick ratio (2026-05-31, 自行計算) | 2.98x | info 2.90x | 約 1.2x (估計) | 健康 |
| Total Debt / Equity (2026-05-31) | 6.3% | FY25 28.2% | 約 40% (估計) | 健康, 已大幅去槓桿 |
| Capex (FQ3 FY26) | 7.83B USD | +166% (vs 2.94B) | 占營收約 15% (估計) | 擴張中, 壓縮 FCF |
| Capex / Revenue (FY25) | 42.4% | FY24 33.4% | 約 15% (估計) | 資本密集偏高 |
| Dividend yield | 0.07% | — | 約 0.5% (估計) | 極低 |
| Dividend payout (info) | 0.71% | — | 約 20% (估計) | 極低, 覆蓋極佳 |
| Share buyback (FY26 9M) | 650M USD | FY25 全年 0 | — | 小規模 |
| Diluted shares (FQ3 FY26) | 1.145B | +1.8% vs FQ3 FY25 1.125B | — | 股本仍微增 |
| Insider net (6M, USD) | -273.4M (只賣不買) | 0 買進 | — | 偏賣, 規模 0.026% 市值 |
| Trailing P/E | 12.3x | — | 約 30x (估計) | 偏低 |
| Forward P/E (forwardEps 206.85) | 4.4x | — | 約 22x (估計) | 偏低 (週期頂點 EPS 之風險高) |
| EV/EBITDA (info) | 9.1x | — | 約 18x (估計) | 偏低 |
| P/FCF (info TTM FCF) | 35.5x | — | 約 30x (估計) | 略高 |
| P/S (trailing) | 7.8x | — | 約 6x (估計) | 略高 |
| P/B | 7.5x | — | 約 5x (估計) | 偏高, ROE 支撐 |
| Analyst mean target | 1,560.57 (+70.8% vs 現價) | — | — | 分歧大 (361–3,000) |
| Beta | 2.23 | — | 約 1.5 (估計) | 高波動 |
| Short interest (% float) | 2.31% | 月減 -12.4% (股數) | 約 3%–5% (估計) | 低 |
| Institutional ownership | 80.1% | — | 約 70% (估計) | 高 |

## Red flags

- 應收帳款快速膨脹: 2026-05-31 AR 26.89B, 較 FY25 期末 7.16B 增加 +275%; FQ3 單季應收變動 -11.66B 吸收大量現金。DSO 約 59 天雖與過去大致相當, 但若客戶付款條件惡化, 會直接侵蝕 FCF。
- FCF 品質偏弱: FY25 FCF/NI 僅 0.20, 9M FY26 為 0.55, 均低於 0.9。獲利率高但現金轉換率並未同步。
- 資本支出加速: FQ3 Capex 7.83B (YoY +166%), 9M FY26 占 OCF 43%; CIP 翻倍。若記憶體價格下跌, 高固定成本與折舊 (FY25 D&A 8.35B) 會快速壓縮獲利。
- 週期性極高: 毛利率由 FY23 的 -9.1% 升至 FQ3 FY26 的 84.6%, 獲利主要來自記憶體價格與供需; 目前低 P/E 是以峰值獲利計算。
- 內部人只賣不買: 6 個月公開市場出售約 273.4M USD, CEO 出售 200,000 股; 規模相對市值小, 但方向一致。
- 股本仍微增: 稀釋股數 YoY +1.8%, 買回金額 (FY26 9M 650M) 無法抵銷 SBC 稀釋。
- 估值分歧大: 分析師目標價 361–3,000, 平均目標價 1,560 與中位數 1,550 之間距離很大, 反映市場對週期位置判斷分歧。
- 股價波動: beta 2.23, 52 週區間 192.59–1,255.00 (約 6.5 倍); 盤前 -3.03%。
- 資料品質 (見下段) 可能影響最新季估值與毛利率的精確性。

## 資料品質與缺口

- 數據時點: 財務明細 (quarterly_fin / quarterly_bs / quarterly_cf) 最新為 2026-05-31 (FQ3 FY26)。FQ4 FY26 (2026-08-31) 於 2026-09-30 已公布 EPS 33.42 (earnings_dates), 但報表明細尚未出現在 yfinance 季度表中。
- info 之 TTM 數字 (totalRevenue 133.19B、grossProfits 107.50B、EBITDA 108.84B、operatingCashflow 89.67B、freeCashflow 29.14B、netIncomeToCommon 84.97B) 已包含 FQ4 FY26。由其反推的 FQ4 FY26 單季營運數字存在不一致: 反推營益率約 95%、毛利率約 86.8%, 與 FQ3 營益率 80.4% 相比顯著偏高, 故本報告不以反推的 FQ4 營益率作為結論依據。
- yfinance 季度 "Reported EPS" (earnings_dates, 可能為調整後) 與 季度報表 "Diluted EPS" (GAAP) 略有差異, 例如 FQ3 FY26 為 25.11 vs 24.67。
- 季度 Interest Expense (2026-05-31) 顯示 0, 疑為資本化利息或資料欄位異常, 未納入判斷。
- yfinance 之 Net Debt (FY25 1.891B) 與 Total Debt 減 Cash 之自行計算值 (4.97B) 不一致, 本報告採自行計算。
- fast_info 之 50/200 日均線與市值欄位為 null, 改採 info 之 fiftyDayAverage / twoHundredDayAverage。
- 即時報價 feed 無法連線 (403 CONNECT tunnel failed), 價格與 fast_info 數字使用 repo 快取 (prices/yf cache), 盤中數據可能有落差。
- forwardEps 期間定義未揭露; epsCurrentYear 176.50 與 forwardEps 206.85 之期間可能不同。
- 分部營收、公司指引、HBM 占比、客戶集中度: DATA_UNAVAILABLE。
- 行業中位數皆為分析師估計 (非工具所得), 僅供相對判斷用。

FUNDAMENTALS REPORT COMPLETE
