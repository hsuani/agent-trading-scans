# Sentiment — RGTI (Rigetti Computing) as of 2026-10-15

資料狀態：Reddit 與 StockTwits 在本沙箱無法存取（Reddit 回傳 "unable to fetch"，StockTwits 回傳 ENOTFOUND），依規定記為 DATA_UNAVAILABLE。WebSearch 找不到 2026 年 10 月的散戶討論。分析師與內部人資料來自 yf 工具（cache 來源，屬正常回退）。分析師歷史評等資料的計數在三個月內完全不變，這可能是 cache 快照的特性，而不一定代表真實的評等停滯，請謹慎解讀。

## Analyst consensus

目前 13 位分析師：1 Strong Buy / 8 Buy / 4 Hold / 0 Sell / 0 Strong Sell，即 9 買進、4 持有、0 賣出（yf `rec_summary`，期間 0m）。

- 近三個月（-1m、-2m）計數與目前完全相同，yf 歷史評等資料中沒有可見的升評或降評紀錄。
- 本次 yf 工具未回傳目標價，目標價變動無法確認。
- 來源不一致：WebSearch 轉引的 Google Finance 快照（2026 年 8 月）為 6 Buy / 3 Hold / 0 Sell，目標價區間 $20–$40。與 yf 的 9 / 4 / 0 相比，分析師樣本數與日期不同，無法直接對齊。
- 較舊的線索：late 2025 年 B. Riley 由 Buy 降為 Neutral，目標價 $42（來源為 Barchart 系列文章，已過時，不代表目前評等）。

結論：分析師整體偏多（多數為 Buy），但評等結構過去三個月幾乎沒有動能變化。

## Retail social

