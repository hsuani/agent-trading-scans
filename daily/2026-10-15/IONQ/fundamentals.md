# Fundamentals — IONQ as of 2026-10-15

## Executive summary
IonQ（IONQ，NYSE）仍處於高度虧損、以股權融資支撐營運的階段：TTM 營收 246.5M USD，TTM 營業利益 -1,006M USD（營業利益率 -408%），TTM FCF 約 -484M USD，FCF margin 約 -196%，財務健康度僅能依賴帳上現金支撐（現金及短期投資 2,119M USD，扣除債務後淨現金約 2,064M USD）。2026 年 Q2 EPS -5.08 與 GAAP 淨利大幅波動，主要來自非營業的投資公允價值變動（-1,649M USD），並非營運改善；2025 年股本由 221.9M 股增至 362.6M 股，SBC 達 TTM 450M USD（約為營收 183%），稀釋壓力極大。估值方面，P/S TTM 約 51.6x、EV/Revenue TTM 約 40.2x，EV/EBITDA、trailing P/E、forward P/E、P/FCF 皆為負值（n/m），目前無法以獲利型估值框架判斷便宜與否；分析師平均目標價 66.63 USD 對應現價 31.42 USD 的上行空間，但此為分析師預期而非基本面證據。

資料說明：本次所有數據來自 `pipeline/tools/yf` 本地快取（`"source": "cache"`，cached_at 2026-10-15T11:20:21Z），屬預期行為。最新財報期為 2026-06-30（Q2 FY2026，2026-08-05 公布）；下次財報日為 2026-11-04，位於 as-of 日期之後。未發現晚於 2026-10-15 的財報資料。

## Revenue & profitability

**營收與成長**
- 年度營收：2022 11.1M → 2023 22.0M → 2024 43.1M → 2025 130.0M USD。
- 2022–2025 三年 CAGR 約 126.9%；2025 YoY +201.9%。
- 季度營收（最近四季）：2025Q3 39.9M、2025Q4 61.9M、2026Q1 64.7M、2026Q2 80.1M USD。2026Q2 YoY +286.8%（yfinance `revenueGrowth` 2.868）。
- TTM 營收 246.5M USD（與 info 的 totalRevenue 246,474,000 一致）。
- 業務組合：yfinance 無分部營收拆分；`longBusinessSummary` 描述業務包含量子運算系統銷售與雲端存取（AWS Braket、Azure Quantum、Google Cloud Marketplace）、量子安全通訊與感測、半導體製造服務、維護與顧問服務。分部營收比重：DATA_UNAVAILABLE。

**毛利率趨勢（年度）**
- 2022 73.6% → 2023 63.2% → 2024 52.2% → 2025 40.4%（毛利 52.5M USD）。
- 季度毛利率持續走低：2025Q3 46.7%、2025Q4 29.6%、2026Q1 23.8%、2026Q2 24.9%。TTM 毛利 76.0M USD，毛利率 30.9%（info grossMargins 0.30854）。
- 解讀：營收快速擴張但單位經濟（成本結構）尚未改善，成本增速仍快於或接近營收增速。

**營業與淨利**
- 營業利益（年度）：2022 -85.7M、2023 -157.8M、2024 -232.5M、2025 -633.7M USD。營業利益率 2025 -487.4%。
- 季度營業利益：2025Q3 -168.8M、2025Q4 -228.6M、2026Q1 -271.5M、2026Q2 -337.2M USD；TTM -1,006.2M，營業利益率 -408%（info operatingMargins -4.08174）。
- 研發費用：2025 年 305.7M USD（營收 235%）；2026Q2 單季 160.6M USD。SG&A 2026Q2 150.5M USD。
- EBITDA：info 顯示 TTM EBITDA -793.1M USD；季度 EBITDA 加總約 -852M USD（-291.2、-228.4、-188.0、-144.6M），兩者來源口徑不同，以季度報表為準，差異需留意。
- 淨利（GAAP）：2025 -510.4M USD；季度 2025Q3 -1,055.0M、2025Q4 +753.7M、2026Q1 +805.4M、2026Q2 -1,867.7M USD。TTM 淨利 -1,363.7M USD（與 info netIncomeToCommon -1,363,670,016 一致）。
- 淨利波動來源：`Gain On Sale Of Security`（yfinance 標示，實質為非營業的投資損益）在 2026Q1 為 +1,057.6M、2026Q2 為 -1,649.1M USD。2026Q1 的 EPS +2.07（遠超一致預期 -0.52）與 2026Q2 的 EPS -5.08（一致預期 -0.60）均由此項主導，而非營運表現。營業層面 2026Q2 營業虧損擴大（-337.2M）。
- 每股盈餘：trailingEps -3.10；2025 年 diluted EPS -1.82（annual）。epsForward -1.29、epsCurrentYear -1.24（yfinance 欄位，期間定義未明）。
- ROE -60.5%、ROA -14.5%（info returnOnEquity、returnOnAssets）。
- ROIC：DATA_UNAVAILABLE（yfinance invested capital 與股東權益相同，無獨立資料；因 NOPAT 為負，ROIC 必為負）。

