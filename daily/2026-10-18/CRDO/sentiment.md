# Sentiment — CRDO as of 2026-10-18

資料狀態：分析師與內部人資料可用（部分為快取，見各節）。散戶社群（Reddit / StockTwits / X）本期資料 DATA_UNAVAILABLE，未取得 2026-10 當期貼文。

## Analyst consensus
目前 rec_summary：5 Strong Buy / 14 Buy / 1 Hold / 0 Sell / 0 Strong Sell（共 20 家）。近四個月結構穩定，僅 Strong Buy 由 4 家增至 5 家（最近一個月）。
- 外部第三方來源（Benzinga，2026-09-04 快照）為 16 家：15 Buy / 1 Hold，平均目標價 $216，當時收盤 $170.57，隱含上行約 27%。兩來源家數不同，原因未確認（可能是覆蓋範圍或快照時點不同）。
- 近期調整（Benzinga，2026-09-02）：JP Morgan 目標價由 $335 降至 $310（維持 Overweight）；Evercore ISI 由 $325 降至 $292（維持 Outperform）。
- 夏季調升：Barclays 2026-07-20 由 $260 升至 $300；Susquehanna 2026-07-21 由 $235 升至 $250。
- 早期 2026 調降（以 Benzinga 等轉載為準）：Susquehanna 3 月由 $230 降至 $170；BofA 由 $200 降至 $160，BofA 理由為產業估值倍數壓縮，非公司基本面惡化。
- 10 月內個別券商的評等或目標價變動：DATA_UNAVAILABLE（yf 的 recommendations 欄位與 rec_summary 相同，只有彙總計數，無逐家評等歷史）。
- 注意：`yf.py CRDO ratings` 不是有效子命令，本次改用 rec_summary 與 recommendations。

## Price context（供解讀用，來源 prices/yf/CRDO.json 快取）
- 2026-10-09 收盤 $216.55，2026-10-16 收盤 $169.70，五個交易日約下跌 21.6%。
- 10-12 至 10-16 的下跌伴隨成交量放大（10-14 成交量 12.5M 股，為區段高點）。

## Retail social
- Reddit：DATA_UNAVAILABLE。WebSearch 對 r/wallstreetbets 與 r/stocks 的 CRDO 查詢未回傳 2026-10 的貼文；直接 WebFetch 依指示未使用。
- 過期的零星訊號（非本期，不計入綜合評分）：
  - 一篇 Yahoo Finance 價格預測文章提到，Reddit 情緒約於 2026-04-22 轉為非常看多，時點對應股價當時的一段上漲。
  - 一篇 StockTwits 轉載文章（日期不明，推測為 2026 年 6 月前後）稱散戶情緒由 neutral 轉為 "extremely bullish"，文中有交易者認為股價「priced for perfection」，估值已高。
- StockTwits 直接 API：DATA_UNAVAILABLE（本期未取得訊息流與情緒比例）。
- X / 新聞討論：WebSearch 僅找到 2026-06 前後的選擇權流量與情緒估計網站（historicaloptiondata.com 等），其提供的「60%–72% 看多」為第三方估計，來源未驗證，不採用。2026-10 的 X 貼文量：DATA_UNAVAILABLE。
- 聲量（buzz volume）：無法與基準比較，DATA_UNAVAILABLE。
- 主要主題（僅就 2026 年 6 月前後的零星來源歸納，供參考）：高估值與本益比（trailing P/E 約 98 的說法來自第三方頁面）、客戶集中度風險（2025 年 3 月單一超大規模客戶佔 Q3 營收約 86%）、毛利率壓縮（約 64–66%）、內部人持續賣出。
- 散戶傾向：DATA_UNAVAILABLE（無當期樣本，不推論）。

