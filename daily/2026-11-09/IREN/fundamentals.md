# Fundamentals — IREN as of 2026-11-09

資料說明: 數據來源為 pipeline/tools/yf 快取 (source: cache, cached_at 2026-11-08 13:11–13:16 UTC)。分析基準日 2026-11-09, 價格為 2026-11-08 收盤附近值。財報以 FYE 6 月計 (FY26 = 2025-07 至 2026-06)。金額單位為 USD, 以 M (百萬) / B (十億) 標示。info 與 quarterly 表之間存在期間不一致 (詳見 Red flags), 本報告分別標明。

## Executive summary

IREN 是以 AI 雲端與資料中心為主、比特幣挖礦為輔的成長型公司, FY26 營收 707.0M (YoY +41.1%), 但營業利益率 -53.6%、淨利率 -99.4%、FCF -2,350.4M, 財務體質正由「自有資金」轉為「高槓桿加股權稀釋」驅動的擴張, Jun-26 總負債 7.84B (YoY 約 8.1 倍), 股本 YoY 增加 47.3%。估值以 EV/Revenue 22.8x、P/S 13.2x 計價, 但 EPS 與 EBITDA 皆為負值, P/E、EV/EBITDA、P/FCF 均不具意義, 估值吸引力無法以獲利指標支撐, 只能以資本支出兌現與 AI 合約轉換進度判斷。Q4 FY26 營收季減 5.2%、年減 26.7%, 且 FY26 營業現金流 2,100.4M 主要來自約 1.8B 遞延收入流入, 非經常性質, 需與 capex 強度一併看待。

## Revenue & profitability

**營收與成長**
- 營收 (FY, Jun 結算): FY23 75.5M → FY24 187.2M → FY25 501.0M → FY26 707.0M。
- YoY: FY24 +147.9%、FY25 +167.6%、FY26 +41.1%。3 年 CAGR (FY23–FY26) 約 110.8%。
- 季度趨勢 (quarterly_fin): 2025-06 季 187.3M → 2025-09 季 240.3M → 2025-12 季 184.7M → 2026-03 季 144.8M → 2026-06 季 137.2M。FY26 下半年起連續三季環比下滑, Q4 年減 26.7%。info 欄位 revenueGrowth 為 -0.05。
- 業務組合: info.longBusinessSummary 描述為垂直整合 AI 雲端服務平台 (澳洲、加拿大)、資料中心建置與營運、比特幣挖礦, 並有 IREN Europe 規劃中的西班牙 Badajoz 約 300MW AI 資料中心。工具未提供分部營收, 分部占比為 DATA_UNAVAILABLE。

**獲利能力**

| 年度 | 毛利率 | 營業利益率 | 淨利率 | 稀釋 EPS |
|---|---|---|---|---|
| FY23 | 27.9% | -64.4% | -227.5% | -3.14 |
| FY24 | 44.6% | -14.6% | -15.4% | -0.29 |
| FY25 | 63.6% | +4.4% | +17.3% | +0.34 |
| FY26 | 62.3% | -53.6% | -99.4% | -2.22 |

- FY26 營業利益 -378.8M (季度加總相符), 但含減損等特殊項目之 Total Operating Income As Reported 為 -1,046.7M。特殊項目包括 Write Off 638.8M、Special Income Charges -779.8M 等, 工具未提供逐項說明。
- FY25 淨利 +86.9M 含非營業投資證券利得 (Gain On Sale Of Security 69.8M, Total Unusual Items +74.1M)。FY26 淨損 -702.6M 中, 非經常項目 (Total Unusual Items) 為 -351.4M。FY26 Gain On Sale Of Security 為 428.4M 且 CF 中 Unrealized Gain Loss On Investment Securities 為 -558.5M, 兩者方向與性質需於完整財報確認, 此處不做推論。
- 毛利率 FY25–FY26 維持約 62–64%, 但 FY26 營業費用由 296.3M 增至 819.4M (+176.6%), 其中 SG&A 319.8M (FY25 127.2M), 薪資 205.0M (FY25 70.2M), 折舊攤銷 417.7M (FY25 181.1M)。營運槓桿目前為負向。
- ROE (info TTM): -33.8%。以 FY26 淨利與期初期末平均股東權益 (3,001.6M) 計算, ROE 約 -23.4%。
- ROIC (推算): 以 FY26 營業利益 -378.8M 除以期初期末平均投入資本 (7,279.5M) 約 -5.2%。稅率僅 0.9%, 未另做稅盾調整。

