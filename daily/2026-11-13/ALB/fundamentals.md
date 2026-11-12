# Fundamentals — ALB (Albemarle Corporation) as of 2026-11-13

資料來源與時點說明：
- 財報（annual / quarterly income、balance sheet、cashflow）與 insider、holders、earnings_dates 皆由 `pipeline/tools/yf` 回傳；最新財季為 2026-09-30（Q3 2026，財報發布於 2026-11-04 盤後，早於 as-of）。
- 報價與 info/fast_info 來源標示 `source: cache`（cached_at 2026-11-12T15:01–15:04 UTC，盤中價），as-of 當日（2026-11-13）收盤資料未取得。
- 貨幣單位：USD，以 B（十億美元）/ M（百萬美元）標示，未使用億。
- 本報告未晚於 as-of 的財務數據。`info.exDividendDate`（2026-12-18）與 `dividendDate`（2027-01-04）晚於 as-of，未作為已發生事件採用。

## Executive summary
ALB 在 2024–2025 年陷入虧損（2025 年 GAAP 稀釋 EPS -5.76，淨利歸屬普通股東 -677M），但 2026 年前三季營收與獲利快速回升，TTM 營收 6.15B、TTM 稀釋 EPS 約 4.34（GAAP）、調整後 EPS 9 個月合計 9.28，且負債已從 YE2025 的 3.30B 降至 Q3 2026 的 1.88B，淨負債幾乎歸零（35M），財務體質明顯改善。估值方面，Yahoo 口徑 trailing P/E 22.7x、forward P/E 11.1x、EV/EBITDA 8.2x，相較 2026-05 內部人賣出價（約 $183–185）已下跌約 49%，但 TTM 獲利中約 66% 來自權益法投資收益，盈餘品質與 2.24B 特別股及 167M/年的特別股股利仍是主要扣分項。

## Revenue & profitability

**營收趨勢（USD）**

| 年度 | 營收 | 毛利 | 營業利益 | 淨利（含 NCI） | 歸屬普通股淨利 | 稀釋 EPS |
|---|---|---|---|---|---|---|
| FY2022 | 7.32B | 3.07B | 2.48B | 2.82B | 2.69B | 22.84 |
| FY2023 | 9.62B | 1.19B | 0.19B | 1.67B | 1.57B | 13.36 |
| FY2024 | 5.38B | 0.06B | -0.64B | -1.14B | -1.32B | -11.20 |
| FY2025 | 5.14B | 0.67B | 0.07B | -0.47B | -0.68B | -5.76 |

- 3 年營收 CAGR（FY2022→FY2025）：約 **-11.1%**；2 年（FY2023→FY2025）：約 **-26.9%**。資料中 FY2021 營收為 None，無法計算 4–5 年 CAGR。
- 2026 季度營收：Q1 1.43B、Q2 1.74B、Q3 1.55B（9M 合計 4.73B）。Q3 2026 YoY +18.8%（1.55B vs Q3 2025 的 1.31B），與 `info.revenueGrowth` 0.188 一致。
- TTM 營收 6.15B，較 FY2025 的 5.14B 高 +19.6%，顯示景氣回升。
- 分部營收：yfinance 未提供分部數字。業務描述列出三大分部 Energy Storage（鋰化合物）、Specialties（溴素與特化品）、Ketjen（觸媒）；各分部營收與利潤 **DATA_UNAVAILABLE**。

**獲利能力（TTM，計算值）**
- 毛利率（TTM）：約 25.8%（Yahoo grossMargins 26.2%）；FY2025 為 13.0%。
- 營業利益率（TTM，由季度 Operating Income 加總）：約 16.3%（Yahoo operatingMargins 17.1%）；FY2025 為 1.3%。
- 淨利率（歸屬普通股，TTM）：約 8.4%（TTM 514.9M / 6.15B）。
- ROE：Yahoo returnOnEquity 7.05%；以普通股權益平均值計算約 6.4%。
- ROIC（估算）：TTM EBIT 約 694M × (1-20%) / Q3 2026 Invested Capital 10.19B ≈ **5.4%**（假設稅率 20%，為粗估）。
- 盈餘品質警示：TTM 淨利（含 NCI）743M 中，權益法投資收益（Earnings From Equity Interest）為 494M，占比約 **66%**。2023 年權益法收益更高達 1.85B，佔當年淨利 1.67B 以上，顯示獲利高度依賴合資企業表現。
- 特殊項目：FY2025 Impairment of Capital Assets 426.7M（Q3 2025 181.1M、Q4 2025 245.6M）；Q1 2026 Special Income Charges -120.9M，Q3 2026 -8.0M。
- GAAP 與調整後 EPS 差異：Q3 2026 GAAP 稀釋 EPS 2.15，調整後（earnings_dates）2.58。

