# Fundamentals — TLT as of 2026-11-21

## Executive summary
TLT 為 iShares 20+ Year Treasury Bond ETF，屬長天期美國公債指數基金，不是營運公司，因此不適用營收、獲利率、資產負債表與 P/E 等公司財務框架，本報告改以基金規模（AUM 約 USD 47.52B）、費用率（0.15%）、長天期公債的利率敏感度與技術面為主軸。最新可得價格（2026-11-20 快取收盤約 80.985，較 52 週高點 90.86 低約 10.9%）顯示價格仍在 MA200（84.12）之下、MA50（80.06）之上，動能偏弱但短線已止跌於中期均線附近。基金的估值與資金流向無法以 yfinance 取得（flows、歷史 AUM、持倉明細皆為 DATA_UNAVAILABLE），因此「估值是否有吸引力」只能以 NAV 溢價與長端利率的宏觀條件定性判斷，無法與同業中位數比較。

## Revenue & profitability
本節不適用。TLT 無營收、毛利、營業利益與淨利，yfinance 的 financials / balance_sheet / cashflow 類別對 ETF 不提供資料，本報告未呼叫這些端點。
- 財報類 EPS 欄位（epsTrailingTwelveMonths = -12.586）為基金分配會計的會計欄位，並非公司獲利，不可解讀為虧損。
- 替代指標：基金配息率（trailingAnnualDividendRate = 2.152 USD，除以最新價 80.985 約 2.66%）。
- 1 年期 AUM 歷史、5 年 CAGR 與 segment mix：DATA_UNAVAILABLE（工具未提供 AUM 時間序列）。

## Cashflow & balance sheet
本節不適用於基金本身。以下為基金層級可得數據：
- 基金規模（totalAssets / netAssets）：USD 47.52B（47,518,568,448 USD，cache 時間 2026-11-20 15:24 UTC）。
- 淨值 NAV（navPrice）：80.31198 USD；bookValue 欄位為 148.865，與 NAV 不一致，判定為資料源錯誤，不採用。
- 流通股數：info 的 sharesOutstanding 為 109,700,000，與 AUM / NAV 推算值 約 591.6M 股（47.52B ÷ 80.31）明顯不符，判定為過期或錯誤欄位，不採用。
- 槓桿與負債：ETF 本身以現金與公債持有，無公司式負債比；衍生性商品使用情形 DATA_UNAVAILABLE。
- 流動性指標：近 10 日平均成交量 35,958,580 股、近 3 個月平均 39,155,293 股；2026-11-20 成交量 10,095,682 為盤中快照，非完整交易日。
- 持倉面：指數成分為到期年限超過 20 年、面額至少 USD 300M 的美國公債（不含 Fed 持有部分），基金至少 80% 資產追蹤指數、至少 90% 投資美國公債。持倉檔數、個別券種權重、加權存續期（duration）與殖利率：DATA_UNAVAILABLE。

## Capital allocation & insider signal
- 費用率（netExpenseRatio）：0.15%，對長天期公債 ETF 屬低費用水準（定性判斷）。
- 配息：trailingAnnualDividendRate 2.152 USD；info 的 yield 欄位為 0.0476、dividendYield 為 4.76、trailingAnnualDividendYield 為 0.026783，三者不一致。以 配息 ÷ 價格 推算約 2.66%，故採此值；4.76% 與 0.0476 疑為年化前瞻或資料源錯誤，需由交易員留意。dividends 端點本次回傳空值，配息歷史 DATA_UNAVAILABLE。
- 資金流（creations / redemptions）：DATA_UNAVAILABLE（工具未提供，本次無 WebSearch 可用來源）。
- 內部人交易：ETF 無內部人（insider 端點本次未呼叫，因基金無管理層持股申報概念），不適用。
- 機構持股（major_holders / inst_holders）：本次回傳空陣列，DATA_UNAVAILABLE。
- 價差：盤中 bid 82.92 / ask 82.97 出現在 info 快照，與 80.985 收盤快取價差距很大，明顯為非同步資料（bid/ask 欄位不可靠），不採用作為交易價格依據。

## Valuation
- P/E（trailing / forward）：n/a。epsTrailingTwelveMonths 為 -12.586、forwardPE 為 -4052.75，皆為基金會計產物，無經濟意義，不採用。
- P/B：priceToBook 0.544 由錯誤的 bookValue 推算，不採用。
- EV/EBITDA、P/FCF、P/S：不適用於 ETF。
- NAV 溢折價：收盤快取價 80.985 相對 navPrice 80.31198 為溢價約 +0.84%；info 盤中價 81.055 相對 NAV 為 +0.93%。溢價幅度小，但 NAV 為盤中以前一日為基礎的估值，僅供參考。
- Sector median：n/a（工具未提供同類 ETF 估值中位數；category 為 Long Government，同類比較 DATA_UNAVAILABLE）。
- 價格位置：以 info 52 週區間 76.43–90.86 計，現價位於區間約 31.6% 位置（(80.985−76.43)/(90.86−76.43)），偏下段；以快取收盤價 1 年區間 77.11–90.82 計算，亦位於約 31% 分位。
- 報酬：ytdReturn -2.92%（info）；以快取收盤價自 2026-01-02（87.03）至 2026-11-20（80.985）計，價格報酬為 -6.95%，兩者不一致（前者可能含配息），採用時需註明口徑。3 年平均報酬 0.43%、5 年平均報酬 -8.10%（info 欄位）。
- 風險指標：beta3Year = 2.3（資料源值，對純公債 ETF 而言偏高，對 S&P 500 的 beta 解讀需謹慎）；20 日年化波動率 10.40%（ta 工具）。