## Cashflow & balance sheet

**現金流量 (FY26, USD M)**

| 項目 | FY26 | FY25 | FY24 |
|---|---|---|---|
| 營業現金流 (OCF) | 2,100.4 | 245.9 | 52.2 |
| 資本支出 (Capex, Purchase of PPE) | -4,343.3 (CF Capex -4,450.8) | -1,372.6 | -479.9 |
| 自由現金流 (FCF) | -2,350.4 | -1,126.7 | -427.7 |
| 股權發行 | 4,743.5 | 602.7 | 783.6 |
| 債務發行 | 6,299.6 | 701.2 | 0.0 |
| 債務償還 | -1,681.6 | 0.0 | 0.0 |
| 股權酬勞 (SBC) | 205.0 | 42.6 | 23.6 |

- FCF margin: FY26 -332.4%。FCF / NI 比率: FY26 FCF 與 NI 均為負, 比率不具判讀意義 (健康值 >0.9 不適用)。
- OCF 品質: FY26 OCF 2,100.4M 中, Change In Other Working Capital 為 +1,841.7M, 與 Non Current Deferred Revenue 由 0 增至 1,796.1M 相呼應。Q4 FY26 單季 OCF 1,811.1M, 而 Q1–Q3 合計僅 289.4M。此為一次性預收款性質, 不宜外推為經常性現金流。以 Q1–Q3 合計 289.4M 作為粗略參考, 經常性 OCF 規模遠不足以覆蓋 capex。
- 季度 Capex 加速: Q1 280.6M → Q2 836.9M → Q3 1,355.2M → Q4 1,978.2M。Capex 占營收 FY26 約 6.3 倍 (629%)。
- 期末現金 (CF) 7,619.5M, 其中資產負債表現金 5,895.6M 加上 Restricted Cash 1,670.3M, 差額 53.6M 為工具未拆分項目。

**資產負債表 (Jun-26 年報, USD M)**

| 項目 | Jun-26 | Jun-25 |
|---|---|---|
| 現金及約當現金 | 5,895.6 | 564.5 |
| 受限現金 (Restricted Cash) | 1,670.3 | 0.0 |
| 總債務 (Total Debt, 含租賃) | 7,839.5 | 964.2 |
| 淨債務 (工具值, 不含租賃) | 1,697.4 | 398.2 |
| 總資產 | 15,790.0 | 2,940.3 |
| 股東權益 | 4,185.6 | 1,817.5 |
| 有形帳面價值 | 3,831.6 | 1,817.5 |
| 在建工程 (Construction In Progress) | 3,764.1 | 240.8 |
| 淨 PP&E | 6,863.0 | 1,935.1 |
| 流動比率 | 3.55x (扣除受限現金約 2.80x) | 4.29x |
| 負債 / 股東權益 | 187% | 53% |

- 槓桿: 總債務由 964.2M 增至 7,839.5M, 其中長期債務 7,423.6M。利息費用季度趨勢: Q1 9.3M → Q2 10.7M → Q3 14.8M → Q4 24.5M, FY26 合計 59.3M; 因 EBIT 為負, 利息保障倍數 n/m。
- 最新季 (info, 推測為 2026-09-30 季) TTM 值: totalCash 3,522.0M、totalDebt 10,215.0M、淨債務約 6.69B、currentRatio 1.596、debtToEquity 199.7%。此為 info 欄位, 非 Jun-26 年報, 與 quarterly_bs 最末期 (2026-06) 不同, 見 Red flags。
- 流動性: 現金充裕但依賴持續融資。FY26 融資淨流入 9,680.0M, 同期 FCF -2,350.4M 與投資現金流出 -4,723.0M 合計需融資覆蓋。

## Capital allocation & insider signal

**資本配置**
- 無股利 (dividendYield 0.0)。FY26 無庫藏股買回。
- 資本配置重心為 AI 資料中心建置 (Capex 4,450.8M) 與債務/股權融資。
- 稀釋: 期末股數 258.1M (Jun-25) → 380.2M (Jun-26), +47.3%。FY26 加權平均稀釋股數 316.1M, 較 FY25 258.1M 增加 22.5%。info sharesOutstanding 為 424.4M (較 Jun-26 再增 11.6%, 工具未說明區間)。
- 股權酬勞 SBC 205.0M, 占營收約 29.0%, 為重要隱性稀釋成本。

