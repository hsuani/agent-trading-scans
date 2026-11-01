# Fundamentals — SIVE.ST (Sivers Semiconductors AB) as of 2026-11-02

單位說明：本報告金額皆為 SEK，依規定以「億 SEK」表示（1 億 = 100,000,000 SEK），全文不使用 B。股價單位為 SEK。資料來源為 `pipeline/tools/yf`，最新季度為 2026-06-30，截至 2026-11-02 無新季報。下一次財報日 2026-11-26 為未來排程，不是已公布資料。

## Executive summary
Sivers 2026-06 為止仍是深度虧損、持續燒錢的公司：TTM 營收 2.78 億 SEK（YoY -12.4%）、毛利為負（毛利率 -7.6%）、TTM 淨利 -2.94 億 SEK（淨利率 -105.8%）、TTM FCF -0.83 億 SEK，現金 0.63 億 SEK 低於總債務 1.82 億 SEK。估值上，股價 20.9 SEK、市值 63.65 億 SEK，P/S 22.9x、P/B 6.6x，P/E、EV/EBITDA、P/FCF 因分母為負而無法計算；僅有的 2 位分析師目標價均值 7.7 SEK，遠低於現價。綜合判斷財務健康度偏弱、估值缺乏基本面支撐，主要依賴增資與股權市場的資金來源。

## Revenue & profitability
**營收**：yfinance 年度利潤表未直接回傳 Total Revenue 欄位，以下年度營收為「Total Expenses + Total Operating Income As Reported」推算值（推算值，非原始欄位）：

| 年度 | 推算營收 (億 SEK) | 淨利 (億 SEK) | 稀釋 EPS (SEK) |
|---|---|---|---|
| 2022 | 1.33 | -0.86 | -0.41 |
| 2023 | 2.36 | -1.57 | -0.68 |
| 2024 | 2.19 | -1.84 | -0.78 |
| 2025 | 3.07 | -2.23 | -0.81 |
| TTM (至 2026-06) | 2.78（info.totalRevenue 原始值） | -2.94（info.netIncomeToCommon） | -0.74（info.trailingEps） |

- 3 年 CAGR（2022→2025，推算值）約 +32%，但 2024 年曾下滑 -7%，2025 年回升 +40%。
- 2026 上半年推算營收為 1.16 億 SEK（Q1 0.62 + Q2 0.54），對比 2025 上半年 1.40 億 SEK，年減約 -17%。Q2 2026 推算營收 0.54 億 SEK，yoy 約 -12%，與 info.revenueGrowth -12.4% 相符。
- 營收分部：info.longBusinessSummary 指出分為 Wireless 與 Photonics 兩大部門，應用包括 AI datacenter、衛星通訊、國防與電信；但無分部營收占比數據，標記為 n/a。

**獲利能力**：
- 毛利：info.grossProfits TTM 為 -0.21 億 SEK，grossMargins -7.6%。季度來看 Q2 2026 Reconciled Cost of Revenue 為 0.73 億 SEK，高於推算營收 0.54 億 SEK，毛利為負。2025 年 Cost of Revenue 3.09 億 SEK，推算毛利率約 -0.6%。
- 營業利益：2025 年 EBIT -2.11 億 SEK（推算營業利益率約 -69%）；2026 Q2 EBIT -1.07 億 SEK。info.operatingMargins 為 -217%，與季度 EBIT 加總不一致，已列為資料缺口，以季度數為準。
- 淨利率：2025 年約 -73%（-2.23 億 / 3.07 億，推算），TTM 為 -106%（info.profitMargins -1.058）。
- EBITDA：2025 年 -1.39 億 SEK（推算淨利率約 -45%）；TTM info.ebitda -2.18 億 SEK，EBITDA margin -78.6%。
- ROE：info.returnOnEquity TTM -28.6%；ROA -12.3%。
- ROIC：NOPAT 為負，ROIC 為負值，n/m（無意義）。

