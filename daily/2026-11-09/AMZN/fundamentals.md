# Fundamentals — AMZN as of 2026-11-09

## Executive summary
AMZN 獲利能力明顯改善（FY2025 營業利益率 11.2%、Q3'26 營業利益率 13.9%），但 2026 年資本支出大幅放大，TTM 自由現金流為 -34.7B USD，總負債（BS 口徑）在 2026 年前三季由 153.0B 增至 271.9B USD，財務體質正由「高現金流」轉向「高資本支出、高舉債」。估值上，trailing P/E 20.96x 受 Q2'26 一次性 EPS 5.75 拉低，剔除後約 27.6x（估計）；forward P/E 23.78x、EV/EBITDA 16.3x 處於大型成長股合理區間，sell-side 平均目標價 326.99 USD 高於現價 259.30 USD，但估值是否合理取決於 AWS AI 資本支出能否在 2027 年後轉化為現金流。

資料狀態：所有數字來自 `pipeline/tools/yf` 輸出，`source: cache`（cached_at 2026-11-08T13:14:39Z），屬正常回退，不是錯誤。Q2'26（2026-06-30）季度的營收、淨利、資產負債表在工具中缺漏，以 DATA_UNAVAILABLE 標示。全部資料日期均不晚於 as-of 2026-11-09，無資料後置問題。

## Revenue & profitability

**營收與成長（單位：USD B）**

| 年度 | Total Revenue | YoY | Gross Profit | 毛利率 | Operating Income | 營業利益率 | Net Income | 淨利率 |
|---|---|---|---|---|---|---|---|---|
| FY2022 | 513.98 | n/a | 225.15 | 43.8% | 12.25 | 2.4% | -2.72 | -0.5% |
| FY2023 | 574.78 | +11.8% | 270.05 | 47.0% | 36.85 | 6.4% | 30.43 | 5.3% |
| FY2024 | 637.96 | +11.0% | 311.67 | 48.9% | 68.59 | 10.7% | 59.25 | 9.3% |
| FY2025 | 716.92 | +12.4% | 360.51 | 50.3% | 79.97 | 11.2% | 77.67 | 10.8% |

- 3 年 CAGR（FY2022 至 FY2025）為 11.7%。工具只提供 4 個年度，無法計算 5 年 CAGR，此處為 DATA_UNAVAILABLE（5 年）。
- 2025 年 Net Income 增幅 31.1%（77.67 / 59.25），遠高於營收增幅，主要來自營業利益率提升與 Total Unusual Items 15.32B（FY2025，tax effect 為 3.00B）。
- 季度 Total Revenue（USD B）：Q1'25 155.66（由 FY2025 扣除其他三季推算）、Q2'25 167.70、Q3'25 180.17、Q4'25 213.39、Q1'26 181.52（YoY +16.6%）、Q2'26 DATA_UNAVAILABLE、Q3'26 201.94（YoY +12.1%）。
- Q3'26 毛利 107.37B（毛利率 53.2%，去年同期 50.8%）；營業利益 28.08B（營業利益率 13.9%，去年同期 9.7%，YoY +61%）。
- Q3'26 Net Income 20.68B，YoY -2.4%（與 yfinance earningsQuarterlyGrowth -0.024 一致）。營業利益上升但淨利下滑，原因是 Q3'26 Pretax Income 26.87B 低於營業利益，利息支出由 Q3'25 的 0.54B 升至 1.69B，Net Interest Income 由 +0.56B 轉為 -0.50B。
- 報酬指標（info 欄位，TTM）：ROE 27.4%、ROA 6.6%。ROIC 以 FY2025 營業利益 79.97B × (1 - 稅率 19.6%) ÷ (權益 411.06B + 總負債 152.99B - 現金與短期投資 123.03B) 推算約 14.6%（估計）。

**Segment mix**：工具的 `longBusinessSummary` 只描述三大分部（North America、International、AWS），未提供分部營收數字，分部營收與分部營業利益為 DATA_UNAVAILABLE。

## Cashflow & balance sheet

**現金流（單位：USD B）**

| 年度 | Operating CF | Capex | FCF | FCF margin | FCF / NI |
|---|---|---|---|---|---|
| FY2022 | 46.75 | 63.65 | -16.89 | -3.3% | n/a |
| FY2023 | 84.95 | 52.73 | 32.22 | 5.6% | 1.06 |
| FY2024 | 115.88 | 83.00 | 32.88 | 5.2% | 0.55 |
| FY2025 | 139.51 | 131.82 | 7.70 | 1.1% | 0.10 |

