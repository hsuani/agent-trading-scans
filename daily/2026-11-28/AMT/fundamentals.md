# Fundamentals — AMT as of 2026-11-28

資料時點說明：yfinance 快取時間為 2026-11-27 16:34 UTC（regularMarketTime 對應 2026-11-27 16:34:12 UTC），未見 2026-11-28 之後的資料。即時 host 被擋，資料來自 repo 快取（source: cache），屬工具正常回退。fast_info 的 last_price 為 184.525，info 為 184.745（差 0.12%），本報告以 info 為準。USD 金額以 B（十億）與 M（百萬）表示，全文未使用 億。

## Executive summary
AMT 是以長期租約與高穩定現金流為核心的通訊基礎設施 REIT，TTM 營收 USD 11.01B、淨利率 30.1%、2025 年 FCF USD 3.78B，獲利與現金流品質良好（FCF/NI 2025 為 1.50x）。然而總債務 USD 45.29B（TTM EBITDA 倍數約 6.4x）、流動比率 0.35、有形淨值為 -USD 22.32B，財務槓桿與再融資依賴度偏高。估值方面 P/E 26.0x、EV/EBITDA 19.1x、TTM P/FCF 28.4x，相對一般 REIT 經驗值偏貴，且因 FFO/AFFO 無法取得，無法以 REIT 標準指標完整驗證估值；整體體質為「穩定但高槓桿、估值偏高」。

## Revenue & profitability

年度與 TTM 數據（USD B，除 EPS 與百分比外）：

| 期間 | 營收 (USD B) | YoY | 營業利益 (USD B) | 營業利益率 | 淨利-普通股 (USD B) | 淨利率 | 稀釋 EPS (USD) |
|---|---|---|---|---|---|---|---|
| 2022 | 9.65 | n/a | 2.74 | 28.4% | 1.77 | 18.3% | 3.82 |
| 2023 | 10.01 | +3.8% | 3.13 | 31.2% | 1.48 | 14.8% | 3.18 |
| 2024 | 10.13 | +1.1% | 4.52 | 44.6% | 2.26 | 22.3% | 4.82 |
| 2025 | 10.64 | +5.1% | 4.85 | 45.5% | 2.53 | 23.8% | 5.40 |
| TTM（至 2026-Q3） | 11.01 | 見下 | 5.02 | 45.6% | 3.31 | 30.1% | 7.10 |

- 營收成長：2022–2025 三年 CAGR 約 +3.3%（2021 資料為 null，無法計算 5 年 CAGR）。2026-Q3 營收 USD 2.785B，YoY +2.5%（Q3'25 為 USD 2.717B）。
- 毛利：2025 毛利 USD 7.90B / 營收 USD 10.64B = 74.2%（2024 為 74.6%、2023 為 74.4%）。info 的 grossMargins 為 73.5%（TTM 口徑）。
- 獲利趨勢：2026-Q3 淨利 USD 0.766B，YoY -10.3%；稀釋 EPS 1.64 對 1.82，YoY -9.9%。TTM 淨利大幅高於 2025 年度，主因 2025 年度 GAAP 淨利受非營業項目拖累（Other Income Expense 2025 為 USD -0.66B；Gain On Sale of Security 2025 為 USD -0.81B），此類非經常項目使 GAAP EPS 波動大。
- 2024 年度淨利含已停業部門淨額 USD -0.98B（Net Income Discontinuous Operations），同年現金流量表列出出售業務收入 USD 2.16B；2024 年 Net Income Continuous Operations 為 USD 3.26B。
- ROE 32.96%、ROA 4.9%（info）。ROE 偏高主因普通股權益僅 USD 3.65B（2025 年底），屬權益規模極小的結果，不代表資本效率極高。
- ROIC 估計約 10.2%：2025 營業利益（as reported）USD 4.85B × (1 - 稅率 13.7%) = USD 4.18B，除以 Invested Capital USD 40.87B。
- 產業分段（segment mix）：yfinance 無分段營收欄位；longBusinessSummary 僅描述 147,000+ 座通訊站點及美國數據中心（CoreSite）業務。分段營收為 DATA_UNAVAILABLE。

