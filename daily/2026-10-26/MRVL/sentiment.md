# Sentiment — MRVL (Marvell Technology) as of 2026-10-26

資料說明：分析師與持股資料取自 `pipeline/tools/yf.py`（yfinance 快照，Yahoo cookie/crumb 取得失敗但資料仍回傳）。Reddit 與 StockTwits 依指示不直接抓取，DATA_UNAVAILABLE；零售情緒改以 WebSearch 聚合的新聞與社群間接線索代替，信心較低。2026-10-26 之後的資料視為未知。

## 價格與估值快照

| 項目 | 數值 | 單位 |
|---|---|---|
| 最新價 (currentPrice) | 228.51 | USD |
| 前收 | 223.47 | USD |
| 52 週高 / 低 | 329.88 / 70.69 | USD |
| 市值 | 205.4 | USD B |
| TTM 營收 | 9.45 | USD B |
| 自由現金流 | 2.41 | USD B |
| Trailing P/E / Forward P/E | 75.2 / 31.2 | x |
| 流通股數 | 876.9 | M shares |
| 做空比例 (占 float) | 3.2 | % |

## Analyst consensus

本期（0m）分布：strongBuy 9 / buy 33 / hold 4 / sell 0 / strongSell 0，合計 42 家（info 欄位 numberOfAnalystOpinions 為 43，差 1 家，屬來源口徑差異）。recommendationKey = strong_buy。

| 期間 | strongBuy | buy | hold | sell | strongSell | 買方合計 |
|---|---|---|---|---|---|---|
| 0m（本期） | 9 | 33 | 4 | 0 | 0 | 42 |
| -1m | 8 | 32 | 6 | 0 | 0 | 40 |
| -2m | 8 | 31 | 5 | 0 | 0 | 39 |
| -3m | 8 | 30 | 5 | 0 | 0 | 38 |

Recent moves:
- 買方家數 3 個月內由 38 增至 42，hold 由 5-6 家降至 4 家，最近一個月的 hold 減少 2 家，方向偏向升評或新增買進覆蓋。
- 沒有任何賣方評級，sell / strongSell 持續為 0。
- 個別升降評（券商名稱、日期、前後評等）：DATA_UNAVAILABLE，`recommendations` 只回傳彙總計數，無逐筆紀錄。
- 目標價（targetMeanPrice / High / Low）：平均 341.44 USD，最高 450.00，最低 229.95。平均目標相對最新價約 +49%。最低目標幾乎貼近現價（約 +0.6%），表示幾乎沒有覆蓋券商的目標價低於現價。
- 目標價的日期與逐家調整紀錄：DATA_UNAVAILABLE。

## Retail social

- Reddit (r/wallstreetbets, r/stocks)：DATA_UNAVAILABLE。依指示不直接抓取，且 WebSearch 未找到 r/wallstreetbets 中 MRVL 的實際討論串。無法給出討論串樣本、提及次數或多空比例。
- StockTwits：DATA_UNAVAILABLE（直接 API 被本環境阻擋）。間接線索：一篇較早的 StockTwits 新聞標題（2026 年 6 月，Nvidia 執行長公開背書後股價兩日大漲約 45%）描述社群情緒為 "extremely bullish"，之後出現隔夜獲利了結。該線索時間較舊，不代表 10 月的情況。
- X / 新聞與意見聚合（WebSearch，來源日期不一，部分無法確認）：
  - Naga 的 2026 年 10 月頁面將群眾情緒標為負面（NEGATIVE），開盤訊號偏空，但同頁新聞情緒標示偏多（約 95%），部落客觀點偏多約 69%。兩個指標方向不一致。
  - Wealthawesome 報導 2026 年 10 月 9 日股價下跌，歸因於市場對半導體成長可持續性的疑慮。該頁的價格數字有明顯錯誤（如顯示 C$0.12），不採用其價格資料。
  - Barchart 聚合的分析師分布為 24 Strong Buy / 3 Moderate Buy / 5 Hold（共 32 家），來源日期不明，與本期 Yahoo 口徑不同，僅作參考。
  - Google Finance 的意見分布 54.7% 偏多 / 1.6% 偏空，為 10 月初快照。
- 聲量（buzz volume）：DATA_UNAVAILABLE（無可靠的提及次數資料）。定性判斷：搜尋結果中 MRVL 的文章量屬中等偏高，多為分析與新聞，而非散戶討論串。

## Retail themes（定性，低信心）

- 偏多主軸：AI 資料中心與客製化 ASIC 需求，以及公司長期營收目標（報導提及 2028 年 200 億 USD 目標）。
- 偏空主軸：估值（trailing P/E 超過 90 的說法在部分來源出現，本次 yfinance 的 trailing P/E 為 75）、AI 資本支出可持續性、半導體板塊的成長疑慮，以及 2026 年 10 月初的股價回檔。
- 引述（僅作語氣代表，非完整貼文）：新聞標題 "retail traders keep the faith" 類型的語氣，顯示散戶仍偏好持有。

