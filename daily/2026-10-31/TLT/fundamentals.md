# Fundamentals — TLT (iShares 20+ Year Treasury Bond ETF) as of 2026-10-31

> 資料時點note：分析基準日為 2026-10-31。本次工具回傳皆來自 repo 快取（`source: cache`），快取時間戳為 2026-10-30 12:45 UTC（info）與 2026-10-30 12:39 UTC（fast_info）；技術指標 `ta snapshot` 的 as_of 為 2026-10-29。`info.regularMarketTime` 為 1793304000，換算為 2026-10-31 00:00 UTC（即 2026-10-30 美東收盤時戳），屬於接近或晚於分析基準日的資料，需留意。價格 81.49 USD 與 ta 的 as_of 2026-10-29 可能不是同一個交易日，下游引用時請以此為準。TLT 為 ETF 而非公司，財務報表與內部人、機構持股相關欄位大多無資料，已逐項標示 DATA_UNAVAILABLE。

## Executive summary

TLT 追蹤的是剩餘年期超過 20 年、面額 3 億美元以上的美國公債指數，屬於長天期公債 ETF，不具有傳統公司財務報表，因此「財務健康度」改以標的規模、費用率、淨值溢折價與技術面評估。目前價格 81.49 USD 與 NAV 81.44277 USD 幾乎平價（溢價約 +0.06%），股價位於 20 日與 50 日均線之上、200 日均線（84.65 USD）之下，RSI14 為 60.8、MACD 柱狀體為正，YTD 報酬 -7.998%，近 12 個月 mom 為 -11.4%，顯示長天期公債仍處於中期弱勢、短期偏多整理的狀態。估值層面 P/E、EV/EBITDA、P/FCF 等公司型指標不適用；持倉存續期（duration）、SEC yield、資金流向等關鍵欄位工具未回傳，無法量化評估。

## Revenue & profitability（不適用，改為標的與規模概況）

- 性質：ETF，無營收、毛利、營業利益或淨利；`financials` 工具回傳空陣列，標示 DATA_UNAVAILABLE。
- 規模：`totalAssets` = 46,233,321,472 USD，約 462.33 億美元（46.23B USD），為單一時點數值，無歷史序列，故無法計算 AUM 趨勢（YoY 與 CAGR 皆為 DATA_UNAVAILABLE）。
- 指數定義（來自 `longBusinessSummary`）：標的指數為剩餘年期 > 20 年、面額 ≥ 3 億美元之美國公債（排除聯準會持有部分）；基金至少 80% 資產投入指數成分、至少 90% 資產投入美國公債。
- 類別：`category` = Long Government；基金家族 iShares；成立日 fundInceptionDate 為 1027296000（Unix 時間，換算約為 2002 年 7 月）。
- 績效（price-only 與 NAV 口徑未明，原值引用）：ytdReturn = -7.998%；trailingThreeMonthReturns = -8.846%；fiftyTwoWeekChangePercent = -9.746%；threeYearAverageReturn = 0.029346；fiveYearAverageReturn = -0.0803459（工具未標示單位為百分比或小數，未換算）。

## Cashflow & balance sheet（不適用）

- 現金流量表 `cashflow`、季度現金流量表 `quarterly_cf`、資產負債表 `balance_sheet` / `quarterly_bs` 皆回傳空陣列，FCF、FCF/NI、淨負債、流動比率、負債權益比等 DATA_UNAVAILABLE。
- 可引用的替代指標：`netAssets` = 46.23B USD（與 totalAssets 一致）；`sharesOutstanding` = 109,700,000 股（見下方資料一致性警示）。
- 基金本身無槓桿舉債結構的揭露資料，不得自行推定。

## Capital allocation & insider signal

