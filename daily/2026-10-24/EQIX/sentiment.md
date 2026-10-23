# Sentiment — EQIX as of 2026-10-24

> 資料時點注意: 本報告標示之 as-of 為 2026-10-24，但執行環境日期為 2026-10-23。yf 工具回傳之分析師與內部人資料為當前可取得之最新快照；網路搜尋結果多數未標註日期或為 2026 年 5 月至 9 月之舊資料，已逐項標示。

## Analyst consensus

**yfinance 分析師分布 (35 家，USD 不適用，計數):**

| 評等 | 家數 | 占比 |
|---|---|---|
| Strong Buy | 6 | 17.1% |
| Buy | 24 | 68.6% |
| Hold | 5 | 14.3% |
| Sell | 0 | 0.0% |
| Strong Sell | 0 | 0.0% |

合計 Buy 類 (SB + B) 30 家，佔 85.7%；無任何 Sell 評等。

**近 4 個月趨勢 (yf rec_summary 歷史快照):**

| 期間 | Buy 類家數 | Hold | Sell |
|---|---|---|---|
| 0m (當期) | 30 | 5 | 0 |
| -1m | 28 | 6 | 0 |
| -2m | 27 | 6 | 0 |
| -3m | 26 | 6 | 0 |

Buy 類家數近三個月小幅增加 (26 → 30)，Hold 由 6 減為 5，未見降評。

**近期升降評與目標價變動:** DATA_UNAVAILABLE。`recommendations` 工具回傳內容與 rec_summary 相同之彙總格式，未提供個別券商升降評事件；目標價 (PT) 分布亦無當期數據。

**次要來源交叉比對 (與 yf 不一致，已標示):**
- Barchart (搜尋摘要，未標註日期): 33 家分析師，23 Strong Buy / 3 Moderate Buy / 7 Hold，Buy 類佔 78.8%。與 yf 家數與分類不同，推測為不同資料商之計算口徑差異，本報告以 yf 為主。
- Benzinga 情緒頁 (搜尋摘要，快照約 2026 年 8 月下旬): 29 家 Buy 共識，平均目標價 $1,137。此為舊快照。以未標註日期之報價 $1,018.96 估算，約高出 11.6%，僅供參考。

**共識分數 (1 = Strong Sell 至 5 = Strong Buy 加權平均):** (6×5 + 24×4 + 5×3 + 0×2 + 0×1) ÷ 35 = **4.03 / 5**，偏向 Buy。

## Retail social

- **Reddit (r/wallstreetbets、r/stocks):** DATA_UNAVAILABLE。兩個 subreddit 之 search.json 直接抓取均遭工具層封鎖 (Claude Code 無法存取 www.reddit.com)。改以 WebSearch 替代查詢，仍未找到 EQIX 相關 Reddit 討論串，無法取得樣本帖與多空傾向。
- **StockTwits:** DATA_UNAVAILABLE。api.stocktwits.com 無法解析 (DNS 失敗)。WebSearch 僅抓到 StockTwits 報價頁 (未標註日期，顯示 $1,018.96，52 週區間 $720.62 至 $1,128.68)，其多空比例分頁未能擷取。
- **X / 新聞聊天:** 無可靠之當期推文量化資料。WebSearch 結果多為聚合站文章，且多為 2026 年 5 月舊文，無法判定當期聲量。
- **NAGA 情緒聚合器 (替代訊號，非散戶原始貼文):** 其 2026 年 10 月頁面將群眾情緒標為 NEGATIVE、起始交易時段訊號為 BEARISH。來源為自動化聚合，且頁面自載免責聲明，權重低。
- **Buzz 量 (相對於典型水準):** DATA_UNAVAILABLE。無法取得提及數量之基準比較。
- **散戶傾向:** DATA_UNAVAILABLE。無法判定為多、空或分歧。

**主題 (由新聞與分析師摘要歸納，非散戶原文):**
- 多方論點: AI 基礎設施需求帶動資料中心擴張；FFO 預期回升 (Barchart 摘要所引用之預估)；連續四季優於華爾街預期。
- 空方論點: 利率上升對 REIT 估值之壓力；FFO 倍數偏高限制短期上行空間 (多篇 5 月之分析文章提及)。

## Insider activity

資料區間: 2026-04-24 至 2026-10-24 (近 6 個月)。

**Net 6mo: 買入 $0.0M，賣出約 $20.4M** (僅計入有明確成交價之公開市場賣出；金額以 USD M 計)

