# Sentiment — LITE as of 2026-10-28

資料限制總覽：Reddit (r/wallstreetbets, r/stocks) 以 WebFetch 讀取皆被拒絕（無法連線），StockTwits API 解析失敗（DNS 錯誤），零售端只能靠 WebSearch 與第三方情緒追蹤站推估，信心偏低。yf 工具的 cookie/crumb 取得失敗，部分呼叫遇到 query1.finance.yahoo.com 連線被 proxy 拒絕，但仍回傳資料，建議確認是否來自快取。

## Analyst consensus

目前 (0m) 共 28 位分析師：Strong Buy 5 / Buy 18 / Hold 5 / Sell 0 / Strong Sell 0。
BUY 比例 (Strong Buy + Buy) = 23 / 28 = **82%**，HOLD 18%，SELL 0%。

近四個月趨勢（yf rec_summary）：

| 期間 | Strong Buy + Buy | Hold | Sell | 合計 | BUY % |
|---|---|---|---|---|---|
| 0m (本期) | 23 | 5 | 0 | 28 | 82% |
| -1m | 23 | 4 | 0 | 27 | 85% |
| -2m | 22 | 4 | 0 | 26 | 85% |
| -3m | 21 | 4 | 0 | 25 | 84% |

解讀：買進家數略增（21→23），Hold 本期多一家，共識仍偏多，沒有賣出評等。

近期評等動作（yf `recommendations` 子指令只回傳與 rec_summary 相同的月度計數表，沒有逐筆升降評事件，以下來自 WebSearch 彙整，需與原始來源核對）：

