# Fundamentals — MTSI as of 2026-11-23

## Executive summary
MTSI 最新會計年度 FY26（9/30 結束）營收 $1,327.6M，YoY +37.3%，Q4 FY26 YoY +62.7%，營業利益率由 FY25 的 13.4% 升至 23.0%，OCF $357.1M，財務體質穩健（現金及短期投資 $792.4M、流動比率 2.54x），但債務 $377.8M 幾乎全數列為流動負債，且 FY26 資本支出 $135.7M（營收 10.2%）使 FCF/NI 僅 0.66，低於 0.9 健康門檻。估值偏高：GAAP trailing P/E 45.2x、EV/EBITDA 39.7x、P/FCF 67.6x 處於高位，forward P/E 16.8x 反映市場對 FY27 獲利續升的預期，股價 $194.91（cache，2026-11-22）較分析師平均目標價 $327 折價約 40%，6 個月內內部人淨賣出 $16.56M、無公開市場買進。基本面評等：財務健康度中上、成長動能強，估值端需依賴後續獲利兌現，本報告不提供交易建議。

**資料時點說明**：分析基準日 2026-11-23。股價取自 cache（2026-11-22 14:27 UTC，`source: cache`，屬預期行為）。其餘財務與內部人資料來自今日 yfinance 工具輸出。未見晚於 2026-11-23 之資料。下次財報日 2027-02-04 為 yfinance 日期，尚未發生。

**單位說明**：本報告財務金額一律為 USD（百萬美元 M 或十億美元 B）。本報告未使用 TWD 或 KRW 單位。

## Revenue & profitability

### 年度趨勢（USD M，FY 9/30 結束）
| 指標 (USD M) | FY23 | FY24 | FY25 | FY26 |
|---|---|---|---|---|
| 營收 Total Revenue | 648.4 | 729.6 | 967.3 | 1,327.6 |
| 營收 YoY | n/a | +12.5% | +32.6% | +37.3% |
| 毛利 Gross Profit | 385.8 | 393.8 | 529.0 | 770.4 |
| 毛利率 Gross margin | 59.5% | 54.0% | 54.7% | 58.0% |
| 營業利益 Operating Income | 107.4 | 73.7 | 129.7 | 305.5 |
| 營業利益率 Operating margin | 16.6% | 10.1% | 13.4% | 23.0% |
| 淨利 Net Income (GAAP) | 91.6 | 76.9 | -54.2 | 335.3 |
| 淨利率 Net margin (GAAP) | 14.1% | 10.5% | -5.6% | 25.3% |
| Normalized Income | 91.6 | 76.9 | 89.5 | 282.8 |
| Diluted EPS (GAAP, USD) | 1.28 | 1.04 | -0.73 | 4.31 |
| Normalized EBITDA | 179.7 | 163.9 | 232.9 | 397.8 |

- 營收 CAGR：FY23→FY26 三年 CAGR 約 27.0%。FY22 欄位為 null，無法計算 4-5 年 CAGR，標記為 n/a。
- 獲利品質：FY25 GAAP 淨損 $-54.2M，主要受 Total Unusual Items $-193.1M 影響。FY26 GAAP 淨利 $335.3M 含 Total Unusual Items +$61.0M，且有效稅率僅 14%。Normalized Income $282.8M 對應淨利率 21.3%，仍為 FY23 以來最高。
- ROE：yfinance 回報 22.2%（自算：FY26 淨利 / 平均股東權益 = 335.3 / 1,511.9 = 22.2%），與 info.returnOnEquity 0.2217 一致。
- ROIC（自算，無工具直接值）：NOPAT = 營業利益 305.5 × (1 − 14%) = 262.7；平均投入資本 (2,037.4 + 1,827.7) / 2 = 1,932.5；ROIC 約 13.6%。若改用 EBIT 396.2 計算則約 17.6%。

### 季度趨勢（USD M）
| 季度 | Q1 FY26 (12/25) | Q2 FY26 (3/26) | Q3 FY26 (6/26) | Q4 FY26 (9/26) | Q4 FY25 (9/25) |
|---|---|---|---|---|---|
| 營收 | 271.6 | 289.0 | 342.2 | 424.8 | 261.2 |
| 毛利率 | 55.9% | 56.9% | 58.3% | 59.9% | 54.5% |
| 營業利益率 | 15.9% | 17.6% | 22.5% | 31.6% | 15.2% |
| 淨利 (GAAP) | 48.8 | 46.3 | 100.7 | 139.4 | 45.1 |
| Diluted EPS (GAAP) | 0.64 | 0.60 | 1.28 | 1.78 | 0.59 |

