# Fundamentals — SMCI as of 2026-10-15

資料基準：yfinance 快取（source=cache，cached_at 2026-10-14 11:43 UTC）。財報期間為 FY2026（截至 2026-06-30）年度與 FQ4 季度。最新公告為 FQ4 FY26（2026-08-11），下一次財報預估 2026-11-03（isEarningsDateEstimate=True）。無 as-of 之後的財報資料。

## Executive summary

SMCI 本輪成長與獲利改善明顯（FY26 營收 $39.06B、YoY +77.8%，淨利 $2.23B，Q4 營業利益率回升至 13.4%），資產負債表仍可控（current ratio 3.87、淨負債/EBITDA 約 0.39x），但現金流品質為主要警示：FY26 FCF 為 -$6.97B（FCF/NI = -3.1x），主要來自存貨 +$8.9B 與應收帳款 +$3.9B 的營運資金吸收，同時以債務與股權（含 $4.2B 特別股）融資。估值倍數低於 DELL/HPE/2317.TW/2382.TW 四家同業中位數（trailing P/E 11.98x vs 24.7x；forward P/E 7.34x vs 12.6x），但折價反映毛利率僅 10.8%、現金燃燒、存貨風險與治理風險評分 10/10，估值便宜需以現金流轉正作為前提來驗證。

## Revenue & profitability

**營收成長**：FY23 $7.12B → FY24 $14.99B（+110.4%）→ FY25 $21.97B（+46.6%）→ FY26 $39.06B（+77.8%）。3 年 CAGR（FY23–FY26）約 76.3%，工具僅提供 4 年資料，5 年 CAGR 為 DATA_UNAVAILABLE。季度來看 FQ1 FY26 $5.02B → FQ2 $12.68B → FQ3 $10.24B → FQ4 $11.12B（FQ4 YoY 對 FQ4 FY25 $5.76B 約 +93%），季度間波動大，FQ2 高點後 FQ3 回落、FQ4 再回升。

**利潤率趨勢**（以 yfinance 科目計算）：

| 年度 | 毛利率 | 營業利益率 | 淨利率 |
|---|---|---|---|
| FY23 | 18.0% | 10.7% | 9.0% |
| FY24 | 13.8% | 8.1% | 7.7% |
| FY25 | 11.1% | 5.7% | 4.8% |
| FY26 | 10.8% | 7.1% | 5.7% |

- 毛利率自 FY23 的 18.0% 持續下滑至 FY26 的 10.8%，是結構性的低毛利 AI server 組合的表現。FQ4 FY26 單季毛利率回升至 17.5%（FQ3 為 9.9%），但僅一季，需要後續季度確認是否可持續。
- 營業利益率 FY26 為 7.1%（FY25 5.7%），主要來自規模效應與 OpEx 占比下降（FY26 OpEx $1.46B，占營收 3.7%，FY25 為 5.4%）。研發費用 FY26 $771M，占營收 2.0%，較 FY23 的 4.3% 持續下降。
- 淨利 FY26 $2.23B；3 年 CAGR 約 51.6%。Diluted EPS FY26 $3.26（FY23 $1.14），但稀釋股數 697.3M 較 FY23 的 559.7M 增加 24.6%，EPS 成長幅度（FY23–FY26 CAGR 約 41.8%）低於淨利 CAGR（約 51.6%），股數稀釋已吃掉部分獲利成長。
- **品質提醒**：FY26 淨利中，FQ4 單季淨利 $1.14B 占全年普通股淨利 $2.20B 約 52%，獲利集中於最後一季。
- ROE（yfinance）21.5%，與 FY26 淨利 / 平均股東權益（$6.30B 與 $14.48B 平均 $10.39B）計算一致；FY25 同口徑約 17.9%。
- ROIC（自算：營業利益 × (1 - 所得稅率)，除以平均 invested capital）：FY24 約 23.3%、FY25 約 11.7%、FY26 約 14.8%。FY26 ROIC 回升但仍低於 FY24 水準，資本投入快速增加（invested capital FY26 $18.97B，FY25 $11.06B）。

