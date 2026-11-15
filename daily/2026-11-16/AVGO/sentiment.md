# Sentiment — AVGO as of 2026-11-16

資料時點備註: 本報告依指示標示 as-of 2026-11-16，但系統當日為 2026-11-15，故 16 日盤後資料尚未存在。Yahoo 端點本次連線失敗 (fc.yahoo.com ConnectionError)，但 yf 工具仍回傳 rec_summary / insider / holder 資料，最新一筆 insider 交易日為 2026-07-10，最新股價參考為 2026-11-10 收盤 $319.48。

## Analyst consensus
目前 51 位分析師: 8 strong buy / 40 buy / 3 hold / 0 sell / 0 strong sell (yf rec_summary, period 0m)。買進側占比約 94%，無賣出評等。

近四個月評等分布 (yf recommendations，period 0m 至 -3m):

| 期間 | Strong Buy | Buy | Hold | Sell | 買進側合計 |
|---|---|---|---|---|---|
| 0m (本月) | 8 | 40 | 3 | 0 | 48 |
| -1m | 8 | 41 | 2 | 0 | 49 |
| -2m | 7 | 40 | 3 | 0 | 47 |
| -3m | 8 | 37 | 4 | 0 | 45 |

Hold 由 -1m 的 2 家回升到本月 3 家，買進側略降，但整體仍偏多。注意: yf recommendations 工具本次只回傳期間彙總，未提供逐筆升降評等紀錄，因此下列個別券商動態來自網路搜尋，日期不一致，需以券商原文或 TipRanks / MarketBeat 核對:

- Macquarie: 評等史顯示 6/4/2026 評等降至 Neutral，目標價由 $513 降至 $437 (原評等未明載)；但另一篇 9 月報導稱其升至 Outperform、目標 $490。兩者時序衝突，未能釐清。
- BMO Capital: 9 月上調目標至 $575 (由 $455)，維持 Outperform。
- Cantor Fitzgerald: 9 月上調目標至 $600 (由 $525)。
- Goldman Sachs: 目標上調至 $435 (由 $380)，日期未明。
- BofA: 目標 $460 (由 $400)，後續另一來源稱 $500 維持 Buy，日期未明。
- 追蹤平台彙整: 30 位分析師平均目標價約 $523.72，相較 $319.48 約 +64%。此數字來自單一追蹤站，未與 yf 的 51 位口徑對齊。

財測與目標價方向: 2026 年 9 月財報後多數券商上調目標價；11 月 10 日股價單日上漲 8.8% 至 $319.48，但仍遠低於 6 月 insider 賣出價區間 (約 $373–401)。

## Retail social
- Reddit: 本次依指示未直接抓取 Reddit JSON。以第三方聚合 AltIndex 代替: 約 30 則/日提及 (r/wallstreetbets、r/stocks、r/investing)，屬正常水準，Reddit 情緒分數 71/100 (中性偏多)。未找到 2026 年 11 月當月的可引用 r/wallstreetbets 熱帖，無法直接引用原文。
- StockTwits: 2026 年 8 月與 6 月的報導顯示散戶情緒明顯偏多，多次在股價回檔時被描述為「買進機會」。報導標題範例: "Retail Dip Buyers Flock To Broadcom After Stock Drops" (字數 ≤15，引用標題而非貼文內容)。AltIndex StockTwits 分數 80/100 (Bullish)。API 直接抓取未執行。
- X / 網路: 可得資料極少。一份選擇權資料站稱 X 上情緒約 45% 偏多、多空分歧，但頁面日期為 2026 年 2 月，來源品質不足，僅供參考。
- 聚合情緒指標 (非直接社群抓取，時點不一): SentiSense 截至 11/8 的 30 日情緒偏多但較前月降溫，其中 Reddit 偏多、Substack 偏空；LunarCrush 社群正面情緒約 77%–83%，時間戳不明。

Themes:
1. AI 客製晶片 (custom AI ASIC) 與 hyperscaler 需求積壓 (backlog)，為最常被提及的多方理由。
2. 估值與技術面: 散戶部分關注 valuation 與技術破位風險，為主要空方理由，但多數回應為「回檔買進」。
3. 9 月財報後的目標價上調，被散戶引用為看多依據。
4. 11 月 10 日單日 +8.8% 反彈，散戶把它解讀為修正結束的訊號；下一個催化劑為 12 月 9 日 FQ4 財報 (盤後)。
5. 「分析師普遍看多但股價仍大幅低於目標價」的分歧敘述，散戶與部分媒體都有提及。

