# Sentiment — MRVL as of 2026-10-12

資料來源說明: 分析師評級、內部人交易與機構持股來自 pipeline/tools/yf 的 repo 快取 (prices/yf/MRVL.json, 快取刷新時間 2026-10-12 00:49 UTC)。Yahoo 即時來源被 proxy 阻擋, 屬預期情況。Reddit、StockTwits 直接抓取被擋, 改以 WebSearch 取得間接資料, 下列零售端結論信心偏低。

## Analyst consensus
目前 46 位評級中 42 buy (9 strongBuy + 33 buy) / 4 hold / 0 sell。快取 info 欄位記為 44 位分析師, 兩者略有差異, 以 rec_summary 為準。

近四個月趨勢 (0m / -1m / -2m / -3m):
- Buy (含 strongBuy): 42 / 40 / 39 / 38
- Hold: 4 / 6 / 5 / 5
- Sell: 0 / 0 / 0 / 0

評價趨勢是買進數緩升、持有數減少, 沒有任何賣出評級。

目標價 (快取 info): 平均 $337.99、中位數 $350、最高 $450、最低 $210。快取現價 $275.28, 距平均目標價約 +23%, 距中位數約 +27%。52 週高點 $329.88, 低點 $70.69。

近期調整 (WebSearch 所得, 日期不完整, 需以券商原文確認):
- Oppenheimer 將目標價由 $300 上調至 $325。
- 另有一家券商維持 $340 目標價, Needham 與 Rosenblatt 均提及 $300 目標價。
- 快取的 recommendations 欄位只有評級分布, 沒有逐筆升降級紀錄, 無法列出具體 upgrade/downgrade 日期。

財報與事件: 上次財報 2026-08-27, EPS 0.94 vs 預估 0.93 (小幅超預期)。快取列出的下次財報日為 2026-12-01 (預估 EPS $1.10)。Investor Day 原定 2026-10-06, 來源僅提及 "預期" 內容 (custom silicon 多年展望), 實際結果未在資料中確認。

## Retail social
- Reddit: 本次 WebSearch 未取得 r/wallstreetbets 或 r/stocks 上 MRVL 的實際貼文, 無法引用樣本或計算提及量。此來源為空白, 不以推測補上。
- StockTwits / X: StockTwits 情緒頁面僅抓到儀表板標題, 未取得多空比例, 快照日期 (顯示 8/27 財報與 $210.70 股價) 明顯過時。
  - 一則 StockTwits 標題將多空情境框為 "$385 Bull Case vs $110 Bear Case" (日期不明)。
  - 一份 TipRanks 摘要稱 MRVL 與同業的投資人情緒 "明顯轉負", 但該摘要日期較早, 僅供參考。
- 聚合情緒指標 (WebSearch 所得, 來源品質不一):
  - Google Finance 快照 (10/5): Outlook 54.7% bullish / 1.6% bearish。注意這個數字的基礎與樣本量未知。
  - NAGA 頁面: 公開情緒分數為 NEGATIVE, 但分析師共識為 buy。
  - 8/27 選擇權統計: 成交金額 71.8% call / 28.2% put, 偏多。8/10 同類統計為 60% bullish。
- Themes (由來源摘要歸納, 非直接引用貼文):
  - AI 加速器 / custom silicon 成長是多方主要論點。
  - 估值是空方主要論點: P/E 約 89.5 (trailing)、forward P/E 約 37.8。
  - 股價 YTD 漲幅大 (來源說法不一, 介於約 160% 至 251% 之間), 追高風險被反覆提及。
  - 一則技術面摘要稱 STOCH 偏超賣、RSI 中性, 但單一來源, 可信度低。
- Stockscan 所列 2027 平均目標價 $147.33 與其他來源嚴重不符, 判斷為離群資料, 不採信。
- 零售聲量: 無可靠的提及次數數據, 無法與平時比較。僅能定性地說, 近期新聞與分析師報導密度高, 屬於關注度高的狀態。

## Insider activity
Net 6mo (2026-04-12 至 2026-10-12, 依快取 insider 交易紀錄計算): **$0 買進 / 約 $35.8M 賣出** (17 筆有價格的賣出交易)。以 "Sale at price" 欄位的價格 × 股數估算, 屬近似值。

