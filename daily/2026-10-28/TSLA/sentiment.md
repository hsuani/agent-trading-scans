# Sentiment — TSLA as of 2026-10-28

資料來源與時點說明: 分析師評等與內部人交易來自 `pipeline/tools/yf` (部分欄位為 cache 回退, 屬正常)。Reddit 與 StockTwits 直接抓取未使用 (依任務指示以 WebSearch 取代), 搜尋結果多為無日期或舊文, 已逐項標註。2026-10-28 之後的資料一律視為未知。

## Analyst consensus

| 評等 | 目前 (0m) | -1m | -2m | -3m |
|---|---|---|---|---|
| Strong Buy | 5 | 4 | 6 | 6 |
| Buy | 14 | 15 | 16 | 17 |
| Hold | 22 | 21 | 20 | 19 |
| Sell | 2 | 2 | 3 | 4 |
| Strong Sell | 0 | 2 | 2 | 2 |
| 合計 | 43 | 44 | 47 | 48 |

目前分布: 19 buy / 22 hold / 2 sell (Strong Buy 與 Buy 合計 19, 佔 44%; Hold 佔 51%; Sell 合計 2, 佔 5%)。

近三個月趨勢: 買進端由 23 家降至 19 家, Hold 由 19 家升至 22 家, 賣方評等由 6 家降至 2 家。整體屬於「評等往 Hold 集中、賣出評等減少」, 不是明顯上調或下調。

目標價: 
- cache info 欄位 (refreshed 2026-10-28 12:41 UTC): targetMeanPrice 410.68 USD, targetHighPrice 600.00 USD, targetLowPrice 128.11 USD, numberOfAnalystOpinions 39 (與評等表 43 家略有差異, 來源口徑不同)。
- Fintel 搜尋摘要 (10 月初, 第三方): 平均一年目標價約 383.06 USD。
- 個別升降評等事件 (upgrade/downgrade 日期與券商): DATA_UNAVAILABLE (yf recommendations 工具僅回傳月度彙總, 未回傳逐筆事件)。
- 目標價逐筆修正歷史: DATA_UNAVAILABLE。

## Retail social

- Reddit (r/wallstreetbets, r/stocks): DATA_UNAVAILABLE。WebSearch 僅回傳 Benzinga 舊文 (無 2026 日期), 無法確認 10 月的討論量與多空傾向。
- StockTwits: 搜尋摘要中一頁顯示 sentiment 67/100 (標示 Neutral), 但該頁無日期, 不能當作 10/28 讀數。另一篇 StockTwits 文章標題指出股價重返兆美元俱樂部但情緒偏空, 圖表日期為 Nov 8, 時點不明, 不採用。整體 StockTwits 情緒: 中性, 信心低。
- X / 新聞輿情: 10 月 21 日股價上漲約 3.4% 至 386.47 USD (搜尋摘要, 來源 heygotrade), 摘要指出與 Elon Musk 揭露 SpaceX 與 Tesla 各自成立董事會委員會研究可能合併相關。此為新聞面主題, 散戶討論熱度無法量化。
- Historical Option Data (9 月分析, 已過時): 選擇權流向偏平衡, 整體略偏多, 信心中等; X 情緒描述為混合。
- SentiSense (2026-08-09, 已過時): 30 日情緒分數 -11.09, Bearish, 趨勢降溫。
- 討論量: DATA_UNAVAILABLE (無可靠的 10 月提及次數)。以新聞量與股價波動推估屬偏高, 但無數值依據, 不作量化結論。

Themes (依搜尋摘要歸納, 信心低):
1. 與 SpaceX 的合併可能性 (董事會委員會), 為近期最明顯的新聞主題。
2. 第二代 Roadster 發表會由 10/1 延至 10/15 (搜尋摘要, 未確認實際發表內容)。
3. Q3 2026 財報: 營收約 28.0B USD, 年增約持平; 自由現金流約 1.5B USD (搜尋摘要引用 Q3 Update, 未直接驗證原始 SEC 文件)。
4. 技術面: Tickeron 指 MACD 於 10/06 轉正 (模型輸出, 非獨立驗證)。

## Insider activity

