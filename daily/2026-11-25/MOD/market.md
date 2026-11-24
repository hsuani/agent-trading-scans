# Technical — MOD as of 2026-11-25

> 資料時點注意: 最新可用 bar 為 2026-11-24 (ta snapshot 與 yf fast_info 皆為 cache 來源, 屬正常情況)。分析日期 2026-11-25 尚無收盤資料, 以下數值皆為 2026-11-24 的快照。

## Snapshot
Price $134.25 (ta 日線收盤, 2026-11-24, source: cache), MA20 $121.71, MA50 $151.93, MA200 $211.84, RSI14=50.78, MACD hist=+4.65

報價交叉檢查: yf fast_info last_price $134.865 (feed: cnyes, source: cache, cached_at 2026-11-24T17:28 UTC), previous_close $137.39。與 ta 收盤價差約 $0.62 (0.5%), 原因應為 fast_info 為盤中/快取報價而非正式收盤。本報告以 ta 日線收盤 $134.25 為計算基準。

## Trend
價格位於 MA20 之上 (+10.3%), 但仍在 MA50 (-11.6%) 與 MA200 (-36.6%) 之下。均線排列為 MA20 < MA50 < MA200, 屬典型空頭排列; MA50 與 MA200 距離約 28%, 距離黃金交叉或死亡交叉皆遠, 無近期交叉訊號。

從 52 週高點 $323.25 下跌 58.5%, 距 52 週低點 $87.84 上漲 52.8%。近一年趨勢仍偏弱, 但短期結構自 11/10 附近收盤低點 $103.07 後已明顯走高。11/13 出現大量跳空上漲 (收盤由 $106.10 升至 $135.66, 成交量 8.43M, 為近期最大量), 之後價格維持在 $130-138 區間整理, 尚未站上 MA50。短線結構為「跳空後整理」, 中期結構仍在空頭均線之下。

## Momentum
- MACD: line -4.15, signal -8.80, histogram +4.65。MACD 仍在零軸之下, 但 MACD 線已高於 signal 線且 histogram 為正, 屬於零軸下方的多方轉折 (動能改善, 尚未轉為多頭趨勢確認)。
- RSI14: 50.78, 中性區間, 未達超買或超賣。
- 多週期報酬: 1m +3.06%, 3m -28.32%, 6m -52.04%, 12m -6.15%。中長期動能仍為負, 近一個月為正。

## Key levels
- Resistance: $137.39 (前收, 2026-11-23 收盤 — 近期整理高點區), $139.33 (2026-11-24 盤中高點, ta/yf 皆可見), $155 附近 (Bollinger 上軌 $154.70), $203.23 (2026-09-22 local high), $219.98 (2026-08-17 local high), $255.80 (2026-07-23 local high)
- Support:    $121.71 (MA20 / BB 中軸), $106.10 (2026-11-12 收盤, 跳空前基準), $103.07 (2026-11-10 收盤, 近期低點), $88.71 (Bollinger 下軌), $87.84 (2026-11-05 local low / 52 週低點)
- 註: ta levels 列出的 $170.21 (2026-07-30) 與 $172.84 (2026-09-01) 目前位於價格上方, 已轉為上方阻力區。
- Stop-loss suggestion (logical, not advice): 若以結構停損, 跌破 $103.07 (近期低點, 跳空前整理區) 視為結構失效; 若以均線停損, 跌破 $121.71 (MA20) 為短線轉弱訊號。

## Volatility profile
ATR14 $12.17, 約佔價格 9.1%。ATR-implied daily move ~$12.17 (上下約 ±$12)。
20d annualized vol 153.1% (1.531), 屬極高波動水準; 此數值包含 11/13 約 +28% 跳空日, 會明顯拉高樣本標準差, 不宜直接以此外推為常態波動。部位規模建議以 ATR 為單位而非年化波動率, 避免過度放大或縮小部位。

## Setup
中性偏弱 (neutral, bearish-structure). 形態: 長期空頭排列 (MA20 < MA50 < MA200), 近期為跳空後的區間整理 (約 $130-138), 價格未能站上 MA50 ($151.93)。MACD 在零軸下方出現多方轉折, RSI 中性, 尚無明確突破或跌破確認。若價格站上 $139.33 並持續放量, 可視為短線區間突破; 若跌破 $121.71 則整理結構轉弱。

## Volume
- 最新 bar (2026-11-24) 成交量 599,385 股, 僅為 10 日平均量 (2,999,510, 不含最新日) 的約 20%。此為盤中未完成或快取不完整之 bar, 不適合作為量能確認依據, 需待正式收盤資料。
- 10 日平均量受 11/13 跳空日 8.43M 拉高; 排除該日後其餘 9 日平均約 2.40M。
- 11/18 (3.56M)、11/20 (2.91M) 等日量能仍高於排除後均值, 顯示跳空後仍有一定買賣活動; 無明顯量能放大突破 $139.33 的證據。

## Indicators table
| Indicator | Value | Reading |
|---|---|---|
| Price (ta close, 2026-11-24) | $134.25 | 區間 $130-138 |
| Price (yf fast_info last, cache) | $134.865 | 與 ta 收盤差 0.5%, 快取報價 |
| MA20 | $121.71 | 價格 +10.3%, 短線偏多 |
| MA50 | $151.93 | 價格 -11.6%, 中期偏弱 |
| MA200 | $211.84 | 價格 -36.6%, 長期偏弱 |
| MA alignment | MA20 < MA50 < MA200 | 空頭排列 |
| RSI14 | 50.78 | Neutral |
| MACD line | -4.15 | 零軸下方 |
| MACD signal | -8.80 | — |
| MACD hist | +4.65 | 正值, 動能改善 |
| BB upper / mid / lower | $154.70 / $121.71 / $88.71 | 價格位於中上段 |
| BB %B | 0.69 | 中上段, 未超買 |
| ATR14 | $12.17 (9.1% of price) | 高波動 |
| 20d annualized vol | 153.1% | 含 11/13 跳空, 極高 |
| 1m return | +3.06% | 近月轉正 |
| 3m return | -28.32% | 明顯下跌 |
| 6m return | -52.04% | 大幅下跌 |
| 12m return | -6.15% | 小幅下跌 |
| 52w high / low | $323.25 / $87.84 | 距高點 -58.5%, 距低點 +52.8% |
| Latest volume vs 10d avg | 599,385 vs 2.9995M (約 20%) | 未完成 bar, 不具確認力 |
| Nearest resistance | $139.33 (2026-11-24 盤中高) | 突破需量能配合 |
| Nearest support | $121.71 (MA20) / $103.07 (近期低點) | 結構支撐 |

## Metrics summary (price + source)
| 項目 | 數值 | 來源 |
|---|---|---|
| Price (基準收盤) | $134.25 | ta snapshot, 2026-11-24, source: cache |
| Price (fast_info last) | $134.865 | yf fast_info, feed: cnyes, source: cache, cached 2026-11-24T17:28 UTC |
| Previous close (fast_info) | $137.39 | yf fast_info, source: cache |
| RSI14 | 50.78 | ta snapshot |
| MACD / signal / hist | -4.15 / -8.80 / +4.65 | ta snapshot |
| ATR14 | $12.17 | ta snapshot |
| BB %B | 0.69 | ta snapshot |
| 20d annualized vol | 153.1% | ta snapshot |
| 52w high / low | $323.25 / $87.84 | ta snapshot |

MARKET REPORT COMPLETE
