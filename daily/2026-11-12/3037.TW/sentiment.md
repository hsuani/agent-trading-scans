# Sentiment — 3037.TW (欣興) as of 2026-11-12

## Analyst consensus
目前 rec_summary 為 6 家 Strong Buy / 12 家 Buy / 1 家 Hold / 0 Sell / 0 Strong Sell（共 19 家）。買進評等占比約 95%（18/19），無賣出評等。

近四個期間（0m、-1m、-2m、-3m）分布完全相同，代表近一季評等沒有升降評等變動，屬於「高度一致、評等不變」狀態。

目標價方面：根據 WebSearch 查到的 CTEE 報導（2026-07-30），Q2 法說後數家外資維持買進並把目標價區間上調至約 NT$1,200–1,500；此為二手報導，未能用 yf 數據逐筆核對，請視為待確認資訊。

## Retail social
- Reddit（r/wallstreetbets、r/stocks）：本次抓取被封鎖（WebFetch 回報無法連線），無法取得樣本貼文與多空傾向。依規則略過。
- StockTwits：api.stocktwits.com 無法解析（DNS 失敗，session 網域未開放），本次無資料。
- X / 新聞媒體：WebSearch 結果以台灣財經媒體為主，整體偏多：
  - 10 月合併營收約 189.86 億元，年增 67.6%；前 10 月累計 1,519.72 億元，年增 40.9%（TechNews，2026-11-06）。
  - 媒體描述 ABF 載板供需缺口持續擴大、外資買盤回流（uAnalyze，2026 年 9 月）。
  - 同期亦有文章指出股價在營收創高時仍曾跌停，市場爭論是否為估值重設（uAnalyze，2026 年 9 月）。
- 聲量：無法量化 Reddit / StockTwits 提及次數，僅能以新聞能見度判斷，屬定性描述。
- 一則 MoneyWeekly 報導的營收與目標價數字與 2026 年資料不符，判定為舊文，未納入計算。

- Themes（僅能由新聞端歸納）：
  - ABF 載板供需缺口與漲價循環（多方主軸）
  - EMIB-T 基板 2027 年初期良率風險（空方疑慮）
  - HDI 業務能見度（部分券商提示風險）
  - 估值是否已反映 AI 基板需求（多空分歧點）

## Insider activity
yf insider 回傳空陣列，無法確認近 6 個月內部人買賣淨額。這是資料缺口，不代表淨買賣為 0。
Net 6mo: 資料不足（無法判定 $X buys / $Y sells）。Notable: 無可用紀錄。

## Ownership shifts
- 內部人持股比例：15.9%
- 機構持股比例：44.2%（占流通股約 52.6%）
- 機構家數：354
- 僅為單一時點快照，無法判斷近期機構集中度趨勢（需下一期資料才能比較）。

## Net sentiment score
Composite: **bullish（信心：中）**

依據：
- 分析師端高度一致偏多（18/19 買進以上，無賣出），且評等近四期未變。
- 新聞與營收數據整體偏多，營收年增率明顯。
- 扣分因素：零售社群（Reddit、StockTwits）完全無資料，內部人交易資料缺漏，無法做多源交叉驗證。因此信心只給中等。

Divergence flag: **無法判定**。缺少零售端資料，無法比較零售傾向與分析師傾向是否相反。若後續取得 Reddit 或 StockTwits 資料，需重新評估。

## Data gaps
- Reddit：WebFetch 被封鎖（r/wallstreetbets、r/stocks 皆失敗）。
- StockTwits：DNS 解析失敗，需於 session 網路設定中開放 api.stocktwits.com 才能重試。
- yf insider：空回傳，需確認是資料源缺漏還是確實無交易。
- yf 其他端點：Yahoo cookie / crumb 取得失敗，但仍回傳資料，數值需視為近似值。

SENTIMENT REPORT COMPLETE
