# Fundamentals — 3324.TWO 雙鴻 (Auras Technology) as of 2026-11-18

資料基準：工具輸出日期為 2026-11-17（價格為 cnyes 快取，cached_at 2026-11-17 15:51 UTC）。最新財報為 2026-09-30 季（Q3'26，公告日 2026-11-11）。未發現晚於 2026-11-18 的資料。金額單位：TWD，以「億」表示（1 億 = 100,000,000 TWD），全文不混用 B。

## Executive summary
雙鴻 2025 年營收 232.76 億 TWD（YoY +47.5%），TTM 營收 346.36 億，成長動能強，但毛利率自 Q1'26 的 29.7% 連兩季下滑至 Q3'26 的 25.6%，且 TTM 自由現金流為負（約 -33.25 億，按季度加總），總負債自 2025 年底的 48.50 億急升至 108.70 億。估值方面，以 927 TWD 計算，trailing P/E 21.8x、EV/EBITDA 16.6x 並不便宜，forward P/E 11.1x 依賴一個口徑未明的 forwardEps (83.70)，需保留懷疑；Q3'26 EPS 11.07 相對分析師預估 14.81 低 25.25%，已連續四季低於預估。財務體質結論：成長與獲利仍在，但現金流與槓桿轉差，屬於「高成長、高資本支出、高負債擴張」的階段。

## Revenue & profitability
**營收趨勢（單位：億 TWD）**
- 年度：FY2022 138.57 → FY2023 127.13 → FY2024 157.79 → FY2025 232.76。FY2025 YoY +47.5%；FY2022-FY2025 三年 CAGR 約 18.9%（以 138.57 與 232.76 計算）。
- 季度：Q4'25 75.97、Q1'26 85.52、Q2'26 87.00、Q3'26 97.87。Q3'26 QoQ +12.5%；Q2'26 YoY +64.0%（對 Q2'25 53.06）。Q1'25 與 Q3'25 在工具輸出中為 null，無法計算 YoY。
- 產品結構：longBusinessSummary 僅列出產品線（AI-GPU/CPU/交換器伺服器散熱、筆電、PC/VGA、顯卡、主機板、智慧型手機/平板、電動車），未提供各產品線營收占比，分部營收 DATA_UNAVAILABLE。

**獲利能力（年度 / 季度）**

| 期間 | 毛利率 | 營業利益率 | 淨利率 |
|---|---|---|---|
| FY2022 | 19.6% | 8.5% | 9.1% |
| FY2023 | 23.6% | 10.8% | 9.7% |
| FY2024 | 25.5% | 12.1% | 12.0% |
| FY2025 | 27.4% | 14.0% | 11.1% |
| Q1'26 | 29.7% | 17.8% | 13.6% |
| Q2'26 | 28.4% | 16.0% | 11.1% |
| Q3'26 | 25.6% | 13.9% | 11.0% |
| TTM | 27.5% | 15.4% | 12.0%（info profitMargins 11.96%） |

- 年度趨勢為毛利與營益率擴張，但 2026 年兩季快速壓縮：毛利率由 29.7% 降至 25.6%（約 -400bp），營業利益率由 17.8% 降至 13.9%。淨利率靠非營業項目維持在 11% 附近。
- ROE（info）33.9%；ROA 11.2%。ROIC 為估算值：TTM EBIT 約 55.97 億 × (1 - 約 19% 稅率) ≈ 45.3 億 NOPAT，除以 Q3'26 invested capital 255.23 億，約 17.8%。
- 費用率：FY2025 R&D 14.10 億（6.1% 營收）、SG&A 17.02 億（7.3%）；Q3'26 R&D 5.17 億（5.3%）、SG&A 6.30 億（6.4%）。

## Cashflow & balance sheet
**現金流（單位：億 TWD）**

| 期間 | OCF | Capex | FCF | FCF margin | FCF/NI |
|---|---|---|---|---|---|
| FY2022 | 12.40 | 6.45 | 5.95 | 4.3% | n/a |
| FY2023 | 19.71 | 8.75 | 10.96 | 8.6% | 0.89 |
| FY2024 | 16.43 | 14.92 | 1.51 | 1.0% | 0.08 |
| FY2025 | -5.71 | 23.04 | -28.75 | -12.4% | 負值（NI 25.72） |
| Q1'26 | 6.09 | 8.81 | -2.72 | | |
| Q2'26 | -2.33 | 11.59 | -13.91 | | |
| Q3'26 | 4.92 | 10.69 | -5.77 | | |
| TTM（按季加總） | 3.67 | 36.92 | -33.25 | 約 -9.6% | 負值 |

