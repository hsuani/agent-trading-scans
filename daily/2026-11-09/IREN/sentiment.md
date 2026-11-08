# Sentiment — IREN (IREN Limited) as of 2026-11-09

**日期注意**: 任務指定的 as-of 日期為 2026-11-09，但系統日期為 2026-11-08。本報告引用的最新可核實資料約停在 2026-11-04 至 11-05 附近，11-09 當日的資料未被核實。

**資料來源說明**: `pipeline/tools/yf` 的 ratings、insider、holders 皆回傳資料（cookie/crumb 取得失敗後採用快取回退），數值可用但時點不明。Reddit 與 StockTwits 直接端點未納入本次取數，改以 WebSearch 取得的二手摘要為主，屬低信心來源。

## Analyst consensus

以 `rec_summary` 最新一期（0m）計算：**16 buy（含 2 strong buy）/ 4 hold / 0 sell**，共 20 家。

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 合計 |
|---|---|---|---|---|---|---|
| 0m（最新） | 2 | 14 | 4 | 0 | 0 | 20 |
| -1m | 3 | 13 | 4 | 0 | 0 | 20 |
| -2m | 2 | 13 | 5 | 0 | 0 | 20 |
| -3m | 1 | 12 | 3 | 0 | 1 | 17 |

- 近四期評級結構大致穩定，買方評級由 -3m 的 13 家增至 0m 的 16 家，評級面未出現明顯下修，但工具回傳的 `recommendations` 與 `rec_summary` 數值完全相同，無法逐筆看到升降評等事件。
- 資料矛盾: JPMorgan 在 2026-05 被報導為 underweight（目標價由 $39 上調至 $46），但 0 sell 的計數未反映此評級；-3m 出現 1 家 strong sell 但 sell 欄為 0，口徑疑似不一致，採用時需保留態度。
- 近期目標價變動（WebSearch 彙整）:
  - Bernstein 於 2026-11-04 由 $100 下調至 $55（仍看多）。
  - Goldman Sachs Hold，目標 $50（2026-07-20）。
  - Cantor Fitzgerald Overweight，目標 $61（2026-04-09）。
  - Rothschild & Co Redburn 首次覆蓋 Neutral，目標 $40（2026-09-21）。
  - BTIG 目標 $80；HC Wainwright 目標 $80（2026-01）。
  - 共識平均目標約 $77–81（來源日期分散於 2026-07 至 10 月）。
- 股價於 2026-10-21 前後約 $26.6，10 月內跌幅約 40%，目標價中位數遠高於現價，分析師面整體偏多，但目標價多數已向下修正。
- 另有 Wall Street Zen 由 Hold 調為 Sell 的報導，日期為 11-15 且年份不明，晚於本報告 as-of 日，未納入計算。

## Retail social

- **Reddit**: 本次 WebSearch 未找到近數週 r/wallstreetbets 或 r/stocks 的 IREN 討論串，無法取得 thread 樣本。可追溯的歷史情緒: 2025-12 社群情緒分數約 85/100（偏多，Microsoft AI 雲端合約題材）；2026-02-06 跌至約 8（偏空）；2026-04 有零星偏多的討論。**近期 Reddit 傾向: 無可核實資料。**
- **StockTwits / X**: 最新可見讀數為 Bearish 情緒 41（股價約 $25.41，頁面日期不明）。2026-03 為中性；2025-10 曾由 extremely bullish 轉為 extremely bearish（降評後）。第三方彙整顯示單日提及量曾達 1,310 次（94 百分位，日期不明）。本次未取得 StockTwits API 資料。
- **Buzz 量**: 定性判斷高於一般水準，但缺乏同期基準，無法給出精確倍數。
- **代表性散戶觀點（WebSearch 摘要改寫，非原文）**: 散戶討論多圍繞「便宜還是陷阱」，近期標題反映「零售散戶認為是撿便宜」與「預期還有 41% 下跌空間」兩種對立看法，顯示分歧。
- **主要主題**:
  1. 融資與資本支出壓力: 市場擔憂 FY2027 可能需要 $25–30B 資本支出；Wingspire $363M 設備融資改善流動性但增加槓桿。
  2. Neocloud 題材: 信貸環境收緊、AI 需求能否轉為報酬是核心疑慮。
  3. 財報: FQ1 財報排定於 2026-11-05，前期市場預期偏正面，實際結果未核實。
  4. 技術面與股價波動: 10 月內多次單日大幅震盪（如 -9%、-6.6%），引發追漲殺跌討論。

## Insider activity

- **6 個月淨額（2026-05-09 至 11-09）**: 公開市場買入 0 股 / $0；公開市場賣出 0 股 / $0。
- 窗口內僅有 2026-07-01 的股票獎勵（Stock Award，價值 $0）: CEO William Gregory Roberts 與 Daniel John Roberts 各 9,651,525 股（間接持有）；CFO Anthony J. Lewis 26,968 股；董事 Michael Alfred、Sunita Parasuraman、Christopher Guzowski、David James Bartholomew 各 6,657–8,369 股。
- 最後一筆公開市場賣出為 2025-09: CEO Roberts 兩人各以 $33.13 賣出 1,000,000 股（合計約 $66.3M，間接持有）；董事 Guzowski 以 $36.32 賣出 11,958 股（約 $0.43M）。屬於 6 個月窗口之外。
- 解讀: 近 6 個月內無內部人公開市場交易，內部人情緒訊號中性；2025 年的大額賣出為 CEO 的間接持股，需注意其與股價區間的關係。

## Ownership shifts

- 機構持股 61.07%（流通股占比 65.33%），機構數 926 家；內部人持股 6.52%。
- 工具僅回傳當期快照，無歷史序列，無法判斷機構集中度趨勢，此項標示為無法判定。

## Net sentiment score

- **分析師面: 偏多（中等信心）**。買方評級約 80%，目標價中位數遠高於近期股價，但目標價近期多次下修。
- **內部人面: 中性（中等信心）**。近 6 個月無公開市場交易，僅有獎勵性質股份發放。
- **散戶面: 偏空至混合（低信心）**。最新可得讀數為 StockTwits Bearish 41，Reddit 無近期資料。
- **綜合**: **中性（信心：低至中）**。分析師與散戶傾向方向相反，但散戶資料時點不明。

**Divergence flag: 是**。分析師傾向偏多（買方評級多數、目標價高於現價），散戶可見讀數偏空，兩者方向相反。此為值得留意的訊號，但需注意散戶資料缺乏明確日期，且 Reddit 近期資料缺失，差異可能部分來自資料時點不一致。

SENTIMENT REPORT COMPLETE
