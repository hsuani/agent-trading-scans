# Sentiment — FN as of 2026-10-21

> 資料時效說明: 本次可取得的最新價格與分析師資料約至 2026-10-15。yf.py 的 rec_summary 與 holders 來自快取，rec_summary 四個期間數字完全相同，需視為可能過期。散戶社群來源 (Reddit、StockTwits) 本次無法取得。

## Analyst consensus

yf.py rec_summary (期間 0m): 7 buy (3 strong buy + 4 buy) / 2 hold / 0 sell，共 9 家。
Google Finance 過去 3 個月: 6 buy / 2 hold / 0 sell，共 8 家，平均 12 個月目標價 $702.14。
Investing.com: 7 buy / 2 hold / 0 sell。

近期動態:
- 2026-10-15: B. Riley (Dave Kang) 維持 Hold，目標價 $431。這是目前已知最低的目標價。
- 2026-08 (約): Susquehanna 維持 Buy，目標價 $850；Rosenblatt 維持 Buy，目標價 $750；J.P. Morgan 維持 Hold，目標價 $695。
- 評級升降級歷史: DATA_UNAVAILABLE (yf.py recommendations 只回傳與 rec_summary 相同的彙總，沒有逐筆升降級紀錄)。

價格脈絡: 最新可得股價約 $377.53 (2026-10-15，當日約 -4%)，52 週區間 $364.41 至 $748.89，距高點回落約 50%。分析師平均目標價 $702 相對該價位約有 86% 的上行空間，但目標價數字本身可能偏舊。

## Retail social

- Reddit (r/wallstreetbets、r/stocks): DATA_UNAVAILABLE。WebFetch 無法連線 www.reddit.com，本次沒有取得任何貼文樣本、提及數或多空傾向。
- StockTwits: DATA_UNAVAILABLE。api.stocktwits.com 無法解析 (DNS 失敗)。
- X / 新聞與網路搜尋: 搜尋結果中沒有可用的散戶觀點。找到的 Reddit 相關頁面多為 2026-05 的自動生成內容，股價 $621 已過時，不採用。另一個搜尋指出 2026-10 沒有找到解釋股價下跌的新聞。
- 提及量 (buzz volume): DATA_UNAVAILABLE。
- 多空傾向 (retail tilt): DATA_UNAVAILABLE。
- 主要主題: DATA_UNAVAILABLE。沒有可引用的散戶貼文樣本，依規定不編造引言。

## Insider activity

評估區間: 2026-04-21 至 2026-10-21。

- 公開市場買入: 0 筆。
- 公開市場賣出 (2 筆，合計約 $2.74M):
  - Archer Edward T (Officer)，2026-09-03，賣出 2,500 股，約 $964,765 (每股 $385.58–386.34)。
  - Bahrami Homa (Director)，2026-05-22，賣出 2,500 股，約 $1,779,775 (每股 $711.91)。
- 非現金授予 (Stock Award，非市場買入，合計約 77,956 股，價格 $0):
  - 2026-08-11 與 2026-08-20 兩批，對象為 Grady Seamus (CEO，合計 42,508 股)、Gill Harpal S. (President，合計 17,120 股)、Sverha Csaba (CFO，合計 10,257 股)、Archer (合計 8,071 股)。
- 淨額: 6 個月淨賣出約 $2.74M，無公開市場買入。

脈絡: 2025 年下半年至 2025 年 11 月的賣出規模大得多，例如 CEO Grady 在 2025-11-26 賣出約 $10.0M (每股約 $446)，Gill 在 2025-09-04 賣出約 $5.0M (每股約 $355)。這些都在 6 個月區間之外，而且成交價高於目前約 $377 的股價。
資料注意: 來源中 Gill Harpal S. 的職稱在 2026 年紀錄為 President，在 2025-06-04 的紀錄為 CEO，職稱欄位前後不一致，未做更正。

## Ownership shifts

- 內部人持股: 約 0.26% (insidersPercentHeld)。
- 機構持股比例: 報告值 103.7%，超過 100%，應為資料計算口徑問題，不宜直接解讀。機構家數 1,033。
- 前十大機構 (2026-06-30 季報，共約 49.8% 持股):
  - 減持: T. Rowe Price Associates -49.5%、Invesco -16.4%、BlackRock -13.8%、FMR -13.1%、Geode -13.1%、Vanguard Portfolio Management -11.0%。
  - 加持: T. Rowe Price Investment Management +278.6%、JPMorgan +42.8%、State Street +0.9%、Vanguard Capital Management +0.6%。
- 趨勢判讀: 前十大中 6 家減持、4 家加持。這只是單一季度的快照，無法確認連續趨勢。

## Net sentiment score

綜合判斷: 中性 (信心: 低)

- 分析師面: 偏多。7 家 buy 對 0 家 sell，但近期 B. Riley 以 Hold 與 $431 目標價給出明顯保守觀點，且資料可能過期。
- 內部人面: 偏空至中性。6 個月僅 2 筆公開市場賣出，合計約 $2.74M，無買入；大部分內部人交易為授予股票。規模相對 2025 年明顯縮小。
- 機構面: 中性偏空。前十大中減持家數略多，但 T. Rowe Price IM 與 JPMorgan 增持。
- 散戶面: DATA_UNAVAILABLE。

Divergence flag: 無法判定 (DATA_UNAVAILABLE)。散戶傾向資料缺失，因此無法判斷散戶與分析師是否背離。目前可見的對比是: 分析師平均目標價 $702 與股價 $377 之間有大幅價差，同時 B. Riley 給出 Hold 與 $431 的保守目標價。

資料缺口與可信度:
1. 散戶社群 (Reddit、StockTwits) 完全缺失，是本報告最大的缺口。
2. rec_summary 與 holders 來自快取，時效不確定。
3. 最新可得價格與評級日期約為 2026-10-15，不是 2026-10-21 當日資料。
4. 機構持股比例超過 100%，應視為資料口徑問題。

SENTIMENT REPORT COMPLETE