- Reddit（r/wallstreetbets、r/stocks）：DATA_UNAVAILABLE。本次無法取得貼文樣本、分數或留言語氣。WebSearch 也找不到 RGTI 的 WSB 討論串。
- StockTwits：DATA_UNAVAILABLE（DNS 解析失敗）。
- X / 新聞散戶語氣（WebSearch）：
  - SentiSense 評分（資料時點 2026-08-09）：30 日情緒為略偏多但降溫，分數 5.68；當日回落至中性，低於 30 日均值。新聞通道最偏多，Reddit 與 YouTube 為中性。（[SentiSense](https://app.sentisense.ai/stocks/RGTI/sentiment)）
  - 中文財經媒體（itiger 異動解讀系列）多為「盤中大漲」型的行情描述，並將漲幅歸因於量子運算概念，時間戳記不明，僅能作為題材熱度的旁證。（[itiger](https://www.itiger.com/news/1119798752)）
  - 2026 年 5 月 Schwab 影片描述量子股的大幅上漲為投資人搶先布局的題材交易。（[Schwab Network](https://schwabnetwork.com/video/ca-htag-rgti-surges-as-bulls-pile-into-quantum-stocks)）
- 聲量（buzz volume）：無法量化，定性為 DATA_UNAVAILABLE。

- 主要主題（依 WebSearch 結果歸納，時效偏舊）：
  - 量子運算題材與產業敘事，市場以此定價。
  - 聯邦資金與政府合約：TipRanks 提及三年期 AFRL 合約與 $350M 資產負債表增補，屬正面。（[TipRanks](https://www.tipranks.com/stocks/RGTI)）
  - 營收與獲利疑慮：Barchart 文章質疑技術路線圖的進展是否被營收認列的現實所掩蓋；TipRanks 指出某關鍵協議到期拖累營收，且量子優勢仍約四年之遙。（[Barchart](https://www.barchart.com/story/news/3676669/rigetti-s-technology-roadmap-keeps-advancing-but-revenue-recognition-tells-a-different-story)）
  - 2026 年 8 月 Q2 財報前，市場對短期前景分歧，焦點在虧損與技術面是否壓過量子敘事。（[Barchart](https://www.barchart.com/story/news/35924112/dear-rigetti-stock-fans-mark-your-calendars-for-november-10)，注意此文為較舊的財報日曆文章）

- 代表性群眾觀點（僅能引用 WebSearch 摘要，無原始貼文）：「量子題材一來就追」類型的題材交易描述與「營收認列落後路線圖」的質疑並存。

## Insider activity

6 個月窗口：2026-04-15 至 2026-10-15。

Net 6mo：$0 買入（無公開市場買進紀錄），約 $22.6M 賣出（10 筆公開市場 Sale，依 yf 報價金額加總）。

主要紀錄（依日期排序）：

| 日期 | 人員 | 職位 | 交易 | 股數 | 金額（USD） |
|---|---|---|---|---|---|
| 2026-09-09 | KULKARNI SUBODH K | CEO | 賣出 @ $15.68 | 120,000 | 約 $1.88M |
| 2026-09-03 | BERTELSEN JEFFREY A | CFO | 賣出 @ $15.00 | 25,000 | 約 $0.38M |
| 2026-08-20 | RIVAS DAVID | COO（另有記載為 CTO） | 賣出 @ $16.79 | 9,038 | 約 $0.15M |
| 2026-08-20 | BERTELSEN JEFFREY A | CFO | 賣出 @ $16.89 | 3,860 | 約 $0.07M |
| 2026-06-22 | JOHNSON RAY O | 董事 | 賣出 @ $20.55 | 84,944 | 約 $1.75M |
| 2026-06-08 | JOHNSON RAY O | 董事 | 賣出 @ $21.28–21.76 | 122,188 | 約 $2.60M |
| 2026-06-01 | KULKARNI SUBODH K | CEO | 賣出 @ $24.38–26.23 | 104,190 | 約 $2.62M |
| 2026-05-29 | RIVAS DAVID | CTO | 賣出 @ $25.40 | 499,328 | 約 $12.68M |
| 2026-05-22 | RIVAS DAVID | CTO | 賣出 @ $22.95–25.63 | 18,759 | 約 $0.43M |
| 2026-05-22 | BERTELSEN JEFFREY A | CFO | 賣出 @ $22.94–25.63 | 3,682 | 約 $0.08M |

其他非買賣紀錄：
- 2026-09-09 CEO 與 2026-09-03 CFO 各有選擇權行權（derivative conversion）紀錄，行權後隨即賣出，不屬於買進。
- 2026-06-09 四位董事（Johnson、Clifton、Fitzgerald、Iannotti）各獲 9,208 股 Stock Award，為薪酬授予，非市場買進。
- 本窗口內未見任何 CEO / CFO / 董事的公開市場買進。

觀察：
- 賣出金額高度集中於 CTO David Rivas 於 2026-05-29 的 499,328 股（約 $12.7M），單筆即占窗口總額超過一半。
- 股價約在 $20–26 區間（2026 年 5–6 月）出現大量賣出，之後 2026 年 8–9 月 $15–17 區間仍有 CEO / CFO 的賣出。
- 無法判斷這些賣出是否屬於 10b5-1 計畫，yf 資料未提供此欄位。
- 職稱紀錄不一致（David Rivas 於 8 月被標為 COO，其餘紀錄為 CTO），以原始 SEC Form 4 為準。
- 2024 年 11 月的 Bessemer 大量賣出（>10% 持有人）發生在窗口之外，不列入計算。

## Ownership shifts

- 機構持股比例 54.35%（機構持股數 624 家），內部人持股 1.74%。
- 本次僅有單一時點快照，無法判斷機構持股的增減趨勢。
- 內部人持股比例低，且近期持續減持，這點需與機構面持續累積的情況一併看待。

## Net sentiment score

綜合判斷：中性（信心：低到中等）

- 分析師：偏多（9 Buy / 4 Hold / 0 Sell），但評等近三個月無變化，且與 WebSearch 的 8 月快照（6 / 3 / 0）樣本不一致。權重中等，信心中等。
- 內部人：偏空。6 個月約 $22.6M 公開市場賣出，零買進，賣出集中在 CEO、CFO 與 CTO。權重高，信心中高。
- 散戶：無法判定。Reddit 與 StockTwits 不可用，最後一筆可得的散戶讀數為 2026-08-09 的中性（略偏多但降溫）。權重低，信心低。

Divergence flag：無法判定（yes/no 皆無足夠依據）。
- 若以已知的代理指標比較，分析師偏多與內部人大量賣出之間存在明顯背離，這是本次最具資訊量的訊號。
- 散戶與分析師的背離無法確認，因 2026 年 10 月的散戶資料缺失。

本報告僅呈現情緒與資料狀態，不構成交易建議。

SENTIMENT REPORT COMPLETE
