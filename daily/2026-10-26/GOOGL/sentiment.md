# Sentiment — GOOGL (Alphabet) as of 2026-10-26

> 注意事項：系統今日日期為 2026-10-25，本報告 as-of 日期為 2026-10-26（未來日期）。以下資料為執行當下可取得的最新資料，並非 10-26 收盤後之資料。Reddit 與 StockTwits 無法取得（見下方），零售情緒部分以網路搜尋摘要為主，證據強度低。

## Analyst consensus

單位：分析師家數（個）。來源：`pipeline/tools/yf GOOGL rec_summary`。

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 合計 | 買方評級占比 |
|---|---|---|---|---|---|---|---|
| 當期 (0m) | 13 | 43 | 5 | 0 | 0 | 61 | 91.8% |
| 前 1 個月 (-1m) | 13 | 44 | 5 | 0 | 0 | 62 | 91.9% |
| 前 2 個月 (-2m) | 13 | 45 | 5 | 0 | 0 | 63 | 92.1% |
| 前 3 個月 (-3m) | 13 | 45 | 6 | 0 | 0 | 64 | 90.6% |

目前分布：61 家中 56 家為買進或強力買進（Strong Buy 13 / Buy 43），5 家 Hold，0 家 Sell。

Recent moves：工具只提供彙總家數，沒有逐家升降評等事件。由家數變化推斷，近 3 個月覆蓋家數由 64 降至 61，Hold 由 6 降至 5，Buy 由 45 降至 43，無任何 Sell 評等。個別券商升降評等與降目標價明細：DATA_UNAVAILABLE。

目標價（Price target）：DATA_UNAVAILABLE（工具未提供）。網路搜尋摘要引述平均目標價約 $429，但來源為二手彙整頁面，未經獨立驗證，僅供參考。

## Retail social

- **Reddit (r/wallstreetbets, r/stocks)**：DATA_UNAVAILABLE。WebFetch 回傳無法存取 reddit.com，curl 經 agent proxy 回傳 403 (CONNECT tunnel failed)。無法取得討論串樣本與情緒傾向。
- **StockTwits**：DATA_UNAVAILABLE。WebFetch 回傳 DNS 解析失敗（api.stocktwits.com），curl 同樣經 proxy 回傳 403。
- **X / 新聞與網路討論**：僅能取得 WebSearch 的二手彙整頁面，非原始貼文。摘要內容如下：
  - Tickeron（10 月初）：股價約 $338，近一個月約持平，遠低於 5 月歷史高點 $408.61，市場對 AI 資本支出與雲端成長的平衡有疑慮。
  - TradingKey（10 月 17 日）：技術面評級中性，股價測試 $341.48 支撐，需站回 $346–347 壓力帶。
  - SentiSense（8 月 9 日資料）：30 日情緒分數偏多，但資料早於 10 月，時效性不足。
  - Stockscan：顯示現價 $373.51 並推估約 60% 下跌，與其他來源明顯衝突，判定為不可靠來源，不採用。
- **Buzz volume（討論量）**：DATA_UNAVAILABLE。無法取得提及次數與相對歷史基準。
- **Retail tilt（零售傾向）**：無法直接量測。依網路彙整來源判斷為**偏中性 / 多空分歧**（low confidence）。

Themes（依網路搜尋摘要歸納，未經原始貼文驗證）：
1. **AI 資本支出**：2026 年資本支出指引約 $195–205B，市場擔心自由現金流壓力。搜尋摘要提到某季自由現金流為負。
2. **雲端成長**：搜尋摘要引述 Google Cloud 營收年增約 82%、約 $24.8B 的 Q2 數據，以及約 $514B 的雲端 backlog。此數據來自二手摘要，未與官方財報核對。
3. **人才與組織變動**：搜尋摘要提到 DeepMind 高層異動（Jeff Dean、Sanjay Ghemawat）相關消息。
4. **財報催化劑**：預計 10-27 公布 Q3 財報，為 as-of 日之後的事件。

