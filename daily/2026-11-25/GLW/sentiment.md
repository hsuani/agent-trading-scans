# Sentiment — GLW as of 2026-11-25

資料說明: yf 來源為 cache fallback (Yahoo cookie/crumb 連線失敗)。Reddit 與 StockTwits 無法取得 (詳見下方 DATA_UNAVAILABLE)。WebSearch 為單次搜尋，來源為媒體與評論文章，時效與可靠度不一。

## Analyst consensus

yf rec_summary (共 19 家):

| 評等 | 家數 | 占比 |
|---|---|---|
| Strong Buy | 1 | 5.3% |
| Buy | 14 | 73.7% |
| Hold | 4 | 21.1% |
| Sell | 0 | 0.0% |
| Strong Sell | 0 | 0.0% |

- Buy 合計 15/19 = 78.9%，Hold 21.1%，Sell 0%。
- 近 4 個月趨勢 (yf): 買方家數 12 (−3m) → 13 (−2m) → 14 (−1m) → 15 (0m)；Hold 4 → 5 → 4 → 4。買方家數緩步增加，Hold 持平。
- 近期評等變動 (WebSearch 二手來源，yf recommendations 僅回傳彙總計數，無逐筆升降評歷史，故未能以主來源驗證):
  - 11/05 Fox Advisors 由 Equal Weight 升至 Overweight。
  - 11/09 Bernstein 目標價由 $140 降至 $120，維持 Market Perform。
  - 11/11 Jefferies 首次覆蓋，給予 Buy，目標價 $134。
- 目標價 (二手彙整): UBS $192 (Buy)、Truist $175 (Buy)、Morgan Stanley $155 (Equal-weight)、Jefferies $134 (Buy)、Bernstein $120 (Market Perform)。區間 $120–192，且近期出現下修。
- 來源差異: Investing.com 近 3 個月彙總為 11 Buy / 2 Hold / 1 Sell，與 yf 的 0 Sell 不同。本表以 yf 為準，差異留存備查。

## Retail social

- Reddit: DATA_UNAVAILABLE。r/stocks 與 r/wallstreetbets 查詢均被 WebFetch 拒絕連線，未取得樣本、聲量與傾向。
- StockTwits: DATA_UNAVAILABLE。api.stocktwits.com 無法解析網域，需在 session 網路設定中允許該網域後才能重試。
- X / 新聞與評論 (WebSearch，非社群貼文，僅作參考):
  - Motley Fool (2026/09/30): 解讀 Corning 股價下跌原因。偏空。
  - Seeking Alpha 評論 "Corning: Not Worth The AI Risk (Rating Downgrade)": 降評文章。偏空。
  - Simply Wall St 敘事: 貿易政策變動與科技需求挫折將限制未來潛力。偏空。
  - StockTwits 新聞 (Jefferies): AI 資料中心建置可望帶動光通訊業務成長。偏多。
  - Investing.com 技術指標日訊號 "Strong Sell" (日期不明)。偏空。
- 聲量: 無 Reddit 與 StockTwits 數據，無法與歷史基準比較。僅能確認近期有數篇評論與新聞。
- 傾向: 混合偏空 (信心: 低)。此為媒體與評論文章的傾向，不能視為散戶情緒。
- 主要主題:
  1. AI 資料中心與光通訊 (Optical) 成長題材 (偏多)。
  2. 股價自高點大幅回落，目標價下修 (偏空)。
  3. 貿易政策與科技需求疑慮 (偏空)。
  4. 技術面 "Strong Sell" 訊號 (偏空)。
- 價格資料衝突: 網頁彙整的股價 ($255.69 於 6/29、$112.13 於 11/10、$94.38 於 11/21) 彼此來源不一且互相矛盾，本報告不採用。改以 yf insider 成交價作參考: 2026 年 5 月約 $184–207，9 月約 $151–152，顯示股價區間明顯下移。

## Insider activity

6 個月窗口: 2026-05-25 至 2026-11-25。

