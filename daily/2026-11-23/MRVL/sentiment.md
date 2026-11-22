# Sentiment — MRVL as of 2026-11-23

資料基準: 價格與分析師數據取自 repo 快取 prices/yf/MRVL.json (2026-11-22 14:31 UTC 更新), 收盤參考價 USD 122.28。Yahoo 直連 cookie/crumb 失敗但工具回傳正常資料。Reddit / StockTwits / nasdaq.com 依規定未直接抓取, 散戶面以 WebSearch 結果的新聞與二手摘要為準。

## Analyst consensus
目前 (0m) 43 位分析師: 7 strong buy / 31 buy / 5 hold / 0 sell / 0 strong sell, 即 38 買進、5 持有、0 賣出。買進側比 1 個月前 (-1m, 47 位: 8 / 35 / 4) 少 5 家, 持有側僅多 1 家, 其餘可能是移出評等或停止更新, 工具未提供個別升降級明細。快取內 numberOfAnalystOpinions 為 40, 與 rec_summary 的 43 不同, 屬口徑差異, 以 rec_summary 為準。

近期變動: 依 WebSearch 新聞, 11/2 公告以全股票方式收購 Lumentum (二手來源, 未核對原公告); 11/3 TD Cowen 由 Buy 降為 Hold, 目標價由 USD 350 砍至 USD 175。快取內 targetLowPrice = USD 175 與此相符。

目標價 (USD): 平均 309.14 / 中位數 300 / 最高 450 / 最低 175。以現價 122.28 計, 平均目標價隱含約 +153% 空間。目標價多數可能尚未反映交易結構改變後的調整, 屬於讀數時應保留的疑慮。

## Retail social
- Reddit: 本次無法直接取得 (WebSearch 未回傳任何 Reddit 討論串), 無法計算提及量或討論串傾向。資料缺口, 不以推測補足。
- StockTwits / X / 新聞: StockTwits 相關報導顯示 11 月急跌期間散戶仍有逢低買入聲音, 有留言認為 20-30% 反彈 "easy" (二手摘要的改寫, 非原文)。另一則報導指出過去某段時間 MRVL 散戶情緒曾 "extremely bullish" (時間不明, 偏舊)。11/11 一度因 AI 資料中心放緩政策消息反彈。整體傾向: 逢低接刀與觀望並存, 偏分歧。
- 量能: 無直接計數。以新聞密度判斷, 11 月 2 日起的收購與降評事件使討論量明顯高於平常, 屬質性判斷, 不是計量結果。
- Themes:
  1. Lumentum 全股票收購的稀釋與結構疑慮 (主要負面題材)
  2. AI 資料中心需求與 hyperscaler 關係 (正面長期敘事, 分歧所在)
  3. 估值: 股價自 52 週高點 USD 329.88 回落至 122.28, 跌幅約 63%, 出現 "估值便宜" 與 "趨勢轉弱" 兩派
  4. 內部人持續出脫 (6 個月內持續被提及)
  5. 12/1 財報前的事件風險

## Insider activity
Net 6mo (2026-05-23 至 2026-11-22, 計價交易): 買進 USD 0 / 賣出 USD 19.98M, 淨賣 USD 19.98M。另有 15 筆無價格紀錄 (多為稅款代扣或歸屬類申報), 未計入金額。

| 內部人 | 職稱 | 6mo 賣出 (USD M) | 備註 |
|---|---|---|---|
| Koopmans, Christopher R | President | 8.53 | 間接持有 (I), 約每月 1 萬股 |
| Murphy, Matthew Joseph | CEO | 8.36 | 直接持有 (D), 約每月 7,500 股 |
| Bharathi, Sandeep | Officer | 2.46 | 7/16 與 6/16 兩筆 |
| Durn, Daniel James | CFO | 0.63 | 6/23 |

Notable:
- 11/16 Murphy (CEO) 賣出 7,500 股 @ USD 146.54, 金額 USD 1.10M (近期最新一筆)
- 11/2 Koopmans (President) 賣出 10,000 股 @ USD 186.97, 金額 USD 1.87M
- 7/1 Koopmans 賣出 10,000 股 @ USD 281.92, 金額 USD 2.82M (6mo 內單筆最大)
- 賣出價格區間從 USD 281.92 下滑到 146.54, 內部人在股價下跌過程中仍持續賣出。
- 形式觀察: CEO 與 President 的賣出股數固定、頻率接近每月一次, 形似預先排程的交易計畫 (10b5-1 類型), 但本資料不能確認。
- 6 個月內無公開市場買進。最近一次買進為 2025-09-25 (USD 77.09–78.03 區間, CEO、President、CFO 與 Officer 同日買入), 距今超過一年。

## Ownership shifts
- 機構持股 80.8% (流通股 81.2%), 機構數約 3,100 家; 內部人持股 0.53%。
- 截至 2026-09-30 前幾大持股: BlackRock 9.96% (季增 +2.0%), Vanguard 6.53% (-1.1%), State Street 4.75% (-0.5%), FMR 4.50% (-30.8%, 大幅減碼), Invesco 3.84% (+11.2%), Geode 2.47% (+2.6%)。
- 解讀: 前幾大被動與指數類持有人變動不大; FMR 大幅減持與 Invesco 加碼是主動基金側的分歧。需要更多季度資料才能判斷趨勢。

## Net sentiment score
Composite: 偏空 (neutral-to-bearish), 信心中等 (medium-low)。
- 分析師 (偏多但降溫): 38 買進 / 0 賣出, 但買進家數 6 個月內明顯收縮, 且最近一次重大降評為 Hold。
- 內部人 (偏空): 6 個月淨賣 USD 19.98M, 無公開市場買進, CEO 與 President 持續出脫。
- 散戶 (分歧, 證據不足): 新聞與 StockTwits 摘要顯示逢低買入與觀望並存, 缺乏 Reddit 與計量資料, 不宜給出確定方向。
- 價格與資金流 (背景): 股價自高點回落約 63%, 機構中 FMR 減持。

Divergence flag: 是。分析師整體仍偏多, 內部人與近期降評方向偏空, 兩者方向相反。散戶方向無法可靠判斷, 不能認定散戶與分析師相反。本份報告不提供交易建議。

資料限制:
- Reddit 無法取得, 散戶結論僅來自新聞摘要。
- 內部人 15 筆無價格交易未計入金額。
- 目標價與評等可能未完全反映 11 月收購案的後續調整。
- 收購案細節來自二手來源, 未核對原始公告。

SENTIMENT REPORT COMPLETE
