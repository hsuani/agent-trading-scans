# Fundamentals — IBM as of 2026-10-23

## Executive summary
IBM 財務體質屬「獲利與現金流穩健、但槓桿與流動性承壓」的狀態：FY2025 FCF 為 11.46B USD、FCF/NI 為 1.08（高於 0.9 健康門檻），但 2026-06-30 淨負債已升至 54.8B USD、現金由年初 14.4B 降至 8.1B，流動比率 0.79。營收成長極低（FY2022–FY2025 3 年 CAGR 3.7%，Q2 2026 YoY 僅 +1.1%），Q2 2026 營業利益率由去年同期 18.2% 收縮至 16.6%。估值方面，以 price 252.11 計，forward P/E 19.0x、trailing adjusted P/E 約 20.5x、EV/EBITDA（TTM）約 16.8x，相對低成長屬中性偏貴，分析師平均目標價 257.22 USD 僅較現價高約 2%。

## Revenue & profitability

**營收與成長（USD B）**
- FY2022 60.53 → FY2023 61.86 → FY2024 62.75 → FY2025 67.54。
- FY2025 YoY +7.6%（FY2024 僅 +1.4%）；FY2022–FY2025 3 年 CAGR 3.7%；FY2023–FY2025 2 年 CAGR 4.5%。FY2021 資料為 null，無法計算 4–5 年 CAGR。
- 最近四季（Q3 2025–Q2 2026，quarterly 加總）營收 TTM 為 69.10B。info 欄位的 totalRevenue 為 69.87B，兩者差約 0.77B，未能釐清來源，本報告以 quarterly 加總為準。
- Q2 2026 營收 17.16B，YoY +1.1%（Q2 2025 為 16.98B）。
- 業務結構：info 之 longBusinessSummary 列出 Software、Consulting、Infrastructure、Financing 四大分部。分部營收與利潤數據在本次工具輸出中無法取得，分部營收占比：DATA_UNAVAILABLE。
- 2025 年 purchase of business 達 8.30B（2024 為 3.29B），FY2025 營收成長中有多少來自併購、有多少為有機成長，工具資料無法拆分：DATA_UNAVAILABLE。

**獲利能力（以 annual income statement 計算）**
- 毛利率：FY2022 54.0% → FY2023 55.5% → FY2024 56.7% → FY2025 58.2%，逐年改善，FY2025 較 FY2024 +1.5 個百分點。Q2 2026 毛利率 57.7%，低於 Q2 2025 的 58.8%。
- 營業利益率（Operating Income / Revenue）：FY2022 13.5% → FY2023 15.2% → FY2024 16.1% → FY2025 18.5%。Q2 2026 為 16.6%（Q2 2025 為 18.2%），季度趨勢轉弱。
- 營業利益：FY2025 12.49B（FY2024 為 10.07B）；Q2 2026 為 2.85B，YoY -7.8%（Q2 2025 為 3.09B）。
- 淨利率：FY2025 15.7%（FY2024 為 9.6%）。但 FY2025 淨利含 Q4 2025 大額稅務利益（Q4 tax provision -1.44B，Q4 稅前利潤僅 4.14B、淨利 5.60B），GAAP 獲利品質需打折看待。
- TTM 淨利（quarterly 加總）為 10.73B；Q2 2026 淨利 2.17B，YoY -1.3%。
- ROE：info 欄位 34.8%；以 TTM 淨利 / 平均權益（6/30/2026 34.45B 與 6/30/2025 27.51B）估算約 34.6%，與 info 一致。
- ROIC（估計）：以 FY2025 EBIT 12.26B × (1 - 25.57% 稅率) ≈ 9.13B 作為 NOPAT，除以平均 invested capital（FY2024 82.28B、FY2025 93.91B，平均 88.09B）約 10.4%。此為粗估，非工具直接提供。
- EPS 雙口徑需注意：
  - GAAP diluted EPS：FY2025 11.17（FY2024 為 6.43，+74%，主要受稅務利益與低基期影響）。
  - Adjusted EPS（earnings_dates 之 Reported EPS）：FY2025 合計 11.57（Q1 1.60 / Q2 2.80 / Q3 2.65 / Q4 4.52）；2026 年 Q1 1.91、Q2 2.93、Q3 2.95，分別 YoY +19.4%、+4.6%、+11.3%。
  - 調整後 EPS 成長（約 +5–19%）顯著高於營收成長（約 +1%）與 GAAP 營業利益衰退（Q2 YoY -7.8%），兩者落差來源（調整項目定義、股數、稅率、利息）工具無法驗證，列為需追查項目。

