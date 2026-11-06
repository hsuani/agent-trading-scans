# Sentiment — 6223.TWO (旺矽科技) as of 2026-11-07

## Executive summary

- 分析師共識偏多: 14 家覆蓋中 13 家為買進等級 (strongBuy 4、buy 9)，hold 1 家，sell 0 家。最新一期相較前兩期多出 1 家 hold，覆蓋家數由 13 增至 14。
- 散戶輿情無法量化: Reddit 無法連線，StockTwits 依規定不以 WebFetch 讀取，只能用搜尋摘要判讀，且搜尋結果多為未標註日期的投資筆記。
- 內部人交易無資料: yf insider 回傳空陣列。這不等於內部人零交易，Yahoo 對台股 insider 申報的覆蓋可能不完整。
- 籌碼面: 機構持股約 54.9%，insider 持股約 12.5%，機構家數 209。缺乏時間序列，無法判斷集中度趨勢。
- 整體: 分析師端偏多、散戶端資料不足、估值為主要爭議。綜合信心低。

## Data availability

| 資料來源 | 狀態 | 說明 |
|---|---|---|
| yf rec_summary / recommendations | 可用 | 僅有彙總分布 (近三期)，無逐筆評等變動、無目標價 |
| yf insider | 空資料 | 回傳 []，6 個月淨買賣金額無法計算 |
| yf major_holders | 可用 | 單一快照，無歷史比較 |
| Yahoo cookie/crumb | 失敗 | fc.yahoo.com 連線失敗，以無 crumb 模式取得資料，資料日期未標註，無法確認是否為 2026-11-07 當日值 |
| Reddit (r/stocks, r/wallstreetbets) | 無法存取 | WebFetch 回報 unable to fetch，依規則跳過 |
| StockTwits | 未讀取 | 屬財經網站，依指示不以 WebFetch 讀取 |
| WebSearch (X / 新聞 / 論壇) | 部分可用 | 最新可查到的日期為 2026 年 10 月；11 月資料查無 |

日期紀律: 本報告只採用 2026-11-07 以前可確認日期的資料。搜尋結果中 2025 年的籌碼數據、2024–2025 年的目標價，以及 2026 年 1 月的本益比，均已排除，不作為現況依據。

## Retail / social sentiment read

- Reddit: 無法取得 r/stocks 與 r/wallstreetbets 的貼文，無法估計討論量與多空傾向。
- StockTwits: 未讀取。
- 中文財經筆記 (CMoney 投資快訊): 搜尋可見多則標題，例如「6223 旺矽：持續受惠於 AI 趨勢，股價表現強勁」、「全球懸臂式探針卡廠龍頭，股價上漲 8.05%」。標題語氣偏多，但多數未標註發布日期，且屬媒體/平台內容，不能視為純散戶情緒。
- 10 月新聞中的正負面:
  - 正面主題: AI 與高效能運算帶動的高階探針卡需求、MEMS 探針卡與 CPO 相關測試題材。
  - 負面主題: 估值偏高，搜尋摘要顯示本益比約 103.56、股價淨值比約 30.13 至 34.59 (各來源不一致)；另有公司因違反水污染防治法遭裁罰的公告 (10/22)。
- 討論量: 無法量化，無法與平常基準比較。
- 主要主題 (依可查資料): AI 探針卡需求、估值是否過高、環保裁罰的影響。

引述 (≤15 字，來自搜尋標題，非原文全文):
- 「持續受惠於AI趨勢，股價表現強勁」(CMoney 投資快訊，日期未確認)

Retail tilt: 無法判定，資料不足。

## Analyst consensus

最新分布 (yf rec_summary，0m 期):

| 評等 | 家數 |
|---|---|
| strongBuy | 4 |
| buy | 9 |
| hold | 1 |
| sell | 0 |
| strongSell | 0 |
| 合計 | 14 |

- 買進等級占比約 92.9% (13/14)。
- 前兩期 (-1m、-2m) 皆為 13 家全數買進等級，0 家 hold。最新期多出 1 家 hold，合計由 13 增至 14。這可能是新增覆蓋或評等下調，工具只給彙總值，無法區分。
- 逐筆升降評等: 工具無逐筆資料，無法列出具體升級或降級券商。
- 目標價: 工具未提供，無法判斷目標價調整方向。本報告不引用舊目標價。

## Institutional / insider signal

- Insider 6 個月交易: 無資料 (空陣列)。無法計算淨買賣金額，也無法判斷 CEO/CFO 是否有動作。
- Insider 持股比例: 約 12.52%。
- 機構持股: 約 54.88% (占已發行股數)，占流通股約 62.74%，機構家數 209。
- 趨勢: 單一快照，無法判斷集中度是升或降。
- 籌碼面 (外資、投信日買賣超): 本次未取得 2026 年 10 月以後的可靠資料。搜尋到的買賣超數字皆為 2025 年或更早，已排除。

## Overall sentiment verdict

- 分析師端: 偏多 (13/14 買進等級)，信心中等。覆蓋家數少，且無目標價與逐筆變動資料。
- 散戶端: 無法判定。Reddit 與 StockTwits 皆無資料，中文財經平台標題偏多但日期不明。
- 內部人端: 無資料，不計入評分。
- 機構端: 持股比例高 (約 55%)，但無趨勢，中性。
- 估值與事件: 估值高、環保裁罰為 10 月的主要負面話題，會抵銷部分分析師偏多訊號。

Composite: 中性偏多 (neutral-to-bullish)，信心低。主因是分析師端一致偏多，但散戶、insider 與機構趨勢資料缺口大。

Divergence flag: 無法判斷。散戶傾向資料不足，無法確認是否與分析師傾向相反。

## Sources

- yf 工具輸出 (本地): `pipeline/tools/yf 6223.TWO rec_summary`、`recommendations`、`insider`、`major_holders` (2026-11-07 執行)
- Reddit 嘗試 (無法存取): https://www.reddit.com/r/stocks/search.json?q=6223&sort=new&limit=25&restrict_sr=1 ; https://www.reddit.com/r/wallstreetbets/search.json?q=6223&sort=new&limit=25&restrict_sr=1
- WebSearch 摘要 (非原文，日期多未確認):
  - https://www.cmoney.tw/notes/note-detail.aspx?nid=920162 (CMoney 投資快訊，AI 趨勢)
  - https://www.cmoney.tw/notes/note-detail.aspx?nid=853069 (CMoney 投資快訊，股價上漲 8.05%)
  - https://goodinfo.tw/tw/StockDetail.asp?STOCK_ID=6223 (財報評分、10/16 收盤價 5,205 元)
  - https://www.nstock.tw/6223?status=5 (本益比、股價淨值比、EPS 47.22 元，更新 2026-10-22)
  - https://tw.stock.yahoo.com/quote/6223/institutional-trading (僅見 2025 年 12 月資料，已排除)

SENTIMENT REPORT COMPLETE
