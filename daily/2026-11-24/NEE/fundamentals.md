# Fundamentals — NEE as of 2026-11-24

## Executive summary
NEE（NextEra Energy）為美國最大受監管公用事業與再生能源發電商之一，營收規模穩定（TTM 營收 USD 28.82B），調整後 EPS TTM 約 4.02，近 12 季皆優於一致預期。財務結構承壓明顯：2026-09-30 總債務已升至 USD 113.93B（較 2025-12-31 增加約 19%），TTM 自由現金流 USD 4.09B 不足以覆蓋股利 USD 5.09B，current ratio 僅 0.53。估值方面，調整後 P/E 約 20.8x、forward P/E 19.1x、EV/EBITDA 約 17.6x 至 22.1x，相對一般受監管電力公用事業偏高，分析師平均目標價 USD 94.47（較現價 USD 83.69 上行約 12.9%）；整體屬「成長與股利兼具、但槓桿與估值偏高」的組合，此為基本面描述，不構成交易建議。

資料基準：yfinance 年度報表至 FY2025（2025-12-31），季度報表至 2026-09-30，價格與 info 取自快取（fast_info 來源為 cache，cached_at 2026-11-23 17:54 UTC）。所有使用的事件日期（最近一次財報 2026-10-21、內部人交易 2026-11-02）均早於 as-of 日期 2026-11-24；2026-11-27 除息日與 2027-01-27 財報日為未來日期，視為排程資訊。

## Revenue & profitability

**營收趨勢（USD B）**

| 年度 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|
| Total Revenue | 20.956 | 28.114 | 24.753 | 27.412 |
| YoY | n/a | +34.2% | -12.0% | +10.7% |

- 3 年 CAGR（2022→2025）為 9.4%。資料僅有 2022 年起的年度欄位（2021 為 null），無法計算 3–5 年完整 CAGR。
- 2024 年營收年減 12.0%，yfinance 未提供原因，需由下游查閱 10-K 補充。
- 季度趨勢：2026-Q3（9 月止）營收 USD 8.090B，對應 2025-Q3 的 USD 7.966B，YoY +1.6%；2026-Q1 USD 6.701B、2026-Q2 USD 7.534B。2025-Q1 與 2025-Q2 季度欄位為 null，無法計算上半年 YoY。
- TTM 營收 USD 28.825B，與 info.totalRevenue（USD 28.82B）一致。
- 分部：yfinance 未提供分部營收拆分（segment revenue = n/a）。依 longBusinessSummary，公司分為 FPL（佛州電力）與 NEER（NextEra Energy Resources）兩大分部，截至 2025-12-31 淨發電裝置約 35,963 MW，服務約 600 萬客戶帳戶。

**獲利能力**

- 毛利率：2025 年 62.3%（gross profit USD 170.69B 對營收 USD 274.12B）；TTM 60.2%（info.grossMargins）。
- 營業利益率：2025 年 29.3%（Operating Income USD 8.02B）；TTM 30.0%。
- 淨利率：2025 年（歸屬普通股東 NI USD 6.835B）為 24.9%；TTM GAAP 淨利率為 40.4%（info.profitMargins），明顯因 2026-Q3 GAAP 淨利偏高而失真，見下方。
- 2025 年歸屬普通股東淨利 USD 6.835B，較 2024 年 USD 6.946B 下降 1.6%。
- 稀釋 EPS（GAAP）：2022 年 2.09、2023 年 3.60、2024 年 3.37、2025 年 3.28。
- 調整後 EPS（earnings_dates 的 Reported EPS）：2025-Q4 0.54、2026-Q1 1.09、2026-Q2 1.15、2026-Q3 1.24，TTM 合計 4.02。2026-Q3 實際值 1.24 高於一致預期 1.19（surprise +4.15%）。近期 12 季 EPS surprise 範圍為 +0.8% 至 +13.4%，全部為正。
- GAAP TTM EPS 為 5.55（info.trailingEps），顯著高於調整後 4.02。差額主要來自 2026-Q3：GAAP 稀釋 EPS 2.28 對比調整後 1.24，差距約 USD 1.04/股。季度損益表顯示 2026-Q3 稅前淨利 USD 5.03B，高於營業利益 USD 2.60B 約 USD 2.4B，yfinance 欄位（Other Income Expense USD 0.50B、Earnings From Equity Interest USD 0.29B、Gain On Sale 等）僅能解釋其中一部分，其餘未能拆解，需以 10-Q 附註確認。
- ROE：2025 年以平均股東權益計算約 13.1%（info.returnOnEquity 14.1%）。
- ROIC（估計）：2025 年 EBIT USD 9.10B × (1 − 有效稅率 25.6%) ÷ 平均投入資本 USD 141.3B，約 4.8%。此為本報告自行估算，非工具直接輸出。

