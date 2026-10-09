# Fundamentals — TLT as of 2026-10-10

> **資料說明**: 要求日期為 2026-10-10, 但今日為 2026-10-09, 目前可用的最新價格 bar 為 **2026-10-08 收盤** (yf info 的 regularMarketTime 亦指向 10-08 收盤)。2026-10-09 與 2026-10-10 尚無資料, 本報告所有數字皆以 2026-10-08 為準, 不引用任何 10-10 之後資訊。Live feed (Yahoo) 遭 403 阻擋, 數據來自 repo 快取 `prices/yf/TLT.json` 與 `prices/TLT.csv` (預期行為)。TLT 為 ETF, 本報告以基金指標取代公司型財務指標。

## Executive summary
TLT 為 iShares 20+ Year Treasury Bond ETF, 資產規模 $46.23B, 費用率 0.15%, 基金結構面無明顯異常, 但價格趨勢為明確下跌 (現價 $77.87, 距 52 週高點 -15.53%, 距 52 週低點 +1.88%, 三條均線皆向下)。由於 TLT 的價格核心驅動是 20 年以上美國公債殖利率, 本報告無法以公司型估值評估其「便宜或昂貴」; 估值面僅能確認 NAV 溢價約 +0.96% (以前一交易日 NAV 估算)。存續期間、SEC 收益率、資金流等關鍵基金指標在本地工具中皆無資料, 已標示 DATA_UNAVAILABLE。

## 基金結構與收益 (取代營收與獲利)
- **標的指數**: 美國公債剩餘年期 > 20 年、面額 ≥ $3 億且排除 Fed 持有部分的指數; 基金至少 80% 資產投資於指數成分, 至少 90% 投資於美國公債 (info.longBusinessSummary)。
- **費用率**: netExpenseRatio = 0.15% (info)。以 AUM $46.23B 推算年費用約 $69M (衍生計算)。
- **分配收益率**: trailingAnnualDividendRate = $2.152, trailingAnnualDividendYield = 2.79% (info, 與 $2.152 / 現價 $77.87 = 2.76% 幾乎一致, 屬衍生驗證)。
- **SEC 30 日收益率**: DATA_UNAVAILABLE (工具無此欄位)。
- **平均年期 (average maturity) / 存續期間 (effective / modified duration)**: DATA_UNAVAILABLE。工具未提供。次級來源 (news.md 引用的彙整網站) 稱存續期間約 16 至 17 年, 屬未驗證數字, 不應作為輸入。
- **Yield 欄位異常**: info.yield = 0.05 與 info.dividendYield = 5.0 與實際分配收益率 2.79% 不符, 疑為單位錯誤, 不採用。
- **報酬 (價格基礎, 含 TA 工具計算)**:
  - YTD: -7.998% (info.ytdReturn)
  - 1 個月: -4.72%, 3 個月: -7.81%, 6 個月: -10.18%, 12 個月: -12.68%
  - 3 個月 NAV 報酬: -8.85% (info.trailingThreeMonthNavReturns)
  - 3 年平均年化報酬: +1.11%, 5 年平均年化報酬: -8.38% (info, Yahoo 定義)
- **歷史高低**: 52 週區間 $76.43 – $92.19; 歷史高點 $179.70 / 歷史低點 $76.43 (info.allTimeHigh / allTimeLow)。現價已接近歷史低點區。
- **Beta**: beta3Year = 2.31 (info)。對一檔利率型 ETF 而言數值偏高, 且 beta 對利率環境高度敏感, 僅列為原始欄位, 不作為風險評級依據。

