# Sentiment — DLR (Digital Realty Trust) as of 2026-11-07

## Executive summary

- 分析師共識偏多：yf 回報 34 位分析師中 29 位給 Buy 類評等（5 Strong Buy + 24 Buy），5 位 Hold，0 位 Sell。近四個月幾乎沒有變化，Buy 類由 3 個月前的 28 微增至 29。
- 內部人近 6 個月（2026-05-07 至 2026-11-07）沒有公開市場買入。唯一的公開市場交易是董事 PATTERSON MARK R 於 2026-08-27 賣出 200 股，約 $0.04M。其餘為股票獎勵（grant）。
- 散戶情緒無法量化。Reddit 直接抓取被擋（工具回報無法存取 www.reddit.com），StockTwits 未抓取（依任務限制不走 WebFetch 財經站），WebSearch 找不到 2026 年的 r/wallstreetbets 或 r/stocks 討論串。
- 機構持股數據有明顯的資料品質問題（institutionsPercentHeld 回傳 102.9%，超過 100%），無法用來判斷持股集中度趨勢。
- 綜合判斷：分析師面偏多、內部人面中性偏弱、散戶面無資料。整體情緒傾向偏多，信心度中等偏低。

## Data availability

| 來源 | 狀態 | 備註 |
|---|---|---|
| yf `recommendations` | 可用 | 4 期快照（0m 至 -3m）。yf 回報 cookie/crumb 取得失敗，但資料仍回傳。 |
| yf `rec_summary` | 可用 | 與 `recommendations` 數字相同，無日期欄位。 |
| yf `insider` | 可用 | 15 筆紀錄，最新一筆為 2026-08-27，無法確認抓取當下的 as-of 時點。 |
| yf `major_holders` | 部分可用 | 機構持股比例 102.9% 異常（疑為比例單位或重複計算問題），機構家數 1,844 可參考。無歷史趨勢。 |
| Reddit r/wallstreetbets, r/stocks | 不可用 | WebFetch 被拒絕（Claude Code 無法存取 www.reddit.com）。 |
| StockTwits | 未抓取 | 任務限制不以 WebFetch 取用財經社群站。 |
| WebSearch（散戶/X 情緒） | 低品質 | 無 2026-11 月的相關結果。ChartExchange 上的 Reddit 提及資料停在約 2025 年 6 月，已過期。 |

資料日期限制：本報告只使用 2026-11-07 當日或之前的資料。yf 回傳值沒有附上抓取時間戳記，因此「截至 2026-11-07」是以任務指定日期作為假設，無法逐筆驗證。未借用 daily/ 下其他日期報告的數字。

## Retail / social sentiment read

- 聲量：無法量化。沒有取得 2026-11 的 Reddit 或 StockTwits 提及數。
- 傾向：無法判定。
- 主題（來自一般新聞與分析文章，非散戶原文）：
  - AI 基礎設施與資料中心需求被視為主要支撐，市場多次提到 AI、雲端與企業需求。
  - 估值溢價是主要爭論點：Zacks 類文章指出 DLR 相對同產業與 S&P 500 有溢價。
  - 利率波動對收益導向的 REIT 形成壓力。
- 過期的散戶訊號：ChartExchange 收錄的 2025 年 6 月 r/stocks 貼文情緒分數為 -0.40，主題是企業是否會自建資料中心。此資料已超過半年，且不在本報告的 as-of 期間內，僅供參考，不計入綜合評分。
- 結論：散戶面為空白，不可拿來與分析師面做背離比較。

## Analyst consensus

yf `rec_summary`（最新快照）：

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 合計 |
|---|---|---|---|---|---|---|
| 0m（當前） | 5 | 24 | 5 | 0 | 0 | 34 |
| -1m | 5 | 24 | 5 | 0 | 0 | 34 |
| -2m | 5 | 24 | 5 | 0 | 0 | 34 |
| -3m | 5 | 23 | 5 | 0 | 0 | 33 |