## Cashflow & balance sheet

**現金流（USD B）**

| 年度 | 2022 | 2023 | 2024 | 2025 | TTM（至 2026-Q3）|
|---|---|---|---|---|---|
| Operating CF | 8.262 | 11.301 | 13.260 | 12.485 | 14.821 |
| Capex | -9.742 | -9.548 | -8.514 | -9.274 | -10.732 |
| FCF（OCF − Capex）| -1.480 | 1.753 | 4.746 | 3.211 | 4.089 |
| 股利支付 | -3.352 | -3.782 | -4.235 | -4.680 | -5.088 |

- FCF margin：2025 年 11.7%（3.211 ÷ 27.412）。
- FCF / 淨利：2025 年 0.47，低於健康門檻 0.9；OCF / 淨利為 1.83，顯示現金獲利能力正常但資本支出吃掉大部分現金流。以 TTM 調整後淨利估算（約 4.02 × 2.097B 股 ≈ USD 8.4B），FCF / 淨利約 0.49。
- 資料異常：info.freeCashflow 為 USD −21.21B，與季度現金流加總的 TTM FCF USD 4.09B 不一致，本報告採季度加總值，並標示 info.freeCashflow 為不可靠欄位。
- info.operatingCashflow（USD 14.82B）與季度加總一致。

**資產負債表（USD B）**

| 項目 | 2025-12-31 | 2026-09-30 | 變動 |
|---|---|---|---|
| Total Debt | 95.619 | 113.932 | +19.2% |
| Current Debt | 6.063 | 16.807 | +177% |
| Long-term Debt | 89.556 | 97.125 | +8.5% |
| Cash & 等價物 | 2.812 | 5.579 | +98% |
| Net Debt | 92.807 | 108.353 | +16.8% |
| 普通股權益 | 54.608 | 61.498 | +12.6% |
| 含非控制權益總權益 | 66.479 | 74.342 | +11.8% |
| Total Assets | 212.721 | 245.052 | +15.2% |
| Current Assets | 13.584 | 18.586 | +36.8% |
| Current Liabilities | 22.817 | 35.138 | +54.0% |

- Current ratio：2026-09-30 為 0.53（18.586 ÷ 35.138），quick ratio 0.35；營運資金 USD −16.55B。
- 負債權益比：總債務 ÷ 含非控制權益總權益 ≈ 1.53x（info.debtToEquity 153.25）。
- 淨負債 / EBITDA：TTM EBITDA 以季度加總為 USD 16.86B，對應 6.4x；若採 info.ebitda USD 13.40B，則為 8.1x。兩者差異需注意，本報告區間列示。
- 利息覆蓋：2025 年 EBIT USD 9.10B ÷ 利息費用 USD 4.57B ≈ 2.0x。利息費用較 2024 年 USD 2.24B 增加約 105%，為明顯的成本上升訊號。
- 現金水位已由 2025 年底 USD 2.81B 升至 2026-09-30 USD 5.58B，但仍遠低於總債務規模。
- 流動負債中 current debt 由 USD 6.06B 增至 USD 16.81B，短期再融資壓力增加。

## Capital allocation & insider signal

**資本配置**