## Cashflow & balance sheet

**現金流量（USD B）**

| 期間 | 營運現金流 OCF | 資本支出 Capex | FCF | FCF/NI | FCF margin |
|---|---|---|---|---|---|
| FY2022 | 10.44 | 1.97 | 8.46 | 5.2x（NI 低基期） | 14.0% |
| FY2023 | 13.93 | 1.81 | 12.12 | 1.62x | 19.6% |
| FY2024 | 13.45 | 1.69 | 11.76 | 1.95x | 18.7% |
| FY2025 | 13.19 | 1.74 | 11.46 | 1.08x | 17.0% |
| TTM（Q3’25–Q2’26） | 14.89 | 1.74 | 13.14 | 1.23x（TTM NI 10.73） | 19.0% |

- FCF 從 FY2023 12.12 連續二年下滑至 FY2025 11.46（-5.5%），趨勢略為走弱；但 TTM FCF 13.14 高於 FY2025，且 H1 2026 季度 FCF 合計 6.99B（Q1 4.78、Q2 2.21）。
- FCF/NI 2025 為 1.08，高於 0.9 健康門檻；但 2025 NI 含稅務利益，若剔除，比值會更高，表示現金轉換並非問題。
- info 欄位的 freeCashflow 為 12.24B、operatingCashflow 為 15.83B，與 cashflow 年報及 quarterly 加總不一致，本報告以 cashflow 報表為準。

**資產負債（USD B）**

| 項目 | 2024-12-31 | 2025-12-31 | 2026-06-30 |
|---|---|---|---|
| Total Debt | 58.40 | 64.61 | 65.27 |
| Cash & ST Investments | 14.59 | 14.42 | 8.13 |
| Net Debt | 41.03 | 47.67 | 54.82 |
| Stockholders' Equity | 27.31 | 32.65 | 34.45 |
| Current Assets | 34.48 | 36.94 | 28.40 |
| Current Liabilities | 33.14 | 38.66 | 35.91 |
| Goodwill | 60.71 | 67.72 | DATA_UNAVAILABLE |

- 淨負債：自 FY2024 41.03B 升至 2026-06-30 54.82B，半年內增加約 7.1B（+15%）。TTM EBITDA（quarterly 加總）17.57B，Net debt / TTM EBITDA 約 3.1x。
- 負債權益比（Total Debt / Equity）：2026-06-30 為 189%（info 欄位為 185.4）。
- 利息保障：TTM EBIT 12.37B / TTM 利息支出 1.93B ≈ 6.4x，仍屬可控。
- 流動性：流動比率 2026-06-30 為 0.79（2025-12-31 為 0.96），info 欄位為 0.855（日期不明）；營運資金 -7.51B。現金及短期投資 6 個月內由 14.42B 降至 8.13B（-44%）。
- 有形淨值為負：Tangible Book Value -46.46B（2025-12-31），商譽 67.72B 為主要原因，權益主要靠商譽與無形資產支撐。
- 退休金相關負債 Employee Benefits 10.84B（2025-12-31）。

## Capital allocation & insider signal

**資本配置（USD B，FY2025 對比 FY2024）**
- 資本支出：1.74（FY2024 為 1.69，+3.1%）；占營收 2.6%，折舊攤提 5.02，capex/D&A 約 0.35x，屬輕資產模式。
- 股利：現金股利 6.26（FY2024 為 6.15，+1.8%）；季股利 1.69，年化 6.76，殖利率 2.68%。
  - 股利覆蓋：FY2025 FCF / 股利 = 1.83x；TTM 為 13.14 / 6.31 ≈ 2.08x。
  - info 之 payoutRatio 0.575（以 earnings 計）。
  - exDividendDate 依 info 欄位推算約為 2026-11-10。
