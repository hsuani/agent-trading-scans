# Sentiment — MU as of 2026-10-19

資料截止：分析師評等與內部人交易資料為 yf 工具輸出（內部人交易最新至 2026-08-21）；價格參考 repo 快取 prices/yf/MU.json（最新收盤 2026-10-16，878.84）。社群資料受 Reddit / StockTwits 封鎖，改以 WebSearch 取得，多數為 2026 年 5 月至 10 月之間的快照，時間戳不一致，僅供參考。

## Analyst consensus
目前 49 位分析師：9 Strong Buy / 36 Buy / 3 Hold / 0 Sell / 1 Strong Sell。
**BUY 佔比 91.8%**（45/49），Hold 6.1%，Sell 2.0%。

- 三個月趨勢：BUY 佔比由 88.9%（-3m，40/45）升至 91.8%；Hold 由 5 家降至 3 家。
- 最近一個月出現 1 家 Strong Sell（於 -1m 快照已存在，-2m 無），未能從工具輸出辨識券商與日期。
- Yahoo info 欄位：recommendationKey = strong_buy，recommendationMean = 1.37，目標價均值 1,560.57、中位數 1,550、高 3,000、低 361（共 46 家，快照日期未知）。
- 近期評等動作（WebSearch，無 2026-10 當月升降評）：
  - Summit Insights 2026-03-19 由 Buy 降至 Hold；Erste Group 2026-04-02 由 Buy 降至 Hold（理由為資本支出加重、FCF 承壓）。
  - Morgan Stanley 由 Equal-weight 升至 Overweight（日期未確認），2026-10 初重申 Overweight，目標 1,200。
  - Susquehanna 2026-10 初重申 Positive，目標 2,000。
  - 24/7 Wall St（2026-10-15）給 Hold，目標 1,059.58，指出街上目標明顯高於其估值。
  - Citigroup 2026-08 由 1,400 下調至 1,150；BofA 目標上調至 950（維持 Buy，日期未明）。
- 目標價與股價差距：以 878.84 計，均值目標 1,560 隱含約 +77% 上行空間；但個別目標分散極大（361 至 3,000），且多數來源停留在 2026-08 前後。

## Retail social
- Reddit：本次 WebFetch 受阻，改以 WebSearch 查詢，未找到 2026-10 的 r/wallstreetbets 或 r/stocks 有效討論串。最近可見的 SentiSense 快照（2026-08-09）顯示 Reddit 偏空，佔提及數約 6%，X 偏多。WSB 過往熱度的文章（標題 "Micron Technology Stock Can Do No Wrong Right Now"）屬舊資料，不代表當前情緒。
- StockTwits / X / 聚合站：
  - LunarCrush 頁面顯示 MU 社群正面情緒 93%（另一語系頁面為 74%），日期不明，且涵蓋 X 與 Reddit 等多平台。
  - 某分析文提到 StockTwits 對 MU 情緒為 bullish，留言量高，但時間不明；另有報導指情緒由 extremely bullish 回落至 bullish。
  - 無法取得本週的留言量數字，**討論量只能定性判斷**：長期處於高檔，近期因股價回檔後熱度降溫的說法有限度支持。
- 主要主題（依 WebSearch 片段整理）：
  1. 記憶體供需緊俏與 DRAM 價格（多頭主論述，HBM 與毛利率被反覆引用）。
  2. 估值與獲利了結：股價自 52 週高 1,255 回落約 30%，部分文章提到「記憶體族群漲多後獲利了結」。
  3. 法律風險：加州集體訴訟指 Samsung、SK Hynix、Micron 涉嫌協同限制 DRAM 供給，屬於空方論點。
  4. 「華爾街過度樂觀」論述（Seeking Alpha 文章），認為評等已擁擠。
- 代表性觀點（短引）：「Micron Technology Stock Can Do No Wrong Right Now」（2026 年較早期標題，代表高點期的多頭情緒）。

## Insider activity
區間：2026-04-19 至 2026-10-18（6 個月）。
**淨額：買入 $0；賣出約 $247.7M（15 筆）；無公開市場買入。** 股票獎勵與贈與不計入金額。

| 內部人 | 職位 | 賣出金額（約） | 備註 |
|---|---|---|---|
| Sanjay Mehrotra | CEO | $182.3M | 2026-07 至 08 多筆，單筆約 $0.8M 至 $39M，成交價約 $906–$990 |
| April S. Arnzen | Officer | $43.4M | 2026-07-01，40,000 股，約 $1,077–$1,096 |
| Sumit Sadana | Officer | $14.0M | 2026-08-18，15,000 股，$934.29 |
| Michael Charles Ray | Officer | $4.1M | 6 個月內 |
| Steven J. Gomo | Director | $1.6M | |
| Lynn A. Dugle | Director | $1.5M | 2026-06-30，1,300 股，$1,150.43 |
| Scott R. Allen | Officer | $0.9M | 2026-07-23，879 股，$1,000 |

- 最大單一賣方為 CEO，佔比約 74%。
- 賣出價位集中在 $900 至 $1,150，對應目前 878.84 的收盤價，內部人賣出時的股價高於現價。
- 工具輸出未標示交易是否為 10b5-1 計畫，無法判斷是否屬預先排定的出售。
- 內部人持股比例 0.24%（insidersPercentHeld），對持股結構影響有限。

## Ownership shifts
- 機構持股比例 80.04%，機構數 5,025 家（major_holders 快照）。
- 工具僅提供當前快照，缺少 13F 季度變動，**機構資金流向無法從本次資料確認**，僅能判定持股集中度高（約八成）。

## Net sentiment score
**Composite：中性偏多（信心：低至中）**

- 分析師面：偏多。BUY 91.8%、Strong Buy 9 家、評等均值 1.37；但有 1 家 Strong Sell 與 2 家降評 Hold 的記錄，目標價離散度高。
- 內部人面：偏空（流向）。6 個月約 $248M 賣出、零買入，CEO 為主要賣方。
- 散戶面：偏多但證據陳舊。LunarCrush 與 StockTwits 的正面比例高，Reddit 快照偏空，2026-10 的即時數據缺漏，信心低。
- 整體評估為分析師偏多、內部人偏空，散戶面未能確認，綜合為中性偏多。

**Divergence flag：是（內部人流向與分析師評等方向相反）**。
- 散戶與分析師方向：散戶目前無可靠 2026-10 數據，無法判定是否背離，故此項標示為「資料不足，無法判定」。
- 內部人與分析師方向相反：分析師 91.8% 買進，而內部人於高檔（$900 至 $1,150）賣出約 $248M，且無買入。

## 資料限制
1. 分析師評等資料無日期欄位（僅 0m、-1m、-2m、-3m 期間快照），無法精確到月內升降評。
2. yf rec_summary 總家數（49）與 Yahoo info 的 numberOfAnalystOpinions（46）不一致，快照時點不同。
3. 股價來源衝突：快取 2026-10-15 收盤 931.24，但 24/7 Wall St 引述 10-15 盤中約 982.14。本報告以快取為準。快取最後一筆為 2026-10-16，10-17 與 10-18 未納入。
4. 社群資料多數為 2026-05 至 2026-10 間的快照，無法確認為本週情緒。
5. 本報告不含交易建議。

SENTIMENT REPORT COMPLETE