**內部人活動 (近 6 個月, 2026-05 至 2026-11)**
- 公開市場買入或賣出: 0 筆。
- 2026-07-01 有一批 Stock Award (Grant), 價值 0 USD, 含 CEO William Roberts 與 Daniel Roberts 各 9,651,525 股 (間接持有, 兩人數字相同, 疑為同一實體持股重複列示)、CFO Anthony Lewis 26,968 股、3 名董事各 6,657 股、Bartholomew 8,369 股。此為薪酬性質, 非市場訊號。
- 超過 6 個月的歷史賣出 (參考, 非本視窗): 2025-09-11 兩位 CEO 各賣 1,000,000 股, 價格 33.13 (合計約 66.3M USD); 2025-09-16 董事 Guzowski 賣 11,958 股 @36.32 (約 0.43M USD)。以目前市值 9.18B 計, 合計約 0.7%, 量級不大。
- 內部人持股 (heldPercentInsiders) 6.5%。

**機構持股**
- 機構持股 61.1%, 926 家機構。前十大持股合計約 23.8%, 單一最大為 Bank of America 3.5%, BlackRock 3.3%, Goldman Sachs 3.1%, Citigroup 3.1%, Situational Awareness LP 2.3% (季減 19.0%)。
- 短期空單: sharesShort 94.6M, 占流通股 24.3% (shortPercentOfFloat), 占總股本約 22.3%; 較前月 83.1M 增加 13.9%; short ratio 2.17 日。空單比例高, 股價波動會放大。

## Valuation

價格基準: 21.64 USD (regularMarketPrice, 2026-11-08 盤後快取值), 當日 +20.0% (fulldayChangePercent +20.9%)。市值 9.18B USD, 企業價值 (EV) 15.88B USD。

| 估值指標 | 數值 | 說明 |
|---|---|---|
| Trailing P/E | n/a | TTM EPS -4.08, 無意義 |
| Forward P/E | n/m | Forward EPS -5.53 為負 (info 回傳 -3.91x, 不採用) |
| P/S (TTM) | 13.2x | 以 TTM 營收 695.0M 計 |
| EV / Revenue (TTM) | 22.8x | EV 15.88B / 695.0M |
| EV / EBITDA | n/m | TTM EBITDA -30.7M (info 回傳 -517.9x, 不採用) |
| P / FCF | n/m | TTM FCF -8.78B |
| P / Book | 1.72x | BVPS 12.57 |
| PEG | n/m | 盈利為負, info 回傳 3.11 不採用 |

- 相對同業中位數: DATA_UNAVAILABLE (工具未提供行業或同業中位數)。info 的行業標示為 Capital Markets / Financial Services, 與 AI 雲端、資料中心與礦業的實際業務不一致, 不宜以此分類推算同業中位數。
- 分析師: 19 位, recommendationMean 1.5 (strong_buy 區), 目標價 low 23.0 / median 58.0 / mean 64.08 / high 139.0。目前股價 21.64 略低於最低目標價 23.0。
- 價格位置: 52 週區間 17.16–70.71, 現價較 52 週高點低 69.4%, 較 50 日均線 (35.87) 低 39.7%, 較 200 日均線 (43.55) 低 50.3%。52 週漲跌幅 -64.0%。Beta 4.335。
- 估值評論 (不含建議): 以營收倍數估值, EV/Revenue 22.8x 遠高於一般 AI 基礎設施或資料中心同業的 EV/Revenue 區間 (同業數據 DATA_UNAVAILABLE, 僅能定性)。估值支撐來自未來合約與產能兌現, 而非目前獲利。

## Key catalysts

