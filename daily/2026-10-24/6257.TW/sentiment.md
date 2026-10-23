# Sentiment — 6257.TW（矽格）as of 2026-10-24

資料限制：本次為台股，英文散戶社群討論稀少。Reddit 公開 JSON 回傳存取錯誤（無法連線），StockTwits API 無法解析網域（DNS 失敗），兩者皆為 DATA_UNAVAILABLE。台灣本地論壇（PTT、Dcard）未取得可用的 2026 年 10 月討論摘要。以下結論信心偏低。

## Analyst consensus

1 buy（strongBuy）/ 0 hold / 0 sell。樣本只有 1 位分析師，統計上不具代表性。

| 期間 | strongBuy | buy | hold | sell | strongSell |
|---|---|---|---|---|---|
| 當期（0m） | 1 | 0 | 0 | 0 | 0 |
| -1m | 1 | 0 | 0 | 0 | 0 |
| -2m | 1 | 0 | 0 | 0 | 0 |

Recent moves: 過去三個月 yfinance 評等歷史無變動（`recommendations` 與 `rec_summary` 一致）。第三方彙整（Investing.com）顯示共識為 Buy，目標價 328 元，但頁面未標示發布日期，且與同時段股價（207 元）差距大，不採用為現行共識。

本土法人的評等與目標價資料（新聞來源）：
- 2025 年 6 月：Overweight，目標價 90 元（舊資料，已過時）。
- 2025 年底：工商時報報導本土法人調升至買進（Buy），股價當時 111 元。
- 2026 年第二季財報後：新聞報導法人大幅上修目標價（約四成），但未取得原始券商報告與確切目標價數字，標記為 DATA_UNAVAILABLE。

## Retail social

- Reddit（r/wallstreetbets、r/stocks）：DATA_UNAVAILABLE（存取錯誤，無法取得貼文數與語氣）。
- StockTwits：DATA_UNAVAILABLE（API 網域解析失敗）。
- X / 網路聲量（WebSearch）：未找到 2026 年 10 月的散戶意見文章。搜尋結果以新聞與資料站為主，無法判斷散戶語氣。
- 聲量相對量：DATA_UNAVAILABLE。無可靠的提及次數基準，不做量化推論。
- 可取得的間接訊號（非散戶意見）：
  - 2026 年 8 月初股價盤中大漲約 5.6% 至 197 元，8 月 4 日收約 199.5 元。
  - 統計狗頁面顯示 10/16 收盤價 252 元，本益比約 29.5，殖利率約 1.7%，9 月營收年增約 26%。
  - 兩個價格來源（207 元與 252 元）時點不同，未能確認 10/23 或 10/24 的最新價位。
- Themes（新聞與法人論述歸納，非散戶原文）：
  - AI、ASIC、矽光子等應用的測試需求。
  - 2026 年第二季營收創歷史新高，單季 EPS 2.55 元，上半年 EPS 4.65 元。
  - 資本支出由 59 億元上修至 88 億元（TWD 億），用於先進製程測試設備。
  - 風險面：毛利率受匯率、水電與人力費用影響。
  - AI 相關營收占比目前仍不高。

## Insider activity

Net 6mo：DATA_UNAVAILABLE。yfinance `insider` 回傳空陣列，無法確認是否為零交易或資料缺漏，不以 0 計。台灣董監持股異動應查 MOPS 公開資訊觀測站，本次未查詢。

Notable：無可驗證資料。

## Ownership shifts

- 內部人持股：約 7.87%（單一快照）。
- 機構持股：約 18.17%（流通股占比約 19.72%），機構家數 77。
- 趨勢：DATA_UNAVAILABLE。`major_holders` 只提供單一時點快照，無法判斷集中度變化方向。

## Net sentiment score

Composite：**偏多（bullish lean），信心低**。

依據：
- 分析師面：唯一可驗證的評等為 Buy，屬偏多，但樣本只有 1 位，且無近期評等變動。
- 基本面新聞：第二季營收創高、資本支出上修、法人上修目標價，偏多。
- 散戶面：無資料，不納入計分。
- 內部人面：無資料，不納入計分。
- 股價動能：8 月至 10/16 股價由約 200 元升至約 252 元，偏多，但時點不完整。

Divergence flag：**無法判斷（DATA_UNAVAILABLE）**。缺少散戶語氣資料，無法比較散戶與分析師方向是否相反。

Sources:
- [Investing.com 矽格共識頁](https://hk.investing.com/equities/sigurd-consensus-estimates)
- [統計狗 6257](https://statementdog.com/analysis/6257)
- [工商時報 2025-12-26](https://www.ctee.com.tw/news/20251226700828-430201)
- [中時 wantrich 2025-06-18](https://wantrich.chinatimes.com/news/20250618900394-420101)
- [中時 wantrich 2025-12-26](https://wantrich.chinatimes.com/news/20251226900303-420101)
- [中時 wantrich 2026-03-30](https://wantrich.chinatimes.com/news/20260330900340-420101)
- [中時 wantrich 2026-08-06](https://wantrich.chinatimes.com/news/20260806900474-420101)
- [中時 wantrich 2026-05-06](https://wantrich.chinatimes.com/news/20260506900250-420101)
- [Yahoo 股市 6257 broker-trading](https://tw.stock.yahoo.com/quote/6257/broker-trading)

## 指標表

| 指標 | 數值 | 信心 | 備註 |
|---|---|---|---|
| 整體情緒傾向 | 偏多（bullish lean） | 低 | 僅依分析師與基本面新聞，散戶與內部人無資料 |
| 分析師 Buy% | 100%（1 / 1） | 低 | 樣本只有 1 位分析師 |
| 分析師綜合分數 | +2.0（-2 至 +2 量表，strongBuy=+2、buy=+1、hold=0、sell=-1、strongSell=-2） | 低 | 單一分析師，僅供參考 |
| 散戶情緒 | DATA_UNAVAILABLE | — | Reddit、StockTwits 無法存取，台灣論壇無可用摘要 |
| 內部人淨交易（6mo） | DATA_UNAVAILABLE | — | yfinance 回傳空值，需查 MOPS |
| 機構持股比例 | 18.17% | 中 | 單一快照，無趨勢資料 |
| 內部人持股比例 | 7.87% | 中 | 單一快照 |
| 背離旗標 | 無法判斷 | — | 缺少散戶資料 |

SENTIMENT REPORT COMPLETE