| 日期 | 內部人 | 職務 | 類型 | 股數 | 金額 (USD M) |
|---|---|---|---|---|---|
| 2026-05-06 | Meyers Charles John | 董事 | 賣出 | 5,224 | 5.67 |
| 2026-05-18 | Paisley Christopher B. | 董事 (間接) | 賣出 | 125 | 0.13 |
| 2026-05-22 | Abdel Raouf F | 高階主管 | 賣出 | 2,040 | 2.21 |
| 2026-06-02 | Fox-Martin Adaire | **CEO** | 賣出 | 2,935 | 3.10 |
| 2026-06-02 | Lin Jonathan | 高階主管 | 賣出 | 150 | 0.16 |
| 2026-06-02 | Pletcher Kurt | 高階主管 | 賣出 | 79 | 0.08 |
| 2026-06-02 | Abdel Raouf F | 高階主管 | 賣出 | 158 | 0.17 |
| 2026-06-08 | Morandi Brandi Galvin | 高階主管 | 賣出 | 3,726 | 4.01 |
| 2026-08-03 | Paisley Christopher B. | 董事 (間接) | 賣出 | 4,000 | 4.08 |
| 2026-08-18 | Paisley Christopher B. | 董事 (間接) | 賣出 | 125 | 0.14 |
| 2026-08-20 | Pletcher Kurt | 高階主管 | 賣出 | 135 | 0.15 |
| 2026-09-02 | Paladin Michael Shane | 高階主管 | 賣出 | 203 | 0.21 |
| 2026-09-04 | Paladin Michael Shane | 高階主管 | 賣出 | 307 | 0.32 |

**重點:**
- **CEO Fox-Martin Adaire** 於 2026-06-02 以約 $1,052–$1,061 賣出 2,935 股，金額 $3.10M。同期另有一筆 5,645 股、無成交價之紀錄 (2026-06-01)，形式上較像股權獎酬歸屬，無法確認，標示為待核實。
- **CFO Taylor Keith David:** 6 個月內無賣出紀錄 (最後一筆為 2026-03-12)。
- **最大單筆:** 董事 Meyers Charles John 於 2026-05-06 賣出 5,224 股，金額 $5.67M。
- **Paisley Christopher B.** (董事，間接持股) 於 2026-08-03 以約 $1,019 賣出 4,000 股，$4.08M；2026-08-18 另以約 $1,104 賣出 125 股。
- **賣出價區間:** 6 個月內約 $1,008–$1,104，2026-03 之前之賣出價約 $925–$975，屬於股價區間上緣之賣出。
- **無內部人買入紀錄**。
- **無成交價之交易** (多為 2026-05-21 前後之董事紀錄、以及部分高階主管於 06-01 與 09-01 之紀錄，疑為獎酬歸屬或稅款代扣): 未計入金額，待核實。

## Ownership shifts

- 內部人持股比例: 0.27% (yf insidersPercentHeld)
- 機構持股比例: 100.74% (yf institutionsPercentHeld)。**數值超過 100%，屬資料商口徑問題 (可能為重複計算)，不可直接採用。**
- 機構家數: 2,000 (yf institutionsCount)
- 機構持股趨勢 (季度變化): DATA_UNAVAILABLE。本次僅取得當期快照，無歷史比較。

## Net sentiment score

- **綜合傾向: 中性 (neutral)**，信心度: **低**
- 分析師面: 偏多 (Buy 類 85.7%，共識分數 4.03/5)
- 內部人面: 偏空 (6 個月淨賣約 $20.4M，無買入，CEO 亦有賣出)
- 聚合情緒面: 偏空 (NAGA，權重低)
- 散戶面: DATA_UNAVAILABLE (Reddit、StockTwits 均不可得)

信心度低之主因為散戶端資料完全缺失，且內部人賣出之動機 (是否屬 10b5-1 計畫或獎酬歸屬) 尚未核實。

**分歧旗標: 是 (部分分歧)。** 分析師之 85.7% 買進評等與內部人淨賣出及聚合器偏空方向相反。散戶端無資料，因此無法判斷是否構成完整之散戶與分析師分歧。

## 指標摘要

| 指標 | 數值 | 備註 |
|---|---|---|
| 綜合情緒傾向 | 中性 (neutral) | 信心度低 |
| 分析師 Buy 占比 (SB+B) | 85.7% (30/35) | yf 口徑；Barchart 口徑為 78.8% (26/33) |
| 分析師 Hold 占比 | 14.3% (5/35) | |
| 分析師 Sell 占比 | 0.0% | |
| 共識分數 (1–5) | 4.03 | 加權平均，偏 Buy |
| 近 3 個月 Buy 家數變化 | 26 → 30 (+4) | |
| 6 個月內部人淨買入 (USD M) | 0.0 | 無買入紀錄 |
| 6 個月內部人賣出 (USD M) | 約 20.4 | 僅計有成交價之公開市場賣出 |
| Benzinga 平均目標價 (USD) | 1,137 | 快照約 2026 年 8 月，已過時 |
| 散戶情緒 (Reddit / StockTwits) | DATA_UNAVAILABLE | 工具封鎖 / DNS 失敗 |
| 機構持股變化 | DATA_UNAVAILABLE | 無歷史快照 |

## 資料來源與限制

- yf 工具: recommendations、rec_summary、insider、major_holders (yahoo cookie/crumb 取得失敗，但資料已回傳)
- WebFetch: Reddit (r/wallstreetbets、r/stocks) 封鎖；StockTwits API DNS 失敗
- WebSearch: 多為聚合站與舊文，未標註日期者已於內文標示；NAGA 與 Barchart 之摘要未直接抓取全文
- 未對任何財經網站使用 WebFetch

SENTIMENT REPORT COMPLETE
