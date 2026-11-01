# Sentiment — ARM as of 2026-11-02

## 資料可得性
- Reddit（r/wallstreetbets、r/stocks）：WebFetch 遭封鎖（無法連線），本次無貼文樣本。
- StockTwits：api.stocktwits.com 無法解析（不在session允許網域內），本次無資料。需由使用者於session網路設定中允許該網域後才能重試。
- X / 新聞：WebSearch 可用，但最新可得的分析師動態約到 2026-07-22，2026-08 至 2026-11-02 之間的社群與評論資料幾乎缺席。
- 結論：散戶面為資料缺口，不應解讀為中性證據。

## Analyst consensus

yf `rec_summary`（當前共 43 位分析師，期間 0m 為現況）：

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 合計（家） | 買方占比 |
|---|---|---|---|---|---|---|---|
| 0m（現況） | 8 | 20 | 13 | 1 | 1 | 43 | 65% |
| -1m | 8 | 21 | 12 | 1 | 1 | 43 | 67% |
| -2m | 7 | 20 | 13 | 1 | 1 | 42 | 64% |

現況為 28 買 / 13 持有 / 2 賣（買方占比 = (Strong Buy + Buy) / 合計，已重算：28 / 43 ≈ 65%）。兩個月內評級分布穩定，賣方家數維持 2 家。

近期評級與目標價變動（WebSearch 聚合，yf 工具未提供逐家異動紀錄，以下需以券商原始報告核對）：
- HSBC（2026-07-14）：Buy 降為 Hold，目標價由 255 升至 315 USD。
- Wells Fargo（2026-07-22）：目標價由 410 降至 350 USD，維持 Overweight。
- Morgan Stanley（2026-05-18）：降為 Equal-Weight，目標 150 USD（單一來源）。
- 2026 年前半其他動態：Needham 升 Buy（目標 200 USD，2026-04-07）、Raymond James 升 Outperform（目標 166 USD，2026-03-26）、BofA 降 Neutral（目標 120 USD，2026-03-20）、Goldman 維持 Strong Sell（目標 125 USD，2026-04-09）、Bernstein 首次 Outperform（目標 300 USD）。
- 某聚合頁面提及平均目標價約 297.65 USD，日期不明，僅供參考。
- 未證實：另一來源稱 Bernstein 將目標價由 300 上調至 500 USD，來源品質不穩，本報告未採用。

價格脈絡（USD，供解讀內部人交易價位）：2026-03 約 148；2026-06-22 創 445.05 高點（兩年高）；2026-06-23 單日回落約 10% 至約 367；2026-09-08 約 258；2026-09-21 內部人賣出價 300。2026-11-02 收盤價未取得。

## Retail social

- Reddit：無法取得（封鎖）。
- StockTwits / X：StockTwits 無法取得；WebSearch 未找到 r/wallstreetbets 或 r/stocks 的 ARM 討論串，無法引用散戶貼文。
- 聲量（buzz volume）：無法量化，與典型水準比較留空。
- 散戶傾向（tilt）：無法判定（零樣本）。媒體端近期論述偏中性至偏空，見下列主題。
- 主要敘事（取自新聞與分析文章，非散戶本身）：
  1. 估值擔憂：有評論認為股價已領先基本面，爭點集中在外年度成長目標能否達成；另有「市值暴增、泡沫警示」類標題（日期不明）。
  2. 波動度偏高：一篇 2026-06 文章引用 30 日歷史波動率 113.1%，長期平均 55.3%。
  3. 多頭論點：2026 年內股價大幅上漲（6 月時年初至今漲幅約 235%），AI 工作負載需求為主要題材。
  4. 分析師評級在 7 月出現降級（HSBC），顯示機構也在重新檢視估值。
- 可引用的散戶原文：無（未取得貼文樣本）。

## Insider activity

視窗：2026-05-02 至 2026-11-02（6 個月）。

淨額：公開市場買入 0 筆（0 USD）；公開市場賣出 15 筆，合計約 58.5 M USD。

