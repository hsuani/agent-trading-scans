# Fundamentals — WDC (Western Digital) as of 2026-10-23

## Executive summary
WDC 的獲利與現金流在 FY26（截至 2026-06-30）出現結構性翻轉：營收 12.92B USD（YoY +35.7%）、毛利率由 FY23 的 22.2% 升至 48.9%、營業利益率 35.6%、FCF 3.51B USD，並已由淨負債轉為淨現金約 0.53B USD。估值面，GAAP trailing P/E 13.2x 被一次性項目墊高（FY26 EPS 26.92 USD vs. 正常化 EPS 約 9.9 USD），以正常化口徑計 P/E 約 35.9x、EV/EBITDA 25.5x、P/FCF 37.8x，估值吸引力取決於 AI 資料中心需求能否延續，且 2026-10-22 財報後股價於 10/23 盤中走弱（最新價 354.19 USD，較 52 週高點 799.87 USD 回落 55.7%），guidance 資料本次未取得，需補齊後再判斷。

## Revenue & profitability

**營收趨勢（USD B）**
- FY23 6.26B → FY24 6.32B（+1.0%）→ FY25 9.52B（+50.7%）→ FY26 12.92B（+35.7%）
- 3 年 CAGR（FY23→FY26）約 27.4%；2 年 CAGR（FY24→FY26）約 43.0%。5 年 CAGR 因 FY22 數據為 null 無法計算（n/a）。
- 季度動能加速：FY25Q4（2026-06 前一年同季）2.61B → FY26Q1 2.82B → FY26Q2 3.02B → FY26Q3 3.34B → FY26Q4 3.75B；FY26Q4 YoY 約 +43.8%（quarterly_fin 計算）。
- 業務組合（segment mix）：yfinance 未提供分部營收，longBusinessSummary 僅列出產品線（內接硬碟、資料中心硬碟與平台、外接/可攜式硬碟、NAS 等）。分部營收比重 DATA_UNAVAILABLE。

**利潤率趨勢**

| 期間 | 毛利率 | 營業利益率 | 淨利率（GAAP） |
|---|---|---|---|
| FY23 | 22.2% | -6.4% | -26.9% |
| FY24 | 28.1% | 1.5% | -12.6% |
| FY25 | 38.8% | 22.4% | 19.5% |
| FY26 | 48.9% | 35.6% | 72.0%（含大額一次性項目，失真） |
| FY25Q4 | 41.0% | 26.1% | — |
| FY26Q4 | 54.1% | 42.9% | — |

- 毛利率與營業利益率自 FY25Q4 起連續 5 季擴張（可取得之季度資料範圍），為本輪基本面最主要的支撐，但 FY26 淨利率 72.0% 明顯受非經常項目影響（Total Unusual Items FY26 = 5.81B USD；Normalized Income FY26 = 3.78B USD），不可直接外推。
- 正常化 EPS：以 Normalized Income 3.78B ÷ 稀釋股數 383M 約 9.87 USD；與 earnings_dates 中四季 adjusted EPS 加總 10.19 USD（1.78+2.13+2.72+3.56）相近，兩者可互相印證。
- GAAP 稀釋 EPS FY26 = 26.92 USD（FY25 = 5.12 USD）。

**ROE / ROIC**
- ROE（info.returnOnEquity）= 130.9%，因淨利含一次性項目且權益基數僅 8.86B USD，屬失真指標，僅作參考。以正常化淨利估算 ROE 約 43%（3.78B ÷ 8.86B，期末權益）。
- ROIC 約 34%（以營業利益 4.60B USD × (1 - 25.6% 常態稅率) ÷ 平均投入資本 9.97B USD 估算；FY26 實際稅率 5% 受一次性項目影響，故採 FY25 稅率）。

## Cashflow & balance sheet

**現金流（USD B，除非另註）**
- 營運現金流 FY26 = 3.93B（FY25 = 1.69B；FY24 = -0.29B）
- 資本支出 FY26 = 0.42B（佔營收 3.2%；FY23 為 0.82B，佔 13.1%）
- FCF FY26 = 3.51B（OCF 3.93B - Capex 0.42B），FCF margin 27.2%
- FCF / NI：以 GAAP NI 9.30B 計 0.38（受非現金一次性利益影響，不具參考性）；以 Normalized Income 3.78B 計 0.93，超過 0.9 健康門檻。
- Q4 FY26（2026-06 季）OCF 1.39B、FCF 1.28B，FCF margin 約 34.2%，季度現金流品質良好。
- 注意：info.freeCashflow 為 2.27B，與財報推導之 FCF 3.51B 不一致（口徑差異），本報告採財報推導值。

