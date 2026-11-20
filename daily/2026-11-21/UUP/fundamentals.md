# Fundamentals — UUP as of 2026-11-21

資料說明：UUP 為 ETF（Invesco DB US Dollar Index Bullish Fund），不是營運公司，故不適用營收、毛利、資產負債表、EPS、內部人交易等公司財務框架。本報告改以基金結構、費用率、規模、價格與淨值關係、技術面與持有人資料呈現。Yahoo 即時端點在本環境被代理拒絕（403 / cookie-crumb 失敗），因此大部分數據來自 `source: cache`（cached_at 2026-11-20），屬正常的快取回退，不是錯誤。所有資料最新日期為 2026-11-20，未觀察到晚於 2026-11-21 的資料。

## Executive summary
UUP 是追蹤 ICE 美元指數（DX）多頭期貨部位的 ETF，費用率（netExpenseRatio）為 0.75%，快取淨資產約 481.4M USD，規模偏小，且持有人與資金流向資料全部無法取得。價格 29.60 相對 NAV 29.65 小幅折價 0.17%，價格位於 50 日與 200 日均線之上，RSI(14) 為 69.8 接近超買區，屬短線偏強但未過熱的狀態。以基本面角度，本標的沒有估值意義（無 P/E、無 EV/EBITDA），應把它視為美元方向的總體曝險工具，評估重點在美元走勢與資金流，而非公司財務。

## 基金結構與費用
- 基金性質：商品池（commodity pool）型 ETF，透過 DX 期貨多頭與短期國庫券擔保，追蹤美元指數的多頭報酬。來源：`info.longBusinessSummary`「invests in futures contracts ... long positions in DX Contracts」。
- 指數成分（靜態知識，非本次工具回傳）：ICE 美元指數以歐元、日圓、英鎊、加幣、瑞典克朗、瑞士法郎六種貨幣組成，其中歐元權重最高（約 57-58%）。本次工具未回傳即時持倉權重，故此項為背景說明，實際持倉請以基金公告為準。
- 費用率：netExpenseRatio = 0.75%（來源 info）。
- 基金公司：Invesco；基金成立日 fundInceptionDate 對應 2007 年（1171929600 秒）。
- 交易所：NYSE Arca（PCX），幣別 USD。

## 持有人、持倉與資金流（資料缺口）
- 持倉組成（DX 期貨部位明細、現金/國庫券比重）：DATA_UNAVAILABLE（`info` 未提供，且 holdings 相關端點不可用）。
- 機構持有人（inst_holders）：回傳空陣列 `[]`，視為 DATA_UNAVAILABLE。
- 主要持有人（major_holders）：回傳空陣列 `[]`，DATA_UNAVAILABLE。
- AUM 歷史趨勢（月度或季度）：DATA_UNAVAILABLE。僅有單點快取 totalAssets = 481,364,192 USD（約 481.4M USD），無法判斷趨勢方向。
- 資金流（淨申購/贖回）：DATA_UNAVAILABLE。
- 內部人交易：不適用於 ETF，insider 端點回傳空陣列。

## 價格與淨值
- 最新價：29.60 USD（2026-11-20，快取 regularMarketPrice）；前收 29.63；當日 -0.10%。
- 淨值 NAV：29.65 USD，價格相對淨值折價 -0.17%（計算值）。
- 52 週區間：26.40 - 29.67（info）；快取日收盤計算 26.47 - 29.63。價格距 52 週高點 -0.24%，距低點 +12.1%。
- 歷史極值：allTimeHigh 30.76、allTimeLow 20.84（info）。
- 日內量能：當日 volume 297,257（盤中快照，非完整交易日），10 日平均量 1,544,840，3 月平均量 1,600,135，流動性充足。
- 報酬（由 `prices/UUP.csv` 日收盤計算）：
  - 1 個月 +2.42%（2026-10-22 起算）
  - 3 個月 +5.87%
  - 6 個月 +6.59%
  - 1 年 +4.26%
  - 2 年 -1.56%（2024-11-20 收盤 30.07）
  - info 的 ytdReturn = 7.13%，fiftyTwoWeekChangePercent = 4.37%，與上述方向一致。
- 月底收盤趨勢：2026 年 1 月低點約 26.85，之後逐月上升，2026-10 為 29.00，2026-11 至今 29.60。

## 技術面（ta snapshot，as_of 2026-11-20）
- 價格 29.60 高於 MA20（29.22，+1.28%）、MA50（28.96，+2.22%）、MA200（28.10，+5.35%）。
- MACD 0.198，訊號線 0.159，柱狀體 +0.039，動能仍為正向。
- RSI(14) 69.8，接近超買門檻（70）。
- 布林 %B 0.85，靠近上軌 29.76。
- ATR(14) 0.115，約為價格 0.39%；20 日年化波動 5.3%。
- 由快取日收盤計算之全期年化波動約 7.8%，近 60 日約 5.0%，屬低波動期。

