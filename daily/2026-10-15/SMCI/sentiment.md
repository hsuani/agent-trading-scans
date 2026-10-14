# Sentiment — SMCI as of 2026-10-15

> 資料時點注意：本機系統日期為 2026-10-14，本報告依任務要求標示為 2026-10-15。分析師與內部人資料取自 repo 快取的最新快照（rec_summary 標示 0m），未能確認 10-15 當日盤後才公布的變動。

## Analyst consensus

目前 18 位分析師：Strong Buy 2 / Buy 2 / Hold 11 / Sell 2 / Strong Sell 1，即 **4 買 / 11 持有 / 3 賣**（買方占比約 22%，持有約 61%，賣方約 17%）。

- 近一個月變化：Buy 由 3 降為 2，總家數由 19 降為 18，其餘評等不變。
- 三個月視窗：Buy 自 -3m 起由 5 降至 4，Hold 維持 11，Sell 維持 3，整體沒有明顯轉向。
- 以 1-5 分加權（Strong Buy=5 至 Strong Sell=1）計算平均分約 3.11，前一月約 3.16，略有下滑但幅度小。
- 個別券商升降評等：DATA_UNAVAILABLE（yf 工具只回傳彙總分布，不含逐家事件）。
- 目標價變動：DATA_UNAVAILABLE（本次工具輸出未包含 target price 欄位）。
- 外部補充（WebSearch，Barchart 2026-08 報導，原文未附連結）：20 位分析師，共識為 Hold，分布為 3 Strong Buy / 2 Moderate Buy / 12 Hold / 1 Moderate Sell / 2 Strong Sell。與 yf 快照家數不同，屬不同時點與來源差異，以 yf 為主。

## Retail social

- **Reddit**：直接抓取 Reddit JSON 在本沙箱被封鎖，改以 WebSearch 代替。
  - 未找到 2026-10 的 r/wallstreetbets 相關討論串。
  - 唯一近期條目是 r/SMCIDiscussion 鏡像站上一則約 23 小時前的貼文（單一匿名用戶），偏空，主張股價跌回 30 元區間，並宣稱過去 12 個月內部人出脫 2,000 萬美元。該說法無法由 yf 內部人資料完全印證（見下節，同期公開市場賣出約 1,120 萬美元），屬單一意見，不代表整體情緒。
  - 其餘搜尋結果多為無日期、無具體貼文引用的 SEO 文章，可信度低，只能作為「有討論、偏分歧」的粗略參考。
  - 整體傾向：**無法可靠判定，資料不足**。
- **StockTwits**：本次未取得資料（DATA_UNAVAILABLE）。
- **X / 新聞聲量**：
  - SentiSense（截至 2026-08-09）：30 日情緒分數 10.75，評為略偏多，新聞偏正面，Reddit 與 X 多為中性。
  - Schaeffer's（2026-05-21）：大量買入 put 被視為反向指標，歷史上該訊號後一個月股價下跌比例約 71%，平均跌幅約 15.1%。
  - TipRanks（時間不詳）：文章標題描述股價回檔後的投資人情緒，內文未能完整擷取。
- **聲量（buzz volume）**：DATA_UNAVAILABLE（無量化提及數）。定性判斷為中低水準，且無法確認與歷史均值的比較。

**主要主題（Themes）**

- 多方：AI 伺服器需求強勁、台灣／馬來西亞／荷蘭產能擴張、EPS 優於預期（一則 2026-06 摘要）。
- 空方：會計與內控疑慮、營收成長放緩、利潤率未擴張、客戶集中度、估值偏高，以及內部人持續減持。
- 股價背景：Barchart 2026-08 報導指出 52 週跌幅約 49.4%，同期 S&P 500 約上漲 21.8%。

## Insider activity

視窗：2026-04-15 至 2026-10-15（6 個月）。

**公開市場交易（已確認 Sale 類型）**

- 2026-09-04：CEO Charles Liang（LIANG CHARLES）與其關聯 10% 以上持股人 LIU LIANG CHIU-CHU SARA 申報同一筆交易，賣出 200,000 股，價格區間 36.60–40.00 美元，金額約 **771.9 萬美元**（同一筆交易在兩個申報人下各出現一次，此處只計一次）。
- 買入：6 個月內未見公開市場買入紀錄。

**非公開市場或無金額紀錄（未計入）**

- 2026-05-26：CEO 與關聯 10% 持股人各申報 340,000 股 Stock Gift（價格 0，屬贈與）。
- 2026-05-08、06-17、06-30、07-01、08-10、08-17：多位高管與董事有小額股數申報，feed 中無價格與金額，多半屬於既定配股、稅務預扣或其他非市場交易，性質未經確認，**未計入淨額**。

**淨額**

- 6 個月淨額：買入 $0，賣出約 $7.7M，**淨賣出約 $7.7M**。
- 參考對照（過去 12 個月，2025-10-15 起，公開市場 Sale）：Kao George W（2025-11-24，約 187 萬美元）、Tuan Sherman 董事（2025-11-26，約 160 萬美元）、CEO 關聯方（2026-09-04，約 772 萬美元）。合計約 **1,120 萬美元**，與 Reddit 貼文所述 2,000 萬美元有差距，可能是 feed 不完整或計算口徑不同，無法確認。
- 歷史脈絡：CEO 關聯 10% 持股人在 2025 年 5 至 7 月曾分批以 45 至 60 美元賣出（2025-06-18 約 1,350 萬美元，2025-07-28 約 1,200 萬美元）。2026-09 的賣價區間明顯較低。

