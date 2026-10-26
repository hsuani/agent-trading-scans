# Fundamentals — ARQQ (Arqit Quantum Inc.) as of 2026-10-27

## Executive summary
ARQQ 財務體質偏弱: FY2025 (9 月結束) 營收僅 0.53M USD、營業虧損 35.2M USD、OCF -29.6M USD，TTM 營收 1.09M USD 相對市值 285.6M USD，P/S 約 263x，基本面無法支撐現有估值。現金與淨現金仍為正 (2026-03-31 現金 28.86M USD、淨現金約 26.7M USD)，但該數字已落後 7 個月，且公司過去三年依賴股權募資 (FY23–FY25 合計 95.3M USD)，股數自 FY25 底增加 13.8%。Insider 近 6 個月無公開市場買入、公開市場賣出約 2.88M USD，另有一筆 4.6M 股衍生證券轉換待查，整體訊號偏負。

資料時點說明: 本報告以 2026-10-27 為 as-of。yfinance 最新季度資料為 2026-03-31 (Q2 FY26)，FY2026 (2026-09-30 結束) 年報尚未出現於資料中，預計 2026-12-09 公布。所有 insider 資料最晚為 2026-10-16，未有晚於 as-of 的資料。

## Revenue & profitability

**營收 (USD, 原始值 / 百萬 USD)**

| 年度 (FYE 9 月) | 營收 (M USD) | YoY | 營業利益 (M USD) | 淨利 (M USD) |
|---|---|---|---|---|
| FY2022 | 7.21 | n/a | -50.23 | +65.08 (含 unusual items 103.9M 與 discontinued ops) |
| FY2023 | 0.64 | -91.1% | -67.46 | -74.53 |
| FY2024 | 0.29 | -54.2% | -37.37 | -56.82 |
| FY2025 | 0.53 | +80.9% | -35.17 | -35.34 |
| TTM (yfinance info, 至 2026-03-31) | 1.09 | n/a | n/a | -48.98 (netIncomeToCommon) |

- 3 年 CAGR (FY22→FY25): 約 -58.1%。營收基期大幅縮水，FY25 的 +80.9% 係由極低基期推動，尚無法判斷為趨勢反轉。
- 可得年度資料僅 4 年 (FY22–FY25)，無法做 3–5 年完整 CAGR。
- 營收 TTM 1.09M USD，yfinance 另提供 revenueGrowth = 8.299 (原始值，單位不明，未採用)。
- 分部: longBusinessSummary 僅描述 QuantumCloud PaaS、維護支援與專業服務，無分部營收數據，segment mix 為 n/a。

**獲利能力 (FY2025, 自算)**

| 指標 | FY2024 | FY2025 | 說明 |
|---|---|---|---|
| 營業利益率 | -12,754% | -6,636% | 營收極低，比率失真，僅表示虧損規模遠大於營收 |
| 淨利率 | -19,391% | -6,668% | 同上 |
| 毛利率 (TTM, yfinance) | n/a | 49.7% | grossProfits TTM 0.54M USD |
| EBITDA (FY25) | -22.43M | -36.81M | TTM EBITDA -49.94M USD |
| ROE (TTM, yfinance) | n/a | -220.2% | 負值 |
| ROIC (FY25, 自算) | n/a | 約 -138% | EBIT -37.57M / 期末 Invested Capital 27.24M |
| 研發費用 | n/a | n/a | 財報 index 未列 R&D，無法拆分 |

- 營業費用 FY25 為 35.70M USD，其中 SG&A 34.94M USD，佔比 98%，幾乎全為 SG&A。
- 數據一致性驗算: FY25 Diluted EPS -2.56 × 加權平均股數 13.79M ≈ -35.3M，與淨利 -35.34M 吻合。

## Cashflow & balance sheet

**現金流 (USD, M)**

