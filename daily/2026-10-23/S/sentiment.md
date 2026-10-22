# Sentiment — S (SentinelOne) as of 2026-10-23

資料來源狀態: yf 工具可用（analyst、insider、holders）；Reddit JSON 無法連線（Claude Code 回報 unable to fetch）；StockTwits DNS 解析失敗（getaddrinfo ENOTFOUND），兩者皆 soft-fail。散戶面向改以 WebSearch 結果代替，僅能定性。

## Analyst consensus

近期 yf rec_summary（當期快照，USD 不適用）: **34 家覆蓋**，Strong Buy 3 / Buy 15 / Hold 16 / Sell 0 / Strong Sell 0。
- 買進側（Strong Buy + Buy）= 18 家，佔 **52.9%**；Hold 16 家，佔 47.1%；Sell 0。

過去 3 個月趨勢（yf recommendations，買進側家數 / Hold 家數）:

| 期間 | 買進側 | Hold | 買進佔比 |
|---|---|---|---|
| -3m | 22 | 13 | 62.9% |
| -2m | 21 | 14 | 60.0% |
| -1m | 19 | 15 | 55.9% |
| 當期 | 18 | 16 | 52.9% |

解讀: 無賣出評級，但買進佔比三個月內下降約 10 個百分點，Hold 家數增加 3。此為評級向中性收斂，非翻空。

近期動作（WebSearch，MarketBeat / Google Finance 快照，未逐筆於 EDGAR 驗證）:
- 10/02 TD Cowen: 目標價 $26 → $29，維持 Buy。
- 10/06 Yorkville Ives & Co.: 首次覆蓋，Buy，目標 $32。
- 10/06 FBN Securities: 降評至 Hold，目標 $24。
- 10/13 Needham（Mike Cikos）: 維持 Buy，目標 $31。

目標價: MarketBeat 平均 $23.92；Google Finance 快照平均約 $25.13，高 $32、低 $17.50。來源之間計數不一致（Google Finance 3 個月口徑為 18 Buy / 13 Hold / 0 Sell，共 31 家；WSJ 引述 39 家），以 yf 為主。

股價背景: 10/13 MarketBeat 報導盤中跳空低開至 $23.46，回升至約 $25.03；前收 $25.66；市值約 USD 8.68B。平均目標價約等於現價，共識上行空間有限。

## Retail social

- **Reddit**: 無法存取（Claude Code 回報 unable to fetch）。WebSearch 以 r/wallstreetbets、r/stocks 相關查詢均未找到 S 的 Reddit 討論串，無法量測 tilt。
- **StockTwits**: 無法存取（DNS 解析失敗）。
- **X / 部落格 / 新聞**（WebSearch 代理）:
  - 偏空聲音: 一篇被 Insider Monkey 引用的 Substack 作者建議賣出，理由是營收成長放緩與管理層撤回營收指引，儘管自由現金流仍在成長。Nasdaq 文章指出股價約 $13 且一年跌幅超過 30%，理由為保守指引、大型競爭者、AI 衝擊 SaaS 的擔憂（此文時間點偏早，與目前 $25 不一致，視為過時）。
  - 偏多聲音: 同一類媒體引用 FY2026 營收超過 $1B、非 GAAP 獲利、FY2027 約 20% 營收成長指引。TipRanks 顯示 Blogger 情緒 88% 看多，但樣本僅 27 則，且多數來自 Seeking Alpha 文章而非散戶論壇，權重低。
- **Buzz 量**: 無法量化。可見討論以財經媒體與分析師文章為主，散戶社群聲量在搜尋結果中不明顯，判定為低至中等、以媒體驅動。
- **Tilt**: 混合偏空（以近期指引與內部人賣出為主要論點），信心低。

主要主題（WebSearch 所見）:
1. 近期指引保守、營收成長放緩（偏空）。
2. 與大型平台競爭、AI 衝擊 SaaS 估值（偏空）。
3. FY2026 營收破 $1B、已達非 GAAP 獲利（偏多）。
4. 高層密集出售股票（偏空敘事）。
5. 分析師評級仍以 Buy 為主，無 Sell（偏多）。

