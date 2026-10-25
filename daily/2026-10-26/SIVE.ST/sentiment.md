# Sentiment — SIVE.ST (Sivers Semiconductors AB, Nasdaq Stockholm) as of 2026-10-26

> 資料時效註記: 本報告以 2026-10-26 為基準日。實際執行日為 2026-10-25, 搜尋來源多數止於 2026-10 中旬 (Fox Business 報價頁更新至 2026-10-16), 2026-10-17 至 10-26 之間的事件與價格未能確認。

## Analyst consensus
- yf `rec_summary` / `recommendations` (三個期間皆相同): **1 buy / 0 hold / 0 sell / 0 strong buy / 0 strong sell**。覆蓋家數極少, 且此為 Yahoo 端資料, 與瑞典本地券商評等可能不一致。
- 歷史評等變動: yf `recommendations` 三期 (0m, -1m, -2m) 內容完全相同, 無法判斷期間內升降評。DATA_UNAVAILABLE (升降評明細)。
- 目標價變動: DATA_UNAVAILABLE (yf 未回傳)。
- 本地媒體訊息 (WebSearch 摘要, 非正式評等):
  - Dagens Industri (DI) 發布 "rekommenderar att sälja" 標題, 認為估值遠高於獲利能力, 引用分析認為獲利要到約 2028 年才會出現, 並提及主要股東出售股份。文章日期未在搜尋結果中顯示, 需回查原文。
  - TradingView 頁面列出分析師目標區間 5.80 至 8.00 SEK, 但頁面未註明日期, 且與 DI 的悲觀看法方向不同, 不確定是否為最新。
  - boerse-express / boerse-global 的 "Analysten sehen 60 Prozent Luft nach unten" 類標題, 似為自動化文章, 未提供明確評等, 不採計為分析師評等。
- 結論: 正式覆蓋過少, 共識 (consensus) 無統計意義; 本地媒體與 DI 偏空, 單一買進評等來源不明。

## Retail social
- **Reddit** (r/wallstreetbets, r/stocks): DATA_UNAVAILABLE。WebFetch 回傳 "unable to fetch from www.reddit.com", 無法取得貼文樣本、提及次數與情緒傾向。
- **StockTwits**: DATA_UNAVAILABLE。api.stocktwits.com 無法解析 (DNS 失敗), 無法取得訊息量或 bullish/bearish 標籤。
- **X**: 未取得直接資料。
- **新聞與論壇 (WebSearch 摘要)**:
  - 一篇德文文章指出近期漲勢部分來自社群推廣, 價格隱含高度成長預期 (日期為 2026 年, 具體日期不明)。
  - 2026 年 6 月 1 日, Ningi Research 發布空方報告, 稱公司為 "retail-driven pump" (散戶推動的炒作)。Ningi 持有空單, 此為利益相關來源。
  - 另一篇文章指出約 17% 的可自由交易股數曾被借券放空 (截至 5 月下旬, 較 3 月初約 1.6% 大增)。
  - 一家美國律師事務所表示正在審查可能的證券違規行為 (未確認細節)。
  - Fox Business 報價頁 (2026-10-16 更新): SIVEF (美國櫃檯代號) 單日下跌約 11%, 一週下跌約 24%, 52 週區間約 0.70 至 11.25 USD。
- **Buzz 量級**: 無法量化 (缺 Reddit/StockTwits 數據)。定性判斷: 2026 年 6 月前後曾有明顯投機性拉升與媒體關注度, 10 月為急跌後的關注期。
- **主要論點 (Themes)**:
  1. 估值 (Valuation): 市值相對營收與獲利明顯偏高, DI 與舊版 Simply Wall St 文章皆提及。
  2. 稀釋風險 (Dilution): 定向增資以 SEK 57/股募集約 SEK 7 億 (原文 "roughly SEK 700m"), 市場擔心再融資。
  3. 獲利時程: Q1 2026 淨銷售額 SEK 6,190 萬 (原文 61.9m), 年減 22%; 管理層稱訂單管線 (pipeline) 達 USD 799M (約 0.8B), 較 2025 年底增 77%, 生產啟動預計 2027 年。
  4. 做空與炒作爭議: Ningi 報告、借券比例上升、律師審查。
  5. 內部人動向: 見下節。

