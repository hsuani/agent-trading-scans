# Fundamentals — IRM as of 2026-10-24

資料來源: pipeline/tools/yf (cache 來源, 最新快照 2026-10-23)。本報告金額皆為 USD, 以 M (百萬) / B (十億) 標示, 不涉及 億 單位。最新季度為 2026-06-30 (Q2'26)。Data 未晚於 as-of 日期, 無 post-date 資料。

## Executive summary

IRM 營收成長動能明顯加速 (Q2'26 營收 YoY +18.5%, TTM 營收 7,562.5 M USD), 但財務體質偏弱: 普通股權益為負 (-1,280.9 M USD)、TTM Net debt/Normalized EBITDA 約 6.5x、TTM 利息覆蓋約 1.6x, 且 2023–2025 年 FCF 皆為負, 股利 (TTM 支出 996.5 M USD) 實質仰賴舉債與資本支出規模的管理。估值以 GAAP 計算明顯偏高 (Forward P/E 40.5x, EV/EBITDA 20.8x), 以 OCF 計為 P/OCF 約 20.0x, 整體而言估值吸引力偏低, 需等待資本支出轉化為 FFO/AFFO 成長的證據。

## Revenue & profitability

**年度趨勢 (M USD)**

| 指標 | FY2022 | FY2023 | FY2024 | FY2025 | TTM (至 Q2'26) |
|---|---|---|---|---|---|
| 營收 (Total Revenue) | 5,103.6 | 5,480.3 | 6,149.9 | 6,901.7 | 7,562.5 |
| 營收 YoY | n/a | +7.4% | +12.2% | +12.2% | Q2'26 單季 YoY +18.5% |
| Gross margin | 57.1% | 57.0% | 56.2% | 55.4% | 54.2% (info grossMargins) |
| Operating margin (Total Operating Income As Reported) | 20.6% | 16.8% | 16.4% | 16.9% | 18.8% |
| Normalized EBITDA | 1,809.0 | 1,881.7 | 2,147.5 | 2,474.4 | 2,623.0 |
| Normalized EBITDA margin | 35.5% | 34.3% | 34.9% | 35.9% | 34.7% |
| Net income (common) | 557.0 | 184.2 | 180.2 | 144.6 | 418.7 |
| Net margin | 10.9% | 3.4% | 2.9% | 2.1% | 5.5% |
| Diluted EPS (USD) | 1.90 | 0.63 | 0.61 | 0.49 | 1.40 |

- 營收 CAGR: FY2022–FY2025 (3 年) 約 10.6%。FY2021 資料為 null, 無法計算更長期 CAGR。
- 單季趨勢: Q2'25 1,711.9 → Q3'25 1,754.1 → Q4'25 1,843.2 → Q1'26 1,936.1 → Q2'26 2,029.1 (M USD)。Q2'26 相對 Q1'26 季增 +4.8%, 相對 Q2'25 年增 +18.5%。年增加速的原因在工具資料中未揭露 (是否來自 data-center 擴張、併購或定價, 無法由資料判定)。
- 分部營收: info 的 longBusinessSummary 僅列出業務範圍 (records and information management、data centers、asset lifecycle、digital solutions), 未提供分部營收數字。分部佔比 DATA_UNAVAILABLE。
- 毛利率趨勢: FY 由 57.1% 連續下滑至 55.4%, 單季 Q2'26 為 52.8%, 較 Q2'25 (55.9%) 下降約 3.1 pp, 成長與毛利率走勢不同步。
- 營業利潤率: TTM 18.8%, Q2'26 為 18.4% (Q2'25 為 15.2%), 單季營業利潤率有改善。
- 盈餘品質: FY2025 Total Unusual Items 合計 -359.5 M USD (Yahoo 資料), 重組與併購相關費用 (Restructuring And Mergern Acquisition) 於 FY2022–FY2025 分別為 89.7 / 239.1 / 267.4 / 229.3 M USD, 連續多年出現, 不宜視為一次性。Yahoo 報表中 "Operating Income" (FY2025 1,403.9 M USD) 與 "Total Operating Income As Reported" (1,163.8 M USD) 定義不同, 本報告統一採用 As Reported 值。

**ROE / ROIC**

- ROE: 普通股權益為負, ROE 無經濟意義 (n/m)。
- ROA (info): 4.63%。
- ROIC (估計): 以 TTM Total Operating Income As Reported 1,418.4 M USD × (1 - 12.2% 最新季稅率) = NOPAT 約 1,245.4 M USD, 除以 Jun-26 Invested Capital 16,068.7 M USD, 約 7.8%。此為本報告自行計算的近似值, 非工具直接提供。

## Cashflow & balance sheet

**現金流 (M USD)**

| 指標 | FY2022 | FY2023 | FY2024 | FY2025 | TTM (至 Q2'26) |
|---|---|---|---|---|---|
| 營運現金流 OCF | 927.7 | 1,113.6 | 1,196.7 | 1,340.0 | 1,655.4 |
| OCF margin | 18.2% | 20.3% | 19.5% | 19.4% | 21.9% |
| 資本支出 Capex (Capital Expenditure 科目) | 883.6 | 1,345.1 | 1,854.0 | 2,347.1 | 2,252.1 |
| Capex / 營收 | 17.3% | 24.5% | 30.1% | 34.0% | 29.8% |
| FCF (Yahoo 定義, OCF + Capex) | +44.1 | -231.5 | -657.2 | -1,007.1 | info: -436.1; 季度重算: -596.7 |
| FCF / 淨利 | n/m (為正但 NI 偏低) | n/m (負) | n/m (負) | n/m (負) | n/m (負) |
| OCF / 淨利 | 1.7x | 6.0x | 6.6x | 9.3x | 4.0x |

- FCF/NI 比率在 FY2023–FY2025 及 TTM 皆為負, 未達 >0.9 的健康門檻。OCF 遠高於 NI 主要來自大額非現金折舊攤銷 (FY2025 D&A 1,057.2 M USD), 屬 REIT 常見結構, 但 FCF 仍為負, 代表資本支出規模超過營運現金產出。
- 季度 TTM 重算說明: info 的 freeCashflow (-436.1 M) 與以季度 Capital Expenditure 科目重算的 -596.7 M 有差距, 推測為 Yahoo 的 capex 定義差異 (例如 Capital Expenditure Reported 科目為 -2,146.3 M)。本報告兩者都列出, 不做二選一判斷。

**資產負債表 (M USD)**

| 指標 | Dec-25 (FY2025) | Jun-26 (Q2'26) |
|---|---|---|
| 現金及約當現金 | 158.5 | 204.8 |
| 短期借款 + 長期負債 (不含租賃, Yahoo LTD + Current Debt) | 16,432.0 | 17,349.6 |
| 資本租賃負債 (Capital Lease Obligations) | 2,619.6 | 2,265.3 |
| Total Debt (含租賃) | 19,051.5 | 19,614.9 |
| Net Debt (Yahoo 定義, 不含租賃) | 16,273.4 | 17,144.9 |
| 普通股權益 (Stockholders' Equity) | -981.0 | -1,280.9 |
| Goodwill | 5,285.8 | 5,267.2 |
| 流動資產 | 1,935.0 | 2,103.7 |
| 流動負債 | 2,619.5 | 2,897.5 |
| Current ratio | 0.74 (計算) | 0.73 (info 0.726) |
| Quick ratio (info) | n/a | 0.58 |
| Working capital | -684.5 | -793.8 |
| Tangible Book Value | -7,536.4 | -7,783.6 |

- Net debt 自 FY2022 的 10,427.2 M USD 增至 FY2025 的 16,273.4 M USD, 2026 上半年再增加約 871.5 M USD (Dec-25 至 Jun-26)。
- 槓桿: Net debt / Normalized EBITDA: FY2024 6.3x、FY2025 6.6x、TTM 6.5x (TTM Normalized EBITDA 2,623.0 M USD)。以 info ebitda (2,551.0 M USD) 計 TTM 約 6.7x。
- 利息覆蓋 (TTM Total Operating Income As Reported / 利息支出): FY2024 1.37x、FY2025 1.37x、TTM 1.60x (TTM 利息支出 889.0 M USD)。
- 負債/權益: 普通股權益為負, D/E 比率 n/m。
- 流動性: 現金僅 204.8 M USD, Current ratio 0.73, 營運資金為負。償債依賴持續再融資: Q2'26 單季債務償還 6,750.7 M USD、發行 6,956.4 M USD。
- 普通股權益為負的成因在工具資料中未拆解 (可能與長期股利分配超過盈餘、重組與折舊造成的累積虧損有關), 需查閱財報附註確認, 不宜視為單純會計現象。

## Capital allocation & insider signal

**資本配置**

- 資本支出: FY2022–FY2025 年增率分別為約 +52%、+38%、+27% (FY2025 Capex 2,347.1 M USD, 相對 FY2024 增 +26.6%)。Capex / D&A 於 FY2025 約 2.2x, 顯示成長型投資主導現金流出。Q2'26 單季 Capex 625.2 M USD, 為近五季最高。
- 股利: 年化股利 dividendRate 3.46 USD (季股 0.864 USD), 殖利率 3.12%, 五年平均殖利率 3.48%。Dividends paid FY2025 919.4 M USD, TTM 996.5 M USD。
- 股利覆蓋:
  - 以 OCF 計: FY2022 1.28x、FY2023 1.51x、FY2024 1.52x、FY2025 1.46x、TTM 1.66x。
  - 以 FCF 計: FY2023–FY2025 及 TTM 皆為負, 股利由資本支出之外的融資來源支應。
  - 以 GAAP EPS 計: yfinance payoutRatio 241% (trailing EPS 1.40), GAAP 基礎覆蓋不足。
  - AFFO / 官方 FFO: DATA_UNAVAILABLE (yfinance 不提供)。
- 股份: 年底流通股數 FY2022 290.8 M → FY2025 295.8 M (CAGR 約 +0.6%/年), Jun-26 為 297.7 M。現金流量表未見股票回購科目, 無回購計畫資料。
- 併購: Purchase of Business FY2022 876.9 M、FY2023 57.7 M、FY2024 188.2 M、FY2025 144.8 M USD。

**內部人交易 (最近 6 個月, 截至 2026-10-23)**

- 公開市場買入: 0 筆 (買入合計 0 USD)。
- 公開市場賣出: 17 筆, 合計約 35.5 M USD, 佔市值 32.94 B USD 之約 0.11%, 量級小。
- 主要賣出者:
  - CEO William L. Meaney: 6 筆 (2026-05-08 至 2026-10-01), 每月約 38,474 股, 合計約 27.9 M USD, 成交價區間約 109.57–129.66 USD。每次出售前皆有以 37.00 USD 執行選擇權轉換的紀錄, 屬固定月度的「轉換後賣出」模式。
  - EVP Mark Kidd: 5 筆 (每次 6,000 股), 合計約 3.7 M USD。
  - Greg W. McIntosh: 3 筆, 合計約 2.6 M USD (含 2026-08-06 之 1.5 M USD)。
  - Daniel Borges (2026-05-21) 約 0.9 M USD、Pamela Arway 約 0.24 M USD、Walter Rakowich 約 0.09 M USD。
- 解讀: 賣出呈現規律性、與選擇權轉換綁定, 資料中未標示是否為 10b5-1 預定交易計畫, 需進一步確認。以金額與股本比例看, 不構成重大訊號, 但缺少任何內部人買入是中性偏負面的事實。
- 董事股票獎勵: 2026-05-07 共 8 位獨立董事各取得 1,892 股 (無現金支出)。
- 內部人持股: 0.88% (heldPercentInsiders)。

**機構持股與空頭**

- 機構持股 87.9% (約 1,580 家機構)。
- 前幾大持股: BlackRock 11.28% (33.57 M 股, 季增 +1.66%)、Vanguard (Portfolio Management 8.59% + Capital Management 6.37%)、State Street 5.92%、Cohen & Steers 4.04% (季減 -25.7%)、Geode 2.91%、FMR 2.64%。
- 空頭: 做空股數 6.999 M 股, 較前月 6.463 M 增 +8.3%; 占流通股 3.19%; Short ratio 4.09 天。

## Valuation

以 2026-10-23 收盤價 110.66 USD 計算 (前收 114.72 USD, 當日 -3.54%)。

| 估值指標 | 數值 | 計算/來源 | 說明 |
|---|---|---|---|
| 市值 (B USD) | 32.94 | info marketCap | 流通股 297.7 M × 110.66 USD |
| 企業價值 EV (B USD) | 53.08 | info enterpriseValue | |
| Trailing P/E | 79.0x | info trailingPE (EPS 1.40) | GAAP 基礎, 受大額折舊與非經常項影響, 參考價值低 |
| Forward P/E | 40.5x | info forwardPE (forwardEps 2.73) | |
| 當年度 P/E | 44.6x | priceEpsCurrentYear (EPS 2.48) | |
| P/S (TTM) | 4.36x | info priceToSalesTrailing12Months | |
| EV / EBITDA | 20.8x | info enterpriseToEbitda (EBITDA 2,551.0 M) | |
| P/OCF (TTM) | 20.0x | 110.66 / (TTM OCF 1,655.4 M / 平均稀釋股數 299.8 M = 5.52 USD) | |
| P/FCF | n/m | FCF 為負 | |
| P/FFO (粗估) | 約 21.5x | 110.66 / (TTM NI 418.7 M + TTM 現金流量表 D&A 1,122.2 M = 1,540.8 M, 除以 299.8 M 股 = 5.14 USD) | 非 NAREIT FFO 定義, 含非地產折舊、無形資產攤銷、處分利益, 未扣維持性資本支出, 僅供量級參考 |
| P/B | n/m | 普通股權益為負 | |
| 股利殖利率 | 3.12% | info dividendYield | |

- 分析師: 11 位, 平均目標價 144 USD (較現價 +30.1%), 高/低目標 155 / 132 USD (低標亦高於現價), 推薦平均 1.67 (buy)。
- 技術位置 (僅供估值脈絡): 52 週區間 77.77–134.68 USD; 現價低於 50 日均線 116.04 USD 與 200 日均線 114.48 USD; 52 週漲幅 +6.5% (S&P 500 同期 +13.7%); Beta 1.19。

## Key catalysts

- 下次財報: 2026-11-05 (Q3'26), 資料為非估計日期 (isEarningsDateEstimate: false)。Q3 EPS 一致預期 0.61 USD。
- 財報超預期紀錄: 最近四季 EPS surprise 依序為 +2.4% (2025-11)、+3.8% (2026-02)、+15.8% (2026-04)、+7.5% (2026-08)。更早期為 -4.2% (2025-08)、+7.0% (2025-05)、-6.2% (2025-02)、-9.0% (2024-11)。
- 指引 (guidance): yfinance 未提供管理層指引數字, DATA_UNAVAILABLE。以分析師 EPS 估計推算, 2026 年當年度 EPS 估 2.48 USD, 遠高於 TTM 1.40 USD, 市場預期盈餘有明顯抬升。
- 分部轉變: data-center 業務佔比與成長率 DATA_UNAVAILABLE; 僅能由 Capex 持續加碼 (Q2'26 625.2 M USD 為近五季高點) 推論擴張方向。
- 再融資: 2026 上半年大量債務滾動 (Q2'26 償還 6,750.7 M USD、發行 6,956.4 M USD), 利率與債市條件是重要變數。
- 股利: 最近一次季股 0.864 USD (ex-dividend 依 timestamp 換算約為 2026-09 中旬), 下一次除息日資料未揭露。

## Red flags

- FCF 連續為負: FY2023–FY2025 與 TTM 皆為負, FY2025 FCF -1,007.1 M USD, 股利與成長資本支出須靠舉債。
- 普通股權益為負: Jun-26 -1,280.9 M USD, 較 Dec-25 (-981.0 M USD) 再惡化 30.6%, BVPS -4.30 USD。
- 槓桿與利息覆蓋: Net debt / Normalized EBITDA 約 6.5x, TTM 利息覆蓋 1.60x, 利息支出 TTM 889.0 M USD 佔營業利潤約 63%。
- 流動性: Current ratio 0.73、營運資金 -793.8 M USD、現金 204.8 M USD, 高度依賴再融資市場。
- 毛利率下滑: FY 由 57.1% 降至 55.4%, Q2'26 單季 52.8% (YoY -3.1 pp)。
- 盈餘品質: GAAP 淨利率 FY2025 僅 2.1%; 重組與併購費用連續四年達 89.7–267.4 M USD; Total Unusual Items FY2025 -359.5 M USD。
- GAAP 股利覆蓋不足: payoutRatio 241%。
- 內部人持續出售、零買入: 6 個月約 35.5 M USD 賣出 (CEO 約 27.9 M USD), 規模小但方向單一。
- 空頭比例上升: 做空股數月增 +8.3%, 占流通股 3.19%; 主要機構 Cohen & Steers 季減 25.7%。
- 股價動能偏弱: 現價低於 50 日與 200 日均線, 當日 -3.5%。
- 資料缺口: 無官方 FFO / AFFO、無分部營收、無股票回購資料、無管理層指引數字。本報告的 P/FFO 與 ROIC 為自行推算的近似值。

## Metrics table

金額單位: M USD 或 B USD, 比率單位如表內標示。Sector median 為本報告依一般 REIT 經驗之估計值, 非工具資料。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| Revenue, TTM (M USD) | 7,562.5 | Q2'26 YoY +18.5%; FY2025 +12.2% | 約 4–6% (估計) | 強 |
| Gross margin, TTM (%) | 54.2% | Q2'26 YoY -3.1 pp; FY2025 -0.8 pp | n/a (REIT 不以 GM 比較) | 偏弱 |
| Operating margin, TTM (%) | 18.8% | Q2'26 YoY +3.2 pp | 約 25–30% (估計) | 中性 |
| Net margin, TTM (%) | 5.5% | FY2025 2.1% vs FY2024 2.9% | 約 10% (估計) | 偏弱 |
| Normalized EBITDA margin, TTM (%) | 34.7% | FY2025 35.9% vs FY2024 34.9% | 約 35–40% (估計) | 中性 |
| Diluted EPS, TTM (USD) | 1.40 | FY2025 0.49 vs FY2024 0.61 | n/a | 中性 |
| P/FFO 粗估 (x) | 約 21.5 | n/a (無官方 FFO) | 約 15–18x (估計) | 偏貴 |
| FFO / AFFO (USD/股) | DATA_UNAVAILABLE | n/a | n/a | 無法評估 |
| Net debt / Normalized EBITDA (x) | 6.5 | FY2025 6.6 vs FY2024 6.3 | 約 5–6x (估計) | 偏高 |
| Interest coverage, TTM (x) | 1.60 | FY2025 1.37 | 約 3x (估計) | 偏弱 |
| Current ratio (x) | 0.73 | Dec-25 0.74 | 約 1.0x (估計) | 偏弱 |
| Common equity (M USD) | -1,280.9 | 較 Dec-25 -30.6% | n/a | 偏弱 |
| FCF, TTM (M USD) | -436.1 (info) / -596.7 (季度重算) | FY2025 -1,007.1 vs FY2024 -657.2 | n/a | 偏弱 |
| Capex / Revenue, TTM (%) | 29.8% | FY2025 34.0% vs FY2024 30.1% | 約 10–15% (估計) | 高投資期 |
| OCF / Dividends paid, TTM (x) | 1.66 | FY2025 1.46 | 約 1.2–1.4x (估計) | 中性 |
| FCF / Dividends paid, TTM (x) | < 0 | FY2025 < 0 | 約 1.0x 以上 (估計) | 偏弱 |
| Dividend yield (%) | 3.12% | 5 年平均 3.48% | 約 4% (估計) | 中性 |
| Forward P/E (x) | 40.5 | 當年度 P/E 44.6 | 約 18–22x (估計) | 偏貴 |
| EV / EBITDA, TTM (x) | 20.8 | n/a | 約 15–18x (估計) | 偏貴 |
| P/OCF, TTM (x) | 20.0 | n/a | 約 12–15x (估計) | 偏貴 |
| Insider net flow, 6 mo (M USD) | -35.5 (賣出, 0 買入) | n/a | n/a | 偏負面 (規模小) |
| Short interest (% of float) | 3.19% | 做空股數月增 +8.3% | 約 2–3% (估計) | 中性偏負 |
| Institutional ownership (%) | 87.9% | n/a | n/a | 中性 |

FUNDAMENTALS REPORT COMPLETE