| 日期 | 內部人 | 職稱 | 交易性質 | 股數 | 金額 (USD M) |
|---|---|---|---|---|---|
| 2026-06-09 | WEEKS WENDELL P. | CEO | 公開市場賣出 @ $186.46 | 100,000 | 18.65 |
| 2026-06-09 | WEEKS WENDELL P. | CEO | 選擇權行權 @ $27.03 | 100,000 | 2.70 (行權價值，不計入賣出) |
| 2026-08-28 | STEVERSON LEWIS A | Officer | 賣出 @ $151.29 | 13,100 | 1.98 |
| 2026-09-04 | GULLO MICHELLE L | Officer | 賣出 @ $152.29 | 9,874 | 1.50 |

- Net 6mo: 公開市場買入 $0 M；公開市場賣出 $22.13 M (18.65 + 1.98 + 1.50)。
- 驗算: 100,000 股 × $186.46 ≈ $18.65 M，與 yf 金額一致。
- 6/09 CEO 行權與賣出股數相同，推斷為行權後即賣出，非新增持股。
- notable: CEO Wendell P. Weeks 於 6/09 賣出 100,000 股 (約 $18.65 M)，為窗口內金額最大的一筆。
- 一年期觀察: yf 自 2025-02 起所有附金額的公開市場交易皆為賣出，未見任何 Purchase 紀錄，且多位高階主管 (CEO、CFO、COO、CTO) 持續賣出。此為長期偏空的結構性訊號，但部分賣出可能與薪酬與行權安排有關，訊號強度有限。
- 窗口外邊界: 2026-05-22 CTO Jaymin Amin 賣出 27,395 股 @ $192.14 (約 $5.26 M)，不計入本窗口。
- 無金額且無文字說明的紀錄 (多為 2026-02 與 2026-04 的例行申報) 性質無法由 yf 判定，未計入。

## Ownership

- 機構持股: 72.96% (占總股本)，占流通股 79.42%，機構家數約 3,000。
- 內部人持股: 8.14%。
- 趨勢: DATA_UNAVAILABLE。yf major_holders 僅提供單一時點快照，無時間序列，13F 增減亦未取得。機構集中度目前屬高，變化方向不明。

## Net sentiment score

| 來源 | 傾向 | 信心 | 依據 |
|---|---|---|---|
| 分析師 | 偏多 | 中高 | 78.9% Buy、0 Sell；目標價 $120–192 但近期下修 |
| 內部人 | 偏空 | 中 | 6 個月 0 買、$22.13 M 賣；一年來無買入紀錄 |
| 零售 (Reddit/StockTwits) | DATA_UNAVAILABLE | - | 來源無法連線 |
| 媒體與評論 | 混合偏空 | 低 | 降評、下修與技術面偏空，AI 光通訊題材偏多 |
| 機構 | 持平 (資料不足) | 低 | 持股占比高，趨勢缺資料 |

- 綜合: 中性 (信心: 低)。分析師偏多與內部人持續淨賣出並存，媒體評論偏空，零售端無資料可參考。
- 背離旗標: 是 (有條件)。分析師偏多方向與內部人淨賣出及媒體評論偏空方向相反。零售端無資料，無法確認散戶是否與媒體同向，此判斷需待 Reddit 與 StockTwits 資料補齊後確認。

## 資料缺口與注意事項

- Reddit: WebFetch 拒絕連線 (reddit.com 無法存取)，DATA_UNAVAILABLE。
- StockTwits: api.stocktwits.com 網域解析失敗，DATA_UNAVAILABLE，需在 session 網路設定允許後重試。
- yf: Yahoo cookie/crumb 取得失敗，使用 cache fallback。
- 日期: 今日為 2026-11-24，分析日為 2026-11-25。yf 資料可能停留在前一交易日快取。
- 機構趨勢、逐筆評等歷史、分析師目標價皆無主來源驗證，已標註來源。

SENTIMENT REPORT COMPLETE
