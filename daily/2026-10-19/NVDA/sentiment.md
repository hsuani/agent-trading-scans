# Sentiment — NVDA as of 2026-10-19

資料基準: yf 快取 (refreshed 2026-10-18 10:55 UTC)，現價 214.13。Live feed 因 Yahoo cookie/crumb 失敗，改用快取。社群面以 WebSearch 取得，Reddit 與 StockTwits 無法直接存取。所有資料以 2026-10-19 為截止，之後的資料視為未知。

## Analyst consensus
59 位分析師: **Strong Buy 10 / Buy 49 / Hold 2 / Sell 1 / Strong Sell 0**。
- **%BUY = 95.2%** (Strong Buy 10 + Buy 49 = 59，除以全部評等 62)。Hold 3.2%，Sell 1.6%。
- 近四個月分布穩定: -3m 58/61 (95.1%)、-2m 57/60 (95.0%)、-1m 59/62 (95.2%)、0m 59/62 (95.2%)。沒有明顯的評級漂移。
- recommendationKey: strong_buy，recommendationMean 1.29 (1 為最強買進)。
- 目標價: mean 328.72、high 515、low 180。以現價 214.13 計算，mean 隱含約 +53% 空間。
- 近期 upgrade/downgrade 個別事件: 快取與 feed 只提供月度彙總，**無個別事件明細**，無法列出具體升降評等與目標價調整日期。WebSearch 找到的目標價與評等資料多為 2025 年底或 2024 年，不採用。
- 最近財報: 2026-08-26，EPS 2.22 vs 預估 2.09 (+6.2%)。下次財報 2026-11-17 (預估 EPS 2.47)。

## Retail social
- **Reddit (r/wallstreetbets, r/stocks)**: 無法取得。Reddit 網域無法透過 WebSearch 搜尋 (API 回傳 domain not accessible)，WebFetch 亦被封鎖。**此來源 soft-fail，無樣本、無 tilt 判斷。**
- **StockTwits**: 未嘗試直接抓取 (依任務要求 Reddit/StockTwits 主機被封鎖，改用 WebSearch)。無資料。
- **X / 新聞與選擇權流向 (WebSearch)**:
  - 2026-08 至 09 的 Historical Option Data 頁面記錄 call 比例偏高 (8 月底約 82.6%，9 月初約 71.2%)，屬於偏多的選擇權部位。該來源是自動生成頁面，部分引用 X 貼文，時效為 8/9 月而非 10 月。
  - 2026-10-07 前後的報導描述「謹慎偏多」: 認為 NVDA 在 AI 產業的長期地位仍吸引投資人，同時提到市場修正風險、客戶資本支出放緩、自研晶片競爭與內部人賣股。
  - 新聞的價格敘述不一致: 一篇提到 10/6 觸及約 243 後回落，與快取現價 214.13 有明顯落差。我無法對齊這兩個時點，因此不以此作為價格依據。
- **Buzz 量能**: 無法定量。WebSearch 結果中缺少 10 月的社群討論量資料，無法與常態比較。

## Retail 主題 (從 WebSearch 摘錄，樣本有限)
1. AI 長期需求與資料中心成長仍是多方主論點。
2. 估值偏高與泡沫疑慮是主要空方論點。
3. 內部人持續大額賣出被提及為風險訊號。
4. 自研晶片 (custom silicon) 競爭被列為中期威脅。
5. 客戶資本支出與庫存的隱憂，為市場修正的假設來源。

Retail tilt: **無法判定 (資料不足)**。目前可用的最強訊號是 2026 年 8–9 月的選擇權 call 偏多，但時效不在 10 月。

## Insider activity
資料範圍: feed 最早為 2025-03-03，6 個月視窗為 2026-04-19 至 2026-10-19，涵蓋完整。

