# Sentiment — SYM (Symbotic Inc., NASDAQ: SYM) as of 2026-10-28

資料可得性: 分析師與內部交易來自 yf CLI (有資料)。Reddit 與 StockTwits 無法取得 (DATA_UNAVAILABLE)。WebSearch 僅找到第三方聚合頁, 無 2026-10 當月散戶情緒內容。

## Analyst consensus

來源: `yf SYM rec_summary` (與 `recommendations` 一致, 最新期 0m)

| 評等 | 家數 | 佔比 |
|---|---|---|
| Strong Buy | 1 | 6% |
| Buy | 8 | 47% |
| Hold | 5 | 29% |
| Sell | 2 | 12% |
| Strong Sell | 1 | 6% |
| 合計 | 17 | 100% |

- 買進側 (Strong Buy + Buy) 共 9 家, 佔 53%; 賣出側 (Sell + Strong Sell) 共 3 家, 佔 18%。
- 歷史趨勢 (0m / -1m / -2m / -3m): 買進側 9 / 8 / 9 / 9 家, 賣出側 3 / 3 / 3 / 3 家。最近一期買進側減 1 家, 其餘期間持平。
- 近期升降評等明細 (機構名稱、日期): DATA_UNAVAILABLE。yf 工具只回傳彙總計數, 不含個別評等變動。
- 目標價變動: DATA_UNAVAILABLE (yf 未提供)。WebSearch 第三方來源的平均目標價 (StreetInsider 約 $64.73) 日期不明, 且與 stockalarm、24/7 Wall St. 的家數不一致, 未採用。
- 第三方聚合頁的參考說法 (不作為主要依據): stockalarm 顯示 17 家、Hold 共識、約 53% Buy; 24/7 Wall St. 顯示 19 家 (10 Buy / 6 Hold / 3 Sell); Trefis 提到 2026-05 Weiss Ratings 調降至 Sell。以上來源日期不一, 僅供參考。

## Retail social

- **Reddit (r/wallstreetbets, r/stocks)**: DATA_UNAVAILABLE。WebFetch 回報 www.reddit.com 無法存取, 未取得貼文樣本、分數或情緒傾向。
- **StockTwits**: DATA_UNAVAILABLE。api.stocktwits.com 無法解析 (DNS 失敗), 需在 session 網路設定中允許該網域後才能重試。
- **X / 新聞散戶討論**: WebSearch 僅回傳第三方聚合與評等頁面, 未找到 2026-10 的散戶情緒文章或貼文。
- **聲量 (buzz volume)**: DATA_UNAVAILABLE (無貼文計數可比較)。
- **散戶傾向 (tilt)**: DATA_UNAVAILABLE。無法判定偏多、偏空或分歧。
- **主要話題 (僅來自 WebSearch 第三方文章, 非散戶原文)**:
  - 2026 年 Q2 EPS 不如預期後股價走弱 (Trefis 所述, 約自 2026-03 起跌約 20%)。
  - 客戶集中度與大股東關係 (Barchart 2026-08 財報前預覽標題所示)。
  - Q3 2026 財報結果與 2026-10 評等變動: WebSearch 未找到。

## Insider activity

來源: `yf SYM insider`, 期間 2026-04-28 至 2026-10-28 (6 個月)。金額以 USD 計, 換算為 M。

**6 個月淨額 (以可見的公開市場交易計)**
- 買進 (Buy): **$0** (期間內無任何 Buy 紀錄)。
- 賣出 (Sell): 約 **$289.7M**, 其中:
  - 10% 以上大股東 SoftBank Group 於 2026-05-27 賣出 5,590,000 股, 價格 $50.42, 金額 **$281.8M**。
  - 董事與高階主管合計約 **$7.84M** (24 筆)。
- 淨額: 約 **-$289.7M** (賣超)。若排除 SoftBank, 董事與高階主管淨額約 **-$7.84M**。
- 另有約 10 筆 Value 為空白的紀錄, 性質無法由資料判定, 未計入上述金額。

**主要交易人 (期間內, 金額依 USD)**
| 日期 | 人員 | 職稱 | 股數 | 金額 (M) | 價格區間 |
|---|---|---|---|---|---|
| 2026-05-27 | SoftBank Group Corp | 10% 以上大股東 | 5,590,000 | 281.8 | $50.42 |
| 2026-05-22 | Todd J. Krasnow | 董事 | 26,633 | 1.42 | $52.12–53.73 |
| 2026-05-11 | Todd J. Krasnow | 董事 | 25,422 | 1.33 | $52.41–53.35 |
| 2026-07-27 | Izilda P. Martins | CFO | 27,463 | 1.12 | $40.80 |
| 2026-07-24 | James J. Kuffner Jr. | CTO | 18,987 | 0.77 | $40.38 |
| 2026-10-27 | William Madison Boyd III | 高階主管 | 9,194 | 0.36 | $38.34–39.14 |

- 股價區間線索: 2026-04 至 05 月的賣出價格約 $52–60; 2026-07 至 08 月約 $40–46; 2026-10 最近一筆約 $38–39。賣出價隨期間下滑。
- 交易型態: 多數為小批量、定期性的董事與高階主管賣出, 與 10b5-1 計畫一致的可能性存在, 但 yf 未提供計畫旗標, 無法確認。

## Ownership shifts

來源: `yf SYM major_holders` (最新一期快照)
- 內部人持股: 13.6%
- 機構持股: 79.4% (流通股中占 91.9%)
- 機構家數: 557
- 趨勢: DATA_UNAVAILABLE (工具僅提供單一快照)。
- 值得注意: SoftBank 於期間內賣出 5.59M 股, 為期間內最大的持股變動事件, 但快照未顯示其剩餘持股比例。

## Net sentiment score

- **分析師面: 中性偏多 (信心中)**。買進側 53%, 但 Hold 佔 29%, 賣出側 18%。最近一期買進側減少 1 家, 方向略弱。
- **內部人面: 偏空 (信心中高)**。6 個月內無公開市場買進, 賣出金額集中於大股東與高階主管, 且賣出價由 $50 以上滑落至 $38–39。
- **散戶面: 無法判定 (信心低, DATA_UNAVAILABLE)**。
- **綜合: 中性偏弱 (信心低)**。分析師 (中性偏多) 與內部人 (偏空) 方向不一致, 且缺少散戶資料。

**分歧旗標 (Divergence flag): DATA_UNAVAILABLE**。散戶傾向無法取得, 無法判定散戶與分析師是否反向。

## 資料缺口與來源狀態

| 來源 | 狀態 |
|---|---|
| yf recommendations / rec_summary | 有資料, 無個別評等日期 |
| yf insider | 有資料, 6 個月窗口已計算 |
| yf major_holders | 有資料, 單一快照, 無趨勢 |
| Reddit | DATA_UNAVAILABLE |
| StockTwits | DATA_UNAVAILABLE |
| WebSearch 散戶與評等 | 部分, 僅第三方聚合頁 |

SENTIMENT REPORT COMPLETE
