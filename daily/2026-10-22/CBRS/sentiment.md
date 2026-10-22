# Sentiment — CBRS (Cerebras Systems Inc., Nasdaq) as of 2026-10-22

> 標的確認：CBRS 為 Cerebras Systems Inc.（Nasdaq，2026-05-14 IPO），非 Celebrate Brands。repo cache `prices/yf/CBRS.json` 的 CEO / CTO / COO 姓名與公司描述一致。
> 資料來源狀態：yf 即時 feed 連線失敗，全部使用 repo cache（`_refreshed_at` 2026-10-22T11:39 UTC）。Reddit / StockTwits 無 2026-10 的可用內容；WebSearch 只回傳 6 月至 9 月的快照，下方皆標註時間。

## Analyst consensus

目前 rec_summary（0m）：**11 buy（強力買進 3 / 買進 8）/ 0 hold / 0 sell**。
近 4 個月分佈：-1m 為 10 buy + 1 hold；-2m、-3m 同為 10 buy + 1 hold。近一個月有一家由 hold 升為 buy，屬於單一評等變動，未見降評。

Target price（cache info，yf）：mean $282.55 / high $330 / low $175。
WebSearch 快照（約 8 月）：MarketBeat 12 家 mean $300.30（高 $340、低 $273）；Investing.com 11 家 mean 約 $291.64。Citi 初次評等 Buy / $340，Morgan Stanley Overweight / $250，Rosenblatt 與 UBS Buy / $300。

**注意**：cache 現價 $117.98，mean target $282.55 隱含約 +139% 上行空間。這種落差通常代表 target 尚未隨股價大幅下修，或股價反映了分析師沒有納入的風險（例如 lock-up 或基本面）。analyst 數據的「共識強度」可信，但「target 水準」的參考價值偏低。

## Retail social

- **Reddit（r/wallstreetbets、r/stocks）**：本次無法取得 2026-10 的可用討論串。WebSearch 找不到相關 thread。依規則 soft-fail，不另行 WebFetch。
- **AltIndex 自動化統計（9 月初快照）**：Reddit 提及量 90 日內下降 33.3%，約 8 則/日；9/4 單日暴增 250%。來源為自動化 alt-data，僅供參考。
- **StockTwits**：WebSearch 只得到一則快照（時間不明，約 6 月至 8 月），情緒儀表空白，無法判讀。StockTwits 直接 API 本次未呼叫。
- **SentiSense（約 8 月）**：30 日情緒 neutral，約 5 則提及/日，新聞面 Bullish（100% 提及為正向）。
- **Benzinga（8 月底快照）**：分析師共識 Buy，short interest 14.0% of float，put/call ratio 0.40（解讀為偏多）。
- **Historical Option Data（6 至 7 月）**：X/Twitter 文章混合多空，整體多方占約 60%–70%。這些頁面的價格與事件描述彼此矛盾，僅供參考。
- **Retail 量能**：無法對照 typical baseline。依 AltIndex 與 SentiSense 的數字，提及量屬低至中等，未見 2026-10 的 spike 證據。

**Themes（從公開報導歸納，時間多為 6 至 9 月）**：
1. 基本面：Q2 core revenue $209.9M，年增 74%，高於預期 $190.6M。EPS 大幅不如預期，財報後股價盤後 -15.66%。
2. 客戶與合作：OpenAI 750MW 合約（1 月）、Amazon AWS 部署 CS-3（3 月）、CrowdStrike 合作（股價當日 +23%）。
3. 估值爭論：Jim Cramer 指出 $311 時約 187 倍前一年營收。報導標題 "You'll Have to Buy It Up Here Without My Blessing" 反映追價疑慮。
4. Nvidia 替代敘事：CMC 文章 "Is Cerebras Really a Threat to Nvidia?" 為常見的牛市與競爭論點。
5. 供給壓力：早期釋出約 28M 股（財報後），主要 180 天 lock-up 預計 2026-11 中旬到期（來源為 Curved Trading，未經 SEC filing 驗證）。
6. 反向意見：TradingView 一則 idea 寫 "Don't buy yet, wait for the correction."

**Retail tilt**：無法以 2026-10 數據判定。6 至 9 月的零散樣本偏多（約 60%–70% 多方，Benzinga 偏多），但 9 月後股價已由 $195–240 跌至 $118，多方敘事是否延續無從確認。暫定為 **mixed / 資料不足**。

## Insider activity

