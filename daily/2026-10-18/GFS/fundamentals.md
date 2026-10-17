# Fundamentals — GFS (GlobalFoundries Inc.) as of 2026-10-18

## Executive summary
GFS 財務體質穩健: TTM 淨現金約 $0.68B (totalCash 2,357M − totalDebt 1,678M)、流動比率 2.48、FY2025 FCF $1,009M。但營收成長停滯，2022–2025 營收 CAGR −5.7%、FY2025 YoY 僅 +0.6%，GAAP 獲利率中段 (TTM 淨利率 10.3%)。估值上 forward P/E 17.8x、EV/EBITDA 12.6x 相對半導體 foundry 估計中位數偏低，但股價已由 6 月下旬約 $87 (內部人賣出成交價區間) 回落約 46%，且 TTM GAAP P/E 高達 36.5x；內部人近 6 個月僅出現定期性小額賣出、無公開市場買進。整體結論: 財務健全、估值具吸引力，但成長動能與盈餘品質 (GAAP vs 非 GAAP 落差) 需持續觀察。本報告不含交易建議。

**資料時點說明**: 分析基準日 2026-10-18；工具回傳來源為 repo 快取 (`source: cache`, cached_at 2026-10-17T10:33 UTC)，最新報價為 2026-10-16 收盤 (regularMarketTime 2026-10-16 20:00 UTC)，即 as-of 日前一交易日資料。財報最新已到 2026-Q2 (2026-06-30)，無 post-date 財報資料。

## Revenue & profitability

**營收趨勢 (年度, 單位 $M)**
| 年度 | 營收 | YoY | 毛利率 | 營業利益率 | 淨利率 |
|---|---|---|---|---|---|
| FY2022 | 8,108 | — | 27.6% | 15.6% | 17.9% |
| FY2023 | 7,392 | −8.8% | 28.4% | 16.2% | 13.8% |
| FY2024 | 6,750 | −8.7% | 24.5% | 10.8% | −3.9% |
| FY2025 | 6,791 | +0.6% | 24.9% | 11.7% | 13.0% |

- 2022–2025 3 年營收 CAGR: **−5.7%**。2021 年資料為 null，無法計算 4–5 年 CAGR (DATA_UNAVAILABLE)。
- FY2024 淨利為 −$265M，主因 Impairment of Capital Assets $935M (special income charges −$942M)；FY2025 淨利 $885M 含 Total Unusual Items +$76M，且 FY2025 所得稅費用僅 $23M (有效稅率約 2.5%)，淨利品質需打折看待。
- 最近四季 (quarterly_fin): 2025-06 營收 1,688 → 2025-09 1,688 → 2025-12 1,830 → 2026-03 1,634 → 2026-06 1,786。2026-Q2 YoY **+5.8%** (1,786 vs 1,688)，為近期較明確的回升訊號。
- TTM (2025-Q3 至 2026-Q2) 營收 $6,938M，與 info.totalRevenue 一致。TTM 毛利 $1,883M，**毛利率 27.1%**；TTM 營業利益率 (GAAP 季度加總) **11.6%**；TTM 淨利 $716M，**淨利率 10.3%**，與 info.profitMargins (10.32%) 一致。
- **注意**: info.operatingMargins 為 9.74%，與由季度 GAAP 營業利益加總算出的 11.6% 不一致，可能為 Yahoo 口徑差異，本報告以季度 GAAP 數字為準並標記。

**業務組合**: longBusinessSummary 僅描述為「主流 wafer fabrication 服務與技術」，產品包含 microprocessors、mobile application processors、RF modems、MCU、PMU 等；另有量子技術解決方案 (與 Xanadu 合作、DOE Genesis Mission AI 合作)。工具未提供分部營收 (segment revenue)，分部占比為 DATA_UNAVAILABLE。