## 風險與注意事項（對 UUP 的特殊性）
- 期貨展期（roll）成本與期貨曲線結構會影響實際報酬，與現貨美元指數會有偏差。本次無展期成本數據，DATA_UNAVAILABLE。
- beta3Year 回傳 -7.93，數值明顯不合理（美元 ETF 的 beta 不會接近 -8），判定為資料錯誤，不採用。
- 股息欄位互相矛盾：trailingAnnualDividendYield = 0.0，但 dividendYield = 3.2（百分比形式）、yield = 0.032。無法確認近期配息，標記為資料不一致。
- 快取的 fast_info 與 info 的 52 週高點略有差異（29.63 收盤 vs 29.67 盤中），本報告兩者並列，以盤中數據為準。

## 催化因子
- 公司財報：不適用。
- 總體事件：美元方向主要受 Fed 利率路徑、美國 CPI/就業數據與主要貨幣（EUR、JPY）政策影響。本次未取得可驗證的事件日曆，DATA_UNAVAILABLE（不列具體日期）。
- 基金層面：費用率、規模與資金流變化會影響長期持有成本與流動性，但目前無歷史數據可判斷趨勢。

## Metrics table
單位：價格為 USD，規模為 USD M（百萬美元）。ETF 無營收與獲利數據，相關欄位標記為 n/a 或 DATA_UNAVAILABLE。本表不使用億元單位。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 最新價 (USD) | 29.60 | 1Y +4.26% | n/a | 偏強，距 52 週高點 -0.24% |
| 淨值 NAV (USD) | 29.65 | n/a | n/a | 價格相對 NAV 折價 -0.17%，無異常 |
| 基金規模 totalAssets (USD M) | 481.4 | DATA_UNAVAILABLE | n/a | 規模偏小，流動性需留意 |
| 費用率 netExpenseRatio | 0.75% | n/a | n/a | 中等偏高，持有成本需考慮 |
| 殖利率 (dividendYield 欄) | 3.2%（與 trailingAnnualDividendYield 0% 矛盾） | n/a | n/a | 資料不一致，不採信 |
| 1 個月報酬 | +2.42% | n/a | n/a | 短期上行 |
| 3 個月報酬 | +5.87% | n/a | n/a | 中期偏強 |
| 6 個月報酬 | +6.59% | n/a | n/a | 中期偏強 |
| 2 年報酬 | -1.56% | n/a | n/a | 長期仍低於 2024 年底水準 |
| RSI(14) | 69.8 | n/a | n/a | 接近超買，需留意 |
| MACD 柱狀體 | +0.039 | n/a | n/a | 動能正向 |
| 布林 %B | 0.85 | n/a | n/a | 靠近上軌 |
| 20 日年化波動 | 5.3% | n/a | n/a | 低波動 |
| 日均成交量 (10 日) | 1,544,840 股 | 3 月均量 1,600,135 | n/a | 流動性充足 |
| 持倉組成 | DATA_UNAVAILABLE | n/a | n/a | 無法驗證 |
| 資金流 (淨申購) | DATA_UNAVAILABLE | n/a | n/a | 無法判斷 |
| 機構/主要持有人 | DATA_UNAVAILABLE | n/a | n/a | 無法判斷 |
| 內部人交易 | n/a（ETF 不適用） | n/a | n/a | 不適用 |
| 營收 / 毛利 / 淨利 / ROE | n/a（ETF 不適用） | n/a | n/a | 不適用 |
| P/E / EV/EBITDA / P/FCF | n/a（ETF 不適用） | n/a | n/a | 不適用 |
| 下次財報日 | n/a（ETF 不適用） | n/a | n/a | 不適用 |

## Red flags
- 規模僅約 481.4M USD，且無 AUM 趨勢與資金流資料，無法確認基金是否正在流失資產。
- 持倉與展期成本 DATA_UNAVAILABLE，無法驗證期貨部位與實際追蹤誤差。
- 費用率 0.75% 加上期貨展期成本，長期持有可能侵蝕報酬，需納入評估。
- beta3Year (-7.93) 與股息欄位互相矛盾，屬資料品質問題，已排除使用。
- RSI 69.8 接近超買，價格在布林上軌附近，短線追價風險上升。
- 本次即時 Yahoo 端點不可用，數據以 2026-11-20 快取為主，與當日收盤可能有落差。

FUNDAMENTALS REPORT COMPLETE
