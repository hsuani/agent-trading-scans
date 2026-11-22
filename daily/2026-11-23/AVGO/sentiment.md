# Sentiment — AVGO as of 2026-11-23

資料基準: 價格與 consensus 取自 prices/yf/AVGO.json 快取 (refreshed 2026-11-22 14:30 UTC, misses 為空)。yf 即時端 recommendations / insider / inst_holders 可取得且與快取一致; actions 與 news 回傳 403 (soft-fail, 已略過)。Reddit 與 StockTwits 依指示未抓取, 散戶面資料僅來自 WebSearch 摘要。

## Analyst consensus

最新 (0m) 分布: 8 strongBuy / 40 buy / 3 hold / 0 sell / 0 strongSell, 合計 51 家。info 欄位的 numberOfAnalystOpinions 為 47, 與 51 相差 4 家, 應為不同統計口徑, 本報告以 rec_summary 的 51 家為準。

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 買進佔比 (SB+B) |
|---|---|---|---|---|---|---|
| 0m (現在) | 8 | 40 | 3 | 0 | 0 | 94.1% |
| -1m | 8 | 41 | 2 | 0 | 0 | 96.1% |
| -2m | 7 | 40 | 3 | 0 | 0 | 94.0% |
| -3m | 8 | 37 | 4 | 0 | 0 | 91.8% |

近四個月評等結構幾乎沒有變化, 買進佔比維持在 92% 至 96% 之間, 無任何 sell 評等。Hold 由 4 家降至 3 家, 幅度很小。yf 工具只提供彙總計數, 無法列出個別券商的升降評等事件, actions 端點也因 403 無法取得, 因此「近期升降評等」只能描述為結構性持平, 不能列出具體事件。

目標價 (47 家): 平均 526.47 USD、中位數 525.00 USD、最高 660.00 USD、最低 398.47 USD。以快取 currentPrice 304.41 USD 計算, 平均目標隱含約 +73% 上行空間, 最低目標仍高出約 31%。這個價差異常大, 可能代表目標價尚未隨股價下修, 或 consensus 本身偏樂觀, 解讀時需保留。個別目標價歷史變動無法從工具取得。

市值約 1,453 B USD (流通股數約 4,773.6M 股)。

## Retail social

- Reddit: 依指示未抓取 (WebSearch 未回傳 Reddit 原文, 本節不列舉討論串)。
- StockTwits / X: StockTwits 直接 API 未使用。WebSearch 找到的 StockTwits 文章多為 2026 年 3 月前後的報導, 非 11 月即時。代表性標題如 "Retail says no way so many analysts can be wrong", 顯示散戶偏多但對全面看多的分析師有質疑。另一篇標題 "retail stays bullish" 也指向散戶在回檔時偏向逢低承接。
- 降溫訊號: Earnings Whispers 頁面顯示市場看多比例自 12.6% 降至 1.9%, 偏空, 但頁面無日期, 時點無法確認。
- 聲量: 散戶原生貼文量 (mention count) 無法取得, 無法與平常水準比較, 只能定性判斷為「無法量化」。11 月可見的討論主要來自媒體報導 (如 247wallst 2026-11-13), 而非散戶社群。
- Themes (反覆出現的主題):
  1. AI 需求與 backlog: 媒體與散戶普遍認同 AI 訂單能見度, 有提到 $73B backlog。
  2. 估值疑慮: 約 48 倍 forward P/E, 市場擔心樂觀已 price in。
  3. 板塊拋售: Trefis 提到 2026-11-05 的板塊性拋售, 原因包括選後政策審查可能拖慢資料中心建設。
  4. 年度漲幅: Barchart 引述 AVGO 一年漲約 89%, 大幅勝過 S&P 500 的約 27%, 此數據時點不明。
- Tilt: 偏多但降溫 (mixed-to-bullish)。信心低, 因 11 月可用的散戶來源極少。

## Insider activity

6 個月窗口: 2026-05-23 至 2026-11-23。注意: 工具回傳的最後一筆內部人交易為 2026-07-10, 之後約 4.5 個月無紀錄。這可能是 feed 更新落後, 也可能確實無交易, 需與 SEC Form 4 交叉確認。

以下僅計公開市場買賣, 不含 gift 與 stock award。

- Net 6mo (open-market): 買進 1 筆, 1,000 股, 約 0.37 M USD (YOU HARRY L, Director, 2026-06-11, 373.57 USD/股); 賣出 7 筆, 合計 740,885 股, 約 283.7 M USD; 淨賣出約 283.3 M USD。

