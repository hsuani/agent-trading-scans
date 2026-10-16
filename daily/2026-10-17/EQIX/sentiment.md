# Sentiment — EQIX as of 2026-10-17

## Analyst consensus
34 家覆蓋：5 strong buy / 23 buy / 6 hold / 0 sell / 0 strong sell（買進評級占 82%，無賣出評級）。
近 3 個月趨勢：買進側由 26 家（-3m）增至 28 家（0m），hold 固定 6 家，sell 始終為 0；覆蓋家數由 32 增至 34。
Recent moves：`yf recommendations` 只回傳彙總計數，沒有個別券商升降評等明細，因此無法列出具體 upgrade / downgrade。網路搜尋補充到的近期事件：
- Q2 財報優於預期，上調 2026 年 EPS 指引；但第三季營收指引為 $2.5–2.6B，中位數略低於 $2.6B 的市場共識。
- TD Cowen 重申 Buy，目標價上調至 $1,166。
- Cantor Fitzgerald 於 2026-07-30 有偏多論述（MarketBeat 標題為 "expected to rise"），未取得原始評等與目標價細節。
- 目標價的整體分布（平均/中位數/高低區間）本次工具未提供，無法量化。

## Retail social
- Reddit（r/wallstreetbets、r/stocks）：本次 WebSearch 未找到任何 EQIX 相關討論串，無法取樣熱門討論串，也無法判斷情緒傾向。依規定不以 WebFetch 直接抓取 Reddit，故此項資料缺漏。
- StockTwits：未取得近期串流資料，不可用。
- X / 第三方聚合站：
  - NAGA 頁面（資料時點 2026-09-30）：crowd sentiment 標示為「負向」，短線訊號為「偏空」；但同頁 blogger 意見為 68% 偏多 / 32% 偏空，investor sentiment 標示為「正向」。同一頁面內部說法不一致，可信度低。
  - SentiSense（2026-08-09 快照）：30 天情緒「略偏多，但較一個月前降溫」；約 13 則/日提及量。來源分布：News 79% bullish、Reddit 8% bullish、X 6% bullish。該站數字與樣本規模未揭露，僅供參考。
- 提及量相對基準：缺乏歷史基準線，無法判定相對於典型水準是高或低，只能說目前可取得的資料顯示討論量不高（約每日十餘則）。
- 本次沒有可直接引用的 Reddit / X 原文，因此不附引述。
- 主題（依第三方摘要歸納，非直接取樣）：
  1. AI / 雲端需求帶動資料中心租賃與互連（interconnection）成長。
  2. 利率敏感度與 REIT 估值之爭。
  3. 第三季營收指引偏保守是否為短期壓力。
  4. 高股價（約 $1,000 以上）下的估值疑慮。
- Retail 傾向：混合偏空（以 NAGA 的 crowd 標示為主）與部分偏多（blogger / news 端）並存，資料品質低。

## Insider activity
Net 6mo（2026-04-17 至 2026-10-17）：$0 買進 / 約 $20.4M 賣出（13 筆，以 Yahoo 回傳「Sale at price」為準）。無公開市場買進紀錄。另有若干無金額（Value 為 null）的申報，多半為股權激勵歸屬或稅務扣繳，未計入上述金額。

主要交易（6 個月內）：

| 日期 | 人員 | 職稱 | 方向 | 股數 | 金額 |
|---|---|---|---|---|---|
| 2026-09-04 | Paladin, Michael Shane | Officer | 賣出 | 307 | $0.32M |
| 2026-09-02 | Paladin, Michael Shane | Officer | 賣出 | 203 | $0.21M |
| 2026-08-20 | Pletcher, Kurt | Officer | 賣出 | 135 | $0.15M |
| 2026-08-18 | Paisley, Christopher B. | Director（間接持有） | 賣出 | 125 | $0.14M |
| 2026-08-03 | Paisley, Christopher B. | Director（間接持有） | 賣出 | 4,000 | $4.08M |
| 2026-06-08 | Morandi, Brandi Galvin | Officer | 賣出 | 3,726 | $4.01M |
| 2026-06-02 | Fox-Martin, Adaire | CEO | 賣出 | 2,935 | $3.10M |
| 2026-06-02 | Lin, Jonathan / Pletcher / Abdel Raouf | Officer | 賣出 | 合計約 387 | 合計約 $0.41M |
| 2026-05-22 | Abdel Raouf, F. | Officer | 賣出 | 2,040 | $2.21M |
| 2026-05-18 | Paisley, Christopher B. | Director（間接持有） | 賣出 | 125 | $0.13M |
| 2026-05-06 | Meyers, Charles John | Director | 賣出 | 5,224 | $5.67M |

