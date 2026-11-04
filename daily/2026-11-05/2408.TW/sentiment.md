# Sentiment — 2408.TW (南亞科) as of 2026-11-05

> 資料時效注意: 系統當前日期為 2026-11-04，本報告以指定之 as-of 日期 2026-11-05 命名。可取得的最新資料多停在 2026 年 10 月初 (Q3 自結財報)，11 月的股價、評等與社群討論均未取得。

## Analyst consensus

資料來源: `yf rec_summary` (Yahoo Finance 彙整，本期快照)。

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 合計 |
|---|---|---|---|---|---|---|
| 本期 (0m) | 4 | 8 | 1 | 1 | 0 | 14 |
| 前一月 (-1m) | 4 | 7 | 0 | 1 | 0 | 12 |
| 前二月 (-2m) | 4 | 7 | 0 | 1 | 0 | 12 |

目前分布: 14 家中 12 家買進 (Buy 以上)，1 家持有，1 家賣出，買進比例約 86%。

Recent moves:
- 本期合計由 12 家增為 14 家，新增 1 家 Hold 評等與 1 家覆蓋，但無法從工具確認是哪家券商、何時變動。
- Investing.com 彙整: 12 位分析師綜合評等 Buy，平均 12 個月目標價約 559.83 元，JPMorgan 目標價 850 元為高點。
- FactSet 彙整 (2026 年 7 月): 14 位分析師目標價中位數由 457.5 元下修至 428 元 (下修 6.45%)，區間 230 元至 800 元。
- FactSet 較早一版 (時點較舊，僅供參考): 2026 年 EPS 中位數 41.76 元，目標價 317.5 元。
- 9 月一則法人報告: 維持「增加持股」，目標價 608 元，預估 Q3 EPS 約 23.5 元。
- 目標價變動: 近期最明確的是 7 月 FactSet 中位數下修; 10 月後的目標價調整 DATA_UNAVAILABLE。

判讀注意: 各家目標價時點不同 (7 月至 9 月)，平均值與中位數不可直接比較。Q3 財報公布後 (10 月) 評等與目標價是否調整，未能確認。

## Retail social

- Reddit (r/wallstreetbets, r/stocks): **DATA_UNAVAILABLE**。本沙箱封鎖 Reddit 網域，依指示未重試。
- StockTwits: **DATA_UNAVAILABLE**。本沙箱封鎖 StockTwits 網域，依指示未重試。
- PTT / X / 新聞論壇: 未直接抓取原文。以搜尋摘要為準 (CMoney 股市社群): 討論兩極，樂觀者看好 AI 與 DRAM 需求成長，謹慎者關注外資動向與高頻交易對股價的壓力，整體偏向觀望與風險控管。此為二手摘要，未取得原始貼文，不可視為定量結論。
- 討論量 (buzz volume): 無法量化 (DATA_UNAVAILABLE)。定性上，Q3 財報公布前後新聞量明顯高於平常，屬事件驅動。
- 直接引述: 本期未取得可核實的原始貼文，故不附引述。

Retail tilt: **混合偏謹慎 (mixed-to-cautious)**，信心低 (僅一則二手摘要)。

Top themes (依搜尋摘要):
1. AI 與 DRAM 需求與報價延續 (樂觀主軸)。
2. Q3 獲利爆發後股價仍未同步上漲，「利多出盡」與外資賣壓疑慮。
3. 產能吃緊、銷售量季減 (Q3 銷量季減中個位數百分比)，是否延續至 Q4 的不確定性。

## Insider activity

Net 6mo: **DATA_UNAVAILABLE**。
- `yf insider` 回傳空陣列。因同一次執行中 Yahoo cookie/crumb 取得失敗，無法區分「確實無內部人交易」與「資料抓取失敗」，故不以「零交易」解讀。
- 台灣董監事持股申報 (公開資訊觀測站) 本期未查核，為缺口。
- Notable: DATA_UNAVAILABLE。

## Ownership shifts

`yf major_holders` 快照 (本期):

| 指標 | 數值 |
|---|---|
| 內部人持股比例 (insidersPercentHeld) | 51.66% |
| 機構持股比例 (institutionsPercentHeld) | 15.87% |
| 機構流通股持股比例 (institutionsFloatPercentHeld) | 32.83% |
| 機構家數 (institutionsCount) | 238 |

- 內部人持股高 (約一半)，一般理解為控股股東集團持股，流通股比例偏低；此為推論，需與公開持股資料核對。
- 機構持股趨勢 (季度變化): DATA_UNAVAILABLE，本次僅取得單一快照。

## Net sentiment score

- **分析師面 (Analyst)**: 偏多 (bullish)。14 家中 12 家買進，但目標價為 7 月以前的快照，時效性不足。信心: 中。
- **散戶面 (Retail)**: 混合偏謹慎 (mixed-to-cautious)。僅有二手摘要，未取得 Reddit/StockTwits。信心: 低。
- **內部人面 (Insider)**: DATA_UNAVAILABLE，不納入計分。
- **股權結構 (Ownership)**: 內部人持股高，流通股比例低，屬結構性特徵，不直接計為情緒分數。

**Composite: 中性偏多 (neutral-to-bullish)，整體信心低。** 主要因素為分析師一致買進，而散戶面資料薄弱、無法量化，內部人資料缺失。

**Divergence flag: 可能 (tentative)。** 分析師整體偏多，二手散戶摘要偏謹慎，方向相反，但因散戶資料僅一則摘要，信心低，不宜作為強訊號。

## Data gaps and reliability notes

1. Reddit / StockTwits: 沙箱封鎖，DATA_UNAVAILABLE。
2. Yahoo 工具 (`yf`) cookie/crumb 取得失敗，insider 空陣列需視為可疑; recommendations 與 major_holders 仍有回傳，但可能為快取或不完整資料。
3. Q3 2026 自結財報數字內部不一致: 報導稱稅後淨利約 876 億元、EPS 25.4 元。以 EPS 25.4 反推，股數約 34.5 億股，與南亞科約 27.7 億股的常識數字不符 (反推 EPS 約 31.6 元)。兩數字至少一個有誤，需以公司公告 (MOPS) 核對，本報告不採用其中任一作為確定數字。
4. 股價: 本期未取得 2026 年 11 月收盤價。10 月報導指股價失守 500 元，8 月報價約 436 至 482.5 元。
5. 月營收 (供參考，非情緒指標): 2026 年 8 月營收 446.90 億元，年增 560.8%; 2026 年 1 至 8 月累計 2,201.94 億元，年增 638.2%。

## 來源 (本期 WebSearch 與工具)

- yf recommendations / rec_summary / insider / major_holders (Yahoo Finance，本地工具)
- 鉅亨網 FactSet 調查 (2026 年 7 月及較早一版): https://news.cnyes.com/news/id/6465581
- nStock 南亞科營收資料: https://nstock.tw/%E5%8D%97%E4%BA%9E%E7%A7%91%E5%81%9A%E4%BB%80%E9%BA%BC.html
- TechNews 8 月營收報導: https://finance.technews.tw/2026/09/02/ntc-2408-202608-financial-report/
- Investing.com 南亞科分析師共識: https://www.investing.com/equities/nanya-tech-consensus-estimates
- Statementdog Q3 財報報導: https://statementdog.com/news/17872

---
SENTIMENT REPORT COMPLETE
