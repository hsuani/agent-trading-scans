# Fundamentals — VRT (Vertiv Holdings) as of 2026-11-18

## Executive summary
Vertiv 基本面動能強勁: FY2025 營收 10.23B USD (YoY +27.7%)，2026 Q3 單季營收 4.31B USD (YoY +61.2%)，TTM 自由現金流約 3.11B USD，2026-09-30 已轉為淨現金約 0.35B USD，財務體質良好。估值面 trailing P/E 36.1x、EV/EBITDA 22.7x 仍不便宜，但 forward P/E 18.8x 與股價 186.43 USD 較 52 週高點 379.94 USD 已回落約 51%、較 200 日均線 271.59 USD 低約 31%，市場已大幅壓縮其估值溢價。主要保留點為 Q3 單季 FCF/淨利比僅 0.85 (低於 0.9 健康門檻)、流動負債 YTD 幾乎翻倍，以及 2026 年 2–3 月董監高集中出售 (約 123M USD，屬 6 個月窗口外但仍為重要背景)。

資料時點: 工具為快取資料 (cache，cached_at 2026-11-17 約 15:51–15:57 UTC)，即時 feed 於本次執行時 CONNECT 403 失敗，屬正常 fallback。資料未晚於 2026-11-18。

## Revenue & profitability
單位: 營收與獲利以 B USD 或 M USD 標示 (本報告不使用 億)。

**營收趨勢 (annual，來源 yf financials)**

| 年度 | 營收 (B USD) | YoY | 毛利率 | 營業利益率 | 淨利率 |
|---|---|---|---|---|---|
| FY2022 | 5.69 | n/a | 28.4% | 4.0% | 1.3% |
| FY2023 | 6.86 | +20.6% | 35.0% | 13.4% | 6.7% |
| FY2024 | 8.01 | +16.7% | 36.6% | 17.2% | 6.2% |
| FY2025 | 10.23 | +27.7% | 36.3% | 18.5% | 13.0% |

- 3 年 CAGR (FY2022→FY2025): 約 +21.6%。yfinance 未提供 2021 年完整數值，無法計算 4–5 年 CAGR (以 DATA_UNAVAILABLE 處理)。
- 季度動能加速: Q3'25 2.68B → Q4'25 2.88B → Q1'26 2.65B → Q2'26 3.27B → Q3'26 4.31B USD。Q3'26 YoY +61.2%，QoQ +31.7%。
- TTM 營收 13.12B USD (季度加總，與 info totalRevenue 13.12B 一致)，info revenueGrowth 為 +61.2%。
- 分部 (segment) 營收比重: 工具 (info longBusinessSummary) 未提供分部營收數字，**DATA_UNAVAILABLE**。產品線定性描述為電源管理、熱管理、模組化解決方案與生命週期服務。

**獲利能力**
- 毛利率: FY2025 36.3% (FY2024 36.6%，微降 0.3pp)；Q3'26 單季 38.1%，TTM 毛利約 5.00B USD / 13.12B = 38.1%。
- 營業利益率 (Operating Income 列): FY2025 18.5%，TTM 20.4%，Q3'26 23.0%，呈持續擴張。
- 淨利率: FY2025 13.0%，TTM 16.0% (info profitMargins 15.995%)，Q3'26 17.7%。
- FY2025 淨利暴增 (NI 1.33B vs FY2024 0.50B) 有基期因素: FY2024 非經常性項目合計 -466M USD，FY2025 僅 -68M USD；FY2024 有效稅率 35.2% vs FY2025 23.5%。
- EPS: Diluted EPS FY2025 3.41 (FY2024 1.28，+166%)。Q3'26 GAAP diluted EPS 1.95；earnings_dates 顯示 Q3'26 調整後 EPS (Reported) 2.21。兩者口徑不同，需注意。
- ROE: 46.6% (info, TTM)。ROA 11.9%。
- ROIC (自算): TTM 營業利益 2.67B × (1 - 23.2% 稅率) ÷ 期末投入資本 8.43B ≈ 24%。yfinance 未直接提供 ROIC，此為估算。
- 驗算: FY2025 淨利 1,332.8M ÷ Diluted 股數 390.65M = 3.41 EPS，與 yf 報告值一致。

## Cashflow & balance sheet

**現金流 (來源 yf cashflow / quarterly_cf)**

