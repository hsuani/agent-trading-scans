# Sentiment — POET as of 2026-11-22

## Analyst consensus
資料缺口：yf `rec_summary` 回傳全部為 0（0 buy / 0 hold / 0 sell），`recommendations` 歷史評等為空。兩者皆來自 cache fallback，無法作為計數依據。

以 WebSearch 補充的零散來源（非完整分佈，樣本僅 2 筆）：
- Stockchase：最新評等 "DON'T BUY"，過去一年 1 buy、1 sell。
- Benzinga：共識目標價 $6.25，對照 2026-11-02 收盤約 $5.135。
- TipRanks：Smart Score 為 Underperform；部落客情緒偏多，crowd wisdom 近 30 日非常負面。
- Jim Cramer 於 2026-09-30 曾列為 "Top Pick"（時點已早於本報告約 2 個月）。
- 另一來源引述 12 個月平均目標價 $17.50，但日期不明且與目前股價差距極大，判定為過時資料，不採信。

近期升降評：yf 無資料；WebSearch 未見 2026-11-16 Q3 財報後的正式評等調整。

## Retail social
- Reddit：本輪依指示以 WebSearch 取得彙整內容，未直接抓取 Reddit JSON。結果多來自媒體與聚合站轉述，需自行驗證。
  - 4 月暴跌後（單日約 -45%）出現集體訴訟，當時 Reddit 情緒數據為極空。
  - 5 月中旬 WSB 熱度升至高點，一篇 5/19 貼文主張年底目標 $40。
  - 來源多為 2026-05 前後，非近期貼文，無法確認 11 月 WSB 討論量。
- StockTwits / X：StockTwits 報導顯示 11/16 Q3 財報當天散戶情緒仍偏多，但股價當日跌逾 11%。11/9 Earnings Whispers 預覽指出股價自上次財報後約跌 42%，多頭情緒大幅退潮。X 上無可用的 11 月資料。
- 討論量：定性判定為「較 5 月高點明顯下降」，但無實際提及數可量化。
- 散戶傾向：混合偏多（StockTwits 仍多）與偏空（TipRanks crowd 負面、空方報告）並存。
- 主要主題（重複出現）：
  - AI 光學（optics）題材，Nvidia 提及其光學技術曾引發熱議。
  - 稀釋風險：近期股權與權證發行。
  - 空方：Night Market Research 質疑業務往來並宣稱持空。
  - 法律風險：4 月暴跌後的集體訴訟。
  - 產能擴張：Q3 財報提出產能 10 倍擴張目標，並以 2027 年中建立可量產引擎組裝線為目標。
- 代表性標題（媒體標題，非社群原文，未取得可逐字引用的 Reddit / StockTwits 貼文）：
  - 「Bulls Vs Bears: POET Stock Eyes Best Month In Over 2 Years」（StockTwits，5 月前後）。
  - 「POET Stock Drops Premarket: Retail Optimism Holds Firm Even As Short Interest Rises」（StockTwits）。

## Insider activity
Net 6mo（2026-05-22 至 2026-11-22）：$0.00M 買入（公開市場）／約 $3.86M 賣出（公開市場 "Disposition"）。
- 金額以 yf 原始值加總：6 月約 $2.95M、7 月 $0.06M、8 月 $0.85M。
- 買入：窗口內無公開市場買入紀錄。6 月另有選擇權行權（Exercise of options）約 $0.18M，屬行權後賣出，不計為買入。
- 主要賣方：
  - Kevin Barnes（Senior Officer）：6/5 以 $11.25 賣出約 $0.57M；窗口內另有 8/10 以 $8.93 賣出約 $0.13M。
  - Mo Jinyu（Senior Officer）：6/3 以 $14.65 賣出約 $0.44M；6/5 以 $10.82 賣出約 $0.65M。
  - Lee James（Director/Senior Officer）：6/1、6/3、6/12 分批以 $14.17–$14.68 賣出，合計約 $1.03M。
  - Thomas R. Mika（Senior Officer）：8/7 以 $8.93 賣出約 $0.41M。
  - Venkata Kankipati（Senior Officer）：8/7 以 $8.93 賣出約 $0.21M；6/16 以 $14.73 賣出約 $0.08M。
  - Glen Riley（Director）：6/30 以 $6.71 賣出約 $0.05M；8/19 以 $9.45 賣出約 $0.10M。
  - 其他董事（Ende、Tirva、Khan）：小額賣出，合計約 $0.15M。
- 價格軌跡：6 月賣出價約 $10.8–$14.7，8 月約 $8.9–$9.5，與 11/2 股價約 $5.1 相比，內部人在高點區間大量出脫。
- 注意：8/7 另有多筆無金額、無價格的 "D" 紀錄（Mika、Venkatesan、Jinyu 等），性質不明（可能為股權獎勵、持股申報或稅務扣繳），本報告未計入。
- 持股比例：內部人持股 0.068%，極低。

## Ownership shifts
- 機構持股比例 16.6%（機構數 187）。
- yf 僅提供單一時點快照，無法判定 QoQ 趨勢，須標註為資料限制。
- 內部人持股比例極低，對「內部人作為穩定持有者」的判讀幫助有限。

## Net sentiment score
Composite：**偏空（bearish），信心：中低**
- 分析師面：偏空。Underperform、DON'T BUY 為主，共識目標價 $6.25 高於股價約 22%，但樣本僅 2 筆，資料完整性差。
- 內部人面：偏空。6 個月內約 $3.86M 公開市場賣出、零買入，且賣出集中在高價區間。
- 散戶面：混合偏多。StockTwits 在 Q3 前後仍偏多，但 crowd 指標與空方報告偏負，且討論熱度較 5 月明顯下降。
- 信心受限原因：analyst 計數全 0、Reddit 無直接資料、目標價來源時點不一致、ownership 無趨勢。

Divergence flag：**是**。散戶（StockTwits）偏多，與分析師（DON'T BUY / Underperform）及內部人（淨賣出）的偏空方向相反。此背離依慣例值得留意，但應與股價跌幅、稀釋與訴訟風險一併判讀，本報告不作交易建議。

## 資料時效與限制
- 所有引用內容日期皆早於 2026-11-22（最新為 11/16 Q3 財報）；未使用任何 2026-11-22 之後的資料。
- 未取得 StockTwits API、Reddit JSON 的直接數據（依任務指示以 WebSearch 替代）。
- yf 在本次執行中 Yahoo cookie/crumb 取得失敗，改用 cache，屬預期情況。

SENTIMENT REPORT COMPLETE