- FY2025 FCF / NI 僅 0.10，遠低於 0.9 健康門檻。OCF / NI 為 1.80，說明問題在於資本支出，不在應計品質。FCF 計算已對照 OCF - Capex 驗證（139.51 - 131.82 = 7.69）。
- SBC（FY2025）19.47B，約占營收 2.7%。
- TTM（info）：Operating CF 168.30B、FCF -34.73B，推算 TTM Capex 約 203.0B（derived），占 TTM 營收 797.46B 的 25.5%。
- 季度：Q4'25 FCF +14.94B；Q1'26 FCF -18.17B（Capex 44.20B）；Q2'26 DATA_UNAVAILABLE；Q3'26 FCF -34.84B（OCF 42.42B、Capex 77.26B）。Q3'26 Capex 占 OCF 達 182%，去年同期 Capex 為 35.09B，YoY +120%。

**資產負債表（單位：USD B）**

| 項目 | 2025-12 (FY) | 2026-03 (Q1) | 2026-09 (Q3) |
|---|---|---|---|
| Cash & Cash Equivalents | 86.81 | 101.82 | 55.78 |
| Cash + ST Investments | 123.03 | 143.09 | 114.23 |
| Total Debt（BS，含 capital lease） | 152.99 | 209.89 | 271.95 |
| Long Term Debt | 65.65 | 119.07 | 173.12 |
| Capital Lease Obligations | 87.34 | 90.81 | 98.82 |
| Net Debt（BS 欄位） | n/a | 17.26 | 117.34 |
| Total Assets | 818.04 | 916.63 | 1243.39 |
| Stockholders Equity | 411.06 | 441.91 | 613.60 |
| Total Liabilities | 406.98 | 474.72 | 629.79 |
| Current Ratio | 1.05（derived） | 0.99（derived）| 0.99（derived）|

- 淨負債（自行推算，BS Total Debt - Cash+STI）：2026-09 為 157.7B；若用 info totalDebt 304.84B 則為 190.6B。兩者與 BS「Net Debt」欄位 117.34B 無法對上，已列為資料品質問題。
- 2026-09 info 指標：Current Ratio 0.989、Quick Ratio 0.793、Debt/Equity 49.68%（以 info totalDebt 304.84B 除權益 613.60B 得出，與工具一致）；BS 口徑 Debt/Equity 約 44.3%（derived）。2025-12 BS 口徑約 37.2%（derived）。
- Working Capital 由 2026-03 的 38.40B 降至 2026-09 的 -2.88B。
- 利息支出：Q3'26 1.69B，Q3'25 0.54B（約 3 倍）。
- 總負債在 9 個月內增加約 119B（Total Debt 152.99B → 271.95B，+78%），其中 Long Term Debt 增加 107.5B。現金與短期投資由 123.03B 降至 114.23B。
- 權益由 411.06B 跳升至 613.60B（+49%），其中 Other Equity Adjustments 由 28.23B 增至 102.28B。工具未說明此科目來源，此處不推測原因，需以 10-Q 附註核實。
- 異常：Gross PPE 2025-09 為 407.89B，2025-12 跳至 620.15B，2026-09 為 605.77B。Q4'25 Capex 只有 39.52B，無法解釋 212B 跳升，判定為口徑或重分類問題，不作為資本投入的依據。

## Capital allocation & insider signal

**資本配置**
- Capex：FY2022 63.65B → FY2023 52.73B → FY2024 83.00B → FY2025 131.82B（FY2025 YoY +58.8%）。FY2025 Capex 占營收 18.4%，FY2024 為 13.0%。2026 年前三季 Capex 明顯更高（Q1 44.20B、Q3 77.26B），Q2 DATA_UNAVAILABLE。
- 股票回購：FY2023、FY2024 為 0；FY2025 欄位為 None（DATA_UNAVAILABLE），2022 年為 6.00B。過去三年未回購。
- 股利：info 的 dividendRate 欄位缺漏，payoutRatio 0.0，trailingAnnualDividendYield 0.0。AMZN 不配息，股利覆蓋率為 n/a。
- 股本：Ordinary Shares 由 2024 年 10.59B 增至 2025 年 10.73B（+1.3%），Diluted Average Shares 由 10.721B 增至 10.827B（+1.0%），SBC 稀釋仍在持續。Q3'26 Ordinary Shares 為 10.81B。

**內部人交易（yfinance insider，過去 6 個月：2026-05-08 至 2026-11-08）**

| 類別 | 筆數 | 股數 | 金額 (USD M) |
|---|---|---|---|
| 公開市場賣出（全部） | 21 | 1,359,105 | 385.5 |
| 其中 Bezos（2026-08-03，286.41 USD/股） | 1 | 1,209,649 | 346.5 |
| 其餘內部人賣出 | 20 | 149,456 | 39.1 |
| 贈與（Stock Gift，無金額） | 2 | 437,580 | 0 |

