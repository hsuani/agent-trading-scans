# Fundamentals — ISRG as of 2026-10-26

資料基準：價格與 info 欄位為 2026-10-26 快取 (cached_at 2026-10-26 12:44 UTC)。金額單位為 USD，以 B (十億) / M (百萬) 標示。TTM 數字取自 yfinance `info`，財務報表 (financials / quarterly_fin / balance_sheet / cashflow) 經交叉檢核後判定資料錯置，未用於本報告的趨勢判斷（詳見下方「資料完整性」）。

## Executive summary
ISRG 的獲利品質與財務體質極佳：TTM 營收約 11.58B USD、毛利率 66.6%、營業利益率 33.3%、FCF 約 3.43B USD、FCF / NI 約 1.16，且無負債、現金約 4.04B USD。估值仍屬高檔，trailing P/E 54.7x、forward P/E 36.4x、EV/EBITDA 34.2x、P/FCF 約 46.5x，遠高於醫療器材一般水準，但股價 452.29 USD 較 52 週高點 603.88 USD 低約 25%，且站上 200 日均線 (436.21)。主要風險在於 TTM EPS 成長為負 (-23.6%) 與財務報表資料不可用，使歷史趨勢無法獨立驗證；內部人與大股東近六個月以賣出為主，但主要金額來自 SoftBank 單筆減持。

## Revenue & profitability
- 營收：TTM 總營收 11.58B USD，`revenueGrowth` 為 +21.7%（YoY）。
- 3-5 年 CAGR：n/a（財務報表資料錯置，無法可靠計算）。
- 收入組成：`longBusinessSummary` 列示業務為 da Vinci 手術系統、Ion 內視鏡系統、手術器械與耗材、服務與數位化服務；yfinance 未提供分部營收數字，分部占比 n/a。
- 獲利能力（TTM，info）：
  - 毛利率 66.6%（毛利 `grossProfits` 7.72B USD，與 11.58B × 66.6% 吻合）
  - 營業利益率 33.3%（推算營業利益約 3.85B USD）
  - EBITDA 4.47B USD，EBITDA margin 38.6%
  - 淨利率 25.5%；淨利 `netIncomeToCommon` 2.96B USD
- ROE 17.9%、ROA 11.9%。以 bookValue 46.12 USD × 353.3M 股推算股東權益約 16.3B USD，ROE 驗算吻合。
- ROIC（估算）：以營業利益 × (1 - 21%) 約 3.0B USD，投入資本以股東權益減現金約 12.3B USD 推算，ROIC 約 25%（估算值，非 yfinance 原始欄位）。
- 獲利成長：`earningsGrowth` -23.6%、`earningsQuarterlyGrowth` -25.8%，與營收 +21.7% 方向相反，原因無法從可用資料判定（可能與一次性項目或費用結構有關，需以財報原文確認）。

## Cashflow & balance sheet
現金流（TTM，info）：
- 營業現金流 OCF 4.09B USD，自由現金流 FCF 3.43B USD
- FCF margin 29.7%（3.43 / 11.58）
- FCF / NI = 1.16，高於 0.9 健康門檻；OCF / NI = 1.38
- 推算資本支出（OCF - FCF）約 0.65B USD，占營收約 5.7%

資產負債表（info）：
- 總負債 `totalDebt` = 0；現金 `totalCash` 4.04B USD；淨負債為 -4.04B USD（淨現金）。
- 由 EV 反推（EV 152.87B 與市值 159.78B 差額）淨現金約 6.9B USD，差額推測為現金以外的短期投資，yfinance 未明列，列為待確認。
- 流動比率 3.33、速動比率 2.32，短期償債能力充裕。
- Debt / Equity：n/a（總負債為 0）。

## Capital allocation & insider signal
資本配置：
- 股利：`dividendYield` 0、`payoutRatio` 0，目前無配息。
- 買回：yfinance 無可靠的庫藏股資料，買回金額 n/a。
- 股本：`sharesOutstanding` 353.28M，`floatShares` 344.58M。
- 資本支出趨勢：歷史報表錯置，n/a。

