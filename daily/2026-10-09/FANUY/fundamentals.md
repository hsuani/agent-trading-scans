# Fundamentals — FANUY (Fanuc Corp ADR) as of 2026-10-09

註: 資料來源為 pipeline/tools/yf 快取 (cached_at 2026-10-08 13:15–13:19 UTC)。價格為 regularMarketTime 對應之最新收盤 (約 2026-10-07), 非即時。財務報表原幣為 JPY (financialCurrency JPY), 報價為 USD (OTC Pink ADR)。下列 "(計算)" 標示為由 JSON 數字推算。

## Executive summary
Fanuc 財務體質極佳: 無有息負債、現金及約當現金加短期投資 ¥753.9bn、流動比率約 6.9x、FY3/2026 FCF 率 26.8%, FCF/NI 1.38。但營收 FY23 至 FY26 三年 CAGR 僅約 +0.2%, 成長停滯; 以 trailing P/E 32.9x、P/B 3.0x 計, 估值已反映相當溢價, 且 2 位分析師覆蓋、ADR 掛牌於 OTC Pink、數據有幣別混用與股數不一致等問題, 估值倍數 (尤其 EV 與 P/S) 需以本報告重算值為準。內部人資料 yfinance 回傳空值, 無法判讀內部人買賣訊號。

## Revenue & profitability
- 營收 (JPY bn, 財年截至 3/31): FY23 851.96 / FY24 795.27 / FY25 797.13 / FY26 857.83。
  - FY26 YoY +7.6% (計算); FY25 YoY +0.2%; FY24 YoY -6.7%。
  - 3 年 CAGR (FY23→FY26) +0.2% (計算)。yfinance FY22 無資料, 無法算 4-5 年 CAGR。
  - info.revenueGrowth 為 +17.7%, 應為最近一季 YoY, 但報表層無對應資料, 無法驗證。
- 分部: info.longBusinessSummary 僅列產品線 (CNC、robots、robomachine、伺服馬達、雷射等), 無分部營收數字。分部占比: n/a。
- 毛利率: FY23 38.2% / FY24 34.7% / FY25 37.0% / FY26 38.3% (計算)。info.grossMargins TTM 38.4%。
- 營業利益率: FY23 22.5% / FY24 17.8% / FY25 19.9% / FY26 21.4% (計算)。info.operatingMargins TTM 23.2%。
- 淨利率: FY23 20.0% / FY24 16.7% / FY25 18.5% / FY26 19.4% (計算)。淨利 FY26 ¥166.54bn, YoY +12.9% (計算)。
- EBITDA 利潤率 (報表): FY26 27.0% (計算, EBITDA ¥231.5bn)。
- 盈餘品質提示: FY26 稅前利益 ¥227.49bn 高於營業利益 ¥183.76bn 約 ¥43.7bn; 扣除利息收入 ¥7.54bn、其他營業外 ¥4.54bn 後, 仍有約 ¥31.6bn 無法由 JSON 欄位解釋 (計算), 推測來自投資證券相關收益, 但 yfinance 無此明細 (未驗證)。獲利有相當部分依賴非營業性收益。
- ROE: info.returnOnEquity 10.05% (TTM); 以 FY26 期末權益計算為 8.9% (計算)。
- ROIC (計算): NOPAT = EBIT ¥183.76bn × (1 − 25.5% 稅率) = ¥136.9bn; 若扣除現金後之投入資本 (權益 ¥1,864.9bn − 現金 ¥753.9bn = ¥1,111.0bn) 則 ROIC 約 12.3%; 若以全部權益為投入資本則僅 7.3%。以現金扣除法較合理, 但仍屬估算。

## Cashflow & balance sheet
現金流 (JPY bn):

| 年度 | OCF | Capex | FCF | FCF 率 | FCF/NI | Capex/D&A |
|---|---|---|---|---|---|---|
| FY23 | 99.5 | 47.1 | 52.4 | 6.2% | 0.31 | 0.96x |
| FY24 | 171.8 | 53.9 | 117.9 | 14.8% | 0.89 | 1.10x |
| FY25 | 255.3 | 40.8 | 214.5 | 26.9% | 1.45 | 0.88x |
| FY26 | 250.9 | 21.2 | 229.7 | 26.8% | 1.38 | 0.44x |

