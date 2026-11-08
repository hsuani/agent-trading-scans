# Fundamentals — GOOGL as of 2026-11-09

資料說明: 本報告以 `pipeline/tools/yf` 輸出為準, 價格來自 cnyes 快取 (cached_at 2026-11-08T13:11Z, source: cache), 屬正常 fallback, 非錯誤。最新財報為 2026-09-30 結束之 Q3 2026 (2026-10-28 公布)。未發現 2026-11-09 之後的資料。金額統一為 USD B (十億美元), 本報告不使用 億。

## Executive summary
Alphabet 的獲利與流動性仍屬強健: Q3 2026 營收 127.58B USD (YoY +24.7%), 營業利益率約 31.8%, 現金及短期投資 265.1B USD 高於總債務 141.9B USD。然而 2026 年 AI 資本支出急升 (9M 2026 capex 131.9B USD, 已超過 FY2025 全年 91.4B USD), 使自由現金流 9M 合計為 -4.8B USD, 總債務由 FY2025 的 59.3B 擴增至 141.9B USD, 基本面體質正在由「高現金流」轉向「高投資、高負債」; 估值上, trailing P/E 14.9x 被非經常性投資收益嚴重扭曲, 以 normalized 口徑估算約 26.7x, forward P/E 18.5x, EV/EBITDA 18.4x, 價格較 52 週高點 408.61 回落約 30%。

## Revenue & profitability

