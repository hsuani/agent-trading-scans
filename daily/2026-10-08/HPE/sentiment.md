# Sentiment — HPE as of 2026-10-08

資料時點說明: yfinance 快取 (`prices/yf/HPE.json`) 刷新於 2026-10-07 13:12 UTC; 網路搜尋結果最新只到 2026-09 初 (Q3 FY26 財報後), 2026-09 中至 10-07 之間的散戶與新聞資料未取得。以下凡無法取得者標示 DATA_UNAVAILABLE。

## Analyst consensus

rec_summary (0m): 5 Strong Buy / 10 Buy / 9 Hold / 0 Sell / 0 Strong Sell (共 24 家, Buy 系 15 家, 佔 62.5%)。

近四個月評級趨勢 (Buy 系 / Hold / Sell):
- 0m (當前): 15 / 9 / 0
- -1m: 14 / 10 / 0
- -2m: 15 / 8 / 0
- -3m: 13 / 9 / 0

評級分佈穩定, 無 Sell 評級, Hold 數量在 8 至 10 之間小幅波動。

yfinance info 欄位: recommendationKey = buy, recommendationMean = 1.96 (1 為 Strong Buy), 目標價 mean 72.03 / median 70.00 / high 92.00 / low 52.59, 分析師數 21 (與 rec_summary 之 24 家略有差異, 屬不同統計口徑)。快取收盤價 70.48, 故平均目標價隱含上行空間約 +2%, 上行空間有限。

近期評級變動 (來自 WebSearch, 可靠度中等, 未經券商原文核對):
- Morgan Stanley: 2026-08-10 升評為 Overweight, 目標價由 71 降至 69 (Benzinga 摘要)。
- Citigroup: 2026-07-24 維持 Buy, 目標價由 70 升至 74。
- 6 月初目標價: Goldman Sachs 79、Loop Capital 75、Argus 70、Wells Fargo 67、UBS 65 (FN2 摘要, 部分列有舊日期資料, 可信度低)。
- yfinance 歷史評級變動明細 (recommendations 欄位僅含計數): DATA_UNAVAILABLE。
- 2026-09 至 10-07 之間的新評級變動: DATA_UNAVAILABLE。

## Retail social

- Reddit (r/wallstreetbets, r/stocks): 本次依指示僅以 WebSearch 查詢, 未取得 HPE 相關原始貼文; 搜尋未回傳 r/wallstreetbets 或 r/stocks 的 HPE 討論串。直接 Reddit JSON 查詢: DATA_UNAVAILABLE。
- Reddit 相關指標 (第三方追蹤器, 日期不明): SentiSense 顯示 Reddit 為唯一偏空來源, 約佔提及量 19% 偏空; AltIndex 綜合分數 75/100 (Bullish), 但標示近期較 30 日均值轉弱。
- StockTwits: 即時讀數 DATA_UNAVAILABLE。最近可得快照為 2026-03-05 財測偏弱當日, 散戶情緒由 bullish 轉為 extremely bullish (屬 7 個月前資料, 僅供參考)。
- X / 新聞散戶語氣: 搜尋未取得 2026-09 後的 X 貼文摘要, DATA_UNAVAILABLE。
- 選擇權流向: 2026-03-25 MarketBeat 指出散戶 call 買盤異常放大 (約 4.3 萬張, 較常態高約 71%); 2026-06 一篇選擇權文章的 call 與 put 美元成交量約 9.7 萬美元對 1.8 萬美元 (樣本小)。
- 聲量 (buzz volume): 無量化數據 DATA_UNAVAILABLE。定性判斷: 2026-09 初 Q3 財報前後應有明顯升溫, 但無實際提及次數可比對。

Themes (由新聞與追蹤器彙整, 非直接引述散戶貼文):
- 正面: Q3 FY26 營收年增 34% 至 $12.2B, non-GAAP EPS $1.11 (+66%); FY26 營收成長指引上調至 34%–37%; 創紀錄 AI 訂單積壓 $7.9B; 與 Oracle 合作在其 AI 資料中心部署 HPE Juniper 網路。
- 負面: 管理層警示 Q4 與 FY27 毛利率與營業利益率將因 AI 系統比重提高而下滑; 盤中曾跌近 12% 後收漲 5%, 顯示多空分歧; 內部人高檔賣出 (見下節)。
- 情緒訊號: 散戶對成長與 AI 題材偏多, 但對利潤率稀釋的擔憂未見直接討論樣本 (DATA_UNAVAILABLE)。
- 無法摘錄代表性貼文原文 (未取得 Reddit / StockTwits 原文)。

## Insider activity

Net 6mo (2026-04-08 至 2026-10-08, 公開市場交易, 依 yfinance insider 欄位彙整):
- 買入: $0 (無公開市場買進紀錄)
- 賣出: 約 $29.4M (10 筆 Sale 交易)
- 不計入的非公開市場項目: 衍生性證券行使 (conversion)、股票贈與 (gift)、董事股票獎勵 (grant)