- 當前分布：29 Buy 類（約 85%）/ 5 Hold（約 15%）/ 0 Sell。
- 近期變動：過去約 3 個月，Buy 類由 28 增至 29，Hold 穩定在 5，無 Sell。yf 此處沒有提供個別的升級與降級事件，也沒有目標價變動資料。
- 外部文章（非 yf，時間較早，僅作背景）：Barchart 系列文章曾提到平均目標價約 $196，並提到 Barclays 的 sell 評等與 Truist 目標價下調、Mizuho 降級。這些事件發生時間不明，與 yf 目前的 0 Sell 不一致，因此不採用其數字。

## Institutional / insider signal

### 內部人（yf insider，6 個月窗口：2026-05-07 至 2026-11-07）

| 日期 | 內部人 | 職位 | 類型 | 股數 | 金額 (USD M) |
|---|---|---|---|---|---|
| 2026-08-27 | PATTERSON MARK R | Director | 公開市場賣出（$193.96/股） | 200 | 0.04 |
| 2026-05-29 | MANDEVILLE JEAN F H P | Director | 股票獎勵 | 1,289 | 0（獎勵，無現金） |

- 6 個月淨額：買入 $0.00M，賣出 $0.04M（僅 1 筆）。沒有 CEO、CFO 或其他高層的公開市場買入。
- 窗口外的參考紀錄（不計入淨額）：
  - 2025-09-15 CEO POWER ANDREW P 賣出 58,000 股，約 $10.16M（$175.10–175.16/股）。窗口外，但規模最大。
  - 2025-12-01 PREUSSE MARY HOGAN（董事）賣出 4,166 股，約 $0.66M。
  - 2024-12-12 CFO MERCIER MATT 賣出 2,518 股，約 $0.47M。
- 解讀：6 個月內內部人幾乎沒有動作，只有一筆很小的董事賣出與獎勵股。窗口外則有較大的 CEO 賣出。整體偏中性，略偏空，不代表明確看空。

### 機構持股（yf major_holders）

- 內部人持股比例：0.014%（回傳值 0.00014）。
- 機構持股比例：回傳 102.9%（1.02926），超過 100%，明顯為資料異常。可能是比例單位誤用，或來自不同 13F 申報的重複計算。此數字不可用於判斷集中度。
- 機構家數：1,844。
- 歷史趨勢：無資料，無法判斷機構持股是增加還是減少。

## Overall sentiment verdict

- 分析師面：偏多。29/34 Buy 類，評等近幾個月穩定，無 Sell。
- 內部人面：中性偏弱。6 個月內只有一筆小額董事賣出，沒有公開市場買入。
- 散戶面：無資料，無法評分。
- 機構面：資料異常，無法評分。
- 綜合評分：偏多（Bullish-leaning），信心度中等偏低。信心受限於散戶與機構資料缺失，且分析師資料沒有目標價與個別評等變動細節。
- 背離旗標：否（無法判定）。散戶資料不存在，因此無法確認散戶傾向是否與分析師相反。

## Sources

- yf 本地工具（`pipeline/tools/yf.py DLR recommendations | rec_summary | insider | major_holders`），2026-11-07 任務期間執行。
- WebSearch，查詢 "DLR Digital Realty stock opinion sentiment November 2026"：
  - https://www.barchart.com/story/news/35300610/barclays-remains-a-sell-on-digital-realty-dlr （Barclays sell 評等，日期不明，僅作背景）
  - https://www.nasdaq.com/articles/do-wall-street-analysts-digital-realty-trust-stock （分析師背景，日期不明）
- WebSearch，查詢 "Digital Realty DLR reddit wallstreetbets stocks discussion 2026"：
  - https://chartexchange.com/symbol/nyse-dlr/trends/reddit （Reddit 提及快照，停在約 2025 年 6 月，已過期）
  - https://www.tikr.com/blog/digital-realty-stock-is-up-27-in-2026-can-the-rally-continue （2026 年股價表現背景，非情緒資料）
- Reddit r/stocks 搜尋（WebFetch）：失敗，連線被拒絕。

SENTIMENT REPORT COMPLETE
