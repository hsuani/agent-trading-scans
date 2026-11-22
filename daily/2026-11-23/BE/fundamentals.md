# Fundamentals — BE (Bloom Energy Corporation) as of 2026-11-23

資料說明：本報告以 `pipeline/tools/yf` 取得資料，工具回傳來源為 repo cache（`cached_at` 2026-11-22 14:30 UTC），即時來源未取得。最新可用股價為 2026-11-20 收盤（`regularMarketTime` 2026-11-20 21:00 UTC），未取得 2026-11-23 股價。未發現任何晚於 2026-11-23 的資料。單位：USD，以 B / M 表示；本報告不含 TWD / KRW 金額。Serenity 提及 BE 與 NBIS 的脈絡屬於外部背景，本報告未驗證該說法。

## Executive summary

BE 在 2026 年 Q3 已由虧損轉為明顯獲利（Q3 營收 1235.8M USD，年增 138.1%，營業利益率 18.2%，GAAP 淨利 250.3M USD），TTM 營收約 3.83B USD，財務體質在損益面明顯改善。然而 Q3 單季自由現金流為 -180.6M USD，應收與存貨大幅增加，同期股本增加約 25%、總債務升至 2.78B USD，現金流與資本結構的品質仍是主要風險。估值方面，trailing P/E 約 86.3x、EV/EBITDA 約 70x、P/FCF 約 96x，遠高於一般工業設備股，前瞻 P/E 26.7x 則建立在大幅成長的 FY2027 盈餘預估上；股價在 11-20 單日下跌 15.3%，距 52 週高點 351.28 USD 已回落約 59.5%，同期內部人在 6 個月內淨賣出約 42.7M USD、無公開市場買入。

## Revenue & profitability

**營收趨勢**（單位 M USD，來源 `financials` 與 `quarterly_fin`）

| 年度 | 營收 | 年增 | 毛利率 | 營業利益率 | 淨利率 |
|---|---|---|---|---|---|
| 2022 | 1199.1 | n/a | 12.4% | -21.8% | -25.1% |
| 2023 | 1333.5 | +11.2% | 14.8% | -15.7% | -22.7% |
| 2024 | 1473.9 | +10.5% | 27.5% | 1.6% | -2.0% |
| 2025 | 2024.0 | +37.3% | 29.0% | 3.6% | -4.4% |

- 3 年 CAGR（2022–2025）約 19.1%，2 年 CAGR（2023–2025）約 23.2%。yfinance 2021 年數據為 null，5 年 CAGR 為 DATA_UNAVAILABLE。
- 季度動能明顯加速：2025Q3 519.0M、2025Q4 777.7M、2026Q1 751.1M、2026Q2 1065.4M、2026Q3 1235.8M，Q3 季增 16.0%，年增 138.1%。
- 2026 年 TTM 營收合計約 3830.0M USD，與 `info.totalRevenue` 3829.9M 吻合。
- 毛利率持續改善：季度毛利率由 2025Q3 的 29.2% 升至 2026Q3 的 33.8%；TTM 毛利率約 32.3%（`info.grossMargins` 為 31.8%，口徑略有差異）。
- 營業利益率：2025Q3 1.5%、2025Q4 11.3%、2026Q1 9.6%、2026Q2 17.1%、2026Q3 18.2%；TTM 營業利益約 567.3M USD，TTM 營業利益率約 14.8%。
- 獲利品質需留意：2025Q4 GAAP 淨利僅 1.1M USD，當季含 -66.4M USD 非經常項目與 -20.8M USD 權益法損益；2025 全年權益法損益為 -40.4M USD。
- 段落與分部（segment）營收占比：DATA_UNAVAILABLE。`longBusinessSummary` 僅描述產品（Energy Server 固態氧化物燃料電池、Electrolyzer 製氫）與客戶類別（公用事業、資料中心、零售、醫療、教育、電信、製造業），未提供分部營收。