視窗: 2026-04-28 至 2026-10-28。

Net 6mo: 公開市場買進 0 USD; 公開市場賣出約 13.3M USD (約 0.0133B USD)。

| 日期 | 人員 | 職位 | 類型 | 股數 | 金額 (M USD) |
|---|---|---|---|---|---|
| 2026-04-30 | Kathleen Wilson-Thompson | Director | 賣出 (369.01–384.28) | 26,409 | 9.99 |
| 2026-05-13 | Vaibhav Taneja | CFO | 賣出 (450.00) | 3,000 | 1.35 |
| 2026-06-08 | Vaibhav Taneja | CFO | 賣出 (402.20) | 2,605 | 1.05 |
| 2026-09-08 | Vaibhav Taneja | CFO | 賣出 (360.13) | 2,605 | 0.94 |

衍生性工具轉換 (非現金買入, 不計入淨買賣):
- 2026-06-16 Elon Musk (CEO): 選擇權行權 (23.34 USD/股), 303,960,630 股, 名目約 7.09B USD。工具輸出未見同期賣出紀錄, 但需注意名目金額龐大。
- 2026-05-13 Taneja (CFO): 行權 3,000 股, 約 0.05M USD。
- 2026-04-30 Wilson-Thompson (Director): 行權 40,948 股, 約 0.61M USD。

重點觀察:
- 近六個月無任何 CEO 或董事的公開市場買進。
- 賣出金額以 Director Wilson-Thompson 為最大 (約 10.0M USD), CFO Taneja 為連續多筆小額賣出 (合計約 3.3M USD)。
- 有數筆 Taneja 交易 Value 欄位為空 (2026-03-05、06-05、09-04 等, 每次約 6,538 股), 性質未知 (疑似例行權益分配或稅務扣繳), 未計入金額。
- 歷史上 CEO 與部分董事曾有大額 Gift 與權益行權, 超出本視窗, 不納入計算。

## Ownership shifts

- 內部人持股比例: 17.8% (insidersPercentHeld)。
- 機構持股比例: 43.7%; 流通股機構持股: 53.2%; 機構數量: 5,293 家。
- 前五大機構 (2026-06-30 申報, cache): BlackRock 5.42% (較前期 +2.9%)、Vanguard Capital Management 4.66% (+0.6%)、State Street 2.97% (+2.4%)、Geode 1.74% (+1.3%)、Invesco 1.40% (+1.1%)。前五大皆為增持。
- 機構持股趨勢的多期比較: DATA_UNAVAILABLE (工具僅提供單期快照與單期變動)。

## Net sentiment score

Composite: **中性偏空 (信心: 低)**

| 來源 | 傾向 | 信心 | 依據 |
|---|---|---|---|
| 分析師 | 中性 (Hold 主導, 買進端減少) | 中 | 19 buy / 22 hold / 2 sell, 賣方評等減少 |
| 內部人 | 偏空 | 中 | 6 個月約 13.3M USD 賣出, 0 買進 |
| 散戶 / 社群 | 中性 | 低 | StockTwits 67/100 但無日期; Reddit 無 2026 資料 |
| 新聞面 | 混合 | 低 | SpaceX 合併可能性與股價反彈 |

評分理由: 分析師端無明顯偏空, 但評等結構轉向 Hold; 內部人端無買進且有持續賣出, 支持偏空; 散戶端資料不足。整體定為中性偏空, 信心低, 主要因社群資料缺口。

Divergence flag: **否** (散戶 vs 分析師: 散戶資料不足無法判定方向, 兩者皆非明顯對立)。
補充: **是** (內部人 vs 分析師): 分析師為 Hold 主導且賣方減少, 內部人則持續賣出且無買進, 方向不一致, 值得後續追蹤。

資料缺口: Reddit 2026 討論量與傾向 (DATA_UNAVAILABLE)、個別升降評等事件 (DATA_UNAVAILABLE)、目標價逐筆修正 (DATA_UNAVAILABLE)、StockTwits 10/28 當日讀數 (DATA_UNAVAILABLE)、機構持股多期趨勢 (DATA_UNAVAILABLE)。

SENTIMENT REPORT COMPLETE
