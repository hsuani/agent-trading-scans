# Sentiment — NVDA as of 2026-10-26

資料說明: 分析師評級與內部人、機構持股來自 yf 工具 (live feed 因 Cookie/crumb 失敗, 使用 repo cache)。散戶社群部分 Reddit / StockTwits 在沙箱內無法直接存取, 改用 WebSearch 的二手摘要, 其中多數來自 2026 年 7 月至 9 月, 2026-10 的散戶資料 DATA_UNAVAILABLE。2026-10-26 之後的資料一律視為未知。

## Analyst consensus

單位: 家數 / USD

| 評級 (0m 期間) | 家數 | 占比 |
|---|---|---|
| Strong Buy | 10 | 16.1% |
| Buy | 49 | 79.0% |
| Hold | 2 | 3.2% |
| Sell | 1 | 1.6% |
| Strong Sell | 0 | 0.0% |
| 合計 | 62 | 100% |

整體: 買進系 (Strong Buy + Buy) 59 / 62 = 95.2%, 持有 3.2%, 賣出系 1.6%。yfinance 的 recommendationMean 為 1.29 (1 = Strong Buy), recommendationKey = strong_buy。注意: info 欄位的 numberOfAnalystOpinions 為 58, 與 rec_summary 合計 62 不一致, 推測為不同快照或計算口徑, 不影響方向判讀。

評級趨勢 (rec_summary 四期):

| 期間 | 買進系 | 持有 | 賣出系 | 合計 | 買進系占比 |
|---|---|---|---|---|---|
| 0m (本期) | 59 | 2 | 1 | 62 | 95.2% |
| -1m | 59 | 2 | 1 | 62 | 95.2% |
| -2m | 57 | 2 | 1 | 60 | 95.0% |
| -3m | 58 | 2 | 1 | 61 | 95.1% |

評級分布近四個月幾乎沒有變化, 無明顯上修或下修趨勢。

目標價 (USD):

| 指標 | 數值 | 相對現價 (210.96) |
|---|---|---|
| 平均 (mean) | 328.95 | +56% |
| 中位數 (median) | 315.00 | +49% |
| 最高 | 515.00 | +144% |
| 最低 | 180.00 | -15% |

現價取自 yf info 快照 (currentPrice 210.96), 快照日期 DATA_UNAVAILABLE。52 週區間 164.27 – 243.37。

近期目標價調整 (WebSearch 摘要, 日期多數無法確認): Morgan Stanley 目標價 265 上調至 285 (Buy); KeyBanc 275 上調至 300 (Overweight); Melius 275 上調至 300。以上皆為未確認日期的二手報導。2026-10 當週的評級變動 DATA_UNAVAILABLE。recommendations 指令只回傳彙總家數, 沒有逐家機構的升降評等紀錄, 因此無法列出本期具體 upgrade / downgrade 名單。

## Institutional and insider flow

### 機構持股 (最新 13F 季末 2026-06-30)

機構持股合計 71.4%, 持有機構 7,703 家; 內部人持股 4.0%。

單位: 股數為百萬股 (M), 市值為 USD B。

| 機構 | 持股比例 | 股數 (M) | 市值 (USD B) | 季度變化 (pctChange) |
|---|---|---|---|---|
| BlackRock | 8.06% | 1,941.9 | 409.7 | +0.85% |
| Vanguard Capital Management | 6.39% | 1,540.8 | 325.1 | +0.15% |
| FMR (Fidelity) | 4.26% | 1,026.1 | 216.5 | +3.24% |
| State Street | 4.19% | 1,009.8 | 213.0 | +1.60% |
| Geode Capital | 2.52% | 606.2 | 127.9 | +0.81% |
| Vanguard Portfolio Management | 2.15% | 517.8 | 109.2 | +1.51% |
| JPMorgan Chase | 1.86% | 449.4 | 94.8 | +0.36% |
| T. Rowe Price | 1.53% | 369.8 | 78.0 | -0.07% |
| Morgan Stanley | 1.48% | 356.4 | 75.2 | +3.93% |
| Invesco | 1.37% | 329.6 | 69.5 | +0.64% |

流向判讀: 前十大機構中 9 家季度增持, 僅 T. Rowe 微幅減持 (-0.07%)。FMR 與 Morgan Stanley 增幅最大 (約 +3% 至 +4%)。機構整體方向為淨增持、集中度維持高位, 但增幅本身不大, 屬於穩定累積而非大幅換手。

### 內部人交易 (近 6 個月: 2026-04-26 至 2026-10-26)

單位: USD M (百萬美元)。

| 類別 | 金額 (USD M) | 備註 |
|---|---|---|
| 公開市場買進 | 0 | 區間內無 open-market purchase 紀錄 |
| 公開市場賣出 | 約 1,370.5 | 以 yf 的 Value 欄位加總 |
| 其中: Mark A. Stevens (Director) | 約 1,353.7 | 9/18、9/4、9/2、6/18、6/4 共 5 筆 |
| 其中: Timothy S. Teter (General Counsel) | 約 13.3 | 9/21、8/31 |
| 其中: Stephen C. Neal (Director) | 約 3.3 | 6/3 |
| 其中: John O. Dabiri (Director) | 約 0.1 | 5/27 |
| 淨額 | 約 -1,370.5 | 純賣出 |

