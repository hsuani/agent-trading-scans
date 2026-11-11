# Fundamentals — HPE as of 2026-11-12

> 資料時點: yf `fast_info` / `info` 快取於 2026-11-11 (UTC 14:00 前後)，財報至 FQ3 FY26 (2026-07-31)。下一次財報日 2026-11-23 為未來事件。USD 金額以 B (十億美元) 表示。

## Executive summary
HPE 正處於獲利由谷底回升的階段: FY25 (10 月年度) GAAP 淨利僅 $0.06B、營業利益率 4.8%，但最新季 (2026-07-31) 營收 $12.21B 年增 +33.7%、毛利率升至 40.1%、營業利益率升至 12.0%。資產負債表槓桿尚可 (淨負債 $14.0B、淨負債/TTM EBITDA 約 2.0x、流動比率 1.11)，但有形淨值為 −$2.9B，且存貨自 2025-10 起增加 86%，需持續追蹤。估值上 trailing P/E 24.7x 偏高、forward P/E 10.1x 偏低，兩者差距取決於 forward EPS $4.74 是否可信 (若以季度調整 EPS 加總 $3.65 計，P/E 約 13.1x)；內部人近六個月為淨賣出 $38.4M，且無公開市場買進。

## Revenue & profitability
- **營收趨勢 (USD B)**: FY22 28.50 → FY23 29.14 (+2.2%) → FY24 30.13 (+3.4%) → FY25 34.30 (+13.8%)。FY22–FY25 三年 CAGR 約 6.4%。最近四季合計 (TTM) $41.87B，與 `info.totalRevenue` 吻合。
- **季度營收 (USD B)**: Jul-25 9.14 → Oct-25 9.68 → Jan-26 9.30 → Apr-26 10.68 → Jul-26 12.21。Jul-26 季年增 +33.7%，與 `info.revenueGrowth` 0.337 一致。FY25 之後的跳升與 2025 年 7 月前後的大型收購有關 (投資現金流 Jul-25 季 −$12.6B，產品線包含 MX/PTX/QFX/EX 等原 Juniper 產品)，但 yf 未明示併購名稱，此為推斷。
- **分部組合**: yf 未提供分部營收資料。`info.longBusinessSummary` 列出 Server、Hybrid Cloud、Networking、Financial Services、Corporate Investments 五個分部，但無金額。分部占比標示為 n/a。
- **毛利率**: FY22 33.4% → FY23 35.1% → FY24 32.8% → FY25 30.3%；季度上升: Jul-25 29.2% → Oct-25 33.5% → Jan-26 35.9% → Apr-26 36.5% → Jul-26 40.1%。年度下滑與季度回升方向相反，需確認是否為產品組合或一次性因素。
- **營業利益 (GAAP)**: FY22 7.8% / FY23 8.4% / FY24 8.3% / FY25 4.8%。TTM 營業利益 $3.28B，營業利益率 7.8%。FY25 含 impairment 約 $1.62B 與 restructuring 約 $0.46B (`financials`)。
- **淨利與 EPS**: GAAP 稀釋 EPS FY22 $0.66 / FY23 $1.54 / FY24 $1.93 / FY25 −$0.04。TTM GAAP EPS 約 $1.92 (`info.trailingEps` 1.94)。Jul-26 季稀釋 EPS $1.06，淨利 $1.54B，其中含約 $0.37B 一次性收益 (`Total Unusual Items` +$0.373B)，故季度淨利率 12.6% 不宜外推。
- **調整後 EPS (earnings_dates)**: Dec-25 $0.62 (預估 $0.58，+6.6%)、Mar-26 $0.65 (預估 $0.59，+10.8%)、Jun-26 $0.79 (預估 $0.53，+48.0%)。Sep-26 列 EPS 預估 $0.93 但實際值空白，見資料品質。
- **ROE / ROIC**: ROE (TTM) 10.9% (`info.returnOnEquity` 0.10936，以 TTM 淨利 $2.79B 與平均權益 $25.5B 手算吻合)。ROIC 為估計值: TTM EBIT $3.28B × (1 − 25.57% 稅率) ÷ 投入資本 $46.76B ≈ 5.2%。

