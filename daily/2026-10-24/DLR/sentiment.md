# Sentiment — DLR (Digital Realty Trust) as of 2026-10-24

資料時點說明：分析師評級數據來自 yf 工具（as-of 系統當日）；價格與部分目標價來自 2026-10-05 至 2026-10-09 的公開資料；社群資料多為 2026-08-09 的第三方快照。Reddit 直接抓取被封鎖，StockTwits 依規定未抓取（金融網站），X 無可用的當期貼文。以下各項若為缺漏皆標示 DATA_UNAVAILABLE。

## Analyst consensus

目前 35 位分析師（yf rec_summary，0m）：Strong Buy 5 / Buy 25 / Hold 5 / Sell 0 / Strong Sell 0。即買進方（含 Strong Buy）30 家，佔 85.7%；持有 5 家，佔 14.3%；賣出 0 家。

- 共識分數（1 = Strong Sell，5 = Strong Buy，加權平均）：**4.00 / 5**，屬偏多。
- 近三個月趨勢：買進方由 -3m 的 26 家增至 0m 的 30 家；持有方由 7 家降至 5 家；覆蓋家數由 33 增至 35。未見任何降評（sell 始終為 0）。
- 目標價：第三方彙整約 $222.74（early Oct，覆蓋家數來源不一，約 24–33 家）；Benzinga 8 月平均目標約 $210。
- 近期個別動作（網路公開資料，未逐筆核實）：Evercore ISI 8 月將目標上調至 $240；BMO 10/5 維持 Buy，目標 $225；Barclays 為主要 Hold，目標 $197。
- 評級來源差異：WebSearch 彙整站顯示 22 Buy / 4 Hold / 0 Sell（26 家），與 yf 的 35 家口徑不同，本報告以 yf 為主。
- 價格參考：10/9 收盤 $178.76，較 10/6 的 $184.65 下跌；52 週高點 $208.14。目標價隱含上行空間約 20–25%（以 $222.74 對 $178.76 計約 24.6%）。

## Retail social

- Reddit：DATA_UNAVAILABLE。r/wallstreetbets 與 r/stocks 的 JSON 搜尋皆回傳存取錯誤（無法抓取 www.reddit.com），無法取得貼文樣本、分數與留言數。WebSearch 亦未找到 2026 年的 DLR 相關討論串。
- StockTwits：DATA_UNAVAILABLE。依任務規定不對金融網站使用 WebFetch，未取得。
- X / 新聞輿情：無當期（10 月）可用資料。SentiSense 30 日情緒分數 7.45（偏多，趨勢回升），統計日期為 2026-08-09，提及量約 12 則/日；其中新聞來源約 77% 偏多，Reddit 與 X 各佔小比例且皆偏多。此為約兩個月前的快照，不代表 10 月狀況。
- 聲量（buzz volume）：以 8 月快照推估約 12 則/日，屬低至中等水準；與 DLR 歷史基準的比較 DATA_UNAVAILABLE。
- 散戶傾向：8 月快照偏多（bullish）；10 月 DATA_UNAVAILABLE。
- 主題（依 8 月第三方摘要與公開評論）：多頭側重產業龍頭地位與資料中心／AI 需求成長；空頭側重估值偏高（TipRanks 的 bear case 指估值偏貴）。另有 10 月股價回落至 $178–185 區間，為近期市場焦點之一。

## Insider activity

6 個月窗口（2026-04-24 至 2026-10-24），yf insider 資料：

| 日期 | 人員 | 職稱 | 交易 | 股數 | 金額（USD） |
|---|---|---|---|---|---|
| 2026-08-27 | PATTERSON MARK R | Director | 賣出 @ $193.96 | 200 | $0.039M |
| 2026-05-29 | MANDEVILLE JEAN F H P | Director | 股票獎勵（非公開市場買入） | 1,289 | $0（獎勵） |