**主要人物**

- CEO Charles Liang 與關聯 10% 持股人（LIU LIANG CHIU-CHU SARA）：為最大賣方，2026-09 一筆大額賣出。
- 其他高管（CFO David Weigand、George Kao、Sherman Tuan 等）：近期以小額申報為主，2025 年底有賣出紀錄。

## Ownership shifts

截至 2026-06-30（13F 季度申報）：

- 內部人持股 12.66%，機構持股 69.57%（流通股口徑約 79.65%），機構家數 1,110。
- 前十大機構：
  - BlackRock 7.26%（47.69M 股，股數較前季 +9.98%）
  - Vanguard Capital Management 5.53%（+10.5%）
  - Vanguard Portfolio Management 5.00%（+11.1%）
  - Jane Street 4.38%（股數大幅增加，約 +551%）
  - State Street 3.75%（+11.9%）
  - UBS 3.00%（+63.1%）
  - Geode 2.36%（+9.6%）
  - Invesco 1.78%（-0.8%，小幅減持）
  - Goldman Sachs 1.69%（+222%）
  - Two Sigma 1.49%（+979%）
- 趨勢判讀：前十大機構多數於最近一季增持，並無集中撤出跡象。注意 Q2 申報有 45 天延遲，與 10-15 當下的實際持倉可能有落差。

## Net sentiment score

- **分析師**：中性偏空（Hold 為主，平均分約 3.1／5，買賣家數比 4:3，且近月 Buy 微降）。信心：中。
- **散戶**：無法可靠判定。Reddit 與 StockTwits 資料不足，X／新聞側則偏分歧（SentiSense 2026-08 偏多，Schaeffer's 2026-05 偏空反向訊號）。信心：低。
- **內部人**：偏空（6 個月淨賣出約 770 萬美元，無公開市場買入，賣出者為 CEO 關聯方）。信心：中（金額已由 feed 確認，但 feed 完整性未知）。
- **機構**：偏多（前十大多數增持）。信心：中。
- **綜合**：**中性偏空**（信心：低至中）。分析師與內部人方向一致偏保守，機構面相對正面，散戶面資料不足，無法作為獨立佐證。

**背離旗標（Divergence flag）**：**無法判定**。散戶傾向資料不足，無法確認是否與分析師方向相反。但存在內部背離：機構持續增持，與 CEO 關聯方減持方向相反，值得後續追蹤。

**資料缺口**
- 個別券商升降評等與目標價：DATA_UNAVAILABLE
- StockTwits 資料：DATA_UNAVAILABLE
- Reddit 聲量與逐篇貼文：無法直接抓取，僅能以 WebSearch 取得零星結果
- 當前股價：本次未取得，無法換算目前賣價相對區間的位置

## 指標表（Structured metrics）

| 指標 | 數值 | 備註 |
|---|---|---|
| 分析師家數 | 18 | yf rec_summary 0m |
| 買方（Strong Buy + Buy） | 4（22%） | |
| 持有（Hold） | 11（61%） | |
| 賣方（Sell + Strong Sell） | 3（17%） | |
| 分析師加權平均分（1-5） | 約 3.11 | 前一月約 3.16 |
| 近一月 Buy 家數變化 | -1（3 → 2） | |
| 個別評等升降 | DATA_UNAVAILABLE | |
| 目標價變動 | DATA_UNAVAILABLE | |
| Reddit 聲量 | DATA_UNAVAILABLE（定性：中低） | |
| Reddit 傾向 | 無法判定 | 資料不足 |
| StockTwits 情緒 | DATA_UNAVAILABLE | |
| SentiSense 情緒分數（2026-08-09） | 10.75（略偏多） | 外部資料，時點較舊 |
| 內部人 6 個月公開市場買入 | $0 | |
| 內部人 6 個月公開市場賣出 | 約 $7.72M | 2026-09-04，CEO 關聯方，200,000 股 |
| 內部人 6 個月淨額 | 約 -$7.72M | |
| 內部人 12 個月公開市場賣出 | 約 $11.2M | 與 Reddit 所稱 $20M 不符 |
| 內部人持股比例 | 12.66% | |
| 機構持股比例 | 69.57% | 2026-06-30 |
| 機構家數 | 1,110 | |
| 前十大機構本季多數增持 | 是（9 家增持，Invesco 微減） | |
| 綜合情緒 | 中性偏空 | 信心：低至中 |
| 背離旗標 | 無法判定 | 內部背離：機構增持 vs 內部人減持 |

## 來源

- SentiSense SMCI 情緒頁：https://app.sentisense.ai/stocks/SMCI/sentiment
- Schaeffer's 情緒分析（2026-05-21）：https://www.schaeffersresearch.com/content/analysis/2026/05/21/sentiment-signal-doesnt-look-good-for-smci
- TipRanks 情緒文章：https://www.tipranks.com/news/smci-stock-heres-what-investor-sentiment-signals-after-recent-pullback
- r/SMCIDiscussion 鏡像站（單一貼文，低可信度）：https://redlib.groet-infra.nl/r/SMCIDiscussion/top
- Barchart 分析師共識（2026-08）：來源未附連結，僅作補充
- yf 工具：`pipeline/tools/yf.py SMCI recommendations / rec_summary / insider / major_holders / inst_holders`（repo 快取）

SENTIMENT REPORT COMPLETE
