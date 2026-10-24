# Sentiment — GFS as of 2026-10-25

**注意事項**: Reddit 兩個來源與 StockTwits 皆無法取得 (Reddit 回報 "unable to fetch", StockTwits DNS 解析失敗)。X/新聞搜尋只找到 2026-08-14 前後的快照, 找不到 10 月資料。因此散戶情緒部分**資料缺口大**, 本報告的綜合判斷信心偏低。

## Analyst consensus

23 位分析師: **13 buy** (Strong Buy 3 + Buy 10) / **9 hold** / **1 sell** (Strong Sell 1)。

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 合計 | Buy 類合計 |
|---|---|---|---|---|---|---|---|
| 本期 (0m) | 3 | 10 | 9 | 0 | 1 | 23 | 13 |
| -1m | 4 | 10 | 8 | 0 | 1 | 23 | 14 |
| -2m | 4 | 9 | 8 | 0 | 1 | 22 | 13 |
| -3m | 3 | 9 | 9 | 0 | 1 | 22 | 12 |

- 買入類比例從 -3m 的 12 家升到 -1m 的 14 家, 本期回落到 13 家; Hold 由 8 增到 9。整體仍偏正面但有降溫跡象。
- `recommendations` 工具回傳的是各期彙總分布, 不是個別升降評等事件, 因此無法列出具體 upgrade / downgrade 名單。
- 目標價: 唯一可用資料為 2026-08 快照 (Benzinga, 約 08-14): 平均目標價 $63, 股價約 $54.58; TD Cowen 維持 Buy, 目標價 $85 → $75; UBS 維持 Neutral, 目標價 $61 → $55。該快照分析師數為 19 家, 與 yf 的 23 家不一致, 原因未明。本期目標價變動無法確認。
- 股價參考 (由內部人交易價格推算): 2026-06-25 約 $87, 07-23 約 $57, 08-18 約 $51, 09-28 約 $49。股價在 6 月至 9 月間大幅回落, 10 月價格未取得 (DATA_UNAVAILABLE)。

## Retail social

- **Reddit (r/wallstreetbets, r/stocks)**: 抓取失敗 (無法連線), 無樣本可引用, 無法判斷 tilt 與討論量。
- **StockTwits**: DNS 解析失敗, 無資料。
- **X / 新聞**: 未找到 2026-10 的散戶或分析師輿情文章。Benzinga sentiment 頁面 (2026-08 快照) 顯示 short interest 約 15.0% of float, options put/call ratio 約 0.31, 30 天內內部人淨賣出。這些是 8 月資料, 僅供背景參考。
- **Buzz 量**: 無法量化; 無 10 月資料可比較。
- **Themes**: 無法從可用來源歸納。

## Insider activity

視窗: 2026-04-25 至 2026-10-25。

| 項目 | 金額 (USD M) | 筆數 |
|---|---|---|
| 公開市場賣出 (Sale) | 3.09 | 約 45 筆 |
| 公開市場買入 (Buy) | 0.00 | 0 |
| 股票獎勵 (Director grant, 07-28) | 0 (價值 0, 股數計) | 5 |
| 贈與 (Gift) | 0 | 多筆 |

**淨額: 約 -$3.09M (純賣出, 無買入)。**

主要賣方 (視窗內):

| 內部人 | 職稱 | 合計賣出 (USD M) | 特徵 |
|---|---|---|---|
| VICARI SAMUEL | Officer | 0.66 | 2026-05-11 單筆 8,692 股, 約 $657K, 價格 $75.62 |
| HOGAN MICHAEL JAMES | Officer | 約 1.28 | 約每月 1 至 2 次, 常見 2,800 股或 1,800 股; 多次另有 150 股贈與 |
| DORCHAK GLENDA MARY | Director | 0.23 | 2026-07-20 賣 4,000 股, 約 $233K, 價格 $58.22 |
| RAMAN PRADHEEPA | Officer | 0.45 | 2026-08-18 賣 6,760 股 ($345K); 2026-09-28 賣 2,145 股 ($105K) |
| AZAR SAMAK L | Officer | 約 0.47 | 約每週 1 次, 每次 335 或 500 股, 金額小但筆數多 |

觀察:
- 買入為零, 所有重大交易皆為賣出。Director 獎勵 (07-28) 為例行授予, 非市場買入。
- AZAR 的小額規律賣出與 HOGAN 的固定股數賣出, 看起來像預定計畫, 但資料中無法確認是否為 10b5-1 計畫, 需查 Form 4 附註。
- 大量賣出集中於 5 月至 8 月, 9 月後交易頻率降低。

## Ownership shifts

- 內部人持股: 0.117% (極低)。
- 機構持股: 工具回傳 100.39%, 超過 100%, 屬資料異常 (疑為多來源重複計算), 無法用於判斷集中度。
- 機構家數: 594。
- 無時間序列資料, **無法判斷機構持股趨勢**。

## Net sentiment score

- **分析師**: 偏正面 (13 buy / 9 hold / 1 sell, 買入類約 57%), 但近期買入家數由高點回落。
- **內部人**: 偏負面 (6 個月淨賣 $3.09M, 零買入, 多名 officer 與 director 參與)。
- **散戶**: 無法評估 (資料缺口)。
- **綜合**: **中性 (neutral)**, 信心**低** — 分析師正面與內部人賣出並存, 散戶端缺資料, 且股價資料停在 8 月至 9 月。

**Divergence flag: 無法判定 (散戶資料缺失)**。
- 分析師 vs 內部人: 有明顯分歧 — 分析師多數 Buy, 內部人持續淨賣出。這一點通常值得注意, 但內部人賣出也可能來自分散持股或稅務、預定計畫等非資訊性原因。
- 散戶 vs 分析師: 無資料, 無法判斷。

## 資料缺口與後續建議

1. 補抓 2026-10 的 Reddit 或 StockTwits 資料 (需替代來源或 API key)。
2. 取得 2026-10 的當期股價與目標價變動, 確認 Benzinga 與 yf 分析師家數差異。
3. 查 SEC Form 4 確認 AZAR / HOGAN 的賣出是否屬 10b5-1 計畫。
4. 取得機構持股時間序列, 並修正 100.39% 的異常數字。

## 來源

- yf 工具: recommendations, rec_summary, insider, major_holders (2026-10-25 執行)
- [Benzinga GFS sentiment](https://www.benzinga.com/quote/GFS/sentiment) (2026-08 快照, 僅作背景)
- [Benzinga 分析師評等彙整](https://benzinga.com/z/28133839) (日期不明)
- [Benzinga 文章](https://benzinga.com/z/38796240) (日期不明)

SENTIMENT REPORT COMPLETE
