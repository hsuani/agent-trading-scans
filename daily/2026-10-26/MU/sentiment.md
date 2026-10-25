# Sentiment — MU (Micron Technology) as of 2026-10-26

資料基準: yfinance 快照 (`pipeline/tools/yf.py`) 與 WebSearch。快照的實際抓取時間無法從工具輸出確認, 視為 2026-10-26 前後的最新值。2026-10-26 之後的資料一律視為未知。

## 價格與估值快照 (供對照用)

| 項目 | 數值 | 備註 |
|---|---|---|
| 最新價 (USD) | 877.55 | 前收 856.49, 日漲 +2.7% |
| 市值 (USD B) | 992.9 | 877.55 × 1,131.4M 股 ≈ 992.9B, 單位換算已核對 |
| 企業價值 (USD B) | 954.6 | |
| 52 週高 / 低 (USD) | 1,255.0 / 192.59 | |
| 50 日 / 200 日均價 (USD) | 982.7 / 732.1 | 現價低於 50 日均, 高於 200 日均 |
| trailing P/E / forward P/E | 11.8x / 4.2x | |
| Beta | 2.23 | |

## Analyst consensus

**分布 (rec_summary, 0m 當期):** Strong Buy 9 / Buy 36 / Hold 3 / Sell 0 / Strong Sell 1。合計 49 家。
- Yahoo `info` 的 `numberOfAnalystOpinions` 為 45, 與 rec_summary 的 49 不一致 (可能是計算口徑差異, 未能確認), 本報告以 rec_summary 的分布為準。
- `recommendationKey` = strong_buy, `recommendationMean` = 1.37 (1 = Strong Buy, 5 = Sell)。

**三個月趨勢 (rec_summary):**

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell |
|---|---|---|---|---|---|
| 0m (當期) | 9 | 36 | 3 | 0 | 1 |
| -1m | 9 | 36 | 3 | 0 | 1 |
| -2m | 9 | 35 | 4 | 0 | 0 |
| -3m | 9 | 31 | 5 | 0 | 0 |

買方評級 (Strong Buy + Buy) 由 -3m 的 40 家增至 0m 的 45 家, Hold 由 5 家降至 3 家。Sell 維持 0 家, Strong Sell 於 -1m 之後出現 1 家 (機構名稱: DATA_UNAVAILABLE)。

**目標價 (info, USD):** 平均 1,561.9 / 中位數 1,550 / 最高 3,000 / 最低 361。平均目標較現價高約 78%。目標價區間極寬 (361 至 3,000), 分歧明顯。

**個別券商近期動作:** `recommendations` 工具僅回傳彙總計數, 不含個別券商升降評等, 因此逐家升降評等 = DATA_UNAVAILABLE。WebSearch 找到的零星報導 (日期與可信度未能驗證, 僅供參考):
- Cantor Fitzgerald (C.J. Muse): Overweight, 目標價 2,000 USD。
- Susquehanna: Positive, 目標價 2,000 USD。
- Morgan Stanley: Overweight, 目標價 1,200 USD。
- WebSearch 的共識目標價為 1,581.40 USD, 與 yf 的 1,561.9 略有出入, 以 yf 為準。

**Analyst 小結:** 評等結構強烈偏多 (買方佔 45/49 ≈ 92%, 賣方 1/49), 但這類報告的時點可能落後於近期 10 月的股價回檔。

## Retail social

- **Reddit (r/wallstreetbets, r/stocks, r/MU_Stock):** 依任務指示未直接抓取 Reddit JSON。以 WebSearch 代替, 找不到 2026-10 的個別討論串, 因此 10 月的散戶語氣 = DATA_UNAVAILABLE。
  - 可用的舊資料 (非 10 月, 僅作趨勢參考): 一篇 24/7 Wall St. 報導描述 2026 年 6 月前後 Reddit 與 X 上的情緒「由中度轉為極度看多」, 並提到 r/wallstreetbets 的 MU 熱度飆升。報導中價格與本次快照差距很大 (報導引用 $345 與 $1,035 等不同價位), 時點不一致, 應以舊聞看待。
  - r/MU_Stock 的 GummySearch 頁面顯示約 2.6 萬名成員, 最常見標籤為 discussion、meme、loss、news、dd。貼文資料止於 2026-07 下旬。
  - 一則標題為「480k MU YOLO (240k in margin)」的 wallstreetbets 熱門貼文, 日期未能確認。
