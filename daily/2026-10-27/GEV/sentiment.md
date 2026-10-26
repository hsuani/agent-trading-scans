# Sentiment — GEV (GE Vernova) as of 2026-10-27

> 資料時點注意：執行環境系統日期為 2026-10-26 (UTC 20:11)，本報告以 2026-10-27 作為指定 as-of 日期，但 yfinance 類資料為 2026-10-26 盤後快照。Reddit、StockTwits 無法取得，零售情緒部分為空白，不以推測填補。

## Analyst consensus

yf rec_summary（當前，USD 不適用，為家數）：**6 Strong Buy / 25 Buy / 7 Hold / 0 Sell / 0 Strong Sell**，合計 38 家；Buy 類（Strong Buy + Buy）佔 **83%**，Sell 類 **0%**。

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell |
|---|---|---|---|---|---|
| 當前 (0m) | 6 | 25 | 7 | 0 | 0 |
| -1m | 6 | 24 | 7 | 0 | 0 |
| -2m | 6 | 24 | 7 | 0 | 0 |
| -3m | 6 | 24 | 8 | 0 | 0 |

近三個月評級分布幾乎不變，Hold 由 8 降為 7，Buy 由 24 增為 25，屬於微幅上調。

- 近期變動：MarketBeat 摘要提到一家機構近期下調至 Hold（機構名與日期未能在 yf 資料中核實）。Mizuho 維持 Neutral，目標價 2026-07-27 由 $913 調至 $949。7 月財報後多家上調目標價，Guggenheim 目標價 $1,450 為高點。
- 目標價：二手來源平均目標價約 $1,172（MarketBeat），屬快照，非即時共識。
- 家數不一致：Barchart 轉述為 31 家（23 Strong Buy / 2 Moderate Buy / 6 Hold），與 yf 的 38 家不同，本報告以 yf 為準。
- 近期營收與獲利：來源稱營收年增 21.9%，但季度 EPS $2.47 低於預估 $3.17（來源日期與季度標示不明確，需自行核對）。
- 下次財報：共識預期 2026-10-28 盤前公布，EPS 預估 $4.01（TrendSpider 另列 10-21，未確認）。此事件在 as-of 日後 1 天，為分析師情緒的最大變數。

## Retail social

- Reddit（r/wallstreetbets、r/stocks）：**資料取得失敗**，WebFetch 回傳 "unable to fetch from www.reddit.com"，無法取得樣本串文、分數與傾向。
- StockTwits：**資料取得失敗**，DNS 解析錯誤（api.stocktwits.com ENOTFOUND），無法取得訊息量與多空標記比例。
- X / 新聞搜尋：WebSearch 僅找到機構型評論與評級彙整網站（MarketBeat、Benzinga、Webull、Fintel、TrendSpider 等），未找到可辨識的散戶貼文，故無法判斷散戶語氣。
- 討論量（buzz volume）：**無資料**，無法與常態比較。
- 零售傾向：**無法判定**（bullish / bearish / mixed 均不成立，因無樣本）。
- 主題：無可引用的零售主題。若要補足，建議於可連線的環境重新執行 Reddit 與 StockTwits 查詢，或改以 X 搜尋工具補查。

## Insider activity

資料區間：2026-04-27 至 2026-10-27（6 個月）。金額單位 USD，以 M 表示。

| 日期 | 人員 | 職務 | 交易 | 股數 | 金額 (USD M) |
|---|---|---|---|---|---|
| 2026-06-01 | Abate Victor | Officer | 公開市場賣出 @ $948.08 | 4,819 | 4.57 |
| 2026-05-14 | Potvin Matthew Joseph | Officer | 公開市場賣出 @ $1,059.09 | 2,333 | 2.47 |
| 2026-05-14 | 董事 x 8 人（Reynolds、Donald、Hund-Mejean、Angel、Akins、Rucker、Malave、Matthew Harris） | Director | 未註明（推定年度股權獎勵） | 495–1,350 each | 無資料 |
| 2026-04-27 | Strazik Scott | CEO | 衍生性證券行權（conversion） | 44,496 | 5.35（行權價計算值） |
| 2026-04-02 | Baert Steven | Officer | 未註明 | 8,505 | 無資料 |

- 6 個月公開市場買入（Purchase）：**$0**，未發現任何內部人買入。
- 6 個月公開市場賣出（已確認金額）：約 **$7.0M**（Abate $4.57M、Potvin $2.47M）。
- 不確定項目：CEO Strazik 4/27 的 44,496 股屬行權，不等同賣出；Baert 4/2 的 8,505 股與董事 5/14 的股數未標示交易性質，不計入淨額。
- 最值得注意：**CEO 與 CFO 在本區間沒有公開市場賣出紀錄**；賣出者為 Officer 層級（Abate、Potvin）。CFO Parks 上一筆公開賣出為 2025-08-26，已超過 6 個月。
- 較早紀錄（2026-03-03 Baert 賣出 $4.5M、2026-02-27 多人大量紀錄）超出 6 個月窗口，未納入。
- 解讀：內部人為淨賣方（無買入），但賣出規模占大型股市值比例很小，且無 CEO / CFO 公開賣出，信號偏中性偏弱空。

## Ownership shifts

- 機構持股比例：**81.5%**（機構持股 4,246 家）
- 內部人持股比例：**0.13%**
- 趨勢：yf major_holders 僅提供快照，無法判斷季度變化，**趨勢資料缺失**。
- 解讀：機構持股高度集中，支撐股價穩定性，但也意味著財報後的機構再平衡可能放大價格波動。

## Net sentiment score

- **分析師共識：偏多（bullish-leaning）**。38 家中 83% 為買進評級，零賣出評級，近三個月分布穩定。信心：**高**（資料一致）。
- **內部人：偏弱 / 中性**。6 個月無公開買入，有約 $7.0M 公開賣出，但無 CEO / CFO 公開賣出。信心：**中**（部分交易性質未明）。
- **零售情緒：無資料**。Reddit 與 StockTwits 皆無法取得，X 搜尋未找到可用樣本。
- **綜合評分：偏多（bullish-leaning），信心低至中**。主要依據是分析師一致偏多，內部人與零售部分缺乏足夠支持，綜合信心受限於資料缺口。

**Divergence flag：無法判定**。因零售資料缺失，無法確認零售傾向是否與分析師相反。若後續補上零售資料，需特別留意「分析師偏多、零售偏空」的組合。

## Sources

- yf rec_summary、recommendations、insider、major_holders（pipeline/tools/yf，2026-10-26 執行）
- WebSearch 結果（MarketBeat、Benzinga、Webull、Fintel、TrendSpider 等彙整頁面，日期混合，部分數字為舊資料）

SENTIMENT REPORT COMPLETE
