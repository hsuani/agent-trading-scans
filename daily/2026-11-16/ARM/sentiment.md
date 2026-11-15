# Sentiment — ARM as of 2026-11-16

資料說明：Reddit 與 StockTwits 直接抓取皆失敗（Reddit 被擋；api.stocktwits.com 無法解析），散戶面僅能以 WebSearch 彙總的第三方摘要判讀，可信度偏低。Yahoo cookie/crumb 取得失敗，評級與持股資料為工具回傳值，部分來源有日期落差（見各節）。

## Analyst consensus

分析師評級分布（yf rec_summary，期間 0m，共 43 家）：

| 評級 | 家數 | 占比 |
|---|---|---|
| Strong Buy | 8 | 19% |
| Buy | 20 | 47% |
| Hold | 14 | 33% |
| Sell | 1 | 2% |
| Strong Sell | 0 | 0% |

Buy 合計 28 家（65%），Hold 14 家，Sell 1 家。近 4 個月趨勢：Strong Sell 由 0（0m、-1m）變為 1（-2m、-3m），Buy 由 20–21 家變動不大，Hold 在 12–14 之間來回。yf 的 0m 與 -1m 數字完全相同，表示本月初至今評級分布無結構性變化，但工具未提供個別升降評等的日期與機構名稱。

近期目標價與評等動作（WebSearch 結果，日期需留意）：
- Barclays（2026-11-05）：目標價由 $360 下調至 $325，維持 Overweight。
- TIKR 報導：財報後約 9 家機構下調目標價，平均目標價約 $273，高於 11-10 收盤價 $181.49，但未取得各家明細。
- Morgan Stanley：由 Overweight 降至 Equal-Weight，目標價 $185 降至 $150。來源未標日期，無法確認是否屬本期。
- Goldman Sachs：降為 Sell，目標價 $120（原 $160）。來源為 2025-12-15，屬舊聞，不列入本期。
- MarketBeat 有一則「19 Buy / 7 Hold / 1 Sell」的數字，與 yf 的 43 家口徑不同，且頁面標示為 2026 年 1 月，視為過時，本報告以 yf 為準。

## Retail social

- Reddit：r/wallstreetbets 與 r/stocks 搜尋皆無法抓取（被擋）。SentiSense（截至 2026-11-08）顯示 ARM 30 日情緒為中性且降溫，其中 Reddit 來源標為偏空。無法取得本週貼文樣本，也無法量化討論量。
- StockTwits / X：StockTwits 無法連線。LunarCrush 頁面宣稱近 24 小時約 2.8K 則貼文、98% 正向，但該數字無明確日期，可信度低，不採計入綜合判斷。SentiSense 的 X 來源標為偏空。
- 討論量：無法與常態基準比較，只能定性判斷。財報後（11-05 起）有多篇「該賣還是該買」類型的文章，顯示市場討論度在提高，但缺乏可驗證的提及次數。
- 主要議題（依 WebSearch 摘要歸納）：
  1. 財報後股價重挫：11-05 股價約跌 13%，原因是 royalties 只成長 8%（營收 +27% 至 $1.44B 創紀錄，EPS 優於預期）。
  2. 估值爭論：TIKR 指出 ARM 的銷售倍數仍遠高於 QCOM、AMD，散戶對「高估值是否合理」有分歧。
  3. 記憶體價格與手機出貨：Barclays 與多家機構將 royalties 放緩歸因於記憶體成本壓抑手機需求。
  4. SoftBank 相關的循環融資疑慮與晶片族群的連動下跌（Intel 警告事件後）。
  5. 買低派的論調：Barclays 認為賣壓過度，此類論點在財經媒體被引用較多。

## Insider activity

Net 6mo（2026-05-16 至 2026-11-15）：$0M 公開市場買入，約 $45.4M 賣出（13 筆，6 位內部人）。