- Barclays (Tom O'Malley)：2026-07-20 由 Equal Weight 升至 Overweight，目標價 $1,000。另有來源仍記為 Equalweight，評等有衝突。
- TD Cowen：Hold，目標價由 $800 調至 $820（來源為 Webull 二手摘要）。
- Needham：2026-06-09 目標價升至 $1,040。
- Stifel：目標價 $1,100。Wolfe Research：Buy，目標價 $1,200。Rosenblatt：高點 $1,300。
- B. Riley：2026-02 升至 Buy。Bank of America：2026-02 調為 Neutral，目標價 $520。
- 目標價共識：MarketBeat 約 $1,013，Benzinga 8 月快照約 $830，來源與日期不一。TIKR 文中 median target 約 $4,260 明顯為異常值，本報告不採用。
- 2026-10 月份無可查到的新評等動作，最新一筆為 7 月的 Barclays 升評。

## Retail social

- **Reddit**：無法讀取 r/wallstreetbets 與 r/stocks 的搜尋結果（403/連線拒絕），且 WebSearch 找不到 LITE 相關的近期討論串。此部分缺資料，無法給出 Reddit 語氣判斷。
- **StockTwits / X**：StockTwits API 無法解析（DNS 失敗），無 bullish/bearish 標籤比例。X 端無可用抓取結果。
- **第三方情緒追蹤**：
  - SentiSense：30 日情緒為「微偏多但降溫」（截至 2026-08-09），提及量約 15 則/日，屬低量。
  - LunarCrush：有 LITE 社群追蹤頁面（涵蓋 X、Reddit、YouTube、TikTok），但頁面未顯示情緒數值。
  - 選擇權流向（2026-08 末快照）：偏多但信心中等，偏多傾向不強。
- **聲量**：依 SentiSense 估計約 15 則/日，相對 NVDA、AVGO 等大型 AI 標的屬低聲量（定性判斷，無法精確比對歷史基準）。
- **零售語氣**：整體偏多但降溫，支撐來自「AI 光學需求」敘事；近期（10/13 前後）板塊性拋售與高空頭部位，使情緒轉為謹慎。來源多為聚合站，數字需保留誤差。

主要主題（依新聞與追蹤站歸納，非原始貼文）：

1. **AI 光學需求**：TIKR（10/9）報導 CEO 表示 AI 光學元件產能至 2029 年已售罄，為多方核心敘事。
2. **板塊拋售與波動**：TIKR（10/13）報導股價單日近 -10%，光學類股同步下跌；Tickzen（10/20）顯示股價約 $822.51，高空頭部位被標示為可能的戰場。
3. **估值壓力**：8 月來源指出約 11.4 倍 P/S，屬偏高，有人質疑。
4. **內部人減持**：多份內容將內部人賣股視為「小幅壓力」，而非基本面警訊。
5. **AI 硬體連動風險**：8 月的一則 Anthropic 與 WSJ 相關報導拖累 AI 硬體與光學股，顯示 LITE 與 AI 資本支出敘事高度連動。

代表性散戶觀點（無原始貼文可引，僅以新聞標題性質歸納）：
- 多方：「AI 光學產能售罄」類敘事。
- 空方：「估值偏高、短線波動大」類敘事。

## Insider activity

6 個月窗口 (2026-04-28 至 2026-10-28)，以 yf `insider` 資料計算（金額為 USD，原始 Value 欄位為美元基礎單位，已逐筆核對 807 股 × $945 ≈ $0.76M）：

- **公開市場賣出 (Sale)**：28 筆，合計約 **$101.4M**。
- **公開市場買入 (Purchase)**：0 筆。
- **股票獎勵 (Award / Grant)**：21 筆，屬於薪酬發放，不計入買賣淨額。

| 內部人 | 職位 | 窗口內賣出筆數 | 賣出金額 (USD M) |
|---|---|---|---|
| RETORT VINCENT D | Officer | 4 | 40.95 |
| KIM JAE | General Counsel（部分紀錄為 CFO，資料不一致） | 5 | 16.24 |
| WUPEN YUEN | Officer | 10 | 14.10 |
| LILLIE BRIAN J | Director | 2 | 11.78 |
| SMALL IAN SEYMOUR | Director | 2 | 7.49 |
| HARRIS ISAAC HOSOJIRO | Officer and Director | 2 | 4.86 |
| FLETCHER PAMELA | Director | 1 | 3.07 |
| ALI WAJID | CFO | 1 | 2.37 |
| HURLSTON MICHAEL E. | CEO | 1 | 0.53 |
| **合計** | | **28** | **約 101.4** |

重點：
- 最大單筆：RETORT VINCENT D 於 2026-08-25 賣出 38,663 股，約 $32.96M（均價約 $842–860）。
- CEO HURLSTON 僅於 2026-08-27 賣出 548 股（約 $0.53M），金額極小，主要為獎勵股的部分處分。
- 2026-08-17 與 2026-08-25 有大量 Award 紀錄（如 HURLSTON 66,764 股、RETORT 63,956 股），屬年度薪酬發放，非公開市場買入。
- 整體方向：**淨賣出，無買入**。賣出價格區間約 $824–$1,004，與股價大幅上漲相符，屬獲利了結型態（歷史上 2025-11 至 2026-02 亦有賣出）。
- 窗口最後一筆為 2026-09-29，10 月份無可查到的 Form 4 紀錄（可能為資料延遲，需確認）。

## Ownership shifts

- 機構持股比例：94.19%（流通股為 94.48%），機構家數 1,872。
- 內部人持股比例：0.31%。
- 本工具僅提供單一時點快照，無法判斷機構集中度的變化方向。若需趨勢，需取 13F 歷史資料。
- 結論：機構持股極高，屬高度機構化持有，但無法判定近期淨增減。

## Net sentiment score

- **分析師**：偏多（BUY 82%，零賣出，目標價多數高於最近股價）。
- **內部人**：偏空（6 個月淨賣出約 $101.4M，零買入）。
- **零售**：中性偏多但降溫（SentiSense 微偏多，聲量低，Reddit/StockTwits 缺資料）。

**綜合：中性偏多（信心：中低）**。分析師共識強、機構持股高，但內部人持續出售且零售資料不完整，無法把握方向性。

**背離旗標：部分背離 (是)**。
- 內部人淨賣出與分析師 82% BUY 方向相反，這是本報告最主要的背離訊號。
- 零售端（微偏多）與分析師（偏多）方向一致，未出現零售與分析師相反的情況。
- 若零售端 Reddit/StockTwits 能補齊，需重新評估是否背離。

## Data notes

1. Reddit、StockTwits 無法取得，零售情緒僅依 WebSearch 與第三方追蹤站，信心受限。
2. 目標價與股價的來源不一致（例如 Tickzen 10/20 的 $822.51 與 TIKR 10/13 的 ~$995，差距約 17%），需以即時報價核對。
3. KIM JAE 職稱在 yf 紀錄中同時出現 General Counsel 與 CFO，本報告以 General Counsel 列示，需核對 SEC Form 4。
4. 窗口內 Sale 的 Value 為 yf 提供的 USD 金額，總計 $101.4M，已自行加總驗證。
5. 無 Reddit、StockTwits 原始貼文，因此不引用任何散戶貼文原文。

SENTIMENT REPORT COMPLETE
