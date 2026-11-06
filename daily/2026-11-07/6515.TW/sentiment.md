# Sentiment — 6515.TW (穎崴科技 WinWay) as of 2026-11-07

## Executive summary

- 分析師評級面偏多: yf 顯示 12 buy / 0 hold / 0 sell (strongBuy 4、buy 8)，近三個月評級結構幾乎沒有變動，沒有看到降評。
- 零售與社群情緒無法完整量測: Reddit 與 StockTwits 皆無法取得，WebSearch 只拿到 CMoney 股市討論區的 AI 彙整摘要，且頁面標示資料時間不明，可信度有限。
- 內部人交易資料為空: yf `insider` 回傳空陣列，這代表工具沒有資料，不等於內部人沒有交易，需視為未知。
- 法人持股比例約 29.8%，機構數 117 家；屬單次快照，無法判斷趨勢。
- 綜合判斷: 分析師面偏多、零售面證據不足、內部人面未知。整體情緒傾向偏多但信心低。

## Data availability

| 來源 | 狀態 | 備註 |
|---|---|---|
| yf `rec_summary` | 可用 | 3 個月 (0m / -1m / -2m) 買賣評級分布 |
| yf `recommendations` | 部分可用 | 回傳內容與 rec_summary 相同，未見個別升降評事件明細 |
| yf `insider` | 空值 | 回傳 `[]`，TW 個股內部人資料可能未被 yfinance 收錄，無法確認是否真的無交易 |
| yf `major_holders` | 可用 | 單次快照，無歷史序列 |
| Reddit (r/wallstreetbets, r/stocks) | 不可用 | WebFetch 被沙箱擋下，無法取得 |
| StockTwits | 不可用 | `api.stocktwits.com` 無法解析，需由使用者在沙箱網路設定中放行，本次未重試 |
| WebSearch (CMoney、新聞彙整) | 部分可用 | 只有摘要層級，無法對應到具體發文日期與數量 |
| 2026-11 當月資料 | 缺 | WebSearch 結果最新停在 2026 年 9 月中，無 11 月資料 |

本報告未引用其他日期 `daily/` 報告的數字。

## Retail / social sentiment read

- **聲量**: 無法量化。Reddit 與 StockTwits 皆未取得，無法比較當前提及次數與平常水準。
- **CMoney 股市討論區 (AI 彙整摘要，非原文)**:
  - 摘要一: 市場情緒偏保守，有人對近期跌幅感到失望，但也提到小幅反彈，整體氣氛偏樂觀但謹慎。
  - 摘要二: 焦點在基本面與法規風險，同時有人看好後市，並留意到外資持續買進、投信持續賣出的資金面分歧。
  - 頁面本身也標示目前「沒有任何討論」，因此上述摘要的代表性不足，不應當作定論。
- **主要題材 (依摘要歸納)**:
  - AI 與 HPC 需求帶動高階測試座與 MEMS 探針卡出貨。
  - 月營收高成長 (8 月年增約 233%)，但 9 月月增轉負。
  - 股價波動大、估值偏高，是多方與空方共同提到的風險點。
  - 外資與投信買賣方向分歧。
- **零售傾向判定**: 混合偏多 (低信心)。依據僅來自 AI 彙整摘要，不足以支撐強結論。

## Analyst consensus

12 buy / 0 hold / 0 sell (yf, 0m 快照)。

| 期間 | strongBuy | buy | hold | sell | strongSell | 合計 |
|---|---|---|---|---|---|---|
| 0m (當前) | 4 | 8 | 0 | 0 | 0 | 12 |
| -1m | 4 | 7 | 0 | 0 | 0 | 11 |
| -2m | 4 | 7 | 0 | 0 | 0 | 11 |

- **近期變動**: 0m 相較 -1m 增加 1 家 buy，未見 hold 或 sell 出現；無降評紀錄。
- **目標價**: yf 工具未提供目標價序列。WebSearch 摘要中提到 Citi 目標價 13,000 TWD，日期不明，無法確認是否為最新。另一來源 (Investing.com) 顯示平均目標價相對現價有明顯下行空間 (約 -36%)，但兩者快照時間不同，無法對帳，且此數字與 Citi 目標價的關係不清楚，請勿直接採用。
- **評級數量偏少**: 12 家覆蓋分析師對一檔小型 TW 個股而言屬於不少，但評級集中於買進，無賣方反向意見。