**獲利能力**
- 淨利率：TTM 約 13.5%（`info.profitMargins` 13.53%），2025 全年為 -4.4%。
- ROE：yfinance 39.6%（以平均權益計算，與本報告以 Q3'25 與 Q3'26 權益平均推估的約 40% 相符）；以期末權益計算約 26.8%。
- ROIC（本報告估算）：以 TTM 營業利益 × (1 - 25.57% 稅率) 除以期末 (總債務 + 權益 - 現金) 得約 18.9%，屬估算值。
- 2025 年 `info.returnOnAssets` 為 7.45%。

## Cashflow & balance sheet

**現金流**（單位 M USD，來源 `quarterly_cf`，TTM 為本報告以 2025Q4 至 2026Q3 四季加總）

| 期間 | 營業現金流 | 資本支出 | 自由現金流 |
|---|---|---|---|
| 2025 全年 | 113.9 | -56.8 | 57.2 |
| 2025Q4 | 418.1 | -23.0 | 395.1 |
| 2026Q1 | 73.6 | -26.2 | 47.4 |
| 2026Q2 | 226.4 | -51.6 | 174.8 |
| 2026Q3 | -27.1 | -153.5 | -180.6 |
| TTM（本報告加總） | 691.0 | -254.3 | 436.7 |

- TTM 自由現金流利潤率約 11.4%；FCF / NI（TTM）約 0.84，低於 0.9 的健康門檻；OCF / NI 約 1.33。
- Q3 2026 營運現金流轉負，主要受營運資金拖累（變動營運資金 -356.0M USD，其中應收帳款相關 -605.6M、存貨 -170.4M）。
- `info.freeCashflow` 為 -1.7M USD，與本報告以 OCF 減資本支出推算的 436.7M 差距很大，口徑不一致，本報告以季度加總為準並標示此差異。
- 2025 年股權激勵（SBC）為 139.4M USD；TTM SBC 約 201.8M USD，約占 TTM 營收 5.3%。

**資產負債表**（單位 M USD，來源 `quarterly_bs`，最新為 2026-09-30）
- 現金及約當現金：2486.7M（2025Q3 為 595.1M）。
- 總債務：2783.4M（2025Q3 為 1513.4M；2025 年底為 2992.0M，2025 年發行約 2500M 債務、償還約 978.8M）。其中長期債務 2473.5M。
- 淨債務（本報告計算）：約 296.7M（總債務減現金）。`annual balance_sheet` 內的 `Net Debt` 欄位 2025 年為 163.8M，與本報告口徑不同，本報告不採用該欄。
- 負債權益比（總債務 / 權益）：144.0%（2025Q3 為 231.7%）；`info.debtToEquity` 為 141.9%。
- 流動比率：3.74（`info.currentRatio`，與本報告計算 5207.8 / 1391.8 一致），2025Q3 為 4.39。流動負債自 2025 年底 623.8M 增至 2026Q3 的 1391.8M。
- 利息保障倍數（TTM 營業利益 / TTM 利息費用 35.6M）：約 15.9x。
- 存貨：927.7M（2025 年底 643.3M，季增 44.2%）。
- 應收（yfinance `Receivables` 總計）：1465.5M（季增 64.3%）；其中應收帳款（`Accounts Receivable`）為 634.7M。總計欄位組成未逐項拆解，需進一步核對是否包含非流動或其他應收項目。
- 有形帳面價值：1717.3M（2026Q3）。
- 股本（已發行普通股）：295.5M 股（2025Q3 為 236.4M，年增 25.0%）。

## Capital allocation & insider signal

**資本配置**
- 資本支出：TTM 254.3M USD，為 2025 全年 56.8M 的 4.5 倍；Q3 單季 153.5M（2025Q3 為 12.3M），顯示產能擴張明顯啟動。資本支出占 TTM 營收約 6.6%。
- 股利：近期為零（2025 年現金股利 0.9M USD，TTM 為 0）；`info.dividendYield` 0.0%。
- 買回：現金流量表未見買回項目，本報告未發現買回。
- 股權稀釋：普通股數由 2025Q3 236.4M 增至 2026Q3 295.5M（+25.0%）；加權稀釋股數由 234.9M 增至 324.3M（+38.0%）。現金流量表中股權發行金額有限（Q3 約 10.8M），稀釋來源需進一步確認（例如股權激勵、可轉換債券轉換或市場增發），本報告無法從工具資料判定。
- 負債籌資：2025 年底大量發債（2500M），使總債務大幅提高；利息費用 2026Q3 為 7.5M，相對 TTM 營業利益偏低。

