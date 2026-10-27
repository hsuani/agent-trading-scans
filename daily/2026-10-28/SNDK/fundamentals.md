# Fundamentals — SNDK (Sandisk Corporation) as of 2026-10-28

資料基準：最新已申報財季為 2026-06-30（FY26 Q4，Yahoo 以 2026-07-03 記為 mostRecentQuarter）；下次財報 2026-10-29（美東盤後，時間戳 20:00 UTC），在分析日之後。現價取自 yfinance `info.regularMarketPrice` = 1255.58 USD（regularMarketTime 對應 2026-10-26 收盤），`fast_info` cnyes 快取另有 1265.61 USD（快取時間 2026-10-27 12:00 UTC），兩者未能對帳，本報告以 `info` 為準。所有資料來自 repo 快取（yf 即時端點因 proxy 403 失敗），無 2026-10-27 之後的資料。金額單位：USD，以 **B（十億美元）** 與 **M（百萬美元）** 表示，不使用億。

## Executive summary
SNDK 財務體質目前極強：FY26（2026-06 會計年度）營收 20.25B USD（年增 +175.3%）、淨利 11.43B USD、淨利率 56.5%，期末現金 4.76B USD、總負債（有息）僅 0.18B USD，流動比率 2.29，且 FY26 FCF 11.49B USD 與淨利幾乎相等（FCF/NI 1.01）。獲利結構在 4 個季度內由毛利率 29.8% 攀升至 84.6%，屬高度景氣循環的峰值特徵，歷史趨勢無法判斷可持續性。估值以 trailing P/E 17.0x、P/FCF 15.8x（statement 口徑）看似不貴，但 yfinance 的 forward P/E 4.7x 依賴的 forward EPS 與其他欄位不一致，不宜單獨採信；同時 6 個月內 CEO/CFO/CTO 等高層合計賣出約 130.3M USD 股票、無公開市場買進。整體判定：財務健康度優，景氣峰值與高層減持為主要風險，估值吸引力需以財報後盈餘品質判斷。

## Revenue & profitability

**年度趨勢（USD B）**

| 期間（會計年度 6 月底） | 營收 | YoY | 毛利 | 毛利率 | 營業利益 | 營業利益率 | 淨利 | 淨利率 |
|---|---|---|---|---|---|---|---|---|
| FY23 | 6.086 | — | 0.430 | 7.1% | -1.295 | -21.3% | -2.143 | -35.2% |
| FY24 | 6.663 | +9.5% | 1.072 | 16.1% | -0.444 | -6.7% | -0.672 | -10.1% |
| FY25 | 7.355 | +10.4% | 2.212 | 30.1% | 0.507 | 6.9% | -1.641 | -22.3% |
| FY26 | 20.248 | +175.3% | 14.472 | 71.5% | 12.468 | 61.6% | 11.433 | 56.5% |

- 3 年營收 CAGR（FY23→FY26）：約 49.3%（由 6.086B 至 20.248B）。資料僅涵蓋 FY23 起，無 5 年 CAGR。
- FY26 EPS：GAAP 稀釋 EPS 以四季加總約 72.90 USD（Q1 0.75 + Q2 5.15 + Q3 23.03 + Q4 43.97）；yfinance `info.trailingEps` 為 73.76 USD。FY25 稀釋 EPS 為 -11.32 USD。
- 季度趨勢（USD B）：

| 季度（財季末） | 營收 | 季增/年增 | 毛利率 | 營業利益率 | 淨利 | 稀釋加權股數（M） |
|---|---|---|---|---|---|---|
| 2025-09（Q1 FY26） | 2.308 | — | 29.8% | 8.3% | 0.112 | 149 |
| 2025-12（Q2 FY26） | 3.025 | +31.1% | 50.9% | 35.5% | 0.803 | 156 |
| 2026-03（Q3 FY26） | 5.950 | +96.7% | 78.4% | 70.0% | 3.615 | 157 |
| 2026-06（Q4 FY26） | 8.965 | +50.7% | 84.6% | 78.5% | 6.903 | 157 |

