# Technical — VRT as of 2026-11-25

> 資料說明：分析日為 2026-11-25，但目前可用的最新價格 bar 為 2026-11-24（來源 cache：prices/VRT.csv）。`yf fast_info` 的 last_price 為 $172.25（cache，cnyes，cached_at 2026-11-24T17:28 UTC），與 CSV 最新收盤 $172.075 相差 $0.175。以下指標以 `ta snapshot` 的 2026-11-24 bar 為準。2026-11-24 成交量僅 2.95M，約為 10d 平均的 41%，可能為盤中或未完整的資料，視為暫定值。

## Snapshot
Price $172.08（2026-11-24 收盤，cache）, MA20 $202.14, MA50 $220.74, MA200 $271.37, RSI14=39.67, MACD hist=-1.61

## Trend
趨勢為明確的下降趨勢。價格在 MA20（-14.9%）、MA50（-22.0%）、MA200（-36.6%）之下，三條均線呈空頭排列（MA20 < MA50 < MA200）。MA50 已低於 MA200，約低 18.7%，屬 death cross 狀態，而非接近交叉的階段。MA200 持續下彎（第 11-17 至 11-24 的 MA200 由 271.59 降至 271.37），仍是主要壓力帶。

近期結構為高點與低點持續下移。11-17 至 11-24 的收盤序列為 190.37、194.48、184.99、166.24、186.35、172.08，11-20 單日下跌 -10.1%，11-24 再跌 -7.7%。價格已跌破 2026-11-05 的支撐 $170.80，11-20 盤中低點 $163.57 與 11-24 盤中低點 $168.27 皆位於其下方。趨勢強度偏強（空方），但 52w 相對位置仍在區間中段偏上（距 52w 低點 +16.4%）。

## Momentum
- MACD：MACD -12.32、signal -10.71、histogram -1.61。MACD 線與 signal 線皆為負值，且 MACD 位於 signal 之下，屬空方動能。histogram 自 11-18 的 -0.28 擴大至 -1.61（11-20 為 -1.94），目前仍在擴大，尚未出現收斂跡象。
- RSI14：39.67，位於中性偏弱區，未進入超賣（<30）。近 6 個交易日 RSI 介於 35.14（11-20，本段最低）至 43.65（11-23）之間，未出現 RSI 底部背離的跡象（價格與 RSI 同步創低）。
- 多週期報酬：1m -13.9%、3m -34.8%、6m -46.2%、12m +7.7%。短中期（1m 至 6m）皆為大幅下跌，僅 12m 因基期較低而為正。

## Key levels
- Resistance: $202.14（MA20，動態壓力）, $220.74（MA50）, $254.73（2026-10-29 local high）, $258.10（2026-10-05 local high）, $271.37（MA200）, $295.34（2026-09-08 local high）, $300.30（2026-08-17 local high）, $358.54（2026-06-22 local high）
- Support:    $170.80（2026-11-05 local low，已於 11-20 與 11-24 跌破，轉為待測壓力/確認失守）, $163.57（2026-11-20 盤中低點，目前最近的下方參考低點）, $155.30（Bollinger lower band）, $147.82（52w low）, $220.92（2026-07-29 local low，位於價格上方，屬歷史支撐轉壓力）, $226.94（2026-09-14 local low，同上）
- 52w 距離：距 52w 高點 $379.94 為 -54.7%；距 52w 低點 $147.82 為 +16.4%。
- Stop-loss suggestion (logical, not advice): below $163.57（2026-11-20 盤中低點，因 $170.80 支撐已被跌破）

## Volatility profile
ATR-implied daily move ~$17.95（約為價格的 10.4%），annualized vol 約 128.7%（20d，snapshot 值）。
波動度極高，ATR 與年化波動皆處於高檔。部位大小若以 ATR 計算，單日合理波動約 ±$18，停損距離須遠大於此值，否則容易被日內雜訊觸發。相同風險金額下，部位規模應明顯小於低波動標的。Bollinger 帶寬（上軌 $248.98 至下軌 $155.30，約 $93.7）亦反映高波動。

## Volume confirmation
- 最新 bar（11-24）成交量 2.95M（暫定，見資料說明）。
- 10d 平均成交量（不含最新 bar）為 7.16M，最新量約為其 41%；含最新 bar 的 10d 平均為 6.78M。
- 20d 平均成交量（含最新 bar）為 8.60M。
- 下跌段量能較大：11-19 為 7.31M（-7.4%），11-20 為 12.02M（-10.1%，本段最大量），11-23 為 9.70M（+0.8% 反彈，量能仍大）。11-20 的大量下跌確認賣壓集中釋放，之後量能回落。
- 解讀：下跌伴隨放量，屬有量的空方走勢；11-24 量縮是否代表賣壓減弱，需待完整成交資料確認。

