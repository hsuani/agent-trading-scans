# Sentiment — HON as of 2026-10-23

## 資料來源與可靠度
- yf `recommendations` 與 `rec_summary` 回傳相同的四期評等分布 (0m 至 -3m)；歷史升降評等事件 (rating change history) 未回傳，列為 DATA_UNAVAILABLE。
- yf 執行時 Yahoo cookie/crumb 取得失敗，但資料仍有回傳。
- 內部人交易: yf `insider` 共 116 筆，本報告取 2026-04-23 至 2026-10-23 窗口內 19 筆。
- 社群情緒: 依指示僅用 WebSearch，未以 WebFetch 直接抓 Reddit JSON。未取得可引用的 r/wallstreetbets 或 r/stocks 貼文。
- 目標價與近期評等動態來自二手網站 (Investing.com、MarketBeat 等)，日期不一且來源互相矛盾。明顯為鏡像網域、文字亂碼的頁面已排除。

## Analyst consensus

評等分布 (yf, 單位: 家數)

| 評等 | 0m (當期) | -1m | -2m | -3m |
|---|---|---|---|---|
| Strong Buy | 3 | 3 | 3 | 3 |
| Buy | 11 | 11 | 12 | 12 |
| Hold | 9 | 9 | 8 | 8 |
| Sell | 0 | 0 | 0 | 0 |
| Strong Sell | 1 | 1 | 1 | 1 |
| 合計 | 24 | 24 | 24 | 24 |

當期為 14 家偏多 (含 3 家 Strong Buy)、9 家 Hold、1 家偏空 (含 1 家 Strong Sell)。與 3 個月前相比，偏多由 15 家降至 14 家，Hold 由 8 家增至 9 家，變化幅度小，屬於邊際降溫。

近期評等與目標價動態 (二手來源，信心中低):
- 7/24 RBC 目標價由 272 上調至 298，維持 Outperform (MarketBeat)。
- 7/27 BMO 目標價由 253 上調至 276，維持 Outperform (MarketBeat)。
- 8/31 Morgan Stanley 維持 Hold，目標價 250 (Investing.com)。
- 9/14 Melius 降評至 Hold，目標價 190 (Investing.com)。
- 9/24 Wells Fargo 首次覆蓋，Hold，目標價 231 (Investing.com)。
- 10/2 RBC 首次覆蓋列為 Buy，目標價 293 (Investing.com)。此與 7 月 RBC 目標價 298 的說法不一致，待核。
- BofA 維持 Buy，目標價由 275 下修至 265；JPMorgan Hold，目標價 212。日期不明。
- Q1 財報後 (4 月前後) Barclays、Jefferies、TD Cowen、Citigroup 下修目標價，評等仍偏正面。
- Mizuho 目標價 480 (MarketBeat, 7/1) 疑為資料錯誤 (前值 240)，不採用。

平均目標價: Investing.com 為 258.83 (高 303 / 低 186)；MarketBeat 為 259.67。MarketBeat 彙總為 13 Buy / 10 Hold / 2 Sell，與 yf 的 14 / 9 / 1 不同，本報告以 yf 為主。以 10/2 價格 213.80 計算，平均目標價隱含約 +21% 空間。今日價格未確認。

## Retail social

- Reddit: 直接 r/wallstreetbets 與 r/stocks 搜尋未取得可用貼文，無法抽樣引用。AltIndex 估計 Reddit 情緒 76/100 偏多，聲量約每日 2 次提及，且低於其近期平均。聲量屬低檔。
- StockTwits: 頁面顯示 "Bearish Sentiment" 標題，但無百分比、無日期，且快照價格互相矛盾，判定為不可靠，視為 DATA_UNAVAILABLE。
- X: 未取得可用資料，DATA_UNAVAILABLE。
- AltIndex 綜合指數 (Reddit、StockTwits、論壇 NLP) 為 98/100 偏多，但歷史資料只到 2026-07。同站 Reddit 單項 76 分與綜合 98 分並存，口徑不一，信心低。
- SentiSense 30 日分數 4.82，中性且降溫，截至 2026-08-09，資料已過期約 2.5 個月。

