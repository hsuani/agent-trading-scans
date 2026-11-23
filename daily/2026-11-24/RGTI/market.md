# RGTI 技術分析 (Market Analyst)

- 分析日期: 2026-11-24
- 資料日期: 2026-11-23 (`ta.py` snapshot `as_of`)
- 資料來源: 快取 (`source: cache`), 網路受限為預期情況
- 價格狀態: 可取得
  - `ta.py` snapshot 價格 8.375 USD
  - `yf.py` fast_info `last_price` 8.355 USD (cnyes feed, cached_at 2026-11-23T17:54:53+00:00), 兩者差距約 0.24%
  - 本報告以 `ta.py` 價格 8.375 為準

## 1. 價格與趨勢結構

- 現價 8.375, 前收 7.16, 當日區間 8.07 - 8.62
- 價格位於 MA20 (10.42)、MA50 (12.71)、MA200 (16.29) 之下, 偏離幅度分別為 -19.6%、-34.1%、-48.6%
- 均線排列為 price < MA20 < MA50 < MA200, 屬空頭排列
- 52 週區間 7.08 - 30.21; 距 52 週高點 -72.3%, 距 52 週低點 +18.3%

## 2. MACD

- MACD -1.314, Signal -1.095, Histogram -0.220
- MACD 位於 Signal 之下且柱狀為負, 動能偏空
- 僅有單點數值, 無歷史序列, 無法判斷柱狀是擴大或收斂

## 3. RSI14

- RSI14 = 36.9
- 偏弱區間, 尚未進入超賣 (< 30)

## 4. 布林通道 (Bollinger Bands, 20, 2)

- Upper 13.84 / Mid 10.42 / Lower 6.99
- %B = 0.20, 價格位於下軌上方約兩成位置, 接近下軌
- Bandwidth 約 65.7% (由 (Upper - Lower) / Mid 計算), 波動度高

## 5. 動能 (Momentum)

- 1M -27.3%, 3M -50.6%, 6M -66.6%, 12M -63.3%
- 各期間報酬皆為負, 中期下跌趨勢明確

## 6. 波動度 (Volatility)

- ATR14 = 1.015, 約為現價的 12.1%
- 20 日年化波動率 140.4%, 屬極高波動

## 7. 支撐與壓力

以下價位取自可得的快照數據 (52 週高低、布林通道、均線、當日高低), 並非由歷史 OHLC 計算之 pivot 點:

- 支撐:
  - 7.08 (52 週低點)
  - 6.99 (布林下軌)
- 壓力:
  - 8.62 (當日高點)
  - 10.42 (MA20 / 布林中軌)
  - 12.71 (MA50)
  - 13.84 (布林上軌)

## 8. 成交量 (Volume)

- 資料缺失: `ten_day_average_volume` 為 null, 無成交量序列
- 無法判斷量價關係, 本節標示為 N/A

## 9. 綜合判斷 (技術面)

- 技術面偏空: 價格低於所有主要均線, MACD 位於 Signal 之下, 各期間動能皆為負
- RSI 未超賣, 價格位於布林下半部, 短線可能出現反彈, 但需站回 MA20 (10.42) 才能改變中期結構
- 若價格跌破 52 週低點 7.08, 下方可參考的支撐僅剩布林下軌 6.99, 此處需留意

## 10. 資料限制

- 資料日期為 2026-11-23, 較分析日落後一天
- 全部數據來自快取, 無法確認即時性
- `yf.py` 歷史資料抓取失敗 (出現 "possibly delisted" 訊息, 原因為網路連線被阻擋, 非確認下市); fast_info 數據來自 cnyes 快取
- `ta.py` snapshot 未標示資料來源, 無法確認其是否為快取
- 股本數 (shares)、市值 (market_cap)、開盤價 (open)、成交量 (volume) 皆為 null

## 指標總表 (Metrics)

| Metric | Value | Signal / Note |
|---|---|---|
| price | 8.375 | yf last_price 8.355 (cache) |
| previous_close | 7.16 | fast_info |
| day_high / day_low | 8.62 / 8.07 | fast_info |
| MA20 | 10.4175 | price -19.6% vs MA20, bearish |
| MA50 | 12.7107 | price -34.1% vs MA50, bearish |
| MA200 | 16.2893 | price -48.6% vs MA200, bearish |
| MA alignment | price < MA20 < MA50 < MA200 | bearish |
| MACD | -1.3143 | below signal, bearish |
| MACD signal | -1.0947 | reference |
| MACD histogram | -0.2196 | negative, trend direction unknown (single point) |
| RSI14 | 36.93 | weak, not oversold (< 30) |
| BB upper | 13.8422 | resistance |
| BB mid | 10.4175 | equals MA20, resistance |
| BB lower | 6.9928 | support |
| BB %B | 0.20 | lower part of band |
| BB bandwidth | ~65.7% | derived, high volatility |
| ATR14 | 1.0153 | ~12.1% of price |
| 20d annualized volatility | 140.4% | extremely high |
| mom_1m | -27.3% | negative |
| mom_3m | -50.6% | negative |
| mom_6m | -66.6% | negative |
| mom_12m | -63.3% | negative |
| 52w high | 30.205 | price -72.3% from high |
| 52w low | 7.08 | price +18.3% from low, key support |
| Support levels | 7.08, 6.99 | derived from available levels |
| Resistance levels | 8.62, 10.42, 12.71, 13.84 | derived from available levels |
| Volume | N/A | ten_day_average_volume null |
| Data as-of | 2026-11-23 | one day before analysis date, cache |
