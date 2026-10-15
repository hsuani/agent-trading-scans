# Fundamentals — QBTS as of 2026-10-15

資料說明: 本報告以 pipeline/tools/yf.py 快取資料 (source: cache) 為準。最新價格為 2026-10-14 美股正常交易時段收盤價 12.03 USD (regularMarketTime 2026-10-14 20:00 UTC)。財報最新期為 2026-06-30 (Q2 2026)。唯一晚於 as-of 日期的項目是下一次財報日 2026-11-05, 屬 yfinance 預估日期。本報告為基本面分析, 不含交易建議。

## Executive summary

D-Wave Quantum (QBTS) 仍處於重度虧損與持續燒錢階段: TTM 營收僅 12.4M USD (YoY -0.6%), TTM FCF 為 -119.8M USD, 2026 年上半年現金及短期投資由 884.5M 降至 546.2M (含約 250.8M 收購現金支出)。估值方面, P/S 達 367.6x、EV/Revenue 達 320.5x, 股價已較 52 週高點 45.13 回落約 73%, 目前估值無法以傳統獲利或現金流倍數衡量, 價值高度依賴未來營收與技術里程碑的兌現。財務體質短期仍有流動性緩衝 (流動比率 20.5x, 淨現金約 498M USD), 但 6 個月內 0 筆公開市場買入與約 36.9M USD 的內部人賣出, 加上股本持續擴張, 對每股價值形成壓力。

## Revenue & profitability

- 營收規模: 年度 Total Revenue 為 2022 年 7.17M, 2023 年 8.76M, 2024 年 8.83M, 2025 年 24.59M USD。2022-2025 CAGR 為 50.8%, 但 2025 年營收的成長主要來自 Q1 2025 季度資料缺漏 (quarterly_fin 未提供 Q1 2025), 由年度減去 Q2-Q4 季度加總推得 Q1 2025 約 15.0M USD, 此推算無法驗證。若排除此異常, 2023-2024 營收基本持平 (2024 YoY +0.8%)。
- 季度趨勢: Q2 2026 營收 3.08M USD, 較 Q2 2025 的 3.10M 下降 0.6%。TTM 營收 12.43M USD, yfinance info 之 revenueGrowth 為 -0.6%, 與季度數據一致。
- 業務組合: longBusinessSummary 描述產品包括 Advantage / Advantage2 量子退火系統、Leap 雲端服務、Ocean SDK 與混合求解器服務, 但工具輸出未提供分部營收, 分部占比為 DATA_UNAVAILABLE。
- 毛利率: 年度 Gross Profit 2025 為 20.31M, 占營收 82.6%, 但 2025 年數字含上述推算的 Q1 異常項, 不宜直接外推。TTM 毛利為 7.98M, 毛利率 64.2%。季度毛利由 Q3 2025 的 2.67M 降至 Q2 2026 的 1.70M, 毛利絕對額持續走低。
- 營業利益率: 年度 Operating Income 2025 為 -100.37M, 占營收 -408%; 2024 為 -77.22M (-875%); TTM 營業利益 -170.58M, 占營收 -1,373%。Q2 2026 營業費用 54.98M, 較 Q2 2025 的 28.48M 增加 93%, 其中 R&D 由 12.69M 增至 28.24M (+122%)。yfinance info 的 operatingMargins 為 -17.32 (即 -1,732%), 與本報告以季度加總計算的 -1,373% 不一致, 以季度加總為本報告採用值。
- 淨利率: 年度 Net Income 2025 為 -355.06M, 2024 為 -143.88M, 2023 為 -82.72M, 2022 為 -53.70M。TTM 淨利 -248.70M, 淨利率 -2,002%。2025 年淨虧損含 Total Unusual Items -270.70M, yfinance 之 Normalized Income 2025 為 -84.36M。非經常項目組成 DATA_UNAVAILABLE, 無法逐項確認。
- ROE: yfinance info returnOnEquity 為 -27.99% (TTM)。以 2025 年淨利 / 平均股東權益 (852.2M 與 62.6M 平均) 估算約 -77.6%, 兩者口徑不同, 以 info 數值為報告值。
- ROIC (本報告推算): TTM 營業利益 -170.58M / (股東權益 1,083.1M + 總債務 48.1M - 現金及短期投資 546.2M) = 約 -29.2%。此為自行推算值, 非 yfinance 欄位。
- 季度 EPS: Q2 2026 Diluted EPS -0.13, Q1 2026 -0.05, Q4 2025 -0.12, Q3 2025 -0.41。