| 項目 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|
| OCF | -26.72 | -32.83 | -34.13 | -29.55 |
| Capex | -24.43 | -16.12 | -3.33 | -0.55 |
| FCF | -51.15 | -48.95 | -37.45 | -30.10 |
| 股權發行 (Common Stock Issuance) | 0.00 | 45.08 | 13.08 | 37.18 |

- FCF margin (FY25, 自算): 約 -5,680%；FY24: 約 -12,783%。
- FCF / NI (FY25): 30.10 / 35.34 ≈ 0.85，但兩者皆為負，此比率無經濟意義，不適用 >0.9 的健康門檻。
- Capex 由 FY22 的 24.4M 降至 FY25 的 0.5M，燒錢主要來自營運面 (OCF)，而非資本開支。
- 資料警示: yfinance TTM OCF = -42.75M，TTM FCF = -19.70M，兩者差值暗示淨 capex 為正約 +23M，與公司歷史 capex 水準不符，判定為資料口徑或來源問題，不採用 TTM FCF 做判斷。

**資產負債表 (USD, M)**

| 項目 | 2025-03-31 | 2025-09-30 (FY25) | 2026-03-31 (最新季) | 說明 |
|---|---|---|---|---|
| 現金及約當現金 | 24.78 | 36.98 | 28.86 | 6 個月下降 8.12M (-22.0%) |
| 總負債 | 13.41 | 15.62 | 7.73 | 2026-03 負債下降 |
| 總債務 (Total Debt) | 0.83 | 0.72 | 2.17 | 2026-03 增加 |
| 淨現金 (現金 − 債務) | 23.95 | 36.26 | 26.69 | 6 個月減少 9.57M (-26.4%) |
| 股東權益 | 15.98 | 27.24 | 28.51 | |
| 流動比率 | 2.45 (自算: 26.57/10.83) | 2.69 (40.02/14.90) | 4.88 (32.16/6.59) | yfinance 2026-03 值 4.88 吻合 |
| 負債權益比 (Debt/Equity) | 0.052x | 0.026x | 0.076x | yfinance 原始 debtToEquity 7.62 為百分比單位 |

- 無長期償債壓力: 總債務僅 2.17M USD，流動比率高，但 EBITDA 為負，Net debt/EBITDA 不適用。
- 現金跑道 (估算，非官方數字): 以 FY25 OCF 速率 (約 2.46M USD/月) 推算，自 2026-03-31 起算約 7 個月理論消耗 17.2M USD，剩餘約 11.6M USD (未計期間募資)。此為推算，需以 2026-06-30 與 2026-09-30 季報/年報核實。
- 股數由 FY25 底 15.29M 增至 2026-03-31 的 16.58M，再增至目前 17.40M，期間很可能已發生股權融資，募資金額 yfinance 未提供。
- 每股現金 1.741 USD (yfinance totalCashPerShare)，每股帳面價值 1.719 USD。

## Capital allocation & insider signal

**資本配置**
- 股利: 0 (FY22–FY25 皆為 0)；payoutRatio = 0.0。
- 回購: 無紀錄。
- 資本配置本質是「燒錢 + 股權募資」。FY23–FY25 股權募資合計 95.3M USD，遠超同期 FCF 負值累計 (FY23–FY25 FCF 合計 -116.5M)，其中大部分用於填補營運缺口。
- 股數稀釋: FY25 底 15.29M → 目前 17.40M，+13.8%。FY22 為 4.88M (已反映 2024-09 之 1:25 反向拆股，lastSplitFactor 1:25)。
- 舊 SPAC 痕跡: prevName = Centricus Acquisition Corp.，yfinance 記錄 nameChangeDate = 2026-10-25。此為 as-of 前 2 天的實體資訊變動，需確認是否為公司改名或資料標籤更新。

**Insider 活動 (近 6 個月, 2026-04-01 至 2026-10-16, yfinance 資料)**

