# Fundamentals — HON as of 2026-10-27

## Executive summary
Honeywell (HON) 的財務體質屬中等水準：FY2025 營收 37.44B USD、FCF 5.42B USD、FCF/NI 1.15，且 2026 年 Q3 淨負債大幅降至 10.90B USD（Q2 為 25.24B USD），約為 TTM EBITDA 的 1.2x；但 2026 年 Q2 單季 5.92B USD 的 Gain On Sale Of Business 使 trailing P/E（10.96x）與 ROE（44.4%）嚴重失真，且 TTM 營業現金流僅 1.95B USD、流動比率 0.96、營運資金為負，短期流動性偏緊。估值上，以 forward P/E 22.5x、EV/EBITDA 9.0x、P/S 1.86x 衡量，市場並未給予明顯折價或溢價，分析師共識為 Buy（平均目標價 253.47 USD，較參考價高約 14.6%）。資料來源存在明顯的組合變動（perimeter change）與 discontinued operations 不一致問題，本報告數字需以 10-Q/10-K 原文複核後才能作為決策基礎。

## Quantinuum 曝險背景（簡述）
- 依使用者提供之背景，HON 持有 Quantinuum 約 54% 股權，故 HON 為 Quantinuum 的多數股東。yfinance 不提供 Quantinuum 獨立財務資料，以下僅就 HON 合併報表中可觀察到的跡象描述，不作出未經驗證的推論。
- Quantinuum 相關跡象（工具數據，性質待 10-Q 確認）：
  - 2026-06-30 季度：Gain On Sale Of Business 5,921M USD、Special Income Charges 5,858M USD、Other Income Expense 6,028M USD，單季 Pretax Income 7,529M USD，遠高於 Operating Income 1,785M USD。此非經常性收益是 TTM 獲利被放大的主因。
  - Minority Interest（非控制權益，資產負債表）：2026-03-31 為 1,077M USD，2026-06-30 降至 320M USD，2026-09-30 為 237M USD。以 54% 持股推算，非控制權益的市場價值遠高於帳面數字；帳面 NCI 不能代表 Quantinuum 的經濟價值。
- 估值含意：HON 市值中包含 Quantinuum 約 54% 的經濟權益，但該部分估值無法從 yfinance 數字導出；若需做 sum-of-parts，需另外取得 Quantinuum 的估值依據。
- 其他跡象：2026 年 Q1 Repayment Of Debt 為 -18,623M USD，同季 Net Other Financing Charges 為 +15,743M USD，期間對應的交易結構未在工具資料中揭露，本報告不做推論。

## Revenue & profitability
資料口徑：年度資料單位為 USD B；季度資料單位為 USD M（以下統一換算為 B）。

**營收與成長**
- 年度 Total Revenue：2022 35.47B、2023 33.01B、2024 34.72B、2025 37.44B。
- YoY：2023 -6.9%、2024 +5.2%、2025 +7.9%。
- CAGR：2022–2025 三年約 +1.9%；2023–2025 兩年約 +6.5%。
- TTM Total Revenue 37.74B USD（info），revenueGrowth 1.3%。
- 注意：季度營收口徑不一致。Q4 2025 6.86B、Q1 2026 9.14B、Q2 2026 9.72B、Q3 2026 4.99B 四季加總約 30.72B，與 info 的 TTM 37.74B 不符；Q3 2026 YoY（對 Q3 2025 的 4.93B）為 +1.3%，與 TTM 增速一致。推測 2026 年 H1 數字包含即將分拆/已分拆之業務，而 Q3 2026 已不含，但工具未明確標示，須以原始 filing 確認。
- 分部結構（依 info.longBusinessSummary）：Industrial Automation、Building Automation、Energy and Sustainability Solutions（含 UOP）。工具未提供分部營收數字，無法量化分部占比。

**獲利能力（年度，USD B）**

| 年度 | 毛利率 | 營業利益率 | 淨利率 | Diluted EPS |
|---|---|---|---|---|
| 2022 | 37.0% | 18.1% | 14.0% | 14.54 |
| 2023 | 37.5% | 18.5% | 17.1% | 16.94 |
| 2024 | 38.5% | 19.2% | 16.4% | 17.42 |
| 2025 | 36.9% | 17.5% | 12.6% | 14.72 |

