# Sentiment — HON as of 2026-10-15

資料狀態摘要: 分析師評等 (yf rec_summary) 與內部人交易 (yf insider) 可用; 散戶社群 (Reddit / StockTwits) 本次全數無法存取 (Reddit 被擋, StockTwits DNS 解析失敗), 僅能以 WebSearch 聚合站資料替代, 可信度低。部分 yf 資料來源為 cache 或為單一快照, 日期需留意。

## Analyst consensus

目前 24 家覆蓋: 3 strong buy / 11 buy / 9 hold / 0 sell / 1 strong sell (yf rec_summary, period 0m)。買進側 (strong buy + buy) 合計 14 家, 約 58%; 持有 9 家, 約 37.5%; 賣出側 1 家 (strong sell), 約 4%。

近 4 個期間趨勢: 買進 12 → 11 (-2m 到 0m), 持有 8 → 9, strong buy 維持 3、strong sell 維持 1。整體為溫和降溫: 少量買進評等移至持有, 並未出現大規模評等下調。

Recent moves: yf recommendations 欄位只回傳月度彙總, 未提供個別升降評等事件, 因此無法確認具體 upgrade / downgrade 券商與日期, 此項 DATA_UNAVAILABLE。

目標價 (聚合站, 日期不明, 僅供參考): 平均約 258.83 USD, 高 303 USD, 低 186 USD。另一聚合站 (Benzinga, 2026-08-14 快照) 顯示 20 家 Outperform, 平均目標約 260 USD。兩個來源的家數與目標價不完全一致, 需以券商原始報告為準。

## Retail social

- Reddit: DATA_UNAVAILABLE。r/stocks 搜尋請求被擋 (www.reddit.com 無法存取)。WebSearch 針對 r/wallstreetbets 與一般 Reddit 討論未找到任何 HON 相關討論串, 無法判斷 HON 在 WSB 的熱度, 也無法判斷 r/stocks 的傾向。
- StockTwits: DATA_UNAVAILABLE。api.stocktwits.com 解析失敗 (ENOTFOUND), 無法取得 bullish / bearish 標記統計。
- X / 聚合站 chatter: 唯一的散戶情緒訊號來自 NAGA 聚合頁, 標示群眾情緒為 NEGATIVE (未標註日期, 方法不明)。此來源品質低, 只能視為弱訊號。
- 媒體與分析文章 (非散戶, 但影響討論框架): Jim Cramer (CNBC, 2026-04-30 前後) 認為 HON 被低估、拆分 (spin-off) 可望消除 conglomerate discount; 一篇 Substack 式 SOTP 模型估值約 307 USD (單一分析師觀點); Simply Wall St 的敘事 "Execution Risk And 2026 Guidance Tone May Cap Further Upside" 公允價值 US$198, 為偏空敘述。
- 近期價格參考: 聚合站 10 月初快照約 213.80 USD, 52 週區間約 195.77 – 260.15 USD。目前即時股價未經驗證, 不應直接以此判斷。
- Buzz volume: 無法量化。WebSearch 未見明顯的近期爆量社群討論, 定性判斷為 低 / 無法確認。

Themes (依可取得的有限資料):
1. 拆分 (spin-off) 與集團折價收斂: 多為看多敘述的核心論點。
2. 2026 指引與執行風險 (尤其航太端成長與營運執行): 主要空方論點。
3. 近期股價由高點回落的疑慮: 聚合站顯示價格走弱, 與 Q2 強勁財報形成反差。
4. 一則聚合站提到 6 月 30 日拆分日期, 來源品質不足, 需以 Honeywell 公告核實。

Representative takes: 無法取得可引用的原始貼文, 故不引用具體發文內容。

## Insider activity

計算區間: 2026-04-15 至 2026-10-15 (6 個月)。

- 有明確價格與金額的公開市場賣出 (Sale at price): 約 $4.23M 美元
  - Kenneth J. West (Officer, feed 中曾列為 CEO / President): 2026-07-27 賣出 17,032 股, 價 243.77, 約 $4.15M; 2026-08-03 賣出 316 股, 價 245.47, 約 $77.6K。
  - 同期另有 West 17,032 股之 derivative conversion / exercise (約 $3.31M 估值, 屬選擇權行權, 非買入)。