| 類別 | 股數 | 金額 (USD) | 說明 |
|---|---|---|---|
| 公開市場賣出 (Sale at price) | 112,146 | 約 2.88M | 佔市值約 1.0%；佔股數約 0.64% |
| 公開市場買入 | 0 | 0 | 無 |
| 衍生證券轉換 (Conversion of exercise, 2026-06 至 2026-09) | 約 4.80M (含 4.6M 於 2026-09-22) | 約 12.0M (依 yfinance Value 欄位) | 間接持有 (Ownership I) 之 4.6M 股 Lefebvre d'Ovidio Manfredi (Director)，估值 11.5M；其餘為 Calabria 120K、Ritchie 73.6K、Pointon 3K 等，多以約 2.5 USD/股行權 |
| 例行小額股票發放 (Text 空白) | 約數千股/季 | n/a | 董事與高管每月/季度的小額股數變動，推測為薪酬或 director fee 股票，性質待確認 |

- 主要賣出者: CEO Andrew Leaver 公開市場賣出約 27.8K 股 (約 0.58M USD)；Patrick Willcocks 約 9.5K 股 (約 0.23M USD)；Lefebvre d'Ovidio 約 54.4K 股 (約 1.64M USD)；Jennifer Bers 8.3K 股 (約 0.18M USD)。
- 賣出時點集中在 2026-10-05/06 (價約 23.78–24.19 USD) 與 2026-10-13 (CEO 2,573 股 @16.40)；股價於一週內由約 24 USD 跌至約 16 USD，賣出價與當前價差距約 -32%。
- 4.6M 股衍生證券轉換 (2026-09-22) 為本次最需核實項目：若轉換後股份已賣出或流通，對 float 與價格壓力影響遠大於公開市場賣出；yfinance 之 heldPercentInsiders = 2.84% (約 0.49M 股) 未能反映該筆 4.6M 股，資料不一致。
- 整體判讀: 6 個月內 open-market 淨賣出、無買入；賣出金額相對市值比例不大 (約 1.0%)，但行權後的賣出與價格同步下跌，訊號偏負。

## Valuation

**價格與市值 (USD)**
- 現價 16.41 USD (fast_info, 2026-10-26 cache)；前收 15.81；當日區間 15.51–16.95。
- 市值 285.57M USD (info marketCap 285,573,568)；驗算: 16.41 × 17.40M 股 = 285.6M，吻合。
- EV: yfinance 245.40M USD；自算 (市值 + 債務 2.17M − 現金 28.86M) = 258.9M USD。兩者差約 13.5M，原因推測為 yfinance 使用不同期間現金，本報告以自算值為參考。
- 52 週區間: 11.52–49.33 USD；現價較 52 週高點下跌約 66.7%，52 週報酬 -65.1% (S&P 500 同期 +10.9%)。
- 50 日均線 20.33 USD (現價低於 19.3%)；200 日均線 18.42 USD (現價低於 10.9%)。

**估值倍數**

| 指標 | 數值 | 說明 |
|---|---|---|
| Trailing P/E | n/a | EPS TTM -3.21，為負 |
| Forward P/E | -15.5x (yfinance) | forwardEps -1.06，為負，n/m |
| P/S (TTM) | 263.0x | 市值 / 營收 TTM 1.086M |
| EV/Revenue (TTM) | 226.0x (yfinance) / 約 238x (自算) | |
| EV/EBITDA (TTM) | -4.9x (yfinance) | EBITDA TTM -49.9M，n/m |
| P/FCF (TTM) | n/m | FCF 為負 |
| P/B | 9.5x | 每股帳面 1.719 USD |
| Beta | 2.79 | 高波動 |

- 估值結論: 以 P/S 263x 與 P/B 9.5x 計價，市場定價隱含的是未來營收規模大幅成長 (與 FY22–FY25 萎縮的歷史背離)。以目前財務資料，無法提供可量化的估值支撐；估值以期權式/題材式定價為主。
- 分析師覆蓋: targetMeanPrice、targetHigh/Low、numberOfAnalystOpinions 均為 n/a；recommendationKey = none，無可用的分析師共識。