- 2025 Diluted EPS 年減 15.5%，但 Total Unusual Items 為 -1.435B USD（2024 為 -0.326B），含 Impairment 2025 Q4 979M USD。以 Normalized Income 推算：2025 5.60B / 321.4M 股 ≈ 17.41，2024 為 5.22B / 327.65M 股 ≈ 15.93，正常化 EPS 年增約 +9.3%。
- R&D 2025 1.81B USD（2024 1.45B，+24.6%），占營收 4.8%（2024 為 4.2%）。
- 2026 年季度營業利益率：Q1 19.0%、Q2 18.4%、Q3 14.8%（Q3 2025 為 8.4%）。
- ROE：info 44.4%（TTM，受 Q2 一次性利益與低淨值放大影響，不宜直接採信）；以 FY2025 NI 4.73B / YE2025 股東權益 13.90B 計算為 34.0%。
- ROIC（自算）：FY2025 EBIT 6.82B × (1 - 稅率 18.4%) ≈ 5.56B，除以平均投入資本（YE2024 49.66B、YE2025 48.48B 平均 49.07B）≈ 11.3%。

## Cashflow & balance sheet

**現金流（年度，USD B）**

| 年度 | OCF | Capex | FCF | FCF margin | FCF/NI |
|---|---|---|---|---|---|
| 2022 | 5.27 | 0.77 | 4.51 | 12.7% | 0.91 |
| 2023 | 5.34 | 0.74 | 4.60 | 13.9% | 0.81 |
| 2024 | 6.10 | 0.87 | 5.23 | 15.1% | 0.92 |
| 2025 | 6.41 | 0.99 | 5.42 | 14.5% | 1.15 |

- FY2025 FCF/NI 1.15，高於 0.9 的健康門檻；但 2023 為 0.81，現金轉換並非穩定。
- 2026 季度現金流明顯轉弱：Q1 OCF -650M USD（FCF -873M）、Q2 OCF 1,276M（FCF 961M）、Q3 OCF 117M（FCF 286M）。前三季合計 OCF 約 0.74B USD，FCF 約 0.37B USD。
- info 報告 TTM freeCashflow 為 7.02B USD，但季度 OCF 加總 TTM 僅 1.95B USD（與 info operatingCashflow 一致），兩者無法調和；本報告以季度為準，TTM FCF 約 1.5B USD（Q4 2025 至 Q3 2026 季度 FCF 加總）。此為重大資料風險。

**資產負債表**

| 指標 | 2025-12-31 (USD B) | 2026-09-30 (USD B) | 備註 |
|---|---|---|---|
| Total Debt | 35.56 | 16.59 | 2026 年前三季償還約 19B |
| Cash & Equivalents | 12.49 | 5.69 | 9 月底現金低於年初 |
| Net Debt | 22.09 | 10.90 | |
| Total Equity（含 NCI） | 15.03 | 22.65 | 股東權益 22.42（Q3） |
| Tangible Book Value | -13.91 | -0.59 | 有形淨值為負，年初 -13.9B |
| Current Ratio | 1.30 | 0.96 | 14.32 / 14.91 |
| Working Capital | 6.97 | -0.60 | |
| Debt/Equity | 2.56x | 0.74x | 年初權益受庫藏股與 AOCI 壓縮 |

- Net Debt/EBITDA：YE2025 為 2.69x（22.09 / 8.21 reported EBITDA）；Q3 2026 為 1.21x（10.90 / 9.02 TTM EBITDA）。
- 利息覆蓋（FY2025）：EBIT 6.82B / Interest Expense 1.34B ≈ 5.1x。
- 流動性偏緊：Q3 2026 流動比率 0.96、Quick Ratio 0.76，短期債務 6.21B（Current Debt）；需留意 2027 年到期債務與現金水位。
- 股權結構：庫藏股 43.85B（Q3 2026），長期壓縮帳面權益；帳面 P/B 3.13x（BV/share 70.64）意義有限。

## Capital allocation & insider signal

**資本配置**
- 股利：年化股息 2.80 USD（季 0.70），殖利率 1.27%，2025 現金股利支付 2.98B USD，FCF 覆蓋約 1.8x（5.42 / 2.98）。
- 最新股息公告：0.70 USD，除息日 2026-11-13（info corporateActions）。
- 買回：2022 4.20B、2023 3.72B、2024 1.66B、2025 3.80B USD；2026 Q1 1.0B，Q2 與 Q3 為 0。買回已在 2026 下半年暫停。
- Capex：2025 0.99B（占營收 2.6%），年增 13.2%。
- 流通股數：Diluted Average Shares 由 2022 的 341.6M 降至 2025 的 321.4M，Q3 2026 為 319.2M；Ordinary Shares 2026-09-30 為 316.94M。
- 債務：2026 年 Q1 大幅償還債務（18.6B）後，Q2、Q3 債務仍持續償還（5.9B、6.1B）；資本配置重心已由股東回饋轉向去槓桿。