- Q4 FY26 營收 QoQ +24.1%、YoY +62.7%。FY26 四季營收加總 1,327.6 與年度數一致，數字互相驗證。
- Q4 FY26 淨利 139.4 高於營業利益 134.2，差額主要來自 Total Unusual Items +19.4 及稅率 12.6%。Q3 FY26 亦有 +41.5 的 unusual items。GAAP 季度獲利波動大，需以 normalized 口徑交叉檢視。
- yfinance earnings_dates 所列 Q4 FY26 EPS 為 2.09（預估 2.00，超出 +4.5%），與 GAAP diluted 1.78 口徑不同，推測為調整後 EPS（non-GAAP，yfinance 未明確標示）。

### 業務組合
- yfinance info 僅提供終端市場描述，包括 carrier infrastructure（long-haul/metro、5G/6G、satellite、FTTX/PON）、industrial & defense、data centers、multi-market。
- 各業務線營收占比：DATA_UNAVAILABLE（yfinance 與 info 均未提供分部營收）。

## Cashflow & balance sheet

### 現金流（USD M）
| 指標 (USD M) | FY23 | FY24 | FY25 | FY26 |
|---|---|---|---|---|
| 營運現金流 OCF | 166.9 | 162.6 | 235.4 | 357.1 |
| 資本支出 Capex | -24.7 | -25.6 | -82.2 | -135.7 |
| 自由現金流 FCF | 142.2 | 137.0 | 153.2 | 221.4 |
| FCF margin | 21.9% | 18.8% | 15.8% | 16.7% |
| FCF / NI (GAAP) | 1.55 | 1.78 | 負值（NM） | 0.66 |
| OCF / NI (GAAP) | 1.82 | 2.12 | 負值（NM） | 1.07 |
| 股權激勵 SBC | 38.1 | 45.6 | 79.4 | 87.8 |

- FCF/NI：FY26 為 0.66，低於 0.9 健康門檻。若以 normalized NI 282.8 計算則為 0.78，仍偏低。主因是資本支出大增。
- Capex 占營收：FY26 為 10.2%，FY24 僅 3.5%。FY26 Q3 單季 capex 為 $82.8M，Q4 回落至 $19.4M。Capex 擴張動機（產能、GaN 或其他）yfinance 無法說明，需由 earnings call 或 10-K 補充。
- 季度 FCF 波動：Q3 FY26 FCF $-2.8M，Q4 FY26 FCF $136.2M。

### 資產負債表（USD M，FY26 9/30 對比 FY25 9/30）
| 指標 (USD M) | FY26 | FY25 | YoY |
|---|---|---|---|
| 總資產 Total Assets | 2,322.9 | 2,103.4 | +10.4% |
| 流動資產 Current Assets | 1,325.4 | 1,205.1 | +10.0% |
| 流動負債 Current Liabilities | 522.9 | 325.1 | +60.8% |
| 現金及約當現金 Cash & equivalents | 112.0 | 112.1 | -0.1% |
| 現金及短期投資 Cash + ST investments | 792.4 | 786.0 | +0.8% |
| 總債務 Total Debt | 377.8 | 538.0 | -29.8% |
| 其中：流動債務 Current Debt | 348.0 | 167.9 | +107% |
| 股東權益 Stockholders Equity | 1,696.7 | 1,327.1 | +27.8% |
| 商譽 Goodwill | 335.7 | 336.3 | -0.2% |
| 存貨 Inventory | 284.3 | 237.8 | +19.5% |
| 應收帳款 Accounts Receivable | 209.5 | 148.6 | +41.0% |

- 淨債務（定義不一）：yfinance `Net Debt` 為 228.7（FY25 為 388.4）。若以 總債務 − 現金及短期投資 計算，為淨現金 $414.6M。兩者差異來自是否計入短期投資，本報告兩者並列。
- 流動比率 2.54x、速動比率 1.92x，短期償債能力良好。
- 負債風險：總債務的 92%（348.0 / 377.8）列於流動負債，且 FY26 非流動負債僅 $103.3M。這表示多數債務將於 12 個月內到期或需再融資。yfinance 未提供票據條款（到期日、利率、是否為可轉債），標記為 DATA_UNAVAILABLE，需進一步確認。
- D/E：yfinance debtToEquity 為 26.1%，自算總債務 / 股東權益為 22.3%。
- 利息保障倍數：營業利益 / 利息費用 = 305.5 / 6.3 ≈ 48x，償債壓力低。
- 應收週轉：DSO 約 58 天（FY25 約 56 天），穩定。存貨天數約 186 天（FY25 約 198 天），略改善但仍偏高。