## Key catalysts

- **下次財報 (預估)**: 2026-12-09 (yfinance earnings_dates)。此日期為 FY2026 (2026-09-30 結束) 年報預計公布日，EPS estimate 為 n/a。FY26 全年營收、現金餘額與 FY27 展望是本季最重要的基本面資料點。
- **上次財報**: 約 2026-05-21 (earningsTimestamp 1779366600)，對應 FY26 Q2 (2026-03-31)。yfinance 尚未納入 2026-06-30 季度資料，資料落後。
- **融資**: 現金消耗與股數增加顯示公司持續募資。若新一輪募資或 ATM 發行出現，對股價與每股價值為直接壓力；需追蹤 8-K 與 S-3/S-1 申報。
- **衍生證券轉換與賣壓**: 4.6M 股 (2026-09-22) 的後續處置，以及 Lefebvre d'Ovidio 與 CEO 的 Form 4 申報。
- **空頭結構**: sharesShort 2.26M 股 (佔流通股約 13.0%；yfinance 報 shortPercentOfFloat 17.8%，但以 floatShares 5.32M 計算約 42.5%，float 數據不一致，需核實)，days to cover 6.1 天，較上月 2.60M 股下降約 13%。空頭仍高但有回補跡象。
- **實體/資料異動**: nameChangeDate 2026-10-25、prevName Centricus Acquisition Corp.，需確認是否為公司層級事件。
- **業務主題**: 量子安全加密 (QuantumCloud PaaS)，產業題材熱度為股價驅動因素之一，但目前無公司層級的量化指引 (guidance) 可得。

## Metrics table

金額單位: USD；營收/利潤/現金以 M USD 表示。Sector median 為估計值 (非 yfinance 提供)，僅供粗略比較。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 TTM (M USD) | 1.09 | FY25 +80.9% (基期 0.29M) | 成長中位數約 +10–15% (估) | 規模極小，不具可比性 |
| 營收 3 年 CAGR (FY22–FY25) | -58.1% | n/a | 正成長 (估) | 負 |
| 毛利率 (TTM) | 49.7% | n/a | 約 70% (估) | 偏低 |
| 營業利益率 (FY25) | -6,636% | 改善自 FY24 -12,754% | 約 -5% 至 +10% (估) | 嚴重虧損 |
| 淨利率 (FY25) | -6,668% | 改善自 FY24 -19,391% | 約 -5% 至 +10% (估) | 嚴重虧損 |
| ROE (TTM) | -220.2% | n/a | 約 5–15% (估) | 負 |
| ROIC (FY25, 自算) | 約 -138% | n/a | 約 8% (估) | 負 |
| FCF (FY25, M USD) | -30.10 | 改善自 FY24 -37.45 | 正 (估) | 持續燒錢 |
| FCF margin (FY25) | -5,680% | n/a | 約 10% (估) | 負 |
| FCF / NI | n/m (兩者皆負) | n/a | >0.9 | 不適用 |
| 現金 (M USD) | 28.86 (2026-03-31) | YoY +16.5% (vs 24.78); 較 FY25 底 -22.0% | 科技業通常為淨現金 (估) | 跑道有限，資料已落後 |
| 淨現金 (M USD) | +26.69 | 較 FY25 底 -26.4% | 正 (估) | 正但持續消耗 |
| 流動比率 | 4.88 | FY25 底 2.69 | 約 2.0x (估) | 佳 |
| Debt/Equity | 0.076x | FY25 底 0.026x | 約 0.2x (估) | 低 |
| 股數 (M 股) | 17.40 | vs FY25 底 15.29 (+13.8%) | 年稀釋 <5% (估) | 高稀釋 |
| 股權募資 FY25 (M USD) | 37.18 | FY24 13.08 (+184%) | n/a | 依賴股權融資 |
| Insider 6 個月公開市場淨買入 (M USD) | -2.88 (淨賣出) | n/a | 小型股 insider 多為小額 (估) | 偏負 |
| Insider 賣出/市值 | 約 1.0% | n/a | n/a | 中性偏負 |
| 空頭比率 (% float) | 17.8% (days to cover 6.1) | 空單 -13% MoM | 小型股中位數 (估) 約 5–10% | 偏高 |
| P/E (Trailing) | n/a | n/a | 約 25x (估) | n/a (EPS 為負) |
| P/E (Forward) | -15.5x | n/a | 約 25x (估) | n/m |
| P/S (TTM) | 263.0x | n/a | 約 5–7x (估) | 極度昂貴 |
| EV/EBITDA (TTM) | n/m (-4.9x) | n/a | 約 20x (估) | n/m |
| P/FCF | n/m | n/a | 約 25x (估) | n/m |
| P/B | 9.5x | n/a | 約 3–5x (估) | 偏貴 |
| 52 週股價報酬 | -65.1% | 相對 S&P +10.9% 落後 76 ppt | n/a | 弱勢 |
| Beta | 2.79 | n/a | 約 1.1–1.3 (估) | 高波動 |

