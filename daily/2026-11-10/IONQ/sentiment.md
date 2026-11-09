# Sentiment — IONQ as of 2026-11-10

## Analyst consensus
13 家（rec_summary 當期）: 1 strong buy / 10 buy / 2 hold / 0 sell / 0 strong sell，偏多結構。
近四期趨勢: buy+strong buy 由 -1m 的 12 家降至當期 11 家，hold 維持 2 家，sell 維持 0 家。工具回傳為彙總計數，未列出個別升降評等事件。

新聞側補充（WebSearch 取得，日期不一，未逐筆核對原始報告）:
- Morgan Stanley 目標價降至 43 USD，評等 equal-weight。
- B. Riley 下調目標價。
- Weiss Ratings 給予 Sell，評等 D-。
- 有來源列出平均目標價 63.33 USD、評等「Moderate Buy」，與上列 Morgan Stanley 降目標價存在明顯分歧，數字需另行核對。

Recent moves: 分析師整體仍偏多，但目標價有下修跡象；評等面與目標價面的方向不完全一致。

## Retail social
- Reddit: 無法取得。r/wallstreetbets 與 r/stocks 的 JSON 搜尋皆被拒絕（WebFetch 無法連線 www.reddit.com），本期無法量測討論量與多空傾向。
- StockTwits / X: StockTwits 因 api.stocktwits.com DNS 無法解析而失敗，需於 session 網路設定中允許該網域後才能重試。X 端僅有新聞型網站與財經部落格，無法區分散戶貼文。
- 新聞與文章語氣（代理指標，非散戶原始貼文）: 10 月底至 11 月初偏空，標題多為「下跌 32% 一個月」「稀釋疑慮」「虧損持續」；11 月 5 日 Q3 財報後轉為偏正面，標題多為「beat and raised」「股價大漲」。
- Sample 新聞標題（≤15 字引述）: "IonQ Just Dropped 32% In a Month: Is IONQ Stock Hopeless or Ready for a Rebound?"（247wallst, 2026-11-03）
- Sample 新聞標題: "IonQ Beat and Raised. Can the Quantum Stock Buck the Tech Selloff?"（247wallst, 2026-11-06）
- Buzz volume: 無法量化（社群來源全部失效）。以新聞數量判斷，11 月初前後報導密度明顯高於平常，但無基準值可比。
- Themes:
  1. 股權稀釋與持續虧損（主要空方論點）
  2. Q3 營收大幅成長與上調 2026 全年指引（主要多方論點）: Q3 營收約 173.8M USD、年增約 336%；2026 全年指引上修至 505M–515M USD。以 Q3 年化粗估約 695M USD，與全年指引非直接矛盾（前幾季基數較低），但仍屬二手報導數字，未經 SEC 文件驗證。
  3. 量子板塊同步拋售（RGTI、QBTS、QUBT 等同業連動）
  4. 技術面: 財報前跌破 50 日與 200 日均線，財報後反彈。

## Insider activity
統計區間: 2026-05-10 至 2026-11-10（6 個月）。資料來源 yf insider（101 筆總紀錄，最早 2024-12-11，最新 2026-09-10）。

Net 6mo: 買入 0 USD（無公開市場買進）/ 賣出約 0.60M USD（4 筆，共 11,736 股）/ 另有董事股票獎勵 7 筆（共 33,710 股，無現金價值）。

| 日期 | 申報人 | 職位 | 交易 | 股數 | 金額 (M USD) |
|---|---|---|---|---|---|
| 2026-06-18 | RAYMOND JOHN W. | Director | 賣出 @55.01 | 約 3,814 | 0.21 |
| 2026-06-18 | CHOU KATHRYN K | Director | 賣出 @55.02 | 約 2,757 | 0.15 |
| 2026-06-18 | TOLEDANO GABRIELLE B | Director | 賣出 @55.01 | 約 2,757 | 0.15 |
| 2026-09-10 | RAYMOND JOHN W. | Director | 賣出 @37.21 | 2,407 | 0.09 |

註: 6 個月內無 CEO / CFO 交易紀錄; 所有賣出均為董事層級。獎勵股（2026-06-17 與 2026-08-24）為董事例行授予，不計入買賣淨額。

Notable: 董事 RAYMOND JOHN W. 於 6 月與 9 月兩次賣出，為區間內唯一重複賣出者。

Ownership: 內部人持股約 0.66%；機構持股約 48.1%，機構數約 1,037 家。目前僅有單期快照，無法判斷機構集中度趨勢。

## Net sentiment score
Composite: **中性偏多 (neutral-to-bullish)**，信心 **低**。

依據:
- 分析師面偏多（11 買 / 2 持 / 0 賣），但目標價有下修，評等與目標價不完全同向。
- 散戶面無法量測（Reddit、StockTwits 失效），此項缺漏是信心偏低的主因。
- 內部人面偏中性: 無公開市場買進，3 次董事賣出金額小（合計約 0.60M USD），董事獎勵屬例行。
- 新聞語氣由財報前偏空轉為財報後偏多，但時間窗口短，且含二手來源數字。

Divergence flag: **無法判定**。散戶端資料缺失，無法確認散戶傾向是否與分析師相反。若以新聞語氣代替，財報後兩者方向大致同為偏多，無明顯背離。

Data gaps and caveats:
- Reddit 兩個 subreddit 與 StockTwits 皆無資料，需網路權限或後續重試。
- 新聞來源日期標示不一致（部分頁面為舊日期或 stale 日期）；財報日期有來源寫 11 月 5 日、另一來源寫 11 月 9 日，本報告以 11 月 5 日為準（多數來源指向已發布）。
- 分析師平均目標價 63.33 USD 與 Morgan Stanley 目標價 43 USD 的分歧，尚未核實。
- 所有資料以 2026-11-10 為準，未使用之後日期的資料。

SENTIMENT REPORT COMPLETE
