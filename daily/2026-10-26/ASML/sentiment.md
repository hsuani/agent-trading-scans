# Sentiment — ASML as of 2026-10-26

資料基準：ADR（NMS，USD 計價）。價格時間戳約 2026-10-24 收盤（由 regularMarketTime 推算，yfinance 無明確日期欄位），快取時間 2026-10-25 11:14 UTC。2026-10-26 之後的資料視為未知。

## Analyst consensus

rec_summary（當期）：Strong Buy 7 / Buy 31 / Hold 2 / Sell 1 / Strong Sell 0，合計 41 筆評等。買進以上佔 38/41（約 93%）。
info 欄位：numberOfAnalystOpinions = 17，recommendationMean = 1.37（strong_buy）。

注意：41 筆評等與 17 位分析師的差異未能於工具層面對齊，兩者口徑不同，報告以 41 筆分布為主、17 位為目標價樣本數。

近期變化（rec_summary 近四個月）：

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 合計 |
|---|---|---|---|---|---|---|
| 0m（當期） | 7 | 31 | 2 | 1 | 0 | 41 |
| -1m | 7 | 31 | 3 | 1 | 0 | 42 |
| -2m | 6 | 32 | 4 | 1 | 0 | 43 |
| -3m | 7 | 33 | 3 | 1 | 0 | 44 |

- 工具回傳的 recommendations 與 rec_summary 相同，僅為月度彙總，沒有逐筆升降評等紀錄（個別券商 upgrade/downgrade 明細 = DATA_UNAVAILABLE）。
- 近一個月 Hold 由 3 降為 2，總筆數由 42 降至 41，方向偏正面但幅度很小。
- 目標價（info，USD）：平均 2,149 / 中位數 2,302 / 最高 2,847 / 最低 867。
  - 相對現價 1,571.8（約 10/24 收盤）：平均 +36.7%，中位數 +46.4%，最高 +81.1%，最低 -44.8%。
  - 最低目標價 867 與其餘分布落差過大，疑為過時或離群值，解讀時不宜採用。
- 網路搜尋的舊資料（aggregator 站，2026-04）提到平均目標價約 1,550，已明顯落後於目前 2,149，僅供歷史對照，不採信。

## Retail social

- Reddit（r/wallstreetbets、r/stocks）：DATA_UNAVAILABLE。依指示未直接抓取 Reddit；WebSearch 以 "ASML Holding reddit wallstreetbets stocks discussion 2026" 查詢，結果無任何 2026 年 WSB 或 r/stocks 的 ASML 討論串。
- StockTwits：DATA_UNAVAILABLE（依指示不直接抓取）。
- X / 新聞輿情（WebSearch）：未找到 2026-10 的相關文章，最新可取得的資料停在 2026-07。
  - 2026-07（MarketBeat 快訊）：分析師持續強調 EUV 領先地位與 High-NA 對 AI 先進製程的長期受惠；同時有評論質疑高估值，半導體族群於 7 月因獲利了結回檔。
  - 2026-04（options flow 追蹤站）：多空部位接近均衡，關稅疑慮壓抑股價；該站來源可靠度低。
  - 2026-02 至 03：社群多空分歧，多方看 AI 需求與 EUV，空方聚焦中國出口限制與約 50x 本益比。
  - 2026-Q2 財報：TradingKey 類 aggregator 稱 Q2 2026 財報優於預期並上修全年指引，ADR 上半年最大漲幅約 87%。此來源品質待查證。
- 成交量代理（非社群聲量，僅作交易熱度參考）：10 日均量 1.60M，3 個月均量 1.43M，近 10 日量能高於 3 個月平均約 12%。
- 聲量相對基準（mention count vs typical）：DATA_UNAVAILABLE，無法量化。

Retail tilt：DATA_UNAVAILABLE（無法確認 Reddit、StockTwits 近期貼文）。僅能依主流新聞標題的敘述判斷，為「多空分歧、偏中性」，信心低。

Themes（僅依新聞層面，非社群實證）：
- EUV / High-NA 技術領先與 AI 先進製程需求。
- 估值偏高（trailing P/E 約 38.7x，forward P/E 約 25.0x）。
- 中國出口限制與關稅風險。
- DRAM 市占提升帶動 lithography 需求（BofA 2026 年選股、J.P. Morgan 半導體設備族群首選的敘述，來源為 aggregator 報導）。

## Insider activity

Net 6mo：DATA_UNAVAILABLE。insider 工具回傳空陣列，無法區分「確實無交易」與「資料缺漏」，因此不得推論為零交易。

