# Sentiment — AMZN as of 2026-10-15

資料狀態：分析師評等與內部人交易來自 yf 快取（`source: cache`，refreshed 2026-10-15 11:19 UTC）。散戶社群（Reddit、StockTwits）本次無法取得，列為 DATA_UNAVAILABLE。

## Analyst consensus

yf 最新評等分布（0m）：16 strong buy / 42 buy / 2 hold / 0 sell / 0 strong sell，合計 60 家。

近三個月趨勢（yf trend）：

| 期間 | Strong Buy | Buy | Hold | Sell | 合計 |
|---|---|---|---|---|---|
| 0m（現在） | 16 | 42 | 2 | 0 | 60 |
| -1m | 16 | 43 | 2 | 0 | 61 |
| -2m | 16 | 45 | 2 | 0 | 63 |
| -3m | 16 | 45 | 3 | 0 | 64 |

買進側（strong buy + buy）由 61 降至 58，hold 由 3 降至 2，總家數由 64 降至 60。未見任何 sell 評等，整體仍為明確偏多，但評等數量呈小幅收縮。

近期升降評等：yf `recommendations` 只回傳彙總趨勢，不含個別券商的 upgrade/downgrade 明細，本次無法列出個股升降評等與目標價調整（資料缺口）。

第三方彙總（WebSearch，非本次 yf 資料，日期較舊）：
- MarketBeat（收盤價日期 2026-09-04）：59 家，評等 "Moderate Buy"（約 56 buy、1 strong buy、2 hold、0 sell），平均 12 個月目標價 $323.26，約高於當日收盤 $258.51 的 25%。
- Barchart（2026 年 4 月）：58 家中 49 家為 Strong Buy，Street-high 目標價 $360，該文指出共識較三個月前降溫。

與 yf 的家數與分布略有出入，屬不同彙總來源的口徑差異，本報告以 yf 為主。

## Retail social

- Reddit（r/wallstreetbets、r/stocks）：WebFetch 被封鎖（"unable to fetch from www.reddit.com"），無法取得貼文樣本、留言數與情緒傾向。DATA_UNAVAILABLE。
- StockTwits：DNS 解析失敗（api.stocktwits.com ENOTFOUND），無法取得訊息流。DATA_UNAVAILABLE。
- X / 新聞鏈接（WebSearch）：搜尋結果未找到 2026 年 10 月的散戶討論。最新一則與 r/WallStreetBets 相關的報導為 2025 年 10 月（與 Amazon 大規模裁員消息相關），屬舊資料，不能代表當前情緒。
- 提及量（buzz volume）：無法與常態比較，本次不下定性結論。
- 散戶傾向（tilt）：無資料，無法判定 bullish / bearish / mixed。

媒體與分析師常見論點（非散戶，但可作為市場敘事參考）：
- 多方：AWS AI 曝險與雲端加速（AWS 2025 Q4 營收 $35.6B、年化 $142B、backlog $244B）、廣告業務成長；BofA 的 Justin Post 將 AMZN 列為 2026 年大型網路股首選。
- 空方／保留：估值偏高與資本支出壓力（Q1 capex 年增逾 76%）。WinCap 的 CFA Michael Collins 認為股票 "looks fully priced"，並指其在 Mag 7 量化排名偏弱。

## Insider activity

6 個月窗口（2026-04-15 至 2026-10-15）：
- 公開市場買進：$0（窗口內無 open-market purchase）。
- 公開市場賣出：約 $411.7M。其中 Bezos 2026-08-03 賣出 1,209,649 股（約 $346.5M）占大部分；扣除 Bezos 約 $65.2M。
- 非市場性轉移（gift，未計入金額）：Bezos 2026-05-04（1,253,797 股）與 2026-08-26（415,580 股）；Herrington 2026-08-06（22,000 股）。

