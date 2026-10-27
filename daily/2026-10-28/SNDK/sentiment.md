# Sentiment — SNDK（SanDisk）as of 2026-10-28

> 資料時效注意：yf 工具即時 Yahoo 連線失敗（fc.yahoo.com ConnectionError，Cookie/crumb 取得失敗），所有 rating、insider、holder 數據皆取自 `prices/yf/SNDK.json`（cache `_refreshed_at` 2026-10-27 12:05 UTC）。Reddit 與 StockTwits 無法存取（StockTwits 為 DNS 解析失敗，需在 session 網路設定中放行 `api.stocktwits.com`），X 搜尋未取得 2026 年 10 月的散戶討論樣本。散戶面為 DATA_UNAVAILABLE，信心度整體偏低。

## Analyst consensus

25 家（yf rec_summary 加總）：**4 strongBuy / 17 buy / 3 hold / 0 sell / 1 strongSell**，即買進側 21 / 25 = **84%**。yf info 的 numberOfAnalystOpinions 為 24，與彙總計數差 1 家，推測為評等與目標價樣本數口徑不同，未另行核對。recommendationKey = buy。

評等趨勢（yf recommendations，家數）：

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 買進側佔比 |
|---|---|---|---|---|---|---|
| 0m（本月） | 4 | 17 | 3 | 0 | 1 | 21/25 = 84% |
| -1m | 4 | 17 | 3 | 0 | 1 | 21/25 = 84% |
| -2m | 4 | 16 | 3 | 0 | 1 | 20/24 = 83% |
| -3m | 3 | 15 | 4 | 0 | 1 | 18/23 = 78% |

近三個月買進側增加 2 家（-3m 至 0m），Hold 減少 1 家，Sell 維持 0 家。yf 僅回傳彙總計數，無個別券商升降評等明細。

目標價（yf info，USD / 股）：

| 項目 | 目標價（USD） | 相對 cache 股價 1,255.58 之空間 |
|---|---|---|
| 平均（targetMeanPrice） | 2,143.8 | 約 +71% |
| 最高（targetHighPrice） | 3,600 | 約 +187% |
| 最低（targetLowPrice） | 1,000 | 約 -20% |

註：cache 股價 1,255.58 USD（previousClose 1,238.03）為 10/27 前後快照，與網路搜尋所見 10/2 約 1,788 USD 相差甚大，**股價水準未與即時行情核對，上述空間百分比僅供參考**。

Recent moves（WebSearch，日期標註如可確認）:
- Investing.com 彙總（截至 2026-10-02）：共識 Buy，平均 12 個月目標價約 2,137 USD，與 yf 平均值一致。
- Citi（2026-10-01 維持）：Buy，目標價 2,100 USD。另有 Yahoo 文章稱 Citi 目標價上調至 2,000 USD 以上，日期不明。
- Susquehanna：Yahoo 文章稱上調至 2,000 USD；StreetInsider 列示 3,250 USD 為 12 個月內最高目標價，日期不明，可能過時。
- 一篇 Street 文章稱目標價由 2,100 上調至 2,425 USD，日期未註明。
- TipRanks 平均目標價約 163 USD、Arete 中性 63 USD、Benchmark 85 USD 等數字明顯為較早期資料，**不納入判斷**。

方向性：可確認的近期動向為上修多於下修，評等無降級。目標價離散度大（1,000 至 3,600 USD），反映估值假設分歧。

## Retail social

- Reddit（r/wallstreetbets、r/stocks）：**DATA_UNAVAILABLE**。WebFetch 回傳 "unable to fetch from www.reddit.com"，無貼文樣本、分數或留言數。
- StockTwits：**DATA_UNAVAILABLE**。`api.stocktwits.com` DNS 解析失敗，本次不再重試。
- X / 新聞鏈：WebSearch 結果以法人目標價與財經媒體報導為主，未找到可歸類為散戶意見的 2026 年 10 月貼文，無法引用樣本。
- 討論量（相對常態）：無法量化。

Retail tilt：**無法判定（樣本不足）**。

Top recurring themes（僅依法人報導與財經媒體可見內容歸納，非散戶原文）:
1. 估值與 forward P/E：yf forwardPE 約 4.7 倍、trailingPE 約 17.0 倍，獲利預估變動幅度大，市場對盈餘可持續性有分歧。
2. 獲利超預期：最近一季（8/5 公布）EPS 39.25 USD，優於預估 34.52 USD，超出 13.7%；前幾季超預期幅度更大（4/30 +59.7%、1/29 +75.0%）。
3. AI 資料中心需求與 NAND 供需：法人目標價上修的主要依據。
4. 股價回檔：cache 股價與 9 月內部人賣出價（約 1,520 至 1,770 USD）相比明顯偏低，回檔原因未能從可得來源確認。

## Insider activity

