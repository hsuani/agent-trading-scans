# Sentiment — LWLG as of 2026-11-02

資料完整度: 低。Reddit 與 StockTwits 無法取得 (見下方), WebSearch 只回傳重複的舊頁面 (日期 2026-04-16), 不採用。分析師與內部人資料可用, 但樣本很薄。

## Analyst consensus
目前 rec_summary: 1 buy / 0 hold / 0 sell (共 1 位分析師, strongBuy 0, strongSell 0)。
最近升降評等: yf recommendations 只回傳當期彙總, 無歷史評等變動紀錄, 無法判斷近期升級或降級, 也無法判斷目標價變化。
結論: 覆蓋家數極少, 「一致買進」的訊號強度有限。

## Retail social
- Reddit (r/wallstreetbets, r/stocks): 無法取得。WebFetch 回傳 "Claude Code is unable to fetch from www.reddit.com", 無法判斷討論量與多空傾向。
- StockTwits: 無法取得。api.stocktwits.com DNS 解析失敗 (ENOTFOUND), 需在 session 網路設定中放行此網域後才能重試。
- X / 新聞討論: WebSearch 查詢結果為同一批重複的鏡像頁面 (日期 2026-04-16), 內容為通用模板, 沒有可用的 2026-11 前後討論, 不列為證據。
- 討論量 (相對於典型水準): 無法判斷。
- 多空傾向: 無資料, 無法判定 bullish / bearish / mixed。
- 主要話題: 無資料。

## Insider activity
查詢區間: 2026-05-02 至 2026-11-02 (6 個月)。

| 日期 | 內部人 | 職位 | 交易 | 股數 | 金額 (USD M) |
|---|---|---|---|---|---|
| 2026-06-01 | QUAN SNIZHANA P | Officer | 賣出 @ 11.41 | 345 | 0.0039 |
| 2026-06-01 | 5 位董事 (Connelly, Bucchi, El-Ahmadi, Partridge, Ciesla) | Director | 股票獎勵 (grant) | 各 13,612 | 0 (無現金) |
| 2026-06-01 | QUAN SNIZHANA P | Officer | 股票獎勵 (grant) | 2,500 | 0 (無現金) |
| 2026-07-24 | GRAFFAM FRED ALBERT III | Chief Financial Officer | 股票獎勵 (grant) | 396,694 | 0 (無現金) |

- 6 個月內公開市場買進: 0 筆, 0 USD M。
- 6 個月內公開市場賣出: 1 筆 (Officer, 約 0.0039 USD M)。
- 淨額 (6 個月): 買進 0 USD M / 賣出約 0.004 USD M, 淨賣出極小。
- 重點: CEO (LE MAITRE YVES) 與 CFO 在區間內沒有公開市場買進。CFO 的 396,694 股為獎勵, 不是買進。
- 區間外參考 (不計入 6 個月淨額): 2026-04-01 至 04-10 有多筆董事與 Officer 賣出, 合計約 0.4 USD M 以上 (例如 EL-AHMADI 2026-04-07 賣出 54,536 股, 約 0.42 USD M)。2026-03-30 Quan 賣出 25,000 股, 約 0.18 USD M。這些是較早的賣壓, 不影響 6 個月淨額, 但可作為背景。
- 解讀: 區間內以獎勵性股權發放為主, 沒有可見的內部人加碼買進訊號。

## Ownership shifts
- insidersPercentHeld: 1.08%
- institutionsPercentHeld: 38.78%
- institutionsFloatPercentHeld: 39.21%
- institutionsCount: 225
- 趨勢: yf 只提供當期快照, 無法判斷機構持股的增減趨勢。

## Net sentiment score
Composite: **neutral** (信心: 低)

- 分析師: 偏多, 但只有 1 位分析師, 證據力弱。
- 內部人: 中性偏淡, 區間內無公開市場買進, 僅一筆極小額賣出, 其餘為獎勵。
- 散戶: 無資料, 不計入評分。
- 整體因資料缺口大而定為中性, 信心低。

Divergence flag: **無法判定 (no)**。散戶資料缺失, 無法比較散戶與分析師的傾向是否相反。若日後 Reddit / StockTwits 可取得, 應重新評估此項。

## 資料缺口與後續
1. Reddit (r/wallstreetbets, r/stocks) 被封鎖, 需要代理或網域放行後重試。
2. api.stocktwits.com 解析失敗, 需在 session 網路設定中放行。
3. 分析師歷史評等與目標價資料缺失, 建議補抓。
4. 機構持股趨勢缺乏多期資料。

SENTIMENT REPORT COMPLETE
