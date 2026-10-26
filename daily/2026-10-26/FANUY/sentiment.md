# Sentiment — FANUY (Fanuc ADR) as of 2026-10-26

資料完整度：分析師評等可取得（僅 2 位分析師，覆蓋薄）；Reddit 與 StockTwits 皆無法取得，散戶面為空白；內部人交易資料為空；持股資料可疑。整體信心偏低。

## Analyst consensus
2 hold / 0 buy / 0 sell（0m、-1m、-2m 三期皆同，無變動）。
- 近期升降評等：`recommendations` 工具只回傳期數統計，未提供個別升降級紀錄，無法確認近期 upgrade/downgrade。
- 目標價：無 USD 計價的最新目標價。網路來源提到舊的目標價 JP¥5,066（最樂觀 JP¥6,000），屬日股幣別且日期不明，不可直接與 FANUY 美元價比較。
- 評等衝突：一則 2026-10-08 前後的 Seeking Alpha 文章（經 Pluang 轉載）給 Buy 評等，與 Yahoo 類資料的 2 hold 不一致。可能是不同來源或不同分析師，尚未查證原文。

| 項目 | 數值 |
|---|---|
| Strong Buy / Buy | 0 / 0 |
| Hold | 2 |
| Sell / Strong Sell | 0 / 0 |

## Retail social
- Reddit（r/wallstreetbets、r/stocks）：無法取得。工具回報 "unable to fetch from www.reddit.com"，視為 soft-fail，未取得任何討論串，因此無法判斷聲量與傾向。
- StockTwits：無法取得。DNS 解析失敗（api.stocktwits.com 無法連線），soft-fail。
- X / 新聞散戶語氣：網路搜尋結果中沒有可辨識的散戶貼文。主要內容是經紀商與聚合站頁面，包括 Investing.com 的技術信號 "Strong Sell"（資料標示為 2026-07-31，可能過時）與 MarketBeat 舊資料（新聞情緒 0.49，屬 FANUF 快照，非當期）。
- 聲量：無法量化，現有資料無法判斷相對於平常的水位。
- 主題（從新聞來源歸納，非散戶貼文）：
  - 工廠自動化（Factory Automation）成長，受日本工具機訂單帶動。
  - 北美機器人銷售據報年增 21%，與美國再工業化題材相關。
  - 2026-07-31 季報據報 EPS 0.17 高於預期 0.16，營收 1.48B（USD）略高於預期 1.47B。此數字來自單一聚合來源，未以原始財報核對。
- 引言樣本：無可引用的散戶貼文。

## Earnings catalyst 狀態
- 下一季財報日期來源不一：有的標 2026-10-22，有的標 10-23 或 10-30，皆未經公司公告確認。
- 找不到 2026-10-22 財報結果或盤後股價反應的報導。因此財報後的情緒方向完全未知，這是本報告最大的資料缺口。

## Insider activity
Net 6mo：$0 買入 / $0 賣出（資料為空，`insider` 工具未回傳任何交易）。
- 解讀：Fanuc 為日本上市公司，內部人申報主要在日本進行，美國 Form 4 不存在屬預期現象。此空值不代表內部人無交易，只代表本工具無法觀察。

## Ownership shifts
- `major_holders` 回傳：機構持股比例 0.229%、機構家數 27、內部人持股 0.0%。
- 0.229% 機構持股比例明顯偏低，與一家全球大型工業股不符，疑為 Yahoo 類資料對 OTC ADR 的計算缺陷，不應用於判斷集中度。
- 無歷史趨勢資料，無法判斷機構增減方向。

## Net sentiment score
Composite：**中性（neutral），信心低**。
- 分析師面：中性偏多。2 hold 無賣出，另有一則 Buy 評等的網路來源，但未能核實。
- 散戶面：無資料，不納入評分。
- 內部人面：無資料，不納入評分。
- 技術面標註（非本代理人職責，僅供參照）：Investing.com 的 Strong Sell 信號日期過舊。

Divergence flag：**無法判斷（資料不足）**。散戶面缺席，無法與分析師傾向比對。若日後取得 Reddit 或 StockTwits 資料，需重新評估。

## 建議後續查證（僅資料面，非交易建議）
1. 確認 FANUY 2026 Q3 財報實際公布日期與市場反應（公司 IR 或日本財經媒體）。
2. 以原始來源核對 Seeking Alpha Buy 評等的分析師與日期。
3. 以替代來源重試 Reddit（例如 old.reddit 或其他公開 API）與 StockTwits，或改用 X 搜尋。
4. 以 FANUC 日股（TSE:6954）的評等與目標價做交叉比對，並換算為 USD 後再比較。

來源：
- [Pluang — Fanuc 近期發展](https://pluang.com/en/news-feed/perkembangan-terkini-fanuc-dan-data-menjanjikan)
- [Investing.com — Fanuc Corporation (FANUY)](https://www.investing.com/equities/fanuc-corporation)
- [MarketBeat — FANUY](https://www.marketbeat.com/stocks/OTCMKTS/FANUY)
- [Simply Wall St — Fanuc 第三季後分析師調整估計](https://simplywall.st/stocks/jp/capital-goods/tse-6954/fanuc-shares/news/analysts-are-updating-their-fanuc-corporation-tse6954-estima)
- [Digrin — Fanuc (FANUF) 財報](https://www.digrin.com/stocks/detail/FANUF/earnings)
- [TipRanks — Fanuc (DE:FUCA)](https://www.tipranks.com/stocks/DE:FUCA)

SENTIMENT REPORT COMPLETE
