# Sentiment — 6669.TW 緯穎 Wiwynn as of 2026-11-19

## Analyst consensus

yf rec_summary（0m 期）：20 家中 **6 Strong Buy / 14 Buy / 0 Hold / 0 Sell**，即 **100% BUY**（含 Strong Buy）。

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 合計 |
|---|---|---|---|---|---|---|
| 0m（當期） | 6 | 14 | 0 | 0 | 0 | 20 |
| -1m | 6 | 14 | 0 | 0 | 0 | 20 |
| -2m | 5 | 14 | 0 | 0 | 0 | 19 |
| -3m | 5 | 14 | 0 | 0 | 0 | 19 |

- 近四個月沒有出現 Hold 或 Sell 評級，評級結構穩定。Strong Buy 數在 -2m 至 -1m 之間由 5 增至 6（合計家數由 19 增至 20），這是近四個月內唯一可見的評級變動，可能是新增覆蓋或既有券商升級，無法從彙總表確認。yf `recommendations` 只回傳彙總表，沒有逐筆升降評等紀錄，因此無法確認是哪一家券商。
- 目標價變動：yf 工具未提供目標價欄位。網路搜尋的來源數字互相衝突：
  - Investing.com 快照：近 12 個月平均目標價約 7,526 至 7,569 元，最高 9,500 元、最低 6,000 元，評級「強力買入」，17 Buy / 0 Hold / 0 Sell。與 yf 的 20 家家數不同，可能是不同快照日期或統計口徑。
  - 高盛（TechNews，2026-11-16）：重申買進，12 個月目標價 4,000 元。
  - 高盛（TechNews，2026-06-15）：買進，目標價 7,147 元。
  - 高盛 11 月的 4,000 元與 6 月的 7,147 元差距過大，可能是報導誤植，也可能是目標價大幅下修，目前無法查證，本報告不採用其中任一數字作為結論依據。
- 外資近期看法（CMoney 彙整）：美銀、花旗、摩根士丹利最新報告維持正向評等，但都提醒 AI 伺服器營收占比提高與零組件成本上升會壓縮毛利率。花旗預估 Q4 毛利率降至 8.5%。

## Retail social

- **Reddit**：WebSearch 以 `r/wallstreetbets` 與 `Wiwynn 6669 TW` 查詢，沒有找到相關討論串，只有財經資料站頁面。依照本次指示未使用 WebFetch 直接讀取 Reddit JSON，因此 r/stocks 未逐一檢視。無法判斷 Reddit 聲量，記為資料不足。
- **PTT / Dcard**：搜尋結果沒有找到 2026 年 11 月的 PTT 或 Dcard 討論串。最接近的是 CMoney 股市社群彙整，留言整體偏樂觀，看好 ASIC 與 AI 運算伺服器的長線需求，同時也有人提醒價位不穩與大戶調整跡象，看法分歧。
- **StockTwits / X**：WebSearch 沒有索引到可用的貼文，此來源軟失敗，略過。
- **聲量（相對水位）**：可見來源的文章與討論量偏低，無法與前期基準做量化比較。以定性判斷，本期聲量屬於「低至中等」，主要聲音來自新聞與券商報告，而不是散戶社群。
- **散戶傾向**：可見樣本偏多（看 AI 需求），但樣本少，且含有風險提醒。

### 主要主題（Themes）

1. **AI ASIC 與 AI 伺服器放量**：多數正面意見的核心，連結到 2027 年成長預期。
2. **液冷與 GPU 機櫃**：高盛認為這些產品放量會推動 2027 年第一季成長。
3. **毛利率壓力**：Q3 毛利率 8.87%、營益率 7.47%，優於預期，但外資普遍預期 AI 伺服器比重上升與零組件漲價會壓縮後續毛利率。這是最常被提到的風險點。
4. **股價波動與大戶調整**：社群與價格相關數據都指出股價震盪，屬於看多者的風險提醒。

### 基本面數字（來自新聞，供交叉確認，單位 億 TWD）

- 2026 年 10 月營收：1,651.32 億 TWD，月增 -4.3%，年增 80.9%。
- 2026 年 1 至 10 月累計營收：約 1.15 兆 TWD（即 11,500 億 TWD），年增 54.0%。
- 2026 年前三季累計稅後純益：524.48 億 TWD，年增約 4 成。

## Insider activity

Net 6mo: 資料不足（yf `insider` 回傳空陣列）。

- 空陣列可能代表近六個月沒有申報的內部人交易，也可能是資料來源（Yahoo 的 cookie/crumb 取得失敗，已 fallback）沒有回傳。目前無法區分，因此**不能視為「零交易」**。
- 無 Notable 內部人可列。
- 持股結構參考（yf `major_holders`）：內部人持股 43.91%，機構持股 29.56%（占流通股 52.70%），機構數 347 家。

## Ownership shifts

- yf 工具只提供當期快照，沒有時間序列，因此無法判斷機構持股的增減趨勢。
- 機構家數 347 家，流通股中機構占比約 52.7%。這是當期快照，無法判斷變化方向。

## Net sentiment score

**Composite: 偏多（bullish-leaning）— 信心度：中低**

- 分析師面：強烈偏多（100% BUY，4 個月無 Hold/Sell，評級穩定）。
- 散戶面：可見樣本偏多但稀少（CMoney 社群、無 PTT/Dcard/Reddit/StockTwits 可用樣本），並帶有毛利率與股價波動的保留。
- 其他訊號：自動化新聞情緒工具對一則新聞給出 -0.35（偏負），價格相關的 Simply Wall St 頁面顯示股價跌幅後情緒轉弱。價格數據來源之間嚴重不一致（有的頁面股價約 1,645 元，有的高達 5,925 元），因此價格相關訊號的可信度低。

**Divergence flag: 否**。散戶與分析師的傾向都是偏多，沒有相反傾向的衝突。差異只在強度：分析師全數 BUY，散戶可見樣本則把毛利率與波動列為主要保留。

**Net retail sentiment call: 中性偏多（mixed-to-bullish），信心度低。** 原因是可見的散戶樣本少，無法排除偏誤。

## 資料限制

- 高盛目標價 4,000 元與 7,147 元衝突，未查證。
- 股價數字在不同快照間不一致（約 1,645 元至 5,925 元），本報告不引用具體股價作為結論。
- yf 的 cookie/crumb 取得失敗，已 fallback；insider 空陣列未能確認是否真的沒有交易。
- Reddit、StockTwits、X 與 PTT/Dcard 都沒有可用樣本，本報告的散戶判斷只能依賴 CMoney 社群彙整，樣本不足。
- 本報告只描述情緒，不構成交易建議。

## 來源（WebSearch 參考）

- TechNews 高盛 4,000 元目標價（2026-11-16）：https://finance.technews.tw/2026/11/16/wiwynn-4000-target-price/
- TechNews 10 月營收（2026-11-06）：https://finance.technews.tw/2026/11/06/wiwynn-6669-202610-financial-report/
- TechNews 高盛 7,147 元目標價（2026-06-15）：https://finance.technews.tw/2026/06/15/gs_wiwynn-asic-ai/
- Investing.com 共識頁：https://www.investing.com/equities/wiwynn-consensus-estimates
- CMoney 6669 社群：https://www.cmoney.tw/follow/channel/stock-6669

SENTIMENT REPORT COMPLETE
