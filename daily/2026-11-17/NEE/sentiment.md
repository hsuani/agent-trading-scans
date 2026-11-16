# Sentiment — NEE as of 2026-11-17

> 資料來源註記: Reddit (r/wallstreetbets, r/stocks) 與 StockTwits 抓取失敗 (Reddit 無法連線, api.stocktwits.com DNS 解析失敗), 散戶情緒部分未取得實際樣本。yf 工具的 Yahoo cookie/crumb 亦失敗, 但 JSON 資料有回傳。系統日期為 2026-11-16, 任務指定 DATE 為 2026-11-17, 本報告以指定日期標註, 實際資料時點以工具回傳為準。

## Analyst consensus

目前 (yf rec_summary, 0m) 共 22 家: 2 Strong Buy + 12 Buy = 14 買進 (約 64%) / 7 Hold (約 32%) / 1 Sell (約 5%) / 0 Strong Sell。

近 3 個月趨勢 (表格):

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 買進合計 | 總家數 |
|---|---|---|---|---|---|---|---|
| 0m (當前) | 2 | 12 | 7 | 1 | 0 | 14 | 22 |
| -1m | 2 | 12 | 7 | 1 | 0 | 14 | 22 |
| -2m | 3 | 11 | 6 | 1 | 0 | 14 | 21 |
| -3m | 2 | 10 | 7 | 1 | 0 | 12 | 20 |

觀察: 買進家數由 -3m 的 12 增至當前 14, 總覆蓋家數由 20 增至 22, Hold 與 Sell 數量大致持平。yf recommendations 只回傳彙總而非逐筆升降評等, 因此無法從該來源確認單一券商動向。

近期評等與目標價 (來自網路搜尋彙整, 第三方聚合站, 非原始券商報告):
- Wells Fargo: 評等升至 Strong Buy (MarketBeat 報導, 2026-10 前後)。先前 4 月為 Buy, 目標價 $99。
- Wall Street Zen: 評等由 Strong Sell 升至 Sell (MarketBeat, 2026-10-17)。此為量化評等機構, 權重低。
- Evercore ISI: Buy, 目標價 $107 (7 月)。
- Barclays: Hold, 目標價 $90 (6 月)。
- Morgan Stanley: Overweight, 目標價 $97 (報導日期 11/20, 年份未明, 可能為 2025 年, 需存疑)。
- MarketBeat 彙整平均目標價 $99.65 (10 月), 共 1 Strong Buy / 17 Buy / 5 Hold, 與 yf 數字不同, 因各平台覆蓋範圍與計算方式不同。

注意: 目前搜尋結果缺 11 月的券商報告, 上述目標價與評等多為 10 月前資料, 時效性有限。

## Retail social

- Reddit: 無法取得 (r/wallstreetbets 與 r/stocks 搜尋皆連線失敗)。聲量與情緒傾向 **未知**。
- StockTwits: 無法取得 (DNS 解析失敗, 需於 session 網路設定允許 api.stocktwits.com)。
- X / 新聞: 搜尋未找到 2026-11 的散戶情緒文章。可見的多為分析師彙整與估值文章 (Simply Wall St 估值模型認為 P/E 27.2x 低於合理 P/E 28.7x, 判定為合理偏低估; 偏機構/分析師視角, 非散戶聲量)。
- 聲量 vs 常態: **無法量化** (缺 Reddit / StockTwits 樣本)。
- 情緒傾向: **無法判定** (僅有 "moderate buy" 類分析師文章, 不代表散戶立場)。
- 主要題材 (由搜尋結果歸納, 非散戶原文): 清潔能源長期需求、季度營收表現 (Q2 2026 營收 $7.5B, 略低於市場預期)、估值相對歷史與同業。

## Insider activity

6 個月窗口 (2026-05-17 至 2026-11-17) 內:
- 買進: $0 (無 open-market 買進)
- 賣出: $0.59M (1 筆)。唯一一筆為 **Michael Dunne (CFO)** 於 2026-11-02 以 $85.00 賣出 6,888 股, 合計 $585,480 (6,888 × 85 = 585,480, 已核對)。
- 淨額: 約 -$0.59M (賣出)。

排除項目: 授予 (Stock Award/Grant) 與衍生性證券行使 (Conversion of Exercise) 不計入買賣金額。

窗口外重要交易 (供背景參考, 不計入 6mo 淨額):
- **John W. Ketchum (CEO)** 2026-02-09 行使選擇權 99,603 股後以 $89.34 賣出, 合計約 $8.90M (已核對: 99,603 × 89.34 ≈ 8.90M)。
- Charles E. Sieving (Officer) 2026-02-04 以 $90.00 賣出 30,000 股, 約 $2.70M。
- Armando Pimentel Jr. (Director) 2025-11-17 以 $83.91 賣出 145,140 股, 約 $12.18M。
- Ronald R. Reagan (Officer) 2026-01 至 2026-02 多筆賣出, 合計約 $3.2M。

觀察: 近 12 個月內內部人以賣出為主, 6 個月窗口內僅一筆小額 CFO 賣出, 且無買進紀錄。大額賣出多集中於 2025-11 至 2026-02 股價 $83–93 區間。

## Ownership shifts

- 機構持股比例: 86.82% (institutionsPercentHeld), 流通股機構持股 87.21%, 機構家數 3,788。
- 內部人持股比例: 0.44% (insidersPercentHeld)。
- 趨勢: 工具僅回傳單一時點快照, **無法判定** 機構集中度變化方向。

## Net sentiment score

**Composite: neutral 偏多 (confidence: 中低)**

依據:
- 分析師面 (權重最高): 偏多。買進佔 64%, 買進家數近 3 個月上升 (12 至 14), 第三方彙整平均目標價約 $99.65 (10 月)。本次未取得當前股價, 無法換算上檔空間。
- 內部人面: 中性偏空但幅度小。6 個月內僅 $0.59M 賣出, 無買進; 大額賣出為 12 個月前至 3 個月前的歷史行為。
- 散戶面: 無資料, 不納入評分。
- 信心降低原因: 兩個散戶來源皆失敗, 分析師資料為 10 月前後之第三方彙整, 且 yf 與 MarketBeat 的家數不一致。

**Divergence flag: 無法判定** — 因缺少散戶情緒樣本, 無法確認散戶傾向是否與分析師傾向相反。待 Reddit 或 StockTwits 可取得後再行判斷。

建議後續補查: 允許 api.stocktwits.com 網域後重抓; 以代理方式或其他來源重試 Reddit; 確認當前股價後計算目標價隱含上檔空間。

SENTIMENT REPORT COMPLETE
