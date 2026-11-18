# Sentiment — 3231.TW 緯創 Wistron as of 2026-11-19

資料可信度提醒：本次 Yahoo 端點多數連線被 agent proxy 拒絕（guce / query2 / fc.yahoo.com），yf 工具回傳的 insider 為空陣列，無法區分「確實無申報」與「抓取失敗」。Reddit 與 StockTwits 直接抓取未執行（依指示改用 WebSearch），WebSearch 也未找到 2026-11 的 Reddit 討論串。多數社群與新聞結果日期模糊或為舊文，以下結論信心偏低。

## Analyst consensus

yf `rec_summary` / `recommendations`（同一組趨勢資料）當期分布：Strong Buy 5 / Buy 11 / Hold 0 / Sell 0 / Strong Sell 0，即 16 家中 16 家 BUY，**BUY 比例 100%**。過去三個月趨勢：Strong Buy 由 5 增至 6（-2m、-3m 期間），Buy 維持 11，無 Hold 或 Sell 出現。

另一來源（Investing.com 共識頁，日期標示約 2026-10-30）為 14 Buy / 2 Hold / 0 Sell，**BUY 比例約 87.5%**。兩個來源差 2 家 Hold，本報告以區間 87.5%–100% 呈現，yf 數字為較新的主要依據。

目標價：
- 公開報導引用的目標價包括 NT$200.94（Nasdaq 轉載的目標價上修 12.89% 文章），Investing.com 12 個月平均目標價約 NT$222.43。
- 2026-05 KGI 報告維持 Outperform，目標價 NT$225。
- 部分頁面另列有 NT$400 的外資目標價（Macquarie），其日期與可信度不一，未納入平均。
- 股價參考：2026-10-30 前後約 NT$183.5，11 月初報導區間約 NT$168–171（年份於頁面未明確標示，僅能推斷為 2026-11）。

近期評等動向：yf 未回傳 upgrade/downgrade 明細（recommendations 僅為彙總計數），無法確認個別評等變動。無 Sell 評等出現於近三個月。

## Retail social

- Reddit：WebSearch 以 r/wallstreetbets 與 r/stocks 關鍵字搜尋，未找到 3231 相關 2026-11 討論串。無法評估 Reddit 情緒。
- StockTwits / X：未取得 2026-11 貼文。WebSearch 結果多為新聞與評論，無可引用的即時 X 貼文。
- PTT / CMoney 股市討論：找到的內容多為 2025-12 與 2026-02 前後的文章（例如 2025-11 單月營收創高後網友留言「要噴到200了吧」，此為舊文）。CMoney 論壇有網友描述持股與股價連漲的樂觀貼文，但日期接近 2026-07，與本報告時點不符。
- 媒體評論：Invezz 2026-09 文章標註 AI 情緒分數 35/100（偏空），但屬單篇文章語氣，非市場整體情緒。

Buzz 量：WebSearch 結果篇數與一般時期相比無明顯放大跡象，但因來源時效性不足，無法量化，只能定性為「無法判定，偏低可見度」。

Themes（自既有資料歸納，時效不一）：
1. AI 伺服器需求與 Nvidia 供應鏈定位：多數正面論述集中於此。報導引用 Q2 營收年增 64%、淨利年增 128%，以及 2026 年 AI 伺服器出貨預估年增約 31%。
2. 稀釋與資金面疑慮：2026-09 全球案股份釋出稀釋約 7%，市場因此修正股價。
3. 外資買賣動向：有報導提及外資單日大幅減碼超過 3.3 萬張，但該篇 URL 時間戳指向 2025-04，時效存疑，不列入判斷。
4. 股利發放作業：2026-08 股務系統作業疏失造成現金股利發放日兩度順延，並引起主管機關關注，是負面事件。
5. 財報催化：WebSearch 結果提及下一次財報約在 2026-11-18 發布，屬即將公布事件，其結果未知（資料日期 2026-11-19 之後不可得）。

## Insider activity

Net 6mo：資料不足。yf `insider` 回傳空陣列，無法得知 CEO/CFO 或其他內部人近六個月的買賣金額。此為抓取限制所致，不代表無內部交易，亦不應視為「中性」證據。
參考：insidersPercentHeld 約 4.77%（yf major_holders）。

## Ownership shifts

- institutionsPercentHeld：約 33.72%；institutionsFloatPercentHeld 約 35.41%；機構家數約 252 家。
- yf 僅提供當期快照，無歷史持股變化，無法判斷機構集中度趨勢。
- 2026-09 外資減碼之說因時效存疑，不能據此判定機構淨賣出。

## Net sentiment score

Composite: **偏多（信心：低）**
- 分析師面：偏多且高度一致（BUY 87.5%–100%，無 Sell），信心中高。
- 散戶面：無法可靠量化。Reddit 無資料、X/StockTwits 無即時資料、PTT/CMoney 多為舊文。以可得資訊看，AI 伺服器題材仍是正面主軸，稀釋與股利作業為負面疑慮，整體可能為「分歧、偏正面」，但信心低。
- 內部人面：資料缺失，不納入評分。

Divergence flag: **無法判定（資料不足）**。若以分析師偏多與媒體/散戶負面語氣（Invezz 35/100、稀釋與股利事件）相比，表面上有分歧，但因散戶端樣本過少且時效混雜，不宜作為強訊號。

**Analyst consensus % BUY: 100%（yf，16 家中 16 家）；另一來源 87.5%（14/16），區間 87.5%–100%。**
**Net retail sentiment call: 中性偏多（分歧，信心低）。**

SENTIMENT REPORT COMPLETE
