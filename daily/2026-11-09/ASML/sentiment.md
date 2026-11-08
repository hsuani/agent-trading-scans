# Sentiment — ASML as of 2026-11-09

資料說明：yf 工具的 live 連線失敗，改用 repo 快取（source: cache）。社群資料以 WebSearch 取代直連 Reddit / StockTwits。最新可查到的新聞與社群快照多停在 2026-11-05 前後，距離 as-of 日期有數日落差。

## Analyst consensus

yf `rec_summary` / `recommendations`（0m 快照）：Strong Buy 7 / Buy 31 / Hold 2 / Sell 1 / Strong Sell 0，共 41 家，約 93% 為買進以上評等。

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell |
|---|---|---|---|---|---|
| 0m（目前） | 7 | 31 | 2 | 1 | 0 |
| -1m | 7 | 31 | 2 | 1 | 0 |
| -2m | 7 | 31 | 3 | 1 | 0 |
| -3m | 6 | 32 | 4 | 1 | 0 |

近期變化：過去三個月 Hold 由 4 家降至 2 家，Strong Buy 由 6 家升至 7 家，評等整體小幅往買進方向移動。yf 的 `recommendations` 只回傳上述彙總表，沒有逐筆升評、降評紀錄，因此無法列出個別券商動作。目標價變動在本次資料中也無法取得。

資料衝突：WebSearch 抓到的 MarketBeat 彙總頁顯示 3 Strong Buy / 17 Buy / 2 Hold / 3 Sell，與 yf 的分布不一致。本報告以 yf 為準，但兩者的分析師家數與計算口徑不同，數字不可直接混用。

## Retail social

- Reddit：本次無法取得 r/wallstreetbets 或 r/stocks 中 2026-11 月的 ASML 討論串。WebSearch 只找到幾則 2026 年 4 月與 6 月的 Reddit 快照（來源為第三方鏡像站，可靠度有限），內容偏向長期 AI 需求與地緣政治風險的辯論，並非近期情緒數據。因此 Reddit 的傾向無法判定，只能標記為「資料不足」。
- StockTwits / X：WebSearch 找到的 StockTwits 新聞摘要指出，ASML 在 11 月初的拋售期間，散戶情緒仍維持「bullish」，部分摘要提到情緒由 bullish 升至 extremely bullish，但摘要本身沒有註明確切日期。另一則摘要提到 ASML 美股連續六個交易日中有五日下跌，散戶仍多數認為拋售過度。引述樣本（≤15 字）：「dismiss selloff」（StockTwits 標題語意）。
- 聲量：無法量化提及次數。從搜尋結果看，11 月初的 ASML 話題量高於平常，但僅為定性判斷。
- 主要主題：
  1. 中國技術進展：DUV 國產化消息被視為短期威脅，散戶多認為中國需要數年才能追上 EUV 技術。
  2. 拋售是否過度：BofA 在 7 月即表示下跌是過度反應，散戶多數引用此觀點。
  3. 供需與 AI 需求：CEO 表示供給「無法完全滿足需求」，被視為長期多頭論點。
  4. 美國中期選舉與資料中心支出：拋售期間的主要敘事，擔心民主黨勝選後資料中心支出放緩，但 ASML 本身並無公司特定利空消息。

## Insider activity

yf `insider` 回傳空陣列，無法判定 6 個月內的淨買賣金額與人員職稱。這不等於「沒有內部人交易」，只代表資料源未提供。Insider 持股比例約 0.008%（yf `major_holders`），內部人持股比例極低，對內部人情緒的參考價值有限。

Net 6mo：資料不足（無 buys / sells 紀錄）。Notable：無。

## Ownership shifts

- 機構持股比例：約 20.36%，機構數量 3,002 家（yf `major_holders` 快照）。
- 只有單一時點快照，無法判斷機構集中度趨勢。
- 內部人持股約 0.008%。

## Net sentiment score

Composite：**bullish（信心：中）**

- 分析師面：高度偏多（約 93% 買進以上，過去三個月 Hold 減少）。
- 散戶面：StockTwits 摘要偏多，Reddit 無法判定，信心受限於資料日期不明確。
- 價格面：11 月初連續下跌，屬於情緒與價格背離的短期現象，但本報告不涉及交易建議。

Divergence flag：**no**。散戶與分析師傾向均偏多，無明顯反向背離。需注意的是，短期價格走弱與多方情緒並存，這種「情緒偏多但價格走弱」的組合本身值得留意，但不構成 divergence flag 的定義範圍。

SENTIMENT REPORT COMPLETE
