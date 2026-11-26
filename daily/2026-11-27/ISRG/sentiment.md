# Sentiment — ISRG (Intuitive Surgical) as of 2026-11-27

注意事項: 價格與估值欄位來自 pricefeed 快取 (source: cache)，最新內部人交易日為 2026-11-20。Reddit / StockTwits 直連遭封鎖，社群資料僅能以 WebSearch 取得的第三方快照代替。

## Analyst consensus

資料來源: pipeline/tools/yf rec_summary (0m) 與 info。

| 評級 | 家數 | 佔比 |
|---|---|---|
| Strong Buy | 7 | 20% |
| Buy | 20 | 57% |
| Hold | 7 | 20% |
| Sell | 1 | 3% |
| Strong Sell | 0 | 0% |
| 合計 | 35 | 100% |

- 買方合計 27 家 (77%)，持有 7 家，賣方 1 家。
- 注意: info 的 numberOfAnalystOpinions 為 31，與 rec_summary 合計 35 不一致，兩者口徑 (期間或是否計入 Strong Buy) 未能確認，以 35 為主要值。

趨勢 (rec_summary 過去 3 個月):

| 期間 | Buy 含 Strong Buy | Hold | Sell 含 Strong Sell |
|---|---|---|---|
| -3m | 24 | 8 | 1 |
| -2m | 24 | 7 | 1 |
| -1m | 26 | 6 | 2 |
| 0m | 27 | 7 | 1 |

買方家數近一月回升 3 家，持有家數略有波動，整體評級未見明顯下調。

目標價 (info, 價格 427.18 USD):

| 指標 | 目標價 (USD) | 相對現價 |
|---|---|---|
| 平均 | 487.72 | +14.2% |
| 最高 | 685.00 | +60.4% |
| 最低 | 324.00 | -24.2% |

近期評級變動:
- yf actions 回傳空值，無法從工具確認逐筆升降評等。DATA_UNAVAILABLE (工具層)。
- WebSearch 第三方報導 (未經工具交叉驗證，僅供參考):
  - 2026-07-30 HSBC 由 Buy 調為 Hold。報導中列出的 $931 目標價明顯異常，視為資料錯誤，不採用。
  - 2026-08-12 Oppenheimer 升評 Outperform，目標 $500。
  - 2026-08-13 Citigroup 維持 Buy，目標 $500。
- 2026-11 月內未找到任何評級變動。DATA_UNAVAILABLE。

## Retail social

- Reddit: 直連 r/wallstreetbets 與 r/stocks 搜尋 JSON 被封鎖，無法取得個別討論串樣本與當期熱度。DATA_UNAVAILABLE (執行層)。第三方 AltIndex 快照顯示約每日 4 則提及、較近期均值高 53%，Reddit 情緒分數 87/100 偏多；但其最新月度數據停在 2026-08，時效不明。量能屬溫和偏高。
- StockTwits: 直連 API 未取得。WebSearch 找到的 StockTwits 文章內容對應 2024 年財報，不具時效。當期 StockTwits 情緒 DATA_UNAVAILABLE。
- X / 新聞鏈: 未能直接搜尋 X 貼文。LunarCrush 快照顯示社群正向比例介於 45% 至 90%，各快照時間戳不一致，無法定錨；其中一則 24 小時快照為 81% 正向。SentiSense 顯示 30 日情緒為「略偏多」，截至 2026-11-08，並維持平穩。
- 逐篇引述樣本: 因無法取得原始貼文，無可引用之 crowd 原文。DATA_UNAVAILABLE。
- 散戶傾向: 偏多至中性，但資料薄弱且時效參差，信心低。

主要主題 (依第三方報導整理):
1. 安全性與召回: Da Vinci 組件 Class II 自願召回報導，時間點未確認。
2. 網路安全事件: 2026-03 公司揭露 IT 系統資安事件，市場視為持續性拖累，公司稱不影響營運。
3. 中國定價調整: 中國自 11 月起的計費代碼政策與器械降價，預估 2027 年每台手術器械收入下降約 3% 至 5%。
4. 財報與和解: Q3 財報後股價盤前下跌約 7.5%，同時伴隨 $450M 反托拉斯和解。
5. 手術量放緩: 美國手術量成長放緩為空方主要論點。
6. 多方論點: 財報仍有超預期部分，分析師目標價仍有上行空間。