**分部 / 產品組合**：yfinance 未提供分部營收，longBusinessSummary 僅描述產品線（液冷與氣冷 AI server、SuperBlade/BigTwin 等 multi-node 系統、SuperStorage、embedded 系統、workstation 與網通設備），分部營收占比為 DATA_UNAVAILABLE。

**指引（guidance）**：工具未提供管理層指引，為 DATA_UNAVAILABLE。

## Cashflow & balance sheet

**現金流品質（FCF 與 FCF/NI）**：

| 年度 | OCF | Capex | FCF | FCF margin | FCF/NI |
|---|---|---|---|---|---|
| FY23 | $663.6M | $36.8M | $626.8M | 8.8% | 0.98x |
| FY24 | -$2,486.0M | $124.3M | -$2,610.3M | -17.4% | -2.26x |
| FY25 | $1,659.5M | $127.2M | $1,532.3M | 7.0% | 1.46x |
| FY26 | -$6,809.9M | $162.0M | -$6,971.9M | -17.8% | -3.13x |

- FY26 OCF 為負主要來自營運資金：存貨變動 -$8,876.7M、應收帳款變動 -$3,921.9M，應付與應計費用變動 +$1,583.0M 僅部分抵消。
- 季度：FQ1 FY26 FCF -$950M、FQ2 -$45M、FQ3 -$6,696M、FQ4 +$719M（OCF +$747M）。FQ4 出現正 FCF，但單季不足以判斷趨勢。
- FCF/NI 遠低於 0.9 的健康門檻。
- 工具內 info.freeCashflow 為 -$8,248.8M，與 cash flow statement 計算的 FY26 FCF -$6,971.9M 不一致（差約 $1.28B），本報告以報表計算值為準，此差異列為資料品質問題。

**資產負債表（2026-06-30）**：

- 現金及約當現金 $7.52B（FY25 $5.17B，YoY +45.5%）。
- 總負債 / 有息債務：total debt $8.76B（長期 $6.68B + 流動 $2.08B），FY25 為 $4.78B（YoY +83%）。Interest expense FY26 $194.6M（FY25 $59.6M，+226%），FQ4 單季 $79.8M，季度趨勢 $22M → $25M → $25M → $65M → $80M，利息支出快速上升。
- 淨負債（yfinance）$1.20B；FY25 為淨現金約 $0.39B（自算：$4.78B 負債 - $5.17B 現金）。淨負債 / 正規化 EBITDA（$3.07B）= 0.39x。
- 注意：info.totalDebt 為 $9.26B，與 balance_sheet 的 total debt $8.76B 不一致，列為資料品質問題。
- Current ratio 3.87（FY25 5.25）。流動資產中存貨占 46.5%，剔除存貨的 quick ratio 約 2.07（info quickRatio 1.93）。
- 負債 / 股東權益：total debt / equity = 60.5%（自算，FY25 為 75.8%）；info debtToEquity 為 63.95%。股東權益 $14.48B 中含 $4.23B 特別股（preferred stock），FY25 為 0。普通股權益（tangible book value）$10.25B。
- 存貨 $12.90B（FY25 $4.68B，YoY +176%），其中 finished goods $10.28B（占存貨約 80%），WIP $1.68B，raw materials $0.94B。
- 應收帳款 $6.13B（FY25 $2.20B，YoY +178%）。
- 營運週期（自算，以 FY COGS 為基礎）：DSO 約 57 天（FY25 約 37 天）、DIO 約 135 天（FY25 約 87 天）、DPO（僅應付帳款）約 24 天（FY25 約 24 天），現金循環週期約 169 天（FY25 約 100 天）。
- 投入資本 FY26 $18.97B（FY25 $11.06B）。

## Capital allocation & insider signal

**Capex**：FY23 $36.8M → FY24 $124.3M → FY25 $127.2M → FY26 $162.0M，占營收僅 0.41%（FY25 0.58%），Capex / D&A（$90.3M）約 1.8x。資本支出規模相對於營收與存貨增幅偏小，資金主要流向營運資金而非固定資產。

**股東報酬與稀釋**：