Notable:
- Mark A. Stevens (Director): 區間內 5 筆大額賣出, 合計約 USD 1,354M, 最大單筆為 9/2 約 USD 411M (1,848,501 股, 成交價約 USD 220 至 226)。是本區間最主要的賣壓來源。
- Timothy S. Teter (General Counsel): 9/21 約 USD 6.8M, 8/31 約 USD 6.5M, 金額小, 但持續賣出。
- Colette M. Kress (CFO): 區間內 DATA_UNAVAILABLE 於交易紀錄。feed 最後一筆為 2026-03-20 (不在區間內), 因此 6 個月內 CFO 無賣出紀錄。
- Jen-Hsun Huang (CEO): 區間內僅有 6/16 一筆 400,000 股 gift (無現金價值)。feed 中 2025-10 之後無 CEO 公開市場賣出紀錄。2026-03-18 有一筆 58.96M 股 gift, 不在區間內。
- 非現金交易 (不計入淨額): 董事與高管的 RSU / 股票獎勵 (例如 2026-06-25 多位董事各 1,211 股, 2026-09-09 Nicholas P. Parker 約 17 萬股), 以及 Coxe 的 500,000 股 gift (7/1、8/5、9/2 各一筆)。
- feed 未標示交易是否屬於 10b5-1 預定計畫, 無法判斷賣出動機。

## Retail social

- Reddit (r/wallstreetbets, r/stocks): 直接 JSON 抓取在沙箱內被擋, 改用 WebSearch 摘要。2026-09 的 WSB 熱門文 "Nvidia earnings proved 2 things again…" 約 1,083 upvotes, 語氣偏多。2026-10 的 Reddit 帖文樣本 DATA_UNAVAILABLE。
- StockTwits: 沙箱限制, 未取得資料, DATA_UNAVAILABLE。
- X / 新聞輿情 (WebSearch 二手): 
  - 某情緒追蹤器 NVDA 分數 76/100 (Bullish), 2026-01 至 06 月各月介於 74 至 77 之間 (NLP 彙整 Reddit、StockTwits 等論壇, 非純 WSB 指標)。
  - 2026-07 Vanda Research 顯示過去五日 NVDA 散戶淨流入約 USD 706M。
  - 2026-08-11 某社群統計 bullish 占比 70%, 樣本小且未經驗證。
  - 2026-08 期權流向顯示多空大致平衡, 略偏 call。
  - 排除: 一則標題為 "Sentiment in Nvidia Turns Negative, Down to 41/100" 的報導, 其內容指向 2025-10, 不是 2026-10 的資料, 不採用。
- 聲量 (buzz volume): 無可靠的提及次數資料。Reddit 與 StockTwits 的量化數字 DATA_UNAVAILABLE, 只能定性判斷為 2026-09 財報後曾出現高聲量, 2026-10 的聲量 DATA_UNAVAILABLE。

### 主要主題 (Themes)

1. AI 資料中心需求與財報動能: 多數多頭論述集中於營收成長與 AI 基建需求, WebSearch 摘要提到下季營收指引約 USD 91.0B, 前一季約 USD 81.6B (日期與來源未經 filings 核對)。
2. 估值爭議: 本益比 trailing 約 26.7x, forward 約 13.3x, 散戶與部分分析師以 forward 估值為核心論點。
3. 中國出口管制與晶片出貨: 分析師與散戶都提到中國出貨重啟可能是催化劑, 也是下行風險來源。
4. 內部人賣出: 散戶社群會把董事大額減持當作獲利了結的訊號, 但未形成主流論述 (DATA_UNAVAILABLE 於具體帖文)。

Representative takes (摘要, 未逐字轉錄): 散戶多數語氣是 "財報再次證明 AI 需求仍強" 類型的看多論述; 反方則集中於估值與董事大額減持。

## Net sentiment score

綜合判斷: **偏多 (Bullish), 信心中等**。

- 分析師面: 偏多, 信心高 (95% 買進系, 評級四個月穩定, 中位目標價較現價高約 49%)。
- 機構面: 偏多, 信心中 (前十大機構 9 家季度增持, 持股比例高)。
- 內部人面: 偏空, 信心中高 (6 個月約 USD 1.37B 純賣出, 集中於董事 Stevens; 無公開市場買進; CEO 區間內無公開市場賣出)。注意: 董事大額賣出常見於分散持股或既定計畫, 不必然代表看空公司基本面。
- 散戶面: 偏多, 信心低 (可用資料多為 2026-07 至 09 的二手摘要, 2026-10 資料 DATA_UNAVAILABLE)。

Divergence flag: **部分是 (內部人與分析師方向相反)**。
- 散戶 vs 分析師: 兩者同向偏多, 無散戶與分析師相反的分歧。
- 內部人 vs 分析師: 方向相反。分析師 95% 買進且中位目標價約高於現價 49%, 但區間內董事大額賣出約 USD 1.37B, 值得留意。
- 機構 vs 內部人: 方向相反。機構季度增持, 內部人淨賣出。

資料缺口 (DATA_UNAVAILABLE):
- 2026-10 當週的分析師評級與目標價個別變動 (無 firm-level 紀錄)。
- Reddit、StockTwits 的 2026-10 帖文量與情緒分數。
- 現價快照日期 (yf info 的 currentPrice 來源時間戳)。
- 內部人交易的計畫類型 (是否為 10b5-1)。

SENTIMENT REPORT COMPLETE
