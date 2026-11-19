# Sentiment — MP as of 2026-11-20

> 資料品質警示: Reddit 與 StockTwits 本次皆無法取得 (Reddit 回傳 fetch 失敗; api.stocktwits.com DNS 解析失敗, 需於 session 網路設定允許該網域)。網路搜尋結果多為 2025 至 2026 年 8 月的聚合報導, 無法確認 2026-11 當月動態。本報告的散戶情緒部分為空白, 不應視為「散戶中性」。

## Analyst consensus

以 yf 工具取得的評等分布 (rec_summary, 期間 0m):

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 合計 |
|---|---|---|---|---|---|---|
| 0m (現在) | 5 | 14 | 0 | 0 | 0 | 19 |
| -1m | 5 | 13 | 1 | 0 | 0 | 19 |
| -2m | 5 | 13 | 1 | 0 | 0 | 19 |
| -3m | 5 | 13 | 0 | 0 | 0 | 18 |

目前為 19 buy / 0 hold / 0 sell (含 5 Strong Buy)。過去三個月 Hold 票由 1 降為 0, Buy 票由 13 增為 14, 屬小幅正向漂移, 未見降評。

個別券商動態 (網路搜尋, 日期不完整, 需獨立驗證):
- Freedom Broker: Hold 升 Buy, 目標價由 57 降至 51 USD (日期不明)。
- Morgan Stanley: 2025 年末升 Overweight, 目標價 71 USD; 2026-05-11 再調至 70 USD, 維持 Overweight。
- Goldman Sachs: 2026-05-08 目標價由 71 升至 80 USD, 維持 Buy。
- BMO: 升 Outperform, 目標價 75 USD (由 76 微降)。
- Barclays: 2026-07-16 目標價由 69 降至 65 USD, 維持 Overweight。
- Needham: 目標價由 81 降至 73 USD。
- Deutsche Bank: 2026-07-09 目標價由 70 降至 61 USD, 維持 Buy。
- Wedbush: 2026-04-20 首次覆蓋, Buy, 目標價 90 USD。

共識目標價: MarketBeat 2026-07 版約 79.25 USD; Fintel 2026-08-28 版約 78.28 USD, 最高 105 USD。2026 年中以來多數券商為目標價下修而非評等調整, 評等仍偏多。

## Retail social

- Reddit (r/wallstreetbets, r/stocks): 本次無法取得 (fetch 失敗), 無貼文樣本, 無法判斷散戶語氣。
- StockTwits / X: StockTwits 無法連線。X 相關搜尋未找到 2026-11 的討論。以新聞聚合站 (StockTwits 新聞頁面) 的標題語氣看, 偏向報導「升評」「買進機會」, 但這是媒體標題而非散戶貼文。
- 討論量 (buzz volume): 無法量化, 標記為「未知」。
- Themes (由搜尋結果歸納, 非散戶原文): 國防需求與供應鏈自主 (美國稀土供應鏈)、沙烏地合資 (Saudi JV) 的上行空間、營運成本下降、估值偏高 (前瞻 EV/Sales 約 37 倍, 高於同業與自身五年平均, 來源為 2025 年底至 2026 年初報導)。
- Tilt: 無法判定 (資料缺口)。

## Insider activity

Net 6mo: $0 buys, $0 sells (yf insider 回傳空陣列)。

注意: 空陣列可能是真實無交易, 也可能是資料源缺漏 (本次 Yahoo cookie/crumb 取得失敗, 工具降級執行)。在採信「無內部人交易」之前, 建議以 SEC Form 4 直接核對。

## Ownership shifts

- 內部人持股: 19.7% (yf major_holders)
- 機構持股: 78.5%; 浮動股機構持股 97.7%
- 機構家數: 966
- 歷史趨勢: 本次工具僅提供單一時點快照, 無法判斷季度增減趨勢。

## Net sentiment score

- Composite: **偏多 (bullish), 信心度中低**
- 依據: 分析師評等 19 buy / 0 sell, 近三月 Hold 減少, 目標價共識約 78-79 USD。扣分因素: 近期目標價多次下修 (Barclays, Needham, Deutsche Bank, Freedom Broker), 估值偏高, 散戶與 Reddit/StockTwits 無資料, 內部人交易資料為空且可能不完整。
- 信心度受限於資料缺口: 三個社群來源中兩個失敗, 其餘資料多為 2026-08 以前的時點。

Divergence flag: **無法判定 (no)**。缺少散戶語氣資料, 無法比較與分析師傾向是否相反。若後續取得 Reddit 或 StockTwits 資料, 再重新評估。

## 待補項目

1. 允許 api.stocktwits.com 網域, 重跑 StockTwits 串流。
2. Reddit 公開 JSON 需替代路徑或稍後重試。
3. 以 SEC EDGAR Form 4 核對 6 個月內部人交易。
4. 取得 2026-11 的即時股價與近期評等變動 (現有搜尋結果止於 2026-08)。

Sources (網路搜尋參考):
- [Freedom Broker upgrade (StockTwits News)](https://stocktwits.com/news-articles/markets/equity/mp-stock-freedom-broker-upgrade-upside-price-target-magnet-production/cNGD0paR9BT)
- [Fintel MP snapshot](https://fintel.io/s/us/MP)
- [Morgan Stanley raises price target on MP (Yahoo Finance)](https://finance.yahoo.com/markets/stocks/articles/morgan-stanley-raises-price-target-231210134.html)
- [BMO upgrade (Investing.com)](https://ng.investing.com/news/stock-market-news/bmo-upgrades-mp-materials-on-us-supply-chain-push-and-saudi-jv-upside-2225382)
- [StockAnalysis MP ratings](https://stockanalysis.com/stocks/mp/ratings/)

SENTIMENT REPORT COMPLETE
