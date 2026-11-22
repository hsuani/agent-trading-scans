# Sentiment — ARM as of 2026-11-23

資料來源註記：yfinance 即時呼叫失敗（Yahoo 無法連線），以下 yf 數據皆取自 repo 快取 `prices/yf/ARM.json`（快取時間 2026-11-22 14:30 UTC）。Reddit 被擋（WebFetch 無法連線 reddit.com），StockTwits DNS 解析失敗（需於 session 網路設定允許 api.stocktwits.com）。散戶面以 WebSearch 替代，缺乏 2026 年 11 月的直接社群資料。

## Analyst consensus

快取 rec_summary（當期）：8 Strong Buy + 20 Buy = 28 買進；14 Hold；1 Sell，0 Strong Sell，合計 43 家。買進佔比約 65%，共識仍偏買進。

三個月趨勢（快取 recommendations）：

| 期間 | 買進 (SB+B) | 持有 | 賣出 (S+SS) | 合計 |
|---|---|---|---|---|
| 當期 (0m) | 28 | 14 | 1 | 43 |
| -1m | 28 | 14 | 1 | 43 |
| -2m | 29 | 12 | 2 | 43 |
| -3m | 27 | 13 | 2 | 42 |

評級分布在三個月內變動不大，買進家數由 29 微降至 28，持有略升至 14，屬於「評級沒有明顯轉向、但共識略有降溫」。

近期目標價與評級動作（來自 WebSearch 彙整，屬二手來源，個別數字未逐一核對原始券商報告）：
- Piper Sandler 維持 Overweight，目標價由 320 降至 270 美元。
- Barclays 維持 Overweight，目標價由 360 降至 325 美元。
- TD Cowen 維持 Buy，目標價降至 250 美元。
- Loop Capital 維持 Buy，目標價由 155 升至 180 美元（11 月 12 日）。
- Morgan Stanley 維持 Equal-Weight，目標價 212 美元，11 月 17 日上調盈餘預估（AI 資料中心與 CPU 需求）。
- Raymond James 首次評等 Market Perform（中性），11 月 20 日。
- HSBC 11 月 5 日重申 Hold、目標 215 美元；另有一篇報導稱 HSBC 升至 Buy、目標 205 美元，兩則日期與數字衝突，未能確認，不採信。

注意：WebSearch 彙整的「18 Buy / 7 Hold / 1 Sell」與快取的 43 家分布不一致，原因應為來源計數口徑不同（部分來源只計活躍且有明確評等的分析師）。本報告以快取 43 家為準，並保留此差異。

財報後背景：11 月 5 日財報營收創紀錄 14.4 億美元（年增 27%），調整後 EPS 優於預期，但股價當日下跌約 13%，原因是授權收入大增 50% 而權利金僅增 8%，加上記憶體成本推升智慧型手機出貨壓力。

## Retail social

- Reddit：無法取得（r/wallstreetbets 與 r/stocks 的 search.json 皆被擋）。
- StockTwits / X：StockTwits 無法連線；X 未取得可靠樣本。
- WebSearch 替代來源：可找到的最新 WSB 提及為 2026 年 5 月，主要論點是估值過高、部分散戶對 ARM 熱度感到困惑。2024 年初 ARM 曾是 WSB 提及前三名；StockTwits 新聞文章停留在 2024–2025 年的情緒翻轉紀錄。沒有 2026 年 11 月的散戶情緒直接證據。
- 聲量：無法量化。近期新聞量集中在財報後下跌與分析師調降目標價，但這不等同於散戶社群聲量，不能推論為高檔熱度。
- 散戶傾向：無法可靠判定，標為「資料不足」。

主題（由新聞面整理，非散戶原文）：
- 授權與權利金結構差異（授權 +50% vs 權利金 +8%）。
- 記憶體價格對智慧型手機出貨的衝擊。
- AI 資料中心 CPU 與自研資料中心晶片的成長敘事。
- 估值爭議（分析師目標價區間約 212 至 325 美元，分歧大）。
- 未經證實傳聞：Nvidia 與 CEO Rene Haas 就 Nvidia 自身 CEO 人選有接觸，無正式公告，不列入判斷。

