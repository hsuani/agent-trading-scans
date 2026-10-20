# Sentiment — 3653.TW（健策） as of 2026-10-21

## Analyst consensus
目前 11 家（4 Strong Buy / 7 Buy / 0 Hold / 0 Sell）。近 4 個月趨勢：Strong Buy 由 3 增至 4，Buy 由 6 增至 7，覆蓋家數由 9 增至 11，無降評紀錄。

近期重點動態（WebSearch 彙整，未能逐筆核對原始報告日期）：
- **大和資本（Daiwa）**：重申 Buy，12 個月目標價由 9,420 上調至 10,000 元。理由為平均售價提升與產品升級，預估第 3 季營收與毛利率有望創歷史新高。報導稱目標價隱含約 73x 遠期本益比，高於過去三年約 16x–53x 區間。
- **里昂（CLSA）**：目標價由 5,480 上調至 5,700 元，維持「優於大盤」，2026 年 EPS 上修至 62.38 元，受惠 Rubin 均熱片量產與水冷板含量提升。
- **共識目標價**：Investing.com 摘要顯示平均目標價約 4,998–5,070 元（數據版本不一，來源時點不同）。
- **負面事件**：2026 年 5 月曾傳出 NVIDIA 下一代 Rubin GPU 散熱設計降規消息，股價一週內跌幅超過 30%（來源為新聞彙整，未能取得當時完整分析師降評紀錄；`recommendations` 歷史表回傳空值）。
- 大和列出的下行風險：全球 AI 伺服器需求不如預期、散熱規格升級進度低於預期。

## Retail social
- **Reddit（r/wallstreetbets、r/stocks）**：DATA_UNAVAILABLE。WebFetch 無法連線 www.reddit.com，無法取得貼文樣本與多空傾向。
- **StockTwits**：DATA_UNAVAILABLE。api.stocktwits.com DNS 解析失敗（ENOTFOUND），soft-fail。
- **X / 新聞論壇聲量**：WebSearch 能找到的內容以法人報告與財經新聞為主，未找到可辨識的散戶貼文樣本。無法給出聲量與提及次數的可靠估計（DATA_UNAVAILABLE）。
- **Themes（以新聞與法人報告推估，非散戶原文）**：
  - AI 伺服器散熱（Rubin 世代 GPU 均熱片、水冷板）是核心多頭論點。
  - 高估值與 Rubin 設計進度是主要爭議點，對應 2026 年 5 月的大幅回檔事件。
  - 第 3 季營收與獲利創高的預期（報導提到 8 月自結 EPS 約 NT$7.35，年增約 95%；5 月營收年增約 37.75%）。
  - 報導提到 Intel、AMD PC 出貨放緩造成部分營收低於預期，屬於次要的負面因素。

## Insider activity
Net 6mo: DATA_UNAVAILABLE。`insider` 工具回傳空清單，且同時出現 Yahoo cookie/crumb 取得失敗（ConnectionError）。無法區分「期間無申報交易」與「資料抓取不完整」，因此不能據此判斷內部人淨買賣方向。
- Notable: DATA_UNAVAILABLE

## Ownership shifts
- 內部人持股比例：約 37.66%（`inst_holders` 摘要 insidersPercentHeld）。
- 機構持股比例：約 40.52%；占浮動股數約 64.99%。
- 機構家數：247。
- 歷史趨勢（季別持股變化）：DATA_UNAVAILABLE。`major_holders` 與 `inst_holders` 明細皆為空清單，僅回傳彙總值，無法判斷集中度是增加或減少。

## Data quality notes
- 股價：各來源數據互相矛盾（有報導 NT$6,800 為 9 月底收盤；其他來源顯示 NT$3,300–3,840 區間）。本報告未採用任何單一股價，目標價與估值倍數的相對距離需以即時行情重新核對。
- Yahoo cookie/crumb 取得失敗，部分 yf 工具回傳空值，未必代表實際無資料。
- Reddit 與 StockTwits 皆無法取得，散戶面向本次僅能以新聞與法人報告替代，無法代表真實散戶情緒。

## Net sentiment score
**Composite: bullish（信心：低）。**
- 分析師面：強烈偏多（11 家全部買進以上，目標價多數高於多數股價來源的現價區間，近期無降評）。信心高，但僅為單一面向。
- 散戶面：DATA_UNAVAILABLE，無法評分。
- 內部人面：DATA_UNAVAILABLE，無法評分。
- 整體信心偏低，原因是散戶與內部人兩大面向皆缺資料，而且股價來源不一致，無法確認目前估值是否仍低於目標價。

Divergence flag: **無法判定**（散戶面 DATA_UNAVAILABLE，無法比較與分析師傾向是否相反）。

## Sources
- [健策目標價 大和喊上萬元（udn）](https://money.udn.com/money/amp/story/5607/9786948)
- [里昂：健策今年 EPS 可達 62.38 元 目標價上調 4% 到 5,700 元（udn）](https://money.udn.com/money/amp/story/5607/9423686)
- [AI 晶片新設計助威 法人大升健策獲利預估值及目標價（udn）](https://money.udn.com/money/amp/story/5607/9802684)
- [Jentech Precision Industrial Co Ltd (3653)（Investing.com 共識）](https://www.investing.com/equities/jentech-consensus-estimates)
- [【投資快訊】健策(3653)：營收結構最佳化，股價上揚 9.78%（CMoney）](https://www.cmoney.tw/notes/note-detail.aspx?nid=939590)
- [健策 (3653) 電子零組件業（PChome）](https://pchome.megatime.com.tw/stock/sto1/ock4/sid3653.html)

SENTIMENT REPORT COMPLETE