- 資本支出：2026 年前三季（Q1 3.194、Q2 2.857、Q3 2.459，單位 USD B），TTM 為 USD 10.73B，2022–2025 年維持於 USD 8.5–9.7B 區間。淨 PPE 自 2025-12-31 的 USD 156.2B 增至 2026-09-30 的 USD 177.1B（+13.4%）。
- 股利：info.dividendRate USD 2.49（年化），最近一季股利 USD 0.623（lastDividendValue），股息殖利率 2.99%，5 年平均殖利率 2.51%。2022–2025 年股利支付金額由 USD 3.35B 增至 USD 4.68B，CAGR 約 11.8%。
- 股利覆蓋：2025 年 FCF ÷ 股利 = 0.69x；TTM FCF ÷ 股利 = 0.80x（均低於 1.0）。以調整後 EPS 計算，TTM 4.02 ÷ 年化股利 2.49 = 1.61x，覆蓋來自會計獲利而非現金流，依靠舉債與增發支應資本支出與股利。
- 回購：現金流量表中未見 repurchase 或 buyback 項目，本期無回購（資料顯示為零）。
- 增發：2025 年普通股發行 USD 2.04B；2026-Q3 發行 USD 0.94B。稀釋股數由 2022 年 1.987B 增至 2025 年 2.083B（CAGR 約 1.6%），最新 2026-09-30 流通股數為 2.097B。

**內部人交易（近 6 個月：2026-05-24 起）**

- 公開市場賣出 1 筆：CFO Michael Dunne 於 2026-11-02 以 USD 85.00 賣出 6,888 股，金額 USD 0.59M。
- 公開市場買入：0 筆。
- 過去 12 個月合計賣出 11 筆、金額 USD 19.5M（包括 Armando Pimentel Jr. 2025-11-17 USD 12.2M、CEO John Ketchum 2026-02-09 USD 8.9M 等，多為選擇權行使後賣出）。相對市值 USD 175.5B 約 0.011%，規模可忽略。
- 2026-02-12 有大量例行股票獎勵（如 CEO 157,085 股），屬薪酬性質，不視為市場買賣。
- 內部人持股比例 0.25%。
- 解讀：內部人無買入、賣出金額相對市值極小，訊號中性。

**機構持股**（截至 2026-09-30 季報為主）

- 機構合計持股 87.8%，持股機構數 3,792 家。
- 前幾大持有人：BlackRock 9.45%（198.2M 股，較前期 +6.1%）、Vanguard Capital Management 6.51%（+0.25%）、State Street 5.90%（+3.95%）、JPMorgan 5.71%（+3.11%）、Vanguard Portfolio Management 2.95%（−0.74%）、Morgan Stanley 2.92%（−3.6%）、Geode 2.37%（−0.59%）、Franklin Templeton 2.03%（−4.0%）、Norges Bank 1.53%（2026-06-30 資料，−8.5%）、Wells Fargo 1.49%（+6.8%）。
- 指數型資金為主要持有人，主動型持倉 2026-Q3 呈現淨減持與淨加碼並存，無單一方向性訊號。

## Valuation

**價格與技術位置**

- 現價：USD 83.69（info.currentPrice）；快取 fast_info 為 USD 83.745，差異 0.07%。
- 52 週區間 USD 74.41–98.75，現價位於區間 38% 位置。
- 50 日均線 USD 80.95（現價高於 +3.4%）；200 日均線 USD 87.27（現價低於 −4.1%）。
- Beta 0.60。市值 USD 175.5B，企業價值（EV）USD 296.2B。

**估值倍數**

- P/E（GAAP TTM）15.1x：因 GAAP EPS 含 2026-Q3 非經常性項目而失真，僅供參考。
- P/E（調整後 TTM，4.02）：約 20.8x。
- Forward P/E：19.1x（info.forwardPE，對應 forwardEps USD 4.377，年度基準未標示）。
- EV/EBITDA：22.1x（info.enterpriseToEbitda，採 EBITDA USD 13.40B）；若採季度加總 EBITDA USD 16.86B，為 17.6x。
- P/FCF（TTM）：42.9x；P/OCF（TTM）：11.8x。
- P/S（TTM）：6.09x。P/B：2.85x。