- **StockTwits:** DATA_UNAVAILABLE (任務指示禁止直接抓取, 未取得資料)。
- **X / 新聞論述:** 10 月的情緒以媒體敘事為主, 不是散戶貼文。TIKR (10/20 前後) 認為這波回檔是買進機會, 理由是營收指引與獲利預估持續上修, 股價約為 FY2027 預估 EPS 的 5 倍。另一方面, 中國 CXMT 在更高密度 DRAM 的進展是主要被提及的風險。
- **Buzz 量能:** 無可靠的提及次數資料, 相對一般水準的量能判定 = DATA_UNAVAILABLE。

**Themes (依可取得的媒體與舊貼文歸納):**
1. 記憶體供給短缺可能延續至 2028 (Cantor、Susquehanna 的看法)。
2. 中國競爭者 (CXMT) 與 AI 資本支出融資疑慮, 是 10 月回檔的主要敘事。
3. 估值便宜 (forward P/E 僅約 4x) vs. 週期股的風險。
4. 11 月季度毛利率可能暫時下滑 (Susquehanna 看法)。
5. 傳聞中的 12 月 9 日 $35B 庫藏股授權 (Cantor 提及, 日期未驗證)。

**價格資料衝突 (需注意):** 10 月的個別報導數字彼此不一致: TIKR 稱一個月內跌 10.9% (10/7 後); Gotrade 稱 10/15 收 931.24 USD, 盤中曾跌至 858.00; 另一篇報導稱 10 月初至今跌 17%, 盤前約 913。以上數字無法在同一時點同時成立, 以 yf 快照的 877.55 為最新參考值。

## Insider activity

**6 個月窗口: 2026-04-26 至 2026-10-26。** 窗口內的公開市場交易全部為賣出 (Sale), 無公開市場買進 (Purchase)。Stock Gift 與 Stock Award 為零價值交易, 未計入金額。

**淨額: 買進 $0M, 賣出約 $273.4M (USD M)。**

| 日期 | 內部人 | 職稱 | 股數 | 金額 (USD M) |
|---|---|---|---|---|
| 2026-10-16 | Scott J. DeBoer | President | 28,544 | 25.7 |
| 2026-08-21 | Sanjay Mehrotra | CEO & Chairman | 40,000 | 38.8 |
| 2026-08-18 | Sumit Sadana | Senior Advisor / Officer | 15,000 | 14.0 |
| 2026-07-24 | Sanjay Mehrotra | CEO & Chairman | 31,285 + 8,715 | 37.3 |
| 2026-07-23 | Scott R. Allen | CAO | 879 | 0.9 |
| 2026-07-01 | April S. Arnzen | Officer | 40,000 | 43.4 |
| 2026-06-30 | Lynn A. Dugle | Director | 1,300 | 1.5 |
| 2026-06-26 | Sanjay Mehrotra | CEO & Chairman | 28,506 + 11,494 | 46.3 |
| 2026-06-26 | Alexis Bjorlin | Director | 25 (間接持有) | 0.03 |
| 2026-05-29 | Sanjay Mehrotra | CEO & Chairman | 37,439 + 2,561 | 38.5 |
| 2026-05-11 | Steven J. Gomo | Director | 2,000 | 1.6 |
| 2026-05-01 | Sanjay Mehrotra | CEO & Chairman | 40,000 | 21.5 |
| 2026-05-01 | Michael C. Ray | Officer | 7,601 | 4.1 |

