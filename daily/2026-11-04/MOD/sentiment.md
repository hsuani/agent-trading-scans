# Sentiment — MOD as of 2026-11-04

資料截止：2026-11-03 可取得之最新資料（報告日 2026-11-04）。Reddit 與 StockTwits 無法取得，零售情緒僅能由新聞與分析網站間接推估，信心偏低。

## Analyst consensus

| 項目 | 數值 |
|---|---|
| 目前（0m）分析師數 | 10 家：Strong Buy 1 / Buy 9 / Hold 0 / Sell 0 |
| 一個月前（-1m） | 8 家：Strong Buy 1 / Buy 7 / Hold 0 / Sell 0 |
| 兩個月前（-2m） | 8 家：Strong Buy 1 / Buy 7 / Hold 0 / Sell 0 |
| Buy 類佔比（目前） | 100%（Strong Buy 10% + Buy 90%） |

10 家 buy / 0 hold / 0 sell，即 100% 買進評等。覆蓋家數近兩個月由 8 增至 10，但評等結構沒有變動。

近期動向（來自新聞彙整網站，日期與數字在各來源間不一致）：
- KeyBanc：2026-07-30 將目標價由 370 USD 下調至 280 USD，維持 Overweight；2026-09-02 重申 Overweight 與 280 USD。
- B. Riley：2026-07-30 將目標價由 340 USD 下調至 305 USD，維持 Buy。
- Oppenheimer：2026-05 下旬將目標價由 271 USD 上調至 325 USD，維持 Outperform。
- UBS：2026-05-27 將目標價上調至 310 USD，維持 Buy。
- DA Davidson：重申 Buy，目標價降至 265 USD。
- Roth/MKM：新覆蓋 Buy，目標價 263 USD（日期不明）。
- 未找到 2026 年內明確的評等升級或降級，主要動作是目標價調整。

共識目標價（各來源差異大）：MarketBeat 約 314.29 USD；Investing.com 約 310.29 USD；Benzinga 約 261.00 USD。MarketBeat 另列 2 家 Hold，與本地 yf 資料（0 hold）不符，以 yf 為準。

股價參照問題：內部資料的內部交易成交價顯示，2026-06 約在 280–300 USD，2026-09-10 約為 180 USD。另一來源（Benzinga）顯示 2026-11-02 約 124 USD，但無法與本地行情互相核對。若該價位為真，目前股價較多數目標價低約 50% 以上，共識目標價的上行空間可信度需要重新驗證。本報告未以單一股價作為判斷依據。

## Retail social

- Reddit：r/wallstreetbets 與 r/stocks 的 JSON 端點被封鎖（WebFetch 失敗），無法取樣本貼文。WebSearch 也未找到 2026 年的 WSB 相關討論，僅搜到 2025-02 的 r/Racine 舊討論。無法給出可靠的貼文傾向。
- StockTwits / X：StockTwits API 因網域無法解析而失敗，需於 session 網路設定中允許 api.stocktwits.com 後才能重試。X 端無獨立可用的資料，僅有新聞轉載。
- 聲量（定性）：偏低至中等。主要聲量來自 2026-05-26 的事件：Airedale data center cooling 長期產能協議（超過 4B USD，涵蓋 2027–2029 年），當日股價大漲約 17%，帶動一波討論。
- 傾向：由新聞與分析文章推估為偏多（mixed-to-bullish）。信心低，因為缺少直接的散戶貼文樣本。
- 主要主題：
  - AI 資料中心散熱（data center cooling）成長敘事，為最主要的多方論點。
  - 動能股定位：一篇分析把 MOD 形容為動能重、成長預期高的熱管理標的；同時提到空單比率近期上升，可能放大上漲時的波動。
  - 估值爭議：2025-11 的分析指出 NTM P/E 約 29 倍，偏貴，但資料已過時。
  - 質疑面：有人認為它「不是熱門 AI 股」，較像低調的產業股；也有舊貼文提及高層管理變動的疑慮。
- 代表性摘錄（≤15 字，來源為 2025 年 r/Racine 舊貼文）：「It certainly isn't a glamour AI stock, but might be a low key winner.」

## Insider activity

查詢區間：2026-05-04 至 2026-11-04（6 個月）。

| 日期 | 內部人 | 職稱 | 類型 | 股數 | 金額（USD M） |
|---|---|---|---|---|---|
| 2026-06-01 | MCGINNIS ERIC S | Officer | 公開市場賣出 | 38,082 | 10.86 |
| 2026-06-01 | LASZLO ARTHUR JR | Officer | 公開市場賣出 | 900 | 0.27 |
| 2026-06-16 | ASHLEMAN ERIC D | Director | 公開市場賣出 | 15,000 | 4.33 |
| 2026-06-18 | AGEN BRIAN JON | Officer | 公開市場賣出 | 38,282 | 11.30 |
| 2026-06-18 | MCGINNIS ERIC S | Officer | 公開市場賣出 | 1,020 | 0.30 |
| 2026-09-10 | AGEN BRIAN JON | Officer | 公開市場賣出 | 4,306 | 0.78 |

- 6 個月淨額：買進 0 USD M；賣出合計約 27.8 USD M（97,590 股）。淨買賣為 -27.8 USD M。
- 另有 2026-09-10 AGEN 的衍生性證券行使（5,269 股，約 0.06 USD M），屬行使而非市場賣出，未計入上表。
- 獎勵股發放（Stock Award，金額 0）：2026-05-20 與 05-26 的多位高管與董事，以及 2026-08-20 的董事會成員，不計入買賣金額。CEO BRINKER NEIL DAVID 於 05-26 獲發 215,464 股獎勵，無公開市場交易。
- 重點觀察：
  - CEO BRINKER 與 CFO LUCARELI 在 6 個月內沒有公開市場賣出。LUCARELI 最後一次大額賣出為 2026-02-17（約 4.29 USD M，價格約 217–222 USD），在區間之外。
  - 賣出集中於 6 月，成交價約 280–300 USD；9 月的賣出價約 180 USD。
  - 6 個月內沒有任何公開市場買進。
  - 無法判斷這些賣出是否屬於預先排定的交易計畫（10b5-1），需以 SEC Form 4 附註確認。

## Ownership shifts

- 機構持股比率（institutionsPercentHeld）回傳值為 100.7%，超過 100%，屬資料異常，不宜直接採用。
- 機構持股家數（institutionsCount）：787 家。
- 內部人持股比率（insidersPercentHeld）：約 1.9%。
- 沒有時間序列資料，無法判斷機構持股是增加或減少。

## Net sentiment score

- 分析師面：偏多，信心高（10 買 / 0 持有 / 0 賣，評等方向一致；但目標價離散度大、股價來源衝突）。
- 內部人面：偏空（6 個月淨賣約 27.8 USD M、零買進），信心中等（樣本少，且未確認是否為計畫性交易）。
- 零售面：偏多（由新聞推估），信心低（無直接貼文樣本）。
- 綜合：中性（neutral），信心中低。分析師與零售的方向偏多，內部人的淨賣出則是主要反向訊號。

Divergence flag：是。
- 分析師偏多，與內部人的淨賣出方向相反；這種落差通常值得留意。
- 零售傾向無法精確判定，因此無法確認零售與分析師是否同向。
- 股價來源衝突（124 USD 與 180 USD 等），會影響目標價隱含的上行空間判斷，需先核對即時行情。

SENTIMENT REPORT COMPLETE
