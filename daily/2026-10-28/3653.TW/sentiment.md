# Sentiment — 3653.TW（健策） as of 2026-10-28

資料時點說明：Yahoo 即時呼叫失敗（cookie/crumb ConnectionError），以下 yf 數據全部取自 `prices/yf/3653.TW.json` 快取（`_refreshed_at` 為 2026-10-27 12:01 UTC，未超過 14 天上限）。Reddit 與 StockTwits 無法連線，散戶面僅能以新聞與法人報告替代。

## Analyst consensus
目前 11 家：**4 Strong Buy / 7 Buy / 0 Hold / 0 Sell**，即 **100% 買進**（買進以上）。

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 合計 |
|---|---|---|---|---|---|---|
| 0m（本期） | 4 | 7 | 0 | 0 | 0 | 11 |
| -1m | 4 | 7 | 0 | 0 | 0 | 11 |
| -2m | 3 | 7 | 0 | 0 | 0 | 10 |
| -3m | 3 | 6 | 0 | 0 | 0 | 9 |

- 趨勢：近 3 個月覆蓋家數由 9 增至 11，Strong Buy 由 3 增至 4，全期無降評、無 Hold 或 Sell 紀錄。
- `recommendations` 歷史逐筆表在快取中僅有期別彙總，無法核對個別機構的升降評日期。

近期目標價動態（WebSearch 彙整新聞報導，未逐筆核對原始報告）：
- **大和資本（Daiwa）**：維持 Buy，12 個月目標價由 9,420 元上調至 10,000 元（NT$/股）。理由為平均售價提升與可拆卸三片式均熱片。風險提示為 AI 伺服器需求不如預期、散熱規格升級進度落後。
- **里昂（CLSA）**：維持「優於大盤」，目標價由 5,480 元上調至 5,700 元（NT$/股），2026 年 EPS 預估約 62.38 元，2027 年約 142.32 元。
- **其他（2026 年 3–5 月報導）**：摩根大通、CLSA、野村等多數維持買進，目標價約 4,785 至 6,130 元。
- **目標價離散度大**：約 4,800 至 10,000 元，主要差異來自各家對 Rubin 世代規格與平均售價的假設不同。
- **股價來源不一致**：報導中的股價在 NT$3,300 至 6,800 之間，多個來源互相矛盾。本報告不採用任何單一股價計算上行空間。Investing.com 頁面顯示的 3,840 元判定為舊資料。

## Retail social
- **Reddit（r/wallstreetbets、r/stocks）**：DATA_UNAVAILABLE。WebFetch 回報無法連線 www.reddit.com，無法取得貼文樣本、分數或留言數，因此無法判斷多空傾向。
- **StockTwits**：DATA_UNAVAILABLE。api.stocktwits.com DNS 解析失敗（ENOTFOUND），屬於 session 網路白名單未開放，soft-fail。
- **X / 論壇聲量**：WebSearch 找到的內容以法人報告與財經新聞為主，未找到可辨識的散戶貼文樣本。提及次數與相對於平常的聲量均無法可靠估計（DATA_UNAVAILABLE）。
- **主題（以新聞與法人報告推估，非散戶原文）**：
  - AI 伺服器散熱（Rubin 世代均熱片、水冷板含量提升）是核心多頭論點。
  - 高估值是主要爭議。報導指出 Daiwa 目標價隱含遠期本益比約 73 倍，高於過去三年約 16 至 53 倍區間。
  - 獲利動能：8 月自結 EPS 約 NT$7.35，年增約 95%（9/29 公告）。5 月營收年增約 37.75%。
  - 負面事件：2026 年 5 月曾傳出 NVIDIA 下一代 Rubin 散熱設計可能降規，股價一週內跌幅超過 30%（新聞彙整，未取得當時完整分析師降評紀錄，屬於未驗證資訊）。
  - 次要負面因素：部分 PC 客戶（Intel、AMD）出貨放緩，影響部分營收。

## Insider activity
Net 6mo: DATA_UNAVAILABLE。`insider` 工具與快取皆回傳空清單，且 Yahoo 即時呼叫失敗，無法區分「6 個月內無申報交易」與「資料抓取不完整」。因此不能判定內部人淨買或淨賣方向，也無法給出金額（不以 0 代替）。
- Notable: DATA_UNAVAILABLE（CEO、CFO 或其他董監事的交易紀錄皆未取得）。

## Ownership shifts
- 內部人持股比例：約 37.66%。
- 機構持股比例：約 40.58%，占浮動股數約 65.10%。
- 機構家數：247。
- 季度持股變化：DATA_UNAVAILABLE。`major_holders` 與 `inst_holders` 明細皆為空，僅有彙總值，無法判斷機構集中度是增加或減少。

## Net sentiment score
**Composite: bullish（信心：中低）。**
- 分析師面：強烈偏多。11 家全部買進以上，近 3 個月無降評，目標價多數高於多數股價來源的價位。信心高，但只有單一面向。
- 散戶面：DATA_UNAVAILABLE，不評分。
- 內部人面：DATA_UNAVAILABLE，不評分。
- 機構面：持股比例高，但缺少趨勢資料，只作為中性背景，不計入方向。
- 整體信心降為中低，原因是散戶與內部人兩大面向皆缺資料，且股價來源不一致，無法確認目前估值相對目標價的距離。

Divergence flag: **無法判定**。散戶面 DATA_UNAVAILABLE，無法與分析師傾向比較是否相反。

## Data quality notes
- yf 即時呼叫因 Yahoo cookie/crumb 失敗，全部改用快取（2026-10-27 12:01 UTC）。`insider`、`inst_holders`、`major_holders` 明細為空。
- Reddit、StockTwits 無法連線，X 無有效散戶樣本。
- 股價來源矛盾（NT$3,300 至 6,800），未採用單一股價。

## Sources
- [健策目標價 大和喊上萬元（udn）](https://money.udn.com/money/amp/story/5607/9786948)
- [里昂：健策今年 EPS 可達 62.38 元 目標價上調 4% 到 5,700 元（udn）](https://money.udn.com/money/amp/story/5607/9423686)
- [Jentech Precision Industrial Co Ltd (3653)（Investing.com 共識）](https://www.investing.com/equities/jentech-consensus-estimates)
- [【投資快訊】健策(3653)：營收結構最佳化，股價上揚 9.78%（CMoney）](https://www.cmoney.tw/notes/note-detail.aspx?nid=939590)
- [3653 健策 股價與估值（statementdog）](https://statementdog.com/analysis/3653)

SENTIMENT REPORT COMPLETE