**內部人交易（過去 6 個月，2026-04-26 至 2026-10-26）**
- 公開市場賣出：KENNETH J WEST（Officer）2026-08-03 賣出 316 股 @245.47（約 77.6K USD）；2026-07-27 賣出 17,032 股 @243.77（約 4.15M USD），同日行使衍生性證券 17,032 股（行使價區間 181.39–200.61，價值約 3.31M USD）。
- 公開市場買入：無。
- 其餘約 100 筆紀錄無金額（Value 為 null），多數為 RSU/PSU 歸屬或代扣稅性質，工具未標示交易代碼，需以 Form 4 確認。
- 合計公開市場賣出約 4.23M USD，相對市值 70.09B USD 約 0.006%，規模極小，不構成顯著訊號。
- 參考脈絡：2026 年 1–3 月亦有數筆行使後賣出（MAILLOUX 約 2.42M / 1.26M USD、LIEBLEIN 1.43M USD、DAVIS 0.57M USD、CURRIER 0.55M USD、價位 229–244 USD），但不在 6 個月窗口內。
- CEO/CFO（Kapur、Stepniak）於窗口內無公開市場賣出。內部人持股比例 0.082%。

## Valuation

價格基準：regularMarketPrice 221.15 USD（盤前快照，cached 2026-10-26 08:48 ET，前收 218.31 USD）。市值 70.09B USD，EV 81.47B USD。

| 指標 | 數值 | 說明 |
|---|---|---|
| Trailing P/E | 10.96x | TTM EPS 20.17；含 Q2 一次性利益，不具代表性 |
| Forward P/E | 22.47x | Forward EPS 9.84；EPS 基礎已因組合變動下修 |
| EV/EBITDA（TTM） | 9.04x | EBITDA TTM 9.02B USD |
| EV/EBITDA（FY2025） | 9.93x | 以 EV 81.47B / EBITDA 8.21B 計算 |
| P/S（TTM） | 1.86x | |
| P/FCF | 約 10.0x（info FCF 7.02B）／約 12.9x（FY2025 FCF 5.42B）／約 46x（季度加總 TTM FCF 約 1.5B） | 三種口徑差距大，採用時需標註 |
| P/B | 3.13x | |
| PEG | 3.61 | |

- 分析師：23 位，推薦均值 2.0（Buy），目標價平均 253.47 USD、中位數 254.0、高 290.0、低 186.0。
- 52 週區間 195.87–260.28 USD；50 日均線 212.30、200 日均線 230.73。
- 盈餘紀錄：過去 8 季 EPS 皆超過預估（超出幅度 +2.1% 至 +13.6%），最新一季（2026-10-22）EPS 2.27 vs 預估 2.16，+4.9%。注意：2025 年前的 EPS 為舊組合基礎（約 4–5 USD/季），2026 年起為 1.9–2.3 USD/季，不可直接比較。
- 估值判讀：以 forward 與 EV/EBITDA 衡量，估值約落在工業類股中段（估計值，見下表）；trailing P/E 因一次性收益失真，不應作為估值錨點。

## Key catalysts
- 已公布：2026-10-22 Q3 財報（EPS 2.27 vs 2.16 預估，超出 4.9%）。
- 下次財報：工具標示 2027-01-28（EPS 預估 2.45），為 yfinance 估計日期，是否為確認日期需查證。
- 股息：除息日 2026-11-13，金額 0.70 USD。
- 組合變動：Aerospace 分拆或其他重大交易的時程與影響，工具無直接資料；須以公司公告為準。
- Quantinuum：Q2 的一次性收益與 NCI 變動顯示其股權結構或帳面處理已有變化，後續 10-Q 之附註為關鍵查核點。
- 管理層：CEO Kapur 年薪總額 5.32M USD（FY2025）；治理風險分數 overallRisk 4（1–10 級）、compensationRisk 8 偏高。

## Metrics table

