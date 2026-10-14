# Fundamentals — IPGP as of 2026-10-14

## Executive summary
IPGP（IPG Photonics）資產負債表極為穩健，截至 2026-06-30 現金及短期投資 $871.3M、總負債性借款 $16.3M，淨現金約 $855M，流動比率 6.18x；但獲利能力偏弱，TTM 淨利率僅 2.6%、ROE 1.3%，FY2025 自由現金流為 -$3.5M，FCF/NI 不健康。估值上 trailing P/E 116.7x、P/FCF 約 71x 偏貴，forward P/E 32.9x 與分析師平均目標價 $124.14（較現價 $75.85 隱含 +63.7%）形成強烈對比，市場對 2026 下半年獲利復甦的定價尚未被數據證實；同期內部人（含 >10% 持股的關聯實體）6 個月淨賣出約 $23.2M，為需追蹤的負面訊號。

資料時點說明：本報告以 2026-10-14 為 as-of。價格與部分 info 欄位來自 yfinance cache（fast_info 來源標示 `cache`，cached_at 2026-10-14T11:38:30 UTC），Yahoo cookie/crumb 取得失敗，故即時性未獨立驗證。最新已報告季度為 2026-06-30（Q2'26，2026-08-04 公布）；下一次財報預定 2026-11-03，尚未發生。未發現晚於 as-of 的已實現數據。

## Revenue & profitability

**營收趨勢**
- FY2022 $1,429.5M → FY2023 $1,287.4M（-9.9%）→ FY2024 $977.1M（-24.1%）→ FY2025 $1,003.8M（+2.7%）。
- 3 年 CAGR（FY2022→FY2025）約 -11.1%；2 年 CAGR（FY2023→FY2025）約 -11.7%。FY2025 營收仍較 FY2022 低約 29.8%。
- 季度動能回升：Q2'25 $250.7M → Q3'25 $250.8M → Q4'25 $274.5M → Q1'26 $265.5M → Q2'26 $278.6M，Q2'26 YoY +11.1%，與 info 的 revenueGrowth 0.111 一致。TTM 營收 $1,069.3M。
- 業務組合：yfinance `info.longBusinessSummary` 僅列出應用領域（一般製造、汽車、消費品、醫療、能源、微電子、航太與國防、鐵路、造船等）與產品線（光纖雷射、二極體雷射、雷射系統、冷卻機等），未提供分部營收占比。分部 mix：DATA_UNAVAILABLE。

**毛利 / 營益 / 淨利率**

| 年度 | 毛利率 | 營益率 | 淨利率 | 備註 |
|---|---|---|---|---|
| FY2022 | 38.9% | 16.2% | 7.7% | 毛利 555.4 / 營益 231.4 / NI 109.9 |
| FY2023 | 42.1% | 18.0% | 17.0% | NI 218.9 |
| FY2024 | 34.6% | 1.5% | -18.6% | NI -181.5；2024 Total Unusual Items -222.7M |
| FY2025 | 38.0% | 2.3% | 3.1% | NI 31.1；Total Operating Income As Reported 13.1（1.3%） |

- FY2025 毛利率較 FY2024 改善約 3.4 個百分點，營益率改善約 0.8 個百分點，但仍遠低於 FY2023 水準。
- 季度趨勢：Q2'26 毛利率 40.4%（Q2'25 為 37.3%，+3.1pp），營益 $21.2M（營益率 7.6%，Q2'25 為 1.3%）；Q1'26 營益 $5.6M。
- TTM 營益率依季度加總約 4.0%；info 的 operatingMargins 為 5.9%。兩者口徑不同，本報告以季度加總為準並保留 info 數值供參照。
- TTM 淨利率（info profitMargins）2.58%；季度淨利 Q2'26 $5.2M、Q1'26 $1.6M、Q4'25 $13.3M、Q3'25 $7.5M，合計 TTM 約 $27.6M。
- 獲利能力指標：ROE（info, TTM）1.30%、ROA 0.97%；ROIC 為估計值：FY2025 NOPAT ≈ 營益 23.1 × (1-31%) ≈ 15.9，投入資本 ≈ 權益 2,128.1 + 負債 17.2 - 現金及短期投資 839.3 ≈ 1,306，ROIC 約 1.2%。
- 有效稅率：FY2025 為 31%，FY2024 為 21%（yfinance Tax Rate For Calcs）。
- 每股盈餘（GAAP 稀釋）：FY2022 $2.16、FY2023 $4.63、FY2024 -$4.09、FY2025 $0.73；info trailingEps $0.65、forwardEps $2.31。
- 季度 EPS（earnings_dates 的 Reported EPS，口徑與 GAAP trailingEps 不同，推測為調整後 EPS，yfinance 未明示）：Q2'25 $0.30、Q3'25 $0.35、Q4'25 $0.46、Q1'26 $0.29、Q2'26 $0.58。

