# Fundamentals — TLT (iShares 20+ Year Treasury Bond ETF) as of 2026-11-14

> 資料時點：yfinance 快取 2026-11-13 14:32 UTC（盤中快照，非收盤價）。未發現晚於 2026-11-14 的資料。
> 單位：USD，AUM 以 B（十億美元）表示。本標的為 ETF，無營收、獲利、現金流量表與資產負債表，相關欄位皆為 n/a。

## Executive summary
TLT 是追蹤美國國債指數（剩餘年限 >20 年）的被動型 ETF，AUM 約 47.52B USD，費用率 0.15%，流動性充足（3 個月平均成交量約 3,916 萬股）。盤中價格 79.27 USD 略低於 NAV 79.71 USD（折價約 0.55%），價格低於 50 日與 200 日均線，過去 52 週下跌 10.30%，財務健康度評估不適用，估值以殖利率與利率環境為主要衡量。本標的對長天期利率高度敏感，評價重點在利率走勢與持有成本，而非企業基本面。

## Revenue & profitability
不適用。TLT 是 ETF，yfinance 未提供營收、毛利、營業利益或淨利。
- info 中 epsTrailingTwelveMonths = -12.586、epsForward = -0.02、forwardPE = -3963.5，這些數值是基金分配與淨值計算的副產品，不具獲利意義，不採用。
- 報酬面（yfinance 提供）：YTD -2.92%；過去 3 個月 +0.72%；3 年年化平均 +1.50%；5 年年化平均 -8.09%。
- 歷史高點 179.7 USD（allTimeHigh），目前 79.27 USD 相當於歷史高點的約 44%。
- 52 週區間 76.43 – 90.86 USD（即目前價格僅高於 52 週低點約 3.7%，低於高點約 12.8%）。

## Cashflow & balance sheet
不適用。`balance_sheet` 與 `cashflow` 工具回傳空陣列 []，ETF 無自有財報。
- 基金資產規模：totalAssets ≈ netAssets ≈ 47.52B USD。
- 持有人分配：trailingAnnualDividendRate = 2.152 USD/股，以目前價格計算殖利率約 2.70%。info 另有 dividendYield = 4.76%，兩者不一致（4.76% 應為前瞻或 SEC 型殖利率，計算口徑未明），報告以 2.70%（實際 12 個月分配）與 4.76%（欄位）並列，不擅自取捨。
- 費用率 netExpenseRatio = 0.15%，以 AUM 估算每年成本約 71M USD（47.52B × 0.15%）。
- 債務與槓桿：TLT 本身無負債比率指標；其持有標的為美國國債，信用風險屬美國主權信用。yfinance 未提供持倉明細（久期、票息、到期分布），duration 與 YTM 皆 n/a。

## Capital allocation & insider signal
- 申購贖回與資金流量：yfinance 未提供資金流（fund flows）資料，淨申購/贖回 n/a。sharesOutstanding 欄位（109.7M）與 AUM/NAV 反推約 596M 股不一致（47.52B ÷ 79.71 ≈ 596M），股數資料可信度低，不作為規模判斷依據。
- 內部人交易：`insider` 工具回傳 []，ETF 無內部人交易概念，n/a。
- 機構持股：`inst_holders` 與 `major_holders` 皆回傳 []，持股集中度 n/a。
- 持倉集中度（結構面）：指數定義為美國公債中剩餘年限 >20 年、面額 ≥3 億 USD 的發行，排除聯準會持有部分；基金至少 90% 投資於美國國債、至少 80% 投資於指數成分。個別債券權重 yfinance 未提供，n/a。

## Valuation
ETF 的估值以殖利率、淨值折溢價與利率環境衡量，P/E、EV/EBITDA、P/FCF、P/S 皆不適用。
- 價格 vs NAV：79.27 vs 79.71，折價約 0.55%（盤中）。
- 價格 vs 均線：vs 50 日均線 80.26，偏離約 -1.24%；vs 200 日均線 84.33，偏離約 -6.0%。價格位於兩條均線之下，呈弱勢格局。
- 價格淨值比 priceToBook = 0.53，但 bookValue = 148.865 USD 與 NAV 79.71 USD 明顯不一致，此比率不可用。
- beta3Year = 2.30，數值偏高，與一般國債 ETF 的低β印象不符，應視為對特定基準（利率或股市）的回歸結果，參考時需謹慎。
- 同類比較：category 為 Long Government，同類中位數 n/a（yfinance 無同類資料）。
- 報價異常：bid 82.92 / ask 82.97 與最新成交價 79.27 相差約 4.6%，顯示報價可能過時或快照不同步；盤中成交量 1,974,025 股僅為部分時段，與 10 日均量 38.18M 不可直接比較。以 last price 與 NAV 為準。

