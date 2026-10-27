# Sentiment — WDC as of 2026-10-28

資料來源與完整度：分析師評級與內部人交易來自 `pipeline/tools/yf`（yfinance 的 Cookie/crumb 取得失敗，但仍回傳資料，本次判定為可用）。Reddit（r/wallstreetbets、r/stocks）的 WebFetch 被拒絕（DATA_UNAVAILABLE）。StockTwits 的 api.stocktwits.com 因 DNS 解析失敗（ENOTFOUND）無法連線（DATA_UNAVAILABLE；需在 session 網路設定中允許該網域才能重試）。WebSearch 可用，但只取得分析師與聚合站的二手內容，沒有可辨識的零售貼文樣本。因此散戶聲量與傾向無法量化，本報告不以任何 Reddit、StockTwits 數字作結論。

## Analyst consensus

yf `rec_summary` 0m 期：**26 家中 21 家 Buy 系（4 Strong Buy + 17 Buy）、5 家 Hold、0 家 Sell**。Buy 系佔比約 81%。

逐月趨勢（yf 只提供月度計數，`recommendations` 回傳內容與 `rec_summary` 相同，沒有個別券商的升降評明細）：

| 期間 | Strong Buy + Buy | Hold | Sell | Strong Sell | 合計 | Buy 系佔比 |
|---|---|---|---|---|---|---|
| 0m（本月） | 21 | 5 | 0 | 0 | 26 | 81% |
| -1m | 21 | 5 | 0 | 0 | 26 | 81% |
| -2m | 21 | 5 | 0 | 0 | 26 | 81% |
| -3m | 22 | 3 | 0 | 1 | 26 | 85% |

近期動作：過去三個月 Hold 由 3 家增至 5 家，Strong Sell 由 1 家降為 0，Buy 系由 22 家減為 21 家。整體仍偏多，但評級有小幅往中性移動。yf 無法確認是哪些券商調整。

二手來源（WebSearch，時點與口徑不一，僅供參考，未獨立驗證）：
- Google Finance 顯示 18 家（14 Buy、4 Hold），與 yf 的 26 家口徑不同。
- 平均目標價來源間差距很大，約 $655–668（Investing.com、Tickzen）。這與同期約 $364–527 的報價落差很大，無法確認，不宜直接採用。
- Fox Advisors 曾下調評級（2026-08 的頁面，理由是硬碟定價預期過高），時點可能過舊。
- 下一次財報：**2026-10-29 盤後**（WebSearch 二手來源），距本報告日僅 1 天，為評級更新的主要催化事件。

## Retail social

- **Reddit (r/wallstreetbets)**：WebFetch 被拒，DATA_UNAVAILABLE。
- **Reddit (r/stocks)**：同上，DATA_UNAVAILABLE。
- **StockTwits**：DNS 解析失敗，DATA_UNAVAILABLE。
- **X / 新聞聊天**：WebSearch 找不到 2026-10 的零售討論樣本，結果以分析師、聚合站與技術文章為主。
- **聲量**：無法與基準比較，判定為資料缺口。
- **零售傾向**：無法判定（資料缺口）。
- **二手技術與部位指標（時點不明，僅供參考）**：Barchart 技術評級由約 64% Buy 轉為約 8% Sell；Benzinga 顯示 short float 約 6.0%，put/call 約 0.23。
- **主題**（由二手聚合內容歸納，非零售原文）：AI 資料中心需求是多頭主軸；股價自 2026 年中高點回落、技術面轉弱是主要空方論點；財報前的預期管理是常見討論方向。

## Insider activity

統計區間：2026-04-28 至 2026-10-28（6 個月）。金額單位為 USD，以 M 表示。

**6 個月淨額：公開市場買入 $0.00M，賣出約 $35.79M，淨額約 −$35.79M。** 共 20 筆公開市場賣出，由 6 位內部人執行。未見任何公開市場買入。

主要賣出（依金額排序）：