## Cashflow & balance sheet

現金流（USD B）：

| 年度 | OCF | Capex | FCF (OCF-Capex) | FCF margin | FCF/NI | 股利支出 | FCF/股利 |
|---|---|---|---|---|---|---|---|
| 2022 | 3.70 | 1.87 | 1.82 | 18.9% | 1.03x | 2.63 | 0.69x |
| 2023 | 4.72 | 1.80 | 2.92 | 29.2% | 1.97x | 2.95 | 0.99x |
| 2024 | 5.29 | 1.59 | 3.70 | 36.5% | 1.64x | 3.07 | 1.20x |
| 2025 | 5.46 | 1.68 | 3.78 | 35.5% | 1.50x | 3.16 | 1.20x |
| TTM（info） | 5.71 | 隱含 2.69 | 3.02 | 27.4% | 0.91x | 約 3.32（推算） | 約 0.91x（推算） |

- FCF 品質：2025 年 FCF/NI 1.50x，遠高於 0.9 健康門檻；但 TTM（info freeCashflow 3.02B）對 TTM 淨利 3.31B 的比值僅 0.91x，且 TTM 隱含 capex USD 2.69B，明顯高於 2025 年度 capex USD 1.68B。此差異來源不明（季度現金流 quarterly_cf 欄位未取得完整結果），標記為待查。
- 股利覆蓋：2025 年 FCF/股利 1.20x，2022 與 2023 年分別僅 0.69x 與 0.99x。TTM 以 info FCF 推算約 0.91x，若此口徑為準，股利覆蓋轉為不足（推算值，非 yfinance 直接提供）。

資產負債表（USD B）：

| 項目 | 2025-12-31 | 2026-09-30（最新季） |
|---|---|---|
| Total Debt | 44.96 | 45.29 |
| Net Debt（yfinance 欄位） | 35.75 | 35.71 |
| 現金及約當現金（年報） | 1.47 | 不適用（info totalCash 為 1.87） |
| Common Stock Equity（普通股權益） | 3.65 | 不適用 |
| Total Equity 含少數股權 | 10.36 | 不適用 |
| Tangible Book Value | -23.13 | -22.32 |
| Goodwill + Other Intangibles | 26.79 | 不適用 |
| Total Assets | 63.19 | 不適用 |

- 淨債務口徑衝突：yfinance Net Debt 為 USD 35.71B，但以 Total Debt USD 45.29B 減去 info totalCash USD 1.87B 得 USD 43.42B。兩者差距約 USD 7.7B，yfinance Net Debt 欄位與現金列之間的定義不一致，本報告以 Total Debt 口徑為保守估計，並標示差異。
- 槓桿：Total Debt / TTM EBITDA（info ebitda USD 7.08B）= 6.4x；以淨債務 USD 43.42B 計約 6.1x。Debt/Equity（info）463.8%。
- 利息保障：TTM 營業利益 USD 5.02B（季度 Operating Income 加總）/ TTM 利息費用 USD 1.41B（季度 Interest Expense 加總）= 3.6x。利息費用季度趨勢：Q4'25 USD 344.4M、Q1'26 USD 347.3M、Q2'26 USD 354.5M、Q3'26 USD 366.1M（Q3 YoY +5.5%），利率成本呈上升趨勢。
- 流動性：Current ratio 0.353、Quick ratio 0.306（info，最新季）。2025 年 Current Debt USD 3.39B，短期債務依賴滾動再融資。
- 債務到期結構：DATA_UNAVAILABLE（yfinance 無到期表）。
- 債務趨勢：Total Debt 2022 USD 47.05B → 2025 USD 44.96B → 2026-Q3 USD 45.29B（Q3'25 為 USD 45.01B，YoY +0.6%），債務規模近三年大致持平。
- 流動負債 vs 流動資產 2025：Current Liabilities USD 6.91B、Current Assets USD 2.74B，營運資金為負（USD -4.17B），屬 REIT 常見結構。

