# Sentiment — 6213.TW 聯茂 as of 2026-10-29

資料抓取日為 2026-10-28（系統日期），報告依任務設定標示 2026-10-29。散戶社群與內部人資料缺漏，綜合結論信心低。

## Analyst consensus

目前 9 家券商：7 buy（strongBuy 3 + buy 4）/ 1 hold / 1 sell / 0 strongSell。

| 期間 | Buy | Hold | Sell | 備註 |
|---|---|---|---|---|
| 0m（現在） | 7 | 1 | 1 | |
| -1m | 7 | 1 | 1 | 無變化 |
| -2m | 7 | 1 | 1 | 無變化 |
| -3m | 4 | 3 | 1 | 較現在 buy 少 3 家、hold 多 2 家 |

近期變動：過去約 3 個月 buy 家數由 4 增至 7，hold 由 3 降至 1，近兩個月合計數字無變化。yfinance 只給彙總數字，個別券商升降評等明細無法取得。

目標價：yfinance 無目標價欄位。搜尋來源單一提及一家日系外資將目標價調升至 1,110 TWD，理由為 CCL（銅箔基板）漲價，尚未以其他來源交叉驗證，列為待確認。

## Retail social

- **Reddit**：無法取得。r/wallstreetbets 與 r/stocks 的 search.json 請求被工具封鎖（無法連線 www.reddit.com）。討論量與多空傾向皆無資料。
- **StockTwits**：無法取得。api.stocktwits.com 解析失敗（DNS ENOTFOUND），需在 session 網路設定中允許該網域後才能重試。
- **X / 新聞**：僅一次 WebSearch，結果以新聞與報價頁為主，未見散戶個別貼文或情緒標籤。討論量無 baseline，無法做定性比較。
- **可用 quote sample**：無（未取得任何散戶貼文，不引用）。

主題（僅來自新聞，非散戶原文）：
1. 營收高成長：5 月合併營收 38.03 億 TWD（月度歷史新高），6 月 42.14 億 TWD，年增 47.9%；1–6 月累計 206.73 億 TWD，年增 25.6%。
2. 股價波動大：8 月 11 日收 452 TWD，前有八連漲；10 月報價落在約 760–774 TWD。
3. 產業題材：外資以 CCL 漲價為調升依據。
4. 資料不一致：來源之間的價格與日期有出入（例如 1 月約 115 TWD 與 8 月 452 TWD 的走勢跨度過大），數字僅供參考，需以行情源確認。StatementDog 提到本益比約 120 倍，同樣未經交叉驗證。

Retail tilt：無法判定。

## Insider activity

yfinance insider 回傳空陣列，無法取得近 6 個月內部人申報交易，因此無法計算淨買賣金額，也無法指出 CEO/CFO 或其他人員的動向。空陣列可能是資料缺漏，不代表沒有交易，建議人工查詢公開資訊觀測站（MOPS）內部人持股申報。

持股結構快照：內部人持股比例 37.64%，屬高度集中。

## Ownership shifts

- 機構持股比例 7.72%（占已發行股數），占浮動股數 12.37%，機構家數 46 家。
- 只有單一時點快照，無法判定機構持股趨勢是增加或減少。

## Net sentiment score

- 分析師：偏多（7/9 buy，過去三個月 buy 側增加）。
- 散戶：無資料（Reddit 與 StockTwits 皆不可用）。
- 內部人：無資料。

**Composite：偏多（bullish），信心低。** 結論只建立在分析師結構上，散戶與內部人兩項缺漏，且目標價與價格來源未經交叉驗證。

**Divergence flag：無法判定。** 缺乏散戶資料，無法比較散戶與分析師的傾向是否相反。

## 來源（WebSearch）

- [nstock 6213](https://www.nstock.tw/6213)
- [StatementDog 6213](https://statementdog.com/analysis/6213)
- [TechNews 2026-06 月營收](https://finance.technews.tw/2026/07/03/iteq-6213-202606-financial-report/)
- [Yahoo 股市 6213 新聞](https://tw.stock.yahoo.com/quote/6213/news)
- [Yahoo 股市 6213 多空](https://tw.stock.yahoo.com/quote/6213/bullbear)
- [nStock 聯茂做什麼](https://nstock.tw/聯茂做什麼.html)

SENTIMENT REPORT COMPLETE