- Buyback：FY23 $150M、FY24 $0、FY25 $200M、FY26 $1.0M（實質為零）。
- Dividend：無（dividendYield 0、payoutRatio 0），dividend coverage 不適用。
- 特別股：FY26 新增 preferred stock $4.23B，相關優先股股利（declared）$13.1M，另有 preferred dividends 相關調整 $21.5M（yfinance 欄位）。
- 股權發行：FY26 Issuance of capital stock $5.64B（FY25 $0，FY24 $2.31B）。流通股數由 FY25 的 594.1M 增至 FY26 的 656.9M（+10.6%），其中 FQ4 單季由 601.4M 增至 656.9M（+9.2%）。
- 債務發行：FY26 Issuance of debt $4.47B、償還 $0.52B（淨舉債約 $3.9B），其中 FQ3 單季發行 $4.0B。債務工具明細（可轉債 vs 銀行借款）為 DATA_UNAVAILABLE。
- SBC：FY26 $412.1M（占營收 1.05%，占淨利約 18%），FY25 $314.5M。
- 持股集中度：insider 持股 12.66%，機構持股 69.6%（1,110 家機構）。13F 持股前三大為 BlackRock 7.26%、Vanguard Capital 5.53%、Vanguard Portfolio Management 5.00%。Jane Street 持股 4.38%（較前季 +551%）、Two Sigma 1.49%（+979%），機構持股變化劇烈，但 13F 不含期權與避險部位，無法判斷方向性。
- 空頭：Shares short 87.36M，占浮動股數（557.7M）14.8%；以 10 日均量 31.0M 計，回補天數約 2.8 天。

**Insider 交易（近 6 個月，2026-04-15 至 2026-10-14）**：

- 期間內共 35 筆紀錄。唯一一筆明確的公開市場賣出為 2026-09-04，Liu Liang Chiu-Chu Sara（Director，>10% 股東）與 Charles Liang（間接持有）各列一筆，同一筆交易共 200,000 股，價格區間 $36.60–$40.00，金額約 $7.72M。去除重複列示後，6 個月內賣出金額約 $7.7M，占市值 $25.67B 約 0.03%。
- 期間內公開市場買進：0 筆。
- 其餘紀錄多為無價格、無金額的異動（2026-05-08、06-17、06-30、07-01、08-10、08-17 等），可能屬於股權獎勵、歸屬或轉換，但工具未明確交易性質，此部分 DATA_UNAVAILABLE。另有 2026-05-26 的 340,000 股 stock gift（$0）。
- 近兩年 sale 紀錄加總約 2.27M 股、約 $105M，但包含 Liu/Liang 重複列示，未去重。
- 整體解讀：6 個月內 insider 以小額賣出與股權異動為主，無內部人買進，賣出規模相對市值可忽略。

## Valuation

**價格與倍數（as-of 快取價 $39.07，前收 $39.98）**：

- 市值 $25.67B；EV $31.61B（info）；52 週區間 $19.48–$56.60（距高點 -31%，52 週變動 -27.6%）；20 日年化波動 58.4%；beta 2.01。
- Trailing P/E 11.98x（trailing EPS $3.26）；Forward P/E 7.34x（forward EPS $5.33）。
- EV/EBITDA 11.19x（info EBITDA $2.82B）；以正規化 EBITDA $3.07B 計約 10.3x。
- P/S 0.66x（trailing），EV/Revenue 0.81x。
- P/FCF 不適用（FCF 為負）。
- P/B 2.50x（BVPS $15.61，普通股權益口徑）。PEG 0.91。

**同業比較**（yfinance 快取，DELL/HPE/2317.TW/2382.TW 四家中位數，為工具實算，非外部估計）：

| 指標 | SMCI | DELL | HPE | 2317.TW | 2382.TW | 四家中位數 |
|---|---|---|---|---|---|---|
| Trailing P/E | 11.98x | 33.28x | 35.47x | 16.15x | 14.64x | 24.7x |
| Forward P/E | 7.34x | 19.13x | 14.61x | 10.51x | 10.10x | 12.6x |
| EV/EBITDA | 11.19x | 21.87x | 15.31x | 8.11x | 12.23x | 13.8x |
| P/S | 0.66x | 2.41x | 2.18x | 0.37x | 0.44x | 1.30x |