Retail buzz volume: 相對一般水準，屬常態到略高；無足夠數據支撐量化比較，僅為定性判斷。

## Insider activity
Net 6mo (2026-05-16 至 2026-11-16 窗口): 買入 $0.37M，賣出 $283.70M，淨賣出約 $283.3M。

注意: 窗口內 yf 僅回傳至 2026-07-10 的 11 筆交易，7/10 之後至 11/16 之間無任何紀錄，可能是資料延遲或 feed 缺漏，需人工核對 SEC Form 4 後再採信。

| 日期 | 人員 | 職位 | 交易 | 股數 | 金額 (USD M) |
|---|---|---|---|---|---|
| 2026-06-24 | Samueli Henry | Director (間接持有 I) | 賣出 @ $377.61–388.17 | 654,241 | 250.01 |
| 2026-07-08 / 07-10 / 06-25 / 06-17 | Brazeal Mark David | Officer | 多筆賣出 @ $377–401 | 83,152 合計 | 32.36 合計 |
| 2026-07-08 | Delly Gayla J | Director | 賣出 @ $385.38 | 1,890 | 0.73 |
| 2026-06-29 | Page Justine F. | Director | 賣出 @ $373.86 | 1,602 | 0.60 |
| 2026-06-11 | You Harry L | Director | 買進 @ $373.57 | 1,000 | 0.37 |

Notable:
- 唯一公開市場買進為獨立董事 You Harry L，金額僅 $0.37M，規模小。
- 最大賣出為 Samueli Henry 於 6/24 出售 654,241 股，約 $250.0M，占淨賣出的 88% 以上，以間接持有方式進行。
- Brazeal Mark David 於 6 月中至 7 月初分 4 次賣出，合計約 $32.4M，屬反覆性賣出。
- 其他: CFO O'Toole Amie Thuener 於 6/15 獲授予 50,000 股 (Stock Award，非公開市場交易)；Samueli 與 Delly 另有贈與 (Stock Gift) 紀錄，不計入賣出。
- 賣出價格集中在 $373–401，明顯高於 11/10 收盤 $319.48，後續價差對內部人而言為負。無法從資料判斷是否為事先安排的交易計畫，未作推論。

## Ownership shifts
- 機構持股比例 79.46%，機構數 6,301 家；內部人持股 2.12%。
- 前十大持有人 (最新申報):

| 機構 | 持股比例 | 季度變動 | 報告日 |
|---|---|---|---|
| BlackRock | 8.34% | +3.18% | 2026-06-30 |
| Vanguard Capital Management | 6.48% | +0.37% | 2026-06-30 |
| State Street | 4.21% | +2.10% | 2026-09-30 |
| FMR (Fidelity) | 2.67% | -11.73% | 2026-09-30 |
| Vanguard Portfolio Management | 2.66% | -1.11% | 2026-06-30 |
| Capital World Investors | 2.59% | +1.28% | 2026-09-30 |
| Geode Capital | 2.47% | +1.33% | 2026-09-30 |
| Capital Research Global | 2.28% | -3.91% | 2026-09-30 |
| JPMorgan | 1.99% | +0.09% | 2026-09-30 |
| T. Rowe Price | 1.74% | -1.92% | 2026-06-30 |

判讀: 指數型與被動資金持續加碼，主動基金分化 (FMR 大幅減碼 11.7%，Capital Research 減 3.9%，Capital World 與 Geode 加碼)。整體為被動增持、部分主動減持的結構，無法從單一快照判斷趨勢方向。機構持股數量的時間序列 yf 未提供。

## Net sentiment score
Composite: **偏多 (bullish)**，信心度 **中等 (medium)**。

- 分析師面: 強烈偏多 (94% 買進側、0 賣出、目標價上調)。
- 散戶面: 偏多 (StockTwits、聚合指標皆偏多，Reddit 中性偏多)。
- Insider 面: 偏空 (淨賣出約 $283M，買進僅 $0.37M，且資料可能不完整)。
- 機構面: 中性偏多 (被動增持，主動基金分化)。

信心度下調的理由: insider 窗口資料於 7/10 後中斷；Reddit 未直接抓取；分析師個別評等動態日期衝突；網路摘要的時點不一致。

Divergence flag: **否** (散戶與分析師方向一致，皆偏多)。
另有一項值得留意的分歧: insider 淨賣出與分析師偏多方向相反，此為 insider 與 sell-side 之間的分歧，而非散戶與分析師之間的分歧。

SENTIMENT REPORT COMPLETE
