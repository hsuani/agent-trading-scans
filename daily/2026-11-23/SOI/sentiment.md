# Sentiment — SOI (Soitec, Euronext Paris) as of 2026-11-23

> 資料品質警示：本次 yf 即時與快取（prices/yf/SOI.json，刷新於 2026-11-22 14:32 UTC）的 recommendations / rec_summary / insider / major_holders / inst_holders 全部為空，且 quoteType 為 NONE，Yahoo 未正確解析此代號。以下分析主要依賴 WebSearch 聚合站資料，多數為無日期或數月前快照，**分析師與內部人數字僅供方向參考，不可當作當前共識使用**。Reddit 與 StockTwits 皆無法存取。
>
> 代號確認：SOI 指 Soitec（Euronext Paris: SOI），與 repo 內 serenity 系列追蹤的 Photonics-SOI 題材一致。搜尋結果中曾出現「NYSE: SOI = Solaris」的說法，經查 Solaris 實際代號為 SEI，該說法應排除。

## Analyst consensus

- 主要來源（S&P Global 經 StockAnalysis，截至 2026 年 5 月下旬）：19 位分析師，共識 **Hold**，平均目標價 €91.82。
- 另一聚合站快照（Investing.com，無日期）：11 buy / 4 sell，顯示偏多；與上一來源分歧大，應視為過期或口徑不同。
- 可確認的近期單一券商動作（皆為 2026 年，已非近期）：
  - Morgan Stanley：Buy，目標價 €200（2026-05-19）
  - J.P. Morgan：Hold，目標價上調至 €150（2026-05-14）
  - Oddo BHF：降評至 Hold（2026-04-28）
  - UBS：降評至 Sell，理由為「光子樂觀情緒過度」（日期不明，媒體標題指稱股價在光子題材下漲幅過大）
  - 2026-09-15 一份報告指稱光子 SOI 營收要到 2029 年才會加速，當日股價約跌 14%（券商名稱未在搜尋結果中確認）
- 目標價變動方向：5 月前後目標價有上調（JPM 至 €150），但 UBS 降評後評價端轉為謹慎。最新的 rating 與 target 無法從現有資料確認。

**彙總**：以 Hold 為主的分歧共識，偏謹慎；買方與賣方同時存在，且近期降評（UBS、Oddo）多於明確升評。

## Retail social

- **Reddit（r/wallstreetbets、r/stocks）**：無法存取（WebFetch 遭拒），本節無資料。
- **StockTwits**：無法存取（DNS 解析失敗，api.stocktwits.com 不在允許網域），本節無資料。需在 session 網路設定中允許該主機後才能重試。
- **X / 影響者（repo 內 serenity 紀錄，非群眾量測）**：
  - serenity.json 中 SOI 近期提及約 6 次，最新一筆 2026-11-19 標記為 bear，時間序列 [0,1,1,-1,1,-1]，正負比約 3 : 2。
  - serenity 11-20 策略摘要：在 AI 板塊修正期間重申「Bullish $SOI」，強調 $1.2B 多年期晶圓預訂承諾。
  - serenity 11-21 策略摘要：將 SOI 納入光學／CPO 樂觀敘事。
  - 代表性言論（短引，≤15 字）：「$25M -> $1.2B LTAs... Vindicated.」
  - 注意：此為單一高追蹤度影響者的觀點，並非一般散戶討論量。
- **一般新聞與論壇（WebSearch）**：Investing.com 會員情緒調查（無日期）顯示偏多，但與 UBS 降評及「400% 年內漲幅、估值過高」的批評並存。
- **Buzz 量**：無法量化。repo 內 SOI 提及次數屬中低（serenity 系列單一來源 6 次），相較其他光學標的（如 MRVL、LITE、COHR）屬次要話題。
- **Tilt**：散戶／影響者端偏多（以 serenity 為代表），但社群原始資料缺失，信心低。

**主要主題（依現有資料）**
1. 光子 SOI（Photonics-SOI）營收放量：$25M 季收入 → 多年期 LTA 承諾約 $1.2B（來源為影響者引述，未獨立核實）
2. 共封裝光學（CPO）與 NPO 放量時點：2027 年起量、2028 年後高量
3. 估值過高與「光學敘事透支」批評（UBS、Substack 文章）
4. 產能預訂與現金押金（80% 產能協議）的品質

## Insider activity

Net 6mo: 資料不可得（yf insider 回傳空值）。無法判斷 CEO / CFO 或其他內部人近六個月買賣淨額。需在 Euronext 或 AMF 公告系統補查。

## Ownership shifts

major_holders / inst_holders 皆為空，無法評估機構集中度趨勢。

## Net sentiment score

- **分析師端**：中性偏謹慎（Hold 共識，近期降評多於升評，資料過期）
- **散戶／影響者端**：偏多（serenity 等影響者仍持多頭立場，但 11-19 單次標記為 bear）
- **綜合**：**中性（Neutral）**，信心 **低**。原因：分析師與影響者資料皆有重大缺口，且 Reddit／StockTwits 完全缺失。

**Divergence flag：是（tentative）**。影響者與部分散戶論述偏多，而券商端共識為 Hold 並伴隨 UBS Sell 與近期降評，兩端方向相反。此訊號在資料補齊前不應過度解讀。

SENTIMENT REPORT COMPLETE