- 買回與稀釋：FY2025 股票買回 1.02（FY2024 為 0.65，+56%），但同年股票發行（含員工股權）0.71，淨買回 -0.31；diluted average shares 由 937.2M（FY2024）升至 948.7M（FY2025），+1.2%；Q2 2026 diluted shares 953.3M，YoY +0.6%。整體而言，買回未能抵銷股權稀釋。
- 併購：FY2025 purchase of business 8.30B，佔 FY2025 FCF 約 72%；並搭配 debt issuance 8.39B、repayment 5.49B。併購是 2025–2026 年淨負債上升的主要驅動，需追蹤併購標的之營收貢獻與整合成效（標的名稱與金額細節：DATA_UNAVAILABLE）。

**內部人交易（insider，近 6 個月：2026-04-23 至 2026-10-23）**
- 公開市場賣出：1 筆。THOMAS ROBERT DAVID（Senior VP，officer）於 2026-08-26 賣出 25,000 股，成交價 230.32 USD，金額約 5.76M USD。
- 公開市場買入：0 筆。
- 其他交易：ROBINSON ANNE 於 2026-07-01 有 7,295 股變動（value 欄位為 null，性質無法判定，可能為既有獎勵歸屬或稅務扣繳，DATA_UNAVAILABLE）；FEHRING NICOLAS A. 於 2026-06-04 贈與 400 股（非交易性）。
- 淨額：近 6 個月淨賣出約 5.76M USD（僅公開市場口徑），占市值 237.5B 約 0.002%，規模極小，不構成強烈訊號。
- 前期參考：2026-01-30 董事 FARR DAVID N 買入 1,000 股（304.00 USD，約 304K USD）；2026-02-25 董事 MIEBACH MICHAEL 買入 434 股（233.33 USD，約 101K USD）、HOWARD MICHELLE J. 買入 50 股（237.83 USD，約 11.9K USD）。上述買入均在近 6 個月窗口之前，且 FARR 買價高於現價。
- 內部人持股僅 0.105%（heldPercentInsiders 0.00105），機構持股 66.5%（4,394 家機構）。

**空方部位**
- sharesShort 24.16M（較前月 22.02M 增加 9.8%），占流通股 2.84%，days to cover 約 4.4 日。空方壓力溫和。

## Valuation

以 price 252.11 USD（fast_info cache 2026-10-23 11:26 UTC，info 欄位 marketState 為 PRE，屬盤前數據，非當日收盤）計算：

- 市值：237.52B USD（252.11 × 942.1M 流通股數，驗算一致）。
- 企業價值 EV：294.84B USD（市值 + 總債務 65.27 − 現金 8.13 ≈ 294.66，約一致）。
- P/E：
  - trailing（info trailingEps 11.72）= 21.5x。
  - trailing（GAAP TTM diluted EPS 11.27，quarterly 加總）= 22.4x。
  - trailing（adjusted TTM EPS 12.31，earnings_dates 加總）= 20.5x。
  - forward（info forwardEps 13.23）= 19.0x；以 FY2026 adjusted EPS 估計值 12.42（1.91 + 2.93 + 2.95 + Q4 估計 4.63 之合計，與 info epsCurrentYear 一致）計算 = 20.3x。
  - PEG（info）= 2.38，偏高。
- EV/EBITDA：info 為 18.3x（ebitda 16.14B）；以 quarterly TTM EBITDA 17.57B 計算約 16.8x。
- EV/Revenue：info 4.22x。
- P/S：info 3.40x；以 TTM 營收 69.10B 計算約 3.44x。
- P/FCF：以 TTM FCF 13.14B 計算約 18.1x（FCF yield 約 5.5%）。
- P/B：info 6.70x；以 2026-06-30 權益 34.45B 計算約 6.9x。
- 分析師共識（23 位）：recommendationMean 2.28（buy）；平均目標價 257.22 USD（+2.0%）、中位數 260 USD（+3.1%）、區間 174–300 USD。
- 股價位置：52 週高 332.46 / 低 199.19，現價距高點 -24.2%、距低點 +26.6%；52 週漲跌 -11.5%，同期 S&P 500 為 +13.7%；現價高於 50 日均線 232.71 與 200 日均線 250.67。
- 相對估值（sector median，估計）：IT Services 同業之 trailing P/E 約 20–25x、EV/EBITDA 約 13–17x、P/S 約 2–3x、P/FCF 約 18–25x，為本報告依一般市場認知之粗估，非工具資料，僅供參考。IBM 在 P/E 與 P/FCF 上接近同業中位，EV/EBITDA 與 P/B 偏高，但考量其槓桿與低成長，估值不具明顯折價。

