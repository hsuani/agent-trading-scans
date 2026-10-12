# Sentiment — ASML as of 2026-10-12

資料品質提醒: 本報告的 Reddit、StockTwits 與 insider 資料皆無法取得有效內容 (見各節說明)。分析師評等來自 repo 快取的 yf 資料, 社群情緒僅能依賴第三方彙整分數與零散新聞, 信心偏低。

## Analyst consensus
目前 (0m) 共 42 家覆蓋: 6 strong buy / 31 buy / 4 hold / 1 sell / 0 strong sell, 即 37 buy 類、4 hold、1 sell。

三個月趨勢 (yf rec_summary, 快取):

| 期間 | Strong Buy + Buy | Hold | Sell |
|---|---|---|---|
| 目前 (0m) | 37 | 4 | 1 |
| -1m | 38 | 3 | 1 |
| -2m | 38 | 4 | 1 |
| -3m | 40 | 3 | 1 |

評等結構穩定偏多, 買進類家數較三個月前小幅減少 3 家, 持有類增加 1 家, 屬於輕微降溫, 未見評等集中轉空。

Recent moves: 
- `recommendations` 指令回傳內容與 `rec_summary` 完全相同, 只有彙總家數, 沒有逐筆升降評等紀錄與目標價, 因此無法列出個別券商的 upgrade/downgrade 事件。
- 網路搜尋找到的降評為 New Street Research 於 2025-10-06 將 ASML 由 Buy 降至 Neutral (目標價 €790), 理由是 2026 年後成長可能見頂。這是 2025 年的事件, 不是近期動作。先前某篇德文文章提及的「2026 年 New Street 降評與 10/15 財報」無法在搜尋結果中確認, 不採信。
- 目標價變動: 無可用資料。

## Retail social
- Reddit: 無法取得。WebFetch 對 r/wallstreetbets 與 r/stocks 的 search.json 被封鎖, WebSearch 也找不到 2026 年 10 月的相關討論串。沒有可引用的代表性貼文, 不推估 tilt。
- StockTwits / X: 無法取得。StockTwits 直接 API 與訊息量資料皆無, WebSearch 未找到 10 月的訊息統計或多空投票。
- 第三方彙整 (AltIndex): 顯示 ASML 情緒分數 76/100, 標示 bullish, 但分數較 30 日均值下滑。該站以 NLP 分類 Reddit、StockTwits 與論壇貼文, 月度序列 2026 年 4 月為 71, 8 月為 87。頁面未標明 76 這個讀數的日期, 因此只能當作「偏多但未明確定日」的參考。同頁 AMD 為 71、Intel 為 70。
- 聲量 (buzz volume): 無可量化的提及次數, 無法與平均比較。以新聞量判斷, 10 月市場討論集中在財報前預期, 但這點未能由社群資料確認。
- Themes (由次級來源摘要, 非原文):
  - 多方: 中國需求帶動的 bookings 超出預期; 估值低於三年平均; EUV 需求受 AI 與記憶體客戶拉動。
  - 空方: 2026 年後成長見頂的疑慮; 毛利率壓力; 宏觀與地緣政治不確定性。
- Price context (非社群, 供參考): 2026-10-01 約 $1,596.6, 52 週區間 $813.80 至 $1,740.60, 單週上漲約 4.1%, 一個月約上漲 11.5% (來源為 TipRanks 轉載頁, 日期非 10/12 當日)。

## Insider activity
Net 6mo: 無法判定。yf insider 指令回傳空陣列 (`[]`), 此為「無資料」而非「零交易」。ASML 為荷蘭上市公司, 內部人申報依 MAR 規定, 不一定會出現在 yf 的 Form 4 式彙整中。`insidersPercentHeld` 為 0.008%, 顯示內部人持股比例極低, 但這與交易方向無關。

Notable: 無。

## Ownership shifts
- institutionsPercentHeld: 20.41%
- institutionsCount: 2,963
- 無歷史季度變化資料, 無法判斷集中度趨勢。
- 次級來源提及近期機構有一家加碼、一家減碼, 但無法確認時點與規模, 不計入評分。

## Net sentiment score
Composite: **偏多 (bullish)**, 信心 **低-中**。

判斷依據:
- 分析師面 (權重最高): 37 buy 類 / 42, 結構偏多, 但三個月內買進家數微降, 方向為小幅降溫。
- 散戶面: 只有單一第三方彙整分數 76 (偏多), 日期不明, 且 Reddit/StockTwits 無法直接驗證, 權重降低。
- 內部人面: 無資料, 不納入評分。
- 機構面: 持股 20.4%, 無趨勢, 中性。

Divergence flag: **否**。散戶 (彙整分數) 與分析師方向同為偏多, 沒有相反訊號。唯一的反向論述來自 2025 年 New Street 的成長見頂觀點, 屬於舊資料, 未構成當前背離。

限制與待辦:
- 若要提高信心, 需取得 StockTwits 訊息量與多空比、Reddit 近 7 日熱門貼文, 以及 yf 逐筆 upgrade/downgrade 與目標價。
- 財報日期 (依次級來源為 10/15, 未經確認) 落在報告日之後, 財報前後的情緒可能明顯波動, 建議次日重新檢查。

SENTIMENT REPORT COMPLETE
