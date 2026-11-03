# Sentiment — IPGP as of 2026-11-04

> 注意: 執行日為 2026-11-03, 指定的 as-of 日為 2026-11-04。最新 insider 申報日為 2026-10-02, 最新分析師摘要無日期標示, 本報告未包含 11-03 之後的任何資料。

## Analyst consensus

9 位分析師: 6 buy (2 strong buy + 4 buy) / 2 hold / 1 sell (1 strong sell)。
換算比例: Buy 66.7% / Hold 22.2% / Sell 11.1%。
近一個月分布與目前相同 (yfinance `rec_summary` 的 0m 與 -1m 一致), 代表 Yahoo 資料中近一月無評級變動。

| 項目 | 數值 | 來源 / 可信度 |
|---|---|---|
| 目前評級分布 | 6 Buy / 2 Hold / 1 Sell | yfinance rec_summary, 高 |
| 平均目標價 | 約 $137.17 | MarketBeat (2026-08-04 報導), 中 |
| 近期個別調整 | Citigroup PT $150 (報導稱 2026-05-06); Needham 由 Hold 調升 Buy (報導稱 2026-05-06); Zacks 由 strong-buy 降為 hold (報導稱 2026-05) | 網路搜尋摘要, 低, 日期與來源彼此不一致, 需核對 |

yfinance `recommendations` 只回傳彙總分布, 沒有逐筆升降評等紀錄, 因此無法從工具確認個別調整。

## Retail social

- Reddit (r/wallstreetbets, r/stocks): 抓取被封鎖 (WebFetch 無法連線 www.reddit.com), 無資料。
- StockTwits: DNS 解析失敗 (api.stocktwits.com 不在允許網域內), 無資料。需在 session 網路設定允許該網域後才能重試。
- X / 新聞討論: 一般搜尋找不到 2026-10 或 11 月的散戶討論串。能找到的多為股價頁面與聚合站, 其中「討論」區塊是制式內容, 不代表投資人情緒。
- 討論量 (buzz volume): 無法量化, 無樣本可比較。
- 散戶語氣: **無法判定** (資料不足, 不宜據此推論看多或看空)。
- 主題: 無可靠樣本。搜尋結果中反覆出現的敘事為資料中心與 AI 相關需求、工業與醫療/國防應用, 以及「估值是否偏高」的質疑 (Simply Wall St 標題指稱股價高於其估算公允價值), 但這些是媒體敘事, 不是散戶貼文。

## Insider activity

統計窗口: 2026-05-03 至 2026-11-03 (6 個月)。已排除 0 美元的股票獎勵 (grant) 與 derivative 轉換。

| 類別 | 金額 (USD M) | 筆數 | 說明 |
|---|---|---|---|
| 公開市場買入 | 0.20 | 1 | 董事 John R. Peeler (2026-08-26, 約 $72.84–74.57) |
| 公開市場賣出, 合計 | 23.38 | 13 | 見下表 |
| 其中: >10% 股東 (IP Fibre Devices LTD、Gapontsev Trust) | 21.17 | 6 | 依名稱推斷與創辦人 Valentin Gapontsev 相關 |
| 其中: 董事與高管 | 2.21 | 7 | 含 Scherbakov (董事兼 >10% 持有人) 0.55 |
| **淨額** | **約 -23.18** | | 淨賣出 |

主要申報:
- CFO Timothy P. V. Mammen, 2026-05-22, 賣出 $1.20M (約 $119.60–120.37)。
- 大額 >10% 持有人: IP Fibre Devices LTD 於 2026-06-29 賣出 $6.81M (約 $100–106), 2026-08-05 賣出 $2.90M (約 $95–99), 2026-10-02 賣出 $1.32M (約 $85–86)。Gapontsev Trust 於 2026-07-21 賣出 $5.76M (約 $100–103), 2026-09-02 賣出 $2.07M (約 $75–76)。
- 其他董事/高管: Director Agnes Tang 2026-06-22 賣出 $0.18M; Director Jeanmarie F. Desmond 2026-05-14 賣出 $0.18M; General Counsel Angelo P. LoPresti 2026-06-29 賣出 $0.11M。

觀察:
- 窗口內的大額賣出多在 $95–120 區間執行, 近期成交價 (2026-09 至 10) 已降到約 $75–86, 價格區間與賣出時點有明顯落差。
- 大部分賣出來自 >10% 持有人, 而非 CEO 或 CFO 的個人決策。高管中只有 CFO 一筆較大的賣出 (5 月)。
- 唯一公開市場買入為獨立董事 Peeler, 金額小 (約 $0.2M)。
- 2026-05-12 與 2026-02-18 有大批董事與高管股票獎勵, 屬例行薪酬, 不計入淨額。

## Ownership shifts

- 機構持股: 77.3% (yfinance `major_holders`), 機構數 490 家。
- Insider 持股: 39.0%。
- 資料異常: `institutionsFloatPercentHeld` 為 126.6%, 超過 100%, 屬計算口徑錯誤, 不應採用。
- 前十大機構合計約 40.6% (以下逐列加總):

| 機構 | 持股比例 | 持股數 (M 股) | 最近一期變動 | 報告日 |
|---|---|---|---|---|
| First Eagle Investment Mgmt | 7.85% | 3.34 | -27.3% | 2026-06-30 |
| BlackRock | 6.70% | 2.85 | +5.1% | 2026-06-30 |
| Sumitomo Mitsui Trust | 4.83% | 2.06 | +50.9% | 2026-09-30 |
| Vanguard Portfolio Mgmt | 3.87% | 1.65 | +0.4% | 2026-06-30 |
| Dimensional Fund Advisors | 3.76% | 1.60 | -5.9% | 2026-06-30 |
| Lazard Asset Mgmt | 3.36% | 1.43 | +3.9% | 2026-06-30 |
| Victory Capital | 3.09% | 1.32 | +325.6% | 2026-06-30 |
| Vanguard Capital Mgmt | 2.71% | 1.15 | +1.1% | 2026-06-30 |
| Neuberger Berman | 2.30% | 0.98 | +15.7% | 2026-06-30 |
| State Street | 2.14% | 0.91 | +11.0% | 2026-06-30 |

機構動向: 有增持 (Sumitomo、Neuberger、State Street、BlackRock), 也有明顯減持 (First Eagle -27%)。Victory Capital 的 +325.6% 很可能是建倉口徑或基期變動, 不宜解讀為大幅加碼。整體為輪動而非單向流動。

## Net sentiment score

**綜合: 中性偏謹慎 (信心: 低)**

- 分析師面: 偏多。66.7% Buy、無 Sell 以外的負面評等變動 (近一月無變動), 平均目標價高於多數近期成交價。
- Insider 面: 偏空。6 個月淨賣出約 $23.2M, 主要來自 >10% 持有人, 高管買入僅 $0.2M。
- 機構面: 中性。持股集中度高, 有增有減。
- 散戶面: 無資料, 無法評估。

**Divergence flag: 無法判定。** 分析師與 insider 方向相反 (分析師偏多、insider 淨賣出), 但缺少散戶資料, 無法確認散戶是否與分析師相反。若後續取得 Reddit 或 StockTwits 資料, 應再檢查此分歧。

資料缺口與後續:
1. Reddit 與 StockTwits 因網路限制無法存取。
2. 分析師目標價與個別升降評等來自網路摘要, 需對照 Bloomberg 或 Yahoo 即時資料核實。
3. 報告日為 2026-11-04, 但最新 insider 資料止於 2026-10-02, 最新 rating 資料無日期。

SENTIMENT REPORT COMPLETE
