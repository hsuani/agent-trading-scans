# Sentiment — NEE as of 2026-10-28

資料來源狀態: yf CLI 成功 (recommendations / rec_summary / insider / major_holders，Yahoo cookie/crumb 失敗但資料有回傳)。Reddit (r/wallstreetbets, r/stocks) 被拒絕存取 (DATA_UNAVAILABLE)。StockTwits 網域無法解析 (DATA_UNAVAILABLE，需在 session 網路設定允許 api.stocktwits.com)。WebSearch 有少量二手來源。

## Analyst consensus

分析師評等分布 (yf rec_summary, 期間 0m，共 22 位):

| 評等 | 人數 | 佔比 |
|---|---|---|
| Strong Buy | 2 | 9% |
| Buy | 12 | 55% |
| Hold | 7 | 32% |
| Sell | 1 | 5% |
| Strong Sell | 0 | 0% |

買進側 (Strong Buy + Buy) 共 14 位，約 64%。

近四個月趨勢 (人數):

| 期間 | Strong Buy | Buy | Hold | Sell | 買進側合計 |
|---|---|---|---|---|---|
| 0m (本期) | 2 | 12 | 7 | 1 | 14 |
| -1m | 3 | 11 | 6 | 1 | 14 |
| -2m | 2 | 10 | 7 | 1 | 12 |
| -3m | 2 | 11 | 7 | 1 | 13 |

Recent moves: yf recommendations 只回傳月度彙總，沒有個別升評降評紀錄，因此「具體 upgrade / downgrade 事件」為 DATA_UNAVAILABLE。整體評等分布近四個月大致持平，僅 Strong Buy 由 3 降為 2、Hold 由 6 升為 7，屬小幅變動。

目標價變動: yf 工具未提供目標價欄位，DATA_UNAVAILABLE。WebSearch 找到兩筆個別目標價，但年份在摘要中不明確，僅供參考，未經核實:
- Evercore ISI 維持 Buy，目標價 $107 (摘錄日期為 7/28，年份未確認)
- Goldman Sachs 重申 Buy，目標價 $94 (摘錄日期為 1/30，年份未確認)

來源不一致: Barchart 摘錄為 23 位分析師 (15 Strong Buy / 7 Hold / 1 Strong Sell)，與 yf 的 22 位分布不同 (yf 無 Strong Sell 而 Barchart 有 1 位)。本報告以 yf 為主。Barchart 統計為 "Moderate Buy"，其餘多為 Buy 方向，與 yf 結論一致。

## Retail social

- Reddit (r/wallstreetbets, r/stocks): DATA_UNAVAILABLE。WebFetch 被拒絕存取 reddit.com，無法取得貼文數、分數與留言。因此無法給出討論量與語氣的一手樣本，也無法引用代表性貼文。
- StockTwits: DATA_UNAVAILABLE。api.stocktwits.com 無法解析，未取得訊息流與 bullish/bearish 標籤。
- X / 新聞 / 二手聚合來源 (WebSearch):
  - 一篇德文 TipRanks 相關頁面 (標示日期為 2026 年 10 月，但具體日期未確認，可能落在 10/28 之後，屬 unknown) 顯示: 散戶/大眾情緒分數 VERY-NEGATIVE，短期訊號 BEARISH；同頁也出現部分部落客偏多的讀數，訊號分歧。該頁提到股價年初至今約下跌 6.6%，為未經核實的二手數字。
  - Benzinga 摘錄 (9 月快照): 空單比例約 2.4% of float，選擇權 put/call ratio 約 0.72。這兩項屬於中性偏保守的市場結構訊號，不是純散戶情緒。
- 討論量 (buzz volume): DATA_UNAVAILABLE。無法取得 Reddit / StockTwits 提及次數，無法與歷史基準比較。
- 主要主題 (Themes): 由於一手社群資料全數缺失，無法列出可信主題。WebSearch 與二手頁面中反覆出現的關鍵字為「分析師看多但股價與情緒偏弱」的落差，以及 data center 用電需求相關的成長敘事，但這些僅來自媒體摘要，非散戶原文，置信度低。

