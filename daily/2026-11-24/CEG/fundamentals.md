# Fundamentals — CEG as of 2026-11-24

## Executive summary
CEG（Constellation Energy，美國最大核能發電商，Utilities - Independent Power Producers）TTM 營收 34.25B USD、淨利 4.37B USD、TTM 自由現金流約 1.34B USD，獲利在 2026 年前三季明顯回升（2026Q3 EPS 5.19，Yahoo 報告值 5.06，超出預期 30%），但 2026 年資產負債表因併購與增發大幅擴張（total debt 由 2025 年底 8.99B 升至 2026Q3 23.39B，流通股數由 312M 增至 352M）。估值面 trailing P/E 20.2x、forward P/E 18.7x、EV/EBITDA 約 11.2x，相對獲利成長並不昂貴，但 FCF 仍為正值且偏薄，股價距 52 週高點仍有 34% 跌幅、低於 50 日與 200 日均線；分析師 23 位評等為 Buy（mean 1.64），平均目標價 340.38 USD。整體財務健康度為「獲利改善、槓桿顯著升高、現金流尚待驗證」，估值偏合理，財務結構是主要風險點。本報告不提供交易建議。

## Revenue & profitability

**資料時點說明**：Yahoo live 介面於本次執行時被阻擋（CONNECT 403），本報告所有數字取自 repo 快取 `prices/yf/CEG.json`（`_refreshed_at` 2026-11-23T17:57:43+00:00，`_misses` 為空）。快取內最新價為 2026-11-23（info `regularMarketTime` 換算日期）。未發現資料晚於 2026-11-24 的內容；2027-02-24 為下一次財報預定日，屬未來排程而非既有資料。

**年度營收（USD B，FY 為 12 月底）**

| 年度 | Total Revenue | 年增率 | Gross Profit | 毛利率 | 營業利益（報告值） | 營業利益率 | 淨利 | 淨利率 | Diluted EPS |
|---|---|---|---|---|---|---|---|---|---|
| FY2022 | 24.44 | n/a | 2.14 | 8.7% | 0.50 | 2.0% | -0.16 | -0.7% | -0.49 |
| FY2023 | 24.92 | +2.0% | 3.23 | 13.0% | 1.61 | 6.5% | 1.62 | 6.5% | 5.01 |
| FY2024 | 23.57 | -5.4% | 5.99 | 25.4% | 4.35 | 18.5% | 3.75 | 15.9% | 11.89 |
| FY2025 | 25.53 | +8.3% | 4.69 | 18.4% | 3.09 | 12.1% | 2.32 | 9.1% | 7.40 |

- 營收 CAGR：2022–2025（3 年）約 +1.5%。2021 年資料缺失，無法計算 5 年 CAGR。
- FY2025 淨利年減 38.1%、Diluted EPS 年減 37.8%，主因毛利率由 25.4% 回落至 18.4%，以及營業利益率由 18.5% 降至 12.1%。
- 年度 2024 與 2025 獲利的 Yahoo 欄位不一致：`Operating Income` 為 4.20B（2025），`Total Operating Income As Reported` 為 3.09B。本報告以 As Reported 數字為準。

**季度趨勢（USD B）**

| 季度 | Total Revenue | Gross Profit | 毛利率 | 淨利 | Diluted EPS | 單季 YoY（營收） |
|---|---|---|---|---|---|---|
| 2025Q4 | 6.07 | 0.99 | 16.3% | 0.43 | 1.38 | n/a |
| 2026Q1 | 11.12 | 2.99 | 26.9% | 1.59 | 4.49 | n/a |
| 2026Q2 | 7.50 | 1.23 | 16.4% | 0.51 | 1.42 | n/a |
| 2026Q3 | 9.55 | 3.16 | 33.1% | 1.84 | 5.19 | +45.4%（vs 2025Q3 6.57） |

- TTM（2025Q4 至 2026Q3 合計）：營收 34.25B、淨利 4.37B，與 Yahoo info 的 `totalRevenue` 34.25B、`netIncomeToCommon` 4.37B 一致（交叉驗證通過）。
- 2026Q3 淨利年增 +97.3%（與 info `earningsQuarterlyGrowth` 0.973 一致）。營收年增率 +45.4% 與 info `revenueGrowth` 0.454 一致。
- 2026Q2 營業利益為 -0.047B（季度 `Operating Income`），原因資料未說明，需追查（可能為衍生性商品或其他非經常項目，屬推測）。
- TTM 利潤率（Yahoo info）：毛利率 25.2%、EBITDA 利潤率 27.7%、營業利益率 17.9%、淨利率 12.8%。
- 季度毛利率波動大（16%–33%），TTM 數字掩蓋了單季不穩定性，屬於需關注的特徵。

