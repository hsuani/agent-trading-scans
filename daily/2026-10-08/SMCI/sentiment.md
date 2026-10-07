# Sentiment — SMCI as of 2026-10-08

資料時點說明: yf 快取於 2026-10-07 13:13 UTC 更新 (`prices/yf/SMCI.json`)，live 查詢亦回傳同一組數值。as-of 2026-10-08 當日資料未取得。WebSearch 結果多為 2026 年 5 月至 7 月的快照，未能確認 10 月的評等或情緒。Reddit / StockTwits 依指示未抓取 (sandbox proxy 封鎖)，標記為 DATA_UNAVAILABLE。

工具備註: `pipeline/tools/yf.py` 不支援 `ratings` 與 `holders` 子命令，改用 `rec_summary` / `recommendations` (評等) 與 `major_holders` / `inst_holders` (持股)。

## Analyst consensus

15 位分析師 (yf info `numberOfAnalystOpinions`) / rec_summary 計數合計 18 筆: 4 buy (strongBuy 2 + buy 2) / 11 hold / 3 sell (sell 2 + strongSell 1)。yf `recommendationKey` = hold。

- 近四個月趨勢: buy 數 -3m 至 -1m 為 5 (strongBuy 2 + buy 3)，當月降為 4；hold 固定 11；sell 固定 3。近一月小幅降溫，無明顯轉向。
- 目標價 (yf info): 平均 41.87 / 最高 60.00 / 最低 15.00。現價 43.46，平均目標價較現價低約 3.7%，隱含小幅負報酬。
- 近期個別評等變動 (WebSearch 來源，日期為 2026 年中，已超過 2 個月前): Rosenblatt Buy 目標 45 (7/22)、Needham Buy 目標 46 (7/22)、Mizuho Hold 目標 34 (7/23)、GF Securities 升至 Buy (6/22)、Wolfe Research 首次覆蓋 Peer Perform (6/11)、Citi 目標 31 與 JPMorgan 目標 32 維持 Neutral (約 5 月，財報後)。
- 完整升降評等歷史 (upgrade/downgrade 明細): DATA_UNAVAILABLE (yf `recommendations` 僅回傳彙總計數，無逐筆紀錄)。
- 2026-10 之後的任何評等變動: DATA_UNAVAILABLE。

## Retail social

- Reddit (r/wallstreetbets, r/stocks): DATA_UNAVAILABLE (依指示不抓取 reddit 網域，sandbox proxy 封鎖)。
- StockTwits: DATA_UNAVAILABLE (依指示不抓取)。
- X / 新聞與評論 (WebSearch，無 10 月資料):
  - TipRanks 投資人情緒頁 (無日期快照) 標示為 "Very Negative"；頁面另述約 2.9% 的 TipRanks 散戶持有 SMCI，近 30 天持股變動 3.6%，持股者平均年齡超過 55 歲。此為 TipRanks 自身組合樣本，非全市場散戶。
  - 一篇 2026-05-07 的選擇權流量分析稱近期貼文約 60% 偏多，但 put 成交金額占 65.8%，以金額計偏空。單日樣本，權重低。
  - 較早的 TipRanks 文章標示 "Very Positive"，並提到近 30 天追蹤組合持股增加 19.9%，且分析師共識為 Moderate Buy (7 Buy / 3 Hold / 1 Sell)。與上述 "Very Negative" 來自不同時期，無法判定哪個較新。
- 聲量 (buzz volume) 相對於平常的量化數字: DATA_UNAVAILABLE。

## Retail tilt

- 方向: 無法確認可靠的 10 月散戶傾向。現有最新的單一快照 (TipRanks) 偏空，較早快照偏多，兩者衝突。
- 主要議題 (可辨識的 WebSearch 主題，非來自 Reddit / StockTwits): 會計與治理疑慮 (分析師 Citi / JPMorgan 以此為維持 Neutral 的理由)、財報後毛利率表現、Netflix 相關事件與審計爭議 (TradingView 舊文，已過時)。
- 散戶貼文原文引述: DATA_UNAVAILABLE。

## Insider activity

6 個月窗口 (2026-04-08 至 2026-10-08)，yf `insider` 共 135 筆歷史紀錄，窗口內可辨識的交易如下:

