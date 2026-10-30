# Fundamentals — GLD (SPDR Gold Shares) as of 2026-10-31

> 資料時點: 價格與 info 欄位為 2026-10-29 (週四) 美股收盤 (regularMarketTime 2026-10-29 20:00 UTC)，快取時間 2026-10-30。分析日 2026-10-31 為週六，最近一個交易日 2026-10-30 (週五) 的收盤未納入本次快取，因此資料落後約一個交易日。未發現晚於分析日的資料。所有數據來源均為 repo 快取 (prices/, prices/yf/)，屬預期行為。

## Executive summary
GLD 是以實體金條為唯一資產的商品信託 ETF，規模 141.70B USD，費用率 0.40%，沒有營收、獲利、現金流等營運面指標可供評估，判讀重點在於規模、折溢價與黃金價格走勢本身。截至 2026-10-29，收盤價 368.57 USD 相對 navPrice 369.00 USD 僅折價約 0.12%，屬正常範圍，估值層面沒有明顯訊號。技術面偏弱: 價格位於 MA20 / MA50 / MA200 之下 (分別為 -2.2% / -5.9% / -10.8%)，MACD 為負、RSI14 為 38.5，距 52 週高點 509.7 USD 仍有 27.7% 的跌幅空間，但距 52 週低點 361.36 USD 僅 2.0%。

## Revenue & profitability (不適用，改為標的與規模概況)
- 信託性質: 持有金條，並於必要時發行 Baskets 以換取黃金存款、贖回時分配黃金 (info.longBusinessSummary)。投資目標為讓股份反映黃金現貨價格扣除費用後的表現。
- 持倉集中度: 單一資產 100% 為實體黃金 (依信託定義)，無分散效果。`major_holders` 與 `inst_holders` 皆回傳空陣列，前幾大持有人比重與機構持有分布: DATA_UNAVAILABLE。
- 規模: `totalAssets` 與 `netAssets` 同為 141,702,414,336 USD，即 **141.70B USD**。
- AUM 趨勢: 工具只提供單一時點的 AUM，無歷史序列，1 個月 / 1 年 AUM 變化: DATA_UNAVAILABLE。
- 基金基本資訊: 基金公司 State Street Investment Management，類別 Commodities Focused，成立時間 (fundInceptionDate 1100736000) 約為 2004-11，交易所 NYSEArca，貨幣 USD。
- 歷史報酬 (info): YTD -3.34%，3 個月 +3.63%，3 年平均年化 +0.26%，5 年平均年化 +0.17%。
- 3 年 beta: 0.44，與股市相關性偏低，具避險屬性描述。

## Cashflow & balance sheet (不適用)
- 信託無營運現金流與資產負債表。`financials`、`balance_sheet`、`cashflow` 三項工具皆回傳空陣列，相關欄位全部 DATA_UNAVAILABLE，且對本標的本來就不適用。
- `epsTrailingTwelveMonths` 為 -9.394，屬信託會計的損益口徑，不作為獲利指標解讀。
- 費用率 `netExpenseRatio` 0.40%。以 141.70B USD 推算，一年費用規模約 0.57B USD (0.40% × 141.70B，為本報告自行推算)。
- 帳面價值 `bookValue` 170.017 USD 與市價 368.57 USD 差距大，信託財報多以成本與市價孰低計價，`priceToBook` 2.17 的意義有限，不宜據此判斷高估。

## Capital allocation & insider signal
- 配息: `dividendYield` 0.0，`trailingAnnualDividendRate` 0.0。ETF 不配息，無股息覆蓋率概念。
- 買回與資本支出: 不適用 (信託無營運資本支出與庫藏股)。
- 申購贖回淨流量 (net creations / redemptions): DATA_UNAVAILABLE，工具未提供，無法判斷近期資金是流入或流出。
- 股數與規模一致性: `sharesOutstanding` 為 260,300,000 股，以 navPrice 369.00 計算約 96.0B USD；但 `netAssets` 141.70B USD ÷ 369.00 反推約 384M 股，兩者相差約 47%。兩欄位來源或時點可能不同，本報告以 `netAssets` / `totalAssets` 作為規模口徑，股數口徑待確認。
- 內部人交易 (insider): `insider` 工具回傳空陣列。信託無公司內部人，此欄位以 DATA_UNAVAILABLE 標示，實際上不適用於本標的。

## Valuation
- 折溢價 (Premium / Discount to NAV): 市價 368.57 USD，navPrice 369.00 USD，折價約 **-0.12%**。在高流動性實體黃金 ETF 中屬正常範圍，不構成估值訊號。
- 單日變化: 10/29 收盤 -1.32% (由 373.51 跌至 368.57)，日內區間 366.97–369.94，成交量 8,983,381 股，約為 3 個月均量 9,618,046 股的 0.93 倍，屬溫和量能。
- NAV 對應現貨金價: 工具未提供現貨金價 (XAU/USD) 與黃金期貨的同期報價，「NAV 隱含金價」與追蹤誤差: DATA_UNAVAILABLE。
- 本標的的 P/E、EV/EBITDA、P/FCF、P/S 皆不適用 (無盈餘與營收)。`trailingPegRatio` 為 null，PEG 亦不適用。
- 技術面估值參考 (來自 ta snapshot，as_of 2026-10-29):
  - 收盤 368.57，距 MA20 376.98 為 -2.2%，距 MA50 391.76 為 -5.9%，距 MA200 413.27 為 -10.8%。
  - 52 週區間 361.36–509.7 USD，現價距 52 週高點 -27.7%，距 52 週低點 +2.0%。
  - 動能: 1 個月 -3.2%，3 個月 -0.8%，6 個月 -13.0%，12 個月 +1.1%。
  - 指標: MACD -5.34，訊號線 -5.09，柱狀 -0.26，仍為負值且柱狀縮小幅度有限；RSI14 38.5，尚未進入超賣區；布林帶 %B 0.12，價格位於中軌與下軌之間偏下緣。
  - 波動: 20 日年化波動 17.7%，ATR14 5.63 USD (約 1.5% 日內波幅)。