- Q4 FY26 營收 YoY：8.965 對 2025-06 季 1.901，為 +371.6%（yfinance `info.revenueGrowth` 3.716 即此季度年增率，非全年）。
- 營收來源分部：yfinance `info.longBusinessSummary` 描述產品為 NAND flash 的 SSD、嵌入式儲存、可攜式卡與 USB、晶圓與元件，客戶涵蓋 PC/OEM、資料中心、雲端服務商與零售通路；**分部營收占比 DATA_UNAVAILABLE**（快取中無分部財務）。
- 盈利品質觀察：Q4 毛利率 84.6% 與 Q1 的 29.8% 差距約 55pp，為記憶體景氣循環的典型放大效果；營業費用僅 0.545B（Q4），占營收 6.1%，營運槓桿極高，價格下行時利潤同樣會快速收縮。

**ROE / ROIC**
- ROE：`info.returnOnEquity` 91.6%（以平均股東權益計）；期末權益 15.736B USD（FY25 9.216B）。
- ROA：`info.returnOnAssets` 43.9%。
- ROIC（推算，非工具直接輸出）：營業利益 12.468B × (1 - 12% 稅率) ÷ 期末投入資本 15.736B ≈ 70%；若以 EBIT 13.09B 計約 73%。

## Cashflow & balance sheet

**現金流（USD B）**

| 指標 | FY23 | FY24 | FY25 | FY26 |
|---|---|---|---|---|
| 營業現金流 | -0.713 | -0.309 | 0.084 | 11.671 |
| 資本支出 | -0.219 | -0.166 | -0.204 | -0.177 |
| 自由現金流（FCF） | -0.932 | -0.475 | -0.120 | 11.494 |

- FCF margin（FY26）：11.494 ÷ 20.248 ≈ 56.8%。
- FCF / NI（FY26）：11.494 ÷ 11.433 ≈ 1.01，高於 0.9 健康門檻。
- 注意：yfinance `info.freeCashflow` 為 7.721B USD，與 cashflow statement 的 11.494B 及四季 quarterly_cf 加總 11.494B 不一致，本報告以 statement 口徑為準；若採 info 口徑 FCF/NI 僅 0.68。
- 四季 FCF 軌跡：Q1 0.438 → Q2 0.980 → Q3 2.993 → Q4 7.083（USD B），顯示 FY26 下半年現金流爆發式成長。
- 營運資金壓力：應收帳款由 FY25 的 1.068B 增至 4.708B（Q4 季末），以 Q4 營收推算 DSO 約 48 天（FY25 Q4 約 51 天），未見惡化。存貨 2.698B（FY25 2.079B）。

**資產負債表（期末 2026-06-30，USD B）**

| 項目 | FY25 期末 | FY26 期末 | 說明 |
|---|---|---|---|
| 現金及約當現金 | 1.481 | 4.762 | 較 FY25 +3.28B |
| 有息負債（總計） | 2.042 | 0.177 | 主要為資本租賃；長期借款欄位本期為 null |
| 淨負債（現金） | 0.368 | -4.585 | 淨現金約 4.585B（現金 4.762 - 負債 0.177） |
| 流動資產 | 5.086 | 12.780 | |
| 流動負債 | 1.427 | 5.581 | |
| 流動比率 | 3.56 | 2.29 | 速動比率 1.71（info） |
| 總資產 | 12.985 | 22.507 | |
| 總負債 | 3.769 | 6.771 | |
| 股東權益 | 9.216 | 15.736 | |
| 負債 / 權益 | — | 1.28%（info `debtToEquity` 1.277 為百分比單位） | 有息負債極低 |

- 每股淨值（期末權益 ÷ 146M 股）約 107.8 USD；info `bookValue` 105.61 USD。
- 有息負債自 FY25 2.042B 降至 FY26 0.177B，當期償還 1.9B 長期借款。

## Capital allocation & insider signal

