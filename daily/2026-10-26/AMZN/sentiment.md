# Sentiment — AMZN as of 2026-10-26

> 資料註記：系統日期為 2026-10-25，本報告依任務指定以 2026-10-26 為 as-of 日。分析師評級快照無原始日期標記；內部人交易最新一筆為 2026-10-01；網路新聞搜尋結果多為 2026 年 7 月至 9 月。以下凡標註「過時」者，不代表 10/26 當日狀態。

## Analyst consensus

| 項目 | 數值 | 備註 |
|---|---|---|
| Strong Buy | 16 | |
| Buy | 42 | |
| Hold | 2 | |
| Sell | 0 | |
| Strong Sell | 0 | |
| 合計 | 60 | 買入側 (Strong Buy + Buy) 58，佔 97% |

評級趨勢 (yf rec_summary 四個快照，時間順序由舊到新)：

| 快照 | Strong Buy + Buy | Hold | Sell |
|---|---|---|---|
| -3m | 61 | 3 | 0 |
| -2m | 61 | 2 | 0 |
| -1m | 59 | 2 | 0 |
| 0m (現況) | 58 | 2 | 0 |

近三個月買入側評級由 61 降至 58，Hold 由 3 降至 2，無 Sell 評級。買入側小幅減少，但整體仍為明顯偏多。

近期評級異動與目標價 (網路搜尋，過時，約 2026 年 7 月底至 8 月初，Q2 2026 財報後)：
- Benchmark 目標價 $400 (由 $370 上調)，為最高目標價。
- JPMorgan 目標價 $365 (由 $330 上調)，維持 Best Idea。
- Truist $350 (由 $320 上調)；Citigroup $350 (由 $325 上調)。
- Bank of America $320 (由 $310 上調)，維持買進。
- Wedbush $310 (由 $293 上調)，維持 Outperform。
- Cantor Fitzgerald $320 (由 $330 下調)，維持 Overweight。
- MarketBeat 平均目標價約 $322.56 (8 月初快照)。
- Goldman Sachs (Eric Sheridan) 目標價 $335，維持 Buy，日期 DATA_UNAVAILABLE。

yf 工具未提供逐筆升降評等 (upgrade / downgrade) 歷史，逐筆異動明細為 DATA_UNAVAILABLE。10/26 當日最新目標價為 DATA_UNAVAILABLE。

## Retail social

- Reddit (r/wallstreetbets, r/stocks)：DATA_UNAVAILABLE。WebFetch 回傳無法存取 www.reddit.com，兩個子版均未取得貼文樣本，無法判定 tilt 與熱度。
- StockTwits：DATA_UNAVAILABLE。API 回傳 DNS 解析失敗 (api.stocktwits.com 無法解析)，無訊息樣本。
- X / 新聞聚合 (WebSearch)：無法取得 10 月 X 貼文樣本。搜尋結果顯示的是期權流向與分析師意見的第三方彙整，而非散戶貼文本身。
- 期權流向 (Benzinga 等，時間不一)：多個快照互相矛盾，一次為 64% 偏多 / 21% 偏空，另一次為 40% 偏多 / 44% 偏空，再一次為 33% 偏多 / 57% 偏空；Nasdaq 文章為 34% 偏多 / 47% 偏空。Historical Option Data 於 9/2 至 9/3 記錄過偏多的 call 集中流向。整體屬「混合偏中性」，但日期分散，不具當前代表性。
- 熱度量化 (提及次數 vs 常態)：DATA_UNAVAILABLE。

主要題材 (取自新聞與分析師摘要，非散戶貼文原文，因此不附引文)：
- AWS 成長：Q2 2026 AWS 年增約 37%，為 18 季來最快；AWS 積壓訂單約 $496B。多方主要論點。
- 資本支出：Q2 2026 資本支出指引上調至約 $220B。多方認為是 AI 基礎建設投入；空方擔憂獲利壓力與 AI 投資回收期。
- 消費端：Goldman Sachs 點名消費支出與 AI 投資是需留意的風險。
- Prime Day 與電商：分析師認為銷售表現健康。

## Insider activity

視窗：2026-04-26 至 2026-10-26 (6 個月)。來源：yf insider，共 150 筆。

