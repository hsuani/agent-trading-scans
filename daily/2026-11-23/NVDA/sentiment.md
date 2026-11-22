# Sentiment — NVDA as of 2026-11-23

資料時點說明：價格與 yf 快取更新於 2026-11-22 14:32 UTC，最新收盤為 2026-11-20（週五，USD 125.53）。Live yf 呼叫在本次執行中多數失敗（CONNECT 403），分析師評級、內部人交易與持股資料改以 `prices/yf/NVDA.json` 快取為準。Reddit / StockTwits / nasdaq.com 無法直接存取，散戶情緒改以 WebSearch 彙整之二手報導為主，樣本量不可量化。

## Analyst consensus

以 `rec_summary` 快取計算（單位：家數）：

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 合計 | 買方占比 |
|---|---|---|---|---|---|---|---|
| 本月（0m） | 11 | 34 | 16 | 2 | 0 | 63 | 約 71% |
| 上月（-1m） | 10 | 49 | 2 | 1 | 0 | 62 | 約 98% |

- 評級結構在一個月內明顯轉弱：Buy 由 49 降至 34（減少 15 家），Hold 由 2 增至 16（增加 14 家），買方占比由約 98% 降至約 71%。
- 近期事件與 WebSearch 報導吻合：Baird 於 11/11 降至 Neutral、目標價由 500 降至 200 USD；Bernstein 於 11/12 降至 Market Perform、目標價減半至 200 USD；WebSearch 來源提及約十家機構在 11/11 至 11/13 之間下調評級（含 Evercore ISI、Melius、Oppenheimer、KeyBanc、Truist，來源為 Webull 彙整，需自行核對）。Morgan Stanley 則是依停損規則將 NVDA 移出 Top Picks，並非正式降評。
- 目標價：快取之 targetMean 為 244.18 USD、最高 425 USD、最低 130 USD，相對現價 125.53 USD 仍有約 94% 上行空間。但已知多家大幅下修目標價，平均值明顯落後於實際調整，**此數字不宜當作可信上行參考**。最低目標 130 USD 幾乎貼近現價。
- 快取 `numberOfAnalystOpinions` 為 56，與 rec_summary 合計 63 略有出入（不同來源計算口徑不同），以 rec_summary 為準。
- 盈餘：2026-11-17 報告 EPS 2.68 USD，優於預期 2.47 USD（+8.4%）。盈餘超預期後股價仍走弱，市場焦點顯然不在當季數字。

## Retail social

- **Reddit（r/wallstreetbets、r/stocks）**：無法直接抓取。WebSearch 轉引之二手報導（Reuters 系列）指出 WSB 上關於 NVDA 未來走向的負面留言占比高達約 60%，語氣偏空。這是樣本留言比例，非嚴謹民調。
- **StockTwits / X**：StockTwits 無法直接存取。二手報導呈現分歧：
  - 一則 StockTwits 文章稱「retail sentiment 仍 extremely bullish」，並引用民調顯示 58% 散戶在買進跌勢，但該文未標註日期，且內文提及之「Huang 離任」無法由其他來源證實，**視為未驗證**。
  - Vanda Research 資料（經多家媒體轉引，屬同一來源而非獨立佐證）顯示，散戶於 11/13 當週淨買入約 2.0B USD，另一版本為約 1.6B USD（三個交易日）。
  - 同份資料亦指出，截至 11/16，被追蹤散戶組合中 8.9% 已減持 NVDA，僅 2.7% 加碼，顯示熱度降溫。
- **Buzz 量（定性）**：11 月初以來討論量明顯高於平常水準（與跌幅與領導層新聞相關）；但無法取得可比較之提及數，僅能定性描述為「高於一般、以負面議題為主」。
- **Themes（主要議題）**：
  1. 領導層不確定性：CEO 人事與個人操守報導。報導版本分歧（「辭任」與「董事會擬罷免」兩種說法並存），**目前無可靠一手確認**。
  2. 2027 年資料中心需求能見度：Baird 降評之主要理由，亦是 WSB 討論焦點。
  3. 監管與調查：WSJ 報導 SEC 調查（二手轉引，未直接核實），以及晶片出口管制疑慮。
  4. 逢低買進：散戶資金流入與「dip buying」敘事並存。
  5. 估值：快取 trailing P/E 約 13.5x、forward P/E 約 7.6x，部分散戶以此論述「便宜」，但也有人質疑盈餘可持續性。
- 代表性標題（二手來源，非原文引用）：「Bernstein Just Gave Up on Nvidia, Cutting Its Target in Half to $200」、「Are Retail Traders Still Buying The Dip?」。
- **散戶傾向**：WSB 偏空、資金流偏多頭（逢低買）、組合層面偏減持。整體為**混合偏空**。