**資本配置**
- 資本支出：FY26 0.177B USD，占營收 0.9%，為近四年最低強度，顯示公司目前為輕資產營運（晶圓製造委外或既有產能利用），未見大規模擴產。
- 買回：FY26 買回股票 4.524B USD（現金流量表 `Repurchase Of Capital Stock`），FY25 為 0；期末庫藏股 4.537B USD。
- 股數：普通股期末 146M（Q3 FY26 為 148M，Q4 減少）；info `sharesOutstanding` 144.5M，稀釋加權股數 157M，三者口徑不一致，市值計算採 info 的 144.5M。
- 股利：`dividendYield` 0.0，`payoutRatio` 0.0，無配息。
- 償債：FY26 還款 1.9B USD，利息支出 73M USD（FY26）。
- 股權激勵：SBC FY26 232M USD（占營收 1.1%）。

**內部人交易（yfinance `insider`，統計區間 2026-04-28 至 2026-10-27，約 6 個月）**
- 公開市場賣出：13 筆，合計 83,524 股，約 130.28M USD。
- 公開市場買進：0 筆。
- 賣出人：CEO David V. Goeckeler、CFO Luis Felipe Visoso、CTO Alper Ilkbahar、Bernard Shek、Michael Pokorny、Necip Sayiner。
- 重點交易：2026-09-14 CEO 賣出 33,838 股（約 51.70M USD，價格 1522.59–1541.88）；2026-09-17 CEO 賣出 33,841 股（約 53.27M USD，價格 1567.26–1587.00）；2026-09-15 CFO 賣出 1,000 股（約 1.57M USD，價格 1568.83）。
- 非市場交易：2026-05-12 Thomas Caulfield 股票贈與 9,666 股，2026-06-02 Ilkbahar 股票贈與 2,694 股，2026-08-20 Ilkbahar 一筆 276 股（無交易文字）。
- 2026-09-17 另有高階主管獲配股票授予（CEO 3,296 股、CFO 1,635 股等），屬薪酬性質，非市場買進。
- 規模：6 個月賣出 130.28M USD 相當於市值 181.47B USD 的約 0.07%，絕對金額不大，但全部為高層單向賣出，無買進對沖。
- 解讀限制：yfinance 未提供 10b5-1 計畫標記，無法判斷是否為預先排程；賣出價位集中在 1500–1590 USD，現價 1255.58 已低於該區間約 19–21%。
- 機構持股：82.5%（2,351 家機構）；內部人持股 1.09%。
- 放空：sharesShort 4.82M 股，占流通股 3.34%，short ratio 0.47 天；前月 5.996M 股，減少約 19.6%。

## Valuation

**估值倍數（以現價 1255.58 USD 計）**

| 指標 | 數值 | 計算 / 來源 |
|---|---|---|
| 市值 | 181.47B USD | info `marketCap`；= 1255.58 × 144.5M 股 |
| 企業價值（EV） | 179.28B USD | info `enterpriseValue`（市值 - 淨現金 + 有息負債，與本報告推算 176.88B 略有差異） |
| 本益比（trailing） | 17.0x | 1255.58 ÷ 73.76 |
| 本益比（current FY） | 5.8x | 1255.58 ÷ epsCurrentYear 214.82 |
| 本益比（forward） | 4.7x | info `forwardPE`，依 forwardEps 266.30；與 current-year EPS 之間落差大，**可信度低** |
| EV/EBITDA（TTM） | 14.2x | info：EV 179.28B ÷ EBITDA 12.617B；statement EBITDA 13.239B 口徑為 13.5x |
| P/FCF（statement） | 15.8x | 181.47B ÷ 11.494B |
| P/FCF（info） | 23.5x | 181.47B ÷ 7.721B |
| P/S（TTM） | 8.96x | info `priceToSalesTrailing12Months` |
| P/B | 11.9x | info `priceToBook`，每股淨值 105.61 USD |

- 同業中位數（sector median）：**DATA_UNAVAILABLE**，快取中未提供同業估值資料，無法給出數字對照；僅能定性判斷。
- 定性判斷：以 trailing 獲利計估值不貴，但獲利來自毛利率暴增後的峰值水準，trailing P/E 的參考價值有限；以 FCF 計約 16x 亦同理。P/B 11.9x 反映市場不認為當前獲利可以永續。

