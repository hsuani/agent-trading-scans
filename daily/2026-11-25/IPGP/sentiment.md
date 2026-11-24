# Sentiment — IPGP as of 2026-11-25

資料來源狀態：
- yf 工具（ratings / insider / holders）：Yahoo cookie/crumb 連線失敗，改用快取資料回傳，屬於正常 fallback。
- Reddit（r/wallstreetbets、r/stocks）：WebFetch 無法連線 www.reddit.com，視為 DATA_UNAVAILABLE。
- StockTwits API：DNS 解析失敗（api.stocktwits.com 不在允許網域內），視為 DATA_UNAVAILABLE。
- X / 新聞：以 WebSearch 取得零散片段，多數日期不明。

## Analyst consensus

yf rec_summary（9 位分析師）：強買 2 / 買 4 / 持有 2 / 賣 0 / 強賣 1。
- 買方比例 66.7%（6/9），持有 22.2%（2/9），賣方 11.1%（1/9）。
- 注意：rec_summary 與 recommendations 三個期間（0m、-1m、-2m）數字完全相同，疑似快取過舊，不宜當作即時分布。
- 與 Investing.com 的統計衝突：該站為 7 位分析師，買 6 / 持有 2 / 賣 1。

近期評等與目標價變動（網路來源，日期有衝突）：
- Needham 由 Hold 升為 Buy，時間為 2026-05-06（Fintel、Yahoo 報導）。Benzinga 則描述同日為目標價調升至 $110，兩者說法不一。
- Citigroup 目標價 $150 調整為 $137，日期為 8/11/2026（日期格式可能是 11/8，需再確認）。
- Stifel 維持 Buy，目標價 $125（6/29 與 7/17 紀錄）。
- Raymond James 於 2026-02-13 有目標價調整，非明確評等調降。
- yf 的 recommendations 工具沒有可驗證的升降評事件。

目標價區間（各站快照不一）：
- Benzinga 共識約 $120.71 至 $121.14。
- Google Finance 平均 $131.42（6 位）。
- Fintel 平均 $147.64（2026-04-28），區間 $93.42 至 $189.00。
- Investing.com 區間約 $97 至 $126。

股價參考有衝突：2026 年內部人成交價約 $75 至 $137，最近一筆 2026-11-03 為 $75.18；網路片段則顯示 $65 至 $130 不等。本報告不以單一股價做結論。

## Institutional and ownership

- 內部人持股 38.96%。
- 機構持股 79.25%，機構家數 477。
- 機構持股變化趨勢：DATA_UNAVAILABLE，目前只有單一快照，無法判斷季度增減。
- 異常值：institutionsFloatPercentHeld 為 129.8%，超過 100%，明顯資料錯誤，本報告不採用。

## Retail social

- Reddit：DATA_UNAVAILABLE（連線遭拒，無法取得 r/wallstreetbets、r/stocks 貼文與熱度）。
- StockTwits：DATA_UNAVAILABLE（DNS 失敗）。WebSearch 片段中有一則無日期快照標示 Bearish，當時股價約 $92.53，時效性不明。
- 其他片段（時效不一）：
  - TipRanks 部落客情緒中性，僅兩則意見樣本，較科技板塊整體偏空。
  - Benzinga 顯示放空比率（short interest）約 21.9% of float，偏高。
  - Zacks 與 Nasdaq 文章提到營業利益率收縮、年初至今跌約 30%、盈餘預估下修（日期不明）。
  - Barchart 認為股價在上漲後風險偏高，前瞻本益比約 63.7 倍。
- 聲量（buzz volume）：DATA_UNAVAILABLE，無法取得提及次數與歷史基準。
- 主要話題（由網路片段歸納，非社群原文）：估值偏高、利潤率壓力、盈餘預估下修、放空比率高。
- 零售語氣：偏空或分歧，證據薄弱，信心低。

## Insider activity

6 個月窗口為 2026-05-25 至 2026-11-25。金額單位為 USD（M）。

| 身分 | 交易 | 日期 | 金額 (USD M) |
|---|---|---|---|
| Gapontsev 信託（10% 以上持股人） | 賣出 3 筆 | 7/21、9/2、11/3 | 賣出 9.38 |
| IP Fibre Devices（10% 以上持股人） | 賣出 4 筆 | 6/29、7/31、8/5、10/2 | 賣出 13.34 |
| Scherbakov Eugene（董事，兼 10% 以上持股人） | 賣出 3 筆 | 6/29、7/31、10/2 | 賣出 0.55 |
| LoPresti Angelo（總法律顧問） | 賣出 1 筆 | 6/29 @ $110.33 | 賣出 0.11 |
| Tang Agnes（董事） | 賣出 1 筆 | 6/22 | 賣出 0.18 |
| Peeler John R（董事） | 買進 1 筆 | 8/26 @ 約 $73.7，2,710 股 | 買進 0.20 |

- 合計：買進 0.20M，賣出 23.56M，淨賣出約 23.36M。
- 扣除 10% 以上持股實體後：官員與董事賣出 0.84M，買進 0.20M，淨賣出約 0.64M。
- 10% 以上持股實體的身分（疑似創辦人 Gapontsev 家族關聯）需再確認。
- 窗口外：CFO Mammen Timothy 於 2026-05-22 賣出 1.20M（窗口起點 5/25 之前，未計入）。
- CEO Gitin Mark：窗口內僅有股票授予（stock award），無公開市場買賣紀錄。
- 2026-05-12 董事會成員有股票授予，無現金金額。
- 解讀：大額賣出集中在 10% 以上持股實體，官員與董事買賣規模小，且只有一筆公開市場買進。

## Net sentiment score

- 分析師面：中性偏多（信心中）。買方 6/9，但評等資料快取過舊，且各站數字互相衝突。
- 內部人面：偏空（信心中）。窗口內大額淨賣出，但主要來自 10% 以上持股實體，官員與董事淨賣出規模小。
- 零售面：DATA_UNAVAILABLE 為主，網路片段偏空（信心低）。
- 綜合：中性（信心低）。資料缺口多，尤其 Reddit、StockTwits、聲量與機構趨勢皆缺。

Divergence flag：是。分析師整體偏多，與零售片段偏空、內部人大額淨賣出方向相反。此訊號來自薄弱證據，解讀時需保守。

資料品質提醒：yf rec_summary 與 recommendations 疑似快取過舊；機構 float 百分比超過 100%；股價來源互相衝突；Investing.com 與 yf 分析師家數不同。

SENTIMENT REPORT COMPLETE
