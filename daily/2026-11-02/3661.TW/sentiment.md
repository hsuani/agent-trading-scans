# Sentiment — 3661.TW (世芯-KY, Alchip Technologies) as of 2026-11-02

資料可信度提醒: Reddit 與 StockTwits 本次皆無法取得資料, 零售情緒部分為空白而非「中性」。網頁搜尋結果日期混雜, 無法確認 2026-11 當月的評等或股價變化。

## Analyst consensus

截至 0m 快照: 6 strongBuy / 9 buy / 1 hold / 0 sell / 0 strongSell (共 16 家, 其中 15 家偏多, 1 家中立, 0 家偏空)。

| 期間 | strongBuy | buy | hold | sell | strongSell |
|---|---|---|---|---|---|
| 0m (現在) | 6 | 9 | 1 | 0 | 0 |
| -1m | 6 | 9 | 1 | 0 | 0 |
| -2m | 6 | 9 | 1 | 0 | 0 |
| -3m | 6 | 8 | 1 | 0 | 0 |

近期動向: 評等分布幾乎沒有變化, 過去三個月僅 -3m 到 -2m 之間 buy 由 8 變 9, 沒有偵測到降評。yfinance `recommendations` 回傳的是彙總分布而非個別升降評事件, 因此無法列出具體券商的升降評紀錄。

目標價: 網頁搜尋的一個聚合來源顯示平均 12 個月目標價約 NT$5,666, 另一來源提及 Citi 目標價 NT$6,800。這些數字的日期無法確認, 且與另一快照的股價區間 (NT$2,870 至 NT$3,620, 52 週區間約 NT$2,480 至 NT$5,640) 之間的落差很大, 不宜直接作為當前判斷依據。

## Retail social

- Reddit (r/stocks, r/wallstreetbets): 本次抓取被阻擋 (Claude Code unable to fetch www.reddit.com), 無樣本、無情緒傾向統計。
- StockTwits: api.stocktwits.com 無法解析 (DNS 失敗), 需在 session 網路設定中允許該網域才能重試。
- X / 新聞: 單次網頁搜尋未找到 2026-11 的個人或社群觀點, 僅有 Simply Wall St 敘事頁面的看多論點 (預估營收高速成長, 認為 ASIC 與 HPC 需求擴張), 這屬於分析師端或網站編撰觀點, 不代表散戶情緒。
- 聲量 (buzz volume): 無法量化, 與典型水準比較無資料。
- 主要主題 (由網頁敘事推得, 非散戶原文): ASIC 客製晶片需求、HPC/AI 擴張、高本益比對獲利兌現的依賴。
- 散戶傾向: 無法判定 (bullish / bearish / mixed 皆無資料支持)。

## Insider activity

Net 6mo: 無資料。yfinance `insider` 回傳空陣列, 此為資料缺失, 不代表「沒有內部人交易」。需另行查詢公開資訊觀測站 (MOPS) 的董監事持股變動申報才能確認。

## Ownership shifts

- 內部人持股比例: 約 3.14%
- 機構持股比例: 約 38.85% (流通股口徑約 40.11%)
- 機構持股家數: 259
- 趨勢: 單一時點快照, 無法判定機構集中度的變化方向。

## Net sentiment score

Composite: **偏多 (bullish), 信心低 (low)**

- 分析師端偏多且穩定: 15 買進 + 1 持有 + 0 賣出, 三個月內無降評紀錄。
- 零售端無資料, 無法與分析師端交叉比對。
- 內部人端無資料, 不能作為佐證或反證。
- 信心低的主因是零售與內部人資料缺失, 而非訊號互相矛盾。

Divergence flag: **無法判定 (no data)**。目前沒有零售傾向可與分析師傾向比較, 因此不做背離判斷。

## 待補資料

1. 解除 api.stocktwits.com 與 Reddit 的存取限制後重跑零售情緒部分。
2. 以 MOPS 核對近 6 個月董監事與大股東的申報買賣。
3. 取得帶明確日期的最新券商評等與目標價變動, 確認 2026-10 財報後 (預計 2026-10-30 前後) 的評等調整。

SENTIMENT REPORT COMPLETE