## Cashflow & balance sheet

現金流:
- 年度 Operating Cash Flow: 2025 -71.98M, 2024 -42.64M, 2023 -60.65M, 2022 -45.23M。
- TTM Operating Cash Flow -110.88M (Q3 2025 至 Q2 2026 加總), 與 info operatingCashflow 一致。
- TTM Capex 8.88M, TTM FCF (以季度 Free Cash Flow 加總) -119.76M, FCF margin 約 -964%。
- 2025 年度 FCF -76.29M, FCF margin -310%。
- FCF / NI 比率: 兩者皆為負數, 比率 n/m (不具意義), 不符合 >0.9 的健康標準。
- 資料差異: yfinance info freeCashflow 為 -73.38M, 與季度現金流表加總的 -119.76M 不一致。本報告以季度加總為準, 差異來源 DATA_UNAVAILABLE。
- SBC: 2025 年度 Stock Based Compensation 22.66M (占營收 92%), TTM SBC 31.13M。SBC 為非現金費用, 但實質為股東稀釋成本。

資產負債表 (2026-06-30):
- 現金及短期投資 (Cash, Cash Equivalents & STI) 546.2M, 其中現金及約當現金 296.6M, 其他短期投資 249.6M。較 2025-12-31 的 884.5M 減少 338.3M, 較 2025-06-30 的 819.3M 減少 33.3%。
- 總債務 (Total Debt) 48.1M, 含長期債務 34.9M 與資本租賃 13.1M。淨現金 = 546.2 - 48.1 = 約 498.1M USD。
- 流動比率 20.5x (流動資產 560.6M / 流動負債 27.3M), 2025-06-30 為 43.0x, YoY 下降約 52%。
- 負債 / 權益 (以 total debt / equity 計) 為 4.4%, 2025-06-30 為 5.8%。yfinance info debtToEquity 欄位 4.442 為百分比口徑, 非倍數。
- 商譽 Goodwill 342.6M (2026-03-31 起出現), 占總資產 1,158.4M 約 29.6%, 占股東權益 1,083.1M 約 31.6%。
- 收購: Q1 2026 Purchase of Business 現金支出 250.8M, Q2 2026 另有 2.0M。收購對象名稱與營收貢獻於工具輸出中 DATA_UNAVAILABLE。Q1 2026 之後營收仍持平, 收購對營收的實際貢獻未見於財報數據。
- 股東權益 Stockholders Equity 1,083.1M (2026-06-30), 2025-12-31 為 852.2M, 2025-06-30 為 694.3M。股東權益增加主要來自股權融資, 非獲利累積。
- 累積虧損 Retained Earnings -1,048.4M (2026-06-30)。

現金跑道 (本報告推算): 以 TTM FCF 平均每季 -29.9M 計, 現金約可支撐 18 季; 若以 2026 年上半年平均每季 FCF -39.7M 計, 約 13.8 季 (約 3.4 年), 未計入未來股權募資與收購支出。

## Capital allocation & insider signal

資本配置:
- 股利: 無 (Cash Dividends Paid 2021-2025 為 0 或 null, dividendYield 0.0)。
- 買回: 年度現金流量表無 Repurchase of Capital Stock 項目, 無買回紀錄。
- 股權融資: 2025 年 Net Common Stock Issuance 574.5M USD (2024 年為 214.2M)。2025 年 Q2 募資 527.7M, Q3 出現 -99.3M 的淨流出項目, 性質 DATA_UNAVAILABLE。
- 股本: Ordinary Shares Number 由 2022 年 113.3M 增至 2025 年 358.7M, 2026-06-30 為 372.0M。2026 年上半年股本增加 3.7%, YoY (2025-06-30 為 343.4M) 增加 8.3%。2025 年 Diluted Average Shares 321.2M, YoY +67%。
- 資本支出: 2025 年 Capex 4.31M (2024 年 2.40M), 占營收 17.5%, 絕對額小。TTM Capex 8.88M。
- 股息覆蓋率: 不適用 (無股息且淨利為負)。

