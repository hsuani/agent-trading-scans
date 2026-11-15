# Sentiment — NVDA as of 2026-11-16

> 資料缺口: Reddit 與 StockTwits 直接抓取失敗 (見下方), 散戶部分以第三方報導替代; 系統日期為 2026-11-15, 本報告 as-of 日期晚一天, 數據以工具回傳為準。

## Analyst consensus

| 期間 | 買進 (含強力買進) | 持有 | 賣出 | 合計 |
|---|---|---|---|---|
| 目前 (yf rec_summary, 0m) | 47 (強力買進 10 + 買進 37) | 14 | 0 | 61 |
| 一個月前 (-1m) | 59 (強力買進 10 + 買進 49) | 2 | 1 | 62 |

目前 47 of 61 家為買方評級 (約 77%)。一個月內買方家數減 12、持有增 12、賣方減 1, 評級明顯向持有收斂。

近期評級與目標價變動 (來源: WebSearch 次要報導, yf 不提供逐筆升降評級紀錄):
- Baird (Tristan Gerra): Outperform 降至 Neutral, 目標價 $500 降至 $200; 報導點名 AI 資本支出放緩與 Jensen Huang 相關風險。
- Melius: 目標價 $420 降至 $315 (11/2)。
- Mizuho: 目標價 $315 降至 $250。
- Citi (Atif Malik): 12 個月目標價 $315 降至 $285。
- Morgan Stanley: 自 semiconductor "Top Pick" 移除, 維持 Overweight, 目標價 $300。
- Seeking Alpha 一位作者下調評級, 理由為財報前恐慌性拋售風險。

共識目標價來源不一: TipRanks 近 3 個月 35 家平均 $317.83; 另一來源 $327.14 (參照股價約 $177.81, 11/9)。11/9 文章稱僅一家賣方評級, 與 yf 目前 sell=0 不一致, 兩者時點不同, 以 yf 為準。

## Retail social

- **Reddit**: 無法取得。WebFetch 對 r/wallstreetbets 搜尋端點回報 "unable to fetch from www.reddit.com", 因此無法列出抽樣貼文、分數或留言數。次要報導指出 WSB 近期貼文多談大盤虧損而非 NVDA 本身, 屬轉述, 未經直接驗證。
- **StockTwits**: 無法取得。api.stocktwits.com 解析失敗 (DNS), 需於 session 網路設定允許該網域。次要報導 (StockTwits 新聞稿) 指出 NVDA 單週下跌 8.8%, 為 2025 年 4 月以來最大週跌幅, 但散戶情緒仍標示為 "extremely bullish"。
- **X**: 未直接檢索, WebSearch 結果中無可用的 X 原文。
- **第三方綜合情緒分數** (各平台方法不同, 不可直接比較):
  - LunarCrush: 24 小時跨平台正向情緒 89%。
  - AltIndex: 76/100, 偏多 (無日期)。
  - Yahoo/247 Wall St 報導: 由 10 月底 89/100 降至 41/100。
  - AOL 報導: 綜合分數 33, 三個 subreddit 皆有懷疑論調, 主因 AI 泡沫疑慮。
- **Buzz volume**: 無可靠提及數基準, 無法量化; 不做量能判斷。
- **Themes** (依報導頻次排序):
  1. AI 資本支出放緩疑慮 (Baird 下調評級的核心論點)。
  2. 中國先進晶片出口管制與地緣政治 (Trefis 歸因於近期急跌)。
  3. 內部人大額賣出 (見下節)。
  4. AI 泡沫擔憂。
  5. 財報前波動與跌後是否進場的討論。
- 代表性標題 (非貼文原文): "Baird Downgrades Shares, Flags Slower AI Spending" (次要新聞標題)。

## Insider activity

取樣窗口 2026-05-16 至 2026-11-16 (yf insider 原始資料, 單位 USD)。

| 類別 | 筆數 | 金額 (USD M) |
|---|---|---|
| 公開市場賣出 | 9 | 1,370.5 |
| 公開市場買進 | 0 | 0 |
| 股票贈與 (不計入買賣) | 5 | 0 |
| 股票獎勵 (不計入買賣) | 13 | 0 |