## Insider activity

6 個月窗口 (2026-05-27 至 2026-11-27) 內，yf insider 紀錄:
- 買進: 0 筆、$0。
- 賣出: 26 筆有金額紀錄，合計約 $27.36M (USD M 口徑)。
- 淨額: 約 -$27.36M (純賣出)。
- 衍生性證券 (選擇權) 轉換列 (Conversion of Exercise) 與對應賣出配對，未重複計入賣出金額。
- 另有 3 筆無金額紀錄 (Rosa David J 2026-06-10 與 2026-07-10，CEO 身分；Loeb Gary 與 Wadors Patricia 於 2026-10-09)，交易性質 (如稅款扣繳、贈與或其他) DATA_UNAVAILABLE，不計入。

| 內部人 | 職位 | 6 個月賣出 (USD M) | 最近一筆 |
|---|---|---|---|
| Guthart Gary S | Director | 17.65 | 2026-11-04，10,000 股，約 $457.34 |
| Widman Fredrik | Officer | 4.62 | 2026-10-30，5,448 股，約 $436.06 |
| Jeddi Iman | Officer | 2.37 | 2026-06-01，5,625 股，約 $420.55 |
| Barratt Craig H | Director | 1.04 | 2026-11-04，1,150 股，約 $460.00 |
| Brosius Mark Preston | Officer | 0.53 | 2026-11-20，92 股，約 $407–421 |
| Loeb Gary | Officer | 0.50 | 2026-11-10，400 股，約 $458.15 |
| Wadors Patricia L. | Officer | 0.48 | 2026-10-23，1,078 股，約 $443.80 |
| Ladd Amy L | Director | 0.18 | 2026-08-11，472 股，約 $379–393 |

重點:
- 最大賣方為 Director Guthart Gary S，2026-08 至 2026-11 間多次出售，最近一次 (11-04) 價位高於現價 427.18。
- 2026-11 月內兩位董事、數位高管有賣出，賣出價位集中在 430 至 460 區間。
- 賣出多為既有選擇權轉換後賣出，部分可能屬預定計畫交易，但工具無法確認 10b5-1 計畫註記。DATA_UNAVAILABLE。

## Ownership shifts

yf major_holders (快取):
- 機構持股比例 88.68%，機構家數 3,144。
- 內部人持股 0.53%。

前 6 大機構 (報告日 2026-09-30):

| 機構 | 持股比例 | 季度股數變化 |
|---|---|---|
| BlackRock | 8.53% | -1.54% |
| Vanguard | 6.67% | -0.01% |
| State Street | 4.67% | +0.69% |
| Invesco | 3.47% | +1.47% |
| T. Rowe Price | 2.87% | -11.65% |
| Geode | 2.46% | +0.09% |

- 前 6 大合計約 28.7%。
- 被動型大型機構持平，T. Rowe Price 明顯減碼，Invesco 小幅加碼。整體為輕微分化，無明顯大規模撤出。
- 注意: 工具回傳的 Value 欄位以現價 (約 427 USD) 估算，並非報告日市值。

## Net sentiment score

- 分析師: 偏多。77% 買方評級，平均目標價高於現價約 14%。
- 散戶社群: 中性偏多，資料薄弱，信心低。
- 內部人交易: 偏空訊號。6 個月淨賣出約 $27.36M，0 筆買進，且近一個月仍有董事級賣出。
- 綜合: 中性偏多 (Composite: neutral-to-bullish)，信心中低。綜合分析師與散戶訊號偏多，但內部人純賣出與召回、中國定價、手術量放緩等主題形成拖累。

Divergence flag: 否 (散戶與分析師方向大致一致，但散戶資料信心低)。內部人賣出與分析師偏多之間存在分歧，屬值得留意的訊號。

資料缺口 (DATA_UNAVAILABLE 彙整):
- Reddit 討論串樣本與當期熱度。
- StockTwits 當期情緒與留言。
- X 貼文與即時情緒。
- 2026-11 月內逐筆評級變動。
- 內部人無金額交易之性質與 10b5-1 註記。
- 工具層 yf actions 空值。
