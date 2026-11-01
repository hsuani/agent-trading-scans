# Sentiment — CBRS as of 2026-11-02

## Analyst consensus
目前 11 家覆蓋：3 Strong Buy / 8 Buy / 0 Hold / 0 Sell（yf rec_summary，期間 0m）。
與前一個月相比，總覆蓋數維持 11、Hold 由 1 減為 0、Buy 由 7 增為 8，推估為 1 家由 Hold 升為 Buy（個別機構與日期無法從計數資料確認）。再往前兩個月（-2m）為 3 SB / 7 B / 1 Hold / 0 S，與 -1m 相同。
Recent moves: 工具僅提供評等計數，沒有個別升降評等明細，目標價變動亦無資料，無法確認。
Benzinga 情緒頁顯示 consensus 為 Buy（頁面無日期，僅供參考）。

## Retail social
- Reddit: 無法取得。r/wallstreetbets 與 r/stocks 的搜尋 JSON 皆被 proxy 阻擋（WebFetch: unable to fetch www.reddit.com），soft-fail，無貼文樣本、無計數、無 tilt 判斷。
- StockTwits: 無法取得。api.stocktwits.com DNS 解析失敗（需於 session 網路設定中允許此網域），soft-fail。
- X / 新聞 chatter: WebSearch 未檢索到 2026-11 期間的內容，最新快照為 2026-08 前後。可取得的聚合資訊：
  - Benzinga：Buy 共識、short float 14.1%、put/call 0.50（無日期）。
  - SentiSense：30 日情緒為 neutral（分數 1），較一個月前轉強；快照日 2026-08-18，距報告日超過兩個月，僅作背景參考。
  - Historical Option Data 系列盤中文章（2026-06 至 2026-07）：選擇權流向偏多、技術面偏弱並存；7 月一篇給出偏多中等信心。此來源可信度低，僅作參考。
- Buzz volume: 無法量化（Reddit/StockTwits 計數皆缺），無法與常態比較，維持未知。
- Retail tilt: 無法判定。聚合結果呈混合訊號，沒有可驗證的散戶多空比例。
- Themes（可得資料中反覆出現）:
  - 估值偏高（高本益比）是空方主要論點。聚合摘要引用一則「CBRS overvalued at 400+ P/E」的貼文，但原文來源未能驗證，僅列為主題參考。
  - 關稅與貿易風險。
  - 空方部位上升（short float 14.1%）與 put/call 0.50 偏多頭的選擇權解讀並存。

## Insider activity
窗口：2026-05-02 至 2026-11-02（6 個月）。單位：US$M（yf 原始值為 USD）。

| 類別 | 公開市場賣出 (US$M) | 筆數 | 公開市場買入 |
|---|---|---|---|
| CEO Andrew Feldman | 64.3 | 4 | 0 |
| CTO Sean Lie | 200.7 | 6 | 0 |
| COO Dhiraj Mallick | 103.6 | 5 | 0 |
| CFO Robert Komin | 6.6 | 1 | 0 |
| Officer Yagnesh Patel | 3.0 | 4 | 0 |
| 董事 Steven Vassallo (間接持股) | 21.4 | 2 | 0 |
| 董事 Eric Vishria (間接持股) | 15.7 | 1 | 0 |
| 合計 | 415.3 | 23 | 0 |

Net 6mo: 公開市場買入 US$0，公開市場賣出 US$415.3M，淨額 約 -US$415M。
排除項目：
- 贈與（0 價值，非賣出）：CTO Lie 4 筆（合計約 26.3 萬股）、CEO Feldman 1 筆（5 萬股）。
- 獎勵授予：Patel 2026-06-26 授予 1.5 萬股（0 價值）。
- 2026-05-15 衍生性證券轉換（行權價 279.72）：Vassallo 與 Benchmark / Foundation Capital 相關實體共轉換約 3,000 萬股以上，名目金額約 US$12.1B。此為轉換而非現金交易，未計入上表。

Notable:
- 2026-08-21 CTO Sean Lie 賣出 72.7 萬股，約 US$151.1M，為窗口內最大單筆。
- 2026-09-29 COO Dhiraj Mallick 賣出 39.6 萬股，約 US$80.8M，為 9 月最大單筆。
- 2026-10-27 CTO Sean Lie 賣出 6 萬股，成交價 113.92–116.82，約 US$6.9M，為窗口內最近一筆。此價位較 9 月（約 195–213）與 8 月（約 215–240）低約 40–45%，yf 資料中無其他佐證。需以主要行情來源核對，可能是真實下跌，也可能是資料錯誤。
- 賣出分散於 CEO、CTO、COO、CFO 與董事，並非單一人士。是否屬於 10b5-1 預定計畫，資料無法確認。

## Ownership shifts
- 機構持股 80.4%（institutions float-held 88.9%），機構數 579 家。
- 內部人持股 9.6%。
- 趨勢：工具只提供單一快照，無法判定機構持股的增減方向。
- VC 大股東（Benchmark、Foundation Capital 相關實體，Vassallo 與 Vishria 為其董事）的 Form 4 持股數列示前後不一致（例如 2026-08-17 列 240 萬股、2026-08-24 列 96 萬股），且資料中無其公開市場賣出紀錄。其持股趨勢需以 13D/13G 或 13F 申報核對。

## Net sentiment score
- 分析師面：偏多。11 家全數為 Buy 級以上、無 Sell，信心 中高（計數清楚，但無日期與目標價）。
- 內部人面：偏空。6 個月公開市場賣出約 US$415M、買入為 0，且多名高階主管同步出售，信心 中（是否為預定計畫未知）。
- 散戶面：無法判定。Reddit、StockTwits 皆無法取得，聚合來源呈混合訊號，信心 低。
- Composite: 中性（neutral），信心 低。分析師偏多與內部人持續賣出相互抵銷，散戶端缺資料，無法給出明確方向。

Divergence flag: 是。分析師端偏多，內部人持續大額賣出，兩者方向相反。散戶端與分析師是否相反無法確認，因此不能判定第二層背離。

## Data gaps
- Reddit、StockTwits 皆未取得，散戶聲量與 tilt 為缺口。
- 分析師目標價變動、個別評等升降明細無資料。
- 2026-10-27 的低價成交（約 US$114–117）需以主要行情來源核對。
- 機構持股趨勢無歷史快照。

SENTIMENT REPORT COMPLETE