- 配息：`trailingAnnualDividendRate` = 2.152 USD（近 12 個月），`trailingAnnualDividendYield` = 0.02657，即約 2.66%（以 81.49 計算約 2.64%，兩者吻合）。配息頻率與最近除息日未回傳（`dividendDate` 為 1496793600，即 2017 年，屬過期欄位，不採用）。
- 內部人交易：`insider` 回傳空陣列。ETF 無內部人申報制度，故無淨買賣訊號，視為不適用。
- 機構持股：`inst_holders` 與 `major_holders` 皆回傳空陣列，持有人集中度與機構流向 DATA_UNAVAILABLE。
- 資金流向（fund flows / creation-redemption）：工具未提供，DATA_UNAVAILABLE。`averageVolume` 為 39,170,962 股（3 個月平均）、`averageVolume10days` 為 34,426,290 股，此為交易量指標而非資金流，不可直接解讀為申購贖回。

## Valuation

- 本益比：`epsTrailingTwelveMonths` = -12.586、`forwardPE` = -4074.5、`epsForward` = -0.02；對 ETF 而言這些值不具備公司盈餘意義，且 forwardPE 為負值無效，標示為不適用，不作為估值依據。
- 淨值與溢折價：`navPrice` = 81.44277 USD；現價 81.49 USD（fast_info `last_price`）。溢價 = 81.49 / 81.44277 − 1 ≈ +0.058%，屬極小幅溢價，流動性與定價效率正常。注意 info 的 bid 82.92 與 ask 82.97 明顯高於現價，與 last_price 不一致，屬過時或錯誤報價，本報告不採用 bid/ask 計算價差。
- 帳面價值：`priceToBook` = 0.547 與 `bookValue` = 148.865 並不符合 NAV（81.44），與基金淨值定義不一致，判定為不可靠，不引用。
- EV/EBITDA、P/FCF、P/S 不適用。
- 同類比較：工具未提供同類（Long Government）中位數或其他 ETF 的 expense ratio、duration 比較資料，故「sector median」欄位以 n/a 表示，不估計。
- 費用率：`netExpenseRatio` = 0.15%，為本基金最明確的成本指標。
- 波動度：`beta3Year` = 2.31，與長天期公債的利率敏感度並不直觀相符，且工具未說明基準指數，視為可疑值，不作為風險結論依據。
- 技術面（ta snapshot，as_of 2026-10-29）：價格 81.49；MA20 = 79.445（價格高於 +2.57%）；MA50 = 80.509（高於 +1.22%）；MA200 = 84.654（低於 −3.74%）。MACD = 0.4435、signal = 0.0845、hist = +0.3590，動能偏多。RSI14 = 60.8，未達超買。Bollinger %B = 0.80，接近上軌（上軌 82.82、下軌 76.07）。ATR14 = 0.806 USD。20 日年化波動率 10.8%。
- 區間位置：52 週低點 76.43 USD，52 週高點在 info 為 90.86、ta 為 91.89（兩來源不一致，已標示）；現價距低點 +6.6%，距高點約 −10.3%（以 info）或 −11.3%（以 ta）。
- 動能：1M +4.77%、3M −0.92%、6M −4.82%、12M −11.44%。

## Key catalysts

- 財報：TLT 無財報，`earnings_dates` 回傳錯誤（連線失敗），下次「財報」不適用。
- 宏觀催化劑（需由宏觀研究員補充，本報告不作預測）：長天期美國公債殖利率走勢直接影響 TLT 淨值，主要變數包括聯準會政策路徑、通膨數據、美國公債發行與期限結構變化。
- 指數結構變動：指數成分每月再平衡，成分到期或新發行公債納入會改變有效存續期；工具未回傳當前 duration 數據，無法量化此影響。
- 1 個月動能轉正（+4.77%）與 MACD 翻多為技術面近期正向訊號；200 日均線（84.65）為中期壓力位，價格距離約 3.7%。
- 配息：目前年化配息約 2.152 USD，除息日未知，無法列入事件日曆。

## Metrics table

