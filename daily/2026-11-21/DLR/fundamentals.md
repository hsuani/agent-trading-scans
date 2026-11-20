# Fundamentals — DLR (Digital Realty Trust) as of 2026-11-21

資料基準: 2026-11-21 (as-of)。yfinance 快取時間戳為 2026-11-20，最新季報為 2026-09-30 (Q3 2026)。Q2 2026 季度欄位在 yfinance 多數為 null，TTM 數字取自 info 欄位。單位: 美元，以 B (十億美元) / M (百萬美元) 表示；股數以 M 表示。2026-12-15 除息、2027-01-15 發放、2027-02-11 財報日均屬 as-of 之後的已公告或預估事件，僅列為排程，不視為已發生。

## Executive summary
DLR 基本面呈現「營收高成長、獲利品質差、槓桿偏高、股利覆蓋偏薄」的組合: FY2025 營收 $6.11B (YoY +10.0%)，Q3 2026 營收 $1.90B (YoY +20.6%)，但 GAAP ROE 僅 3.3%、FY2025 GAAP 淨利含一次性利益，正常化獲利率僅約 9.7%，且 Q3 2026 營運現金流 $382M 低於同季股利支付 $476M。TTM net debt / EBITDA 約 5.9x，股本 2026 年內已由 343.6M 增至 374.9M (Q3)，稀釋壓力明顯。估值方面，trailing P/E 71.4x、forward P/E 58.5x、EV/EBITDA 26.4x 明顯高於一般 REIT 水準，分析師平均目標價 $224 (+32%) 反映市場對 AI 數據中心需求的長期預期，但目前估值已將此預期大幅定價，且缺少 FFO / AFFO 原始資料，無法以 P/FFO 完整驗證。

## Revenue & profitability

**營收與成長**
- 年度營收 (USD B): FY2022 4.69 / FY2023 5.48 (YoY +16.7%) / FY2024 5.56 (YoY +1.4%) / FY2025 6.11 (YoY +10.0%)。
- 2022→2025 3 年 CAGR 約 9.2%。2024 年幾乎停滯，2025 年恢復成長。
- 季度趨勢: Q3 2025 營收 $1.577B → Q3 2026 $1.902B，YoY +20.6%。Q1 2026 $1.635B、Q4 2025 $1.635B；Q2 2026 資料缺失 (null)。
- info 欄位 TTM 營收 $7.08B，revenueGrowth 20.7%，與 Q3 YoY 方向一致。
- 業務組合: yfinance 未提供分部營收數字；longBusinessSummary 僅描述 300+ 據點、55+ 都會區、30+ 國家之資料中心 / colocation / interconnection 平台，並提及 AI 為需求方向。分部比重 DATA_UNAVAILABLE。

**獲利能力**
- 毛利率 (FY): 2023 52.6% → 2024 54.7% → 2025 55.4%，逐年改善；info TTM 毛利率 57.0%。
- 營業利益率 (FY): 2023 13.3% → 2024 13.6% → 2025 15.1%；info TTM 18.9%。注意 yfinance 歷史 "Operating Income" 與 "Total Operating Income As Reported" (2024 為 $472M) 定義不同，本報告採 Operating Income 系列。
- GAAP 淨利 (FY): 2023 $949M (淨利率 17.3%) / 2024 $602M (10.8%) / 2025 $1,309M (21.4%)。2025 年 Q2 單季 NI $1,032M，明顯含非經常性利益，因此 FY2025 GAAP 淨利率不具代表性。
- 正常化獲利: yfinance Normalized Income FY2025 $594M，對應正常化淨利率約 9.7%；FY2024 $324M (5.8%)。
- GAAP 稀釋後 EPS: FY2023 $0.72 / FY2024 $0.40 / FY2025 $0.895。info trailing EPS $2.37 (TTM，口徑與季度 EPS 不一致，見資料品質)。
- ROE (info, TTM): 3.3%；ROA (info, TTM): 1.6%。
- ROIC (估算): FY2025 營業利益 $922M × (1 − 2.4% 稅率) / 平均投入資本 $39.0B ≈ 2.3%。此為本報告自行估算，僅供參考。
- 結論: 營收端成長動能強，但 GAAP 報酬率偏低，且 ROIC 估算值 (約 2.3%) 遠低於 REIT 資本成本常見區間，獲利效率仍是核心質疑點。