內部人交易（yfinance `insider`，視窗 2026-04-26 至 2026-10-26）：
- 共 25 筆公開市場賣出，合計 289.8M USD、5.76M 股；買進 0 筆。
- 其中 SoftBank Group 於 2026-05-27 以 50.42 USD 賣出 5.59M 股，金額 281.8M USD，占全部賣出金額約 97%。
- 扣除 SoftBank 後，董監事與高階主管合計賣出約 8.0M USD，主要為：Krasnow（董事，約 3.49M USD）、Boyd（約 1.15M USD）、Kuffner（CTO，約 1.13M USD）、Martins（CFO，約 1.12M USD，2026-07-27 以 40.80 USD 賣出 27,463 股）。
- Kane、Krasnow 有每月約 2,000 股的固定規模賣出，屬例行性質，訊號強度低。
- 相對市值：全部賣出金額 289.8M / 市值 159.78B ≈ 0.18%；扣除 SoftBank 後約 0.005%。金額本身不構成大量減持訊號，但 SoftBank 減持屬實質性的大股東退出。
- 近期（2026-09 至 10 月）賣出價位約 39 至 44 USD，與目前股價區間接近。
- 2025-12-11 執行長 Cohen 有 1,000,000 股贈與（非市場交易，且在視窗外）。

大股東（yfinance `inst_holders`，截至 2026-06-30）：
- SoftBank 持股 39.83M 股，Walmart 15.0M 股，Baillie Gifford 12.26M 股（季減 -1.7%）。
- 機構持股比例 `heldPercentInstitutions` 91.2%；內部人持股 `heldPercentInsiders` 0.52%（info）。
- 資料衝突：`major_holders` 顯示 insidersPercentHeld 13.6%，`inst_holders` 內的 pctHeld 與股數不一致（SoftBank 39.83M / 353.28M 股 ≈ 11.3%，但 feed 寫 30.7%）。此處以股數推算為準，pctHeld 欄位不採用。

## Valuation
估值（以 452.29 USD 計）：
- Trailing P/E 54.7x（EPS 8.27 USD）
- Forward P/E 36.4x（forward EPS 12.43 USD，隱含 EPS 成長約 +50%）
- EV / EBITDA 34.2x（EV 152.87B / EBITDA 4.47B，驗算吻合）
- P / S 13.8x（市值 159.78B / 營收 11.58B，驗算吻合）
- P / FCF 約 46.5x（159.78B / 3.43B，推算）
- P / B 9.8x（bookValue 46.12 USD）
- 驗算：EPS 8.27 × 353.3M 股 ≈ 2.92B，與 netIncomeToCommon 2.96B 差約 1%（加權股數差異），數字一致。

股價位置與分析師：
- 現價 452.29 USD，前收 443.85 USD，當日 +1.9%（日內區間 442.56 至 458.45）
- 50 日均線 396.06 USD（股價高於 +14%）；200 日均線 436.21 USD（股價高於 +3.7%）
- 52 週區間 328.57 至 603.88 USD，股價位於區間低段偏上，距高點 -25%
- 分析師平均目標價 478.30 USD（30 位，recommendationKey = buy），隱含上行約 5.8%
- Beta 1.463

與醫療器材板塊中位數比較（估計值，非工具輸出）：trailing P/E 約 28x、forward P/E 約 24x、EV/EBITDA 約 18x、P/S 約 4.5x。ISRG 各項估值倍數均明顯高於板塊估計中位數，溢價主要對應其 33% 營業利益率、約 22% 營收成長與手術機器人的壟斷性地位（本段為分析師判斷）。

## Key catalysts
- 下次財報：yfinance `earnings_dates` 列示 2026-11-16（EPS 預估 0.16，見資料完整性說明）。另 `info.earningsTimestamp` 為 2026-10-20 20:00 UTC（對應 mostRecentQuarter 2026-09-30），兩者衝突，且 Q3 2026 實際財報未出現在任何可用 feed 中。此為本報告最需確認的日程事項，trader 應以公司公告為準。
- 最近已公布季度：`earnings_dates` 最近一筆為 2026-08-05（Q2 2026）。
- 指引 (guidance)：工具未提供，n/a。
- 業務面催化劑：da Vinci 手術量與裝機量、Ion 內視鏡系統放量、服務收入占比（分部數字 n/a，需以財報補充）。
- 大股東動向：SoftBank 已於 2026-05 大幅減持，後續是否持續減持為待觀察事項。