## Cashflow & balance sheet
**現金流**：
- 2025 年 FCF -1.06 億 SEK（FCF = OCF - Capex），推算 OCF 約 -0.39 億 SEK，Capex -0.67 億 SEK。
- FCF margin（2025，推算）約 -34%；TTM FCF -0.83 億 SEK，info.operatingCashflow TTM -1.20 億 SEK。
- FCF / NI：2025 為 0.47，但兩者皆為負，比率無意義（n/m），不能視為健康信號。2025 年 OCF 遠優於淨利（-0.39 億 vs -2.23 億），差額多為非現金費用或營運資金變化，但資料中無 impairment 明細，需確認。
- 2026 季度 FCF：Q1 -0.61 億、Q2 -0.79 億 SEK，燃燒速度較 2025 年上升。

**資產負債表（2026-06-30）**：
| 項目 | 數值 (億 SEK) | 說明 |
|---|---|---|
| 總債務 Total Debt | 1.82 | 2025-12 為 1.22 |
| 現金 totalCash (info) | 0.63 | 與 BS 推算不一致，見資料缺口 |
| 淨債務 Net Debt (BS) | 1.00 | 2025-12 為 0.73；2026-03 為 1.32 |
| 股東權益 | 9.49 | 2025-12 為 9.50，2024 為 10.91 |
| 總負債 | 4.69 | 2025-12 為 3.81，半年增加約 23% |
| 有形淨資產 Net Tangible Assets | -1.10 | 負值，商譽或無形資產占比高 |
| 營運資金 | 1.12 | 2025-12 為 -0.21 |

- 流動比率 current ratio 1.64、速動比率 quick ratio 1.25（info）。
- Debt/Equity 19.2%（info.debtToEquity 19.157，與 1.82 / 9.49 相符）。
- 利息支出：2025 年 0.26 億，2026 上半年已達 0.29 億（Q1 0.18 + Q2 0.11），費用率上升。EBIT 為負，利息保障倍數 n/m。
- 到期結構、再融資條款、可轉債條件：資料缺口，標記 n/a。

## Capital allocation & insider signal
**資本配置**：
- Capex：2022 -0.85 億、2023 -0.54 億、2024 -0.42 億、2025 -0.67 億 SEK；2026 Q1 僅 -0.03 億、Q2 -0.09 億，資本支出大幅收縮。
- 股利：無（dividendYield 0.0）。
- 買回：2025 年 -0.08 億 SEK，規模極小，可忽略。
- 增資：2023 年 +1.50 億、2024 年 +0.20 億、2025 年 +2.11 億、2026 Q2 單季 +1.30 億 SEK。2026 Q2 亦有 +1.54 億 SEK 債務發行（Q1）。
- 股本稀釋：Ordinary Shares 由 2025-06 的 2.71 億股增至 2026-06 的 3.05 億股（+12%，約 12 個月）；2025-12 的 2.97 億股至 2026-06 增加約 +2.7%；加權平均稀釋股數 2022 為 2.10 億股，2025 為 2.75 億股（+31%）。
- 債務償還：2025 年償還 1.58 億、發行 1.18 億 SEK，淨償還 0.40 億；2026 Q1 償還 1.04 億、發行 1.53 億，顯示債務週轉依賴再融資。

**內部人交易（6 個月）**：
- yfinance insider 端點回傳空陣列，過去 6 個月無內部人交易紀錄。
- 內部人持股比例 heldPercentInsiders 21.3%（2026-06 資料）。因無買賣紀錄，淨買賣金額為 0，相對市值（63.65 億 SEK）為 0%。
- 留意：空陣列可能代表真的無申報，也可能是資料源缺口，瑞典 MAR 制度下應有申報，建議人工比對 Finansinspektionen 公開資料。

**機構持股**：heldPercentInstitutions 17.6%。inst_holders 前三大持股數字極小（Shikiar 4.93 萬股，約 0.0001%），與 17.6% 機構持股比例不一致，視為資料缺口。

