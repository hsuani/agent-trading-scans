# Sentiment — IRM as of 2026-10-24

## 資料狀態

| 來源 | 狀態 | 說明 |
|---|---|---|
| yf recommendations / rec_summary | 可用 | 回傳當期評等分布與近 3 個月趨勢（Yahoo cookie/crumb 取得失敗，但資料有回傳） |
| yf insider | 可用 | 最新交易日 2026-10-01，之後的 Form 4 未納入 |
| yf major_holders | 可用 | 僅當期快照，無時間序列 |
| Reddit r/wallstreetbets、r/stocks | DATA_UNAVAILABLE | WebFetch 無法存取 www.reddit.com，已軟失敗 |
| StockTwits | DATA_UNAVAILABLE | api.stocktwits.com DNS 解析失敗（ENOTFOUND），已軟失敗 |
| X / 網路社群貼文 | DATA_UNAVAILABLE | WebSearch 未找到貼文級討論，僅有新聞與分析文 |
| 網路新聞與分析師摘要（WebSearch） | 可用 | 最新資料約至 2026-10-16（Benzinga 快照） |

## Analyst consensus

12 位分析師，當期分布為 4 Strong Buy / 7 Buy / 0 Hold / 1 Sell / 0 Strong Sell（yf rec_summary）。

近 3 個月趨勢（yf recommendations）：-3m 為 4 / 6 / 0 / 1 / 0（11 家）。當期 Buy 類多 1 家，Sell 維持 1 家，無 Hold。

近期評等變動（WebSearch 摘要，來源見文末）：
- 2026-09-08：Barclays 維持 Overweight，目標價由 USD 143 調至 USD 144。
- 2026-09-21：Rothschild & Co 首次覆蓋，給予 Buy，目標價 USD 132。
- 平均目標價：Benzinga（2026-10-16 快照，股價 USD 112.51）為 USD 126，約上行 12%。Barchart 較早的快照（約 8 月）為 USD 134。
- 來源之間的評等分布不一致：Barchart 的 8 月快照為 9 Strong Buy / 1 Moderate Buy / 1 Hold / 1 Strong Sell，與 yf 當期分布不同。本報告以 yf 為準。

## Retail social

- Reddit：DATA_UNAVAILABLE。抓取遭拒，WebSearch 也未找到 r/wallstreetbets 或 r/stocks 的 IRM 討論串，無法判斷討論量與傾向。
- StockTwits：DATA_UNAVAILABLE。DNS 失敗，無多空標籤可計數。
- X：DATA_UNAVAILABLE。未找到貼文級資料。
- 聲量：無法量化（DATA_UNAVAILABLE），不推估「高於或低於平常」。
- 散戶傾向：DATA_UNAVAILABLE。

替代參考（媒體與獨立分析，不代表散戶意見）：
- Seeking Alpha 獨立分析，標題為「Iron Mountain: Deserves A Downgrade, Overly Expensive Here」，主張估值偏高（偏空）。
- Gotham City Research 於 2025 年 11 月發布做空報告，估算公允價 USD 22–40，質疑槓桿與現金流品質。報告當日股價跌 2.9%，次一交易日再跌 4.3%。這是歷史偏空敘事。
- 正面基本面：Q2 2026 營收年增 18.5% 至約 USD 2B，優於市場預期（WebSearch 摘要）。

主要主題（來自媒體與分析文，非散戶貼文）：
1. 成長動能：營收加速，Q2 優於預期。
2. 估值與槓桿爭議：做空報告與獨立分析持續質疑估值。
3. 內部人持續賣出：與公開交易紀錄一致（見下節）。

## Insider activity

窗口：2026-04-24 至 2026-10-23（6 個月）。金額單位 USD M。Option exercise（行權）與 Stock Award（股票授予）不計入買賣淨額。

| 內部人 | 職稱 | 買進 (USD M) | 賣出 (USD M) | 賣出筆數 | 備註 |
|---|---|---|---|---|---|
| William L. Meaney | CEO | 0 | 27.9 | 6 | 每月約 38,474 股，多數於同月行權（USD 37.00）後賣出；最近一筆 2026-10-01 約 USD 110 |
| Mark Kidd | Officer | 0 | 3.7 | 5 | 每月約 6,000 股 |
| Greg W. McIntosh | Officer | 0 | 2.6 | 3 | 最近一筆 2026-10-01，約 USD 110.72 |
| Daniel Borges | Officer | 0 | 0.9 | 1 | 2026-05-21 |
| Pamela M. Arway | Director | 0 | 0.2 | 1 | 2026-05-12 |
| Walter C. Rakowich | Director | 0 | 0.1 | 1 | 2026-05-20 |
| **合計** | | **0** | **35.5** | **17** | 扣除 CEO 後為 USD 7.6M |