## Capital allocation & insider signal

### 資本配置（USD M）
| 指標 (USD M) | FY23 | FY24 | FY25 | FY26 |
|---|---|---|---|---|
| 買回 Repurchase of stock | 32.6 | 14.2 | 43.1 | 56.9 |
| 償還債務 Debt repayment | 122.0 | 1.4 | 1.3 | 163.8 |
| 發行債務 Debt issuance | 0 | 0 | 115.4 | 0 |
| 股利 Dividend | 無（dividendYield 0.0） | | | |

- FY26 買回 $56.9M 約占 FCF 的 26%；償還債務 $163.8M 約占 FCF 的 74%。
- 稀釋：FY26 稀釋股數 77.7M，較 FY25 74.0M 增加 +5.1%。SBC $87.8M（營收 6.6%）已超過買回金額，買回實際上僅抵銷部分稀釋。
- 股利：不配息，dividend coverage 不適用。

### 內部人交易（過去 6 個月，2026-05-22 至 2026-11-22）
| 日期 | 內部人 | 職位 | 股數 | 金額 (USD M) | 類型 |
|---|---|---|---|---|---|
| 2026-05-29 | Stephen G. Daly | CEO | 15,828 | 5.79 | 公開市場賣出 |
| 2026-06-25 | Donghyun Hwang | SVP Global Sales | 2,620 | 1.01 | 公開市場賣出 |
| 2026-08-17 | John F. Kober III | CFO | 7,389 | 2.41 | 公開市場賣出 |
| 2026-08-28 | Robert B. Dennehy | COO | 252 | 0.07 | 公開市場賣出 |
| 2026-10-01 | Ambra R. Roth | General Counsel | 653 | 0.20 | 公開市場賣出 |
| 2026-10-26 | John F. Kober III | CFO | 1,027 | 0.24 | 公開市場賣出 |
| 2026-11-09 | John F. Kober III | CFO | 22,009 | 4.56 | 公開市場賣出 |
| 2026-11-09 | Ambra R. Roth | General Counsel | 9,497 | 2.15 | 公開市場賣出 |
| 2026-11-12 | Ambra R. Roth | General Counsel | 552 | 0.14 | 公開市場賣出（價格需核對，見紅旗） |

- 6 個月賣出合計 59,827 股，金額 $16.56M。公開市場買進 0 筆。
- 占市值：$16.56M / 市值 $14,966.7M ≈ 0.11%。規模不大，但方向一致為淨賣出。
- 其他：董事 Bland 與 Murugesan 有 Stock Gift（0 金額，分別 700 與 1,400 股）；CEO、CFO、COO、GC、SVP 等於 2026-10 至 11 月有大量 Stock Award（Grant，金額為 0）。這些為獎勵股，不計入賣出。
- 脈絡：2025-11 至 2026-05 期間曾有 10% 以上持股者 Susan Ocampo 大量賣出（2026-02 單日最多 $80M），但不在本 6 個月窗口內。
- 持股結構：內部人持股 6.6%，機構持股 98.8%（871 家），BlackRock 13.1%（10.09M 股，QoQ +6.0%），FMR 11.9%（QoQ -13.5%），Janus Henderson 1.9%（QoQ +89%）。
- 放空：shares short 2.85M，較前月 3.40M 減少 16%，佔流通股約 3.7%，days to cover 1.8 天。

## Valuation

以 2026-11-22 cache 價 $194.91 為準。市值 $14.97B、EV $14.62B（yfinance）。

| 指標 | 數值 | 計算說明 |
|---|---|---|
| Trailing P/E (GAAP) | 45.2x | 194.91 / 4.31 |
| Trailing P/E (non-GAAP 估) | 34.8x | 194.91 / 5.60，5.60 為 4 季 yfinance Reported EPS 加總，為估算 |
| Forward P/E | 16.8x | 194.91 / forwardEps 11.59（yfinance） |
| EV/EBITDA | 39.7x | yfinance info（TTM EBITDA 368.1M） |
| EV/EBITDA (FY26 EBITDA 458.8) | 31.9x | 自算，EBITDA 採 statement 口徑 |
| EV/EBITDA (FY26 Normalized EBITDA 397.8) | 36.7x | 自算 |
| P/S (trailing) | 11.3x | yfinance，與 市值 / 營收 一致 |
| EV/Revenue | 11.0x | yfinance |
| P/FCF (FY26) | 67.6x | 市值 14,966.7 / FCF 221.4 |
| P/B | 8.8x | yfinance |