Notable：
- CEO Fox-Martin 於 2026-06-02 賣出約 $3.10M；CFO Keith David Taylor 在 6 個月窗口內無賣出紀錄（最後一筆為 2026-03-12）。
- 最大賣方為董事 Meyers（$5.67M）與董事 Paisley（6 個月合計約 $4.35M）。
- 2026-05-06 另有 Morandi 112 股贈與（gift，無金額）。
- 多筆賣出集中在同一天、價格區間相同，符合依計畫交易或同批歸屬後賣出的特徵，但本次資料無法確認是否為 10b5-1 計畫，請勿據此推定意圖。
- 解讀：6 個月內完全無公開市場買進，屬於偏空的內部人訊號，但大額賣出在大型 REIT 中常見於分散持股或既有計畫，單靠此數據不足以判定。

## Ownership shifts
- insidersPercentHeld：0.27%（內部人持股比例很低）。
- institutionsPercentHeld：100.75%，超過 100%，明顯為 Yahoo 資料的重複計算問題，不可直接使用。
- institutionsCount：1,995 家。
- 工具只提供單一時點快照，無時間序列，無法判斷法人持股集中度是上升還是下降。

## Net sentiment score
Composite：**中性偏多（confidence：中低）**

| 構面 | 傾向 | 信心 | 依據 |
|---|---|---|---|
| Analyst | 偏多 | 中高 | 82% 買進評級，無賣出，覆蓋家數微增 |
| Insider | 偏空 / 中性 | 中 | 6 個月 $0 買進、約 $20.4M 賣出，但多為非典型大額交易，且有 CEO 與董事參與 |
| Retail | 混合偏空 | 低 | NAGA crowd 偏空，blogger / news 偏多，樣本與時效不足，Reddit 與 StockTwits 缺資料 |

Divergence flag：**是（低信心）**。分析師與 NAGA 的 crowd 標示方向相反（分析師偏多、crowd 偏空），且內部人淨賣出與分析師偏多相反。但零售端資料本身品質低、NAGA 頁面內部矛盾，不宜把這一分歧當作強訊號。

資料限制與時效：
- 報告指定 as-of 日期為 2026-10-17，系統日期為 2026-10-16；本次所有資料均早於 2026-10-01，以 2026-09-30 為最新零售資料點、2026-09-04 為最新內部人交易。未找到 2026 年 10 月的零售或社群資料。
- 分析師彙總數字為 yf 快照，未附日期（標示 0m）。
- 下一次財報日（equibles 估計 2026-10-28，尚未確認）在 as-of 日期後約 11 天，屆時分析師與零售情緒可能出現明顯變動。
- Reddit、StockTwits 未取得資料，其餘來源皆為第三方聚合站或搜尋摘要，部分網域疑似鏡像站，已排除無法核實的內容。

來源（WebSearch 摘要，供追溯）：
- NAGA 股票頁：https://naga.com/en/instruments/EQIX.re
- MarketBeat（Cantor Fitzgerald 2026-07-30）：https://www.marketbeat.com/instant-alerts/equinix-nasdaqeqix-stock-price-expected-to-rise-cantor-fitzgerald-analyst-says-2026-07-30/
- SentiSense EQIX 情緒頁：https://app.sentisense.ai/stocks/EQIX/sentiment
- equibles EQIX 頁：https://equibles.com/stocks/EQIX

SENTIMENT REPORT COMPLETE