**營收與成長**
- FY2022 / FY2023 / FY2024 / FY2025 營收: 282.84 / 307.39 / 350.02 / 402.84 B USD。
- FY2025 YoY +15.1%; FY2024 YoY +13.9%。
- 3 年 CAGR (FY2022→FY2025): 約 12.5%; 2 年 CAGR (FY2023→FY2025): 約 14.5%。
- TTM 營收 471.10 B USD (info.totalRevenue), 與 Q4'25 + Q1'26 + Q2'26 + Q3'26 季度加總 (113.83 + 109.90 + 119.80 + 127.58) 吻合。
- Q3 2026 營收 127.58 B USD, YoY +24.7% (對 Q3'25 102.35 B), QoQ +6.5%。
- 分部營收 (Google Services / Google Cloud / Other Bets): DATA_UNAVAILABLE。info.longBusinessSummary 僅列出三大分部與 Cloud 產品 (AI infrastructure, Vertex AI, Gemini enterprise, Workspace), 未提供分部營收數字。TPU 相關營收或資本支出拆分亦無資料, 無法直接量化 Cloud/TPU 題材貢獻。

**獲利能力 (毛利 / 營業 / 淨利)**

| 年度 | 毛利率 | 營業利益率 | 淨利率 | Diluted EPS (USD) |
|---|---|---|---|---|
| FY2022 | 55.4% | 26.5% | 21.2% | 4.56 |
| FY2023 | 56.6% | 27.4% | 24.0% | 5.80 |
| FY2024 | 58.2% | 32.1% | 28.6% | 8.04 |
| FY2025 | 59.7% | 32.0% | 32.8% | 10.81 |

- 季度營業利益率: Q3'25 30.5% → Q4'25 31.6% → Q1'26 36.1% → Q2'26 34.0% → Q3'26 31.8%。Q3'26 毛利率 59.7%, 與 Q3'25 的 59.6% 持平。
- 營業利益 FY2025 129.04 B USD (+14.8% YoY), 但 FY2025 淨利 132.17 B USD (+32.0% YoY) 高於營業利益, 差額來自非營業收益 (Other Income Expense FY2025 約 26.2 B USD, 以及 Total Unusual Items 24.2 B USD)。
- 研發費用 Q3'26 20.64 B USD, YoY +36%, 為 AI 投入加速的主要支出項目。SG&A Q3'26 14.94 B USD, YoY +2.4%。
- EBITDA FY2025 180.70 B USD (YoY +33.5%); TTM EBITDA 185.5 B USD (info.ebitda)。

**GAAP 淨利品質 (重要)**
- TTM 淨利 235.69 B USD (info.netIncomeToCommon) 由季度 NI 加總 (34.46 + 62.58 + 112.19 + 26.47) 得出, 其中 2026 年 Q1 含 Total Unusual Items 36.95 B USD, Q2 含 98.84 B USD, Q3 含 -9.03 B USD。
- Yahoo 之 Normalized Income 季度值為: Q4'25 32.44、Q1'26 32.71、Q2'26 32.23、Q3'26 33.85 B USD, TTM 合計約 131.2 B USD。
- 因此 info.trailingPE 14.87 與 info.returnOnEquity 44.3% 均被非經常性項目放大, 不宜作為估值與獲利能力的基準。
- Q3 2026 GAAP 淨利 26.47 B USD, YoY -24.3%; Diluted EPS 2.12, YoY -26.1% (對 Q3'25 2.87)。Q3'26 其他收益為 -9.0 B USD, 是 GAAP EPS 下滑的主因之一。

**ROE / ROIC (估算)**
- ROE (FY2025, 年末權益 415.27 B USD): 31.8%; (FY2025 淨利 / 年初與年末平均權益 370.2 B USD): 35.7%。
- ROE 口徑 normalized (TTM normalized NI 131.2 B USD / 平均權益 (Q3'25 386.87 + Q3'26 677.55)/2 = 532.2 B USD): 約 24.7%。
- ROIC (FY2025 NOPAT = 129.04 × (1 - 16.8%) = 107.3 B USD; 平均 Invested Capital (461.81 + 335.97)/2 = 398.9 B USD): 約 26.9%。以年末 IC 計約 23.2%。上述為本報告估算, 非工具直接輸出。

## Cashflow & balance sheet

**現金流量 (B USD)**

| 項目 | FY2022 | FY2023 | FY2024 | FY2025 | Q3'26 | 9M 2026 |
|---|---|---|---|---|---|---|
| Operating Cash Flow | 91.50 | 101.75 | 125.30 | 164.71 | 42.29 | 127.15 |
| Capital Expenditure | -31.48 | -32.25 | -52.53 | -91.45 | -51.35 | -131.94 |
| Free Cash Flow (OCF - capex) | 60.01 | 69.50 | 72.76 | 73.27 | -9.06 | -4.79 |

- FCF margin: FY2025 18.2%; TTM 約 4.2% (TTM FCF 約 19.8 B USD / TTM 營收 471.1 B USD)。Q2'26 與 Q3'26 連續兩季 FCF 為負。
- FCF / NI: FY2025 0.55 (低於 0.9 的健康門檻); FY2025 OCF / NI 為 1.25, 顯示差距來自資本支出, 而非應計盈餘品質問題。TTM FCF / normalized NI 約 0.15。
- **TTM FCF 口徑不一致**: info.freeCashflow 為 -1.16 B USD, 但季度 OCF TTM 179.55 B USD (與 info.operatingCashflow 吻合) 減去季度資本支出 TTM 159.79 B USD, 得 +19.8 B USD。兩者差約 21 B USD, 原因未在工具輸出中說明, 本報告以季度加總值為準並標示此差異。
- 資本支出強度: 資本支出 / 營收 FY2022 11.1%、FY2023 10.5%、FY2024 15.0%、FY2025 22.7%; TTM 33.9%; Q3'26 單季 40.2%。Q3'26 資本支出 51.35 B USD, YoY +114% (對 Q3'25 23.95)。
- 折舊攤提: Q3'26 Depreciation 8.37 B USD, YoY +49% (對 Q3'25 5.61), 未來幾季會持續壓縮營業利益率。

**資產負債表 (USD B)**

| 項目 | FY2025 (12/31) | Q2'26 (06/30) | Q3'26 (09/30) |
|---|---|---|---|
| Total Assets | 595.28 | 921.98 | 1,003.31 |
| Current Assets | 206.04 | 343.52 | 374.67 |
| Current Liabilities | 102.75 | 126.11 | 134.50 |
| Cash & Cash Equivalents | 30.71 | 55.91 | 56.33 |
| Cash + Short-Term Investments | 126.84 | 242.47 | 265.10 |
| Total Debt | 59.29 | 112.76 | 141.92 |
| Long-Term Debt | 46.55 | 98.17 | 125.10 |
| Stockholders' Equity | 415.26 | 640.48 | 677.55 |
| Total Liabilities | 180.02 | 281.50 | 325.76 |

- 流動比率 (Q3'26): 2.79 (374.67 / 134.50), 與 info.currentRatio 2.786 吻合; quick ratio 2.51 (info)。營運資金 240.16 B USD。
- 負債權益比: 22.2% (info.debtToEquity, 以 TTM/MRQ 總債務 150.33 B USD 計); 以 Q3'26 總債務 141.92 / 權益 677.55 估算約 20.9%。
- 淨負債 / 淨現金: Yahoo 欄位 Net Debt (Q3'26) 為 68.77 B USD, 但無法由 Total Debt 與 Cash 欄位對齊: Total Debt 141.92 - Cash & Equivalents 56.33 = 85.59 B USD; Total Debt 141.92 - Cash + STI 265.10 = -123.18 B USD (即淨現金)。定義不一致, 報告以 "總債務 141.9B vs 現金及短期投資 265.1B, 估算淨現金約 123B" 為口徑, Yahoo Net Debt 欄位標示為 DATA_UNAVAILABLE (無法對齊)。
- 負債快速擴張: 總債務 FY2025 59.29 → Q3'26 141.92 B USD (+139%), 總資產 +69%, 總負債 +81%, 權益 +63%。9M 2026 債務發行 85.23 B USD (Q1 31.38、Q2 24.85、Q3 29.00), 償還 8.89 B USD。
- 利息費用 (Yahoo Interest Expense 欄位) Q3'26 僅 0.97 B USD, 與 142 B USD 債務規模不成比例, 可能有資本化利息或欄位口徑差異, 需以 10-Q 確認。
- 2026 年 Q2 至 Q3 權益項目: Yahoo 季度 BS 顯示 Preferred Stock Equity 18.02 B USD (Q2、Q3 皆有), 且 Q2 Net Common Stock Issuance 30.50 B USD、Q3 為 12.37 B USD, 但季度 CF 無明細。此項性質不明, 為 DATA_UNAVAILABLE 待確認之項目。

## Capital allocation & insider signal

**資本配置**
- 股票回購: FY2022 59.30、FY2023 61.50、FY2024 62.22、FY2025 45.71 B USD。2026 年 Q1–Q3 回購皆為 0.0 B USD (Q4'25 為 5.50、Q3'25 為 11.50)。
- 股利: FY2024 7.36、FY2025 10.05 B USD; 季度股利 Q1'26 2.54、Q2'26 2.69、Q3'26 2.94 B USD。每股年股利 0.88 USD, 殖利率 0.31%, payout ratio 4.5% (info); 以 TTM FCF 19.8 B USD 計算股利覆蓋約 1.8x (TTM 股利約 10.7 B USD)。
- 股東回饋 (回購 + 股利) / FCF: FY2024 96%、FY2025 76%。2026 年 9M 僅股利 8.17 B USD, 已由 FCF 轉負的情況下, 以舉債支應資本支出。
- 股本: 流通股數由 FY2025 12.09B 升至 Q3'26 12.29B (+1.7%), 2026 年未回購而股數仍增加, 有稀釋跡象。info.sharesOutstanding 5.888B 疑為 Class A 單一股別, 與總股本不一致, 本報告不採用。
- 資本配置總結: 2026 年由「回購 + 股利 + 內生 FCF」轉為「資本支出 + 舉債 + 股利」, 資本支出動能為最重要的資金去向。

**內部人交易 (last 6 months, 2026-05-09 起算)**
- 公開市場買入: 0 筆。
- 公開市場賣出 (6 個月內): 0 筆 (工具輸出中無)。
- 6 個月內之紀錄僅為股票贈與 (Stock Gift, 價格 0):
  - Shriram Kavitark Ram (Director, 間接持有): 2026-10-13, 396,700 股, 名目 (以 284.78 計) 約 113.0 M USD。
  - Sergey Brin (Director / >10% 持有人, 直接持有): 2026-08-07, 673,200 股, 名目約 191.7 M USD。另有同日一筆 673,200 股無文字說明之重複列 (工具疑似重複), 不計入。
- 6 個月外之最近紀錄: Brin 2026-02-19 贈與 437,500 股; John L. Hennessy 2026-02-13 出售 600 股 (約 0.18 M USD)、2026-01-13 出售 600 股 (約 0.20 M USD)。
- 名目規模占市值比: 贈與合計約 304.7 M USD, 占市值 3,501 B USD 約 0.009%。贈與不屬市場賣壓, 但 Brin 之直接持股減少為一項紀錄。
- Insider 持股比例 1.59%, 機構持股比例 80.6%, 機構數 7,463 (major_holders); short interest 78.4M 股, short ratio 3.1 日 (info)。
- 結論: 內部人無近期公開市場買賣訊號, 信號中性偏無意義。

## Valuation

**價格與市值 (USD)**
- 價格: 284.78 (cnyes 快取, 2026-11-08); 前收 282.57; 日內區間 284.59–290.49。
- 市值: 3,501.1 B USD (info.marketCap); 企業價值 EV 3,404.3 B USD (info.enterpriseValue)。
- 52 週區間 270.70–408.61; 價格較 52 週高點回落 30.3%, 較 52 週低點高 5.2%。
- 50 日均線 332.93 (price 低 14.5%); 200 日均線 339.51 (price 低 16.1%)。來源為 info; fast_info 之 MA 欄位為 null。
- 52 週股價變動 -1.8% (info.fiftyTwoWeekChangePercent)。Beta 1.226。

**估值倍數**

| 指標 | 數值 | 計算基礎 |
|---|---|---|
| Trailing P/E | 14.9x | info; 以 GAAP TTM EPS 19.15 計, 受非經常性項目放大 |
| Trailing P/E (normalized) | 約 26.7x | 3,501.1 / TTM normalized NI 131.2 B USD (本報告估算) |
| Forward P/E | 18.5x | info; forwardEps 15.44 |
| EV/EBITDA (TTM) | 18.4x | info; EV 3,404.3 / EBITDA 185.5 B USD |
| P/S (TTM) | 7.4x | info.priceToSalesTrailing12Months |
| EV/Revenue (TTM) | 7.2x | info.enterpriseToRevenue |
| P/OCF (TTM) | 約 19.5x | 3,501.1 / OCF 179.55 B USD (本報告估算) |
| P/FCF (TTM) | 約 177x | 3,501.1 / FCF 19.8 B USD (本報告估算); info 口徑為負, 不具參考性 |
| P/B | 5.3x | info.priceToBook |
| PEG (trailing) | 1.01 | info.trailingPegRatio |

- 分析師一致目標價 400.37 USD (info.targetMeanPrice, 53 位分析師), 推薦等級 strong_buy (info.recommendationKey); 相對現價隱含 +40.6%。此為外部共識資料, 非本報告意見。
- 股利殖利率 0.31%, 估值以成長與 AI 投資回報為主要定價因子, 非股息導向。

**與板塊中位數比較**
- 板塊 (info.sector): Communication Services; 產業: Internet Content & Information。
- 板塊中位數為估計值 (工具未提供), 信心低, 僅供粗略比較。

## Key catalysts
- 下次財報: Yahoo 列示 2027-02-03 (Q4 2026, 為估計日期), EPS 共識 3.20 USD。前次 Q3 財報為 2026-10-28, 共識 3.01 USD, 實際 GAAP EPS 2.12 USD, 差異 -29.5%。
- 財報後股價反應與盤後指引: DATA_UNAVAILABLE (工具無指引與管理層展望資料)。
- 資本支出指引與 2027 年資本支出規模: DATA_UNAVAILABLE; 此為 AI/TPU 題材最關鍵的未知數。
- 債務發行與股權類流入 (Q2 Net Common Stock Issuance 30.50 B USD, Q3 12.37 B USD) 的性質與用途: DATA_UNAVAILABLE, 需查 10-Q / 8-K。
- Cloud 分部營收與 backlog: DATA_UNAVAILABLE。
- 除息日: info.exDividendDate 換算約 2026-09-04, 已過; 下一次配息日 DATA_UNAVAILABLE。
- 內部人與機構動向: 本月無公開市場交易紀錄 (見上節)。

## Metrics table

單位: 金額為 USD B (十億美元), 比率為 %, 倍數為 x。Sector median 為估計值 (工具未提供), 信心低。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 (Revenue, USD B) FY2025 | 402.84 | +15.1% | n/a | 強 |
| 營收 Q3'26 (USD B) | 127.58 | +24.7% | n/a | 強 |
| 營收 TTM (USD B) | 471.10 | n/a | n/a | 強 |
| 毛利率 (Gross Margin) Q3'26 | 59.7% | +0.1pp | 約 55% | 中上 |
| 營業利益率 (Operating Margin) Q3'26 | 31.8% | 較 Q3'25 30.5% 上升 1.3pp | 約 20% | 強 |
| 淨利率 (Net Margin) FY2025 | 32.8% | +4.2pp | 約 15% | 強 (含非營業收益) |
| 淨利率 normalized TTM (估算) | 約 27.9% (131.2 / 471.1) | n/a | 約 15% | 強 |
| Net Income Q3'26 (USD B) | 26.47 | -24.3% | n/a | 弱 (含 -9.0B 非營業損失) |
| Diluted EPS Q3'26 (USD) | 2.12 | -26.1%; 低於共識 3.01 (-29.5%) | n/a | 弱 |
| ROE (info, TTM) | 44.3% | n/a | 約 15% | 失真 (受非經常性項目放大) |
| ROE (normalized TTM 估算) | 約 24.7% | n/a | 約 15% | 強 |
| ROIC (FY2025 估算) | 約 26.9% | n/a | 約 10% | 強 |
| Operating Cash Flow FY2025 (USD B) | 164.71 | +31.4% | n/a | 強 |
| Free Cash Flow FY2025 (USD B) | 73.27 | +0.7% | n/a | 中 |
| Free Cash Flow 9M 2026 (USD B) | -4.79 | n/a | n/a | 弱 |
| FCF Margin FY2025 | 18.2% | 約 -2.6pp (FY24 20.8%) | 約 10% | 中 |
| FCF Margin TTM (估算) | 約 4.2% | n/a | 約 10% | 弱 |
| FCF / NI FY2025 | 0.55 | n/a | 約 0.8 | 偏弱 (低於 0.9) |
| Capex (USD B) FY2025 | 91.45 | +74.1% | n/a | 高投資 |
| Capex / Revenue FY2025 | 22.7% | +7.7pp | 約 10% | 高投資 |
| Capex Q3'26 (USD B) | 51.35 | +114% | n/a | 高投資 |
| 流動比率 Current Ratio (Q3'26) | 2.79x | n/a | 約 1.5x | 強 |
| Quick Ratio (info) | 2.51x | n/a | 約 1.2x | 強 |
| 總債務 Total Debt (USD B, Q3'26) | 141.92 | +139% vs FY25 59.29 | n/a | 弱 (擴張迅速) |
| 現金及短期投資 (USD B, Q3'26) | 265.10 | +109% vs FY25 126.84 | n/a | 強 |
| 淨現金估算 (USD B, Q3'26) | 約 123 (cash+STI - debt) | n/a | n/a | 強 (定義需確認) |
| Debt / Equity (info) | 22.2% | n/a | 約 30% | 強 |
| 股票回購 FY2025 (USD B) | 45.71 | -26.6% | n/a | 中 (2026 年 9M 為 0) |
| 股利 FY2025 (USD B) | 10.05 | +36.5% | n/a | 強 (覆蓋充足) |
| 流通股數變動 (FY25 → Q3'26) | 12.09 → 12.29 B | +1.7% | n/a | 弱 (稀釋) |
| 內部人公開市場買賣 (6 個月) | 買入 0 / 賣出 0 | n/a | n/a | 中性 (僅贈與 304.7 M USD) |
| Trailing P/E (GAAP) | 14.9x | n/a | 約 20x | 失真 |
| Trailing P/E (normalized 估算) | 約 26.7x | n/a | 約 20x | 偏貴 |
| Forward P/E | 18.5x | n/a | 約 19x | 中性 |
| EV/EBITDA (TTM) | 18.4x | n/a | 約 13x | 偏貴 |
| P/S (TTM) | 7.4x | n/a | 約 3.5x | 偏貴 |
| P/FCF (TTM 估算) | 約 177x | n/a | 約 30x | 偏貴 (FCF 暫時壓縮) |
| 價格 vs 52 週高點 | -30.3% (408.61 → 284.78) | n/a | n/a | 超跌 |
| 價格 vs 200 日均線 | -16.1% (339.51) | n/a | n/a | 弱勢 |
| 分析師目標價 (平均) | 400.37 USD (+40.6%) | n/a | n/a | 共識偏多 (53 位) |
| 分部營收 (Services / Cloud) | DATA_UNAVAILABLE | n/a | n/a | n/a |
| 公司指引 (Guidance) | DATA_UNAVAILABLE | n/a | n/a | n/a |

## Red flags
- **資本支出爆發 + FCF 轉負**: 9M 2026 capex 131.94 B USD 已超過 FY2025 全年 91.45 B USD; Q2、Q3 2026 FCF 分別為 -5.86 與 -9.06 B USD。
- **負債快速擴張**: 總債務 59.3 → 141.9 B USD (+139%), 9M 2026 債務發行 85.2 B USD, 同時回購停擺 (2026 年 Q1–Q3 皆為 0)。
- **GAAP 獲利被非經常性項目扭曲**: TTM NI 235.7 B USD 中約 100 B USD 來自非營業收益 (Q1 +36.95、Q2 +98.84、Q3 -9.03 B USD 等), 導致 trailing P/E 與 ROE 失真。
- **Q3 2026 獲利下滑**: GAAP EPS 2.12 vs 共識 3.01 (-29.5%), 淨利 YoY -24.3%, 儘管營收 YoY +24.7%、營業利益 YoY +29.9%。
- **折舊攤提加速**: Q3'26 D&A 8.37 B USD, YoY +49%, 未來營業利益率承壓風險。
- **股價技術面弱勢**: 較 52 週高點回落 30%, 低於 50 日與 200 日均線 14–16%。
- **股數稀釋**: 流通股數 +1.7% (FY25 至 Q3'26), 2026 年未回購。
- **資料一致性問題**: (a) info.freeCashflow -1.16 B 與季度加總 +19.8 B 不符; (b) Yahoo Net Debt 68.77 B 與 Total Debt / Cash 欄位無法對齊; (c) Preferred Stock Equity 18.02 B 與 Q2 Net Common Stock Issuance 30.50 B 性質不明; (d) Interest Expense 偏低; (e) info.sharesOutstanding 5.888B 為單一股別; (f) insider 列表中 Brin 2026-08-07 有重複列。以上均已在正文標註, 建議下游在使用前核對。
- **資料缺口**: 分部營收、Cloud/TPU 營收與資本支出拆分、管理層指引、財報後 call 內容均為 DATA_UNAVAILABLE, 無法在本報告量化 AI 題材之貢獻。

FUNDAMENTALS REPORT COMPLETE
