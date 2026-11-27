# Fundamentals — IRM (Iron Mountain Inc.) as of 2026-11-28

資料說明：所有金額為 USD，依規定以 B（十億美元）/ M（百萬美元）表示，本報告不使用 億。資料來源為 yfinance 工具（info、financials、quarterly_fin、balance_sheet、quarterly_bs、cashflow、quarterly_cf、earnings_dates、insider、major_holders、inst_holders）。yfinance 的 cookie/crumb 取得失敗，工具已改用 repo cache，`fast_info` 的 source 為 cache（cached_at 2026-11-27 16:31 UTC）。最新季度為 FY2026 Q3（2026-09-30），最新財報發布日為 2026-11-05。本報告未引用任何歷史 daily 報告數字。資料日期皆不晚於 2026-11-28；下一次財報 2027-02-11 為排程日期，尚未發生。

## Executive summary

IRM 的營收維持雙位數成長（Q3 FY26 YoY +13.5%，TTM 營收 7.80B），但 GAAP 淨利率僅約 5.9%，TTM FCF 為 -0.63B（OCF 1.70B 扣除 capex 2.34B），股利 3.97 USD/股（殖利率 3.82%）實際由舉債支應。資產負債表槓桿偏高（Q3 FY26 Total Debt 20.16B、股東權益 -1.39B、current ratio 0.55），財務體質屬偏弱。估值方面 trailing P/E 68.0x、forward P/E 38.3x、EV/EBITDA 19.6x，相對一般 REIT 估計偏貴，但分析師平均目標價 138.73 USD 高於現價 104.11 USD，市場定價取決於對 REIT 營運指標（如 AFFO，本工具未提供）的認定。

## Revenue & profitability

**營收（USD，年度）**

| 年度 | Total Revenue | YoY | 毛利率 | 營業利益率（Total Operating Income As Reported） | 淨利率 |
|---|---|---|---|---|---|
| FY2022 | 5.10B | — | 57.1% | 20.6% | 10.9% |
| FY2023 | 5.48B | +7.4% | 57.0% | 16.8% | 3.4% |
| FY2024 | 6.15B | +12.2% | 56.2% | 16.4% | 2.9% |
| FY2025 | 6.90B | +12.2% | 55.4% | 16.9% | 2.1% |

- 3 年 CAGR（FY2022→FY2025）：約 10.6%。yfinance 未提供 FY2021 數據，無法計算 4-5 年 CAGR。
- 營收成長穩定，但毛利率連續下滑（57.1% → 55.4%），淨利率從 FY2022 的 10.9% 降至 FY2025 的 2.1%。FY2022 淨利含大額非經常性收益（Gain On Sale Of Security 61.7M、Gain On Sale Of PPE 93.3M 等），不宜作為基準。
- 特殊項目持續存在：Special Income Charges 在 FY2023-FY2025 分別為 -226.3M / -279.3M / -253.9M；Restructuring And Mergers Acquisition 為 239.1M / 267.4M / 229.3M，顯示「非經常性」費用已連續多年發生。

**季度趨勢（USD）**

| 季度 | Total Revenue | 毛利率 | Operating Income（yfinance 口徑） | Net Income | Diluted EPS |
|---|---|---|---|---|---|
| FY25 Q3（2025-09-30） | 1.75B | 54.9% | 364.7M | 84.3M | 0.28 |
| FY25 Q4（2025-12-31） | 1.84B | 55.4% | 404.7M | 89.3M | 0.30 |
| FY26 Q1（2026-03-31） | 1.94B | 54.0% | 405.7M | 143.7M | 0.48 |
| FY26 Q2（2026-06-30） | 2.03B | 52.8% | 386.7M | 101.4M | 0.34 |
| FY26 Q3（2026-09-30） | 1.99B | 53.5% | 423.4M | 124.1M | 0.41 |

