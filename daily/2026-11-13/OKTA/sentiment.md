# Sentiment — OKTA (Okta Inc) as of 2026-11-13

資料截止：2026-11-13（不採用之後的資料）。價格基準為 repo 快取 `prices/yf/OKTA.json`（2026-11-12 更新）之 USD 179.03。

## Analyst consensus

44 位分析師評等分布（yf `rec_summary`）：9 Strong Buy / 25 Buy / 10 Hold / 0 Sell / 0 Strong Sell。
推算買進比例約 77%（34/44），零賣出評等。`recommendationMean` 1.66（1 = Strong Buy，5 = Sell），`recommendationKey` = buy。

| 指標 | 數值 | 備註 |
|---|---|---|
| 目標價 平均 / 中位數 | USD 214.7 / USD 225 | 相對現價 179.03 約 +20% / +26% |
| 目標價 高 / 低 | USD 250 / USD 127 | 快取 `info` |
| 近 3 個月評等變化 | 買進側 35 → 34 含 Strong Buy；Hold 9 → 10 | 1 檔由 Buy 轉 Hold 的淨變化（以 yf 計數為準） |

Recent moves：yf `recommendations` 工具僅回傳彙總計數（與 rec_summary 相同），**個別升降評等明細 DATA_UNAVAILABLE**。
搜尋補充（次要來源，未逐筆驗證）：Mizuho 於 2026-06 降評至 Neutral；TD Cowen 維持 Hold（目標 USD 200）；BofA 維持 Underperform（日期不明）；Morgan Stanley、Scotiabank、Truist、Citizens 維持 Buy，目標 USD 225–245（約 2026-10 初）。

注意：yf `info` 的分析師家數為 43，與分布加總 44 相差 1，以分布表為準。

## Retail social

- **Reddit (r/wallstreetbets, r/stocks)**：直接 JSON 抓取依規定不使用（視為受限來源），**thread 數量與情緒比例 DATA_UNAVAILABLE**。
- **StockTwits / X**：StockTwits 流量與 bullish/bearish 投票結果 DATA_UNAVAILABLE（搜尋僅見頁面，未見當期投票數字）。
- **WebSearch 補充（Motley Fool 留言區、Seeking Alpha 留言頁）**：可見零星討論，語氣偏分歧。多頭論點集中在 AI agent 產品與 Q2 財報後的上調；空頭論點集中在估值偏高與 AI 衝擊軟體板塊估值倍數下修。未取得可量化的點讚或提及數。
- **Buzz volume（相對常態）**：無法量化，定性判斷為中低（搜尋結果以 2024–2025 舊文為主，2026-11 當期討論量不明）。

Representative takes（改寫自搜尋摘要，非原文引用；搜尋未取得個別留言原文）：
- 多頭：Seeking Alpha 留言頁可見看好上檔空間的留言。
- 空頭：Seeking Alpha 2026-10-05 一篇文章認為股價在 AI agent 產品熱度下仍偏貴；Simply Wall St 評論指分析師因板塊估值倍數下修而調降目標價。

Themes：
1. AI agent 與身分安全（identity security）產品成長敘事。
2. 估值與 SaaS 板塊倍數壓縮。
3. AI 取代軟體（AI disruption）之長期疑慮。
4. Q2 財報後股價創年內新高（Invezz 2026-08-27），之後買方是否延續之討論量不明。

Retail tilt：**混合（mixed），信心低**。資料不足以量化零售多空比例。

## Insider activity

Window：2026-05-13 至 2026-11-13（yf `insider`，金額為 USD）。

Net 6mo：**USD 0.0M 買進 / USD 46.0M 賣出**（公開市場賣出 10 筆；無公開市場買進）。

| 內部人 | 職位 | 6mo 公開市場賣出 (M USD) | 主要交易 |
|---|---|---|---|
| TIGHE BRETT | CFO | 20.5 | 2026-09-02 賣出 80,000 股，約 USD 12.9M；2026-06-08 賣出 65,000 股，約 USD 7.6M |
| MCKINNON TODD | CEO | 19.6 | 2026-09-22 賣出 48,822 股，約 USD 9.4M；2026-07-08 賣出 68,936 股，約 USD 10.1M |
| SCHWARTZ LARISSA NICOLE | Officer | 3.6 | 2026-06-02 賣出 24,971 股，約 USD 3.3M |
| KELLEHER ERIC ROBERT | President | 2.1 | 2026-06-18 賣出 3,977 股，約 USD 0.45M |
| ARCHAMBEAU SHELLYE L | Director | 0.2 | 2026-05-18 賣出 2,500 股 |

- 6mo 之外的對照：2026-04-16 董事 SCHELLHASE DAVID R 公開市場買進 3,712 股，約 USD 0.27M，為近期唯一一筆買進。
- 多筆 Value 為空白的交易（多為 RSU 歸屬、稅務代扣、贈與或 0 價格交易）未計入金額。
- 解讀限制：大額賣出與 2026-06 及 2026-09 之 RSU 歸屬時段相關，無法僅憑資料判斷是否為預定交易計畫（10b5-1）。

## Ownership shifts

- 機構持股比例 96.6%（流通股 97.1%），機構家數 1,307（yf `major_holders`）；內部人持股 0.5%。
- 前幾大持股（yf `inst_holders`，USD 市值依快取計）：
  - BlackRock 11.2%，q/q -1.8%（2026-06-30）。
  - FMR LLC 8.0%，q/q **-18.2%**（2026-09-30），為前幾大持股中最明顯的減持。
  - Vanguard PM 5.4%，q/q -3.1%；Vanguard CM 4.5%，q/q +0.1%。
  - State Street 3.8%，q/q +2.7%。
  - Morgan Stanley 2.1%，q/q **+85.9%**（2026-06-30）。
- 空頭：short interest 約 6.59M 股，佔流通股 4.4%，days to cover 約 2.05。

趨勢判讀：前十大中減持（FMR、BlackRock）與加碼（Morgan Stanley、State Street）並存，整體集中度穩定，無單一方向性大變化。

## Net sentiment score

- **分析師面（bullish，信心高）**：77% 買進、零賣出、目標價中位數高於現價約 26%。
- **內部人面（bearish 偏向，信心中）**：6 個月 USD 46.0M 公開市場賣出、零公開市場買進；CEO 與 CFO 為主要賣方。
- **零售面（mixed，信心低）**：資料不足，搜尋所見為多空交織。
- **機構面（中性）**：整體持股穩定，FMR 減持與 Morgan Stanley 加碼互相抵銷。

**Composite：中性（neutral），信心中低。** 分析師看多與內部人密集賣出並存，零售面無可靠量化資料。

**Divergence flag：是（有限度）。** 分析師與內部人方向相反（分析師看多、內部人賣出），零售面因資料不足無法判定是否與分析師相反，故標示為「部分背離，零售部分 DATA_UNAVAILABLE」。

## 資料缺口（DATA_UNAVAILABLE）

- 個別分析師升降評等明細（yf `recommendations` 僅回傳彙總）。
- Reddit 討論串數量與多空比例（依規定不直接抓取）。
- StockTwits 訊息量與投票結果。
- X 相關討論量化數據。
- 2026-11 當期零售提及量與相對常態比較。

SENTIMENT REPORT COMPLETE