(FCF、FCF 率、FCF/NI、Capex/D&A 為計算值; FCF 與 yfinance 報表 "Free Cash Flow" 一致。)

- FCF/NI FY26 1.38, 高於 0.9 健康門檻。但 FY26 含營運資金釋放: 存貨變動 +¥27.9bn、應收/應付合計 +¥4.8bn、營運資金總變動 +¥21.5bn (JSON)。扣除營運資金變動後 FY26 FCF 約 ¥208bn, FCF/NI 約 1.25 (計算), 仍健康。
- 資本支出 FY26 ¥21.2bn, YoY −48.1% (計算), 僅為 D&A ¥47.8bn 的 0.44 倍 (計算)。在建工程由 ¥48.0bn 降至 ¥22.0bn。資本支出明顯收縮, 需留意是週期性收斂抑或長期投資不足, 資料無法判定。
- 資產負債表 (JPY bn, 2026-03-31):
  - 現金及約當現金 ¥718.07bn (FY25 ¥590.50bn, +21.6%); 含短期投資 ¥753.87bn。
  - 有息負債: info.totalDebt = 0; 資產負債表未見借款科目。淨現金約 ¥753.9bn (計算), 以隱含匯率約 151 JPY/USD 換算約 $5.0bn (計算, 匯率為由 EPS 反推之估計值)。
  - 另有可供出售投資證券 ¥223.29bn (FY25 ¥192.21bn), 屬非現金流動資產, 未計入淨現金。
  - 流動比率: 計算 6.89x (CA ¥1,237.0bn / CL ¥179.5bn); info.currentRatio 7.34 (應為最近一季)。速動比率計算 5.26x; info.quickRatio 5.41。
  - 負債權益比: 有息負債為 0; 總負債/權益 11.1% (計算)。權益/總資產 89.2% (計算)。
  - 退休金負債 ¥20.19bn, 較 FY23 ¥55.20bn 大幅下降。
  - 商譽及無形資產 ¥8.54bn, 占比低。
  - 營運效率: DSO 約 73 天 (計算), DIO 約 201 天 (計算, 以 COGS 計)。存貨 ¥292.2bn 占總資產 14%, 存貨與營收比偏高, 為營運資金重點。
  - PP&E 淨額 ¥591.4bn; yfinance 的 Gross PPE 與 Net PPE 數字相同, 無累計折舊明細, 無法評估資產老化程度。

## Capital allocation & insider signal
- 股利 (JPY bn): FY23 96.5 / FY24 90.1 / FY25 83.1 / FY26 94.5。
  - 股利覆蓋: FCF/股利 FY26 2.43x (計算); NI/股利 1.76x (計算)。
  - info.payoutRatio 57.6%, 與計算之 56.7% (股利/NI) 接近。
  - info.dividendYield 1.74% (前瞻股利率 USD 0.34), 五年平均殖利率 2.1%。
  - 注意: info.trailingAnnualDividendRate 為 107.09, 明顯為 JPY 單位, 與 USD 殖利率混用, 不採用。
- 回購: FY23 ¥24.4bn / FY24 ¥28.4bn / FY25 ¥49.6bn / FY26 ¥0.55bn。FY26 回購近乎停止。
  - 庫藏股張數 62.2M (FY25) → 49.2M (FY26); 已發行股數 995.4M → 982.4M, 推測為註銷庫藏股 (推論)。
  - 股東總回饋 FY26 (股利 + 回購) ≈ ¥95.0bn, 占 FCF 約 41% (計算), 其餘留存於現金與投資證券。
- 內部人交易: yfinance insider 回傳 [] (6 個月無資料); info.heldPercentInsiders 0.0%。此為資料缺漏而非「零交易」證據, 內部人淨買賣: n/a。
- 高階主管薪酬 (info.companyOfficers, 2026 財年): 社長 CEO Kenji Yamaguchi 總薪酬 ¥2.31m (JSON 單位不明, 可能為千日圓), 無持股市值資料。
- 機構持股: yfinance heldPercentInstitutions 0.23%, institutionsCount 28; 前十大 (2026-06-30 申報) 以 Aristotle Capital 3.56M 股最大 (−5.8% QoQ)。ADR 機構持股資料覆蓋不全, 不具代表性。
- 內部人與機構訊號整體: 資料不足, 無法判定。

