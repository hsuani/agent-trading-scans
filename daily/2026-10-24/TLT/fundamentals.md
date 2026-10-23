# Fundamentals — TLT as of 2026-10-24

資料基準: 報價與 NAV 取自 cache (`source: cache`, cached_at 2026-10-23 11:31 UTC); 技術指標 `as_of` 2026-10-22。無 2026-10-24 之後的資料。TLT 為 ETF 而非營運公司, 本報告以基金結構、規模、費用、殖利率與估值框架 (NAV / 折溢價) 為主。

## Executive summary
TLT 為 iShares 20+ Year Treasury Bond ETF (指數: 剩餘到期>20年之美國公債), 淨資產 $46.23B, 費用率 0.15%, 最新價 81.74 (前收 80.24, +1.87%), 年初至今 -7.998%, 距 52 週高點 92.18 下跌 11.3%。市價與 NAV (81.7063) 幾乎持平 (溢價約 +0.04%), 追蹤殖利率 (trailing) 約 2.68%, 價格位於 52 週區間下半部 (距低點 76.43 約 +6.9%)。持倉明細、存續期間、SEC yield、資金流等核心欄位在可用資料中皆為 DATA_UNAVAILABLE, 結構性分析完整度有限; 以上僅為基本面與估值描述, 不構成交易建議。

## Revenue & profitability (基金規模與報酬)
不適用營收/獲利率框架。可用數據:
- 淨資產 (netAssets): $46.23B (totalAssets 46,233,321,472 USD, 與 netAssets 一致)
- 年度報酬: ytdReturn -7.998%; trailingThreeMonthReturns -8.846%; 52 週價格變動 fiftyTwoWeekChangePercent -10.598%
- 3Y 平均報酬 (threeYearAverageReturn) 原始值 0.0307814、5Y 平均報酬 (fiveYearAverageReturn) 原始值 -0.0761063; 欄位單位未確認, 僅列原值供參考
- 3Y beta (beta3Year): 2.31 (Yahoo 欄位原值, 基準定義未確認)
- 歷史 AUM 趨勢: DATA_UNAVAILABLE (cache 僅有單一時點淨資產, 無歷史序列)

## Cashflow & balance sheet (持倉結構與存續期間)
- 指數定義: 剩餘到期 > 20 年、面額 ≥ $300M 之美國公債, 排除 Fed 持有部分; 基金至少 80% 資產投資於指數成分, 至少 90% 資產投資於美國公債 (來源: longBusinessSummary)
- 持倉集中度 / 前十大持倉: DATA_UNAVAILABLE (無持倉資料)
- 平均到期日 (average maturity): DATA_UNAVAILABLE
- 有效存續期間 (effective duration): DATA_UNAVAILABLE; 依指數定義屬長天期端, 利率敏感度顯著高於短債 ETF, 但未有可引用之數值
- 現金/衍生性部位: DATA_UNAVAILABLE
- 成分信用風險: 美國公債為政府債, 信用風險欄位不適用; 主要風險為利率與存續期間風險

## Capital allocation & insider signal (分配、資金流與持有人)
- 費用率 (netExpenseRatio): 0.15%
- 分配 (trailing 12M): trailingAnnualDividendRate 2.152 (每股), 約 2.68% 殖利率 (trailingAnnualDividendYield 0.02682); 以 2.152 / 81.74 換算約 2.63%, 兩者差異源於計算基準。
- SEC yield: DATA_UNAVAILABLE (info 之 `yield` 欄位值 0.05 單位不明, 未採用; `dividendYield` 5.0 亦未採用)
- 最近分配日 (dividendDate) 欄位為 2017 年時間戳, 屬過期欄位, 不採用
- 資金流 (net creations/redemptions): DATA_UNAVAILABLE
- 內部人交易 (insider): 不適用 (ETF 無內部人交易揭露); 機構持有人清單 (inst_holders) 與 major_holders 本次回傳為空, 視為 DATA_UNAVAILABLE
- 流動性: 近 10 日平均成交量 41.29M 股, 3 個月平均 39.09M 股; 當日成交量 65.59M 股; 流動性充足

## Valuation (NAV、折溢價、殖利率與技術位置)
- 市價 vs NAV: 81.74 vs 81.7063, 溢價約 +0.04% (注意 NAV 為 cache 時點, 市價為盤前/最新報價混合, 僅供參考)
- 買賣報價: bid 82.92 / ask 82.97, 與最新價 81.74 不一致, 屬盤前或快取時點差異, 不作為估值依據
- P/E、Forward P/E、EV/EBITDA、P/FCF、P/S: 不適用 (ETF 無獲利與現金流歸屬); info 之 epsTrailingTwelveMonths -12.586、forwardPE -4087.0 為無意義數值, 不採用
- P/B: priceToBook 0.549 與 bookValue 148.865 與 NAV 81.71 矛盾, 不採用
- 歷史殖利率區間 (yield vs historical range): DATA_UNAVAILABLE
- 價格區間: 52W 76.43–92.18; 歷史高點 (allTimeHigh) 179.7、歷史低點 (allTimeLow) 76.43 (與 2026-10-07 支撐位一致)
- 技術位 (ta snapshot, as_of 2026-10-22): MA20 78.67 / MA50 80.58 / MA200 84.81; 價格高於 MA20 (+3.9%) 與 MA50 (+1.4%), 低於 MA200 (-3.6%); RSI14 66.47; MACD 0.018、Signal -0.477、Histogram +0.495; BB %B 1.107 (站上上軌 81.20); ATR14 0.868; 20 日年化波動 11.2%
- 動能: 1M +1.59%, 3M -1.81%, 6M -5.56%, 12M -11.15%

