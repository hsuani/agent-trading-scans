# Fundamentals — UUP (Invesco DB US Dollar Index Bullish Fund) as of 2026-10-24

資料說明: 工具資料來源為 cache (cached_at 2026-10-23 11:31 UTC), 即時 feed 被阻擋, 屬預期情況。最新一筆價格時間戳為 2026-10-21 (regularMarketTime), TA 快照 as_of 2026-10-22, 因此資料落後報告日 1 至 2 個交易日, 沒有超過 2026-10-24 的資料。本標的為宏觀避險工具 (期貨基金), 非營運公司, 故不做營收、利潤率、資產負債表分析。單位: 金額以 USD (M) 表示。

## Executive summary
UUP 為追蹤美元指數 (DXY) 多頭期貨的 ETF, 淨資產約 $431.1M, 費用率 0.75%, 無公司基本面可評估。價格 28.90 位於 MA20 (28.93) 附近, 高於 MA50 (28.47) 與 MA200 (27.87), 中期趨勢偏多但短期 MACD 已呈負柱, 動能偏中性。估值面僅能看 NAV 溢價 (約 +0.03%) 與追蹤誤差相關資訊, 由於 fund-flow、持倉權重與 roll yield 皆為 DATA_UNAVAILABLE, 無法完整判斷資金面與展期成本。

## Revenue & profitability
不適用。UUP 不是營運公司, 沒有營收、毛利、營業利潤或淨利。替代指標為基金報酬與追蹤表現:
- 1 年報酬 (fiftyTwoWeekChangePercent): 3.55%
- 年初至今 YTD (ytdReturn): 6.28%
- 3 個月報酬 (trailingThreeMonthReturns): 1.27%
- 3 年年化平均報酬 (threeYearAverageReturn): 3.68%
- 5 年年化平均報酬 (fiveYearAverageReturn): 5.91%
- 自 2007 年上市以來的歷史高低: 最高 30.76 / 最低 20.84 (allTimeHigh / allTimeLow)
- 目前價格距 52 週高點 29.25 約 -1.20%, 距 52 週低點 26.40 約 +9.47%

## Cashflow & balance sheet
不適用於公司財報。基金層面的觀察項:
- 持倉結構 (USD 指數期貨籃子 vs EUR/JPY/GBP/CAD/SEK/CHF): 工具 (info、major_holders、inst_holders) 未回傳持倉權重, 標示 DATA_UNAVAILABLE。若需要, 可參考 ICE US Dollar Index 公開方法論之固定權重 (EUR 約 57.6%, JPY 約 13.6%, GBP 約 11.9%, CAD 約 9.1%, SEK 約 4.2%, CHF 約 3.6%), 但此數字不是本次工具抓取結果, 未在 cache 中驗證, 僅供參考。
- 歐元權重最高, 因此 UUP 的走勢大致反映 EUR/USD 的反向變動。
- balance_sheet、cashflow、quarterly 財報工具皆回傳空陣列 (基金不適用), 不做財務比率計算。
- 殖利率: info.yield 為 3.22%, 但 trailingAnnualDividendRate 為 0, 兩者互相矛盾, 疑為 Yahoo 欄位口徑差異 (可能含 T-bill 利息收入), 未確認為實際配息, 標示為待確認。

## Capital allocation & insider signal
- 資金流 (creations/redemptions): DATA_UNAVAILABLE。cache 內無 shares outstanding 與申購贖回資料, 無法判斷淨流入或流出。
- 日成交量: 1,793,819 股 (volume); 10 日平均 1,527,440 股; 3 個月平均 1,666,735 股。近期量能與 3 個月平均相近, 無明顯放大或萎縮。
- 內部人交易: 不適用 (ETF 無內部人)。info.companyOfficers 與 executiveTeam 皆為空。
- 機構持股 (inst_holders) 與大股東 (major_holders) 皆回傳空陣列, 標示 DATA_UNAVAILABLE。

## Valuation
公司估值倍數 (P/E、EV/EBITDA、P/FCF、P/S) 皆不適用。基金估值框架:
- 最新價格 regularMarketPrice: 28.90 USD (前收 28.92)
- NAV (navPrice): 28.89 USD
- 溢價/折價: 約 +0.03% (28.90 vs 28.89), 幾乎等於 NAV, 無顯著溢價或折價。注意 NAV 與價格可能非同一時點, 盤前 (marketState PRE) 報價需謹慎解讀。
- 買賣價差: bid 28.93 / ask 28.99, 價差約 0.21%。
- 費用率 (netExpenseRatio): 0.75%, 為年化持有成本。
- Roll yield / 期貨展期收益: DATA_UNAVAILABLE。cache 無近月與次月期貨價格, 無法計算期貨曲線斜率或展期成本。
- beta3Year 回報為 -11.39, 數值明顯異常 (與 DXY 相關的基金 beta 通常接近 0 或為小數值), 不採信, 不用於風險計算。