**ROE / ROIC**
- ROE（info）：18.3%；ROA（info）：4.9%。
- ROIC 為本報告估算：NOPAT ÷ Invested Capital。2025 年：EBIT 4.02B × (1 − 33.8%) ÷ 23.51B ≈ 11.3%；2024 年：5.02B × (1 − 17.1%) ÷ 21.58B ≈ 19.3%。2026 年因併購後 invested capital 未能在快取中直接取得，故不估算，ROIC 有下滑可能。

**Segment mix**：Yahoo 的 `longBusinessSummary` 僅列出五個營運區段（Mid-Atlantic、Midwest、New York、ERCOT、Other Power Regions）與約 31,676 MW 裝置容量（核能、風、太陽能、天然氣、水力）。快取中沒有各區段營收，故 segment 營收占比為 n/a。

## Cashflow & balance sheet

**現金流（USD B）**

| 年度 / 期間 | Operating CF | Capex | FCF（Yahoo 定義） | FCF ÷ 淨利 |
|---|---|---|---|---|
| FY2022 | -2.35 | -1.69 | -4.04 | n/m（淨虧） |
| FY2023 | -5.30 | -2.42 | -7.72 | 不適用（FCF 為負） |
| FY2024 | -2.46 | -2.57 | -5.03 | 不適用（FCF 為負） |
| FY2025 | 4.24 | -2.95 | 1.29 | 0.56 |
| TTM（2025Q4–2026Q3） | 5.78 | -4.45 | 1.34 | 0.31 |

- FCF 率：FY2025 為 5.0%（1.29 ÷ 25.53）；TTM 為 3.9%（1.34 ÷ 34.25）。
- FCF ÷ 淨利：FY2025 為 0.56，TTM 為 0.31，皆低於 0.9 健康門檻。
- FY2022–FY2024 合計 FCF 約 -16.8B，前三年為資本支出擴張期，且經營現金流在 FY2023–FY2024 為負。
- **資料衝突**：Yahoo info 的 `freeCashflow` 為 -5.37B，但季度 CF 加總與年度 FCF 均為正值（TTM +1.34B）。本報告採用報表加總值。info 欄位與報表不一致，需後續確認（見 Red flags）。

**資產負債表（USD B）**

| 項目 | 2025-12-31 | 2026-03-31 | 2026-06-30 | 2026-09-30 |
|---|---|---|---|---|
| Total Debt | 8.99 | 22.47 | 24.70 | 23.39 |
| Cash & Equivalents | 3.64 | 0.80 | 0.70 | 0.60 |
| Net Debt | 5.35 | 21.67 | 24.00 | 22.78 |
| Stockholders' Equity | 14.52 | 33.48 | 31.98 | 32.71 |
| Total Assets | 57.25 | 96.91 | 98.25 | 99.19 |
| Current Assets | 12.12 | 18.01 | 18.97 | 18.92 |
| Current Liabilities | 7.94 | 13.22 | 13.03 | 12.73 |
| 流通股數（M） | 312.3 | 362.0 | 355.3 | 351.6 |

- 流動比率（2026Q3）：18.92 ÷ 12.73 = 1.49（info `currentRatio` 1.486 一致）。
- D/E（2026Q3）：23.39 ÷ 32.71 ≈ 0.72（info `debtToEquity` 70.8%）。2025 年底為 0.62。
- 淨負債 ÷ TTM EBITDA：2026Q3 為 22.78 ÷ 9.48 ≈ 2.4x（2025 年底約 0.85x）。
- 利息保障倍數（FY2025）：EBIT 4.02 ÷ 利息費用 0.51 ≈ 7.9x。TTM 利息費用未在快取中提供。
- 2026 年資產負債表大幅擴張（資產 +73%、負債由 42.4B 升至 66.1B、股東權益由 14.5B 升至 32.7B）。快取中沒有直接註明併購案名稱。現金流量表 2026Q1 投資現金流出 -3.73B，且流通股數一次增加約 50M 股，大幅跳升。此兩項與大型併購吻合，但這是推測，需以公司公告確認。
- 現金水位已由 2025 年底的 3.64B 降至 2026Q3 的 0.60B，流動性緩衝明顯變薄。
- TTM EBITDA（Yahoo info）為 9.48B；季度 EBITDA 加總為 9.40B，兩者接近。