| 日期 | 內部人 | 職稱 | 股數 | 金額 (M USD) | 價格 (USD) | 持有型態 |
|---|---|---|---|---|---|---|
| 2026-06-24 | SAMUELI HENRY | Director | 654,241 | 250.01 | 377.61–388.17 | I (間接) |
| 2026-07-10 | BRAZEAL MARK DAVID | Officer | 25,000 | 10.03 | 401.33 | D |
| 2026-06-25 | BRAZEAL MARK DAVID | Officer | 25,000 | 9.68 | 387.00 | D |
| 2026-07-08 | BRAZEAL MARK DAVID | Officer | 25,000 | 9.48 | 379.19 | D |
| 2026-06-17 | BRAZEAL MARK DAVID | Officer | 8,152 | 3.18 | 377.10–400.29 | D |
| 2026-07-08 | DELLY GAYLA J | Director | 1,890 | 0.73 | 385.38 | D |
| 2026-06-29 | PAGE JUSTINE F. | Director | 1,602 | 0.60 | 373.86 | D |

Notable:
- SAMUELI HENRY (Director) 於 6/24 以間接方式賣出 654,241 股, 約 250 M USD, 占窗口內賣出金額約 88%。同日另有 336,893 股 gift, 不計入上表。
- BRAZEAL MARK DAVID (Officer) 窗口內 4 筆賣出合計約 32.4 M USD, 是窗口內第二大賣方, 也是最頻繁的賣方。
- CEO HOCK E. TAN: 窗口內無交易。最後一筆公開市場賣出為 2026-01-06, 在窗口之外。
- CFO O'TOOLE AMIE THUENER: 2026-06-15 獲得 50,000 股 stock award, 屬授予而非市場買入。
- 公開市場買入僅見 Director YOU HARRY L, 窗口內 1 筆 (2026-06-11), 窗口外另有 2025-09-10 與 2025-12-18 兩筆。
- 價格脈絡: 窗口內賣出成交價在 373 至 401 USD 之間, 快取現價 304.41 USD 較這些價位低約 18% 至 24%。窗口內唯一買進價 373.57 USD 目前同樣為負報酬。
- 未採信資料: Trefis 提到 2026-09-23 Samueli 賣出超過 525 M USD, 但快取內 Samueli 的 9 月紀錄為 2025-09-24, 金額約 124.6 M USD, 兩者不符。此說法未核實, 本報告不採用。

Ownership (快取 major_holders 與 inst_holders):
- 內部人持股約 1.96%。機構持股約 79.7% (流通股口徑 81.3%), 機構家數約 6,312。
- 前十大機構 (2026-09-30 13F, 為一季前資料) 合計約 35.6%。10 家中 7 家增持、3 家減持。
- 增減結構: 被動型基金增持 (Vanguard Portfolio Management +8.4%、State Street +2.1%、Geode +1.3%); 主動型基金減持 (FMR -11.7%、Capital Research Global -3.9%); BlackRock 小幅減 -0.7%。多數變動幅度在 ±2% 內, 集中度沒有劇烈變化。

## Net sentiment score

Composite: 偏多 (bullish-leaning), 信心中低。

- 分析師面: 強烈偏多 (買進佔比約 94%、0 sell、平均目標隱含 +73%)。
- 內部人面: 偏空 (窗口內淨賣約 283 M USD, 其中近 9 成來自單一董事的間接持股)。賣出是否屬預定交易計畫, 資料無法判定。
- 散戶面: 中性偏多、近期降溫。來源稀少且多為非即時, 信心低。

Divergence flag: 是 (內部人與分析師方向相反)。散戶與分析師方向: 否, 兩者都偏多, 但散戶資料薄弱, 不宜據此推論強烈分歧。

資料限制:
- 快取現價 304.41 USD 與 247wallst 引用的 2026-11-13 開盤價 356.54 USD 相差約 15%, 這段價格變化未經獨立核實。
- 分析師人數 47 與 51 不一致 (已在上文說明採用 51)。
- 目標價平均與現價差距過大, 可能有陳舊目標價。
- 內部人 feed 在 2026-07-10 後無紀錄。
- actions、news 因 403 無法取得, 個別評等事件與新聞面未涵蓋。
- Reddit 與 StockTwits 未直接抓取, 散戶面以 WebSearch 摘要為主。

來源 (WebSearch): [247wallst 2026-11-13](https://247wallst.com/investing/2026/11/13/not-one-analyst-rates-broadcom-a-sell-what-are-they-missing/)、[Trefis AVGO](https://www.trefis.com/data/companies/AVGO?from=AVGO-2026-05-26)、[Invezz 2026-09-03](https://invezz.com/news/2026/09/03/broadcom-stock-falls-why-analysts-are-divided-on-the-stock/)、[StockTwits 散戶報導](https://stocktwits.com/news-articles/markets/equity/avgo-stock-falls-after-earnings-retail-stays-bullish/c7zSSIrRPP)。

SENTIMENT REPORT COMPLETE
