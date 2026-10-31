# Sentiment — ALB as of 2026-10-31

**資料完整度警示**: Reddit (r/wallstreetbets、r/stocks) 與 StockTwits 無法取得。散戶情緒部分**無法評估**。analyst 與 insider 數據為 yf 工具回傳, 但 analyst 摘要未附日期, 且網路新聞最新僅到 2026-07/08, 未見 10 月資料。

## Analyst consensus

rec_summary (單位為家數):

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 合計 |
|---|---|---|---|---|---|---|
| 當期 (0m) | 2 | 12 | 9 | 0 | 0 | 23 |
| -1m | 3 | 10 | 9 | 0 | 0 | 22 |
| -2m | 3 | 10 | 9 | 0 | 0 | 22 |
| -3m | 3 | 10 | 9 | 0 | 0 | 22 |

當期共 14 buy (含 strong buy) / 9 hold / 0 sell。Buy 家數較 -1m 增加 1 家, strong buy 由 3 降至 2, 整體結構穩定, 無賣方評級。

近期動向 (來源: 網路搜尋, 非 yf 工具):
- Scotiabank 於 2026-07-28 將目標價由 $215 下調至 $200, 維持 sector outperform。
- Mizuho 於 2026-07-01 將目標價下調至 $185, 評級 neutral。
- Zacks 於 2026-07-20 將評級下調至 hold。
- Citi 於 2026-06 升評至 buy, 目標價 $225。
- 各追蹤平台平均目標價約 $187 至 $207, 數值不一致。

## Retail social

- **Reddit**: 無法取得。
- **StockTwits**: 無法取得 (DNS 解析失敗)。
- **X / 新聞聲量**: 網路搜尋未找到 10 月的散戶或社群討論, 最新結果停在 2026-07/08 的分析師與新聞文章。聲量相對基準無法量化, 僅能定性判斷為**資料不足**。
- **Themes**: 無法從散戶來源歸納。從新聞側可見的敘事為 Q1 2026 財報後股價回落、目標價連續下修, 以及市場對鋰價復甦的分歧看法。這些是媒體與分析師敘事, 不是散戶貼文。
- **散戶傾向**: 無法判定 (資料缺)。

## Insider activity

以 USD 計, 單位 M (百萬美元)。6 個月窗口 = 2026-05-01 至 2026-10-31。

| 日期 | 人員 | 職位 | 類型 | 股數 | 金額 (USD M) |
|---|---|---|---|---|---|
| 2026-05-15 | Jerry Kent Masters | CEO | 公開市場賣出 (Sale, $183.12–184.52) | 16,393 | 3.01 賣出 |

- 6 個月淨額: **買入 $0.00M, 賣出 $3.01M, 淨賣出 $3.01M**。
- 窗口內另有多筆 Stock Award (授予, 非市場交易, 已排除), 以及 2026-03-12 CEO 贈與 (Gift, $5.00M, 已排除, 且不在窗口內)。
- 窗口外的近期賣出: CEO 2026-03-10 賣出 $2.01M; COO/officers 2026-02 賣出約 $0.9M 至 $1.4M。
- 窗口外的近期買入: 董事 Alejandro Wolff 於 2025-10-01 買入 $0.018M (金額極小)。
- 解讀: 內部人以 CEO 單筆賣出為主, 無公開市場買進。多數近期 insider 交易為獎勵股授予, 不宜直接解讀為看多或看空。

## Ownership shifts

- insidersPercentHeld: 0.21%, 內部人持股極低。
- institutionsPercentHeld: 102.37%, 超過 100% 屬資料計算重複 (常見於雙重計算 float 或 ADR), 實際機構持股比例應以來源為準, 不宜直接引用。
- institutionsCount: 1,282 家。
- 趨勢: 僅有單一快照, 無法判斷機構持股時間序列的增減。

## Net sentiment score

- **Analyst tilt**: 偏多 (14 buy / 9 hold / 0 sell)。但近期目標價連續下修, 顯示正面評等與目標價動能背離。
- **Insider tilt**: 偏空 (6 個月內 CEO 單筆 $3.01M 賣出, 無買進)。信心低, 因為樣本只有一筆市場交易。
- **Retail tilt**: 無法判定 (Reddit 與 StockTwits 不可用, 新聞聲量資料不足)。
- **Composite**: **中性 (neutral)**, 信心 **低**。分析師面偏多但目標價下修, 內部人面偏空但樣本小, 散戶面完全缺資料。
- **Divergence flag**: **無法判定** (缺散戶數據, 無法比較散戶與分析師傾向)。

## Data gaps and follow-ups
1. 補 Reddit 或 StockTwits 來源, 才能完成散戶面評估。
2. rec_summary 未標示資料日期, 需確認是否為 2026-10-31 當日快照。
3. 網路新聞未覆蓋 2026-08 至 10 月, 包括 Q2 2026 財報 (約 8 月初) 後的評等變動。

SENTIMENT REPORT COMPLETE
