# 情緒分析 — AMT (American Tower Corp) 截至 2026-11-07

## Executive summary

- 分析師評級面偏多: yf `rec_summary` 顯示 25 家券商中 22 家為 Buy 類 (7 Strong Buy + 15 Buy), 3 家 Hold, 0 家 Sell. 但三個期間 (0m / -1m / -2m) 數字完全相同, 無法判斷近期評級變動.
- 散戶情緒無法可靠量化: Reddit 直接存取被擋 (WebFetch 回傳無法連線), StockTwits 依規則未直接抓取, WebSearch 只找到 2025 年與低品質聚合站資料. 無 2026 年 11 月的可用散戶樣本.
- 內部人近 6 個月淨賣出約 $0.82M (買入 $0.50M / 賣出 $1.32M). 唯一公開市場買入為董事 Rajesh Kalathur (2026-08-21, $500,733). 賣出集中於 2026-07-29 的 Meyer 與 Dowling, 以及 2026-10-30 的 Font.
- 機構持股高度集中於被動型基金 (BlackRock 9.87%, Vanguard 合計約 12.7%). 最新可得的 13F 為 2026-06-30 季, 其中 JPMorgan 減持約 41%, Lazard 與 Cohen & Steers 增持.
- 綜合判讀: 分析師面偏多, 內部人淨賣出溫和, 散戶面無法判定. 整體信心低到中等.

## Data availability

| 來源 | 狀態 | 備註 |
|---|---|---|
| yf `rec_summary` / `recommendations` | 可用, 但不完整 | 同一組數字重複三期, 且 `recommendations` 未回傳升降評歷史. 數據日期不明. |
| yf `insider` | 可用 | 含 2025-03 至 2026-10-30 交易紀錄. 6 個月窗口為 2026-05-07 至 2026-11-07. |
| yf `major_holders` | 可用 | 機構持股 97.25%, 內部人 0.08%, 機構數 2,403. |
| yf `inst_holders` | 可用 | 報告日 2026-06-30 (Q2 13F). Q3 13F 截至 2026-11-07 尚未完整公布. |
| Reddit r/stocks 搜尋 | 失敗 | WebFetch 回傳 "unable to fetch from www.reddit.com". r/wallstreetbets 未嘗試 (同一網域). |
| StockTwits | 未直接抓取 | 依規則不對財經站使用 WebFetch. 僅以 WebSearch 取得 2025 年文章. |
| X / 新聞 WebSearch | 部分可用 | 2026-04 至 2026-07 資料為主, 無 11 月資料. 部分來源品質低, 已標示. |
| Yahoo cookie / crumb | 失敗 | 連線錯誤, 但 yf 工具仍回傳資料. |

## Retail / social sentiment read

- **Reddit**: 無法取得. WebSearch 未找到 2026 年 AMT 的 r/wallstreetbets 或 r/stocks 討論串. 唯一相關結果為 Quiver Quantitative 的 AI 摘要頁, 描述社群語氣偏多 ("breakout" 類字眼), 但該頁本身標註為 AI 生成摘要, 不具樣本代表性, 且日期不明.
- **StockTwits**: 最近可找到的專文為 2025 年 4 月 (Morgan Stanley 升評後, 散戶情緒由 bearish 35/100 轉為 neutral 50/100) 與 2025 年中 (財報後轉為 bullish, 討論量 high). 皆早於本報告窗口, 不能代表 2026 年 11 月.
- **X / 其他社群**: 2026 年多頁面為自動生成內容, 含 "constructive" 或 "mixed" 等描述, 無可驗證的情緒數據支持, 不採用.
- **討論量**: 無法估算相對於常態的提及次數. 定性上, 缺乏 2026 年 11 月的獨立散戶討論來源, 不能判定聲量高或低.
- **主要主題 (有限樣本推測)**: 資料中心與 Oi 相關營收 (外匯與非現金收入) 被提及較多; 股價落後大盤 (Barchart: 52 週跌約 19%, 日期不明). 這些是來自分析文章的主題, 並非散戶原文.
- **散戶傾向**: 無法可靠判定. 暫列「無法判定 (資料不足)」。

