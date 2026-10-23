# Fundamentals — GLD (SPDR Gold Shares) as of 2026-10-24

> 資料時點: 價格與 info 欄位為 2026-10-22 (週四) 美股收盤 (regularMarketTime 2026-10-22 20:00 UTC)，快取時間 2026-10-23。相對 2026-10-24 分析日屬於較舊資料，未發現晚於分析日的資料。所有數據來源均為 cache (pricefeed fallback)，屬預期行為。

## Executive summary
GLD 是以實體金條為唯一資產的商品信託 ETF，規模 USD 141.70B，費用率 0.40%，屬於黃金的被動持有工具，沒有營運面的財務健康指標可評估。截至 2026-10-22，收盤價 369.00 USD 相對 NAV 371.04 USD 小幅折價約 0.55%，股價位於 MA20 / MA50 / MA200 之下 (分別為 -3.0% / -6.6% / -11.0%)，RSI14 35.7，技術面偏弱，但 52 週低點僅 2.5% 之距，價格區間位於 360–510 USD 的寬幅區間下緣。基本面 (費用、規模、折溢價) 本身無明顯異常，主要風險來自黃金價格走勢本身，而 NAV 對現貨金價的比較、基金申購贖回流量等關鍵資料於本次工具中皆無法取得。

## Revenue & profitability (不適用，改為標的與規模概況)
- 信託性質: 持有金條，並於必要時發行 Baskets 以換取黃金存款、贖回時分配黃金 (info.longBusinessSummary)。投資目標是讓股份反映黃金現貨價格扣除費用後的表現。
- 持倉集中度: 單一資產 100% 為實體黃金 (依信託定義)。`major_holders` 與 `inst_holders` 皆回傳空陣列 `[]`，因此機構持有人分布、前幾大持有人比重: DATA_UNAVAILABLE。
- 規模: `totalAssets` = 141,702,414,336 USD，即 **141.70B USD** (`netAssets` 同值)。
- AUM 趨勢: 工具僅提供單一時點的 AUM，無歷史 AUM 序列，因此 1 個月 / 1 年 AUM 變化: DATA_UNAVAILABLE。
- 基金基本資訊: 基金公司 State Street Investment Management，類別 Commodities Focused，成立時間 (fundInceptionDate 1100736000) 約為 2004-11，交易所 NYSEArca。
- 歷史報酬 (info): YTD -3.34%，3 個月 +3.63%，3 年平均年化 +0.27%，5 年平均年化 +0.18%。
- 3 年 beta: 0.44。

## Cashflow & balance sheet (不適用)
- 本標的無營運現金流與資產負債表。現金流、負債、ROE/ROIC、毛利率等欄位皆不適用，`epsTrailingTwelveMonths` 為 -9.394，屬信託會計的損益口徑，不作為獲利指標解讀。
- 費用率 0.40% (`netExpenseRatio` 0.4)。依此推算一年的費用規模約 0.57B USD (0.40% × 141.70B，屬本報告自行推算)。
- 會計帳面價值 `bookValue` 170.017 USD，與 NAV 371.04 USD 差距很大。信託財報多以成本與市價孰低計價，因此 `priceToBook` 2.17 的意義有限，不宜據此判斷高估。

## Capital allocation & insider signal
- 配息: `dividendYield` 0.0，`trailingAnnualDividendRate` 0.0。ETF 不配息，無股息覆蓋率概念。
- 買回與資本支出: 不適用 (信託無營運資本支出與庫藏股)。
- 申購贖回流量 (net creations/redemptions): DATA_UNAVAILABLE。工具未提供，無法判斷近期資金是流入或流出。
- 股數與規模的一致性: `sharesOutstanding` 260,300,000 股，以 NAV 371.04 計算約 96.6B USD，與 `netAssets` 141.70B USD 相差約 47%。以 `netAssets` ÷ NAV 反推約 382M 股，與 `sharesOutstanding` 不符。兩個欄位來源或時點可能不同，本報告以 `netAssets` / `totalAssets` 作為規模口徑，並標記為待確認。
- 內部人交易 (insider): 本標的為信託，無公司內部人，不適用。`insider` 工具未於本次執行，視為不適用。

## Valuation
- 折溢價 (Premium / Discount to NAV):
  - 市價 369.00 USD，NAV 371.0446 USD，折價約 **-0.55%**。
  - 這屬於輕微折價，在 GLD 這類高流動性實體黃金 ETF 中屬正常範圍，不構成估值訊號。
