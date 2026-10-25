# Sentiment — AEVA (Aeva Technologies) as of 2026-10-26

## 資料狀態
| 來源 | 狀態 |
|---|---|
| yf rec_summary / recommendations | 成功（Yahoo cookie/crumb 失敗但仍回傳資料） |
| yf insider | 成功，最新交易日 2026-09-02，距 as-of 日期約 7.5 週，資料可能落後 |
| yf major_holders | 成功，僅為當期快照，無季度變化 |
| Reddit r/wallstreetbets、r/stocks | DATA_UNAVAILABLE（WebFetch 被擋） |
| StockTwits | DATA_UNAVAILABLE（api.stocktwits.com DNS 解析失敗） |
| WebSearch（X / 新聞） | 僅找到第三方快照（MarketBeat、Benzinga），日期多不明或為 2026-04 / 2026-08，無 2026-10 資料 |

## Analyst consensus
目前（0m）：**3 buy / 2 hold / 0 sell**（strongBuy 0、strongSell 0）。

| 期間 | Buy | Hold | Sell |
|---|---|---|---|
| -2m | 3 | 1 | 0 |
| -1m | 3 | 2 | 0 |
| 0m（current） | 3 | 2 | 0 |

- 近期動態：-2m 至 -1m 期間有一家分析師由 Buy 轉為 Hold 的可能性（但 Buy 數未減，故實際是新增一家 Hold 或其他組合，個別評等變動明細 DATA_UNAVAILABLE）。-1m 至今無變化。
- 目標價（PT）：yf 未提供，DATA_UNAVAILABLE。WebSearch 所見 Benzinga 快照（日期 2026-08-04）顯示平均 PT 約 USD 17、共 9 位分析師 Buy，但與 yf 的 5 家分析師數字不一致，且快照已過期，僅供參考，不採信為當前共識。

## Retail social
- **Reddit**：DATA_UNAVAILABLE。無法取得 r/wallstreetbets 與 r/stocks 貼文，故無樣本、無 tilt 判定。
- **StockTwits**：DATA_UNAVAILABLE。
- **X / 新聞**：
  - MarketBeat 快照顯示空單佔流通股約 25.6%，並稱月增，但日期不明。
  - Benzinga 快照（2026-08-04）顯示 short float 約 10.2%。與 MarketBeat 數字差距大，來源分歧，無法確認。
  - MarketBeat 新聞情緒分數在 0.29 至 1.06 之間（尺度 -2 至 2，依快照不同）。
  - 同一頁面稱本週有 18 則新聞，平均週約 4 則。日期不明，聲量訊號的可信度低。
- **聲量（buzz volume）**：社群聲量無法量化，DATA_UNAVAILABLE。僅有上述新聞量快照。
- **零售傾向（tilt）**：DATA_UNAVAILABLE，無法判定 bullish / bearish / mixed。
- **代表性引述**：無，因未取得任何社群貼文。
- **主題（可見範圍內）**：
  1. 空頭部位偏高（來源分歧，數字不可靠）。
  2. 內部人持續減持（由 yf insider 資料得出，非社群來源）。
  3. 股價自 2026-08 高點明顯回落（由內部人成交價推估，見下節）。

## Insider activity
統計區間：2026-04-26 至 2026-10-26（6 個月）。

- 公開市場買進：**0 筆，USD 0.00M**
- 公開市場賣出：原始加總 USD 31.14M；扣除鏡像重複列（同一筆交易在 CEO 與 CTO 的持股實體各出現一次，如 2026-07-08、2026-07-27）後為 **USD 29.61M**，以下採扣除後數字。
- 淨額：**約 -USD 29.6M（純賣出）**

| 人員 | 職稱 | 6mo 賣出（USD M） | 筆數（扣重複） | 備註 |
|---|---|---|---|---|
| Dardashti Soroush Salehian | CEO | 15.64 | 4 | 06-16、07-08、07-27、08-11 |
| Rezk Mina | CTO | 11.00 | 2 | 06-16、08-10（另有 2 筆鏡像列已排除） |
| Sinha Saurabh | CFO | 2.83 | 5 | 07-02 至 09-02，持續減持 |
| Motlagh Katherine | Director | 0.06 | 1 | 08-12 |
| Zadesky Stephen Paul | Director | 0.08 | 1 | 06-22 |

