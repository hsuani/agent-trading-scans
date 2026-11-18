# Sentiment — 6213.TW (聯茂 ITEQ) as of 2026-11-19

資料可得性總覽: Reddit 與 StockTwits 無法取得 (Reddit 抓取被拒, StockTwits 網域無法解析)。社群資料僅能由 WebSearch 摘要間接取得, 且無 PTT / Dcard 原文。內部人交易 (yf insider) 回傳空陣列, 無法確認。最新可查到的股價與營收資料止於 2026-11-12, 2026-11-13 至 11-19 無資料。

## Analyst consensus
yf rec_summary (4 個期間皆相同): 3 strong buy / 4 buy / 1 hold / 1 sell / 0 strong sell, 共 9 家, 其中 7 家偏買進、1 家持有、1 家賣出。

注意: 四個月份 (0m, -1m, -2m, -3m) 的數字完全相同, 疑似 yfinance 回傳的靜態快照而非逐月更新, 不宜當作近期評等變動的證據。recommendations 亦無近期 upgrade / downgrade 紀錄可辨識。

Recent moves: 無法從 yf 確認近期評等變動或目標價調整。WebSearch 找到的分析師資訊來源不一、日期多在 2025 年或更早, 其中一項聚合站顯示平均 12 個月目標價約 487.36 TWD, 但該站股價快照與其他來源差距很大, 僅供參考, 不能當作 2026-11 的共識。Simply Wall St 提到盈餘未達預期後分析師下修 EPS 估計 (日期不明)。

## Retail social
- Reddit: 無法取得 (r/stocks 搜尋抓取被拒)。r/wallstreetbets 未嘗試 (同一站點限制)。
- StockTwits / X: StockTwits 無法連線 (網域無法解析, 需於 session 網路設定允許 api.stocktwits.com)。X 上未找到可用的 2026-11 貼文。
- PTT / Dcard: 搜尋未找到相關討論串。
- CMoney 股市社群 (WebSearch 摘要): 意見分歧。有人提醒保持警覺、現階段不宜追高, 也有人看好 AI 新產品與 CCL 族群下半年的成長動能。摘要未提供貼文數與具體留言, 無法量化情緒比例。
- 注意股相關新聞 (wantrich / 時報, 2026-11-05 前後): 2026-11-04 被證交所列為注意股, 當日收盤 612 元。

Buzz volume: 無法與歷史基準比較。以新聞與媒體露出判斷, 11 月初因注意股處置與股價大跌而有明顯討論量, 屬於「偏高但以新聞驅動」, 不是散戶社群自發性的熱議。

Representative sample (來源摘要, 非原文): 「...看好其在 AI 領域的發展」 / 「現階段不宜追高, 市場仍有下跌風險」 (以摘要改寫, 未直接引用原文)。

Themes:
1. 營收高成長 (2026-10 月營收 60.36 億 TWD, 年增 119.5%; 前 10 月累計 423.26 億 TWD, 年增 57.2%)
2. 估值過高與注意股處置 (本益比偏高, 外資與三大法人近 5 日合計賣超)
3. CCL 族群與 AI 題材
4. 股價波動劇烈 (近 5 日跌約 21.34%, 11/12 單日跌 10%)

## Insider activity
Net 6mo: 無法確認 (yf insider 回傳空陣列, 可能是資料缺漏而非真的無交易; yf 認證失敗未補救)。
- 交叉檢查: yf major_holders 顯示 insidersPercentHeld 約 37.6%, 與 WebSearch 摘要中 histock 的董監持股約 19.66% (2026-05 至 2026-07 數值未變) 不一致, 兩者口徑可能不同, 尚未釐清。
- 2026 年董監增減持申報 WebSearch 未找到明細。建議至公開資訊觀測站 (MOPS) 查詢「董監事持股異動申報」以確認 6 個月內的買賣淨額與職務 (CEO / CFO / 其他董監)。

## Ownership shifts
- institutionsPercentHeld 約 7.9%; institutionsFloatPercentHeld 約 12.7%; 機構家數 48 (yf major_holders)。
- 機構持股趨勢: 無歷史序列, 無法判斷集中度變化方向。
- 外資近期 (11 月) 為淨賣超 (WebSearch 摘要: 近 5 日外資賣超約 1.19 萬張), 方向上為籌碼鬆動, 但無季度持股比例可對照。

## Net sentiment score
Composite: **中性偏空 (neutral-to-bearish), 信心低 (low)**

依據:
- 分析師面 (yf 快照): 偏多 (7/9 買進), 但資料疑似靜態, 權重降低。
- 散戶 / 社群面: 無法量化, 僅有分歧的 CMoney 留言與媒體報導; 未見明確偏多或偏空的主流敘事。
- 價格與籌碼面 (可作為市場情緒代理): 11 月初注意股處置、近 5 日跌約 21%、外資大幅賣超, 偏空。
- 基本面 (營收強勁) 為正面, 但估值面 (本益比在 37 至 95 之間, 因來源不同而不一致) 造成爭議。

Divergence flag: **yes (有條件)** — 分析師評等 (7/9 買進) 偏多, 而近期股價走勢與外資籌碼偏空, 兩者方向相反。但因 yf 評等為靜態快照, 且散戶面無有效資料, 此分歧信號的可靠度有限; 需待取得即時評等與 MOPS 內部人資料後再確認。

資料缺口與信心限制:
1. 社群 (Reddit / StockTwits / PTT) 皆無法取得, 散戶情緒為推論而非實測。
2. 內部人交易為空值且無法驗證。
3. 分析師評等四期相同, 疑似未更新。
4. 注意股前後的本益比來源數字不一致 (94.88 vs 37.34), 估值判斷需以官方資料再核對。
5. 最新價格資料止於 2026-11-12, 距 as-of 日 2026-11-19 有一週缺口。

SENTIMENT REPORT COMPLETE