- 合計賣出金額 385.5M USD 占市值 2,803.8B USD 約 0.014%；排除 Bezos 後約 0.0014%。量級很小，不構成強烈的內部人負面訊號。
- 內部人持股比例 8.83%（major_holders insidersPercentHeld）。
- 行為模式：CEO Jassy 每季約 20,000 股賣出（2025-11-21、2026-02-23、2026-05-21、2026-08-21），各季同時有 49,680–50,000 股的 RSU 歸屬紀錄（Value 0），與歸屬後的例行賣出吻合。Herrington 每月 1,000 股的小額賣出亦屬例行計畫。
- 非例行大額賣出：2026-04 Jassy 兩筆合計 62,352 股（約 16.5M USD，價格 255–275 USD）；Herrington 2026-04 至 05 兩筆合計 49,000 股（約 12.9M USD）。這些在 6 個月窗口之外，但應納入 trader 的參考資料。
- Q1'26 有 2 位董事（Nooyi、Ng）的 RSU 紀錄；2026-02 至 2026-04 有 Rubinstein、Alexander 的小額賣出。金額小。

## Valuation

**估值（price 259.30 USD，source: cache）**

| 指標 | 數值 | 來源 / 計算 |
|---|---|---|
| Market Cap | 2,803.8B USD | info（259.30 × 10.813B 股，已驗證） |
| Enterprise Value | 2,994.5B USD | info |
| Trailing P/E | 20.96x | info（trailingEps 12.37） |
| Trailing P/E（剔除 Q2'26 一次性 EPS，以 Q1'26 2.78 代入） | 約 27.6x | 估計：EPS 9.40，非工具輸出 |
| Forward P/E | 23.78x | info（forwardEps 10.90） |
| PEG | 1.20 | info |
| EV/EBITDA (TTM) | 16.3x | info（TTM EBITDA 約 183.7B，由 ebitdaMargins × totalRevenue 推算） |
| P/S (TTM) | 3.52x | info，已驗證（2,803.8 / 797.5） |
| P/FCF (TTM) | n/a | TTM FCF 為負值（-34.73B） |
| P/B | 4.57x | info（bookValue 56.757） |

- Trailing EPS 12.37 = Q4'25 1.95 + Q1'26 2.78 + Q2'26 5.75 + Q3'26 1.89，其中 Q2'26 EPS 較 consensus 1.82 高 215%，屬一次性項目，NI 與 Operating Income 數字在工具中缺漏，無法拆解來源。Q1'26 Total Unusual Items 達 15.68B，也推升了當季 EPS。因此 trailing P/E 20.96x 被低估，不宜作為估值依據。
- Forward P/E 23.78x 以 forwardEps 10.90 計算（已驗證 259.30 / 10.90）。
- 分析師共識（info，59 位）：目標價平均 326.99 USD（+26.1%）、最高 405.00 USD（+56.2%）、最低 230.00 USD（-11.3%）；recommendationMean 1.33（strong_buy）。此為外部共識，不是本報告的評價。
- 股價位置：52 週高點 287.20 USD（現價低 9.7%）、52 週低點 196.00 USD（現價高 32.3%）；50 日均線 253.95 USD、200 日均線 243.94 USD，現價在兩線之上。

## Key catalysts
- 下次財報：2027-02-04（earnings_dates），EPS consensus 2.40 USD（推測為 Q4'26）。
- 前次財報：2026-10-29，Q3'26 EPS 1.89，低於 consensus 1.96（-3.5%）。營收 201.94B 高於去年同期 12.1%，但 EPS 未達標，主要受利息支出與稅後淨額拖累。
- 資料注意：info 的 earningsTimestamp（1793304000）約對應 2026-10-29，已過期，不應作為下次財報日期。以 earnings_dates 為準。
- AWS AI 資本支出：TTM Capex 約 203B（derived），Q3'26 Capex 77.26B。資本支出回收速度、AWS 營收與營業利益貢獻，工具未提供分部數據，需由 10-Q 分部附註或後續法說補充（DATA_UNAVAILABLE）。
- 融資結構變化：Long Term Debt 9 個月內增加 107.5B。後續債券發行、利率與利息支出走勢，為財務槓桿的主要觀察點。
- 股權科目變化：Other Equity Adjustments 102.28B，來源需由 10-Q 核實（DATA_UNAVAILABLE）。

## Metrics table

