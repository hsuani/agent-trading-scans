# Sentiment — AMT as of 2026-10-24

## 資料來源狀態
- Reddit (r/wallstreetbets, r/stocks): DATA_UNAVAILABLE，WebFetch 回傳無法連線錯誤。
- StockTwits: DATA_UNAVAILABLE，api.stocktwits.com 解析失敗（ENOTFOUND）。
- X / 社群原文: DATA_UNAVAILABLE，WebSearch 只回傳財經網站與分析師彙整頁，沒有可辨識的散戶貼文。
- 可用來源: yf 分析師評級彙總、yf 評級歷史、yf 內部人交易、yf 持股結構，以及 WebSearch 找到的第三方分析師目標價彙整。

## Analyst consensus
目前 25 位分析師: 7 Strong Buy / 15 Buy / 3 Hold / 0 Sell / 0 Strong Sell。Buy 合計 22 位，佔 88%。
- 近 3 個月趨勢: 3 個月前為 6 Strong Buy / 15 Buy / 4 Hold。目前 Hold 少 1 位、Strong Buy 多 1 位，屬於一檔評級小幅升級，沒有降級紀錄。
- 評級變動明細: yf recommendations 只回傳與彙總相同的月度計數，沒有逐筆升降評級紀錄，因此個別券商升降級屬 DATA_UNAVAILABLE。
- 目標價 (WebSearch 第三方彙整，非 WebFetch 財經站): Investing.com 平均 12 個月目標價約 $215.70，區間 $188–$260，約 23 位分析師；Benzinga 顯示約 $226，19 位分析師。兩來源有差距，且 Investing.com 的 SWOT 區段引用的 $255.50 與自身數字不一致，以 $215.70 與 $226 為參考區間，不採用單一數字。
- 參考股價: 搜尋彙整提到約 $176，與 2026-07 至 2026-08 內部人交易成交價 (約 $169–$179) 同一區間，判斷屬實，但未以即時報價驗證。
- 財報日期來源不一致: 一來源列 2026-10-27，另一來源列 2026-10-22。若 2026-10-27 為真，財報將在本報告日後數日內公布，屬於分析師情緒的近期催化劑。

## Retail social
- Reddit: DATA_UNAVAILABLE。
- StockTwits: DATA_UNAVAILABLE。
- X / 新聞鏈: 搜尋結果未出現可引用的散戶原文，無法量化聲量與多空比例。
- 聲量 (相對典型水準): DATA_UNAVAILABLE，不以推測數字填補。
- 散戶多空傾向: DATA_UNAVAILABLE。
- 主題: 無法從散戶端歸納。搜尋結果中的分析師與媒體敘事集中在兩點: 防禦型基礎建設 REIT 定位，以及相對 AI 相關標的較弱的股價表現 (WebSearch 摘要提到 52 週跌約 19%，年初至今微幅上漲；此數字僅來自單一第三方，未經驗證)。

## Insider activity
統計區間: 2026-04-24 至 2026-10-24（近 6 個月）。金額來自 yf insider 的 Value 欄位，單位為 USD，以 M USD 表示。

| 日期 | 人員 | 職稱 | 交易 | 股數 | 金額 (M USD) |
|---|---|---|---|---|---|
| 2026-08-21 | KALATHUR RAJESH | Director | 買進 @ $177.00 | 2,829 | +0.50 |
| 2026-07-29 | MEYER ROBERT JOSEPH JR | Officer | 賣出 @ $178.89 | 5,000 | -0.89 |
| 2026-07-29 | DOWLING RUTH T | General Counsel | 賣出 @ $169.54–$174.96 | 1,791 | -0.31 |
| 2026-04-29 | DOWLING RUTH T | General Counsel | 賣出 @ $177.54–$178.48 | 972 | -0.17 |

- 6 個月內: 買進 $0.50M（1 筆，董事），賣出 $1.38M（3 筆，其中 GC 2 筆、Officer 1 筆）。淨額約 -$0.88M，屬小幅淨賣出。
- CEO / CFO 在此區間無公開市場交易。CEO VONDRAN 與 CFO SMITH 的大額賣出集中在 2026-02 至 2026-03，且與期權行權 (行權價 $94.57–$94.71) 相連，屬於行權後賣出，型態可能是計畫性交易，無法確認是否為 10b5-1 計畫。此區間外的 CEO/CFO 賣出不列入 6 個月淨額。
- 其餘為獎勵授予 (Stock Award / Grant, 金額 0)，與 2026-03-10 及 2026-10-01 的年度或新任授予相關，不計入淨買賣。
- 同一 Director (KALATHUR) 於 2026-03-10 亦有買進 $0.49M (2,671 股 @ $185.30)，因此董事端近 8 個月出現兩次市場買進，為較正面的訊號。

## Ownership shifts
- 機構持股比例: 96.9%（機構持股 2,387 家）。內部人持股 0.08%。
- 機構持股趨勢 (季度變化): DATA_UNAVAILABLE。yf major_holders 只回傳單一時點快照，無歷史序列，無法判斷增減。
- 集中度判讀: 機構持股高，屬於大型機構持有為主的結構，個別機構進出對股價的影響需另以 13F 資料確認。

## Net sentiment score
- 分析師面: 偏多。88% Buy，無 Sell，評級小幅升級，目標價區間高於參考股價約 20–28%。
- 內部人面: 偏空 (輕度)。6 個月淨賣出約 $0.88M，且主要為 GC 與 Officer 的賣出；董事於 2026-03 與 2026-08 有兩次市場買進，部分抵銷。
- 散戶面: DATA_UNAVAILABLE，未納入權重。
- 綜合: 偏多 (Bullish)，信心低。分析師一致偏多是主要支撐，內部人淨賣出與缺乏散戶資料使信心降低。
- 分歧旗標: 無法判定。散戶端缺資料，無法比較散戶與分析師傾向是否相反。

## Metrics

| 指標 | 數值 | 說明 |
|---|---|---|
| 整體情緒傾向 | 偏多 (Bullish) | 信心低；散戶端缺資料 |
| 分析師 Buy 佔比 | 88% (22 / 25) | 7 SB + 15 B，3 Hold，0 Sell |
| 分析師綜合分數 | 4.16 / 5 | 以 SB=5, B=4, H=3, S=2, SS=1 加權平均 |
| 近 3 個月評級變化 | +1 Strong Buy，-1 Hold | 小幅升級，無降級 |
| 目標價 (平均 / 區間) | 約 $216–$226 / $188–$260 | 第三方彙整，來源有差距 |
| 6 個月內部人淨額 | 約 -$0.88M | 買進 $0.50M，賣出 $1.38M |
| 機構持股比例 | 96.9% (2,387 家) | 單一快照，趨勢 DATA_UNAVAILABLE |
| 內部人持股比例 | 0.08% | 屬 yf 快照 |
| 散戶聲量 / 傾向 | DATA_UNAVAILABLE | Reddit、StockTwits 皆無法取得 |
| 分歧旗標 | N/A | 散戶端缺資料 |

SENTIMENT REPORT COMPLETE