金額單位：USD 以 B（十億美元）或 M（百萬美元）標示；本表無 TWD/KRW 數值。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 總資產 totalAssets（USD B） | 46.23 | DATA_UNAVAILABLE（無歷史序列） | n/a | 規模大、流動性充足 |
| 費用率 netExpenseRatio | 0.15% | n/a | n/a（無同類數據） | 對被動式長天期公債 ETF 屬合理水準，成本不構成主要拖累 |
| 現價 vs NAV 溢折價 | +0.058%（81.49 vs 81.44277） | n/a | n/a | 幾乎平價，定價效率正常 |
| 12 個月配息率（trailingAnnualDividendYield） | 2.66% | n/a | n/a | 收益率約 2.7%，計算吻合 |
| 近期報酬 YTD | -7.998% | n/a | n/a | 長天期公債弱勢 |
| 近 12 個月動能 mom_12m | -11.44% | n/a | n/a | 中期偏弱 |
| 價格 vs MA200 | -3.74% | n/a | n/a | 仍位於長期均線下方 |
| 價格 vs MA50 | +1.22% | n/a | n/a | 短中期站回均線 |
| RSI14 | 60.8 | n/a | n/a | 偏強但未超買 |
| MACD hist | +0.359 | n/a | n/a | 動能偏多 |
| Bollinger %B | 0.80 | n/a | n/a | 接近上軌，短線偏熱 |
| ATR14（USD） | 0.806 | n/a | n/a | 日內波動正常 |
| 20 日年化波動率 | 10.8% | n/a | n/a | 波動度中等 |
| 52 週區間位置 | 距低點 +6.6%、距高點 -10.3%（info）/ -11.3%（ta） | n/a | n/a | 位於區間中下段 |
| 存續期 duration | DATA_UNAVAILABLE | n/a | n/a | 無法評估利率敏感度 |
| SEC yield | DATA_UNAVAILABLE | n/a | n/a | 無法評估 |
| 資金流向 fund flows | DATA_UNAVAILABLE | n/a | n/a | 無法評估 |
| 持倉集中度 / 期限分布 | DATA_UNAVAILABLE（僅知指數定義為 > 20 年） | n/a | n/a | 無法量化 |
| P/E、forwardPE | 不適用（EPS 為負、forwardPE 無效） | n/a | n/a | 不適用 |
| 內部人淨買賣 | 不適用（ETF 無內部人申報，insider 為空） | n/a | n/a | 不適用 |
| 機構持股 | DATA_UNAVAILABLE | n/a | n/a | 無法評估 |
| 財務報表（營收、FCF、負債） | DATA_UNAVAILABLE | n/a | n/a | 不適用於 ETF |

## Red flags

- 資料缺口大：財務報表、資產負債、內部人、機構持股、財報日曆、存續期、SEC yield、資金流向全部 DATA_UNAVAILABLE，本報告的基本面評估深度受限。
- 股數與淨資產不一致：`sharesOutstanding` = 109.7M 股，若以 `netAssets` 46.23B USD 反推，隱含每股淨值約 421 USD，與 `navPrice` 81.44 USD 相差約五倍，無法同時成立。此為欄位層級的資料品質問題，不可用於計算市值或每股指標，需以後續資料源核對。
- 報價不一致：info 的 bid 82.92 / ask 82.97 高於 last_price 81.49；52 週高點 info 為 90.86、ta 為 91.89；info 的 `yield` 0.05 與 `dividendYield` 5.0 與 `trailingAnnualDividendYield` 0.0266 單位不一致。本報告以 `trailingAnnualDividendYield` 與 fast_info 價格為準。
- 估值欄位失真：`priceToBook` 0.547 與 `bookValue` 148.865 與 NAV 不符；`forwardPE` -4074.5 為負值無效；`beta3Year` 2.31 對長天期公債顯著偏高，疑似口徑錯誤。
- 利率風險：長天期公債對利率高度敏感，20 年以上存續期代表殖利率小幅上升即可造成淨值明顯下跌；YTD -8.0%、12 個月 -11.4%、距 52 週高點約 10% 以上，顯示利率環境對本標的不利。
- 技術面：價格仍低於 200 日均線約 3.7%，中期趨勢未翻多；Bollinger %B 0.80 接近上軌，短線漲幅後存在回測風險（僅為技術描述，非交易建議）。
- 時點風險：多數資料為 2026-10-30 之前的快取，`regularMarketTime` 指向 2026-10-31 00:00 UTC，與分析基準日存在時差，引用時需確認對應交易日。

FUNDAMENTALS REPORT COMPLETE