## Valuation
股價與市場數據（info / fast_info）：
- 現價 20.90 SEK（fast_info.last_price），前收 23.12 SEK，當日 -9.6%。
- 52 週區間 2.85 至 110.00 SEK，現價距 52 週高點 -81%。
- 50 日均線 28.63 SEK、200 日均線 33.12 SEK，現價分別低於 -27%、-37%。
- 市值 63.65 億 SEK；企業價值 EV 63.84 億 SEK；流通股 2.30 億股。

估值倍數：
- Trailing P/E：n/m（TTM EPS -0.74）。
- Forward P/E：-104.5（forwardEps -0.20），n/m。
- P/S（TTM）：22.9x。
- EV/Revenue：23.0x。
- P/B：6.6x（bookValue 3.166 SEK/股）。
- EV/EBITDA：-29.2x（EBITDA 為負），n/m。
- P/FCF：n/m（FCF 為負）。

分析師：2 位分析師，目標價 high 8.0、low 7.4、mean 7.7 SEK，recommendationKey 為 none。目標價均值為現價的 37%，代表市場定價大幅高於分析師估值，或分析師目標價未更新。Beta -0.66，參考價值低。

與同業比較（估計值，非 yfinance 數據，標示為估計）：半導體 RF / 光電細分（小型股）EV/Sales 中位數約 3–6x，P/B 約 2–4x，毛利率約 35–50%。SIVE 的 EV/Sales 23.0x 與 P/B 6.6x 均顯著高於估計區間，毛利率為負。

估值判讀：以基本面看，SIVE 的估值溢價很難由現有營收與獲利解釋，市場定價隱含對 AI datacenter 光電（InP 雷射）與衛星國防應用的成長期權。這部分屬敘事假設，無財務數據支撐。

## Key catalysts
- 下次財報：2026-11-26（yfinance earnings_dates，EPS 預估 -0.10 SEK）。此日期在分析基準日 2026-11-02 之後，為排程資料。
- 歷史 EPS 驚喜：近 4 次為 -22%、+63%、-25%、-18%（最近 4 期中有 3 期低於預期）；歷史長期 18 季中多數為未達預期。
- 近期營運變化：營收連續兩季下滑、毛利轉負、Capex 縮減、2026 年 Q1 與 Q2 分別完成債務發行與增資，顯示公司仍依賴外部融資。
- 增資或再融資：若無新增資金來源，以 2026 Q2 FCF -0.79 億 SEK 估算，現金 0.63 億 SEK 不足一個季度的燃燒量，後續增資或融資公告是最重要的近期事件。
- 業務催化：InP 光電與 AI datacenter 相關訂單、衛星與國防合約，目前數據中無訂單簿、指引或分部數據，標記為 n/a。
- 公司指引：yfinance 無公司 guidance 資料，標記為 n/a。

## Metrics table
| Metric | Latest | YoY | Sector median (估計) | Verdict |
|---|---|---|---|---|
| 營收 TTM (億 SEK) | 2.78 | -12.4% | n/a（小型 RF 股無標準值） | 弱 |
| 推算營收 2026 上半年 (億 SEK) | 1.16 | 約 -17% | n/a | 弱 |
| 毛利率 TTM | -7.6% | n/a | 35–50% | 極弱 |
| 營業利益率 2025（推算 EBIT） | -69% | n/a | 約 10–20% | 極弱 |
| 淨利率 TTM | -105.8% | n/a | 約 5–15% | 極弱 |
| ROE TTM | -28.6% | n/a | 約 10–15% | 弱 |
| FCF TTM (億 SEK) | -0.83 | n/a | 正值 | 極弱 |
| FCF margin 2025（推算） | -34% | n/a | 約 5–15% | 極弱 |
| FCF / NI | n/m（兩者皆負） | n/a | >0.9 | 不適用 |
| 現金 (億 SEK) | 0.63 | n/a | n/a | 弱 |
| 總債務 (億 SEK) | 1.82 | 2025-12 為 1.22 | n/a | 弱 |
| 淨債務 (億 SEK) | 1.00 | 2025-12 為 0.73 | n/a | 偏高 |
| 流動比率 | 1.64 | n/a | 約 1.5–2.5 | 中性 |
| Debt/Equity | 19.2% | n/a | 約 30–60% | 可接受 |
| 股本（億股） | 3.05 | +12%（12 個月） | n/a | 稀釋中 |
| Capex 2025 (億 SEK) | -0.67 | 2024 為 -0.42 | n/a | 中性 |
| 股息 | 0 | n/a | n/a | n/a |
| 內部人淨買賣 (6 個月) | 0（無紀錄） | n/a | n/a | 無訊號 |
| P/E TTM | n/m | n/a | 約 20–30x | n/a |
| P/S TTM | 22.9x | n/a | 約 3–6x | 極高 |
| EV/EBITDA | n/m | n/a | 約 15–20x | n/a |
| P/B | 6.6x | n/a | 約 2–4x | 偏高 |
| 分析師目標價均值 (SEK) | 7.7 | 現價 20.9，溢價約 171% | n/a | 偏離 |