## Insider activity

統計區間: 2026-04-23 至 2026-10-22（6 個月）。USD 單位為 **百萬美元 (USD M)**。

| 項目 | 金額 (USD M) | 備註 |
|---|---|---|
| 公開市場賣出（Sale，共 42 筆） | 約 32.0 | 工具判定 Sale 類別 |
| 公開市場買入 | 0.0 | 6 個月內無買入 |
| 淨額 | 約 -32.0 | 淨賣出 |

依人員（賣出金額，USD M）:

| 人員 | 職稱 | 賣出金額 | 賣出股數 |
|---|---|---|---|
| Tomer Weingarten | CEO | 25.8 | 約 1.26M 股 |
| Sonalee Parekh | CFO | 2.6 | 約 120K 股 |
| Robin Tomasello | Officer | 1.0 | 約 55K 股 |
| Keenan Conder | Officer | 0.9 | 約 48K 股 |
| Barry Padgett | President | 0.9 | 約 41K 股 |
| Ana Pinczuk | Officer & Director | 0.8 | 約 38K 股 |

Notable:
- **CEO Tomer Weingarten**，2026-10-05 賣出 527,368 股，成交價 $25.26，約 USD 13.3M；同日另有 500,000 股衍生性證券行使（履約價 $9.74，約 USD 4.9M）。行使後立即賣出，屬選擇權變現。
- CEO 另有多筆規律性賣出（如 07-01、07-31、09-11 各約 57,941 股）與其他時點的大額賣出，是否屬 10b5-1 計畫，工具無法確認。
- CFO Parekh 於 10-06 賣出約 51,703 股（約 USD 1.3M）。
- 董事與高階主管於 2026-04 至 06 月另有股票獎勵（Grant，價格 0），不計入買賣淨額。

解讀: 高層（CEO、CFO、President）在 6 個月內持續賣出，且無任何買入，為偏空訊號。其中部分屬行使後變現，需與一般市場交易區分。

## Ownership shifts

- 機構持股比例: 86.9%（institutionsPercentHeld 0.869），機構家數 648。
- 內部人持股: 0.89%。
- 機構持股時間序列: yf major_holders 僅提供當期快照，無法得出趨勢。
- 13F 片段（WebSearch，Fintel 第三方彙整，未驗證於 EDGAR，且樣本偏重搜尋命中，非完整名單）:
  - Millennium Management: 2026 Q1 約 7.41M 股，較前期增加約 379%（含 511,500 股 call 選擇權標的）。
  - Freestone Grove Partners: 2026 Q1 約 2.25M 股，增加約 337%。
  - IEQ Capital: 約 2.12M 股，增加約 34%。
  - AXQ Capital: 約 0.21M 股，增加約 95%。
  - JPMorgan Chase: 2026 Q1 約 2.55M 股，減少約 18%。
- 結論: 樣本內增持多於減持，機構淨流向偏正面，但樣本小且片段化，信心低。

## Net sentiment score

**Composite: 中性（neutral），信心: 低至中。**

各面向判定:
- 分析師: 偏多（買進佔 52.9%、無賣出），但三個月內買進佔比下降，目標價約等於現價。
- 散戶/社群: 無法直接量測，媒體與部落格語氣混合偏空（指引、競爭、AI 衝擊）。
- 內部人: 偏空（6 個月淨賣約 USD 32M，零買入）。
- 機構: 偏多（樣本淨增持，持股比例高達 86.9%）。

**Divergence flag: 是（有限，信心低）。** 分析師整體偏多，而可觀察的散戶與媒體語氣、以及內部人行為偏空，方向相反。因 Reddit 與 StockTwits 無法取得，散戶面向的證據基礎薄弱，此旗標僅作參考。

資料缺口: Reddit、StockTwits 無資料；機構流向僅有第三方片段；yf 無法提供股價歷史與評級的時間對齊資料。

SENTIMENT REPORT COMPLETE