- Q3 FY26 YoY 營收 +13.5%（1.99B vs 1.75B），與 info.revenueGrowth 0.135 一致。
- 毛利率自 FY25 Q3 的 54.9% 小幅波動至 FY26 Q2 的 52.8%，Q3 回升至 53.5%；SG&A 在 Q2 FY26 升至 402.3M（Q3 降至 348.8M）。
- TTM（FY25 Q4 至 FY26 Q3）：營收 7.80B、毛利率 53.9%、營業利益率 19.5%（Total Operating Income As Reported）或 20.8%（yfinance Operating Income 口徑，與 info.operatingMargins 0.2078 一致）、淨利 458.5M、淨利率 5.9%（與 info.profitMargins 0.0588 一致）、TTM Diluted EPS 1.53。
- 盈利品質：FY26 Q1 淨利 143.7M 含大額有利的 Gain On Sale Of Security 24.5M 與 Tax Rate 15.4%，Q2 稅率僅 12.2%，Q3 稅率回升至 30.6%。稅率波動大，單季 EPS 不宜外推。

**ROE / ROIC**

- ROE：n/m。股東權益為負（FY25 -981.0M，Q3 FY26 -1,388.2M），yfinance 未提供 returnOnEquity。
- ROA：4.7%（info.returnOnAssets 0.04716）。
- ROIC（估計）：FY2025 NOPAT ≈ 1,163.8M × (1 - 27.9%) ≈ 839.0M，平均 Invested Capital ≈ 14.33B，ROIC ≈ 5.9%。此為估算值，非工具直接提供。

**Segment mix**

- DATA_UNAVAILABLE：info.longBusinessSummary 僅描述業務範疇（資訊管理、數位轉型、資料中心、資產生命週期管理等），未提供分部營收或分部獲利。yfinance 亦無分部資料。

## Cashflow & balance sheet

**現金流（USD）**

| 指標 | FY2022 | FY2023 | FY2024 | FY2025 | TTM（FY25Q4-FY26Q3） |
|---|---|---|---|---|---|
| Operating Cash Flow | 0.93B | 1.11B | 1.20B | 1.34B | 1.70B |
| Capex | -0.88B | -1.35B | -1.85B | -2.35B | -2.34B |
| Free Cash Flow（OCF - Capex） | +0.04B | -0.23B | -0.66B | -1.01B | -0.63B |
| FCF margin | +0.9% | -4.2% | -10.7% | -14.6% | -8.1% |
| Cash Dividends Paid | -0.72B | -0.74B | -0.79B | -0.92B | — |

- FCF / NI：FY2025 為 -6.97x（FCF 為負，比率無參考意義）；TTM 同為負。健康標準 >0.9 不成立。
- OCF / NI：FY2025 為 9.3x，反映折舊攤提（FY25 D&A 1.06B）佔淨利比重極高，GAAP 淨利低估現金產出，但 capex 吃掉大部分 OCF。
- 註：yfinance info.freeCashflow 為 -451.7M，與由季度資料加總的 TTM FCF -632.3M 不一致，本報告採季度加總值，差異未解。

**資產負債表（USD）**

| 指標 | FY2024（12-31） | FY2025（12-31） | Q3 FY26（09-30） |
|---|---|---|---|
| Total Assets | 18.72B | 21.13B | 22.32B |
| Total Debt | 16.37B | 19.05B | 20.16B |
| Cash & Equivalents | 0.16B | 0.16B | 0.19B |
| Net Debt（yfinance） | 13.56B | 16.27B | 17.78B |
| Stockholders Equity | -0.50B | -0.98B | -1.39B |
| Current Assets | 1.69B | 1.93B | 2.10B |
| Current Liabilities | 3.09B | 2.62B | 3.79B |
| Goodwill | 5.08B | 5.29B | — |

- Current ratio：0.555（Q3 FY26 = 2.10B / 3.79B，與 info.currentRatio 一致）；quick ratio 0.448。流動負債大於流動資產，短期償債能力偏弱，依賴再融資。
- Debt / Equity：n/m（股東權益為負）。
- Net debt / EBITDA：約 6.6x（以 yfinance Net Debt 17.78B / TTM Normalized EBITDA 2.71B 計算）或約 7.4x（以 Total Debt 減 cash 19.97B 計算）。yfinance 的 Net Debt 與 Total Debt − Cash 差約 2.19B，口徑不明，未能釐清。
- 利息保障倍數：TTM Total Operating Income As Reported 1.52B / TTM Interest Expense 0.90B ≈ 1.7x（偏低）。
- 債務結構：FY2025 Issuance of Debt 18.40B、Repayment of Debt 16.02B，持續以新債償還舊債（滾動再融資）。Long Term Debt FY25 16.22B，Current Debt 0.22B。
- 有形帳面價值：FY25 Tangible Book Value -7.54B。Book value per share -4.66 USD，P/B 為負值（n/m）。
- 現金部位：Q3 FY26 cash 188.2M，相對 20.16B 債務極低。

