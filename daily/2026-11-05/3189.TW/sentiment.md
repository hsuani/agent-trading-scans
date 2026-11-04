# Sentiment — 3189.TW (景碩) as of 2026-11-05

**資料完整度警示**：本次為部分資料。Reddit 與 StockTwits 無法取得，內部券商評等無歷史變動紀錄，且目前沒有 2026-11 的報價或新聞。下列結論信心偏低。另外，系統日期為 2026-11-04，分析基準日 2026-11-05 尚未到達，本報告無法包含基準日當天資料。

## Analyst consensus
目前 13 位分析師：2 strongBuy / 11 buy / 0 hold / 0 sell / 0 strongSell（yf rec_summary，0m 期）。
- 近 4 個月（0m 到 -3m）的分布完全相同，沒有任何評等上修或下調。這種不變很可能是資料快取或來源沒有更新，不是真正的無變動，需要人工確認。
- `recommendations` 工具回傳的內容與 rec_summary 相同，並非逐筆評等異動紀錄，因此無法列出具體的升評或降評事件。
- 目標價：Investing.com 顯示 12 位分析師的 12 個月平均目標價約 891.75 TWD，但頁面未標示日期，且與當時的股價時點不明確。
- 獲利預估：鉅亨網引用 FactSet，2026 EPS 中位數由 8.99 上修至 9.15 TWD（最高 13.6、最低 7.71），預估目標價 588 TWD。該篇文章日期也不明，且目標價低於 891.75 的平均值，兩者方向不一致。

## Retail social
- Reddit（r/wallstreetbets、r/stocks）：抓取被封鎖（WebFetch 無法連線 www.reddit.com），無樣本可引用。
- StockTwits：api.stocktwits.com DNS 解析失敗，需在 session 網路設定中允許此網域後才能重試。
- X / 新聞搜尋：以下為零星資料，且最新的內容停在 2026-08 前後，沒有 11 月的討論。
  - 微風智慧科技（Zephyrtech）的 2026-03 文章給予「持有」，認為當時 380 元股價已明顯高估，主張等待回檔（[連結](https://zephyrtech.substack.com/p/zephyrtech-9523189ai-380)）。這篇文章的股價基準已過時，且屬於 AI 產出的分析，不能代表目前的散戶情緒。
  - 2026-08-03 股價報 698 TWD，單日上漲 9.92%；2026-07-22 報 785 TWD（[MONEY LINK](https://ww2.money-link.com.tw/TWStock/StockChart.aspx?symid=3189)）。
  - 籌碼與主力進出資料可參考 [histock](https://histock.tw/stock/main.aspx?no=3189)。
- 聲量：無法量化與平常基準比較。
- 情緒傾向：無法判定可靠的散戶傾向。
- 主要議題（從搜尋結果歸納，非直接來自社群）：AI 伺服器題材、估值偏高（Investing.com 比較頁顯示 trailing P/E 約 224 倍、P/B 約 9.7 倍，明顯高於同業中位數）、股價波動劇烈。

## Insider activity
yf insider 回傳空陣列，6 個月內無可得的內部人交易資料。這可能代表來源不支援台股內部人申報資料，不代表沒有交易。淨買賣金額無法計算，CEO/CFO 動向也無法判斷。

## Ownership shifts
- 內部人持股約 39.6%，機構持股約 19.7%（占流通股約 32.7%），機構家數 109 家（yf major_holders，單一快照）。
- 缺乏時間序列，無法判定機構集中度是增加或減少。
- 高內部人持股（約 40%）代表股權集中度高，流通股相對少，這可能放大股價波動。

## Net sentiment score
**Composite: 偏多（信心：低）**
- 分析師面：偏多，13 家全數買進或強力買進，但評等無變化，且 EPS 上修幅度小（8.99 到 9.15）。
- 散戶面：無可靠資料，無法評估。
- 內部人面：無資料。
- 唯一的負面聲音是 2026-03 的持有評等，且已過時。

**Divergence flag: 無法判定**。散戶傾向資料缺失，無法與分析師傾向比較。若日後取得 Reddit 或 StockTwits 資料，應優先檢查是否出現「分析師全買、散戶偏空」的背離。

## 估值參考（非情緒指標，僅供上下文）
- 以 2026 EPS 中位數 9.15 TWD 與 698 TWD（2026-08 股價）估算，約為 76 倍預估本益比。此股價已非現值，僅作為量級參考。
- 目前股價與 11 月的實際價位均未取得，無法更新估值。

## 限制與待辦
1. rec_summary 的 4 期完全相同，需確認是否為快取問題。
2. 需要 StockTwits 網域授權後重試。
3. 需要 2026-11 的報價與近期新聞，才能判斷情緒是否已有變化。

## 參考來源
- [MONEY LINK 3189 股價](https://ww2.money-link.com.tw/TWStock/StockChart.aspx?symid=3189)
- [Investing.com 3189 (kinsus)](https://hk.investing.com/equities/kinsus)
- [微風智慧科技 2026-03 分析](https://zephyrtech.substack.com/p/zephyrtech-9523189ai-380)
- [histock 籌碼分析](https://histock.tw/stock/main.aspx?no=3189)

SENTIMENT REPORT COMPLETE