## Red flags
- 毛利率為負（TTM -7.6%），2026 Q2 推算 Cost of Revenue 高於營收，代表產品層面尚未達到經濟規模。
- 現金 0.63 億 SEK 低於總債務 1.82 億 SEK，且單季 FCF 燃燒約 0.79 億 SEK，短期流動性依賴增資與借款。
- 債務自 2025-12 的 1.22 億增至 2026-06 的 1.82 億 SEK，總負債增加約 23%，利息費用上升。
- 2026 年 Q2 股本較 2025-06 增加約 12%，加權稀釋股數 2022–2025 增加 31%，股東稀釋風險高。
- 營收年減約 12%，2026 上半年推算年減約 17%，與長期成長敘事方向不一致。
- 股價距 52 週高點 -81%、低於 50 日與 200 日均線，但 52 週漲幅仍高達 +470%（info.52WeekChange），價格波動劇烈。
- 分析師目標價均值 7.7 SEK，僅 2 位覆蓋，遠低於現價，市場估值與分析師估值脫節。
- 內部人無交易紀錄，無法從內部人行為取得訊號。
- 有形淨資產為負（-1.10 億 SEK），股東權益完全依賴商譽或無形資產支撐。

## 資料缺口與一致性檢核
- fast_info 的 market_cap、shares、ten_day_average_volume 為 null，且回報 Yahoo 端點 403 錯誤，但 last_price 20.90 SEK 與 info.currentPrice 一致。
- 年度利潤表不回傳 Total Revenue 欄位，營收為推算值。
- 2025-09-30 季度資料全部為 null，TTM 季度加總需以 info 為準。以 info 的 TTM 營收 2.78 億 SEK 反推 2025 Q3 推算營收約 0.82 億 SEK，與 Q4 0.81 億 SEK 合理，但 Q3 原始資料缺失。
- earnings_dates 的「Reported EPS」與季度利潤表的稀釋 EPS 不一致（例如 2026-05-29 公告 EPS -0.12，季度表 2026-06-30 為 -0.38；2026-02-26 公告 -0.04，季度表 2026-03-31 為 -0.14），可能為不同口徑（調整後或不同股數基礎），需以公司公告為準。
- 現金：info.totalCash 0.63 億 SEK，淨債務 1.00 億 SEK 推算之現金為 0.82 億（1.82 - 1.00），兩者不符。
- info.operatingMargins（-217%）與季度 EBIT 加總不符，已改用季度數據。
- inst_holders 的持股數與 heldPercentInstitutions 17.6% 不符。
- 年度 Capex 2025-03 季度為正值 +0.56 億，與其他季度方向不一致，可能為資料錯誤，未納入判讀。
- 本報告無公司正式 guidance、分部營收、訂單簿、到期債務表等資料，這些項目皆標記為 n/a。
- 本報告無任何資料晚於 2026-11-02 的數據被採用；2026-11-26 財報日為排程資料，未包含實際結果。

FUNDAMENTALS REPORT COMPLETE
