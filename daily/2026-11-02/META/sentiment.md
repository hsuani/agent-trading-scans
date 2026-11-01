# Sentiment — META as of 2026-11-02

資料取得狀態: Reddit (r/wallstreetbets, r/stocks) 與 StockTwits 無法取得 (見下方 Retail social)。Analyst 與 insider 資料來自 yf 工具。Analyst 目標價變動與散戶氛圍來自 WebSearch，日期與可靠度較弱。

## Analyst consensus

Rating 分布 (yf rec_summary, 0m 期間，合計 62 家):

| 評級 | 家數 | 占比 |
|---|---|---|
| Strong Buy | 9 | 14.5% |
| Buy | 46 | 74.2% |
| Hold | 6 | 9.7% |
| Sell | 1 | 1.6% |
| Strong Sell | 0 | 0% |

Buy 系 (Strong Buy + Buy) 合計 55 家，占 88.7%。

近三個月趨勢 (yf 各期間快照):

| 期間 | Strong Buy | Buy | Hold | Sell | 合計 |
|---|---|---|---|---|---|
| 本月 (0m) | 9 | 46 | 6 | 1 | 62 |
| 上月 (-1m) | 8 | 47 | 7 | 1 | 63 |
| -2m | 8 | 47 | 7 | 0 | 62 |
| -3m | 8 | 47 | 7 | 0 | 62 |

上月至本月: Strong Buy 增 1，Buy 與 Hold 各減 1，Sell 持平，合計少 1 家。整體評級結構穩定，沒有明顯集體轉向。

目標價與近期調整 (WebSearch，非 yf 原始資料，日期未完全確認):
- 平均目標價: TipRanks 約 $845.9 (44 家，標示 2026-10-22)；MarketBeat 約 $785.2 (47 家)。兩者相差約 $61，來源口徑不同。
- 目標價區間約 $595 至 $1,000 (Rothschild Redburn $1,000，2026-07-20 由 $900 調升)。
- Q3 後下修 (文章標示 post-Q3，個別日期未全部確認): JPMorgan $875 至 $800 (維持 Overweight)；Citi $915 至 $850；Mizuho $925 至 $815；Morgan Stanley $820 至 $750 (維持 Overweight)；BofA $900 至 $810；Piper Sandler $880 至 $840。
- 上調: Guggenheim $800 至 $875；BMO $610 至 $710；Baird $680 至 $750；Cantor Fitzgerald 維持 Overweight，目標價 $920。
- 升評: Arete 由 Neutral 升 Buy，目標 $718，文章只標 "12-04"，年份不確定，不納入判斷。

判讀: 評級仍偏多，但 Q3 後目標價普遍下修，平均目標價與近期股價之間的空間縮小。yf 沒有逐家升降評紀錄，無法確認 10 月內個別機構動作的完整名單。

## Retail social

- Reddit: 無法取得。WebFetch 對 www.reddit.com 回傳 "unable to fetch"，依規則軟失敗。無 r/wallstreetbets 或 r/stocks 樣本，無法評估 tilt。
- StockTwits / X: StockTwits (api.stocktwits.com) DNS 解析失敗，依規則軟失敗。需在 session 網路設定允許此網域後才能重試。WebSearch 找不到 2026-10 的 Reddit 或 X 貼文。
- 替代參考 (WebSearch，多為 2026-08 以前的自動化或低深度網站，時效性弱):
  - 2026-08-10/11 期權流量頁面顯示 call 美元成交量高於 put，偏多；同頁面另有 MACD 偏空訊號。
  - 2026-08 某頁面估計整體情緒約 60% 偏多，交易者對估值與成長有分歧。
  - 2026 年初與春季的氛圍較分散，主要擔心關稅、歐盟監管調查與法律訴訟。
- 散戶聲量 (buzz volume): 無法量化，因為沒有可取得的提及數資料。
- Themes (由 WebSearch 摘要推得，非直接抓取的貼文):
  - 偏多: AI 投入帶來的成長與估值支撐、期權 call 流量、Overweight 評級。
  - 偏空: 歐盟監管與法律風險、AI 支出是否侵蝕利潤、ChatGPT 等生成式 AI 對用戶的競爭擔憂。
- 散戶 tilt: 無法判定 (資料缺)。以替代來源看，屬 mixed，偏多略佔優勢，但時效性不足。

## Insider activity

Net 6mo (2026-05-02 至 2026-11-02): 買入 $0 M，賣出約 $128.6 M (USD M)。未見任何公開市場買入。以下金額為 "Sale at price" 有成交價的列，不含 Stock Gift (0 美元) 與無成交價的列 (多為 RSU、選擇權或稅務相關的股數變動，不計現金流)。

依人員彙總 (USD M，已核對總和 = $128.6 M):