**分析師共識（info）**
- 覆蓋 24 位分析師；推薦均值 1.52（"buy"，1 為最強買入）。
- 目標價：平均 2143.83 USD，中位數 2150 USD，高 3600 USD，低 1000 USD。平均目標價相對現價 1255.58 為 +70.7%；此為共識數據，非本報告推薦。
- 價格位置：現價較 50 日均線 1585.74 低 20.8%，與 200 日均線 1240.94 幾乎持平（+1.2%）；較 52 週高點 2354.39 低 46.7%；52 週低點 164.56。

## Key catalysts

- **下次財報：2026-10-29**（美東盤後，時間戳 20:00 UTC；`isEarningsDateEstimate` = false，為確認日期）。
  - 共識 EPS：46.41 USD（yfinance `earnings_dates`，對應 FY27 Q1，即 2026-09 季）。
  - 近四次 EPS 超預期幅度：+13.7%（2026-08，實際 39.25 對 估計 34.52）、+59.7%（2026-04）、+75.0%（2026-01）、+36.9%（2025-11）。
  - 注意：2026-08 財報的 "Reported EPS" 39.25 USD 與本報告由 GAAP 季度淨利推算的 Q4 稀釋 EPS 43.97 USD 不一致，應為調整後口徑（yfinance 來源未標示），兩者不可直接相加或比較。
- **指引（guidance）**：快取中無管理層文字指引，**DATA_UNAVAILABLE**。
- **分部變化**：無分部財報，**DATA_UNAVAILABLE**。
- **治理與薪酬**：yfinance 治理風險評分 `overallRisk` 9（10 分制，高風險）、`boardRisk` 9、`shareHolderRightsRisk` 9、`auditRisk` 8、`compensationRisk` 7；CEO FY26 薪酬 6.17M USD。
- **資料後續**：yfinance 快取日期為 2026-10-27，本報告之後的財報、價格、內部人申報均未納入。

## Metrics table

金額單位：USD B（十億美元）或 USD M（百萬美元），股價單位 USD。YoY 為 FY26 對 FY25（除非另註）。