**獲利效率**
- ROE (info): **6.2%**；以 FY2025 淨利 / 期末股東權益 $11,928M 計算為 7.4%。
- ROIC 估算 (FY2025): EBIT $797M × (1 − 2.5%) ≈ NOPAT $777M。以工具回傳的 invested capital $13,079M 計算 ROIC 約 **5.9%**；若以總負債 + 權益 − 現金與短投 (= $10,532M) 計算則約 **7.4%**。兩種口徑差異大，本報告採較保守的 5.9%。
- ROA (info): 3.0%。
- 研發費用 FY2025 $518M (7.6% of revenue)，R&D 持續高於 FY2023 的 $428M。

## Cashflow & balance sheet

**現金流 (年度, $M)**
| 年度 | OCF | Capex | FCF (OCF−Capex) | FCF 利潤率 | FCF/NI | Capex/Revenue | Capex/D&A |
|---|---|---|---|---|---|---|---|
| FY2022 | 2,624 | 3,059 | −435 | −5.4% | 負值 | 37.7% | 1.88x |
| FY2023 | 2,125 | 1,804 | 321 | 4.3% | 0.31 | 24.4% | 1.24x |
| FY2024 | 1,722 | 625 | 1,097 | 16.3% | n/m (NI 為負) | 9.3% | 0.40x |
| FY2025 | 1,731 | 722 | 1,009 | 14.9% | **1.14** | 10.6% | 0.55x |

- TTM FCF (info.freeCashflow) **$758M**，FCF 利潤率 10.9%；TTM OCF $1,916M。TTM FCF 低於 FY2025 的 $1,009M，表示 2026 年上半年 capex 回升，需留意。
- FCF/NI 2025 為 1.14 (>0.9 健康)，但該年淨利含一次性稅務與非營業項目，且 FY2024 淨利為負，FCF/NI 比率波動大，僅供參考。
- **Red flag**: FY2024 與 FY2025 capex 均低於折舊攤銷 (D&A 1,568 / 1,314)，Net PPE 由 FY2023 的 $10,164M 降至 FY2025 的 $7,792M。FCF 改善有相當部分來自 capex 收縮 (underinvestment)，非純粹營運效率提升。
- SBC FY2025 $200M (2.9% of revenue)。

**資產負債表 (FY2025-12-31, $M)**
- 現金及約當現金 $1,809M；加計其他短期投資 $1,294M，現金與短投合計 **$3,103M**。
- 總負債 (含資本租賃) **$1,707M**: 長期負債 $1,065M、流動債務 $86M、資本租賃 $556M。
- **淨債務 (FY2025 計算)**: 1,707 − 3,103 = **−$1,396M (淨現金)**。以 info 最新季 (2026-Q2) 計算: totalDebt 1,678 − totalCash 2,357 = **−$679M (淨現金)**。Yahoo 年度 Net Debt 欄位 FY2025 為 n/a。
- 流動比率 (info) **2.48**，速動比率 1.73；FY2025 計算流動比率 2.62 (6,205 / 2,368)。
- 負債/權益: 14.1% (info debtToEquity 14.13，Yahoo 以百分比表示)；FY2025 計算 14.3%。
- 股東權益 $11,928M (FY2025)，較 FY2024 的 $10,776M 增加。Goodwill + 無形資產由 $660M 增至 **$1,368M**，因 FY2025 併購支出 $682M (Purchase of Business)，商譽由 $75M 增至 $407M。
- 每股淨值 (book value) $21.54；P/B 2.17x。
- 有形帳面價值 (Tangible Book Value) $10,560M。
- 利息收入 $159M 大於利息支出 $50M (FY2025)，利息淨收益為正。

**短期流動性**: 流動性充足，無即期償債壓力。FY2025 長期負債 $1,065M 為主要債務來源。到期結構細節 (debt maturity schedule) 工具未提供，為 DATA_UNAVAILABLE。

## Capital allocation & insider signal