## Cashflow & balance sheet

**現金流**
- 營運現金流：FY2022 $212.6M → FY2023 $296.0M → FY2024 $247.9M → FY2025 $75.3M（FY2025 較 FY2024 下降約 70%）。
- 資本支出：FY2022 $110.1M → FY2023 $110.5M → FY2024 $98.5M → FY2025 $78.8M（占營收 7.9%）。
- 自由現金流（yfinance Free Cash Flow）：FY2022 $102.5M → FY2023 $185.5M → FY2024 $149.4M → FY2025 **-$3.5M**。
- FCF margin：FY2025 約 -0.3%；TTM（info freeCashflow $45.3M）約 4.2%。
- FCF / NI：FY2023 0.85、FY2022 0.93（接近但未達 0.9 門檻），FY2025 為 -0.11（不健康），FY2024 因 NI 為負而 n/m。TTM 以 info 值 FCF $45.3M 對 NI TTM $27.6M 計算約 1.6，但 TTM FCF 與季度 NI 來源不同，僅供參考。
- 股份基礎報酬（SBC）FY2025 $42.9M，約占營收 4.3%，已超過 FY2025 FCF 絕對值；若以 FCF 扣除 SBC 計算，FY2025 自由現金流實質為負。

**資產負債表（FY2025 年底；Q2'26 為最新季）**
- 總資產 FY2025 $2,424.3M；股東權益 $2,128.1M（FY2024 為 $2,024.5M，FY2023 為 $2,415.4M）。
- 現金及短期投資：FY2025 $839.3M（FY2024 $930.2M，-9.8%）；Q2'26 $871.3M，較 Q1'26 $812.9M 回升。
- 總負債性借款：FY2025 $17.2M；Q2'26 $16.3M。淨現金（現金及短期投資 - 總負債）：FY2025 約 $822M；Q2'26 約 $855M，約占市值 26.5%。
- 流動比率：FY2024 6.98x、FY2025 6.08x；info（最新）6.18x。速動比率（info）4.42x。
- 負債權益比（info debtToEquity 0.764，單位為百分比）約 0.76%，財務槓桿極低。
- 總負債 FY2025 $296.1M，流動負債 $234.0M。
- 存貨：FY2022 $509.4M → FY2023 $453.9M → FY2024 $284.8M → FY2025 $313.4M，FY2025 回升約 10%。
- 商譽：FY2024 $67.2M → FY2025 $71.7M。
- 每股帳面值 $50.01、每股現金 $20.49，現價 $75.85 對每股現金的倍數約 3.7x。

## Capital allocation & insider signal

**資本配置**
- 買回股票（Repurchase Of Capital Stock）：FY2022 $499.5M → FY2023 $223.5M → FY2024 $343.8M → FY2025 $53.1M。FY2025 買回金額較 FY2024 減少約 85%，且 FY2025 FCF 為負，買回主要以既有現金支應。
- 加權平均基本股數：FY2022 50.76M → FY2025 42.35M，降幅約 16.6%。目前 sharesOutstanding 42.53M，floatShares 27.84M。
- 股利：無配息（info dividendYield 0.0、payoutRatio 0.0；dividendRate 欄位缺漏）。股利覆蓋率：DATA_UNAVAILABLE（無配息）。
- 負債償還（Repayment Of Debt）：FY2025 為 0、FY2024 為 0、FY2023 為 -$16.0M、FY2022 為 -$18.1M；總負債由 FY2022 $38.1M 降至 FY2025 $17.2M。