## Institutional / insider signal

**內部人 (insider)**
- 本次 yf `insider` 回傳空陣列，無法計算 6 個月淨買賣金額，亦無法確認 CEO / CFO 的交易情況。
- 狀態: 未知 (資料缺漏，非「無交易」的確認)。
- 內部人持股比例 (yf major_holders): 約 29.4%。持股高，但單看快照無法判斷近期增減。

**機構持股 (major_holders 快照)**
- 機構持股比例: 約 29.8% (占總股本)；占流通股比例約 42.2%。
- 機構家數: 117 家。
- 趨勢: 無歷史序列，無法判斷集中度上升或下降。
- 解讀: 機構占流通股比例不低，但這是單點資料，需下一次快照才能看出趨勢。

**資金面 (摘要提及)**
- 有摘要指出外資持續買進、投信持續賣出，方向分歧。來源為 AI 彙整，未經原始籌碼數據驗證。

## Overall sentiment verdict

**綜合情緒分數**: 偏多 (信心: 低)

| 面向 | 判讀 | 信心 |
|---|---|---|
| 分析師評級 | 偏多 (12 buy / 0 sell，無降評) | 中 |
| 零售 / 社群 | 混合偏多 (僅 AI 摘要，無 Reddit/StockTwits) | 低 |
| 內部人 | 未知 (資料為空) | — |
| 機構持股 | 持股比例中等偏高，無趨勢 | 低 |

**背離旗標**: 無法判定。零售面證據不足，無法確認零售傾向是否與分析師傾向相反。若後續取得 CMoney 原文或 PTT 討論串，需再檢查是否出現「分析師全買、零售轉空」的背離。

**資料限制說明**:
1. Reddit 與 StockTwits 皆不可用，零售情緒主要依據不完整的摘要。
2. 內部人資料為空，無法排除內部人大量賣出的可能。
3. 2026 年 11 月當月資料缺漏，本報告為 9 月前後資訊加上 yf 快照的組合。
4. 本報告不含交易建議，僅描述情緒狀態。

**營收交叉檢查 (供其他分析師參考)**: 8 月營收 17.06 億 TWD，9 月營收 12.5 億 TWD，月增約 -26.7%，與 17.06 → 12.5 的計算結果一致。金額單位為 TWD 億。

## Sources

- yf 工具輸出 (本地執行): `pipeline/tools/yf.py 6515.TW rec_summary`、`recommendations`、`insider`、`major_holders`，2026-11-06 執行。
- WebSearch: 「6515 穎崴科技 股票 討論 情緒 2026年11月」 — 相關連結包括:
  - https://www.cmoney.tw/forum/stock/6515?tab=news
  - https://www.cmoney.tw/forum/stock/6515?tab=column
  - https://www.cmoney.tw/forum/stock/6515?tab=report
  - https://udn.com/news/story/7253/9569333
  - https://tw.stock.yahoo.com/quote/6515.TW/revenue
  - https://www.nstock.tw/6515
  - 注意: 上述連結為搜尋結果列出的頁面，本次僅依搜尋摘要引用，未逐頁開啟原文。
- WebSearch: 「WinWay 6515.TW stock opinion sentiment November 2026」 — 相關連結包括:
  - https://stockanalysis.com/quote/tpe/6515/forecast/
  - https://www.investing.com/equities/winway-tech-consensus-estimates
  - https://simplywall.st/stocks/tw/semiconductors/twse-6515/winway-technology-shares
  - 注意: 上述來源日期不一，部分為無日期快照，僅作參考。
- 未取得: Reddit (r/wallstreetbets、r/stocks) — WebFetch 被沙箱阻擋；StockTwits — `api.stocktwits.com` 無法解析，需使用者於沙箱網路設定放行。

SENTIMENT REPORT COMPLETE