**資本配置**
- **Capex**: 2022 高峰 $3,059M → 2025 $722M，降幅約 76%，與 Net PPE 下降同步。目前以較低資本支出運行，未見擴產循環訊號。
- **股票回購**: FY2024 $200M，FY2025 僅 $5M，FY2023 為 0。
- **股利**: info.dividendRate 0.48 (前瞻年化)，殖利率 **1.03%**；trailingAnnualDividendRate 0.12 (TTM 僅一次配息)。最近除息日 2026-09-23，發放日 2026-10-09。現金流量表中未見 Dividends Paid 欄位，實際股利現金流為 DATA_UNAVAILABLE。以前瞻股利 $0.48 × 557.4M 股估算年股利約 $268M，TTM FCF $758M 約可覆蓋 **2.8x**。
- **併購**: FY2025 併購支出 $682M，FY2024 $69M。
- 支付率 (payoutRatio, info): 9.4%；但以 TTM GAAP EPS $1.28 計算為 37.5% (0.48 / 1.28)，口徑差異需注意。

**股權結構**
- 股本 557.4M 股；流通股 (floatShares) 148.4M，**自由流通比率約 26.6%**。
- Mubadala Investment Co PJSC 持股 **72.8%** (399.6M 股)，2026-06-30 季報顯示較前一季減持 5.55%。大股東持續減持為需追蹤的供給面因素。
- 機構持股數 591 家；FMR 持股 12.7% (季增 +9.0%)。Yahoo heldPercentInstitutions 為 100.4%，超過 100%，為資料口徑異常，不可直接採用。

**做空**: sharesShort 7.00M 股 (2026-09-30)，較上月 6.41M 增加 9.2%；shortRatio 1.79 天。info.shortPercentOfFloat 為 13.57%，但以 sharesShort / floatShares 計算為 4.7%，兩者不一致，已標記，以 shares short / sharesOutstanding = 1.26% 為較保守參考。

**內部人交易 (近 6 個月, 2026-03-18 至 2026-09-28)**
- 共 58 筆紀錄。**公開市場買進: 0 筆**。
- 賣出 (Sale) 合計約 **$3.74M**，占市值 26.0B 約 **0.014%**。
- 主要賣出人:
  - Samak L. Azar (CLO): 約 40 筆，每次 335–500 股，頻率約每週一次，屬典型定期小額賣出模式，疑似 10b5-1 計畫 (工具未標示計畫旗標，為推論)。
  - Michael James Hogan (Officer): 多筆 100–2,800 股賣出，並伴隨 Stock Gift 紀錄。
  - Pradheepa Raman (Officer): 2026-08-18 賣出 6,760 股 ($345.6K, @$51.12)，2026-09-28 賣出 2,145 股 ($104.7K, @$48.83)。
  - Vicari Samuel (Officer): 2026-05-11 賣出 8,692 股 ($657K, @$75.62)，為期間單筆最大金額。
  - Dorchak Glenda Mary (Director): 2026-04-20 與 2026-07-20 各賣出 4,000 股。
- 董事 (Director) 於 2026-07-28 獲得限制性股票授予 (Stock Award)，無金額。
- **結論**: 無內部人買進訊號；賣出為常態化小額行為，金額相對市值可忽略，但同期股價由約 $87 跌至 $47，賣出價格區間 $43–$87 不等。

## Valuation

| 指標 | 數值 | 計算/來源 | 備註 |
|---|---|---|---|
| 股價 | $46.68 | regularMarketPrice (2026-10-16 收盤) | 日內 −4.27% |
| 市值 | $26.02B | info.marketCap | 557.4M 股 |
| EV | $24.99B | info.enterpriseValue | |
| Trailing P/E (GAAP) | 36.5x | info.trailingPE; 46.68 / 1.28 | 含一次性與稅務項目 |
| Forward P/E | 17.8x | info.forwardPE; 46.68 / 2.63 | 分析師前瞻 EPS |
| FY2026 P/E (consensus) | 23.9x | 46.68 / 1.955 (epsCurrentYear) | |
| PEG | 0.73 | info.pegRatio | |
| EV/EBITDA (TTM) | 12.6x | info.enterpriseToEbitda (EBITDA 1,981M) | |
| EV/Revenue (TTM) | 3.6x | info.enterpriseToRevenue | |
| P/S (TTM) | 3.75x | info.priceToSalesTrailing12Months | |
| P/FCF (FY2025) | 25.8x | 26,020 / 1,009 | |
| P/FCF (TTM) | 34.3x | 26,020 / 758 | |
| P/B | 2.17x | info.priceToBook | |