## Key catalysts
- 最近財報：2026-10-21 公布 Q3 2026，adjusted EPS 2.95 USD，高於一致預期 2.87（+2.7%）。Q3 營收、分部表現與管理層指引文字：DATA_UNAVAILABLE（工具未提供新季度損益表，見 Red flags 之資料落後說明）。
- 下次財報：2027-01-27（info 與 earnings_dates 皆列出，屬估計日期），Q4 2026 adjusted EPS 一致預期 4.63 USD。
- 過去 13 季 EPS 表現：12 季超過或符合預期（2023-10 至 2026-10，僅 2026-07 為持平），季度超額幅度多在 +2% 至 +12% 之間。
- 股利：除息日約 2026-11-10（依 info 欄位推算），季股利 1.69 USD。
- 策略面：info 摘要提及與 Arm Holdings 合作開發 dual-architecture 硬體、與 Adobe、AWS、Microsoft、Oracle、Salesforce、SAP 等之合作，以及 UK Ministry of Defence 之 Team ORION 合約。這些對營收之具體貢獻：DATA_UNAVAILABLE。
- 併購整合：2025 年大額收購之整合進度與營收貢獻，為下季追蹤重點。

## Metrics table
(金額單位 USD B；比率為 %；EPS 為 USD/股)

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| Revenue（FY2025, USD B） | 67.54 | +7.6% | 約 +3–6%（估計） | 中性 |
| Revenue TTM（quarterly 加總, USD B） | 69.10 | info 4.7% | n/a | 中性偏弱 |
| Revenue 3Y CAGR（FY22–25） | 3.7% | — | 約 4–5%（估計） | 偏弱 |
| Q2 2026 Revenue（USD B） | 17.16 | +1.1% | n/a | 偏弱 |
| Gross margin（FY2025） | 58.2% | +1.5pp | 約 35–45%（估計） | 優（同業之上） |
| Operating margin（FY2025） | 18.5% | +2.4pp | 約 12–16%（估計） | 良 |
| Operating margin（Q2 2026） | 16.6% | -1.6pp | n/a | 需關注 |
| Net margin（FY2025，含稅務利益） | 15.7% | +6.1pp | 約 8–12%（估計） | 良（品質需打折） |
| ROE（TTM 估算） | 34.6%（info 34.8%） | — | 約 15–20%（估計） | 優 |
| ROIC（粗估） | 約 10.4% | — | 約 8–12%（估計） | 中性 |
| OCF（FY2025, USD B） | 13.19 | -1.9% | n/a | 良 |
| FCF（FY2025, USD B） | 11.46 | -2.6% | n/a | 中性 |
| FCF margin（FY2025） | 17.0% | -1.7pp | 約 10–15%（估計） | 良 |
| FCF / NI（FY2025） | 1.08x | — | 約 0.9–1.1x（估計） | 健康（>0.9） |
| Net debt（2026-06-30, USD B） | 54.82 | +15% vs 2025-12-31 | n/a | 紅旗 |
| Net debt / TTM EBITDA | 約 3.1x | — | 約 2–3x（估計） | 偏高 |
| Total debt / Equity | 189% | — | 約 50–100%（估計） | 偏高 |
| Current ratio（2026-06-30） | 0.79 | 較 0.96 下降 | 約 1.0–1.5（估計） | 紅旗 |
| Cash & ST inv.（2026-06-30, USD B） | 8.13 | -44% vs 2025-12-31 | n/a | 紅旗 |
| Interest coverage（TTM EBIT / 利息） | 約 6.4x | — | n/a | 可接受 |
| Capex / Revenue（FY2025） | 2.6% | +0.1pp | 約 2–4%（估計） | 中性 |
| Dividend coverage（TTM FCF / 股利） | 約 2.1x | — | 約 1.5–2.5x（估計） | 良 |
| Diluted shares（Q2 2026, M） | 953.3 | +0.6% | n/a | 需關注（稀釋） |
| Insider 6M 公開市場淨額 | -5.76M USD（僅 1 筆賣出） | — | n/a | 中性偏弱（規模極小） |
| Short interest / Float | 2.84% | 月增 9.8% | n/a | 溫和 |
| trailing P/E（info） | 21.5x | — | 約 20–25x（估計） | 中性 |
| trailing P/E（adjusted TTM） | 20.5x | — | — | 中性 |
| forward P/E | 19.0x | — | 約 18–22x（估計） | 中性 |
| EV/EBITDA（TTM） | 約 16.8x（info 18.3x） | — | 約 13–17x（估計） | 偏高 |
| P/FCF（TTM） | 約 18.1x | — | 約 18–25x（估計） | 中性 |
| P/S（TTM） | 約 3.4x | — | 約 2–3x（估計） | 偏高 |
| P/B | 約 6.9x | — | 約 2–4x（估計） | 偏高（受商譽與低有形淨值影響） |
| PEG（info） | 2.38 | — | 約 1.5–2.0（估計） | 偏高 |
| Adjusted EPS（FY2026E, USD） | 12.42（含 Q4 估計 4.63） | 約 +7.3% vs FY2025 adj 11.57 | n/a | 中性 |
| Dividend yield | 2.68% | — | 約 2–3%（估計） | 中性 |
| 分析師目標價均值 | 257.22（+2.0%） | — | n/a | 中性 |

