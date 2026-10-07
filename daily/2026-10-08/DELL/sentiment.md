# Sentiment — DELL as of 2026-10-08

資料時點說明: yf 即時來源被阻擋 (Yahoo cookie/crumb ConnectionError), 本報告使用 `prices/yf/DELL.json` 快取 (`_refreshed_at` 2026-10-07 13:11 UTC)。股價 574.00 為快取值, 非 2026-10-08 收盤價。Reddit 與 StockTwits 經 proxy 阻擋, 社群部分無法取得直接資料。

## Analyst consensus
快取 rec_summary (0m): 6 Strong Buy / 14 Buy / 9 Hold / 0 Sell / 0 Strong Sell (合計 29 家)。Buy 類佔 69%, Hold 佔 31%, 無賣出評等。
- 近 3 個月趨勢: Strong Buy 由 5 增至 6, Hold 由 8 增至 9, Buy 維持 14, Sell 維持 0。
- 注意: info 欄位 `numberOfAnalystOpinions` 為 25, 與 rec_summary 合計 29 不一致, 可能是統計口徑不同 (例如含 Strong Buy 與否或期間差異), 未能確認。
- 目標價 (快取 info): 平均 585.96, 最高 735.00, 最低 480.00。相對 574.00 的平均目標隱含約 +2.1%。recommendationKey = buy。
- Fintel 彙整 (9/2 前後): 平均一年期目標由 511.05 (8/25) 上修至 582.33 (+13.95%), 區間 469.65 至 735.00。

近期評等異動 (網路來源, 非 yf 逐筆):
- 5/29 Susquehanna 由 Neutral 升至 Positive (Nasdaq / Fintel)。
- 6/1 Morgan Stanley 升評 (StreetInsider 記載, 目標 477, 各來源時間與目標價不一致, 需保留疑慮)。
- 6/25 GF Securities 由 Buy 降至 Hold。
- 9/9 Evercore ISI 維持 Outperform。
- 9/10 RBC Capital 首次給予 Outperform。
- 逐筆評等異動清單 (yf `recommendations` 僅含彙總counts): DATA_UNAVAILABLE。

## Retail social
- Reddit (r/wallstreetbets, r/stocks): DATA_UNAVAILABLE。WebFetch 回應 "unable to fetch from www.reddit.com"。
- StockTwits: DATA_UNAVAILABLE。proxy 回應 EGRESS_BLOCKED (api.stocktwits.com)。
- X / 新聞討論: WebSearch 未找到 2026-10 的散戶情緒資料。搜尋結果多為 2026 年初至 9 月的分析文章, 以及疑似自動生成的低品質頁面 (已排除)。
- 選擇權情緒 (historicaloptiondata.com, 弱參考): 4 月偏空 (put 約 92%), 6 月偏空 (put 約 64%), 8 月底轉為偏多 (call 約 79.5%)。來源數字彼此不完全一致, 僅供方向參考。
- 聲量 (buzz volume) 相對基準: DATA_UNAVAILABLE。
- 主要主題 (從新聞與分析文章歸納, 非直接散戶貼文):
  - AI 伺服器成長: 有來源指 FY2027 AI 伺服器營收約 500 億美元 (+103%), AI 伺服器客戶逾 4,000 家 (二手來源, 未核實)。
  - 9/1 財報超預期: EPS 7.04 vs 預估約 5.01; 營收約 469.7 億美元 vs 預估約 458.1 億美元。
  - 估值與預期過高: 一篇文章標題指股價 3 個月上漲 84%, 評論認為預期已拉高、容錯空間低。
  - 毛利與記憶體成本: 分析師原預期毛利受記憶體成本壓縮, 實際表現優於預期。
  - PC 業務循環性: 企業 IT 支出放緩的下行風險。
  - 散戶報價語氣: 「AI 贏家」與「交易動能驅動」兩派並存。

## Insider activity
資料覆蓋範圍: 快取 insider 紀錄僅涵蓋 2026-06-10 至 2026-09-24 (共 150 筆)。6 個月窗口 (2026-04-08 至 2026-10-08) 中 4/8 至 6/9 無資料, 淨額為部分期間結果。

