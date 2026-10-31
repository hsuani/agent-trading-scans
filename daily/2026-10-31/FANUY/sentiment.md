# Sentiment — FANUY as of 2026-10-31

資料完整度偏低: Reddit、StockTwits 無法取得, 內部人交易為空, 機構持股數據疑似異常。以下結論信心等級為「低」。

## Analyst consensus
目前 (period 0m) 2 位分析師: 1 strong buy / 1 hold / 0 sell (樣本數極少)。
- 近 1 個月: 2 hold (無 buy)。
- 近 2 個月: 2 hold。
- 近期變動: 由 2 hold 轉為 1 strong buy + 1 hold, 屬於 hold 轉偏多方向, 但樣本只有 2 位, 單一評級即可改變結構。
- 第三方網頁摘要 (WebSearch, 非 yfinance 直接來源) 提到 2026-10-08 一則 Seeking Alpha 分析 給予 "Buy", 理由為工廠自動化與機器人銷售受美國回流製造 (reshoring) 與日本需求帶動。此為二手引述, 未能核對原文, 與 yfinance 的 1 strong buy 方向一致, 但不可視為獨立第二來源。
- 目標價 (target price) 變動: 本次工具未提供, 無法評估。
- 財報: 依網頁資料, 下一次財報日期列為 2026-10-22 至 10-23。截至 2026-10-31 已過財報窗口, 但本次搜尋未找到財報結果或財報後評級變動, 無法判斷財報後的情緒反應。

## Retail social
- Reddit (r/wallstreetbets、r/stocks): 無法取得。WebFetch 回傳 "Claude Code is unable to fetch from www.reddit.com", 本次無法查看貼文數、分數與語氣, 無法提供熱門貼文樣本。
- StockTwits / X: StockTwits 因 api.stocktwits.com DNS 解析失敗 (ENOTFOUND) 無法存取, 需於 session 網路設定中允許該網域後才能重試。X 端未找到可靠的 2026-10 當月貼文。
- 一般網路搜尋結果: 找到的觀點多為 Pluang、Investing.com、MarketBeat 等聚合頁面, 並非散戶社群原始貼文, 不能代表散戶情緒。
- 討論量 (buzz volume): 無法量化, 無法與平常基準比較。
- 散戶傾向 (tilt): 無法判定, 信心低。
- 主要主題 (依聚合頁面推論, 非社群原文): 工廠自動化與機器人需求、美國回流製造、日本市場需求。
- 注意: FANUY 為 ADR (美國存託憑證, OTC), FANUF 為日本本地股的另一報價代號, MarketBeat 上 FANUF 的做空比率數據不可直接套用到 FANUY。

## Insider activity
Net 6mo: $0 buys, $0 sells (yfinance insider 回傳空陣列)。
- 注意: 空陣列可能代表此 ADR 在 yfinance 無內部人申報資料, 而非真正零交易。日本上市公司內部人申報規則與美國不同, 不宜直接解讀為「無內部人動作」。
- 沒有可指名的 CEO/CFO 交易紀錄。

## Ownership shifts
- institutionsCount: 26
- institutionsPercentHeld: 0.229%
- insidersPercentHeld: 0.0%
- 機構持股比例 0.229% 明顯不合理 (Fanuc 為大型股, 機構持股通常遠高於此), 應判定為 ADR 資料口徑問題或 yfinance 欄位錯誤, 不可作為集中度或持股變化的依據。
- 機構持股趨勢: 無時間序列資料, 無法判斷是增持還是減持。

## Net sentiment score
Composite: **中性 (neutral)**, 信心 **低**。

依據:
- 分析師面: 偏多, 但樣本僅 2 位, 且近兩個月為 hold, 最新一筆為 buy/strong buy, 權重有限。
- 散戶面: 無資料, 無法納入計分。
- 內部人面: 無資料 (空陣列), 不列入計分。
- 機構面: 數據不可用。

Divergence flag: **無法判定** — 因缺少散戶資料, 無法確認散戶傾向是否與分析師傾向相反。

資料缺口與後續建議:
1. 允許 api.stocktwits.com 網域後重新抓取 StockTwits。
2. Reddit 來源需修正存取權限後重試, 或改用其他可存取的散戶情緒來源。
3. 取得 2026-10-22/23 財報後的評級與目標價變動 (yfinance 於本次未回傳目標價, 需另行確認)。
4. 以 FANUF (日本本地股) 或 ADR 比例換算核對機構持股與內部人資料。

SENTIMENT REPORT COMPLETE
