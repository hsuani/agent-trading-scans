# Sentiment — ALAB (Astera Labs) as of 2026-10-11

資料時效聲明：yf 工具的 Yahoo cookie/crumb 取得失敗，回傳為快取資料（cache fallback）。Reddit 與 StockTwits 直接抓取在此沙箱被封鎖，改用 WebSearch 取得的第三方快照，最新日期多落在 2026-09 或 2026-08。所有缺漏欄位標示 DATA_UNAVAILABLE。

## Analyst consensus

目前 rating 分布（yf rec_summary，0m）：**18 buy**（7 strongBuy + 11 buy）/ **8 hold** / **0 sell**，共 26 家。

近四個月趨勢（yf rec_summary）：

| 期間 | strongBuy | buy | hold | sell | 合計 Buy 類 / Hold |
|---|---|---|---|---|---|
| 0m（目前）| 7 | 11 | 8 | 0 | 18 / 8 |
| -1m | 7 | 12 | 7 | 0 | 19 / 7 |
| -2m | 7 | 12 | 7 | 0 | 19 / 7 |
| -3m | 7 | 11 | 8 | 0 | 18 / 8 |

解讀：Buy 類家數在近一個月減少 1、Hold 增加 1，屬小幅降溫；無任何 sell 評等。

近期評等與目標價動作（yf recommendations 只回傳上表彙總，逐筆 upgrade/downgrade 歷史 DATA_UNAVAILABLE；以下來自 WebSearch 快照）：
- Northland Capital Markets：2026-08-17 由 Market Perform 升至 Outperform，目標價 $350。
- Barclays：目標價由 $200 升至 $325，維持 Equal Weight（日期未確認）。
- UBS：維持 Neutral，目標價 $425（日期未確認）。
- Stifel、Roth：有目標價調整快照（Stifel $100 升至 $150；Roth $130 降至 $100，或 Roth 升至 $105），日期不明，不列為 2026-09 動作。
- 2026-09 內的新評等變動：未找到，DATA_UNAVAILABLE。

目標價共識（Bullstory，2026-09-01 與 2026-09-22 兩次快照一致）：平均 $389.95，最高 $500，最低 $190（Bullstory 另列 23 家 Buy）。Benzinga 快照另見最低 $82（Raymond James），與 $190 衝突，未採信。stockscan 平均 $128 與其他來源嚴重不一致，剔除。

現價：DATA_UNAVAILABLE（2026-09-22 快照約 $340.74，2026-09-14 快照約 $291.22，兩者皆非 2026-10-11 行情）。

## Retail social

- **Reddit**：直接抓取被封鎖，未重試。WebSearch 取得 AltIndex 快照（2026-09-08）：約 5 則提及/日，較近期均值 +114%；AltIndex 情緒分 66/100（中性）。同類比較：AMD 約 71/日、Intel 約 144/日。可辨識的具名貼文僅 r/wallstreetbets 兩則（各 1 upvote），樣本過薄，不足以判定趨勢。
  - 樣本引述（≤15 字）：無可用引述，DATA_UNAVAILABLE。
- **StockTwits**：直接 API 同樣未取得。WebSearch 取得 AltIndex 快照（時間約至 2026-08）：平均約 192 則提及/日，較三個月前 +26%；多空情緒分 70/100（中性）；訂閱人數 12,869，三個月成長 13.2%。AltIndex 綜合情緒（Reddit+StockTwits+其他）76/100，偏多，但較 30 日均值走弱。
- **X / 新聞聲量**：未取得可靠 X 原文。Benzinga 選擇權快照：2026-09 的 put/call 1.12（標示偏空），7 月底快照 0.37（標示偏多），兩者日期衝突，不採為當前信號。
- **Short interest**：Benzinga 中段快照 6.8% of float，後期快照 9.7% of float，時點不一，僅供參考。
- **聲量定性**：低於 AMD、Intel 的絕對水準；屬事件驅動型（earnings、產業新聞時放大），目前無 2026-10 的聲量數據，DATA_UNAVAILABLE。

主要論點（由摘要歸納，非逐字引用）：AI 網路與連接晶片的成長敘事、財報超預期後的追價與獲利了結爭論、估值是否已反映 AI 需求，以及內部人大量減持的解讀。