## Capital allocation & insider signal

**資本配置**
- Capex：FY2022 1.69B → FY2023 2.42B → FY2024 2.57B → FY2025 2.95B（FY2025 年增 +15%）。TTM capex 4.45B，2026 年季度 capex 為 1.28B、1.25B、0.94B，資本支出仍處高檔。
- 股利：FY2025 配息 0.49B，每季 0.427 USD，年化 dividendRate 1.71 USD；以 352M 股計算的年化總配息約 0.60B。Dividend yield 0.72%（5 年平均 0.56%），payout ratio 13.4%。TTM FCF 對股息覆蓋倍數約 2.2x（1.34B ÷ 0.60B），在 FCF 為正前提下覆蓋尚可，但 FY2023–FY2024 FCF 為負時並未覆蓋。
- 回購：FY2023 0.99B、FY2024 1.00B、FY2025 0.40B；2026Q3 回購 1.03B。同期流通股數自 312M 增至 352M，淨增約 12.7%（主要由併購增發所致，回購並未抵銷增發）。
- Debt 發行／償還：FY2025 發行 1.65B、償還 1.08B；2026 年舉債規模明顯大於前期。

**內部人交易（最近 6 個月，即 2026-05-24 至 2026-11-24）**
- 唯一公開市場買入：Director Roger W. Crandall，2026-08-11，1,500 股，約 0.42M USD（每股 278.62 USD）。
- 其他 2026 年內 Director 股票授予（award）：Crandall 2026-08-04 462 股（約 0.12M USD）；2026-04-28 多位董事各 556 股（每股 305.71 USD，超出 6 個月窗口，僅供參考）。
- 6 個月內無內部人賣出紀錄。2026 年 2 月另有 CEO、CFO 與多位高管的紀錄（Transaction 欄位空白，性質無法確認），且超出 6 個月窗口。
- 淨買入規模：約 0.42M USD（不足 0.001% 市值），對市場判斷的參考價值很低。
- 內部人持股比例（Yahoo）：0.35%。Insider 買入僅為象徵性。
- 2025 年 2 月曾有單筆 Officer 賣出（Bauer，4,000 股，約 1.24M USD），屬過去紀錄。

**機構持股（2026-09-30 13F 資料）**
- 機構持股比例 85.0%，機構數 2,534 家。
- 前十大：BlackRock 7.36%（持股 25.88M 股，季增 +5.4%）；Vanguard Capital Management 6.20%（季增 +3.6%）；State Street 5.80%（季增 +5.1%）；Vanguard Portfolio Management 4.66%（季增 +3.5%）；Capital International Investors 4.10%（季增 +13.9%）；ECP ControlCo, LLC 4.03%（14.18M 股，季內無變動）；Invesco 3.08%（季減 -2.4%）；Morgan Stanley 2.69%（季增 +4.7%）；Geode 2.22%（季增 +4.0%）；FMR 1.79%（季減 -3.6%）。
- ECP ControlCo, LLC 持有 4.03%，為大型單一股東；其持股來源資料未說明，但其持股數與增發後股本變化相符，屬推測。
- 空頭：short interest 10.49M 股，佔流通股約 3.3%，short ratio 2.5 天；上月為 11.84M 股，空單減少約 11%。

## Valuation

以現價 250.81 USD（info `currentPrice`，2026-11-23）計算。市值 88.19B USD，企業價值（EV）106.59B USD。

| 指標 | 數值 | 說明 |
|---|---|---|
| Trailing P/E | 20.2x | 250.81 ÷ TTM EPS 12.44 |
| Forward P/E | 18.7x | 250.81 ÷ forward EPS 13.38 |
| EV/EBITDA（TTM） | 11.2x | 106.59B ÷ TTM EBITDA 9.48B |
| P/FCF（TTM） | 約 66x | 88.19B ÷ TTM FCF 1.34B；以 info FCF -5.37B 則為 n/m |
| P/S（TTM） | 2.6x | info `priceToSalesTrailing12Months` 2.57 |
| P/B | 2.7x | 250.81 ÷ BVPS 93.04 |
| PEG（info trailingPegRatio） | 0.82 | 以 Yahoo 快取數字引用 |

