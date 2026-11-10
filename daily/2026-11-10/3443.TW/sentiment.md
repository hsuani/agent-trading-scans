# Sentiment — 3443.TW 創意電子 (Global Unichip Corp) as of 2026-11-10

> 資料品質註記: yf 工具回傳為快取資料 (Yahoo cookie/crumb 取得失敗), 快取時間戳不明。Reddit 與 StockTwits 無法取得, 網頁搜尋結果的日期多數無法確認, 且股價數字在各來源之間差距極大。以下判讀以「可確認的方向」為主, 不以單一數字做結論。

## Analyst consensus

截至快取日, 共 19 位分析師: **6 Strong Buy / 13 Buy / 0 Hold / 0 Sell / 0 Strong Sell** (yf rec_summary, 0m 期)。

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell |
|---|---|---|---|---|---|
| 0m (當前快取) | 6 | 13 | 0 | 0 | 0 |
| -1m | 6 | 13 | 0 | 0 | 0 |
| -2m | 6 | 13 | 0 | 0 | 0 |
| -3m | 6 | 12 | 0 | 0 | 0 |

- 近三個月評等結構幾乎不變, 僅 -3m 時 Buy 少一家 (12 → 13), 屬於單家分析師的增加, 沒有評等下修。
- yf 的 `recommendations` 歷史端點回傳與 rec_summary 相同的彙總表, 沒有個別券商的升降評逐筆紀錄, 因此「近期升評/降評」的個別事件無法從結構化資料確認。
- 目標價: 網頁搜尋 (非結構化、日期不明) 顯示多家券商目標價差異極大, 可確認的僅為:
  - 里昂 (CLSA): 目標價由 3,600 元上調至 6,000 元 (上調 66.6%), 維持「優於大盤」, 並上調 2026 EPS 預估 8%、2027 預估 30%, 理由為 CPU 需求高於預期 (日期未確認, 但為搜尋結果中最明確的一筆近期調整)。
  - 大和資本: 買進, 目標價由 2,450 元上調至 2,920 元 (日期未確認)。
  - 其他舊報導 (摩根士丹利 3,288 元、花旗 2,725 元) 日期不明, 不採計為現況。
  - 其餘來源 (investing.com 平均目標價 約 6,922 元、Stockopedia 共識目標價 約 3,114 元、simplywall.st 約 1,723 元) 數字彼此矛盾, 判定為 **無法統一, 標記 DATA_UNAVAILABLE**。
- 投顧 (本土) 有喊 9,360 元目標價之新聞標題 (約 11/2), 屬單一極端值, 不納入共識。

## Retail social

- **Reddit (r/wallstreetbets, r/stocks)**: DATA_UNAVAILABLE。WebFetch 對 reddit.com 回傳封鎖, 無法取得貼文數與情緒。
- **StockTwits**: DATA_UNAVAILABLE。api.stocktwits.com DNS 解析失敗 (沙箱網域未允許), 未重試。
- **X / 論壇 (經 WebSearch)**:
  - CMoney 股市討論區彙整頁 (無日期): 同時出現悲觀 (股價走弱、成交量縮小) 與樂觀 (AI 與高階記憶體需求推升) 的看法, 無法判定是否為 2026-11 的貼文。
  - PTT Stock 與 Dcard 未在搜尋結果中找到當月可讀貼文, 無法引述。
- **聲量 (buzz volume)**: 無法以數字量化。網頁新聞量顯示 2026 年內股價大幅波動 (盤中單日漲逾 7%、單日收漲約 10% 的報導皆有), 媒體關注度高, 但這是新聞量, 不等於散戶討論量。
- **Retail tilt**: 無法可靠判定。僅有的可讀訊號為「營運成長強、估值高、波動大」之混合論述。

### 主要論述主題 (來自新聞與彙整頁, 非散戶原文)
1. **營收高速成長**: 2026 年 6 月單月營收 49.29 億元, 年增 103.72%; 8 月 58.4 億元, 年增 111%; 10 月 37.16 億元, 年增 150.6% (單月數字之間有波動, 以月為單位觀察)。2025 全年營收 341.4 億元, 年增 36.3%。
2. **CPU / CSP 客戶題材**: 外資認為最大 CSP 客戶的下一代雙晶粒 CPU 專案於 2026 年底起貢獻營收, 2027 年放量更明顯。
3. **估值與波動疑慮**: 本益比與股價漲幅被部分評論視為短線震盪風險。
4. **毛利率下滑**: nStock 資料顯示 2026 Q2 EPS 11.61 元、毛利率 21.55%, 較 Q1 下滑。

## Insider activity

Net 6mo: DATA_UNAVAILABLE。yf insider 端點回傳空陣列, 無法區分「無申報」與「資料缺漏」, 因此不以「零交易」判定。

Notable: 無可確認之董監事或經理人申報紀錄。

## Ownership shifts

- 內部人持股 (insidersPercentHeld): 36.68%
- 機構持股 (institutionsPercentHeld): 33.91%; 占流通股 (float) 53.56%
- 機構數量: 229 家
- 趨勢 (季/年變化): DATA_UNAVAILABLE。快取僅單一時點, 無法判斷集中度是升或降。

## Net sentiment score

- **分析師面 (可確認)**: 偏多 (bullish)。19 家中 19 家為 Buy 或 Strong Buy, 0 家 Hold 以下, 近三個月無下修; 里昂最新上調目標價。信心: 中-高 (評等結構明確, 但目標價分歧大, 且日期不明)。
- **散戶面**: 無法判定 (Reddit、StockTwits 不可得; 網頁論壇內容無日期、混合)。信心: 低。
- **內部人面**: DATA_UNAVAILABLE, 不計分。
- **綜合**: **偏多 (bullish), 信心中等偏低**。主要由分析師一致買進支撐; 散戶與內部人面缺資料, 綜合判斷的可靠度受限。

**Divergence flag: 無法判定 (no determination)**。散戶 tilt 不可得, 因此無法確認是否與分析師方向相反。若日後補上 Reddit / StockTwits 資料, 再重新判定。

## 資料缺口與後續建議

1. 取得 yf 快取時間戳與個別券商評等逐筆紀錄 (recommendations 端點需 Yahoo cookie/crumb, 目前失敗)。
2. 允許 api.stocktwits.com 網域後重試 StockTwits。
3. Reddit 需另尋可用來源 (目前 WebFetch 被封鎖)。
4. 目前股價在各來源之間差距極大 (約 1,700 元至 8,000 元以上), 本報告未採用任何單一股價, 需以即時行情另行確認。

SENTIMENT REPORT COMPLETE
