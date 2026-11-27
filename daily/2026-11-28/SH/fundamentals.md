# Fundamentals — SH as of 2026-11-28

## Executive summary
SH 為 ProShares Short S&P500（-1x 反向 ETF），不是公司，本報告以基金結構、規模、費用、淨值折溢價與價格資料代替營收與獲利分析。截至 2026-11-27 收盤，股價約 34.11 美元（yfinance info 紀錄），淨值（NAV）34.5705 美元，折價約 1.33%；基金淨資產約 9.50 億美元（USD 0.95B），淨費用率 0.88%，財務報表與持股/Swap 組成、資金流向等資料本次工具無法取得（DATA_UNAVAILABLE）。以基金本身而言結構健全（規模約 USD 0.95B、流動性充足），但反向型商品的每日重置與波動耗損會使長期持有報酬與指數反向報酬出現偏離，3 年平均年化報酬為 -10.19%，屬於對沖/戰術工具而非價值型持有標的。

## 資料可得性與時間說明
- 資料來源：pipeline/tools/yf 與 pipeline/tools/ta，多數 Yahoo 端點因 CONNECT 403 失敗，本次 info 與 ta 資料皆來自 repo cache（cached_at 2026-11-27 16:36 UTC 附近）。
- 本次分析 as-of 2026-11-28，所用最新行情為 2026-11-27 收盤附近，未見晚於 2026-11-28 的資料。
- 三個來源的現價不一致：yf info regularMarketPrice 34.1101、yf fast_info last_price 34.205（cnyes feed）、ta snapshot price 34.15（as_of 2026-11-27）。本報告以 info 之 regularMarketPrice 為主，價差約 0.1 美元（約 0.3%），不影響結論。
- financials、balance_sheet、cashflow、quarterly 系列、earnings_dates、insider、major_holders、inst_holders 均回傳空值或錯誤，列為 DATA_UNAVAILABLE。

## Revenue & profitability（ETF 結構與績效替代）
- 基金類型：Exchange Traded Fund，類別 Trading--Inverse Equity，發行商 ProShares，交易所 NYSEArca。
- 投資目標摘要（info.longBusinessSummary）：以金融工具達成相對標的指數每日報酬的 -1x 反向曝險；至少 80% 總資產為指數成分或具相似經濟特性之工具曝險（即 Swap 與期貨等衍生性工具，實際持股/Swap 對手方組成 DATA_UNAVAILABLE）。非分散型基金（non-diversified）。
- 規模：totalAssets 與 netAssets 皆為 950,363,712 美元（USD 0.95B）。由 NAV 反推之流通股數約 2,749 萬股（派生估算，非基金公告數字）。
- 績效（info 欄位）：
  - YTD 報酬 -6.63%
  - 近 3 個月 NAV 報酬 -1.10%
  - 3 年平均年化報酬 -10.19%
  - 5 年平均年化報酬 -5.79%
  - 3 年 beta -0.92（對標的指數之反向關係）
- 52 週區間：31.64 至 39.20 美元，現價距 52 週低點 +7.8%、距高點 -13.0%。
- 歷史最高/最低（allTimeHigh 843.52、allTimeLow 31.64）：843.52 明顯與目前價位不連續，疑為歷史拆分/調整前價格資料異常，本報告不採用。
- AUM 趨勢：僅有單一時點規模，無歷史 AUM 序列，AUM 趨勢為 DATA_UNAVAILABLE。

## Cashflow & balance sheet（基金資產負債與費用）
- 財報（現金流量/資產負債）為 DATA_UNAVAILABLE，因 ETF 不適用公司層級財報；以基金層級指標替代。
- 淨費用率（netExpenseRatio）0.88%。依淨資產 USD 0.95B 推算，年化費用約 USD 8.4M（派生估算）。
- 基金若以衍生性工具達成曝險，報告中之現金與短期國債抵押品、Swap 交易對手風險等均無法由工具取得，列 DATA_UNAVAILABLE。
- 槓桿與重置：-1x 每日重置，持有期間的報酬會受路徑影響（波動耗損）。在高波動、來回震盪的盤勢中，即使指數中期方向正確，基金報酬仍可能偏離 -1x 的累積結果。近 20 日年化波動率 31.8%（ta vol_20d_annualized），該值亦為觀察波動耗損風險的依據之一。

## Capital allocation & insider signal（分配、資金流與內部人替代）
- 股利/分配：info 之 dividendYield 與 yield 皆為 3.87%。反向基金通常無穩定配息，此數字可能反映近期或前期的收益分配（distribution）而非年化股息，本報告不將其視為穩定收益來源，且無分配明細可核對，標記為待驗證。
- 內部人交易：insider 回傳空值，ETF 無內部人交易概念，此項不適用。
- 機構持股：inst_holders 與 major_holders 回傳空值，為 DATA_UNAVAILABLE。
- 資金流（creation/redemption、淨申購贖回）：DATA_UNAVAILABLE。
- 成交量訊號：
  - 當日成交量 4,246,099 股
  - 3 個月平均成交量 10,424,033 股（當日約為其 40.7%）
  - 10 日平均成交量 13,837,640 股（當日約為其 30.7%）
  - 近 10 日量能高於 3 個月均量，但當日量偏低，顯示近期交易熱度先升後降。