## 資產規模與資金流 (取代現金流與資產負債表)
- **AUM (totalAssets / netAssets)**: $46,233,321,472 (約 $46.23B) (info)。
- **AUM 趨勢 (YoY)**: DATA_UNAVAILABLE (工具只提供最新快照, 無歷史 AUM 序列)。
- **股數**: sharesOutstanding = 109.7M (info)。但 109.7M × NAV $77.13 ≈ $8.46B, 與 AUM $46.23B 相差約 5.5 倍, 兩欄位彼此不一致, **屬資料品質警示**, 股數欄位不採用, AUM 以 totalAssets 為準。
- **資金流 (fund flows, 週/月/年淨申購贖回)**: DATA_UNAVAILABLE。工具無此資料, 亦無 ETF 流量來源可用。
- **成交量流動性**:
  - 2026-10-08 成交量 49.38M (prices/TLT.csv)
  - 10 日均量 59.0M (info.averageDailyVolume10Day), 3 個月均量 35.94M (info.averageDailyVolume3Month)
  - 10-08 量能為 10 日均量的 0.84 倍 (衍生計算), 反彈日量能未放大
- **ATR14**: $0.80 (約 1.03%), 20 日年化波動 10.56% (ta snapshot)。

## 分配與持有人結構 (取代資本配置與內部人訊號)
- **分配 (dividend)**: 最近一次分配欄位 dividendDate 對應 2017-06-07 (Unix 1496793600), 屬歷史資料, 不代表近期分配; 近期分配頻率與下次除息日 n/a。
- **分配覆蓋率**: 不適用 (ETF 分配來自債券票息, 非盈餘覆蓋概念)。
- **申購贖回 / 做市商活動**: DATA_UNAVAILABLE。
- **主要持有人 (major_holders)、機構持有人 (inst_holders)**: 工具回傳空陣列, 記為 n/a。
- **內部人交易 (insider)**: ETF 無內部人交易概念, 工具回傳空陣列, 記為 n/a (不適用)。

## 估值 (NAV 溢折價與價格位置)
- **市價**: $77.87 (2026-10-08 收盤, regularMarketPrice)。
- **NAV**: navPrice = $77.12984 (info)。NAV 的日期未在欄位中明示, 數值接近 2026-10-07 收盤 $77.145 (prices/TLT.csv), 推測為前一交易日 NAV。
- **NAV 溢價**: 77.87 / 77.12984 − 1 = **+0.96%** (衍生計算, 以前一交易日 NAV 估算, 非盤中 iNAV 比較)。溢價幅度小, 屬正常範圍。
- **bid / ask**: bid 82.92 / ask 82.97 (info)。這與市價 $77.87 明顯不符, 可能為快取失真或報價欄位過期, **不採用, 也不得用來計算即時價差**。bid-ask spread 以 n/a 處理。
- **P/E、Forward P/E、P/B、EV/EBITDA、P/FCF、P/S**: 對 ETF 不適用。info 的 forwardPE = -3893.5 與 priceToBook = 0.52 為無意義數字, 不採用。epsTrailingTwelveMonths = -12.586 與 epsForward = -0.02 亦不適用。
- **同類比較**: category = Long Government。同類 ETF 費用率、規模、存續期間之中位數 n/a (工具無同類資料)。估計 (非工具數據): 美國長天期公債 ETF 費用率多落在 0.03% – 0.15% 區間, TLT 的 0.15% 位於同類偏高端; 此為一般產業知識估計, 未從本地資料驗證。
- **技術面位置 (參考)**: 價格位於 BB 中軌 $79.42 與下軌 $75.92 之間, BB %B = 0.28; RSI14 = 33.45 (弱勢區, 接近超賣, 10-05 最低 22.0)。

## Key catalysts
- **Earnings**: 不適用 (ETF 無盈餘公告)。earnings_dates 工具連線失敗, 記為 n/a。
- **下一個重要總體事件 (取自同日 news.md, 未由本工具驗證)**:
  - 2026-10-14 (週三) 9 月 CPI 公布: 通膨超預期會推升長端殖利率, 對 TLT 不利; 低於預期則有利。
  - 2026-10-27 至 10-28 FOMC 會議, 10-28 公布利率決議 (非 SEP 會議)。
  - 2026-11-06 非農就業, 以及 11 月初季度再融資公告 (Treasury 借款規模) 會影響長端供給預期。
