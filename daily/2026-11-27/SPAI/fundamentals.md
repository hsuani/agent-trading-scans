# Fundamentals — SPAI as of 2026-11-27

資料來源說明：本次所有數據均來自 `pipeline/tools/yf` 與 repo cache（`source: cache`，info 與 fast_info 的 cached_at 為 2026-11-26）。財報區間最新至 2026-09-30（Q3 2026），Q3 財報於 2026-11-16 公布，早於 as-of 日期。未發現 as-of 日期之後的資料。幣別為 USD，表格金額以 USD M（百萬美元）標示。

## Executive summary

Safe Pro Group（SPAI）目前仍處於深度虧損與現金消耗階段：TTM 營業利潤率為 -208.7%，TTM 自由現金流約 -9.28M USD，9 月底現金 7.78M USD，依 2026 年前三季平均燃燒速度估計約 10 至 11 個月的現金跑道，未計入後續融資。2026 年營收於 Q3 明顯跳升至 2.68M USD（YoY 約 +2,539%），但 2025 全年營收仍較 2024 下滑 72.0%，營收的持續性無法從工具數據確認。以 P/S 8.31x、EV/Revenue 7.0x 與 P/B 3.98x 估算，相對於其虧損與燒錢速度估值偏高；目前股價 2.23 USD 低於 50 日與 200 日均線，且接近 52 週低點 2.05 USD。基本面面向的結論：財務體質脆弱、估值吸引力不足。

## Revenue & profitability

**營收趨勢**
- 年度營收（USD M）：2022 為 1.15、2023 為 0.92、2024 為 2.17、2025 為 0.61。2022→2025 的 3 年 CAGR 約 -19.2%，2024→2025 年減 72.0%。年度數字波動極大，4 年區間內沒有穩定成長軌跡。
- 季度營收（USD M）：2025Q3 為 0.10、2025Q4 為 0.23、2026Q1 為 1.22、2026Q2 為 1.33、2026Q3 為 2.68。Q3 2026 對 Q3 2025 的 YoY 為 26.4 倍（revenueGrowth 欄位 25.392，即 +2,539%）。
- TTM 營收（由季度加總）為 5.46 USD M，與 info.totalRevenue 5,456,587 一致。
- 工具輸出未提供分部（segment）營收拆分。info.longBusinessSummary 描述業務包含防爆物（EOD/UXO 處理產品）、防彈背心與頭盔、以及無人機巡檢與 AI 影像分析服務，但未給出各項目的金額比重，此部分標為 DATA_UNAVAILABLE。2026 年營收跳升的來源（新產品、併購、或一次性專案）工具數據無法判定。
- 2025 年上半年（2025Q1、Q2）季度財報欄位為空值，無法做完整季度趨勢。

**獲利能力**
- 毛利率：2022 為 45.1%、2023 為 33.9%、2024 為 41.8%、2025 為 33.3%。2026 季度毛利率為 Q1 68.1%、Q2 64.0%、Q3 71.2%，TTM 毛利率由季度加總計算為 67.1%（info.grossMargins 為 68.97%，兩者差異來自計算口徑）。2026 年毛利率明顯高於 2025 年，但營收基數極小，數字對單一訂單的敏感度高。
- 營業利潤率：TTM 為 -208.7%（info.operatingMargins -2.0867 一致）。營業費用 2025 年為 13.92M USD，2026 前三季合計約 11.39M USD（Q1 3.75、Q2 4.12、Q3 3.52）。
- 淨利率：TTM 為 -200.5%（TTM 淨利 -10.94M USD）。EPS：TTM -0.53（info.trailingEps），2026 季度 EPS 為 Q1 -0.14、Q2 -0.15、Q3 -0.08。
- 研發費用：2025 年 0.39M USD；2026 前三季 0.85M USD（Q1 0.36、Q2 0.19、Q3 0.30），佔季度營收比例隨營收波動，Q3 約 11%。
- ROE：-110.3%（info.returnOnEquity）；ROA：-60.5%（info.returnOnAssets）。ROIC 為負值，無法有意義地計算（NOPAT 為負）。以 BS 推算的投入資本約 3.8M USD（股東權益 11.39 + 有息負債 0.17 − 現金 7.78），ROIC 數值無參考意義。