## Red flags
- 淨負債持續擴大：Net debt 由 2024 年末 41.03B 升至 2026-06-30 54.82B；Total debt / Equity 達 189%。
- 現金大幅下降：現金及短期投資 6 個月內由 14.42B 降至 8.13B（-44%），流動比率 0.79，營運資金 -7.51B。
- 營收成長低、季度動能轉弱：3 年 CAGR 3.7%；Q2 2026 營收 YoY +1.1%、營業利益 YoY -7.8%、營業利益率收縮 1.6pp。
- GAAP 獲利品質需打折：FY2025 淨利含 Q4 大額稅務利益（tax provision -1.44B）；調整後 EPS 成長與 GAAP 營業利益走勢出現落差，需以財報附註驗證。
- 併購依賴與商譽風險：2025 年 purchase of business 8.30B（占 FCF 約 72%），商譽升至 67.72B，有形淨值為 -46.46B。
- 股權稀釋未被完全抵銷：FY2025 diluted shares +1.2%，Q2 2026 YoY +0.6%，買回 1.02B 不足以覆蓋股權發行與 SBC。
- 股價表現落後大盤：52 週 -11.5% vs S&P 500 +13.7%，現價距 52 週高點 -24.2%。
- 空方部位小幅增加：sharesShort 月增 9.8% 至 24.16M（2.84% float）。
- 治理風險評分（info，1–10 量表）：auditRisk 8、boardRisk 7、overallRisk 6。
- 內部人交易訊號薄弱：6 個月內僅一筆公開市場賣出（5.76M USD），無公開市場買入；近期買入（2026-01 至 02）金額亦小。
- 資料落後與不一致（重要）：
  - quarterly 財務與資產負債表僅更新至 2026-06-30；info 之 mostRecentQuarter 為 2026-09-30，Q3 2026 完整三大報表未進入本工具輸出，Q3 營收、現金流與負債變化無法驗證。
  - info totalRevenue（69.87B）、EBITDA（16.14B）、freeCashflow（12.24B）、operatingCashflow（15.83B）與 quarterly / 年報加總不一致。
  - trailingEps（11.72）與 GAAP TTM EPS（11.27）及 adjusted TTM EPS（12.31）三者口徑不同，本報告分別標註，不混用。
  - 價格為 2026-10-23 盤前 cache 數據，非當日收盤價。
  - 無法取得分部營收、Q3 管理層指引原文、標的併購細節：皆記為 DATA_UNAVAILABLE。

FUNDAMENTALS REPORT COMPLETE
