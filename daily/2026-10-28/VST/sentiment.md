# Sentiment — VST as of 2026-10-28

## Analyst consensus

資料來源: `pipeline/tools/yf VST rec_summary` (0m 期間), 與 `recommendations` 回傳相同 (僅為彙總, 無逐筆升降評等紀錄)。

| 評等 | 本期 (0m) | 前一期 (-1m) | -2m | -3m |
|---|---|---|---|---|
| Strong Buy | 4 | 4 | 4 | 4 |
| Buy | 18 | 15 | 15 | 15 |
| Hold | 0 | 0 | 0 | 0 |
| Sell | 0 | 0 | 0 | 0 |
| Strong Sell | 1 | 1 | 1 | 1 |
| 合計 | 23 | 20 | 20 | 20 |

結論: 23 家中 22 家為買入側 (Strong Buy + Buy), 0 家 Hold, 1 家方向相反 (Strong Sell)。即 22 買 / 0 持有 / 1 賣。

近期變化: 本期買入側由 19 增至 22 (Buy 由 15 增至 18), 為最近一個月唯一明顯變動。yf 未回傳逐筆升降評等與目標價變動明細, 故升降評等明細與目標價歷史 = DATA_UNAVAILABLE。

外部來源目標價 (非 yf, 日期不一, 僅供參考):
- MarketBeat (8 月): 共識 Buy, 平均目標價 $228.50。
- TIKR (10 月): 平均目標價 $210.10, 約高於收盤 38%。
- BMO Capital 於 10/5 將目標價由 $231 調降至 $210 (來源: WebSearch 彙整之 TIKR 文章)。
- 247 Wall St (9 月): 共識目標價 $217.42。

與 yf 數字不一致之處: Barchart 報 16 Strong Buy / 1 Hold, yf 報 4 Strong Buy / 18 Buy / 1 Strong Sell / 0 Hold。兩者分類與家數不同, 以 yf 為主, 差異列為待核對。

## Retail social

- Reddit (r/wallstreetbets, r/stocks): DATA_UNAVAILABLE。WebFetch 被拒 ("unable to fetch from www.reddit.com"), 無法取得貼文樣本、分數、留言數與情緒傾向。
- StockTwits: DATA_UNAVAILABLE。`api.stocktwits.com` DNS 解析失敗 (ENOTFOUND), 需於 session 網路設定中允許該網域後才能重試。本次未重試。
- X / 新聞評論: WebSearch 未找到可信的 X 貼文樣本。以下為相關結果:
  - LunarCrush 顯示社群情緒偏高, 但為較早期快照, 日期不明。
  - Equibles 綜合評等 Neutral, 技術面 Sell, 聰明錢 (smart money) Bullish, 6 個月報酬約 -19%。
  - Benzinga 短期利率 (short interest) 3.6% 且上升 (日期不明)。
  - Stockanalysis 標示 VST 出現偏空期權流 (6,926 張 put, 約 3 倍預期量), 日期不明。
- 聲量 (buzz volume): DATA_UNAVAILABLE。無可量化的提及次數, 無法與平常基準比較。
- 散戶傾向: 無可直接量測之資料。僅能從新聞與社群摘要判斷為「社群熱度偏高、價格面偏弱」, 信心低。

主要主題 (取自次級來源, 非散戶原文):
- 資料中心電力需求推動長期發電前景 (bullish 主軸)。
- ERCOT 電價走弱與 2027 指引疑慮 (bearish 主軸), 多篇文章提到 2027 指引可能尚未觸底。
- 股價自 2026 年高點回落, 一年跌幅約 25%–28%, 市場關注 11/6 第三季財報 (未來事件, 截至 10/28 尚未發生)。
- 執行長於 9 月小額買入, 被部分文章解讀為信心訊號。

## Insider activity

計算區間: 2026-04-28 至 2026-10-28 (6 個月)。來源: `pipeline/tools/yf VST insider`, 幣別 USD。