- **長端殖利率背景 (news.md 引用, 未驗證)**: 30 年期殖利率於 10-07 盤中約 5.70%, 為 2002 年以來高點; 2026-09-16 FOMC 升息 25bp 至 3.75%–4.00%, dot plot 顯示 2026 年底中位數 4.1%。
- **長債拍賣**: 2026-10-08 30 年期重新開標結果未取得, 為需求面關鍵資料缺口。
- **基金層面事件**: 無 (指數重構、費用變更、基金合併等資料 n/a)。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 價格 (2026-10-08 收盤) | $77.87 | 12m -12.68% (TA 計算) | n/a | 偏弱, 趨勢下行 |
| YTD 報酬 | -7.998% | n/a | n/a | 偏弱 |
| 3 年平均年化報酬 | +1.11% | n/a | n/a | 中性偏弱 |
| 5 年平均年化報酬 | -8.38% | n/a | n/a | 偏弱 |
| AUM (totalAssets) | $46.23B | DATA_UNAVAILABLE | n/a | 規模大, 流動性充足 |
| 資金流 (淨申購贖回) | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | 無法判定 |
| 費用率 (netExpenseRatio) | 0.15% | n/a | 0.03%–0.15% (估計, 非工具數據) | 偏高端 |
| 分配收益率 (trailing) | 2.79% | n/a | n/a | 中性 |
| SEC 30 日收益率 | DATA_UNAVAILABLE | n/a | n/a | 無法判定 |
| 平均年期 / 存續期間 | DATA_UNAVAILABLE | n/a | n/a | 無法判定 (次級來源 16–17 年未驗證) |
| NAV 溢折價 | +0.96% (前一日 NAV) | n/a | 接近 0 (估計) | 正常範圍 |
| 買賣價差 (bid-ask) | n/a (報價欄位不可信) | n/a | n/a | 無法判定 |
| 52 週位置 | 距高 -15.53%, 距低 +1.88% | n/a | n/a | 接近 52 週低點 |
| RSI14 | 33.45 | n/a | 50 (中性參考) | 弱勢, 接近超賣 |
| MA50 / MA200 相對 | -4.07% / -8.62% | n/a | n/a | 空頭排列 |
| 20 日年化波動 | 10.56% | n/a | n/a | 低波動 |
| ATR14 | $0.80 (1.03%) | n/a | n/a | 日內波動正常 |
| Beta (3y) | 2.31 | n/a | n/a | 數值偏高, 僅供參考 |
| 內部人交易 / 機構持有 | n/a (ETF 不適用) | n/a | n/a | 不適用 |
| 股數 vs AUM 一致性 | 不一致 (109.7M vs $46.23B) | n/a | n/a | 資料品質警示 |

## Red flags
- **殖利率環境逆風**: 長端殖利率處於高位 (30 年期約 5.7%, 次級來源未驗證), 基金淨值與價格對利率高度敏感, 且 TLT 的價格走勢與長端殖利率負相關。
- **價格趨勢弱**: 三條均線向下, MA50 低於 MA200 (死亡交叉狀態), 價格距 52 週低點僅 1.88%, 52 週低點 $76.43 為關鍵價位。
- **資料缺口**: SEC 收益率、存續期間、平均年期、資金流、AUM 歷史趨勢、同類比較皆無資料, 無法完整評估基金品質與流動性動態。
- **資料品質警示**: sharesOutstanding (109.7M) 與 AUM ($46.23B) 不一致; bid/ask (82.92/82.97) 與市價 $77.87 不符; info.yield (0.05) 與 dividendYield (5.0) 與實際分配收益率不符; forwardPE、priceToBook 對 ETF 無意義。以上欄位已排除於結論之外。
- **日期差異**: 報告要求 as-of 2026-10-10, 實際最新數據為 2026-10-08 收盤; 10-09 與 10-10 無資料, 不得視為已驗證。
- **工具連線失敗**: earnings_dates 與 fast_info 的部分欄位因 Yahoo 403 阻擋無法即時取得, 本報告依 repo 快取。

FUNDAMENTALS REPORT COMPLETE
