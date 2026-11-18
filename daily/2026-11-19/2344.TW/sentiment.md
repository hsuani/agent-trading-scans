# Sentiment — 2344.TW (華邦電 Winbond) as of 2026-11-19

> 資料時點注意：執行日為 2026-11-18，報告指定 as-of 2026-11-19。yfinance 分析師與股東資料為當下快照；網路搜尋結果最新僅到 2026 年 10 月，未找到 11 月資料。

## Analyst consensus

8 家分析師：3 strongBuy / 4 buy / 1 hold / 0 sell（共 7 bullish、1 neutral、0 bearish）。

- 近 1 個月分布變化：前一期（-1m）為 4 strongBuy / 4 buy / 0 hold，本期多出 1 家 hold，其餘未變，屬於小幅轉趨保守，未見評等集體下修。
- 近 3 個月趨勢：-3m 為 4 strongBuy / 3 buy，整體評等分布穩定偏多。
- 個別券商（次要來源，日期與完整性未經驗證）：JPMorgan 目標價於 2026-07-15 上調至 NT$360；Morgan Stanley 2026-03-19 下調至 Hold，目標價 NT$140。WebSearch 另一頁顯示平均 12 個月目標價約 NT$234，日期不明。
- 目標價與股價資料來源彼此衝突（10 月中旬約 NT$155.5 至 NT$177 之間），需以即時報價確認，本報告不採用單一股價作為比較基準。
- yfinance `recommendations` 端點回傳內容與 `rec_summary` 相同，未提供逐筆評等變動明細，故無法列出確切的升降評日期。

## Retail social

- Reddit（r/wallstreetbets、r/stocks）：**資料取得失敗**。WebFetch 回報 "Claude Code is unable to fetch from www.reddit.com"，無法取得貼文樣本、討論量或多空傾向。
- StockTwits：**資料取得失敗**。`api.stocktwits.com` DNS 無法解析（ENOTFOUND），需在 session 網路設定中允許該網域後才能重試。
- X / 新聞與論壇（WebSearch，一次搜尋）：Investing.com 使用者意見區顯示看法分歧，10 月貼文偏多、9 月多為偏空；此為零星個別留言，未做加權，不能代表整體散戶情緒。
- Buzz 量：**無法量化**。缺少 Reddit / StockTwits 的提及數，無法與歷史常態比較。
- Themes（僅來自有限搜尋結果）：記憶體景氣循環與報價、產能擴充（10 月 14 日一則公告：購置機器設備約 NT$17 億，即 NT$1.7B）、股價波動幅度大（52 週區間約 NT$16.5 至 NT$233.5）。

**社群情緒結論：本次無足夠社群資料可判讀散戶傾向，明確標示為缺失。**

## Insider activity

Net 6mo: **無資料**。yfinance `insider` 端點回傳空陣列。空陣列代表工具未取得交易紀錄，不能直接解讀為「零交易」，需以 TWSE 公開資訊觀測站的董監事持股異動申報再行核對。

Notable: 無可引用之 CEO / CFO 或其他內部人交易紀錄。

## Ownership shifts

- 內部人持股：約 30.3%
- 機構持股（佔總股本）：約 27.6%；佔流通股約 39.6%
- 機構法人數：220 家
- 歷史趨勢：工具僅提供當期快照，無法判斷近期增減，趨勢欄位標示為無資料。

## Net sentiment score

Composite: **偏多（信心低）**。
- 分析師面：偏多（7/8 bullish，評等穩定，近期僅 1 家轉 hold）。
- 散戶面：無可靠資料，不納入加權。
- 內部人面：無資料，不納入加權。
- 整體偏多僅來自分析師單一來源，且股價與目標價來源不一致，信心評為低。

Divergence flag: **無法判定**。散戶傾向資料缺失，無法確認是否與分析師傾向相反。若日後取得 Reddit 或 StockTwits 資料，再重新評估。

SENTIMENT REPORT COMPLETE
