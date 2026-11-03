# Sentiment — 6805.TW 富世達 (Fositek) as of 2026-11-04

> Reddit 與 StockTwits 無法取得，散戶面資料缺口大，綜合評分信心偏低。

## Analyst consensus

9 buy / 0 hold / 0 sell（rec_summary: strongBuy 3 + buy 6；hold 與 sell 皆為 0）。

| 期間 | strongBuy | buy | hold | sell | strongSell |
|---|---|---|---|---|---|
| 0m（當前） | 3 | 6 | 0 | 0 | 0 |
| -1m | 3 | 6 | 0 | 0 | 0 |
| -2m | 3 | 5 | 0 | 0 | 0 |

- 近兩個月買進家數由 8 增至 9，無賣出或中立評等，評等結構偏向一致看多。
- `recommendations` 端點未回傳具體升降評明細，無法確認個別券商的升降評日期。
- 目標價: 日系外資於 2026-07 重申「買進」，目標價 2600 TWD（來源為新聞報導，非 yf）。另有摩根士丹利舊報告目標價 1800 TWD，發布日期不明，已過時，僅供參考。
- 投資網站 Investing.com（日期不明）顯示約 33% 上漲空間，此數據無法核對日期。
- 無法確認 11 月內的最新評等變動。

## Retail social

- Reddit（r/wallstreetbets、r/stocks）: 無法取得。WebFetch 回傳 "unable to fetch from www.reddit.com"，視為 soft-fail。
- StockTwits: 無法取得。api.stocktwits.com DNS 解析失敗（ENOTFOUND），需在工作階段網路設定中允許此網域後才能重試。
- X / 新聞輿論（WebSearch 替代）: 可取得的資料以新聞標題為主，非社群情緒量化。
  - 2026-10-08 報導標題: 奇鋐、富世達遭搜索不受影響，外資喊買富世達（僅見標題，內文未讀到，喊買券商與目標價無法核實）。
  - 2026-10-16 公司重訊: 富世達發布補充公告，說明特定員工被要求協助釐清股票內線交易案件。
- 聲量: 無法量化，本次未取得 Reddit 或 StockTwits 的則數資料。
- 台灣散戶平台（PTT、Dcard 等）未納入本次工具清單，亦未查詢。
- 散戶傾向: 無法判定（資料缺口）。

Themes（由新聞標題歸納，非社群原文）:
- 液冷與散熱需求延續的成長敘事（外資持續看好）。
- 公司治理風險: 員工涉及內線交易調查的公告。
- 估值偏高: Simply Wall St 報導本益比約 59 倍，遠高於台灣電子業平均約 23 倍（日期不明）。
- 股價波動大: 52 週區間約 849 至 2275 TWD（Investing.com，日期不明）。nStock 於 2026-10-16 顯示股價約 2250 TWD。

## Insider activity

Net 6mo: 資料不可得。yf `insider` 端點回傳空陣列，無法確認 6 個月內內部人買賣金額。以 TWD 計，本次無任何可驗證金額，因此不寫入 億 或 B 單位。
- 2026-10-16 公告涉及「特定員工」協助調查，屬於調查協助，不是交易紀錄，不能當作買賣訊號。
- 建議到公開資訊觀測站核對董監事與大股東持股申報（申報資料需人工查證）。

Ownership（yf major_holders）:
- insidersPercentHeld 21.1%
- institutionsPercentHeld 40.6%（float 持股占比 51.5%）
- institutionsCount 80
- 歷史趨勢（季變化）無法取得，本次無法判斷機構集中度是升或降。

## Net sentiment score

Composite: **偏多 (bullish-leaning neutral)**，信心 **低-中**。

分項判斷:
- 分析師: 偏多（9/9 買進，無賣出，信心中等；樣本數不大，且目標價來源多為新聞而非即時數據）。
- 散戶: 無法判定（Reddit、StockTwits 不可得）。
- 內部人: 無法判定（yf 無資料）。
- 新聞面: 混合（外資正面評價 vs. 內線交易調查公告與搜索新聞）。

Divergence flag: **無法判定**。散戶資料缺失，無法比較散戶與分析師傾向是否相反。

資料缺口與建議補強:
1. 允許 api.stocktwits.com 網域後重試 StockTwits。
2. Reddit 公開 JSON 端點需改用可用的代理或其他來源重試。
3. 補抓 PTT 與 Dcard 的富世達相關討論。
4. 人工核實內線交易調查公告的完整內容與案件進度，此為主要治理風險來源。
5. 核實 Investing.com 與 Simply Wall St 數據的日期。

本報告為情緒面分析，不含交易建議。

## Sources

- [nStock 6805](https://www.nstock.tw/6805)
- [nStock 新聞 article 551341](https://www.nstock.tw/news/article_m?id=551341)
- [中時 wantrich 2026-07-08](https://wantrich.chinatimes.com/news/20260708900406-420101)
- [工商時報/cnyes 新聞 6535038](https://news.cnyes.com/news/id/6535038)
- [Yahoo 股市 機構買賣 6805](https://tw.stock.yahoo.com/quote/6805/institutional-trading)
- [Investing.com Fositek consensus](https://www.investing.com/equities/fositek-consensus-estimates)
- [Simply Wall St Fositek](https://simplywall.st/stocks/tw/tech/twse-6805/fositek-shares/valuation)

SENTIMENT REPORT COMPLETE
