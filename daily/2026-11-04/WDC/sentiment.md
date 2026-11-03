# Sentiment — WDC as of 2026-11-04

> 資料限制: 本報告日期 (2026-11-04) 晚於執行當日 (2026-11-03)。yf 內部資料最後一筆內部人交易為 2026-10-21；Reddit 與 StockTwits 無法取得；WebSearch 未找到 2026-11 的任何相關輿情。以下結論的可信度因此偏低。

## Analyst consensus

26 位分析師: 4 strongBuy / 17 buy / 5 hold / 0 sell / 0 strongSell (yf `rec_summary`，0m / -1m / -2m 三個期間數字完全相同)。

| 指標 | 數值 |
|------|------|
| Buy 類 (strongBuy + buy) | 21 (約 81%) |
| Hold | 5 (約 19%) |
| Sell 類 | 0 |
| 共識評等 | Buy |

近期升降評等: yf `recommendations` 僅回傳彙總計數，無逐筆升降評等紀錄；三個期間計數不變，代表近兩個月評等結構沒有變動，或資料來源未更新。無法確認個別分析師的升降評等。

目標價: yf 工具未提供。WebSearch 結果中的目標價 (Benzinga 約 $149，TipRanks 約 $115) 屬於 2025 年底或較早的快照，遠低於 2026 年 6 至 10 月的成交價區間 (約 $380–556)，不可作為當前目標價使用。

資料來源 (WebSearch 轉引，時間為 2026 年 5 至 6 月): Barchart 2026-05 報告共識 "Strong Buy"；MarketBeat 2026-06 報告共識 "Moderate Buy"，Mizuho 與 Citi 維持看多，UBS 態度保守。

## Retail social

- Reddit (r/wallstreetbets、r/stocks): 無法取得。WebFetch 回傳 "Claude Code is unable to fetch from www.reddit.com"，依規則略過，無貼文樣本與情緒傾向。
- StockTwits: 無法取得。api.stocktwits.com DNS 解析失敗 (ENOTFOUND)，需在 session 網路設定中允許該網域後才能重試。
- X / 新聞輿情 (WebSearch 替代): 未找到 2026-11 的相關資料。2026 年前半的評論偏多，主軸是 AI 與資料中心儲存需求。WebSearch 另指出部分 2026 年中期的選擇權流量快照偏空 (put 多於 call)，但不同時點的結論互相衝突，無法確認當前狀態。
- 聲量 (buzz volume): 無法量化，無 Reddit 或 StockTwits 基準可比。
- 情緒傾向: 無法判定 (資料缺失)。
- 主要主題 (依 2026 年前半外部報導整理，非本期直接觀察): AI 資料中心的 HDD 與高容量儲存需求；估值偏高的疑慮；股價自 6 月高點回落後的獲利了結情緒。

## Insider activity

6 個月區間 (2026-05-03 至 2026-11-03)，依 yf `insider` 計算:

- 公開市場賣出: 19 筆，合計 約 $27.55M (USD)
- 公開市場買入: 0 筆，$0
- 股票授予 (Stock Award / Grant): 8 筆，屬例行薪酬，不計入買賣淨額
- 淨額: 約 -$27.55M (純賣出，無買進)

各內部人賣出金額 (USD):

| 內部人 | 職稱 | 賣出金額 (USD M) |
|--------|------|----------------|
| TAN IRVING | Chief Executive Officer | 8.90 |
| DAVIS BRIAN SCOTT | Officer | 5.01 |
| GUBBI VIDYADHARA K | Officer | 4.27 |
| COLE MARTIN I | Director | 3.86 |
| TREGILLIS CYNTHIA LOCK | Officer | 2.59 |
| STREETER STEPHANIE A | Director | 2.52 |
| KIDDOO BRUCE E | Director | 0.40 |

值得注意的交易:
- CEO TAN IRVING 2026-08-11 賣出 20,000 股，均價約 $444 (約 $8.90M)；同類型交易 2026-05-01 (約 $8.24M，價約 $406–415) 與 2026-02-02 (約 $5.11M)。
- 董事 COLE MARTIN I 2026-06-09 與 2026-07-28 合計賣出約 $3.86M。
- 2026-10-21 Officer TREGILLIS CYNTHIA LOCK 以 $380.00 賣出 807 股 (約 $0.31M)，為窗口內最後一筆可見交易，價格低於 2026 年 6 至 8 月的賣出價。

解讀: 賣出金額龐大且集中在 CEO 與多位高階主管，無任何公開買進。賣出價格自 2026-06 的約 $545–556 下滑至 10 月的約 $380，屬於高價位分批出脫，不是低價承接。但多數為定期或計畫性賣出 (例如固定股數的 20,000 股)，未必反映內部人對基本面的判斷。

## Ownership shifts

- 機構持股比例: 約 88.4%；機構數 2,443 家 (yf `major_holders`)。
- 內部人持股比例: 約 0.27%。
- 趨勢: 單一時點快照，無法判定季度間的增減。

## Net sentiment score

Composite: **neutral** (信心: 低)

- 分析師面: 偏多 (21 Buy 類 / 26，零 Sell)，權重高，但計數兩個月未變動，時效性不明。
- 內部人面: 偏空 (6 個月淨賣出約 $27.55M，零買進，高價位賣出)，解讀上需考慮計畫性交易的因素。
- 散戶面: 無資料，無法計入。

Divergence flag: **無法判定** — 散戶端資料缺失，無法比較散戶與分析師傾向是否相反。若後續取得 Reddit 或 StockTwits 資料，應重新評估此欄位。

重試建議: (1) 在 session 網路設定允許 api.stocktwits.com 後重新抓取；(2) Reddit 需改用其他可用管道或授權存取；(3) 補上 2026-11 的 yf 資料以確認 rec_summary 是否為最新快照。

SENTIMENT REPORT COMPLETE
