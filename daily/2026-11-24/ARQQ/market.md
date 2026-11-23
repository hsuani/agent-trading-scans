# ARQQ 技術面分析 (Market Analyst)

- 分析日期: 2026-11-24 (pipeline date)
- 資料基準日: 2026-11-23 (ta snapshot `as_of`; 來源為 cache, 屬正常情況)
- 價格來源: `ta.py` snapshot price 11.28 / `yf.py` fast_info last_price 11.30 (cache, feed=cnyes, cached 2026-11-23T17:54:53Z)
- 價格可取得, 未觸發 PRICE_DATA_UNAVAILABLE

## 1. 價格與趨勢結構

- 現價約 11.28–11.30 USD, 前收 10.97, 當日區間 11.21–12.88 (yf fast_info)。
- 價格位於 MA20 (14.61)、MA50 (17.71)、MA200 (17.50) 之下, 距離分別為 -22.8%、-36.3%、-35.5%。
- 均線排列為 MA20 < MA200 < MA50, 整體呈空頭排列, 中長期趨勢偏弱。
- 距 52 週高點 31.75 為 -64.5%, 距 52 週低點 10.90 僅 +3.5%, 價格貼近年內低點。

## 2. 動能指標

- MACD: -1.569, Signal: -1.323, Histogram: -0.245。MACD 位於 signal 之下且柱狀體為負, 動能偏空。
- RSI(14): 34.9。接近但尚未進入超賣區 (<30), 反映賣壓仍在但已有減速跡象的可能性, 需後續確認。
- ATR(14): 1.63, 約為現價的 14.4%, 日內與隔日波動幅度大。

## 3. 布林通道 (Bollinger Bands, 20, 2σ)

- Upper: 19.00 / Mid: 14.61 / Lower: 10.22
- %B: 0.12, 價格位於通道下緣附近。
- 布林通道寬度大, 反映高波動環境; 20 日年化波動率約 156%。

## 4. 報酬動能 (Momentum)

- 1M: -31.3%
- 3M: -44.8%
- 6M: -32.0%
- 12M: -53.5%
- 各期間報酬皆為大幅負值, 跌勢橫跨短中長期。

## 5. 支撐與壓力

- 支撐 (Support):
  - 約 10.90: 52 週低點, 為最關鍵支撐, 現價距離僅約 3.5%。
  - 約 10.22: 布林通道下軌, 為統計上的下檔參考。
- 壓力 (Resistance):
  - 約 14.61: MA20 / 布林中軌, 為第一道壓力。
  - 約 17.50–17.71: MA200 與 MA50 匯聚區, 為重要中期壓力帶。
  - 約 19.00: 布林上軌。
  - 約 31.75: 52 週高點 (遠離現價, 僅作為長期參考)。

## 6. 成交量

- 本次 snapshot 與 fast_info 皆未提供有效成交量資料 (`ten_day_average_volume` 為 null, 無 volume 序列)。
- 因此無法判斷量價配合狀況, 此項標記為資料不足 (N/A)。
- 日內最高 12.875 至最低 11.205 的區間 (yf) 與收盤 11.30 相比, 顯示日內波動大, 但無量能佐證。

## 7. 資料品質注意事項

- `ta.py` 與 `yf.py` 的 Yahoo 連線皆因網路封鎖失敗 (CONNECT 403), 資料取自本地 cache。
- `yf.py` 的 `fifty_day_average`、`two_hundred_day_average`、`year_high`、`year_low`、`market_cap`、`shares`、`ten_day_average_volume` 皆為 null 或 NaN, 因此均線與 52 週高低以 `ta.py` 的值為準。
- 資料基準日為 2026-11-23, 較分析日 2026-11-24 落後一日。
- 兩來源價格差異 (11.28 vs 11.30) 屬正常誤差範圍, 不影響判斷。

## 8. 綜合判讀

- 趨勢: 空頭。價格低於所有主要均線, 均線呈空頭排列。
- 動能: 偏空。MACD 負向且柱狀體為負, RSI 接近超賣但尚未確認反轉。
- 位置: 價格貼近 52 週低點與布林下軌, 短線處於超跌區間, 有技術性反彈的可能, 但趨勢未改變。
- 關鍵觀察點: 能否守住 10.90 (52 週低點); 若跌破則下檔缺乏明確支撐。向上需站回 14.61 (MA20) 才能改善短線結構。
- 風險: 年化波動率約 156%, 為極高波動標的, 技術指標的訊號可靠度受限。
- 本報告僅為技術面描述, 不構成投資建議。

## 9. 指標總表

| Metric | Value | Note |
|---|---|---|
| Price (ta snapshot) | 11.28 | as_of 2026-11-23, cache |
| Price (yf fast_info) | 11.30 | cache, feed=cnyes |
| Previous Close | 10.97 | yf fast_info |
| Day Range | 11.205 – 12.875 | yf fast_info |
| MA20 | 14.61 | price -22.8% vs MA |
| MA50 | 17.71 | price -36.3% vs MA |
| MA200 | 17.50 | price -35.5% vs MA |
| MACD | -1.569 | below signal |
| MACD Signal | -1.323 | |
| MACD Histogram | -0.245 | negative, bearish |
| RSI(14) | 34.9 | near oversold (<30 not reached) |
| BB Upper | 19.00 | |
| BB Mid | 14.61 | |
| BB Lower | 10.22 | |
| BB %B | 0.12 | near lower band |
| ATR(14) | 1.63 | ~14.4% of price |
| 20D Vol (annualized) | 156.4% | high volatility |
| Momentum 1M | -31.3% | |
| Momentum 3M | -44.8% | |
| Momentum 6M | -32.0% | |
| Momentum 12M | -53.5% | |
| 52W High | 31.75 | -64.5% from current |
| 52W Low | 10.90 | +3.5% from current |
| Support (key) | 10.90 / 10.22 | 52W low / BB lower |
| Resistance (key) | 14.61 / 17.50–17.71 / 19.00 | MA20 / MA200–MA50 / BB upper |
| Volume | N/A | no volume data available |
