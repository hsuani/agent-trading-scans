# Sentiment — ETN as of 2026-10-23

## Analyst consensus
資料來源: `pipeline/tools/yf.py ETN rec_summary`（快取 refreshed 2026-10-23 11:29 UTC；Yahoo 直連被 proxy 拒絕，數據取自快取，最多落後一日）。

目前 28 位分析師: 5 strong buy / 18 buy / 4 hold / 0 sell / 1 strong sell，即 23 買方評級（約 82%）、4 持有（約 14%）、1 強烈賣出（約 4%）。

近三個月趨勢（yf 快取）: strong buy 6 → 5，buy 16 → 18，hold 持平 4，strong sell 持平 1。整體評級結構穩定偏多，無明顯轉向。

近期調整（WebSearch 交叉比對，非 yf 來源）:
- 2026-09-07 UBS 由 neutral 升至 buy，目標價 450 → 515 USD。
- 2026-09 Evercore 由 in-line 升至 outperform，目標 502 USD。
- 2026-08-16 Wall Street Zen 由 buy 降至 hold（非主流評級機構）。
- 2026-08-28 Morgan Stanley 目標價 500 → 520 USD。
- 2026-10-14 RBC 目標價 512 → 526 USD，維持 outperform。
- 2026-10-14 之後未找到新的評級變動。

目標價共識分歧: Investing.com 約 464.59 USD（25 位）、MarketBeat 10 月文章 481.41 USD、Stockscan 約 639 USD（明顯離群，不採信）。以 MarketBeat 與 Investing.com 區間 465–481 USD 作為參考。

注意: `yf.py ETN recommendations` 回傳內容與 `rec_summary` 完全相同（同為月度計數），未提供逐筆升降評等歷史，故升降評等資料改由 WebSearch 補充。

## Retail social
- Reddit: DATA_UNAVAILABLE。`WebFetch` 指定之 Reddit JSON 端點於本環境遭阻擋，改以 WebSearch 查 r/wallstreetbets 與 r/stocks 相關討論，未搜得 2026 年 ETN 相關主題帖，無法取樣、無法判定多空比例。
- StockTwits: DATA_UNAVAILABLE（多空比例）。WebSearch 僅找到 StockTwits 個股頁，快照無日期且無 bull/bear 百分比。快照顯示價格 418.56 USD、52 週區間 311.92–436.74 USD，但日期不明，不納入判斷。
- X / 新聞輿情: DATA_UNAVAILABLE。未搜得 2026-10 的 X 貼文或散戶情緒文章。
- 替代參考（非散戶，僅作旁證）: TipRanks 顯示 "Very Positive" 投資人情緒（基於 820,848 位投資人近季活動，多為機構與投資組合數據，非社群聲量）。
- 聲量（buzz volume）: 無法量化，以 DATA_UNAVAILABLE 處理。
- 主題（新聞層級，非社群）: 資料中心、電網與公用事業、AI 基礎建設需求為主要多頭敘述；風險敘述包括 2026 年約 110 億美元併購後的負債水準、暫停回購，以及可能出售或分拆車用單位（約 50 億美元）的傳聞。
- 股價背景: 2026 年至今漲幅約 28%–42%（來源時點不一）；2026-09-14 單日下跌 7.6% 至約 393 USD；2026-10-14 開盤約 418.55 USD。

## Insider activity
區間: 2026-04-23 至 2026-10-23（6 個月）。來源 `yf.py ETN insider`（快取）。以公開市場買賣（Sale / Purchase）為準，排除選擇權行使（Conversion）、董事年度股票獎勵（無價格）與無價格紀錄。

| 項目 | 金額（USD M） | 筆數 | 備註 |
|---|---|---|---|
| 公開市場買入 | 0.48 | 2 | 僅董事 JOHNSON GERALD（05-11 約 0.39M；08-13 約 0.09M） |
| 公開市場賣出 | 17.11 | 6 | Officer 與 Director 合計 |
| 淨額 | -16.63 | — | 明顯淨賣出 |
| 選擇權行使（Conversion，不計入淨額） | 2.76 | 2 | MONESMITH 2.66M；YELTON 0.10M |