## Setup
偏空（bearish）。型態為高點與低點持續下移（lower highs / lower lows）的下降趨勢，並已跌破前一個擺動低點 $170.80。價格位於 Bollinger 中下半部（%B = 0.18），RSI 未超賣，MACD histogram 仍在擴大。

可觀察的條件：
- 若價格收復 $170.80 並站穩，可視為短線失守狀態的修復，但 MA20 $202.14 仍為主要壓力。
- 若價格無法站回 $170.80 且跌破 $163.57，下方缺乏由工具計算出的明確支撐，須以 Bollinger lower band $155.30 與 52w low $147.82 作為參考。
- 本報告僅描述技術條件，不構成買賣建議。

## Indicators table
| Indicator | Value | Reading |
|---|---|---|
| Price（2026-11-24 收盤，cache） | $172.08 | 下跌，低於 MA20/50/200 |
| MA20 | $202.14 | 價格低 14.9%，短期壓力 |
| MA50 | $220.74 | 價格低 22.0%，中期壓力 |
| MA200 | $271.37 | 價格低 36.6%，長期壓力；MA50 < MA200 為 death cross 狀態 |
| RSI14 | 39.67 | 中性偏弱，未超賣（6 日區間 35.14–43.65） |
| MACD | -12.32 | 負值，空方 |
| MACD signal | -10.71 | MACD 位於 signal 下方 |
| MACD hist | -1.61 | 空方，負值擴大中（11-20 為 -1.94） |
| BB %B | 0.18 | 位於中下半部，接近下軌但未跌破 |
| BB upper / mid / lower | $248.98 / $202.14 / $155.30 | 帶寬寬，波動高 |
| ATR14 | $17.95 | 約為價格 10.4%，高波動 |
| 20d annualized vol | 128.7% | 極高 |
| 1m return | -13.9% | 短期大跌 |
| 3m return | -34.8% | 中期大跌 |
| 6m return | -46.2% | 半年大跌 |
| 12m return | +7.7% | 基期較低，僅此週期為正 |
| % from 52w high | -54.7% | 距高點遠 |
| % from 52w low | +16.4% | 距低點有限 |
| Volume（最新，暫定） | 2.95M | 約為 10d 均量 41%，待確認 |
| Volume 10d avg（不含最新） | 7.16M | 下跌段放量基準 |
| Volume 20d avg（含最新） | 8.60M | 量能偏高 |

## Metrics summary
| 項目 | 數值 | 來源 |
|---|---|---|
| Current price（2026-11-24 收盤，ta snapshot） | $172.075 | cache（prices/VRT.csv） |
| Current price（yf fast_info last_price） | $172.25 | cache（cnyes，cached_at 2026-11-24T17:28 UTC） |
| Previous close（fast_info） | $186.35 | cache，與 CSV 2026-11-23 收盤一致 |
| Day high / low（2026-11-24） | $180.53 / $168.27 | cache |
| MA20 / MA50 / MA200 | $202.14 / $220.74 / $271.37 | cache（ta snapshot） |
| RSI14 | 39.67 | cache（ta snapshot） |
| MACD / signal / hist | -12.32 / -10.71 / -1.61 | cache（ta snapshot） |
| Bollinger upper / mid / lower（%B） | $248.98 / $202.14 / $155.30（0.18） | cache（ta snapshot） |
| ATR14 | $17.95 | cache（ta snapshot） |
| 20d annualized vol | 128.7% | cache（ta snapshot） |
| 52w high / low | $379.94 / $147.82 | cache（ta snapshot；fast_info 52w 欄位為 NaN，未採用） |
| 1m / 3m / 6m / 12m 報酬 | -13.9% / -34.8% / -46.2% / +7.7% | cache（ta snapshot） |
| 最新成交量（暫定） | 2.95M | cache（prices/VRT.csv） |
| 資料最新日期 | 2026-11-24（分析日 2026-11-25） | cache |

註：本報告所有數值來源為 pipeline/tools 的 cache 資料（quote_source / history_source = cache），屬預期行為。cache 中 52w 欄位與 fast_info 數值不一致，本報告採用 ta snapshot 的 52w 值。

MARKET REPORT COMPLETE
