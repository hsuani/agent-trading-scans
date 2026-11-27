# Fundamentals — TLT as of 2026-11-28

資料說明：分析基準日 2026-11-28。工具回傳為快取資料（cached_at 2026-11-27 約 16:31–16:37 UTC），未見 2026-11-28 之後的資料。TLT 為 ETF（iShares 20+ Year Treasury Bond ETF，類別 Long Government），不適用公司營收、獲利、現金流、內部人交易分析，以下以基金結構指標取代。大部分 ETF 結構資料（存續期間、平均到期日、持有人、基金淨流量）工具無法提供，標示為 DATA_UNAVAILABLE。

## Executive summary
TLT 為規模龐大的長天期美國公債 ETF（淨資產 47.52B USD，費用率 0.15%），結構面與流動性不構成問題，但存續期間、資金流向等核心結構資料缺失，無法完整評估。市價 81.26 USD 相對 NAV 82.19 USD 小幅折價約 1.1%，價格位於 52 週區間 76.43–90.86 的中下段，且低於 200 日均線（84.00）約 3.2%、高於 50 日均線（80.12）約 1.5%，技術面中性偏弱。估值指標（P/E、P/B、EV/EBITDA）對 ETF 不適用，本報告不提供買賣建議。

## Revenue & profitability
不適用。TLT 為被動追蹤指數的債券基金，無營收、毛利、營業利益或淨利。yfinance `financials` 回傳空值，EPS 欄位（trailing -12.586、forward -0.02）與 forwardPE（-4063）屬於無意義數值，不採用。

基金層級的「收益面」僅能參考以下欄位：
- 3 年年化報酬（欄位原值 0.0136，推定為 1.36%）
- 5 年年化報酬（欄位原值 -0.0765，推定為 -7.65%）
- YTD 報酬 -2.92%
- 近 12 個月價格報酬 -8.83%（fiftyTwoWeekChangePercent）
- 近 3 個月報酬欄位 0.72213（單位未明，可能為 %，含配息口徑不明，未採用）

## Cashflow & balance sheet
不適用。ETF 無自身負債與現金流量表。`cashflow`、`quarterly_cf`、`balance_sheet` 工具回傳空值。

基金資產端可取得：
- 淨資產（netAssets / totalAssets）：47,518,568,448 USD，即 47.52B USD
- bookValue 欄位為 148.865，與 NAV 82.19 明顯不一致，且 priceToBook 0.546 由此推算，判定為資料異常，不採用。

## Capital allocation & insider signal
- 配息：trailingAnnualDividendRate 2.152 USD（近 12 個月配息）。以 81.26 計算約 2.65%；以 trailingAnnualDividendYield 欄位 0.02617 為約 2.62%。但 `yield` 與 `dividendYield` 欄位為 4.76%（與 2.152 USD 配息不一致，推算需 3.87 USD 年配息），兩者無法調和，本報告以 2.6% 為較保守的推算值，4.76% 需以發行商公告 SEC yield 核對。
- 買回（buyback）：ETF 不適用，無此項。
- 內部人交易：ETF 無內部人，`insider` 工具回傳空值，判定不適用。
- 機構持有人：`major_holders`、`inst_holders` 回傳空值，持有人集中度 DATA_UNAVAILABLE。
- 基金淨流量（creation/redemption flows）：工具未提供，DATA_UNAVAILABLE。

## Valuation
ETF 估值以 NAV 折溢價與費用率為主，傳統公司估值指標不適用。
- 市價 vs NAV：yf info 市價（regularMarketPrice）81.26 vs navPrice 82.19389，折價 -1.13%。fast_info 最新價 81.465（cnyes 來源）則折價約 -0.88%。兩者差異約 0.25%，屬報價時點差異，結論一致：小幅折價。
- 股數不一致：sharesOutstanding 109.7M 股，若以 NAV 82.19 計算僅約 9.0B USD，與 totalAssets 47.52B 不一致（以 AUM 反推約 578M 股）。股數欄位判定為異常，不採用。
- P/E、forward P/E、EV/EBITDA、P/FCF、P/S：不適用（ETF）。
- 費用率 0.15%：ETF 結構成本，相對被動長債基金屬低水準；同類（Long Government）中位數工具未提供，sector median 標示 n/a。
- 3 年 beta 2.30（yf 欄位原值）：相對大盤的敏感度欄位，對長債 ETF 而言代表其報酬對市場與利率變化高度敏感，僅作參考。