## Cashflow & balance sheet

**現金流品質**
- 營業現金流（OCF）：2022 -44.7M、2023 -78.8M、2024 -105.7M、2025 -283.2M USD。季度 OCF 2026Q1 -151.0M、2026Q2 -103.8M；TTM -452.4M（與 info operatingCashflow -452,368,992 一致）。
- 資本支出（PPE）：2025 年 16.4M USD；TTM 約 31.5M（季度加總）。CapEx 占 TTM 營收約 12.8%。
- FCF（OCF - CapEx）：2025 年 -299.6M USD，FCF margin -230.4%；季度加總 TTM -483.9M，FCF margin -196.3%。
- info 的 freeCashflow 為 -87.8M USD，與季度 OCF 減 CapEx 的推算值（約 -484M）不一致，以報表推算值為準，此欄位視為資料異常。
- FCF / NI 比率：NI 為負，比率無意義（n/m），依規定不可判定為健康或不健康；但 OCF 連續為負，現金流品質無法符合 > 0.9 的健康門檻。
- SBC（非現金費用）：2025 年 312.0M USD；TTM 約 450.0M USD，為 TTM 營收的 183%。若將 SBC 視為經濟成本，實際現金消耗與股權稀釋均遠高於 FCF 數字。
- 季度 OCF 與 FCF 方向一致為負，未見轉正跡象。

**資產負債表（2026-06-30）**
- 總資產 6,778.6M USD；股東權益 3,327.2M USD（2025 年底 3,799.5M，2026Q1 高點 4,976.0M）。
- 現金及等價物 1,235.7M；現金加短期投資（Cash, Cash Equivalents and Short Term Investments）2,119.0M USD（與 info totalCash 2,118.97M 一致）。
- 總債務 54.5M USD（yfinance 以 capital lease obligations 呈現），淨現金約 2,064.5M USD（淨負債為負）。
- 流動比率 10.66、速動比率 9.92（info currentRatio、quickRatio），流動性極高。
- 負債/權益：info debtToEquity 為 1.632（yfinance 以百分比表示），換算 D/E 約 0.016x（1.6%），槓桿極低。
- 總負債 2026-06-30 為 3,439.0M USD，較 2026Q1 的 1,704.0M 大幅增加。扣除流動負債 226.1M 與債務 54.5M 後，非流動其他負債約 3,158.5M USD；其組成（如遞延稅、或有對價、衍生性負債或其他）yfinance 無法提供，標記為 DATA_UNAVAILABLE，需以 10-Q 附註確認。
- 商譽 2,186.0M USD，占總資產約 32%；2025 年底為 1,963.6M，2025 年 6 月僅 370.7M，顯示 2025 年下半年起發生大規模收購。有形淨資產 2026-06-30 為 362.4M USD（2026Q1 為 2,067.2M，2025Q3 為 -248.4M），波動劇烈。
- 存貨 87.5M（2026Q2），應收帳款 37.3M。

## Capital allocation & insider signal

