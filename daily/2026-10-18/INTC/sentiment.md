# Sentiment — INTC as of 2026-10-18

資料來源說明: `pipeline/tools/yf.py` 沒有 `ratings` 與 `holders` 子命令，改用 `rec_summary`、`recommendations`、`major_holders`、`inst_holders`、`insider`。Yahoo 即時連線失敗，數據來自 `prices/yf/INTC.json` 快取（_refreshed_at 2026-10-17 10:34 UTC，_misses 為空）。Reddit 與 StockTwits 直接抓取在本環境不可用，改以 WebSearch 取得間接資料。

## Analyst consensus
目前 (0m) 評級分布: 1 strongBuy / 14 buy / 32 hold / 1 sell / 1 strongSell，共 49 筆。快取 info 記載 43 位分析師意見，兩者計數不一致，以分布表為準並標註差異。

- 偏多比例約 31% (15/49)，持有約 65% (32/49)，偏空約 4% (2/49)。
- 近 3 個月趨勢: sell 由 2 降為 1，strongSell 維持 1，buy 由 13 升至 14，hold 由 31 升至 32。變化幅度小。
- recommendationMean 2.47 (1 至 5 分制，偏向 buy)，recommendationKey 為 buy。
- 目標價: 平均 118.05 / 中位數 115 / 最高 200 / 最低 80。以快取現價 89.85 計算，平均目標價高於現價約 31%。現價為 2026-10-17 快取值，可能已過時。
- 個別升降評等與目標價調整明細: DATA_UNAVAILABLE (rec 工具只回傳彙總計數，未回傳逐家事件)。

## Retail social
- Reddit: DATA_UNAVAILABLE。WebSearch 未找到 2026 年 10 月的 r/wallstreetbets 或 r/stocks 相關討論串，無法評估提及量與多空傾向。
- StockTwits: 2026 年 10 月的情緒分數 DATA_UNAVAILABLE。StockTwits 符號頁快照顯示價格 $92.32、單日 +7.89%，但沒有可確認日期的情緒分數。
- 間接情緒指標 (均非 10 月資料，時效性低):
  - AltIndex 聚合情緒 66/100，偏多 (頁面無日期)。
  - SentiSense 30 日分數 8，輕微偏多 (截至 2026-08-09)。
  - Naga 頁面: 群眾情緒分數偏空，部落客 67% 偏多，投資人情緒偏正面 (約 9 月)。
  - 9 月 3 日期權資料: 買權成交金額占 74%，賣權占 26%。同一來源指 RSI 超賣、MACD 偏空，與期權訊號分歧。
- 量能: 相對一般水準的提及量 DATA_UNAVAILABLE。
- Themes (取自次級來源，非直接社群文本):
  - 多方: Terafab 合作案; 2026 年股價大幅上漲 (52 週高點 142.35)。
  - 空方: 晶圓代工新創成本造成營業虧損; 股價高 Beta (約 2.24) 放大波動; 獲利為負 (trailing EPS 約 -2.12)。
  - 事件: Q3 財報日期來源不一致。快取與一則行事曆顯示 10/29 盤後，其他來源估 10/22 或 10/27。
  - Q2 財報 EPS 0.42 對比預估 0.22，超出約 95%。
- 代表性社群語句: 無可直接引用的 2026 年 10 月貼文，DATA_UNAVAILABLE。

## Insider activity
6 個月視窗 (2026-04-18 至 2026-10-18)，只計入有價格的交易:
- 買入: 約 $10.00M。CEO Tan Lip-Bu 於 2026-08-11 以 $95.00 買入 105,263 股 (間接持有)。該價格與 2026 年 8 月的增資/次級發行價一致，屬於發行相關交易，不一定代表一般公開市場買盤。
- 賣出: 約 $6.49M。
  - CTO Chandrasekaran 2026-05-29 以 $118.28 賣出 21,024 股 (約 $2.49M)。
  - Officer Miller (Boise April) 2026-05-01 以 $99.53 賣出 40,256 股 (約 $4.01M)。
- 淨額: 約 +$3.51M (買入大於賣出，僅計入有金額的交易)。
- 無金額紀錄: CFO Zinsner 2026-06-01 股數 37,015; CTO Chandrasekaran 2026-07-30 股數 33,007; 多位董事 2026-05-07 各 12,552 股 (Barratt 2,730、Yeary 26,611); Chandrasekaran 2026-04-30 股數 33,008。這些多半是授予、歸屬或稅款代扣，無法判定為市場買賣，未計入淨額。
- 視窗外參考: CFO Zinsner 2026-01-26 以 $42.50 買入 5,882 股 (約 $0.25M)。

## Ownership shifts
- 機構持股 62.89%，流通股口徑 73.12%，機構數 4,415。
- 內部人持股 13.99%。
- 前十大持股 (2026-06-30 13F):
  - BlackRock 8.46% (股數 -4.71%)
  - Vanguard Capital 5.65% (+1.14%)
  - State Street 4.30% (+1.18%)
  - Nvidia 4.26% (持平，策略持股)
  - Invesco 3.13% (+2.56%)
  - Geode 2.19% (+0.74%)
  - FMR 1.87% (+64.19%)
  - Vanguard PM 1.77% (+4.65%)
  - SoftBank 1.72% (持平，策略持股)
  - Primecap 1.49% (-0.67%)
- 趨勢: 前十大中多數增持，主要是指數與主動型基金。BlackRock 減持。FMR 大幅加碼是最明顯的主動型買盤訊號。

## Net sentiment score
- 分析師: 偏多 (信心中)。買方占比約 31%，持有占多數，平均評分 2.47，目標價高於現價。
- 零售: 偏多，但信心低。主要依據 AltIndex、SentiSense 與 Naga 的舊資料，沒有 2026 年 10 月的直接數據。
- 內部人: 中性偏多 (信心低至中)。CEO 有一筆金額約 $10M 的買入，但與發行相關，兩名高階主管於 5 月賣出。
- 綜合: 中性偏多 (信心低至中)。
- Divergence flag: 無法判定。零售與分析師方向目前都偏多，但零售資料時效性不足。若取得 10 月有效社群資料後方向相反，需重新評估。

限制: 快取價格為 2026-10-17 盤前數據；分析師分布與目標價為快取值；未取得個別分析師升降事件；零售面全部為間接指標。本報告不含交易建議。

Sources (次級來源，僅供方向參考):
- https://historicaloptiondata.com/?p=86245
- https://naga.com/eu/instruments/INTC.re
- https://altindex.com/ticker/intc/sentiment
- https://app.sentisense.ai/stocks/INTC/sentiment
- https://stocktwits.com/symbol/INTC
- https://newsable.asianetnews.com/markets/intel-stock-flashes-sell-signal-after-20-weekly-surge-but-retail-traders-position-for-more-gains-articleshow-6rwb41k
- https://www.tipranks.com/news/article/new-ceo-plans-intels-intc-comeback-trail
- https://chartrow.com/quote/intc/earnings
- https://247wallst.com/investing/2026/09/07/prediction-intel-stock-is-up-big-in-2026-but-the-best-may-still-be-ahead/
