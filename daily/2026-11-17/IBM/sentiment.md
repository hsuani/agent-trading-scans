# Sentiment — IBM as of 2026-11-17

資料說明：Reddit、StockTwits 兩個來源本次皆無法取得（Reddit 連線被拒；api.stocktwits.com 在本 session 網路白名單外無法解析）。X / 新聞部分只有一筆無日期的彙整頁面，可信度低。因此本報告的散戶情緒部分為「資料不足」，綜合評分主要依據分析師與內部人資料。

## Analyst consensus

25 家分析師：12 buy（3 strong buy + 9 buy）/ 11 hold / 2 sell（1 sell + 1 strong sell）。

| 期間 | strong buy | buy | hold | sell | strong sell | 合計 |
|---|---|---|---|---|---|---|
| -3m | 3 | 10 | 10 | 1 | 1 | 25 |
| -2m | 3 | 9 | 10 | 1 | 1 | 24 |
| -1m | 3 | 9 | 11 | 1 | 1 | 25 |
| 目前 (0m) | 3 | 9 | 11 | 1 | 1 | 25 |

近期變化：3 個月內 buy 評等由 10 家降為 9 家，hold 由 10 家增為 11 家，strong buy 與 sell 家數未變。整體偏向為「多數持有、略偏正面」，正面評等占比由約 48% 小幅收斂。工具未提供個別券商的升降評等名稱與目標價調整明細，因此無法確認是哪家券商調整，也無法判斷目標價方向。

## Retail social

- Reddit（r/wallstreetbets、r/stocks）：本次無法存取，無法取得討論量、熱門帖或語氣。
- StockTwits / X：StockTwits 無法連線。X 與新聞搜尋只找到一筆無日期的彙整頁，內容為歷史與近期意見混雜，多處引用 2006、2015、2018 年的數據，無法當作當期散戶情緒。
- 粗略語氣：彙整頁中有人把 IBM 視為低本益比、高股息的價值股；也有人認為營收成長停滯、EPS 主要靠買回股票撐起。整體屬「混合」，但樣本不具代表性。
- 討論量：無法與常態比較，記為未知。
- 主要主題（依彙整頁，非即時散戶貼文）：價值 / 股息、軟體與雲端是否轉強、自家股票買回對 EPS 的貢獻、成長是否可持續。
- 價格脈絡：彙整頁引用 2026-11-10 股價約 244.53 USD，屬於區間偏高段。

## Insider activity

分析窗口：2026-05-17 至 2026-11-17（近 6 個月）。金額單位為 USD。

| 日期 | 姓名 | 職稱 | 交易 | 股數 | 金額 (M USD) |
|---|---|---|---|---|---|
| 2026-08-26 | THOMAS ROBERT DAVID | Officer | 賣出，每股 230.32 | 25,000 | 5.76 |
| 2026-07-01 | ROBINSON ANNE | Officer | 性質未標示（金額空白） | 7,295 | 不明 |
| 2026-06-04 | FEHRING NICOLAS A. | Officer | 贈與 | 400 | 0 |

Net 6mo：公開市場買入 0 M USD，賣出約 5.76 M USD（均為 Officer THOMAS ROBERT DAVID）。另有一筆 7,295 股 ROBINSON ANNE 交易性質不明，可能為稅款代扣或其他非交易性質，無法計入淨額。

Notable：
- CEO KRISHNA ARVIND 與 CFO KAVANAUGH JAMES J. 在窗口內無公開市場交易，主要為 2026-01-30 與 2026-02 的股票授予（Grant），非買賣。
- 上一次公開市場買入為 2026-02-25 董事 MIEBACH MICHAEL（約 0.10 M USD）與 HOWARD MICHELLE J.（約 0.01 M USD），皆在窗口之外。
- 2026-01-30 董事 FARR DAVID N 買入 1,000 股，約 0.30 M USD，在窗口之外。
- 窗口內唯一實質賣出來自非 CEO / CFO 的 Officer，金額約 5.76 M USD。

## Ownership shifts

- 機構持股比例約 64.85%（機構數 4,301）。
- 內部人持股約 0.28%。
- 工具只給單一時點快照，無法判斷機構集中度的趨勢方向。

## Net sentiment score

綜合：**中性偏謹慎（neutral，信心低）**

- 分析師面：偏中性偏正面。12 buy / 11 hold / 2 sell，但 buy 家數近 3 個月微降。
- 內部人面：偏負面（信心中）。窗口內無公開市場買入，唯一實質交易為 Officer 賣出約 5.76 M USD；CEO / CFO 無動作。注意：賣出金額占內部人持股比例未能計算，解讀需保守。
- 散戶面：無資料，不納入評分。
- 信心低的主因是散戶來源全數無法取得，且內部人資料的 6 個月窗口只有一筆實質交易。

Divergence flag: **無法判定**。因散戶情緒缺資料，無法確認散戶與分析師方向是否相反。若後續取得 Reddit 或 StockTwits 資料，需重新評估。

資料缺口與待補項目：
1. Reddit 與 StockTwits 需在 session 網路設定中允許存取後重抓。
2. 分析師個別升降評等與目標價明細，工具 `recommendations` 本次回傳內容與 `rec_summary` 相同，未含逐筆事件。
3. ROBINSON ANNE 2026-07-01 交易性質需確認。

SENTIMENT REPORT COMPLETE