**資本配置**
- 股利：無（dividendYield 0.0）；股利覆蓋率 n/a。
- 買回：無（yfinance 未見回購現金流）。
- 股權融資：2025 年普通股發行淨額 3,312.5M USD（2025Q3 1,000.0M、2025Q4 1,954.3M）。2024 年與 2023 年均為 0。
- 股數變化：流通股數 2024 年底 221.9M → 2025 年底 362.6M（+63%）→ 2026-06-30 381.0M（半年再 +5.1%）→ info sharesOutstanding 405.1M（+11.7% 相對 2025 年底）。持續稀釋。
- 資本支出趨勢：2022 9.3M → 2023 13.7M → 2024 18.0M → 2025 16.4M USD，規模仍小。
- 收購：2024 年 15.5M；2025 年下半年與 2026 年有明顯商譽增加（見上），收購對價與型態需以 10-Q 確認。

**內部人交易（2026-04-15 至 2026-10-15，約 6 個月）**
- 公開市場賣出：6 筆，合計 18,009 股，約 903,303 USD（RAYMOND JOHN W. 2026-06-18 約 209,863 USD、2026-09-10 約 89,564 USD；CARDILLO ROBERT THOMAS 2026-05-06 約 188,273 USD、2026-04-16 約 112,250 USD；CHOU KATHRYN K 2026-06-18 約 151,690 USD；TOLEDANO GABRIELLE B 2026-06-18 約 151,663 USD）。
- 公開市場買入：無。
- 授予（Stock Award）：多筆董事與 CEO 股票獎勵（例如 2026-06-17 五位董事各 4,526 股；2026-08-24 BAXTER TIMOTHY E 與 BALL ERIC R 各 5,540 股），不計入買賣淨額。
- 期權行使（derivative conversion）：CARDILLO 等人的行使-賣出配對，屬行權後賣出。
- 淨額：約 -903K USD 淨賣出，相對市值 12,729M USD 約 0.007%，規模極小，對基本面訊號強度為弱。
- 較早期（2025 年 6 月）內部人賣出規模遠大於本期，例如 DE MASI NICCOLO M 2025-06-11 賣出 2,597,500 股（約 104.8M USD）、CHAPMAN PETER HUME 2025-06-17/20 大量賣出（合計約 230M USD 量級），屬本次視窗外歷史資料，僅供背景。
- 內部人持股 0.72%（heldPercentInsiders 0.00717）。

**機構持股**
- 機構持股 50.8%（heldPercentInstitutions 0.50772），機構數 1,044。
- 前十大（2026-06-30 季報）：Morgan Stanley 6.9%（+24.2% QoQ）、BlackRock 5.48%（-30.0%）、Vanguard Capital Management 4.09%（+3.6%）、Vanguard Portfolio Management 3.66%（-9.3%）、State Street 2.13%（-12.4%）、UBS 2.07%（+36.0%）、Geode 1.70%（-23.5%）、Bank of America 1.70%（+258%）、Norges Bank 1.36%（+16.6%）、Marex 0.97%（-7.5%）。
- 空頭：shortPercentOfFloat 10.08%（sharesShort 40.6M）、shortRatio 1.66 天，空單壓力中等。

## Valuation

- 現價：31.42 USD（fast_info / info regularMarketPrice，cache 來源）；前收 34.73 USD，盤中跌幅 -9.53%（info regularMarketChangePercent）。quote 時戳與 marketState（PRE）存在不一致，交易前須重新確認報價。
- 市值：12,729M USD（info marketCap；31.42 × 405.1M 股）。企業價值（EV）9,919M USD。
- 價格位置：52 週區間 25.89–73.87 USD（現價距高點 -57.5%、距低點 +21.4%）；50 日均線 41.25（-23.8%）；200 日均線 43.12（-27.1%）。
- Beta 3.361。
- P/E trailing：n/m（EPS -3.10）。P/E forward：n/m（-24.3）。
- P/S TTM：51.6x（info priceToSalesTrailing12Months）。
- EV/Revenue TTM：40.2x（info enterpriseToRevenue）。
- EV/EBITDA：-12.5x（info enterpriseToEbitda，EBITDA 為負，n/m）。
- P/FCF：n/m（FCF 為負）。
- P/B：3.6x（priceToBook 3.598；bookValue 8.732 USD/股）。
- 同業中位數（sector median）：DATA_UNAVAILABLE（工具未提供產業同業倍數）。定性上，量子運算同業普遍仍為虧損，故 P/S 絕對水準偏高，需與同業實際倍數比較後再下判斷。
- 分析師共識（14 位）：recommendationMean 1.36（strong_buy）；目標價平均 66.63、中位數 62.5、最高 100.0、最低 41.85 USD。平均目標價相對現價 +112%。分析師目標價為預期值，非基本面證據。

