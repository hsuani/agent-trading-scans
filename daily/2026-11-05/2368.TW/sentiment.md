# Sentiment — 2368.TW (金像電) as of 2026-11-05

**資料時效警告:** 今天系統日期是 2026-11-04,要求的分析日期 2026-11-05 尚未到達。以下資料最新只到約 2026-07 至 2026-08,沒有 10 月、11 月的股價、法人或社群資料。本報告的判讀可信度因此偏低,請勿把它當成當日情緒快照。

## Analyst consensus
rec_summary(0m):9 家中 strongBuy 1 / buy 8 / hold 0 / sell 0 / strongSell 0,即 9 家全數偏多。近 1、2 個月的快照相同,沒有評等變動。
recommendations 歷史表為空,無法列出 upgrade/downgrade 紀錄。
目標價方面,媒體報導的時間點與數字彼此不一致,需自行查證:
- 3 月:法人大幅上修獲利與目標價,一則報導指目標價上調逾五成至 1,100 元。
- 約 5 月:大和資本目標價由 1,100 元上調至 1,380 元,本益比目標由 26 倍調至 30 倍。
- 6-7 月:一篇獨立媒體彙整文章提到 1,700 元目標價,但它不是正式券商報告,來源不明確。
- 高盛在更早的報導中有目標價 725 元,買進評等,時間點不明。
- 7 月 21 日收盤價約 980 元。10 月的新目標價沒有找到。

## Retail social
- Reddit(r/stocks、r/wallstreetbets):無法取得,WebFetch 遭拒。本次未取得任何貼文樣本。
- StockTwits:無法取得,api.stocktwits.com 無法解析(需在 session 網路設定中允許該網域)。
- X / 新聞聲量:搜尋結果只到 2026 年中。CMoney 社群的討論偏分歧,有人認為信心偏弱,也有人認為 PCB 與 AI 題材仍有推升空間。這是媒體摘要的描述,不是直接引用的貼文。
- 聲量相對一般水準:無法量化。
- 主要題材(來自媒體,非社群直接取樣):ASIC 客戶需求、800G 交換器、Google TPU 板卡供應鏈、AWS Trainium 3 放量、HDI 良率風險。
- 散戶傾向:無法判定,標記為資料不足。

## Insider activity
Net 6mo:無法判定。yf insider 回傳空陣列,而 Yahoo cookie/crumb 取得失敗,可能是資料缺漏,也可能是該標的在此來源無資料。不能據此判斷「無內部人交易」。
內部人持股比例(insidersPercentHeld)為 30.1%,這是持股結構,不是買賣方向。

## Ownership shifts
- 機構持股(institutionsPercentHeld)38.98%,占流通股(float)55.77%,機構家數 250。
- 只有單一時點快照,無法判斷集中度趨勢。

## Net sentiment score
Composite:**偏多(信心低)**。
- 分析師面:9 家全數買進或強力買進,偏多,信心中等偏高。
- 散戶面:無可用的 Reddit、StockTwits 資料,社群訊號只有零星媒體描述,分歧,無法評分。
- 內部人面:無資料。
- 資料時效:最新資料約 3 個月前,評分應視為過期參考。

Divergence flag:**無法判定**。散戶面資料不足,不能確認散戶與分析師是否方向相反。

## Data gaps and next steps
1. 補 2026-11 的 Reddit 或 StockTwits 資料,需允許 api.stocktwits.com 網域,Reddit 也需要可用的抓取方式。
2. 重新檢查 yf insider 的 Yahoo cookie 問題,或改用台灣 MOPS 內部人申報資料。
3. 取得 10 月後的券商目標價與評等變動。
4. 補最新收盤與三大法人買賣超,以校正上述評分。

SENTIMENT REPORT COMPLETE
