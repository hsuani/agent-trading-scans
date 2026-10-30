# Sentiment — AMT (American Tower Corp) as of 2026-10-31

## Executive summary

分析師端明顯偏多：rec_summary 顯示 25 位分析師中 22 位為 Buy 或 Strong Buy（約 88%），3 位 Hold（約 12%），無 Sell。近四個月的分布略為改善（3 個月前為 21 Buy / 4 Hold），評級沒有下調。

散戶社群端資料不足：Reddit 與 StockTwits 直接抓取皆被封鎖，WebSearch 也未找到近期 r/wallstreetbets、r/stocks 的 AMT 討論串。因此提及量與多空比例皆為 DATA_UNAVAILABLE，無法判斷散戶與分析師是否背離。

內部人近六個月淨賣出約 $0.70M（公開市場買入 $0.50M，賣出 $1.20M），金額小，且由董事與高階主管的單筆交易組成。2026 年 2 至 3 月 CEO、COO、CFO 有大額的選擇權行使後賣出（合計約 $20M+），但已超出六個月窗口，列為背景資訊。

綜合判斷：中性偏多，信心中低。分析師與機構面支持偏多，內部人與散戶面缺乏有效資料，綜合分數只能反映前者。

## Retail / social sentiment

- **Reddit（r/wallstreetbets、r/stocks）**：DATA_UNAVAILABLE。直接 JSON 抓取被封鎖（WebFetch 回傳無法存取 www.reddit.com）。WebSearch 結果未出現 AMT 的近期社群討論串，搜尋結果以財經媒體與分析師文章為主。
- **StockTwits**：DATA_UNAVAILABLE。api.stocktwits.com 無法解析（DNS 失敗），需於 session 網路設定中放行該網域後才能重試。
- **X / 新聞與意見類網站**：WebSearch 僅找到聚合型財經網站與分析師報導，未能取得可量化的多空比例或提及量，不做百分比推估。
- **提及量相對常態**：DATA_UNAVAILABLE（無法取得可比較的提及數）。
- **主要主題（以 WebSearch 所得之媒體敘述為準，非散戶原文）**：
  - 估值：媒體提到 AMT 股價較 52 週高點低約 24%，trailing P/E 約 29x，低於其五年歷史平均（報導稱五年平均高於 40x）。
  - 股價與 5G 資本支出循環：媒體多以電信業者 5G 投資節奏作為核心論述。
  - 股息價值：部分報導以股息與被低估的成長催化劑作為賣點。

## Analyst consensus

| 項目 | 期間 0m（現在） | 期間 -3m | 變化 |
|---|---|---|---|
| Strong Buy | 7 | 6 | +1 |
| Buy | 15 | 15 | 0 |
| Hold | 3 | 4 | -1 |
| Sell | 0 | 0 | 0 |
| Strong Sell | 0 | 0 | 0 |
| 總家數 | 25 | 25 | — |
| Buy 合計比例 | 約 88% | 約 84% | 約 +4 pct |

- **近期評級變動**：yf recommendations 工具僅提供家數彙總，無個別券商的升降評等明細，故無法列出具名的 upgrade/downgrade。
- **目標價**：yf 工具未提供目標價。WebSearch 聚合站顯示平均目標價約 $214–218（一篇 Barchart 報導為 $217.85，另一篇聚合站為 $214.04 與 $215.7），但各來源日期不一，且無法對應到 2026-10-31 當日，僅作參考，標示為未驗證。
- **個別券商**：聚合站曾提及 Mizuho 在 4 月將目標價由 $189 調至 $205，RBC 維持 Hold 與 $195 目標價。此為 4 月資訊，已過時，無法確認是否仍有效。
- **分歧訊號**：Barchart 報導稱共識相較一個月前轉趨保守，與 yf 家數顯示的小幅改善方向不一致。兩者時間點不同，無法確定哪個代表最新狀態。
- **股價參考**：WebSearch 聚合站提到 7 月約 $174，12 個月區間約 $160–234。無 10 月 31 日當日收盤價，無法計算目標價隱含上行空間。
- **財報**：一篇來源提及 Q3 2026 財報預計於 10 月 27 日前後公布，但未能確認實際發布日期與市場反應，此點需於後續確認。

