# Sentiment — SNDK as of 2026-10-21

> 資料時點說明: 本次執行環境日期為 2026-10-20, 報告標示 as-of 2026-10-21。yf 價格與分析師數據為執行當下可取得的最新值; 散戶社群資料僅能取得 2026 年 7 月以前的快照, 未能取得 10 月資料 (見下方)。

## Analyst consensus

yf `rec_summary` (0m): 25 家, strongBuy 4 / buy 17 / hold 3 / sell 0 / strongSell 1。Buy 類 (含 strong buy) 佔 84%。近三個月趨勢: -3m 為 buy 15 / hold 4 / strongSell 1, 目前為 buy 17 / hold 3, 屬於小幅偏多移動, 期間無淨降評。
注意: 各來源家數不同 (Investing.com 為 21 Buy / 3 Hold / 1 Sell)。yf `recommendations` 與 `rec_summary` 回傳相同內容, 工具未提供逐筆升降評歷史。

yf `info`: 目標價平均 $2,173 (24 家)、中位數 $2,150、高 $3,600、低 $1,000; recommendationMean 1.52 (buy 區間)。現價 $1,371.12 (yf 即時值), 距 52 週高點 $2,354.39 約 -42%。

近期重要動作 (來自 WebSearch, 無法由 yf 逐筆驗證):
- 9/22 Rosenblatt 首次覆蓋, Buy, 目標 $2,400
- 10/1 Citi 重申 Buy, 目標 $2,100
- 8/6 Wells Fargo 目標由 $1,620 降至 $1,400 (評等未變)
- 8/6 RBC 目標由 $1,000 升至 $1,300 (Sector Perform)
- 8/25 Mizuho 目標由 $1,900 降至 $1,875 (Outperform)
- Susquehanna 8 月後目標 $2,000; 另一來源顯示 $3,050, 兩者不一致, 未採用

10 月份未發現新的升降評, 但搜尋覆蓋可能不完整。

下一個催化: 10/29 財報, yf 顯示 EPS 預估 $46.27。前一季 (8/5) 實際 EPS $39.25, 超出預估 13.7%。

## Retail social

- Reddit: WebSearch 未找到 r/wallstreetbets 相關結果, 無法直接取得 r/stocks 搜尋 (本環境 Reddit 網域不可達)。間接來源 (24/7 Wall St, 2026-07-22) 顯示 Reddit 情緒分數 58 (中性), 活躍度 13 (低), 較 7/2 高峰 51 明顯下滑。代表性熱門貼文為 r/stocks 一則自陳於約 $2,330 買入、詢問是否買在高點的貼文, 約 596 upvotes, 之後討論快速冷卻。引述 (≤15 字): 「bought near the top」 類提問。Tilt: 7 月時偏中性, 無 10 月資料。
- StockTwits / X: StockTwits 網域不可達, 改以搜尋摘要判讀。
  - 3/5: 「bullish」, 訊息量 extremely high, 多頭主張 "unstoppable" 與泡沫擔憂並存。
  - 7/28: 三個交易日下跌超過 30%, 成為 StockTwits 熱門股, 散戶辯論 $1,000 能否守住。
  - 無日期的 SNDK 頁面標示 "Extremely Bullish", 時點不明, 不採用為當前值。
  - 選擇權流向在 6 月底偏向 put, 有 0DTE 看跌部位被廣泛分享的紀錄。
- buzz 量能: 相對於 3 月與 7 月高峰, Reddit 量能於 7 月明顯降溫; 10 月無資料, 無法判定目前量能。
- Themes (主要可辨識主題):
  - AI 資料中心需求與 NAND 供需緊張 (多頭主軸)
  - 估值擔憂: 前瞻 P/E 約 34 倍, 泡沫與高點追價疑慮 (空頭主軸)
  - $1,000 關卡是否守住 (技術與情緒分水嶺)
  - 選擇權 put 流向與空頭部位
  - 空單比例: Benzinga 快照 8.3% (日期不明) vs yf `shortPercentOfFloat` 3.34%, 來源不一致

## Insider activity

Net 6mo (2026-04-21 至 2026-10-21, 以 yf `insider` 計): 公開市場買入 $0 / 已標價賣出約 $130.3M (6 位內部人, 約 83.5k 股)。
不計入上述統計: 9/17 年度 grant (標示 Stock Award), 6/2 CTO 贈與 2,694 股, 5/12 董事 Caulfield 間接持有贈與 9,666 股, 8/20 CTO 276 股 (無價格, 性質不明)。