## Key catalysts
- 財報：不適用（ETF 無財報），earnings_dates 工具回傳錯誤，n/a。
- 利率與總體事件（yfinance 未提供具體日期，以下為一般性觀察，未經工具驗證）：FOMC 會議、CPI 與 PCE 通膨數據、美國國債拍賣（尤其 20 年與 30 年期）、財政部發債規模與期限結構變化。長天期殖利率上升通常使 TLT 價格下跌，反之則上漲。
- 基金事件：corporateActions 為空，無近期配息或分割公告。配息日 dividendDate 欄位為舊值（2017 年），不代表近期配息安排。

## Metrics table
| 指標 (Metric) | 最新值 (Latest) | 年變化 (YoY) | 同類中位數 (Peer median, est.) | 判讀 (Verdict) |
|---|---|---|---|---|
| 資產規模 AUM (B USD) | 47.52 | n/a（無歷史 AUM 序列） | n/a | 規模大，流動性充足 |
| 費用率 Expense ratio | 0.15% | n/a | n/a | 低成本，符合被動型 ETF 定位 |
| 盤中價格 Last price (USD) | 79.27 | 52 週 -10.30% | n/a | 弱勢，接近 52 週低點區 |
| NAV (USD) | 79.71 | n/a | n/a | 價格略低於 NAV，折價約 0.55% |
| 價格 vs 50 日均線 | -1.24% | n/a | n/a | 短期偏弱 |
| 價格 vs 200 日均線 | -6.00% | n/a | n/a | 長期趨勢偏弱 |
| 年初至今報酬 YTD | -2.92% | n/a | n/a | 小幅負報酬 |
| 3 年年化平均報酬 | +1.50% | n/a | n/a | 近 3 年勉強為正 |
| 5 年年化平均報酬 | -8.09% | n/a | n/a | 長期受利率上升拖累 |
| 殖利率（實際 12 個月分配） | 2.70% | n/a | n/a | 與欄位 4.76% 不一致，待確認口徑 |
| 殖利率（yield 欄位） | 4.76% | n/a | n/a | 口徑未明 |
| 3 個月日均成交量 (M 股) | 39.16 | n/a | n/a | 流動性極佳 |
| beta (3Y) | 2.30 | n/a | n/a | 數值偏高，解讀需謹慎 |
| P/E、EV/EBITDA、P/FCF、P/S | n/a | n/a | n/a | ETF 不適用 |
| 久期 Duration、YTM | n/a | n/a | n/a | yfinance 未提供 |
| 資金流 Fund flows | n/a | n/a | n/a | 未提供 |
| 內部人交易 Insider | n/a | n/a | n/a | ETF 不適用 |

## Red flags
- 資料完整性：balance_sheet、cashflow、insider、major_holders、inst_holders、earnings_dates 皆無資料或錯誤，持倉、久期與資金流缺口大。
- 股數與 NAV 不一致：sharesOutstanding 109.7M 與 AUM/NAV 反推約 596M 股矛盾；bookValue 148.865 與 NAV 79.71 矛盾。
- 殖利率口徑不一致：dividendYield 4.76% 與實際 12 個月分配推算 2.70% 差距大。
- 報價異常：bid/ask 與成交價偏離約 4.6%，盤中快照可能過時，不宜用單一價格下結論。
- 趨勢偏弱：價格低於 50 日與 200 日均線，52 週跌 10.30%，5 年年化報酬 -8.09%，長期持有者面臨利率上升的持續性損失。
- 利率敏感度高：長天期國債對殖利率變化敏感，beta 與久期皆指向高利率風險；此為標的本質，非公司特有風險。
- 估值指標失真：forwardPE -3963.5、epsTrailingTwelveMonths -12.586 等數值不具意義，若下游代理人誤用會產生錯誤判斷。

FUNDAMENTALS REPORT COMPLETE
