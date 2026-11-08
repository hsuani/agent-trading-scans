# Sentiment — AMZN as of 2026-11-09

資料截止：2026-11-08（工具輸入日）。分析師與內部人資料來自 pipeline/tools/yf.py（部分為 cache），散戶與新聞面資料來自 WebSearch。Reddit 與 StockTwits 的直接抓取未能取得近期貼文，故下列散戶段落以搜尋摘要為主，可信度標示為低。

## Analyst consensus

目前 61 位分析師中，14 位 Strong Buy、44 位 Buy、3 位 Hold、0 位 Sell、0 位 Strong Sell，即 58 買進 / 3 持有 / 0 賣出。與一個月前相比，買進類合計維持 58 家，Hold 由 2 家增至 3 家，Strong Buy 由 16 家降至 14 家，覆蓋總數由 60 家增至 61 家。與三個月前（61 買進類、2 持有）相比，評等整體略向 Hold 位移，但仍是高度偏多的結構。

近期動向（WebSearch 摘要，部分日期未明確）：
- Morgan Stanley（Brian Nowak）於 10/19 將 AMZN 列為網路產業首選，維持 Overweight，目標價由 335 上調至 350 USD。
- UBS（Stephen Ju）於 10/26 將目標價由 318 上調至 348 USD，維持 Buy。
- Phillip Securities 由 Accumulate 升為 Buy，目標價 330 USD，多處報導指向 11/02 財報後，但來源對日期說法不一。
- Evercore（Mark Mahaney）目標價由 280 上調至 335 USD；Canaccord（Maria Ripps）由 280 上調至 300 USD，兩者均維持 Buy，日期未明。
- 共識目標價來源差異大：247wallst（11/06）引用約 326.74 USD，另一來源引用 S&P Global 約 332.41 USD，MarketBeat 另有 322.56 USD（日期偏舊）。
- 未找到 11/2026 的降評紀錄。

## Retail social

- Reddit：WallStreetBets 與 r/stocks 的 AMZN 搜尋未取得 2026-11 的現行貼文，僅有 2026-01 的快照。其中一則高讚貼文（約 3,150 upvotes）將裁員與 AI 取代人力連結，代表樣本語句："Combined with AI-driven lay-offs."。近期 tilt 無法可靠判定。
- StockTwits / X：StockTwits 最近可得的讀數停在 2026-01，當時情緒為 bearish；2025 年財報後曾飆至 extremely bullish（約 90/100），伴隨訊息量暴增。未找到 11 月的即時讀數，一則未註明日期的摘要稱近期為 extremely bullish 且訊息量高，但無法驗證。
- 聲量（定性）：財報前後與大跌反彈時段聲量明顯高於平常；2026-10-29 財報後的反彈期應屬高聲量，但缺乏可量化的提及數。
- 主要議題（Themes）：
  1. 多方：AWS 成長與 AI 基礎建設需求、財報後反彈、假日銷售與 Phillip 升評。
  2. 空方：AI 資本支出（2026 年指引約 220B USD）壓縮自由現金流；TIKR 引用 TTM 自由現金流約 -42.4B USD；封鎖外部 AI 購物代理的爭議；AI 相關裁員。
  3. 股價面：Stocktwits 提及 AMZN 自 5 月高點回落逾 18%，且 2026 上半年為 2022 年以來首度上半年下跌。
- 散戶 tilt：財報後偏多、長期偏空疑慮仍在。整體判定為 mixed，信心低。

## Insider activity

視窗：2026-05-09 至 2026-11-08（6 個月）。

| 項目 | 金額（USD） | 說明 |
|---|---|---|
| 公開市場買進 | 0 | 視窗內未見任何 open-market purchase |
| 公開市場賣出（合計） | 約 385.5M（0.39B） | 含 Bezos 單筆約 346.5M，占 90% |
| 扣除 Bezos 的賣出 | 約 39.1M | 性質需進一步查證，工具無法判定是否為計畫性出售 |
| 贈與（Gift，無金額） | 不計 | Bezos 8/26 贈與 415,580 股；Herrington 8/6 贈與 22,000 股 |

重點交易：
- Jeffrey P. Bezos（Officer and Director）：2026-08-03 賣出 1,209,649 股，均價約 286.41 USD，金額約 346.45M USD。
- Andrew R. Jassy（CEO）：2026-05-21 賣出 20,000 股，約 5.27M USD；2026-08-21 賣出 20,000 股，約 5.18M USD。
- Brian T. Olsavsky（CFO）：2026-08-21 賣出 6,172 股，約 1.61M USD。
- Douglas J. Herrington（Officer）：視窗內最頻繁的賣方，多為每月 1,000 股的小額賣出；其 2026-05-04 的大額賣出在視窗之外，未計入。
- Matthew S. Garman、David A. Zapolsky：2026-05 與 2026-08 各有約 3.8–4.1M USD 的賣出。
- Shelley L. Reynolds：2026-05-21 與 2026-08-21 各約 0.6M USD。
- 註：工具輸出中有部分無金額列（Value 為空），多為與同日賣出配對的衍生性或持股變動列，未計入。
- 判讀：視窗內無內部人買進，賣出集中於 8 月，金額高度集中於 Bezos 單一交易。大型股內部人賣出的訊號強度通常有限，但 6 個月內完全無買進，仍屬偏空側證據。

## Ownership

- 內部人持股：8.83%
- 機構持股：68.85%（流通股占比 75.51%）
- 機構家數：7,934
- 工具僅提供當前快照，無法判定機構集中度的時間趨勢。

## Net sentiment score

- 分析師面：偏多（高信心）。58/61 為買進類，0 賣出，目標價多在 300–350 USD 區間。
- 散戶面：mixed，偏向財報後的正向情緒，但近期可信讀數不足（低信心）。
- 內部人面：偏空（中低信心）。6 個月無買進，賣出金額約 385.5M USD，以 Bezos 為主，且大型股的內部人賣出訊號雜訊較高。
- 綜合判定：偏多（中等信心）。分析師共識與財報後的散戶情緒一致偏多，內部人賣出為主要反向訊號。

Divergence flag：否。散戶與分析師方向大致一致（均偏多）。但散戶資料薄弱，若日後確認 StockTwits 仍為 bearish，則會形成背離，屆時需重新評估。

## 資料來源與限制

- 工具：pipeline/tools/yf.py（rec_summary、recommendations、insider、major_holders），部分來自 cache。
- WebSearch 來源（摘要引用）：247wallst（2026-11-06 "Not One Analyst Rates Amazon a Sell"；2026-11-02 Amazon Climbs 5%）、MarketBeat、TIKR、Stocktwits、Zacks、Yahoo Finance、Quiver Quantitative、Reddit 快照（2026-01）。
- 限制：Reddit 與 StockTwits 無 2026-11 的直接讀數；部分新聞與目標價日期不明或互相矛盾；本報告不構成交易建議。

SENTIMENT REPORT COMPLETE