## Valuation
價格與市值 (USD):
- regularMarketPrice $19.39 (前收 $19.64, 當日 −1.27%); 52 週區間 $14.79–$27.54 (現價位於區間 36% 位置, 計算); 歷史高點 $30.42。
- 50 日均線 $19.33; 200 日均線 $20.71 (現價低於 200 日均線 6.4%, 計算)。52 週漲幅 +26.5%, S&P 500 同期 +15.8%。Beta 0.938。
- 市值 $35.87bn (info.marketCap); 流通股數 1.87bn (floatShares)。

倍數:
- trailing P/E 32.9x; forward P/E 28.9x (EPS TTM $0.59, forward $0.67); PEG 2.6 (info)。
- P/B 3.0x (info.priceToBook 3.00)。
- P/S: info 為 0.04x, 不可信 (幣別混用, 見下方註記)。以隱含匯率換算 TTM 營收約 $5.68bn 估算, P/S 約 6.3x (計算, 估計值)。
- EV/EBITDA: info 為 −2.9x, 不可信 (info.enterpriseValue 為 −¥708.7bn 之混合幣別計算結果)。以市值 $35.87bn 減淨現金 $4.98bn 得 EV 約 $30.9bn, FY26 EBITDA ¥231.5bn ≈ $1.53bn, 故 EV/EBITDA 約 20.2x (計算, 估計值)。
- P/FCF 約 23.6x; FCF 殖利率約 4.2% (計算, FY26 FCF ÷ 市值)。
- 分析師: 2 位覆蓋, recommendationKey "none"; 目標價均值 $21.72 (高 $22.81、低 $20.63), 較現價 +12.0% (計算)。樣本僅 2 位, 權重低。

同業中位數 (估計, 非來自 yfinance): 工業自動化/機器人類股 P/E 約 25–30x、EV/EBITDA 約 15–20x、P/S 約 2–3x、毛利率約 35%、營業利益率約 12–15%。Fanuc 之 P/E 與 EV/EBITDA 位於或略高於中位數, 但其營業利益率 21% 高於估計中位數; P/S 因估計值不可靠而未直接比較。

幣別註記: yfinance info 中 totalRevenue、totalCash、ebitda、enterpriseValue、trailingAnnualDividendRate 為 JPY, marketCap、bookValue、price 為 USD, 直接相除會得出錯誤結果 (P/S 0.04、EV 為負)。上述估計值已統一換算為 USD 後計算, 匯率以 EPS 反推約 151 JPY/USD, 為估計值。

## Key catalysts
- 下次財報: earnings_dates 顯示 2026-10-30 (UTC 20:00, 即 10-31 日本時間), isEarningsDateEstimate = false; 但 info.earningsTimestamp 對應約 2026-10-23, 兩者不一致, 需以公司公告為準。
- 下季 EPS 預估 $0.13 (2 位分析師)。
- 近季 ADR EPS 趨勢 (USD): 2025-07 季 0.14 (預估 0.13, +7.3%); 2025-10 季 0.15 (預估 0.13, +8.7%); 2026-01 季 0.09 (預估 0.14, −33.9%); 2026-04 季 0.17 (預估 0.13, +23.9%); 2026-07 季 0.17 (預估 0.17, −1.0%)。
- 最近 4 季 EPS 合計 $0.58 (計算), 與 info TTM $0.59 相符。
- 最近一季 (mostRecentQuarter 2026-06-30) 之完整損益表與資產負債表未出現在 quarterly_fin/quarterly_bs 中 (quarterly_fin 僅有 2025-06 季 EPS, quarterly_bs 僅至 2026-03-31), 最新季財務資料為資料缺口。
- 營收指引、分部動態與管理層展望: n/a (工具未提供)。
- 匯率: 財報以 JPY 記帳, ADR 以 USD 計價, JPY 走勢將影響 USD EPS 與股價。
- 股利: 上次除息日 2026-03-31 (exDividendDate), 下次除息日 n/a。