- 公開市場買進 (purchase): 0 筆。
- 淨額: 約 $0 買進 / 約 $4.23M 賣出 (僅計算有明確金額的 Sale 紀錄; 不含行權估值)。
- 其他大量交易列 (無金額欄位): CEO Vimal Kapur、CFO Michal Stepniak、General Counsel Su Ping Lu、Billal Hammoud、Jennifer Reilly、James Masso 及多位董事 (2026-04-15 共 10 位董事各 625 股左右) 的交易, 多為 Form 4 獎酬或稅款扣繳類型, 性質需以 SEC 原始檔確認, 不應直接解讀為買入或賣出。
- 資料缺口: 最近一筆交易為 2026-08-03, 2026-08-04 至 10-15 之間無紀錄, 需確認是否為 feed 延遲。
- 注意: 先前 WebSearch 聚合站稱 "net sale of about 4.2M shares last quarter", 此數字與本次計算的約 $4.23M 美元金額相符, 更像是單位誤植 (美元非股數), 不予採用。

判讀: 6 個月內無任何公開市場買進, 賣出集中於 7 至 8 月, 且以前任高階主管 West 為主。此類賣出常見於行權後出售, 不必然代表對前景的負面判斷, 但缺乏內部人買進支撐。CEO 與 CFO 在本區間內無明確金額的賣出紀錄。

## Ownership shifts

- 內部人持股: 0.081% (insidersPercentHeld 0.00081)
- 機構持股: 84.49%, 機構持股家數 2,789
- 機構持股比例變化趨勢: DATA_UNAVAILABLE。yf major_holders 僅提供單一快照, 無法判斷季度增減。
- 解讀: 機構集中度高, 屬於大型機構主導的持股結構, 散戶比重低。這也意味著社群情緒對股價影響相對有限, 股價主要由機構資金流與拆分相關敘事驅動。

## Net sentiment score

Composite: **neutral (中性)**, 信心: **低**

分項判讀:
- 分析師: 偏多 (58% 買進側, 但買進評等近期小幅流向持有)
- 散戶社群: 無法可靠判斷 (Reddit / StockTwits 皆不可用, 僅一則聚合站標示 NEGATIVE)
- 內部人: 偏空 (6 個月無公開買進, 約 $4.23M 明確賣出)
- 股價動能 (聚合站參考): 偏弱 (10 月初約 213.80, 距 52 週高點有明顯回檔)

信心低的主因: 散戶來源全數失效, 分析師目標價來源不一致, 內部人資料最新至 8 月初。

Divergence flag: **不確定 (資料不足, 無法確認)**
- 分析師整體偏多, 而可取得的散戶訊號 (NAGA 聚合站) 偏空, 若該訊號屬實則屬於分析師與散戶的反向分歧, 但此訊號品質低, 不足以判定。
- 內部人淨賣與分析師偏多亦形成分歧, 此分歧常見於行權後出售, 需搭配 SEC Form 4 原始資料再確認。
- 建議: 待 Reddit / StockTwits 可存取後補做散戶面, 並於 2026-10-22 前後 (聚合站估計的財報日, 尚未確認) 重新檢視。

## 資料來源

- yf 工具: analyst recommendations / rec_summary / insider / major_holders (cache 或即時資料, 以工具回傳為準)
- WebSearch 聚合資料:
  - [Honeywell HON Stock Forecast (TradersUnion)](https://tradersunion.com/currencies/forecast/hon-usd/)
  - [Honeywell Benzinga sentiment](https://www.benzinga.com/quote/HON/sentiment)
  - [Honeywell VCP Scanner price target](https://www.vcpscanner.com/stock/hon/price-target)
  - [Barchart: do Wall Street analysts like Honeywell](https://www.barchart.com/story/news/130463/do-wall-street-analysts-like-honeywell-international-stock)
  - [NAGA HON instrument page](https://naga.com/en/instruments/HON.re)
  - [TIKR: Honeywell has risen 21% in 6 months](https://www.tikr.com/blog/honeywell-has-risen-21-in-the-last-6-months-heres-where-the-stock-could-head-in-2026)
  - [Simply Wall St HON](https://simplywall.st/stock/NasdaqGS/HON)
- Reddit / StockTwits: 本次無法存取 (DATA_UNAVAILABLE)

SENTIMENT REPORT COMPLETE
