# Sentiment — PWR (Quanta Services) as of 2026-10-15

## Analyst consensus
目前 31 位分析師中 25 買進 (含 1 Strong Buy) / 5 持有 / 1 賣出 (Strong Sell)。
近 3 個月趨勢: 買進端由 22 增至 25，持有由 7 降至 5，賣出端維持 1 家不變，屬溫和上調趨勢。
近期動向 (WebSearch 彙整，時間點不完全一致):
- Bernstein SocGen 升級至 Buy，目標價 $775 (2026-09 底)。
- Piper Sandler 維持 Buy，目標價 $714 (2026-09)。
- UBS 目標價 $900 Buy (2026-08)，為目前列出的最高目標價。
- 平均 12 個月目標價: Investing.com 約 $769 (2026-09)，Barchart 約 $809 (2026-08)，StreetInsider 近 12 個月平均約 $683，三者落差大，建議以區間看待。
- yf 工具的 recommendations 欄位僅回傳月度彙總，無個別升降評等明細，故個別 upgrade/downgrade 以 WebSearch 結果為準。

## Retail social
- Reddit: 直接抓取 r/wallstreetbets 與 r/stocks 的 JSON 端點依規定不採用 (改以 WebSearch)。WebSearch 未找到與 PWR 相關的 Reddit 討論串，無法判定 Reddit 語氣。SentiSense 的來源拆分顯示 Reddit 屬中性，但樣本量不足以作為依據。 **DATA_UNAVAILABLE (Reddit 直接樣本)**
- StockTwits / X: 未取得 StockTwits 訊息或 X 貼文原始樣本 (WebSearch 未回傳)。SentiSense 30 日評分 6.82 (標示 bullish 且回升, 2026-08-09)，提及量約每日 14 則，其中新聞佔 78%、X 佔 9% 且偏多。CFGI 每日情緒指數 2026-09 平均為 47 (中性)，三個月平均 44。
- 聲量 (qualitative): 整體屬中低，約每日十餘則量級，遠低於高熱度 AI 基礎建設題材股，主要聲量來自新聞與分析師報導而非散戶社群。
- Tilt: 社群側整體 **偏多但低信心** (主要受新聞情緒驅動，散戶原生貼文樣本缺失)。
- 主要敘事 (取自 WebSearch 之財經頁與分析文章，非直接社群貼文):
  - 多方: AI 資料中心相關電力與基礎建設需求，record backlog (TipRanks 引述 $48.5B)，2026 全年營收與 adjusted EPS 指引上調 (營收指引 $39.5B、EPS $16.70)，2026 Q2 財報後股價大漲約 17%。
  - 空方: 估值相對 EPC 同業溢價約六成 (TipRanks)；能源政策變動可能拖慢再生能源建置。
  - 股價動能: 2026 年迄今約上漲 57% 至 60%，距 52 週高點 $788.75 約 14% (2026-10-02 快照)。

## Insider activity
查詢區間 2026-04-15 至 2026-10-15 (6 個月)。
Net 6mo: $0 公開市場買進，約 $123.2M 公開市場賣出。
- 2026-05-05: CEO Earl Charles Austin Jr 賣出 155,992 股，成交價 $765.14–777.60，約 $120.2M (為本區間最大單筆)。同日另有 4,008 股贈與 (non-cash)。
- 2026-05-04: Officer Paul M. Nobel 賣出 4,000 股，$756.98，約 $3.0M。另有 45 股贈與。
- 2026-05-28: Director Bernard Fried 4,823 股 (無價格資訊，性質待確認，可能為董事薪酬股)。
- 2026-05-11: Director Martha B. Wyrsch 贈與 2,500 股。
- 2026-06-01: 多位董事各 559 股 (與 870 股之 Beneby) 之 D 類持股，無金額，推測為年度董事股權授予。
- 2026-02-26 之 CFO、CEO、General Counsel 等股權授予 (ex. CEO 90,154 股) 超出 6 個月窗口，未計入。
解讀注意: 區間內無任何公開市場買進。最大賣出為 CEO 單筆，且發生於 5 月中旬附近的高價區。是否屬 10b5-1 預定計畫無從判定。資料末筆為 2026-06-01，6 月至 10 月之內部人交易未出現在來源中，可能為快取資料落後，需以 SEC Form 4 核對。

## Ownership shifts
- 機構持股 94.04% (float 94.68%)，機構數 2,567 家；內部人持股 0.67%。
- 本次僅取得單一快照，無法判定機構集中度的季度趨勢。ownership 為高度機構化結構，屬常態，非本次信號。

## Net sentiment score
Composite: **偏多 (bullish)，信心中等**。
- 分析師: 偏多，信心高 (25/31 買進，買進端近 3 個月增加，目標價區間仍高於現價)。
- 散戶/社群: 偏多至中性，信心低 (SentiSense 偏多、CFGI 中性，Reddit/StockTwits 樣本缺失)。
- 內部人: 偏空訊號 (6 個月內無公開買進，CEO 大額賣出約 $120M)，但需排除 10b5-1 與稅務用途的可能，信心中低。
- 扣分因素: 估值溢價、內部人大額出售、以及資料來源時間點分散 (8 月至 10 月) 造成的不確定性。

Divergence flag: **是 (內部人與分析師方向相反)** — 分析師與散戶語氣皆偏多，但內部人在高價區有大額淨賣出。
- 散戶 vs 分析師: 否 (兩者方向一致，皆偏多)。
- 內部人 vs 分析師: 是 (需留意)。

## Data notes
- yf 工具之 recommendations 與 rec_summary 回傳相同月度彙總，無逐筆評等變化。
- Cookie/crumb 取得失敗，但資料仍可回傳 (cache 來源屬正常)。
- 股價資料來源間不一致: Investing.com 引用 $651.79 (日期不明)，trade-ideas 2026-10-02 快照暗示約 $678，insider 交易價位約 $757–777 (5 月)。解讀目標價上行空間時請先確認當日報價。
- Reddit、StockTwits 直接端點未依指示使用；WebSearch 未回傳 X 原始貼文。
- 來源 (WebSearch):
  - https://www.barchart.com/story/news/3969715/are-wall-street-analysts-bullish-on-quanta-services-stock
  - https://www.streetinsider.com/rating_history.php?q=PWR
  - https://www.investing.com/equities/quanta-services-consensus-estimates
  - https://www.tipranks.com/stocks/pwr
  - https://www.tipranks.com/stocks/MX:PWR
  - https://app.sentisense.ai/stocks/PWR/sentiment
  - https://www.benzinga.com/quote/PWR/sentiment
  - https://www.trade-ideas.com/stock-info/PWR/
  - https://cfgi.io/quanta-services-stock-monthly-report/

SENTIMENT REPORT COMPLETE