Net 6mo（2026-04-28 至 2026-10-27）：**買進 $0；賣出約 $130.3M**（13 筆公開市場 Sale，USD；另有股票授予、贈與與一筆無金額紀錄，未計入金額）。

| 內部人 | 職稱 | 賣出金額（USD M） | 賣出股數 | 期間 |
|---|---|---|---|---|
| David V. Goeckeler | CEO | 104.97 | 67,679 | 9/14、9/17 |
| Alper Ilkbahar | CTO | 11.40 | 7,112 | 6/1、9/3 |
| Bernard Shek | Officer | 7.99 | 4,708 | 6/3 至 9/8（每月一次為主） |
| Michael Pokorny | Officer | 3.49 | 2,446 | 5/12 |
| Luis Felipe Visoso Lomelin | CFO | 1.57 | 1,000 | 9/15 |
| Necip Sayiner | Director | 0.87 | 579 | 5/8 |

Notable:
- CEO Goeckeler 於 9/14 與 9/17 合計賣出約 67,679 股，成交價約 1,522 至 1,587 USD，為 6 個月內最大單一賣方。同日（9/17）另有 CEO 與多位高管的股票授予紀錄，賣出與授予是否屬於既定交易計畫或稅務相關處分，本資料無法判定。
- 2026-08-20 CTO 有一筆 276 股紀錄（無金額，類型未標示），未納入計算。
- 賣出多集中於 9 月，價格區間高於 cache 股價 1,255.58 USD。
- 無任何董監事或高管公開市場買進紀錄。

## Ownership shifts

- insidersPercentHeld：1.09%
- institutionsPercentHeld：82.5%（institutionsCount 2,351；institutionsFloatPercentHeld 83.5%）
- shortPercentOfFloat：3.34%
- 前十大機構（2026-06-30 快照，單一時點，無時間序列）：10 家中 6 家增持、4 家減持。
  - 增持代表：Invesco +381%、JPMorgan +176%、Clear Street +144%、Situational Awareness LP +119%。
  - 減持代表：FMR（Fidelity）-41%；BlackRock -1.0%、Geode -14.8%。
  - BlackRock（7.12%）與 Vanguard（6.69%）為最大持股，變動幅度小。
- 整體：**機構流向方向中性，前十大內增減互見，無法判斷趨勢**。百分比變動多為小部位，FMR 大幅減持為主要負向訊號。

## Net sentiment score

Composite：**中性（信心度：低）**。分析師面偏多，內部人面偏空，兩者抵銷後整體中性；散戶面無資料。

- 分析師面：**偏多**（信心度中）。25 家中 21 家買進側，近三個月淨上修 2 家買進、平均目標價約為現價 1.7 倍，但股價來源未經即時核對。
- 內部人面：**偏空**（信心度中高）。6 個月內 13 筆賣出、約 $130.3M，0 筆公開市場買進，CEO 賣出為最大宗；授予與贈與不計入方向。
- 零售面：**無法判定**（信心度低）。Reddit、StockTwits、X 皆無可用樣本。
- 機構面：**中性**（信心度低）。前十大增減互見，無時間序列。

Divergence flag：**無法判定**。零售端無資料，無法套用「零售與分析師反向」的判定。但分析師面（偏多）與內部人面（偏空）方向相反，是本次最明確的分歧訊號，需在後續 debate 中納入考量。

Upcoming catalyst：下一次財報日為 **2026-10-29**（美股盤後，yf 時間 20:00 UTC），EPS 預估 **46.41 USD**（前次 Q3 實際 39.25 USD）。財報前後的評等與目標價變動應於下一次快照重新核對。

## 數字核對

- 市值：181,465,923,584 USD ÷ 10^9 ≈ **181.5B USD**（yf info.marketCap）。
- 股數反推：181.5B USD ÷ 1,255.58 USD ≈ 1.445 億股，與 yf sharesOutstanding 144,527,564 股一致（約 144.5M 股）。
- 內部人賣出加總：104.97 + 11.40 + 7.99 + 3.49 + 1.57 + 0.87 = **約 130.3M USD**，與逐筆加總一致。
- 分析師目標價：2,143.8 USD × 144.5M 股 ≈ 3,098 億 USD，此為目標價隱含市值，單位為 USD，未與 TWD 混用。

## 資料缺口與後續建議

1. 即時 Yahoo 連線恢復後，重跑 `pipeline/tools/yf SNDK rec_summary`、`insider`、`info` 以確認現價與目標價。
2. 放行 `api.stocktwits.com` 與 Reddit 存取後，補抓散戶情緒，才能判斷 divergence flag。
3. 向 SEC EDGAR Form 4 核對 CEO 9/14 與 9/17 賣出是否屬於 10b5-1 交易計畫。
4. 取得機構持股的時間序列（本次僅 2026-06-30 單點快照）。
5. 財報（10/29）公布後，重新核對分析師評等與目標價變動。

SENTIMENT REPORT COMPLETE
