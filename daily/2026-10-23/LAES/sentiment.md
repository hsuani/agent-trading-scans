# Sentiment — LAES (SEALSQ) as of 2026-10-23

## Analyst consensus
2 buy / 0 hold / 0 sell（yf `rec_summary`：strongBuy 1 + buy 1）。覆蓋樣本僅 2 位，結論強度有限。

| 期間 | strongBuy | buy | hold | sell | strongSell |
|---|---|---|---|---|---|
| 0m（現在） | 1 | 1 | 0 | 0 | 0 |
| -1m | 1 | 1 | 0 | 0 | 0 |
| -2m | 1 | 1 | 0 | 0 | 0 |

- 近三個月評級分布完全未變，`recommendations` 歷史無升評或降評紀錄。
- 目標價（target price）與目標價變動：DATA_UNAVAILABLE（yf 工具本次未回傳）。
- 交叉核對：WebSearch 抓到的聚合頁（MarketBeat 類，快照日期不明，多為 2025 年資料）顯示 1 buy / 0 hold / 0 sell，且近 90 天無新覆蓋。與 yf 的 2 buy 不一致，以 yf 為準，但兩者都顯示覆蓋極薄。

## Retail social
- Reddit：依任務指示僅以 WebSearch 查詢，未以 WebFetch 直接抓取 r/wallstreetbets 或 r/stocks 的 search.json。WebSearch 未找到 LAES 相關討論串。第三方聚合頁顯示 Reddit mentions 2、subscribers 3,860，來源為 AI 生成分析頁，可信度低。結論：Reddit 討論量極低，tilt 無法判定。
- StockTwits：DATA_UNAVAILABLE（本次未抓取）。
- X：無可用的 X 直接資料，僅有零散第三方文章。
- Investing.com 多空投票（"Will LAES shares go up or down in price?"，時間點約 2026-08）存在，但投票結果未能取得，DATA_UNAVAILABLE。
- Investing.com 法文論壇頁面的摘要顯示，散戶在討論股價下跌與量子安全（quantum-security）題材。這只是頁面摘要，無法量化多空比例。
- Buzz 量：低（定性判斷）。以搜尋可見的第三方內容數量推估，未見明顯聲量高峰。
- 原文引述：DATA_UNAVAILABLE。搜尋只回傳頁面標題與摘要，沒有取得可引用的原文貼文，因此不引用、不捏造。
- 價格脈絡（推估，非即時報價）：由內部人成交價推估，2026-06 約 $3.5、2026-07 約 $2.8、2026-08 至 10 月約 $2.4 至 $2.5。第三方頁面的價格數字互相矛盾，未採用。

### 主要主題（Themes）
1. 量子安全（quantum-security）題材：散戶對此敘事有興趣，但頁面摘要未提供多空細節。
2. 股價自 6 月高點回落後的疑慮：從成交價走勢推論，散戶在討論下跌原因。

### Retail tilt
無法判定（資料極少，信心低）。

## Insider activity
Net 6mo（2026-04-23 至 2026-10-23）：**$0.00M 買入 / $0.65M 賣出（公開市場 sale）**，淨額 約 -$0.65M。

| 內部人 | 職稱 | 公開市場賣出（USD M） | 賣出股數 | 公開市場買入（USD M） |
|---|---|---|---|---|
| Jean-Pierre Enguent | Officer | 0.30 | 110,000 | 0 |
| John Charles O'Hara | CFO | 0.18 | 55,664 | 0 |
| Carlos Creus Moreira | CEO | 0.11 | 31,444 | 0 |
| Franck Jean Buonanno | Officer | 0.06 | 20,000 | 0 |
| 合計 | | **0.65** | **217,108** | **0** |

- 重點：CEO 與 CFO 在窗口期內皆有賣出，且全數為公開市場 sale，沒有任何公開市場買入。
- 規律性：Enguent 在 5 月至 10 月每月前後先以 $0.01 行權（conversion）取得約 15,000 股，隨即賣出，共 6 筆賣出，形態一致。資料未揭露是否為 10b5-1 預定交易計畫，此點 DATA_UNAVAILABLE。
- 期權行權（以 $0.01 行權價取得股份，非公開市場買入）：窗口期內另有 Director Peter Ward 於 2026-06-16 行權 366,746 股，行權現金成本約 $3,667，屬於非現金型行權，不計為買入。
- 持股比例：insidersPercentHeld 3.19%。

## Ownership shifts
- institutionsPercentHeld 6.64%，機構持有者 127 家（institutionsCount），institutionsFloatPercentHeld 6.86%。
- 機構持股變動趨勢：DATA_UNAVAILABLE（僅有單一時點快照）。
- 6.6% 的機構持股比例偏低，需確認是否為實際結構或資料來源覆蓋不全。

## Net sentiment score
**Composite：中性偏空（neutral-to-bearish），信心：低。**

理由：
- 內部人：窗口期 $0.65M 純賣出、零買入，且涵蓋 CEO、CFO 與多名 Officer，是本報告最明確的訊號。
- 分析師：2 buy、0 sell，近期無評級變動，但樣本只有 2 位，且無目標價資料。
- 散戶：Reddit 幾乎無聲量，StockTwits 與 X 無可用資料，無法判定 tilt。

**Divergence flag：是**（分析師偏多 vs 內部人偏空）。散戶端無資料，無法確認散戶是否與分析師或內部人同向。

### 資料缺口（DATA_UNAVAILABLE 彙整）
- 分析師目標價與目標價變動
- StockTwits 貼文與情緒
- X 直接貼文與情緒
- Investing.com 多空投票結果
- Reddit 原文討論串（僅有 WebSearch 摘要層級資訊）
- 可引用的散戶原文
- 機構持股變動趨勢
- 即時報價與市值（本報告未取得，價格區間僅由內部人成交價推估）

Sources:
- [MarketBeat LAES 內部人交易頁](https://www.marketbeat.com/stocks/NASDAQ/LAES/insider-trades/news/chart/chart)
- [Investing.com LAES 評論頁（法文）](https://fr.investing.com/equities/sealsq-commentary)
- [Investing.com LAES scoreboard](https://uk.investing.com/equities/sealsq-scoreboard)
- [AltIndex LAES 頁面](https://altindex.com/ticker/laes)
- [Seeking Alpha LAES sell-side ratings](https://seekingalpha.com/symbol/LAES/ratings/sell-side-ratings)

SENTIMENT REPORT COMPLETE