## Key catalysts
- 次要宏觀驅動（定性）：長天期公債價格對長端殖利率高度敏感，美國通膨數據、Fed 政策展望、財政赤字與國債拍賣需求為主要變數。具體日程（CPI、FOMC、長債拍賣日期）未由工具取得，DATA_UNAVAILABLE。
- 基金層面：無財報、無 earnings_dates（本次回傳空值），不適用。
- 指數重新配置：到期年限結構隨時間推移，持倉的平均存續期會改變，但具體再平衡日期 DATA_UNAVAILABLE。
- 近期價格事件：近 1 個月動能 -0.92%、近 3 個月 -1.91%、近 6 個月 -4.36%、近 12 個月 -8.88%（ta 工具）。現價已在 MA20（80.97）附近，MA50（80.06）略低於現價，MA200（84.12）在上方約 3.9%，中期下降趨勢尚未翻轉。

## Technical snapshot (ta tool, as_of 2026-11-20)
| 指標 | 數值 |
|---|---|
| 價格 | 80.985 |
| MA20 / MA50 / MA200 | 80.971 / 80.064 / 84.123 |
| 距 MA20 / MA50 / MA200 | +0.02% / +1.15% / -3.73% |
| RSI14 | 54.41 |
| MACD / signal / hist | -0.038 / 0.072 / -0.110 |
| 布林 %B | 0.504（中軌 80.971，上軌 82.783，下軌 79.160）|
| ATR14 | 0.738（約現價 0.91%）|
| 20 日年化波動 | 10.40% |
| 距 52 週高 / 低 | -10.87% / +5.96% |

## Metrics table
單位：價格與 NAV 為 USD；基金規模為 USD B；成交量為百萬股。ETF 無公司財務指標，以下僅列基金可得項目。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 基金規模 totalAssets (USD B) | 47.52 | DATA_UNAVAILABLE | n/a | 規模大、流動性充足（定性）|
| 最新價（收盤快取 2026-11-20，USD）| 80.985 | 1Y 價格報酬 約 -9.2%（89.23 → 80.985）| n/a | 位於 52 週區間下段 |
| NAV（navPrice，USD）| 80.312 | DATA_UNAVAILABLE | n/a | 溢價約 +0.84%，尚可 |
| 費用率 netExpenseRatio | 0.15% | DATA_UNAVAILABLE | n/a（同類 ETF 中位數 DATA_UNAVAILABLE）| 低費用 |
| 配息率（trailing 2.152 ÷ 價格）| 2.66% | DATA_UNAVAILABLE | n/a | 資料源 yield 欄位不一致，採推算值 |
| 流通股數 sharesOutstanding | 109.7M（與 AUM/NAV 推算 約 591.6M 不符）| DATA_UNAVAILABLE | n/a | 不可用，已排除 |
| 10 日平均成交量（百萬股）| 35.96 | DATA_UNAVAILABLE | n/a | 流動性高 |
| 3 個月平均成交量（百萬股）| 39.16 | DATA_UNAVAILABLE | n/a | 流動性高 |
| RSI14 | 54.41 | n/a | n/a | 中性偏多 |
| 距 MA200 | -3.73% | n/a | n/a | 仍在長期均線下方，偏弱 |
| 近 12 個月動能 | -8.88% | n/a | n/a | 長天期公債弱勢 |
| 20 日年化波動 | 10.40% | n/a | n/a | 波動中等偏高（對公債而言）|
| beta3Year（資料源值）| 2.30 | n/a | n/a | 數值偏高，解讀需謹慎 |
| 5 年平均報酬 | -8.10% | n/a | n/a | 長期負報酬 |
| 資金流 creations / redemptions | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | 無法評估 |
| 持倉檔數 / 加權存續期 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | 無法評估 |
| P/E、forward P/E | n/a | n/a | n/a | 不適用 |
| 內部人淨買賣 | 不適用 | 不適用 | 不適用 | ETF 無內部人 |

## Red flags
- 資料來源不一致：info 的 price（81.055）、ta / 收盤快取（80.985）、fast_info（80.86，cnyes 來源）三者價格不同，且多為盤中快照，時間點不一致，需以收盤資料為準。
- 股數與 bookValue 欄位錯誤：sharesOutstanding 與 bookValue 與 AUM / NAV 無法對齊，已排除。
- 配息殖利率三種口徑不一致（2.66% 推算、0.0476、4.76），需確認口徑後再用於比較。
- YTD 報酬口徑衝突：info 為 -2.92%，快取價格為 -6.95%。
- 資金流、持倉、AUM 歷史、配息歷史、機構持股、財報日程全數 DATA_UNAVAILABLE，基金基本面判斷的關鍵資料缺口大。
- 價格位於 MA200 之下（-3.73%），12 個月動能 -8.88%，中期趨勢偏空，對長端利率上行敏感。
- 最新快取時間為 2026-11-20 15:24 UTC（盤中），非 2026-11-21 完整交易日；本報告以 2026-11-21 為 as-of，但實際最新資料為 2026-11-20，無資料晚於 2026-11-21。

FUNDAMENTALS REPORT COMPLETE