## Cashflow & balance sheet

**現金流品質**
- 營運現金流 (OCF, USD B): FY2022 1.66 / FY2023 1.63 / FY2024 2.26 / FY2025 2.41 (YoY +6.7%)。
- 注意: yfinance 年度 "Free Cash Flow" 欄位與 OCF 完全相同 (FY2025 均為 $2,412M)，表示 capex 未被獨立拆出；投資活動現金流 FY2025 為 −$2.23B (FY2024 −$1.91B)，應為主要資本支出 / 收購支出。因此真正 FCF (OCF − 資本支出) 無法從資料計算，DATA_UNAVAILABLE。
- info 的 freeCashflow TTM $3.93B 與年度 OCF 口徑不一致，本報告不採用於 FCF 計算，僅列為參考。
- FCF / NI: 以 OCF / GAAP NI 計 FY2025 為 1.84x (受非經常利益與高 D&A $1.89B 影響)；以 OCF / 正常化淨利計為 4.06x。兩者都超過 0.9 門檻，但主要是 D&A 大量非現金費用所致，屬於 REIT 特性，不宜直接以 0.9 標準判讀為品質良好。
- Q3 2026 單季 OCF $382M，較 Q1 2026 $532M、Q4 2025 $719M、Q3 2025 $653M 明顯下滑，為近期紅旗。

**資產負債表 (槓桿)**
- Total debt: FY2024 $18.01B → FY2025 $19.66B → Q3 2026 $20.69B。
- Cash: FY2025 $3.45B → Q3 2026 $0.80B，現金大幅下降；Q1 2026 為 $2.43B。
- Net debt (自算 Q3 2026 = Total debt − Cash) ≈ $19.88B。yfinance 季度 "Net Debt" 欄位顯示 $18.69B，與自算值不一致，本報告採自算值。
- Net debt / EBITDA:
  - FY2025 (BS 口徑: net debt $14.95B / EBITDA $3.68B) ≈ 4.1x；FY2024 ≈ 4.5x；FY2023 ≈ 5.0x；FY2022 ≈ 7.2x。
  - TTM (info 口徑: (total debt $20.89B − cash $0.84B) / EBITDA $3.37B) ≈ 5.9x。
  - Q3 2026 自算淨負債 $19.88B / TTM EBITDA $3.37B ≈ 5.9x。
  - 注意 FY2025 與 TTM 之間 EBITDA 口徑 (reported EBITDA $3.68B vs info ebitda $3.37B) 有差異，TTM 數字較保守。
- 利息保障: FY2025 EBITDA / 利息費用 ($438M) ≈ 8.4x；FY2024 ≈ 6.3x，改善。
- Debt / Equity: info 欄位 69.1% (0.69x)；FY2025 BS 自算 total debt / stockholders' equity = $19.66B / $22.93B ≈ 0.86x。兩者口徑不同，本報告以 BS 自算為準。
- Current ratio: info 欄位 0.575；FY2025 BS 自算 $5.16B / $4.68B = 1.10x；Q3 2026 自算 $2.61B / $6.14B = 0.43x。REIT 之流動性比率解讀價值有限，但 Q3 2026 流動負債增至 $6.14B 同時流動資產縮至 $2.61B，短期償債壓力需關注 (debt maturities DATA_UNAVAILABLE)。
- 債務到期結構 (maturity ladder) yfinance 未提供，DATA_UNAVAILABLE。FY2025 Current Debt $0.90B，Long-term debt $17.50B。
- 股東權益: FY2025 $22.93B → Q3 2026 $28.11B，權益擴增主要來自股權發行。

## Capital allocation & insider signal

**資本配置**
- 股利: 季度股利 $1.22，年化 $4.88，info 殖利率 2.8%。最近一次宣告 / 發放日期 2026-09-15；info corporateActions 顯示下一次除息日 2026-12-15、發放日 2027-01-15 (皆為 as-of 之後之排程)。
- 股利覆蓋:
  - FY2025 OCF / 現金股利 ($1,728M) = 1.40x；FY2024 1.38x；FY2023 1.08x；FY2022 1.14x。覆蓋比率改善，但仍偏薄。
  - Q3 2026 單季 OCF $382M / 股利支付 $476M = 0.80x，單季不足覆蓋。
  - 以年化股利 $4.88 × 378.3M 股 ≈ $1.85B 對 FY2025 OCF $2.41B 計 ≈ 1.31x。
  - info payoutRatio 206% 以 GAAP EPS 計，不具代表性，因 REIT 應以 FFO / AFFO 計算。