- NAV 對現貨金價: 現貨金價 (XAU/USD) 與 GC=F 期貨報價在工具中皆無法取得 (GC=F 回傳 no price data)，因此「NAV 對應金價」的隱含每盎司金價比較: DATA_UNAVAILABLE。
- 本標的的 P/E、EV/EBITDA、P/FCF、P/S 皆不適用 (無盈餘與營收)。`trailingPegRatio` 為 null，PEG 亦不適用。
- 技術面估值參考 (來自 ta snapshot，as_of 2026-10-22):
  - 收盤 369.00，距 MA20 -3.0% (MA20 380.43)、距 MA50 -6.6% (MA50 395.15)、距 MA200 -11.0% (MA200 414.42)。
  - 52 週區間 360.12–509.7 USD (info)，現價距 52 週高點 -27.6%，距 52 週低點 +2.5%。
  - 1 年 (約 400 個交易日的序列，起點 2025-03-21) 收盤最高 495.9 USD、最低 273.71 USD。注意 info 的 52 週高點 509.7 可能為盤中價，與收盤序列不同。
- 動能: 1 個月 -6.1%，3 個月 -0.8%，6 個月 -14.4%，12 個月 -2.2%。
- 波動: 20 日年化波動 22.1%，ATR14 5.90 USD (約 1.6% 日內波幅)。
- 指標: MACD -4.67 (訊號線 -4.46，柱狀 -0.21，仍為負值)，RSI14 35.7 (接近超賣前區)，布林帶 %B -0.12 (價格低於下軌)。
- 成交量: 10/22 成交量 17.0M 股，約為 3 個月均量 9.46M 的 1.8 倍，與 -2.63% 的下跌同步。

## Key catalysts
- 無公司財報，無 earnings_dates。ETF 無季報與指引。
- 主要驅動因素為黃金現貨價格與美元、實質利率、央行黃金購買等宏觀變數。本次工具未提供這些數據，因此 DATA_UNAVAILABLE，不做推論。
- 後續需關注的資料: 現貨金價 (XAU/USD) 與 GLD 的 NAV 對照、申購贖回流量、AUM 變化。
- 下一次財報: 不適用。

## Metrics table
單位: AUM 以 USD B 表示，價格以 USD 表示，無 億 單位。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 資產規模 AUM (USD B) | 141.70 | DATA_UNAVAILABLE (無歷史序列) | 不適用 | 規模充足，流動性佳 |
| 費用率 Expense ratio | 0.40% | n/a | 不適用 (同類 ETF 無 sector median) | 屬 Gold ETF 常見費率區間，偏高於部分低費率競品，需看同類比較 |
| 市價 / NAV 折溢價 | 369.00 / 371.04，-0.55% | n/a | 不適用 | 輕微折價，屬正常 |
| 現貨金價對照 (XAU/USD) | DATA_UNAVAILABLE | DATA_UNAVAILABLE | 不適用 | 無法評估 NAV 追蹤誤差 |
| 申購贖回淨流量 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | 不適用 | 無法判斷資金動向 |
| 持倉集中度 | 100% 實體黃金 (依信託定義) | n/a | 不適用 | 單一資產，無分散效果 |
| 3 年 beta | 0.44 | n/a | 不適用 | 與股市相關性低，為避險屬性 |
| YTD 報酬 | -3.34% | n/a | 不適用 | 年內偏弱 |
| 價格 vs 52 週高點 | -27.6% (高 509.7) | n/a | 不適用 | 處於大幅修正後的區間 |
| 價格 vs MA200 | -11.0% | n/a | 不適用 | 長期趨勢偏弱 |
| RSI14 | 35.7 | n/a | 不適用 | 接近超賣邊緣，中性偏弱 |
| 20 日年化波動 | 22.1% | n/a | 不適用 | 中等波動 |
| 股數 sharesOutstanding | 260.3M | n/a | 不適用 | 與 netAssets 推算股數不一致，待確認 |
| 股息殖利率 | 0.0% | n/a | 不適用 | 無配息 (設計如此) |
| P/E, EV/EBITDA, P/FCF, P/S | 不適用 | 不適用 | 不適用 | 信託無盈餘、營收 |

## Red flags
- 現貨金價與 NAV 比較、申購贖回流量、AUM 歷史趨勢皆為 DATA_UNAVAILABLE，本報告無法確認 NAV 追蹤誤差或資金流向，這是最大的資料缺口。
- `sharesOutstanding` (260.3M) 與 `netAssets` ÷ NAV 推算股數 (約 382M) 不一致，約差 47%，規模口徑需向資料源確認。
- `major_holders` / `inst_holders` 皆為空，無法評估機構持有集中度。
- 價格資料為 2026-10-22 收盤，相對 2026-10-24 分析日屬於較舊資料，且來源為快取 (pricefeed cache fallback)。
- 技術面全面偏弱: 價格低於 MA20 / MA50 / MA200，MACD 為負，10/22 量能放大伴隨 -2.6% 的下跌。
- `info` 的 52 週高點 509.7 與收盤序列最高 495.9 不一致，疑為盤中高點，比較時需注意口徑。

FUNDAMENTALS REPORT COMPLETE