內部人交易 (2026-04-15 至 2026-10-15, 6 個月):
- 公開市場賣出: 12 筆, 合計 1.408M 股, 總值約 36.88M USD。
- 公開市場買入: 0 筆。
- 其他: 衍生性證券行權 (conversion of exercise) 合計約 1.016M 股, 股票授予 (grant) 約 0.810M 股 (授予價格 0)。
- 主要賣方: CEO Alan E. Baratz (含 2026-06-08 約 687,627 股賣出價約 26.13 USD, 2026-04-30 授予 753,941 股), CFO John M. Markovich (2026-06-15 約 246,043 股, 價約 24.01-25.75; 2026-05-22 約 328,752 股, 價 27.70), General Counsel Diane Nguyen, 董事 John Dilullo, Rohit Ghai, Officer Sophie Ames。
- 淨買賣規模: 淨賣出約 36.88M USD, 占市值 4,566.9M 約 0.81%。以金額相對市值而言並不大, 但 0 筆買入、且賣出價格由 2026-05 的約 27.7 降至 2026-09 的約 18, 內部人方向一致偏向減持。
- 注意: 多筆賣出係行權後立即賣出 (衍生性證券行權價約 0.85-0.92 USD), 屬選擇權變現, 不能直接解讀為對公司前景的看法。

## Valuation

估值指標 (價格 12.03 USD):
- 市值 (marketCap) 4,566.9M USD; 企業價值 (EV) 3,982.3M USD。
- P/S (TTM): 367.6x。EV/Revenue (TTM): 320.5x。
- EV/EBITDA: -24.7x (EBITDA 為負, n/m)。yfinance 所列 TTM EBITDA -161.2M 與季度 EBITDA 加總 -262.6M 不一致, 以 info 為標示值但註明差異。
- P/FCF: n/m (TTM FCF 為負)。
- P/E (trailing): n/a (EPS 為負, info trailingEps -0.62)。
- Forward P/E: -31.9x (forwardEps -0.378, 負值, n/m)。Current year P/E -41.1x (epsCurrentYear -0.293)。
- P/B: 4.13x (bookValue 2.911/股)。
- 分析師: 16 家, 平均目標價 34.65, 中位數 36.0, 最高 43.0, 最低 18.36, recommendationMean 1.29 (strong_buy)。以目前股價計算, 平均目標價隱含上行約 188%, 與市價之間差距極大, 反映分析師對長期技術與市場假設的分歧。
- 股價動能: 52 週變動 -66.9%, 52 週區間 11.95-45.13, 股價低於 50 日均線 17.68 (-32.0%) 與 200 日均線 20.37 (-40.9%)。
- 風險: Beta 2.167; 空方持倉 70.9M 股, 占流通股約 21.2%, days to cover 4.53 (dateShortInterest 2026-09-30)。
- 與板塊比較: 板塊中位數 (估計) 見 Metrics table。P/S 367.6x 與 EV/Revenue 320.5x 為估計板塊中位數的數十倍, 估值完全不以目前營收為錨。

## Key catalysts

- 下一次財報: 2026-11-05 (yfinance earnings_dates 預估日期, 標示為 estimate), 分析師 EPS 預估 -0.09。
- 最近兩季財報:
  - 2026-08-06 (Q2 2026): EPS -0.13 vs 預估 -0.09, 差異 -42.2%。
  - 2026-05-12 (Q1 2026): EPS -0.05 vs 預估 -0.08, 差異 +34.5%。