- 下一次財報: earnings_dates 列出最近未公布日為 2027-02-04 (EPS 預估 -2.20)。info 的 earningsTimestamp 指向 2026-11-05 並標示為估計日期 (isEarningsDateEstimate: true)。2026-11-05 已早於分析基準日, 但 earnings_dates 中無該季實際 EPS 紀錄, 是否已公布無法從工具確認。
- 前一季財報 (2026-08-27 列示): EPS 實際 -0.25 vs 預估 -0.45, 超預期 44.1%。但此 EPS 與 quarterly_fin 的 GAAP 季度 EPS 不一致 (見 Red flags)。
- 推算的 2026-09 季 (由 info TTM 減去 2025-12、2026-03、2026-06 季加總): 營收約 228.3M、淨利約 -263.4M。此為推算值, 非工具直接揭露。
- 資本支出進度: CIP 由 240.8M 增至 3,764.1M, 完工與轉為營運資產的時程是營收兌現的關鍵。
- 融資與債務: 總債務由 0.96B 升至 7.84B, 後續再融資條件與利率為主要外部變數。
- 客戶合約: 遞延收入 1,796.1M (非流動) 顯示有大型預收合約, 但工具未揭露客戶與合約條款, 此項為 DATA_UNAVAILABLE。
- 組織變動: info 顯示 nameChangeDate 2026-11-07 (prevName Iris Energy Limited), 但 longBusinessSummary 寫明改名於 2024-11, 兩者不一致, 僅列為待確認項目。

## Metrics table

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| Revenue FY26 (USD M) | 707.0 | +41.1% | DATA_UNAVAILABLE | 成長快, 但需檢視季度趨勢 |
| Revenue Q4 FY26, Jun-26 (USD M) | 137.2 | -26.7% (QoQ -5.2%) | DATA_UNAVAILABLE | 負面 |
| Gross margin FY26 | 62.3% | -1.3 pp | DATA_UNAVAILABLE | 尚可 |
| Operating margin FY26 | -53.6% | -58.0 pp (由 +4.4%) | DATA_UNAVAILABLE | 負面 |
| Net margin FY26 | -99.4% | 由 +17.3% 轉負 | DATA_UNAVAILABLE | 負面 |
| ROE (info TTM) | -33.8% | n/a | DATA_UNAVAILABLE | 負面 |
| ROIC (推算, 營業利益基礎) | -5.2% | n/a | DATA_UNAVAILABLE | 負面 |
| Diluted EPS FY26 (USD) | -2.22 | 由 +0.34 轉負 | DATA_UNAVAILABLE | 負面 |
| OCF FY26 (USD M) | 2,100.4 | +754% | DATA_UNAVAILABLE | 含一次性預收款, 品質存疑 |
| FCF FY26 (USD M) | -2,350.4 | 虧損擴大 108.6% | DATA_UNAVAILABLE | 負面 |
| FCF margin FY26 | -332.4% | n/a | DATA_UNAVAILABLE | 負面 |
| FCF / NI | n/m (兩者皆負) | n/a | DATA_UNAVAILABLE | 不適用 |
| Capex FY26 (USD M) | 4,450.8 | +224% | DATA_UNAVAILABLE | 擴張中, 與 AI 資產建置一致 |
| SBC FY26 (USD M) | 205.0 | +381% | DATA_UNAVAILABLE | 稀釋成本偏高 |
| Total debt Jun-26 (USD B) | 7.84 | 由 0.96B, 約 +713% | DATA_UNAVAILABLE | 負面 |
| Net debt Jun-26, 不含租賃 (USD B) | 1.70 | 由 0.40B, 約 +326% | DATA_UNAVAILABLE | 負面 |
| Debt / Equity Jun-26 | 187% | 由 53% | DATA_UNAVAILABLE | 負面 |
| Current ratio Jun-26 | 3.55x (扣除受限現金 2.80x) | 由 4.29x | DATA_UNAVAILABLE | 尚可 |
| Cash & equivalents Jun-26 (USD B) | 5.90 (另有受限現金 1.67) | 由 0.56B | DATA_UNAVAILABLE | 短期流動性充裕, 依賴融資 |
| Shares outstanding Jun-26 (M) | 380.2 | +47.3% | DATA_UNAVAILABLE | 稀釋嚴重 |
| Insider open-market activity (6 mo) | 0 筆 (僅 2026-07-01 薪酬型授予) | n/a | DATA_UNAVAILABLE | 中性 |
| Institutional ownership | 61.1% | n/a | DATA_UNAVAILABLE | 中性 |
| Short interest, % of float | 24.3% | 股數較前月 +13.9% | DATA_UNAVAILABLE | 負面 (高波動風險) |
| Market cap (USD B) | 9.18 | n/a | DATA_UNAVAILABLE | 中性 |
| P/E (TTM) | n/a | n/a | DATA_UNAVAILABLE | n/a (負 EPS) |
| P/S (TTM) | 13.2x | n/a | DATA_UNAVAILABLE | 偏高 |
| EV / Revenue (TTM) | 22.8x | n/a | DATA_UNAVAILABLE | 偏高 |
| EV / EBITDA | n/m (EBITDA 為負) | n/a | DATA_UNAVAILABLE | n/a |
| P / FCF | n/m (FCF 為負) | n/a | DATA_UNAVAILABLE | n/a |
| P / Book | 1.72x | n/a | DATA_UNAVAILABLE | 中性 |
| Analyst mean target (USD) | 64.08 (低 23.00 / 高 139.00) | n/a | DATA_UNAVAILABLE | 分析師意見偏正面, 差異極大 |
| Beta | 4.335 | n/a | DATA_UNAVAILABLE | 高波動 |