主要賣方:
- CEO David Goeckeler: 9/14 與 9/17 兩筆, 合計約 67.7k 股, 約 $105.0M, 佔期間賣出金額約 81%。
- CTO Alper Ilkbahar: 6/1 (2,000 股, $3.51M)、9/3 兩筆 (合計 5,112 股, $7.88M), 期間合計約 $11.4M。
- 官員 Bernard Shek: 6/3、7/1、8/3、9/1、9/8 共 5 筆 (每筆 600 至 2,308 股), 合計約 $8.0M。
- 官員 Michael Pokorny: 5/12 賣出 2,446 股, $3.49M。
- CFO Luis Visoso: 9/15 賣出 1,000 股, $1.57M。
- 董事 Necip Sayiner: 5/8 賣出 579 股, $0.87M。

Notable: CEO 9 月連續兩個交易日合計賣出約 $105M, 單一事件規模超過其他所有內部人期間賣出總額。yf 資料未標示是否為 10b5-1 計畫, 無法判斷是否預先排定。

## Ownership shifts

來源: yf `inst_holders` (13F, 截至 2026-06-30)。
- 機構持股比例 82.1%, 持有機構數 2,349 家; 內部人持股 1.08%。
- 前十大持有人變化:
  - BlackRock 7.12% (-1.0%)
  - Vanguard Capital Management 6.69% (+1.5%)
  - FMR 5.44% (-41.3%, 為最大減持)
  - State Street 4.10% (+6.3%)
  - Invesco 3.88% (+381%)
  - JPMorgan 2.73% (+176%)
  - Geode 2.48% (-14.8%)
  - Vanguard Portfolio Management 2.43% (-1.7%)
  - Clear Street 2.06% (+144%)
  - Situational Awareness LP 1.73% (+119%)
- 趨勢: 大型被動與指數持有人大致持平, 主動型基金中 FMR 大幅減持, Invesco、JPMorgan、Clear Street、Situational Awareness 明顯加碼。整體為主動資金輪動, 集中度未明顯上升。
- 大股東: Western Digital 持股 29.86M 股 (>10%), 申報日期為 2025-02-13, 資料為舊值, 百分比未提供。

## Net sentiment score

| 面向 | 判讀 | 信心 | 依據 |
|---|---|---|---|
| 分析師 | 偏多 | 高 | 84% buy 類, 平均目標 $2,173, 近 3 月小幅升評 |
| 散戶 | 無法判定 (最後可得為中性偏空) | 低 | 僅 7 月前資料, Reddit 低活躍, StockTwits 7 月大跌 |
| 內部人 | 偏空 | 中高 | 0 筆公開買入, 約 $130M 賣出, CEO 佔大宗 |
| 機構 | 中性偏多 | 中 | 機構持股 82%, 主動基金淨加碼多於減碼 (但 FMR 大減) |

Composite: 中性偏多 (信心: 中低)。分析師與機構面支撐, 內部人賣出與散戶歷史資料偏弱形成拉扯。散戶面資料缺口是本次判讀的主要限制。

Divergence flag: 是 (低信心)。分析師偏多與散戶最後可得資料 (7 月) 的偏空或中性情緒方向相反。內部人賣出方向與散戶偏空一致, 與分析師偏多相反。由於散戶資料已過期約三個月, 此分歧旗標需待 10 月資料補齊後確認。

Data gaps:
- Reddit (wallstreetbets、stocks) 10 月資料: 無 (網域不可達, 搜尋未回傳近期內容)
- StockTwits 10 月資料: 無
- yf `recommendations` 逐筆歷史: 未提供
- 10b5-1 標記: 未提供
- 大股東 WDC 持股比例: 未提供

Sources (WebSearch):
- https://www.investing.com/equities/sandisk-corp
- https://www.barchart.com/story/news/3663127/are-wall-street-analysts-bullish-on-sandisk-stock
- https://247wallst.com/investing/2026/07/22/wall-street-loves-sandisk-but-retail-is-strangely-silent/
- https://stocktwits.com/news-articles/markets/equity/sndk-stock-sandisk-drop-30-percent-loss-3-days-1000-retail-debate/cZZCrYiRJbB
- https://stocktwits.com/news-articles/markets/equity/is-san-disk-stock-unstoppable-after-doubling-in-3-weeks-here-s-what-wall-street-and-retail-see-ahead-of-earnings/cmUz1wOR4QE
- https://www.benzinga.com/quote/SNDK/sentiment
- https://www.tradingview.com/news/gurufocus:508fece63094b:0-sandisk-stock-gets-more-than-2-000-price-target-boost-from-citi/
- https://www.marketbeat.com/stocks/NASDAQ/SNDK/price-target/

SENTIMENT REPORT COMPLETE
