# Sentiment — 3363.TWO (上詮) as of 2026-11-01

資料時效註記：報告日為 2026-11-01，但執行日為 2026-10-31。網路來源最新可見資料約停在 2026-09 中，10 月的散戶討論與股價皆未取得，以下結論以較早期資料為主。

## Analyst consensus

目前 3 位分析師：1 strongBuy / 1 buy / 1 hold，即 **2 buy / 1 hold / 0 sell**（Yahoo rec_summary，覆蓋極少，樣本不足以代表市場共識）。

| 期間 | strongBuy | buy | hold | sell | strongSell | 合計 |
|---|---|---|---|---|---|---|
| 0m（目前） | 1 | 1 | 1 | 0 | 0 | 3 |
| -1m | 2 | 1 | 0 | 0 | 0 | 3 |
| -2m | 1 | 1 | 0 | 0 | 0 | 2 |
| -3m | 1 | 1 | 0 | 0 | 0 | 2 |

Recent moves: 目前一位原本 strongBuy 的評等變為 hold（由 -1m 的 2 strongBuy 降為 1 strongBuy，hold 由 0 增為 1），推定為一次降評；總家數由 3 維持 3。目標價調整資料工具未提供，無法判定。

## Retail social

- Reddit（r/wallstreetbets、r/stocks）：**無法取得**。WebFetch 無法連線至 reddit.com，未能取樣貼文與語氣。
- StockTwits：**無法取得**。api.stocktwits.com 解析失敗（DNS ENOTFOUND），需於 session 網路設定中放行後才能重試。
- PTT 股板：搜尋僅能看到標題級資訊，例如「[情報] 3363上詮 8月營收」，未能讀取內文與散戶語氣，無法判定 10 月的討論方向。
- 新聞與題材端（非散戶直接發言）：
  - 2026-09-07 有《通網股》報導「上詮 FAU 放量、Q4 營運看俏」，屬正向題材敘事。
  - 2026-09-11 同來源報導近 5 日跌 7.75%，短線情緒偏弱。
  - 2025 年 8 月曾因 CPO 題材盤中漲停並有外資買盤，屬舊題材，不代表目前看法。
- 聲量：無法量化與常態比較；就搜尋結果數量判斷，近期討論可見度中等偏低，屬小型櫃買股的常見狀態。
- Themes（自來源可見的重複主題）：CPO / 光通訊題材、FAU 產能與 Q4 營運展望、月營收年增轉正（8 月年增 13.2%，但年初至今營收仍負成長）、基本面虧損與估值偏高。
- Retail tilt: **無法判定（資料缺口）**。

## Insider activity

Net 6mo: 資料缺口。yf insider 回傳空陣列，無法區分「無交易」與「資料未涵蓋」。台灣董監事持股異動依規定於公開資訊觀測站揭露，本次未查核，不宜視為零交易。

Notable: 無可列出之個人交易。

## Ownership shifts

- 內部人持股比例（insidersPercentHeld）：26.4%，屬高度集中。
- 機構持股比例（institutionsPercentHeld）：11.3%；占浮動股比（institutionsFloatPercentHeld）：15.4%。
- 機構家數：33。
- 趨勢：單一時點快照，無歷史序列，無法判定增減方向。
- 外資與法人買賣超：未於本次工具取得，僅有 2025 年底櫃買注意股公告中提及外資於前五日為淨買方的舊資料。

## Net sentiment score

Composite: **中性（neutral），信心低**。

- 分析師面：偏正向但樣本極少（3 家），且近期出現一次降評至 hold，信號薄弱。
- 散戶面：無法取得 Reddit、StockTwits 與 PTT 內文，無有效樣本。
- 新聞與基本面面：題材敘事（FAU、CPO、Q4 展望）偏正向，但獲利仍為虧損（2026 上半年 EPS 約 -1.18，據新聞），年初至今營收負成長，估值與櫃買注意股紀錄偏負面。
- 內部人面：資料缺口，不納入評分。

Divergence flag: **無法判定**。散戶語氣未取得，無法與分析師傾向比較。若日後取得散戶資料，分析師偏多（2 buy）與散戶若明顯偏空，即屬背離，值得留意。

## 資料來源與缺口

| 來源 | 狀態 |
|---|---|
| yf recommendations / rec_summary | 成功（Yahoo cookie 失敗但仍回傳資料） |
| yf insider | 空陣列，視為資料缺口 |
| yf major_holders | 成功 |
| Reddit r/wallstreetbets、r/stocks | 失敗（WebFetch 無法連線） |
| StockTwits | 失敗（DNS 解析失敗，需 session 放行 api.stocktwits.com） |
| WebSearch（英文、中文） | 部分成功，多為新聞與股價頁，價格數字彼此不一致，僅作方向參考 |

建議後續：放行 api.stocktwits.com 後重試；於 PTT 股板人工查核 10 月「上詮」或「3363」討論；於公開資訊觀測站查核董監事持股異動與 10 月月營收。

SENTIMENT REPORT COMPLETE