## Cashflow & balance sheet
- **經營現金流 (USD B)**: FY22 4.59 / FY23 4.43 / FY24 4.34 / FY25 2.92。TTM $6.69B (與 `info.operatingCashflow` 6.694 一致)。
- **資本支出 (USD B)**: FY22 3.12 / FY23 2.83 / FY24 2.37 / FY25 2.29。資本支出占營收 FY25 6.7%、TTM 6.1%。
- **自由現金流**: yf `Free Cash Flow` FY22 1.47 / FY23 1.60 / FY24 1.97 / FY25 0.63 (FY25 年減 68%)。FCF margin FY22 5.2% / FY23 5.5% / FY24 6.6% / FY25 1.8%。TTM FCF (OCF − capex，手算) $4.16B，FCF margin 9.9%。`info.freeCashflow` 為 $4.74B，兩者相差約 $0.6B，定義不明，本報告以手算值為主。
- **FCF / NI**: FY22 1.69x / FY23 0.79x / FY24 0.77x (低於 0.9 健康門檻)。FY25 為 11.0x，但分母 NI 僅 $0.06B 失真。TTM 為 1.49x，但 NI 含一次性收益，數字偏高。
- **資產負債表 (2026-07-31, USD B)**: 總資產 83.6；股東權益 26.5；總負債 57.0；總債務 20.2 (2025-10 為 24.1)；現金 6.2；淨負債 14.0 (2025-10 為 16.6，2025-07 為 19.1)。商譽 23.9；有形淨值 −2.9。
- **償債指標**: 流動比率 1.11 (流動資產 $33.9B ÷ 流動負債 $30.4B)；負債/權益 76%；`info.quickRatio` 0.53；淨負債/TTM EBITDA 約 2.0x (以 `info.ebitda` $6.89B 計)。TTM 淨利息費用約 $0.46B，EBIT 對利息覆蓋約 7x (估計)。
- **營運資金變化**: 存貨 Oct-25 $6.35B → Jul-26 $11.82B (+86%)；應付帳款及應計費用 $11.87B → $19.09B (+61%)。存貨約為 Jul-26 季營收的 97%。FY25 營運資金變動為 −$2.71B，為經營現金流下滑的主因之一。
- **負債結構**: 長期負債 Jul-26 $17.3B、短期負債 $2.9B。FY25 償還債務 $6.84B、發行債務 $9.19B。Jul-26 季償還 $1.32B、發行 $0.32B。

## Capital allocation & insider signal
- **股利**: 每股年股息 $0.57 (殖利率 1.19%，`info.dividendYield`)。TTM 現金股利合計 $0.86B，其中普通股 $0.74B、特別股 $0.12B。TTM FCF 對股利覆蓋 4.9x。FY25 普通股股利 $0.68B。
- **買回**: 年度買回 FY22 $0.51B / FY23 $0.42B / FY24 $0.15B / FY25 $0.20B；TTM 約 $0.55B。買回規模小於股利與稀釋相抵的程度。
- **稀釋**: 流通股數 Oct-25 1,318.3M → Jul-26 1,328.1M (+0.75%)。季度稀釋後加權股數 1,361M → 1,449M (+6.5%)，主要與 FY24 發行的特別股 ($1.46B，`Preferred Stock Issuance`) 相關，屬推斷。
- **內部人交易 (近六個月，2026-05-12 起)**:
  - 賣出 7 筆，合計 613,916 股、$38.4M，全部為公開市場 "Sale"。
  - CEO Antonio Neri 於 2026-09-11 與 2026-10-05 合計賣出 500,000 股 ($32.2M；價格 $60.44 與 $68.31)。
  - 公開市場買進 0 筆。
  - 衍生性證券轉換 3 筆，共 1,193,939 股、$49.1M (主要為 Rami Rahim 於 2026-07-02 轉換 1,122,365 股，行權價 $41.23)，屬非公開市場交易。
  - 贈與 2 筆，合計 657,127 股，價值 $0。
  - 賣出金額占市值 $63.6B 約 0.06%，幅度極小。但方向為單向淨賣出，且 CEO 大部分賣出發生在股價約 $60–68 區間，目前股價 $47.93。
  - 內部人持股比例 0.24%。