- EPS 核對：FY26 GAAP 淨利 335.3 / 稀釋股數 77.7 = 4.31，與 yfinance EPS 一致。
- 分析師：16 位，平均目標價 $327.0，最高 $450，最低 $220。現價 $194.91 低於最低目標價。recommendationKey 為 none。
- 股價位置：52 週區間 $158.02–$418.90，現價位於區間低段，距歷史高點 -53.5%。MA50 $262.54、MA200 $283.63，現價均在兩線之下。
- Beta 1.83，波動性高。
- 與板塊比較：yfinance 未提供板塊中位數。下表「Sector median (estimate)」為分析師估計值，非工具輸出，供參考。

## Key catalysts
- **下次財報**：2027-02-04（yfinance 日期，EPS 預估 2.25）。與 Q4 FY26 實際 2.09 相比，預估增幅約 +7.7%。
- **財報歷史**：自 2021 年起，yfinance 所列 24 個已公布季度中有 22 季 EPS 超出預估（2024 年 8 月與 11 月為小幅不及）。最近四季 surprise 依時間序為 +2.2%（2026-02）、+1.6%（2026-05）、+3.9%（2026-08）、+4.5%（2026-11）。
- **獲利動能**：Q4 FY26 營業利益率 31.6%，為 5 季來最高。毛利率連續四季上升（55.9% → 59.9%）。
- **Capex 擴張**：FY26 capex 大增，後續能否轉化為營收為重要觀察點。
- **Forward EPS 跳升**：forwardEps 11.59 相對 FY26 non-GAAP 估算 5.60，隱含 FY27 獲利接近翻倍。此預期的兌現度為最主要的估值風險。
- **負債到期**：流動債務 $348.0M 的償還或再融資動向。
- **最近股價走勢**：2026-11-22 單日 -7.57%（$218.55 → $194.91），原因未能由工具確認，WebSearch 於本次工作階段不可用，DATA_UNAVAILABLE。
- **Guidance**：FY27 營收或毛利率指引文字 DATA_UNAVAILABLE（yfinance 未提供，本次無新聞搜尋工具）。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 Revenue (USD M) | 1,327.6 (FY26) | +37.3% | 約 +8-12%（估計） | 優於 |
| 毛利率 Gross margin | 58.0% | +3.3pp | 約 55%（估計） | 優於 |
| 營業利益率 Operating margin | 23.0% | +9.6pp | 約 20%（估計） | 優於 |
| 淨利率 Net margin (GAAP) | 25.3% | +30.9pp（由負轉正） | 約 15%（估計） | 優於（含 unusual items） |
| 淨利率 Net margin (Normalized) | 21.3% | +12.0pp | 約 15%（估計） | 優於 |
| ROE | 22.2% | 由負轉正 | 約 12-15%（估計） | 優於 |
| ROIC（自算） | 13.6% | n/a | 約 10%（估計） | 優於 |
| FCF margin | 16.7% | +0.9pp | 約 15-20%（估計） | 持平 |
| FCF / NI (GAAP) | 0.66 | n/a | 約 0.9（估計） | 劣於（低於 0.9 門檻） |
| OCF / NI (GAAP) | 1.07 | n/a | 約 1.0（估計） | 持平 |
| Capex / 營收 | 10.2% | +1.7pp | 約 5-8%（估計） | 劣於（擴張期） |
| 流動比率 Current ratio | 2.54x | n/a | 約 2.5-3.0x（估計） | 持平 |
| 現金及短期投資 (USD M) | 792.4 | +0.8% | n/a | 中性 |
| 總債務 Total debt (USD M) | 377.8 | -29.8% | n/a | 優於（去槓桿），但 92% 為流動 |
| 淨債務 (yfinance, USD M) | 228.7 | -41.1% | n/a | 優於 |
| 淨現金（總債務 − 現金及短期投資, USD M） | 414.6 | n/a | n/a | 優於 |
| D/E（自算） | 22.3% | n/a | 約 30%（估計） | 優於 |
| 利息保障倍數（營業利益/利息） | 約 48x | n/a | 約 10x（估計） | 優於 |
| 稀釋股數 Diluted shares (M) | 77.7 | +5.1% | 約 1-2%（估計） | 劣於 |
| SBC / 營收 | 6.6% | -1.6pp | 約 4-6%（估計） | 劣於 |
| 股利殖利率 | 0.0% | n/a | 約 1%（估計） | 中性（不配息） |
| 內部人 6 個月淨買賣（USD M） | -16.56（純賣出） | n/a | n/a | 劣於（方向性賣出） |
| Trailing P/E (GAAP) | 45.2x | n/a | 約 35x（估計） | 劣於 |
| Trailing P/E (non-GAAP 估) | 34.8x | n/a | 約 35x（估計） | 持平 |
| Forward P/E | 16.8x | n/a | 約 25x（估計） | 優於 |
| EV/EBITDA (yfinance) | 39.7x | n/a | 約 20x（估計） | 劣於 |
| P/FCF | 67.6x | n/a | 約 30x（估計） | 劣於 |
| P/S (trailing) | 11.3x | n/a | 約 6x（估計） | 劣於 |
| 分析師均價 vs 現價 | 目標 $327 vs 現價 $194.91 | n/a | n/a | 中性（上行空間約 +68%，分析師目標仍具參考性） |
| 52 週位置 | 現價 距 52W 高 -53.5% | n/a | n/a | 中性 |