**相對同業（sector median 為本報告估計，非工具輸出）**

- 受監管電力公用事業一般 forward P/E 估計約 17–19x，NEE 略高於區間上緣。
- EV/EBITDA 估計約 12–14x，NEE 偏高，主要反映高槓桿與再生能源開發比重。
- P/B 估計約 1.8–2.2x，NEE 2.85x 偏高。
- 股息殖利率估計約 3.0–3.5%，NEE 2.99% 處於區間低端。

**分析師共識（yfinance，19 位分析師）**

- 評等分布：strongBuy 2、buy 12、hold 7、sell 1、strongSell 0；推薦平均值 1.91（買進區間）。三個月前為 strongBuy 2、buy 10、hold 7、sell 1，買進類評等由 12 增至 14。
- 目標價：平均 USD 94.47（+12.9%）、中位數 USD 99.00（+18.3%）、最高 USD 117.00（+39.8%）、最低 USD 56.00（−33.1%）。

## Key catalysts

- 2026-11-27：除息日（exDividendDate，排程），季股息約 USD 0.623。距 as-of 日期 3 天。
- 2027-01-27：下一次財報（Q4 2026），一致預期 EPS 0.57。此日期來自 yfinance，尚需以公司公告確認。
- 2026-12-31：2026 會計年度結束。
- 再融資：current debt 由 USD 6.06B 增至 USD 16.81B，短期到期債務上升，為需追蹤的事件。
- 利率與融資成本：2025 年利息費用 +105% YoY，若持續增加將壓縮淨利。
- 增發：2026-Q3 普通股發行 USD 0.94B，後續是否延續需觀察。
- 公司指引（guidance）：DATA_UNAVAILABLE。yfinance 不提供管理層財測或指引文字，無法引用。
- 分部轉變：分部營收資料 n/a，無法判斷 FPL 與 NEER 之間的結構性變化。
- 2026-Q3 的非營業獲利（GAAP EPS 2.28 對比調整後 1.24）來源未能拆解，為待釐清事項。

## Metrics table