## Capital allocation & insider signal

**資本配置**

- Capex：FY2025 2.35B，佔營收 34.0%，較 FY2024（30.1%）與 FY2022（17.3%）持續上升。Capex 擴張（資料中心等）是 FCF 為負的主因。
- 股利：Dividend rate 3.97 USD/年，殖利率 3.82%。FY2025 現金股利 0.92B，超過當年 FCF（-1.01B 為負）；以 OCF 計算的股利覆蓋倍數 FY2025 為 1.85x，但 OCF 尚需支應 capex，實際覆蓋不足。payoutRatio（info）2.26，以 GAAP EPS 計算的股利支付率超過 100%。
- 股票回購：yfinance cashflow 未列 Repurchase of Capital Stock，DATA_UNAVAILABLE。股本由 FY2022 290.8M 股增至 Q3 FY26 297.8M 股，為淨增發（含員工股權）。Stock Based Compensation FY2025 140.3M。
- 派息日期：yfinance 列示 lastDividendDate 對應 2026-09-15，exDividendDate 對應 2026-12-15（推算自 Unix 時間戳，屬排程資料，未經公司公告確認）。

**內部人交易（過去 6 個月：2026-05-28 至 2026-11-28）**

| 項目 | 數值 |
|---|---|
| 賣出筆數 | 14 筆 |
| 賣出股數 | 281,683 股 |
| 賣出金額 | 33.19M USD |
| 賣出金額佔市值比 | 約 0.11%（市值 31.01B USD） |
| 主要賣出人 | CEO William L. Meaney 230,844 股 / 27.02M USD；Greg W. McIntosh 26,839 股 / 3.22M USD；Mark Kidd 24,000 股 / 2.94M USD |
| 買進 | 過去 6 個月無買進紀錄；全期間僅 1 筆 33 股（約 2,954 USD） |

- Meaney 於 2026-06 至 2026-11 每月固定賣出 38,474 股，同步出現 37.00 USD 選擇權行權（Conversion of Exercise of derivative security）紀錄，屬「行權後賣出」模式。yfinance 未標示是否為 10b5-1 計畫，無法確認。
- 董事於 2026-05-07 獲得 1,892 股 stock award；2026-11-12 Walter Rakowich 有 5,000 股 stock gift（無金額）。
- 內部人淨賣出金額 33.19M USD，相對市值 31.0B USD 占比極小（約 0.11%），信號強度低；但持續性的 CEO 月度賣出仍值得注意。
- 內部人持股比例 0.88%（heldPercentInsiders），內部人持股比例偏低。

**機構持股**

- 機構持股 87.9%（1,593 家機構）。前十大包括 BlackRock 10.91%（32.49M 股，季度變動 -3.2%）、Vanguard PM 8.59%、Vanguard CM 6.38%、State Street 5.73%、Cohen & Steers 3.81%（季度變動 -5.5%）、Geode 2.98%、Wellington 1.85%（季度變動 +9.76，即大幅加碼）、FMR 1.77%。
- 機構持股高、集中於指數型基金，主要為被動配置。

## Valuation

**價格與技術位置（yfinance）**

- 現價：104.11 USD（info.currentPrice）；fast_info.last_price 為 103.61 USD（cnyes cache），兩者差 0.5%，以 info 為準。
- 50 日均線 112.56 USD（現價低於 7.5%）；200 日均線 116.82 USD（現價低於 10.9%）。
- 52 週區間：77.77 - 134.68 USD，現價位於區間中段偏低（約 46% 位置）。
- Beta：1.20。

**估值倍數（yfinance，TTM / 預估）**

