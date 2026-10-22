# Sentiment — ISRG as of 2026-10-22

資料說明：yf live feed 的 cookie/crumb 取得失敗，分析師、內部人、機構持股資料改用 repo cache（prices/yf/ISRG.json，_refreshed_at 2026-10-22T11:40 UTC，_misses 為空），數字與 yf 工具輸出一致。散戶社群部分僅能透過 WebSearch 取得，Reddit 與 StockTwits 無法直接讀取原始貼文，所有社群數字皆為聚合站點的快照，日期不明。

## Analyst consensus
目前 yf rec_summary（0m）：strongBuy 8 / buy 18 / hold 7 / sell 1 / strongSell 0，合計 34 家，換算為 26 buy / 7 hold / 1 sell。

3 個月趨勢（-3m）為 23 buy / 9 hold / 1 sell。過去 3 個月 hold 由 9 降至 7，buy 增加 3 家，評等偏向正面。

目標價（cache info）：targetMeanPrice 480.17、targetHigh 685、targetLow 324，共 30 家；recommendationKey 為 buy。cache 中 currentPrice 為 428.12，平均目標相對現價約 +12%。52 週區間 328.57 – 603.88。

近期評等動態（WebSearch 聚合，多為 2026 年中以前，未找到 2026-10 月的評等變動）：
- Jul 30 HSBC 降評，目標價 $931。此數字與現價明顯不合，疑為資料錯誤，未採信。
- Jul 28 UBS 首次覆蓋，目標 $500。
- Jul 20 BMO 維持 Outperform，目標 $518。
- May 27 Goldman Sachs 目標由 $621 降至 $558，維持 Buy，理由為 medtech 股近期表現弱。
- May 18 BofA 目標由 $650 降至 $520，維持 Buy。
- Evercore ISI 目標由 $480 降至 $430，評等 In Line（日期不明）。
- Barclays 首次覆蓋（日期不明，來源為 Simply Wall St）。

整體：分析師偏多，多數評等為 buy，但 2026 年中以來目標價普遍下修，顯示估值壓力。

## Retail social
- Reddit：WebSearch 未找到 r/wallstreetbets 或 r/stocks 中 ISRG 的近期討論串，無法列出具體貼文樣本，也無法給出 tilt 的直接證據。AltIndex 聚合頁顯示 Reddit 情緒分數 87/100（偏多），但同頁註明此分數不具方向性預測力，且討論量僅約每日 4 則，屬低量。
- StockTwits / X：StockTwits 無可用 2026 年數據。LunarCrush 快照呈現正面但不一致：45%、81%、90%、95% 正面，皆無日期，較可能反映不同時點而非真實分歧。
- 討論量：整體偏低（AltIndex 每日約 4 則），相對於 ISRG 的市值與機構關注度，屬於低於典型的散戶話題熱度。此為定性判斷。
- Tilt：偏多但證據薄弱，置信度低。
- 主要主題（來自聚合站與新聞摘要，非原始貼文）：
  - 多方：Q3 盈餘超預期、30 日股價反彈、分析師評等偏多。
  - 空方：醫院資本支出預算收緊、競爭者機器人系統增加、產品召回與網路安全疑慮（LunarCrush AI 摘要提及）。
- 引用樣本：本次未取得可核實的原始貼文，故無直接引用。

## Insider activity
統計區間 2026-04-22 至 2026-10-22（6 個月），依 yf insider 資料：
- 公開市場賣出（Sale）：約 $8.08M，共 18 筆，皆為賣出，無公開市場買進。
- 選擇權行使（Conversion）：約 $0.54M，屬行使後持有，非買賣方向。
- Net 6mo：約 -$8.1M（純賣出，無買進）。

主要賣方：
- GUTHART GARY S（Executive Chair，董事）：2026-08-11，10,000 股，$400.00，約 $4.0M，為區間最大單筆。
- JEDDI IMAN（Officer）：2026-06-01，5,625 股，$420.55，約 $2.37M。
- LOEB GARY（Officer）：多次小額賣出，合計約 $0.5M。
- LADD AMY L（Director）：2026-08-11，472 股，約 $0.18M；另 2026-04-29 亦有賣出。
- WIDMAN FREDRIK（Officer）：2026-09-15，1,089 股，$374.44，約 $0.41M。
- BROSIUS MARK PRESTON（Officer）：多次小額賣出，合計約 $0.33M，為頻率最高的賣方。

CEO（ROSA DAVID J）在區間內無公開市場賣出，僅有 2026-07-10 一筆無金額交易（疑為授予或稅務扣繳，未計入）。CFO（SAMATH JAMIE E.）區間內無交易紀錄。

其他注意事項：
- 2026-04-30 董事股票授予（531 股等）與 2026-10-09 LOEB、WADORS 無金額交易，性質不明，未計入買賣統計。
- 賣出多集中在 Jun–Sep 股價 $345–$425 區間，與股價由高點回落時段一致，但無法確認是否為 10b5-1 計畫。

## Ownership shifts
- 機構持股 89.5%（float 持股 89.9%），機構數 3,129 家；內部人持股僅 0.51%。
- 前幾大持股（2026-06-30，13F 有一季延遲）：
  - BlackRock 8.5%，持股 -0.17%
  - Vanguard Capital Management 6.55%，+0.22%
  - State Street 4.55%，+1.36%
  - Invesco 3.35%，+5.84%
  - T. Rowe Price 3.19%，-10.09%（明顯減持）
  - Geode 2.42%，+0.8%
  - Capital World Investors 2.19%，-3.79%
- 趨勢：前十大機構淨變動混合，Invesco 與 State Street 加碼，T. Rowe 與 Capital World 減碼。單一季資料，無法確認長期趨勢。

## Earnings context
cache 顯示 Q3 2026 已於 2026-10-20 公布：EPS 3.00，預估 2.64，超出 13.6%。過去 Q4 2025 至 Q3 2026 共 6 季皆為 EPS 超預期。盈餘後的評等與目標價變動未在本次搜尋中找到，為資料缺口。

## Net sentiment score
Composite：偏多（bullish），置信度中低。

依據權重（估計）：
- 分析師（偏多，置信度高）：buy 占比約 76%，目標價高於現價約 12%，但 2026 年中以來目標普遍下修。
- 散戶（偏多但薄弱，置信度低）：Reddit 與 LunarCrush 偏正面，討論量低，資料不一致。
- 內部人（偏空訊號，置信度中）：6 個月 $8.1M 純賣出、無買進，主要為高層與董事，但多數屬於行使後賣出，訊號解讀需保守。
- 機構（中性）：持股比例高，淨變動混合。

Divergence flag：部分分歧（yes，限內部人）。
- 散戶與分析師同向偏多，但散戶資料薄弱，不具強訊號。
- 內部人為單向賣出，與分析師的 buy 評等方向相反，值得留意。
- 2026-10-20 盈餘超預期後，後續評等與股價反應是下一步需要驗證的變數。

資料缺口與後續查核建議：
- Reddit、StockTwits 原始貼文無法直接取得，建議日後以可直接存取的來源補充。
- 2026-10 月的評等變動（盈餘後）未找到，建議查 MarketBeat、TipRanks 或 TheFly。
- HSBC $931 目標價數據異常，建議核實。

SENTIMENT REPORT COMPLETE