**資產負債表（期末 2026-06-30，USD B）**
- 現金及約當現金 1.58B；總債務 1.05B（不含租賃，info totalDebt 1.19B 含租賃）→ 淨現金約 +0.53B
- 總負債 5.00B；股東權益 8.86B；總資產 13.86B
- 流動比率 1.33x（流動資產 5.63B ÷ 流動負債 4.24B）；速動比率 0.85x（info）
- 負債/權益（總債務 ÷ 權益）約 0.12x（info debtToEquity 13.4% 同口徑）
- 槓桿去化：總債務由 FY25 的 4.71B 降至 FY26 的 1.05B，FY26 償還債務合計 2.88B；季度上看 FY26Q3 債務 1.58B、Q4 降至 1.05B，去化仍在進行中。
- 每股帳面價值 24.55 USD；有形淨值（TBV）4.54B USD
- 存貨 1.51B、應收帳款 2.03B（FY25 為 1.29B / 1.49B），應收帳款增幅 36% 高於營收成長（+35.7%），略為留意的營運資金變化。

## Capital allocation & insider signal

**資本配置**
- 股票回購：FY26 合計 2.59B（FY25 仍為 0.15B），佔 FCF 約 74%；FY26 各季 0.55B / 0.62B / 0.75B / 0.67B。
- 但股本未因回購而下降：期末流通股 361M（FY25 期末 347M，+4.0%），FY26 稀釋股數 383M（FY25 359M，+6.7%）。股本增加的原因（發行或其他）DATA_UNAVAILABLE，需向下游確認是否有股權發行或轉換。
- 股利：年化股利 0.60 USD（每季 0.15），殖利率 0.17%，payout ratio 1.9%（以 GAAP EPS 計）；FY26 現金股利合計 0.18B，以 FCF 計覆蓋倍數約 19x。下一個除息日 2026-12-04（依 info.exDividendDate）。
- 資本支出：FY23→FY26 由 0.82B 降至 0.42B，資本支出維持低水準，屬於輕資本擴張期（實際產能擴建計畫 DATA_UNAVAILABLE）。
- 債務償還 2.88B（FY26），利息費用由 FY25 的 0.36B 降至 0.17B。

**內部人交易（最近 6 個月，2026-04-23 至 2026-10-23）**
- 公開市場買入：0 筆。
- 公開市場賣出：約 20 筆，合計約 78.8k 股、約 35.8M USD（以 insider 資料 Value 加總）。主要賣方：Irving Tan（CEO，約 40k 股 / 17.1M USD，賣價 441–447 USD，2026-08-11 為其中一筆）、Brian Scott Davis（約 10k 股 / 5.0M USD）、Vidyadhara Gubbi（約 8.9k 股 / 4.3M USD）、Martin Cole（董事，約 8k 股 / 3.9M USD）、Cynthia Tregillis（法務長，約 5.5k 股 / 2.6M USD）、Stephanie Streeter（董事，5.6k 股 / 2.5M USD）、Bruce Kiddoo（董事，750 股 / 0.4M USD）。
- 規模：賣出金額約 35.8M USD，佔市值 132.6B USD 約 0.03%，屬於極小幅度，出售是否依 10b5-1 計畫執行 DATA_UNAVAILABLE。
- 其他：2026-08-25 大量 Stock Award（RSU 授予）；2026-09-01 CEO 贈與 112.5k 股（Stock Gift，非市場交易）。
- 信號解讀：內部人為淨賣出、無買入，且多數賣出價格在 380–560 USD 區間，高於目前 354.19 USD。內部人持股比例僅 0.27%（heldPercentInsiders），因此內部人行為的參考權重有限。

## Valuation

**估值倍數（股價 354.19 USD，市值 132.58B USD，EV 127.31B USD）**

