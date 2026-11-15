# Sentiment — 3661.TW (世芯-KY, Alchip Technologies) as of 2026-11-16

## Analyst consensus
Yahoo rec_summary: 6 strongBuy / 9 buy / 1 hold / 0 sell (共 16 家，全部期間數字相同)。
Investing.com 摘要: 15 buy / 1 hold / 0 sell，共同結論 "Strong Buy"。

最近動態:
- yf recommendations 回溯 4 個月，評等分布完全沒有變化，無可見升降評。這可能代表資料未更新，或期間內無評等變動，需以券商報告為準。
- 目標價: 一家外資維持「加碼」評等，目標價 NT$5,888 不變；另一家上修未來兩年獲利預估、維持「買進」，目標價由先前水準調整為 NT$6,000。JPMorgan Buy，目標價 NT$6,000，日期標示 2026-11-05 (來源為 Investing.com UK 頁面)。
- 資料不一致: Investing.com 平均目標價 NT$3,755 (15 家) 明顯低於近期個別目標價 NT$5,888–6,000，疑為過時數字，不採信為現況。

## Retail social
- Reddit (r/stocks、r/wallstreetbets): 無法取得。WebFetch 回傳 "unable to fetch"，此來源跳過。
- StockTwits: 無法取得。api.stocktwits.com 無法解析 (DNS 失敗)，需於 session 網路設定中放行才能使用。此來源跳過。
- PTT 股板 / CMoney 社群: 直接存取受限。以搜尋間接取得: CMoney 股市爬蟲頁顯示「目前沒有任何討論」，但摘錄的留言提到融資壓力可能拖累股價，也有人期待外資買超帶動短線拉升。留言時間與可信度無法確認。
- X / 新聞鏈: 以 WebSearch 取得，主要是營收與法人評等新聞，非散戶原始貼文。
- 討論量 (qualitative): 新聞量高 (每月營收公告、外資報告均有媒體跟進)，但論壇原始貼文量偏低、難以量化。以「討論量低於新聞量」描述，無可靠的提及次數。
- 情緒傾向: 偏謹慎至中性，資料薄弱，信心低。

Themes (依搜尋到的媒體與論壇內容歸納):
1. 營收高速成長: 2026 年 8 月單月營收 NT$87.76億 (年增 273.61%，為歷史單月新高)；10 月營收 NT$102.60億 (月增 2.8%、年增 515.8%)；1–10 月累計 NT$480.60億 (年增 72.6%)。
2. AWS Trainium 3 量產與第二家美國大型客戶: 外資指出客戶進度比預期提前，預估 2027 年營收可能翻倍。
3. 客戶集中與訂單分食疑慮: 2026 年 9 月 Qualcomm 與 AWS 宣布長期客製化 AI 晶片合作，市場擔心世芯訂單被分食。
4. 產能瓶頸: 董事長提到晶圓、載板與封裝產能短缺，限制營收上限。
5. 融資與籌碼: 論壇提及融資壓力與股價波動風險。

## Insider activity
Net 6mo: 資料不足。yf insider 回傳空陣列 `[]`，無法區分「無交易」與「資料缺漏」，因此不推定淨買或淨賣。
Notable: 無可驗證資料。

Ownership 快照 (yf major_holders):
- 內部人持股 3.13%
- 機構持股 39.04% (流通股 40.30%)，機構家數 257
- inst_holders 回傳空陣列，無法判斷機構持股趨勢。只有單一時點快照，無法判斷集中度變化方向。

## Price / fundamentals cross-check (僅供情緒解讀)
- 股價資料不一致: TradingView 顯示 NT$3,630 (日跌 −2.29%)；其他頁面報價介於 NT$3,765–4,900；歷史高點 NT$5,640 (2026-05-12)。無可靠的 2026-11-16 收盤價。
- 營收數據已交叉驗證: 2025 年 1–11 月累計 NT$295.40億，扣除 2025 年 11 月 NT$16.98億後，2025 年 1–10 月約 NT$278.4億，與 2026 年 1–10 月 NT$480.60億 的年增 72.6% 吻合。

## Net sentiment score
Composite: **bullish (信心: 中低)**
- 分析師面: 強烈偏多，16 家中 15 家為買進 (含強力買進)，0 家賣出。
- 散戶面: 偏謹慎至中性，資料薄弱 (Reddit、StockTwits、PTT 皆無法直接取得)。
- 內部人面: 無資料，不計入評分。
- 籌碼面: 機構持股 39% 為中性指標，無趨勢資料。

信心偏低的原因: (1) 散戶來源缺失，只能用媒體與少量論壇內容推估；(2) 股價資料互相矛盾；(3) 評等歷史疑似未更新；(4) 內部人交易無資料。

Divergence flag: **yes (低信心)** — 分析師明顯偏多，散戶/論壇語氣偏謹慎 (融資壓力、客戶集中疑慮)。此分歧需以更完整的散戶資料確認後才能採信，目前僅能視為方向性訊號。

資料缺口 (建議後續補足):
- 放行 api.stocktwits.com 後重新抓取 StockTwits 訊息流。
- 以 PTT 股板 (Stock) 直接搜尋「世芯」或「3661」，取得實際貼文與多空比例。
- 確認 yf insider 空陣列是否為真正無交易，或另以 TWSE 內部人申報資料交叉核對。
- 以 TWSE 即時行情確認 2026-11-16 收盤價，修正目標價與股價的比較基準。

## Sources (WebSearch / WebFetch)
- [Investing.com: Alchip consensus](https://www.investing.com/equities/alchip-technologies-ltd-consensus-estimates)
- [Investing.com UK: Alchip consensus](https://uk.investing.com/equities/alchip-technologies-ltd-consensus-estimates)
- [TradingView: TWSE 3661](https://www.tradingview.com/symbols/TWSE-3661/)
- [中時 wantrich: 2026-11-09 外資報告](https://wantrich.chinatimes.com/news/20261109900111-420101)
- [優分析 uanalyze: 法說會摘要](https://uanalyze.com.tw/articles/5791058627)
- [nStock: 世芯-KY 概況](https://nstock.tw/世芯-KY做什麼.html)
- [TechNews: 2026 年 10 月營收](https://finance.technews.tw/2026/11/10/alchip-3661-202610-financial-report/)
- [TechNews: 2025 年 11 月營收](https://finance.technews.tw/2025/12/10/alchip-3661-202511-financial-report/)
- [CMoney 股市 3661 討論區](https://www.cmoney.tw/forum/stock/3661)

SENTIMENT REPORT COMPLETE
