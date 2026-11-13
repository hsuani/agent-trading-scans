# Sentiment — IRM as of 2026-11-14

## Analyst consensus
12 家分析師：4 strong buy / 7 buy / 0 hold / 1 sell / 0 strong sell（Buy 類佔 11/12，約 92%）。
近四個月結構幾乎不變：2026-08 起為 4/7/0/1；-3m 時為 4/6/0/1，即淨增 1 家 Buy，無 Hold 或 Sell 轉向紀錄。
Recent moves: yfinance `recommendations` 只回傳彙總計數，未列出個別升降評等與目標價變動，無法逐筆確認。
外部搜尋提到 JP Morgan 維持 Overweight 並將目標價由 $121 上調至 $138（日期標示為 May，年份不明，需核實）。
同一搜尋另有一份資料來源顯示 19 家分析師為 Hold 共識（63% Buy / 26% Sell），與 yfinance 的 12 家結構明顯衝突，且日期不明，本報告以 yfinance 為主要來源，未予採納。

## Retail social
- Reddit: 無法取得。WebFetch 對 www.reddit.com 回應無法存取（r/wallstreetbets 與 r/stocks 搜尋皆失敗），此來源 soft-fail。
  搜尋引擎可查到的最具體 WSB 貼文為 2024-08 的看空 DD（認為估值過高、負債高），已超過半年，不代表近期情緒。
- StockTwits: 無法取得。api.stocktwits.com 無法解析（DNS 失敗），此來源 soft-fail。
- X / 聚合器: 第三方情緒追蹤器數據粗略且彼此不一致。SentiSense 30 日分數 12（略偏多，最新標示為 2026-09），提及量約 25 則/日。
  AltIndex 給予 X 情緒分數 86/100（偏多），提及量高於近期均值。TipRanks 描述為 Positive。
  Benzinga 的 put/call ratio 為 0.55，選擇權面偏多。
- Retail tilt: 略偏多（低信心）。聚合器與選擇權數據偏多，但缺乏 Reddit/StockTwits 原始樣本，無法驗證。
- Buzz volume: 相較一般 S&P 中型股屬中等偏低（約 25 則/日的聚合器估計），無法與歷史均值精確比較。
- Themes（依有限樣本歸納）:
  1. 估值與負債：部分看多者以營運成長與股價表現支持，看空者則聚焦高負債與估值（D/E 遠高於 REIT 中位數）。
  2. 營收成長與財報：外部報導指 Q2 2026 營收年增約 18.5% 並優於預期，被視為多方論點。
  3. 內部人減持：社群可能將 CEO 的規律性賣出解讀為看空訊號（需以 Insider 段落為準）。
- 代表性引述（僅記錄可得的標題式陳述，非完整貼文）：多方強調財報超預期；空方強調負債與估值。

## Insider activity
統計區間：2026-05-14 至 2026-11-14（6 個月）。以公開市場 Sale（代碼 S）計，排除選擇權行使（conversion）、股票獎勵與贈與。

Net 6mo: **$0 buys, $40.1M sells**（以 USD 計，單位 M）。買入：無（最近一次公開市場買入為 2025-11-19，董事 Kelly 2,954 美元，已超出區間）。

| 日期 | 內部人 | 職稱 | 股數 | 金額 (USD M) |
|---|---|---|---|---|
| 2026-05-08 | William L. Meaney | CEO | 38,474 | 4.96 |
| 2026-06-01 | William L. Meaney | CEO | 38,474 | 4.91 |
| 2026-07-01 | William L. Meaney | CEO | 38,474 | 4.73 |
| 2026-08-07 | William L. Meaney | CEO | 38,474 | 4.68 |
| 2026-09-01 | William L. Meaney | CEO | 38,474 | 4.39 |
| 2026-10-01 | William L. Meaney | CEO | 38,474 | 4.25 |
| 2026-11-06 | William L. Meaney | CEO | 38,474 | 4.07 |
| 2026-08-06 | Greg W. McIntosh | Officer | 11,839 | 1.51 |
| 2026-05-21 | Daniel Borges | Officer | 7,189 | 0.90 |
| 2026-05-12 | Pamela M. Arway | Director | 1,892 | 0.24 |
| 2026-05-20 | Walter C. Rakowich | Director | 757 | 0.09 |
| 區間其他 | Mark Kidd（5 筆，各 6,000 股）、Greg McIntosh（3 筆，各 5,000 股） | Officer | 合計 45,000 股 | Kidd 3.71、McIntosh 1.72（合計約 5.43） |

- 主要訊號：CEO Meaney 每月約 38,474 股公開市場賣出（區間總額約 31.98M USD），並同步行使 $37.00 選擇權（每月 conversion 紀錄，價值約 1.42M USD），股數與時點高度規律，推測為預定交易計畫（10b5-1），但本報告無法自工具輸出確認，需以 SEC Form 4 附註驗證。
- 規律性減持金額隨股價變動：區間內股價約 104–129 USD，單月賣出約 4.1–5.0M USD。
- 解讀：內部人淨賣出在規模上顯著，但 CEO 的減持模式較像計畫性變現，而非方向性看空；仍需留意其與分析師偏多形成的分歧。
- 2026-03-02 至 03-05 之間 Meaney 的大額賣出（合計約 46.6M USD）已超出 6 個月區間，未納入本段統計。

## Ownership shifts
- 機構持股比例：85.6%（float 口徑 86.3%），機構數 1,587 家。
- 內部人持股：0.88%。
- 趨勢：工具僅回傳當期快照，無歷史序列，無法判斷集中度是增加或減少。

## Net sentiment score
Composite: **偏多（bullish-leaning）**，信心：中低。
- 分析師面：偏多，信心中高（11/12 Buy，結構穩定）。
- 內部人面：偏空／中性，信心中（金額大、6 個月零買入，但減持模式疑似計畫性）。
- 散戶面：略偏多，信心低（聚合器數據與選擇權 put/call 0.55 支持，但缺 Reddit／StockTwits 原始樣本）。
- 合成：分析師與散戶方向一致偏多，內部人賣出為主要反向訊號，整體為中性偏多。

Divergence flag: **部分是**。
- 散戶 vs 分析師：兩者同向（皆偏多），無分歧。
- 內部人 vs 分析師：內部人淨賣出與分析師偏多方向相反。此分歧常見於計畫性減持，解讀價值有限，但值得在後續輪次中核實 Form 4 附註。

資料缺口：Reddit、StockTwits 無法取得；分析師目標價逐筆變動與個別升降評等未取得；外部資料來源日期多不明或互相衝突，已於對應段落標註。

SENTIMENT REPORT COMPLETE