## Capital allocation & insider signal

資本配置：
- Capex：2025 USD 1.68B（YoY +5.7%，2024 為 USD 1.59B），2022–2023 較高（USD 1.87B、1.80B），2024–2025 投資節奏回升但仍低於 2022 水準。
- 收購：2025 Purchase Of Business USD 0.45B；2024 出售業務收入 USD 2.16B。
- 股利：最新季度股利 USD 1.79，年化 USD 7.16，殖利率 3.88%（5 年平均 3.01%）。exDividendDate 為 2026-09-30，dividendDate 為 2026-10-20（由 timestamp 換算）。下一次除息日為 DATA_UNAVAILABLE。payoutRatio（info）99.6%，此為以 GAAP EPS 計算，REIT 應以 AFFO 計算，AFFO 無法取得。
- 買回：2025 Repurchase USD 0.36B；2024、2023 為 0；2022 USD 0.02B。流通股數由 2025-12-31 的 466.3M 降至 2026-09-30 的 464.2M（-0.46%）。
- 股本稀釋：Diluted Average Shares 2022 462.8M → 2025 468.8M（+1.3%）。
- 融資：2025 發行債務 USD 9.08B、償還 USD 9.45B，淨償還 USD 0.37B。

內部人交易（近 6 個月，即 2026-05-28 起，依 yfinance insider 欄位）：
- 公開市場買入：KALATHUR RAJESH（董事），2026-08-21，2,829 股，USD 500,733（@177.00）。
- 公開市場賣出：
  - FONT JUAN HERNANDEZ（CoreSite 總裁），2026-10-30，592 股，USD 112,261。
  - DOWLING RUTH T（總法律顧問），2026-07-29，1,791 股，USD 309,641。
  - MEYER ROBERT JOSEPH JR（Officer），2026-07-29，5,000 股，USD 894,450。
  - 合計賣出 USD 1,316,352。
- 獎勵發放（Grant，無現金）：BLANCHETT PAUL，2026-10-01，16,299 股。
- 贈與：REEVE PAMELA D A，2026-05-28，810 股。
- 淨額：買入 USD 0.50M、賣出 USD 1.32M，淨賣出 USD 0.82M。相對市值 USD 85.68B 僅約 0.001%，規模極小，不構成明確的內部人方向性訊號。
- 較舊交易（2026-03 CEO 選擇權行使後賣出約 USD 6.3M、CFO 2026-02 賣出 USD 6.6M 等）超出 6 個月窗口，未計入。
- 機構持股：機構持股比例 97.9%，內部人持股 0.1%。前三大持股為 BlackRock 9.79%（45.40M 股）、Vanguard Capital Management 6.58%、Vanguard Portfolio Management 6.01%（2026-09-30 13F 資料）。
- 放空：Short interest 6.41M 股（佔流通股 1.59%），short ratio 2.02 日，放空壓力低。

## Valuation

- 股價：USD 184.745（info regularMarketPrice）；前收 USD 184.59；50 日均線 USD 179.97；200 日均線 USD 178.32；52 週區間 USD 160.06–202.50；Beta 0.842。
- 市值 USD 85.68B；企業價值（EV）USD 135.28B（info，約等於市值 + 總債務 - 現金 + 少數股權）。