主要交易:
- Antonio F. Neri, CEO: 2026-09-11 賣出 250,000 股 @ $60.44 (約 $15.1M); 2026-04-17 賣出 150,000 股 @ $26.50 (約 $4.0M)。另 2026-05-01 贈與 1,682,393 股 (非賣出)。
- Marie Elizabeth Myers, CFO: 2026-05-05 賣出 93,583 股 @ $30.01 (約 $2.8M)。
- Rami Rami, Officer: 2026-09-29 賣出 34,456 股 @ $61.42 (約 $2.1M); 2026-07-02 衍生性證券行使 1,122,365 股 @ $41.23, 7-07 贈與 655,427 股 (行使後是否出售未見公開紀錄)。
- Gary M. Reiner, Director: 2026-09-14 賣出 17,000 股 @ $56.91 (約 $1.0M); 2026-06-03 賣出 20,000 股 @ $54.77 (約 $1.1M)。
- Kirt P. Karros, Officer and Treasurer: 2026-07-22 賣出 23,675 股 @ $47.02; 2026-06-22 賣出 18,785 股 @ $48.50。
- Russo Fidelma (CTO) 2026-04-21 賣出 17,001 股 @ $27.97; Mayer Bethany J (Director) 2026-05-05 賣出 6,482 股 @ $29.10; MacDonald Neil B (Officer) 2026-04-20 賣出 24,251 股 @ $27.01。

觀察:
- 高階主管 (CEO / CFO / CTO) 與多數董事皆有賣出, 買入紀錄為零。
- 9 月的 CEO 大額賣出 (約 $15.1M) 為近期最大單筆, 價位在 $60 附近, 高於 4 月的 $26.50 賣價。
- 10b5-1 交易計畫標記: DATA_UNAVAILABLE (快取欄位未提供), 無法判斷是否為預先排定之賣出。
- 內部人持股比例 0.37% (yfinance major_holders), 持股基數小, 賣出佔比對持股影響有限。

## Ownership shifts

- 機構持股比例 91.2%, 機構數 1,948 家; 內部人持股 0.37%; 做空比例 (short % of float) 4.8% (快取 info)。
- 前十大持有人 (截至 2026-06-30, pctChange 為較前期變化):
  - BlackRock 10.1% (-6.8%)
  - Vanguard Capital Management 6.5% (+0.4%)
  - Vanguard Portfolio Management 5.5% (-1.5%)
  - State Street 5.1% (+0.6%)
  - Capital World Investors 4.5% (+1.6%)
  - JPMorgan Chase 3.0% (-26.6%)
  - Bank of America 3.0% (-46.7%)
  - Geode Capital 2.8% (+1.9%)
  - Elliott Investment Management 2.4% (+17.7%)
  - Goldman Sachs Group 1.9% (+44.1%)
- 趨勢判讀: 被動指數基金持股大致持平; 主動型與對沖型資金出現分化, Elliott 與 Goldman 增持, JPMorgan 與 Bank of America 大幅減持 (減持可能與做市或避險部位有關, 無法由此資料確認)。
- 季度持股變化的完整時間序列: DATA_UNAVAILABLE (僅有單期快照)。

## Net sentiment score

Composite: NEUTRAL (信心度: 低至中)

分項判讀:
- 分析師: 偏多 (信心度中高)。評級穩定, 0 Sell, Buy 系佔 62.5%, 但平均目標價僅較快取收盤價高約 2%, 上行空間有限。
- 內部人: 偏空 (信心度中)。6 個月淨賣出約 $29.4M, 買入為零, 且多為高階主管。需注意股價自 $26 至 $60 區間大幅上漲後, 主管賣出可能屬獲利了結與既定交易計畫, 未必反映對基本面的看法。
- 散戶: 無法確認 (信心度低)。Reddit、StockTwits、X 即時資料皆 DATA_UNAVAILABLE; 僅有 2026-03 至 2026-06 的第三方快照, 偏多 (AltIndex 75/100, StockTwits 3 月 extremely bullish), 但 SentiSense 顯示 Reddit 為偏空來源。
- 機構: 中性偏多 (持股比例高, 增減持分化)。

Divergence flag: 是 (部分)
- 散戶 vs 分析師: 無法確認, 因散戶即時資料缺失; 若以第三方快照看, 兩者方向大致一致 (偏多)。
- 內部人 vs 分析師: 有分歧。分析師全面維持 Buy 系, 內部人持續賣出且無買進。此分歧值得在後續分析中留意。

資料缺口摘要 (DATA_UNAVAILABLE):
- Reddit 直接貼文與提及量
- StockTwits 即時情緒
- X 即時討論
- yfinance 歷史評級變動明細
- 2026-09 中至 10-07 之間的新聞與評級變動
- 內部人交易的 10b5-1 標記
- 季度機構持股時間序列

注意: 本報告為情緒彙整, 不含交易建議。

SENTIMENT REPORT COMPLETE
