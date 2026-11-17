# Sentiment — 8996.TW (高力 Kaori Heat Treatment) as of 2026-11-18

資料基準：yf 快取於 2026-11-17 15:54 UTC 更新（無 miss）；WebSearch 結果多為 2026-11 中旬前後媒體與研究報告。Reddit 與 StockTwits 本次皆無法取得。

## Analyst consensus

資料來源：yf rec_summary（快取）。

| 評等 | 家數 |
|---|---|
| Strong Buy | 2 |
| Buy | 5 |
| Hold | 0 |
| Sell | 0 |
| Strong Sell | 0 |

共 7 家，全數偏多（Buy 或 Strong Buy）。yf 的 rec_summary 在 0m、-1m、-2m、-3m 四個期間數字完全相同，代表近三個月沒有評等變動，或來源只回傳彙總快照。

Recent moves: DATA_UNAVAILABLE。yf recommendations 端點回傳的內容與 rec_summary 相同（彙總分布），沒有個別券商的升降評等紀錄，無法列出 upgrade / downgrade 事件。

目標價（WebSearch 彙整，來源不一致，部分資料日期不明）：
- 里昂證券（CLSA 相關報導）目標價由 1,680 元上調至 2,300 元，維持強力買進；報導引用的日期未能確認，媒體標題為「法人調升高力目標價逾60%」。
- Fintel 平均一年期目標價約 2,234 元（最高 2,415 元）。
- Investing.com 5 家平均約 1,878 元。
- Growth Investing 最高 2,300 元、平均 2,000 元，更新日期標示 2026-07-09。
- StockAnalysis（2026-06-05 頁面）4 家平均約 1,235 元，區間 770 至 1,680 元。
- AlphaSpread 與 TradingView 的 397 至 400 元應為舊資料，忽略。

家數不一致（yf 7 家、Investing 5 家、StockAnalysis 4 家），目標價大多停在 2026-08 以前，無法確認是否已反映 2026-11-10 前後的財報。

## Retail social

- Reddit（r/wallstreetbets、r/stocks）：DATA_UNAVAILABLE。WebFetch 回傳無法存取 www.reddit.com，本次未取得討論串、分數與留言數。
- StockTwits：DATA_UNAVAILABLE。api.stocktwits.com 無法解析（網路白名單未放行），未取得訊息量或多空標籤比例。
- X / 新聞與論壇（WebSearch）：可取得的是媒體與研究報告，而非散戶貼文。整體論調分成兩側：
  - 偏多：2026 年前三季 EPS 14.39 元，已超過 2025 全年 EPS 9.07 元；第三季毛利率回升至 28.28%；液冷散熱與燃料電池（主要客戶 Bloom Energy）為成長動能；板式熱交換器切入美國 CSP 供應鏈，預計下半年出貨。
  - 偏空或保留：股價由 10 月盤中高點 1,800 元回落，11 月 6 日收 1,180 元，11 月 13 日反彈至 1,440 元，11 月 12 日盤中衝高至 1,575 元後收 1,425 元留下長上影線；以已公布獲利粗估本益比約 80 倍；9 月底負債比約 61.87%（前一季約 50%）；已發行可轉債，未來轉換有稀釋風險。
- 討論量（buzz volume）：DATA_UNAVAILABLE。無法取得提及次數與歷史基準，僅能從媒體報導頻率判斷近期話題度偏高。

Themes（依 WebSearch 結果歸納）：
1. AI 資料中心液冷與燃料電池需求。
2. 高估值與季線支撐（約 1,400 元附近）是否守住。
3. 負債比上升與可轉債稀釋。
4. 美國 CSP 供應鏈切入的出貨時點。

## Insider activity

Net 6mo: DATA_UNAVAILABLE。yf insider 回傳空陣列，無法區分「期間內無申報」與「來源無資料」，不能推定為零交易。未取得 CEO / CFO 或其他人員的買賣紀錄。

## Ownership

yf major_holders（快照，無時間序列）：
- 內部人持股：約 10.66%
- 機構持股（占總股本）：約 35.30%
- 機構占流通股比例：約 39.51%
- 機構家數：97

機構集中度趨勢：DATA_UNAVAILABLE（僅有單一時點快照，無法判斷增減）。

## Net sentiment score

Composite: 偏多（信心：低）。

依據：
- 分析師端偏多（7 家全數 Buy 或 Strong Buy，零 Hold、零 Sell），為明確的多方共識。
- 散戶端無法量測（Reddit、StockTwits 皆不可用），無法確認散戶情緒。
- 媒體與研究端論調偏多但夾雜估值與槓桿疑慮，屬於「基本面正面、估值與股價波動偏負」的混合訊號。
- 內部人交易與機構趨勢皆無法判斷，未納入加權。

信心偏低的主因是缺少散戶與內部人兩項資料，且目標價資料多停在 2026-08 以前。

Divergence flag: 無法判定（散戶資料缺失）。媒體端的保留意見（估值、負債、稀釋）與分析師端的全面偏多之間存在張力，但這不是散戶與分析師方向相反，不應視為背離訊號。

## Data gaps

- Reddit：DATA_UNAVAILABLE（www.reddit.com 無法存取）
- StockTwits：DATA_UNAVAILABLE（api.stocktwits.com 無法解析）
- 評等變動歷史：DATA_UNAVAILABLE（yf recommendations 僅回傳彙總）
- 內部人交易：DATA_UNAVAILABLE（yf insider 空陣列，不可視為零）
- 機構趨勢：DATA_UNAVAILABLE（僅單一快照）
- 目標價日期：多數來源早於 2026-08，未能確認是否反映 2026-11 財報

## Sources

- [高力 液冷散熱放量 研究報告（cnyes）](https://hao.cnyes.com/post/251002)
- [法人調升高力目標價逾60%（udn）](https://money.udn.com/money/amp/story/5607/9580374)
- [MoneyWeekly 相關報導](https://www.moneyweekly.com.tw/_Article?AID=262060)
- [Kaori Heat Treatment 目標價彙整（StockAnalysis）](https://stockanalysis.com/quote/tpe/8996/forecast/)
- [Kaori Heat Treatment 分析師目標（Fintel）](https://fintel.io/s/tw/8996)
- [Kaori Heat Treatment 分析師資料（Investing.com）](https://ca.investing.com/equities/kaori-heat)

SENTIMENT REPORT COMPLETE