| 內部人 | 職稱 | 賣出筆數 | 金額（USD M） | 期間 |
|---|---|---|---|---|
| Collins Spencer | Officer | 2 | 19.8 | 05-11、05-19 |
| Child Jason E | CFO | 3 | 13.0 | 05-20、08-27、09-21 |
| Abbey William | Officer | 6 | 12.0 | 05-15 至 06-01 |
| Grisenthwaite Richard Roy | Officer | 1 | 5.1 | 05-18 |
| Bartels Laura Kathleen | Officer | 1 | 4.4 | 06-02 |
| Eaton Charlotte Claire | Officer | 2 | 4.2 | 05-21 |
| 合計 | | 15 | 58.5 | |

重點觀察：
- 賣出高度集中於 2026-05-11 至 06-02，約 52.7 M USD（13 筆）；之後僅 CFO Child 於 08-27 與 09-21 兩筆，合計約 5.8 M USD。
- CEO Rene Haas 於本視窗內無公開市場交易。其最後一次賣出為 2026-03-26 與 04-14（視窗外）。窗口內僅有 2026-05-15 年度授予（265,643 股，以 0 USD 計）與 2026-08-31 授予（64 股，約 15.5 K USD）。
- 董事 Jeffrey Sine 於 2026-08-07 有一筆股票贈與（非現金，不計入淨額）。董事無公開市場買入。
- 驗算：CFO Child 2026-05-20 賣出 31,920 股 × 226.54 USD ≈ 7.23 M USD，與工具值吻合。
- 2026-05-15 有多筆 Value 為空白的交易，性質（推測為歸屬或稅款代扣）無法從工具確認，本報告未計入。
- 賣出是否屬於預定 10b5-1 計畫無法從本工具判定，此點為主要不確定性。

## Ownership shifts
- 內部人持股：0.073%（極低）。
- 機構持股：96.25%，機構家數 1,295。
- 持股變化趨勢：工具僅提供單一時點快照，無法判定季度間增減，留空。

## Net sentiment score

- 分析師面：偏多（買方占比約 65%，近兩個月穩定；但 7 月有 HSBC 降級，目標價分散度大）。
- 內部人面：偏空（6 個月約 58.5 M USD 淨賣出、零買入；賣出集中於 5 月中至 6 月初；CFO 於 8、9 月仍持續賣出）。
- 散戶面：無資料。
- 綜合：中性，信心低。分析師偏多與內部人淨賣出方向相反，但散戶面缺席，無法完成三方判斷。

Divergence flag：無法判定（散戶資料缺席，無法檢驗「散戶與分析師方向相反」）。但分析師（偏多）與內部人（淨賣出）之間存在明確分歧，此分歧值得後續驗證 10b5-1 計畫與賣出動機。

## 限制與待辦
- 價格基準以 2026-09-08 為最近可得點，2026-11-02 價格未知。
- 下一次財報日期未確認：Capital.com 估計 2026-11-04 盤後，Earnings Whispers 列為 2026-11-09 盤後。若落在 DATE 之後，視為未知，不納入判斷。
- WebSearch 來源品質不一，部分鏡像網站已排除。
- 重跑建議：Reddit 與 StockTwits 網域放行後重新抓取；並取得 SEC Form 4 的 10b5-1 旗標。

## 來源
- [Capital.com ARM 預測](https://capital.com/en-eu/analysis/arm-holdings-stock-forecast)
- [Barchart：分析師降級](https://www.barchart.com/story/news/3282839/this-analyst-just-downgraded-arm-stock-here-s-why)
- [Benzinga：多空論點](https://benzinga.com/z/34919903)
- [MarketBeat：Wells Fargo 2026-07-22](https://www.marketbeat.com/instant-alerts/wells-fargo-company-issues-pessimistic-forecast-for-arm-nasdaqarm-stock-price-2026-07-22/)
- [Quantisnow ARM 動態](https://qnow.quantisnow.com/ticker/ARM)
- [247wallst：2026-06-23 回落](https://247wallst.com/investing/2026/06/23/arm-stock-is-up-235-in-2026-is-todays-10-drawdown-a-take-profits-signal/)
- [Earnings Whispers ARM](https://beta.earningswhispers.com/go/w/ARM)

SENTIMENT REPORT COMPLETE
