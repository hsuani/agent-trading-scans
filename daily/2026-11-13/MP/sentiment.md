# Sentiment — MP as of 2026-11-13

資料截止: 所有數據不晚於 2026-11-13。yf 快取 `prices/yf/MP.json` 刷新於 2026-11-12 15:06 UTC。live feed 無 cookie/crumb 而退回快取，屬正常。

## Analyst consensus

yf `rec_summary` 當期 (0m): Strong Buy 5 / Buy 14 / Hold 0 / Sell 0 / Strong Sell 0 (合計 19 筆評等)。
yf `info` 的 `numberOfAnalystOpinions` 為 16，與評等表合計 19 不一致，可能是不同來源或統計口徑，以評等表為準並註記差異。

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell |
|---|---|---|---|---|---|
| 0m (本期) | 5 | 14 | 0 | 0 | 0 |
| -1m | 5 | 13 | 1 | 0 | 0 |
| -2m | 5 | 13 | 1 | 0 | 0 |
| -3m | 5 | 13 | 0 | 0 | 0 |

目標價 (yf `info`，USD):

| 項目 | 金額 (USD) |
|---|---|
| 平均目標價 | 67.5 |
| 最高目標價 | 100.0 |
| 最低目標價 | 40.0 |
| 現價 (快取) | 36.165 |
| 隱含上行空間 (至平均目標價) | 約 +87% |

Recent moves: yf 的 `recommendations` 只提供彙總計數，沒有逐筆升降評等紀錄 (DATA_UNAVAILABLE: 個別券商升降評日期與對象)。由彙總變化可見，約一個月內有一筆 Hold 轉為 Buy，之後 Hold 歸零。
外部搜尋結果提及 JPMorgan 與 Goldman Sachs 曾升評，但來源日期混雜，無法確認是否落在本期，故不採信為近期事件。Goldman 目標價 $80 (由 $71 上調) 與 Morgan Stanley 目標價 $70 (由 $62 上調) 出現於搜尋結果，日期標註為 2026-05，屬較舊資料。

## Retail social

- Reddit: DATA_UNAVAILABLE。r/wallstreetbets 與 r/stocks 搜尋依規定不直接抓取，本次 WebSearch 也未回傳 2026-11 的 Reddit 討論串，無法取得樣本或 tilt。
- StockTwits / X: 部分可用，但時間戳不完整。
  - 一則 StockTwits 新聞稱散戶情緒於 11/7 前後由 bearish 轉為 neutral，訊息量 high。該文同時提及 YTD 漲幅 247%，年度無法確認，故只採方向性資訊。
  - 另一則 StockTwits 文章描述近數月情緒由 bearish 轉 bullish，訊息量增 140%，追蹤人數增 76%，時間範圍不明。
  - LunarCrush 頁面顯示社群正面情緒約 86–88%，但頁面無日期，數值彼此不一，且該指標為社群文本分析，不等於散戶問卷。
- Buzz volume: 定性判斷為偏高。LunarCrush 快照提及單日數百則貼文等量級，但無同期基準可比，只能判定為「高於一般」的弱證據。
- Themes (由 StockTwits 與新聞標題歸納):
  - 稀土供應鏈與中國出口管制的戰略性 (政府/國防需求、DoD 價格底板等議題)。
  - 磁鐵 (magnet) 業務進度，特別是 GM 等客戶的初次交付時程。
  - 股價自 52 週高點回落的估值與風險承受度爭議。
  - CEO 對稀土專案的表態 (一則標題稱「warp speed」，另一則稱應謹慎)，散戶解讀分歧。
- Sample (≤15 字，僅示意): 「retail sentiment moved to neutral from bearish」 (StockTwits 標題轉述)。

## Insider activity

Net 6mo: DATA_UNAVAILABLE。yf `insider` 回傳空陣列 (live 與快取一致)，無法區分「六個月內無交易」與「資料源缺漏」，不推定為零交易。
參考 (非交易資料): yf 公司高管清單顯示 CEO James Litinsky、COO Michael Rosenthal、CFO Ryan Corbett 等，FY2025 薪酬 (totalPay) 分別約 USD 3.23M、1.97M 等，屬薪酬而非內部人買賣。
內部人持股比例 (yf `major_holders`): 19.6%。

## Ownership shifts

yf `major_holders`: 機構持股 79.15%，機構持股占流通股 98.45%，機構家數 968。

Top holders (yf `inst_holders`，最新申報期 2026-06-30 或 2026-09-30):

| 持有人 | 持股比 | 股數 (M) | 市值 (USD M) | 較前期變化 | 申報期 |
|---|---|---|---|---|---|
| Hancock Prospecting Pty Ltd | 8.34% | 14.86 | 537.2 | 0.0% | 2026-06-30 |
| BlackRock Inc. | 8.27% | 14.74 | 532.8 | -0.06% | 2026-06-30 |
| State Street Corp | 4.36% | 7.77 | 281.0 | +5.09% | 2026-06-30 |
| Vanguard Capital Management | 3.89% | 6.94 | 250.7 | +0.91% | 2026-06-30 |
| Vanguard Portfolio Management | 3.83% | 6.82 | 246.7 | +0.78% | 2026-06-30 |
| Shaw D.E. & Co. | 3.27% | 5.83 | 210.7 | +85.1% | 2026-06-30 |
| Morgan Stanley | 2.68% | 4.77 | 172.5 | -14.0% | 2026-06-30 |
| UBS Group AG | 2.62% | 4.68 | 169.1 | +8.2% | 2026-09-30 |
| Van Eck Associates | 2.56% | 4.57 | 165.0 | -0.5% | 2026-06-30 |
| Invesco Ltd. | 1.98% | 3.54 | 127.9 | -6.8% | 2026-06-30 |

趨勢: 前十大多為指數與被動資金，合計持股仍穩定；主動型與量化機構 (Shaw、UBS) 有增持跡象，Morgan Stanley、Invesco 略減。機構分歧不大，但單一時點資料，無法判斷長期趨勢。

## 市場價格與事件背景

- 現價 (快取) USD 36.165，前收 USD 36.73，52 週區間 USD 31.9–76.8。
- 最近一次財報: 2026-11-05 (yf `earnings_dates`)，報告 EPS USD 0.04，預估 USD -0.01，優於預期。
- 外部搜尋提及 Q3 營收約 USD 147.7M，與 yf 財報日一致，但外部來源日期與數字說明有矛盾，僅作輔助。
- 外部來源股價 (如 USD 55.46) 與 yf 快取 USD 36.165 不一致，來源時間不明，本報告以 yf 快取為準。

## Net sentiment score

Composite: **bullish (信心: 中)**

- 分析師面: 強烈偏多。19 筆評等中 0 Sell、0 Hold (本期)，平均目標價隱含約 +87% 上行。信心高，但目標價分散 (USD 40–100)，且本期評等計數與 info 的 16 家不一致。
- 散戶面: 混合偏多，信心低。社群正面指標與 StockTwits 情緒訊息相互矛盾 (由 bearish 轉 neutral 或 bullish)，且日期不完整。
- 內部人面: DATA_UNAVAILABLE，未納入評分。
- 機構面: 中性偏多 (主動型小幅增持)。

Divergence flag: **no** (散戶與分析師傾向無明顯反向)。
附註: 本期更明顯的落差是股價 (USD 36.17) 與平均目標價 (USD 67.5) 之間的估值缺口，約 87%。此落差反映市場對目標價的懷疑，而非散戶與分析師之間的分歧。由於散戶資料不完整，此判斷可能隨補充資料而改變。

SENTIMENT REPORT COMPLETE