- 資本支出 / 投資: 投資活動現金流 FY2025 −$2.23B，FY2024 −$1.91B，FY2023 −$1.12B，FY2022 −$4.70B。投資規模持續擴張，與 AI 資料中心建置一致 (依 summary 文字，未有分項數據)。
- 股權發行 (dilution): 股權發行淨額 FY2022 $0.93B / FY2023 $2.21B / FY2024 $3.65B / FY2025 $1.11B。流通股數 FY2022 291.1M → FY2025 343.6M → Q3 2026 374.9M → info sharesOutstanding 378.3M (相對 FY2025 年底 +10.1%)。資本主要依賴股權與債務滾動，股東稀釋為顯著結構特徵。
- 買回: FY2022–FY2025 無股票買回 (2021 為 $201M)。

**內部人交易 (last 6 months: 2026-05-21 ~ 2026-11-21)**
- 共 2 筆紀錄:
  - 2026-08-27 Director Mark R. Patterson 賣出 200 股，@ $193.96，金額約 $38.8K。
  - 2026-05-29 Director Jean F. H. P. Mandeville 股票獎勵 1,289 股 (無現金交易)。
- 淨交易: 賣出 200 股 / $38.8K，買入 0。
- 相對市值 $65.2B，淨賣出金額僅約 0.00006%，訊號強度極低。
- 歷史背景 (超出 6 個月窗口): CEO Andrew P. Power 2025-09-15 賣出 58,000 股，金額約 $10.16M；Director Mary Hogan Preusse 2025-12-01 賣出 4,166 股，約 $0.66M。
- 內部人持股比例 info heldPercentInsiders 0.031%，極低，對持股一致性之參考價值有限。
- 機構持股 heldPercentInstitutions ≈ 100.4% (info 數值，超過 100% 屬資料口徑問題)，機構家數 1,823 (major_holders)。

## Valuation

以 info 之 regularMarketPrice $169.295 (cache 時間 2026-11-20) 計:
- 市值: $65.18B；企業價值 EV $88.75B。
- P/E (trailing, EPS $2.37): 71.4x；P/E (forward, EPS $2.89): 58.5x；FY2026 EPS 估計 $3.29 → P/E 51.4x。
- P/S (trailing): 9.2x；EV / Revenue (TTM): 12.5x。
- P/B: 2.32x (book value/share $73.04)；P/B 驗證: Q3 2026 equity $28.11B / 374.9M 股 ≈ $75.0，與 info 接近。
- EV / EBITDA (TTM, info EBITDA $3.37B): 26.4x (手算 $88.75B / $3.37B = 26.4x，吻合)。
- P/FCF:
  - 以 info TTM freeCashflow $3.93B 計 16.6x。
  - 以 FY2025 OCF $2.41B 計 27.0x (與 capex 未扣除之口徑)。
- P/FFO / P/AFFO: DATA_UNAVAILABLE。yfinance 未提供 FFO / AFFO，不得以 EPS 替代。
- PEG: 14.4x (info)，顯示以盈餘成長估值極高。
- 分析師: 共 32 位，recommendationMean 1.44 (strong buy 區間)；目標價 mean $223.97 / median $225 / high $250 / low $190；相對 $169.3 之中位目標上行約 +33%。此為市場共識，不等於本研究結論。
- 技術面參考 (ta snapshot, as_of 2026-11-20, price $169.765): 低於 MA20 $178.49、MA50 $178.43、MA200 $184.47；RSI14 39.5；距 52 週高點 $208.14 為 −18.4%，距 52 週低點 $146.23 為 +16.1%；ATR14 $5.68 (約 3.3%)。
- 估值結論: 以 GAAP 及 EBITDA 口徑，DLR 相對 REIT 同業 (估計) 明顯溢價；以 P/FFO 檢視需補資料。

**Sector median (estimate)**: 以下為估計值，非資料工具輸出，僅供粗略對照: 數據中心 / 專業型 REIT 之 EV/EBITDA 估計約 18–24x，P/AFFO 估計約 18–25x，P/S 估計約 6–10x。

