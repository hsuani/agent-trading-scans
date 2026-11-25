# Sentiment — 3037.TW（欣興 Unimicron）as of 2026-11-26

資料時效註記：本報告以 2026-11-26 為基準日，但執行當日系統日期為 2026-11-25，部分來源（尤其是網路彙整頁）日期不一、可能過時。Reddit 與 StockTwits 無法連線，社群面資料缺口明顯。

## Analyst consensus

單位：分析師家數（人）。目標價單位：NT$（新台幣元／股）。

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 合計 |
|---|---|---|---|---|---|---|
| 當期（0m） | 5 | 12 | 1 | 0 | 0 | 18 |
| 前 1 個月（-1m） | 6 | 12 | 1 | 0 | 0 | 19 |
| 前 2 個月（-2m） | 6 | 12 | 1 | 0 | 0 | 19 |
| 前 3 個月（-3m） | 6 | 12 | 1 | 0 | 0 | 19 |

目前分布：17 買進（含 5 Strong Buy）/ 1 持有 / 0 賣出。

Recent moves：
- 近一個月 Strong Buy 由 6 降為 5，合計由 19 變 18，無 Buy 或 Hold 變動，推測為一家券商調降評等或停止覆蓋，無法從 yfinance 彙總確認具體券商。
- 網路彙整頁提及 Bernstein SocGen 與 Macquarie 於 10 月重申買進，目標價分別約 NT$1,400 與 NT$1,270（來源為第三方彙整頁，未交叉驗證）。
- 目標價範圍在不同彙整頁差異極大，約 NT$650 至 NT$1,700（17 家），平均約 NT$1,190 至 NT$1,240。低端 NT$650 的來源日期不明，宜視為陳舊資料。
- 網路彙整頁引用 Q3 2026 營收約 NT$52.65B（約 526.5 億）、稅後淨利約 NT$10.05B（約 100.5 億），屬第三方摘要，未對照 MOPS 公告；EPS 與股本未能取得，無法做 EPS × 股數的反推驗算。

## Retail social

- Reddit（r/wallstreetbets、r/stocks）：無法存取（WebFetch 回報 unable to fetch），本次無樣本。社群多空傾向：資料缺口，無法判定。
- StockTwits：api.stocktwits.com 無法解析（DNS 失敗，屬會話網路白名單限制），本次無樣本。需由使用者於會話網路設定允許此網域後再重試。
- X／新聞鏈：WebSearch 僅回傳彙整型頁面（investing.com、stockanalysis.com、quartr.com、trading-treff.de 等），沒有可辨識的散戶貼文。提及次數：無法量化，無法與常態基準比較。
- Themes（僅能從彙整頁與分析師面推得，非散戶原文）：
  - AI 伺服器與高階 ABF／載板需求成長帶動 Q3 獲利。
  - 股價波動劇烈：不同頁面報價差距大（約 NT$688 至 NT$1,185），技術指標頁顯示 RSI(14) 約 85，屬超買區，但同頁仍給出短期技術面買進評等。
  - 原始資料不一致：彙整頁的股價區間與目標價平均差異過大，需以 TWSE 即時報價與 MOPS 公告再核對。

## Insider activity

Net 6mo：資料缺口。yfinance `insider` 回傳空陣列，無法得知董監事、經理人的 6 個月買賣淨額。台股董監持股申報需以公開資訊觀測站（MOPS）內部人持股異動查詢補充，本次未取得。

Notable：無。

Ownership snapshot（單一時點，無趨勢資料）：
- 內部人持股 約 15.9%
- 機構法人持股 約 44.3%（流通股口徑約 52.7%）
- 機構法人家數 約 359 家

Ownership shifts：無歷史序列，無法判斷集中度趨勢。以目前數字看，機構持股比重偏高，屬於法人主導的籌碼結構。

## Net sentiment score

Composite：**偏多（bullish），信心低至中**。
- 分析師面：強烈偏多（17 買進 / 1 持有 / 0 賣出），近三個月無實質調降，權重最高。
- 散戶面：無資料，無法納入評分。
- 內部人面：無資料，無法納入評分。
- 信心受限於社群與內部人資料全數缺失，以及目標價與股價來源不一致。

Divergence flag：**無法判定（資料不足）**。分析師偏多，散戶傾向未知，因此不能確認兩者是否背離。待 Reddit、StockTwits 或 MOPS 內部人資料補齊後再重評。

Data gaps 清單：
1. Reddit（r/wallstreetbets、r/stocks）連線失敗。
2. StockTwits DNS 失敗，需會話網路白名單。
3. yfinance insider 空資料，需改查 MOPS。
4. 目標價與股價來源不一致，需 TWSE／MOPS 交叉驗證。

Sources（WebSearch 彙整，時效不一）：
- https://quartr.com/events/unimicron-technology-corp-3037-q3-2026_F9DCOXs6
- https://stockanalysis.com/quote/tpe/3037/forecast/
- https://www.investing.com/equities/unimicron-tech-consensus-estimates
- https://trading-treff.de/wirtschaft/unimicron-aktie-das-kurslimit-war-noch-nicht-der-boden
- https://simplywall.st/ko/stocks/tw/tech/twse-3037/unimicron-technology-shares/future

SENTIMENT REPORT COMPLETE