| 期間 | OCF (M USD) | Capex (M USD) | FCF (M USD) | FCF 淨利比 | FCF margin |
|---|---|---|---|---|---|
| FY2022 | -152.8 | 111.0 | -263.8 | n/a (淨利為負向區) | n/a |
| FY2023 | 900.5 | 134.6 | 765.9 | 1.66 | 11.2% |
| FY2024 | 1,319.3 | 184.1 | 1,135.2 | 2.29 | 14.2% |
| FY2025 | 2,113.8 | 226.4 | 1,887.4 | 1.42 | 18.4% |
| TTM (Q4'25–Q3'26，季度加總) | 3,639.5 | 525.3 | 3,114.2 | 1.48 | 23.7% |
| Q3'26 單季 | 794.0 | 141.8 | 652.2 | 0.85 | 15.1% |

- FCF 品質: FY2025 與 TTM 皆 >0.9 健康門檻，但 Q3'26 單季降到 0.85，Q2'26 單季 FCF margin 為 28.3%，Q3 轉弱主要反映營運資金消耗 (見下方流動負債增加)。
- 注意 yf info 的 TTM freeCashflow 為 2.96B USD，與季度加總 3.11B USD 不同 (口徑差異)；本報告以季度加總為主，兩者皆列示。
- Capex 強度上升: FY2025 Capex 佔營收 2.2%，TTM 4.0%，FY2025 Capex 年增 +23.0%。

**資產負債表 (來源 yf balance_sheet / quarterly_bs，最新為 2026-09-30)**

| 項目 | 2026-09-30 | FY2025 (12-31) | 變動 |
|---|---|---|---|
| 現金與短期投資 (M USD) | 3,711.7 | 1,827.9 | +103% |
| 總負債 Total Debt (M USD) | 3,356.9 | 3,227.9 | +4.0% |
| 淨負債 Net Debt (M USD) | -354.8 (淨現金，自算) | 1,184.6 | 轉為淨現金 |
| 股東權益 (M USD) | 5,502.0 | 3,941.3 | +39.6% |
| 流動資產 (M USD) | 12,123.3 | 6,819.5 | +77.8% |
| 流動負債 (M USD) | 8,710.7 | 4,407.0 | +97.7% |
| 總資產 (M USD) | 18,174.5 | 12,212.4 | +48.8% |
| 有形帳面淨值 (M USD) | 1,486.3 | 12.8 | 明顯改善 |