## Key catalysts
- 最近財報 2026-10-29: EPS $0.61 vs 預估 $0.57，超預期 +5.7%。
- 前一季 2026-07-23: EPS $0.62 vs 預估 $0.73，不及預期 −15.0%。
- 2026-04-23: $0.46 vs $0.45 (+2.7%)；2026-02-05: $0.40 vs $0.39 (+2.2%)。近四季 3 勝 1 負，但 EPS 口徑 (可能非 FFO) 需確認。
- 下次財報: 2027-02-11 (yfinance 為估計日期，EPS 預估 $0.43)，屬 as-of 之後事件。
- 公司指引 (guidance): DATA_UNAVAILABLE。
- 分部與產能 (MW 在建 / 已租、租約續約、AI 相關訂單): DATA_UNAVAILABLE。
- 股利事件: 2026-12-15 除息 ($1.22)、2027-01-15 發放，為已公告之排程。
- 治理: info overallRisk 7，shareHolderRightsRisk 9 (高)，compensationRisk 7，僅為 info 之外部評分，供參考。

## Metrics table
單位: 營收 / 現金流 / 市值 / 負債為 USD B；股數為 M。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 FY2025 (USD B) | 6.11 | +10.0% | 估計 +5–10% | 成長良好 |
| 營收 Q3 2026 (USD B) | 1.90 | +20.6% | n/a | 加速 |
| 營收 TTM (USD B, info) | 7.08 | +20.7% (info revenueGrowth) | n/a | 成長強 |
| 毛利率 FY2025 | 55.4% | +0.7pt | 估計 ~50–60% | 中上 |
| 營業利益率 FY2025 | 15.1% | +1.5pt | 估計 ~20–30% | 偏低 |
| 營業利益率 TTM (info) | 18.9% | n/a | 估計 ~20–30% | 偏低 |
| GAAP 淨利率 FY2025 | 21.4% (含一次性) | n/a | n/a | 不具代表性 |
| 正常化淨利率 FY2025 | 9.7% | 2024 為 5.8% | 估計 ~5–15% | 改善中 |
| ROE (TTM, info) | 3.3% | n/a | 估計 ~3–6% | 偏低 |
| ROIC (估算) | 2.3% | n/a | 估計 ~4–6% | 偏弱 |
| OCF FY2025 (USD B) | 2.41 | +6.7% | n/a | 穩定成長 |
| FCF 真正口徑 (OCF − capex) | DATA_UNAVAILABLE | n/a | n/a | 無法判定 |
| OCF / GAAP NI FY2025 | 1.84x | n/a | >0.9 健康門檻 | 有 D&A 影響 |
| OCF / 正常化淨利 FY2025 | 4.06x | n/a | >0.9 健康門檻 | 達標 |
| Q3 2026 OCF (USD M) | 382 | 低於 Q1 2026 (532) | n/a | 紅旗 |
| Net debt / EBITDA (TTM) | ~5.9x | FY2025 BS 4.1x | 估計 ~5–6x | 偏高 |
| EBITDA / 利息 FY2025 | 8.4x | FY2024 6.3x | 估計 ~4–6x | 改善 |
| Total debt Q3 2026 (USD B) | 20.69 | +5.3% vs FY2025 | n/a | 持續擴張 |
| Cash Q3 2026 (USD B) | 0.80 | FY2025 3.45 | n/a | 大幅下降 |
| Current ratio (BS, FY2025) | 1.10x (Q3 2026 0.43x) | n/a | 不適用 (REIT) | 需關注 |
| Debt / Equity (BS, FY2025) | 0.86x (info 0.69x) | n/a | 估計 ~0.8–1.2x | 中性 |
| 股利覆蓋 (OCF / 股利) FY2025 | 1.40x | FY2024 1.38x | 估計 ~1.2–1.5x | 偏薄 |
| 股利覆蓋 Q3 2026 單季 | 0.80x | n/a | n/a | 紅旗 |
| 股利殖利率 | 2.8% | 5 年均 3.27% | 估計 ~3–4% | 低於歷史 |
| 股權發行淨額 FY2025 (USD B) | 1.11 | FY2024 3.65 | n/a | 稀釋 |
| 流通股數 (M) | 378.3 (info) | FY2025 343.6 (+10.1%) | n/a | 稀釋 |
| 內部人淨交易 (6 個月) | 賣出 200 股 / $38.8K | n/a | n/a | 極弱訊號 |
| 市值 (USD B) | 65.18 | n/a | n/a | n/a |
| Trailing P/E (GAAP) | 71.4x | n/a | 估計 ~20–40x | 偏高 |
| Forward P/E | 58.5x | n/a | 估計 ~20–40x | 偏高 |
| EV / EBITDA (TTM) | 26.4x | n/a | 估計 ~18–24x | 溢價 |
| P/FCF (info TTM FCF) | 16.6x | n/a | n/a | 參考 |
| P/OCF (FY2025) | 27.0x | n/a | n/a | 偏高 |
| P/S (TTM) | 9.2x | n/a | 估計 ~6–10x | 偏高 |
| P/B | 2.32x | n/a | 估計 ~2–4x | 合理 |
| P/FFO / P/AFFO | DATA_UNAVAILABLE | n/a | 估計 ~18–25x | 無法驗證 |
| 分析師目標價均值 | $224 (+32%) | n/a | n/a | 市場樂觀 |

