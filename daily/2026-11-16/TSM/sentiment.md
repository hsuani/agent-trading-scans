# Sentiment — TSM as of 2026-11-16

> 資料時點注意: 系統當日為 2026-11-15, 本報告以 2026-11-16 為 as-of 日期。yf 工具回傳為快照, 搜尋結果中有部分日期晚於 as-of (如 11/17 BofA 報告、11/25 訴訟), 已排除或標示待驗證。

## Analyst consensus

rec_summary 當前分布 (21 家): **6 Strong Buy / 14 Buy / 1 Hold / 0 Sell / 0 Strong Sell**, 買方比例約 95%。

| 期間 | Strong Buy | Buy | Hold | Sell | 合計 |
|---|---|---|---|---|---|
| 當前 (0m) | 6 | 14 | 1 | 0 | 21 |
| -1m | 6 | 14 | 1 | 0 | 21 |
| -2m | 6 | 14 | 1 | 0 | 21 |
| -3m | 6 | 12 | 1 | 0 | 19 |

近三個月評級結構幾乎不變, 僅 -3m 到當前新增 2 家 Buy。未見 Sell 評級。

Recent moves (搜尋, 未經 yf 直接驗證):
- Bernstein 目標價上調至 $600 (前值 $554), 理由為 ASIC/CPU 新需求; 來源為第三方轉載, 日期約 11/5。
- 另有 Bernstein Outperform 重申 (約 11/4) 的報導。
- 台股端據報有目標價下修 (TWD 700), 屬本地股價, 不確定是否適用 ADR。

Price target 資料衝突 (yf 工具未提供目標價欄位):
- $355 中位數: 較舊, 不採用。
- $521 平均: Benzinga 來源。
- $529 至 $558 區間: 11 月初彙整。
- $584.39: 24/7 Wall St. 11/6 報導, 與 6 SB / 14 Buy / 1 Hold 分布一致。
- 結論: 目標價共識約落在 $520 至 $585 區間, 來源不一致, 需以 Bloomberg/FactSet 等終端確認。
- 價格參考: 24/7 Wall St. 引用股價約 $406, 內部人買入成交價 $322 至 $405, 與此區間一致。

## Retail social

- **Reddit**: 因直接存取受限, 無法取得 r/wallstreetbets 與 r/stocks 當前 TSM 搜尋結果。搜尋找到的 2026 相關資料有限: 247WallStreet (2026/06) 提及 6/8 Reddit 情緒恐慌, 情緒分數 28 (單一作者觀點); 其餘多為 2024 至 2025 舊文。Reddit 近期聲量無法量化。
- **StockTwits / X**: StockTwits API 未取得資料 (soft-fail)。AltIndex 綜合 Reddit、StockTwits 與論壇, 給 TSM 情緒 82/100 (Bullish), 2026/02 至 07 月度區間為 79 至 85。此為綜合指數, 非單一平台。
- **Buzz volume**: 無法取得可靠提及數, 定性判斷為 中等 (AI 題材相關討論常見, 但缺乏 11 月量化資料)。
- **Retail tilt**: 偏多 (bullish)。

Themes (搜尋彙整):
1. AI 需求與 ASIC/CPU 客戶擴張: 分析師上調的主要論點。
2. 近期自高點回落約 19% (10/5 高點至 11/5 前後), 散戶多視為加碼機會, 但也有獲利了結聲音。
3. 資本支出上升引發短期謹慎 (Webull 報導)。
4. 訴訟風險: 前 TSMC 高階主管加入 Intel 相關訴訟, 被提為短期壓力 (日期待驗證)。
5. 估值擔憂: 部分文章指出 forward P/E 接近歷史高檔區間。

Representative takes (≤15 words each, 來源為文章轉述, 非原始貼文):
- 「The pullback looks like a buying opportunity given rising estimates.」 (TIKR 11/5 評論)
- 「Analysts see near-term sentiment as more cautious after capex plans.」 (Webull 報導摘要)

## Insider activity

6 個月窗口 (2026-05-16 至 2026-11-16) 內:
- 買入: **$316,498 (約 $0.32M)**, 4 筆; 賣出: $0。
- 淨額: **+$0.32M (淨買入)**。

| 日期 | 內部人 | 職位 | 方向 | 股數 | 金額 (USD) |
|---|---|---|---|---|---|
| 2026-11-05 | SPLINTER MICHAEL R | Director | 買入 @ $357 | 840 | $299,880 |
| 2026-07-28 | TIEN BOR-ZEN | Officer | 買入 @ $390 | 15 | $5,850 |
| 2026-07-20 | TIEN BOR-ZEN | Officer | 買入 @ $405 | 10 | $4,050 |
| 2026-05-20 | TIEN BOR-ZEN | Officer | 買入 @ $391.81-400 | 17 | $6,718 |

Notable: 11/05 Director Michael Splinter 買入 $0.30M, 為窗口內最大單筆。Officer 小額多次買入 (TIEN BOR-ZEN) 規模小, 較像例行買入。窗外另有 Director Ursula Burns 2026/03/31 買入 $0.32M (不計入 6 個月淨額)。

資料查核: 股數 × 成交價 與 Value 相符 (840 × 357 = 299,880)。

## Ownership shifts

- insidersPercentHeld: 0.051%, 內部人持股極低 (ADR 結構因素)。
- institutionsPercentHeld: 15.4%, institutionsCount: 4,749。此數值偏低, 可能因 ADR 持股結構未完整納入, 僅供參考。
- 前十大機構 (合計約 4.9% 持股) 的季度變動, 增加 6 家 (FMR +10.9%, BlackRock +10.4%, Goldman +71.5%, Morgan Stanley +7.3%, BofA +8.3%, Fisher +0.3%), 減少 4 家 (JPMorgan -25.6%, Sanders -6.5%, Van Eck -10.7%, Capital World -1.7%)。
- 持股金額 (USD): FMR 約 $26.1B 為最大, 其次 Capital World 約 $13.5B。
- 判讀: 機構結構中性偏多, 增減互見, 無明確集中化或撤出訊號。部分機構資料截至 6/30, 非同一時點。

## Net sentiment score

**Composite: 偏多 (bullish), 信心中等。**

依據:
- 分析師: 95% Buy, 近三月無下修, 偏多且穩定。
- 綜合情緒指數: AltIndex 82/100 偏多。
- 內部人: 6 個月淨買入 $0.32M, 無賣出, 偏多。
- 機構: 中性, 增減互見。
- 扣分: 目標價來源衝突、Reddit/StockTwits 即時資料缺失、近期股價自高點回落, 估值偏高的疑慮。

**Divergence flag: 否。** 分析師與散戶情緒同向偏多, 無相反訊號。唯一的分歧來自估值與近期回檔的擔憂, 屬於價格層面而非情緒層面。

資料缺口:
- Reddit / StockTwits 即時樣本無法取得, 散戶結論主要依賴綜合指數與第三方文章。
- 目標價需以終端資料確認。
- 機構資料截至 6/30 至 9/30, 非當日快照。

SENTIMENT REPORT COMPLETE