## Metrics table
| 指標 | 最新值 | YoY | 同業中位數 (估計) | 判定 |
|---|---|---|---|---|
| 營收 (JPY bn) | 857.8 (FY3/26) | +7.6% | 成長約 3–6% | 持平偏弱, 3Y CAGR +0.2% |
| 毛利率 | 38.3% | +1.3pt | 約 35% | 優於中位數 |
| 營業利益率 | 21.4% | +1.5pt | 約 12–15% | 明顯優於中位數 |
| 淨利率 | 19.4% | +0.9pt | 約 8–12% | 優於中位數, 但含非營業收益 |
| ROE (info TTM) | 10.1% | n/a | 約 10–12% | 中性 |
| ROIC (扣現金, 計算) | 約 12.3% | n/a | 約 8–10% | 良好 |
| FCF 率 | 26.8% | −0.1pt | 約 8–12% | 極佳 |
| FCF/NI | 1.38 | −0.07 | 約 0.9 | 健康 |
| 流動比率 | 6.9x (計算) | n/a | 約 2.0 | 極佳 |
| 有息負債 | 0 | n/a | n/a | 無負債 |
| 淨現金 (JPY bn) | 753.9 | +27.7% (計算) | n/a | 極佳 |
| Capex/D&A | 0.44x | 由 0.88x 降 | 約 1.0–1.2x | 投資偏低, 需追蹤 |
| 股利覆蓋 (FCF/股利) | 2.43x | 由 2.58x 降 | 約 1.5–2.5x | 充足 |
| 回購 (JPY bn) | 0.55 | 由 49.6 大降 | n/a | 近乎停止 |
| 內部人交易 | n/a (資料空) | n/a | n/a | 無法判定 |
| trailing P/E | 32.9x | n/a | 約 25–30x | 偏高 |
| forward P/E | 28.9x | n/a | 約 22–28x | 略高 |
| P/B | 3.0x | n/a | 約 2–3x | 偏高 |
| EV/EBITDA (計算) | 約 20.2x | n/a | 約 15–20x | 略高 |
| P/FCF (計算) | 約 23.6x | n/a | 約 20–25x | 中性偏高 |
| P/S (計算) | 約 6.3x | n/a | 約 2–3x | 高 (資料有限度) |
| 分析師目標價上檔空間 | +12.0% | n/a | n/a | 樣本 2 位, 低權重 |

## Red flags
- 數據品質: yfinance 混用 JPY 與 USD, info 之 P/S (0.04x) 與 EV (負值) 不可用; 本報告倍數已重算, 但匯率為估計值。
- 股數不一致: info.sharesOutstanding 為 1.85bn, 資產負債表普通股流通股數約 933M (933,158,809), 比例約 1.98x。市值 (USD 35.9bn) 與 BVPS、EPS 之計算基礎需以公司公告再確認。
- 掛牌與流動性: ADR 掛於 OTC Markets OTCPK (exchange: PNK), info.tradeable = false; 3 個月日均量 500,892 股, 10 日均量 418,890 股。流動性與執行成本需納入交易面考量。
- 營收停滯: FY23–FY26 三年 CAGR +0.2%, FY24 −6.7%。FY26 的 +7.6% 恢復是否可延續, 需季度資料驗證。
- 盈餘品質: 稅前利益與營業利益之間約 ¥31.6bn 無明細之差額 (計算), 淨利可能受投資證券相關收益影響, 投資證券 ¥223bn 有估值波動風險。
- 資本支出收縮: FY26 Capex 較 FY25 下降 48%, 僅為 D&A 的 0.44 倍; 在建工程減半。長期產能與研發投入是否不足, 需追蹤。
- 營運資金釋放: FY26 FCF 有約 ¥21.5bn 來自營運資金變動 (計算), 非經常性成分, 不宜外推為常態。
- 回購停止: FY26 回購 ¥0.55bn, 較前一年 ¥49.6bn 大減; 股東回饋主要靠股利。
- 估值溢價與資料有限: trailing P/E 32.9x 配合營收停滯, 估值相對基本面偏高; 分析師僅 2 位, 無共識可參考。
- 內部人資料缺失: insider 空值, insidersPercentHeld 0.0%, 無法判讀內部人買賣。
- 技術面: 現價低於 200 日均線 6.4%, 且 52 週高點 $27.54 較現價高 42%。
- 財報日期不一致: earnings_dates 為 10-30, earningsTimestamp 約 10-23, 需以公告確認。
- 最新季報表缺漏: mostRecentQuarter 2026-06-30 之完整財務報表未入庫, info 內的 TTM 與季度成長率無法逐項核對。
- 非美國公司: 財報以 JPY 編製, yfinance 對 Tokyo 普通股 (6954.T) 查詢無回傳, 無法交叉驗證股數與 EPS。

FUNDAMENTALS REPORT COMPLETE