資料單位：營收、利潤、現金流、負債為 USD B；市值與 EV 為 USD B；比率為 %、x。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| Total Revenue（FY2025，USD B） | 37.44 | +7.9% | n/a（估計：中單位位數成長） | 中性 |
| TTM Revenue（info，USD B） | 37.74 | +1.3%（revenueGrowth） | n/a | 成長趨緩 |
| Gross Margin（FY2025） | 36.9% | -1.6pp | 約 30–35%（估計） | 優於同業（估計） |
| Operating Margin（FY2025） | 17.5% | -1.7pp | 約 14–16%（估計） | 中上（估計） |
| Net Margin（FY2025） | 12.6% | -3.8pp | 約 8–10%（估計） | 受一次性項目影響 |
| Normalized EPS（FY2025，USD） | 17.41 | +9.3% | n/a | 正常化獲利改善 |
| Diluted EPS（FY2025，USD） | 14.72 | -15.5% | n/a | 失真，含一次性項目 |
| ROE（TTM，info） | 44.4% | n/a | 約 12–18%（估計） | 失真，不採信 |
| ROIC（FY2025，自算） | 11.3% | n/a | 約 9–12%（估計） | 中性 |
| FCF（FY2025，USD B） | 5.42 | +3.7% | n/a | 良好 |
| FCF/NI（FY2025） | 1.15 | +0.23 | 約 0.8–1.0（估計） | 健康 |
| FCF（季度加總 TTM，USD B） | 約 1.52 | n/a | n/a | 警示 |
| OCF（季度加總 TTM，USD B） | 1.95 | n/a | n/a | 警示 |
| Net Debt（Q3 2026，USD B） | 10.90 | 低於 YE25 22.09 | n/a | 改善 |
| Net Debt/EBITDA（TTM） | 1.21x | 由 2.69x 降低 | 約 2.0–3.0x（估計） | 改善 |
| Current Ratio（Q3 2026） | 0.96 | 由 1.30 降低 | 約 1.2–1.5x（估計） | 偏弱 |
| Debt/Equity（Q3 2026） | 0.74x | 由 2.56x 降低 | 約 0.5–1.0x（估計） | 改善 |
| Tangible BV（Q3 2026，USD B） | -0.59 | 由 -13.91 改善 | n/a | 偏弱 |
| Capex（FY2025，USD B） | 0.99 | +13.2% | 約占營收 3–4%（估計） | 投資節奏穩定 |
| 股利殖利率 | 1.27% | n/a | 約 1.5–2.0%（估計） | 偏低 |
| 股利 FCF 覆蓋（FY2025） | 1.8x | n/a | 約 1.5x 以上（估計） | 健康 |
| 買回（FY2025，USD B） | 3.80 | +130% | n/a | 2026 H2 已暫停 |
| 內部人公開市場淨買賣（6 個月） | 淨賣約 4.23M | n/a | n/a | 規模極小，中性 |
| Trailing P/E | 10.96x | n/a | 約 20–25x（估計） | 失真 |
| Forward P/E | 22.47x | n/a | 約 18–22x（估計） | 略高（估計） |
| EV/EBITDA（TTM） | 9.04x | n/a | 約 13–16x（估計） | 偏低 |
| P/S（TTM） | 1.86x | n/a | 約 2.0–3.0x（估計） | 略低 |
| P/FCF（以 info FCF 計） | 約 10.0x | n/a | 約 18–25x（估計） | 偏低，但口徑未確定 |
| 分析師推薦（均值） | 2.0（Buy） | n/a | n/a | 正面 |
| 分析師平均目標價（USD） | 253.47（+14.6%） | n/a | n/a | 正面 |

（Sector median 欄為估計值，非工具輸出；Industrials / Conglomerates 類別的參考區間為估算。）

## Red flags
- **資料口徑不一致**：TTM 營收（info 37.74B）與季度加總（30.72B）不符；TTM FCF（info 7.02B）與季度加總（約 1.52B）不符；Q4 2025 Diluted EPS 0.92 與同季淨利 -115M USD 不一致；trailing EPS 20.17 與季度 EPS 加總 23.41 不一致。任何以 TTM 為基礎的比率都需先行複核。
- **獲利被一次性收益放大**：2026 Q2 Gain On Sale Of Business 5.92B USD 佔 TTM 淨利的大部分，trailing P/E 10.96x 與 ROE 44.4% 失真。
- **營業現金流轉弱**：2026 年 Q1 OCF 為負，Q3 僅 117M USD；TTM OCF 1.95B USD，相對季度淨利加總（約 7.05B USD）轉換率偏低。
- **短期流動性偏緊**：Q3 2026 流動比率 0.96、營運資金 -0.60B USD、Quick Ratio 0.76；短期債務 6.21B USD。
- **有形淨值為負**：Tangible BV -0.59B USD（Q3 2026），年初為 -13.91B USD，帳面權益受庫藏股與組合變動影響大。
- **Quantinuum 相關不透明**：Q1 Net Other Financing +15.7B USD 與 Q2 Gain On Sale of Business 5.92B USD 之性質、NCI 變動與 Quantinuum 估值，工具資料無法確認，須以 10-Q 附註查核。
- **買回暫停**：2026 Q2–Q3 買回為零，相較 2025 年 3.80B USD 明顯收縮。
- **EPS 基礎變動**：2026 年季度 EPS（約 2 USD）與 2025 年前（約 5 USD）不可直接比較，forward EPS 9.84 相較 trailing 20.17 的落差需以組合說明解釋。
- **治理**：compensationRisk 8（1–10，偏高）。

FUNDAMENTALS REPORT COMPLETE