## Key catalysts
- 無公司財報，`earnings_dates` 無法取得，下一次財報: 不適用。ETF 無季報與管理層指引。
- 主要驅動因素為黃金現貨價格，以及美元、實質利率、央行黃金購買等宏觀變數。本次工具未提供這些數據，DATA_UNAVAILABLE，不做推論。
- 後續需追蹤的資料: 現貨金價 (XAU/USD) 與 GLD 的 NAV 對照、申購贖回淨流量、AUM 歷史變化。這些欄位補齊後，才能判斷折溢價與資金動向是否有結構性變化。
- 近期技術面事件: 價格已跌破 MA50 與 MA200，若未能收復 MA20 (約 377 USD) 則趨勢仍偏弱。

## Metrics table
單位: AUM 以 USD B 表示，價格以 USD 表示，本報告無 億 單位。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 資產規模 AUM (USD B) | 141.70 | DATA_UNAVAILABLE (無歷史序列) | 不適用 | 規模充足，流動性佳 |
| 費用率 Expense ratio | 0.40% | n/a | 不適用 (同類比較數據 DATA_UNAVAILABLE) | 費率固定，持有成本約 0.57B USD/年 (本報告推算) |
| 市價 vs NAV 折溢價 | 368.57 vs 369.00，-0.12% | n/a | 不適用 | 微幅折價，屬正常 |
| 現貨金價對照 (XAU/USD) | DATA_UNAVAILABLE | DATA_UNAVAILABLE | 不適用 | 無法評估 NAV 追蹤誤差 |
| 申購贖回淨流量 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | 不適用 | 無法判斷資金動向 |
| 持倉集中度 | 100% 實體黃金 | n/a | 不適用 | 單一資產，無分散效果 |
| 股數 sharesOutstanding | 260.3M (推算約 384M) | n/a | 不適用 | 與 netAssets 不一致，待確認 |
| 3 年 beta | 0.44 | n/a | 不適用 | 與股市相關性低 |
| YTD 報酬 | -3.34% | n/a | 不適用 | 年內偏弱 |
| 3 個月報酬 | +3.63% | n/a | 不適用 | 短期回升後再度轉弱 |
| 價格 vs 52 週高點 | -27.7% (高 509.7) | n/a | 不適用 | 處於大幅修正後區間 |
| 價格 vs MA200 | -10.8% | n/a | 不適用 | 長期趨勢偏弱 |
| RSI14 | 38.5 | n/a | 不適用 | 中性偏弱，未達超賣 |
| MACD 柱狀 | -0.26 | n/a | 不適用 | 負值，動能偏空 |
| 布林帶 %B | 0.12 | n/a | 不適用 | 位於下緣附近 |
| 20 日年化波動 | 17.7% | n/a | 不適用 | 中等波動 |
| ATR14 | 5.63 USD (約 1.5%) | n/a | 不適用 | 日內波幅正常 |
| 股息殖利率 | 0.0% | n/a | 不適用 | 無配息 (設計如此) |
| P/B (priceToBook) | 2.17 | n/a | 不適用 | 信託帳面價值意義有限，不作估值依據 |
| P/E, EV/EBITDA, P/FCF, P/S | 不適用 | 不適用 | 不適用 | 信託無盈餘、營收 |
| 盈餘 / 財報 / 內部人 / 機構持有 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | 不適用 | 工具無資料 |

## Red flags
- 現貨金價與 NAV 比較、申購贖回淨流量、AUM 歷史趨勢皆為 DATA_UNAVAILABLE，無法確認 NAV 追蹤誤差或資金流向，是本次最大的資料缺口。
- `sharesOutstanding` (260.3M) 與 `netAssets` ÷ NAV 推算股數 (約 384M) 相差約 47%，規模與股數口徑需向資料源確認。
- `major_holders`、`inst_holders`、`insider` 皆為空陣列，無法評估持有人集中度與資金面異動。
- 價格資料為 2026-10-29 收盤，分析日 2026-10-31 為週六，10-30 收盤未納入，資料落後一個交易日，且來源為 repo 快取。
- 技術面偏弱: 價格低於 MA20 / MA50 / MA200，MACD 為負，6 個月動能 -13.0%。
- `info` 的 52 週低點 361.39 與 `ta` 計算的 361.36 略有差異，屬來源口徑微差，不影響判讀。

FUNDAMENTALS REPORT COMPLETE