- FCF/NI 遠低於 0.9 健康門檻；FY2023 之後僅 FY2023 達標。
- info 欄位 freeCashflow 為 -42.03 億、operatingCashflow 為 3.67 億；OCF 與季度加總一致，FCF 差異（-42.03 vs -33.25）推測為 Yahoo 口徑不同（如將其他投資項目納入），本報告以季度加總為準並註記差異。
- capex/D&A：FY2025 D&A 6.72 億，capex 為 3.4 倍，屬擴產期。TTM capex 占營收 10.7%。
- 現金流量表 FY2025 的 Net Income From Continuing Operations 為 32.77 億，與損益表 Net Income 25.72 億不一致，差額 7.05 億未說明，需向資料來源確認。

**資產負債表（Q3'26，2026-09-30；單位：億 TWD）**
- Total debt：108.70（YE2025 48.50，+124%；Q2'26 89.53；Q1'26 83.39）。其中 long-term debt 70.47、current debt 35.18。
- Cash & equivalents：52.26（cash + 短期投資 52.77）。
- Net debt：53.39（YE2025 32.60；Q2'26 40.59）。
- Total assets 381.89；total liabilities 226.31；股東權益 149.59（YE2025 110.85）。
- Current ratio 1.80（流動資產 276.87 / 流動負債 154.17）；quick ratio 1.15（info）。
- Debt/Equity：total debt / equity = 72.7%（info debtToEquity 68.0%，口徑差異）；net debt / equity = 35.7%。
- Net debt / TTM EBITDA：約 0.9x（info EBITDA 61.53 億；按季 EBITDA 加總為 65.31 億，則約 0.8x）。
- 營運資金：Inventory 88.65（YE2025 60.57，+46%）、Accounts receivable 123.32（YE2025 100.68，+22.5%）。以 Q3'26 營收推算 AR 週轉約 115 天（估算），應收與存貨同步墊高，營運資金占用加重。

**借款與融資活動**
- FY2025：借款發行 66.85 億、償還 39.23 億。
- 2026 年前三季：借款發行 152.43 億、償還 79.79 億，淨借款約 72.64 億。
- 解讀：淨借款主要用於 capex 與營運資金，現金並未同步累積，利息與再融資壓力上升（FY2025 利息費用 0.70 億，僅為年度數字，2026 季度利息 DATA_UNAVAILABLE）。

## Capital allocation & insider signal
**資本配置**
- Capex：FY2022 6.45 億 → FY2025 23.04 億（占營收 4.7% → 9.9%）；TTM 36.92 億（占 10.7%）。資本支出快速上升，為近年最主要現金流出。
- 股利：現金股利 FY2022 5.17 億、FY2023 5.77 億、FY2024 5.71 億、FY2025 9.03 億。info dividendRate 11.9 TWD/股、yield 1.16%、payout ratio 27.7%。以 11.9 × 93.66M 股推算年度股利約 11.15 億，TTM OCF 3.67 億 → 股利 OCF 覆蓋約 0.33x；FY2025 FCF 為負，股利未被自由現金流覆蓋，須靠舉債或現金支應。
- 買回：2022-2025 無買回（2021 年買回 4.93 億）；treasury shares 於 2026 年 Q2/Q3 歸零。
- 增資/股本：已發行股數 YE2025 92.32M → Q3'26 93.66M（+1.5%）；2024 增資收款 1.67 億、2025 1.55 億、2026 Q1 1.53 億。

**內部人與持股**
- insider（近 6 個月交易明細）工具回傳空陣列。由於 Yahoo cookie/crumb 取得失敗，空陣列無法確認為真實零交易或來源缺漏，交易淨買賣及占市值比 DATA_UNAVAILABLE。
- companyOfficers 清單中各主管 exercisedValue 與 unexercisedValue 皆為 0，無可參考的持股變動資訊。
- heldPercentInsiders 28.92%（高集中度，內部人持股比例高）；institutions 持股 11.61%，機構數 56（major_holders）。

## Valuation
價格基準：927 TWD（快取；前收 1030，當日 -10.0%；52W 高 1750、低 810）。市值 868.24 億 TWD（927 × 93.66M 股 = 868.24 億，已核對）。企業價值 EV 1,019.00 億（info）。