## Insider activity

以 2026-05-23 至 2026-11-23 為 6 個月窗口，公開市場交易（有價格的 Sale）：

| 類別 | 金額 (USD M) | 主要人員 |
|---|---|---|
| 公開市場賣出 | 15.3 | CFO Jason Child（9/21 約 312 萬、8/27 約 266 萬）、Laura Bartels（6/2 約 444 萬）、William Abbey（6/1 約 264 萬、5/28 約 144 萬）、Richard Grisenthwaite（11/17 約 104 萬，成交價 180.40 美元） |
| 公開市場買進 | 0 | 未見 |
| 無價格的 Grant / 贈與 / 其他 | 不計金額 | CEO Rene Haas 8/31 授予 64 股；5/15 大量 Stock Award（無成本價）；8/7 Jeffrey Sine 贈與 |

重點觀察：
- 窗口內沒有任何公開市場買進。
- CEO Rene Haas 在窗口內無賣出（其 3 月、4 月的賣出約 660 萬美元發生在窗口之前）。
- CFO Jason Child 是窗口內賣出最多的人（約 578 萬美元），且於 8/27 與 9/21 各賣一次，均為 10,400 股。
- 11 月 16 日出現一批無價格、無說明的交易（Child、Abbey、Collins、Grisenthwaite、Eaton、Bartels 等，合計約 12.5 萬股）。性質無法從快取資料判定，可能是稅款代扣或歸屬相關交易，未能確認，不計入賣出金額。
- 窗口外另有一波較大的賣出：2026-05-11 至 05-22 約 4,420 萬美元（Collins 約 1,100 萬、Child 與 Abbey 於 5/20 合計約 1,100 萬）。這波與財報後解鎖期吻合，屬於窗口外資料，僅作背景。

## Ownership shifts

- 內部人持股約 0.08%（快取 major_holders）。
- 機構持股約 95.8%，機構家數 1,306。
- 前十大機構（13F 資料日 2026-09-30，約 45 天落後）：
  - 增持：Invesco（+3.0%，約 1,320 萬股，持股 1.24%）、Morgan Stanley（+76%）、Goldman Sachs（+21%）、Capital Research Global（+35%）、Van Eck（+13%）、BlackRock（+9%）。
  - 減持：Dz Bank（-25%）、FMR（-46%）、Arrowstreet（-33%）、Capital International（小幅減）。
- 前十大中增持家數略多於減持，但集中度分散、落後期長，不能視為明確的機構加碼或撤退訊號。

## Net sentiment score

- 分析師面：偏多（Bullish-leaning）。買進佔比約 65%，但近期目標價普遍下修，評等未明顯轉向。信心：中。
- 內部人面：偏空（Bearish-leaning）。6 個月內公開市場賣出約 1,530 萬美元、無買進，CFO 為主要賣方；CEO 窗口內未賣。信心：中。注意窗口外有更大的 5 月賣出潮，但依規格不納入計算。
- 機構面：中性偏多（Neutral-to-bullish），增持與減持家數接近，且資料落後約 45 天。信心：低。
- 零售面：資料不足（Unknown）。Reddit 與 StockTwits 皆無法取得，WebSearch 找不到 2026 年 11 月的直接情緒樣本。

綜合分數：Neutral（中性），信心：低。理由是分析師偏多、內部人偏空，兩者方向不一致，而零售面缺席，無法提供第三方交叉驗證。

Divergence flag: 無法判定（零售資料缺失，無法比較零售與分析師方向）。另外已觀察到「分析師買進偏多 vs 內部人公開市場賣出」的背離，此背離不等於零售背離，但值得後續追蹤。若補齊 Reddit 或 StockTwits 資料（需要 api.stocktwits.com 允許連線，Reddit 需解除封鎖），建議重跑本報告以判定零售與分析師是否反向。

SENTIMENT REPORT COMPLETE