- info 內高階管理層（CEO Christophe Fouquet、CFO Roger Dassen、COO Frederic Schneider-Maunoury 等）的 exercisedValue 與 unexercisedValue 皆為 0，但此欄位不代表 6 個月內的買賣紀錄。
- insidersPercentHeld 約 0.008%，內部人持股比例極低，即使有交易，對市場訊號的權重也有限。

## Institutional and ownership flow

資料基準：13F 持股截至 2026-06-30（Q2 報告，較新的 Q3 13F 尚未納入）。

Institutions 持股比例約 20.4%（institutionsCount 2,973）。

前十大機構（USD B 為持股市值，shares 為股數）：

| 機構 | 持股比例 | 股數（M） | 市值（USD B） | 較前期變化 |
|---|---|---|---|---|
| FMR, LLC | 1.41% | 5.48 | 8.61 | +74.0% |
| Fisher Asset Management | 1.22% | 4.74 | 7.45 | +3.0% |
| Capital World Investors | 0.96% | 3.73 | 5.86 | -0.2% |
| Invesco Ltd. | 0.81% | 3.14 | 4.94 | +5.7% |
| State Farm Mutual | 0.71% | 2.76 | 4.34 | 0.0% |
| Capital International Investors | 0.63% | 2.44 | 3.83 | +38.0% |
| Van Eck Associates | 0.63% | 2.46 | 3.87 | +31.7% |
| JPMorgan Chase | 0.62% | 2.40 | 3.77 | +12.4% |
| T. Rowe Price | 0.50% | 1.93 | 3.04 | +25.7% |
| Morgan Stanley | 0.46% | 1.79 | 2.81 | +0.2% |

- 前十大中有 7 家在 Q2 增持（FMR、Capital International、Van Eck、T. Rowe、JPMorgan、Invesco、Fisher），1 家持平（State Farm），僅 Capital World 小幅減持。整體傾向為機構淨增持。
- 持股集中度不高，前十大合計約 8.9%，無單一大股東主導。
- 空頭部位：sharesShort 約 1.45M，佔流通約 0.38%，shortRatio 約 1.1 天，較前月 1.52M 下降約 5%。空方壓力低。資料日期約 2026-10-01。

## Market context (non-sentiment, for reference)

- 市值約 605.8B USD（現價 1,571.8 × 385.4M 股，手算吻合）。
- 52 週區間 946.11 至 1,999.96，距高點約 -21.4%，52 週漲幅約 +48.3%。
- 50 日均線 1,722.7 高於現價約 8.8%；200 日均線 1,588.0 略高於現價約 1%。短期動能弱於中期。
- 股利：每股 2.108 USD，ex-date 2026-10-27，殖利率約 0.58%（dividendRate 9.08 / 現價）。
- 財報：Q3 財報日推算約 2026-10-14，可能已公布；本報告未能取得財報後股價反應，DATA_UNAVAILABLE。

## Data quality flags

- enterpriseValue（約 33.4T USD）與 enterpriseToEbitda（2,067）明顯錯誤，不採用。
- bookValue（1.16）與 priceToBook（1,350）疑似 ADR 與普通股基準不一致，不採用。
- EPS × 股數手算：trailingEps 40.64 × 385.4M ≈ 15.7B，與 netIncomeToCommon 13.5B 差約 16%，未能對齊，獲利數字僅供參考。
- floatShares（21.3B）與 sharesOutstanding（385M）口徑不一致，未採用 float 相關比率。
- 現價與 bid/ask（1,732 / 1,916）不合理，本報告以 regularMarketPrice 為準。

## Net sentiment score

Composite：**偏多（bullish），信心：中低**。

- 分析師面（權重最高）：強烈偏多。Mean 1.37、買進以上約 93%、目標價中位數高於現價約 46%。
- 機構面：偏多。前十大 7 家增持，空方比例極低。
- 零售面：DATA_UNAVAILABLE，無法納入評分。新聞層面為多空分歧。
- 內部人面：DATA_UNAVAILABLE，無法納入評分。

信心偏低的原因：零售與內部人資料缺失，且分析師目標價離散度大，最低目標價疑似離群。缺少 2026-10 的新聞與社群資料，無法確認當前情緒是否與 2026-07 的分歧狀態一致。

Divergence flag：**無法判定（DATA_UNAVAILABLE）**。零售語調缺失，無法比較與分析師傾向是否相反。若以新聞層面粗判，零售與分析師未見明顯相反，但此判斷信心低，不應作為訊號使用。

本報告僅為情緒彙整，不構成交易建議。

SENTIMENT REPORT COMPLETE
