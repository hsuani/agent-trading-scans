# Sentiment — SPAI as of 2026-10-28

資料狀態總覽：Reddit（r/wallstreetbets、r/stocks）與 StockTwits 皆無法取得，標記為 DATA_UNAVAILABLE。分析師評級、內部人交易、股權結構來自 yf 工具（cache fallback）。散戶情緒僅有 WebSearch 的少量結果，品質低，可信度有限。

## Analyst consensus

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell |
|---|---|---|---|---|---|
| 0m（當期） | 0 | 3 | 0 | 0 | 0 |
| -1m | 0 | 3 | 0 | 0 | 0 |
| -2m | 0 | 3 | 0 | 0 | 0 |

目前 yf 共 3 buy / 0 hold / 0 sell。三個期間數字完全相同，yf 回傳中沒有可見的評級變動，也沒有目標價資料，因此「近期升降評」與「目標價變動」標記為 DATA_UNAVAILABLE。

交叉比對（非 yf，日期較早）：MarketBeat 2026-08-06 預覽列出 1 Strong Buy / 1 Buy / 1 Hold / 1 Sell，共識 "Moderate Buy"，平均目標價 $11.00。這與 yf 的 3 buy / 0 hold / 0 sell 不一致，可能是來源與統計口徑不同（時間點、分析師樣本不同），本報告不做調和，僅註記差異。

## Retail social

- Reddit：DATA_UNAVAILABLE。r/wallstreetbets 與 r/stocks 搜尋 SPAI 的 JSON 端點回傳 "Claude Code is unable to fetch from www.reddit.com"，無法取得貼文、分數、留言數與多空傾向。
- StockTwits / X：StockTwits 回傳 DNS 解析失敗（api.stocktwits.com 不在本次 session 允許網域內），DATA_UNAVAILABLE。需在 session 網路設定中允許該網域後才能重試。
- WebSearch（一次搜尋）：結果多為重複的 2026-04 頁面與聚合站模板，缺乏實質分析。可辨識的來源包括 Benzinga 情緒頁（最後更新 2026-10-08，列出 Buy 共識、3 位分析師、股價約 $4.39–$4.51）與 MarketBeat 2026-08-06 預覽。其中無可引用的散戶貼文或社群情緒量化數據。
- 聲量（buzz volume）：DATA_UNAVAILABLE。無法與歷史基準比較提及次數。
- 散戶傾向：DATA_UNAVAILABLE（無可靠樣本，不推定多空）。
- 主要主題：DATA_UNAVAILABLE。

## Insider activity

6 個月窗口（2026-04-28 至 2026-10-28）內的交易：

| 日期 | 內部人 | 職稱 | 類型 | 股數 | 金額（USD M） |
|---|---|---|---|---|---|
| 2026-09-09 | ERDBERG DANIYEL | Chief Executive Officer | 賣出 @ $4.00 | 1,000,000 | 4.0 |
| 2026-05-01 | MACK BRIAN WILLIAM | Officer | 股票獎勵（Grant） | 300,000 | 0（非現金） |

窗口外的參考交易（不計入 6mo 淨額）：COO MATHEWS JARRET DANIEL 2026-04-01 獎勵 20,000 股；CEO 2026-03-06 贈與 9,000 股；CEO 2025-12-23 贈與 24,000 股。

- 6mo 淨額：$0 買入 / $4.0M 賣出（僅一筆，即 CEO 於 2026-09-09 以 $4.00 賣出 1,000,000 股，ownership 為 D，直接持有）。
- 公開市場買入：無紀錄。
- 獎勵與贈與不計入現金買賣，僅列為背景。
- 單位換算核對：1,000,000 股 × $4.00 = $4,000,000 = $4.0M，與 yf 回傳 Value 4000000 一致。

## Ownership shifts

- 內部人持股比例：45.47%（yf insidersPercentHeld）。持股高度集中於內部人，流通股可能較小，此為結構性背景，非方向性訊號。
- 機構持股比例：12.06%（institutionsPercentHeld）；占流通股比例 22.13%（institutionsFloatPercentHeld）。
- 機構家數：31（institutionsCount）。
- 趨勢：yf 僅提供當期快照，無歷史季度比較，機構持股增減趨勢標記為 DATA_UNAVAILABLE。

## Net sentiment score

- 分析師面：偏多（yf 3 buy / 0 hold / 0 sell），但資料無近期變動、無目標價，且與較早來源的統計不一致，信心低。
- 內部人面：偏空（6mo 內 CEO 一筆 $4.0M 賣出，無公開市場買入），單筆樣本，信心低。
- 散戶面：DATA_UNAVAILABLE。
- 綜合：**中性（neutral），信心低**。分析師與內部人訊號方向相反，且散戶端無資料，無法形成可靠的多空判斷。

Divergence flag：**無法判定（DATA_UNAVAILABLE）**。散戶傾向缺失，無法確認是否與分析師傾向相反。若日後取得散戶資料，應重點比對：分析師偏多 vs. CEO 9 月賣出 + 散戶傾向。

## 來源與限制

- yf 工具：recommendations / rec_summary / insider / major_holders，cookie 與 crumb 取得失敗，改以 cache 回傳，數值可用但時效性未經驗證。
- WebSearch 結果：Benzinga 情緒頁（2026-10-08）、MarketBeat 預覽（2026-08-06）。另有一頁 Yahoo Finance 報價顯示 SPAI 約 $4.95，但無日期，未納入綜合判斷。
- 2026-10-28 之後的資料一律視為未知，未採用。

SENTIMENT REPORT COMPLETE
