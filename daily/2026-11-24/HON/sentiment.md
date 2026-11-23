# HON 情緒分析 (Sentiment Analysis)

- **Ticker**: HON (Honeywell International Inc.)
- **分析日期**: 2026-11-24
- **資料來源**: `pipeline/tools/yf.py` (source: cache), WebSearch
- **注意**: 資料為 cache 快取值；本次未取得即時股價，`recommendations` 與 `rec_summary` 回傳內容相同。

---

## 1. Analyst Consensus (分析師共識)

| Period | strongBuy | buy | hold | sell | strongSell | Total | Bullish (SB+B) | Hold | Bearish (S+SS) |
|---|---|---|---|---|---|---|---|---|---|
| 0m (current) | 3 | 11 | 9 | 0 | 1 | 24 | 14 (58.3%) | 9 (37.5%) | 1 (4.2%) |
| -1m | 3 | 11 | 9 | 0 | 1 | 24 | 14 (58.3%) | 9 (37.5%) | 1 (4.2%) |
| -2m | 3 | 11 | 9 | 0 | 1 | 24 | 14 (58.3%) | 9 (37.5%) | 1 (4.2%) |
| -3m | 3 | 12 | 8 | 0 | 1 | 24 | 15 (62.5%) | 8 (33.3%) | 1 (4.2%) |

**觀察**
- 目前 24 位分析師中 14 位給予買進 (Buy 或 Strong Buy)，比例 58.3%；無 Sell 評等，僅 1 位 Strong Sell。
- 過去約 3 個月有一檔買進評等轉為持有 (-3m 時 Buy 12 / Hold 8；-2m 起 Buy 11 / Hold 9)，目前維持不變，評等結構微幅向中性移動。
- 整體仍偏多，但看多幅度較 3 個月前略為收斂。

---

## 2. Institutional Holdings Trend (機構持股趨勢)

**整體持股指標**

| Metric | Value |
|---|---|
| institutionsPercentHeld | 82.34% |
| institutionsFloatPercentHeld | 82.39% |
| institutionsCount | 2,847 |
| insidersPercentHeld | 0.058% |

**前十大機構持股 (報告日 2026-09-30)**

| # | Holder | pctHeld | Shares | pctChange (QoQ) | 方向 |
|---|---|---|---|---|---|
| 1 | Blackrock Inc. | 7.91% | 25,091,619 | +10.16% | 增持 |
| 2 | Vanguard Capital Management LLC | 6.54% | 20,741,214 | +0.23% | 持平 |
| 3 | State Street Corporation | 6.07% | 19,264,303 | +2.81% | 增持 |
| 4 | Vanguard Portfolio Management LLC | 3.99% | 12,675,681 | +61.21% | 大幅增持* |
| 5 | Invesco Ltd. | 3.33% | 10,578,111 | -5.97% | 減持 |
| 6 | Morgan Stanley | 3.26% | 10,360,419 | +7.56% | 增持 |
| 7 | Geode Capital Management, LLC | 2.50% | 7,925,297 | -3.43% | 減持 |
| 8 | Newport Trust Company, LLC | 2.03% | 6,432,598 | -50.00% | 大幅減持 |
| 9 | Franklin Templeton, Inc. | 1.61% | 5,106,787 | -21.54% | 減持 |
| 10 | Massachusetts Financial Services Co. | 1.48% | 4,696,282 | -7.34% | 減持 |

- 前十大合計持股約 38.7%。
- 十大機構中 5 家增持、5 家減持；合計來看，指數型與被動投資機構 (Blackrock、Vanguard、State Street) 持續加碼。
- \*Vanguard Portfolio Management 的 +61% 增幅可能反映 Vanguard 申報架構調整，而非實際買入，解讀時需保守。
- 主動型基金 (Franklin、MFS、Newport) 多數減持，為較偏空的訊號。
- 前十大名單未出現 Elliott Management，無法從本次資料確認其目前持股狀況。

---

## 3. Insider Transactions (內部人交易)

資料時間範圍：約 2025-02 至 2026-10-26。以下聚焦近 6 個月 (2026-05 起)。

**近 6 個月有明確金額的 Sale 交易**

