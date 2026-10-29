# Sentiment — SYM (Symbotic Inc.) as of 2026-10-30

資料基準: 盤後資料以 2026-10-29 為準 (最後可確認報價為 2026-10-26 收盤附近, 約 USD 37.90)。Reddit 與 StockTwits 來源無法取得, 散戶情緒部分為低信心度。

## Analyst consensus

yfinance rec_summary (18 家, 0m): Strong Buy 1 / Buy 9 / Hold 5 / Sell 2 / Strong Sell 1, 即 10 buy / 5 hold / 3 sell。
近三個月 (-1m 至 -3m) 結構大致穩定, 最新一期 Buy 側由 8 增至 10 (含 Strong Buy), Sell 側持平 (3)。

MarketBeat (2026-09-18) 彙整: 7 Buy / 4 Hold / 4 Sell, 共同目標價 USD 65.42。兩個來源家數與結構不一致, 原因是家數與日期口徑不同, 不宜合併。

近期評等動向 (網路彙整, 日期多為報導日, 未逐一核對原始評等單):
- Barclays: 目標價由 USD 44 降至 USD 38, 評等 Underweight (2026-09-08)。
- Goldman Sachs: 目標價由 USD 54 降至 USD 45, 評等 Sell (2026-05-26)。
- DA Davidson: 維持 Buy, 目標價 USD 70 (2026-05-11)。
- Weiss Ratings: 5 月下調至 sell。
- Citi: 10 月中維持 Buy (標題報導)。
- KeyBanc: 有升評標題 (日期未確認)。

目標價落差: 共同目標價約 USD 63–66, 相對 USD 38 左右股價仍有約 65–70% 上行空間。此落差較可能反映目標價未隨股價下修, 而非分析師普遍看多, 解讀時需保留。

## Retail social

- Reddit (r/wallstreetbets, r/stocks): 無法取得。WebFetch 回傳 Reddit 網域被拒, 本次未取得任何 SYM 討論串, 無法評估論壇語氣與討論量。來源狀態: 失敗 (軟失敗, 已略過)。
- StockTwits: 無法取得。api.stocktwits.com 無法解析 (DNS 不在本次 session 允許網域內), 需於 session 網路設定中允許後才能重試。已改用網路彙整替代。
- StockTwits 第三方彙整 (AltIndex, 非官方數據): 約 56 則/日提及, 較三個月前增加約 24%; 情緒分數 94/100 (偏多)。方法論未公開, 且頁面數據日期不一, 僅供量級參考。
- X / 新聞鏈: 近期文章語氣偏中性, 多為財經聚合站轉載; MarketBeat 新聞情緒分數 0.63, 但同頁社群評分僅 2.9/5, 整體只能判定為「不一致」。
- 本次未能引用任何原始貼文 (無可驗證的貼文內容), 因此不提供引述。

Buzz 量能: 相對一般水準為中等偏高 (依 AltIndex 增幅估計), 但信心低, 且事件驅動 (財報、併購、大幅跌價時會放大)。

Themes (由新聞與彙整文章歸納, 非來自散戶貼文本身):
1. FQ2 2026 大幅下修 EPS 指引, 之後一連串下調評等, 是股價自高點 (約 USD 60 上下) 回落的主因。
2. 空頭部位偏高 (MarketBeat 約 10.1 天回補), 反彈時有軋空敘事。
3. 2026-10-13 宣布收購 Cellumation, 被視為成長敘事的新變數。
4. 下一次財報預估日 2026-11-23 (TrendSpider、StockAnalysis 一致) 被視為近期主要催化劑, 但日期來源僅兩家, 需以公司公告確認。

Retail tilt: 偏多 (僅一個第三方來源, 信心低)。

## Insider activity

Net 6mo (2026-04-29 至 2026-10-29, 皆為 Sale, 無公開市場買入): 
- 買入: USD 0 M
- 賣出: USD 290.6 M (其中 SoftBank Group 單筆 USD 281.8 M, 5.59M 股, 2026-05-27, 價約 USD 50.42, 為 10% 以上大股東)
- 扣除 SoftBank 後賣出約 USD 8.8 M (25 筆有價成交)