- 2317.TW、2382.TW 的財務覆蓋較薄，本表僅使用工具可取得之倍數欄位，其餘欄位為 n/a。
- SMCI 在四項倍數上皆低於中位數，但同業毛利率差異極大（DELL 19.9%、HPE 36.6%，SMCI 10.8%），且 FCF 與同業相反（DELL FCF +$6.03B、HPE +$4.74B，SMCI -$6.97B）。以 EV/EBITDA 或 P/E 直接比較，並未調整毛利率、現金轉換與存貨風險。

**分析師共識（15 位）**：目標均價 $42.27（median $43.00，高 $60.00、低 $15.00），相對現價約 +8.2%；recommendationMean 2.94（介於 hold 區間）。此為外部共識，非本報告建議。

## Key catalysts

- **下一次財報**：預估 2026-11-03（isEarningsDateEstimate=True），對應 FQ1 FY27（2026-09 季）。EPS 共識 $1.04。
- **近四季 EPS 表現**：FQ1 FY26（2025-11-04 公告）EPS $0.35 vs 預估 $0.39（-10.1%）；FQ2（2026-02-03）$0.69 vs $0.49（+41.4%）；FQ3（2026-05-05）$0.84 vs $0.62（+34.5%）；FQ4（2026-08-11）$1.70 vs $0.96（+77.6%）。注意 yfinance 季度財報中 FQ4 diluted EPS 為 $1.62，earnings_dates 的 Reported EPS 為 $1.70，兩者口徑不同，列為資料品質提醒。
- **毛利率回升是否延續**：FQ4 毛利率 17.5% vs FQ3 9.9%，為下一季最關鍵的驗證點。
- **存貨與現金流**：存貨 $12.9B 能否在 FQ1 FY27 開始去化、FQ4 正 FCF 能否延續，是現金流轉正的主要觀察指標。
- **債務與股權**：利息支出季度已升至約 $80M，特別股與可能的再融資條件為 DATA_UNAVAILABLE。
- **管理層指引**：DATA_UNAVAILABLE。
- **分部營收變化**：DATA_UNAVAILABLE。

## Metrics table

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 股價 / 市值 | $39.07 / $25.67B | 52 週 -27.6% | n/a | 中性 |
| 營收（FY26） | $39.06B | +77.8%（3Y CAGR +76.3%） | DELL +57.7%、HPE +33.7% | 強 |
| 毛利率（FY26） | 10.8% | -0.2pp（FY23 18.0%） | DELL 19.9%、HPE 36.6% | 弱 |
| 營業利益率（FY26） | 7.1%（FQ4 13.4%） | +1.4pp | DELL 12.0%、HPE 12.6%（info） | 改善中 |
| 淨利率（FY26） | 5.7% | +0.9pp | DELL 7.5%、HPE 6.7%（info） | 中性 |
| Diluted EPS（FY26） | $3.26 | +94%（FY25 $1.68） | n/a | 強（含稀釋） |
| ROE | 21.5% | +3.6pp（FY25 約 17.9%，自算） | n/a | 改善 |
| ROIC（自算） | 14.8% | +3.1pp（FY25 約 11.7%） | n/a | 中性 |
| FCF（FY26） | -$6.97B | 由 +$1.53B 轉負 | DELL +$6.03B、HPE +$4.74B（info TTM） | 警示 |
| FCF margin | -17.8% | 由 +7.0% 轉負 | n/a | 警示 |
| FCF / NI | -3.13x | 由 1.46x 轉負 | 目標 >0.9 | 警示 |
| Current ratio | 3.87 | 由 5.25 下降 | n/a | 健康 |
| Quick ratio | 1.93（info） | n/a | n/a | 健康 |
| Net debt（yfinance） | $1.20B | 由淨現金 $0.39B 轉為淨負債（自算） | n/a | 警示 |
| 淨負債 / 正規化 EBITDA | 0.39x | 由淨現金轉負債 | n/a | 可控 |
| Total debt / equity | 60.5%（自算）/ 63.95%（info） | FY25 75.8%（自算） | n/a | 中性 |
| Interest expense | $194.6M（FQ4 $79.8M） | +226% | n/a | 警示 |
| Inventory | $12.90B | +176% | n/a | 警示 |
| DSO / DIO / 現金循環 | 57 / 135 / 169 天（自算） | FY25 37 / 87 / 100 天 | n/a | 警示 |
| Capex（占營收） | $162M（0.41%） | +27%（FY25 $127M） | n/a | 中性 |
| SBC（占營收） | $412M（1.05%） | +31% | n/a | 中性 |
| 股票回購 | $1.0M | FY25 $200M | n/a | 無 |
| 股權發行 | $5.64B | FY25 $0 | n/a | 警示（稀釋） |
| 特別股 | $4.23B | FY25 $0 | n/a | 警示 |
| 流通股數 | 656.9M | +10.6% | n/a | 警示（稀釋） |
| Dividend / payout | 無 | n/a | n/a | 不適用 |
| Insider 6 個月淨買賣 | 買入 0、賣出約 $7.7M（去重） | n/a | n/a | 中性 |
| Insider 持股 / 機構持股 | 12.66% / 69.6% | n/a | n/a | 中性 |
| Short % of float | 14.8% | n/a | n/a | 警示 |
| Trailing P/E | 11.98x | n/a | 24.7x（四家中位數） | 偏低 |
| Forward P/E | 7.34x | n/a | 12.6x（四家中位數） | 偏低 |
| EV/EBITDA | 11.19x | n/a | 13.8x（四家中位數） | 偏低 |
| P/S（trailing） | 0.66x | n/a | 1.30x（四家中位數） | 偏低 |
| P/FCF | n/a（FCF 為負） | n/a | n/a | 不適用 |
| P/B | 2.50x | n/a | n/a | 中性 |
| PEG | 0.91 | n/a | n/a | 偏低 |
| 分析師目標均價 | $42.27（+8.2%） | n/a | n/a | 中性 |
| Beta / 20 日年化波動 | 2.01 / 58.4% | n/a | n/a | 高 |
| 治理風險評分（overallRisk / auditRisk） | 10 / 10（yfinance） | n/a | n/a | 警示 |
| 分部營收 / 管理層指引 | DATA_UNAVAILABLE | n/a | n/a | n/a |