| Date | Insider | Position | Type | Shares | Price | Value (USD) |
|---|---|---|---|---|---|---|
| 2026-10-26 | KAPUR VIMAL M | Chief Executive Officer | Sale | 6,459 | $220.99 | $1,427,374 |
| 2026-10-26 | LU SU PING | General Counsel | Sale | 2,943 | $221.18 | $650,934 |
| 2026-08-03 | WEST KENNETH J | Officer | Sale | 316 | $245.47 | $77,569 |
| 2026-07-27 | WEST KENNETH J | Officer | Sale | 17,032 | $243.77 | $4,151,891 |

- 近 6 個月明確 Sale 合計：26,750 股，約 **$6.31M**。
- 相關 Option 行使 (Conversion of Exercise)：KAPUR 8,684 股 (2026-10-26，行使價 $114.44)、LU SU PING 4,033 股 (2026-10-26，行使價 $114.44)、WEST 17,032 股 (2026-07-27，行使價 $181.39–$200.61)。行使後隨即賣出，屬選擇權變現。
- 另有多筆 Value 為空白的紀錄 (如 2026-07 至 2026-04 之多位董事與高管股份異動)，性質未在資料中標示，可能為股權獎勵或稅務代扣，本次**不計入**賣出統計。

**較早期的重要交易 (參考)**
- 2026-02-06 至 2026-02-23：MAILLOUX ROBERT D、LIEBLEIN GRACE D 等有選擇權行使後賣出，合計約 $5.5M。
- 2025-08-27：BOLDEA LUCIAN 行使並賣出約 42,149 股，約 $9.3M。
- 2025-02-10：MADDEN ANNE T 行使並賣出 28,885 股，約 $6.0M。

**摘要判讀**
- 近 6 個月資料中 **未見任何公開市場買進 (Purchase) 交易**。
- 執行長 KAPUR 與總法律顧問 LU SU PING 於 2026-10-26 同日執行選擇權並賣出，屬於近期最具代表性的高階主管交易。
- 整體模式為「選擇權行使後賣出」，偏向獲利了結，而非加碼信號；但持股比例僅 0.058%，內部人持股本身偏低。
- 近期賣出價位約 $220–$245，與 2026-11 初約 $229 的報價區間相近，賣壓規模對流動性而言不大。

---

## 4. Retail / Social Sentiment (散戶與社群情緒)

| Source | Reading | 備註 |
|---|---|---|
| Stocktwits | Extremely bullish (引用文章) | 該文描述 Elliott 揭露 $50 億持股後的看多情緒與訊息量暴增；文中圖表標示 Nov 12，年份未明確 |
| AltIndex (aggregated) | 98/100, bullish | 彙整 Reddit、Stocktwits 與論壇 |
| AltIndex (Reddit) | 76/100 | Reddit 提及量約每日 2 次，低於近期均值 |
| LunarCrush | ~97% positive (過去 24 小時約 658 則貼文) | 頁面股價 $225.02 偏低，可能為舊資料 |
| SentiSense | "Slightly bullish", 趨勢增強 | Reddit 中性，X 偏多 |
| TipRanks | "Very Positive" | 近一季約 821,666 名投資人參與 |

**判讀**
- 各平台整體偏多，但數值來源與計算方式不一，**不宜直接平均**。
- 搜尋結果中有若干 Stocktwits 文章為 2025 年舊文 (如 "death cross" 偏空文)，不代表目前情緒，已排除於判斷之外。
- 社群熱度的主要驅動仍是 Elliott 與拆分計畫相關新聞，屬事件驅動型情緒，持續性待觀察。

---

## 5. Activist / Corporate Event Angle (激進投資人與拆分事件)

- **Elliott Management**：2024 年 11 月揭露超過 $50 億持股，為其單一個股最大部位之一，並主張拆分。
- **拆分計畫**：2025 年 2 月 HON 宣布將航太 (Aerospace)、自動化 (Automation) 業務分拆，並另行拆出先進材料 (Advanced Materials) 業務，目標 2026 下半年完成、以免稅方式進行。
- **最新狀態**：Semafor 2026-06-12 報導指出 Honeywell Aerospace 預計 2026-06-29 獨立上市，CEO Kapur 地位未受挑戰，Elliott 公開給予正面評價；Kapur 將主導自動化業務 (Honeywell Technologies)。
- **未能確認**：搜尋結果未涵蓋 2026-06 之後的進展，**航太分割是否已完成、自動化業務分拆的時程與狀態均無法確認**，需進一步核對最新公告。
- 目前無新的激進投資人公開施壓的證據；但 Elliott 的既有影響力與拆分進度仍是重要的事件風險。