## Cashflow & balance sheet

**現金流品質**
- 營業現金流（OCF）：2022 為 +1.08M、2023 為 -2.00M、2024 為 -4.10M、2025 為 -6.22M USD。TTM OCF 為 -8.80M USD（與 info.operatingCashflow 一致）。
- 自由現金流（FCF = OCF + capex）：2025 年 -6.46M USD。2026 季度 FCF 為 Q1 -1.26M、Q2 -2.97M、Q3 -2.38M，前三季合計 -6.61M。TTM FCF 由季度加總為 -9.28M USD，FCF 利潤率為 -170.1%。
- 注意：info.freeCashflow 為 -5,416,506，與季度加總的 -9.28M 不一致，工具來源可能使用不同口徑，本報告採季度加總值並標示差異。
- FCF / NI：兩者皆為負值（TTM FCF -9.28M / TTM NI -10.94M = 0.85），比率於此情境無經濟意義。FCF 轉正前無法滿足「>0.9 健康」的判準，應視為不合格。
- 資本支出（capex）：2025 年 -0.24M；2026 前三季 -0.47M，其中 Q3 單季 -0.30M，較前幾季明顯增加。
- 股權激勵（SBC）：2025 年 6.91M USD，超過同年營收（0.61M）；2026 前三季 3.60M USD。SBC 為非現金成本的主要來源之一，對股東稀釋影響大。

**資產負債表**
- 現金及約當現金：2024/12 為 1.97M、2025/12 為 16.79M、2026/03 為 14.80M、2026/06 為 10.23M、2026/09 為 7.78M USD。2026 前三季現金減少 9.01M USD（由 16.79M 降至 7.78M）。
- 有息負債（BS Total Debt）：2026/09 為 0.17M USD；info.totalDebt 為 0.60M USD，差額可能為租賃負債，工具未明示，標示為待確認。
- 淨現金：以 BS 口徑約 7.61M USD（現金 7.78 − 有息負債 0.17）。以 info 口徑約 7.18M USD（現金 − totalDebt 0.60）。
- 流動比率（current ratio）：5.24（2026/09 流動資產 12.01M / 流動負債 2.29M）。2025/12 為 14.33。營運資金由 2025/12 的 16.68M 降至 2026/09 的 9.72M。
- 負債/權益：info.debtToEquity 為 5.293，此欄位為百分比格式，換算為 0.053x（603,054 / 11,393,987）。
- 股東權益：2026/09 為 11.39M USD，每股淨值 0.56 USD（info.bookValue）。
- 總資產：2026/09 為 13.83M USD，2025/12 為 19.11M USD。
- 結論：短期流動性強（流動比率高、負債極低），但絕對現金水位小、燒錢速度快，屬於「短期償債風險低、但融資依賴度高」的結構。

**跑道估計（推導值，非工具直接輸出）**
- 2026 前三季平均 FCF 燃燒約 0.73M USD/月（6.61M / 9）。以 9 月底現金 7.78M USD 估算，跑道約 10.6 個月（約至 2027 年中至下半年），未計入 Q4 2026 燃燒、融資、或營收提升帶來的改善。

## Capital allocation & insider signal

**資本配置**
- 股利：無（info.dividendRate 為 None，dividendYield 為 0.0）。
- 買回：2025 年 -0.61M USD；2026 季度 Q1 -0.73M、Q2 -1.60M、Q3 -0.09M，前三季合計 -2.42M USD。在 FCF 為負、現金快速下降的情況下進行買回，原因不明（可能為員工股權相關的稅務代扣等非典型股票回購，工具無法判定），列為待確認事項。
- 股權融資（Common Stock Issuance）：2024 年 4.67M、2025 年 19.71M USD（2025Q3 7.82M、2025Q4 11.90M）。2025 年為主要資金來源。
- 股數稀釋：2024/12 流通股數 14.53M，2025/12 為 20.74M（+42.7%），2026/09 為 20.34M（相對 2025/12 減少 1.9%，但仍高於 2025/09 的 18.85M）。過去兩年稀釋幅度大。
- 負債：2025 年發行 0；2024 年 Issuance of Debt 0.51M，淨債務規模極小。

