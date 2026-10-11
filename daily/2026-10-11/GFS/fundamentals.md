# Fundamentals — GFS (GlobalFoundries Inc.) as of 2026-10-11

## Executive summary
GFS 財務體質穩健：Q2'26 末帳上現金及短期投資 2,388M USD、總債務 1,678M USD（info 口徑淨現金約 679M USD），流動比率 2.48，TTM FCF 796M USD，FCF/NI 約 1.11。然而營收長期停滯（2022-2025 營收 CAGR -5.7%，2025 年僅 +0.6%），TTM GAAP 淨利率 10.3%，ROIC 估約 5%，獲利能力仍偏弱。估值方面，TTM GAAP P/E 37.7x 偏高、前瞻 P/E 18.4x 與 EV/EBITDA 13.0x 相對合理，分析師平均目標價 74.68 USD 較現價 48.24 USD 高約 55%；本報告不提供交易建議。

資料時效：價格為 2026-10-09 收盤（yfinance regularMarketTime 對應 2026-10-09 20:00 UTC），快取時間 2026-10-11 12:38 UTC；財報資料至 2026-06-30 (Q2'26)。下次財報日 2026-11-04 為未來排程事件，非已發生資料。

## Revenue & profitability

**營收趨勢（annual, USD M）**
| 年度 | Total Revenue | YoY | Gross Profit | Gross Margin | Operating Income | Op Margin | Net Income | Net Margin |
|---|---|---|---|---|---|---|---|---|
| 2022 | 8,108 | — | 2,239 | 27.6% | 1,261 | 15.6% | 1,448 | 17.9% |
| 2023 | 7,392 | -8.8% | 2,101 | 28.4% | 1,200 | 16.2% | 1,020 | 13.8% |
| 2024 | 6,750 | -8.7% | 1,651 | 24.5% | 728 | 10.8% | -265 | -3.9% |
| 2025 | 6,791 | +0.6% | 1,690 | 24.9% | 797 | 11.7% | 885 | 13.0% |

- 3 年 CAGR（2022→2025）：約 -5.7%。2021 年欄位為 null，無法計算 3-5 年以上 CAGR。
- 2024 年 GAAP 虧損主因為 impairment 935M USD（cashflow 欄位 Asset Impairment Charge），屬非經常性項目；2025 年淨利 885M 含 unusual items 約 76M 且 Q1'25 淨利於 quarterly 欄位未列出，年度數字需保守解讀。
- TTM（Q3'25～Q2'26）營收 6,938M USD（與 info totalRevenue 6,937,999,872 吻合）。Q2'26 營收 1,786M，對比 Q2'25 1,688M，YoY +5.8%。Q1'26 營收 1,634M（Q1'25 欄位缺漏，無法計算 YoY）。
- TTM 毛利率 約 27.7%（Q3'25 419/1,688=24.8%、Q4'25 508/1,830=27.8%、Q1'26 451/1,634=27.6%、Q2'26 505/1,786=28.3%），較 2024-2025 年度水準 24.5%-24.9% 明顯改善，已回到 2022-2023 年度 27.6%-28.4% 區間附近。
- TTM 營業利率 11.6%（804/6,938）；TTM GAAP 淨利率 10.3%（716/6,938，與 info profitMargins 0.1032 一致）。Q2'26 營業利率 9.7%，較 Q1'26 11.0% 下滑。
- ROE：TTM 淨利 716 / 期末股東權益 11,818 = 約 6.1%；2025 年以平均權益計 約 7.8%。
- ROIC：以 TTM 營業利益 804M、期末 Invested Capital 12,940M 估算，稅率 14.8%（Q2'26 Tax Rate for Calcs）時約 5.3%，稅率 21% 時約 4.9%。此為本報告自行估算，yfinance 未直接提供 ROIC。
- 營收結構（segment mix）：info.longBusinessSummary 僅提及 mainstream wafer fabrication、quantum technology solutions，**未提供分部營收**，segment mix 為 DATA_UNAVAILABLE。

## Cashflow & balance sheet

**現金流（USD M）**
| 期間 | OCF | Capex | FCF | FCF Margin | FCF/NI |
|---|---|---|---|---|---|
| 2023 | 2,125 | 1,804 | 321 | 4.3% | 0.31 |
| 2024 | 1,722 | 625 | 1,097 | 16.3% | n.m.（NI 為負） |
| 2025 | 1,731 | 722 | 1,009 | 14.9% | 1.14 |
| TTM（至 Q2'26） | 1,916 | 1,120 | 796 | 11.5% | 1.11 |

- Quarterly FCF：Q3'25 406、Q4'25 166、Q1'26 230、Q2'26 -6。Q2'26 FCF 轉負，主因 Capex 411M（YoY +158%，Q2'25 為 159M）。
- FCF/NI TTM 1.11，高於 0.9 健康門檻；但 2025 年 NI 含非經常性收益，需留意。
- 營運資金：Change in Working Capital 2025 年 -538M；Q2'26 -115M，應收帳款 Q2'26 1,458M（Q1'26 1,279M）回升，為 OCF 壓力來源之一。

**資產負債表（USD M）**
| 項目 | 2025-12-31 | 2026-03-31 | 2026-06-30 |
|---|---|---|---|
| Cash & Equivalents | 1,809 | 1,849 | 1,087 |
| Cash + ST Investments | 3,103 | 3,071 | 2,388 |
| Total Debt | 1,707 | 1,724 | 1,678 |
| Long-Term Debt | 1,065 | 1,063 | 1,024 |
| Current Liabilities | 2,368 | 2,329 | 2,209 |
| Current Assets | 6,205 | 6,036 | 5,468 |
| Inventory | 1,577 | 1,686 | 1,622 |
| Total Assets | 17,141 | 16,897 | 16,888 |
| Stockholders' Equity | 11,928 | 11,693 | 11,818 |
| Goodwill | 407 | n/a | n/a |

- 淨負債：info totalCash 2,357M 減 totalDebt 1,678M = 淨現金約 679M（以 BS 現金+STI 計約 710M）。yfinance quarterly_bs 之 Net Debt 欄位為 35M（口徑不明，與上述不一致，見 Red flags）。
- 槓桿：Debt/Equity 約 14.1%（info debtToEquity 14.132，為百分比口徑）。總債務自 2022 年 2,856M 降至 2026-06 1,678M，去槓桿明顯。
- 流動性：Current Ratio 2.48（Q2'26 計算 5,468/2,209=2.48，與 info 2.475 一致）；Quick Ratio 1.73（info）。
- 現金：Q2'26 Cash & Equivalents 單季減少 762M，主要動用項目為 Purchase of Business 440M、Net Investment Purchase 299M、Capex 411M，同期 OCF 為 405M。
- Goodwill 自 2024 年 75M 升至 2025 年 407M，表示 2025 年併購活動增加（2025 年 Purchase of Business 合計 682M）。收購標的之名稱與交易條件**未見於工具輸出，DATA_UNAVAILABLE**。

## Capital allocation & insider signal

**資本配置**
- Capex：2022 3,059M → 2023 1,804M → 2024 625M → 2025 722M，2024-2025 為低檔；TTM 1,120M（佔營收 16.1%），Q2'26 單季 411M 顯示投資回升。Capex 回升方向與營收尚未同步成長，需留意資本效率。
- 股票回購：2024 年 200M、2025 年 5M、Q1'26 單季 430M（同期 FCF 230M，回購超過當季 FCF）、Q2'26 3M。TTM 回購約 438M。流通股數 2025-12-31 555.9M → 2026-06-30 548.8M（-1.3%）。
- 股息：info 顯示 dividendRate 0.48 USD（年化）、dividendYield 1.0%、lastDividendValue 0.12 USD（單季）、exDividendDate 2026-09-23、dividendDate（發放日）2026-10-09。以年化 0.48 × 557.4M 股 估算年派息現金約 268M，TTM FCF 796M 之覆蓋倍數約 3.0x。注意：cashflow 歷史年度資料無 Cash Dividends Paid 欄位，無法與歷史派息交叉驗證；info 的 payoutRatio 0.0938 疑似以單季股利 0.12 除以 TTM EPS 1.28 計算，與年化口徑不一致。
- 併購：2025 年 682M、2026 Q2 440M，為近期主要資本支出之外的資金用途。

**內部人交易（2026-04-11 至 2026-10-11，共 58 筆紀錄中之近 6 個月部分）**
| 內部人 | 職位 | 賣出金額 (USD) |
|---|---|---|
| HOGAN MICHAEL JAMES | Officer | 約 1.40M |
| VICARI SAMUEL | Officer | 約 0.66M |
| AZAR SAMAK L | Officer（CLO） | 約 0.52M |
| DORCHAK GLENDA MARY | Director | 約 0.47M |
| RAMAN PRADHEEPA | Officer | 約 0.45M |

- 6 個月合計：淨賣出約 3.50M USD，約 53,499 股；**無公開市場買入紀錄**。另有 2026-07-28 董事股票獎勵合計約 11,484 股（Value 0，屬授予非市場交易）。
- 賣出金額佔市值 26.89B 約 0.013%，規模極小。AZAR 之定期小額賣出（約每週 335-500 股）呈規律性，較像計畫性出售而非資訊性減持。
- 內部人持股比例 heldPercentInsiders 0.058%，幾乎無內部人持股基礎。
- 機構持股：Mubadala Investment Co PJSC 持股 72.8%（399.6M 股，2026-06-30 季報，較前期 -5.55%）為主要股東；FMR 12.7%（+9.0%）、T. Rowe Price 0.73%（+61.4%）、JPMorgan 1.23%（+33.3%）。major_holders 之 institutionsPercentHeld 為 100.2%，超過 100%，為資料口徑重複計算，**不採用**。
- 流通股 floatShares 148.4M，約為總股本 27%，流通性受限於大股東持股。
- 空單：sharesShort 7.00M（前月 6.41M，+9.2%），shortPercentOfFloat 13.6%，shortRatio 1.79 日。

## Valuation

| 指標 | 數值 | 來源 / 計算 |
|---|---|---|
| 現價 | 48.24 USD | 2026-10-09 收盤，previousClose 49.36 |
| 市值 | 26.89B USD | info marketCap；48.24 × 557.4M 股 驗證吻合 |
| 企業價值 EV | 25.85B USD | info enterpriseValue |
| Trailing P/E (GAAP) | 37.7x | 48.24 / TTM EPS 1.28 |
| Forward P/E | 18.4x | 48.24 / forwardEps 2.62（yfinance 未標註期別，推測為 FY2027 共識） |
| FY2026E P/E | 24.7x | 48.24 / epsCurrentYear 1.955 |
| 調整後 TTM EPS 之 P/E | 約 26.5x | earnings_dates 最近四季 Reported EPS 合計 1.82（adjusted 口徑，與 GAAP 1.28 不同） |
| EV/EBITDA | 13.0x | info enterpriseToEbitda；EBITDA 1,981M（TTM） |
| EV/Revenue | 3.7x | info enterpriseToRevenue |
| P/S | 3.9x | info priceToSalesTrailing12Months |
| P/FCF (TTM) | 33.8x | 26,890 / 796 |
| P/B | 2.24x | info priceToBook；bookValue 21.54 USD/股 |
| PEG | 0.72 | info pegRatio（基於 yfinance 成長率估計） |

- 分析師共識：22 位分析師，recommendationMean 2.04（averageAnalystRating "2.0 - Buy"）；目標價 平均 74.68 / 中位 71.0 / 高 140.0 / 低 51.0 USD。相對現價：平均目標 +54.8%、最低目標 +5.7%。
- 股價位置：52 週區間 32.02–92.55 USD，現價較 52 週高點 -47.9%，較 52 週低點 +50.7%；較 50 日均線 47.93 USD 約 +0.6%，較 200 日均線 54.55 USD 約 -11.6%。Beta 1.765。
- 估值判讀：以前瞻 EPS 看 P/E 偏低，以 TTM GAAP EPS 看偏高，兩者差異主要來自 2025-2026 年 GAAP 獲利之非經常性與稅務波動。EV/EBITDA 13.0x 相對於低成長的代工業務並無明顯折價或溢價之工具數據支持。

## Key catalysts
- **下次財報**：2026-11-04（yfinance earningsTimestamp 2026-11-04 12:30 UTC，isEarningsDateEstimate = false）。Q3'26 EPS 共識 0.51（earnings_dates）。
- **近期財報表現**：Q2'26 Adjusted EPS 0.46，對比共識 0.43，Surprise +6.5%；Q1'26 Adjusted EPS 0.40，對比 0.35，Surprise +14.0%；連續 5 季 EPS 超預期（2025-08 起）。
- **營運動能**：Q2'26 營收 YoY +5.8%；毛利率 28.3% 為近 5 季高點之一。
- **資本支出擴張**：Q2'26 capex 411M，為 2025 全年 722M 之 57%，需追蹤產能擴張與需求對應。
- **策略合作（info.longBusinessSummary）**：與 U.S. Department of Energy 之 Genesis Mission 合作（AI 與先進運算）；與 Xanadu Quantum Technologies 合作（量子製造）。這些合作之財務影響**DATA_UNAVAILABLE**。
- **管理層指引（guidance）**：工具未提供，**DATA_UNAVAILABLE**。
- **併購案**：2025 年 682M、Q2'26 440M，標的與整合進度 **DATA_UNAVAILABLE**。
- **派息**：最近一次發放日 2026-10-09，後續派息節奏未知。

## Metrics table

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| Revenue (TTM, USD M) | 6,938 | Q2'26 +5.8% | 估計 YoY 中單位數正成長（無工具來源） | 中性 |
| Revenue CAGR 2022-25 | -5.7% | 2025 +0.6% | 估計 3-5% 正成長（無工具來源） | 警示 |
| Gross Margin (TTM) | 約 27.7% | 2025 24.9%（2024 24.5%） | 估計 35-45%（無工具來源） | 偏弱 |
| Operating Margin (TTM) | 11.6% | 2025 11.7%（2024 10.8%） | 估計 15-20%（無工具來源） | 偏弱 |
| Net Margin (TTM, GAAP) | 10.3% | 2025 13.0%（含非經常性） | 估計 10-15%（無工具來源） | 中性 |
| ROE (TTM) | 約 6.1% | 2025 約 7.8% | 估計 12-15%（無工具來源） | 偏弱 |
| ROIC (本報告估算) | 約 4.9-5.3% | n/a | 估計 8-12%（無工具來源） | 偏弱 |
| FCF Margin (TTM) | 11.5% | 2025 14.9% | 估計 15-20%（無工具來源） | 中性 |
| FCF / NI (TTM) | 1.11 | 2025 1.14 | 健康門檻 >0.9 | 健康 |
| Capex / Revenue (TTM) | 16.1% | 2025 10.6% | 估計 8-12%（無工具來源） | 警示（擴張期） |
| Current Ratio | 2.48 | 2025-12 2.62 | 估計 1.5-2.5（無工具來源） | 健康 |
| Debt / Equity | 14.1% (0.14x) | 2025 14.3% | 估計 20-40%（無工具來源） | 健康 |
| Net Cash (USD M) | 約 679（info 口徑）/ 約 710（BS 現金+STI 口徑） | 2025-12 BS 口徑約 1,396（3,103-1,707） | n/a | 健康 |
| Total Debt (USD M) | 1,678 | 2025-12 1,707 | n/a | 健康（持續去槓桿） |
| Trailing P/E (GAAP) | 37.7x | n/a | 估計 30-35x（無工具來源） | 偏貴 |
| Forward P/E | 18.4x | n/a | 估計 25-30x（無工具來源） | 偏便宜 |
| EV/EBITDA | 13.0x | n/a | 估計 15-20x（無工具來源） | 中性偏便宜 |
| P/FCF (TTM) | 33.8x | n/a | 估計 25-30x（無工具來源） | 偏貴 |
| P/S | 3.9x | n/a | 估計 3-5x（無工具來源） | 中性 |
| P/B | 2.24x | n/a | 估計 3-4x（無工具來源） | 中性 |
| Dividend Yield | 1.0%（年化 0.48） | n/a | 估計 0.5-1.5%（無工具來源） | 中性 |
| Dividend Coverage (FCF/年派息) | 約 3.0x | n/a | n/a | 健康 |
| Insider 6mo 淨買賣 | 淨賣約 3.5M USD（0.013% 市值） | n/a | n/a | 中性（規模小、多為規律性賣出） |
| 機構 Mubadala 持股 | 72.8%（-5.55% QoQ） | n/a | n/a | 中性（大股東減持） |
| Short % Float | 13.6% | 空單 +9.2% MoM | 估計 3-8%（無工具來源） | 偏高 |
| Analyst 平均目標 vs 現價 | +54.8% | n/a | n/a | 正面（分析師一致偏多，但為共識非事實） |
| EPS Surprise（最近季） | +6.5%（Q2'26） | 連續超預期 | n/a | 正面 |
| Beta | 1.77 | n/a | 估計 1.2-1.5（無工具來源） | 高波動 |

## Red flags
- **營收停滯**：2022→2025 營收由 8,108M 降至 6,791M（-5.7% CAGR），2025 年僅 +0.6%；Q2'26 YoY +5.8% 僅為單季，尚未確認趨勢反轉。
- **獲利波動大**：2024 年 GAAP 淨虧損 -265M（impairment 935M）；2025 年 GAAP 淨利 885M 含非經常性項目，TTM 淨利率 10.3%，ROE 僅 6%-8%，ROIC 約 5%，資本報酬低於一般 WACC 常見水準（WACC 本報告未計算，為一般性判斷）。
- **Q2'26 現金快速下降**：Cash & Equivalents 由 1,849M 降至 1,087M（單季 -762M）；Cash+STI 由 3,071M 降至 2,388M（-683M）；FCF 單季轉為 -6M。
- **Q1'26 回購超過 FCF**：Q1'26 buyback 430M，同期 FCF 230M，回購資金來源需留意。
- **Capex 大幅回升**：Q2'26 Capex 411M，YoY +158%；TTM capex/revenue 16.1%，遠高於 2025 年 10.6%，短期 FCF 壓力增加。
- **Working capital 轉弱**：Working Capital 由 2025-09 4,239M 降至 2026-06 3,259M；Receivables 由 2026-03 1,279M 回升至 1,458M。
- **Net Debt 口徑不一致**：info totalCash 2,357M 與 BS 現金+STI 2,388M 接近，但 quarterly_bs 之 Net Debt 欄位為 35M，與上述淨現金約 679M-710M 口徑衝突，建議以 BS 原始欄位核對。
- **EBITDA 口徑不一致**：info ebitda 1,981M，而 quarterly_fin 最近四季 EBITDA 合計約 2,213M（reported）或較低之 normalized，口徑需統一。
- **股息資料不一致**：info dividendRate 0.48 與 trailingAnnualDividendRate 0.12 不一致；payoutRatio 0.0938 疑似以單季股利計算；cashflow 歷史無派息欄位無法驗證。
- **機構持股超過 100%**：major_holders 之 institutionsPercentHeld 100.2%、inst_holders 前幾名合計亦需以 13F 原始資料核對，本報告不採用此欄位。
- **大股東集中與低流通**：Mubadala 持股 72.8%，floatShares 僅 148.4M；且 Mubadala 持股在 2026-06-30 季報減少 5.55%，流通性與籌碼結構需留意。
- **股價弱勢與空單上升**：現價低於 200 日均線 -11.6%，較 52 週高點 -47.9%；空單 sharesShort 由 6.41M 增至 7.00M，short % float 13.6%；Beta 1.77。
- **資料缺漏**：segment mix、管理層 guidance、併購標的細節、Q1'25 季度損益（部分欄位缺漏）、2021 年度財務資料皆為 DATA_UNAVAILABLE 或 null。
- **快取資料**：本次 yfinance 即時 feed 不可用，部分欄位取自 repo cache（source: cache，cached_at 2026-10-11 12:38 UTC），fast_info 之 50/200 日均線、market_cap、year_high/low 為 null 或 NaN，已改用 info 欄位。
