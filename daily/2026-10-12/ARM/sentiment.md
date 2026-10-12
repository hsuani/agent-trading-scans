# Sentiment — ARM as of 2026-10-12

資料品質聲明: Reddit、StockTwits 無法取得 (WebFetch 被擋)，WebSearch 查無 2026-10 月的散戶討論資料。分析師與內部人資料來自 `pipeline/tools/yf` 的 repo 快取 (`prices/yf/ARM.json`，`_refreshed_at` 2026-10-12 00:47 UTC，即時 feed 因 cookie/crumb 失敗而未更新)。以下凡無來源的散戶部分皆標示為「無資料」，不推測填補。

## Analyst consensus
目前 43 位分析師: 29 buy (8 strongBuy + 21 buy) / 12 hold / 2 sell (1 sell + 1 strongSell)。Buy 佔比約 67%。

趨勢 (以 yf recommendations 快取):
- 3 個月前: 27 buy / 11 hold / 2 sell (合計 40)
- 2 個月前: 27 buy / 14 hold / 2 sell
- 目前: 29 buy / 12 hold / 2 sell
- 整體為小幅偏多，Buy 增加 2 家，hold 略降。快取無個別 upgrade/downgrade 明細，無法逐筆列出。

Recent moves (WebSearch 二手來源，未經 yf 驗證):
- 2026-07-14 HSBC 由 Buy 下調為 Hold，認為估值已反映過度炒作，當時約 288x forward earnings。
- 2026-07-30/31 UBS (目標 $320) 與 Rosenblatt (目標 $250) 維持 Buy。
- Benzinga 2026-08 快照: 27 位 Buy 共識，平均目標價 $272。此數字與 yf 的 43 家計數口徑不同，且為 8 月資料，時效有限。
- 價格對照: 最近一筆可驗證的內部人成交價為 2026-09-21 的 $300。若以 $300 計，平均目標價 $272 低於現價約 9%。這是本報告中最需注意的分歧點。

Earnings: 上次 2026-07-29 EPS 0.45 vs 預估 0.40 (+11.4%)。下次 2026-11-04 EPS 預估 0.47。

## Retail social
- Reddit (r/wallstreetbets, r/stocks): 無資料。WebFetch 被擋，WebSearch 未找到 2026-10 的 Reddit 討論串。
- StockTwits: 無資料 (被擋)。
- X / 其他社群: WebSearch 只找到 historicaloptiondata.com 的 2026-07 頁面，顯示約 60% bullish / 30% bearish / 10% neutral (07-10 與 07-22 兩頁)。此來源可信度低: 同一段文字在不同日期重複出現，且各頁引用的股價互相矛盾 (6 月約 $439、7 月約 $287-291)，判定為模板化或重複內容，不納入評分。Investing.com 有個人投資人 bull/bear 投票頁，但擷取不到當前數值。
- 聲量 (buzz volume): 無法量化，無 2026-10 的提及數資料，無法與基準比較。
- 不引用原文: 因無可驗證的原始貼文，不附 quote。

Themes (僅來自 2026-06/07 的二手摘要，非 2026-10 散戶原文):
- 看多: AI 資料中心需求、AGI/資料中心 CPU 題材 (2026-03 公告，約 $15B 年營收目標，Meta 為早期客戶，MarketBeat 報導)。
- 看空: 估值過高 (HSBC 的核心論點)、關稅與 pullback 風險。
- 價格走勢 (內部人成交價推估): 2026-04 約 $160，05 月中至 06 月初升至約 $390-415，8 月約 $255，9 月 21 日約 $300。6 月後明顯回落。

## Insider activity
區間: 2026-04-12 至 2026-10-12 (6 個月)。
- 買入 (open market): 0 筆。
- 賣出 (有價格的 Sale 紀錄): 合計約 $63.9M，共 17 筆。
- Net 6mo: $0 buys / 約 $63.9M sells。
- 另有 Stock Award/Grant (如 CEO Haas 2026-05-15 約 265,643 股，價格 0，屬授予而非買入) 與 Gift 紀錄，未計入買賣金額。
- 2026-05-15 有多筆無價格的 Form 4 項目 (約為歸屬或代扣稅)，無法確認性質，未計入。