**內部人交易**（來源 `insider`，時間窗 2026-05-23 至 2026-11-23）
- 買進：0 筆、0 USD。
- 賣出：合計約 42.7M USD（以 `Value` 加總），約占市值 42.1B USD 的 0.10%。
- 主要賣出：JOHN T. CHAMBERS（間接持有）於 2026-05-28 以 297.69 USD 賣出 55,000 股（約 16.4M USD），2026-08-13 以 250 USD 賣出 15,000 股，2026-11-02 以 203.43 USD 賣出 8,828 股；JEFFREY R. IMMELT 於 2026-08-17 以 238.91 USD 賣出 30,000 股（約 7.2M USD）；AMAN JOSHI（CCO）多次賣出，合計約 5.6M USD；SODERBERG、CHITOORI 等高階主管亦有賣出。
- 最近一週（2026-11-16）高階主管以約 178.4–178.5 USD 賣出，當時股價已自 2026 年 6-7 月的約 290–300 USD 回落。
- CEO K.R. SRIDHAR 於 2026-08-31 有 300,000 股贈與（Stock Gift），2026-09-01 有 9,688 股衍生性證券轉換（行權價 30.96），未見公開市場賣出；本報告未見其 6 個月內的買入。
- 解讀：賣出金額相對市值比例很小，但方向一致（無買進、多名高階主管與董事賣出），股價大幅回落後仍有賣出，屬偏負面的內部人訊號。未見 10b5-1 計畫之標示，無法判定是否為預先安排。

**機構與持股**
- 機構持股比例 81.7%（機構數 1865）；內部人持股 5.5%。
- 2026Q3 前十大機構多數增持：BlackRock 8.32%（+33.4%）、Vanguard Capital Management 6.35%（+55.5%）、Ameriprise 6.23%（+1.6%）、State Street 4.19%（+96.4%）、Geode 2.39%（+85.9%）。
- 空單：空單股數 17.69M，占流通股 6.81%，回補天數 1.19 天；前月空單 20.98M，較前月下降約 15.7%。

## Valuation

**估值指標**（股價 142.39 USD，市值 42.10B USD，企業價值 EV 42.43B USD（yfinance）；本報告以 Q3 資產負債表計算 EV 約 42.40B USD）

- trailing P/E：86.3x（`info.trailingPE` 86.3；TTM EPS 1.65）。
- forward P/E：26.7x（`info.forwardPE`；`epsForward` 5.32 USD，依 yfinance 為 FY2027 預估）。
- FY2026 預估 P/E：43.5x（`epsCurrentYear` 3.27 USD）。
- EV/EBITDA（TTM）：約 70.3x（EV 42.43B / TTM EBITDA 603.0M，`info.ebitda`）。yfinance 年度 EBITDA 2025 為 20.1M，與 TTM 口徑不一致，本報告採用 `info.ebitda`。
- P/FCF（TTM，本報告推算）：約 96.4x（市值 / 436.7M）；`info.freeCashflow` 為負值，依規則以本推算值呈現並註明。
- P/S（TTM）：11.0x。
- P/B：21.8x。
- 同業 / 產業中位數（Electrical Equipment & Parts，Industrials）：DATA_UNAVAILABLE，本報告不提供估計值。

**分析師共識**（來源 `info`，26 位分析師）
- 平均評等 2.10（Buy）；平均目標價 282.69 USD（較現價 +98.5%），中位數 295.0 USD，最高 380.0 USD，最低 102.0 USD（較現價 -28.4%）。
- Beta 3.618，屬高波動標的。

**股價位置**
- 52 週區間 75.70–351.28 USD；現價距 52 週高點 -59.5%。
- 距 50 日均線（234.02 USD）-39.2%，距 200 日均線（223.89 USD）-36.4%。
- 2026-11-20 單日跌 15.3%（由 168.11 跌至 142.39），盤後 145.55 USD。單日下跌原因未從工具資料取得：DATA_UNAVAILABLE。

