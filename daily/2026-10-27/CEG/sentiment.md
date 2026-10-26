# Sentiment — CEG as of 2026-10-27

> 註：本報告 DATE 依任務指定為 2026-10-27，執行當日系統日期為 2026-10-26。Analyst 與 insider 數據為 pipeline 當下拉取值；網路新聞多數無明確日期，視為參考。

## Analyst consensus
25 家覆蓋：6 Strong Buy / 15 Buy / 4 Hold / 0 Sell / 0 Strong Sell（yf rec_summary，period 0m）。
近三個月趨勢：Buy 類（含 Strong Buy）由 -3m 的 20 家 → -2m 的 19 家 → -1m 的 19 家 → 本期 21 家；Hold 由 3 → 3 → 3 → 4。Sell 始終為 0。
Recent moves：yf `recommendations` 回傳與 rec_summary 相同的彙總，無個別券商升降評等明細，無法列出逐家 upgrade/downgrade。
網路來源（日期不一，需留意）：
- Mizuho 將目標價由 $335 上調至 $390，維持 Neutral（日期未明）。
- Evercore ISI 目標價 $380（Google Finance 所示 10/1 設定）。
- Goldman Sachs Hold，目標價 $305。
- Investing.com 快照：20 Buy / 3 Hold / 0 Sell，平均 12 個月目標價約 $353；Barchart 另計 16 Strong Buy / 1 Moderate Buy / 5 Hold（22 家），與 yf 數字口徑不一，以 yf 為主。

## Retail social
- Reddit（r/wallstreetbets、r/stocks）：**資料缺失**。WebFetch 被拒，curl 經 proxy 回 403（CONNECT tunnel failed），依規則 soft-fail，未取得任何 thread 樣本與 tilt。
- StockTwits：**資料缺失**。api.stocktwits.com DNS 解析失敗（ENOTFOUND），無法取得訊息量與多空標籤。
- X / 新聞搜尋：找不到 2026-10 期間的 CEG 散戶討論串。一則聚合站點稱 Reddit 情緒偏多（78% 正向、熱度 27/100），但無法對應到具體貼文，且日期不明，僅作弱參考。
- 聲量（Buzz volume）：無法量化對比典型水準，定性判斷為「無法判定」。
- Themes（僅依新聞標題與聚合摘要歸納）：
  - 核能與資料中心電力需求的長期成長敘事（仍是分析師主要論據）。
  - 股價自高點回落後的估值爭論；Jim Cramer 等人認為「當前價位具價值」。
  - 電力批發拍賣與政策風險（先前一月因政府推動緊急批發電力拍賣而重挫）。
  - Q2 2026 財報超預期並上調全年調整後營運獲利指引至 $11.50–$12.50/股（Barchart 摘要）。

## Insider activity
過去 6 個月（約 2026-04-27 至 2026-10-27）：
- 公開市場買入：約 $0.42M（1 筆）。
- 公開市場賣出：0 筆。
- 淨額：約 +$0.42M（淨買）。

主要交易明細：
| 日期 | 人員 | 職位 | 交易 | 股數 | 金額（USD M） |
|---|---|---|---|---|---|
| 2026-08-11 | Roger W. Crandall | Director | 公開市場買入 @ $278.62 | 1,500 | 0.42 |
| 2026-08-04 | Roger W. Crandall | Director | 股票獎勵（Grant）@ $267.25 | 462 | 0.12 |
| 2026-04-28 | 董事會 10 位成員 | Director | 股票獎勵（Grant）@ $305.71 | 各 556（合計約 5,560） | 各 0.17（合計約 1.70） |

注意：
- 獎勵（Grant）屬董事薪酬，非市場買入，不計入淨買。
- 2026-02 的 CEO Joseph Dominguez、CFO Shane Smith、Daniel Eggers 等高階主管紀錄數值為空白，性質多為歸屬或扣繳，且均在 6 個月窗口之外，不計入。
- 聚合網站的一則摘要稱 6 個月內有 2 筆賣出，與 yf 紀錄不符，判定為過時資料，未採用。

## Ownership shifts
- 機構持股比例：82.9%（institutionsCount 2,465 家）。
- 內部人持股比例：0.34%。
- 本次僅有單一時點快照，無法判斷機構集中度趨勢（需要至少兩期比較）。
- CEO 直接持股約 191,817 股（yf 紀錄，日期 2026-02-09）。

## Net sentiment score
Composite：**偏多（bullish），信心中低**。
- 分析師：強偏多。25 家中 21 家買入評等、0 家賣出，近三個月買入家數小幅上升，Hold 由 3 增至 4，屬溫和分歧而非轉空。
- 內部人：小幅偏多。唯一公開市場交易為董事買入約 $0.42M，窗口內無賣出。
- 散戶：無資料，無法納入評分。
- 信心扣分原因：Reddit 與 StockTwits 皆取不到；網路共識數字來源間不一致；股價與目標價資料日期不明。

Divergence flag：**無法判定**。散戶 tilt 缺失，無法比較與分析師的方向是否相反。若後續取得散戶資料，應特別檢查「分析師偏多 + 散戶偏空」的組合。

資料缺口與後續建議：
1. Reddit 與 StockTwits 需在可連線的環境重跑，或改用其他來源（例如可授權的社群 API）。
2. 需要確認 2026-10-27 當日股價，目前可引用的股價資料最遲約為 10 月初（約 $268）。
3. 分析師逐家升降評等需要其他資料源（yf recommendations 本次僅回傳彙總）。

SENTIMENT REPORT COMPLETE