## Insider activity

統計區間：2026-05-23 至 2026-11-22（近 6 個月），以 `insider` 快取計算。

- **Open-market 買進：0 筆、0 USD。** 近 6 個月無任何公開市場買進。
- **Open-market 賣出：約 1.37B USD（約 1,370.5M USD）**，主要由以下人員構成：

| 日期 | 姓名 | 職位 | 股數（萬股，約） | 金額（M USD） |
|---|---|---|---|---|
| 2026-09-02 | Mark A. Stevens | Director | 185 | 410.8 |
| 2026-09-18 | Mark A. Stevens | Director | 137 | 300.1 |
| 2026-09-04 | Mark A. Stevens | Director | 102 | 235.6 |
| 2026-06-04 | Mark A. Stevens | Director | 100 | 221.1 |
| 2026-06-18 | Mark A. Stevens | Director | 88.5 | 186.0 |
| 2026-09-21 | Timothy S. Teter | General Counsel | 3.0 | 6.8 |
| 2026-08-31 | Timothy S. Teter | General Counsel | 3.0 | 6.5 |
| 2026-06-03 | Stephen C. Neal | Director | 1.6 | 3.3 |

- Stevens（董事）為主要賣方，6 個月內合計約 1.35B USD，成交價區間約 210 至 234 USD，遠高於目前 125.53 USD。
- CEO Jen-Hsun Huang 與 CFO Colette Kress 於 6 個月內無公開市場賣出（Kress 最近一次賣出為 2026-03-20，已超過 6 個月）。
- 非現金交易（不計入上表）：Huang 於 2026-06-16 贈與 40 萬股；Coxe 於 9/2、8/5、7/1 各贈與 50 萬股；Stevens 於 6/4 贈與 30.75 萬股。另有多筆董事與高管獎勵股（Grant）。
- **解讀限制**：快取資料未標註是否為 10b5-1 計畫交易，無法判斷賣出是否屬預先安排。賣出價格集中於股價高點（210 至 234 USD），與目前約 125 USD 之價差約 43% 至 47%，顯示賣方並非在低點出脫。

## Ownership shifts

- 機構持股占比 71.6%，機構數 7,813 家；內部人占比 4.04%（快取 `major_holders`）。
- 前三大持股（2026-09-30 申報）：BlackRock 8.05%（季變化 -0.05%）、Vanguard 6.39%（-0.01%）、State Street 4.25%（+1.51%）。
- 前三大持股整體變化不大，State Street 為唯一明顯加碼者。快取僅提供單一季度之 `pctChange`，無法判斷機構持股之多季趨勢。下一季 13F 資料出爐前，無法確認此週期內機構是否在跌幅中撤退。

## Net sentiment score

- **分析師（水平）**：多數仍為 Buy（約 71%），但評級結構在一個月內大幅轉向 Hold。方向性為負，水平仍偏正。
- **散戶**：WSB 負面（約 60% 負面留言）；資金流與逢低買進敘事偏正，情緒指標與組合減持偏負。整體混合偏空。
- **內部人**：近 6 個月無公開市場買進、約 1.37B USD 賣出，但賣價遠高於現價，且無法確認是否為預定計畫，訊號偏空但解讀空間大。
- **綜合評分：中性偏空（信心：中等）**。主要依據：評級結構快速轉弱、散戶社群偏空、內部人淨賣出；反向因素為評級仍以買方為多、估值倍數偏低、盈餘超預期。

**Divergence flag：是**。分析師評級仍以 Buy 為主，但其動向（大量降評）偏空；散戶社群（WSB）偏空，而散戶資金流呈逢低買進。兩類群體對 NVDA 的短期方向判斷不一致，是本次報告最需留意的訊號。

## 資料限制與待核實事項

1. 無法直接存取 Reddit / StockTwits，散戶情緒全部來自二手彙整，樣本與時間不可控。
2. Huang 的人事狀態（辭任或被罷免）報導互相矛盾，未獲一手確認。
3. SEC 調查、Vanda 資金流數字均屬二手轉引，數字間有出入（2.0B vs 1.6B USD）。
4. 11/20 之單日跌幅（快取顯示 145.98 → 125.53，約 -14%）未在 WebSearch 中獲得獨立證實；WebSearch 結果提及的價位（約 163 USD）與快取價格亦不一致，以快取為準。
5. 分析師目標價平均值（244 USD）顯著落後於已知之下修，參考價值有限。

SENTIMENT REPORT COMPLETE