**內部人交易（6 個月窗口：2026-05-27 至 2026-11-27）**
- 唯一公開市場交易：CEO Daniyel Erdberg 於 2026-09-09 賣出 1,000,000 股，成交價 4.00 USD，總額約 4.00M USD。以目前市值 45.36M USD 計，約佔 8.8%。以 2.23 USD 現價計，該筆出脫的成交價高於現價約 44%。
- 其他紀錄為股權獎勵（Stock Award）與贈與（Stock Gift），無市場買賣：2026-05-01 Brian William Mack 獲 300,000 股獎勵；2026-04-01 COO Jarret Daniel Mathews 獲 20,000 股；2026-03-06 CEO 贈與 9,000 股。
- 6 個月內無內部人公開市場買進紀錄。淨交易方向：淨賣出（以市場交易計）。
- 持股結構：內部人持股比例 44.16%（major_holders.insidersPercentHeld），機構持股 11.20%，機構持股占浮動股比例 20.05%，機構數量 33。浮動股數 11.54M 股，佔總流通股數 20.34M 的約 57%。

## Valuation

以 2.23 USD 現價計算（市值 45.36M USD、企業價值 EV 38.19M USD）：

- 本益比（trailing P/E）：n/a（EPS 為負）。
- 預估本益比（forward P/E）：n/a（forwardEps 為 None）。
- P/S（TTM）：8.31x。
- EV/Revenue（TTM）：7.00x。
- EV/EBITDA：-3.46x（EBITDA 為 -11.05M USD，為負值，倍數無意義，判定為 n/a）。
- P/FCF：n/a（FCF 為負）。
- P/B：3.98x（每股淨值 0.56 USD）。
- 同業中位數：DATA_UNAVAILABLE（工具未提供同業估值數據，本報告不估計數字）。
- 技術面參考（非基本面，僅作估值背景）：股價 2.23 USD，50 日均線 3.50 USD、200 日均線 4.25 USD，股價低於兩條均線；52 週區間 2.05 至 6.70 USD；beta 3.91。
- 分析師目標價：平均 10.67 USD（targetMeanPrice），來自 3 位分析師（numberOfAnalystOpinions 3），recommendationKey 為 strong_buy。覆蓋家數少，目標價與現價的差距高達約 378%，此數字僅作為參考，不宜視為估值依據。
- 估值判讀：以 P/S 8.31x 與 P/B 3.98x 配合 -200% 淨利率，在沒有明確營收持續性證明的情況下，估值偏高。基本面不支持估值擴張，目前價格反映的更多是營收跳升的可能性，而非已實現的獲利能力。

## Key catalysts

- 上次財報：2026-11-16（Q3 2026），EPS 實際 -0.08 對 預估 -0.14，超預期 +44.8%。Q3 營收 2.68M USD、毛利率 71.2%，為 2026 年最佳單季。
- 下次財報日期：DATA_UNAVAILABLE（工具輸出未提供下次財報日期）。
- 營收持續性：2026 年 Q1 至 Q3 營收由 1.22M 增至 2.68M USD。若 Q4 2026 能維持此水準，TTM 營收與毛利改善；若為一次性專案，2027 年可能回落。工具數據無法判定，需在財報電話會議或 10-Q 中確認。
- 融資事件：現金跑道約 10 至 11 個月，未來 6 至 12 個月內極可能需要再次股權融資，屬於潛在的稀釋催化劑。
- 管理層與內部人：CEO 在 2026-09 出售 1M 股，屬於重要的負面訊號，後續 Form 4 申報值得追蹤。
- 無公開的管理層年度指引（guidance）數據，此項標為 DATA_UNAVAILABLE。

## Metrics table