- 分析師評價（rec_summary，當期）：Strong Buy 6、Buy 14、Hold 5、Sell 0、Strong Sell 0，共 23 位；平均評等 1.64（Buy）。近 3 個月評等結構穩定，未見下調。
- 目標價：平均 340.38、中位數 346、最高 399、最低 240 USD。平均目標價相對現價隱含 +35.7% 上行空間；最低目標價 240 低於現價。
- 股價位置：52 週區間 228.63–380.78，現價距高點 -34.1%、距低點 +9.7%；低於 50 日均線 266.22（-5.8%）與 200 日均線 278.31（-9.9%）。
- 與同業比較（**估計，非資料來源**）：美國 Utilities – Independent Power Producers 同業的 trailing P/E 中位數約 18–22x、EV/EBITDA 約 11–13x、P/S 約 2–3x、P/B 約 2–3x。以此估計，CEG 的 P/E 與 EV/EBITDA 落在同業區間中段，並非明顯偏貴或偏便宜。P/FCF 因 FCF 偏低，指標數字偏高，在同業比較上意義有限。

## Key catalysts

- **下一次財報**：2027-02-24（Yahoo earnings_dates，`isEarningsDateEstimate` 為 false）。該季 EPS 共識估計 2.57 USD。
- **近期財報結果**：2026-11-09 公布 2026Q3，EPS 5.06 vs 預估 3.89（+30.1%）；2026-08-06（2026Q2）EPS 2.55 vs 2.28（+11.7%）；2026-05-11（2026Q1）EPS 2.74 vs 2.60（+5.3%）；2026-02-24（2025Q4）EPS 2.30 vs 2.25（+2.4%）。過去四季皆為正向超預期。2025 年則為 Feb +14.1%、May -3.1%、Aug +4.2%、Nov -2.6%。
- **股息**：除息日 2026-11-16（已過）；Yahoo `dividendDate` 為 2026-12-04（屬支付日，需確認）。
- **管理層指引**：快取中無公司 guidance 資料，標示為 n/a。
- **併購整合與資本支出**：資產規模與股本的大幅變化顯示 2026 年有重大交易事件，但快取中無該交易的條件、時程與效益描述。後續整合進度、利息成本上升對獲利的影響，是需追蹤的催化因子（屬推測）。
- **共識預期上修**：目前 forward EPS 13.38、FY2026 EPS 共識 12.57；2026 年 9 個月 diluted EPS 合計 11.10，表示 Q4 EPS 隱含約 1.5 USD 左右（由 12.57 - 11.10 推算，屬估算）。

## Metrics table

金額單位：USD（B = 十億，M = 百萬）。市值與 EV 為 B，每股數字為 USD。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| Total Revenue（FY2025，B USD） | 25.53 | +8.3% | n/a | 中性，3 年 CAGR 約 +1.5% |
| Total Revenue（TTM，B USD） | 34.25 | n/a | n/a | 因併購顯著擴大 |
| 2026Q3 營收 YoY | 9.55 | +45.4% | n/a | 強勁 |
| Gross Margin（TTM） | 25.2% | n/a | n/a | 波動大，季度 16%–33% |
| Operating Margin（TTM，info） | 17.9% | n/a | n/a | 中性 |
| Net Margin（TTM） | 12.8% | FY2025 9.1%（FY2024 15.9%） | n/a | 恢復中，但未達 FY2024 水準 |
| EBITDA Margin（TTM） | 27.7% | n/a | n/a | 尚可 |
| ROE（info） | 18.3% | n/a | n/a | 良好 |
| ROIC（估算，FY2025） | 約 11.3% | FY2024 約 19.3% | n/a | 下滑 |
| FCF（TTM，B USD，報表加總） | 1.34 | n/a | n/a | 正值但薄弱 |
| FCF 率（TTM） | 3.9% | n/a | n/a | 偏低 |
| FCF ÷ 淨利（TTM） | 0.31 | n/a | 0.9（健康門檻） | 不健康 |
| Operating CF（TTM，B USD） | 5.78 | n/a | n/a | 改善中 |
| Capex（TTM，B USD） | 4.45 | FY2025 +15% | n/a | 高檔 |
| Total Debt（2026Q3，B USD） | 23.39 | 2025 年底 8.99，+160% | n/a | 明顯升高 |
| Net Debt（2026Q3，B USD） | 22.78 | 2025 年底 5.35 | n/a | 偏高 |
| Net Debt ÷ TTM EBITDA | 2.4x | 2025 年底 0.85x | 約 2–3x（估計） | 偏高 |
| Current Ratio（2026Q3） | 1.49 | 2025 年底 1.53 | 約 1.0–1.5（估計） | 可接受 |
| Debt ÷ Equity（2026Q3） | 0.72 | 2025 年底 0.62 | 約 1.0–1.5（估計） | 可接受 |
| Cash（2026Q3，B USD） | 0.60 | 2025 年底 3.64 | n/a | 偏低 |
| 流通股數（2026Q3，M） | 351.6 | 2025 年底 312.3，+12.7% | n/a | 稀釋明顯 |
| Dividend Yield | 0.72% | 5 年平均 0.56% | 約 3%–4%（估計，依一般公用事業經驗） | 偏低 |
| Payout Ratio | 13.4% | n/a | n/a | 保守 |
| 股息覆蓋（TTM FCF ÷ 年化股息） | 約 2.2x | n/a | n/a | 尚可 |
| 內部人 6 個月淨買入（USD） | 約 0.42M | n/a | n/a | 象徵性，佔市值 <0.001% |
| 機構持股比例 | 85.0% | n/a | 約 80%–90%（估計） | 正常 |
| 空頭比例（佔流通） | 3.3% | 上月 short 11.84M → 10.49M | 約 2–5%（估計） | 偏低 |
| Trailing P/E | 20.2x | n/a | 約 18–22x（估計） | 中性 |
| Forward P/E | 18.7x | n/a | n/a | 中性偏合理 |
| EV/EBITDA（TTM） | 11.2x | n/a | 約 11–13x（估計） | 中性 |
| P/FCF（TTM） | 約 66x | n/a | n/a | 偏高，受 FCF 偏低影響 |
| P/S（TTM） | 2.6x | n/a | 約 2–3x（估計） | 中性 |
| P/B | 2.7x | n/a | 約 2–3x（估計） | 中性 |
| Beta | 1.13 | n/a | n/a | 中等 |
| 分析師平均評等 | 1.64（Buy） | n/a | n/a | 正面 |
| 平均目標價（USD） | 340.38 | 相對現價 +35.7% | n/a | 正面 |
| 股價距 52 週高點 | -34.1% | n/a | n/a | 偏弱 |
| 股價相對 200 日均線 | -9.9% | n/a | n/a | 偏弱 |
| Yahoo overall governance risk | 7（滿分 10） | n/a | n/a | 偏高 |