| 指標 | 數值 | 計算/說明 |
|---|---|---|
| Trailing P/E（GAAP） | 13.2x | 354.19 ÷ 26.92，EPS 含一次性項目，失真 |
| Trailing P/E（正常化） | 約 35.9x | 354.19 ÷ 9.87 |
| Forward P/E（info） | 9.6x | forwardEps 36.87 USD，與季度共識不一致（見下） |
| EV/EBITDA（info） | 25.5x | EBITDA 5.00B（info）；以財報 EBITDA 4.64B（Normalized）計 27.4x |
| P/FCF | 37.8x | 132.58B ÷ 3.51B |
| P/S（trailing） | 10.3x | 132.58B ÷ 12.92B |
| P/B | 14.4x | 354.19 ÷ 24.55 |
| PEG（info） | 0.72 | 依 info 成長率計算，參考性有限 |

- 與 sector median 比較：本次工具未提供同業中位數，sector median 為 DATA_UNAVAILABLE。若以大型科技/硬體類股一般區間作粗估（非工具數據，僅供參考），P/E 與 EV/EBITDA 高於多數科技硬體股，但 P/S 與 P/B 仍偏高。
- Forward EPS 一致性問題：info forwardEps 36.87 USD，但 earnings_dates 顯示下一季（2026-12 季）共識 EPS 僅 5.13 USD，本季（2026-09 季）共識 4.10 USD。若以季度共識粗估全年 FY27 EPS 約在 20 USD 上下，forward P/E 約 17x，而非 9.6x。此差異未能由工具資料解決，已列為紅旗。
- 分析師共識（info）：24 位，recommendationMean 1.54（偏買進），目標價均值 636.08 USD（區間 405–1,050 USD），現價較目標均值低約 44%，且低於最低目標價 405 USD。

**股價技術位置（僅供基本面參考）**
- 52 週區間：121.72–799.87 USD；目前價格較 52 週高點回落 55.7%
- 50 日均線 435.87 USD、200 日均線 413.93 USD，現價分別低於 18.7% 與 14.4%
- Beta 2.17；10 日均量 9.03M 股，短期空單占浮動股 4.9%（shortRatio 2.77）

## Key catalysts
- **已發生 — 2026-10-22 FY27Q1 財報**（2026-10-22 20:00 UTC 公布）：Reported EPS 4.64 USD vs. 共識 4.10 USD，Surprise +13.2%。前一季（2026-08-05）為 3.56 USD vs. 3.30 USD（+7.9%）；過去 4 季皆為正向 surprise。
- **財報細節缺漏**：FY27Q1 營收、毛利率、FCF、Q2 指引（guidance）未由工具取得，DATA_UNAVAILABLE。10/23 股價盤中波動區間 348.23–367.34 USD，最新 354.19 USD，相對前收 378.51 USD 約 -6.4%，市場反應原因需以 guidance 內容判斷。
- **下一次財報**：2027-02-04（預估 EPS 5.13 USD）。
- **除息日**：2026-12-04（季股利 0.15 USD，依 info 數據）。
- **資料來源品質**：fast_info 價格來自快取 feed（cnyes，cached 2026-10-23T11:26 UTC），Yahoo cookie/crumb 取得失敗；info 內 previousClose（378.51）、fulldayPrice（337.93）與 currentPrice（354.19）時間戳不一致，本報告以 354.19 作為計算基準。
- 產業面：AI 資料中心 HDD 需求、企業級容量需求、NAND/快閃記憶體業務分拆後之影響等為主要變數，但工具未提供相關定量資料，DATA_UNAVAILABLE。

## Metrics table
單位：營收、獲利、現金流、債務、市值單位為 USD B（小數點後兩位）或 USD M（標示者）；股價為 USD；倍數為 x；比率為 %。