- 淨買入（公開市場）：$0.00M
- 淨賣出：$0.039M（1 筆，董事）
- 合計：買方 0 筆、賣方 1 筆（公開市場），獎勵 1 筆（不計入情緒）
- 注意：yf 未回傳 2026-04 至 2026-10 期間的 CEO 或 CFO 交易紀錄。
- 背景（窗口外）：CEO ANDREW P. POWER 於 2025-09-15 賣出 58,000 股，成交價約 $175.10–175.16，金額約 $10.16M；CFO MATT MERCIER 於 2024-12-12 賣出 2,518 股，約 $0.47M；兩者均在 6 個月窗口之外，僅作參考。
- 解讀：窗口內未見高階主管公開市場買入，唯一賣出為小額董事減持；屬中性偏弱的內部人訊號，但金額與樣本都小。

## Ownership shifts

- 機構持股比例（institutionsPercentHeld）：yf 回傳 1.04959，換算為 104.96%，超過 100%，屬資料異常，不採用。
- 機構家數（institutionsCount）：1,841。
- 內部人持股比例（insidersPercentHeld）：0.014%（yf 回傳 0.00014）。
- 機構持股趨勢（多期比較）：DATA_UNAVAILABLE（yf 僅提供單期快照，無歷史序列）。
- 大股東集中度：無可靠數據，DATA_UNAVAILABLE。

## Net sentiment score

綜合判斷：**偏多（bullish），信心中低**。

- 分析師面：偏多且趨勢正向（買進方 85.7%，共識分數 4.00，過去三個月買進方增加、無降評）。權重高。
- 散戶面：8 月第三方快照偏多，但資料已過時，10 月與 Reddit、StockTwits、X 皆無可用數據。權重降低。
- 內部人面：窗口內無公開市場買入，僅一筆小額董事賣出，偏中性至微弱負面。權重低（金額小）。
- 股價面（補充）：10 月自約 $185 回落至 $178.76 附近，仍低於目標價中位數；市場情緒可能短線偏弱，但與分析師評級並無直接衝突。

Divergence flag: **無法判定（DATA_UNAVAILABLE）**。分析師傾向偏多；8 月散戶快照亦偏多，兩者方向一致。但 10 月散戶資料缺漏，無法確認是否出現背離。

## Metrics

| 指標 | 數值 | 說明 |
|---|---|---|
| 整體情緒傾向（Overall sentiment lean） | **偏多（bullish）** | 信心中低，主因散戶資料缺漏 |
| 分析師買進比例（Analyst buy%） | **85.7%**（30 / 35） | 含 Strong Buy；hold 14.3%；sell 0% |
| 共識分數（Consensus score，1–5） | **4.00** | 加權平均，偏多 |
| 目標價均值（Avg price target） | ~$222.74（彙整）／ ~$210（Benzinga 8 月） | 來源與日期不一 |
| 分析師覆蓋家數 | 35（yf）／ 26（彙整站） | 口徑不同 |
| 散戶情緒分數（SentiSense，8 月） | 7.45（偏多，回升） | 2026-08-09 快照，非 10 月 |
| 社群聲量 | 約 12 則/日（8 月） | 10 月 DATA_UNAVAILABLE |
| 6 個月內部人淨交易（公開市場） | 買 $0.00M／賣 $0.039M | 1 筆董事賣出 |
| 機構家數 | 1,841 | 持股比例資料異常，趨勢 DATA_UNAVAILABLE |
| 背離旗標（Divergence flag） | 無法判定 | 10 月散戶資料缺漏 |

## 資料缺漏與限制

- Reddit（r/wallstreetbets、r/stocks）：抓取被封鎖，DATA_UNAVAILABLE。
- StockTwits：未抓取（金融網站限制），DATA_UNAVAILABLE。
- X：無 10 月當期可用貼文，DATA_UNAVAILABLE。
- 機構持股趨勢與持股比例：DATA_UNAVAILABLE（yf 數據異常且無歷史序列）。
- 目標價與評級來源跨站不一致，已分別標示，未強行統一。
- 本報告未提供交易建議。

主要來源（WebSearch 結果）：stockanalysis.com DLR 歷史價格；tipranks.com DLR 預測與目標價頁；benzinga.com DLR 情緒與目標價頁；app.sentisense.ai DLR 情緒頁；marketbeat.com 2026-07-24 相關快訊。

SENTIMENT REPORT COMPLETE