## Cashflow & balance sheet

**現金流（USD）**

| 項目 | FY2022 | FY2023 | FY2024 | FY2025 | TTM（Q4'25–Q3'26） |
|---|---|---|---|---|---|
| 營業現金流（OCF） | 1.91B | 1.33B | 0.69B | 1.28B | 1.85B |
| 資本支出（Capex） | 1.26B | 2.15B | 1.68B | 0.59B | 0.41B |
| 自由現金流（OCF − Capex） | 0.65B | -0.83B | -0.99B | 0.69B | 1.44B |
| FCF 利潤率 | 8.8% | -8.6% | -18.5% | 13.5% | 23.5% |

- FCF / 淨利（歸屬普通股）：FY2025 因淨利為負不適用；TTM 為 1.44B / 0.51B ≈ **2.8x**，高於 0.9 健康門檻，但需扣除權益法非現金收益後判讀。
- 現金品質：TTM 權益法收益 494M，同期自合資企業收到的股利（Dividend Received CFO）為 373M，現金轉換率尚可但非全部由自身營運產生。
- Yahoo 口徑 freeCashflow 為 1.25B（與本報告 TTM 計算 1.44B 有差異，定義不同，已分別列示）。

**資產負債表（USD，Q3 2026 為 2026-09-30）**

| 項目 | YE2024 | YE2025 | Q3 2026 |
|---|---|---|---|
| 現金及約當現金 | 1.19B | 1.62B | 1.85B |
| 總債務（Total Debt） | 3.62B | 3.30B | 1.88B |
| 淨負債（Net Debt） | 2.32B | 1.58B | 0.04B |
| 流動資產 | 3.84B | 4.01B | 4.23B |
| 流動負債 | 1.97B | 1.80B | 1.81B |
| 股東權益（含特別股） | 9.96B | 9.53B | 10.54B |
| 特別股權益 | 2.24B | 2.24B | 2.24B |
| 普通股權益 | 7.73B | 7.30B | 8.31B |
| 總資產 | 16.61B | 16.37B | 16.08B |

- 流動比率（Q3 2026）：2.34x（Yahoo currentRatio 2.344）；速動比率：約 1.44x。
- 負債權益比（總債務 / 股東權益）：約 0.18x（Yahoo debtToEquity 18.5%）。
- 淨負債 / TTM EBITDA：Yahoo ebitda 1.70B，淨負債 0.04B，比率約 0.02x。
- 償債：Q1 2026 償還債務 1.31B（Repayment of Debt -1,307.8M），同季出售事業現金流入 525.2M（Sale of Business）。
- 存貨：Q3 2026 為 1.39B，較 YE2025 的 1.18B 增加約 18%，需留意週轉。
- 其他非流動負債：Q3 2026 為 1.14B，YE2025 僅 0.07B；tool 資料未說明重分類原因，列為 **資料缺口**（deferred revenue 與 other liabilities 間之重分類需對照 10-Q 確認）。

## Capital allocation & insider signal

**資本配置**
- Capex：FY2022 1.26B → FY2023 2.15B（高峰）→ FY2024 1.68B → FY2025 0.59B → TTM 0.41B。TTM Capex / D&A（TTM 642M）= 0.63x，低於 1.0，屬於投資明顯收縮，長期產能維持需要留意。
- 股利：普通股每股年化 $1.64（季配 $0.41），TTM 普通股股利支出 191M，另有特別股股利 167M/年（41.7M/季）。TTM 股利合計 358M。
- 股利覆蓋：以 TTM FCF 1.44B 計，普通股股利覆蓋 7.6x，合計股利覆蓋 4.0x；以歸屬普通股淨利計，普通股股利覆蓋 2.7x。`payoutRatio` 0.39（Yahoo）。
- 買回：現金流量表無 repurchase 項目，**無買回**。股本由 FY2022 117.2M 股增至 Q3 2026 118.0M 股，年化稀釋約 0.1%（主要為 SBC，TTM SBC 約 37M）。
- 特別股：2024 年發行 2.24B 特別股（CF 2024 Preferred Stock Issuance 2.24B），股利為財務主要負擔之一。

**Insider 活動（近 6 個月，約 2026-05-13 至 2026-11-13）**
- 公開市場賣出：1 筆。CEO Jerry Kent Masters Jr. 2026-05-15 賣出 16,393 股，價格 $183.12–184.52，金額約 $3.01M。
- 公開市場買進：0 筆。
- 獎勵性股權（非市場交易）：2026-09 有 Norris、Mummert、Gagarinas、Hood 等 Officer 之 Stock Award；7 月董事會 RSU 授予。
- 金額相對市值：$3.01M / 市值 $11.12B ≈ **0.03%**，訊號強度低。
- 內部人持股：insidersPercentHeld 0.21%。
- 窗口外參考：2026-03-12 CEO 股票贈與 30,716 股（$5.0M），2026-02 Norris、Anderson 賣出，均早於 6 個月窗口。