| 指標 | 數值 | 計算驗證 |
|---|---|---|
| 市值 | 31.01B USD | 297.83M 股 × 104.11 ≈ 31.00B |
| 企業價值（EV） | 51.68B USD | info.enterpriseValue |
| Trailing P/E | 68.0x | 104.11 / TTM EPS 1.53 |
| Forward P/E | 38.3x | 104.11 / forwardEps 2.716 |
| EV / EBITDA | 19.6x | info.enterpriseToEbitda；TTM EBITDA 2.64B |
| EV / Revenue | 6.63x | info.enterpriseToRevenue |
| P / S（trailing） | 3.98x | info.priceToSalesTrailing12Months |
| P / FCF | n/m | TTM FCF 為負 |
| P / B | n/m | 股東權益為負 |

- Forward EPS 2.716 與 TTM GAAP EPS 1.53 差距大，可能為 AFFO 或其他正常化口徑，yfinance 未說明來源；Forward P/E 的可比性需保留。
- 分析師：11 家，建議 buy（recommendationKey buy），目標價平均 138.73 USD、最高 155.00、最低 124.00 USD。
- 估計 sector median（Real Estate / REIT-Specialty，非工具資料，僅供參考）：Trailing P/E 約 35x（REIT GAAP 盈餘受折舊影響，不具可比性）；EV/EBITDA 約 18x；P/S 約 6x；股利殖利率約 4%。IRM 的 EV/EBITDA 與 P/S 略高於估計中位數，trailing P/E 明顯偏高。

**盈餘預期與財報品質**

- 近 8 季 EPS 相對預估：6 季超預期、2 季低於預期。最近一季（2026-11-05）EPS 0.64 vs 預估 0.61，超預期 +4.6%；前一季（2026-08-05）0.60 vs 0.56，+7.5%；FY26 Q1（2026-04-30）0.60 vs 0.52，+15.8%。
- 下一季財報（2027-02-11）EPS 預估 0.69 USD（yfinance）。

## Key catalysts

1. **下次財報 2027-02-11**：EPS 預估 0.69 USD。需關注 TTM 營收能否延續 10% 以上成長、毛利率能否回升至 54% 以上、FCF 是否改善（資本支出高峰期）。
2. **資本支出與 FCF 轉正時點**：FY2025 capex 2.35B，TTM FCF -0.63B。若 capex 增速放緩，FCF 有機會轉正，但目前缺乏公司指引數據，DATA_UNAVAILABLE。
3. **再融資與利率**：利息費用 TTM 0.90B，債務 20.16B 持續滾動；利率環境與信用評等（yfinance 未提供）為重要變數。
4. **股利可持續性**：年化股利 3.97 USD，FCF 為負，市場會關注是否調整股利或以新債支應。
5. **分析師目標價（平均 138.73 USD）**：較現價上行約 33%，但目標價隱含的 AFFO 基礎本工具未提供。
6. **內部人持續月度賣出（CEO）**：後續是否延續，為市場情緒指標。
7. **分部與營運指標**：DATA_UNAVAILABLE（分部營收、資料中心 MW、儲存量、AFFO、guidance 等皆未由工具提供）。

## Metrics table

