# Sentiment — FCX as of 2026-10-23

資料品質備註：本次 Reddit（r/wallstreetbets、r/stocks）WebFetch 皆失敗（reddit.com 無法存取），StockTwits 依任務規定未以 WebFetch 抓取金融頁面。零售情緒僅能靠 WebSearch 聚合頁的快照，且多數快照日期落在 2026 年 8 月或更早，時效性不足。analyst 與 insider 數據來自 yf 工具，為目前可取得的最新資料。

## Analyst consensus

目前 23 位分析師評等：6 Strong Buy / 12 Buy / 4 Hold / 1 Sell / 0 Strong Sell。
Buy 合計 18 / 23 = **78.3%**，Hold 17.4%，Sell 4.3%。

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | Buy 占比 |
|---|---|---|---|---|---|---|
| 目前 (0m) | 6 | 12 | 4 | 1 | 0 | 78.3% |
| -1m | 6 | 12 | 4 | 1 | 0 | 78.3% |
| -2m | 6 | 12 | 4 | 1 | 0 | 78.3% |
| -3m | 6 | 13 | 3 | 1 | 0 | 82.6% |

近期動向：過去約三個月 Buy 家數由 19 降為 18，Hold 由 3 增為 4，屬小幅降溫；工具只提供評等計數，無個別升降評等明細。

網路補充（非工具資料，日期偏舊，僅供參考）：
- Morgan Stanley 2026 年 4 月降評為 Equalweight，目標價後調至 $70（StreetInsider）。
- Barclays 2026 年 7 月 27 日維持 Buy，目標價 $80–82；Wells Fargo 7 月 24 日將目標價由 $68 調至 $70；RBC 將目標價由 $70 調至 $73 但維持 Sector Perform（stockanalysis.com）。
- Investing.com 彙整 22 位分析師，平均 12 個月目標價 $71.73 USD，區間 $30–$82 USD。
- 2026 年 10 月內未找到新的評等變動紀錄，無法確認 10 月是否有調整。

## Retail social

- Reddit：WebFetch 兩個子版皆失敗（無法存取 reddit.com），無樣本可引用。WebSearch 也未找到 FCX 相關 wallstreetbets 或 stocks 討論串。判定：本項無資料。
- StockTwits：依任務規定未抓取（金融頁面禁止 WebFetch），無資料。
- X / 新聞聚合（WebSearch）：
  - SentiSense 頁面（日期 2026-08-09）：30 日情緒分數 5，屬小幅偏多，且較一個月前降溫。提及來源中新聞佔 81%，Reddit 佔 7%。
  - historicaloptiondata 頁面（2026-08-24）引述 X 使用者：「copper supercycle」論述，近期目標 $85；另一則警告若股價在 $85 下方停滯，可能轉弱。
  - 2026-01-29 選擇權快照：97% 成交金額為 call，偏多但當時 RSI 顯示超買。
- 聲量（定性）：新聞驅動為主，社群原生討論佔比低，整體聲量屬「中低」，無法與歷史基準做量化比較。
- 主要主題（依聚合頁面推論）：
  1. 銅供需與「超級週期」敘事（偏多）。
  2. 目標價 $80–85 附近的阻力與追價風險（中性偏謹慎）。
  3. 關稅、全球庫存與供應面疑慮（偏空，作為風險提示）。
  4. 2026 年 Grasberg 礦場事故造成的 2026 年銅產量指引下修（歷史事件，仍被提及）。

## Insider activity

Net 6mo（2026-04-23 至 2026-10-23）：**$0 買入 / 約 $8.39M 賣出**（USD M）。
排除項目：董事年度股票獎勵（約 $20–34K USD / 人，屬例行授予）、贈與（Adkerson 贈與股份，非市場交易）、選擇權行使（Currault 行使 $1.20M，為行使而非賣出）。

| 日期 | 姓名 | 職稱 | 交易 | 股數 | 金額 (USD M) |
|---|---|---|---|---|---|
| 2026-08-25 | Currault, Douglas Nicholas II | General Counsel | 賣出 @ $78.56 | 80,000 | 6.28 |
| 2026-08-05 | Higgins, Stephen T | Officer | 賣出 @ $69.50 | 14,277 | 0.99 |
| 2026-07-30 | Higgins, Stephen T | Officer | 賣出 @ $63.00 | 7,550 | 0.48 |
| 2026-08-27 | Kennard, Lydia H | Director | 賣出 @ $79.11 | 3,798 | 0.30 |
| 2026-08-05 | Mikes, Ellie L. | Officer | 賣出 @ $70.00 | 4,773 | 0.33 |

Notable：
- 最大單筆為 General Counsel Currault 於 8 月出售 80,000 股（約 $6.3M USD），同時伴隨選擇權行使，屬具規模的內部人士減持。
- CEO（Kathleen Quirk）與 CFO（Maree Robertson）於此 6 個月內無公開市場賣出紀錄（CFO 最近一次賣出為 2026-02-13，超出窗口）；CEO 僅有 2026-02-09 授予股票。
- 2026-02 至 2026-03 另有 Adkerson（Chairman）約 $25.5M USD 賣出，但已超出 6 個月窗口，僅作背景。
- 內部人士未有任何公開市場買入紀錄。

## Ownership shifts

- 機構持股：89.6%（institutionsFloatPercentHeld 90.2%），機構數 2,544。
- 內部人持股：0.72%。
- 趨勢方向：工具僅提供單一快照，無時間序列，**無法判定機構淨流入或淨流出方向**，此項標記為資料不足。

## Net sentiment score

Composite：**偏多（bullish），信心低至中**。

- 分析師面：偏多（78.3% Buy），但近三個月 Buy 占比小幅下滑，信心中高。
- 零售面：輕度偏多但資料過時（最新 2026-08 快照），Reddit 與 StockTwits 無資料，信心低。
- 內部人面：偏空傾向（6 個月約 $8.4M USD 賣出、零買入），但多數為 2026 年 8 月的集中減持，且包含部分選擇權相關交易，解讀需保守。
- 機構面：持股比例高，流向無法判定。

Divergence flag：**是（部分）**。零售（偏多但低信心）與分析師（偏多）同向；但內部人士的淨賣出與分析師及零售偏多方向相反，屬值得留意的分歧訊號。

價格參考：2026-10-01 董事股票授予價為 $70.00 USD；2026-08 內部人售價約 $69–79 USD；聚合網頁顯示的 $63 與 $67 快照日期不明，無法確認當前股價。

## 來源

- yf 工具：recommendations、rec_summary、insider、major_holders（2026-10-23 執行）。
- WebSearch 聚合：Barchart、Benzinga、Yahoo Finance、SentiSense（app.sentisense.ai/stocks/FCX/sentiment）、historicaloptiondata.com、StreetInsider、Investing.com、stockanalysis.com、TipRanks。

SENTIMENT REPORT COMPLETE