| Metric | Latest（FY26 / 2026-06 期末） | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收（USD B） | 20.248 | +175.3% | DATA_UNAVAILABLE | 爆發式成長，景氣驅動 |
| 營收 3 年 CAGR（FY23–26） | 49.3% | — | DATA_UNAVAILABLE | 高成長 |
| Q4 營收年增（USD B） | 8.965 | +371.6%（對 Q4 FY25 1.901） | DATA_UNAVAILABLE | 峰值動能，需留意循環 |
| 毛利率 | 71.5%（Q4 季 84.6%） | +41.4pp | DATA_UNAVAILABLE | 歷史高點，循環峰值風險 |
| 營業利益率 | 61.6%（Q4 季 78.5%） | +54.7pp | DATA_UNAVAILABLE | 極高，槓桿效應明顯 |
| 淨利率 | 56.5% | +78.8pp（FY25 為 -22.3%） | DATA_UNAVAILABLE | 極高 |
| 淨利（USD B） | 11.433 | 由 -1.641 轉正 | DATA_UNAVAILABLE | 獲利轉折 |
| ROE | 91.6%（平均權益） | — | DATA_UNAVAILABLE | 極高，受低權益基數影響 |
| ROIC（推算） | ~70% | — | DATA_UNAVAILABLE | 極高，屬推算值 |
| 營業現金流（USD B） | 11.671 | +11.59B（FY25 0.084） | DATA_UNAVAILABLE | 強勁 |
| 自由現金流（USD B） | 11.494 | — | DATA_UNAVAILABLE | 強勁 |
| FCF margin | 56.8% | — | DATA_UNAVAILABLE | 極高 |
| FCF / NI | 1.01 | — | 0.9 以上為健康 | 健康 |
| 資本支出 / 營收 | 0.9% | 由 2.8% 降至 0.9% | DATA_UNAVAILABLE | 輕資產，擴產意願低 |
| 現金（USD B） | 4.762 | +3.28B | DATA_UNAVAILABLE | 充足 |
| 有息負債（USD B） | 0.177 | -1.865B | DATA_UNAVAILABLE | 極低 |
| 淨現金（USD B） | 4.585 | 由淨負債 0.368 轉為淨現金 | DATA_UNAVAILABLE | 健康 |
| 流動比率 | 2.29 | 由 3.56 降至 2.29 | DATA_UNAVAILABLE | 健康 |
| 負債 / 權益 | 1.28%（有息） | — | DATA_UNAVAILABLE | 極低槓桿 |
| 股份買回（USD B） | 4.524 | 由 0 增至 4.524 | DATA_UNAVAILABLE | 積極回購 |
| 股利殖利率 | 0.0% | — | DATA_UNAVAILABLE | 無配息 |
| 高層 6 個月淨買賣（USD M） | -130.3（全為賣出） | — | DATA_UNAVAILABLE | 負面訊號 |
| 機構持股 | 82.5% | — | DATA_UNAVAILABLE | 高 |
| 放空占流通股 | 3.34% | 前月 5.996M 股降至 4.82M 股 | DATA_UNAVAILABLE | 低，壓力降低 |
| 本益比（trailing） | 17.0x | — | DATA_UNAVAILABLE | 表面不貴，峰值獲利 |
| 本益比（forward，info） | 4.7x | — | DATA_UNAVAILABLE | 不可信，EPS 基準不一致 |
| EV/EBITDA（TTM） | 14.2x | — | DATA_UNAVAILABLE | 中性 |
| P/FCF（statement） | 15.8x | — | DATA_UNAVAILABLE | 中性偏低 |
| P/S（TTM） | 8.96x | — | DATA_UNAVAILABLE | 高，反映高毛利 |
| P/B | 11.9x | — | DATA_UNAVAILABLE | 高 |
| 分析師平均目標價（USD） | 2143.83（中位數 2150） | 相對現價 +70.7% | DATA_UNAVAILABLE | 共識偏多 |

## Red flags
- **景氣峰值風險**：毛利率由 FY25 的 30.1% 在一年內升至 Q4 的 84.6%，營業利益率 78.5%，獲利對記憶體價格極度敏感；Q1 FY26 季營業利益率僅 8.3%，同樣幅度的逆轉將快速壓縮獲利。
- **高層持續減持**：6 個月內 CEO、CFO、CTO 等合計賣出約 130.3M USD，零公開市場買進；2026-09 賣價 1500–1590 USD，現價已低約 20%。
- **股價趨勢轉弱**：現價 1255.58 較 50 日均線低 20.8%，較 9 月高點區間明顯回落，而 200 日均線仍在 1240.94 附近。
- **治理風險評分高**：yfinance 治理風險 overallRisk 9、boardRisk 9、shareHolderRightsRisk 9（10 分制）。
- **資料口徑不一致**：(1) forward P/E 4.7x 依賴 forwardEps 266.30，與 current-year EPS 214.82 落差大；(2) FCF 在 info（7.72B）與 statement（11.49B）不符；(3) EBITDA 在 info（12.62B）、statement（13.24B）、normalized（12.51B）三者不同；(4) 股數在 info（144.5M）、資產負債表（146M）、稀釋加權（157M）不同；(5) 2026-08 財報 EPS 39.25 與 GAAP 推算 43.97 口徑不同。估值數字應以 statement 為基準並註明口徑。
- **價格來源不一**：info 現價 1255.58 與 fast_info 快取 1265.61 不一致，且快取時點為 2026-10-27，分析日為 2026-10-28，當日盤中價未納入。
- **即時資料缺口**：yfinance 即時端點因 proxy 403 失敗，cookie/crumb 取得失敗，全部數字取自 repo 快取；共識目標價、推薦評等等為快取時點數據。
- **同業比較缺失**：sector median 全部 DATA_UNAVAILABLE，無法量化相對估值。

FUNDAMENTALS REPORT COMPLETE