- **分析師共識**: 22 位分析師，recommendationMean 2.04 (buy)，key = buy。近 4 個月 rec_summary 最新為 Strong Buy 3 / Buy 10 / Hold 9 / Sell 0 / Strong Sell 1。
- **目標價**: 平均 $74.68 (+60%)、中位數 $71.00 (+52%)、最高 $140.00、最低 $51.00 (+9%)。最低目標價仍高於現價，顯示分析師對 2027 年後獲利回升有相當預期，但目標價與現價落差大，需留意估值假設的不確定性。
- **相對 sector median (估計)**: 半導體 foundry/IDM 族群 forward P/E 中位數估計約 25x，EV/EBITDA 約 15x，P/S 約 5x (以上為估計，非工具數據)。GFS 在 forward P/E、EV/EBITDA、P/S 上皆低於估計中位數，GAAP trailing P/E 則高於估計中位數，主因 GAAP 獲利基數較低。
- **價格位置**: 50 日均線 $47.68、200 日均線 $54.85，現價低於兩條均線。52 週區間 $32.02–$92.55，現價位於區間下段 (距 52 週高點 −49.6%，距 52 週低點 +45.8%)。Beta 1.765，波動性高於大盤。

## Key catalysts
- **下次財報**: 2026-11-04 (earningsTimestamp 12:30 UTC；法說會 20:00 UTC)，info.isEarningsDateEstimate = False，為確認日期。
- **EPS 預期**: Q3 2026 consensus EPS **$0.51** (earnings_dates)。上一季 (2026-Q2) 調整後 EPS $0.46，優於預期 $0.43 (+6.5%)。
- **EPS 驚喜歷史**: earnings_dates 所列 20 季 (2021-11 至 2026-08) 全部為正向驚喜；2024 年多季驚喜幅度超過 +20%，2026-Q1 為 +14.0% (0.40 vs 0.35)，2026-Q2 為 +6.5% (0.46 vs 0.43)，近兩季驚喜幅度收斂。
- **公司指引 (guidance)**: 工具未提供管理層最新營收/毛利指引，為 DATA_UNAVAILABLE。
- **策略性事件**: 與 DOE Genesis Mission (AI 科學計算) 及 Xanadu Quantum Technologies (量子晶片製造) 之合作，為 longBusinessSummary 所述，對營收貢獻尚未量化。
- **股利**: 除息已於 2026-09-23 完成，發放日 2026-10-09 已過。下一次除息需待公告。
- **股權事件**: Mubadala 持續減持、內部人定期賣出，屬供給面壓力來源。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 (TTM, $M) | 6,938 | +5.8% (2026-Q2 季) | n/a | 成長不足，但近季回升 |
| 營收 CAGR (2022–2025) | −5.7% | — | 約 +3%~+5% (估計) | 偏弱 |
| 毛利率 (TTM) | 27.1% | FY25 24.9% → TTM 27.1% | 約 35%–45% (估計) | 偏低，但改善中 |
| 營業利益率 (TTM, 季度加總) | 11.6% | FY25 11.7% | 約 15%–20% (估計) | 偏低 |
| 淨利率 (TTM) | 10.3% | FY25 13.0% | 約 12%–15% (估計) | 中性 |
| ROE | 6.2% (info) | FY25 7.4% (計算) | 約 12%–15% (估計) | 偏低 |
| ROIC (FY25) | 約 5.9%–7.4% | — | 約 10%–12% (估計) | 偏低 |
| FCF (TTM, $M) | 758 | FY25 1,009 (YoY −8%) | n/a | 下滑中 |
| FCF 利潤率 (TTM) | 10.9% | FY25 14.9% | 約 15%–20% (估計) | 中性偏弱 |
| FCF / NI (FY25) | 1.14 | n/m (FY24 NI 為負) | >0.9 為健康 | 健康，但 NI 品質需打折 |
| 淨債務 / (淨現金) (TTM, $M) | (679) | FY25 (1,396) | 約 0 至小負債 (估計) | 健康 |
| 流動比率 | 2.48 | FY25 2.62 | 約 2.0 (估計) | 健康 |
| 負債/權益 | 14.1% | FY25 14.3% | 約 30%–50% (估計) | 健康 |
| Capex / 營收 (FY25) | 10.6% | FY23 24.4% | 約 15%–25% (估計) | 偏低，留意 underinvestment |
| 股利殖利率 (前瞻) | 1.03% | — | 約 0.5%–1.0% (估計) | 中性 |
| Trailing P/E (GAAP) | 36.5x | — | 約 30x (估計) | 偏高 |
| Forward P/E | 17.8x | — | 約 25x (估計) | 偏低 |
| EV/EBITDA (TTM) | 12.6x | — | 約 15x (估計) | 偏低 |
| P/FCF (TTM) | 34.3x | — | 約 30x (估計) | 中性偏高 |
| P/S (TTM) | 3.75x | — | 約 5x (估計) | 偏低 |
| 內部人淨買賣 (6mo) | 買進 0 / 賣出 $3.74M | — | n/a | 無買進訊號，賣出金額微小 |
| 空單佔流通股 | 13.57% (info) / 4.7% (計算) | 空單股數 +9.2% MoM | n/a | 資料不一致，需追蹤 |
| 分析師目標價 (平均) | $74.68 (+60%) | — | n/a | 上行空間大 (分析師視角) |
| 52 週股價漲跌 | +31.2% | 距 52W 高 −49.6% | S&P 500 52 週 +13.7% (info.SandP52WeekChange) | 1 年報酬優於大盤，但近 3 個月大幅回落 |