**內部人與大股東（過去 6 個月，2026-04-14 至 2026-10-14）**
- 公開市場賣出合計約 $23.4M（約 24.2 萬股）；公開市場買進僅 1 筆，即 Director John R. Peeler 於 2026-08-26 以 $72.84–74.57 買進 2,710 股，金額約 $0.20M。淨賣出約 $23.2M，約占市值 3,226M 的 0.72%。
- 賣方結構高度集中於關聯實體：IP Fibre Devices Ltd（>10% 持股實體）賣出約 $13.3M（約 13.8 萬股，占 6 個月賣出金額約 57%）；Valentin Gapontsev Trust I 賣出約 $7.8M；Director Eugene A. Scherbakov 小額多次賣出約 $0.7M。其餘高階主管包括 Mammen（2026-05-22，$1.2M）、Lopresti（2026-06-29，$0.1M）、Desmond、Agnes Tang 等小額賣出。
- 2026-05-12 有董事與高管受領股票獎勵（Stock Award，無現金金額）；屬例行薪酬性質。
- 持股集中：insidersPercentHeld 38.98%；institutionsPercentHeld 75.13%（約 491 家機構）。前十大機構包括 First Eagle（7.85%，較前期 -27.3%）、BlackRock（6.70%）、Vanguard（3.87%）、Dimensional（3.76%）等。
- 空頭部位：shortPercentOfFloat 23.75%，屬偏高水準。
- 注意：內部人賣出與大股東減持均含 Gapontsev 家族相關實體，屬於結構性減持，不能僅以金額判斷為主觀看空訊號；但買進訊號極少。

## Valuation

- 股價：$75.85（fast_info, cache）；前收 $76.05；日內區間 $72.75–75.99；成交量 326,212 股，10 日均量 418,410 股。
- 52 週區間：$69.41–$155.82；距 52 週高點回落約 51.3%。50 日均線 $79.85（現價低於 5.0%）、200 日均線 $101.42（現價低於 25.2%）。
- 市值 $3,226.2M；企業價值 EV $2,371.2M（市值 + 總負債 - 現金，依 info 數值計算）。
- trailing P/E 116.7x（GAAP TTM EPS $0.65）；forward P/E 32.9x（forwardEps $2.31）；PEG 1.83。
- EV/EBITDA（TTM EBITDA $104.4M）22.7x；EV/Revenue 2.22x。
- P/S（TTM）3.02x；P/B 1.52x；P/FCF（TTM FCF $45.3M）計算約 71.2x。
- 同業中位數：DATA_UNAVAILABLE（工具未提供同業估值數據，無法給出可驗證的 sector median）。
- 分析師：共 7 位，平均目標價 $124.14、最高 $152.00、最低 $78.00；info recommendationKey 為 none，無共識評等。最低目標價仍高於現價。
- 估值判讀：以 forward 獲利計算仍不便宜（32.9x），但以 2026 下半年獲利恢復為前提，市場與分析師的預期分歧極大。

## Key catalysts

- 下一次財報：2026-11-03（yfinance earnings_dates 列出，EPS 預估 $0.49，對照 Q3'25 實際 $0.35，隱含 YoY 約 +40%）。
- 近四次財報 EPS 表現：Q2'25 超預期 +127%、Q3'25 +79%、Q4'25 +85%、Q1'26 -7%、Q2'26 +49%（相對 EPS 預估），過去五季有四季超預期。
- 最近一次財報（Q2'26）：營收 $278.6M（YoY +11.1%）、毛利率 40.4%、營益率 7.6%，為近五季最佳獲利結構之一。
- 管理層指引（guidance）內容：DATA_UNAVAILABLE（工具未提供公司 earnings call 或指引文字）。
- 分部或產品組合轉變：DATA_UNAVAILABLE（工具未提供分部數據）。
- 治理：info overallRisk 4、compensationRisk 9（滿分 10，薪酬風險偏高）、auditRisk 5、boardRisk 2、shareHolderRightsRisk 2。CEO FY2025 totalPay $2.07M。