- **機構持股**: 機構持股 91.9% (2,123 家)。前十大包括 BlackRock 10.1% (QoQ −6.8%)、Vanguard 合計約 12.0%、State Street 5.1%、Capital World 4.5% (QoQ +1.6%)、Elliott Investment Management 2.4% (QoQ +17.7%，為激進投資人)。JPMorgan (−26.6%) 與 Bank of America (−46.7%) 為大幅減持。

## Valuation
- **市值與 EV**: 市值 $63.6B (股價 $47.93 × 1.327B 股，手算吻合)；EV $77.8B。
- **P/E**: trailing 24.7x (GAAP TTM EPS $1.94)；forward 10.1x (`forwardEps` $4.74)。若改用季度調整 EPS 加總 $3.65 (0.65 + 0.79 + 0.93 + 1.28)，forward P/E 為 13.1x。
- **EV/EBITDA**: 11.3x (`enterpriseToEbitda`)；EV/Revenue 1.86x。
- **P/S**: 1.52x (TTM)。P/B: 2.40x。
- **P/FCF**: 15.3x (市值 ÷ TTM 手算 FCF $4.16B)；若採 `info.freeCashflow` $4.74B 則為 13.4x。
- **Analyst 目標價 (未經交叉驗證)**: 平均 $72.20 (高 $92、低 $62，共 21 位)，較現價 +51%。
- **技術位置 (供參考，非交易建議)**: 股價 vs 50 日均線 $59.02 為 −18.8%；vs 200 日均線 $41.73 為 +14.9%；vs 52 週高 $73.56 為 −34.8%；52 週低 $19.84。Beta 1.47。
- **行業中位數**: yf 未提供，以下為估計值 (非工具輸出)，供比較用。

## Key catalysts
- **下一次財報**: 2026-11-23 (yf `earnings_dates`)，預估稀釋 EPS (調整後) $1.28，為 FQ4 FY26。`info` 內的 earnings timestamp 為 2026-11-12，與此不一致，見資料品質。
- **近期財報表現**: 最近三季調整 EPS 皆超過預估 (+6.6% / +10.8% / +48.0%)。
- **毛利率回升**: Jul-26 季 40.1%，若在 Nov-26 財報維持，為獲利改善最直接的證據。
- **存貨與營運資金**: 存貨 +86% 若對應訂單或產品轉換，有助營收；若為需求低於預期，則為減值風險。需於財報中確認。
- **FY25 一次性項目**: impairment 與 restructuring 是否持續，影響 GAAP 獲利可比性。
- **分部與指引**: yf 未提供分部數字或管理層指引，本報告無法量化。