| 項目 | 金額 (USD M) | 筆數 | 備註 |
|---|---|---|---|
| 公開市場買入 | 0 | 0 | 無 |
| 公開市場賣出 (合計) | 402.7 | 23 | 含 Bezos 單筆 346.5M |
| 賣出 (剔除 Bezos) | 56.3 | 22 | 主要為高階主管 |
| 贈與 (Stock Gift，無金額) | 不計 | 3 | Bezos 415,580 股 (8/26)；Herrington 22,000 股 (8/6) 等 |
| 金額缺漏 (Value = null) | 不計 | 17 | 性質 DATA_UNAVAILABLE，多為同日成批列示之歸屬或行權紀錄，未逐筆核實 |

依人員彙總 (賣出 USD M)：

| 人員 | 職稱 | 筆數 | 金額 (USD M) |
|---|---|---|---|
| Jeffrey P. Bezos | Officer and Director | 1 | 346.5 (8/3，1,209,649 股 @ $286.41) |
| Andrew R. Jassy | CEO | 3 | 19.1 |
| Douglas J. Herrington | Officer | 10 | 14.4 |
| Matthew S. Garman | Officer | 3 | 10.9 |
| David A. Zapolsky | Officer | 2 | 8.1 |
| Brian T. Olsavsky | CFO | 1 | 1.6 |
| Shelley L. Reynolds | Officer | 2 | 1.2 |
| Jonathan J. Rubinstein | Director | 1 | 1.0 |

Notable：
- Bezos 8/3 單筆賣出 1,209,649 股，約 $346.5M，為視窗內最大單筆。其 8/26 之 415,580 股為贈與，非賣出。此類大額個人持股調整常見於既定計畫，不宜單獨解讀為看空訊號，需 DATA_UNAVAILABLE 之 Form 4 附註佐證。
- Jassy (CEO) 於 5/21、8/21 各賣出 20,000 股 (約 $5.3M、$5.2M)，為 CEO 層級的主要賣出。
- Olsavsky (CFO) 8/21 賣出 6,172 股，約 $1.6M。
- 賣出多集中於 2 月、5 月、8 月、11 月的約 21 日前後，與 2025 年同期模式相近，屬例行性質的可能性高，但是否為 10b5-1 計畫或 RSU 歸屬，DATA_UNAVAILABLE。
- 最近一筆為 Herrington 10/1 之 1,000 股 @ $251.50，為小額、規律性交易。

## Ownership

yf major_holders 為單一快照，無歷史序列：
- 內部人持股：8.85%
- 機構持股 (佔流通股外之總股本)：68.84%
- 機構持股 (佔流通股)：75.53%
- 機構持有人數：7,901 家

機構持股比例的季度趨勢：DATA_UNAVAILABLE (工具無歷史資料)。前十大機構名單與增減：DATA_UNAVAILABLE。

## Net sentiment score

**綜合傾向：偏多 (bullish lean)，信心：中低。**

分項判斷：
- 分析師：偏多，信心高 (評級分布明確)，但目標價與異動資料偏過時，且評級數量近三個月微降。
- 散戶社群：中性偏混合，信心低。Reddit 與 StockTwits 皆無法取得，僅有期權流向彙整，且日期分散、互相矛盾。
- 內部人：中性偏空，信心中。6 個月內無任何公開市場買入，賣出總額 $402.7M 中 86% 來自 Bezos 單筆；剔除後 $56.3M 仍以高階主管例行賣出為主。但賣出多屬季度性且規模相對 AMZN 市值不大。
- 持股結構：機構持股高度集中且穩定，無趨勢資料，不加權。

信心受限原因：散戶訊號缺失 (Reddit、StockTwits DATA_UNAVAILABLE)，分析師目標價與新聞為 7 至 9 月資料，10/26 當日股價為 DATA_UNAVAILABLE。

**Divergence flag：否 (無法確認)。** 分析師偏多與內部人賣出並存，但兩者方向並不相反，內部人賣出多為例行性質。散戶 tilt 因資料缺失無法判定，因此無法確認是否與分析師相反。若取得 Reddit 或 StockTwits 資料後，應重新評估此旗標。

## 資料缺失清單

- Reddit (r/wallstreetbets、r/stocks)：DATA_UNAVAILABLE (存取受阻)
- StockTwits：DATA_UNAVAILABLE (DNS 失敗)
- 散戶提及次數與熱度基準：DATA_UNAVAILABLE
- 逐筆分析師升降評等與目標價歷史：DATA_UNAVAILABLE
- 10/26 當日股價與最新目標價：DATA_UNAVAILABLE
- 17 筆內部人交易之金額：DATA_UNAVAILABLE
- 機構持股歷史趨勢與前十大持有人變化：DATA_UNAVAILABLE

SENTIMENT REPORT COMPLETE