## Metrics table

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收（TTM） | $1,069.3M | Q2'26 YoY +11.1%；FY25 +2.7% | DATA_UNAVAILABLE | 中性偏弱，剛止跌回升 |
| 毛利率（FY25） | 38.0% | +3.4pp（FY24 34.6%） | DATA_UNAVAILABLE | 中性 |
| 毛利率（Q2'26） | 40.4% | +3.1pp（Q2'25 37.3%） | DATA_UNAVAILABLE | 改善中 |
| 營益率（FY25） | 2.3% | +0.8pp（FY24 1.5%） | DATA_UNAVAILABLE | 偏弱 |
| 淨利率（TTM） | 2.6% | FY25 3.1% vs FY24 -18.6% | DATA_UNAVAILABLE | 偏弱 |
| ROE（TTM） | 1.3% | n/a | DATA_UNAVAILABLE | 偏弱 |
| ROIC（FY25 估計） | 約 1.2% | n/a | DATA_UNAVAILABLE | 偏弱 |
| 自由現金流（FY25） | -$3.5M | FY24 $149.4M（-102%） | DATA_UNAVAILABLE | 紅旗 |
| FCF margin（TTM） | 4.2% | FY25 約 -0.3% | DATA_UNAVAILABLE | 偏弱 |
| FCF / NI（FY25） | -0.11x | FY24 n/m | >0.9 為健康 | 不健康 |
| 營運現金流（FY25） | $75.3M | FY24 $247.9M（-70%） | DATA_UNAVAILABLE | 紅旗 |
| 淨現金（Q2'26） | $855M | FY25 $822M | DATA_UNAVAILABLE | 強 |
| 流動比率（最新） | 6.18x | FY25 6.08x；FY24 6.98x | DATA_UNAVAILABLE | 強 |
| 負債權益比（最新） | 0.76% | FY25 約 0.81% | DATA_UNAVAILABLE | 極低，強 |
| 資本支出（FY25） | $78.8M（占營收 7.9%） | FY24 $98.5M（-20%） | DATA_UNAVAILABLE | 中性，支出下降 |
| 買回股票（FY25） | $53.1M | FY24 $343.8M（-85%） | DATA_UNAVAILABLE | 轉弱 |
| 股利殖利率 | 0%（無配息） | n/a | DATA_UNAVAILABLE | 無股利 |
| SBC（FY25） | $42.9M（占營收 4.3%） | FY24 $37.1M（+16%） | DATA_UNAVAILABLE | 偏高 |
| 內部人 6 個月淨交易 | 淨賣出約 $23.2M（約 0.72% 市值） | n/a | DATA_UNAVAILABLE | 負面（關聯實體為主） |
| 空頭占流通股 | 23.75% | n/a | DATA_UNAVAILABLE | 偏高 |
| trailing P/E | 116.7x | n/a | DATA_UNAVAILABLE | 偏貴 |
| forward P/E | 32.9x | n/a | DATA_UNAVAILABLE | 偏貴 |
| EV/EBITDA（TTM） | 22.7x | n/a | DATA_UNAVAILABLE | 偏貴 |
| P/FCF（TTM，計算值） | 約 71.2x | n/a | DATA_UNAVAILABLE | 偏貴 |
| P/S（TTM） | 3.02x | n/a | DATA_UNAVAILABLE | 中性偏貴 |
| P/B | 1.52x | n/a | DATA_UNAVAILABLE | 合理 |
| 分析師平均目標價 | $124.14（隱含 +63.7%） | n/a | DATA_UNAVAILABLE | 樂觀，分歧大（$78–$152） |
| 股價相對 200 日均線 | -25.2%（現價 $75.85 / 200DMA $101.42） | 距 52 週高點 -51.3% | DATA_UNAVAILABLE | 技術面弱勢 |

## Red flags

- 獲利能力薄弱：TTM 淨利率 2.6%、ROE 1.3%、ROIC 估計約 1.2%，遠低於一般資本成本。
- FY2025 自由現金流為負（-$3.5M），營運現金流較 FY2024 下降約 70%，FCF/NI 為 -0.11x。
- SBC（$42.9M）超過 FY2025 FCF，實質股東稀釋與現金流壓力並存。
- 營收三年下滑後僅 FY2025 小幅回升（+2.7%），仍較 FY2022 低約 30%；FY2024 出現 $181.5M 淨虧損與 $222.7M 非經常性項目。
- 估值偏貴：trailing P/E 116.7x、P/FCF 約 71x，forward P/E 32.9x 須依賴 2026 下半年獲利大幅回升（consensus Q3'26 EPS $0.49）。
- 內部人與關聯大股東 6 個月淨賣出約 $23.2M，買進僅 1 筆 $0.2M。
- 空頭占流通股 23.75%，股價距 52 週高點回落 51.3%，且低於 50 日與 200 日均線。
- 治理面薪酬風險評分 9/10（info compensationRisk），偏高。
- 股利為零，買回金額在 FY2025 大幅減少（-85%），資本回報對股東的支撐減弱。
- 資料品質：yfinance Yahoo cookie/crumb 取得失敗，fast_info 來源為 cache；info 的 bid/ask 為 68.90 / 79.49，價差極寬，快照報價可能不具代表性；earnings_dates EPS 與 GAAP trailingEps 口徑不同；operatingMargins（5.9%）與季度加總營益率（約 4.0%）不一致。
- 缺漏欄位（DATA_UNAVAILABLE）：同業中位數、分部營收、管理層指引文字、dividendRate、lastDividendValue。

FUNDAMENTALS REPORT COMPLETE