---

## 6. Composite Judgment (綜合判斷)

| Dimension | Signal | Score (-2 ~ +2) | Weight | Weighted | 依據摘要 |
|---|---|---|---|---|---|
| Analyst consensus | 偏多 | +1 | 30% | +0.30 | Buy 占 58%，無 Sell 評等；近 3 個月微幅降溫 |
| Institutional holdings | 中性偏多 | +1 | 20% | +0.20 | 機構持股 82%，指數型機構加碼；主動型基金多減持 |
| Insider transactions | 中性偏空 | -1 | 20% | -0.20 | 近 6 個月 Sale 約 $6.3M，無公開買進；多為選擇權變現 |
| Retail / social sentiment | 偏多 | +1 | 10% | +0.10 | 多數平台偏多，但數據雜亂且部分資料過時 |
| Activist / event angle | 不確定 | 0 | 20% | 0.00 | 拆分進度未完全確認，事件風險仍在 |
| **Composite** | **中性偏多** | | 100% | **+0.40** | |

**判讀與信心**
- 綜合分數 **+0.40 (範圍 -2 ~ +2)**，歸類為「中性偏多」。
- 信心水準：**中低**。主要原因：(1) 內部人交易與機構持股的解讀依賴推論；(2) 社群數據來源不一；(3) 拆分事件的最新狀態未能確認。
- 若後續確認航太分割已順利完成且自動化業務時程明確，活動面分數可上調；若出現內部人大額持續賣出或機構淨減持擴大，則綜合分數應向中性偏空調整。

---

## 資料缺口與待辦
1. 即時股價與當日成交量未取得 (yf.py 以 cache 為主)。
2. Cookie / crumb 取得失敗 (ConnectionError)，部分欄位可能為快取值。
3. 需以最新公告確認 Honeywell Aerospace 分割與自動化業務分拆的完成狀態。
4. Vanguard Portfolio Management 的持股大幅變動需確認是否為申報架構調整。

---

## Sources
- [Bloomberg: Honeywell to Break Up After Pressure From Activist Elliott](https://www.bloomberg.com/news/articles/2025-02-06/honeywell-to-split-into-three-separate-companies)
- [Semafor: Honeywell CEO on the brutal truth about breaking up an industrial giant (2026-06-12)](https://www.semafor.com/article/06/12/2026/honeywells-ceo-on-the-brutal-truth-about-breaking-up-an-industrial-giant)
- [Stocktwits: Honeywell Stock Hits Record Intraday High After Elliott Reveals $5B Stake](https://stocktwits.com/news-articles/markets/equity/hon-stock-surges-on-elliott-5-billion-stake/cJ402vrRON)
- [Stocktwits: Honeywell Stock Flirts With 'Death Cross' Zone (舊文，僅供參考)](https://stocktwits.com/news-articles/markets/equity/honeywell-stock-flirts-with-death-cross-zone/chDMMs4R37l)
- [AltIndex HON Sentiment](https://altindex.com/ticker/hon/sentiment)
- [AltIndex HON Reddit Mentions](https://altindex.com/ticker/hon/reddit-mentions)
- [LunarCrush: Honeywell International (HON)](https://lunarcrush.com/en/stock/honeywell-international-inc-hon)
- [SentiSense: Honeywell International, Inc. (HON) Sentiment](https://app.sentisense.ai/stocks/HON/sentiment)
- [TipRanks: HON stock investors](https://www.tipranks.com/stocks/hon/stock-investors)
- [Trefis: Which Dates Could Move Honeywell Stock Most? (2026-11-10)](https://www.trefis.com/stock/hon/articles/624114/which-dates-could-move-honeywell-stock-most/2026-11-10)