## Red flags
- **成長停滯**: 2022–2025 營收 CAGR −5.7%，FY2025 僅 +0.6%；雖 2026-Q2 回升至 +5.8% YoY，但僅一季驗證。
- **盈餘品質**: FY2024 因 $935M 資產減損轉為淨虧損；FY2025 有效稅率僅 2.5%，淨利 $885M 含 $76M 非經常性收益，TTM GAAP EPS $1.28 與 forward EPS $2.63 差距大，GAAP 與調整後 EPS 口徑差異需納入判斷。
- **Capex 低於折舊**: FY2024 與 FY2025 capex 分別為 D&A 的 0.40x 與 0.55x，Net PPE 連續兩年下降 (10,164 → 8,260 → 7,792)。FCF 回升部分來自投資不足，長期產能與競爭力風險待觀察。
- **TTM FCF 下滑**: TTM FCF $758M 低於 FY2025 $1,009M (−25%)，2026 年上半年 capex 回升。
- **股價與估值**: 股價較 6 月下旬約 $87 (內部人賣出價) 回落約 46%，距 52 週高點 $92.55 為 −49.6%，現價低於 50 日與 200 日均線；Beta 1.765。
- **大股東減持與低自由流通**: Mubadala 持股 72.8%，流通股僅約 26.6%，減持壓力與流動性受限並存。
- **內部人持續賣出**: 6 個月內 0 筆買進，CLO 等高階主管定期賣出；金額雖小，但無買進訊號。
- **資料品質警示**: (1) info.operatingMargins 9.74% 與季度加總 11.6% 不一致；(2) info.shortPercentOfFloat 13.57% 與計算 4.7% 不一致；(3) info.heldPercentInstitutions 100.4% 超過 100%；(4) payoutRatio 9.4% 與 TTM EPS 計算 37.5% 不一致。以上皆以原始數字標記，未自行修正。
- **資料缺漏 (DATA_UNAVAILABLE)**: 分部營收、公司最新營收/毛利指引、債務到期結構、現金流量表中之股利支付金額、2021 年完整資料、4–5 年 CAGR。

---
工具使用說明: 原任務指定之 kinds (statements, ratings, holders) 不存在於 `pipeline/tools/yf.py`，本報告改用對應的 financials / balance_sheet / cashflow (年度)、quarterly_fin (季度)、rec_summary / recommendations (評等)、insider、major_holders / inst_holders (持股)，以及 info、earnings_dates。資料來源均為 repo 快取 (source: cache)，屬預期狀況。

FUNDAMENTALS REPORT COMPLETE