金額單位：USD B（十億美元）；比率以 % 或 x 表示。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| Total Revenue, 2025 (USD B) | 27.41 | +10.7% | n/a | 成長穩定，但 2024 年曾減 12% |
| Total Revenue, TTM (USD B) | 28.82 | 2026-Q3 YoY +1.6% | n/a | 近期成長趨緩 |
| Gross margin, TTM | 60.2% | n/a | n/a | 結構性高，符合公用事業特性 |
| Operating margin, TTM | 30.0% | n/a | n/a | 中上 |
| Net margin, TTM (GAAP) | 40.4% | n/a | n/a | 失真，含 2026-Q3 非營業項目 |
| Diluted EPS, GAAP TTM (USD) | 5.55 | n/a | n/a | 失真，不作估值依據 |
| Adjusted EPS, TTM (USD) | 4.02 | n/a | n/a | 近 12 季 surprise 皆為正 |
| ROE, 2025 | 13.1% | n/a | 約 9–10% | 優於同業估計 |
| ROIC, 2025（估計） | 4.8% | n/a | 約 5–6% | 偏低，資本支出效率待觀察 |
| FCF, TTM (USD B) | 4.09 | n/a | n/a | 偏弱，低於股利支出 |
| FCF margin, 2025 | 11.7% | n/a | 約 5–10% | 中性 |
| FCF / 淨利, 2025 | 0.47 | n/a | 門檻 0.9 | 不健康 |
| Current ratio, 2026-Q3 | 0.53 | n/a | 約 0.8–1.0 | 偏弱 |
| Total Debt, 2026-Q3 (USD B) | 113.93 | +19.2%（對 2025-12） | n/a | 快速上升 |
| Net Debt / EBITDA | 6.4x（季度 EBITDA）／8.1x（info EBITDA） | n/a | 約 5–6x | 偏高 |
| Debt / Equity（含 NCI） | 1.53x | n/a | n/a | 高槓桿 |
| EBIT / Interest, 2025 | 2.0x | 利息 +105% | n/a | 覆蓋偏薄 |
| Dividend coverage, FCF TTM | 0.80x | n/a | 約 1.0x 以上 | 不足 |
| Dividend coverage, 調整後 EPS | 1.61x | n/a | n/a | 尚可 |
| Dividend yield | 2.99% | 5 年均 2.51% | 約 3.0–3.5% | 中性 |
| Dividends paid, 2025 (USD B) | 4.68 | +10.5% | n/a | 持續增加 |
| Buyback | 0 | n/a | n/a | 無回購 |
| Diluted shares (B) | 2.097（2026-09-30） | 2022→2025 CAGR 1.6% | n/a | 溫和稀釋 |
| P/E, adjusted TTM | 20.8x | n/a | 約 17–19x | 偏高 |
| Forward P/E | 19.1x | n/a | 約 17–19x | 中性偏高 |
| EV/EBITDA | 22.1x（info）／17.6x（季度） | n/a | 約 12–14x | 偏高 |
| P/FCF, TTM | 42.9x | n/a | n/a | 不具參考性 |
| P/B | 2.85x | n/a | 約 1.8–2.2x | 偏高 |
| Price vs 200DMA | −4.1%（USD 87.27） | n/a | n/a | 位於長期均線下方 |
| Analyst mean target (USD) | 94.47（+12.9%） | n/a | n/a | 上行空間中等 |
| Insider sales, 12 個月 (USD M) | 19.5（0.011% 市值） | n/a | n/a | 中性，規模可忽略 |
| Institutional ownership | 87.8% | n/a | n/a | 機構持股高 |

## Red flags
- 股利超過自由現金流：TTM 股利 USD 5.09B 高於 FCF USD 4.09B，2025 年股利覆蓋 0.69x；股利成長依賴舉債與增發。
- 負債快速擴張：總債務於 9 個月內增加約 19%，淨負債 / EBITDA 估計 6.4x–8.1x，current ratio 0.53。
- 利息成本上升：2025 年利息費用較 2024 年增加約 105%，EBIT 利息覆蓋僅約 2.0x。
- 短期債務壓力：current debt 由 USD 6.06B 增至 USD 16.81B。
- GAAP 與調整後獲利差距：2026-Q3 GAAP EPS 2.28 對比調整後 1.24，未能從工具資料拆解，TTM GAAP 獲利與淨利率（40.4%）不宜直接用於估值。
- 估值偏高：調整後 P/E 約 20.8x、EV/EBITDA 最高至 22.1x、P/B 2.85x，相對一般公用事業估計區間偏高；股價位於 200 日均線下方 4.1%。
- ROIC 估計僅約 4.8%，資本支出高峰期投入報酬偏低。
- 資料一致性：info.freeCashflow（USD −21.21B）與季度 FCF 加總（USD +4.09B）不一致；info.ebitda（USD 13.40B）與季度 EBITDA 加總（USD 16.86B）不一致。本報告分別標示。
- 資料缺口：2025 年第一季與第二季季度財報為 null；分部營收、公司指引、sector median 均非工具直接提供（sector median 為本報告估計）。
- 2024 年營收年減 12.0%，工具資料未提供原因。

## 資料與來源註記
- 工具：pipeline/tools/yf.py（info、financials、quarterly_fin、balance_sheet、quarterly_bs、cashflow、quarterly_cf、earnings_dates、rec_summary、insider、major_holders、inst_holders、fast_info）。
- info 與 fast_info 在執行時遇到 cookie/crumb 取得失敗，已依 cache fallback 正常回傳資料，屬預期行為，非錯誤。
- 本報告未包含 as-of 2026-11-24 之後的資料。

FUNDAMENTALS REPORT COMPLETE