## Key catalysts

- 下次財報：2026-11-04（earnings_dates 首筆，EPS 一致預期 -0.81），位於 as-of 日期之後。
- 上次財報（2026-08-05）：EPS -5.08 vs 預期 -0.60，surprise -748.6%；營收 80.1M USD（YoY +286.8%）。
- 前次財報（2026-05-06）：EPS 2.07 vs 預期 -0.52，surprise +498.9%（非營運損益主導）。
- 業務面：營收動能強（Q2 YoY +286.8%），但毛利率持續走低；需觀察 2026Q3 毛利率能否止跌回升，以及 R&D 與 SG&A 增速是否收斂。
- 資本面：現金 2,119M USD 按 Q2 FCF 年化速度（約 -456M USD/年）估算約 4.6 年消耗量，但若持續稀釋或收購，實際耗用率將變動。
- 非營業損益：Q1 與 Q2 的投資公允價值變動幅度超過 1B USD，會直接改變 GAAP EPS 符號，財報解讀時應拆分營業與非營業項目。
- 股權結構：空單占流通股 10.1%，股數持續增加。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 TTM (USD) | 246.5M | +286.8%（2026Q2 單季） | DATA_UNAVAILABLE | 高成長，但基數小 |
| 營收 3Y CAGR (2022–2025) | 126.9% | 2025 YoY +201.9% | DATA_UNAVAILABLE | 成長強勁 |
| 毛利率（TTM） | 30.9% | 2025 年 40.4% vs 2024 52.2%（-11.8pp） | DATA_UNAVAILABLE | 走弱 |
| 營業利益率（TTM） | -408% | 2025 -487% vs 2024 -540%（改善） | DATA_UNAVAILABLE | 嚴重虧損 |
| 淨利率（TTM） | -553% | 非營業損益主導，波動大 | DATA_UNAVAILABLE | 不具可比性 |
| ROE | -60.5% | n/a | DATA_UNAVAILABLE | 負值 |
| ROA | -14.5% | n/a | DATA_UNAVAILABLE | 負值 |
| ROIC | DATA_UNAVAILABLE | n/a | DATA_UNAVAILABLE | 無法判定（NOPAT 為負） |
| OCF（TTM, USD） | -452.4M | 2025 -283.2M（較 2024 -105.7M 惡化） | DATA_UNAVAILABLE | 惡化 |
| FCF（TTM, USD） | -483.9M | 2025 -299.6M | DATA_UNAVAILABLE | 持續燒錢 |
| FCF margin（TTM） | -196.3% | 2025 -230.4% | DATA_UNAVAILABLE | 差 |
| FCF / NI | n/m（NI 為負） | n/a | DATA_UNAVAILABLE | 無法判定 |
| SBC / 營收（TTM） | 183% | 2025 年 SBC 312.0M，較 2024 106.9M 增 192% | DATA_UNAVAILABLE | 極高，稀釋風險高 |
| 現金及短期投資（USD） | 2,119.0M | 2025 年底 2,392.2M（-11.4%） | DATA_UNAVAILABLE | 流動性充足 |
| 總債務（USD） | 54.5M | 2025 年底 30.0M（+81.5%） | DATA_UNAVAILABLE | 低槓桿 |
| 淨現金（USD） | 2,064.5M | n/a | DATA_UNAVAILABLE | 具淨現金 |
| 流動比率 | 10.66 | n/a | DATA_UNAVAILABLE | 極佳 |
| 速動比率 | 9.92 | n/a | DATA_UNAVAILABLE | 極佳 |
| D/E | 0.016x（1.6%） | n/a | DATA_UNAVAILABLE | 低 |
| 總負債（USD） | 3,439.0M | 2026Q1 1,704.0M（+102%） | DATA_UNAVAILABLE | 需查明組成 |
| 股東權益（USD） | 3,327.2M | 2025 年底 3,799.5M（-12.4%） | DATA_UNAVAILABLE | 下降中 |
| 有形淨資產（USD） | 362.4M | 2026Q1 2,067.2M | DATA_UNAVAILABLE | 波動劇烈 |
| 流通股數 | 405.1M（info） | 2025 年底 362.6M，+11.7%；2024 年底 221.9M，2025 年 +63% | DATA_UNAVAILABLE | 高度稀釋 |
| 股利殖利率 | 0.0% | n/a | DATA_UNAVAILABLE | 不適用 |
| 股權融資（2025, USD） | 3,312.5M | 2024 為 0 | DATA_UNAVAILABLE | 依賴外部募資 |
| 內部人淨買賣（6 個月） | 淨賣出約 903K USD | 無公開市場買入 | DATA_UNAVAILABLE | 規模小，弱負面 |
| 機構持股比例 | 50.8% | n/a | DATA_UNAVAILABLE | 中高 |
| 空單占流通股 | 10.1% | n/a | DATA_UNAVAILABLE | 中等 |
| Trailing P/E | n/m（EPS -3.10） | n/a | DATA_UNAVAILABLE | 無法使用 |
| Forward P/E | n/m（-24.3） | n/a | DATA_UNAVAILABLE | 無法使用 |
| EV/EBITDA | -12.5x（n/m） | n/a | DATA_UNAVAILABLE | 無法使用 |
| EV/Revenue（TTM） | 40.2x | n/a | DATA_UNAVAILABLE | 極高 |
| P/S（TTM） | 51.6x | n/a | DATA_UNAVAILABLE | 極高 |
| P/FCF | n/m（FCF 為負） | n/a | DATA_UNAVAILABLE | 無法使用 |
| P/B | 3.6x | n/a | DATA_UNAVAILABLE | 偏高 |
| 分析師平均目標價（USD） | 66.63（相對現價 +112%） | n/a | DATA_UNAVAILABLE | 分析師樂觀，僅供參考 |
| Beta | 3.36 | n/a | DATA_UNAVAILABLE | 波動極高 |