估值倍數（以 info 與本報告計算值）：
- P/E TTM 26.0x（184.745 / 7.10）；Forward P/E 26.5x（Forward EPS USD 6.98）；PEG 4.82。
- EV/EBITDA（TTM）19.1x；EV/Revenue 12.3x。
- P/S（TTM）7.8x。
- P/FCF：TTM 28.4x（市值 85.68B / TTM FCF 3.02B）；2025 年度 22.6x（市值 / 2025 FCF 3.78B）。FCF yield TTM 3.5%。
- P/B 24.4x（info，權益規模小所致，參考價值有限）。
- 分析師：24 位分析師，平均目標價 USD 216.13（+17.0%），區間 USD 188–260，推薦平均 1.5（strong_buy）。此為市場情緒參考，非本報告建議。

同業中位數（估計）：yfinance 不提供同業資料，以下為依一般 REIT 經驗之估計值，僅供參考：P/E 約 25–35x（REIT GAAP P/E 常因折舊而偏高）、EV/EBITDA 約 17–20x、P/S 約 6–8x、P/FCF 約 18–22x、股息殖利率約 3–4%、Debt/EBITDA 約 5–6x、淨利率約 15–25%、ROE 約 5–10%。

結論：AMT 各項倍數落在「偏貴但未離譜」區間，EV/EBITDA 與 P/FCF 偏高，股息殖利率 3.88% 略高於一般估計中位數但被高槓桿抵銷。REIT 關鍵指標 FFO/AFFO 無法取得，P/FFO 與 P/AFFO 為 DATA_UNAVAILABLE。

## Key catalysts

- 上次財報：2026-10-27，Q3 稀釋 EPS 1.64 vs 預估 1.63（+0.47%）。前三季 EPS 超預期幅度：2026-07-28 1.87 vs 1.55（+20.7%）、2026-04-28 1.84 vs 1.57（+17.0%）、2026-02-24 1.75 vs 1.47（+19.1%）。近 8 季有 6 季 EPS 超預期，2025-07 與 2025-04 兩季為 GAAP 大幅不及（-53.0%、-33.7%）。
- 下次財報：2027-02-23（yfinance earnings_dates，isEarningsDateEstimate 為 false），EPS 預估 USD 1.65。此日期在 as-of 日之後。
- 指引（guidance）：DATA_UNAVAILABLE（yfinance 無指引文字）。
- 分段或業務變動：yfinance 無分段資料；2024 年有一筆出售業務（現金流 USD 2.16B），標的未在欄位中註明。info 的 name change 日期為 2026-11-26（prevName 為 American Tower Corporation (REIT)），名稱變更本身不影響財務，但需要在後續資料源核實。
- 股利：下次除息日未知（DATA_UNAVAILABLE）。
- 數據中心：CoreSite 為數據中心業務，其 CEO 為 Juan Font；數據中心營收與利潤貢獻 DATA_UNAVAILABLE。

## Red flags

- 高槓桿：Total Debt USD 45.29B，Debt/TTM EBITDA 6.4x，有形淨值 -USD 22.32B（商譽與無形資產 USD 26.79B，佔總資產約 42%）。
- 流動性偏緊：Current ratio 0.35、Quick ratio 0.31，短期債務依賴滾動再融資，到期結構 DATA_UNAVAILABLE。
- 利息成本上升：季度利息費用 Q3'26 較 Q3'25 增 5.5%，利息保障約 3.6x。
- 股利覆蓋轉弱：2025 FCF/股利 1.20x，但 TTM 以 info FCF 推算約 0.91x；payout ratio 以 GAAP EPS 計 99.6%。
- 獲利波動：2026-Q3 淨利 YoY -10.3%；2025 年度 GAAP EPS 受非經常項目影響明顯，TTM 與年度數字差距大。
- 估值偏高：P/E 26.0x、EV/EBITDA 19.1x、P/FCF 28.4x（TTM）、PEG 4.82，缺乏 FFO/AFFO 作為驗證。
- 營收成長偏慢：2025 YoY +5.1%，但 2026-Q3 僅 +2.5%，三年 CAGR 約 3.3%。
- 資料一致性問題（需後續核實）：
  - Net debt 口徑衝突（yfinance USD 35.71B vs Total Debt - Cash USD 43.42B）。
  - TTM capex（隱含 USD 2.69B）與 2025 年度 capex（USD 1.68B）差距大。
  - 2025-Q4 與 2026-Q1 營收皆為 USD 2.7375B，數值完全相同，疑似資料重複。
  - TTM EBITDA（info USD 7.08B）與季度 EBITDA 加總（USD 7.37B）不一致。
  - fast_info 與 info 股價有 0.12% 差距。
