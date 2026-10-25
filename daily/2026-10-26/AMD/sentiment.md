# Sentiment — AMD (Advanced Micro Devices) as of 2026-10-26

資料時點說明：yfinance 快取時間為 2026-10-25 11:14 UTC，價格為 USD 516.79（當日 +1.74%）。2026-10-26 之後的資料一律視為未知。Reddit 與 X 的 2026-10 當期內容未取得，相關項目標示 DATA_UNAVAILABLE。

## Analyst consensus

| 項目 | 數值 | 備註 |
|---|---|---|
| 評等分布（最新，0m） | Strong Buy 5 / Buy 39 / Hold 11 / Sell 0 / Strong Sell 0 | 合計 55 家 |
| 評等分布（-1m / -2m / -3m） | 56 / 55 / 52 家；Hold 由 10 升至 11 | 無 Sell 評等，Buy 比例約 78% |
| recommendationMean | 1.49（strong_buy） | 1 = Strong Buy，5 = Sell |
| 分析師家數（yfinance info） | 50 | 與評等分布加總 55 不一致，屬資料源差異 |
| 目標價（USD） | 平均 637.6 / 中位數 635.5 / 最高 1,250 / 最低 365 | 相對現價 516.79 隱含上漲約 23%（平均值）|
| 歷史升降評等事件 | DATA_UNAVAILABLE | yf `recommendations` 只回傳彙總趨勢，不含逐筆升降評等 |

近期動向（網路報導，日期不一，未能與 yfinance 逐筆核對，僅供參考）：
- Bernstein 維持 Outperform，目標價由 525 上調至 600。
- Bank of America 維持 Buy，目標價由 450 上調至 500（約 2026-05）。
- Daiwa 由 Buy 降至 Outperform，理由為估值（約 2026-05）。
- Northland 由 Outperform 降至 Market Perform，目標價 260（約 2026-04）。此價位明顯低於現價，屬舊評等。
- Jefferies 上調目標價至 650；JPMorgan 上調至 550 但維持 Neutral（財報後）。Wells Fargo、Cantor Fitzgerald 亦上調目標價（約 2026-07）。
- 整體觀察：分析師一致偏多，但目標價離散度大（365 至 1,250），最高價目標與多數目標價相差甚遠，共識強度應以分布而非平均值解讀。

## Retail social

- **Reddit（r/wallstreetbets、r/stocks）**：DATA_UNAVAILABLE。WebSearch 未找到 2026-10 的 AMD 討論串。唯一找到的 WSB 相關文章為舊期間報導，不採計。
- **StockTwits / X**：
  - StockTwits 相關文章（2026-07 盤前）標題為「Retail Traders Eye $600 Level」，語氣偏多。
  - 2026-08 一篇 StockTwits 導向文章將情緒描述為 Volatile / Bearish-Neutral，聚焦利潤率壓力與出口管制。此文品質偏低，權重低。
  - 一則 StockTwits 投票（未註明日期）顯示 59% 投票者看好 AMD 未來五年表現。
  - X：DATA_UNAVAILABLE。
- **討論量（相對基準）**：DATA_UNAVAILABLE（無可靠量化數據）。搜尋結果中未見 2026-10 出現討論熱度飆升的跡象。
- **散戶語氣**：偏多至中性（資料信心低）。多數近期散戶論述集中在 AI 資料中心需求與 $600 價位，但也存在對估值與財報後賣壓的擔憂。

**主要主題（依出現頻率排序，資料信心低）**
1. AI 資料中心需求：EPYC 與 Instinct 加速器，被視為成長主軸。
2. 價位心理：$600 為常被提及的目標價位，現價較此低約 14%。
3. 估值與財報後反應：財報後曾出現賣壓，市場關注 guidance 是否低於預期。
4. 內部人賣出：散戶媒體偶有提及，但未見主流論述將其解讀為看空訊號。

## Insider activity

資料區間：2026-04-26 至 2026-10-25（近 6 個月）。金額單位為 USD M，由 yfinance 逐筆 Value 加總。