## Metrics table
| Metric | Latest | YoY / 前期比較 | Sector median (estimate, 估計) | Verdict |
|---|---|---|---|---|
| 營收 (TTM, USD B) | 41.87 | 最新季 +33.7%；FY25 +13.8% | 約 3–6% 成長 (估計) | 強，含併購效應 |
| 毛利率 (Jul-26 季) | 40.1% | 年增 +10.9pt (Jul-25 為 29.2%) | 約 40% (估計) | 改善中，與行業持平 |
| 營業利益率 (TTM, GAAP) | 7.8% | FY25 4.8% vs FY24 8.3% | 約 10% (估計) | 偏弱 |
| 淨利率 (TTM) | 6.7% | FY25 0.02% | 約 7% (估計) | 中性 |
| ROE (TTM) | 10.9% | n/a | 約 12% (估計) | 中性 |
| ROIC (估計) | 5.2% | n/a | 約 8% (估計) | 偏弱 |
| 自由現金流 (TTM, USD B) | 4.16 | FY25 0.63，年減 68% | n/a | 回升中 |
| FCF / NI (TTM) | 1.49x | FY24 0.77x | 約 1.0x (估計) | 達標，但 NI 含一次性收益 |
| 流動比率 | 1.11 | n/a | 約 1.3 (估計) | 偏低 |
| 負債/權益 | 76% | 2025-10 為 98% (24.1/24.7) | 約 60% (估計) | 偏高 |
| 淨負債/EBITDA | 2.0x | 2025-10 淨負債 16.6 | 約 1.5x (估計) | 中性偏高 |
| 有形淨值 (USD B) | −2.9 | 2025-10 為 −5.5 | n/a | 偏弱，商譽 23.9 |
| Trailing P/E | 24.7x | n/a | 約 25x (估計) | 中性 |
| Forward P/E | 10.1x (EPS 4.74)；13.1x (EPS 3.65) | n/a | 約 18x (估計) | 便宜，視 EPS 可信度 |
| EV/EBITDA | 11.3x | n/a | 約 13x (估計) | 略便宜 |
| P/S (TTM) | 1.52x | n/a | 約 1.5x (估計) | 中性 |
| P/FCF (TTM) | 15.3x | n/a | 約 20x (估計) | 略便宜 |
| 股息殖利率 | 1.19% | n/a | 約 1.5% (估計) | 中性 |
| 內部人淨交易 (6 個月) | −$38.4M，0 筆買進 | n/a | n/a | 偏負面，金額占市值 0.06% |
| 機構持股 | 91.9% | n/a | n/a | 高 |

## Red flags
- GAAP 獲利在 FY25 幾近歸零 (淨利 $0.06B)，且有 impairment $1.62B 與 restructuring $0.46B。
- 存貨九個月增加 86%，應付帳款增加 61%，營運資金吃掉 FY25 現金流。
- FY23 與 FY24 FCF/NI 低於 0.9；FY25 FCF 年減 68%。
- FY25 利息支付 $1.02B (`Interest Paid Supplemental Data`) 遠高於損益表淨利息費用 $0.18B 與 EBIT $1.64B，口徑不一致，需確認。
- 有形淨值 −$2.9B，商譽 $23.9B 佔總資產約 29%。
- 稀釋加權股數於三季內增加 6.5%；特別股股利每季 $0.29B 持續支出。
- CEO 於 Sep–Oct 2026 合計賣出 500,000 股，近六個月無任何公開市場買進。
- 資料品質:
  - `info` 中部分欄位與 HPE 財報不一致 (`exchange` = TAI；`epsTrailingTwelveMonths` 15.05；`epsForward` 23.22；`netIncomeToCommon` $212.8B；`grossProfits` $569.6B；`floatShares` 12.05B；`revenuePerShare` 665.8)，判定為污染或他股資料，本報告未採用。市值、P/E、營收、EBITDA、ROE 等已與三大報表手算交叉驗證。
  - `fast_info` 來源為 `cnyes` 快取，`market_cap`、`fifty_day_average`、`shares` 皆為 null，價格 $47.93 與 `info.regularMarketPrice` 一致，但未獨立驗證。
  - `earnings_dates` 中 2026-09-02 列的 Jul-26 季調整 EPS 為空白，但 `quarterly_fin` 已有該季 GAAP 數字。
  - 下一財報日: `earnings_dates` 為 2026-11-23；`info` 為 2026-11-12；以前者為準，待確認。
  - `info` 的 `recommendationMean` 與 `averageAnalystRating` (1.6 Buy) 與 `targetMeanPrice` 同樣未經交叉驗證。
  - FCF 有 yf 定義 ($0.63B FY25) 與 `info` 定義 ($4.74B TTM) 兩種口徑差異。

FUNDAMENTALS REPORT COMPLETE