- 資料缺口：FFO、AFFO、分段營收、債務到期表、指引、同業中位數、下次除息日均為 DATA_UNAVAILABLE。

## Metrics table

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 TTM (USD B) | 11.01 | Q3 營收 YoY +2.5% | 約 4–6% 成長（估計） | 成長偏慢 |
| 營收 2025 (USD B) | 10.64 | +5.1% | 同上 | 中性 |
| 毛利率 2025 | 74.2% | -0.4pp（2024 為 74.6%） | n/a | 高，但微降 |
| 營業利益率 2025 | 45.5% | +0.9pp | 約 30–40%（估計） | 優於同業（估計） |
| 淨利率 TTM | 30.1% | 2025 為 23.8% | 約 15–25%（估計） | 優於同業（估計） |
| ROE (info) | 33.0% | n/a | 約 5–10%（估計） | 偏高，權益規模小所致 |
| ROIC 2025（估計） | 10.2% | n/a | 約 6–8%（估計） | 中性偏正面 |
| FCF margin 2025 | 35.5% | 2024 為 36.5%（-1.0pp） | 約 25–35%（估計） | 良好 |
| FCF/NI 2025 | 1.50x | 2024 為 1.64x | >0.9 為健康 | 健康 |
| FCF/NI TTM | 0.91x | n/a | >0.9 為健康 | 邊緣 |
| FCF/股利 2025 | 1.20x | 2024 為 1.20x | 約 1.0–1.3x（估計） | 偏薄 |
| Total Debt (USD B, 2026-Q3) | 45.29 | YoY +0.6% | n/a | 高位持平 |
| Net Debt (yfinance, USD B) | 35.71 | 2025 為 35.75 | n/a | 口徑待核實 |
| Debt / TTM EBITDA | 6.4x | n/a | 約 5–6x（估計） | 偏高 |
| 利息保障（TTM，EBIT/利息） | 3.6x | n/a | 約 3–4x（估計） | 中性 |
| Current ratio | 0.35 | n/a | 約 0.5–1.0（估計） | 偏弱 |
| Tangible BV (USD B) | -22.32 | 2025 為 -23.13 | n/a | 負值 |
| Debt / Equity (info) | 463.8% | n/a | n/a | 高槓桿 |
| P/E TTM | 26.0x | n/a | 約 25–35x（估計） | 中性偏貴 |
| Forward P/E | 26.5x | n/a | 同上 | 中性偏貴 |
| EV/EBITDA TTM | 19.1x | n/a | 約 17–20x（估計） | 中性偏貴 |
| P/S TTM | 7.8x | n/a | 約 6–8x（估計） | 中性 |
| P/FCF TTM | 28.4x | 2025 年度為 22.6x | 約 18–22x（估計） | 偏貴 |
| 股息殖利率 | 3.88% | 5 年平均 3.01% | 約 3–4%（估計） | 中性 |
| Payout ratio（GAAP EPS） | 99.6% | n/a | n/a（AFFO 不可得） | 偏高 |
| 內部人 6 個月淨額 (USD M) | -0.82 | n/a | n/a | 規模極小，中性 |
| 放空比例（佔流通股） | 1.59% | n/a | n/a | 低 |
| 分析師平均目標價 | USD 216.13（+17.0%） | n/a | n/a | 市場情緒偏正面（參考） |

FUNDAMENTALS REPORT COMPLETE
