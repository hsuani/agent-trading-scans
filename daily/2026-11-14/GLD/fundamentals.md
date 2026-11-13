# Fundamentals — GLD (SPDR Gold Shares) as of 2026-11-14

> 資料時點注意: 本報告分析基準日為 2026-11-14, 實際可取得之 yfinance 快取資料時點為 2026-11-13 14:30 UTC (美東 09:30, 開盤時點), 屬於基準日前一天, 無資料晚於基準日。`fast_info` 與 `info` 報價不一致 (354.89 vs 356.27), 以 `info` 的 regularMarketPrice 356.27 為主。

## Executive summary
GLD 為實體黃金現貨信託 (grantor trust), 無營運現金流、無財務報表, 財務健康度不適用; 本報告聚焦持倉性質、費用率、AUM 與價格結構。截至 2026-11-13 價格 356.27 USD, 較 50 日均線 (382.00) 低 6.7%、較 200 日均線 (409.12) 低 12.9%, 年初至今 -9.46%, 距 52 週高點 (509.70, 亦為歷史高點) 回落 30.1%, 且市價相對淨資產值 (NAV 367.82) 折價約 3.1%。基金規模約 1,310 億 USD, 年費用率 0.40%, 本報告無法取得資金流向 (inflow/outflow) 與持倉明細, 相關結論需由其他來源補足。

## Revenue & profitability (不適用 — ETF)
- 收入、毛利、營業利益、淨利率: n/a (信託不營運, 無營收科目)。
- yfinance 回傳 `epsTrailingTwelveMonths` = -9.394 USD, 但此數值為信託會計層面的報告值, 不代表營運獲利能力, 不應與個股 EPS 比較, 僅列為參考。
- ROE / ROIC: n/a。
- 替代指標 (報酬表現, 來自 info): 年初至今 -9.46%; 近 3 個月 -2.91%; 52 週 -5.60%; 3 年平均年化報酬 +26.71%; 5 年平均年化報酬 +15.97%。
- 報告中 `trailingAnnualDividendRate` = 0.0, `yield` = 0.0: 信託不配息, 此欄位對 GLD 無意義。

## Cashflow & balance sheet (不適用 — ETF)
- FCF、FCF/NI、淨負債、流動比率、負債權益比: n/a (`balance_sheet`、`quarterly_bs`、`cashflow` 工具於本次查詢皆回傳 ConnectionError / 403, 且信託本身通常無負債科目)。
- 資產端結構: 信託持有實體金條 (gold bars), 依 `longBusinessSummary` 所述, 目標為反映金價表現扣除費用後之報酬。持倉以黃金單一資產 100% 集中, 無其他資產類別。
- 持倉數量 (盎司) 與保管機構明細: n/a (本次工具不提供)。
- 推估 (僅供參考, 未經驗證): 若每股仍約代表 1/10 盎司黃金 (GLD 歷史慣例), 則 NAV 367.82 隱含金價約 3,680 USD/盎司 (扣除費用前後略有差異), 需以現貨金價核對。

## Capital allocation & insider signal
- 資本支出、回購、股利: n/a (信託不進行資本配置; 不發股利, 不回購)。
- 申購/贖回 (creation/redemption) 與資金流向: yfinance 無此欄位, 本次無法取得 inflow/outflow 數據。`sharesOutstanding` 欄位 (260.3M) 與 AUM/NAV 不一致 (見 Red flags), 無法作為資金流的可靠代理。
- Insider 交易: n/a (ETF 無內部人; `insider` 工具回傳空陣列)。
- 機構持股 (`major_holders`, `inst_holders`): 本次回傳空陣列, 無法評估持有人集中度。
- 規模變化: 目前 `totalAssets` 與 `netAssets` 皆為 131,009,642,496 USD (約 1,310 億 USD, 即 131.0B USD); 歷史 AUM 趨勢本次無時間序列資料, 無法計算 YoY。

## Valuation
- P/E (trailing): n/a (EPS 為會計數值, 本身為負, 不具估值意義)。Forward P/E: n/a。
- EV/EBITDA、P/FCF、P/S: n/a (信託無 EBITDA、FCF、營收)。
- P/B: yfinance 回傳 2.10x, 但 bookValue (170.017) 與 NAV (367.82) 明顯不一致, 此比值不可採信, 不列為估值依據。
- 相對 NAV 溢折價: 市價 356.27 / NAV 367.82 - 1 = **-3.14% (折價)**。此為本次最具參考價值的估值指標; 但 NAV 為前一日結算或快取值, 盤中折價可能與收盤不同。
- 價格位置:
  - 52 週區間 352.91 – 509.70, 現價位於區間底部附近 (距低點 +0.95%, 距高點 -30.1%)。
  - 現價 < 50 日均線 (382.00) < 200 日均線 (409.12), 呈空頭排列。
  - 52 週低點 352.91 距現價僅約 3.36 USD, 為近期關鍵支撐觀察點 (僅為事實描述, 非交易建議)。