## Metrics table
金額單位：USD（B = 十億，M = 百萬）。板塊中位數為估計值，非工具輸出。

| Metric | Latest (TTM / 2026-10-26) | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 總營收 (USD B) | 11.58 | +21.7% | n/a | 高成長 |
| 毛利率 | 66.6% | n/a | 約 60% | 優於板塊 |
| 營業利益率 | 33.3% | n/a | 約 20% | 優於板塊 |
| EBITDA margin | 38.6% | n/a | 約 24% | 優於板塊 |
| 淨利率 | 25.5% | n/a | 約 15% | 優於板塊 |
| 淨利 (USD B) | 2.96 | n/a | n/a | 獲利規模大 |
| EPS (trailing, USD) | 8.27 | 獲利年增 -23.6% | n/a | 獲利成長轉負，需確認 |
| EPS (forward, USD) | 12.43 | 隱含 +50% | n/a | 市場預期回升 |
| ROE | 17.9% | n/a | 約 15% | 中上 |
| ROIC (估算) | 約 25% | n/a | 約 12% | 優 |
| FCF (USD B) | 3.43 | n/a | n/a | 充足 |
| FCF margin | 29.7% | n/a | 約 15% | 優 |
| FCF / NI | 1.16 | n/a | 約 0.9 | 健康 |
| 淨負債 (USD B) | -4.04（淨現金） | n/a | 約 0 至正值 | 強健 |
| 流動比率 | 3.33 | n/a | 約 2.0 | 充裕 |
| Debt / Equity | n/a（總負債 0） | n/a | 約 0.3 | 無槓桿 |
| P/E (trailing) | 54.7x | n/a | 約 28x | 高估值 |
| P/E (forward) | 36.4x | n/a | 約 24x | 高估值 |
| EV / EBITDA | 34.2x | n/a | 約 18x | 高估值 |
| P / FCF | 約 46.5x | n/a | 約 22x | 高估值 |
| P / S | 13.8x | n/a | 約 4.5x | 高估值 |
| P / B | 9.8x | n/a | 約 3x | 高估值 |
| 股利殖利率 | 0% | n/a | 約 1.5% | 無配息 |
| 內部人淨買賣 (6 個月) | 淨賣出 289.8M（扣除 SoftBank 約 8.0M） | n/a | n/a | 中性偏負，金額小 |
| 52 週位置 | 距高點 -25%，高於 200 日均線 | n/a | n/a | 中性 |

## Red flags
- 財務報表資料錯置（最重要）：`financials`、`quarterly_fin`、`balance_sheet`、`cashflow` 及其 quarterly 版本，在快取中混入至少兩組不同公司或不同幣別規模的資料。Sept-FYE 一組營收約 2.25B USD、淨損 -16.9M，股數約 112.6M，與 ISRG 市值 159.78B / 353M 股不符；另一組 March-FYE 數字為十億級以上的非美元規模。本報告未採用任何報表數字做趨勢或 CAGR 判斷，需修復快取後重跑。
- 財報 EPS 歷史與 info 不一致：`earnings_dates` 的 EPS 序列（2026-08 季 0.41、2026-05 季 0.45 等）加總約 1.84 USD，與 trailingEps 8.27 不符；EPS 估計 0.13 至 0.16 亦與 forwardEps 12.43 不符。surprise 百分比不可用。
- 下次財報日期衝突：2026-10-20（info）與 2026-11-16（earnings_dates）並存，且 Q3 2026 實際數字缺席。
- 獲利成長轉負：`earningsGrowth` -23.6%，與營收 +21.7% 背離，需以財報確認原因。
- 估值溢價高：trailing P/E 54.7x、EV/EBITDA 34.2x、P/S 13.8x，對任何獲利放緩都較敏感。
- SoftBank 大額減持：2026-05-27 以 50.42 USD 賣出 5.59M 股（281.8M USD），屬大股東實質退出。
- 大股東持股資料衝突：`major_holders` 與 `inst_holders` 的持股比例與股數不一致，無法精確確認實際持股結構。
- 高 beta：1.463，股價波動風險高於大盤。
- 缺乏可用分部與指引資料：分部營收、管理層指引、資本支出與買回歷史皆為 n/a，基本面深度分析受限。

FUNDAMENTALS REPORT COMPLETE