### 技術面補充 (ta snapshot, as_of 2026-10-22)
- 價格 28.90、MA20 28.93、MA50 28.47、MA200 27.87
- RSI(14) 55.27 (中性偏多)
- MACD 0.131, 訊號線 0.169, 柱狀 -0.038 (短線動能轉弱)
- 布林通道 %B 0.45 (位於中軌與上軌之間)
- ATR(14) 0.121, 約為價格的 0.42%
- 20 日年化波動 5.16% (低波動, 符合貨幣類指數特性)
- 支撐 (levels.support): 28.22 (2026-07-15)、27.92 (2026-09-09)、27.87 (2026-08-20)
- 壓力 (levels.resistance): 28.56 (2026-06-24)、28.60 (2026-07-27/28), 目前價格已高於這些價位, 屬於已突破的前高, 轉為潛在支撐區

## Key catalysts
- 資料限制: 無公司財報日曆, earnings_dates 不適用。
- 宏觀事件: 美元走勢主要受 Fed 利率路徑、美國與歐元區、日本、英國等央行政策, 以及美國通膨與就業數據驅動。本報告未抓取具體日期的 FOMC 或數據公布時程, 標示為 DATA_UNAVAILABLE, 由 macro 研究員補充。
- 基金結構性事件: 無 corporate actions (corporateActions 為空)。
- 價格位置: 接近 52 週高點 (-1.2%) 與 20 日均線, 近期突破 28.56 至 28.60 壓力區後站穩, 技術上屬於中期偏多結構。

## Metrics table
單位: 價格為 USD; 淨資產為 USD M; 其餘為百分比或倍數。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 最新價格 (USD) | 28.90 | 1Y +3.55% (52w change) | n/a (不適用) | 中性偏多 |
| NAV (USD) | 28.89 | n/a | n/a | 溢價約 +0.03%, 接近 NAV |
| 淨資產 AUM (USD M) | 431.1 | n/a (歷史趨勢 DATA_UNAVAILABLE) | n/a | 規模偏小, 流動性需留意 |
| 費用率 netExpenseRatio | 0.75% | n/a | n/a | 中等偏高, 屬持有成本 |
| 年初至今 YTD | +6.28% | n/a | n/a | 表現強 |
| 3M 報酬 | +1.27% | n/a | n/a | 中性 |
| 3Y 年化平均 | +3.68% | n/a | n/a | 中性 |
| 5Y 年化平均 | +5.91% | n/a | n/a | 中性偏多 |
| 52 週區間 (USD) | 26.40 - 29.25 | n/a | n/a | 位於區間上半部 |
| 買賣價差 | 約 0.21% | n/a | n/a | 流動性尚可 |
| 日均量 3M (股) | 1,666,735 | 10 日均 1,527,440 | n/a | 量能穩定 |
| RSI(14) | 55.27 | n/a | n/a | 中性 |
| MACD 柱狀 | -0.038 | n/a | n/a | 短線轉弱 |
| 20 日年化波動 | 5.16% | n/a | n/a | 低波動 |
| ATR(14) | 0.121 (約 0.42%) | n/a | n/a | 正常 |
| 殖利率 info.yield | 3.22% (待確認) | n/a | n/a | 與 trailingDividend 0 矛盾, 待確認 |
| 持倉權重 (6 種貨幣) | DATA_UNAVAILABLE | n/a | n/a | 無法驗證 |
| 資金流 creations/redemptions | DATA_UNAVAILABLE | n/a | n/a | 無法判斷 |
| Roll yield | DATA_UNAVAILABLE | n/a | n/a | 無法計算 |
| beta3Year | -11.39 (異常) | n/a | n/a | 不採信 |
| P/E, EV/EBITDA, P/FCF, P/S | n/a (不適用) | n/a | n/a | 不適用於基金 |

## Red flags
- 資料為 cache, 價格時間戳 2026-10-21, TA 為 2026-10-22, 落後報告日, 盤前報價 (marketState PRE) 需以當日收盤為準。
- 持倉權重、資金流、roll yield、機構持股皆為 DATA_UNAVAILABLE, 資金面與期貨結構無法完整驗證。
- beta3Year -11.39 數值異常, 疑為資料錯誤。
- 殖利率 3.22% 與 trailingAnnualDividendRate 0 互相矛盾, 未確認配息。
- 淨資產約 $431.1M 規模不大, 若遇市場波動可能影響流動性與價差。
- 費用率 0.75% 加上期貨展期成本, 長期持有的實際拖累需以 roll yield 數據確認, 目前缺乏。
- 技術面短線 MACD 柱狀轉負, 價格接近 MA20, 短期動能不強。

FUNDAMENTALS REPORT COMPLETE