## Red flags
- 股利覆蓋不足: Q3 2026 單季 OCF $382M < 股利支付 $476M (0.80x)；FY2025 覆蓋 1.40x 僅靠營運現金流，且未扣除資本支出。
- 現金大幅下降: cash 由 FY2025 $3.45B 降至 Q3 2026 $0.80B，同期 total debt 升至 $20.69B，短期流動性與再融資依賴需追蹤。
- 槓桿偏高: TTM net debt / EBITDA 約 5.9x，高於 FY2025 BS 口徑 4.1x，顯示 EBITDA 口徑與淨負債變動需一併檢視。
- 持續稀釋: 流通股數 FY2025 年底 343.6M → 2026 Q3 374.9M → info 378.3M；股權發行淨額 FY2024 $3.65B、FY2025 $1.11B，每股 FFO 成長需扣除稀釋。
- GAAP 獲利品質: ROE 3.3%、ROIC 估算 2.3%；FY2025 GAAP 淨利包含 Q2 單季 $1.03B 一次性利益，正常化淨利率僅約 9.7%。
- 估值極高: trailing P/E 71.4x、EV/EBITDA 26.4x、PEG 14.4x，市場定價高度依賴 AI 數據中心成長兌現。
- 盈餘不及預期: 2026-07-23 季度 EPS −15.0% 不及預期，近期仍有不及預期紀錄。
- 技術面弱勢 (參考): 股價低於 MA20/50/200，RSI14 39.5，距 52 週高點 −18.4%。
- 治理評分 (info): shareHolderRightsRisk 9、overallRisk 7，為外部評分之高風險區間。
- 內部人持股極低 (0.031%)，內部人交易資訊量有限。

## 資料品質與缺口
- 價格來源不一致: info regularMarketPrice $169.295 (cache 2026-11-20)；fast_info last_price $169.925 (cnyes 來源)；ta snapshot $169.765。差異約 0.4%，本報告估值以 info 為準。
- info 與報表口徑差異: currentRatio (info 0.575 vs BS 1.10)、debtToEquity (info 69.1% vs BS 0.86x)、TTM cash ($0.84B info vs Q3 2026 BS $0.80B 大致吻合)。以報表自算為主。
- yfinance 年度 FCF 等於 OCF，capex 未拆出；真正 FCF 與 AFFO 無法計算。
- EPS 口徑: earnings_dates 之 "Reported EPS" (如 Q3 2026 $0.61) 與季報 GAAP diluted EPS (Q3 2026 $0.48) 不同，極可能為非 GAAP 口徑但未註明，無法確認為 FFO。
- 季度缺口: Q2 2026 之 income / BS / CF 欄位 null；Q1、Q2 2025 部分欄位 null。
- Short interest 欄位異常 (sharesShort 22,013 vs prior month 8,994,183)，數量級不合理，本報告不採用，shortPercentOfFloat 0.0001% 亦不採用。
- 機構持股比例 100.4% (超過 100%)，口徑不明。
- 未取得: FFO / AFFO、債務到期表、分部營收、公司指引、利率避險比例、資本支出分項，皆為 DATA_UNAVAILABLE。
- 所有數據皆以 cache 或 yfinance 為準，未依賴外部網頁；所列 sector median 皆標示為估計。

FUNDAMENTALS REPORT COMPLETE
