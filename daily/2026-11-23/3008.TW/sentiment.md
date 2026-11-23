# Sentiment — 3008.TW (大立光 Largan Precision) as of 2026-11-23

## Analyst consensus
20 家券商（yf rec_summary，當期快照）：**15 buy**（strongBuy 6 + buy 9）/ **3 hold** / **2 sell**（strongSell 0）。買進占比約 75%。

近四個月趨勢（yf recommendations，依期間由近至遠）：

| 期間 | strongBuy | buy | hold | sell | strongSell | 合計 |
|------|-----------|-----|------|------|------------|------|
| 0m（本期）| 6 | 9 | 3 | 2 | 0 | 20 |
| -1m | 6 | 9 | 2 | 3 | 0 | 20 |
| -2m | 4 | 9 | 4 | 2 | 1 | 20 |
| -3m | 5 | 9 | 3 | 1 | 1 | 19 |

Recent moves: 本期 buy 數與上月持平，hold 增 1、sell 減 1，評等整體沒有明顯轉向。yf 工具只給彙總計數，沒有逐家的升降評紀錄，所以無法列出具名的 upgrade / downgrade。

目標價（新聞與聚合頁，日期不一，僅供參考，需以原報告為準）：
- 高盛（Goldman Sachs）：Buy，目標價由 6,263 元上調至 11,000 元（中文報導，確切日期不明）。Investing.com 另列 2026-07-01 的 Buy、目標價 6,231 元，兩者不一致，無法確認哪個是最新值。高盛看好 FAU 營收占比，預估 2027 年 3%、2030 年超過 50%，同時下調今年獲利預估，理由包括智慧型手機需求低迷與記憶體成本偏高。
- 伯恩斯坦（Bernstein）：Outperform，目標價 5,150 元（2026 年 7 月報告，已逾期）。
- Investing.com 聚合頁：JPMorgan 2026-07-10 升至 Buy（目標 5,000 元）；Nomura/Instinet Buy（目標 6,000 元）；Macquarie Sell（目標 2,250 元，2026-07-13）；CLSA Buy（2026-07-13）。Citi 2025-12-10 降至 Hold。平均目標價約 4,700–4,900 元（聚合頁數字不一，且多數為 2026 年 7 月以前資料）。
- 2026 年 11 月之後的評等變動，本次搜尋沒有找到。

## Retail social
- **Reddit（r/wallstreetbets、r/stocks）**：無資料。WebFetch 回應無法連上 www.reddit.com，兩個子版都沒有取得內容。
- **StockTwits**：無資料。api.stocktwits.com 無法解析（DNS 失敗，目前 session 網路未允許此網域），需於 session 網路設定中加入允許清單後才能重試。
- **X / 新聞與論壇**：WebSearch 只找到新聞與營收報導，沒有 PTT、Dcard 或 X 上的股東討論。主要資訊來源是 TechNews（2026-11-05）報導的 10 月營收，以及高盛、FAU 相關報導，屬於媒體與法人觀點，不是散戶情緒。
- **Retail tilt**：無法判定。現有資料只能看出媒體與法人語氣偏正面，無法區分散戶的看法。
- **Buzz 量（相對平常）**：無法量化。
- **Themes（來自新聞，非散戶原始貼文）**：
  - FAU（光纖陣列單元）與 CPO 光通訊業務，是最主要的正面題材。客戶希望直接採購完整光纖模組，公司規劃 2027 年中完成 FAU 產線建置。
  - 手機本業承壓：今年前 10 月營收 507.05 億元（年增 1.0%），10 月 58.46 億元（年減 7.1%，月增 1.1%）。
  - 公司對 11 月出貨展望保守，預期出貨動能較 10 月下滑（較早期報導，日期需確認）。
  - 高盛列出的風險：智慧機成長不如預期、鏡頭競爭加劇、FAU 擴產速度與競爭。

## Insider activity
yf insider 回傳空陣列（[]）。這可能是真的沒有交易紀錄，也可能是 Yahoo cookie/crumb 取得失敗造成的漏抓（工具執行時出現 cookie fetch 失敗訊息）。**目前無法確認 6 個月淨買賣金額，不能視為 0。**
Net 6mo: 無資料（不能判定買超或賣超）。Notable: 無。

Ownership（yf major_holders）：
- 內部人持股約 28.97%
- 機構持股約 27.26%（占流通股約 38.37%）
- 機構家數 234 家

機構持股的時間序列（前後期比較）本次沒有取得，所以無法判斷集中度是增加或減少。

## Net sentiment score
Composite: **偏多（bullish-leaning）**，信心：**低**。

依據：
- 分析師面：偏多。15/20 家買進，評等在四個月內穩定，沒有明顯下修跡象。權重最高。
- 媒體與法人敘事：偏多，集中在 FAU/CPO 題材。但手機本業營收動能偏弱，高盛也下修今年獲利，正反面並存。
- 散戶面：無資料，無法納入評分。
- 內部人面：無資料（工具可能漏抓）。

信心低的原因：Reddit、StockTwits、PTT/Dcard 都無法取得；內部人交易資料可能不完整；目標價多數來自 2026 年 7 月以前，沒有 11 月的最新券商報告。

Divergence flag: **無法判定**。散戶沒有可靠的資料，無法判斷散戶與分析師的傾向是否相反。若之後取得散戶資料，需要重新檢查這一項。

## 資料缺口與來源狀態
- Reddit：無法連線（WebFetch 錯誤）。
- StockTwits：DNS 解析失敗，需於 session 網路設定允許 api.stocktwits.com。
- yfinance：cookie/crumb 取得失敗，insider 結果可能不完整；rec_summary 與 recommendations 數值一致。
- 新聞來源日期混雜，部分為 2025 年或 2026 年 7 月的資料，已在內文標註。
- 金額單位：營收以億元（TWD）表示，未混用 B。各期營收 507.05 億元（前 10 月）與 2025 年前 11 月 555.10 億元推算的前 10 月約 502 億元相比，年增約 1%，與報導一致。

SENTIMENT REPORT COMPLETE