金額單位：USD M（百萬美元）。比率以 % 或 x 表示。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 市值 (USD M) | 45.36 | n/a | DATA_UNAVAILABLE | 小型股，流動性與波動性高 |
| 企業價值 EV (USD M) | 38.19 | n/a | DATA_UNAVAILABLE | 現金佔市值約 17% |
| TTM 營收 (USD M) | 5.46 | 季度 Q3 YoY +2,539% | DATA_UNAVAILABLE | 2026 年跳升，持續性未證實 |
| 2025 年度營收 (USD M) | 0.61 | -72.0% (vs 2024 2.17) | DATA_UNAVAILABLE | 年度大幅下滑 |
| 營收 3 年 CAGR (2022-2025) | -19.2% | n/a | DATA_UNAVAILABLE | 負成長 |
| 毛利率 TTM | 67.1% (計算) / 69.0% (info) | 2025 年度 33.3%，2024 年度 41.8% | DATA_UNAVAILABLE | 2026 年改善明顯 |
| 營業利潤率 TTM | -208.7% | n/a | DATA_UNAVAILABLE | 嚴重虧損 |
| 淨利率 TTM | -200.5% | n/a | DATA_UNAVAILABLE | 嚴重虧損 |
| ROE | -110.3% | n/a | DATA_UNAVAILABLE | 負值，不合格 |
| ROA | -60.5% | n/a | DATA_UNAVAILABLE | 負值，不合格 |
| ROIC | n/a（NOPAT 為負） | n/a | DATA_UNAVAILABLE | 無法評估 |
| 營業現金流 TTM (USD M) | -8.80 | 2025 年度 -6.22 | DATA_UNAVAILABLE | 持續燒錢 |
| 自由現金流 TTM (USD M) | -9.28 (季度加總) / -5.42 (info) | 2025 年度 -6.46 | DATA_UNAVAILABLE | 持續為負，口徑待確認 |
| FCF 利潤率 TTM | -170.1% | n/a | DATA_UNAVAILABLE | 不合格 |
| FCF / NI | 0.85（雙負值，無意義） | n/a | DATA_UNAVAILABLE | 不合格 |
| 現金及約當現金 (USD M) | 7.78（2026/09） | 2025/12 為 16.79 | DATA_UNAVAILABLE | 現金快速下降 |
| 有息負債 (USD M) | 0.17（BS）/ 0.60（info） | n/a | DATA_UNAVAILABLE | 負債極低 |
| 淨現金 (USD M) | 約 7.61（BS 口徑） | 較 2025/12 (約 16.59) 下降約 9.0 | DATA_UNAVAILABLE | 仍為淨現金 |
| 流動比率 | 5.24 | 2025/12 為 14.33 (17.93/1.25) | DATA_UNAVAILABLE | 短期償債佳 |
| 負債/權益 (D/E) | 0.05x（info 5.293%） | n/a | DATA_UNAVAILABLE | 極低 |
| 營運資金 (USD M) | 9.72（2026/09） | 2025/12 為 16.68 | DATA_UNAVAILABLE | 下降中 |
| 股東權益 (USD M) | 11.39（2026/09） | 2025/12 為 17.72 | DATA_UNAVAILABLE | 持續縮水 |
| 流通股數 (M 股) | 20.34（2026/09） | 2024/12 為 14.53，2025/12 為 20.74 | DATA_UNAVAILABLE | 稀釋嚴重 |
| 股權融資 (USD M) | 2025 年 19.71 | 2024 年 4.67 | DATA_UNAVAILABLE | 依賴外部資金 |
| 買回 (USD M) | 2026 前三季 2.42 | 2025 年 0.61 | DATA_UNAVAILABLE | 與燒錢情境不符，待確認 |
| 股利 | 無 | n/a | DATA_UNAVAILABLE | 不適用 |
| SBC (USD M) | 2025 年 6.91；2026 前三季 3.60 | 2025 年為 2024 年 2.85 的 2.4 倍 | DATA_UNAVAILABLE | 非現金成本偏高 |
| 資本支出 (USD M) | 2026 前三季 0.47 | 2025 年 0.24 | DATA_UNAVAILABLE | 投資擴張初期 |
| 本益比 trailing P/E | n/a（EPS -0.53） | n/a | DATA_UNAVAILABLE | 不適用 |
| 預估本益比 forward P/E | n/a | n/a | DATA_UNAVAILABLE | 不適用 |
| P/S (TTM) | 8.31x | n/a | DATA_UNAVAILABLE | 偏高 |
| EV/Revenue (TTM) | 7.00x | n/a | DATA_UNAVAILABLE | 偏高 |
| EV/EBITDA | n/a（EBITDA -11.05M，為負值） | n/a | DATA_UNAVAILABLE | 不適用 |
| P/FCF | n/a（FCF 為負） | n/a | DATA_UNAVAILABLE | 不適用 |
| P/B | 3.98x | n/a | DATA_UNAVAILABLE | 偏高 |
| 內部人淨交易 (6 個月) | 賣出 1.0M 股，約 4.00M USD（8.8% 市值） | n/a | DATA_UNAVAILABLE | 負面訊號 |
| 內部人持股比例 | 44.16% | n/a | DATA_UNAVAILABLE | 集中度高 |
| 機構持股比例 | 11.20% | n/a | DATA_UNAVAILABLE | 機構覆蓋低 |
| Beta | 3.91 | n/a | DATA_UNAVAILABLE | 波動性極高 |
| 股價 / 50 日均線 / 200 日均線 | 2.23 / 3.50 / 4.25 USD | n/a | DATA_UNAVAILABLE | 低於兩條均線 |
| 52 週區間 (USD) | 2.05 至 6.70 | n/a | DATA_UNAVAILABLE | 接近低點 |
| 分析師目標價 (USD，3 位) | 10.67 | n/a | DATA_UNAVAILABLE | 覆蓋少，參考價值低 |
| 下次財報日 | DATA_UNAVAILABLE | n/a | DATA_UNAVAILABLE | 待確認 |

