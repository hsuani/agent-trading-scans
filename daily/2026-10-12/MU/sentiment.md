# Sentiment — MU as of 2026-10-12

資料品質說明: 分析師評等與內部人交易來自 pipeline/tools/yf (live feed 失敗後使用 repo cache)。Reddit、StockTwits 與財經網站無法直接抓取, 散戶情緒僅能由 WebSearch 的二手摘要推估, 信心偏低。股價數據來源互相矛盾 (約 $1,064 vs 約 $777), 本報告不以價格做判斷。

## Analyst consensus
目前 (0m) 共 49 位分析師: 9 Strong Buy / 36 Buy / 3 Hold / 0 Sell / 1 Strong Sell。買方佔比約 92% (45/49)。

近 4 期趨勢 (yf rec_summary, 0m 對比 -3m):
- 買方 (Strong Buy + Buy) 由 40 增至 45, 增加 5 家
- Hold 由 5 降至 3
- Strong Sell 由 0 增至 1 (出現在 -1m 之後, 目前維持 1 家)

升降評等明細: yf recommendations 只回傳彙總計數, 無個別 upgrade/downgrade 紀錄, 無法列出個別券商動作。

目標價 (WebSearch 二手來源, 未能逐一核對原始研報):
- Susquehanna 維持 Positive, 目標價 $2,000 (10 月初報導)
- Morgan Stanley 維持 Overweight, 目標價 $1,200 (10 月初報導)
- 共識目標價來源不一: 7 月 MarketBeat 快照為 $1,268.93 (37 家); 較新摘要為 $1,581.40 (Strong Buy)
- Susquehanna 預期 11 月季度毛利率短暫收縮, 之後再擴張

## Retail social
- Reddit (r/wallstreetbets, r/stocks): 直接 search.json 抓取被封鎖, 無法取得 thread 樣本。二手摘要 (Yahoo 文章, 日期不明) 指 WSB 情緒分數介於 88 至 94, 偏多頭。無法確認是否為 10 月數據。
- StockTwits: 未能取得資料 (未嘗試直接呼叫, 依規定以 WebSearch 為主)。
- LunarCrush 快照: 一份顯示 24h 正面情緒 93%, 另一份 74%, 兩者皆無明確日期, 無法判斷哪份較新。
- X / 新聞: 10 月 2026 的近期討論未搜尋到。WebSearch 結果多為 5 月與 1 月文章的轉載內容, 多屬低品質內容農場。
- 提及量 (buzz volume): 無可靠的量化數字。定性判斷為 "無法評估", 僅能確認 2026 年初與中期曾有明顯升溫。
- Retail tilt: 二手來源一致偏多 (bullish), 但時間戳記不足, 可信度低。
- 空方聲音: 5 月 Mikhail Fedorov 評論認為應 "take your foot off the gas" (減速); 另有估值過高的警告。
- 主要主題:
  - 多方: 創紀錄財年營收 (FY2026 約 $133.2B, 年增 256%); 最新季 EPS $25.11 高於共識 $21.39; AI 與記憶體需求復甦; 目標價持續上修
  - 空方: 記憶體定價循環風險; AI 資本支出可持續性; 中國競爭; 內部人大額賣股; 估值已大幅上漲
- 無直接 post 樣本可引用。

## Insider activity
統計區間: 2026-04-12 至 2026-10-12 (6 個月)。
- 公開市場買入 (Purchase): 0 筆, $0
- 公開市場賣出 (Sale): 16 筆, 約 $249.2M
- 非現金交易: 3 筆 (2026-06-30 Liu Teyin Mark 股票獎勵 27 股; Dugle Lynn A 贈與 700 股; 2026-06-09 Bjorlin Alexis 股票獎勵 63 股)
- 淨額: 約 -$249.2M (淨賣出)

主要賣方 (金額):
- Mehrotra Sanjay (CEO): 約 $182.3M, 8 筆 (2026-05-01 至 2026-08-21), 最近一筆 2026-08-21, 40,000 股, 價格約 $959–990
- Arnzen April S (Officer): 約 $43.4M, 2026-07-01, 40,000 股, 價格約 $1,077–1,096
- Sadana Sumit (Officer): 約 $14.0M, 2026-08-18, 15,000 股, 價格約 $934
- Ray Michael Charles (Officer): 約 $4.1M, 2026-05-01
- 其餘: Gomo Steven J (Director, 約 $1.6M)、Dugle Lynn A (Director, 約 $1.5M)、Cordano Michael D (Officer, 約 $1.5M)、Allen Scott R (Officer, 約 $0.9M)、Bjorlin Alexis (Director, 約 $28K)

重點解讀: CEO 持續賣出, 且集中在股價高點區間 ($500 至 $1,190), 在期間內無任何公開市場買入。部分賣出可能屬於 10b5-1 預定計畫或稅務相關安排, 但資料中無法驗證計畫類型, 因此僅記錄為事實, 不推定動機。

## Ownership shifts
- 機構持股比例 (insidersPercentHeld 0.24%, institutionsPercentHeld 79.7%)
- 機構數目: 5,005
- 只有單一時點快照, 無法判斷集中度趨勢 (增減持) 。

## Net sentiment score
Composite: **偏多 (bullish), 信心中低 (medium-low)**

判斷依據:
- 分析師面 (權重最高, 信心中高): 92% 買方評等, 買方家數近期增加, Hold 減少。偏多。
- 散戶面 (信心低): 二手來源一致偏多, 但時間戳記不可靠, 無提及量數據。偏多但不可靠。
- 內部人面 (信心中): 6 個月內 $249M 淨賣出, 0 筆公開買入, 大額賣出集中在 CEO。偏空訊號, 但可能含預定計畫因素。

Divergence flag: **否** (散戶與分析師同為偏多方向, 且散戶資料可信度低)。
次要分歧: **是** — 內部人淨賣出方向與分析師偏多方向相反, 值得後續追蹤 (Form 4 交易計畫揭露與後續買入是否出現)。

資料缺口 (需於後續補強):
1. Reddit / StockTwits 直接數據無法取得, 提及量無量化數字
2. 2026-10 近期的 X / 新聞情緒未搜尋到
3. 個別分析師 upgrade/downgrade 紀錄未提供
4. 股價來源矛盾, 目標價共識來源不一致
5. 機構持股僅單一快照, 無趨勢

SENTIMENT REPORT COMPLETE