## Red flags

- **現金流嚴重為負**：FY26 FCF -$6.97B，FCF/NI -3.1x，OCF 為負主因存貨與應收帳款大幅增加。
- **存貨風險**：存貨 $12.9B（YoY +176%），其中 finished goods 約 80%，DIO 約 135 天。若需求或價格下修，存貨減值與毛利率下行的風險升高（自算，工具未提供存貨跌價準備明細）。
- **低毛利結構**：FY26 毛利率 10.8%，較 FY23 下降 7.2pp，同業 DELL 19.9%、HPE 36.6%。FQ4 單季 17.5% 尚未證明可持續。
- **舉債與利息快速上升**：total debt $8.76B（YoY +83%），FQ3 單季新增債務 $4.0B，利息支出 FY26 +226%，季度利息已升至約 $80M。
- **股權稀釋與特別股**：FY26 股權發行 $5.64B、新增特別股 $4.23B、流通股數 +10.6%；稀釋股數較 FY23 增加 24.6%。
- **獲利集中於單季**：FQ4 淨利占全年約 52%，FY26 淨利與現金流方向相反。
- **治理風險評分 10/10**：yfinance 的 overallRisk 與 auditRisk 皆為 10（最高級），工具未提供具體事件內容，需由 news 或 SEC 文件進一步核實。
- **空頭部位高**：short % of float 14.8%，beta 2.01，20 日年化波動 58%。
- **資料品質問題**：(1) info.totalDebt $9.26B 與 balance_sheet total debt $8.76B 不一致；(2) info.freeCashflow -$8.25B 與 cash flow statement FCF -$6.97B 不一致；(3) FQ4 EPS $1.62（quarterly_fin）與 $1.70（earnings_dates）口徑不同；(4) FQ3 2025-03 季度資料為 n/a；(5) info 的 nextEarningsDate 為 None，下一財報日期以 earnings_dates 的 2026-11-03（估計）為準；(6) 同業 2317.TW、2382.TW 的財務覆蓋較薄。
- **內部人無買進**：近 6 個月無公開市場買進，賣出規模雖小但方向一致偏向賣出（一筆 $7.7M）。

FUNDAMENTALS REPORT COMPLETE
