# Sentiment — NBIS (Nebius Group) as of 2026-11-23

資料品質警示：本次 Yahoo 即時呼叫 (recommendations / rec_summary / insider / inst_holders) 因 cookie/crumb 連線失敗，改讀 repo 快取，_refreshed_at 未確認時效。Reddit 與 StockTwits 無法連線，散戶面僅能靠二手 WebSearch 摘要，信心偏低。

## Analyst consensus

截至 2026-11-23 (yf rec_summary，0m)：22 位分析師，Strong Buy 3 / Buy 13 / Hold 5 / Sell 1 / Strong Sell 0。Buy 合計 16 位，佔 73%；Hold 23%；Sell 5%。

趨勢 (yf recommendations，逐月計數)：
- 3 個月前 (-3m)：18 位，Buy 11 位 (61%)，Hold 6，Sell 1，Strong Sell 1。
- 2 個月前 (-2m)：19 位，Buy 14 位 (74%)，Hold 5，Sell 2。
- 1 個月前 (-1m)：22 位，Buy 15 位 (68%)，Hold 6，Sell 1。
- 本月 (0m)：Buy 16 位 (73%)，Hold 5，Sell 1。

近期評級與目標價動向：
- yf 只回傳計數，沒有逐家評級異動清單，也沒有目標價欄位，因此無法列出個別升降評等。
- WebSearch 摘要指 Citi 維持 Buy，目標價由 $265 降至 $215。此為二手摘要，未對應到原始連結。
- 同一摘要指 11/13 股價重挫後，至少 7 家分析師下調目標價。
- 估值爭議：一則來源稱 P/S 約 61.4 倍，高於產業平均；另一則 Motley Fool 文章則認為約 3 倍營收、已趨吸引。

評論：評級計數偏多且 3 個月內 Buy 比例上升，但股價在 11/13 後重挫，目標價下修與評級計數的方向不一致。yf 的 cookie/crumb 取得失敗，無法確認資料為即時或 repo 快取，請上游留意資料時效。

## Retail social