## Valuation（淨值折溢價與技術位置替代）
- P/E、EV/EBITDA、P/FCF、P/S 均不適用於 ETF，列 n/a（ETF 不適用）。
- NAV 折溢價：市價 34.1101 對 NAV 34.5705，折價約 -1.33%（派生）。以 bid 34.18 / ask 34.19 中價 34.185 計算，折價約 -1.11%。NAV 為前一交易日計算值，盤中折溢價會隨標的指數變動，此為參考數字。
- 技術位置（ta snapshot，as_of 2026-11-27）：
  - 價格 34.15 高於 MA20（33.635，+1.53%）、MA50（32.758，+4.25%）與 MA200（33.886，+0.78%）。
  - RSI14 55.52，中性偏多；MACD 0.5423 高於 Signal 0.4727，柱狀體 +0.0696。
  - 布林 %B 0.646（中軌 33.635，上軌 35.395，下軌 31.875）。
  - ATR14 0.692（約股價 2.0%）。
  - 動能：1 個月 +6.29%、3 個月 +5.63%、6 個月 +3.86%、12 個月 -7.10%。
- 支撐/壓力（ta levels）：
  - 支撐：31.64（2026-10-06，同時為 52 週低點）、31.83（2026-08-13）、32.70（2026-07-10）
  - 壓力：33.27（2026-09-16）、33.96（2026-07-29）
- 方向提醒：SH 上漲代表 S&P 500 下跌，近 1 個月 SH 上漲、近 12 個月下跌，表示近期指數偏弱、長期指數偏強。此解讀僅為描述市場方向，不構成交易建議。
- 同類中位數：inverse equity 類別之同類中位數無可靠來源，列 n/a。

## Key catalysts
- 下一次財報/分配公告：earnings_dates 失敗，ETF 無財報；分配日期 DATA_UNAVAILABLE。
- 基金層級催化劑：
  - 標的指數（S&P 500）之波動與方向，為 SH 價格的主要驅動。
  - 基金規模、費用、折溢價之變化（需下次取得 AUM 與 NAV 序列）。
  - 基金經理人公告之收益分配（distribution）時程，DATA_UNAVAILABLE。
- 技術面關注位置：31.64 為 52 週低點與關鍵支撐，33.27 與 33.96 為近期壓力；價格位於 MA20 與 MA200 之上，其相對位置隨盤勢變化。

## Metrics table
單位：USD 以 B/M 標示；無 TWD/KRW 數字，故無億換算。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 基金淨資產 Net assets (USD B) | 0.95（950.36M） | DATA_UNAVAILABLE | n/a | 規模足夠，流動性中等偏上 |
| 淨費用率 Net expense ratio | 0.88% | DATA_UNAVAILABLE | n/a | 反向槓桿型商品費用屬正常區間，持有成本偏高 |
| 市價 Market price (USD) | 34.1101 | n/a | n/a | 2026-11-27 收盤附近 |
| NAV (USD) | 34.5705 | n/a | n/a | 前一交易日計算值 |
| 折溢價 Premium/discount to NAV | -1.33%（派生） | n/a | n/a | 小幅折價，屬可接受區間 |
| YTD 報酬 | -6.63% | n/a | n/a | 年內表現偏弱 |
| 3 個月 NAV 報酬 | -1.10% | n/a | n/a | 近季小幅下跌 |
| 3 年平均年化報酬 | -10.19% | n/a | n/a | 長期持有反向 ETF 之耗損明顯 |
| 5 年平均年化報酬 | -5.79% | n/a | n/a | 同上 |
| 3 年 beta | -0.92 | n/a | n/a | 與標的指數呈強反向關係 |
| 殖利率 Dividend yield | 3.87%（待驗證） | DATA_UNAVAILABLE | n/a | 收益分配性質不明，不視為穩定收益 |
| 52 週距高點 / 距低點 | -13.0% / +7.8% | n/a | n/a | 位於區間中段偏低 |
| 當日成交量 / 3M 均量 | 40.7% | n/a | n/a | 當日量縮 |
| 10 日均量 / 3M 均量 | 132.7% | n/a | n/a | 近期量能偏高 |
| RSI14 | 55.52 | n/a | n/a | 中性 |
| MACD 柱狀體 | +0.0696 | n/a | n/a | 短線偏多（對 SH 而言代表標的偏弱） |
| BB %B | 0.646 | n/a | n/a | 中上位置 |
| 20 日年化波動率 | 31.8% | n/a | n/a | 波動偏高，重置耗損風險提高 |
| 價格 vs MA200 | +0.78% | n/a | n/a | 站上長期均線，幅度小 |
| 內部人交易 | n/a（ETF 不適用） | n/a | n/a | 不適用 |
| 資金流 Fund flows | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | 無法評估 |
| 持股/Swap 組成 Holdings | DATA_UNAVAILABLE | n/a | n/a | 無法評估 |
| P/E、EV/EBITDA、P/FCF、P/S | n/a（ETF 不適用） | n/a | n/a | 不適用 |

## Red flags
- 財務與持股資料缺失：financials、holdings/Swap 組成、資金流、AUM 歷史皆 DATA_UNAVAILABLE，無法驗證基金實際曝險與交易對手風險。
- 報價來源不一致：info、fast_info、ta 三者現價差約 0.1 美元，且均來自 cache，非即時來源。
- 殖利率 3.87% 性質不明，不應視為穩定收益。
- allTimeHigh 843.52 與現價不連續，疑為歷史資料調整問題，不採用。
- 3 年平均年化報酬 -10.19%：長期持有反向 ETF 之波動耗損與費用拖累明顯，不適合作為長期持有工具，需由交易端自行判斷持有期間。
- 近 20 日年化波動率 31.8%，每日重置之路徑依賴性提高。
- 當日成交量僅為 3 個月均量的約 41%，流動性短期內偏弱，需留意盤中成交與價差。

FUNDAMENTALS REPORT COMPLETE
