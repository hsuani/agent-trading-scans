# Sentiment — CEG as of 2026-10-28

資料截止: 2026-10-28。晚於此日期之資料視為未知。

## Analyst consensus

21 buy (6 strongBuy + 15 buy) / 4 hold / 0 sell (yf rec_summary, 0m 快照; 0 strongSell)。

| 期間 (yf period) | strongBuy | buy | hold | sell | strongSell |
|---|---|---|---|---|---|
| 0m (目前) | 6 | 15 | 4 | 0 | 0 |
| -1m | 6 | 13 | 3 | 0 | 0 |
| -2m | 6 | 13 | 3 | 0 | 0 |
| -3m | 6 | 14 | 3 | 0 | 0 |

- 近三個月買入評級 (buy + strongBuy) 由 19 升至 21, 持有由 3 升至 4, 賣出維持 0。
- 評級變動明細 (個別券商 upgrade/downgrade 日期): DATA_UNAVAILABLE。yf `recommendations` 回傳的仍是彙總計數, 未提供逐筆變動紀錄。
- 目標價 (aggregator, 非 yf): 
  - Mizuho 將目標價由 $335 上調至 $390, 評級維持 Neutral (日期未能於搜尋結果確認)。
  - UBS 與 Barclays 於 2026-07 下修目標價。UBS 數據於來源中出現 $380 → $388 的表述, 方向與數字互相矛盾, 無法確認, 標為待核實。
  - Walnut (2026-08) 平均目標價約 $352.86, 區間 $296 至 $441。
  - 以 mid-Oct 價格約 $258.84 (aggregator) 計算, 平均目標價隱含約 36% 上行空間 (推算值)。
- 來源數字不一致: Barchart 稱 22 位分析師 (16 Strong Buy / 1 Moderate Buy / 5 Hold); Investing.com 為 20 Buy / 3 Hold / 0 Sell; Google Finance 為 15 Buy / 2 Hold; 247wallst/TipRanks 為 20 Buy / 3 Hold / 0 Sell (23 位)。本報告以 yf 彙總為主, 上述差異屬於樣本與日期口徑不同。

## Retail social

- Reddit r/wallstreetbets 與 r/stocks 搜尋: DATA_UNAVAILABLE。WebFetch 被拒 (無法連線 www.reddit.com), 無法取得貼文樣本、分數、留言數。
- StockTwits: DATA_UNAVAILABLE。api.stocktwits.com 解析失敗 (DNS, 不在本 session 允許網域內), 需於 session 網路設定中允許該網域後才能重試。
- X: 本次未取得可核實的 X 貼文資料。
- 第三方二手資料 (可信度低, 僅供參考):
  - 247wallst CEG 頁面列出 Reddit 社群分析讀數為 78% 偏多, 但標示「活躍度低」(activity score 27/100), 且未說明資料來源方法。
  - TipRanks 將 CEG 投資人情緒評為 Very Positive, 依據約 821,449 位投資人於近一季的活動。此為綜合投資人活動, 並非 Reddit 專屬, 不可直接視為散戶社群情緒。
- 討論量 (buzz volume) 相對平常水準: DATA_UNAVAILABLE。未能取得提及次數統計。
- 散戶傾向: 以目前可得資料僅能判斷為偏多 (低信心), 無法細分主題。
- 主要題材 (推測自新聞聚合, 非社群貼文直接統計): 核能與資料中心電力需求、目標價調整、股價相對 52 週與短期均線的壓力 (mid-Oct 快照顯示股價低於主要均線)。此部分屬推論, 未經社群原文驗證。

## Insider activity

視窗: 2026-04-28 至 2026-10-28 (6 個月)。

| 日期 | 人員 | 職位 | 類型 | 股數 | 金額 (USD M) | 性質 |
|---|---|---|---|---|---|---|
| 2026-08-11 | CRANDALL ROGER W | Director | 公開市場買入 @ $278.62 | 1,500 | 0.42 | 公開市場買入 |
| 2026-08-04 | CRANDALL ROGER W | Director | 股票授予 @ $267.25 | 462 | 0.12 | 授予 (非買入) |
| 2026-04-28 | 10 位獨立董事 (各 556 股) | Director | 股票授予 @ $305.71 | 5,560 合計 | 1.70 合計 | 授予 (非買入) |

- 6 個月公開市場買入合計: $0.42M (1 筆, Crandall)。
- 6 個月公開市場賣出合計: $0.00M (視窗內無 Sale 紀錄)。
- 淨額: 約 +$0.42M (買方淨流入)。
- 未計入淨額之授予: 約 $1.82M (董事授予 $1.70M + Crandall 授予 $0.12M), 屬薪酬性質。
- 高階管理層 (CEO/CFO) 於 2026-02-09 與 2026-02-27 有持股變動紀錄 (Joseph Dominguez CEO 191,817 股; Daniel Eggers CFO 44,601 股等), 但 yf 未提供金額與交易性質, 且超出 6 個月視窗, 未納入淨額。
- 解讀: 視窗內唯一公開市場交易為獨立董事買入, 金額小 (約 $0.4M), 無 CEO/CFO 近期公開市場買入紀錄。此為中性偏多的訊號, 強度有限。

## Ownership shifts

- 機構持股比例: 82.94%; 機構持股 (float 基礎) 83.21%; 機構數量 2,477。
- 內部人持股比例: 0.34%。
- 持股趨勢 (季度對比): DATA_UNAVAILABLE。yf 僅提供當前快照, 未提供歷史持股變化。

## Net sentiment score

**綜合: 偏多 (bullish), 信心: 中等偏低**

- 分析師面 (權重高, 信心中高): 21 buy / 4 hold / 0 sell, 近三個月買入評級增加, 無賣出評級。但 Mizuho 維持 Neutral, UBS 與 Barclays 近期下修目標價, 且各來源計數不一致。
- 內部人面 (權重中, 信心中): 6 個月唯一公開市場交易為獨立董事買入 $0.42M, 無賣出。
- 散戶面 (權重低, 信心低): 無原始社群資料 (Reddit/StockTwits DATA_UNAVAILABLE)。第三方指標偏多, 但活躍度低, 不具代表性。
- 機構面: 持股比例高且穩定, 但無趨勢數據可判斷加減碼方向。

**Divergence flag: 無法判定 (DATA_UNAVAILABLE)**
散戶傾向無可靠資料, 因此無法判斷散戶與分析師是否背離。目前分析師與內部人方向一致偏多, 若日後取得 Reddit 或 StockTwits 資料, 須優先檢查散戶是否明顯偏空, 以確認是否出現背離。

## Data gaps summary

- Reddit (r/wallstreetbets, r/stocks): 無法連線, DATA_UNAVAILABLE
- StockTwits: DNS 解析失敗, DATA_UNAVAILABLE
- 逐筆分析師評級變動 (upgrade/downgrade 日期): DATA_UNAVAILABLE
- 社群提及次數與相對平常水準: DATA_UNAVAILABLE
- 機構持股歷史趨勢: DATA_UNAVAILABLE
- 來源間目標價與分析師人數互相矛盾, 已以 yf 為主並標註

SENTIMENT REPORT COMPLETE