| 指標 | 數值 | 計算 / 來源 |
|---|---|---|
| Trailing P/E | 21.8x | 927 / trailingEps 42.47 |
| Forward P/E | 11.1x | 927 / forwardEps 83.70（口徑未明，見紅旗） |
| P/B | 5.8x（自算） | 927 / (Q3'26 股東權益 149.59 億 / 93.66M 股 = 159.7) ；info priceToBook 7.70 使用 bookValue 120.47，與 Q3'26 股東權益不一致 |
| P/S (TTM) | 2.5x | info priceToSalesTrailing12Months 2.51 |
| EV/Revenue | 2.9x | info enterpriseToRevenue 2.94 |
| EV/EBITDA | 16.6x | info enterpriseToEbitda 16.56 |
| P/FCF | n/a | TTM FCF 為負，不具意義 |
| Dividend yield | 1.16% | info |
| 產業中位數 | DATA_UNAVAILABLE | 工具未提供 |

- 分析師（16 位）：recommendationMean 1.71（偏買進）；目標價平均 1650.5、中位數 1800、最高 2180、最低 1025。平均目標相對 927 約 +78%。目標價為分析師估值，未必反映最新 EPS 下修。
- 技術面背景（ta snapshot，僅供參考）：RSI14 31.6；MACD 柱 -32.2；價格較 MA20 (1262.35) -26.6%、較 MA50 (1385.94) -33.1%、較 MA200 (1111.85) -16.6%；1 個月動能 -34.9%；距 52W 高點 -47.0%、距 52W 低點 +14.4%；ATR14 109.4。

**估值解讀**：以 trailing 盈餘看，21.8x P/E 與 16.6x EV/EBITDA 已反映高成長，但 Q3'26 單季 EPS 年增與季增皆轉弱。forward P/E 11.1x 僅在 forwardEps 83.70 成立，該數字需要 Q4'26 單季 EPS 約 50 TWD（83.70 - Q1 12.25 - Q2 10.41 - Q3 11.07 ≈ 49.97）才能達成，遠高於 Q3 實際 11.07，因此不應直接採信為 FY2026 盈餘。

## Key catalysts
- 最近財報：2026-11-11（earnings_dates）。Q3'26 EPS 11.07 vs 預估 14.81（-25.25%）；營收 97.87 億 QoQ +12.5%；毛利率再降至 25.6%。
- 財報surprise 紀錄：2025-11 +17.2%、2026-03 -15.6%、2026-05 -3.9%、2026-08 -22.7%、2026-11 -25.3%。近四季連續低於預估。
- 下一次財報日：DATA_UNAVAILABLE（工具輸出中最近一筆即為 2026-11-11）。依過去 Q4 公告時點（2026-03-03、2025-03-11）推測下一次約為 2027 年 3 月，屬推論，非工具資料。
- 近期指引（guidance）：DATA_UNAVAILABLE。
- 股利：最近除息日 2026-06-17（由 Unix timestamp 換算）；下次除息 DATA_UNAVAILABLE。
- 產品/客戶面：AI 伺服器散熱需求為營收成長主因（由 longBusinessSummary 產品描述推論，無分部營收數據佐證）；客戶集中度 DATA_UNAVAILABLE。

## Metrics table
（單位：營收、利潤、現金流、負債、市值以「億 TWD」表示；每股與比率為原始單位）

| Metric | Latest（2026-09-30 或 TTM） | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收（億 TWD，Q3'26） | 97.87 | Q2'26 YoY +64.0%；QoQ +12.5% | DATA_UNAVAILABLE | 強 |
| 營收（億 TWD，TTM） | 346.36 | FY25 YoY +47.5%；3Y CAGR 18.9% | DATA_UNAVAILABLE | 強 |
| 毛利率（Q3'26） | 25.6% | 2 季下滑約 -400bp（自 Q1'26 29.7%） | DATA_UNAVAILABLE | 轉弱 |
| 營業利益率（TTM） | 15.4% | FY25 14.0%，FY24 12.1% | DATA_UNAVAILABLE | 尚可，季度轉弱 |
| 淨利率（TTM） | 12.0% | FY25 11.1%，FY24 12.0% | DATA_UNAVAILABLE | 尚可 |
| ROE（info） | 33.9% | n/a | DATA_UNAVAILABLE | 高 |
| ROIC（估算） | 約 17.8% | n/a | DATA_UNAVAILABLE | 尚可 |
| FCF（億 TWD，TTM 按季加總） | -33.25 | FY25 -28.75 | DATA_UNAVAILABLE | 差 |
| FCF/NI（FY2025） | 負值 | FY24 0.08 | DATA_UNAVAILABLE（健康門檻 >0.9） | 差 |
| Capex 占營收（TTM） | 10.7% | FY25 9.9%，FY22 4.7% | DATA_UNAVAILABLE | 高，擴產中 |
| Total debt（億 TWD） | 108.70 | YE25 48.50（+124%） | DATA_UNAVAILABLE | 惡化 |
| Net debt（億 TWD） | 53.39 | YE25 32.60 | DATA_UNAVAILABLE | 惡化 |
| Current ratio | 1.80 | n/a | DATA_UNAVAILABLE | 尚可 |
| Debt/Equity（total debt / equity） | 72.7%（info 68.0%） | n/a | DATA_UNAVAILABLE | 偏高 |
| Net debt / EBITDA | 約 0.9x | n/a | DATA_UNAVAILABLE | 可控，但速度快 |
| 現金（億 TWD，cash & equivalents） | 52.26 | YE25 14.39 | DATA_UNAVAILABLE | 改善（借款推動） |
| 股利覆蓋（OCF / 股利，TTM） | 約 0.33x | FY25 FCF 為負 | DATA_UNAVAILABLE | 差 |
| 內部人交易（近 6 月） | DATA_UNAVAILABLE（工具回傳空陣列） | n/a | DATA_UNAVAILABLE | 無法判斷 |
| Trailing P/E | 21.8x | n/a | DATA_UNAVAILABLE | 中性偏貴 |
| Forward P/E | 11.1x（forwardEps 口徑未明） | n/a | DATA_UNAVAILABLE | 存疑 |
| P/B（Q3'26 自算） | 5.8x | n/a | DATA_UNAVAILABLE | 偏高 |
| P/S（TTM） | 2.5x | n/a | DATA_UNAVAILABLE | 中性 |
| EV/EBITDA（TTM，info） | 16.6x | n/a | DATA_UNAVAILABLE | 偏高 |
| 市值（億 TWD） | 868.24 | 52W 高點 1750 TWD 對 927 TWD 為 -47.0% | DATA_UNAVAILABLE | 股價大幅回檔 |
| 分析師平均目標價（TWD） | 1650.5 | 相對 927 約 +78% | n/a | 偏樂觀（可能落後） |

## Red flags
- 自由現金流轉負：FY2025 FCF -28.75 億、TTM 按季加總 -33.25 億，TTM OCF 僅 3.67 億，capex 36.92 億，成長高度依賴外部融資。
- 負債快速擴張：total debt 9 個月內由 48.50 億升至 108.70 億（+124%），current debt 35.18 億，短期再融資風險需追蹤。
- 毛利率與營業利益率連續兩季下滑（毛利 29.7% → 25.6%；營益 17.8% → 13.9%），與營收高速成長並存，須確認是否為價格壓力或產品組合轉換。
- EPS 連續四季低於預估，Q3'26 偏離 -25.25%。
- 營運資金惡化：inventory +46%、AR +22.5%（YTD），AR 週轉約 115 天（估算）。
- 股利未被現金流覆蓋：TTM OCF 對應股利覆蓋約 0.33x。
- 股價 1 日 -10.0%、1 個月 -34.9%，RSI14 31.6，接近跌停後的弱勢區；原因未由工具資料證實。
- forwardEps 83.70 與 Q1-Q3 實際 EPS 合計 33.73 差距過大，口徑需要確認，不宜直接用於估值。
- 資料一致性問題（需於下游引用時註記）：
  - FY2025 現金流量表 NI（32.77 億）與損益表 NI（25.72 億）不一致。
  - info EBITDA（61.53 億）與季度 EBITDA 加總（65.31 億）不一致。
  - info priceToBook（7.70）與 Q3'26 股東權益自算（5.8）不一致。
  - info freeCashflow（-42.03 億）與季度 FCF 加總（-33.25 億）不一致。
  - earnings_dates 的 EPS 與 quarterly_fin 的 diluted EPS 有 1-5% 差異（Q1'26 12.0 vs 12.25；Q2'26 9.98 vs 10.41）。
  - 2025 年 Q1、Q3 季度資料為 null，無法計算完整 2025 季度趨勢。
- 工具覆蓋缺口：insider 明細、下次財報日、指引、分部營收、產業中位數、利息費用（2026 季度）均為 DATA_UNAVAILABLE；Yahoo cookie/crumb 取得失敗，部分欄位取自快取。

FUNDAMENTALS REPORT COMPLETE