## Key catalysts

- 下次財報：yfinance `earnings_dates` 最前一筆為 2027-02-04（EPS 預估 1.12 USD），對應 FY2026 Q4 與全年結果；`info.earningsTimestamp` 為 2026-10-22，即上一季（2026Q3）財報。
- 上一季（2026Q3，2026-10-22）：調整後 EPS 0.94 USD，較預估 0.68 USD 高 39.2%。
- 近幾季 GAAP 與公司報告 EPS 差距明顯：2026Q1 GAAP 稀釋 EPS 0.23 vs 報告 0.44；2026Q2 0.62 vs 0.78；2026Q3 0.78 vs 0.94。報告數字應為非 GAAP 口徑，本報告以 GAAP 為獲利品質判斷基準。
- 公司指引（guidance）：DATA_UNAVAILABLE（工具未提供管理層指引原文）。
- 分部或產品組合變化：DATA_UNAVAILABLE。
- 產能與資本支出：Q3 資本支出 153.5M USD 已反映擴產投入，後續產能投產時點與營收認列時程需由公司公告確認。
- 分析師目標價區間 102–380 USD，中位數 295 USD，為市場預期分歧較大的指標。

## Red flags

- 自由現金流轉負：2026Q3 FCF -180.6M USD，營運現金流 -27.1M USD，主因應收與存貨大幅增加（變動營運資金 -356.0M USD）。
- 營運資金壓力升高：應收總計季增 64.3%，存貨季增 44.2%，流動負債一年間增加約 2.2 倍，需確認收款節奏與客戶結構。
- 股本快速稀釋：普通股年增 25.0%、加權稀釋股數年增 38.0%，每股獲利成長被稀釋效應部分抵銷。
- 內部人淨賣出：6 個月約 42.7M USD 賣出、零買進，賣出者包括多名高階主管與持股人（間接持有）；CEO 未見公開市場賣出；股價回落後賣出仍在進行。
- 估值極高：trailing P/E 86.3x、EV/EBITDA 約 70x、P/FCF 約 96x，獲利必須持續高速成長才能支撐。
- 股價劇烈波動：52 週內由 351.28 回落至 142.39，11-20 單日 -15.3%，Beta 3.6；單日下跌原因 DATA_UNAVAILABLE。
- 獲利品質：GAAP 與報告 EPS 差距每季約 0.16 USD；2025Q4 GAAP 淨利接近零（含 -66.4M 非經常項目與權益法損益）；2025 全年 GAAP 淨利 -88.4M USD。
- 債務規模擴大：總債務由 2024 年底 1529.8M 增至 2026Q3 2783.4M，2025 年發行約 2500M 債務；雖目前利息費用低，但長期償付與再融資風險需追蹤。
- 資料品質：yfinance `freeCashflow` 為 -1.7M USD，與季度加總 436.7M 不一致；`EBITDA` 年度與 TTM 口徑不同；`Net Debt` 欄位與總債務減現金不一致；本報告採用可驗證的季度加總與公式計算，並已標示。
- 資料來源：本次為 cache 資料（cached_at 2026-11-22 14:30 UTC），未取得 2026-11-23 股價，部分欄位（指引、分部、同業中位數）為 DATA_UNAVAILABLE。

## Metrics table

