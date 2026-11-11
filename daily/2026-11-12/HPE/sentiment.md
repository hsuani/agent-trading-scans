# Sentiment — HPE as of 2026-11-12

> 資料截止：系統日期為 2026-11-11，本報告以 2026-11-12 為 as-of 日期，但所有資料最晚只到 2026-11-11（yf 內部人交易最新一筆為 2026-10-05）。

## Analyst consensus

24 位分析師：5 strong buy / 10 buy / 9 hold / 0 sell / 0 strong sell。

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 合計 |
|---|---|---|---|---|---|---|
| 0m（現在） | 5 | 10 | 9 | 0 | 0 | 24 |
| -1m | 4 | 10 | 10 | 0 | 0 | 24 |
| -2m | 4 | 10 | 10 | 0 | 0 | 24 |
| -3m | 5 | 10 | 8 | 0 | 0 | 23 |

Recent moves（來自網路搜尋，未能與 yf 歷史評等變動交叉驗證）：
- Daiwa 於 2026-10-02 由 Neutral 升至 Outperform，目標價由 USD 65 升至 USD 75。
- Truist 調升目標價至 USD 75，理由是網路業務綜效與 AI 需求。
- Barchart 統計 21 筆建議，共識 "Moderate Buy"，平均目標價 USD 73.50。
- Wall Street Zen 於 2026-06-02 降評至 Hold（MarketBeat 報導）。
- 有報導標題指 Barclays 在股價大漲約 145% 後發出警示，日期不明。

觀察：評等結構近三個月大致穩定，無任何 sell 評等，hold 由 8 增至 10 再回到 9。買方陣營仍占多數，但 yf 的 rec_summary 與 recommendations 回傳相同的彙總資料，沒有個別升降評事件紀錄，因此歷史評等變動只能依靠網路來源。yf 的 24 位與 Barchart 的 21 位口徑不同，兩者都引用但不互相校正。

## Retail social

- Reddit：WallStreetBets 與 r/stocks 搜尋皆遭代理伺服器以 403 拒絕（WebFetch 與直接 curl 均失敗），無法取得討論串樣本，無法判斷散戶語調。此項為 soft-fail。
- StockTwits：api.stocktwits.com 無法解析（DNS 失敗，疑為會話網路白名單未開放），未取得資料。此項為 soft-fail。
- X / 新聞：僅有網路搜尋結果，多為財經媒體與分析平台（Trefis、Benzinga、MarketBeat、Simply Wall St、Webull）的文章，不屬於散戶貼文。搜尋摘要提及 Trefis 記錄 2026-10-19 前一週股價下跌約 20.6%，2026-11-05 單日下跌約 12%，與 AI 硬體板塊拋售同步。
- 聲量：無法量化，無法與平常基準比較。
- 主題（依新聞與 Simply Wall St 敘事推論，非散戶原文）：
  - AI 網路與伺服器需求成長，網路營收在某季據報大增約 148%。
  - Juniper 併購的綜效與監管風險。
  - 股價大漲後的估值問題。
  - 內部人持續賣股。
- 散戶語調：無法判定（資料缺口），不得以新聞語調代替散戶語調。

## Insider activity

6 個月窗口（2026-05-12 至 2026-11-11）：公開市場賣出 7 筆，合計約 USD 38.4M；公開市場買入 0 筆，買入 USD 0M。

| 日期 | 內部人 | 職稱 | 交易 | 股數 | 金額（USD M） |
|---|---|---|---|---|---|
| 2026-10-05 | Antonio F. Neri | CEO | 賣出 @ 68.31 | 250,000 | 17.08 |
| 2026-09-29 | Rami Rahim | Officer | 賣出 @ 61.42 | 34,456 | 2.12 |
| 2026-09-14 | Gary M. Reiner | Director | 賣出 @ 56.91 | 17,000 | 0.97 |
| 2026-09-11 | Antonio F. Neri | CEO | 賣出 @ 60.44 | 250,000 | 15.11 |
| 2026-07-22 | Kirt P. Karros | Officer and Treasurer | 賣出 @ 47.02 | 23,675 | 1.11 |
| 2026-06-22 | Kirt P. Karros | Officer and Treasurer | 賣出 @ 48.50 | 18,785 | 0.91 |
| 2026-06-03 | Gary M. Reiner | Director | 賣出 @ 54.77 | 20,000 | 1.10 |

- 金額手算驗證：250,000 × 60.44 ≈ USD 15.11M，與表列一致。
- CEO 兩筆合計約 USD 32.2M，占窗口內賣出總額約 84%。
- 窗口外的 CFO Marie Myers 於 2026-05-05 賣出約 USD 2.8M，因早於窗口起點未計入。
- 排除項目：贈與（CEO 2026-05-01 約 168 萬股、Rahim 2026-07-07 約 65.5 萬股等）無金額；衍生性證券行使（Rahim 2026-07-02 約 112 萬股，名目價值約 USD 46.3M；Karros 2026-07-20）不視為賣出；董事 2026-09-30 等例行股票獎勵金額小。
- 資料未標示是否為 10b5-1 計畫，無法判斷賣出是否屬預排計畫。
- 淨額：約 USD -38.4M（淨賣出），高階主管（CEO、CFO 以外的 Officer）與董事皆有賣出，無買入。

## Ownership shifts

- 機構持股約 91.9%（流通股口徑約 92.2%），機構家數約 2,123 家。
- 內部人持股約 0.24%。
- 目前只有單一時點快照，無法判斷機構集中度的趨勢。

## Net sentiment score

- 分析師面：偏多（中等信心）。24 位中 15 位為 buy 或 strong buy，0 位賣出，評等結構近期穩定。
- 內部人面：偏空（中高信心）。6 個月內 7 筆公開市場賣出、0 筆買入，CEO 於 9 月與 10 月兩度大額賣出。
- 散戶面：無法判定（資料缺口，Reddit 與 StockTwits 皆未取得）。
- 價格與新聞面：近期股價在 10 月至 11 月初大幅回檔，媒體語調偏負面。
- 綜合：中性（信心低）。分析師與內部人的訊號方向相反，但散戶面缺失，無法做完整三方交叉。

Divergence flag：是。分析師偏多，與內部人淨賣出及近期價格回檔的偏空方向不一致。散戶語調因資料缺失無法判斷，因此無法確認散戶是否與分析師反向。

## Data quality and gaps

- Reddit（r/wallstreetbets、r/stocks）：403，未取得。
- StockTwits：DNS 無法解析，未取得。需在會話網路設定中開放 api.stocktwits.com 後才能重試。
- yf recommendations 與 rec_summary 回傳相同彙總，無個別評等事件歷史。
- 網路來源日期不一，部分數字（如 Barchart 21 位、目標價 USD 73.50）無法與 yf 的 24 位直接對齊。
- 股價現值未取得，無法確認 2026-11-12 的估值位置。
- 報告 as-of 日期（2026-11-12）晚於系統日期（2026-11-11），資料最新只到 2026-11-11。

SENTIMENT REPORT COMPLETE