主要賣方:
- CEO Matthew Joseph Murphy: 6 月至 9 月每月約 7,500 股, 最近一筆 2026-09-15 約 $1.68M (@ $223.39)。
- President Christopher R. Koopmans: 6 月至 9 月每月約 10,000 股, 最近一筆 2026-09-01 約 $2.03M (@ $203.27)。
- CFO Daniel James Durn: 2026-06-23 賣出 2,250 股 (約 $0.63M)。9/15 另有一筆 6,469 股紀錄, 但無價格欄位, 性質不明。
- Officer Sandeep Bharathi: 2026-04-16 賣出 66,892 股 (約 $8.7M), 7 月與 6 月另有賣出。
- CFO Willem A. Meintjes: 2026-04-15 賣出 30,000 股 (約 $4.0M)。
- Director 方面: 6/10 至 6/25 多筆 3,940 股 (無價格欄位) 與股票贈與, 性質多半為董事酬勞, 非市場買賣。

注意事項:
- 快取中沒有任何 open-market purchase 紀錄。
- 多位高層的定期出售 (CEO、President) 可能屬於 10b5-1 計畫, 但快取資料沒有此欄位, 無法確認。
- 部分紀錄無價格欄位 (如 4/15、7/15 批次交易), 較可能是稅務代扣或歸屬相關交易, 不應直接視為市場出售, 本報告未計入淨額。

## Ownership shifts
- 機構持股比例 81.8% (2,931 家機構), 內部人持股 0.49%。
- 前幾大機構 (截至 2026-06-30 季報, pctChange 為該季股數變化):
  - BlackRock 9.77%, +34%
  - Vanguard Capital Management 6.6%, +48%
  - FMR 6.49%, -57% (明顯減碼)
  - State Street 4.77%, +79%
  - Invesco 3.45%, +5%
  - Geode 2.41%, +68%
  - Vanguard Portfolio Management 2.4%, -37%
  - Goldman Sachs 1.68%, +31%
  - Norges Bank 1.62%, +35%
  - JPMorgan 1.58%, +139%
- 整體看, 指數與被動型機構持續加碼, 主動型大型基金 (以 FMR 為代表) 有減碼跡象。資料為單一季度快照, 趨勢判斷信心中等。

## Net sentiment score
Composite: **偏多 (bullish), 信心中等**。

- 分析師端: 強烈偏多。42/46 buy, 0 sell, 平均目標價高於現價約 23%, 評級分布近期持續改善。信心高。
- 零售端: 混合偏多至中性。聚合指標與選擇權資料偏多, 但 NAGA 公開情緒分數為負、TipRanks 摘要指出情緒轉負, 且 Reddit 與 StockTwits 無可用資料。信心低。
- 內部人端: 偏空。6 個月 $35.8M 賣出, 0 買進, 且 CEO 與 President 持續定期出售。若為 10b5-1 計畫則訊號強度降低, 但快取無法確認。信心中等。

Divergence flag: **是 (部分)**。
- 分析師與內部人方向相反: 分析師強烈偏多, 內部人淨賣出, 這是需要注意的分歧。
- 零售與分析師方向大致一致 (偏多), 但零售端證據薄弱, 不宜據此判定分歧。
- 機構層面: 被動型加碼、主動型 FMR 減碼, 方向亦有分歧。

本報告為情緒盤點, 不含交易建議。

## 資料限制
1. Reddit 與 StockTwits 直接資料未取得, 零售端結論來自二手摘要與日期不明的網頁, 不能視為穩定訊號。
2. 快取現價 $275.28 與多個網頁引用的價格 (約 $271 至 $276) 接近但不完全一致, 日期亦不同, 使用前應以即時報價確認。
3. 來源間的分析師人數 (44 vs 46)、YTD 漲幅、目標價存在不一致, 已在上文註明採用的數字。
4. 內部人淨額為依快取欄位估算的近似值, 未扣除 10b5-1 或稅務代扣等性質區分。

SENTIMENT REPORT COMPLETE
