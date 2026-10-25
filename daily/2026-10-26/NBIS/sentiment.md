# Sentiment — NBIS (Nebius Group) as of 2026-10-26

> 資料時效註記：本次執行日為 2026-10-25，任務指定 as-of 2026-10-26。yfinance 最新內部人交易日期為 2026-10-21，WebSearch 最新可取得的分析師彙整多為 2026 年 7–8 月，部分數據可能落後。

## Analyst consensus

單位：分析師家數（yf rec_summary，當期 0m）

| 評等 | 當期 (0m) | 三個月前 (-3m) | 變化 |
|---|---|---|---|
| Strong Buy | 2 | 1 | +1 |
| Buy | 13 | 10 | +3 |
| Hold | 6 | 5 | +1 |
| Sell | 1 | 0 | +1 |
| Strong Sell | 0 | 1 | -1 |
| 合計 | 22 | 17 | +5 |

- 買進側（Strong Buy + Buy）佔比：當期 15/22 ≈ 68%，三個月前 11/17 ≈ 65%。
- 賣出側（Sell + Strong Sell）：當期 1 家，三個月前 1 家。
- 評等總數與 yf 數據一致，Strong Buy 與 Buy 的合併口徑與 yf 相同。

Recent moves（WebSearch 彙整，日期多為 2026 年 7–8 月，非 yf 逐筆評等變動）：
- Freedom Capital（Paul Meeks）於 7 月升至 Buy，目標價 $200。
- Citigroup 於 8 月中將目標價上調至 $324。
- D.A. Davidson（Gil Luria）將目標價由 $250 下調至 $175，評等改為 Neutral，理由是對 2026 年底 328 MW 營運容量的達成存疑。
- 目標價共識：各來源不一。investing.com 彙整約 $259（14 家，10 買 / 5 持有 / 1 賣）；Benzinga 8 月快照約 $227（15 家，11 買 / 4 持有）；TIKR 於 10 月中引用平均目標價約 $283.60。來源之間日期與口徑不同，不宜直接比較。
- 個別分析師於 2026 年 10 月的評等變動：DATA_UNAVAILABLE（yf recommendations 僅回傳月度彙總，無逐筆 upgrade/downgrade 記錄）。

## Retail social

- Reddit（r/wallstreetbets、r/stocks）：DATA_UNAVAILABLE。WebFetch 回傳無法存取 www.reddit.com，本次無法取得討論串、提及次數或情緒傾向。WebSearch 亦未找到相關 Reddit 討論串。
- StockTwits：DATA_UNAVAILABLE。api.stocktwits.com 無法解析（DNS 失敗），無法取得 bullish/bearish 標籤比例。
- X / 新聞媒體：可參考的內容多為財經媒體報導，而非散戶貼文。
  - TIKR（10 月 19 日）：股價單週下跌約 25%，收於 $165.47；約 79% 跌幅集中在週三與週五。
  - Motley Fool 轉載（Mitrade）：股價約 $165，較 6 月高點低約 40%，10 月單月跌幅約 30%；文中表示 NBIS 本身沒有明顯的公司層面利空，與 CoreWeave 同步下跌。
- 散戶聲量相對典型水準：DATA_UNAVAILABLE（無法量化提及次數）。
- 主要論述主題（依新聞與媒體報導歸納，非散戶原文）：
  1. AI 算力租賃類股同步拋售，CoreWeave 債務疑慮擴散至 NBIS。
  2. 融資壓力：$4.34B 可轉換債（2026 年 3 月發行）轉換價之下約 8–10%，且市場預期 2027 年資本支出大幅增加。
  3. 估值爭論：有分析師認為「跌深後已便宜」，也有評論認為「尚未便宜到足夠」。
  4. 容量兌現風險：328 MW 年底營運目標是分析師降評的主要依據。

## Insider activity

Window：2026-04-26 至 2026-10-26（6 個月）。來源：yf insider，金額為 USD。