Retail tilt: 偏空 (低置信)，依據僅為單一二手聚合頁面與 9 月的空單/選擇權快照，不足以代表整體散戶情緒。

## Insider activity

yf insider feed 的最新一筆交易日期為 2026-03-13。6 個月視窗 (2026-04-28 至 2026-10-28) 內沒有任何紀錄，因此該視窗的內部人交易為 DATA_UNAVAILABLE (可能是 feed 快取過期，不代表沒有交易)。

以下為 feed 中可見的 2026 年初至 3/13 的紀錄 (USD，僅作背景參考):

| 期間 | 公開市場買入 | 公開市場賣出 (約) | 主要人員 |
|---|---|---|---|
| 2026-01-01 ~ 2026-03-13 | 0 | $17.9M | CEO John Ketchum (2/9，約 $8.9M)；CFO Michael Dunne 無此期間紀錄；Officer Charles Sieving (2/4，$2.7M)；Ronald Reagan (1/22、2/4、2/17，合計約 $3.1M)；Terrell Crews (3/9，約 $1.8M)；James May、Mark Lemasney、Nicole Daggs (3/9–3/13，合計約 $1.5M) |

說明:
- 上表 $17.9M 為 feed 內 "Sale" 紀錄的加總，為估算值。
- 期權行使 (Conversion of derivative) 與股票授予 (Stock Award) 不計入上述賣出金額，僅加總 "Sale" 紀錄。
- feed 中 2024-11 以後沒有任何公開市場買入紀錄。
- 值得注意: CEO John Ketchum 於 2/9 行使 99,603 股選擇權後，以約 $89.34 全數賣出，為期間內金額最大的一筆。

Net 6mo (2026-04-28 至 2026-10-28): DATA_UNAVAILABLE (feed 無紀錄)。
前段可見期間 (2025-10 起至 2026-03-13 的 "Sale" 紀錄): 約 $17.9M 賣出，買入 $0。

## Ownership shifts

yf major_holders 僅回傳單一快照，無時間序列:
- 機構持股比例: 約 86.5%
- 內部人持股比例: 約 0.12%
- 機構家數: 3,834

機構集中度趨勢: DATA_UNAVAILABLE (無歷史快照可比較)。

## Net sentiment score

Composite: 中性 (信心低)。

- 分析師面: 偏多。買進側 64%，近四個月大致持平，無降評事件可見。信心中等 (有來源不一致)。
- 散戶面: 偏空 (低置信)。僅一個二手聚合來源與 9 月的空單/選擇權快照。Reddit 與 StockTwits 完全缺失。
- 內部人面: 偏保守。feed 顯示 2025-10 起至 2026-03 有持續賣出 (約 $17.9M)，無公開市場買入；但 2026-04 後的資料缺失，無法判斷近期動向。
- 機構面: 高持股比例 (86.5%) 為穩定訊號，無趨勢資料。

Divergence flag: yes (低置信)。分析師整體偏多，而可取得的散戶/市場情緒訊號偏空。但散戶端證據極薄，且 Reddit 與 StockTwits 缺失，此分歧不應視為確定訊號。若補齊社群資料後仍呈現散戶偏空，分歧才具參考價值。

資料缺口清單 (供下游判斷):
1. Reddit 貼文量與語氣: DATA_UNAVAILABLE
2. StockTwits 訊息流: DATA_UNAVAILABLE (需允許 api.stocktwits.com)
3. 個別升評降評與目標價變動: DATA_UNAVAILABLE (yf 僅月度彙總)
4. 2026-04-28 至 2026-10-28 內部人交易: DATA_UNAVAILABLE (feed 最新至 2026-03-13)
5. 機構持股趨勢: DATA_UNAVAILABLE (單一快照)
6. 散戶情緒來源日期: 部分來源日期 unknown，可能在 10/28 之後，已排除不採用於決策

SENTIMENT REPORT COMPLETE