**Notable 交易**
- CEO Dardashti 2026-06-16 賣出 275,349 股，成交價 USD 24.34–27.09，約 USD 6.76M。
- CEO Dardashti 2026-08-11 賣出 305,099 股，成交價 USD 23.86–25.69，約 USD 7.34M，為區間最大單筆之一。
- CTO Rezk 2026-06-16 賣出 350,000 股，成交價 USD 24.37–26.11，約 USD 8.60M，為區間最大單筆。
- CFO Sinha 2026-09-02 賣出 34,146 股，成交價 USD 14.83，約 USD 0.51M，為區間內最新一筆與最低成交價。

**非公開市場項目（不計入上述淨額）**
- 2026-06-18：10% 以上大股東 Sylebra Capital 取得 6,150 股 stock award，約 USD 0.15M。
- 董事與 CEO/CTO/CFO 之多筆 stock award / gift 為 0 價值，屬薪酬或贈與，不作為賣壓或買壓訊號。

**資料品質提醒**
- 2026-07-27 的 15.40 成交價與同期 07-08（21.16）及 08-11（約 25）不一致，可能是 yf 欄位日期或性質錯誤，待人工核對，未納入結論。
- 2026-03-03 至 2026-09-02 的成交價區間約 USD 13.9 至 27.1，可作為近期價格參考，但目前即時股價 DATA_UNAVAILABLE。

## Ownership
- 內部人持股：17.47%
- 機構持股：67.52%（佔流通股 81.82%）
- 機構家數：272
- 季度變化趨勢：DATA_UNAVAILABLE（僅有當期快照）
- 主要大股東：Sylebra Capital（10% 以上受益人）。2025-03-26 至 2025-03-31 曾大量買進，約 5.85M 股，成交價 USD 4.36–6.77。目前持股數 DATA_UNAVAILABLE。

## Net sentiment score
| 面向 | 判定 | 說明 |
|---|---|---|
| 分析師 | 偏多（中性偏多） | 3 buy / 2 hold / 0 sell，無 sell；hold 近期增加，PT 資料缺失 |
| 內部人 | 偏空（明顯） | 6 個月無公開市場買進，約 USD 29.6M 賣出，CEO、CTO、CFO 皆參與 |
| 零售社群 | 無法判定 | Reddit、StockTwits 皆 DATA_UNAVAILABLE |
| 空頭部位 | 偏高（來源分歧） | short float 報導為 10.2% 至 25.6% 不等 |

**綜合：中性偏空（neutral-to-bearish）。信心：低至中。**
理由：內部人持續、大額、跨三位高階主管的賣出是本次最清楚的訊號，且成交價已由 8 月的 USD 24–26 回落至 9 月初的 USD 14.83。分析師端維持無賣出評等，但 hold 增加且 PT 資料不足。零售面缺席，使綜合判斷的信心受限。資料最新日期距 as-of 約 7.5 週，且社群與即時價格資料缺失，結論應視為暫時性。

**Divergence flag：是（內部人與分析師方向分歧）**
- 分析師偏多，內部人大量淨賣出，兩者方向不一致。
- 零售 tilt 未取得，無法判定零售是否與分析師反向。此項需待 Reddit 或 StockTwits 可用後補做。

## 後續補強建議（僅資料面，非交易建議）
1. 以其他 Reddit 代理或 PRAW 取得 r/wallstreetbets、r/stocks 近 30 天貼文，補上零售 tilt 與聲量。
2. 以即時報價確認 as-of 日股價，以計算內部人成交價與現價之差距。
3. 核對 2026-07-27 異常成交價列。
4. 取得 yf 或其他來源的目標價（PT）與個別分析師評等變動明細。

SENTIMENT REPORT COMPLETE