單位：USD（B = 十億，M = 百萬）；Sector median 為估計值，非工具資料。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| Total Revenue（TTM，B USD） | 7.80 | +13.5%（Q3 FY26 vs Q3 FY25） | — | 成長強 |
| Total Revenue（FY2025，B USD） | 6.90 | +12.2% | — | 成長強 |
| Revenue CAGR（FY22-25） | 10.6% | — | 約 5-8%（估計） | 優於估計 |
| Gross Margin（TTM） | 53.9% | 下滑（FY25 55.4%） | 約 55%（估計） | 略低、下滑中 |
| Operating Margin（TTM，reported 口徑） | 19.5% | — | 約 20-25%（估計） | 偏低 |
| Net Margin（TTM） | 5.9% | 高於 FY25 2.1% | 約 15%（估計） | 偏弱 |
| ROE | n/m（股東權益為負） | — | 約 8-10%（估計） | 無法評估 |
| ROIC（FY25 估算） | 約 5.9% | — | 約 6-7%（估計） | 略低 |
| FCF（TTM，B USD） | -0.63 | — | — | 負值，警訊 |
| FCF margin（TTM） | -8.1% | 惡化（FY25 -14.6%，FY24 -10.7%，此為 FY 數字） | 約 5-10%（估計） | 差 |
| FCF / NI | 負（n/m） | — | 約 0.9 以上為健康 | 不健康 |
| OCF（TTM，B USD） | 1.70 | — | — | 正值 |
| Capex / Revenue（FY25） | 34.0% | 上升（FY24 30.1%） | 約 20-30%（估計） | 偏高 |
| Total Debt（Q3 FY26，B USD） | 20.16 | 較 FY24 +23% | — | 偏高 |
| Net Debt（yfinance，B USD） | 17.78 | 較 FY24 +31% | — | 偏高 |
| Net Debt / EBITDA（TTM） | 約 6.6x（yfinance 口徑）至 7.4x | — | 約 5-6x（估計） | 偏高 |
| Interest Coverage（TTM） | 約 1.7x | — | 約 3x（估計） | 偏低 |
| Current Ratio | 0.55 | — | 約 1.0x（估計） | 偏弱 |
| Debt / Equity | n/m（股東權益 -1.39B） | — | 約 1.0-1.5x（估計） | 無法評估，股東權益為負 |
| Cash（Q3 FY26，M USD） | 188.2 | — | — | 極低 |
| Diluted EPS（TTM，USD） | 1.53 | FY25 0.49，FY24 0.61 | — | 波動大 |
| Trailing P/E | 68.0x | — | 約 35x（估計，不具可比性） | 偏貴 |
| Forward P/E | 38.3x | — | 約 20x（估計） | 偏貴 |
| EV / EBITDA | 19.6x | — | 約 18x（估計） | 略貴 |
| P / S（trailing） | 3.98x | — | 約 6x（估計） | 不貴 |
| P / FCF | n/m（FCF 為負） | — | 約 20x（估計） | 無法評估 |
| 股利殖利率 | 3.82% | — | 約 4%（估計） | 中性 |
| 股利支付率（GAAP EPS） | 226%（info.payoutRatio 2.26） | — | 約 70-90%（估計） | 不可持續（以 GAAP 計） |
| 股利 / OCF 覆蓋（FY25） | 1.85x（OCF 口徑） | — | — | 扣除 capex 後不足 |
| 內部人 6 個月淨賣出（M USD） | 33.19（占市值約 0.11%） | — | — | 信號弱，持續 CEO 賣出 |
| 機構持股比例 | 87.9% | — | 約 85-95%（估計） | 中性 |
| Beta | 1.20 | — | 約 1.0（估計） | 高於市場 |
| 股價 vs 200 日均線 | -10.9% | — | — | 技術面偏弱 |
| 分析師目標價（平均） | 138.73 USD（上行約 33%） | — | — | 市場共識正向 |

## Red flags

- FCF 連續多年為負（FY23 -0.23B、FY24 -0.66B、FY25 -1.01B、TTM -0.63B），靠舉債支應股利與資本支出。
- 股利支出超過 FCF：FY25 現金股利 0.92B，同年 FCF -1.01B；GAAP 股利支付率 226%。
- 槓桿持續上升：Total Debt FY24 16.37B → FY25 19.05B → Q3 FY26 20.16B；Net Debt 由 13.56B 升至 17.78B。
- 股東權益為負並持續擴大（FY24 -0.50B → FY25 -0.98B → Q3 FY26 -1.39B），Tangible Book Value FY25 -7.54B。
- Current ratio 0.55，流動負債大於流動資產；利息保障倍數約 1.7x。
- GAAP 淨利率由 FY22 10.9% 降至 FY25 2.1%，毛利率連續下滑；特殊項目與重組費用連續多年發生。
- Trailing P/E 68x、EV/EBITDA 19.6x，估值相對一般 REIT 偏高；股價低於 50 日與 200 日均線。
- CEO 自 2026 年 6 月起每月固定賣出並行權，累計 6 個月賣出 27.0M USD（yfinance 未確認是否為 10b5-1 計畫）。
- 資料缺口：AFFO / FFO、分部資料、公司財測（guidance）、評等機構評級、回購資料均為 DATA_UNAVAILABLE；yfinance 內部口徑不一致（Net Debt、FCF、Forward EPS）未能完全調和。

FUNDAMENTALS REPORT COMPLETE
