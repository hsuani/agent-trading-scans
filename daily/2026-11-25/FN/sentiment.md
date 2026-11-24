# Sentiment — FN (Fabrinet) as of 2026-11-25

註：本機日期為 2026-11-24，分析日期 2026-11-25 為晚於本機日期的設定值。yf 資料經 cookie/crumb 失敗後走快取回退，資料的實際更新時點未經確認。本報告不含交易建議。

## Analyst consensus

9 位分析師：3 strong buy / 4 buy / 2 hold / 0 sell / 0 strong sell。

| 項目 | 數值 |
|---|---|
| Buy 合計（strong buy + buy） | 7 位，佔 77.8% |
| Hold | 2 位，佔 22.2% |
| Sell | 0 位，佔 0% |

近期變動：yf 的 rec_summary 與 recommendations 工具回傳相同的四期快照（0m、-1m、-2m、-3m），四期數字完全一致，代表近四個月評級分布未變動。工具未提供逐筆升降評等紀錄，個別 upgrade / downgrade 事件與目標價變動為 DATA_UNAVAILABLE。

目標價（DATA_UNAVAILABLE，僅有過期網路資料）：WebSearch 找到的最新來源為 2026-03-19 前後的快照。一家追蹤網站平均目標價為 489.14 USD，另一家 Investing.com 英國頁為 582.22 USD。兩者日期不同，且都早於分析日期八個月以上，不能作為現值使用。另有來源指 JP Morgan 為 Neutral，日期不明。

## Retail social

- Reddit：DATA_UNAVAILABLE。WebFetch 無法連線 reddit.com，r/wallstreetbets 與 r/stocks 的搜尋均未取得。WebSearch 找不到 2026-11 的 r/wallstreetbets 討論串。ChartExchange 的 Reddit 追蹤頁僅有一則 2025-08 的 WSB 貼文「Good week so far with $FN」，情緒分數 0.44，屬過期資料。
- StockTwits：DATA_UNAVAILABLE。api.stocktwits.com 無法解析（DNS 失敗），需在工作階段網路設定中允許該網域後才能重試。
- X / 新聞輿情：WebSearch 未找到 2026-11 的相關內容，最新可查到的日期為 2026-03。Quiver Quant 的 AI 生成摘要描述社群對 FN 的 AI 動能樂觀，但為機器濃縮，日期不明。2026-03-06 FN 單日下跌 10.11%，收於 489.38 USD，屬過期資料。
- 聲量（buzz volume）：DATA_UNAVAILABLE，無提及次數可比對。
- 零售傾向：無法判定（資料缺失）。僅有的弱訊號為 AI 光通訊主題的正面情緒，但來源已過期且不可靠。
- 主要題材（僅依過期來源）：AI 資料中心與光模組需求、高估值與波動大。

## Insider activity

分析窗口：2026-05-25 至 2026-11-25（6 個月）。

| 日期 | 人員 | 職稱 | 類型 | 股數 | 金額（M USD） |
|---|---|---|---|---|---|
| 2026-09-03 | Edward T. Archer | Officer | 公開市場賣出（385.58–386.34） | 2,500 | 0.96 |
| 2026-08-11 / 08-20 | Seamus Grady | CEO | 股票獎勵（非現金買入） | 22,479 + 20,029 | 0 |
| 2026-08-11 / 08-20 | Harpal S. Gill | President | 股票獎勵 | 4,271 + 12,849 | 0 |
| 2026-08-11 / 08-20 | Csaba Sverha | CFO | 股票獎勵 | 2,698 + 7,559 | 0 |
| 2026-08-11 / 08-20 | Edward T. Archer | Officer | 股票獎勵 | 2,024 + 6,047 | 0 |

- 6 個月淨額：公開市場買入 0 USD；公開市場賣出約 0.96M USD（1 筆，Archer）。
- 窗口外但相近：2026-05-22 董事 Homa Bahrami 賣出 2,500 股，單價 711.91，金額 1.78M USD。
- 12 個月公開市場賣出（2025-11-25 至 2026-11-25）約 17.0M USD，買入 0。其中 CEO Seamus Grady 於 2025-11-26 賣出 22,451 股，約 10.03M USD，為最大單筆。其餘為董事 Kelly、Bahrami、Knight 的小額賣出，以及 2026-09-03 的 Archer 賣出。
- 內部人持股比例：0.259%。
- 資料注意：Harpal S. Gill 在多數列為 President，但 2025-06-04 一列標示為 CEO。此職稱不一致可能是資料來源錯誤，未修正。
- 解讀：6 個月內無公開市場買入，賣出金額小；大部分異動為例行股票獎勵。

## Ownership shifts

- institutionsPercentHeld 為 100.499%，institutionsFloatPercentHeld 為 100.76%。數值超過 100%，不可能成立，判定為資料來源重複計算的錯誤，不採用。
- 機構持有人數 975 位，為單一快照。
- 機構集中度趨勢：DATA_UNAVAILABLE（無時間序列，無法判斷增減）。

## Net sentiment score

- 分析師面：偏多。7/9 買進、0 賣出，評級四個月未變。信心中等，目標價資料過期。
- 內部人面：偏空（溫和）。6 個月無買入，1 筆約 0.96M USD 賣出；12 個月約 17.0M USD 賣出，其中包含 CEO 單筆 10.03M USD。信心中等。
- 零售面：無法判定。Reddit、StockTwits、X 均無近期可用資料。
- 綜合：中性偏多（信心低）。分析師一致偏多，內部人淨賣但 6 個月內金額有限，零售面缺資料，不足以提高信心。

Divergence flag：部分分歧。內部人（淨賣）與分析師（多數買進）方向相反。零售傾向無法判定，因此無法確認零售與分析師是否背離。

## 資料缺口總表

- DATA_UNAVAILABLE：Reddit（reddit.com 無法連線）、StockTwits（DNS 失敗）、零售聲量、近期逐筆評級變動、目標價現值、機構持股趨勢。
- 資料異常：機構持股比例超過 100%；Gill 職稱前後不一致。
- 過期來源：WebSearch 最新資料為 2026-03，無 2026-11 的社群或新聞資料。

SENTIMENT REPORT COMPLETE
