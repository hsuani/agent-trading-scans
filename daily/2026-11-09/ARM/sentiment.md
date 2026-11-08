# Sentiment — ARM as of 2026-11-09

資料說明: 價格與分析師 / 內部人 / 持股資料來源為 `pipeline/tools/yf.py`，Yahoo 即時連線失敗，改用 `prices/yf/ARM.json` 快取 (快取刷新時間 2026-11-08 13:14 UTC)。散戶情緒以 WebSearch 取得，Reddit 與 StockTwits 無法直接讀取，且搜尋結果多為 2025 年或 2026 年 8 月前的資料，**2026 年 11 月的散戶原始貼文資料不足**。

快取價格 (USD): 最新 174.62、前收 166.72、52 週區間 100.02–452.70，市值約 186.8B USD (174.62 × 1.07B 股，手算吻合)。

## Analyst consensus

rec_summary (0m) 共 43 筆評等: **28 buy** (strongBuy 8 + buy 20) / **14 hold** / **1 sell** (strongSell 0)。快取 info 的 numberOfAnalystOpinions 為 40，兩者差異來自統計口徑，以 rec_summary 為準。

| 期間 | strongBuy | buy | hold | sell | strongSell |
|---|---|---|---|---|---|
| 0m (目前) | 8 | 20 | 14 | 1 | 0 |
| -1m | 8 | 20 | 14 | 1 | 0 |
| -2m | 8 | 21 | 12 | 1 | 1 |
| -3m | 7 | 20 | 13 | 1 | 1 |

過去三個月評等結構幾乎沒有變化，買方比例約 65%，賣方僅 1 家。hold 由 13 增至 14，strongSell 由 1 降為 0。

目標價 (快取 info): 平均 273.4 USD、最高 500 USD、最低 125 USD。TIKR 文章 (引用 11/2) 提到共識目標 291 USD，兩者時點不同。

近期動作 (WebSearch 交叉比對，日期可信度不一):
- **Barclays** (11/5): 目標價由 360 下調至 325 USD，維持 Overweight，為財報後調整。
- **Rosenblatt** (7/31): 維持 Buy，目標價由 270 降至 250 USD。
- **UBS** (7/30): 維持 Buy，目標價由 360 降至 320 USD。
- **Guggenheim** (7/30): 重申 Buy。
- **HSBC** (7/14): 由 Buy 下調至 Hold。
- **BofA** (日期不明): 維持 Neutral，目標價上調至 460 USD，無法確認是否為近期事件。

財報: 2026-11-04 (快取 earnings_dates) EPS 實際 0.52 USD，預期 0.48 USD，超出 9.33%。手算檢查: 0.52 × 1.07B 股 ≈ 5.6 億 USD 級別的季度淨利，量級合理。

## Retail social

- **Reddit (r/wallstreetbets, r/stocks)**: WebSearch 未找到 2026 年 11 月的 ARM 討論串。可見的相關來源: ChartExchange 的 Reddit 追蹤頁為 2025 年 10 月資料，AltIndex 頁面顯示 Reddit 情緒分 51/100 (中性)，但沒有日期無法對應本期。Quiver Quantitative 提到 ARM 在一次股價下跌期間是社群熱門話題，但沒有標註時間。**傾向: 無法判定。聲量: 無可靠的量化比較基準。**
- **StockTwits**: 可見的最近一筆散戶情緒為 2026 年 8 月 (單日大漲 17%，情緒進入 extremely bullish 區間，市場提醒本益比偏高)。另一篇 Q2 財報 beat 文章提到情緒 92/100 極度看多，但沒有標註年份，無法確認為哪一年。2025 年 11 月曾短暫轉為 bearish。**本期無可用讀數。**
- **X / 新聞**: 本期主要討論集中於 10/30 因 Intel 財測警告下跌近 10%、11/4 財報後股價回落、以及與 Qualcomm 的授權糾紛 (Delaware 法院尚未裁決，Qualcomm 約佔 ARM FY2026 營收 9%)。Barclays 認為下跌已過度，屬於偏多聲音。
- **主題 (依新聞與討論歸納)**: (1) AI CPU / 資料中心成長敘事仍是多方論點; (2) 估值偏高與 Intel、Qualcomm 等外部風險是空方論點; (3) 財報 beat 但股價仍跌，市場多以「利多不漲」解讀; (4) 股價距 52 週高點約 61% 折價，散戶容易把它視為逢低買點或趨勢破壞，兩種說法都有。

## Insider activity

6 個月內 (2026-05-09 至 2026-11-09) 共 15 筆有金額的賣出交易，合計 **58.54M USD 賣出**，**買進 0 筆 (0 USD)**。另有多筆無金額的 RSU 相關股份扣繳與 0 USD 的股票獎勵，不計入淨額。

| 內部人 | 職稱 | 6 個月賣出 (USD M) | 主要交易 |
|---|---|---|---|
| Collins Spencer | Officer | 19.80 | 5/11 約 11.0M、5/19 約 8.8M |
| Child Jason E | CFO | 13.01 | 5/20 約 7.2M、9/21 約 3.1M、8/27 約 2.7M |
| Abbey William | Officer | 12.02 | 5/15 至 6/1 分多筆 |
| Grisenthwaite Richard Roy | Officer | 5.09 | 5/18 約 5.1M |
| Bartels Laura Kathleen | Officer | 4.44 | 6/2 約 4.4M |
| Eaton Charlotte Claire | Officer | 4.18 | 5/21 兩筆 |
| Haas René A | CEO | 0 | 6 個月內無公開市場賣出，最近一次賣出在 3–4 月 (約 1.5M–5.1M)，8/31 為 64 股獎勵 |

重點: 5 月中旬 (5/11 至 5/21) 的賣出密集，並包含 5/15 RSU 歸屬後的大量賣出。CFO 於 9 月仍有賣出。CEO 6 個月內無賣出，但也無買進。沒有任何內部人在近 6 個月內公開市場買進。快取資料未標示交易是否為 10b5-1 計畫，無法判斷賣出動機。

## Ownership shifts

- 內部人持股 0.07%，機構持股 96.3%，機構家數 1,298 家 (快取 major_holders)。
- 最新 13F (2026-06-30) 前幾大持有人: Invesco、Arrowstreet、Capital World 增持；DZ Bank 減持約 30%。
- 機構集中度高，但快取無法提供完整的多期趨勢，只能判斷近期前幾大持有人方向混合。

## Net sentiment score

- **分析師**: 偏多 (28 buy / 43，1 sell，目標價平均值仍高於現價約 57%)。信心: **中-高**。
- **內部人**: 偏空 (6 個月賣出 58.54M USD、買進 0)。信心: **中** (賣出可能含計畫性或 RSU 相關交易)。
- **散戶**: 無可用的 2026 年 11 月讀數，傾向無法判定。信心: **低**。
- **綜合**: **中性** (信心: 低-中)。分析師面偏多，內部人面偏空，散戶面缺資料，三方不一致。

Divergence flag: **無法確認 (資料不足)**。分析師與內部人方向相反 (分析師偏多、內部人淨賣)，這是本報告最可靠的分歧訊號，但它不是散戶與分析師之間的分歧。若之後取得 2026 年 11 月的 Reddit 或 StockTwits 讀數，應重新判斷是否為散戶與分析師方向相反。

來源: pipeline/tools/yf (快取 prices/yf/ARM.json)；WebSearch 結果 (Benzinga、TIKR、Fintel、AAII、ScanX、Quantisnow、StockTwits、AltIndex、ChartExchange、Quiver Quantitative)。

SENTIMENT REPORT COMPLETE