| 人員 | 職位 | 筆數 | 賣出金額 (USD M) | 主要時點與價格 |
|---|---|---|---|---|
| Cox Christopher K | Officer (yf 未標示具體職稱) | 3 | 55.0 | 2026-09-09 至 09-21，約 $650 至 $725 |
| Zuckerberg Mark | CEO | 1 | 21.4 | 2026-09-24，約 $775 至 $779 (間接持股 "I")；另 07-31 有 591,690 股贈與 (無現金) |
| Olivan Javier | COO | 19 | 23.9 | 2026-05 至 10 月，約每 1 至 2 週一筆，單筆約 $0.8 至 $1.4 M；09-08 與 07-06 各約 $3.1 至 $3.3 M |
| Li Susan J. | CFO | 3 | 13.4 | 2026-05-18 ($6.9 M)、08-14 ($1.5 M)、08-18 ($5.1 M) |
| Bosworth Andrew | CTO | 2 | 9.1 | 2026-05-18 ($4.8 M)、08-18 ($4.4 M) |
| Mahoney Curtis J | Officer | 2 | 2.1 | 2026-05-27、08-18 |
| Anderson Aaron | Officer | 1 | 2.0 | 2026-09-03，約 $618 |
| Kimmitt Robert M | Director | 3 | 0.9 | 2026-06 至 08 月，單筆約 $0.3 M |
| Alford Peggy | Director | 2 | 0.5 | 2026-07-31、10-26，約 $0.25 M/筆 |
| Andreessen Marc L | Director | 1 | 0.3 | 2026-08-04，約 $0.25 M |

重點觀察:
- 賣出集中於 2026-09 (Cox、Zuckerberg 及 Olivan 的大額單) 與 2026-08 (Li、Bosworth、Mahoney)，主要發生在股價區間高點 (約 $650 至 $780) 之後。
- 經常性賣出者 (Olivan 週期性小額、Kimmitt、Alford 的固定股數) 看起來像預先排程的交易計畫，不必然代表對前景的判斷。但 CEO 與 Cox 的大額單屬一次性，值得注意。
- 以 yf insider 欄位無法確認是否為 10b5-1 計畫，需要 SEC Form 4 才能確定。
- 股數與價格核對: Zuckerberg 27,474 股 × 約 $777 ≈ $21.4 M，與工具金額一致。

## Ownership shifts

- 機構持股比例: 77.5% (institutionsPercentHeld 0.7753)；流通股口徑 77.6%。
- 機構家數: 6,645。
- 內部人持股: 0.145%。
- yf major_holders 只給單一快照，無時間序列，無法判斷機構集中度的趨勢。

## Net sentiment score

Composite: **中性偏多 (neutral-to-bullish)**，信心 **低**。

分項判斷:
- Analyst: 偏多。Buy 系 88.7%，評級穩定，但 Q3 後目標價普遍下修，上行空間收斂。權重高。
- Insider: 偏空 (賣出為主)。6 個月賣出約 $128.6 M，零買入，9 月大額單集中。不過多為常態性與排程性交易，解讀力度有限。權重中。
- Retail: 無法判定。Reddit 與 StockTwits 皆不可取得，替代來源時效性弱，且偏多與偏空證據並存。權重低、信心低。
- 價格脈絡 (參考，非情緒指標): insider 成交價由 2026-08-18 的約 $547 至 $560，升至 2026-09-24 的約 $775 至 $779，再回到 2026-10-26 的約 $640，約自高點回落 17%。11-02 收盤價未取得。

Divergence flag: **無法判定** (散戶資料缺)。

若只比較 analyst 與 insider: 方向相反 (analyst 偏多、insider 淨賣出)。這屬於 "insider 與 analyst 分歧"，不是 "retail 與 analyst 分歧"，與本模板定義不同，因此不設為 divergence yes。

資料缺口 (待補):
1. Reddit r/wallstreetbets 與 r/stocks 無法取得，需允許 www.reddit.com 或改用其他來源。
2. StockTwits 需在 session 網路設定中允許 api.stocktwits.com。
3. yf recommendations 回傳的是期間快照，缺少個別機構的升降評紀錄。
4. 目標價與 Q3 後調整的日期部分未確認，建議以 Form 4 與分析師原始報告核對。

Sources (WebSearch 摘要使用的網址):
- https://www.tipranks.com/news/the-fly/meta-platforms-price-target-lowered-to-800-from-875-at-jpmorgan-thefly
- https://www.tipranks.com/news/the-fly/meta-platforms-price-target-lowered-to-810-from-900-at-bofa-thefly
- https://www.marketbeat.com/stocks/NASDAQ/META/Forecast/
- https://finance.yahoo.com/news/cantor-fitzgerald-sees-meta-poised-212314908.html
- https://historicaloptiondata.com/?p=72035

SENTIMENT REPORT COMPLETE