## Analyst consensus

**目前分佈 (yf rec_summary, 來源日期未標示)**

| 評級 | 家數 |
|---|---:|
| Strong Buy | 7 |
| Buy | 15 |
| Hold | 3 |
| Sell | 0 |
| Strong Sell | 0 |
| 合計 | 25 |

Buy 類占比約 88% (22/25). 三期數字相同, 因此無法確認近期是否有升降評.

**近期動向 (WebSearch, 2026-04 至 2026-07, 未能與 11 月數據核對)**
- Mizuho: 由 Neutral 升至 Outperform, 目標價 $205 (2026-04).
- BofA: 維持 Buy, 目標價 $210.
- Truist: 首次覆蓋, 給予 Buy, 理由為資料中心成長.
- KeyBanc: 維持 Sector Weight, 認為股價低估.
- RBC: 維持 Hold, 目標價 $195.

**目標價 (各來源不一致, 日期不同)**
- 一則聚合資料: 平均目標價約 $188.
- 另一則: 平均目標價約 $220.
- Benzinga 2026-07-30 快照: 19 家分析師 Buy 共識, 平均目標價 $226.
- 參考價: 最近一筆內部人交易價為 $189.63 (2026-10-30). 這不是即時報價, 僅作為近期價位參考.

## Institutional / insider signal

**內部人交易 (6 個月窗口: 2026-05-07 至 2026-11-07, 單位 USD M)**

| 日期 | 內部人 | 職稱 | 類型 | 股數 | 金額 (USD M) |
|---|---|---|---|---:|---:|
| 2026-08-21 | Rajesh Kalathur | 董事 | 公開市場買入 | 2,829 | 0.50 |
| 2026-07-29 | Robert J. Meyer Jr. | Officer | 賣出 | 5,000 | 0.89 |
| 2026-07-29 | Ruth T. Dowling | 總法律顧問 (GC) | 賣出 | 1,791 | 0.31 |
| 2026-10-30 | Juan Hernandez Font | Officer | 賣出 | 592 | 0.11 |

- 買入合計: $0.50M
- 賣出合計: $1.32M
- 淨額: 約 -$0.82M (淨賣出)
- 驗算: 2,829 股 × $177.00 ≈ $0.50M, 與工具回傳一致.

**窗口外或非現金交易 (不計入淨額)**
- CEO Steven Vondran, COO Eugene Noel, CFO Rodney Smith 於 2026-02 至 2026-03 有大額選擇權行權後賣出 (合計約 $20M 以上), 但皆在窗口外.
- 2026-03-10 多筆董事與高管股票獎勵, 金額為 $0, 不計入.
- 2026-05-28 董事 Reeve 贈與 810 股, $0.

**解讀**: 大額賣出多集中於選擇權行權後的變現, 工具未標示是否為 10b5-1 計畫, 無法判定動機. 唯一公開市場買入來自董事 (非 CEO/CFO). CEO/CFO 在窗口內無公開買入.

**機構持股 (2026-06-30, Q2 13F, 單位: 股數 M, 金額 USD M)**

| 機構 | 持股比例 | 股數 (M) | 市值 (USD M) | 季度股數變化 |
|---|---:|---:|---:|---:|
| BlackRock | 9.87% | 45.8 | 8,884 | +1.9% |
| Vanguard Capital Mgmt | 6.56% | 30.4 | 5,905 | +0.3% |
| Vanguard Portfolio Mgmt | 6.01% | 27.9 | 5,403 | +0.9% |
| State Street | 4.76% | 22.1 | 4,281 | +3.0% |
| Geode Capital | 2.98% | 13.8 | 2,685 | -0.7% |
| Cohen & Steers | 2.97% | 13.8 | 2,673 | +9.2% |
| FMR | 2.45% | 11.4 | 2,207 | +0.5% |
| Morgan Stanley | 2.07% | 9.6 | 1,864 | +0.3% |
| JPMorgan Chase | 1.91% | 8.9 | 1,717 | -41.5% |
| Lazard | 1.81% | 8.4 | 1,630 | +14.7% |