- 2026-09-04: CEO Charles Liang 與 10% 以上持股董事 Liu Liang Chiu-Chu Sara 各申報 Sale，200,000 股，價格 36.60-40.00，金額各 約 $7.72M。兩筆金額與股數完全相同，且 Ownership 分別為 I (間接) 與 D (直接)，可能是同一筆交易的重複申報，需以 SEC Form 4 核對。去重後約 $7.72M；未去重加總約 $15.44M。
- 2026-05-26: CEO 與 10% 持股人各申報 Stock Gift 340,000 股，價格 0.00。屬贈與，非市場賣出或買入，金額 $0。
- 2026-02-27: CEO 與 10% 持股人申報 derivative 轉換 (選擇權行使) 20,980 股，行使價 4.24，金額 約 $88,850。屬行使，非公開市場買入；窗口內。
- 2026-08-17、2026-08-10、2026-07-01、2026-06-30、2026-06-17、2026-05-08、2026-02-17、2026-02-10: 多位高階與董事 (CFO David E. Weigand、Officer Vikranth Malyala、Officer Jin Xiao、Kenneth Cheung、董事 Blair、Lin、Mogensen、Angel、Liaw 等) 有小額股數申報，但價格與金額皆為空值，無法判定為買入、賣出或例行股權發放 / 扣繳。交易型態: DATA_UNAVAILABLE。

窗口內可辨識的公開市場買入: 0 筆。可辨識的公開市場賣出: 1 組 (2026-09-04，去重後 200,000 股，約 $7.72M)。
Net 6mo 淨美元 (扣除空值筆數): 約 -$7.72M (去重)；空值筆數無法計入。

最近一年 (2025 年 8 月至 11 月) 另有數筆公開市場賣出，包括 CFO Weigand 2025-09-15 以 45.14 賣出 25,000 股、KAO George W 2025-08-22 以 43.88 賣出 40,000 股、Director Tuan Sherman 2025-11-26 以 33.00 賣出 48,630 股。不在 6 個月窗口內，僅供背景參考。

Notable: CEO Charles Liang (兼 10% 持股人，與 Liu Liang Chiu-Chu Sara 關係需確認) 於 2026-09-04 賣出，為窗口內唯一有價格的公開市場賣出。CFO 本窗口未見公開市場交易。

## Ownership shifts

依 yf `major_holders` (最新 13F 基準日 2026-06-30):
- 內部人持股 12.68%；機構持股 69.55%；機構佔流通股 79.64%；機構數 1,107 家。
- 前幾大機構 (2026-06-30，pctChange 為相對前期股數變化):
  - BlackRock 7.26% (47.7M 股，+9.98%)
  - Vanguard Capital Management 5.53% (+10.52%)
  - Vanguard Portfolio Management 5.00% (+11.14%)
  - Jane Street Group 4.38% (28.8M 股，+551%，變動幅度最大)
  - State Street 3.75% (+11.89%)
  - UBS Group 3.00% (+63.08%)
  - Geode Capital 2.36% (+9.57%)
  - Invesco 1.78% (-0.82%)
  - Goldman Sachs 1.69%
- 趨勢解讀: 前五大機構多為指數化持股，其增加主要反映指數權重或基金流入，不代表主動判斷。Jane Street 與 UBS 的大幅增加較值得注意，但僅為單季數據。
- 本季 vs 前季整體機構持股淨變動: DATA_UNAVAILABLE (僅取得前十大)。
- 空頭比例 (shortPercentOfFloat，yf info): 16.14%，為偏高水準。

## Net sentiment score

Composite: **中性偏空 (neutral-to-bearish)**，信心度 **低至中**。

分項:
- 分析師: 中性 (4 buy / 11 hold / 3 sell，hold 為多數；平均目標價略低於現價；近月 buy 微降)。信心中。
- 散戶: 無法確認。最新單一快照偏空 (TipRanks "Very Negative")，但較早快照偏多，且 Reddit / StockTwits / 聲量皆 DATA_UNAVAILABLE。信心低。
- 內部人: 偏空 (窗口內唯一可辨識的公開市場交易為 CEO 相關賣出，約 $7.7M；無公開市場買入)。信心中，需確認重複申報與空值筆數。
- 持股變化: 中性 (指數型持股增加，Jane Street、UBS 增加但規模小)。信心低 (資料為 2026-06-30)。
- 空頭比例 16% 為額外的逆向 / 風險訊號，非方向性證據。

Divergence flag: **部分分歧 / 無法確認**。分析師傾向為中性 (非偏多)，最新的散戶快照偏空，兩者方向接近但不完全相同。因散戶資料缺失，無法判定是否為典型的「散戶與分析師方向相反」情形。

## 資料缺口與限制

- Reddit、StockTwits: DATA_UNAVAILABLE (依指示不抓取)。
- 2026-10 的 WebSearch 結果: 未找到；最新分析師與情緒來源停留在 2026 年 7 月或更早。
- 個別評等歷史 (upgrade/downgrade 明細): DATA_UNAVAILABLE。
- 空值內部人交易的型態 (買入 / 賣出 / 發放): DATA_UNAVAILABLE。
- 價格落差: WebSearch 中 2026 年 7 月的價格引用約 $28.64，yf 現價為 $43.46。本報告以 yf 為準，未以該 7 月價格推算任何報酬。

SENTIMENT REPORT COMPLETE