## Red flags

- 嚴重虧損與燒錢：TTM 營業利潤率 -208.7%，TTM 自由現金流約 -9.28M USD，且 2026 Q3 燃燒速度較 Q1 增加（FCF -2.38M vs -1.26M）。
- 現金跑道有限：9 月底現金 7.78M USD，依前三季平均燃燒估計約 10 至 11 個月，未來 6 至 12 個月需再融資，稀釋風險高。
- 股數稀釋劇烈：2025 年流通股數增加 42.7%，2025 年股權融資 19.71M USD，股東權益由 17.72M 降至 11.39M USD（2026/09）。
- 營收來源不透明：2025 年營收下降 72.0%，2026 年季度營收跳升 26 倍，但工具無分部或客戶資料，無法判定 2026 年營收是否可持續。
- 買回與燒錢情境衝突：2026 前三季買回 2.42M USD，同期 FCF 為 -6.61M USD，需確認是否為稅務代扣等非典型交易。
- CEO 出售：2026-09-09 出售 1M 股，成交價 4.00 USD，為 6 個月內唯一公開市場交易，股價目前為 2.23 USD（低 44%）。
- SBC 偏高：2025 年 SBC 6.91M USD 超過同年營收 0.61M USD，非現金薪酬成本對股東稀釋的影響大。
- 估值偏高與技術面弱勢：P/S 8.31x、P/B 3.98x，股價低於 50 日與 200 日均線，beta 3.91。
- 分析師覆蓋低：僅 3 位分析師，目標價 10.67 USD 與現價差距大，不宜作為估值依據。
- 資料口徑差異（需人工確認）：(a) info.freeCashflow -5.42M 與季度加總 -9.28M 不一致；(b) info.totalDebt 0.60M 與 BS Total Debt 0.17M 不一致；(c) 2025 年上半年季度財報為空值，無法完整檢視 2025 年季度趨勢；(d) 2025 年度損益表與季度資料之間無法完全核對。
- 資料缺口（DATA_UNAVAILABLE）：同業中位數、分部營收、下次財報日、管理層指引、Q4 2026 之後的任何資料。

FUNDAMENTALS REPORT COMPLETE