依人員 (賣出金額，約值):
- COLLINS Spencer (Officer): ~$19.8M (2 筆，05-11 與 05-19)
- CHILD Jason E (CFO): ~$16.8M (4 筆，04-22、05-20、08-27、09-21；最近一筆 09-21 約 10,400 股，$300)
- ABBEY William (Officer): ~$16.5M (7 筆，05-15 至 06-02)
- GRISENTHWAITE Richard (Officer): ~$5.1M (1 筆，05-18)
- EATON Charlotte Claire (Officer): ~$4.2M (2 筆，05-21)
- HAAS Rene A (CEO): ~$1.5M (1 筆，04-14)；另有 03-26 約 $5.1M 的賣出在 6 個月窗口之外，不計入。

Notable: CFO Child 為窗口內持續賣出、金額最大的單一主管之一，最近一筆在 9/21。CEO 在窗口內只有一筆小額賣出 (另有 5/15 的 award)。窗口內沒有任何 open-market 買入。

## Ownership shifts
- 機構持股 96.26%，機構數 1,318 家；內部人持股僅 0.07%。
- 前十大機構 (2026-06-30 申報): Invesco 12.8M 股 (1.2%)、DZ Bank 6.5M、Capital World 4.3M、Arrowstreet 4.1M、FMR 4.1M、Goldman Sachs 2.9M、Van Eck 2.6M、Capital Research 2.4M、Morgan Stanley 2.2M、Capital International 2.1M。
- pctChange 欄位單位未確認，僅能描述方向: 前十大中多數為正值 (Invesco、Capital World、Arrowstreet、FMR、Goldman、Van Eck、Capital International)，DZ Bank、Capital Research、Morgan Stanley 為負值。整體看不出明顯的集中或撤離趨勢，只能說法人持股仍高、近一季增減分歧。
- 注意: 快取 holder 資料為 2026-06-30 申報，非 10-12 當期。

## Net sentiment score
Composite: **中性 (neutral)**，信心 **低**。

分項:
- 分析師: 偏多 (29/43 buy，目標價共識 $272 低於最後可驗證現價 $300)。
- 內部人: 偏空 (6 個月約 $63.9M 賣出，0 筆買入，CFO 與多位主管持續減碼)。
- 散戶: 無可靠資料，不評分。唯一的量化來源 (historicaloptiondata) 不可信。
- 估值面 (二手來源): HSBC 認為估值過高，已降評。

Divergence flag: **是 (部分)**。分析師偏多，內部人持續賣出，兩者方向不一致。但缺少 10 月的散戶資料，無法確認散戶是否與分析師相反，因此無法確定是否為散戶 vs 分析師的分歧。

資料缺口 (建議補充):
1. 即時 yf 資料 (cookie/crumb 失敗，目前為 10-12 之前的快取)。
2. Reddit / StockTwits 當期提及數與情緒 (需要可連線的來源)。
3. 2026-10 的 ARM 股價與目標價更新 (目前的最後可驗證價格為 9/21 的 $300)。

Sources (WebSearch 二手資料):
- https://simplywall.st/community/narratives/us/semiconductors/nasdaq-arm/arm-holdings/dqgcwlk1-ai-data-centers-and-iot-will-transform-markets-3jyt/updates/12-analysts-remain-divided-on-arm-holdings-with-bulls-citing-s
- https://www.barchart.com/story/news/3282839/this-analyst-just-downgraded-arm-stock-here-s-why
- https://es.benzinga.com/quote/ARM/sentiment
- https://www.marketbeat.com/instant-alerts/arm-nasdaqarm-ceo-rene-haas-sells-23867-shares-2026-03-28/
- https://historicaloptiondata.com/?p=69981 (低可信度，僅供參考)
- https://247wallst.com/investing/2026/06/23/arm-stock-is-up-235-in-2026-is-todays-10-drawdown-a-take-profits-signal/

SENTIMENT REPORT COMPLETE