- 歷史 EPS 表現: 近 17 筆有效 surprise 中, 11 筆為 miss, 6 筆為 beat。
- 收購整合: Q1 2026 收購 (現金 250.8M, 商譽 342.6M) 之後的營收貢獻、整合成本與商譽減損測試, 工具輸出 DATA_UNAVAILABLE。
- 指引 (guidance): 工具輸出未提供管理層財測或營收指引, DATA_UNAVAILABLE。
- 股權融資: 2025 年 Q2 之大規模募資 (527.7M) 與股本持續增加, 後續是否再募資為重要事件, 工具輸出無公告資料。
- 治理與人事: 公司 officers 清單中 Greg Golkov 標示為 Acting CFO (fiscal 2025), 但內部人交易資料顯示 John M. Markovich 以 CFO 身分於 2026 年仍有大量賣出, 兩者的現任職務需進一步確認。

## Metrics table

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 股價 (2026-10-14 收盤) | 12.03 USD | 52 週 -66.9% | n/a | 弱勢, 低於 50/200 日均線 |
| 市值 | 4,566.9M USD | n/a | n/a | 小型成長股 |
| 企業價值 EV | 3,982.3M USD | n/a | n/a | 估值脫離財務基本面 |
| TTM Revenue | 12.43M USD | -0.6% (Q2 26 vs Q2 25) | 估計: 數十 M 至數 B USD 不具可比性 | 規模極小 |
| 毛利率 (TTM) | 64.2% | 季度毛利絕對額 -13.8% (Q2 YoY) | 估計 55-60% | 中等, 但毛利額下降 |
| 營業利益率 (TTM) | -1,373% | 2025 年度 -408% | 估計 10-15% | 極差 |
| 淨利率 (TTM) | -2,002% | 2025 年度 -1,444% | 估計 8-12% | 極差 |
| ROE | -27.99% | n/a | 估計 10-15% | 極差 |
| ROIC (本報告推算) | 約 -29.2% | n/a | 估計 8-12% | 極差 |
| OCF (TTM) | -110.9M USD | 2025 年度 -72.0M | 估計為正 | 持續燒錢 |
| FCF (TTM) | -119.8M USD | 2025 年度 -76.3M | 估計為正 | 惡化 |
| FCF margin (TTM) | -964% | 2025 年度 -310% | 估計 10-20% | 極差 |
| FCF / NI | n/m (兩者皆負) | n/a | 估計 >0.9 為健康 | 不適用 |
| 現金及短期投資 | 546.2M USD | -33.3% (vs 2025-06-30) | n/a | 下降中, 含收購支出 |
| 淨現金 (cash+STI - total debt) | 約 498.1M USD | 約 -36% (vs 2025-06-30 約 779.3M) | n/a | 仍有緩衝 |
| 流動比率 | 20.5x | -52% (vs 2025-06-30 43.0x) | 估計 1.5-3.0x | 流動性極佳 |
| 總債務 / 股東權益 | 4.4% | 5.8% (2025-06-30) | 估計 30-60% | 槓桿極低 |
| 商譽 / 總資產 | 29.6% | 新增 (2025 年底為 0) | 估計低於 10% | 減損風險 |
| 股本 (流通) | 372.0M 股 | +8.3% | n/a | 稀釋中 |
| SBC (TTM) | 31.1M USD | 2025 年度 22.7M vs 2024 年度 15.7M (+45%) | 估計占營收低於 10% | 占營收比例極高 |
| Capex (TTM) | 8.9M USD | 2025 年度 4.3M (+約 80%) | n/a | 資本支出小 |
| 股利 / 買回 | 0 / 無 | n/a | 估計 多數科技股無股息 | 無資本回饋 |
| P/S (TTM) | 367.6x | n/a | 估計 4-8x | 極度偏高 |
| EV/Revenue (TTM) | 320.5x | n/a | 估計 4-8x | 極度偏高 |
| EV/EBITDA | -24.7x | n/a | 估計 15-25x | n/m (EBITDA 為負) |
| P/FCF | n/m | n/a | 估計 25-35x | n/m |
| Trailing P/E | n/a (EPS 為負) | n/a | 估計 20-30x | n/m |
| Forward P/E | -31.9x | n/a | 估計 20-30x | n/m |
| P/B | 4.13x | n/a | 估計 2-4x | 偏高 |
| 內部人 6 個月淨交易 | 賣出約 36.9M USD, 買入 0 | n/a | n/a | 偏空 (方向一致減持) |
| 內部人淨額 / 市值 | -0.81% | n/a | n/a | 規模小 |
| 分析師平均目標價 | 34.65 USD (隱含 +188%) | n/a | n/a | 分歧極大 |
| 空方持倉占流通股 | 21.2% | n/a | 估計 <5% 為常態 | 偏高, 軋空與波動風險 |
| Beta | 2.167 | n/a | 估計 1.0-1.3 | 波動極高 |