**機構持股（major_holders、inst_holders）**
- 機構持股比例 Yahoo 顯示 108.2%，超過 100%，屬資料重複計算，**不採用**；institutionsCount 1,273。
- 前十大（2026-06-30 或 2026-09-30）：Capital World 8.39%、BlackRock 8.05%、Vanguard Capital Management 6.53%、Vanguard Portfolio Management 5.45%、State Street 4.66%、FMR 3.91%（季增 +71.6%）、Geode 2.66%、Morgan Stanley 2.45%、Primecap 2.25%、Bank of America 2.16%。
- 空單：Yahoo sharesShort 141,902 股，但上月為 11.76M 股，兩者差距為數量級錯誤，**空單資料不可用**（DATA_UNAVAILABLE）。

## Valuation

**價格與估值（as-of 最新可得報價，2026-11-12 盤中，USD）**
- 價格：$94.26（info.regularMarketPrice 94.255；fast_info.last_price 94.34）。
- 市值：$11.12B（118.0M 股 × $94.26 ≈ $11.12B，與 Yahoo marketCap 11.12B 吻合）。
- 企業價值：Yahoo enterpriseValue $13.99B；以 Q3 2026 資產負債表自算（市值 + 總債務 − 現金 + 特別股 + NCI）約 $13.66B。
- Trailing P/E：Yahoo 22.7x（trailingEps 4.15）；以 GAAP 稀釋 EPS 四季加總 4.34 計約 21.7x。
- Forward P/E：11.1x（forwardEps 8.46，pegRatio 0.79）；以 FY2026 consensus EPS 10.51 計，P/E 約 9.0x。
- EV/EBITDA：8.2x（Yahoo，EBITDA TTM 1.70B）；BS 自算約 8.1x。
- EV/Revenue：2.27x；P/S（trailing）：1.81x。
- P/FCF：Yahoo 口徑（FCF 1.25B）約 8.9x；本報告 TTM FCF 1.44B 計約 7.7x。
- P/B：1.34x（bookValue $70.39/股）。
- 股價位置：52 週區間 $89.77–$221.00；距 52 週低點 +5.0%、距高點 −57.4%；50 日均 $105.19、200 日均 $146.54，現價低於兩條均線。

**分析師共識（Yahoo，21 位）**
- recommendationMean 1.86（buy 區間）；平均目標價 $139.35（中位數 $135.0），最高 $211.0，最低 $83.28；目標均價相對現價 +47.8%。以上為外部共識，不構成本報告結論。

**與產業中位數比較（估計）**
- 工具未提供同業中位數，下表為 Specialty Chemicals 一般區間之 **估計值，非工具資料，僅供參考**。

## Key catalysts
- **已發生**：Q3 2026 財報 2026-11-04（盤後），調整後 EPS $2.58 vs 預估 $2.53（+2.0%），GAAP 稀釋 EPS $2.15；Q2 2026 調整後 EPS $3.75 vs 預估 $3.24（+15.7%）；Q1 2026 調整後 $2.95 vs 預估 $1.31（+124.6%）。
- **下次財報**：Yahoo 排程 2027-02-10（盤後），Q4 2026 EPS 預估 $1.27（排程性質，屬 as-of 之後）。
- **股利**：最近一次配息 2026-09-11，每股 $0.41；季配。
- **最新 FY2026 consensus**：EPS 10.51（Yahoo epsCurrentYear），FY2027 forward EPS 8.46。
- **指引（guidance）**：yfinance 未提供管理層指引文字，**DATA_UNAVAILABLE**。
- **鋰價與分部**：工具無鋰碳酸鹽／氫氧化鋰價格與分部營收數據，**DATA_UNAVAILABLE**，無法量化 Energy Storage 對獲利的敏感度。
- **資本支出**：TTM capex 僅 0.41B，後續擴產計畫（如 Q3 2026 建設中資產）**DATA_UNAVAILABLE**。
- **治理**：Yahoo governance risk（1–10 scale，高值為較高風險）：auditRisk 9、shareHolderRightsRisk 8、boardRisk 7、overallRisk 7、compensationRisk 3。

## Metrics table