- Reddit：r/wallstreetbets 與 r/stocks 的 WebFetch 皆被拒絕 (無法連線)，本次無法取得貼文樣本與情緒分數。soft-fail，未取得資料。
- StockTwits：api.stocktwits.com 無法解析 (DNS 失敗)，依規定不再重試。若需此來源，需由使用者在 session 網路設定中允許該網域。
- X / 新聞 (WebSearch，二手摘要)：一則 StockTwits 相關報導形容散戶情緒「極度看多」，且訊息量很高，但該摘要未標註確切日期，且無量化基準，無法換算為提及數的倍數。
- 股價脈絡 (可對應連結)：
  - 股價連續第 6 週收跌，分析師點出資料中心與產能啟用延遲 ([StockTwits 報導](https://stocktwits.com/news-articles/markets/equity/nbis-stock-on-track-for-6th-straight-weekly-loss-analysts-flag-data-center-capacity-activation-delays/cNbRd9dR9f0))。
  - 11/13 股價單日重挫約 15%，Motley Fool 有專文報導 ([Fool](https://fool.com/investing/2026/11/13/why-nebius-group-stock-plunged-again-today))。
  - 52 週高點 $299.86 (6/22)，目前距高點回落約 64%，此數字來自 Barchart 摘要，為二手資料。
  - 股價回撤後，「散戶逢低買」敘事與 CoreWeave 連動的聲量仍存在 ([StockTwits](https://stocktwits.com/news-articles/markets/equity/nbis-retreats-after-core-weave-rally-ahead-of-q3-report-analyst-says-market-can-t-squeeze-out-top-players-amid-record-cloud-demand/cNGzYP9R99x))。
- 散戶傾向 (依可得資料判斷)：二手來源偏多，與股價下跌背離，整體評為「混合偏多、信心低」。
- 主要主題：
  1. 與 CoreWeave 連動，被視為 AI 雲端需求的代理標的。
  2. 融資與負債壓力。9/30 負債約 $14.2B，融資需求被視為最大風險。
  3. 估值之爭，P/S 約 61 倍與約 3 倍營收兩種說法並存。
  4. 產能啟用延遲與資本支出。
  5. 股權稀釋疑慮。
  6. 2026 年初 r/wallstreetbets 曾以 ClickHouse 股權 (約 $15B 估值) 作為多頭論點 ([247WallSt 歷史報導](https://247wallst.com/investing/2026/03/10/reddit-fell-in-love-with-nebius-then-panic-sold-the-wrong-miss/))，歷史上 Reddit 情緒曾在看空與看多之間快速切換。

## Insider activity

視窗：2026-05-23 至 2026-11-23。金額單位為 USD，以 M (百萬美元) 表示。

淨額：買入約 $0.26M；賣出約 $197M；**淨賣出約 $197M**。

- 買入僅有董事 ARNE GRIMME 於 10 月的 4 筆小額買進，合計 1,570 股、約 $0.26M。
- 賣出約 $197M，共約 23 筆。其中：
  - COO OPHIR NAVE 於 10/05 以 $231–243.5 賣出 500,000 股，約 $117.8M，為單筆最大。
  - 董事 CHARLES RYAN 於 8/14 賣出 50,000 股，約 $13.3M。
  - CEO ARKADY VOLOZH 於 7/01 賣出 46,627 股 (約 $11.0M)，10/01 再賣 37,778 股 (約 $8.8M，成交價 $234.16)。
  - CTO DANILA SHTAN、執行官 ANDREY KOROLENKO 等人於 6–10 月有多筆 $3–8M 的賣出。
  - 董事 JOHN BOYNTON 於 6–11 月多次賣出，單次約 $0.06–1.5M。
  - CFO MARIA ALONSO SANCHEZ 賣出規模較小，約 $0.09M 與 $0.42M。
- 同日同價的多人賣出 (10/01 三人同以 $234.16 出售) 可能屬計畫性或分批執行，需對照 Form 4 確認是否為 10b5-1 計畫。
- 計算排除項目：
  - 6/15 BOYNTON 的 $1.47M 交易在資料中重複出現兩次，只計一次。
  - 11/11、10/12、9/14 的衍生品行權 (期權轉股) 與 $0 或空值列，未計入 (配對之賣出已計入)。
  - 7/22 ALMOG 與 9/01 董事/執行長等人之股票獎勵 (grant) 未計入。
  - 5/13 KOROLENKO 的 500,000 股賣出 (約 $101.6M) 落在視窗之前，未計入。
- 驗算：VOLOZH 37,778 股 × $234.16 ≈ $8.85M，與資料值 $8.846M 相符。
- 解讀：淨賣出規模大，但主要來自高層的行權後出售，且股價在 $230–300 區間出售較多。11 月股價下跌後，仍有 11/11 與 11/13 的賣出。內部人淨賣出與分析師偏多形成明顯對照。

## Ownership shifts

- 內部人持股 3.12%。
- 機構持股 61.9% (流通股 63.9%)，機構數 1,489 家。
- 前十大持股合計約 36.0%。9/30 (13F) 資料顯示：
  - Luminarx Capital 持股 7.52% (16.5M 股)，季增 100%。
  - BlackRock 持股 5.83%，季增約 0.1%。
  - GQG Partners 持股 5.00%，季增 100%。
  - Invesco 持股 3.47%，季增約 10%。
  - Fred Alger 持股 2.92%，季增約 12%。
  - Morgan Stanley 持股 2.05%，季增約 20%。
  - State Street 持股 2.01%，季增約 8%。
  - Orbis Allan Gray 持股 2.62%，季減約 11%。
  - UBS 持股 2.31%，季減約 3%。
  - Goldman Sachs 持股 2.31%，季減約 48%。
- 趨勢：前十大中多數為增持，但 Goldman 大幅減碼，且 Orbis 與 UBS 小幅減持。整體偏向機構加碼。資料為 9/30 的 13F，已有一季以上的時間落差，不代表 11 月的部位。

## Net sentiment score

- 分析師面：偏多。Buy 佔 73%，3 個月內 Buy 比例上升，但目標價在 11 月已有下修。
- 內部人面：偏空。6 個月淨賣出約 $197M，以高層大額賣出為主，僅有一筆小額董事買進。
- 散戶面：資料不足。Reddit 與 StockTwits 皆不可得，僅有二手 WebSearch 摘要，描述偏多，但與股價走勢背離。
- 綜合：中性 (信心低至中)。分析師偏多與內部人淨賣出相互抵消，散戶面資料缺口大。

Divergence flag：**是**。
- 內部人 vs 分析師：內部人淨賣出與分析師 73% Buy 方向相反，這是值得注意的訊號。
- 散戶 vs 分析師：二手摘要顯示散戶偏多，與分析師方向一致，因此不是相反。但散戶敘事與股價走勢背離，此項無法以原始 Reddit/StockTwits 資料確認。

資料限制摘要：
1. Reddit 與 StockTwits 不可得 (soft-fail)。
2. yf cookie/crumb 失敗，資料時效未確認。
3. 目標價與逐家評級異動無法由 yf 取得。
4. 機構持股為 9/30 的 13F 資料。

SENTIMENT REPORT COMPLETE