## Insider activity
- yf `insider`: 回傳空陣列 `[]`。**DATA_UNAVAILABLE** (yf 對 Stockholm 上市資料覆蓋不足, 不代表無內部人交易)。
- 根據 WebSearch 摘要 (來源為公司新聞稿 "update on expiry of lock up undertaking and insider transactions", 經二手轉載, 未逐筆核對):
  - 2026-07-16 鎖定期 (lock-up) 屆滿。
  - 7 月初至中旬多位高階人員買進: CEO Vickram Vathulya 買入 70,000 股, 持股約 4,540,076 股; 董事 Todd Thomson, Karin Raj, Helena Svancar 亦有買進 (日期來源不一, 7/9 與 7/13 並存)。
  - 同期賣出: 董事長 Bami Bastani 於 7/16 賣出 275,000 股; 另有一名董事於 7/22 有賣出紀錄。
  - 金額 (SEK / USD): **DATA_UNAVAILABLE** (未取得成交價, 不估算)。
  - 淨買賣: 股數層面無法精確加總 (缺各筆股數與價格); 定性為**買賣互見, 無明確單向訊號**, 買方以執行層為主, 賣方含董事長。
  - 7/28 起進入封閉期, 至 2026-08-27 Q2 報告後解除。Q3 (2026-10 中) 之內部人交易資料未取得。

## Ownership shifts
- yf `major_holders` (2026-10-25 查詢):
  - 內部人持股 (insidersPercentHeld): **21.34%**
  - 機構持股 (institutionsPercentHeld): **17.65%**
  - 機構浮動股持股 (institutionsFloatPercentHeld): **22.44%**
  - 機構家數 (institutionsCount): **56**
- 趨勢 (季度變化): DATA_UNAVAILABLE (yf 僅回傳單一時點)。
- 注意: 內部人持股比例高 (21%+) 但 Q3 內部人交易資料不全, 且 2026 年 6 月定向增資可能改變股權結構, 此數字可能已過時。

## Net sentiment score
- **Composite: bearish (信心度: 低 / low-to-medium)**
  - 分析師面: 正式覆蓋 1 買進, 本地主要媒體 (DI) 偏空 → 偏空至中性, 樣本極小。
  - 散戶面: 無直接量化資料; 間接資訊顯示 6 月後高度投機, 10 月急跌 (2026-10-16 單日 -11%, 一週 -24%), 多數敘事偏負面 (炒作、稀釋、估值)。
  - 內部人面: 7 月買賣互見, 執行層買入為正面但規模與金額不明; 董事長賣出為負面訊號。中性偏弱。
  - 空方面: 借券比例大幅上升 (曾達約 17% 可自由流通股數), 空方報告存在, 空頭情緒強。
- 信心度下調理由: Reddit / StockTwits 缺失、yf insider 空白、分析師覆蓋僅 1 家、資料止於 10 月中旬。

**Divergence flag: 無法判定 (DATA_UNAVAILABLE)**。
- 分析師面 (1 buy, 媒體偏空) 與散戶面 (間接資訊偏投機樂觀, 但近期急跌) 的方向不一致程度無法精確量測。若以 yf 的 1 buy 為準, 與本地偏空敘事相反; 但該 buy 評等來源不明, 不宜過度解讀。
- 此標記不代表無背離, 僅代表資料不足以確認。

## 資料缺口與後續建議
1. Reddit / StockTwits / X 直接資料: DATA_UNAVAILABLE, 需另尋 Flashback、Placera、Avanza 論壇等瑞典來源。
2. 瑞典本地券商評等 (Redeye, Carnegie, ABG, DNB 等) 與目標價: 未取得, 需人工查證。
3. 內部人交易逐筆股數與價格: 建議直接查 Finansinspektionen (FI) 內部人交易登記 (Insynsregistret)。
4. 機構持股季度變化: 建議查 Modular Finance / Euroclear 或 Fi 持股資料。
5. 日期核實: DI 文章與 TradingView 目標價頁面日期未明, 需回查。

來源 (WebSearch / WebFetch 摘要, 非一手資料):
- https://simplywall.st/stocks/se/semiconductors/sto-sive/sivers-semiconductors-shares/news/with-a-26-price-drop-for-sivers-semiconductors-ab-publ-stosi
- https://www.tradingview.com/symbols/SIVE
- https://www.foxbusiness.com/quote?stockTicker=SIVEF
- https://www.itiger.com/hans/news/1134015930
- https://www.finanztrends.de/news/sivers-semiconductors-aktie-mehr-als-70-prozent-wochenplus/
- https://www.boerse-express.com/news/articles/sivers-semiconductors-aktie-1549-prozent-absturz-vor-q1-zahlen-910215
- https://borsvarlden.com/artiklar/di-rekommenderar-att-salja-sivers-semiconductors-efter-kursrusningen
- https://www.boerse-express.com/news/articles/sivers-semiconductors-aktie-insider-kaufen-vor-lock-up-ende-929395
- https://www.boerse-express.com/news/articles/sivers-semiconductors-ceo-kauft-70000-aktien-930666
- https://www.inderes.se/releases/update-on-expiry-of-lock-up-undertaking-and-insider-transactions-in-sivers-semiconductors

SENTIMENT REPORT COMPLETE