| 內部人 | 職稱 | 期間賣出（USD M） | 筆數 | 備註 |
|---|---|---|---|---|
| Jason E. Child | CFO | 13.0 | 3 | 05-20、08-27、09-21，價格 $226–$300 |
| William Abbey | Officer | 9.9 | 5 | 05-20 至 06-01，價格 $287–$415 |
| Spencer Collins | Officer | 8.8 | 1 | 05-19，$215 |
| Richard Roy Grisenthwaite | Officer | 5.1 | 1 | 05-18，$209 |
| Laura K. Bartels | Officer | 4.4 | 1 | 06-02，$393 |
| Charlotte C. Eaton | Officer | 4.2 | 2 | 05-21，$252–$291 |

- CEO René Haas：窗口內無公開市場交易，僅有 08-31 的 64 股獎勵與 05-15 的 265,643 股授予（價值 0，非現金買入）。他在 03-26 與 04-14 有賣出，屬窗口之前。
- 董事（Jacobs、Sohn、Schooler、Sine）於 05-15 有小額股票取得或處置，無公開市場買入，Sine 於 08-07 有贈與 9,572 股。
- 窗口前緣有兩筆較大賣出未計入：Collins 05-11 約 $11.0M、Abbey 05-15 約 $2.2M。若納入，6 個月賣出約 $58.6M。
- 05-15 與 08-17 有多筆 Form 4 無金額（可能為稅務代扣或 RSU 歸屬），未計入。
- 解讀：內部人持續賣出，且多數賣出價位高於現價（11-10 約 $181，11-13 收盤約 $190）。此為「高位獲利了結」型態，但無買入對沖。

## Ownership shifts

- 機構持股 95.8%，機構數 1,297 家；內部人持股 0.14%（低）。
- 前十大機構（持股變化為最近一期申報對比）：
  - Invesco 13.2M 股，+3.0%（09-30）
  - Dz Bank 6.5M 股，-30.6%（06-30）
  - Arrowstreet 4.1M 股，+333%（06-30）
  - Capital Research Global 3.2M 股，+34.9%（09-30）
  - Goldman Sachs 2.9M 股，+79.3%（06-30）
  - Van Eck 2.6M 股，+17.5%（06-30）
  - Morgan Stanley 2.2M 股，-51.7%（06-30）
  - FMR 2.2M 股，-46.4%（09-30）
  - BlackRock 2.0M 股，+63.8%（06-30）
  - Capital International 2.0M 股，-0.1%（09-30）
- 趨勢：前十大中增減混合，減持者（Morgan Stanley、FMR、Dz Bank）與增持者（Arrowstreet、Goldman、BlackRock）大致對半，無明確集中或分散方向。申報有 45 天左右的延遲，且 06-30 與 09-30 的數字不同步。

## Net sentiment score

- 分析師面：偏多（65% Buy），但近期目標價大幅下修，且 Strong Sell 出現，偏多信號正在鬆動。信心：中。
- 散戶面：中性偏空（SentiSense 30 日中性降溫，Reddit 標偏空；LunarCrush 正向數字不可驗證）。信心：低，因 Reddit 與 StockTwits 無法取得原始樣本。
- 內部人面：偏空（6 個月約 $45.4M 賣出、零公開市場買入）。信心：中，但 CEO 未賣出且多為既定計畫性質，無法確認。
- 綜合：中性偏空（neutral-to-bearish），信心中低。

Divergence flag：是。分析師整體偏多，散戶與內部人偏空，兩者方向相反。此類分歧通常代表市場對獲利與估值的疑慮尚未被分析師目標價完全反映，但因散戶數據樣本不足，此訊號僅供參考。

資料缺口與後續：
1. Reddit 與 StockTwits 需在 session 網路設定中允許連線後重抓。
2. 分析師目標價的個別機構明細（尤其 9 家下修者）需補查。
3. 股價來源不一致（11-10 收盤 $181.49、11-13 收盤 $190.53、另一來源 $310 明顯過時），使用前需以行情工具核對。

SENTIMENT REPORT COMPLETE