- CEO Mehrotra 窗口內合計賣出約 $182.3M, 佔總賣出約 67%。
- 其他高額賣出: President DeBoer (10/16, 約 $900/股)、Arnzen (7/1, 約 $1,077–1,096/股)。
- 價位區間: 窗口內賣出價格約 $510 至 $1,190/股, 10 月的 DeBoer 賣出價約 $900, 較現價略高。
- 窗口外的參考: 2026-01-14 董事 Teyin Mark Liu 在 $336–337 買進 23,200 股, 約 $7.8M (不計入 6 個月淨額, 但為一次性的正面內部人訊號)。
- 窗口內無 CFO (Mark Murphy) 的交易記錄。

**解讀注意:** 大額、定期的 CEO 賣出可能屬於預先排定的交易計畫 (如 10b5-1), 但工具輸出不含計畫旗標, 無法確認 = DATA_UNAVAILABLE。

## Ownership shifts

- **機構持股:** 80.1% (機構數 5,052 家); 內部人持股 0.24%。
- **前十大持股 (截至 2026-06-30, 季報):**

| 機構 | 持股比例 | 股數 (M) | 季變化 |
|---|---|---|---|
| BlackRock | 9.27% | 104.8 | +1.6% |
| Vanguard Capital Mgmt | 6.51% | 73.7 | +0.7% |
| State Street | 4.43% | 50.1 | -4.1% |
| Invesco | 3.21% | 36.3 | +1.8% |
| Capital World Investors | 2.60% | 29.5 | -29.9% |
| Geode | 2.45% | 27.7 | +1.0% |
| FMR (Fidelity) | 2.36% | 26.7 | -16.7% |
| JPMorgan | 2.28% | 25.8 | +63.8% |
| Vanguard Portfolio Mgmt | 2.18% | 24.7 | +7.1% |
| Primecap | 1.70% | 19.2 | -12.1% |

- 前十大合計約 37%。集中度高度穩定, 以指數型基金為主。
- 主動型機構的流向分歧: Capital World (-30%)、FMR (-17%)、Primecap (-12%) 減碼; JPMorgan (+64%) 與 Invesco (+2%) 加碼。整體為 **輕微分歧, 無明確一方主導**。
- 空頭部位: 2,602 萬股, 佔流通股約 2.3%, 較前一個月的 2,971 萬股下降約 12%, 回補天數約 1.0 天。空頭壓力低。

## Net sentiment score

**綜合: 偏多 (bullish-leaning), 信心中等。**

| 面向 | 判讀 | 信心 |
|---|---|---|
| 分析師評等 | 強烈偏多 (45/49 買方) | 高 |
| 分析師目標價 | 偏多但分歧極大 (361–3,000) | 中 |
| 內部人交易 | 偏空 (6 個月 $273M 賣出, 零買進, 但含一次正向的 2026-01 買進) | 中高 |
| 機構流向 | 中性, 前十大分歧 | 中 |
| 空頭部位 | 中性偏多 (低空單, 回補天數短) | 中 |
| 散戶情緒 (10 月) | DATA_UNAVAILABLE, 舊資料偏多 | 低 |

- 偏多的主要依據: 分析師評等、估值 (forward P/E 約 4x)、股價在 52 週高點以下約 30%、空頭部位低。
- 偏空的主要依據: 內部人持續大額賣出、股價跌破 50 日均價、中國競爭與 AI 資本支出的敘事風險。

**Divergence flag: 是 (分析師與內部人方向相反)。**
- 分析師 (92% 買方評等) 與內部人 (窗口內零買進、$273M 賣出) 的方向相反, 此分歧值得留意。
- 散戶與分析師的分歧 **無法判定**, 因為 10 月的散戶資料 = DATA_UNAVAILABLE。若只看 2026 年中的舊資料, 散戶偏多, 與分析師方向一致, 但這些資料與本報告的 10 月時點不同步。

## 資料缺口 (DATA_UNAVAILABLE)

- 個別券商的升降評等時序 (`recommendations` 僅回傳彙總)
- 2026-10 的 Reddit 散戶貼文與提及次數
- StockTwits 情緒 (任務限制, 未取得)
- 內部人交易是否屬 10b5-1 預排計畫
- 機構名單的 2026-09-30 季報 (目前最新為 2026-06-30)

SENTIMENT REPORT COMPLETE