## Red flags
- 營收規模極小且歷史萎縮: FY22 7.21M → FY25 0.53M，3 年 CAGR -58.1%；TTM 營收僅 1.09M USD，相對市值 285.6M USD，P/S 263x。
- 持續重大虧損: FY25 營業虧損 35.2M USD、OCF -29.6M USD、淨利 -35.3M USD；TTM EBITDA -49.9M USD。
- 現金跑道不明: 最新現金 28.86M USD (2026-03-31)，已落後 7 個月。以 FY25 OCF 速率估算，理論剩餘約 11.6M USD，須以 2026-09-30 資料核實，並可能需再次募資。
- 高稀釋: FY23–FY25 股權募資合計 95.3M USD；股數 FY25 底至今 +13.8%，FY22 至 FY25 反向拆股後仍持續增加。
- Insider 無買入、公開市場賣出約 2.88M USD，且集中在股價由約 24 跌至約 16 的區間內。
- 衍生證券轉換 4.6M 股 (2026-09-22，間接持有，估值 11.5M USD) 未在 yfinance heldPercentInsiders 反映，後續處置不明，為潛在賣壓來源；需核查 Form 4。
- 機構持股集中且 float 數據不一致: Defiance Etfs 32.6% (5.10M 股) + Penserra 32.5% (5.08M 股) 合計 10.18M 股，超過 yfinance floatShares 5.32M，數據互相矛盾 (同時 sharesShort 2.26M 相對 floatShares 為 42.5%，與 yfinance 報告的 shortPercentOfFloat 17.8% 不一致)；若真實持股屬實，則可流通股極薄，單一大戶出清風險高。
- 資料品質問題: TTM OCF (-42.75M) 與 TTM FCF (-19.70M) 隱含 capex 為正，不合理；yfinance profitMargins = 0.0 與 netIncomeToCommon -48.98M 矛盾；revenueGrowth = 8.299 單位不明。以上欄位均未用於結論。
- 資料落後: quarterly_fin 與 quarterly_cf 為空；最新季度僅至 2026-03-31；FY26 年報尚未揭露。
- 無分析師覆蓋: targetMeanPrice 與 numberOfAnalystOpinions 均為 n/a，recommendationKey = none，缺乏外部共識參照。
- 股價技術結構弱: 現價低於 50 日與 200 日均線；52 週跌幅 -65%；Beta 2.79。
- 實體資訊異動: prevName Centricus Acquisition Corp.，nameChangeDate 2026-10-25，需核實公司層級事件。
- 歷史數據噪音: FY22 淨利 +65.1M 含 unusual items 103.9M 與 discontinued ops，非經常性，不能作為獲利能力參考。

FUNDAMENTALS REPORT COMPLETE