## Red flags
- 獲利與現金流：TTM 營業利益 -1,006M USD、FCF -484M USD，OCF 連續多年為負且 2025 年惡化；FCF / NI 與 OCF 健康門檻均無法達成。
- 稀釋：SBC TTM 450M USD（營收 183%）；流通股數 2024 年底至 2025 年底 +63%，2026 年再增；2025 年股權融資 3,312.5M USD。
- 盈餘品質：GAAP EPS 由非營業投資公允價值變動主導（2026Q1 +1,057.6M、2026Q2 -1,649.1M），EPS 符號與營運表現不一致，不宜以單季 EPS 判斷趨勢。
- 毛利率下滑：年度由 73.6%（2022）降至 40.4%（2025）；季度由 46.7%（2025Q3）降至 23.8%（2026Q1）、24.9%（2026Q2）。
- 負債端不透明：2026-06-30 總負債單季增加 1,735M USD 至 3,439M USD，非流動其他負債約 3,158M USD，組成 DATA_UNAVAILABLE。
- 股東權益與有形淨資產劇烈波動：股東權益 2026Q1 4,976M → 2026Q2 3,327M；有形淨資產 2,067M → 362M。商譽占總資產 32%，減損風險需關注。
- 資料一致性：info freeCashflow（-87.8M）、info EBITDA（-793M）與季度報表推算值（FCF 約 -484M、EBITDA 約 -852M）不一致；info debtToEquity 為百分比單位，需換算。
- 估值：P/S 51.6x、EV/Revenue 40.2x，無任何獲利型估值指標可用；以 DCF 或同業比較判定估值需仰賴未來營收假設。
- 市場風險：Beta 3.36、52 週跌幅約 -47%（yfinance fiftyTwoWeekChangePercent -47.05%）、股價低於 50 日與 200 日均線約 24% 與 27%、空單占流通股 10.1%。
- 治理風險：info overallRisk 10（yfinance 治理評分，滿分 10 為最高風險）、compensationRisk 10。
- 報價時點：現價 31.42 來自 cache，quote 時戳與 marketState 不一致，需交易前確認。

FUNDAMENTALS REPORT COMPLETE