## Red flags

- 營收動能轉弱: FY26 連續三季環比下滑, Q4 年減 26.7%, 與 FY26 全年 +41.1% 的成長敘事不一致。
- 現金流依賴融資與一次性預收款: FCF FY26 -2,350.4M, Q4 OCF 1,811.1M 主要來自約 1.8B 非流動遞延收入, Q1–Q3 OCF 合計僅 289.4M。
- 槓桿快速上升: 總債務 YoY 約 8.1 倍至 7.84B; 利息費用季度內由 9.3M 升至 24.5M。Debt/Equity 187%。
- 稀釋與 SBC: 期末股數 +47.3%, SBC 占營收 29.0%。
- 獲利端非經常項目比重高: FY26 Total Unusual Items -351.4M, 特殊項目 -779.8M, 減損與註銷合計 (Asset Impairment 749.4M) 占淨損失比重大, 盈利品質無法以 GAAP EPS 判讀。
- 資料不一致 (需於下游驗證):
  1. info 的 TTM 欄位 (totalRevenue 695.0M、NI -1,350.6M、EPS -4.08、totalCash 3,522.0M、totalDebt 10,215.0M) 與 quarterly_fin / quarterly_bs 最末期 (2026-06) 不一致, 且 info 的 mostRecentQuarter 為 2026-09-30, 但財報表中無 2026-09 季。
  2. earnings_dates 的 EPS 歷史 (例如 2026-02-05 季實際 -0.03、2026-08-27 季實際 -0.25) 與 quarterly_fin 的 GAAP 季度 EPS (2025-12 季 -0.52、2026-03 季 -0.74) 不一致, 可能為不同基準 (調整後或 consensus 基準)。
  3. info.sharesOutstanding 424.4M 與 Jun-26 股數 380.2M 有 11.6% 差距, 區間未註明。
  4. info 的 earningsTimestamp (2026-11-05) 與 earnings_dates 的下一次財報 (2027-02-04) 不一致。
  5. info.nameChangeDate 為 2026-11-07, 但業務描述寫明改名於 2024-11。
  6. info 行業分類為 Financial Services / Capital Markets, 與 AI 雲端與資料中心業務不符。
- 空單比例偏高: 占流通股 24.3%, 且前月起增加 13.9%。
- 治理風險評分偏高: info 的 overallRisk、auditRisk、compensationRisk、shareHolderRightsRisk 皆為 10 (滿分), boardRisk 6。兩位共同 CEO 為 Roberts 同姓, 工具未說明關係, 關聯交易與董事會獨立性需後續核實。
- 估值與獲利脫鉤: P/S 13.2x、EV/Revenue 22.8x, 但 EPS、EBITDA、FCF 皆為負, 估值完全依賴未來現金流兌現。
- 股價波動極高: Beta 4.335, 單日 +20.0%, 52 週跌幅 -64.0%, 價格低於 50 日與 200 日均線。
- 資料缺口: 分部營收、客戶合約、Q1 FY27 完整財報、同業中位數、2026-11-05 (若已公布) 之實際結果, 工具均未提供, 標示為 DATA_UNAVAILABLE。

FUNDAMENTALS REPORT COMPLETE
