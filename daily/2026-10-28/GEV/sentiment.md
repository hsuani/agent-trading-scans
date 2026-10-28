# Sentiment — GEV as of 2026-10-28

## 資料來源狀態

| 來源 | 狀態 | 備註 |
|---|---|---|
| yf recommendations / rec_summary | 可用 | Yahoo cookie/crumb 取得失敗，但仍回傳評級計數 |
| yf insider | 可用 | 回傳 47 筆，6 個月窗口內有效資料已篩出 |
| yf major_holders | 可用 | 僅有單一時點快照，無歷史趨勢 |
| Reddit r/wallstreetbets | DATA_UNAVAILABLE | WebFetch 無法連線 www.reddit.com |
| Reddit r/stocks | DATA_UNAVAILABLE | 同上 |
| StockTwits | DATA_UNAVAILABLE | api.stocktwits.com 無法解析，需於 session 網路設定放行 |
| X / 新聞搜尋 (WebSearch) | 部分可用 | 結果多為聚合站或日期不明，可信度低 |

## Analyst consensus

38 位分析師: 31 buy (6 strong buy + 25 buy) / 7 hold / 0 sell (yf rec_summary, 0m 期)。

評級分布近四個月變化很小:

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell |
|---|---|---|---|---|---|
| 0m (現在) | 6 | 25 | 7 | 0 | 0 |
| -1m | 6 | 24 | 7 | 0 | 0 |
| -2m | 6 | 24 | 7 | 0 | 0 |
| -3m | 6 | 24 | 8 | 0 | 0 |

- 評級計數: 最近一個月多 1 家 Buy，對應 -3m 時的 1 家 Hold 轉向 Buy。沒有 Sell 評級出現。
- 目標價 (Target price) 異動: 來自搜尋結果的資訊彼此矛盾，無法確認:
  - 一則搜尋結果稱 JPMorgan 於 2026-10 將目標價由 1,330 USD 下調至 1,150 USD，Susquehanna 由 1,300 調至 1,270 USD。
  - 另一則搜尋結果稱 JPMorgan 於 2026-04 將目標價由 1,000 USD 上調至 1,150 USD 並維持 Overweight，同時移出 Analyst Focus List。
  - 兩者目標價數字相同，日期與方向不同。在取得原始評級紀錄 (rating history) 前，判定為 DATA_UNAVAILABLE (10 月異動未確認)。
- 其他已見於搜尋結果的目標價 (日期多為 2026-04 至 2026-08，未在 10 月確認): RBC 2026-04-23 由 996 調至 1,195 USD (Outperform)。
- 共識目標價來源彼此不一: MarketBeat 2026-07 約 1,133 USD (30 位)；Walnut Invest 2026-08 約 1,231 USD (34 位，30 buy / 8 hold / 0 sell)。yf 的 38 位計數與這些來源的樣本數不同，以 yf 為準。

## Retail social

- Reddit: DATA_UNAVAILABLE。r/wallstreetbets 與 r/stocks 的 GEV 搜尋均無法存取，無法估計貼文數、分數與情緒傾向。WebSearch 也未找到 2026-10 的 GEV 相關 Reddit 串文。
- StockTwits / X: StockTwits 為 DATA_UNAVAILABLE。X 的資料未取得。
- LunarCrush 聚合頁 (WebSearch 摘要): 顯示 $GEV 過去 24 小時 377 則貼文，社群情緒 85% 正面。頁面快照日期不明，且未註明 Reddit 占比。此數字不宜單獨作為結論。
- 量能 (volume): 無法與歷史平均比較，判定為 DATA_UNAVAILABLE。
- 搜尋摘要中的散戶論點 (日期不明，僅供參考):
  - 估值擔憂: 本益比超過 50 倍，關稅風險。
  - 多頭敘事: AI 電力需求與燃氣輪機訂單的長期成長。
  - 股價回檔: 摘要提到自 2026-06-30 高點回落約 21%，2026-10-15 收盤約 926 USD。此數字來自聚合站，未經原始來源核對。
- 主題 (Themes): AI 電力建置需求、估值偏高、關稅與政策風險、財報前回檔。

## Insider activity

以 2026-04-28 至 2026-10-28 為 6 個月窗口 (yf insider 原始資料):

- 公開市場賣出 (Sale): 合計 約 7.04M USD (賣出 2 筆)。
  - 2026-06-01 ABATE VICTOR (Officer): 賣出 4,819 股，價格 948.08 USD，金額 4.57M USD。
  - 2026-05-14 POTVIN MATTHEW JOSEPH (Officer): 賣出 2,333 股，價格 1,059.09 USD，金額 2.47M USD。
- 公開市場買入 (Buy): 0 筆。
- 董事 (Director) 2026-05-14 集體取得 8 筆，每人 495 至 1,350 股，yf 未標示金額 (Value 為空)，性質推測為年度董事股權授予，但原始資料未明確註記，標示為 DATA_UNAVAILABLE (性質未確認)。
- 窗口邊界外的相關交易 (供參考):
  - 2026-04-27 STRAZIK SCOTT (CEO): 衍生性證券行權 (conversion/exercise) 44,496 股，行權價 92.13 至 149.78 USD，金額約 5.35M USD。屬於選擇權行權，並非公開市場買入，且落在窗口外。
  - 2026-04-02 與 2026-03-03 BAERT STEVEN (Officer): 分別有 8,505 股 (無金額) 與賣出 5,300 股 (850 USD，約 4.51M USD)，皆在窗口外。
- CEO 與 CFO: 窗口內 CEO (STRAZIK) 無公開市場交易；CFO (PARKS) 最近一筆為 2025-12-01 (無金額)，同樣在窗口外。
- 解讀: 窗口內全為高價位賣出，且無公開市場買入。以 yf 資料判斷為偏空訊號的輕度信號，但未確認是否屬於 10b5-1 預定計畫，此處無法判斷其動機。

## Ownership shifts (yf major_holders)

- 機構持股比例: 81.58% (機構家數 4,245)。
- 內部人持股比例: 0.13%。
- 本次僅為單一快照，無法判定 13F 季度變化趨勢，標示為趨勢 DATA_UNAVAILABLE。機構集中度偏高，代表大型基金佔比高，但不代表買賣方向。

## Net sentiment score

- 分析師: 偏多 (31 buy / 7 hold / 0 sell，四個月內無降級至 sell，信心中高)。
- 內部人: 偏空 (窗口內約 7.04M USD 公開市場賣出，0 筆買入，信心低至中，因無法確認 10b5-1 性質)。
- 散戶: 無法判定。Reddit 與 StockTwits 無資料，LunarCrush 單一快照 85% 正面但來源與日期不明，信心低。
- 綜合: **偏多 (中等信心)**，主要依據分析師一致買進評級。內部人賣出與近期股價回檔是主要反向因素。散戶端缺乏足夠資料，此結論不應視為散戶情緒確認。

Divergence flag: **無法判定 (no reliable retail data)**。分析師與內部人 (賣出) 的方向有分歧，但散戶端資料缺失，故不能下"散戶與分析師相反"的結論。若後續取得 Reddit / StockTwits 資料，需重新評估此旗標。

## 資料限制

- 所有評級計數來自 yf 單一時點，無 rating 日期戳記，無法精確定位個別升降級的日期。
- 搜尋結果中的目標價與股價資料多為聚合站，來源不一，未逐一核對原始公告。
- 2026-10-28 當日若有財報 (搜尋結果稱 10-28 為預定財報日)，財報後的評級與股價反應不在本報告時間範圍內，視為 unknown。
- 本報告不含交易建議。

SENTIMENT REPORT COMPLETE