重點觀察：
- 6 個月內沒有任何公開市場買進。
- CEO 賣出金額佔合計約 79%。其交易呈每月固定節奏，且伴隨同量選擇權行權，可能是預先安排的交易計畫。此點為推測，資料無法確認是否為 Rule 10b5-1 計畫。
- 2026-05-07 董事獲得股票授予（每人約 1,892 股，無現金流），屬薪酬性質，不計為買進。
- 窗口外的背景：2026 年 3 月 CEO 曾有單筆約 USD 21.1M 的賣出（197,318 股，約 USD 107）。

內部人持股比例：0.88%（yf major_holders）。

## Ownership shifts

- 機構持股：87.86%，流通股口徑 88.64%，機構數 1,580（yf major_holders，當期快照）。
- 機構持股趨勢：DATA_UNAVAILABLE。工具只提供當期快照，無季度變化序列，無法判斷是增持還是減持。
- 空單比例：3.2%，且據報導為下降（WebSearch 摘要，Benzinga，2026-10-16）。
- Put/call 比率：0.55，偏向 call（同上來源）。

## 股價脈絡（由內部人交易價格推算）

股價自 2026 年 5 月約 USD 128–129 的高點回落。6 月約 USD 126、7 月約 USD 122–125、8 月約 USD 121–127、9 月約 USD 113–116、10 月初約 USD 110。Benzinga 10/16 快照為 USD 112.51。自高點回落約 13%。

## Sources

- [Benzinga IRM 情緒頁](https://www.benzinga.com/quote/IRM/sentiment)（10/16 快照，評等、目標價、空單比例、put/call）
- [Barchart：Is Wall Street bullish or bearish on Iron Mountain stock](https://www.barchart.com/story/news/34146074/is-wall-street-bullish-or-bearish-on-iron-mountain-stock)（8 月左右，評等分布與目標價）
- [Barchart：Iron Mountain stock analyst estimates ratings](https://www.barchart.com/story/news/3823318/iron-mountain-stock-analyst-estimates-ratings)
- [Barchart：Iron Mountain S Q2 2026 earnings what to expect](https://www.barchart.com/story/news/3331170/iron-mountain-s-q2-2026-earnings-what-to-expect)（Q2 營收數據）
- [Seeking Alpha：Iron Mountain: Deserves A Downgrade, Overly Expensive Here](https://seekingalpha.com/article/4722269-iron-mountain-deserves-a-downgrade-overly-expensive-irm-stock)

注意：WebSearch 摘要中的 Gotham 做空報告與 Q2 營收數字，我無法逐一回溯至原始頁面，應視為摘要資訊。

## Net sentiment score

Composite：**neutral**（信心：低）。分析師面偏多，內部人面偏空，散戶面無資料。

| 面向 | 傾向 | 強度 | 信心 |
|---|---|---|---|
| 分析師（評等與目標價） | 偏多 | 強 | 中（樣本 12 家，來源分布有差異） |
| 內部人（6 個月交易） | 偏空 | 中 | 中（多為行權後賣出，訊號權重可降低） |
| 散戶（Reddit / StockTwits / X） | DATA_UNAVAILABLE | — | — |
| 媒體與做空敘事 | 偏空（歷史）、估值爭議 | 中 | 低 |

Divergence flag：**是**（內部人與分析師方向相反：分析師 91.7% 買進，內部人 6 個月 USD 35.5M 賣出、0 筆買進）。散戶與分析師之間的背離無法判定（散戶資料缺失）。

## 指標摘要

| 指標 | 數值 | 單位 / 說明 |
|---|---|---|
| 整體情緒傾向 | neutral（低信心） | 分析師偏多、內部人偏空、散戶無資料 |
| 分析師買進比例 | 91.7%（11 / 12） | Strong Buy + Buy，當期（yf） |
| 分析師持有比例 | 0.0%（0 / 12） | 當期（yf） |
| 分析師賣出比例 | 8.3%（1 / 12） | 當期（yf） |
| 共識分數 | 4.17 / 5 | (4×5 + 7×4 + 0×3 + 1×2 + 0×1) / 12，5 = Strong Buy，1 = Strong Sell |
| 平均目標價 | USD 126 | Benzinga 10/16，約上行 12%（相對 USD 112.51） |
| 內部人 6 個月買進 | USD 0 M | 0 筆 |
| 內部人 6 個月賣出 | USD 35.5 M | 17 筆，其中 CEO USD 27.9 M |
| 機構持股比例 | 87.86% | 當期快照（yf） |
| 空單比例 | 3.2% | Benzinga 摘要，據報導下降 |
| 散戶聲量 | DATA_UNAVAILABLE | Reddit / StockTwits / X 皆無資料 |
| 散戶傾向 | DATA_UNAVAILABLE | 同上 |

SENTIMENT REPORT COMPLETE