- 淨負債: Q1'26 771.6M → Q2'26 129.2M → Q3'26 淨現金 (自算 -354.8M USD)。
- 流動比率: 1.39 (FY2025 為 1.55)。速動比率 0.93 (info)。
- 負債股東權益比: 0.61x (Q3'26；FY2025 為 0.82x)。
- 利息保障: FY2025 EBIT 1,828.0M ÷ 利息費用 86.1M ≈ 21.2x。
- 2026 年 Q1 發行 2.10B USD 新債並償還 2.08B USD (refinancing 性質，淨債務未顯著增加)。
- 流動負債翻倍的組成明細 (應付帳款 / 合約負債 / 短期借款) 工具未提供分項，**DATA_UNAVAILABLE**，無法判定其性質。Q3'26 短期債務僅 92.1M USD，故增加並非來自短期借款。

## Capital allocation & insider signal

**資本配置**
- 股票回購: FY2024 回購 599.9M USD；FY2025 與 2026 前三季季報回購欄位為 n/a。
- 股利: FY2023 9.5M → FY2024 42.2M → FY2025 66.6M USD；2026 每季約 24M USD，年化約 96M USD (dividendRate 0.25 USD/股，季度 0.063 USD)。
- 股利覆蓋: FY2025 FCF ÷ 股利 ≈ 28x，TTM 約 32x，覆蓋極為充裕。
- 股本: 流通股數 FY2024 380.7M → FY2025 382.6M → Q3'26 385.0M (2026 年至今 +0.6%)，稀釋幅度小。
- 股利殖利率: 0.13% (0.25 ÷ 186.43 ≈ 0.13%)。注意 yfinance 欄位 dividendYield 值為 0.13 (即 0.13%)，非 13%。

**內部人交易 (yf insider，6 個月窗口 2026-05-18 至 2026-11-18)**

| 日期 | 人員 | 職位 | 類型 | 股數 | 金額 (USD) |
|---|---|---|---|---|---|
| 2026-09-01 | MONSER EDWARD L | Director | 公開市場出售 (249.43–256.36/股) | 15,287 | 約 3.88M |
| 2026-09-01 | MONSER EDWARD L | Director | 衍生性證券行權 (11.50/股) | 15,287 | 約 0.18M |
| 2026-09-08 | ALBERTAZZI GIORDANO | CEO | 贈與 (Gift) | 118,523 | 0 (非市場交易) |
| 2026-10-05 | RESHA MICHAEL | Officer | 股票獎勵 (253.62/股) | 3,193 | 約 0.81M |

- 6 個月內公開市場買入: **0 筆**。出售合計 約 3.88M USD，佔市值 71.8B USD 約 0.005%，規模極小。
- 窗口外的大額出售 (2026-02-26 至 2026-03-06): 共約 123M USD (FRADIN 51.4M、REINEMUND 25.4M、COTE 10.2M、VAN DOKKUM 9.8M、KARLBORG 7.5M、MONSER 19.0M 等)，成交價 239–259 USD/股。以現價 186.43 計，較當時成交價低約 22–28%。
- 內部人持股比例 0.25% (heldPercentInsiders)，持股比重低，出售對治理訊號的解讀需保留。
- 股權獎勵 (Stock Award) 於 2026 年多次發放，為例行性小額 RSU/股票授予，本報告不列為交易訊號。

## Valuation
價格基準: 186.43 USD (info regularMarketPrice，快取 2026-11-17)；市值 71.79B USD；EV 72.29B USD；流通股 385.06M。

- 價格版本不一致: fast_info (cnyes 快取) 188.51 USD；info 186.43 USD；ta snapshot 184.73 USD。本報告以 info 186.43 為基準，區間 184.7–188.5 USD。
- 技術位置 (ta，僅作背景): 20 日均線 207.17、50 日 227.35、200 日 271.56；RSI14 39.9，MACD 柱體 -0.88 (低於訊號線)，BB %B 0.22，20 日年化波動 117%，ATR14 16.8 USD。

| 估值指標 | 數值 | 計算基礎 |
|---|---|---|
| Trailing P/E | 36.1x | 186.43 ÷ EPS 5.16 (info)；若用季度加總 EPS 5.35，為 34.9x |
| Forward P/E | 18.8x | 186.43 ÷ forward EPS 9.92 |
| PEG | 0.60x | info pegRatio |
| EV/EBITDA | 22.7x | EV 72.29B ÷ TTM EBITDA 3.19B |
| P/FCF (TTM) | 24.2x (yf FCF 2.96B) / 23.1x (季度加總 3.11B) | 市值 ÷ FCF |
| P/S (TTM) | 5.5x | 市值 71.79B ÷ TTM 營收 13.12B |
| P/B | 13.0x | info priceToBook |

- 分析師共識 (30 位): 目標價均值 334.3 USD、最高 427 USD、最低 240 USD；recommendationKey 為 strong_buy。最低目標價仍高於現價，此為第三方資料，非本報告建議。
- 同業中位數 (sector median): 工具未提供同業估值中位數，**DATA_UNAVAILABLE**，無法做相對估值比較。

## Key catalysts
- 上一次財報: 2026-10-28，EPS 調整後 2.21 vs 預估 1.82，超預期 +21.2%。近 9 季 EPS 全數超預期 (2024-10 至 2026-10，surprise 介於 +3.9% 至 +25.0%)。
- 下一次財報: yfinance 顯示 2027-02-10 (為估計日)，Q4'26 EPS 一致預期 2.29。
- 除息日: 2026-11-24 (yfinance exDividendDate，季度股利 0.063 USD)。
- 管理層指引 (guidance) 數字: yfinance 未提供，**DATA_UNAVAILABLE**。
- 放空部位: 空單股數 11.07M，佔流通股 2.88%，回補天數 1.65 日，壓力偏低。
- 近期股價結構: 1 個月動能 -10.4%、3 個月 -29.2%、6 個月 -42.7%、12 個月 +8.0% (ta)，股價在 2026 年 Q2 後明顯回檔。回檔原因工具無法判定 (新聞或產業資料不在本次工具範圍)。

## Metrics table
單位標示: 營收/獲利/現金流 (B USD 或 M USD)；比率為 %、x。Sector median 全數 DATA_UNAVAILABLE (工具未提供)。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 TTM (B USD) | 13.12 | +61.2% (Q3'26 單季) | DATA_UNAVAILABLE | 強 |
| 營收 FY2025 (B USD) | 10.23 | +27.7% | DATA_UNAVAILABLE | 強 |
| 毛利率 Q3'26 (%) | 38.1% | FY25 36.3% vs FY24 36.6% (-0.3pp) | DATA_UNAVAILABLE | 中性偏優 |
| 營業利益率 TTM (%) | 20.4% | FY25 18.5% vs FY24 17.2% (+1.3pp) | DATA_UNAVAILABLE | 優 |
| 淨利率 TTM (%) | 16.0% | FY25 13.0% vs FY24 6.2% (+6.8pp) | DATA_UNAVAILABLE | 優 |
| ROE TTM (%) | 46.6% | n/a | DATA_UNAVAILABLE | 優 (權益基數偏小需留意) |
| ROIC 自算 (%) | 約 24% | n/a | DATA_UNAVAILABLE | 優 |
| FCF TTM (B USD) | 3.11 | FY25 1.89 vs FY24 1.14 (+66.3%) | DATA_UNAVAILABLE | 優 |
| FCF margin TTM (%) | 23.7% | FY25 18.4% vs FY24 14.2% | DATA_UNAVAILABLE | 優 |
| FCF / 淨利 TTM (x) | 1.48 | Q3'26 單季 0.85 | DATA_UNAVAILABLE | 中性 (Q3 轉弱) |
| 淨負債 Q3'26 (M USD) | -354.8 (淨現金) | vs FY25 +1,184.6 | DATA_UNAVAILABLE | 優 |
| 流動比率 (x) | 1.39 | vs FY25 1.55 (-0.16x) | DATA_UNAVAILABLE | 中性 (負債成長快) |
| 負債股東權益比 (x) | 0.61 | vs FY25 0.82 | DATA_UNAVAILABLE | 優 |
| 資本支出 TTM (M USD) | 525.3 (4.0% of 營收) | FY25 +23.0% | DATA_UNAVAILABLE | 中性 |
| 股利 年化 (USD/股) | 0.25 (殖利率 0.13%) | 2026 季股利 ~24M USD | DATA_UNAVAILABLE | 中性 |
| 6 個月內部人淨交易 (M USD) | -3.88 (0 筆買入) | 窗口外 2026-02/03 約 -123 | DATA_UNAVAILABLE | 中性偏警示 |
| Trailing P/E (x) | 36.1 | n/a | DATA_UNAVAILABLE | 偏貴 |
| Forward P/E (x) | 18.8 | n/a | DATA_UNAVAILABLE | 合理 |
| EV/EBITDA TTM (x) | 22.7 | n/a | DATA_UNAVAILABLE | 偏貴 |
| P/FCF TTM (x) | 23–24 | n/a | DATA_UNAVAILABLE | 偏貴 |
| P/S TTM (x) | 5.5 | n/a | DATA_UNAVAILABLE | 中性 |
| P/B (x) | 13.0 | n/a | DATA_UNAVAILABLE | 偏貴 |

## Red flags
- Q3'26 單季 FCF/淨利 0.85 (低於 0.9)，FCF margin 由 Q2 的 28.3% 降至 15.1%，營運資金吸收現金。
- 流動負債 YTD 由 4.41B 增至 8.71B USD (+98%)，流動比率由 1.55 降至 1.39；組成明細 DATA_UNAVAILABLE，需確認是否為合約負債 (正面) 或應付款項 (需監控)。
- 2026 年 2–3 月董監高集中出售約 123M USD (成交價 239–259 USD)，現價較當時低 22–28%。
- Trailing P/E 36.1x、EV/EBITDA 22.7x、P/B 13.0x 仍屬高檔；股價 52 週內回檔 51%，波動率與 beta (2.11) 偏高。
- 資料一致性: 價格有三個版本 (184.7 / 186.4 / 188.5 USD)；TTM EPS 有 5.16 (info) 與 5.35 (季度加總) 兩值；TTM FCF 有 2.96B 與 3.11B 兩值；Q3'26 EPS 有 GAAP 1.95 與調整後 2.21 兩值。均已於上文註明口徑。
- 工具資料為快取 (cache)，非即時行情；本報告以 2026-11-18 為分析基準，但實際數據時點為 2026-11-17 收盤前後快取。
- 管理層指引、分部營收、同業中位數皆為 DATA_UNAVAILABLE，相對估值與成長驗證有缺口。

FUNDAMENTALS REPORT COMPLETE