**6 個月公開市場交易 (Sale，不含 gift 與 grant):**
- **淨買入: $0** (無任何公開市場買進)
- **賣出合計約 $1.37B** (約 $1,370.5M)，共 9 筆:
  - Mark A. Stevens (Director，Ownership=I 間接持股): 5 筆，合計約 $1,353.7M。最大為 9/2 賣出 1.85M 股 (約 $410.8M)、9/4 賣出 1.02M 股 (約 $235.6M)、9/18 賣出 1.37M 股 (約 $300.1M)。6/4 與 6/18 亦有大額賣出。
  - Timothy S. Teter (General Counsel): 8/31 賣出 30,000 股 (約 $6.5M)，9/21 賣出 30,460 股 (約 $6.8M)。
  - Stephen C. Neal (Director): 6/3 賣出 15,500 股 (約 $3.3M)。
  - John O. Dabiri (Director): 5/27 賣出 625 股 (約 $0.13M)。

**非市場交易 (不計入淨買賣):**
- CEO Jensen Huang: 6/16 gift 400,000 股；3/18 gift 58.96M 股。**6 個月內無公開市場賣出**，最後一筆公開市場賣出為 2025-10-29。2025 年 7 月至 10 月間有固定規模的定期賣出 (每筆約 225,000 股)，已結束。
- Tench C. Coxe (Director): 7/1、8/5、9/2 各 gift 500,000 股。
- 多位董事與經理人: 6/25 與 9/9 有 grant，屬薪酬性質。

**Notable:**
- Stevens 的大額賣出是此視窗內唯一的重大賣壓來源，屬於董事層級而非 CEO/CFO。交易為間接持股，無法確認是否為 10b5-1 預先安排計畫，feed 未提供此欄位。
- CFO Colette Kress 6 個月內無公開市場賣出，最後一筆為 2026-03-20 (約 62,650 股)。
- 方向: **淨賣出，主要來自單一董事；CEO 與 CFO 在本視窗未出售。**

## Ownership shifts (機構)
- 機構持股 71.4% (institutionsPercentHeld)，institutionsFloatPercentHeld 74.4%，機構家數 7,690。內部人持股 4.0%。
- 前十大機構 (資料日期 2026-06-30) 中，**9 家增持、1 家減持** (T. Rowe Price -0.07%)。
- 增持幅度較大: Morgan Stanley +3.93%、FMR +3.24%、Vanguard Portfolio Management +1.51%、State Street +1.60%。
- 方向: **機構淨增持，集中度穩定。** 注意這是 6/30 季報資料，不是 10 月即時資料。

## Net sentiment score
**Composite: 偏多 (信心中等)**

| 面向 | 方向 | 信心 | 說明 |
|---|---|---|---|
| 分析師 | 強烈偏多 | 高 | 95.2% Buy，評等穩定，mean 目標價隱含約 +53% |
| 內部人 | 偏空 | 中 | 6 個月淨賣 $1.37B，主要為單一董事；CEO/CFO 未在公開市場賣出 |
| 機構 | 偏多 | 中 | 前十大 9 家增持，但資料為 6/30 季報 |
| 散戶 / 社群 | 無法判定 | 低 | Reddit/StockTwits 無資料；WebSearch 僅有 8–10 月零星偏多與謹慎訊號 |

**Divergence flag: 是** — 分析師與內部人方向相反 (分析師高度偏多、內部人大額淨賣出)。散戶與分析師的差異無法判定，因為缺乏可靠的散戶資料，因此散戶面不計入背離判斷。

## 限制
1. Reddit、StockTwits 無法取得，社群判斷信心低。
2. 評等僅有月度彙總，無個別升降評事件與目標價變動日期。
3. 機構持股為 6/30 季報資料，不反映 10 月的即時變化。
4. 內部人交易未標示 10b5-1 計畫，無法區分預先安排與主動賣出。
5. WebSearch 新聞價格 (約 243，10 月初) 與快取現價 (214.13，10/18) 不一致，未能調和，未採用。
6. 本報告為情緒彙總，不構成交易建議。

SENTIMENT REPORT COMPLETE