| 內部人 | 職務 | 公開市場賣出（USD M） | 筆數與期間 |
|---|---|---|---|
| Lisa T. Su | 董事長兼 CEO | 168.6 | 4 筆（2026-05-13、06-10、08-18、09-10） |
| Forrest E. Norrod | EVP / 資料中心事業群總經理 | 34.4 | 4 筆（05-20、08-24、09-15、10-15），多為選擇權行使後賣出 |
| Mark D. Papermaster | CTO | 23.9 | 4 筆（06-15、07-15、08-14、08-20） |
| Paul D. Grasby | 業務長（Officer） | 18.6 | 2 筆（05-08、08-17） |
| Jean X. Hu | CFO | 7.1 | 1 筆（08-25） |
| Ava M. Hahn | 總法律顧問 | 1.5 | 2 筆（08-11、08-18） |
| Nora M. Denzel | 董事 | 5.5 | 1 筆（06-02） |
| **合計** | | **約 259.6 賣出，0 買入** | 淨額約 −259.6 |

- 6 個月內無公開市場買入紀錄。上一筆買入為 2025-05-20（Philip Guido，約 USD 1.0M）。
- 期間內的贈與（Stock Gift，無金額）：Su 35,000 股（09-10）、Papermaster 25,052 股（08-19）；未計入金額。
- 部分 2026-08-14 的紀錄未揭露金額（如 Su 396,405 股、Hu 101,698 股），多為授予或稅務扣繳性質，未計入上表，標示為 DATA_UNAVAILABLE。
- 解讀限制：yfinance 未揭露是否為 10b5-1 計畫交易。CEO 與 CTO 的賣出頻率規律，可能屬預先排定計畫，但此項無法從現有資料確認。

## Ownership shifts

| 指標 | 數值 |
|---|---|
| 機構持股比例 | 75.3%（機構家數 5,139） |
| 內部人持股比例 | 0.42% |
| 空單比例（流通股） | 2.42%（39.3M 股）；前月 41.7M，減少約 5.8% |
| Days to cover | 1.83 |

前十大機構（資料日期 2026-06-30，13F 口徑，非即時）：

| 機構 | 持股比例 | 持股變化（季） | 市值（USD B） |
|---|---|---|---|
| BlackRock | 9.21% | +3.3% | 77.7 |
| Vanguard Capital Management | 6.52% | +0.5% | 55.0 |
| State Street | 4.56% | −0.6% | 38.4 |
| Invesco | 3.26% | +5.4% | 27.5 |
| JPMorgan | 2.47% | +66.2% | 20.8 |
| Geode | 2.42% | −0.6% | 20.4 |
| Vanguard Portfolio Management | 2.32% | +0.9% | 19.6 |
| T. Rowe Price | 2.20% | +24.6% | 18.6 |
| FMR | 1.57% | +67.2% | 13.2 |
| Morgan Stanley | 1.49% | +2.1% | 12.6 |

- 前十大合計約 36.0%。多數大型機構季增持，JPMorgan、FMR、T. Rowe 增幅明顯，State Street 與 Geode 小幅減持。
- 整體機構動向偏加碼，但資料為 2026-06-30 季末口徑，距今已有一段時間，需以下一期 13F 驗證。

## Other reference (not sentiment, context only)

- 價位：現價 516.79；52 週區間 188.22 至 658.52（距高點約 −21.5%）；50 日均線 542.3（現價低於均線約 4.7%）；200 日均線 402.1。
- 估值：trailing P/E 131.8，forward P/E 32.8，PEG 0.51（yfinance）。市值約 USD 843.6B。
- 下次財報：yfinance 時間戳約 2026-11-03（非估計旗標），在本報告時點之後，屬於情緒催化事件。

## Net sentiment score

- **分析師（權重高）**：偏多。Strong Buy 與 Buy 合計約 78%，無 Sell，recommendationMean 1.49。信心：高（資料完整）。
- **內部人（權重中）**：偏空。6 個月約 259.6M 賣出、0 買入，集中於 CEO 與高階主管。信心：中（可能含計畫性賣出）。
- **散戶（權重低）**：中性偏多。有 StockTwits 投票與 $600 價位討論，但缺乏 Reddit 與 X 的 2026-10 數據，且 StockTwits 文章偏低品質。信心：低。
- **機構持股變化（權重中）**：偏多。前十大多數季增持，空單比例下降。信心：中（資料為 06-30 口徑）。

**綜合評估：中性偏多**（信心：中低）。分析師與機構流向支持偏多，內部人持續賣出與散戶資料缺口拉低整體信心。

**Divergence flag：是**。分析師一致偏多，但內部人淨賣出規模大（約 260M），方向與分析師相反。散戶資料不足，無法判斷是否與分析師反向；現有 StockTwits 訊號偏多，與分析師方向一致。

SENTIMENT REPORT COMPLETE
