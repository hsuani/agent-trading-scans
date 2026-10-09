# Sentiment — EQIX as of 2026-10-10

資料時點注意: 本機今日日期為 2026-10-09, 報告以 2026-10-10 命名。yf 快取最新 insider 紀錄至 2026-09-04, 價格參考為 2026-09-30 收盤。Reddit / StockTwits 皆無法取得, 散戶情緒部分整體為 DATA_UNAVAILABLE。

## Analyst consensus
yf rec_summary (當期): 34 家, 5 Strong Buy / 23 Buy / 6 Hold / 0 Sell / 0 Strong Sell。Buy 類合計 28 家 (約 82%), 0 家 Sell。
近 3 個月趨勢: 3 個月前為 5 / 21 / 6 (共 32 家), 買進類增加 2 家, 無賣出評等。
yf recommendations 歷史與 rec_summary 數字一致, 未列出個別升降評等事件, 故無法從 yf 取得 upgrade / downgrade 明細。

近期 target 變動 (來自次級聚合網站, 未對照券商原文):
- Evercore ISI: 2026-08-18 目標價 $1,240 → $1,270, 維持 Outperform
- RBC Capital: 2026-08-05 目標價 $1,125 → $1,225, 維持 Outperform
- HSBC: 目標價上調至 $1,400 (從 $1,250), 維持 Buy, 日期未標示
- 共識目標價: Benzinga 約 $1,137 (24 家, 頁面價格為 8 月底); stockanalysis 約 $1,234.55 (32 家)。兩者家數與日期不一致, 以區間理解。
- 2026-10 月內無找到評等變動資訊, 標示為 DATA_UNAVAILABLE。
- 參考價位: 2026-09-30 收盤約 $1,012.96, 52 週區間約 $720.62 至 $1,126.82。

## Retail social
- Reddit (r/wallstreetbets, r/stocks): DATA_UNAVAILABLE。公開 JSON 端點無法連線 (WebFetch 回報 Claude Code 無法存取 www.reddit.com), 網路搜尋亦未找到 EQIX 相關 Reddit 討論串。
- StockTwits: DATA_UNAVAILABLE。api.stocktwits.com 無法解析 (DNS 失敗), 無 bullish / bearish 標籤統計。
- X / 新聞與網路意見: 搜尋結果以交易平台與聚合頁為主, 無可驗證的散戶貼文樣本。單一交易平台 (NAGA) 頁面標示情緒為 NEGATIVE, 另有 news 多空 50/50、blogger 意見 68% 偏多等數字, 但來源單一、日期不一致, 權重極低, 不採用為結論。
- 聲量 (mention volume): DATA_UNAVAILABLE, 無法與歷史基準比較。
- 語氣傾向: DATA_UNAVAILABLE。
- 主要主題: 無足夠樣本歸納。網路聚合頁提到的疑慮為核心經常性收入 (recurring revenue) 低於分析師預期, 來源可信度低, 僅列為待查項目。

## Insider activity
yf insider 紀錄 (2026-04-10 至 2026-09-04, 約 6 個月): 公開市場買進 (open-market buy): 0 筆; 有價格的賣出合計約 $20.85M (不含 $0 贈與與無價格的股權歸屬 / 扣繳紀錄)。
Net 6mo: $0 buys, 約 $20.85M sells (淨賣出約 $20.85M)。

主要賣出者:
- Charles J. Meyers (董事): 2026-05-06, 5,224 股, 約 $5.67M
- Christopher B. Paisley (董事): 2026-08-03, 4,000 股, 約 $4.08M; 2026-08-18 另 125 股, 約 $0.14M; 2026-05-18 另 125 股, 約 $0.13M
- Brandi Galvin Morandi (Officer): 2026-06-08, 3,726 股, 約 $4.01M; 2026-04-08 另 424 股, 約 $0.43M
- Adaire Fox-Martin (CEO): 2026-06-02, 2,935 股, 約 $3.10M
- F. Abdel Raouf (Officer): 2026-05-22, 2,040 股, 約 $2.21M; 2026-06-02 另 158 股, 約 $0.17M
- Michael Shane Paladin (Officer): 2026-09-01 至 09-04 合計約 1,020 股, 約 $0.52M (其中 09-01 為無價格紀錄)
- Kurt Pletcher (Officer): 2026-08-20, 135 股, 約 $0.15M; 2026-06-02, 79 股, 約 $0.08M

CEO / CFO 觀察:
- CEO Fox-Martin 在 2026-06 有賣出紀錄, 2026-02 與 2026-03 亦有大額賣出 (2026-02-18 約 $3.95M)。
- CFO Keith David Taylor 最近一筆為 2026-02-12 與 2026-02-18 的賣出, 2026-06 至 2026-09 無紀錄。
- 2025-12 至 2026-03 期間, 多名高管於同一批日期集中賣出, 呈現與股權歸屬 / 結算週期相關的規律。此集中性使用 yf 資料無法確認是否為計畫性交易 (10b5-1) 或稅務扣繳, 需向 SEC Form 4 原文核對。
- 無 CEO / CFO 公開市場買進紀錄。

## Ownership shifts
- 機構持股比例 (yf major_holders): 100.73% (數字超過 100%, 屬資料來源重複計算的已知問題, 不宜直接解讀為集中度)。
- 內部人持股比例: 0.27%。
- 機構家數: 1,988。
- 季度變化趨勢: DATA_UNAVAILABLE (yf 僅提供當期快照, 無歷史比較)。

## Net sentiment score
Composite: 中性偏多 (neutral-to-bullish), 信心: 低 (low)。
- 分析師面: 偏多, 信心中高 (34 家中 82% Buy 類, 無 Sell, 近 3 個月買進家數增加, 近期 target 上調)。
- 內部人面: 偏空 / 中性, 信心中 (6 個月約 $20.85M 淨賣出, 0 筆公開市場買進; 但多為規律性賣出, 不能單憑此判定看空意圖)。
- 散戶面: DATA_UNAVAILABLE, 無法納入綜合評分。
- 綜合分數因散戶端完全缺資料, 實際上僅由分析師與內部人兩個訊號構成, 信心降級。

Divergence flag: 無法判定 (DATA_UNAVAILABLE)。散戶傾向缺失, 無法判斷是否與分析師偏多方向相反。若日後補到 Reddit / StockTwits 資料, 再重新評估。內部人賣出與分析師偏多的方向差異已記錄於上, 但此差異屬於內部人與外部分析師的訊號分歧, 不等同散戶與分析師的背離。

## 資料缺口與後續
1. Reddit 與 StockTwits 均無法連線, 需改用其他來源或於可連線環境重跑。
2. yf insider 最新紀錄停在 2026-09-04, 2026-09-05 至 2026-10-09 之間的 Form 4 需另行確認。
3. 分析師 target 變動來自次級網站, 建議以 Benzinga / MarketBeat 或券商原文核對。
4. 機構持股超過 100% 的資料品質問題需以 13F 加總核對。

SENTIMENT REPORT COMPLETE