## Insider activity

6 個月窗口：2026-04-26 至 2026-10-26。

| 指標 | 數值 | 單位 |
|---|---|---|
| 公開市場買入（open-market buy） | 0 | USD M |
| 公開市場賣出（open-market sell，共 13 筆） | 20.7 | USD M |
| 淨額 | -20.7 | USD M |
| 贈與（Stock Gift，價格 0）| 2 筆（House 750 股、Casper 1,000 股）| shares |

主要賣出者（6 個月內）：
- CEO Matthew Murphy：6 月 15 日、7 月 15 日、8 月 17 日、9 月 15 日各售約 7,500 股，合計約 7.3M USD。另有 5 月 13 日 7,500 股（約 1.3M USD），窗口內合計約 8.6M USD。
- President Christopher Koopmans：5 月 1 日、7 月 1 日、8 月 3 日、9 月 1 日各售 10,000 股，合計約 8.3M USD，為窗口內金額最大的賣出者之一。
- CFO Daniel Durn：6 月 23 日賣出 2,250 股（約 0.6M USD）。CFO 紀錄另一位 Willem Meintjes 於 5 月 15 日賣出 4,000 股（約 0.7M USD）。
- Officer Sandeep Bharathi 於 6 月、7 月賣出，合計約 2.5M USD。

規律性觀察：CEO 與 President 的賣出股數呈固定、週期性（每月或每季固定股數），符合預定交易計畫的常見特徵，但本資料無 10b5-1 旗標，無法確認 DATA_UNAVAILABLE。

另有大量無金額紀錄（Value 為空）的交易，多為股權歸屬或稅務代扣，不計入上述金額。

對照：2025 年 9 月 25 日曾有 CEO、CFO、President 等集體公開市場買入（約 77-78 USD/股）。近六個月內無買入。

## Ownership shifts（機構，資料截至 2026-06-30 13F）

- 機構持股比例 81.7%，機構數 2,969 家。內部人持股 0.50%。
- 前十大持股（季末 2026-06-30）：

| 機構 | 持股比例 | 股數 (M) | 季變動 |
|---|---|---|---|
| BlackRock | 9.77% | 85.6 | +34.1% |
| Vanguard Capital Mgmt | 6.60% | 57.9 | +48.1% |
| FMR (Fidelity) | 6.49% | 56.9 | -56.6% |
| State Street | 4.77% | 41.8 | +79.3% |
| Invesco | 3.45% | 30.3 | +5.1% |
| Geode | 2.41% | 21.1 | +67.9% |
| Vanguard PM | 2.40% | 21.0 | -36.7% |
| Goldman Sachs | 1.68% | 14.7 | +30.7% |
| Norges Bank | 1.62% | 14.2 | +34.8% |
| JPMorgan | 1.58% | 13.9 | +138.8% |

- 前十大中七家增持、兩家減持（FMR -56.6%、Vanguard PM -36.7%）。FMR 減持幅度最大，是本表中唯一的大型主動基金大幅減碼。多數增持來自指數型與被動帳戶（BlackRock、Vanguard、State Street、Geode）的規模調整，不一定代表主動判斷。
- 2026 年第三季 13F（9 月 30 日）：DATA_UNAVAILABLE，尚未納入資料。

## Net sentiment score

綜合判斷：**中性偏多**（信心：中低）

| 面向 | 方向 | 信心 | 理由 |
|---|---|---|---|
| 分析師 | 偏多 | 高 | 42 家買方，0 家賣方，平均目標約 +49% |
| 內部人 | 偏空 | 中 | 6 個月淨賣約 20.7M USD，無公開市場買入；多數可能為預定計畫 |
| 機構 | 中性偏多 | 中 | 前十大多數增持，但 FMR 大幅減持 |
| 零售 | 分歧 | 低 | Reddit / StockTwits 缺資料；新聞群眾情緒指標偏空，新聞情緒偏多 |

Divergence flag: **是**。分析師與機構偏多，而 (a) 內部人在本窗口持續淨賣出，(b) 可得的群眾情緒指標（Naga 群眾情緒）偏空，兩者方向相反。但零售端資料不完整，此背離訊號信心低，不宜單獨作為判斷依據。

資料缺口彙整（DATA_UNAVAILABLE）：Reddit 討論串與提及量、StockTwits 多空比、X 逐篇貼文、逐筆分析師升降評與券商名稱、2026 年第三季 13F、10b5-1 計畫旗標、目標價修正日期。

SENTIMENT REPORT COMPLETE
