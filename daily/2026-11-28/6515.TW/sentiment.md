# Sentiment — 6515.TW (穎崴) as of 2026-11-28

> 資料可用性說明: Reddit (r/wallstreetbets, r/stocks) 與 StockTwits 均無法存取 (Reddit 回傳 fetch 失敗, StockTwits 因網域無法解析而失敗), 散戶社群面全部 DATA_UNAVAILABLE。Yahoo 直連 (fc.yahoo.com) 亦失敗, 本次分析師與內部人資料來自 `pipeline/tools/yf` 的回傳值, 其中評等快照未附明確擷取日期。環境日期為 2026-11-27, 早於指定的 DATE 2026-11-28, 本報告未採用任何晚於 2026-11-28 的資料。

## Analyst consensus
12 位分析師: 4 strong buy / 8 buy / 0 hold / 0 sell (rec_summary 當期快照, 與近 3 個月期間完全相同)。

近 4 期 (0m 至 -3m) 評等分布:

| 期間 | strongBuy | buy | hold | sell | strongSell |
|---|---|---|---|---|---|
| 0m (當期) | 4 | 8 | 0 | 0 | 0 |
| -1m | 4 | 8 | 0 | 0 | 0 |
| -2m | 4 | 7 | 0 | 0 | 0 |
| -3m | 4 | 7 | 0 | 0 | 0 |

- 近三個月變動: buy 由 7 增至 8 (-2m 至 0m 之間有 1 家由未知評等轉為 buy 或新增覆蓋), 無降評紀錄。
- `recommendations` 回傳的是期間彙總, 不含個別分析師升降評的時間點與機構名稱, 因此無法列出具體 upgrade/downgrade 事件 (DATA_UNAVAILABLE)。
- 目標價: 來自 WebSearch 摘要 (Investing.com), 10 位分析師 12 個月平均目標價約 12,112 TWD, 最近一筆目標價紀錄標示為 2026 年 7 月。此數字來源日期不完整, 且分析師家數 (10 vs 12) 與 yf 不一致, 僅供參考, 目標價變動趨勢 DATA_UNAVAILABLE。
- 股價快照混亂: 不同來源 (CMoney、Investing.com) 的股價快照落在 6,250 至 7,620 TWD 區間, 時點各異, 無法確認 2026-11-27 或 11-28 的收盤價, 本報告不以股價計算評等距離。

## Retail social
- Reddit (r/wallstreetbets): DATA_UNAVAILABLE (fetch 失敗, 無法取得貼文樣本、分數與情緒傾向)。
- Reddit (r/stocks): DATA_UNAVAILABLE (同上)。
- StockTwits: DATA_UNAVAILABLE (api.stocktwits.com 未列入本工作階段允許網域, 需使用者於網路設定中開放後才能重試)。
- X / 新聞與論壇 (WebSearch): 搜尋未找到 2026 年 11 月穎崴專屬的散戶發言串。CMoney 股市討論頁顯示的內容以大盤與族群整理為主, 未能辨識出 11 月的個股發言, 因此無法引用代表性原文。
- 營運面脈絡 (非社群, 供判讀): nStock 頁面提到 2026 年 9 月營收約 12.5 億元 (NT$), 月減 26.69%, 年增 87.72%, 並被描述為十年同月新高。此為 9 月數字, 非 11 月, 且來源為第三方頁面, 未經財報核對。
- 聲量: 無法取得提及次數, 與一般水準比較 DATA_UNAVAILABLE。
- 主題: 無法從可取得的資料歸納散戶主題。以營運面資訊判斷, 可能被討論的題材為營收高峰後的月減與年增對比, 但這是推論, 不是觀察到的散戶發言。

## Insider activity
Net 6mo: DATA_UNAVAILABLE。`insider` 工具回傳空陣列, 無法判斷 6 個月內的買入或賣出金額, 也無法確認 CEO/CFO 或其他內部人是否有交易。空陣列也可能代表資料源缺漏, 不應直接解讀為「無內部人交易」。

## Ownership shifts
`major_holders` 單一快照 (無時間序列):
- 內部人持股比例: 29.37%
- 機構持股比例 (占總股本): 27.996%
- 機構持股比例 (占流通股): 39.64%
- 機構家數: 117

無前期數據可比較, 機構集中度趨勢 DATA_UNAVAILABLE。內部人持股比例偏高, 但不等於近期有增減持。

## Net sentiment score
Composite: **偏多 (bullish), 信心低**。

- 分析師面: 偏多, 信心中高。12 位全數買進 (含 4 家強力買進), 無持有或賣出評等, 三個月內無降評紀錄。但評等資料無擷取日期, 目標價來源不完整。
- 散戶面: DATA_UNAVAILABLE, 不計入分數。
- 內部人面: DATA_UNAVAILABLE, 不計入分數。
- 綜合信心低, 原因是唯一可用的來源是分析師評等, 且 Reddit、StockTwits、內部人交易三項全部缺漏。

Divergence flag: **無法判定 (DATA_UNAVAILABLE)**。因散戶傾向缺漏, 無法確認散戶與分析師是否方向相反。

## 限制與待辦
1. 允許 api.stocktwits.com 後重試 StockTwits。
2. Reddit 需另尋可用的擷取路徑, 或改以 WebSearch 搜尋 r/stocks 與 r/wallstreetbets 的 6515 貼文。
3. 內部人交易需確認 yf insider 空陣列是真的無交易, 或是資料源缺漏, 建議以 TWSE 公開資訊觀測站的董監事持股異動申報核對。
4. 分析師家數 (yf 12 位 vs Investing.com 10 位) 與目標價時點需以單一來源確認。

## 指標表 (Metrics)

| 指標 | 數值 | 單位 / 來源 | 備註 |
|---|---|---|---|
| 分析師評等 (當期) | 4 強力買進 / 8 買進 / 0 持有 / 0 賣出 | 家數, yf rec_summary | 擷取日期未知 |
| 分析師評等變化 (近 3 個月) | buy 7 → 8, 無降評 | 家數, yf recommendations | 無個別升降評明細 |
| 12 個月平均目標價 | 約 12,112 | TWD / 股, WebSearch (Investing.com) | 10 位分析師, 最後更新 2026-07, 來源不完整 |
| Reddit r/wallstreetbets 情緒 | DATA_UNAVAILABLE | — | fetch 失敗 |
| Reddit r/stocks 情緒 | DATA_UNAVAILABLE | — | fetch 失敗 |
| StockTwits 情緒 | DATA_UNAVAILABLE | — | 網域未允許 |
| 散戶提及次數 | DATA_UNAVAILABLE | 次/期 | 無資料 |
| 內部人 6 個月淨買賣 | DATA_UNAVAILABLE | 億 TWD | yf insider 為空 |
| 內部人持股比例 | 29.37% | 百分比, yf major_holders | 單一快照 |
| 機構持股比例 (總股本) | 27.996% | 百分比, yf major_holders | 無趨勢 |
| 機構持股比例 (流通股) | 39.64% | 百分比, yf major_holders | 無趨勢 |
| 機構家數 | 117 | 家, yf major_holders | 無趨勢 |
| 2026-09 月營收 (參考) | 約 12.5 億 | NT$ 億元, WebSearch (nStock) | 第三方頁面, 未核對 |
| 綜合情緒 | 偏多, 信心低 | 判讀 | 僅分析師面有效 |
| 背離旗標 | 無法判定 | 判讀 | 散戶資料缺漏 |

SENTIMENT REPORT COMPLETE