Net 6mo（2026-04-22 至 2026-10-22，只計 open-market "Sale" 列；排除 gifts、awards、IPO conversions 及無金額的分配列）：**$0 買入 / 約 $408M 賣出**。

| 內部人 | 職位 | 6 個月賣出金額（約） | 近期代表性交易 |
|---|---|---|---|
| Sean Lie | CTO | $193.8M | 9/25 賣 120,000 股 @ $204.50–212.14；8/21 賣 726,540 股 @ $203.78–212.64 |
| Dhiraj Mallick | COO | $103.6M | 9/29 賣 396,000 股 @ $194.91–212.93；8/18 賣 38,889 股 @ $214.85–240.01 |
| Andrew Feldman | CEO | $64.3M | 9/4 賣 37,441 股 @ $199.18–216.62；8/21 賣 237,559 股 @ $196.20–210.21 |
| Steven Vassallo | Director | $21.4M | 9/4 賣 50,000 股 @ $209.81–211.56；8/14 賣 50,000 股 @ $216.38–219.97 |
| Eric Vishria | Director | $15.7M | 8/17 賣 68,268 股 @ $224.20–250.30 |
| Robert Komin | CFO | $6.6M | 9/29 賣 32,500 股 @ $194.92–211.79 |
| Yagnesh Patel | Officer | $3.0M | 9/28 賣 1,320 股 @ $204.50 |

觀察：
- 全部高管與董事皆為賣方，**無 open-market 買入**。
- 賣出價格集中在 $195–250。現價 $117.98 代表內部人在 9 月下旬以後的賣出價格比現價高約 65%–75%。
- 9/25–9/29 一週內 CTO、COO、CFO 集中賣出，為近期最密集區段。
- Gift 交易（Lie、Feldman、Patel）不計入賣出金額，但會降低持股，需與 10b5-1 計畫一併判讀。資料中無法確認賣出是否屬於 10b5-1 計畫。
- 6 月底至 7 月 $160–190 區間仍有 COO / CEO / CTO 賣出，代表內部人在不同價位持續減持。
- 10% 股東（Benchmark Capital、Foundation Capital）8 月有分配列，無金額，性質無法判定。6/11 Susan Lior（Director）13.47M 股列為無金額，性質同樣無法判定。

## Ownership shifts

- insidersPercentHeld：9.6%
- institutionsPercentHeld：80.3%（float 口徑 88.9%），機構數 542
- 前三大（6/30 13F）：Eclipse Operations 10.2%（11.45M 股）、FMR 7.5%、Altimeter 6.4%；Coatue 6.3%、Capital World 3.5%、Morgan Stanley 2.9%。
- inst_holders 的 pctChange 欄位在所有持股人皆為 1.0，代表資料格式或欄位定義異常，**無法判讀機構加減碼趨勢**。
- short percent of float：12.6%（cache）；WebSearch 8 月快照為 14.0%。

## Net sentiment score

- **分析師（Analyst）**：偏多，信心高。11/11 buy，共識穩定，近一個月僅一次升評。target 水準疑似過時。
- **內部人（Insider）**：偏空，信心中高。6 個月約 $408M 賣出，零買入，賣出價格高於現價。
- **零售（Retail）**：無法判定，信心低。資料僅來自 6 至 9 月快照，且時間與來源互相矛盾。
- **價格動能**：偏弱。現價 $117.98 接近 52 週低點 $115.13，距 52 週高點 $386.34 約 -69%。

**綜合**：**中性偏空（信心：低至中）**。分析師評等一致偏多，但內部人在股價 $195 以上持續大量賣出，且股價在 9 月後大幅下跌。零售情緒資料不足，不能支持或反駁多方敘事。

**Divergence flag：yes（部分）**
- 分析師（全部 Buy）與內部人（淨賣出）方向相反，屬於值得注意的背離。
- 零售傾向無法在 2026-10 確認，因此無法判斷 retail 是否與分析師同向或反向。
- 若 lock-up 於 11 月到期，內部人賣壓與供給壓力可能成為近期主要變數。此點需以 SEC filing 或 IR 公告再行確認。

## 資料缺口與後續查核

1. Reddit / StockTwits 2026-10 的實際討論量與情緒，需以直接查看或付費工具補足。
2. analyst target 的更新時間與是否已反映 9 月後的股價下跌，需以 MarketBeat 或 Benzinga 最新頁面核對。
3. 內部人賣出是否屬於 10b5-1 計畫，需查 Form 4 footnote。
4. lock-up 到期日與早期釋出股數，需以 S-1 / 公司公告核對。

SENTIMENT REPORT COMPLETE