金額單位：USD（B = 十億、M = 百萬）。除特別註明外，「Latest」為 Q3 2026（2026-09-30）或 TTM（至 2026-09-30）。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收（TTM，USD B） | 6.15 | +19.6%（vs FY2025） | n/a | 回升中 |
| 季營收 Q3 2026（USD B） | 1.55 | +18.8% | n/a | 成長 |
| 3 年營收 CAGR（FY22–25） | -11.1% | n/a | 約 +3% 至 +5%（估計） | 弱 |
| 毛利率（TTM） | 25.8% | FY25 13.0% | 約 25–30%（估計） | 中性 |
| 營業利益率（TTM） | 16.3% | FY25 1.3% | 約 12–15%（估計） | 良好（已恢復） |
| 淨利率（歸屬普通股，TTM） | 8.4% | FY25 -13.2% | 約 8–10%（估計） | 中性 |
| ROE（Yahoo） | 7.0% | n/a | 約 10%（估計） | 偏弱 |
| ROIC（估算） | 5.4% | n/a | 約 8%（估計） | 偏弱 |
| FCF（TTM，USD B） | 1.44 | FY25 0.69 | n/a | 強 |
| FCF 利潤率（TTM） | 23.5% | FY25 13.5% | 約 8–12%（估計） | 強 |
| FCF / 淨利（TTM） | 2.8x | n/a | >0.9 健康 | 健康，但含權益法收益 |
| 總債務（USD B） | 1.88 | YE25 3.30 | 約 1.0–2.0（估計） | 大幅改善 |
| 淨負債（USD B） | 0.04 | YE25 1.58 | n/a | 近乎無淨負債 |
| 淨負債 / EBITDA | ~0.02x | n/a | 約 1.5x（估計） | 優 |
| 流動比率 | 2.34x | n/a | 約 2.0x（估計） | 優 |
| 速動比率 | 1.44x | n/a | 約 1.2x（估計） | 良 |
| 負債權益比 | 0.18x | n/a | 約 0.4x（估計） | 優 |
| 現金（USD B） | 1.85 | YE25 1.62 | n/a | 充足 |
| Capex（TTM，USD B） | 0.41 | FY25 0.59 | n/a | 偏低（Capex/D&A 0.63x） |
| 股利（TTM，普通股，USD M） | 191 | n/a | n/a | 覆蓋 7.6x（FCF） |
| 特別股股利（年化，USD M） | 167 | FY25 167 | n/a | 負擔 |
| 股票回購（TTM） | 0 | n/a | n/a | 無 |
| 內部人淨買賣（6 個月） | -$3.0M（僅 1 筆賣出） | n/a | n/a | 訊號弱 |
| 本益比（Trailing，Yahoo） | 22.7x | n/a | 約 20x（估計） | 中性 |
| 本益比（Forward） | 11.1x | n/a | 約 16x（估計） | 低於同業估計 |
| EV/EBITDA | 8.2x | n/a | 約 12x（估計） | 低於同業估計 |
| P/FCF（Yahoo / 本報告） | 8.9x / 7.7x | n/a | 約 18x（估計） | 低於同業估計 |
| P/S（trailing） | 1.81x | n/a | 約 2.0x（估計） | 中性 |
| P/B | 1.34x | n/a | 約 2.0x（估計） | 中性 |
| 殖利率 | 1.71% | n/a | 約 2%（估計） | 中性 |
| Beta | 1.36 | n/a | 約 1.0（估計） | 波動偏高 |
| 股價 vs 200 日均 | -35.7% | n/a | n/a | 弱勢 |
| 分析師平均目標價 | $139.35（+47.8%） | n/a | n/a | 外部共識，非本報告結論 |

## Red flags
- **獲利依賴權益法收益**：TTM 淨利（含 NCI）743M 中 494M（約 66%）來自合資企業權益法收益，非現金獲利直接貢獻；FY2023 亦有 1.85B 權益法收益。
- **連續虧損與減損**：FY2024 淨利 -1.14B、FY2025 -0.47B（歸屬普通股 -0.68B），FY2025 資本資產減損 427M。
- **特別股負擔**：2.24B 特別股，年化股利 167M，佔 TTM FCF 約 12%，且侵蝕歸屬普通股淨利。
- **營收週期大幅波動**：FY2022 7.32B → FY2024 5.38B（3 年 CAGR -11.1%），景氣敏感度高。
- **Capex 低於折舊**：TTM Capex / D&A 0.63x，若長期維持，產能與競爭力有風險。
- **存貨增加**：Q3 2026 存貨 1.39B，較 YE2025 增 18%，與營收回升節奏需對照週轉天數確認。
- **其他非流動負債跳升**：Q3 2026 1.14B（YE2025 0.07B），原因 tool 資料未揭露，需補充確認。
- **治理風險評分高**：Yahoo auditRisk 9（1–10，高值風險），overallRisk 7。
- **股價趨勢弱勢**：現價 $94.26 低於 50 日（$105.19）與 200 日（$146.54）均線，較 52 週高點 $221.00 下跌約 57%。
- **資料品質警示**：機構持股比例 108% 為重複計算；空單股數量級不一致；Yahoo info 報價為 cache 盤中價，無 2026-11-13 收盤資料。

FUNDAMENTALS REPORT COMPLETE
