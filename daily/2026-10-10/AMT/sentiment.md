# Sentiment — AMT as of 2026-10-10

## Analyst consensus
yf rec_summary（最新期 0m）：**7 Strong Buy / 15 Buy / 3 Hold / 0 Sell / 0 Strong Sell**，合計 25 家。
相對 -3m：Strong Buy 由 6 增至 7，Hold 由 4 減至 3，Buy 持平，賣方評等仍為零。

近期動作（網路搜尋，來源為聚合站，日期與數字不完全一致）：
- 升級：Wolfe Research Peer Perform→Outperform（2026-07-09）；RBC Sector Perform→Outperform（2026-06-26）；Bernstein Market Perform→Outperform（2026-05-19）；Barclays 升級，目標 $198（2026-08-20，investing.com）。
- 降級：HSBC 由 Buy 降至 Hold，理由為估值，時點在 Q2 財報後（TipRanks/TheFly 標題，確切日期 DATA_UNAVAILABLE）。
- 目標價：Scotiabank $218→$220（Outperform）；BMO $190→$195（Market Perform，2026-07-29）；Goldman $215→$210（Buy）；JPMorgan $250→$255（Overweight）；TD Cowen 上調至 $227。
- 共識目標價：investing.com 平均約 $215.70（高 $260、低 $188）；Benzinga 約 $226（19 家）。
- 所有來源均指向共識偏多（Moderate Buy 至 Buy）。

## Retail social
- **Reddit**：r/wallstreetbets 與 r/stocks 的 JSON 搜尋皆被擋（無法擷取），無法取得貼文樣本與語氣。網路搜尋也未找到 AMT 相關 Reddit 討論串。**DATA_UNAVAILABLE**
- **StockTwits**：API 網域無法解析（DNS 失敗），soft-fail。**DATA_UNAVAILABLE**
- **X / 新聞輿論**：網路搜尋未找到可引用的近期散戶貼文，只有分析師與數據站內容。**DATA_UNAVAILABLE**
- **聲量**：無法估計相對典型水準的提及次數。**DATA_UNAVAILABLE**
- **Themes（從媒體與分析師文字歸納，非散戶原文）**：
  - 多方論點：碳體、租約期限長且具防禦性；營運商擴充網路容量需求；Q1 財報優於預期，FFO 全年指引約 $10.90–11.07。
  - 空方論點：EchoStar/DISH 租約取消與訴訟；營運商整併造成租戶流失；利率敏感（REIT 特性）；再融資成本；部分分析師認為估值偏高（HSBC 降評理由）。
  - 管理層表示對 EchoStar 訴訟仍開放庭外和解。
- **Tilt**：散戶面無資料，無法判定。

## Insider activity
yf insider（6 個月窗口：2026-04-10 至 2026-10-10，不含零價格股票授予與贈與）：
- **買入**：1 筆，合計約 **$0.50M**（Rajesh Kalathur，董事，2026-08-21，2,829 股，@ $177.00）。
- **賣出**：3 筆，合計約 **$1.38M**
  - Robert J. Meyer Jr.（Officer）2026-07-29，5,000 股，@ $178.89，約 $0.89M
  - Ruth T. Dowling（General Counsel）2026-07-29，1,791 股，@ $169.54–174.96，約 $0.31M
  - Ruth T. Dowling（General Counsel）2026-04-29，972 股，@ $177.54–178.48，約 $0.17M
- **淨額**：約 **-$0.88M**（小額淨賣）。
- **窗口外的重要大額賣出**（2026-02 至 2026-03，多為期權行權後賣出）：CEO Steven Vondran 2026-03-04 賣出約 $6.31M（另有 $3.17M 行權）；COO Eugene Noel 2026-03-02 賣出約 $7.87M（另有 $3.90M 行權）；CFO Rodney Smith 2026-02-17 賣出約 $6.60M（另有 $3.25M 行權）。此類交易伴隨行權，屬例行性質，但規模大，需留意。
- **例行授予**：2026-10-01 General Counsel Paul Blanchett 授予 16,299 股（零價格，不計入淨額）；2026-03-10 多位高管與董事授予股票。
- 解讀：CEO/CFO 近 6 個月無公開市場買入；唯一買入來自董事 Kalathur（2026-03 與 2026-08 兩次買入，合計約 $1.0M）。

## Ownership shifts
- 機構持股 **96.8%**（institutionsCount 2,387）；內部人持股 **0.08%**。
- 持股集中度的時間序列 **DATA_UNAVAILABLE**（yf 僅提供當期快照，無法判斷增減趨勢）。

## Net sentiment score
**Composite：偏多（信心：中低）**
- 分析師面：偏多，評等結構穩定，近期淨升級，無賣方評等。權重高。
- 內部人面：小幅淨賣，但多為行權後賣出，且有董事小額買入。中性偏弱。
- 散戶面：**無資料**，無法納入評分。
- 股價面（參考）：最近可得報價約 $175–176（2026-08 資料），52 週區間來源不一（$160–199 或高點 $234.33）。最新價格 **DATA_UNAVAILABLE**（見 market.md 以取得實際快取價格）。

**Divergence flag：無法判定**（散戶資料缺失）。若散戶亦偏多，則為同向；若散戶偏空，則為分歧。

**重要事件**：財報日期來源不一致，investing.com 為 2026-10-22，stockanalysis 與 nemo.money 為 2026-10-27，需以公司 IR 頁面確認。財報落在當前日期之後數日內，會放大上述評等與情緒的變化。

## 資料來源
- yf：`rec_summary`、`recommendations`、`insider`、`major_holders`（連線至 Yahoo cookie/crumb 失敗，數據為快取，已依規定 fallback）
- WebSearch：Yahoo Finance、investing.com、Benzinga、MarketBeat、TipRanks/TheFly、tikr、Barchart、stockanalysis.com 等聚合來源（部分為二手摘要，日期與數字不一致）
- Reddit JSON 與 StockTwits：無法存取（soft-fail）

SENTIMENT REPORT COMPLETE