- 買入: 約 $1.2M (1,173,069 USD)。全部為 CEO James A. Burke, 9/1 買入 6,665 股 (約 $0.90M, 均價約 $135.5), 8/24 買入 2,000 股 ($0.27M, $135)。
- 賣出: 約 $25.9M (25,878,803 USD), 共 10 筆。
  - Scott A. Hudson (Officer): 10/6 賣出 22,222 股 ($3.56M), 9/8 賣出 44,444 股 ($6.75M), 合計 $10.3M。
  - Kristopher E. Moldovan (CFO): 10/7 賣出 20,000 股 ($3.30M), 9/8 賣出 20,000 股 ($3.02M), 合計 $6.3M。
  - 董事: Scott B. Helm 6/16 賣出 25,000 股 ($4.0M); Arcilia C. Acosta 6/18 賣出 15,000 股 ($2.51M); John R. Sult 6/18 賣出 6,500 股 ($1.1M); Paul M. Barbas 6/15 賣出 488 股 ($0.07M)。董事合計約 $7.7M。
  - Margaret M. Montemayor (Officer): 5/27 與 6/2 合計 $1.56M (此兩筆於 6 個月窗口內, 5/27 落於 4/28 之後)。
- 淨額: 約 -$24.7M (淨賣出)。
- 注意: 持續性 (例如 10b5-1 計畫) 無法由資料判斷, 標示為 DATA_UNAVAILABLE。賣出價約 $150–$165, 買入價約 $135。
- 2026-05 與 2026-02/03 之董事與高階主管股票獎勵屬授予 (Grant), 非市場交易, 未計入淨額。

最值得注意的訊號: CEO 小額逢低買入 (約 $1.2M), 與 CFO / 高階主管 / 董事於 6–10 月間的大額賣出形成對照。

## Ownership

來源: `pipeline/tools/yf VST major_holders`。
- 內部人持股比例: 0.77%。
- 機構持股比例: 92.4%, 流通股機構持股: 93.1%。
- 機構家數: 1,895。
- 機構持股趨勢 (季度變化): DATA_UNAVAILABLE (僅有當期快照, 無歷史比較)。

## Net sentiment score

- 分析師: 偏多 (22/23 買入側, 高信心)。
- 內部人: 偏空 (6 個月淨賣出約 $24.7M, 且以高階主管與董事為主; CEO 為唯一淨買方, 高信心但樣本少)。
- 散戶: 無法評估 (Reddit / StockTwits 皆為 DATA_UNAVAILABLE; 次級來源呈現社群熱度偏高但價格面偏弱, 信心低)。
- 綜合評分: 中性偏多 (neutral-to-bullish), 信心中等。分析師評等強烈偏多, 但內部人淨賣出與股價弱勢抵消部分正面訊號; 散戶面缺資料。

Divergence flag: 部分 (partial)。
- 分析師 (偏多) 與內部人 (淨賣出) 方向相反, 此為本報告最主要的分歧。
- 散戶面無資料, 無法判斷散戶與分析師是否背離 (flag 無法判定)。
- 聰明錢指標 (Equibles) 偏多而技術面偏空, 亦屬於內部分歧。

## 資料缺口 (DATA_UNAVAILABLE 彙整)
1. Reddit r/wallstreetbets 與 r/stocks 貼文 (WebFetch 被拒)。
2. StockTwits 訊息流 (DNS 失敗, 需網路白名單)。
3. 逐筆升降評等與目標價歷史 (yf `recommendations` 僅回傳彙總)。
4. 機構持股季度變化趨勢 (僅有當期快照)。
5. 散戶提及次數 / 聲量基準。
6. 內部人交易是否為 10b5-1 計畫。
7. 部分次級來源 (MarketBeat, Barchart, LunarCrush) 日期不明或早於 10/28, 僅作參考。

SENTIMENT REPORT COMPLETE