單位：USD B（營收、利潤、現金流、資產負債表、市值）；USD（股價、EPS）；倍數為 x；比率為 %。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| Total Revenue（FY2025，USD B） | 716.92 | +12.4% | n/a（工具未提供同業數字） | 成長穩健 |
| Total Revenue（Q3'26，USD B） | 201.94 | +12.1% | n/a | 成長穩健 |
| Gross Margin（FY2025） | 50.3% | +1.4 pt | 約 35–45%（估計） | 優於同業（估計） |
| Operating Margin（Q3'26） | 13.9% | +4.2 pt | 約 6–10%（估計） | 改善明顯 |
| Net Margin（FY2025） | 10.8% | +1.5 pt | 約 5–8%（估計） | 良好 |
| ROE（TTM，info） | 27.4% | n/a | 約 15–20%（估計） | 強 |
| ROIC（FY2025，derived） | 14.6% | n/a | 約 10–12%（估計） | 尚可 |
| FCF（FY2025，USD B） | 7.70 | -76.6% | n/a | 弱，受 Capex 壓縮 |
| FCF（TTM，USD B） | -34.73 | n/a | n/a | 紅旗 |
| FCF Margin（FY2025） | 1.1% | -4.1 pt | 約 3–5%（估計） | 弱 |
| FCF / NI（FY2025） | 0.10 | 低於 0.9 門檻 | 約 0.8–1.0（估計） | 紅旗 |
| Capex（FY2025，USD B） | 131.82 | +58.8% | n/a | 投資加速 |
| Capex / OCF（Q3'26） | 182% | 去年同期約 108%（35.09 / 32.52，derived） | n/a | 紅旗 |
| Total Debt（2026-09，BS，USD B） | 271.95 | 2025-12 為 152.99（9 個月 +78%） | n/a | 紅旗 |
| Net Debt（2026-09，derived，USD B） | 157.7 | n/a | n/a | 上升中 |
| Debt / Equity（info） | 49.68% | n/a | 約 40–60%（估計） | 中性偏高 |
| Current Ratio（info） | 0.99 | n/a | 約 1.0–1.3（估計） | 偏低，需留意 |
| Cash + ST Investments（2026-09，USD B） | 114.23 | 2025-12 為 123.03（-7.2%） | n/a | 持平 |
| SBC（FY2025，占營收） | 2.7% | 2024 為 3.5%（derived） | n/a | 可接受 |
| 股利 / 回購（FY2025） | 無配息；回購 DATA_UNAVAILABLE（欄位 None） | n/a | n/a | 資本配置以 Capex 為主 |
| 內部人淨賣出（6 個月，USD M） | 385.5（含 Bezos 346.5） | n/a | n/a | 量級小，多為例行計畫 |
| Market Cap（USD B） | 2,803.8 | n/a | n/a | n/a |
| Trailing P/E | 20.96x（剔除一次性後約 27.6x，估計） | n/a | 約 25–30x（估計） | 中性 |
| Forward P/E | 23.78x | n/a | 約 20–25x（估計） | 中性偏合理 |
| EV/EBITDA（TTM） | 16.3x | n/a | 約 12–15x（估計） | 略高 |
| P/S（TTM） | 3.52x | n/a | 約 1.0–2.0x（估計） | 偏高 |
| P/FCF（TTM） | n/a（FCF 為負） | n/a | n/a | 無法評估 |
| PEG | 1.20 | n/a | n/a | 合理 |
| 分析師目標價均值（USD） | 326.99（+26.1%） | n/a | n/a | 共識偏多 |

## Red flags
- TTM 自由現金流為 -34.73B USD，Q3'26 Capex 占 OCF 182%。FY2025 FCF / NI 僅 0.10，遠低於 0.9 健康門檻。
- 總負債（BS）在 9 個月內由 152.99B 增至 271.95B USD（+78%），Long Term Debt 增加 107.5B；Q3'26 利息支出約為去年同期 3 倍，Net Interest Income 轉負。
- Current Ratio 0.99、Working Capital 轉為 -2.88B USD，短期流動性緩衝變薄。
- Q3'26 EPS 1.89 低於 consensus 1.96（-3.5%），淨利 YoY -2.4%，儘管營業利益 YoY +61%。
- trailing EPS 含 Q2'26 一次性 EPS 5.75（+215% surprise），Q2'26 營收、淨利、資產負債表在工具中缺漏。trailing P/E 因此失真。
- 資料品質：(a) Gross PPE 在 2025-09 至 2025-12 間跳升 212B，與同期 Capex 不相容；(b) BS「Net Debt」117.34B 與 Total Debt - Cash 157.7B 不一致；(c) info totalDebt 304.84B 與 BS Total Debt 271.95B 不一致；(d) info earningsTimestamp 已過期。以上均未直接採用為結論，僅作為風險提示。
- 權益 411.06B → 613.60B（+49%），Other Equity Adjustments 102.28B 來源不明，工具未提供說明。
- Bezos 2026-08-03 單筆賣出 1,209,649 股（約 346.5M USD）為窗口內最大內部人交易，並有 2026-08-26 的 415,580 股贈與。量級占市值極小，但屬於市場會關注的訊號。
- 股價處於 52 週高點下方 9.7%，短期未破位。shortPercentOfFloat 0.95%，空方壓力低。

FUNDAMENTALS REPORT COMPLETE
