# Sentiment — PWR as of 2026-11-10

資料時點說明: 本報告以 2026-11-10 為準。Reddit 與 StockTwits 本次皆無法取得 (見下方), 散戶面資料缺漏, 結論信心度因此降低。

## Analyst consensus

目前 (yf rec_summary, period 0m) 共 30 位分析師: 1 Strong Buy + 24 Buy = 25 買進 (約 83%), 5 Hold (約 17%), 0 Sell。

近三個月趨勢 (yf recommendations):

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 合計 |
|---|---|---|---|---|---|---|
| 0m (現在) | 1 | 24 | 5 | 0 | 0 | 30 |
| -1m | 1 | 24 | 4 | 0 | 1 | 30 |
| -2m | 1 | 24 | 5 | 0 | 1 | 31 |
| -3m | 0 | 23 | 6 | 0 | 1 | 30 |

Recent moves: 評級結構過去三個月小幅偏多, Hold 由 6 降至 5, Strong Sell 由 1 降至 0。工具未提供逐筆升降評等紀錄, 無法列出具體 upgrade/downgrade 事件與目標價變動。

網路搜尋的補充 (未標註日期或日期不一, 僅供參考, 不作為主要依據):
- MarketBeat 頁面提及 2026-05-06 一次 Buy 降為 Hold 的調整, 同頁亦提及後續目標價上調至 $725。
- Fintel 頁面顯示分析師情緒分數 75.47, 平均一年期目標價約 $796 (頁面無日期)。
- Simply Wall St 描述分析師情緒偏強、盈餘預估上修, 並列出勞動力短缺與基建專案延誤為風險。

## Retail social

- Reddit (r/wallstreetbets, r/stocks): 本次無法取得 (WebFetch 回報無法連線 www.reddit.com), 無法計算提及量與貼文傾向。
- StockTwits: 無法取得 (api.stocktwits.com DNS 解析失敗, 疑為 session 網路白名單未開放), 需於 session 網路設定允許此網域後再重試。
- X / 新聞鏈接: 以網路搜尋取得的近期事件為主。2026-11-04 Trefis 報導指出 PWR 當日下跌約 11.7%, 同期 S&P 500 上漲約 1.6%, 報導將跌幅歸因於資料中心相關曝險的疑慮, 並提到公用事業業務仍是基本盤。此為新聞敘述, 非散戶貼文。
- Buzz 量: 無法與常態比較 (缺乏 Reddit/StockTwits 數據)。
- Retail tilt: 無法判定 (資料缺)。
- Themes (以新聞與分析師端可見的議題代替): 資料中心需求與估值敏感度、基建專案進度與人力瓶頸、近期股價急跌後的情緒修復。

## Insider activity

Net 6mo (2026-05-10 至 2026-11-10, 嚴格區間): 公開市場買進 $0M, 公開市場賣出 $0M。區間內僅見 董事與高階主管的股權贈與與年度股票獎勵 (無金額), 以及 2026-05-21 至 06-01 的董事股票授予 (無金額)。

區間外但鄰近的大額賣出 (2026-05-04 / 05-05, 供參考):
- CEO Austin Earl Charles Jr (2026-05-05): 賣出 155,992 股, 成交價 $765.14–$777.60, 金額約 $120.2M。
- Officer Paul M. Nobel (2026-05-04): 賣出 4,000 股, 價約 $756.98, 金額約 $3.0M。

合計鄰近大額賣出約 $123.2M, 均為 2026 年 5 月, 與 2025 年 11 月的一批賣出 (General Counsel Wayne、Officer Ducey、Director Jackman、Director Fried, 合計約 $14.3M) 同屬高位減持。此次 CEO 大額賣出是否依 10b5-1 計畫執行, 工具資料未揭露, 無法判定。

Insider ownership: 0.65% (yf major_holders)。

## Ownership shifts

- 機構持股: 91.8% (流通股口徑 92.4%), 機構數 2,561 家。
- 工具僅提供單一時點快照, 無法判斷近期增減趨勢。
- 內部人持股比例低 (0.65%), 股權集中度並非主要風險點。

## Net sentiment score

Composite: **偏多 (分析師端) / 中性 (整體) — 信心度低**

- 分析師端: 偏多 (83% 買進, 0% 賣出, 評級結構近三個月小幅改善)。
- 內部人端: 偏空傾向 (鄰近區間有 $123.2M 高位賣出, 區間內無公開市場買進)。
- 散戶端: 無資料, 無法評分。
- 新聞端: 近期 (2026-11-04) 有一次 -11.7% 的急跌, 原因為資料中心疑慮, 偏空情緒仍在消化。

Divergence flag: **無法判定** — 散戶端資料缺漏, 無法檢驗散戶與分析師是否反向。但分析師偏多與內部人大額減持之間存在方向分歧, 值得後續追蹤: 若 CEO 賣出為計畫性交易, 其訊號強度較低; 若非計畫性, 則與分析師偏多形成對照。

資料來源與限制:
- yf 工具 (recommendations, rec_summary, insider, major_holders): 成功取得; Yahoo cookie/crumb 失敗但資料仍回傳。
- Reddit (r/wallstreetbets, r/stocks): 失敗 (無法連線)。
- StockTwits: 失敗 (DNS 解析)。
- 網路搜尋: 取得部分新聞與評等頁面, 多數無日期, 已在內文標註, 未作為主要結論依據。

SENTIMENT REPORT COMPLETE