## Key catalysts
- 無財報（ETF 不適用）。`earnings_dates` 工具回傳空值。
- 利率與殖利率曲線：TLT 價格對長端公債殖利率高度敏感，為主要驅動因素。工具未提供即時殖利率或 Fed 政策資料，本節僅做定性描述，不宣稱特定排程事件。
- 技術結構位（ta levels，依工具輸出）：
  - 壓力：87.79（2026-06-25）、83.60（2026-08-28）、82.42（2026-11-06）
  - 支撐：81.17（2026-08-18）、76.43（2026-10-07，亦為 52 週低點）
- 現價 81.26 接近 81.17 支撐，且位於 82.42 壓力之下。
- 成交量：當日量 17.99M 股，低於 3 個月均量 40.9M 與 10 日均量 42.3M，但快照可能為盤中值，不宜單獨解讀。

## Metrics table
單位：價格 USD；AUM 為 USD B；其餘為比率或指標原值。本表無台幣或韓元金額，無需 億 換算。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 市價 (USD) | 81.26 | 12M 價格 -8.83% | n/a | 52 週區間中下段（距高點 -10.5%、距低點 +6.4%） |
| NAV (USD) | 82.19 | n/a | n/a | 參考基準 |
| 市價對 NAV 折溢價 | -1.13% | n/a | n/a | 小幅折價 |
| 淨資產 AUM (USD B) | 47.52 | DATA_UNAVAILABLE | n/a | 規模大，流動性充足 |
| 費用率 | 0.15% | n/a | n/a（Long Government 中位數未提供） | 低，結構成本友善 |
| 近 12 月配息 (USD) | 2.152 | n/a | n/a | 推算殖利率約 2.6% |
| 殖利率（yield 欄位） | 4.76% | n/a | n/a | 與配息不一致，待核對 |
| 存續期間 (duration) | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | 無法評估利率敏感度 |
| 平均到期日 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | 無法評估 |
| 持有人集中度 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | 工具回傳空值 |
| 基金淨流量 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | 工具未提供 |
| 3 年 beta | 2.30 | n/a | n/a | 對市場與利率敏感 |
| 3 年年化報酬 | 1.36%（推定） | n/a | n/a | 欄位原值 0.0136 |
| 5 年年化報酬 | -7.65%（推定） | n/a | n/a | 欄位原值 -0.0765 |
| YTD 報酬 | -2.92% | n/a | n/a | 年內偏弱 |
| 價格 vs 200 日均線 | -3.18% | n/a | n/a | 位於長期均線下方，偏弱 |
| 價格 vs 50 日均線 | +1.51% | n/a | n/a | 中期略偏多 |
| RSI(14) | 54.0 | n/a | n/a | 中性 |
| MACD 柱狀體 | +0.100 | n/a | n/a | 動能微正 |
| 布林 %B | 0.58 | n/a | n/a | 中軸上方 |
| ATR(14) | 0.81（約 1.0% 價格） | n/a | n/a | 波動中等偏低 |
| 20 日年化波動 | 11.8% | n/a | n/a | 波動平穩 |
| P/E、EV/EBITDA、P/FCF、P/S | n/a | n/a | n/a | ETF 不適用 |

## Red flags
- 存續期間、平均到期日、持有人與基金淨流量皆為 DATA_UNAVAILABLE，ETF 核心結構判斷缺口大。
- 股數（109.7M）與 AUM / NAV 推算值不一致，股數欄位不可用。
- 殖利率 4.76% 與 近 12 月配息 2.152 USD（約 2.6%）不一致，收益率口徑需核對。
- bookValue 148.865 與 NAV 82.19 不符，P/B 欄位不可用。
- 買賣報價異常：bid 82.92、ask 82.97 高於現價 81.26，bidSize 1、askSize 17，報價同步性存疑。
- 3 年 beta 2.30 顯示報酬對市場與利率的敏感度高。
- 價格位於 200 日均線下方約 3.2%，52 週低點 76.43 與 81.26 距離僅約 6%，波動與利率變化下有再測低點的可能（僅描述結構，不構成建議）。
- 快照資料來自快取，部分欄位（成交量、現價）可能為盤中值，數值之間存在 0.2 至 0.3 USD 的來源差異。

FUNDAMENTALS REPORT COMPLETE