## Red flags
- **現金流資料衝突**：Yahoo info 的 freeCashflow 為 -5.37B，與季度與年度報表推算的 TTM FCF +1.34B 相反。FY2023–FY2024 FCF 為負，FY2025 首度轉正。FCF 能否持續為正仍需驗證。
- **槓桿大幅升高**：total debt 2025 年底 8.99B → 2026Q3 23.39B（+160%），淨負債 ÷ EBITDA 由約 0.85x 升至約 2.4x。利息成本將持續上升（FY2025 利息費用 0.51B，2026 年應明顯高於此）。
- **股本稀釋**：流通股數由 312M 增至 352M（+12.7%），2026Q1 一次增加約 50M 股，其中 ECP ControlCo 持有 14.18M 股（4.03%）。
- **現金水位偏低**：2026Q3 現金 0.60B，較 2025 年底 3.64B 下降 83%。流動性緩衝薄。
- **獲利波動大**：2026 年季度毛利率在 16%–33% 之間波動；2026Q2 營業利益為負（-0.047B），原因資料未說明。
- **獲利與 EPS 不一致**：Yahoo 財報 EPS 報告值 5.06（2026Q3）與季度報表 diluted EPS 5.19 不同，可能為調整後與 GAAP 口徑差異，需確認。
- **獲利下滑歷史**：FY2025 淨利年減 38%，毛利率由 25.4% 回落至 18.4%。
- **股價技術面偏弱**：現價低於 50 日與 200 日均線，52 週跌幅 34%。
- **治理風險分數偏高**：Yahoo overallRisk 7、boardRisk 8、shareholderRightsRisk 8（滿分 10）。
- **內部人買入幾乎沒有**：6 個月內僅一筆約 0.42M USD 的象徵性買入，不足以作為內部人信心的正面訊號。
- **快取資料時效性**：本次 Yahoo live 介面被阻擋，所有數字來自快取（refreshed 2026-11-23 17:57 UTC）。機構持股為 2026-09-30 的 13F 資料，內部人資料為截至快取時點的申報紀錄，非即時。
- **缺口**：segment 營收、管理層 guidance、併購條件與整合進度、TTM 利息費用、2026 年 invested capital 皆為 n/a 或 DATA_UNAVAILABLE（快取與 live 均無），本報告未以估計值取代。

FUNDAMENTALS REPORT COMPLETE