- 淨買入：$0.07M（2 筆，皆為 Director Arne Grimme，2026-10-19 與 10-21，買價約 $165–170）。
- 淨賣出：$304.5M（26 筆有效交易，已排除重複與金額缺失的列）。
- 淨值：約 -$304.4M（淨賣出）。

Notable：
- COO Ophir Nave：2026-10-05 賣出 500,000 股，金額約 $117.8M（價格區間 $231–244）。為本期單筆最大賣出。
- Officer Andrey Korolenko：2026-05-13 賣出 500,000 股，金額約 $101.6M（$203.24）；2026-07-01 另賣出約 $8.0M；2026-10-01 另賣出約 $6.8M。
- CEO Arkady Volozh：2026-10-01 賣出約 $8.8M（$234.16）；2026-07-01 賣出約 $11.0M（$235.45）；2026-04-01 賣出約 $3.5M。
- CTO Danila Shtan：2026-10-01 約 $3.4M；2026-07-01 約 $4.0M。
- CFO María del Dado Alonso Sánchez：2026-09-01 約 $0.09M；2026-06-02 約 $0.42M。
- Director John Boynton：多次定期性賣出（每月或每季約 $1.3–1.5M）。
- Director Charles Ryan：2026-08-14 賣出約 $13.3M（$263–270）。
- Director Arne Grimme：2026-10-19 與 10-21 買入（合計約 $75K），為本期唯一的買入紀錄，且發生在股價跌至約 $165 的低點區間。
- 股票獎勵（Stock Award）：2026-07-22 General Counsel Yael Almog 獲發約 $1.7M（$218.16 估值），2026-09-01 多位董事與管理層獲發 1,352 股，屬於授予而非市場交易，未計入淨買賣。
- 資料品質：yf 原始資料含重複列（Boynton 2026-06-15 重複兩列；Korolenko 2026-05-13 另有一列金額缺失），本報告以單筆計算。Boroditsky 多筆金額缺失列已排除。
- 解讀注意：大額賣出是否屬於 10b5-1 預定計畫或既有選擇權行使：DATA_UNAVAILABLE（yf 未提供交易計畫標記）。

## Ownership shifts

- 機構持股比例：70.0%（institutionsPercentHeld 0.70004）；float 口徑 72.5%。
- 機構家數：1,444。
- 內部人持股比例：3.4%。
- 機構持股趨勢（季度變化）：DATA_UNAVAILABLE。yf major_holders 僅回傳當期快照，無時間序列。

## Net sentiment score

- **綜合判斷：偏空至中性（Bearish-to-Neutral），信心度：低至中。**
- 分析師面：偏多（約 68% 買進側，三個月內僅小幅變化，多數為 Buy）。
- 內部人面：明顯偏空（6 個月淨賣出約 $304M，高階主管與董事持續賣出；僅一名董事於低點買入，金額極小）。
- 價格與資金面：近期跌幅大（10 月約 -30%），且市場敘事集中於融資與容量兌現風險。
- 散戶面：DATA_UNAVAILABLE，無法納入評分。
- 信心度偏低的原因：Reddit / StockTwits 無法取得；分析師與新聞來源的日期多落在 7–8 月；內部人交易的計畫性無法驗證。

**Divergence flag：是（部分）。** 分析師整體偏多，但內部人（尤其 C 級主管）大量賣出，兩者方向相反。散戶端因資料缺失無法判定是否與分析師反向，因此僅能確認分析師與內部人之間的背離。

資料缺口摘要：
- Reddit（r/wallstreetbets、r/stocks）：DATA_UNAVAILABLE（403/連線遭拒）
- StockTwits：DATA_UNAVAILABLE（DNS 失敗）
- 逐筆分析師評等變動（2026 年 10 月）：DATA_UNAVAILABLE
- 機構持股時間序列：DATA_UNAVAILABLE
- 內部人交易計畫（10b5-1）標記：DATA_UNAVAILABLE

SENTIMENT REPORT COMPLETE
