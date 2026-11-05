# Sentiment — MP (MP Materials) as of 2026-11-06

> 資料時點注意：本次 DATE 為 2026-11-06，晚於執行當日 2026-11-05。下列數據為工具回傳的最新快照，部分來自網路新聞，日期互相不一致，需以收盤後資料再核對。

## Analyst consensus

Yahoo 評級分布（yf rec_summary，19 家）：5 strongBuy / 13 buy / 1 hold / 0 sell / 0 strongSell，即 18 家偏多、1 家中立，無賣出評級。

| 期間 | strongBuy | buy | hold | sell | strongSell |
|---|---|---|---|---|---|
| 目前 (0m) | 5 | 13 | 1 | 0 | 0 |
| 前 1 個月 (-1m) | 5 | 13 | 1 | 0 | 0 |
| 前 2 個月 (-2m) | 5 | 13 | 0 | 0 | 0 |

近期變動：兩個月內 hold 由 0 變 1，其餘評級數量不變。yf 的 recommendations 欄位只給月度彙總，未列出個別升降評等動作。

網路新聞補充（非 yf 原始資料，日期與來源不完全一致）：
- MarketBeat 系列快照描述為「Moderate Buy」共識，平均目標價在 9 月約 78.21 美元、10 月約 75 美元、11 月初約 80.33 美元（17 家）。
- 9 月有一家給出 Strong Sell（Zacks Research 列於 10 月文章），Needham 將目標價下調至 73 美元。
- 10 月初 Fintel 預測表：中位數 12 個月目標價約 66.32 美元，區間約 49.91 至 91.03 美元。
- 11 月初一則文章提到升評與目標價上調各一、新覆蓋一家，但該文日期標示有矛盾，未直接採用。
- 文中股價約 67.61 美元，接近 Fintel 中位目標價，低於多數平均目標價。

## Retail social

- Reddit（r/wallstreetbets、r/stocks）：本次無法存取，WebFetch 回傳 "unable to fetch"。此來源缺失。
- StockTwits：api.stocktwits.com DNS 解析失敗（ENOTFOUND），本次無法取得訊息流。此來源缺失，需於 session 網路設定中允許該網域後再試。
- X / 新聞討論：WebSearch 結果以財經新聞與分析師評論為主，缺乏可量化的散戶貼文樣本，無法估計提及量。
- 提及量：無法量化，無法與常態基準比較。
- 散戶傾向：無有效樣本，無法判定，標示為「資料不足」。
- 主要題材（由新聞標題推估，非散戶原文）：稀土與國防需求帶動的題材、分析師目標價調整、空頭部位佔比偏高（一則文章稱空單限制了漲幅）。

## Insider activity

Net 6mo: 資料不足。yf insider 回傳空陣列，無法確定是「6 個月內無內部人交易」還是資料抓取失敗（同一批次 Yahoo cookie/crumb 抓取已失敗）。不列出任何買賣金額或姓名，避免以不完整資料下結論。

## Ownership shifts

- 內部人持股比例：約 19.6%
- 機構持股比例：約 78.2%（佔流通股約 97.2%）
- 機構家數：約 970 家
- 趨勢：yf major_holders 僅提供單一時點快照，無法判斷增減趨勢，標示為「無趨勢資料」。
- 解讀：機構持股高度集中，流通股幾乎全由機構持有，這本身不代表買賣方向。

## Net sentiment score

Composite: **偏多（bullish），信心低至中等**

- 分析師面：偏多。18/19 評級為買入或強力買入，無賣出評級；但目標價在 9 至 11 月間有下調，且股價低於平均目標價。
- 散戶面：無資料。Reddit、StockTwits 皆無法取得，無法評估。
- 內部人面：無資料。空陣列無法判讀。
- 信心：分析師樣本充足（19 家），但時間點偏舊（Yahoo 無明確日期），且缺乏散戶與內部人資料，因此僅為中等偏低信心。

Divergence flag: **無法判定**。散戶傾向缺失，無法與分析師傾向比較。

## 資料缺口與待辦

1. Reddit 與 StockTwits 需重試，或允許相關網域後重跑。
2. yf insider 需於 Yahoo cookie/crumb 恢復後重抓，確認是否真的為空。
3. 分析師目標價需以 MarketBeat / Fintel 當日數據核對，目前新聞來源日期互相矛盾。

SENTIMENT REPORT COMPLETE