## Key catalysts
- 利率相關事件 (非本基金內建, 需外部追蹤): 美國公債殖利率走勢、Fed 政策路徑與公債發行/再融資規模, 直接影響長天期公債價格
- 基金層面: 無財報、無法說會、無盈餘公告; 無 DATA_UNAVAILABLE 以外之公司級催化劑資料
- 技術層面: 價格位於 MA20 之上、BB 上軌之外, RSI 偏高 (66.5), 短期動能偏熱; 上方參考 MA50 80.58 之下方與 MA200 84.81 之上方
- 前期關鍵價位: 支撐 81.17 (2026-08-18)、76.43 (2026-10-07); 壓力 83.60 (2026-08-28)、87.79 (2026-06-25) — 來源為 ta levels

## Metrics table
單位: 價格與 NAV 為 USD/股; 淨資產為 USD B; 殖利率與報酬為 %; 其餘為原值。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 最新價 (USD/股) | 81.74 | 52W 變動 -10.60% | n/a | 位於 52W 區間下半部 |
| NAV (USD/股) | 81.7063 | n/a | n/a | 與市價幾乎持平 |
| 市價 vs NAV 折溢價 | +0.04% | n/a | 0% 附近 (estimate) | 合理 |
| 淨資產 (USD B) | 46.23 | DATA_UNAVAILABLE | n/a | 大型流動性 ETF |
| 費用率 (%) | 0.15 | n/a | 0.03–0.20 (estimate) | 費用率低於一般主動型 |
| 追蹤殖利率 trailing (%) | 2.68 | DATA_UNAVAILABLE | n/a | 收益水準中等 |
| SEC yield (%) | DATA_UNAVAILABLE | n/a | n/a | 無法判斷 |
| 有效存續期間 (年) | DATA_UNAVAILABLE | n/a | n/a | 無法判斷 |
| 平均到期日 (年) | DATA_UNAVAILABLE | n/a | n/a | 無法判斷 |
| 前十大持倉集中度 | DATA_UNAVAILABLE | n/a | n/a | 不適用 (公債指數) |
| 資金流 (net creations/redemptions) | DATA_UNAVAILABLE | n/a | n/a | 無法判斷 |
| YTD 報酬 (%) | -7.998 | n/a | n/a | 弱勢 |
| 3M 報酬 (%) | -8.846 | n/a | n/a | 弱勢 |
| 3Y beta | 2.31 | n/a | n/a | 利率敏感度高 (原值) |
| 52W 高點 / 低點 | 92.18 / 76.43 | n/a | n/a | 距低點 +6.9%, 距高點 -11.3% |
| 近 10 日平均成交量 (M 股) | 41.29 | 3M 均量 39.09 | n/a | 流動性充足 |
| RSI14 | 66.47 | n/a | n/a | 偏熱 |
| MACD histogram | +0.495 | n/a | n/a | 短期動能轉正 |
| ATR14 (USD) | 0.868 | n/a | n/a | 日波動約 1.1% |
| 20 日年化波動 (%) | 11.23 | n/a | n/a | 中等 |

## Red flags
- 核心欄位大量缺失: 持倉、存續期間、平均到期日、SEC yield、資金流、歷史 AUM 皆為 DATA_UNAVAILABLE, 無法完成利率風險的量化評估
- 股份數與淨資產不一致: info 之 sharesOutstanding 109.7M 乘以 NAV 81.71 僅約 $8.96B, 與 netAssets $46.23B 不符 (隱含股數約 566M); 本報告採用 netAssets 為規模依據, 股份數不採用
- bookValue 148.865 與 NAV 81.71 不一致, priceToBook 0.549 不採用
- 報價時點混合: 最新價 81.74、bid 82.92 / ask 82.97、盤前欄位與 fulldayPrice 81.53 並存, 估值與折溢價以 NAV 81.7063 為基準, 精度有限
- 技術指標 as_of 為 2026-10-22, 與價格 cache 2026-10-23 存在一日落差
- 利率風險高: 長天期公債對殖利率變動敏感, 3Y beta 2.31 (原值), 近 12 個月報酬 -11.15%, 價格仍低於 MA200 (-3.6%)
- 所有 Yahoo 財報與持有人端點 (financials、quarterly 系列、major_holders、inst_holders、earnings_dates) 於本次取得空值或失敗, 不適用於基金但意味資料源不完整

FUNDAMENTALS REPORT COMPLETE