單位：營收、利潤、現金流、資產負債表為 M USD；市值與 EV 為 B USD；股價為 USD。Sector median 全數為 DATA_UNAVAILABLE。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收（TTM，M USD） | 3830.0 | n/a（TTM 去年同期 DATA_UNAVAILABLE） | DATA_UNAVAILABLE | 高速成長 |
| 營收（2026Q3 單季，M USD） | 1235.8 | +138.1% | DATA_UNAVAILABLE | 高速成長 |
| 營收 3 年 CAGR（2022–2025） | 19.1% | n/a | DATA_UNAVAILABLE | 成長穩健 |
| 毛利率（2026Q3 單季） | 33.8% | +4.6 pp（2025Q3 29.2%） | DATA_UNAVAILABLE | 改善 |
| 營業利益率（TTM） | 14.8% | 2025 全年 3.6%（+11.2 pp） | DATA_UNAVAILABLE | 改善 |
| 淨利率（TTM） | 13.5% | 2025 全年 -4.4% | DATA_UNAVAILABLE | 轉正 |
| ROE（yfinance，平均權益） | 39.6% | n/a | DATA_UNAVAILABLE | 高，但權益基數快速擴大 |
| ROIC（本報告估算） | 18.9% | n/a | DATA_UNAVAILABLE | 尚可，屬估算 |
| 營業現金流（TTM，M USD） | 691.0 | n/a | DATA_UNAVAILABLE | 改善但季度波動大 |
| 自由現金流（TTM，M USD，本報告推算） | 436.7 | 2025 全年 57.2 | DATA_UNAVAILABLE | 轉強但 Q3 為負 |
| 自由現金流利潤率（TTM） | 11.4% | n/a | DATA_UNAVAILABLE | 尚可 |
| FCF / NI（TTM） | 0.84 | n/a | >0.9 為健康門檻 | 略低於門檻 |
| 自由現金流（2026Q3 單季，M USD） | -180.6 | 2025Q3 +7.4 | DATA_UNAVAILABLE | 偏弱 |
| 資本支出（TTM，M USD） | 254.3 | 2025 全年 56.8（4.5 倍） | DATA_UNAVAILABLE | 擴產中，壓縮 FCF |
| 現金及約當現金（M USD） | 2486.7 | +317.9%（2025Q3 595.1） | DATA_UNAVAILABLE | 充裕 |
| 總債務（M USD） | 2783.4 | +83.9%（2025Q3 1513.4） | DATA_UNAVAILABLE | 偏高 |
| 淨債務（M USD，本報告計算） | 296.7 | n/a | DATA_UNAVAILABLE | 可控 |
| 負債權益比（總債務 / 權益） | 144.0% | 2025Q3 231.7% | DATA_UNAVAILABLE | 仍偏高，但較去年改善 |
| 流動比率 | 3.74 | 2025Q3 4.39 | DATA_UNAVAILABLE | 良好 |
| 利息保障倍數（TTM） | 15.9x | n/a | DATA_UNAVAILABLE | 良好 |
| 普通股股數（M 股） | 295.5 | +25.0%（2025Q3 236.4） | DATA_UNAVAILABLE | 稀釋明顯 |
| 加權稀釋股數（M 股） | 324.3 | +38.0%（2025Q3 234.9） | DATA_UNAVAILABLE | 稀釋明顯 |
| 股權激勵（TTM，M USD） | 201.8 | 占營收 5.3% | DATA_UNAVAILABLE | 偏高 |
| 內部人 6 個月淨買賣（M USD） | -42.7（買進 0） | 占市值 0.10% | DATA_UNAVAILABLE | 偏負面 |
| 空單占流通股 | 6.81% | 前月空單股數 -15.7% | DATA_UNAVAILABLE | 中性 |
| 市值（B USD） | 42.10 | n/a | DATA_UNAVAILABLE | 大型成長股 |
| trailing P/E | 86.3x | n/a | DATA_UNAVAILABLE | 極高 |
| forward P/E | 26.7x | n/a | DATA_UNAVAILABLE | 高，依賴 FY2027 成長 |
| EV/EBITDA（TTM） | 70.3x | n/a | DATA_UNAVAILABLE | 極高 |
| P/FCF（TTM，本報告推算） | 96.4x | n/a | DATA_UNAVAILABLE | 極高 |
| P/S（TTM） | 11.0x | n/a | DATA_UNAVAILABLE | 高 |
| P/B | 21.8x | n/a | DATA_UNAVAILABLE | 高 |
| 股價（2026-11-20 收盤，USD） | 142.39 | 距 52 週高點 -59.5%；單日 -15.3% | DATA_UNAVAILABLE | 大幅回落 |
| 分析師平均目標價（USD） | 282.69 | 較現價 +98.5% | DATA_UNAVAILABLE | 分歧大（低點 102） |
| Beta | 3.618 | n/a | DATA_UNAVAILABLE | 高波動 |

FUNDAMENTALS REPORT COMPLETE