## Institutional / insider activity

### 內部人交易（近六個月，2026-05-01 至 2026-10-31）

| 日期 | 人員 | 職稱 | 類型 | 股數 | 金額 (USD M) |
|---|---|---|---|---|---|
| 2026-08-21 | Rajesh Kalathur | Director | 公開市場買入 @ $177.00 | 2,829 | 0.50 買入 |
| 2026-07-29 | Robert J. Meyer Jr. | Officer | 賣出 @ $178.89 | 5,000 | 0.89 賣出 |
| 2026-07-29 | Ruth T. Dowling | General Counsel | 賣出 @ 約 $173 | 1,791 | 0.31 賣出 |
| 2026-05-28 | Pamela D.A. Reeve | Director | 贈與 | 810 | 0（非市場交易） |
| 2026-10-01 | Paul Blanchett | Officer | 股票獎勵 | 16,299 | 0（授予） |

- 窗口內公開市場買入合計約 $0.50M，賣出合計約 $1.20M，淨賣出約 $0.70M。
- 買入來源為董事（Kalathur），賣出來源為非 CEO/CFO 的高階主管。CEO 與 CFO 在窗口內無公開市場交易。
- 窗口外背景：2026-02 至 03 月，CEO Steven Vondran（約 $6.3M 賣出）、COO Eugene Noel（約 $7.9M）、CFO Rodney Smith（約 $6.6M，2 月）等人以選擇權行使（行使價約 $94.7）後賣出，成交價約 $188–193。屬於選擇權行使後賣出，不宜單純解讀為看空，但規模可觀。
- 注意：yf 工具的交易清單可能不完整，本段以工具回傳為準。

### 機構持股

- 機構持股比例約 97.4%（機構家數 2,391），內部人持股約 0.08%。
- 持股趨勢（季度增減）：DATA_UNAVAILABLE。yf major_holders 僅提供當前快照，無歷史比較。
- 機構持股集中度高屬常態，本身不構成明確的多空訊號。

## Overall sentiment verdict

| 面向 | 判斷 | 信心 | 依據 |
|---|---|---|---|
| 分析師共識 | 偏多 | 中高 | 88% Buy，無 Sell，近期小幅改善；目標價來源不一 |
| 內部人 | 中性偏空（輕度） | 中 | 窗口內淨賣出約 $0.70M，以非 CEO/CFO 為主；窗口外大額選擇權行使後賣出 |
| 機構 | 中性 | 低 | 持股高度集中，無趨勢資料 |
| 散戶 / 社群 | 無資料 | — | Reddit、StockTwits 不可取得，WebSearch 無足夠討論樣本 |

**綜合分數：中性偏多（信心：中低）。** 有效資料僅來自分析師與內部人兩個面向，且散戶面缺席，故不能完整判斷情緒。

**背離旗標：無法判定（DATA_UNAVAILABLE）。** 散戶語調無資料，無法與分析師偏多的語調做比較。若後續取得 Reddit 或 StockTwits 資料，需特別確認是否出現散戶偏空而分析師偏多的情況。

## Data gaps and follow-ups

1. Reddit（r/wallstreetbets、r/stocks）與 StockTwits 因網路封鎖無法取得，需於 session 網路設定中放行相關網域。
2. yf 工具未提供目標價與個別券商評等明細，需另行取得。
3. 當日股價與 Q3 2026 財報實際結果未確認，建議核對後再使用本報告的目標價與估值段落。
4. 機構持股趨勢需要歷史 13F 資料，目前無法取得。

## Sources (WebSearch, 聚合來源，日期不一)

- https://www.barchart.com/story/news/42954/is-wall-street-bullish-or-bearish-on-american-tower-stock
- https://finance.yahoo.com/news/wall-street-thinks-american-tower-144531879.html
- https://www.marketbeat.com/instant-alerts/american-tower-corporation-nyseamt-receives-consensus-rating-of-moderate-buy-from-brokerages-2026-07-23/
- https://www.tikr.com/de/blog/american-tower-stock-is-down-20-over-the-past-year-analysts-see-33-upside-to-238-target

SENTIMENT REPORT COMPLETE