## Insider activity
資料來源：yf insider（150 筆，覆蓋 2025-04 至 2026-10-13）。
- 近 6 個月（2026-04-18 至 2026-10-18）：公開市場買入 $0；賣出約 $205.7M（有金額之交易）。另有若干 2026-06-30 的 CEO/CFO 交易金額欄位為空白，未計入。
- 依人統計（6 個月賣出金額）：
  - CHENG CHI FUNG（CTO）：約 $104.3M，19 筆。多為每週或每兩週一次、約 27,500 股的重複性出售，價格區間約 $164–$281。
  - LAM YAT TUNG（COO）：約 $67.0M，4 筆（含 2026-09-25 的 10 萬股出售與 17.5 萬股贈與）。
  - BRENNAN WILLIAM JOSEPH III（CEO）：約 $14.6M，2 筆（另有贈與）。
  - FLEMING DANIEL W（CFO）：約 $13.5M，3 筆。
  - LAUFMAN JAMES L（Officer）：約 $4.4M，4 筆，每次約 5,000 股。
  - 董事（HOSEIN、ACEVEDO、SUTARDJA、DANESH）：合計約 $2M，屬小額。
- 最近動向：2026-10-13 CTO 於 $186.11–$201.84 出售 31,290 股（約 $6.1M）；10-12 董事 SUTARDJA 於 $212.22 出售；10-08 CFO 於 $211.28–$215.08 出售 7,580 股。
- 重要說明：多數出售呈重複性模式（相似股數、定期），可能屬預先設定的交易計畫（如 10b5-1），但本資料來源未標示計畫狀態，無法確認，標為未驗證。
- 10 月 13 日至 10 月 16 日股價下跌期間，仍有內部人出售，未見逢低買入。
- 內部人持股比例（major_holders）：約 9.1%。

## Ownership shifts（機構持股）
- 機構持股比例約 73.9%（float 口徑約 81.3%），機構數 1,321 家（yf major_holders）。
- 前十大持有人（資料日期 2026-06-30，距今約 3.5 個月，屬過期資料）：
  - BlackRock：9.45%，股數 QoQ 減少 10.4%
  - Vanguard Portfolio Management：4.37%，減少 8.6%
  - Vanguard Capital Management：3.96%，增加 2.8%
  - Point72：3.27%，減少 17.7%
  - State Street：2.25%，減少 13.4%
  - Geode：1.72%，減少 26.3%
  - T. Rowe Price：1.42%，增加 91.8%
  - Jennison Associates：1.41%，增加 974.6%
  - SRS Investment Management：1.37%，增加 2.7%
  - Bank of America：1.16%，增加 13.7%
- 解讀：指數型與部分對沖型持有人減碼，主動型基金（T. Rowe、Jennison）加碼。前十大合計約 35%，集中度中等偏高。此為 Q2 資料，無法反映 Q3 以後的調整；Q3 13F 資料：DATA_UNAVAILABLE。

## Net sentiment score
綜合：中性（信心低）。
- 分析師面：偏多（5 Strong Buy + 14 Buy，0 Sell），且 Benzinga 平均目標價高於當前價格約 27%（以 9 月快照計）。權重高，但目標價在 2026 年多次大幅上下修，分析師觀點的時效性有限。
- 內部人面：偏空。6 個月約 $206M 賣出、無公開市場買入，且近期在股價下跌時仍有出售。出售多屬重複模式，偏空強度應打折。
- 價格動能：偏弱。10 月五日內約 -21.6%。
- 散戶面：DATA_UNAVAILABLE，不納入評分。
- 信心：低。主要原因是當期散戶資料缺失，且機構與分析師資料有時點落差。

Divergence flag：無法判定。散戶傾向資料缺失，無法與分析師傾向比對。分析師偏多與內部人淨賣出方向相反，這一點值得留意，但兩者的解讀都有限制（見上）。

## 資料缺口與限制
- Reddit、StockTwits 直接 API、X 的 2026-10 當期貼文：DATA_UNAVAILABLE。
- 逐家分析師評等歷史與 10 月內的升降評：DATA_UNAVAILABLE。
- 13F Q3 2026 持股：DATA_UNAVAILABLE（現有為 Q2）。
- WebSearch 所得的第三方情緒百分比與選擇權流量網站，來源未驗證，未採用。

SENTIMENT REPORT COMPLETE
