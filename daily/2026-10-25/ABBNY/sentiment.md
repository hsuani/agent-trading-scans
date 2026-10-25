# Sentiment — ABBNY as of 2026-10-25

**資料品質警示**: 本次 Reddit、StockTwits 皆無法取得, 社群情緒欄位為空白。yf 工具執行時 cookie/crumb 取得失敗 (ConnectionError), 但仍回傳資料, 數值可能為快取, 需人工核對。`recommendations` 指令回傳的是評級分布趨勢, 不是評級變動明細。

## Analyst consensus

目前 (0m) 6 位分析師: 0 strong buy / 0 buy / 5 hold / 0 sell / 1 strong sell。以 sell 計, 即 **0 buy / 5 hold / 1 sell**。

評級分布趨勢 (yf, 分析師人數):

| 期間 | Buy 類 | Hold | Sell 類 | 合計 |
|---|---|---|---|---|
| 0m (當前) | 0 | 5 | 1 | 6 |
| -1m | 0 | 3 | 2 | 5 |
| -2m | 0 | 3 | 2 | 5 |
| -3m | 0 | 3 | 2 | 5 |

最近一個月 Sell 類由 2 降為 1, Hold 由 3 增為 5, 方向偏向中性化。

**與網路來源衝突**: 網路資料顯示 2026-07-16 Pareto 由 Hold 升至 Buy (目標價 CHF 96.40), DNB Carnegie 同日有評級變動 (方向未明), 7/21 有 Sector Perform 重申。另有 MarketBeat 2026-04 資料為 3 Strong Buy / 3 Hold / 3 Sell。yf 與網路來源的分析師樣本差異很大, 無法確定哪一組為準。

**目標價 (CHF, 多數為未標日期, 可能過期)**:
- JPMorgan: 80 (Neutral), 由 70 上調
- Citi: 85 (Neutral), 由 78 上調
- RBC: 83 (Sector Perform), 由 81 上調
- DZ Bank: 95 (Buy)
- Simply Wall St 彙整 9 月初目標區間 CHF 80–96
- Handelsbanken: Underperform, $67 (未標日期)
- Barclays: CHF 36 (搜尋結果中的舊資料, 與目前價位差距過大, 不採信)

**其他公司事件 (未標日期)**: 網路出現 ABB 與 Rotork 達成建議現金收購協議的報導, 金額約 $5.5B。對評級的影響未知。

## Retail social

- **Reddit (r/wallstreetbets, r/stocks)**: 全數失敗。WebFetch 回傳 "unable to fetch", curl 回 CONNECT 403。無法評估情緒傾向與討論量。
- **StockTwits**: WebFetch 回 DNS 解析失敗 (ENOTFOUND), curl 回 CONNECT 403。無資料。
- **X / 新聞與意見網站**: Stockchase 意見區為混合, 含 BUY 標記與 $55.92 目標價 (日期不明, 僅供參考)。未取得可引用的個別貼文原文。
- **討論量**: 無法量化, 無法與平時基準比較。
- **傾向**: 不可判定 (資料不足)。
- **主題 (來自網路財經報導, 非社群原文)**:
  - 正面: 電氣化與資料中心需求成長
  - 負面: 估值偏高 (Yahoo 顯示 trailing P/E 38.16、forward P/E 31.06)、景氣循環風險、利潤率回升不確定性 (Geojit 2026-08 對 ABB India 給予 REDUCE, 理由為利潤率與估值)、全球保護主義與成本壓力 (Simply Wall St 敘事)

## Insider activity

Net 6mo: $0 買入 / $0 賣出 (資料來源回傳空陣列, 無交易紀錄)。

**此數字不等於確認為零交易**。ABBNY 為瑞士公司 ADR, 內部人交易申報路徑與美國 Form 4 不同, yf 可能未覆蓋。目前無法判定 CEO/CFO 是否有交易。

## Ownership shifts

- `institutionsPercentHeld` 回傳 0.00202, 明顯為單位錯誤 (可能是比率與百分比混用), 無法採用。
- `institutionsCount` = 88 (機構持有人數, 可參考)。
- `insidersPercentHeld` = 0.0, 疑為未計算, 不採信。
- 無時間序列, 無法判定機構集中度趨勢。

## Net sentiment score

- **分析師面**: 偏中性 (0 buy / 5 hold / 1 sell 為 yf 數據; 網路資料含 Pareto Buy 與 DZ Bank Buy, 整體混合)。
- **零售面**: 無資料。
- **內部人面**: 無資料, 不能視為中性或看多。
- **綜合**: **中性 (Neutral)**, 信心度 **低**。原因是社群與內部人資料缺失, 分析師資料來源彼此衝突。

**背離旗標: 無法判定** (缺少零售傾向)。目前唯一可用的對照是分析師偏 Hold 與網路意見偏中性的混合, 未出現明確背離。

**補足建議**: 重新執行 yf (確認 cookie/crumb 是否恢復); 以 SIX 或 ABB 官網 (瑞士) 查詢內部人交易; 社群資料需改用其他來源或代理 (Reddit 與 StockTwits 目前皆被代理封鎖)。

SENTIMENT REPORT COMPLETE