| Metric | Latest（FY26 / 2026-06） | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收（USD B） | 12.92 | +35.7% | DATA_UNAVAILABLE | 強 |
| 毛利率 | 48.9% | +10.1 pt | DATA_UNAVAILABLE | 強，持續改善 |
| 營業利益率 | 35.6% | +13.2 pt | DATA_UNAVAILABLE | 強 |
| 淨利率（GAAP） | 72.0% | 失真 | DATA_UNAVAILABLE | 不採信，受一次性項目影響 |
| 正常化淨利（USD B） | 3.78 | +79% | DATA_UNAVAILABLE | 改善明顯 |
| ROE（info） | 130.9% | 失真 | DATA_UNAVAILABLE | 不採信；正常化約 43% |
| ROIC（估算） | 約 34% | — | DATA_UNAVAILABLE | 強 |
| OCF（USD B） | 3.93 | +132% | DATA_UNAVAILABLE | 強 |
| FCF（USD B） | 3.51 | +174% | DATA_UNAVAILABLE | 強 |
| FCF margin | 27.2% | — | DATA_UNAVAILABLE | 良好 |
| FCF / NI（正常化） | 0.93 | — | 0.9 健康門檻 | 合格 |
| 淨現金（USD B） | +0.53 | 由淨負債 2.60B 轉正 | DATA_UNAVAILABLE | 強 |
| 總債務（USD B） | 1.05 | -77.7%（FY25 4.71） | DATA_UNAVAILABLE | 強 |
| 流動比率 | 1.33x | FY25 1.08x | DATA_UNAVAILABLE | 普通偏良好 |
| 負債/權益 | 0.12x | FY25 0.85x | DATA_UNAVAILABLE | 強 |
| 資本支出 / 營收 | 3.2% | FY25 4.3% | DATA_UNAVAILABLE | 低資本需求 |
| 股票回購（USD B） | 2.59 | +1,640%（FY25 0.15） | DATA_UNAVAILABLE | 積極，但股本仍增 |
| 流通股數（M，期末） | 361 | +4.0% | DATA_UNAVAILABLE | 紅旗（股本未縮） |
| 股利殖利率 | 0.17% | — | DATA_UNAVAILABLE | 低，非重點 |
| Trailing P/E（GAAP） | 13.2x | — | DATA_UNAVAILABLE | 失真 |
| Trailing P/E（正常化） | 約 35.9x | — | DATA_UNAVAILABLE | 偏高 |
| Forward P/E（info） | 9.6x | — | DATA_UNAVAILABLE | 存疑（與季度共識不一致） |
| EV/EBITDA（info） | 25.5x | — | DATA_UNAVAILABLE | 偏高 |
| P/FCF | 37.8x | — | DATA_UNAVAILABLE | 偏高 |
| P/S | 10.3x | — | DATA_UNAVAILABLE | 偏高 |
| P/B | 14.4x | — | DATA_UNAVAILABLE | 偏高 |
| 內部人淨買入 | 0 筆買入，約 35.8M USD 賣出 | — | DATA_UNAVAILABLE | 中性偏空，規模極小 |
| 分析師目標價均值（USD） | 636.08 | — | DATA_UNAVAILABLE | 現價低於目標價約 44% |
| 距 52 週高點 | -55.7% | — | DATA_UNAVAILABLE | 股價大幅修正 |

## Red flags
- 獲利品質：FY26 GAAP EPS 26.92 USD 與正常化 EPS 約 9.9 USD 差距約 2.7 倍，GAAP trailing P/E 13.2x 具誤導性；FY26Q4 單季 GAAP 稀釋 EPS 8.21 USD 遠高於 adjusted 3.56 USD。
- 股本未縮減：回購 2.59B USD 但流通股數由 347M 增至 361M，稀釋股數 +6.7%，原因 DATA_UNAVAILABLE。
- Forward EPS 不一致：info forwardEps 36.87 USD 與季度共識（4.10 / 5.13 USD）推算的 FY27 約 20 USD 差距大，forward P/E 9.6x 不宜直接採用。
- 估值偏高：正常化 P/E 約 35.9x、EV/EBITDA 25.5x、P/FCF 37.8x，若景氣循環轉弱，獲利可能快速回落（歷史上 FY23–FY24 為虧損或近乎損益兩平）。
- 股價與基本面背離風險：10/22 財報 beat 後 10/23 盤中走弱，現價低於 50 日與 200 日均線；guidance 未取得，市場反應原因不明。
- 內部人持續淨賣出（6 個月內約 35.8M USD，無買入），雖規模小，但方向一致。
- 應收帳款成長（+36%）略快於營收成長，需留意回收品質（DATA_UNAVAILABLE：帳齡資料）。
- 治理面：info auditRisk 10（最高風險分數），overallRisk 4；審計風險項需向下游說明來源（資料欄位原值）。
- 資料品質：Yahoo cookie/crumb 取得失敗，fast_info 來自快取 feed；info 價格欄位時間戳不一致；info freeCashflow（2.27B）與財報推導 FCF（3.51B）不一致，本報告採財報推導值。
- 5 年數據缺口：FY22 財報欄位全為 null，5 年 CAGR 與長期週期比較 DATA_UNAVAILABLE。

FUNDAMENTALS REPORT COMPLETE