| 內部人 | 職位 | 期間賣出 (USD M) | 備註 |
|---|---|---|---|
| SoftBank Group | 10% 以上大股東 | 281.8 | 2026-05-27 單筆大宗 |
| Todd J. Krasnow | Director | 3.49 | 多次小額, 2026-05 至 10 月 |
| James J. Kuffner Jr. | CTO | 1.88 | 2026-10-27 亦有賣出 (USD 0.74 M) |
| Izilda P. Martins | CFO | 1.12 | 2026-07-27 賣出 |
| William M. Boyd III | Officer | 0.97 | 2026-10-27 賣出 (USD 0.36 M) |
| Brian D. Alexander | Officer | 0.72 | 2026-10-27 賣出 (USD 0.36 M) |
| Charles F. Kane | Director | 0.55 | 定期小額 |
| Maria G. Freve | Officer | 0.09 | 小額 |

Notable:
- 2026-10-27 集中賣出: CTO Kuffner (約 19.4 千股, USD 0.74 M, 價 USD 38.24–38.34)、Boyd 與 Alexander 各約 9.2–9.3 千股, 價約 USD 38.3。這是 6 個月內價位最低的一批賣出 (4 月與 5 月的賣出價在 USD 50–60 區間)。
- 部分 10/23 與 7/23 等日期的交易無價格 (可能為限制性股票歸屬、稅款扣繳或贈與), 本次未能確認性質, 未計入金額。
- 多筆賣出為固定股數 (Krasnow、Kane 每次 2,000 股), 較像預先排程 (如 10b5-1), 但未經公司文件確認。
- 本窗口內未見 CEO 的交易紀錄; 未確認是否為無交易或資料缺漏。
- 本窗口內無任何公開市場買入。

判讀: 內部人淨賣出明顯, 且賣出價位逐步下移, 含 SoftBank 大宗出清。不宜單獨解讀為看空訊號 (多數為例行或計畫性賣出), 但買入側完全缺席。

## Ownership shifts

- Insider 持股比例: 13.7%
- 機構持股比例: 79.2% (流通股比例 91.8%), 機構家數 554
- SoftBank (前大股東) 於 2026-05 大幅減持 (5.59M 股), 為近期最明顯的籌碼轉移。
- 無多期機構持股變化資料, 無法判定趨勢方向, 僅能確認目前高集中於機構。

## Net sentiment score

Composite: **中性偏空 (neutral-to-bearish), 信心度: 低至中**

分項:
- 分析師: 中性 (10 買 / 5 持有 / 3 賣; 目標價落差大, 且 Barclays、Goldman 近期下調) — 偏多結構, 但動能偏空。
- 散戶: 偏多 (單一第三方彙整, 無法驗證, 信心低)。
- 內部人: 偏空 (淨賣出, 含大宗減持, 買入缺席)。
- 籌碼: 機構高度持有, 大股東減持, 空頭比例高。

Divergence flag: **是 (部分)**
- 散戶 (偏多) 與分析師 (結構偏多) 方向一致, 但兩者都與股價動能相反, 且散戶訊號不可靠。
- 內部人 (淨賣出, 且在低價區賣出) 與分析師多數 Buy 的評等結構相反, 這一分歧較具參考價值。
- 因 Reddit、StockTwits 無資料, 無法確認散戶與分析師是否真正背離, 此旗標信心低。

資料限制摘要:
- Reddit、StockTwits 均未取得。
- 股價來源不一致 (USD 37.90 於 10/26、USD 39–42 無日期), 以 10/27 內部人成交價 USD 38.2–39.1 作為近期參考。
- 分析師家數與目標價在 yfinance 與 MarketBeat 間不一致。
- 網路彙整頁面有過期數據 (2025 年價格、明顯不合理的目標價), 已排除。

本報告為情緒資料彙整, 不構成交易建議。

SENTIMENT REPORT COMPLETE
