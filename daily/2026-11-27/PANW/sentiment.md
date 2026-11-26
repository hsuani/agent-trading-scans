# Sentiment — PANW as of 2026-11-27

資料說明：分析師評等與內部人交易來自 `pipeline/tools/yf.py`（Yahoo 的 cookie/crumb 取得失敗，資料由快取回傳，屬正常現象）。Reddit 與 StockTwits 直連主機在此沙箱中被封鎖，散戶情緒改以 WebSearch 摘要取得，多數為二手來源，未能逐篇驗證。

## Analyst consensus

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 合計 | 買進比例 |
|---|---|---|---|---|---|---|---|
| 本月（0m） | 10 | 33 | 10 | 1 | 0 | 54 | 約 80% |
| -1m | 10 | 32 | 12 | 1 | 0 | 55 | 約 76% |
| -2m | 10 | 32 | 11 | 1 | 1 | 55 | 約 76% |
| -3m | 11 | 33 | 9 | 1 | 1 | 55 | 約 80% |

目前分布為 43 buy（含 strong buy）/ 10 hold / 1 sell，屬明確偏多。與三個月前相比，評等結構基本持平，賣方評等僅 1 家，無明顯降評趨勢。

近期動作（WebSearch 摘要，未逐一核對原始報告）：
- 2026-11-13：KeyBanc 由 Sector Weight 升至 Overweight，目標價 380 美元。
- 2026-11-18 財報後：多家上調目標價，摘要提及 Goldman Sachs 390 → 440、JPMorgan 384 → 415、Bank of America 420 → 430 美元。
- 共識目標價約 408 美元（摘要稱 55 位分析師）。Morgan Stanley 維持 Overweight，但提醒估值偏高。
- 未找到 2026 年 11 月的降評紀錄。

注意：不同來源的分析師家數與目標價略有出入（54 vs. 55 家），以 yf 數字為準。

## Retail social

- Reddit：DATA_UNAVAILABLE（沙箱封鎖直連，搜尋結果未涵蓋 2026 年 11 月）。
  - 僅有的較近期資料為 AltIndex（2026-08-09）：投資類 subreddit 約 20 次/日提及，Reddit 情緒分數 65/100（中性偏多）。
  - 歷史樣本：r/wallstreetbets 一則質疑「為何 PANW 約 299 倍本益比」的貼文，約 415 upvotes（發文日期不明）。
  - 以上皆為舊資料，不可視為當前讀數。
- StockTwits：二手摘要表示，財報前後散戶情緒被標為 "extremely bullish"，訊息量明顯飆升；財報當日 billings 年減約 14% 的細節也被提及，但散戶多數選擇逢低買進。另有 Earnings Whispers 描述財報前情緒轉為輕度偏空，日期不明。兩者方向不一致，需保留不確定性。無法取得 StockTwits 原始情緒分數，StockTwits 直接數據 DATA_UNAVAILABLE。
- X：未取得可靠的 2026 年 11 月貼文樣本，X 數據 DATA_UNAVAILABLE。
- 聲量相對基準：無歷史聲量基準可比，以定性判斷，財報週前後聲量明顯高於平日。

主要主題（依 WebSearch 摘要歸納）：
1. AI 安全與平台整合（platformization）敘事，多數散戶與分析師都正面引用。
2. 估值偏高：歷史本益比被拿來與 5 年均值對比，是主要的看空論點。
3. 併購驅動成長的質疑：Seeking Alpha 留言中，「靠併購成長」被視為風險，屬於較舊的看空論點。
4. 財報後逢低買進的心態。

代表性散戶看法（≤15 字引述，以下為摘要引語，未核對原文）：
- 「會在財報後的回檔加碼」（StockTwits 財報前貼文摘要）。

## Insider activity

近 6 個月（2026-05-27 至 2026-11-27，依 yf 交易表加總，單位 USD M）：

| 項目 | 筆數 | 金額（USD M） |
|---|---|---|
| 公開市場買進（Purchase） | 0 | 0 |
| 公開市場賣出（Sale） | 20 | 51.8 |
| 淨額 | — | -51.8 |

不含股票授予（Stock Award）與股權轉換（Conversion）。

主要賣方（USD M）：
- William D. Jenkins Jr.（President）：19.9，含 2026-11-02 約 6.5、2026-11-04 約 13.4
- James J. Goetz（Director）：13.1
- Dipak Golechha（CFO）：12.2，含 2026-09-24 約 10.8
- John P. Key（Director）：3.0
- Joshua D. Paul（Officer）：1.8（多為小額定期賣出）
- Aparna Bawa（Director）：1.5
- Helle Thorning-Schmidt（Director）：0.2

備註：
- 2026-03-27 CEO Nikesh Arora 曾以約 10.0 百萬美元公開買進（約 146.9 美元/股），但已超出 6 個月窗口，屬於較早的內部人看多訊號。
- 2026-11-20 Joshua Paul 小額賣出約 0.39 百萬美元，價格約 358.67 美元。
- 2026 年 11 月內部人賣出金額集中（Jenkins 合計約 20 百萬美元），與股價接近 340–367 美元的區間相符。
- 賣出多數可能屬於例行或計畫性交易，但本報告無法從資料中確認交易計畫（10b5-1）是否存在，標示為 DATA_UNAVAILABLE。

## Ownership shifts

- 機構持股比例：84.2%（流通股 84.8%），機構家數 4,083。
- 內部人持股比例：0.66%。
- 歷史季度變化：DATA_UNAVAILABLE（工具僅提供單一時點快照，無法判斷趨勢）。

## Net sentiment score

Composite：**偏多（bullish），信心中等**

分項評估：
- 分析師：強偏多（約 80% 買進，近三個月穩定，目標價陸續上調）。
- 散戶：偏多（StockTwits 二手摘要為 "extremely bullish"），但 Reddit 當前數據缺失，且 StockTwits 與 Earnings Whispers 的描述方向不一致，信心下修。
- 內部人：偏空（6 個月 USD 51.8 M 賣出、0 筆公開買進），但多數屬於高層持股多元化或授予後的例行賣出，權重應低於分析師面向。
- 扣分因素：估值（歷史本益比高於 5 年均值）與財報後 billings 年減的細節。

Divergence flag：**否**。散戶與分析師方向一致（皆偏多）。需注意的是「內部人賣出 vs. 分析師買進」存在方向差異，這是本報告最值得追蹤的訊號，但並非散戶與分析師的背離。

資料缺口摘要：Reddit 當前數據、X 數據、內部人交易計畫、機構持股歷史趨勢均為 DATA_UNAVAILABLE。

SENTIMENT REPORT COMPLETE