註: "Sector median (estimate)" 欄為分析師依 Technology / Computer Hardware 常見區間所作之粗估, 非 yfinance 工具輸出, 僅供量級參考。

## Red flags

- 營收幾乎停滯: TTM 營收 12.43M USD, Q2 2026 YoY -0.6%; 2023-2024 年度營收基本持平, 2025 年的大幅成長含無法驗證的 Q1 2025 數據。
- 營運虧損持續擴大: Q2 2026 營業費用 54.98M USD, 較 Q2 2025 增加 93%; R&D 增加 122%; 毛利絕對額連續下降。
- 燒錢速度加快: TTM FCF -119.8M USD; 2026 年上半年 OCF 已達 -73.5M USD, 超過 2025 年全年 OCF 的 -72.0M。
- 現金減少且含收購: 2026 年上半年現金及短期投資減少 338.3M USD, 其中收購約 252.8M USD。
- 商譽佔比高: 商譽 342.6M USD 占股東權益約 31.6%, 若收購綜效不如預期則存在減損風險。
- 股本持續稀釋: 2025 年 diluted average shares YoY +67%; 2026 年上半年流通股 +3.7%; 2025 年股權融資淨額 574.5M USD。
- 內部人淨減持: 6 個月內 12 筆公開市場賣出, 合計約 36.9M USD, 0 筆買入。
- 估值脫離基本面: P/S 367.6x, EV/Revenue 320.5x; 股價較 52 週高點回落 73%。
- 高空方持倉與高 Beta: 空方持倉占流通股 21.2%, Beta 2.17, 股價波動與軋空風險並存。
- 盈餘品質: 2025 年 Total Unusual Items -270.7M USD, 其組成 DATA_UNAVAILABLE; 季度淨利在 Q2 2025 與 Q3 2025 大幅波動 (-167.3M 與 -140.0M)。
- 資料一致性問題 (需人工確認):
  - yfinance info freeCashflow (-73.4M) 與季度加總 (-119.8M) 不一致。
  - TTM EBITDA (info -161.2M) 與季度加總 (-262.6M) 不一致。
  - info operatingMargins (-1,732%) 與本報告季度加總 (-1,373%) 不一致。
  - 2025 年 Q1 季度財報缺漏 (quarterly_fin 與 quarterly_bs 皆為 None)。
  - info 含 nameChangeDate 2026-10-15 與 prevName "DPCM Capital, Inc." (公司前身為 SPAC), 以及 ipoExpectedDate 2026-07-27 (與公司已上市多年之事實不符), 屬過時或錯誤欄位, 不採用。
  - 管理層: officers 清單 Golkov 為 Acting CFO, 但內部人交易資料顯示 Markovich 以 CFO 身分交易, 需確認現任 CFO。
- 治理風險分數 (yfinance): overallRisk 6, compensationRisk 8, shareHolderRightsRisk 8 (auditRisk 2, boardRisk 4)。

## Data gaps (DATA_UNAVAILABLE)

- 分部營收與業務組合占比。
- 管理層營收與獲利指引 (guidance)。
- 收購對象名稱、收購後營收貢獻與商譽減損測試。
- 2025 年 Q1 季度財報 (quarterly 欄位為 None)。
- 2025 年 Total Unusual Items -270.7M 之組成。
- Q3 2025 Net Common Stock Issuance -99.3M 之性質。
- 板塊中位數 (本報告所列為估計值, 非工具數據)。
- 最近一次公告的 Q2 2026 管理層說明與展望 (工具未提供)。