## Red flags
- **FCF 轉換率偏低**：FY26 FCF/NI 為 0.66，低於 0.9。資本支出由 FY25 $82.2M 增至 $135.7M，成長期投資推升資本開支，獲利現金化程度低於帳面。
- **債務集中於流動負債**：FY26 總債務 $377.8M 中 $348.0M 為流動債務，流動負債由 $325.1M 增至 $522.9M。yfinance 未提供票據條款，短期內需還款或再融資。
- **獲利品質波動**：FY25 GAAP 淨損 -$54.2M，FY26 GAAP 淨利 $335.3M 含 +$61.0M unusual items，且稅率僅 14%。Normalized 口徑 FY26 淨利 $282.8M 仍顯著低於 GAAP。季度 unusual items 亦大（Q3 +41.5、Q4 +19.4）。
- **估值偏高**：GAAP trailing P/E 45.2x、EV/EBITDA 39.7x、P/FCF 67.6x。估值支撐依賴 forward EPS 11.59 的兌現，而該數字相對 FY26 non-GAAP 約 5.60 隱含大幅成長。
- **內部人持續淨賣出**：6 個月內 CEO、CFO、GC、COO、SVP 合計賣出 59,827 股（$16.56M），無公開市場買進。CFO 於 2026-11-09 單筆賣出 22,009 股（$4.56M），發生在 Q4 財報（11-05）之後的窗口期。
- **稀釋持續**：稀釋股數 +5.1%，SBC $87.8M（營收 6.6%）超過買回 $56.9M，股東實質稀釋仍在。
- **股價趨勢弱**：2026-11-22 單日 -7.57%，現價低於 MA50 與 MA200，距 52 週高點 -53.5%，低於最低分析師目標價 $220。
- **資料品質問題**：
  - info 中 bid $224.01 / ask $224.29 與最新價 $194.91 不一致，判定為過時快照，本報告以 cache 最新價為準。
  - 2026-11-12 GC Roth 賣出價 $250.00，與同週其他成交價（11-09 為 $196–230）差距較大，需核對是否為 Form 4 錄入錯誤或限價單。
  - EBITDA 口徑不一：info TTM EBITDA 368.1M，statement 合計 458.8M，EV/EBITDA 結果在 31.9x 至 39.7x 之間。
  - EPS 口徑不一：Q4 FY26 GAAP diluted 1.78 與 yfinance earnings_dates 的 2.09 差異約 17%，推測為 non-GAAP 調整。
  - Net Debt 定義不一：yfinance 228.7M 與自算淨現金 414.6M 方向相反。
- **資料缺口**：
  - FY22 所有欄位為 null，無法計算 4-5 年 CAGR。
  - 業務分部營收占比：DATA_UNAVAILABLE。
  - FY27 guidance 文字：DATA_UNAVAILABLE。
  - 2026-11-22 股價下跌原因：DATA_UNAVAILABLE（無 WebSearch 工具）。
  - 板塊中位數：僅為估計值，非工具輸出。
  - 票據條款（到期日、利率、可轉債與否）：DATA_UNAVAILABLE。
  - Sector median 所有數值均為分析師估計，未經工具驗證。

FUNDAMENTALS REPORT COMPLETE
