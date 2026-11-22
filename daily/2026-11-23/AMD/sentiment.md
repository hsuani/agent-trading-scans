# Sentiment — AMD as of 2026-11-23

資料時點說明：分析師評級與內部人交易取自 repo 快取 `prices/yf/AMD.json`（快取刷新時間 2026-11-22 14:30 UTC，即時 Yahoo 連線失敗）。Reddit / StockTwits 直接抓取未執行（依指示不使用 WebFetch 存取 reddit / stocktwits），散戶情緒改以 WebSearch 彙整，多為 10 月底至 11 月中的二手報導，日期不一。

## Analyst consensus

目前 54 位分析師：6 Strong Buy / 42 Buy / 6 Hold / 0 Sell / 0 Strong Sell（買進類 48 家，約 89%；無賣出評級）。

| 期間 | Strong Buy | Buy | Hold | Sell | 合計 |
|---|---|---|---|---|---|
| 當月 (0m) | 6 | 42 | 6 | 0 | 54 |
| 上月 (-1m) | 5 | 39 | 11 | 0 | 55 |
| 兩個月前 (-2m) | 5 | 40 | 11 | 0 | 56 |
| 三個月前 (-3m) | 4 | 40 | 11 | 0 | 55 |

近一個月 Hold 由 11 降至 6，Buy 增加 3，屬於評級上調方向。`recommendations` 介面只回傳彙總期間，沒有逐家機構的升降評等紀錄，因此個別事件以 WebSearch 補充（未經逐一原始文件核實）：

- William Blair 升至 Outperform（未附目標價），認為風險報酬比已轉向有利。
- Oppenheimer 升至 Outperform，目標價 600 美元（報導中股價約 487 美元，時間為 11 月 9 日前後）。
- BofA 目標價由 650 上調至 700 美元，維持 Buy。
- UBS 維持 Buy，目標價由 730 下調至 700 美元（11 月 4 日）。
- Mizuho 目標價由 705 下調至 610 美元，維持 Outperform（財報後）。
- JPMorgan 目標價調至 575 美元，維持 Neutral。
- TD Cowen 維持 Buy，目標價 675 美元。

目標價共識報導約 659 美元（來源為 TIKR 摘要，覆蓋 53 家，區間約 525 至 1,250 美元），數字來源之間略有出入，僅供參考。未見 11 月內的正式降評。

## Retail social

- Reddit：本次未取得直接資料（WebFetch 被封鎖）。WebSearch 找到的 r/wallstreetbets 相關內容多為 2026 年 2 月的周報，無法代表當前情緒，標記為「資料不足」。
- StockTwits：二手報導（日期多為 11 月中旬附近）指出散戶情緒維持在 "extremely bullish" 區間，訊息量偏高；另有較晚期的報導提及情緒回落至 "neutral"，但日期未能確認。報導亦指出近 30 天訊息量明顯增加，屬定性描述，無法換算為精確提及次數。
- X / 新聞：WebSearch 找到的文章以 StockTwits 新聞稿為主。散戶在財報後股價回檔時仍維持多頭觀點；另有 Michael Burry 稱 AMD "too expensive as eternal alternative" 的空方聲音，以及散戶 "chip rally starting to look exhausted" 的疲勞論述，兩者日期均不明。
- 整體 buzz：高於一般水準（定性），但缺乏可量化的提及數。

Themes（重複出現的主題）：
1. AI 資料中心與推論（inference）需求，是多頭論述的核心，分析師與散戶用語一致。
2. 與 NVDA 的相對位置：NVDA 面臨審查與領導層議題，被視為 AMD 的機會。
3. 估值疑慮：股價漲幅大（報導稱年初至今超過 100%）、本益比偏高，是最主要的空方論點。
4. 內部人賣股：部分散戶把它當成獲利了結的訊號，但多數報導指出這些交易屬預先排定計畫。