Sample quote：DATA_UNAVAILABLE（無原始貼文可引用，不以改寫內容冒充原話）。

## Insider activity

來源：`pipeline/tools/yf GOOGL insider`。6 個月窗口：2026-04-26 至 2026-10-26。

Net 6mo：**$0 買入 / $0 賣出**（窗口內無公開市場買賣，僅有贈與 Stock Gift，價格為 0）。

窗口內交易明細：

| 日期 | 內部人 | 職位 | 類型 | 股數 | 金額 (USD) |
|---|---|---|---|---|---|
| 2026-10-13 | SHRIRAM Kavitark Ram | Director | Stock Gift | 396,700 | 0 |
| 2026-08-07 | Sergey Brin | Director，>10% 受益人 | Stock Gift | 673,200 | 0（同一筆另有一列金額為 null，視為同一交易） |

窗口外參考（不計入 6mo 淨額）：
- Sergey Brin 2026-02-19 贈與 437,500 股。
- John L. Hennessy（Director）2026-01-13 與 2026-02-13 各賣出 600 股，合計約 $0.39M。
- Kavitark Ram Shriram 2025 年有多筆賣出（例如 2025-08-15 以 $205.00 賣 26,000 股，約 $5.3M），2025 年內多數賣出金額為數 M 至十餘 M USD。

解讀：窗口內僅見贈與，屬非市場交易，訊號強度低。工具輸出依日期由新到舊排列，窗口內全部交易已涵蓋（前 4 筆）。窗口內未列示 CEO / CFO（如 Sundar Pichai、Anat Ashkenazi）的交易。但工具輸出僅檢視至前 20 筆，更早期的執行層交易紀錄：DATA_UNAVAILABLE（未完整檢視）。

## Ownership shifts

來源：`pipeline/tools/yf GOOGL major_holders`（單一時點快照）。

| 指標 | 數值 |
|---|---|
| 內部人持股比例 | 1.60% |
| 機構持股比例 | 81.03% |
| 機構持股占流通股比例 | 82.34% |
| 機構家數 | 7,435 |

機構集中度趨勢（季度變化）：DATA_UNAVAILABLE。工具僅提供單一快照，無法判斷機構是加碼還是減碼。

## Net sentiment score

**Composite：偏多（analyst 端，high confidence）／中性（零售端，low confidence）。整體綜合判斷：偏多-中性，信心：中等偏低。**

依據：
- 分析師端：61 家中 91.8% 為買方評級，無 Sell，覆蓋家數近 3 個月小幅下降但評級結構穩定。信心高，但需注意 sell-side 本身的樂觀偏誤。
- 內部人端：6 個月內無公開市場買賣，僅贈與。中性。
- 零售端：Reddit、StockTwits 皆無法取得，僅有網路彙整來源，傾向分歧。信心低。
- 技術面與價格：股價約 $338 附近，測試 $341 支撐、$346–347 壓力，屬震盪區間（來源為二手摘要）。

**Divergence flag：無法判定（DATA_UNAVAILABLE）**。因零售端原始資料缺失，無法確認零售傾向是否與分析師傾向相反。若日後取得 Reddit 或 StockTwits 資料，應重新評估此旗標。

資料缺口清單：
1. Reddit 討論串與提及量（WebFetch 與 curl 皆 403）。
2. StockTwits 訊息流（DNS 失敗與 403）。
3. 分析師目標價與逐家升降評等事件（yf 工具未提供）。
4. 機構持股季度變化（yf 工具僅單一快照）。
5. 財報數據一致性：搜尋摘要中的 Q2 EPS 與 Q3 EPS 預估數字相互矛盾（一處列 Q2 EPS $9.11 對比估計 $2.88，另一處 Q3 EPS 預估 $3.01–3.02），判定為不可靠，本報告不採用。

SENTIMENT REPORT COMPLETE
