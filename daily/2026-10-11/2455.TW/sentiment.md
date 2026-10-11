# Sentiment — 2455.TW (全新光電) as of 2026-10-11

## Analyst consensus
yfinance rec_summary (period 0m): 11 家 — 3 strongBuy / 7 buy / 1 hold / 0 sell / 0 strongSell，即 10 買進、1 持有、0 賣出（買進比例約 91%）。
- 前兩期（-1m）結構相同（3/7/1/0/0）；-2m 為 3/6/1/0/0，即 1 個月前後多一家 buy，屬小幅變動，無實質評等下修。
- 注意：yf 工具的 `recommendations` 指令回傳與 `rec_summary` 完全相同的彙總計數，**未提供歷史個別評等變動明細**，因此「近期 upgrade/downgrade 清單」標記為 DATA_UNAVAILABLE。
- yf 未提供 rec_summary 的資料截止日期，無法確認是否為 2026-10-11 當下數字，請以此理解為「快照」。
- 網路檢索（WebSearch，非 yf）可見的個別券商評等（資料日期較早，未能驗證 2026-10 的最新狀態）：
  - 亞系外資（2026-06-16）：優於大盤表現，目標價 465 元；預估 2026/2027/2028 EPS 分別為 6.04 / 11.62 / 16.69 元；認為砷化鎵、磷化銦磊晶圓漲價有助利潤率回升。
  - 美系外資（2026-05-04）：持股續抱，目標價由 200 上調至 290 元，理由為 AI 資料中心營收較高，獲利預估上修 4% / 11% / 25%（2026/2027/2028）。
  - 澳系外資（2025-11）：優於大盤表現，目標價 236 元（較早報告）。
- 目標價變動方向：多數可見目標價為上修（200→290、236→465），但時間點不一，無法構成完整的 2026-10 目標價分布。

## Retail social
- Reddit（r/stocks、r/wallstreetbets）：DATA_UNAVAILABLE — WebFetch 無法連線 www.reddit.com；且台股個股在這兩個版的討論量預期本來就低。
- StockTwits：DATA_UNAVAILABLE — api.stocktwits.com 無法解析（ENOTFOUND），且 StockTwits 對台股覆蓋有限。
- PTT Stock / Dcard：WebSearch 未找到相關討論串（檢索結果未能直接取得 PTT/Dcard 內容），標記為 DATA_UNAVAILABLE。
- 新聞與財經媒體（代理指標，非純散戶）：
  - 2026-06 中：全新宣布自 6 月起調漲砷化鎵與磷化銦磊晶圓價格（雙位數漲幅），當日股價漲停收盤（來源：中時 wantrich 報導）。
  - 2026-01 月營收 3.40 億元，月增 6.6%、年增 30.3%。
  - 與日本光通訊大廠合作矽光子（Silicon Photonics）項目，市場以此作為 AI 資料中心題材。
  - 2026-Q1 稅後盈餘 1.95 億元，年增 24.03%，單季 EPS 1.06 元；公司指出基板短缺為主要挑戰。
- 聲量（buzz volume）：無可靠的提及次數量化資料，定性判斷為「題材型熱度」，主要集中於新聞媒體與財經入口網站，而非社群論壇。
- 股價資料來源彼此不一致（各頁面時點不同：388、556、353、397 元），**不採用為本報告的價格基準**。

- Themes（主題）：
  1. AI 資料中心 / 矽光子（看多）
  2. 砷化鎵、磷化銦磊晶圓漲價帶動毛利（看多）
  3. 手機 PA 需求疲弱、基板短缺（風險）
  4. 獲利能見度（Q1 年增、2026-2028 EPS 上修）（看多）

- 散戶語氣：DATA_UNAVAILABLE 為主；從媒體與題材文章的語氣推估偏多，但這是媒體立場，不應等同於散戶情緒。

## Insider activity
Net 6mo: DATA_UNAVAILABLE。
- yf `insider` 指令回傳空陣列 `[]`，無法區分「真的沒有交易」與「台股董監事申報不在 yfinance 覆蓋範圍」，因此不能推論為零交易。
- WebSearch 未取得 2026 年董監事持股申報、增減持數字。
- 公開資訊觀測站（MOPS）的「董事、監察人持股異動申報」為權威來源，需人工或另行抓取確認。
- Notable: DATA_UNAVAILABLE

## Ownership shifts
- yf major_holders（單一快照，無時間序列）：
  - 內部人持股（insidersPercentHeld）：5.17%
  - 機構持股（institutionsPercentHeld）：31.43%；流通股中機構占比（institutionsFloatPercentHeld）：33.14%
  - 機構數：65
- 持股集中度的時間趨勢（季度變化）：DATA_UNAVAILABLE（僅有單點資料）。

## Net sentiment score
Composite: **偏多（bullish），信心：低（low）**

依據：
- 分析師端偏多：10 買 / 1 持有 / 0 賣，目標價方向以上修為主（權重高，但資料時點不明）。
- 媒體與題材端偏多：漲價、AI/矽光子題材、獲利上修。
- 散戶端（Reddit / StockTwits / PTT / Dcard）：全部 DATA_UNAVAILABLE，無法驗證。
- 內部人端：DATA_UNAVAILABLE，無法判斷方向。
- 信心降低原因：散戶與內部人兩個關鍵維度缺失；分析師評等快照無日期；股價資料來源互相矛盾；WebSearch 結果多為 2026-06 之前的資料。

Divergence flag: **無法判定（DATA_UNAVAILABLE）** — 散戶語氣資料缺失，無法比對是否與分析師傾向相反。

## Data gaps
- Reddit、StockTwits、PTT、Dcard：連線失敗或無法取得
- yf insider：空回傳
- yf recommendations：無歷史明細，與 rec_summary 相同
- yf 無資料日期標記；Yahoo cookie/crumb 取得失敗（ConnectionError），以無 crumb 方式回傳
- 機構持股無時間序列

SENTIMENT REPORT COMPLETE