Representative takes（僅引用標題，不逐篇轉載）：
- "AMD Earnings 'Checked Every Box,' But Wall Street Remains Split" （StockTwits 新聞標題）
- "Retail Traders Say Chip Rally Is 'Starting To Look Exhausted'" （StockTwits 新聞標題）

## Insider activity

Net 6mo（2026-05-23 至 2026-11-22）：買進 0 筆，公開市場買進金額 0 M USD；賣出 18 筆，合計約 225.2 M USD（458,581 股）。另有 5 筆贈與（無對價）與 6 筆選擇權行使轉換（conversion），不計入買賣金額。

| 內部人 | 職稱 | 賣出筆數 | 賣出金額 (M USD) | 賣出股數 |
|---|---|---|---|---|
| Lisa Su | CEO | 4 | 148.4 | 305,000 |
| Forrest Norrod | Officer | 4 | 31.0 | 61,784 |
| Mark Papermaster | CTO | 4 | 23.9 | 48,180 |
| Paul Grasby | Officer | 1 | 7.7 | 15,000 |
| Jean Hu | CFO | 1 | 7.1 | 15,000 |
| Nora Denzel | Director | 1 | 5.5 | 10,447 |
| Ava Hahn | General Counsel | 3 | 1.6 | 3,170 |

Notable：
- CEO Lisa Su 於 2026-11-16 賣出 70,000 股（約 35.5 M USD，價格區間 502 至 526 美元）。WebSearch 報導指出該交易依 2026-06-08 訂立的 Rule 10b5-1 計畫執行。
- Forrest Norrod（Officer）於 2026-11-16 賣出 10,000 股（約 5.1 M USD），依 2026-05-20 訂立的計畫執行（報導來源）。
- 6 月至 11 月期間，CEO 與 CTO 各有多次定期賣出，屬固定節奏，與股價高低關係不明顯。

注意：交易表中另有 23 筆無金額紀錄（多為 2026-08-14 等日期的大量股份變動，應為 RSU 歸屬或稅款代扣），未計入金額。淨 6 個月賣出以 225.2 M USD 計，無法排除部分交易與稅務相關，但不影響「無公開市場買進」的結論。

## Ownership shifts

- 機構持股比例約 75.3%，內部人持股約 0.45%，機構數約 5,240 家（2026-09-30 13F 快照）。
- 前十大股東（以 2026-09-30 季報計）：BlackRock 9.3%（約 1.525 億股）、Vanguard Capital 6.5%、State Street 4.6%、Invesco 3.3%、FMR 3.3%、Geode 2.5%、Vanguard Portfolio Mgmt 2.3%、JPMorgan 2.3%、T. Rowe Price 2.2%、Morgan Stanley 1.5%。
- 季度股數變化：多數前十大股東增持 0.3% 至 2.1%；FMR 大幅增持（約 +108%，持股約 5,329 萬股）；JPMorgan 減持約 5.7%，Morgan Stanley 減持約 1.2%。
- 整體趨勢偏向機構淨增持，集中度不高（前十大合計約 35%），無單一股東形成控制性持股。

## Net sentiment score

Composite: **偏多 (bullish)**，信心中等偏低。

- 分析師面：強烈偏多（89% 買進類、無賣出、近月上調）。
- 散戶面：偏多（StockTwits 中期報導），但時點資料不新，且多為二手摘要，信心降低。
- 內部人面：偏空／中性（無公開市場買進，CEO 與高階主管持續賣出；多數為 10b5-1 計畫，訊號權重應降低）。
- 機構面：中性偏多（淨增持）。

信心較低的原因：Reddit 無直接資料；StockTwits 與 X 的情緒報導多為 10 月至 11 月中旬的二手摘要，無法確認 11 月 18 至 22 日的最新散戶情緒；價格資料來源之間有出入，未用於本評分。

Divergence flag: **是（部分）**。分析師與散戶同為偏多，無對立；但內部人賣出與分析師偏多方向相反。內部人賣出多屬預先排定計畫，因此歧異的資訊價值有限，但仍值得在後續討論中留意。

SENTIMENT REPORT COMPLETE
