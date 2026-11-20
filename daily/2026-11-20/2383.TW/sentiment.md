# Sentiment — 2383.TW (台光電 Elite Material) as of 2026-11-20

資料來源受限，見下方「資料缺口」。

## Analyst consensus

18 buy / 0 hold / 0 sell（yfinance rec_summary：strongBuy 6、buy 12，0m 期間）。近四個月評級分布：-3m 為 16 家（5+11）、-2m 為 17 家（6+11）、-1m 與 0m 為 18 家（6+12）。近三個月淨增 2 家買進評等，沒有看到降評或改為中立。yfinance 的 recommendations 欄位回傳內容與 rec_summary 相同，無法確認個別升降評事件。

個別目標價（網路搜尋彙整，非 yfinance 原始資料，需核對）：
- Nomura/Instinet：Buy，目標價 8,015 TWD（2026-08-20）
- Macquarie：Buy，目標價 9,100 TWD（2026-08-03）

目標價單位為 TWD/股，不是億元。本報告沒有取得市值或總營收數字，無法進行億元換算。

## Retail social

- Reddit：r/wallstreetbets 與 r/stocks 的 JSON 搜尋皆被擋（工具回報 Claude Code 無法存取 www.reddit.com）。無法取得討論量、貼文樣本或多空傾向。
- StockTwits：api.stocktwits.com 無法解析（DNS 失敗），需在 session 網路設定中允許該網域後才能重試。
- X / 新聞：一般搜尋未找到可辨識的散戶多空討論，只找到分析師評等與公司公告。
- 討論量：無法估計相對於平常的水準（資料不足）。
- 主題：無法從散戶來源歸納。公司端的主要新聞是 11/04 否認媒體報導的「2026 年 EPS 成長 43%」說法，以及 2026 Q2 財報 EPS 與營收高於市場預期（來源為 Simply Wall St 摘要）。

## Insider activity

Net 6mo：無資料。yfinance insider 回傳空陣列，無法區分「六個月內沒有申報交易」與「資料源缺漏」。不應解讀為零交易。需從臺灣公開資訊觀測站（MOPS）的董監事持股異動申報確認。

## Ownership

- 機構持股約 48.6%（institutionsPercentHeld）；佔流通股比例約 60.1%
- 機構家數：381
- 內部人持股約 19.0%（insidersPercentHeld）
- 這是單一時點快照，無法判斷機構集中度的趨勢是增加或減少。

## 資料缺口與數據品質

1. 股價水準互相矛盾：搜尋結果中一頁顯示 4,100 TWD（前收 4,555 TWD，52 週區間 1,295–6,470 TWD），另一頁 MarketScreener 顯示 1,495 TWD、年初至今 +141.91%。日期格式「05/11/2026」也可能是 5 月 11 日或 11 月 5 日。這份報告沒有使用任何股價數字做判斷，需以交易所即時報價為準。
2. 技術面訊號矛盾：同一來源的兩個頁面，一個顯示 Strong Sell，另一個顯示 Strong Buy。不納入本報告。
3. 分析師家數：yfinance 為 18 家買進，搜尋彙整的 Investing.com 為 16 家買進。本報告以 yfinance 為準。
4. yfinance 的 cookie/crumb 取得失敗，資料可能不完整。

## Net sentiment score

Composite：**偏多（bullish），信心低**。

- 分析師面：強烈偏多。18 家買進、0 家持有或賣出，近三個月淨增評等，目標價為 8,015 至 9,100 TWD（2026 年 8 月的資料，日期偏舊）。
- 散戶面：無法評估（Reddit、StockTwits 皆無法存取，搜尋找不到可用的散戶討論）。
- 內部人面：無資料。
- 信心低的原因：只有單一來源（分析師）可用，缺少散戶與內部人資料，且股價資料互相矛盾，無法確認目標價與現價的關係。

Divergence flag：**無法判定**。缺少散戶資料，無法比較散戶與分析師傾向是否相反。若之後補上 Reddit 或 StockTwits 資料，應重新評估。

## 建議後續補充

- 允許 api.stocktwits.com 網域後重試 StockTwits
- 以 Reddit 替代來源（例如 PullPush 或其他公開 archive）補充 WSB/stocks 討論量
- 從 MOPS 補抓近六個月董監事申報，確認內部人淨買賣
- 以 TWSE 即時報價確認現價，並核對 Nomura、Macquarie 目標價的發布日期

SENTIMENT REPORT COMPLETE