賣出明細:

| 人員 | 職稱 | 筆數 | 金額 (USD M) |
|---|---|---|---|
| Mark A. Stevens | 董事 (間接持股) | 5 | 1,353.7 |
| Timothy S. Teter | General Counsel | 2 | 13.3 |
| Stephen C. Neal | 董事 | 1 | 3.3 |
| John O. Dabiri | 董事 | 1 | 0.1 |

Net 6mo: 買入 USD 0, 賣出 USD 1.37B。

Notable:
- Stevens (董事) 於 6/4 至 9/18 分 5 筆賣出, 合計約 612 萬股, 成交價約 $210 至 $234。以 1,366,000 股 × $220 ≈ $300M 核對, 與原始 Value 欄位一致。
- CEO Jen-Hsun Huang 於 6/16 有 40 萬股贈與 (非市場賣出)。3 月另有大額贈與, 不在本窗口內。
- CFO Colette Kress 的賣出紀錄在 3 月, 不在本窗口內。
- 賣出集中於單一董事且多為間接持股, 不能單獨推論公司基本面看法。

## Ownership shifts

- 機構持股 71.17% (機構數 7,773); 內部人持股 4.16%; 機構佔流通股 74.25%。
- 前十大機構 (yf major holders; 持股變化依 pctChange 欄位解讀):

| 機構 | 持股比 | 持股量 (B 股) | 持股變化 |
|---|---|---|---|
| BlackRock | 8.06% | 1.94 | +0.85% |
| Vanguard Capital Mgmt | 6.39% | 1.54 | +0.15% |
| State Street | 4.25% | 1.03 | +1.51% |
| FMR | 3.87% | 0.93 | -9.09% |
| Geode | 2.55% | 0.61 | +1.24% |
| Vanguard Portfolio Mgmt | 2.15% | 0.52 | +1.51% |
| JPMorgan | 1.92% | 0.46 | +2.84% |
| T. Rowe Price | 1.53% | 0.37 | -0.07% |
| Morgan Stanley | 1.48% | 0.36 | +3.93% |
| Norges Bank | 1.35% | 0.33 | -2.34% |

前十大合計約 33.6%。被動型與指數型機構多數增持; 主動型中 FMR 減持幅度最大 (-9.09%), T. Rowe 與 Norges 小幅減持。整體為分歧, 無單一方向的集中化或去集中化趨勢。

## Net sentiment score

**綜合: 中性偏空 (neutral-to-bearish), 信心: 低至中。**

- 分析師: 多數仍為買進 (約 77%), 但一個月內大幅轉向持有, 近期目標價大幅下修, 偏多方向減弱。
- 內部人: 6 個月公開市場賣出約 $1.37B, 零公開市場買進, 偏空。
- 散戶: 來源互相矛盾 (綜合分數 33 至 89), 且 Reddit/StockTwits 無直接數據, 信心最低。

**Divergence flag: 部分是 (信心低)。** 分析師整體仍偏多但評級轉弱, 內部人方向為賣出, 兩者方向不一致。散戶方向無法確定: 若採 StockTwits 報導則偏多, 與分析師一致; 若採 AOL 與 Yahoo 報導則偏空, 與分析師相反。

## 資料缺口與注意事項
- Reddit 與 StockTwits 直接抓取失敗, 散戶判讀依賴第三方次要報導。
- yf `recommendations` 只提供期間彙總, 無逐筆評級升降紀錄; 逐筆動態依 WebSearch 補充, 可能不完整。
- 財報日期來源不一 (11/17、18、19、20); 目前單一來源指向 11/17 盤後, 其餘未確認。
- 股價與目標價來源之間不一致 (例如 11/9 約 $177.81、其他報導約 $181.60 與 $210), 使用前需以即時報價核對。
- 本報告僅為情緒與評級彙整, 不構成交易建議。

SENTIMENT REPORT COMPLETE