主要交易人：
- CEO Andrew Jassy：2026-04-17（31,000 股，約 $255）、2026-05-04（31,352 股，$275）、2026-05-21（20,000 股，約 $263）、2026-08-21（20,000 股，約 $259）。合計約 $27.0M。
- Douglas Herrington（Officer）：窗口內持續有賣出，包含每月約 1,000 股的小額規律賣出（最近 2026-10-01，1,000 股，$251.50），另有 2026-05-04（28,500 股）、2026-08-21 等較大筆。合計約 $14.4M。
- Matthew Garman、David Zapolsky、Brian Olsavsky（CFO）、Shelley Reynolds：多在 2026-05-21、2026-08-21 等同一日批次賣出，合計約 $25M（Garman 約 $10.9M、Zapolsky 約 $8.1M、Olsavsky 約 $1.6M、Reynolds 約 $1.2M）。
- 董事 Jonathan Rubinstein：2026-04-24、04-30 賣出，合計約 $2.0M。

解讀（僅描述交易型態，不作交易建議）：
- 內部人以賣出為主、無買進，方向偏空，但 AMZN 高階主管的賣出多集中於季度內固定日期（如 02-20/23、05-21、08-21、11-21），與股權歸屬週期高度吻合，較可能屬例行薪酬變現，訊號強度有限。需以 SEC Form 4 與 10b5-1 計畫註記確認，本次未取得。
- Bezos 2026-08-03 單筆 $346.5M 為窗口內最大單筆，屬需留意的事件，但其 gift 交易亦頻繁，單一數字不宜直接解讀為看空。

## Ownership shifts

- 機構持股占比：68.7%（流通股口徑 75.4%），機構數 7,881 家。
- 內部人持股：8.85%。
- 大型機構（最新季 2026-06-30）：BlackRock 6.94%（持股 7.48 億股，季增 +1.75%）、Vanguard 5.89%（季增幅未取得完整資料）。
- 本次僅取得單一時點快照，無法判斷多季趨勢；就最新季而言，頭部機構持股略增，集中度穩定。

## Net sentiment score

Composite：**偏多（bullish-leaning）**，信心：**中低**。

理由：
- 分析師端明確偏多：60 家中 58 家為買進側、無賣出評等（強權重）。
- 內部人端偏空但形式上多為例行變現，權重下調。
- 散戶端完全缺資料，無法納入，因此整體信心被壓低。

重要事件：下次財報 2026-10-29（yf 預估 EPS $1.95），在本報告日期之後約兩週。前一季（2026-07-30）yf 記錄的 Reported EPS 為 $5.75，對比估計 $1.83 差距達 214.89%，幅度異常，疑似含一次性項目，本次未查證，建議在財報解讀時確認。

Divergence flag：
- 散戶 vs 分析師：**無法判定**（散戶資料缺失）。
- 內部人 vs 分析師：**是**。分析師多數買進，內部人淨賣出，方向不一致；但 AMZN 內部人賣出的結構性因素較強，此分歧的資訊價值有限。

## 資料缺口與限制

1. Reddit、StockTwits 無法存取，散戶 buzz 與 tilt 無資料。
2. yf 無個別券商升降評等與目標價變動明細。
3. 內部人交易中部分列（無金額、約為行權或歸屬配對）未重複計入，金額以有 `Value` 的賣出列為準。
4. 第三方共識（MarketBeat、Barchart）為 2026 年 9 月與 4 月快照，非 10 月資料。

## 來源

- yf 快取：prices/yf/AMZN.json（recommendations、rec_summary、insider、major_holders、inst_holders、earnings_dates）
- [MarketBeat AMZN Forecast](https://www.marketbeat.com/stocks/NASDAQ/AMZN/Forecast/)
- [Barchart: Do Wall Street analysts like Amazon.com stock](https://www.barchart.com/story/news/1561848/do-wall-street-analysts-like-amazon-com-stock)
- [Barchart: Amazon.com stock analyst estimates ratings](https://www.barchart.com/story/news/3500348/amazon-com-stock-analyst-estimates-ratings?.tsrc=rss)
- [Yahoo Finance: How High Will Amazon Stock Go in 2026?](https://finance.yahoo.com/news/high-amazon-stock-2026-experts-152105608.html)
- [Interactive Brokers Campus (Benzinga 轉載，2025 年 10 月 Amazon 散戶討論)](https://www.interactivebrokers.com/campus/?p=233707)

SENTIMENT REPORT COMPLETE
