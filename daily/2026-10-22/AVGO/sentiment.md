# Sentiment — AVGO as of 2026-10-22

資料狀態：分析師評等與機構持股為即時或快取資料（prices/yf/AVGO.json，refreshed 2026-10-22）；內部人交易最新一筆為 2026-07-10，8 月至 10 月的 Form 4 未見於資料中，屬資料缺口。Reddit 搜尋無可用結果；StockTwits 最新可驗證讀數為 2026-08-17，10 月的散戶情緒未能確認。

## Analyst consensus

目前 50 位分析師：7 Strong Buy / 40 Buy / 3 Hold / 0 Sell / 0 Strong Sell（買進占比約 94%，無賣出評等）。快取中的 numberOfAnalystOpinions 為 47，與 rec_summary 合計 50 略有差異，以 rec_summary 為準。

近四個月評等分佈（rec_summary 歷史欄位）：

| 期間 | Strong Buy | Buy | Hold | Sell | 買進合計 / 總數 |
|---|---|---|---|---|---|
| 目前 (0m) | 7 | 40 | 3 | 0 | 47 / 50 |
| -1m | 7 | 40 | 3 | 0 | 47 / 50 |
| -2m | 8 | 37 | 4 | 0 | 45 / 49 |
| -3m | 7 | 37 | 4 | 0 | 44 / 48 |

近況：過去三個月 Hold 由 4 降至 3，買進合計由 44 增至 47，呈現小幅偏多的評等漂移。工具未提供逐筆升降評等事件，無法列出個別券商動作。

目標價（快取 info 欄位）：平均 $527.59、最高 $660、最低 $215.88。以現價 $337.8 計算，平均目標價隱含約 56% 上行空間。

網路上可查到的個別券商動作（日期偏舊，均為 9 月前後，非 10 月）：Benzinga 於 9/4 顯示共識 Buy、平均目標 $505；Citigroup 調升至 $515；DA Davidson 調降至 $350 並維持 Neutral；Goldman Sachs 維持 Buy、目標 $525；TD Cowen Buy、目標 $500。

## Retail social

- Reddit: WebSearch 查詢 r/wallstreetbets 與 r/stocks 的 AVGO 討論均未回傳 Reddit 貼文，無法評估近期樣本與多空傾向。依規則 soft-fail，未以 WebFetch 直接抓取。
- StockTwits: 最新可驗證的一則為 2026-08-17，文章指股價下跌 6% 後散戶情緒轉為 bullish，當時交易者押注 9/2 財報前的反彈。另一則較早的文章指 6 月前後情緒連續兩週為 bearish，標題重點為 "Co-Founder's Quarterly Stake Sales Top $720M"（創辦人季度減持超過 $720M）。AltIndex 無日期快照顯示情緒分數 80/100（Bullish）、平均每日提及約 4,639 則，較三個月前下降 27%、追蹤人數約 74,068。
- X / 新聞聲量: 未取得 10 月的可驗證散戶貼文，無法判斷近期聲量與多空比例。以 AltIndex 的相對變化看，提及量呈下降趨勢（定性判斷：中等偏低，較前三個月降溫）。
- Themes（自可查到的文章歸納）:
  1. 創辦人 / 董事 Henry Samueli 的大額減持，是 6 月情緒轉弱的主要原因之一。
  2. 6 月財報後的偏保守指引與獲利了結，被視為股價自高點回落的原因。
  3. 估值偏高（trailing P/E 約 43，forward P/E 約 17.4）與 AI 產品組合對毛利率的影響，是多空辯論焦點。
  4. 9/2 財報後的反彈與逢低買進，顯示散戶仍有承接意願。
  5. 下一次財報為 2026-12-09（快取 earnings_dates），散戶可能將焦點轉向該日。

## Insider activity

Net 6mo（2026-04-22 至 2026-10-22，工具資料僅到 2026-07-10）：賣出約 $283.7M（7 筆），買進約 $0.37M（1 筆），淨賣出約 $283.3M。不含贈與與股票授予。

主要交易：

- Henry Samueli（Director，間接持有）：2026-06-24 以 $377.61–$388.17 賣出 654,241 股，約 $250.0M，為窗口內最大單筆。另有 336,893 股贈與（間接）。
- Mark David Brazeal（Officer）：2026-06-17、06-25、07-08、07-10 合計 4 筆賣出，約 $32.4M（07-10 以 $401.33 賣出 25,000 股，約 $10.0M）。為窗口內最活躍的賣方。
- Gayla J. Delly（Director）：07-08 以 $385.38 賣出 1,890 股，約 $0.73M；07-10 贈與 500 股。
- Justine F. Page（Director）：06-29 以 $373.86 賣出 1,602 股，約 $0.60M。
- Harry L. You（Director）：06-11 以 $373.57 買進 1,000 股，約 $0.37M，為窗口內唯一買進。