社群聲量與傾向: 低聲量、傾向中性偏多 (資料弱)。

主要話題 (由搜尋摘要歸納，非逐篇閱讀):
1. 財報超預期與全年有機營收成長上修至 3%-4%，偏多。
2. Solstice 先進材料分拆與組合重整，對估值與價格比較的影響討論分歧，方向不明。
3. Q1 下修與航太 (aerospace) 逆風、中東衝突影響 Q2 指引，偏空疑慮。
4. 高管於 7-8 月在約 243-245 價位的賣出，被解讀為偏空訊號。
5. 「被低估」論述 (如 Jim Cramer 的評論)，偏多。

本節未取得逐篇貼文原文，故不附引文。

## Insider activity

窗口: 2026-04-23 至 2026-10-23。金額單位 USD M。

| 日期 | 人員 | 職稱 (yf) | 交易性質 | 股數 | 金額 USD M |
|---|---|---|---|---|---|
| 2026-07-27 | Kenneth J. West | Officer | 選擇權行使 (conversion) @ 181.39-200.61 | 17,032 | 3.31 |
| 2026-07-27 | Kenneth J. West | Officer | 賣出 @ 243.77 | 17,032 | 4.15 |
| 2026-08-03 | Kenneth J. West | Officer | 賣出 @ 245.47 | 316 | 0.08 |

- 6 個月淨額: 買進 0 筆 / USD 0M；賣出 2 筆 / USD 4.23M。
- 上表選擇權行使後當日全數賣出，性質偏向行權變現，而非方向性加碼或減碼，解讀上應打折。
- CEO (Vimal M. Kapur) 與 CFO (Michal Stepniak) 在窗口內的記錄皆無價格欄位，屬授予、歸屬或稅款扣繳性質的可能性高，無法分類，未計入買賣。
- 同窗口內其餘 16 筆均無價格欄位，同樣未計入。
- 窗口外背景 (不計入 6 個月淨額): 2026-02-19 至 03-02，Lieblein、Currier、Davis、West 等合計賣出約 USD 2.75M (單價約 240-244)。
- 整體解讀: 窗口內唯一有現金價格的交易為單一高管賣出，無 CEO/CFO 公開市場買賣紀錄。內部人方向偏空但規模與信號強度有限。

## Ownership shifts

- 機構持股比例 84.77%，機構數 2,811 家；內部人持股 0.08%。
- 機構持股變化趨勢 (季度比較): DATA_UNAVAILABLE，目前僅有單一快照。

## Net sentiment score

綜合: 中性偏多 (neutral-to-bullish)，信心中低。

| 面向 | 傾向 | 信心 | 依據 |
|---|---|---|---|
| 分析師 | 偏多 | 中 | 14 / 24 家偏多，平均目標價隱含上行；Hold 家數近期增加 |
| 散戶 / 社群 | 中性 | 低 | 聲量低，單一來源 76 分偏多，綜合指數 98 分口徑不一，資料過期 |
| 內部人 | 偏空 (輕度) | 低 | 6 個月 2 筆賣出 USD 4.23M，零買進，單一高管且含行權賣出 |
| 機構 | 持平 (快照) | 低 | 持股 84.8%，無趨勢資料 |

Divergence flag: 部分。
- 分析師偏多與內部人賣出方向不一致，屬於內部人與分析師之間的分歧。
- 散戶 (低信心) 並未與分析師方向相反，散戶背離判定為否。

注意事項:
- 價格來源不一致: 10/2 價 213.80 (52 週區間 195.77-260.15)，與 7 月至 8 月高管賣出價 243-245 相比約降 12%。此跌幅是否含 Solstice 分拆之價格調整，未經證實。
- 今日股價未取得，目標價隱含空間僅供參考。
- 本報告為情緒讀數，不構成交易建議。

SENTIMENT REPORT COMPLETE