- 機構持股合計 97.25%, 機構數 2,403. 內部人持股僅 0.08%.
- 前十大持股以被動型基金為主 (BlackRock, Vanguard, State Street, Geode 合計約 24%), 集中度高但並非由單一主動型基金主導.
- JPMorgan 大幅減持為窗口中最大的單一機構變化, 但持股比例基數小 (1.91%), 對整體籌碼影響有限.
- 主動型基金中 Cohen & Steers 與 Lazard 增持, 方向偏多.
- Q3 2026 13F 尚未完整公布, 截至 2026-11-07 的機構動向只能參考 Q2 數據.

## Overall sentiment verdict

| 面向 | 判讀 | 信心 |
|---|---|---|
| 分析師共識 | 偏多 (22/25 Buy 類) | 中 (分佈來源未標日期, 近期變動無法確認) |
| 散戶 / 社群 | 無法判定 | 低 (資料不足) |
| 內部人 (6 個月) | 溫和淨賣出 (-$0.82M), 董事有一筆公開買入 | 中低 (賣出多為行權後變現, 動機不明) |
| 機構持股 | 穩定, 被動基金為主, 主動型小幅分化 | 中 |

**綜合情緒**: 中性偏多 (信心低到中等).
- 偏多理由: 分析師評級集中於 Buy, 主動型機構 Cohen & Steers 與 Lazard 增持.
- 偏空或保留理由: 內部人窗口內淨賣出, 股價落後大盤 (日期不明), 分析師目標價在不同來源間分歧 ($188 至 $226).

**背離旗標**: 無法判定 (散戶面無資料). 若以分析師與內部人對比, 分析師偏多而內部人淨賣出, 屬於輕度背離, 但內部人賣出的脈絡不明, 不宜過度解讀.

**本報告不含交易建議。**

## Sources

- 本地工具 (pipeline/tools/yf.py): `AMT recommendations`, `AMT rec_summary`, `AMT insider`, `AMT major_holders`, `AMT inst_holders`. 數據為工具回傳值, 日期以各欄位為準.
- WebSearch (2026 年 4 月至 7 月文章, 未能與 11 月數據核對):
  - [Are Wall Street Analysts Predicting American Tower Stock Will Climb or Sink?](https://finance.yahoo.com/markets/stocks/articles/wall-street-analysts-predicting-american-131100596.html)
  - [is wall street bullish or bearish on american tower stock (Barchart)](https://www.barchart.com/story/news/42954/is-wall-street-bullish-or-bearish-on-american-tower-stock)
  - [Here's What Wall Street Thinks About American Tower Corporation (AMT)](https://finance.yahoo.com/news/wall-street-thinks-american-tower-144531879.html)
  - [American Tower Corp Price Targets (Benzinga)](https://kr.benzinga.com/quote/AMT/price-targets)
  - [KeyBanc on American Tower (AMT): '2026 Guide Downside Potential Priced In'](https://www.streetinsider.com/Analyst+Comments/KeyBanc+on+American+Tower+%28AMT%29%3A+2026+Guide+Downside+Potential+Priced+In/26006908.html)
  - [American Tower Upgraded On Growth Prospects Beyond 2025, Retail Traders Yet To Bite (StockTwits)](https://stocktwits.com/news-articles/markets/equity/american-tower-upgraded-on-growth-prospects-beyond-2025/chf2goYRb4y)
  - [AMT Opinions (Quiver Quantitative)](https://www.quiverquant.com/news/American+Tower+Stock+%28AMT%29+Opinions+on+ATNI+Tower+Sale)
- 失敗或未使用: Reddit r/stocks 搜尋 (WebFetch 無法連線); StockTwits 直接 API 未使用 (財經站規則).

SENTIMENT REPORT COMPLETE