| 日期 | 內部人 | 職位 | 股數 | 金額（USD M） | 價格（USD） |
|---|---|---|---|---|---|
| 2026-08-11 | TAN IRVING | Chief Executive Officer | 20,000 | 8.90 | 441.48–447.18 |
| 2026-05-11 | DAVIS BRIAN SCOTT | Officer | 10,000 | 5.01 | 489.78–510.00 |
| 2026-05-01 | TAN IRVING | Chief Executive Officer | 20,000 | 8.24 | 406.52–415.02 |
| 2026-09-01 | STREETER STEPHANIE A | Director | 5,600 | 2.52 | 447.06–455.00 |
| 2026-05-04 | GUBBI VIDYADHARA K | Officer | 4,674 | 2.07 | 443.18 |
| 2026-07-28 | COLE MARTIN I | Director | 3,808 | 1.71 | 424.04–461.23 |
| 2026-06-09 | COLE MARTIN I | Director | 3,280 | 1.68 | 484.28–527.22 |

各人加總（窗口內，USD M）：TAN IRVING（CEO）約 17.14、DAVIS 約 5.01、GUBBI 約 4.20、COLE 約 3.48、TREGILLIS CYNTHIA LOCK（Officer）約 2.65、STREETER 約 2.52、KIDDOO 約 0.40。

重點觀察：
- CEO Tan Irving 在窗口內兩次公開市場賣出（合計約 $17.14M），是最大單一賣方。由於 yf 未提供交易計畫類型，無法確認是否為 10b5-1 預排計畫。
- 窗口內另有 CEO 的 112,500 股 Stock Gift（09-01）與 16,548 股 Stock Award（08-25），屬非市場交易，金額為 0，未計入。
- 窗口內的 Stock Award 集中於 2025-08 與 2026-08-25 的年度授予，屬例行發放，非主動買入。
- CFO Kris Sennesael 在窗口內無公開市場賣出，只有授予與少量申報。
- 股價區間參考：yf 內部人成交價約 $380（10-21）至 $530（07-21），與 WebSearch 的 $364（Tickzen，10-20）大致吻合；其他來源報價（$467、$527）時點不一。

## Ownership shifts

yf `major_holders`：機構持股 88.6%（institutionsPercentHeld 0.88556），機構數 2,434 家；內部人持股 0.27%。**本次只有單一時點快照，無法判斷季度趨勢**，因此無法確認機構集中度是上升或下降。

## Net sentiment score

**Composite：偏多（bullish lean）**，信心度 **低至中**。

- 分析師面（權重最高）：偏多。Buy 系 81%，近三個月有小幅往 Hold 移動，無 Sell 評級。
- 內部人面：偏空（弱訊號）。6 個月淨賣出約 $35.79M，無公開市場買入，CEO 為主要賣方。但執行高階主管賣股在多數情況下屬例行，且無法確認是否為預排計畫，權重應打折。
- 散戶面：無資料，不納入計分。
- 信心度低的原因：散戶面完全缺席，且財報在 2026-10-29 盤後，評級與股價可能在下一交易日出現大幅變動。

**Divergence flag：部分分歧。**
- 分析師（偏多）與內部人（淨賣出）方向不一致，屬於需要留意的訊號，但內部人賣出常見為例行行為，訊號強度有限。
- 零售與分析師是否背離：**無法判定**（DATA_UNAVAILABLE）。Reddit、StockTwits 皆無法取得，不能宣稱零售偏空或偏多。

## 資料缺口與後續

- Reddit 與 StockTwits 需在 session 網路設定中允許 www.reddit.com、api.stocktwits.com 後方可重試。
- 財報（2026-10-29 盤後）發布後，建議重新跑 `rec_summary` 與 `recommendations` 以確認評級變動；本報告的評級為財報前快照。
- 二手目標價（$655–668）與報價來源衝突，未經獨立驗證，不應作為估值依據。

SENTIMENT REPORT COMPLETE
