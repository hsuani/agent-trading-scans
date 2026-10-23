# Sentiment — IBM as of 2026-10-23

## Analyst consensus
目前 (yf rec_summary, period 0m): 25 家分析師中 **12 buy** (strongBuy 3 + buy 9) / **11 hold** / **2 sell** (sell 1 + strongSell 1)。

近三個月趨勢 (yf recommendations):

| 期間 | Buy 合計 | Hold | Sell 合計 |
|------|---------|------|-----------|
| 0m (現在) | 12 | 11 | 2 |
| -1m | 12 | 10 | 2 |
| -2m | 13 | 10 | 2 |
| -3m | 14 | 9 | 2 |

Recent moves: 買方評級三個月內由 14 降到 12，hold 由 9 升到 11，賣方維持 2 家。屬於評級緩慢往中性收斂，沒有明顯的大規模調升或調降。

- 個別升降評等 (upgrade/downgrade 機構名稱與日期): DATA_UNAVAILABLE (yf 工具只回傳月度彙總，未列出個別事件)
- 目標價變動: DATA_UNAVAILABLE (yf 工具未提供 price target 欄位)
- WebSearch 零星提及 (日期與來源不一，僅供參考): UBS 與 Truist 維持謹慎評等，Truist 目標價 $240；Benzinga 彙總 Outperform、平均目標 $264；另一德文來源列 12 buy / 6 hold / 0 sell、平均目標 $334.18，但該數字明顯偏舊，不採信。
- 資料限制: yf 的 Cookie/crumb 取得失敗 (ConnectionError)，但數據本身有回傳；rec_summary 與 recommendations 的 0m 數字相同，屬同一快照。

## Retail social
- Reddit (r/wallstreetbets、r/stocks): DATA_UNAVAILABLE。Reddit 網域在 WebSearch 中被封鎖 (domain 過濾回 400)，一般搜尋也找不到 2026 年 10 月的 IBM 討論串。提及量無法估計。
- StockTwits: 有一則新聞稿 (日期不明) 指 Stocktwits 情緒上移至 bullish 區，當時股價因一週下跌 12.2%，零售留言偏向「逢低買進」，另有一筆 $2M call 交易被解讀為反彈前兆。另一個 Stocktwits 符號頁快照顯示 39 bearish，但對應價格約 $288、財報日期為 7 月 22 日，明顯是舊快照，不採信。目前無法確認當下的數值。
- 情緒聚合站 (WebSearch 結果): 一個 sentiment 頁面標示 crowd view 為 NEGATIVE、過去 30 日投資人情緒 Very Negative；同頁新聞情緒為 70% bullish。兩者方向相反，來源品質有限。
- X: 未取得可用的 X 貼文樣本。DATA_UNAVAILABLE。
- 聲量: 無法與基準比較 (缺 Reddit 與 X 數據)。以 WebSearch 能找到的內容量判斷，屬低聲量，主要是媒體與聚合站的文章，而非散戶討論串。
- Tilt: 混合偏弱 (sentiment 聚合站偏負，StockTwits 最近一次讀數偏多，但日期不明)。
- 主要主題 (由零星來源歸納):
  1. AI 基礎建設需求何時轉化為企業支出，是否足以支撐估值。
  2. 財報與指引是否失望，股價在近期財報後的大幅波動。
  3. 股價跌至低位後是否為「逢低買進」機會。
- 代表性零售觀點 (WebSearch 來源, 摘要引用 ≤15 字): 「current levels a chance to buy」(Stocktwits 新聞稿轉述)。

## Insider activity
資料窗口: 2026-04-23 至 2026-10-23 (6 個月)，金額單位 USD。

Net 6mo: **$0.00M 買入 / $5.76M 賣出** (淨賣出約 $5.76M)。

- 6 個月內唯一的公開市場交易: THOMAS ROBERT DAVID (Officer，title 未揭露)，2026-08-26，賣出 25,000 股，成交價 $230.32，金額約 $5.76M，直接持有 (D)。
- 2026-07-01 ROBINSON ANNE (Officer) 有 7,295 股的異動，無金額欄位，性質不明 (可能為既得股或稅務扣繳)，歸類為無法分類。
- 2026-06-04 FEHRING NICOLAS A. (Officer) 贈與 400 股，金額 $0，不計入買賣。
- 6 個月外、可供背景參考的交易:
  - 2026-02-25: 董事 MIEBACH MICHAEL 買入 434 股 (約 $0.10M)、董事 HOWARD MICHELLE J. 買入 50 股 (約 $0.01M)。
  - 2026-01-30: 董事 FARR DAVID N 買入 1,000 股 (約 $0.30M)。
  - 2026-01-30: CEO KRISHNA ARVIND 獲得 83,028 股 (Stock Award 授予，非公開市場買入)。
  - 2025-03-03: THOMAS ROBERT DAVID 賣出 26,543 股 (約 $6.72M)，為歷史上的大額賣出。
- CEO / CFO 角色: 6 個月內 CEO (KRISHNA) 與 CFO (KAVANAUGH) 無公開市場買賣，僅見授予與無金額的異動。
- 整體解讀: 董事在 2026 年初有小額買入，但 6 個月內無買入；唯一的大額公開市場交易是賣出，淨方向偏負面，金額與持股相比屬小幅。

## Ownership shifts
- 機構持股比例: 66.5% (institutionsPercentHeld 0.665)；機構數量 4,394。
- 內部人持股: 0.1% (insidersPercentHeld 0.00105)。
- 集中度趨勢 (季度比較): DATA_UNAVAILABLE，yf 工具只回傳當前快照，無歷史變化。

## Net sentiment score
Composite: **neutral (中性)**，信心度 **低**。

理由:
- 分析師面: 12 buy / 11 hold / 2 sell，買方比例近三個月小幅下降，整體為偏中性的 hold 傾向。
- 零售面: 來源稀少且互相矛盾 (聚合站偏負、StockTwits 最近讀數偏多但日期不明)，Reddit 與 X 無資料。
- 內部人面: 6 個月淨賣出約 $5.76M，無買入，偏負面。

Divergence flag: **待確認 (資料不足)**。
- 分析師 tilt 偏中性、零售 tilt 混合、內部人 tilt 偏負。三者之間沒有明確的「零售多、分析師空」或「零售空、分析師多」的對立。
- 若以零售聚合站為準 (negative)，則與分析師中性 tilt 只是程度差異，不構成典型的 divergence。

關鍵資料缺口:
1. 2026-10-21 財報已排定，但本次搜尋未取得實際財報結果與盤後/隔日股價反應。財報後的分析師評級與目標價調整可能已發生，但未被抓到。此項為最重要缺口，建議在下一輪更新時補齊。
2. Reddit 與 X 聲量與內容完全缺失。
3. 目標價與個別評等變動事件缺失。

SENTIMENT REPORT COMPLETE