主要交易:
- MONESMITH HEATH B（資料標示為 Officer / President）：2026-05-06 賣出 18,367 股，約 7.51M USD（約 409.11 USD/股）；2026-08-11 賣出 18,036 股，約 8.26M USD（約 458.04 USD/股）。兩次皆為高額賣出，為淨賣出主因。
- WADECKI ADAM A.（Officer）：2026-08-04 賣出 525 股，約 0.23M USD。
- DENK PETER（Officer）：2026-05-06 賣出 2,000 股，約 0.84M USD。
- GALVAO ANTONIO（Officer）：2026-05-13 賣出 494 股，約 0.20M USD。
- THOMPSON DOROTHY C.（Director）：2026-05-22 賣出 167 股，約 0.06M USD。
- JOHNSON GERALD（Director）：唯一定期公開市場買入者，2026-05-11 買入 961 股（約 402–419 USD），2026-08-13 買入 200 股（約 456–470 USD）。

觀察:
- CEO 級別（資料標示 Officer and Director 之 RUIZ STERNADT PAULO）在 6 個月區間內無公開市場交易紀錄。
- 2026-03-02 YELTON MICHAEL 賣出約 1.31M USD，位於區間外，未計入。
- 2026-10-02 WADECKI ADAM A. 有 997 股紀錄但無價格，性質不明，未計入。
- 持股比例極低: insiders 持股約 0.07%（major_holders 快照）。

## Ownership shifts
- 機構持股比例約 87.9%，機構數約 3,483 家（major_holders 快照）。
- 前幾大持有人（13F，截至 2026-06-30）: BlackRock 約 7.9%（30.7M 股，較前期 +0.43%）；Vanguard Capital Management 約 6.5%（+0.47%）；State Street 約 4.5%（+2.96%）；JPMorgan 約 4.3%（-13.03%，明顯減持）；Morgan Stanley 約 3.4%（+1.06%）；Bank of America 約 2.8%（-8.33%）。
- 趨勢判讀: 被動指數基金（BlackRock、Vanguard、State Street）小幅增持；JPMorgan 與 BofA 減持，屬單一季度變化，樣本不足以定論。缺乏多期歷史，無法判定長期集中度趨勢。

## Net sentiment score
- 分析師面: 偏多，信心高（23/28 買方評級、目標價區間 465–481 USD 高於前期價格區間）。
- 內部人面: 偏空，信心中（6 個月淨賣出約 16.6M USD，主要來自 MONESMITH 兩次大額賣出；董事有小額買入）。
- 散戶/社群面: 無資料（DATA_UNAVAILABLE），無法評分。
- 機構面: 中性偏多（前幾大持有人以被動基金增持為主，但 JPMorgan 明顯減持）。

綜合: 偏多（bullish）、信心中等。分析師與機構面支撐偏多結論；內部人淨賣出為主要反向訊號，但部分賣出可能屬既定計畫或行使選擇權後出售，資料無法區分。散戶面缺失，整體信心因此受限。

Divergence flag: 無法判定（散戶資料缺失，無法比較散戶與分析師傾向）。另有內部人與分析師傾向相反: 分析師偏多，內部人淨賣出。此項為值得留意的差異，但不構成對散戶的判斷。

資料缺口: Reddit、StockTwits、X 皆為 DATA_UNAVAILABLE；yf 為快取資料（最多一日延遲）；`recommendations` 未提供逐筆評等歷史；分析師目標價各來源不一致。

Sources (WebSearch):
- [Barchart: 分析師對 ETN 的看法](https://www.barchart.com/story/news/3884742/are-wall-street-analysts-predicting-eaton-corporation-stock-will-climb-or-sink)
- [MarketBeat: ETN 目標價上調至 526 USD（2026-10-14）](https://www.marketbeat.com/instant-alerts/analyst-eaton-nyse-etn-price-target-raised-to-52600-2026-10-14/)
- [MarketBeat: ETN 股價下跌 7.6%（2026-09-14）](https://www.marketbeat.com/instant-alerts/price-eaton-nyse-etn-trading-down-76-time-to-sell-2026-09-14/)
- [Investing.com: Eaton 一致預期](https://www.investing.com/equities/eaton-consensus-estimates)
- [StockTwits: ETN 個股頁](https://stocktwits.com/symbol/ETN)
- [TipRanks: ETN 投資人情緒](https://www.tipranks.com/stocks/etn/stock-investors)

SENTIMENT REPORT COMPLETE