Net 6mo (可取得期間): 公開市場買入 $0 (快取無 Purchase 紀錄)。賣出合計約 $1.03B:
- Silver Lake 關係實體 (10% 股東 / 董事關聯, 66 筆): 約 $939.7M。主要於 6 月至 9 月分批出售, 成交價區間約 370 至 591 美元, 9/17 區間 577.60–591.24。
- 高管與董事 (12 筆 sale): 約 $89.6M。
  - Trizzino Peter (Officer): 9/11, 37,735 股, 約 $21.1M, 價格 560.16。
  - Dorman David Wyatt (Director): 6/12, 41,292 股, 約 $16.8M, 價格約 405–408。
  - Kennedy David Alan (CFO): 9/17, 23,896 股, 約 $14.0M, 價格約 585–586。
  - Rothberg Richard Jay (General Counsel): 3 筆共約 $13.8M (6/15 20,000 股 @410; 9/11 6,000 股 @547.56; 9/17 4,000 股 @583.36)。
  - Saavedra Jennifer D. (Officer): 9/4, 25,251 股, 約 $13.1M, 價格 520.00。
  - Radakovich Lynn Vojvodich (Director): 4 筆共約 $7.9M (含期權轉換, 2022 股數相關紀錄), 6/22 至 9/22 分次出售。
  - Tunnell Jane (Officer): 9/4, 5,436 股, 約 $2.8M, 價格 523.52。
- 其他: 9/24 董事股票授予 6 筆 (價格 0, 屬薪酬性質); 6 月 Stock Gift 2 筆 (價格 0)。
- 10b5-1 計畫註記: DATA_UNAVAILABLE (快取未提供交易計畫旗標)。

Notable: 9/17 CFO 出售約 $14.0M 與 Silver Lake 大量出售同日發生, 但無法確認是否屬預定交易計畫。高管與 Silver Lake 合計仍屬持續性減持, 未見任何公開市場買入。

## Ownership shifts
- 機構持股 77.9%, 內部人持股 7.7%, 機構數量 2,746 (快取 major_holders)。
- 2026-06-30 13F 前十大機構 (快取 inst_holders, 13F 有時間差):
  - BlackRock 7.64% (股數 -2.7%)
  - Vanguard Capital Management 6.03% (-2.2%)
  - State Street 4.36% (-4.0%)
  - Bank of America 3.44% (-24.7%)
  - JPMorgan 3.31% (+238.7%)
  - Geode 2.43%
  - Vanguard Portfolio Management 2.43% (-4.3%)
  - Morgan Stanley 2.24% (+6.4%)
  - FMR 1.79% (+33.3%)
  - Goldman Sachs 1.74% (-16.8%)
- 趨勢判讀: 指數型基金小幅減碼, 主動型與券商部位部分加碼 (JPMorgan, FMR, Morgan Stanley); 前十大合計無明顯集中化趨勢。Silver Lake 不在 13F 前十大名單 (屬 insider 申報), 其減持主導內部人淨賣出數字。
- 2026-09-30 13F 資料: DATA_UNAVAILABLE。

## Net sentiment score
Composite: **中性偏多, 信心低** (Neutral-to-bullish, low confidence)
- 分析師面: 偏多 (29 家中 69% 買進評等, 零賣出, 目標中位數高於現價)。信心中高。
- 內部人面: 偏空 (約 $1.03B 賣出, $0 買進, 大股東 Silver Lake 持續分批減持)。信心中, 因資料僅覆蓋 6/10 之後。
- 散戶面: 無法判定 (Reddit、StockTwits、X 均無 2026-10 可用資料)。
- 新聞敘事: 偏多 (AI 伺服器需求與財報超預期), 但估值與預期風險並提。

Divergence flag: **DATA_UNAVAILABLE** (散戶語氣無法取得, 無法判斷散戶與分析師是否背離)。
補充: 分析師看多與內部人持續減持之間存在背離, 屬需留意的訊號, 但內部人減持可能受大股東基金清算 (Silver Lake 為早期投資人) 與薪酬結構影響, 不應單獨解讀為看空。

## 資料缺口
- Reddit / StockTwits: 網路阻擋, DATA_UNAVAILABLE
- 散戶聲量基準: DATA_UNAVAILABLE
- yf 即時資料 (rec_summary, insider, holders): 阻擋, 採快取 2026-10-07 13:11 UTC
- 逐筆評等異動 (yf recommendations): DATA_UNAVAILABLE
- 內部人 2026-04-08 至 2026-06-09 紀錄: DATA_UNAVAILABLE (快取未覆蓋)
- 10b5-1 旗標: DATA_UNAVAILABLE
- 2026-09-30 13F 持股: DATA_UNAVAILABLE

## 來源 (WebSearch / WebFetch 結果)
- https://www.streetinsider.com/rating_history.php?q=DELL
- https://www.nasdaq.com/articles/susquehanna-upgrades-dell-technologies-dell
- https://www.nasdaq.com/articles/dell-technologies-consensus-price-target-increased-1395-58233
- https://www.tipranks.com/news/dell-stock-sees-its-price-target-slashed-by-morgan-stanley-amid-tricky-setup
- https://www.tikr.com/blog/dell-stock-is-up-84-in-3-months-heres-what-could-drive-the-next-move
- https://historicaloptiondata.com/?p=87102 (選擇權情緒, 弱參考)

SENTIMENT REPORT COMPLETE