- 費用率 0.40%: 以 AUM 1,310 億 USD 計, 每年成本約 5.24 億 USD (0.40% × 131.0B USD)。
- 與同類比較: 黃金現貨 ETF 之費用率通常低於 GLD (估計區間 0.10%–0.25%, 未由工具驗證), 故 GLD 費用率在同類中偏高。

## Key catalysts
- 下次財報: n/a (信託無財報; `earnings_dates` 回傳連線錯誤)。
- 金價驅動因素 (非工具數據, 僅列為需追蹤事項): 實質利率、美元指數、央行購金、地緣政治避險需求、ETF 申贖資金流。本次工具無法量化這些因子, 需由宏觀與商品研究補充。
- 基金層面事件: 無 corporate actions (`corporateActions` 為空); 無分配 (distribution) 事件。
- Beta (3 年) 0.47: 與股市相關性偏低, 屬避險屬性之數據支持, 但不代表與金價相關性, 金價相關性需另行計算。

## Metrics table
單位: USD 以 B (十億) / M (百萬) 表示; 本報告無 TWD/KRW 金額, 未使用 億。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 價格 (regularMarketPrice, USD) | 356.27 | 52 週變動 -5.60% (以 52 週前價計) | n/a | 位於 52 週底部區 |
| 年初至今報酬 (ytdReturn) | -9.46% | n/a | n/a | 弱勢 |
| 近 3 個月報酬 | -2.91% | n/a | n/a | 弱勢 |
| 50 日均線 / 偏離 | 382.00 / 現價低 6.7% | n/a | n/a | 短線偏弱 |
| 200 日均線 / 偏離 | 409.12 / 現價低 12.9% | n/a | n/a | 中期偏弱 |
| 52 週高點 (= 歷史高點) / 回落幅度 | 509.70 / -30.1% | n/a | n/a | 深度回檔 |
| NAV (navPrice, USD) | 367.82 | n/a | n/a | 參考基準 |
| 市價相對 NAV 溢折價 | -3.14% (折價) | n/a | 通常 ±0.1% 內 (估計) | 折價偏大, 需確認 NAV 時點 |
| 淨資產 (netAssets) | 131.0B USD | 無時間序列, n/a | n/a | 大型基金, 流動性充足 |
| 平均日成交量 (3M) | 9.68M 股 | n/a | n/a | 流動性極佳 |
| 費用率 (netExpenseRatio) | 0.40% | n/a | 0.10%–0.25% (估計) | 同類中偏高 |
| 年化費用金額 | 約 0.52B USD | n/a | n/a | 持有成本 |
| 3 年 Beta | 0.47 | n/a | n/a | 與股市相關性低 |
| 3 年平均年化報酬 | +26.71% | n/a | n/a | 長期表現強 |
| 5 年平均年化報酬 | +15.97% | n/a | n/a | 長期表現強 |
| 股利殖利率 | 0.00% | n/a | 0% (實體金 ETF 慣例) | 不適用 |
| 資金流向 (inflow/outflow) | n/a | n/a | n/a | 工具無資料 |
| 持倉 (盎司) / 持有人集中度 | n/a | n/a | n/a | 工具無資料 |
| EPS (trailing, 會計值) | -9.394 USD | n/a | n/a | 不具估值意義 |
| P/E / P/B | n/a / 2.10x (不可採信) | n/a | n/a | 不適用 |
| 內部人交易 | n/a | n/a | n/a | ETF 不適用 |

## Red flags
- **資金流向完全缺失**: yfinance 無申贖/資金流欄位, 無法判斷近期是否有大規模贖回; 這是評估 GLD 需求面的最大資料缺口。
- **NAV 折價 -3.14%**: 對一檔實體黃金 ETF 而言屬較顯著偏離, 可能反映快取 NAV 時點與即時價差, 或申贖機制受阻; 需以當日收盤 NAV 核實後再下結論。
- **股數與淨資產不一致**: `sharesOutstanding` = 260.3M, 但 netAssets / NAV = 131.0B / 367.82 ≈ 356.2M 股; 若以 260.3M 計算, 隱含 NAV 約 503 USD, 與 navPrice 相差約 37%。`bookValue` (170.017) 亦與 NAV 不符。此為資料源內部不一致, 本報告以 netAssets 與 navPrice 為準, 其餘 shares 相關指標不採用。
- **價格快照不一致**: `info` 顯示 356.27, `fast_info` 顯示 354.89 (cnyes feed); 差異約 0.39%。本次快照位於開盤時點 (成交量僅 550,373 股, 遠低於 10 日均量 9.82M), 日內數據不完整。
- **技術面弱勢**: 價格同時低於 50 日與 200 日均線, 且接近 52 週低點 352.91, 若跌破將失去關鍵支撐 (僅為事實描述)。
- **費用率偏高**: 0.40% 在黃金 ETF 中偏高, 長期持有成本拖累明顯 (以 1,310 億 USD 計每年約 5.24 億 USD)。
- **資料工具失敗**: `fast_info`、`balance_sheet`、`cashflow`、`earnings_dates`、`major_holders`、`inst_holders`、`insider` 多數回傳 403 / ConnectionError 或空陣列, 本報告部分欄位因此為 n/a, 不代表資產無此屬性。

FUNDAMENTALS REPORT COMPLETE