Retail 整體傾向：**中性偏多（mixed to modestly positive）**，信心低，因資料多為 2026-08 至 09 的第三方快照。

## Insider activity

6 個月窗口（2026-04-11 至 2026-10-11）：
- 公開市場買入（Purchase）：**$0**。
- 公開市場賣出（Sale）：約 **$628.5M**（依 yf insider 逐筆加總，不含 stock gift、stock award 等非市場交易）。
- 淨額：約 **-$628.5M**（純賣出）。

主要賣方（6 個月賣出金額）：
- Sanjay Gajendra（President）：約 $292.0M
- Jitendra Mohan（CEO）：約 $170.0M
- Manuel Alba（Director）：約 $132.5M
- Stefan A. Dyckerhoff（Director）：約 $24.4M
- Philip Mazzara（General Counsel）：約 $5.8M
- Jack R. Lazar（Director）：約 $3.6M

Notable：
- 2026-09-01 Alba Manuel（Director）賣出 183,000 股，約 $51.3M，價格 $277–289。
- 2026-09-02 Dyckerhoff Stefan A.（Director）賣出 12,499 股，約 $3.4M，價格 $274–277。
- 2026-08-17 CEO Mohan Jitendra 與 President Gajendra Sanjay 各賣出 90,630 股，約 $30.8M，價格 $334–352。
- 2026-07-01 Alba Manuel 大額賣出，價格 $430–468，為 6 個月內最高價區間的賣出。
- 最近一筆買入（Purchase）為：無。最近一筆非市場交易為 2026-07-20 Cota Germaine 股票獎勵。

觀察：賣出價格區間由 2026-04 的 $106–175 上行至 2026-07 的 $430–468，之後回落至 $274–352。多數賣出可能來自 Rule 10b5-1 計畫，但資料無法確認，標示 DATA_UNAVAILABLE（計畫屬性）。6 個月內全體內部人無一筆公開買入。

## Ownership shifts

- insidersPercentHeld：10.32%
- institutionsPercentHeld：75.91%
- institutionsFloatPercentHeld：84.65%
- institutionsCount：1,333
- 季度趨勢（增減持、前十大持股變化）：DATA_UNAVAILABLE（工具僅回傳當期快照）。

## Net sentiment score

- **分析師面：偏多（bullish）**，信心中高。18/26 Buy 類、0 sell，目標價共識 $390 大幅高於 2026-09 的價格區間；近月 Buy 類微降，需留意。
- **內部人面：偏空（bearish）**，信心中。6 個月約 $628M 純賣出、無買入；但大量賣出多與股權獎勵與計畫性出售相關，訊號強度需扣分。
- **散戶面：中性（neutral）**，信心低。聲量中等偏低，情緒分 66–70 屬中性，綜合 76 偏多但走弱；資料多為 2026-08 至 09。
- **綜合：中性偏多（neutral-to-bullish）**，信心低至中。分析師共識與散戶中性同向偏多，但內部人持續大額賣出形成明顯反向訊號。

**Divergence flag：否**（散戶傾向為中性，並非與分析師明確相反）。
補充：內部人與分析師方向明顯分歧（內部人純賣、分析師 0 sell），此點較具資訊量，建議下游報告納入。

## 資料來源

- yf 工具（pipeline/tools/yf）：rec_summary、recommendations、insider、major_holders（快取回傳）
- AltIndex Reddit / StockTwits 快照：https://altindex.com/ticker/alab/reddit-mentions 、https://altindex.com/ticker/alab/stocktwits-mentions 、https://altindex.com/ticker/alab/sentiment
- Bullstory 目標價與評等：https://bullstory.io/en/stocks/alab/forecast/price-target 、https://bullstory.io/en/stocks/alab/forecast/analyst-rating
- Benzinga 情緒與選擇權：https://www.benzinga.com/quote/ALAB/sentiment
- MarketBeat（2026-08 快照）：https://www.marketbeat.com/instant-alerts/astera-labs-nasdaqalab-trading-down-19-whats-next-2026-08-21/
- TipRanks / The Fly（目標價調整，日期不明）：https://www.tipranks.com/news/the-fly/astera-labs-price-target-raised-to-150-from-100-at-stifel

SENTIMENT REPORT COMPLETE
