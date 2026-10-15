# Sentiment — CEG as of 2026-10-15

資料說明：分析師評級與內部人資料來自 `pipeline/tools/yf`（Yahoo 即時來源被擋，走 repo cache，屬正常）。散戶情緒僅能用 WebSearch 取得間接結果。Reddit（r/wallstreetbets、r/stocks）與 StockTwits 直接 API 在本環境不可用，未取得原始貼文，相關段落標示為 DATA_UNAVAILABLE 或以搜尋摘要代替。多數搜尋結果的日期早於 10-15，部分未標註日期，下文已逐一標明。

## Analyst consensus

目前分析師共 22 家：6 Strong Buy / 13 Buy / 3 Hold / 0 Sell / 0 Strong Sell。即 19 家買進或以上（約 86%），3 家持有，無賣出評級。

評級分布近四個月幾乎沒有變動。近 3 個月前（-3m）為 6 SB / 14 B / 3 H，共 23 家；目前少了 1 家 Buy，覆蓋家數同時減 1，較像是覆蓋調整而非明確降評。yf 的 recommendations 欄位只給彙總計數，沒有個別的升降評事件與目標價變動明細，因此無法確認具體券商的升降評與目標價調整。

搜尋摘要中可見的個別券商動作（日期不明或早於 10-15，僅供參考）：
- Mizuho 將目標價由 $335 上調至 $390（來源未標日期）。
- Morgan Stanley 維持 Overweight，目標價上調至 $369（約 9 月 StockTwits 報導引述）。
- Benzinga 與 Walnut 的平均目標價約 $348 至 $353（8 月數據）。
- 各家統計口徑不一：Barchart 為 16 SB / 1 Moderate Buy / 5 Hold（22 家），Walnut 為 20 Buy / 3 Hold / 0 Sell（21 家）。以 yf 的 22 家數據為準。

股價參考：搜尋中最近的價格點是 8 月中約 $282.50（Benzinga）。Barchart 稱 2026 年迄今下跌約 25.4%，但未標日期。10-15 的即時股價未能驗證，本報告不以價格做判斷。

## Retail social

- Reddit：DATA_UNAVAILABLE。WebSearch 未找到 r/wallstreetbets 或 r/stocks 上針對 CEG 的討論串。僅有 Yahoo/Insider Monkey 文章把 CEG 列為「Reddit 上的成長股」之一，但沒有貼文、留言數或語氣細節，不能當作 Reddit 情緒證據。
- StockTwits / X：
  - 最近的 StockTwits 文章（9 月 20 日）指散戶情緒「bearish」，當時訊息量 24 小時內增加約 75%，並提到 CEG 年初至今下跌超過 7%。這是本次搜尋中最接近 10-15 的平台內數據，但已距今約 25 天。
  - AltIndex 顯示 StockTwits 情緒分數 100/100（Bullish），日均提及約 41 則，較三個月前增加約 128%。此數據未標日期，與 9 月的 bearish 讀數相衝突，可信度較低。
  - X 上的摘要（Nasdaq 整理）提到 Q1 財報表現與近一個月股價大幅上漲，以及異常的選擇權成交，但該摘要為 AI 生成，未能逐一核對原文。
  - 未能取得可引用的原始貼文，因此沒有可直接引用的散戶原話。
- 聲量（相對數量）：偏高。依 AltIndex 的相對成長數字判斷，近期討論量明顯高於三個月前，但沒有絕對的 10-15 當日提及數。
- 主要話題（依搜尋結果歸納）：
  1. Q2 2026 財報優於預期，全年調整後營運獲利指引上修至 $11.50 至 $12.50 每股。
  2. 政策風險：1 月川普提出緊急批發電力拍賣，當時股價下跌超過 9%，仍是散戶與媒體提到的風險點。
  3. 估值與「被低估」論：Cramer 稱目前價位「decent value」（日期不明）。
  4. 空單比例低：Benzinga 數據為 float 的 3.3%（未標日期）。

## Insider activity

視窗：2026-04-15 至 2026-10-15（近 6 個月）。

- 公開市場買入（Purchase）：合計約 $418K（1 筆）。
  - Roger W. Crandall（Director）於 2026-08-11 以每股 $278.62 買入 1,500 股，約 $418K。這是本視窗內唯一的公開市場交易。
- 公開市場賣出（Sale）：0 筆。
- 授予股票（Stock Award / Grant，非市場交易）：
  - Crandall 於 2026-08-04 獲授 462 股（約 $123K，每股 $267.25）。
  - 10 位董事於 2026-04-28 各獲授 556 股（每股 $305.71，每人約 $170K），屬年度董事薪酬。
- 高階主管：CEO Joseph Dominguez 持股約 191,817 股（yf 顯示無近 6 個月交易紀錄）。CFO Daniel Eggers 持股約 44,601 股。這些主管於 2026-02 的紀錄 Value 為空，交易代碼也空白，無法判定是否為股權歸屬扣繳或賣出，但因日期早於視窗（2 月），不計入本期淨額。

淨額：6 個月內公開市場淨買入約 $418K，淨賣出 $0。
Notable：Roger W. Crandall，Director，2026-08-11 買入 1,500 股，每股 $278.62。是本期唯一的公開市場交易，且為董事（非 CEO/CFO）。金額與公司市值相比很小，訊號強度有限。

## Ownership shifts

- 機構持股比例：約 83.0%（institutionsPercentHeld 0.8297），機構家數 2,456。
- 內部人持股比例：約 0.34%。
- yf 只提供單一時點快照，沒有季度趨勢，因此無法判斷機構集中度是上升或下降。這是資料缺口。

## Net sentiment score

綜合判斷：偏多（bullish），信心中等偏低。

| 面向 | 判斷 | 信心 | 依據 |
|---|---|---|---|
| 分析師 | 強烈偏多 | 高 | 19/22 為 Buy 以上，0 賣出，評級穩定 |
| 內部人 | 小幅偏多 | 中 | 6 個月 $418K 董事公開買入，無賣出 |
| 散戶 | 中性偏空至分歧 | 低 | 最近 StockTwits 讀數 bearish（9 月），但另一來源 bullish（日期不明）；Reddit 無資料 |
| 籌碼 | 中性 | 低 | 機構持股高，無趨勢資料 |

Divergence flag：是（有條件）。分析師與內部人偏多，但最近一筆可查的 StockTwits 散戶讀數為 bearish，二者方向相反。不過散戶端資料過舊（9 月）、來源互相矛盾，且沒有 Reddit 資料，因此這個背離訊號只能當作弱提示，不宜視為確認。

資料缺口與限制：
1. Reddit 無法取得，散戶面向信心因此降低。
2. StockTwits 最新讀數距今約 25 天，且與 AltIndex 矛盾。
3. 分析師券商級升降評與目標價變動明細缺失，只有彙總計數。
4. 10-15 當日股價未驗證，搜尋中的價格與百分比多為 8 月前後或未標日期。
5. 機構持股沒有趨勢數據。

SENTIMENT REPORT COMPLETE