CEO / CFO 動向：
- CEO Hock E. Tan：窗口內無公開市場賣出；最近一次賣出為 2025-12 系列，另於 2026-04-08 有 22,000 股贈與。
- CFO：Kirsten M. Spears 最近一次賣出為 2025-12-31；2026-03-02 獲授 110,640 股。窗口內 CFO 職位出現 Amie Thuener O'Toole，2026-06-15 獲授 50,000 股（Stock Award），顯示 CFO 職位可能已交接，工具資料未明示交接時點。

解讀：窗口內以董事與 Brazeal 為主的賣出集中在 6 月至 7 月，股價區間約 $373–$401。現價 $337.8 已低於多數賣出價，賣出時點與股價高點重疊。是否屬 10b5-1 預定計畫，工具資料未揭露，無法判斷。

## Ownership shifts

- 機構持股比例 79.7%（流通股口徑 81.3%），機構數量 6,261；內部人持股 1.9%。
- 13F 截至 2026-06-30 的前幾大持有人：BlackRock 8.34%（+3.2% QoQ）、Vanguard Capital Management 6.48%（+0.4%）、State Street 4.12%（+2.9%）、FMR 3.02%（+16.3%，為前十大中加碼最明顯者）、Vanguard Portfolio Management 2.66%（-1.1%）、Capital World Investors 2.55%（+4.9%）、Geode 2.44%（+1.9%）、Capital Research Global Investors 2.37%（-2.5%）。
- 趨勢定性：前十大持有人以增持為主，FMR 與 Capital World 為明顯加碼方，Vanguard PM 與 Capital Research 小幅減碼。整體偏向機構在股價回落期間承接，但此為 6 月底快照，不反映 7 月以後的變動。

## Net sentiment score

- 分析師（權重高，資料完整）：偏多（bullish），信心高。94% 買進評等、無賣出、近三個月小幅上修；平均目標價隱含約 56% 上行空間。
- 內部人（權重中，資料窗口受限）：偏空（bearish），信心中。6 個月淨賣出約 $283M，主要由董事級別與 Samueli 的大額間接減持構成；CEO / CFO 窗口內無公開市場賣出，削弱偏空解讀的力度。
- 散戶（權重低，資料不足）：偏多但未驗證，信心低。最近可驗證讀數為 8 月 bullish，AltIndex 無日期快照為 bullish，6 月曾短暫 bearish；10 月資料缺失，Reddit 無結果。
- 合成：中性偏多（neutral-to-bullish），信心中低。分析師與機構持股偏多，內部人淨賣出與股價自 $495 高點回落至 $337.8 形成對沖。

Divergence flag: 無法確認（no verified October retail reading）。若以可得資料看，分析師與機構偏多、內部人偏空，散戶 8 月以前偏多；三方不構成明確的「散戶與分析師反向」訊號。若 10 月 StockTwits 或 Reddit 有新資料，應重新評估此旗標。

## 資料缺口與限制

1. 內部人交易資料最新為 2026-07-10，8 月至 10 月 Form 4 未覆蓋，淨賣出金額可能被低估或高估。
2. recommendations 工具僅回傳彙總計數，無逐筆升降評等事件。
3. Reddit 無可用結果；StockTwits 與 X 的 10 月資料缺失。
4. 個別券商目標價多為 9 月前資料，與快取 mean target 的時點不一致。
5. 機構持股為 2026-06-30 快照。

Sources:
- [Stocktwits: AVGO Stock Rebounds After Worst Drop In Two Months](https://stocktwits.com/news-articles/markets/equity/avgo-stock-rebounds-after-worst-drop-in-two-months-retail-traders-look-past-v-mware-worry-bet-on-rebound/cZo6qWHRJKk)
- [Stocktwits: AVGO Stock Heads For Worst Month In 7 Years](https://stocktwits.com/news-articles/markets/equity/avgo-stock-heads-for-worst-month-in-7-years-co-founder-s-quarterly-stake-sales-top-720-m/cZ1QdqrR7iP)
- [AltIndex: AVGO Stocktwits mentions](https://altindex.com/ticker/avgo/stocktwits-mentions)
- [Investing.com: Broadcom consensus estimates](https://uk.investing.com/equities/avago-technologies-consensus-estimates)
- [Benzinga: Broadcom price targets](https://www.benzinga.com/quote/avgo/price-targets)
- [Investing.com: Broadcom sentiment poll](https://ca.investing.com/equities/avago-technologies-scoreboard)

SENTIMENT REPORT COMPLETE
